"""Outward fixed-point intervals; no floating point in certified arithmetic.
Log uses range reduction to [1,2] and the atanh series with a proved remainder.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
BITS=128
SCALE=1 << BITS
TERMS=48

def ceil_div(a:int,b:int)->int:
    if b<=0: raise ValueError('positive denominator required')
    return -((-a)//b)

@dataclass(frozen=True,slots=True)
class IV:
    lo:int
    hi:int
    def __post_init__(self):
        if self.lo>self.hi: raise ArithmeticError('reversed interval')
    @staticmethod
    def point(x):
        if isinstance(x,IV):return x
        q=Fraction(x);n=q.numerator*SCALE;d=q.denominator
        return IV(n//d,ceil_div(n,d))
    @staticmethod
    def bounds(a,b):
        return IV(IV.point(a).lo,IV.point(b).hi)
    def __add__(self,b):
        b=IV.point(b);return IV(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return IV(-self.hi,-self.lo)
    def __sub__(self,b):return self+-IV.point(b)
    def __rsub__(self,b):return IV.point(b)+-self
    def __mul__(self,b):
        b=IV.point(b);z=(self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi)
        return IV(min(z)//SCALE,ceil_div(max(z),SCALE))
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi:raise ArithmeticError('interval division across zero')
        if self.hi<0:return -((-self).inv())
        return IV(SCALE*SCALE//self.hi,ceil_div(SCALE*SCALE,self.lo))
    def __truediv__(self,b):return self*IV.point(b).inv()
    def __rtruediv__(self,b):return IV.point(b)*self.inv()
    def sq(self):
        if self.lo<=0<=self.hi:return IV(0,ceil_div(max(self.lo**2,self.hi**2),SCALE))
        return IV(min(self.lo**2,self.hi**2)//SCALE,ceil_div(max(self.lo**2,self.hi**2),SCALE))
    def __pow__(self,n):
        if n<0:return self.inv()**(-n)
        ans=IV.point(1);b=self
        while n:
            if n&1:ans=ans*b
            n//=2
            if n:b=b.sq()
        return ans
    def log(self):
        if self.lo<=0:raise ArithmeticError('nonpositive log interval')
        return IV(log_endpoint(self.lo).lo,log_endpoint(self.hi).hi)
    def rational(self):return [str(Fraction(self.lo,SCALE)),str(Fraction(self.hi,SCALE))]
    def outward_decimal(self,places=12):
        d=10**places;l=self.lo*d//SCALE;h=ceil_div(self.hi*d,SCALE)
        def f(n):return ('-' if n<0 else '')+str(abs(n)//d)+'.'+str(abs(n)%d).zfill(places)
        return [f(l),f(h)]
    def __repr__(self):return str(self.outward_decimal())

@lru_cache(maxsize=1)
def log2():
    return log_reduced(IV.point(2))

def log_reduced(x:IV):
    z=(x-1)/(x+1);z2=z.sq();power=z;total=IV.point(0)
    for k in range(TERMS):
        total=total+power/Fraction(2*k+1)
        power=power*z2
    rem=2*power/((2*TERMS+1)*(1-z2))
    if z.lo<0 or z2.hi>=SCALE:raise ArithmeticError('log range reduction failed')
    return IV((2*total).lo,(2*total+rem).hi)

def log_endpoint(v:int):
    if v<=0:raise ArithmeticError('log of nonpositive dyadic')
    k=v.bit_length()-1-BITS
    q=Fraction(v,1 << (BITS+k)) if BITS+k>=0 else Fraction(v*(1 << (-BITS-k)))
    out=log_reduced(IV.point(q))
    return out+k*log2() if k else out

def horner(coeff,x:IV):
    z=IV.point(0)
    for a in reversed(coeff):z=z*x+a
    return z
