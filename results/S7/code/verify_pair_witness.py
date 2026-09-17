#!/usr/bin/env python3
"""Exact rational-interval certificate for the six-site positive averaged-pair witness.

This certifies only the finite route obstruction used in PR111: for the genuine
six-site half-density sine compression at c=19/20, a=1/40, the averaged pair
term for sites (1,6) is positive while the full entropy Hessian is still
negative.  It is not a counterexample to entropy concavity.
"""
from __future__ import annotations
import argparse, json, time
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path

SCALE=10**40
LOG_TERMS=24

def floor_grid(x:F)->F: return F((x.numerator*SCALE)//x.denominator,SCALE)
def ceil_grid(x:F)->F: return -floor_grid(-x)

@dataclass(frozen=True)
class IV:
    lo:F; hi:F
    def __post_init__(self):
        if self.lo>self.hi: raise ValueError('reversed interval')
    @staticmethod
    def point(x): return IV(F(x),F(x))
    @staticmethod
    def outward(lo,hi): return IV(floor_grid(lo),ceil_grid(hi))
    def __add__(self,o):
        o=o if isinstance(o,IV) else IV.point(o); return IV.outward(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,o): return self+-(o if isinstance(o,IV) else IV.point(o))
    def __rsub__(self,o): return -self+o
    def __mul__(self,o):
        o=o if isinstance(o,IV) else IV.point(o)
        vals=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return IV.outward(min(vals),max(vals))
    __rmul__=__mul__
    def reciprocal(self):
        if self.lo<=0<=self.hi: raise ZeroDivisionError
        return IV.outward(F(1)/self.hi,F(1)/self.lo)
    def __truediv__(self,o):
        o=o if isinstance(o,IV) else IV.point(o); return self*o.reciprocal()
    def square(self):
        lo=F(0) if self.lo<=0<=self.hi else min(self.lo*self.lo,self.hi*self.hi)
        return IV.outward(lo,max(self.lo*self.lo,self.hi*self.hi))

def atan_bounds(q:int,terms:int=20)->IV:
    if q<=1: raise ValueError
    x=F(1,q); total=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
    nxt=(-1)**terms*x**(2*terms+1)/F(2*terms+1)
    return IV(min(total,total+nxt),max(total,total+nxt))

def raw_log_unit(u:F)->IV:
    if not F(1)<=u<=F(2): raise ValueError('range reduction')
    z=(u-1)/(u+1)
    total=2*sum((z**(2*k+1)/F(2*k+1) for k in range(LOG_TERMS)),F(0))
    tail=2*z**(2*LOG_TERMS+1)/((2*LOG_TERMS+1)*(1-z*z))
    return IV.outward(total,total+tail)
LOG2=raw_log_unit(F(2))

def log_point(x:F)->IV:
    if x<=0: raise ValueError('log nonpositive')
    k=0; u=x
    while u<1: u*=2; k-=1
    while u>=2: u/=2; k+=1
    return raw_log_unit(u)+k*LOG2

def log_interval(x:IV)->IV:
    if x.lo<=0: raise ValueError('log interval')
    return IV(log_point(x.lo).lo,log_point(x.hi).hi)

def atom_polynomials(n=6):
    perms=[]
    for perm in permutations(range(n)):
        parity=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))%2
        coeff=F((-1)**parity); fixed=[]; power=0
        for i,j in enumerate(perm):
            if i==j: fixed.append(i); continue
            r=i-j
            if r%2==0: coeff=F(0); break
            sine_sign=1 if ((r-1)//2)%2==0 else -1
            coeff*=F(sine_sign,r); power+=1
        if coeff:
            if power%2: raise ArithmeticError('odd offdiagonal degree')
            perms.append((coeff,fixed,power//2))
    out=[]
    for y in range(2**n):
        p=[F(0) for _ in range(n//2+1)]; overall=(-1)**(n-y.bit_count())
        for coeff,fixed,power in perms:
            v=overall*coeff
            for i in fixed: v*=F(1,2) if y&(1<<i) else F(-1,2)
            p[power]+=v
        out.append(p)
    sums=[sum((p[k] for p in out),F(0)) for k in range(n//2+1)]
    if sums!=[F(1)]+[F(0)]*(n//2): raise ArithmeticError('atoms do not sum identically to one')
    return out

def evaluate(coeff,t):
    v=IV.point(0)
    for x in reversed(coeff): v=v*t+x
    return v

def frac(x): return f'{x.numerator}/{x.denominator}'
def ivjson(x):
    return {'lower':frac(x.lo),'upper':frac(x.hi),'display_lower':format(float(x.lo),'.16g'),'display_upper':format(float(x.hi),'.16g')}

def certify():
    st=time.perf_counter(); n=6; c=F(19,20); a=F(1,40)
    pi=16*atan_bounds(5)-4*atan_bounds(239)
    if not F(3)<pi.lo<pi.hi<F(22,7): raise ArithmeticError('pi interval')
    t=(IV.point(c)/pi).square(); polys=atom_polynomials(n); p=[evaluate(poly,t) for poly in polys]
    if min(x.lo for x in p)<=0: raise ArithmeticError('atom positivity')
    pair=IV.point(0); rows=[]
    for z in range(2**n):
        if z&1 or z&(1<<5): continue
        ids=[z,z+1,z+(1<<5),z+1+(1<<5)]
        A,B,C,D=[p[y] for y in ids]; outside=A+B+C+D
        diff=B*C-A*D
        contr=outside*log_interval((B*C)/(A*D))-diff*(A.reciprocal()+B.reciprocal()+C.reciprocal()+D.reciprocal())
        pair+=contr
        rows.append({'outside_mask':z,'word_indices_00_10_01_11':ids,'outside_mass':ivjson(outside),'contribution':ivjson(contr)})
    if not pair.lo>F(37,100000): raise ArithmeticError('pair lower bound')
    if not pair.hi<F(39,100000): raise ArithmeticError('pair upper bound')
    hpp=IV.point(0)
    for y in range(2**n):
        p1=IV.point(0); p2=IV.point(0)
        for i in range(n):
            si=1 if y&(1<<i) else -1
            p1+=si*(p[y]+p[y^(1<<i)])
            for j in range(i+1,n):
                sj=1 if y&(1<<j) else -1
                marg=p[y]+p[y^(1<<i)]+p[y^(1<<j)]+p[y^(1<<i)^(1<<j)]
                p2+=2*si*sj*marg
        hpp-=p2*log_interval(p[y])+p1.square()/p[y]
    if not hpp.hi<F(-49): raise ArithmeticError('Hessian upper sign')
    if not hpp.lo>F(-50): raise ArithmeticError('Hessian lower sign')
    return {
      'status':'CERTIFIED_FINITE_ROUTE_OBSTRUCTION',
      'claim':"E g_{1,6} is positive; H_6'' remains negative",
      'not_claimed':'No counterexample to finite entropy concavity or entropy-rate concavity',
      'parameters':{'n':n,'rho':'1/2','c':str(c),'a':str(a),'pair_one_based':[1,6]},
      'method':{'arithmetic':'rational outward intervals','grid_denominator':str(SCALE),'atan_terms':20,'log_terms':LOG_TERMS,'all_atoms':2**n,'all_outside_words':len(rows)},
      'pi':ivjson(pi),'t':ivjson(t),'minimum_atom_lower':frac(min(x.lo for x in p)),
      'averaged_pair':ivjson(pair),'full_entropy_hessian':ivjson(hpp),
      'strict_rational_checks':{'Eg_gt_37_over_100000':True,'Eg_lt_39_over_100000':True,'Hpp_gt_minus_50':True,'Hpp_lt_minus_49':True},
      'atom_polynomial_coefficients_in_t':[[str(x) for x in poly] for poly in polys],
      'outside_word_contributions':rows,
      'elapsed_seconds_diagnostic':time.perf_counter()-st,
      'review_status':'Same-author exact certificate; no independent review claimed',
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,required=True); args=ap.parse_args()
    r=certify(); args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(r,indent=2)+'\n')
    print(r['status']); print('averaged pair',r['averaged_pair']); print('full entropy Hessian',r['full_entropy_hessian'])
if __name__=='__main__': main()
