#!/usr/bin/env python3
"""QWE06 floating diagnostic for the typical negative-damping theorem.

This is a regression/falsification check only, not interval arithmetic.
It uses only the exact task formulas for the count law, Q-polynomials,
and the prescribed degree-2 Johnson clock.
"""
from __future__ import annotations
import math

C = 19.0 / 20.0
ASTAR = (1.0 - C) / 2.0

def logsumexp(xs):
    m = max(xs)
    return m + math.log(sum(math.exp(x - m) for x in xs))

def q_logjets(r: int, d: int, xi: float):
    """Return log Q_r^(d), d/dxi log Q, d2/dxi2 log Q."""
    if r == 0:
        return 0.0, 0.0, 0.0
    logs = [0.0]
    cur = 0.0
    for s in range(r):
        ratio = ((r - s) * (r + 2*d - 1 + s) / ((d + s) * (s + 1))) * xi
        cur += math.log(ratio)
        logs.append(cur)
    z = logsumexp(logs)
    ws = [math.exp(x - z) for x in logs]
    mean = sum(s*w for s, w in enumerate(ws))
    var = sum((s-mean)**2*w for s, w in enumerate(ws))
    return z, mean/xi, (var-mean)/(xi*xi)

def logbinom(n, r):
    return math.lgamma(n+1)-math.lgamma(r+1)-math.lgamma(n-r+1)

def layer(n: int, l: int, a: float):
    k = n//2
    m = min(l, n-l)
    d = k-m+1
    Cl = l*(n-l)
    xi = a*(1-C-a)/C
    h = (1-C-2*a)/C
    A = xi*(1+xi)
    gamma2 = 2*(n-1)/Cl

    qm, qm1, qm2 = q_logjets(m, d, xi)
    qp, qp1, qp2 = q_logjets(m-2, d, xi)

    taux = (qm1-qp1)/gamma2
    tauxx = (qm2-qp2)/gamma2

    base = (1-a-C)*(1-a) if l <= k else a*(a+C)
    basep = 2*a + C - 2 if l <= k else 2*a + C
    logpi = logbinom(k,m) + m*math.log(C) + (k-m)*math.log(base) + qm
    phi = (k-m)*basep/base + h*qm1

    Lambda = h*h*(gamma2*taux*taux-tauxx) + 2*taux/C
    M = Lambda - 2*phi*h*taux
    return logpi, M/taux

def diagnostic(n: int, a: float, widths: float = 12.0):
    rho = a + C/2
    v = (1-C*C)/4 - (a-ASTAR)**2
    mu = n*rho
    sd = math.sqrt(n*v)
    lo = max(4, math.floor(mu-widths*sd))
    hi = min(n-4, math.ceil(mu+widths*sd))

    rows = [layer(n,l,a) for l in range(lo,hi+1)]
    mz = max(x[0] for x in rows)
    ws = [math.exp(lp-mz) for lp,_ in rows]
    scale = math.exp(mz)
    retained = scale*sum(ws)
    neg = scale*sum(w for w,(_,mnorm) in zip(ws,rows) if mnorm < 0)
    first = scale*sum(w*max(-mnorm,0.0) for w,(_,mnorm) in zip(ws,rows))/math.sqrt(n)

    h = (1-C-2*a)/C
    limit = 2*abs(h)/math.sqrt(2*math.pi*v)
    return retained, neg, first, limit

def main():
    a = 0.02
    print("fixed a=0.02")
    print("n retained_mass negative_mass scaled_negative_first_moment limit")
    for n in [400, 4000, 10000, 40000]:
        retained, neg, first, limit = diagnostic(n,a)
        print(n, retained, neg, first, limit)

if __name__ == "__main__":
    main()
