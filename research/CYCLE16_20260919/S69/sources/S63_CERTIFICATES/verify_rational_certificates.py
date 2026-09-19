#!/usr/bin/env python3
"""Exact-rational, standard-library verification of the transcendental input
and the final continuous-interval polynomial payment. No floating arithmetic.
Run after payment_certificate has produced payment_coefficients_integer.txt.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def add(p,q):
    r=[F(0)]*max(len(p),len(q))
    for i,v in enumerate(p):r[i]+=v
    for i,v in enumerate(q):r[i]+=v
    while len(r)>1 and not r[-1]:r.pop()
    return r

def scale(p,c):return [v*c for v in p]
def mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,u in enumerate(p):
        for j,v in enumerate(q):r[i+j]+=u*v
    while len(r)>1 and not r[-1]:r.pop()
    return r

def affine_compose(p,b,h):
    ans=[F(0)]
    for c in reversed(p):ans=add(mul(ans,[b,h]),[c])
    return ans

def atan_bracket(x,m=64):
    assert m%2==0
    s=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(m)),F(0))
    return s,s+x**(2*m+1)/F(2*m+1)

l5,u5=atan_bracket(F(1,5));l239,u239=atan_bracket(F(1,239))
pi_lo=16*l5-4*u239;pi_hi=16*u5-4*l239
al,ah,den=map(int,(ROOT/'alpha60.txt').read_text().split())
assert 4*F(al,den)**2*pi_hi**2<3<4*F(ah,den)**2*pi_lo**2
al19=F(2756644477108960247,10**19);ah19=F(2756644477108960248,10**19)
assert 4*al19**2*pi_hi**2<3<4*ah19**2*pi_lo**2
print('ALPHA: PASS, both 19- and 60-place brackets, exact rational comparisons.')

raw=[tuple(map(int,s.split())) for s in (ROOT/'payment_coefficients_integer.txt').read_text().splitlines()]
assert len(raw)==10 and all(l<=h for l,h in raw)
# t=200a-5 is negative throughout the theorem interval.
p=[F(l if k%2==0 else h,10**8) for k,(l,h) in enumerate(raw)]
p[0]-=F(1,10**6)
P=affine_compose(p,F(-5),F(200))
a=[F(0),F(1)];one_minus_a=[F(1),F(-1)];v=[F(19,20),F(1)];one_minus_v=[F(1,20),F(-1)]
b0=mul(a,one_minus_a);b1=mul(v,one_minus_v);D=mul(b0,b1)
num=add(scale(b1,F(2,3)),scale(b0,F(1,3)))
Cminus1=[F(61,200),F(51,10)]
epsilon=F(1,25)
P[0]-=epsilon
G=add(mul(P,D),scale(mul(Cminus1,num),F(-1)))
# Normalize a=21/1000+(3/1000)x, x in [0,1].
Gx=affine_compose(G,F(21,1000),F(3,1000));degree=len(Gx)-1
bern=[sum((Gx[i]*F(comb(k,i),comb(degree,i)) for i in range(k+1)),F(0)) for k in range(degree+1)]
assert all(v>F(1,40000) for v in bern)
bern_floor=[(v*10**9).numerator//(v*10**9).denominator for v in bern]
print('BERNSTEIN: PASS, degree',degree,'all coefficients > 1/40000.')
print('Bernstein lower-bound numerators, common denominator 10^9:',bern_floor)
# Simple published uniform upper bound for the local variational payment.
absbound=sum(max(abs(F(l,10**8)),abs(F(h,10**8)))*F(4,5)**k for k,(l,h) in enumerate(raw))+F(1,10**6)
assert absbound<19
print('PAYMENT UPPER: PASS, P(a)<19 on [21/1000,3/125].')
# Rigorous tail from ||D||_1<=44, hscale=1/200, V0<=1500,V1<=10000.
x=F(11,50)
tail=F(1550)*x**9/F(factorial(9))/(1-x/F(10))
assert tail<F(1,10**8)<F(1,10**6)
print('MOVING-LAW TAIL: PASS, <1/10^8; declared remainder 1/10^6.')
# All affine edge matrices are positive semidefinite on the whole interval.
caps=[tuple(map(int,s.split())) for s in (ROOT/'guard_caps_integer.txt').read_text().splitlines()]
assert len(caps)==256
for l,h in caps:
    for aa in (F(21,1000),F(3,125)):
        C=F(261,200)+F(51,10)*aa
        cap=(F(3,100)-aa)*F(l,100)+(aa-F(1,50))*F(h,100)
        delta=C-cap
        assert 0<=delta<=C/2
print('PSD: PASS, 256 affine matrices, both interval endpoints (hence the interval).')
(ROOT/'bernstein_lower_numerators.txt').write_text(' '.join(map(str,bern_floor))+'\n')
print('RATIONAL CERTIFICATES: ALL PASS.')
