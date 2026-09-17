#!/usr/bin/env python3
"""Exact nested refinements of the split-tail gap cover.

The theorem freezes the 100-bin lower bound.  This auxiliary check shows that
it is conservative rather than a resolution artifact.
"""
from fractions import Fraction as F
from math import isqrt

L=F(3,40)

def ceil_sqrt(x:F)->int:
    n,d=x.numerator,x.denominator
    k=isqrt(n//d)
    while k*k*d<n:k+=1
    while k and (k-1)*(k-1)*d>=n:k-=1
    return k

def cutoff(delta:F)->int:
    z=(1-delta**2)**2/(4*delta**3*(2-delta))
    return max(0,ceil_sqrt(z)-1)

def bound(N:int):
    best=None; row=None
    for i in range(N):
        left=L*F(i,2*N); right=L*F(i+1,2*N)
        m=cutoff(right); ell=L-2*left
        c=F(24*m*m,1)/ell**2
        if best is None or c<best:
            best,row=c,(i,m)
    return best,row

last=F(0)
for N in [50,100,200,400,800,1600]:
    value,(i,m)=bound(N)
    assert value>=last
    last=value
    print(N,f"{value.numerator}/{value.denominator}",f"{float(value):.12f}",i,m)
assert bound(100)[0]==F(366_368_000_000,1323)
print("NESTED_EXACT_COVER_REFINEMENT_PASS")
