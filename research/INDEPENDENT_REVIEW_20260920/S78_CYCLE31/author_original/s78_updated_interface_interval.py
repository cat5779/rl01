#!/usr/bin/env python3
"""Interval arithmetic for the updated S78 entropy interface.

Uses the certified 20-moment upper bound for the infinite-star log-barrier
completion payment, then adds the unchanged S72 core/pair payment.
"""
from math import factorial
from mpmath import iv
import sympy as sp

iv.dps = 90
c = iv.mpf(19)/20
delta = iv.mpf(1)/50
s = c**2/iv.pi**2
A0 = iv.mpf(1)/4-s
N = 20


def ivrat(r):
    r = sp.Rational(r)
    return iv.mpf(int(r.p))/int(r.q)

# Compute moments through 20 as in s78_barrier_moments_interval.py.
q = [iv.mpf([0,0]) for _ in range(N+1)]
for n in range(1,N+1):
    B4=sp.bernoulli(4*n)
    total=ivrat(-B4*(2**(4*n)-1)/sp.factorial(4*n))*c**(4*n)
    old=total-s**(2*n)
    B2=sp.bernoulli(2*n)
    lc=(sp.Rational(2**(2*n)*(2**(2*n)-1),1)*B2
        /(sp.Rational(2*n,1)*sp.factorial(2*n)))
    q[n]=ivrat(lc)*(iv.mpf(2)**(2*n))*old
coef=[iv.mpf([0,0]) for _ in range(N+1)]
coef[0]=iv.mpf(1)
for n in range(1,N+1):
    coef[n]=sum(k*q[k]*coef[n-k] for k in range(1,n+1))/n
mom=[None]+[iv.mpf(factorial(2*n))*coef[n] for n in range(1,N+1)]
D20=2*iv.log(A0/(delta*(1-delta)))
for n in range(1,N+1):
    D20-=mom[n]/(n*(4*A0**2)**n)

kappa=c**2/(4*delta*(delta+c))
C_log=iv.log(1+kappa)
tau2=2/delta-4
core_pair=2*C_log*tau2
new_total=core_pair+D20
benchmark_rhs=new_total-iv.mpf(1)/50-iv.mpf('0.26275')
old_total=iv.mpf('107974.9489647355')
improvement=old_total/new_total

print('D20_completion_upper =',D20)
print('core_pair_payment =',core_pair)
print('new_total_payment =',new_total)
print('benchmark_rhs_using_star_lower_0.26275 =',benchmark_rhs)
print('old_to_new_improvement_factor =',improvement)
assert new_total.b < iv.mpf('490.675')
assert benchmark_rhs.a > 0
print('PASS_UPDATED_INTERFACE_INTERVAL')
