#!/usr/bin/env python3
"""Certified midpoint barrier payment by a 20-moment expansion.

The selected pair is the nearest half-density sine pair at c=19/20.
For the infinite old one-center star, t is a Rademacher series and
  ell = 2 log(A0) + log(1-t^2/(4 A0^2)).
The first 20 positive log-series moments give an upper bound on the exact
completion payment.  The 21st moment plus the support ratio bounds the tail.
"""
from math import factorial
from mpmath import iv
import sympy as sp

iv.dps = 100
N = 21
c = iv.mpf(19) / 20
delta = iv.mpf(1) / 50
s = c**2 / iv.pi**2
A0 = iv.mpf(1) / 4 - s


def ivrat(r):
    r = sp.Rational(r)
    return iv.mpf(int(r.p)) / int(r.q)

# q[n] is the coefficient of z^(2n) in log E exp(z t).
q = [iv.mpf([0, 0]) for _ in range(N + 1)]
for n in range(1, N + 1):
    # Sum of w_l^(2n) over all opposite-parity leaves except the selected
    # nearest leaf.  The total odd-lattice power sum is rational because
    # zeta(4n)/pi^(4n) is rational.
    B4 = sp.bernoulli(4*n)
    total_weight_power = (
        ivrat(-B4 * (2**(4*n) - 1) / sp.factorial(4*n)) * c**(4*n)
    )
    old_weight_power = total_weight_power - s**(2*n)
    amplitude_power = (iv.mpf(2)**(2*n)) * old_weight_power

    B2 = sp.bernoulli(2*n)
    log_cosh_coeff = (
        sp.Rational(2**(2*n) * (2**(2*n) - 1), 1)
        * B2 / (sp.Rational(2*n, 1) * sp.factorial(2*n))
    )
    q[n] = ivrat(log_cosh_coeff) * amplitude_power

# If exp(sum q_n r^n)=sum c_n r^n, then
# n c_n = sum_{k=1}^n k q_k c_{n-k}; E t^(2n)=(2n)! c_n.
coef = [iv.mpf([0, 0]) for _ in range(N + 1)]
coef[0] = iv.mpf(1)
for n in range(1, N + 1):
    coef[n] = sum(k*q[k]*coef[n-k] for k in range(1, n+1)) / n
mom = [None] + [iv.mpf(factorial(2*n))*coef[n] for n in range(1, N+1)]

base = 2 * iv.log(A0 / (delta*(1-delta)))
correction_20 = iv.mpf([0, 0])
for n in range(1, 21):
    term = mom[n] / (n * (4*A0**2)**n)
    correction_20 += term
    if n in (1, 2, 5, 10, 20):
        print(n, 'term', term, 'D_partial', base-correction_20)

D20 = base - correction_20
T = c**2/4 - s
R = (T/A0)**2
term21 = mom[21] / (21*(4*A0**2)**21)
# For x=t^2/(4A0^2) <= R,
# sum_{n>=21} E[x^n]/n <= E[x^21]/(21(1-R)).
tail = term21 / (1-R)
exact_lower = D20 - tail
exact_upper = D20

print('D20 =', D20)
print('support_ratio_R =', R)
print('term21 =', term21)
print('tail_bound =', tail)
print('exact_payment_lower =', exact_lower)
print('exact_payment_upper =', exact_upper)

assert exact_lower.a > 0
assert exact_upper.b < iv.mpf('3.746')
print('PASS_BARRIER_MOMENT_INTERVAL')
