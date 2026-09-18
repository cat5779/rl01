#!/usr/bin/env python3
"""S64: exact-integer, outward-rounded intervals for true sine-DPP entropies.
No third-party packages. All interval endpoints are dyadic rationals.
The only transcendental operations are bounded alternating/positive series.
"""
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import argparse, json, time

PREC = 256
SCALE = 1 << PREC
LOG_TERMS = 54

def ceildiv(a, b):
    if b <= 0: raise ValueError('positive denominator required')
    return -((-a)//b)

class IV:
    __slots__ = ('lo','hi')
    def __init__(self, lo, hi=None):
        self.lo=int(lo); self.hi=int(lo if hi is None else hi)
        if self.lo>self.hi: raise ArithmeticError('empty interval')
    @staticmethod
    def rat(num,den=1):
        if den<0:num,den=-num,-den
        if den<=0:raise ZeroDivisionError
        return IV((num*SCALE)//den,ceildiv(num*SCALE,den))
    def __add__(self,other):
        if not isinstance(other,IV):other=IV.rat(other)
        return IV(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self):return IV(-self.hi,-self.lo)
    def __sub__(self,other):return self+(-other if isinstance(other,IV) else -IV.rat(other))
    def __rsub__(self,other):return IV.rat(other)-self
    def __mul__(self,other):
        if not isinstance(other,IV):
            if other>=0:return IV(self.lo*other,self.hi*other)
            return IV(self.hi*other,self.lo*other)
        a,b,c,d=self.lo,self.hi,other.lo,other.hi
        v=(a*c,a*d,b*c,b*d)
        return IV(min(v)//SCALE,ceildiv(max(v),SCALE))
    __rmul__=__mul__
    def reciprocal(self):
        if self.lo<=0<=self.hi:raise ZeroDivisionError('interval contains zero')
        if self.hi<0:return -((-self).reciprocal())
        return IV((SCALE*SCALE)//self.hi,ceildiv(SCALE*SCALE,self.lo))
    def __truediv__(self,other):
        if isinstance(other,IV):return self*other.reciprocal()
        if other<0:return -(self/(-other))
        if other==0:raise ZeroDivisionError
        return IV(self.lo//other,ceildiv(self.hi,other))
    def square(self):
        if self.lo>=0:return IV(self.lo*self.lo//SCALE,ceildiv(self.hi*self.hi,SCALE))
        if self.hi<=0:return (-self).square()
        return IV(0,ceildiv(max(self.lo*self.lo,self.hi*self.hi),SCALE))
    def decimal(self,digits=30):
        ten=10**digits
        def fmt(k):
            sign='-' if k<0 else '';k=abs(k)
            return sign+str(k//ten)+'.'+str(k%ten).zfill(digits)
        return [fmt((self.lo*ten)//SCALE),fmt(ceildiv(self.hi*ten,SCALE))]
    def raw(self):return [str(self.lo),str(self.hi)]

ZERO=IV(0);ONE=IV(SCALE)

def atan_interval_inverse(q,terms=96):
    s=Fraction(0)
    for k in range(terms):s+=Fraction((-1)**k,(2*k+1)*q**(2*k+1))
    r=Fraction(1,(2*terms+1)*q**(2*terms+1))
    if terms%2:lo,hi=s-r,s
    else:lo,hi=s,s+r
    return IV((lo.numerator*SCALE)//lo.denominator,ceildiv(hi.numerator*SCALE,hi.denominator))

@lru_cache(None)
def pi_interval():
    # Machin's identity follows from the tangent addition formula, with all angles in (0,pi/2).
    return 16*atan_interval_inverse(5)-4*atan_interval_inverse(239)

def twice_atanh_positive(z):
    if not (0<=z.lo<=z.hi<SCALE):raise ValueError('0 <= z < 1 required')
    z2=z.square();power=z;ans=ZERO
    for k in range(LOG_TERMS):
        ans=ans+power/(2*k+1)
        power=power*z2
    # Remaining terms <= z^(2M+1)/((2M+1)(1-z^2)).
    tail=(2*power/((ONE-z2)*(2*LOG_TERMS+1)))
    return 2*ans+IV(0,tail.hi)

@lru_cache(None)
def log2_interval():return twice_atanh_positive(IV.rat(1,3))

def log_point(k):
    if k<=0:raise ValueError('positive point required')
    b=k.bit_length()-1
    exponent=b-PREC
    t=1<<b
    z=IV.rat(k-t,k+t)
    return twice_atanh_positive(z)+exponent*log2_interval()

def log_interval(x):
    if x.lo<=0:raise ValueError('positive interval required')
    # Monotonicity of log permits separate endpoint enclosures.
    lower=log_point(x.lo);upper=log_point(x.hi)
    return IV(lower.lo,upper.hi)

def half_sine_kernel(n,a=Fraction(1,40),c=Fraction(19,20)):
    p=a+c/2
    diag=IV.rat(p.numerator,p.denominator)
    cip=IV.rat(c.numerator,c.denominator)/pi_interval()
    K=[]
    for i in range(n):
        row=[]
        for j in range(n):
            r=abs(i-j)
            if r==0:val=diag
            elif r%2==0:val=ZERO
            else:val=((1 if r%4==1 else -1)*cip)/r
            row.append(val)
        K.append(row)
    return K

def entropy_interval(n,a=Fraction(1,40),c=Fraction(19,20)):
    H=ZERO;mass_sum=ZERO;leaves=0;nodes=0;smallest_q=SCALE;largest_q=0
    def visit(K,mass):
        nonlocal H,mass_sum,leaves,nodes,smallest_q,largest_q
        k=len(K);nodes+=1
        if k==0:
            if mass.lo<=0:raise ArithmeticError('nonpositive atom enclosure')
            H=H-mass*log_interval(mass);mass_sum=mass_sum+mass;leaves+=1
            return
        q=K[0][0];r=ONE-q
        if q.lo<=0 or q.hi>=SCALE:raise ArithmeticError('conditional interval left (0,1)')
        smallest_q=min(smallest_q,q.lo);largest_q=max(largest_q,q.hi)
        if k==1:
            visit([],mass*r);visit([],mass*q);return
        iq=q.reciprocal();ir=r.reciprocal();kk=k-1
        K0=[[ZERO]*kk for _ in range(kk)];K1=[[ZERO]*kk for _ in range(kk)]
        for i in range(kk):
            for j in range(i,kk):
                v=K[i+1][0]*K[0][j+1]
                b=K[i+1][j+1]
                v0=b+v*ir;v1=b-v*iq
                K0[i][j]=K0[j][i]=v0;K1[i][j]=K1[j][i]=v1
        visit(K0,mass*r);visit(K1,mass*q)
    start=time.monotonic()
    visit(half_sine_kernel(n,a,c),ONE)
    assert leaves==(1<<n)
    assert mass_sum.lo<=SCALE<=mass_sum.hi
    return {'n':n,'a':str(a),'c':str(c),'rho':'1/2','precision_bits':PREC,
            'log_terms':LOG_TERMS,'H':H.decimal(),'H_raw':H.raw(),
            'mass':mass_sum.decimal(),'mass_raw':mass_sum.raw(),
            'conditional_probability_range':IV(smallest_q,largest_q).decimal(),
            'leaves':leaves,'nodes':nodes,'seconds':time.monotonic()-start}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,required=True)
    ap.add_argument('--a',default='1/40');ap.add_argument('--output',default=None)
    args=ap.parse_args();d=entropy_interval(args.n,Fraction(args.a))
    if args.output:Path(args.output).write_text(json.dumps(d,indent=2)+'\n')
    print(json.dumps(d,indent=2))
if __name__=='__main__':main()
