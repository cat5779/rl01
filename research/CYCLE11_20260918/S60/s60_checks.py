#!/usr/bin/env python3
"""Exact and floating checks for S60 cycle09.

The script is deliberately supplementary: the universal [CF] verdict in the
report is INCOMPLETE.  Exact routines verify the arithmetic identities and
special-family certificates used in the report; random search is only a
falsification aid.
"""

from __future__ import annotations

import argparse
import itertools
from fractions import Fraction

import numpy as np
import sympy as sp


def exact_reviewed_example() -> None:
    A = sp.Matrix([[sp.Rational(1, 5), sp.Rational(1, 10)],
                   [sp.Rational(1, 10), sp.Rational(3, 5)]])
    v = sp.Matrix([1, 1])
    n = 2
    total = sp.Rational(0)
    h12 = sp.Rational(0)

    rows = []
    for y in itertools.product([0, 1], repeat=n):
        M = A - sp.diag(*[1 - yi for yi in y])
        V = M.inv()
        p = (-1) ** (n - sum(y)) * M.det()
        W = V * v
        u = (v.T * V * v)[0]
        s = sp.trace(V)
        z = (v.T * V**2 * v)[0]
        w = (v.T * V**3 * v)[0]
        term = p * ((s*s - sp.trace(V**2))*u*u - 4*s*u*z + 2*z*z + 4*u*w)
        total += sp.factor(term)

        i, j = 0, 1
        di, dj = V[i, i], V[j, j]
        zi, zj = W[i]**2, W[j]**2
        mixed = ((di*dj - V[i, j]*V[j, i])*u*u
                 - 2*u*(di*zj + dj*zi) + 2*zi*zj
                 + 4*u*sp.re(W[i]*V[i, j]*W[j]))
        h12 += p * mixed
        rows.append((y, sp.factor(p), sp.factor(term)))

    target_total = sp.Rational(1095440907576040000, 3400782877756341)
    target_h12 = sp.Rational(-7058578388000000, 3400782877756341)
    assert sp.factor(total - target_total) == 0
    assert sp.factor(h12 - target_h12) == 0

    C = sp.Matrix([[sp.Rational(16, 100), -sp.Rational(1, 100)],
                   [-sp.Rational(1, 100), sp.Rational(24, 100)]])
    d = sp.Matrix([1, 1])
    Cp = sp.diag(sp.Rational(3, 5), -sp.Rational(1, 5))
    b = C.inv() * d
    Gpp = 2 * (b.T * Cp * C.inv() * Cp * b)[0] + 2 * (b.T*b)[0]
    target_Gpp = sp.Rational(17967160000, 56181887)
    assert sp.factor(Gpp - target_Gpp) == 0

    print("reviewed example F'' =", total)
    print("reviewed example H12 =", h12)
    print("comparator b =", list(b))
    print("comparator G'' =", Gpp)


def exact_negative_single_atom() -> None:
    a = sp.symbols('a', real=True)
    f = (a + sp.Rational(1, 5)) / (a + sp.Rational(4, 5))
    val = sp.diff(f, a, 2).subs(a, 0)
    assert val == -sp.Rational(75, 32)
    print("single full-atom curvature =", val)


def exact_gram_nonconcavity() -> None:
    h = sp.symbols('h', real=True)
    g = (sp.Rational(1, 10) + sp.Rational(4, 5)*h - h*h)**2
    val = sp.diff(g, h, 2).subs(h, 0)
    assert val == sp.Rational(22, 25)
    print("G_{12,12}''(0) =", val)


def power_to_bernstein(coeffs: list[sp.Rational], degree: int) -> list[sp.Rational]:
    out = []
    for j in range(degree + 1):
        bj = sum(coeffs[k] * sp.binomial(j, k) / sp.binomial(degree, k)
                 for k in range(j + 1))
        out.append(sp.factor(bj))
    return out


def exact_three_site_family() -> None:
    t, x = sp.symbols('t x', real=True)
    N = (48 - 280*t + 752*t**2 - 1004*t**3 + 944*t**4
         - 996*t**5 + 1144*t**6 - 1104*t**7 + 352*t**8)
    Q = sp.Poly(sp.expand(N.subs(t, x/2)), x)
    coeffs = [Q.nth(k) for k in range(9)]
    bern = power_to_bernstein(coeffs, 8)
    expected = [sp.Rational(48), sp.Rational(61, 2), sp.Rational(138, 7),
                sp.Rational(1501, 112), sp.Rational(1423, 140),
                sp.Rational(569, 64), sp.Rational(495, 56),
                sp.Rational(297, 32), sp.Rational(9)]
    assert bern == expected
    assert all(b > 0 for b in bern)
    print("three-site Bernstein coefficients:")
    print(bern)


def dpp_atoms(A: np.ndarray) -> np.ndarray:
    n = A.shape[0]
    out = np.empty(2**n, dtype=float)
    for mask in range(2**n):
        y = np.array([(mask >> i) & 1 for i in range(n)], dtype=int)
        M = A - np.diag(1-y)
        out[mask] = ((-1) ** (n-int(y.sum()))) * np.linalg.det(M).real
    return out


def fisher_second(A: np.ndarray, v: np.ndarray) -> float:
    n = A.shape[0]
    total = 0.0
    for mask in range(2**n):
        y = np.array([(mask >> i) & 1 for i in range(n)], dtype=int)
        M = A - np.diag(1-y)
        V = np.linalg.inv(M)
        p = ((-1) ** (n-int(y.sum()))) * np.linalg.det(M).real
        u = np.vdot(v, V @ v).real
        z = np.vdot(v, V @ V @ v).real
        w = np.vdot(v, V @ V @ V @ v).real
        s = np.trace(V).real
        r2 = np.trace(V @ V).real
        total += p * ((s*s-r2)*u*u - 4*s*u*z + 2*z*z + 4*u*w)
    return float(total)


def random_strict_kernel(rng: np.random.Generator, n: int) -> np.ndarray:
    Z = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
    Q, _ = np.linalg.qr(Z)
    lam = rng.uniform(0.02, 0.98, size=n)
    return Q @ np.diag(lam) @ Q.conj().T


def random_search(n: int, trials: int, seed: int) -> None:
    rng = np.random.default_rng(seed)
    best = (float('inf'), None, None)
    for _ in range(trials):
        A = random_strict_kernel(rng, n)
        v = rng.normal(size=n) + 1j*rng.normal(size=n)
        v /= np.linalg.norm(v)
        val = fisher_second(A, v)
        if val < best[0]:
            best = (val, A, v)
    print(f"n={n}, trials={trials}, minimum floating F''={best[0]:.16g}")
    print(f"benchmark 32/n={32/n:.16g}")
    if best[0] < -1e-9:
        print("WARNING: floating negative candidate; exact certification is required.")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--exact', action='store_true', help='run all exact checks')
    ap.add_argument('--exact-example', action='store_true')
    ap.add_argument('--three-site', action='store_true')
    ap.add_argument('--random', action='store_true')
    ap.add_argument('--n', type=int, default=4)
    ap.add_argument('--trials', type=int, default=1000)
    ap.add_argument('--seed', type=int, default=20260918)
    args = ap.parse_args()

    if args.exact or args.exact_example:
        exact_reviewed_example()
        exact_negative_single_atom()
        exact_gram_nonconcavity()
    if args.exact or args.three_site:
        exact_three_site_family()
    if args.random:
        random_search(args.n, args.trials, args.seed)
    if not (args.exact or args.exact_example or args.three_site or args.random):
        ap.print_help()


if __name__ == '__main__':
    main()
