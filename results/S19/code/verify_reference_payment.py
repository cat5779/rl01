#!/usr/bin/env python3
"""Outward rational certificate for an alternating-background payment obstruction.

Standard library only. All accepted inequalities use integer endpoints, not
floating point. The scalar box covers the whole a interval AND perturbations
of each output diagonal and of its squared off-diagonal. See PROOF.md.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction as F
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from time import perf_counter

BITS=120
S=1<<BITS

def ceildiv(a:int,b:int)->int:
    if b<=0: raise ValueError('positive denominator required')
    return -((-a)//b)

@dataclass(frozen=True,slots=True)
class I:
    lo:int
    hi:int
    def __post_init__(self):
        if self.lo>self.hi: raise ValueError('reversed interval')
    @staticmethod
    def of(x):
        if isinstance(x,I):return x
        x=F(x)
        return I(x.numerator*S//x.denominator,ceildiv(x.numerator*S,x.denominator))
    @staticmethod
    def hull(a,b):
        x,y=I.of(a),I.of(b)
        return I(x.lo,y.hi)
    def __add__(self,other):
        b=I.of(other);return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,other):return self+-I.of(other)
    def __rsub__(self,other):return I.of(other)+-self
    def __mul__(self,other):
        b=I.of(other);v=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
        return I(min(v)//S,ceildiv(max(v),S))
    __rmul__=__mul__
    def recip(self):
        if self.lo<=0<=self.hi:raise ArithmeticError('division interval contains zero')
        if self.hi<0:return -(-self).recip()
        return I(S*S//self.hi,ceildiv(S*S,self.lo))
    def __truediv__(self,other):return self*I.of(other).recip()
    def __rtruediv__(self,other):return I.of(other)*self.recip()
    def square(self):
        if self.lo<=0<=self.hi:
            return I(0,ceildiv(max(self.lo*self.lo,self.hi*self.hi),S))
        v=[self.lo*self.lo,self.hi*self.hi]
        return I(min(v)//S,ceildiv(max(v),S))
    def pack(self):return {'lo_dyadic':str(self.lo),'hi_dyadic':str(self.hi),'bits':BITS}


def arctan_enclosure(x:F,terms:int=32):
    v=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
    nxt=(-1)**terms*x**(2*terms+1)/F(2*terms+1)
    return min(v,v+nxt),max(v,v+nxt)

def pi_enclosure():
    a,b=arctan_enclosure(F(1,5));c,d=arctan_enclosure(F(1,239))
    return I.hull(16*a-4*d,16*b-4*c)

# atanh series for 1<=u<=2, with 0<=z<=1/3.
def log_reduced(u:I,terms:int=40):
    z=(u-1)/(u+1)
    if z.lo<0 or z.hi>I.of(F(1,3)).hi:raise ArithmeticError('invalid log reduction')
    z2=z.square();power=z;total=I.of(0)
    for k in range(terms):
        total=total+2*power/F(2*k+1)
        power=power*z2
    remainder=2*power/(F(2*terms+1)*(1-z2))
    return I(total.lo,total.hi+remainder.hi)

LOG2=log_reduced(I.of(2))

def log_point(x:int):
    if x<=0:raise ArithmeticError('log of nonpositive number')
    # x / S = 2^k u, 1<=u<2. The initial argument is an exact dyadic.
    k=x.bit_length()-1-BITS
    u=I.of(F(x,S*(1<<k))) if k>=0 else I.of(F(x*(1<<(-k)),S))
    return log_reduced(u)+k*LOG2

def log_interval(x:I):
    return I(log_point(x.lo).lo,log_point(x.hi).hi)


def reference_box(a:I,pi:I,radius:F):
    c=I.of(F(19,20));t=a-F(1,40)
    den=(1+c.square())/4-t.square()
    q5=1/(5*pi)
    e=F(1,4)+c.square()*q5.square()-t.square()
    q=den*(F(1,2)+t)/e
    r=1+den*(-F(1,2)+t)/e
    s=(den*c*q5/e).square()
    rad=I.hull(-radius,radius)
    return q+rad,r+rad,s+rad


def excess_box(a:I,q:I,r:I,s:I):
    c=I.of(F(19,20))
    A=(1-q)*(1-r)-s;B=q*(1-r)+s;C=(1-q)*r+s;D=q*r-s
    p=[A,B,C,D]
    if min(x.lo for x in p)<=0:raise ArithmeticError('nonpositive atom box')
    x=(q-a)/c;y=(r-a)/c;z=s/c.square()
    caps=[x*y-z,(1-x)*(1-y)-z]
    if min(v.lo for v in caps)<=0:raise ArithmeticError('input contraction caps not certified')
    ri=[x+c*z/(1-r),x-c*z/r]
    rj=[y+c*z/(1-q),y-c*z/q]
    if min(v.lo for v in ri+rj)<=0 or max(v.hi for v in ri+rj)>=S:
        raise ArithmeticError('reverse-Bayes diagonal outside (0,1)')
    beta=[(1-a)*(1-a-c),a*(a+c)]
    W=I.of(0)
    for vi in (0,1):
        for vj in (0,1):
            W=W+z/p[vi+2*vj]*(beta[vj]/(4*ri[vj]*(1-ri[vj]))
                            +beta[vi]/(4*rj[vi]*(1-rj[vi])))
    g=log_interval(B*C/(A*D))-s*sum((1/v for v in p),I.of(0))
    return g-2*W,g,W,min(x.lo for x in p),min(v.lo for v in caps)


def certify(cells:int=200,radius:F=F(1,10000),margin:F=F(1,12)):
    start=datetime.now(timezone.utc).isoformat();tic=perf_counter()
    pi=pi_enclosure()
    if not I.of(3).hi<pi.lo<pi.hi<I.of(F(22,7)).lo:raise ArithmeticError('pi sanity bound')
    rows=[]
    for k in range(cells):
        al=F(1,50)+F(k,100*cells);ah=F(1,50)+F(k+1,100*cells)
        a=I.hull(al,ah);q,r,s=reference_box(a,pi,radius)
        exc,g,W,pmin,capmin=excess_box(a,q,r,s)
        rows.append({'cell':k,'a_lo':str(al),'a_hi':str(ah),
                     'excess':exc.pack(),'g':g.pack(),'budget':W.pack(),
                     'atom_lower_dyadic':str(pmin),'input_cap_lower_dyadic':str(capmin)})
    low=min(int(row['excess']['lo_dyadic']) for row in rows)
    # A strict rational comparison, not a float-derived decision.
    passed=low*margin.denominator>margin.numerator*S
    receipt={'status':'PASS' if passed else 'UNRESOLVED','arithmetic':'outward dyadic rational',
             'bits':BITS,'a_interval':['1/50','3/100'],'c':'19/20','rho':'1/2','lag':5,
             'radius':str(radius),'claimed_excess_margin':str(margin),'cells':cells,
             'pi':pi.pack(),'minimum_excess_lower_dyadic':str(low),
             'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'utc_start':start,'utc_end':datetime.now(timezone.utc).isoformat(),
             'elapsed_seconds':perf_counter()-tic,'rows':rows}
    if not passed: receipt['diagnostic_minimum_lower_decimal']=str(float(F(low,S)))
    return receipt

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cells',type=int,default=200)
    ap.add_argument('--radius',type=F,default=F(1,10000))
    ap.add_argument('--margin',type=F,default=F(1,12))
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    if args.cells<=0 or args.radius<=0 or args.margin<=0:ap.error('positive arguments required')
    result=certify(args.cells,args.radius,args.margin)
    text=json.dumps(result,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    else:print(text,end='')
    raise SystemExit(0 if result['status']=='PASS' else 1)
