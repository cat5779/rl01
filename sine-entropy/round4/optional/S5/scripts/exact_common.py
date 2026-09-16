#!/usr/bin/env python3
"""Exact arithmetic used by the S5 finite certificates.

Only Python's standard library is required. No floating-point number enters
any assertion in the certificate scripts.
"""
from __future__ import annotations
if not __debug__:
    raise RuntimeError('Run without -O: exact certificate assertions must be enabled.')

from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from typing import Iterable
import math

@dataclass(frozen=True)
class Interval:
    lo: Q
    hi: Q
    def __post_init__(self):
        if self.lo > self.hi:
            raise ValueError('Reversed interval.')
    @staticmethod
    def point(x):
        x=Q(x);return Interval(x,x)
    def __add__(self,other):
        if not isinstance(other,Interval): other=Interval.point(other)
        return Interval(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self): return Interval(-self.hi,-self.lo)
    def __sub__(self,other): return self+(-other if isinstance(other,Interval) else -Q(other))
    def __rsub__(self,other):return Interval.point(other)+(-self)
    def __mul__(self,other):
        if not isinstance(other,Interval):other=Interval.point(other)
        a=[self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi]
        return Interval(min(a),max(a))
    __rmul__=__mul__
    def __truediv__(self,other):
        if not isinstance(other,Interval):other=Interval.point(other)
        if other.lo<=0<=other.hi:raise ZeroDivisionError('Interval contains zero.')
        return self*Interval(1/other.hi,1/other.lo)
    def contains_zero(self):return self.lo<=0<=self.hi
    def width(self):return self.hi-self.lo
    def outward(self,digits=40):
        """Round outward to exact terminating decimal strings."""
        scale=10**digits
        lower=(self.lo*scale).__floor__()
        upper=(self.hi*scale).__ceil__()
        def fmt(x):
            sign='-' if x<0 else '';x=abs(x)
            return f'{sign}{x//scale}.{x%scale:0{digits}d}'
        return dict(lower=fmt(lower),upper=fmt(upper))

LOG_TERMS=80

@lru_cache(maxsize=None)
def _log_unit(y:Q,terms:int=LOG_TERMS)->Interval:
    """Enclose log(y) for 1<=y<=2 using an exact atanh series."""
    if not 1<=y<=2:raise ValueError('Unit argument is outside [1,2].')
    z=(y-1)/(y+1)
    power=z;s=Q(0)
    for j in range(terms):
        s+=2*power/(2*j+1)
        power*=z*z
    # power = z^(2*terms+1). Every omitted denominator is >=2*terms+1.
    tail=2*power/((2*terms+1)*(1-z*z))
    return Interval(s,s+tail)

@lru_cache(maxsize=None)
def log_q(x:Q)->Interval:
    x=Q(x)
    if x<=0:raise ValueError('A logarithm requires a positive rational.')
    m=0;y=x
    while y>=2:y/=2;m+=1
    while y<1:y*=2;m-=1
    return _log_unit(y)+m*_log_unit(Q(2))

@dataclass(frozen=True)
class Jet:
    value:Q
    first:Q=Q(0)
    second:Q=Q(0)
    def __add__(self,other):
        if not isinstance(other,Jet):other=Jet(Q(other))
        return Jet(self.value+other.value,self.first+other.first,self.second+other.second)
    __radd__=__add__
    def __mul__(self,other):
        if not isinstance(other,Jet):other=Jet(Q(other))
        return Jet(self.value*other.value,self.first*other.value+self.value*other.first,
                   self.second*other.value+2*self.first*other.first+self.value*other.second)
    __rmul__=__mul__
    def __pow__(self,n:int):
        if n<0:raise ValueError('Only nonnegative powers are supported.')
        z=Jet(Q(1))
        for _ in range(n):z=z*self
        return z


def channel_jets(n:int,k:int,law:dict[int,Q],a:Q,c:Q)->list[Jet]:
    if not Q(0)<a<1-c:raise ValueError('Strict legal interior required.')
    if sum(law.values())!=1:raise ValueError('Input law is not normalized.')
    if any(A.bit_count()!=k or p<0 for A,p in law.items()):raise ValueError('Input is not homogeneous.')
    factors=[Jet(a+c,Q(1)),Jet(1-a-c,Q(-1)),Jet(a,Q(1)),Jet(1-a,Q(-1))]
    out=[]
    for S in range(1<<n):
        ell=S.bit_count();total=Jet(Q(0))
        for A,mu in law.items():
            t=(S&A).bit_count()
            es=(t,k-t,ell-t,n-k-ell+t)
            term=Jet(mu)
            for f,e in zip(factors,es):term=term*f**e
            total=total+term
        out.append(total)
    assert sum(x.value for x in out)==1
    assert sum(x.first for x in out)==0
    assert sum(x.second for x in out)==0
    assert all(x.value>0 for x in out)
    return out


def count_jets(n:int,k:int,a:Q,c:Q)->list[Jet]:
    out=[Jet(Q(1))]
    for i in range(n):
        q=a+c if i<k else a
        f0=Jet(1-q,Q(-1));f1=Jet(q,Q(1))
        new=[Jet(Q(0)) for _ in range(len(out)+1)]
        for j,z in enumerate(out):new[j]=new[j]+z*f0;new[j+1]=new[j+1]+z*f1
        out=new
    return out


def ensure_output(path:Path)->Path:
    """Keep certificate runs away from frozen evidence and source files."""
    path=path.resolve()
    root=Path(__file__).resolve().parents[1]
    protected=[root/'evidence',root/'scripts']
    if path==root or any(path==p or p in path.parents for p in protected):
        raise ValueError('Choose an output directory, not the package root, scripts, or frozen evidence.')
    path.mkdir(parents=True,exist_ok=True)
    return path

@dataclass(frozen=True)
class Qsqrt2:
    """The exact real algebraic number rational + radical*sqrt(2)."""
    rational:Q=Q(0)
    radical:Q=Q(0)
    def __add__(self,other):
        if not isinstance(other,Qsqrt2):other=Qsqrt2(Q(other))
        return Qsqrt2(self.rational+other.rational,self.radical+other.radical)
    __radd__=__add__
    def __neg__(self):return Qsqrt2(-self.rational,-self.radical)
    def __sub__(self,other):return self+(-other if isinstance(other,Qsqrt2) else -Q(other))
    def __mul__(self,other):
        if not isinstance(other,Qsqrt2):other=Qsqrt2(Q(other))
        return Qsqrt2(self.rational*other.rational+2*self.radical*other.radical,
                      self.rational*other.radical+self.radical*other.rational)
    __rmul__=__mul__
    def as_json(self):return {'rational':str(self.rational),'sqrt2_coefficient':str(self.radical)}
