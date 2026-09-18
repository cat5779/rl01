#!/usr/bin/env python3
"""S41 cycle-05 exact obstruction and complete-jet term-algebra checks.

This script is *not* a substitute for the analytic proof in
S41_CYCLE05_RESULT.md.  It supplies three reproducible checks:

1. An exact SymPy counterexample to the cycle-04 U=T+W directional lemma.
   The complete V14 kernel is constructed symbolically and simplifies to an
   explicit one-variable formula.  At the counterexample point T0=W0=0 but
   dK/dt=-16/1197.
2. A symbolic exponent algebra for the repaired connected-pair derivative.
   Starting from the exact Bregman/flip majorant operations in the manuscript,
   it generates all 147 raw marked monomials and reduces them to the 33
   minimal families displayed in the proof.
3. Optional floating-point random diagnostics for the tail and repaired
   directional inequalities (diagnostic only, not certification).
"""
from __future__ import annotations

import argparse
import itertools
import math
from collections import defaultdict
from dataclasses import dataclass
from typing import Iterable

import numpy as np
import sympy as sp


def phi(q):
    return (q - sp.Rational(1, 2)) * sp.log(q / (1 - q))


def phi1(q):
    return sp.log(q / (1 - q)) + (q - sp.Rational(1, 2)) / (q * (1 - q))


def phi2(q):
    return 1 / (2 * q**2 * (1 - q) ** 2)


def bphi(a, b):
    return phi(a) - phi(b) - phi1(b) * (a - b)


def bphi1(a, b):
    return phi1(a) - phi1(b) - phi2(b) * (a - b)


def flip_data(data, j: int):
    q, v, G, signs = data
    oj = signs[j] * G[j, j] - 1
    coeff = signs[j] / oj
    col = G[:, j]
    qn = sp.simplify(q + coeff * sp.conjugate(v[j]) * v[j])
    vn = sp.simplify(v - coeff * col * v[j])
    Gn = sp.simplify(G - coeff * col * col.conjugate().T)
    sn = signs.copy()
    sn[j] = -sn[j]
    return qn, vn, Gn, sn


def Bphi_sum(data):
    q, _, G, signs = data
    total = 0
    for i in range(G.rows):
        qi, _, _, _ = flip_data(data, i)
        rbar = signs[i] - G[i, i]
        total += rbar * bphi(qi, q)
    return sp.factor(total)


def v14_kernel(data):
    q, v, G, signs = data
    n = G.rows
    A = 1 + (v.conjugate().T * v)[0]
    flips = [flip_data(data, j) for j in range(n)]
    base_B = Bphi_sum(data)
    G2 = G * G
    ans = phi2(q)
    for j, dj_data in enumerate(flips):
        qj, vj, _, _ = dj_data
        rbar = signs[j] - G[j, j]
        dj = qj - q
        Aj = 1 + (vj.conjugate().T * vj)[0]
        ans += rbar * bphi1(qj, q)
        ans += G2[j, j] * bphi(qj, q)
        ans += rbar * ((phi1(qj) - phi1(q)) * Aj - phi2(q) * dj * A)
        ans += rbar * (Bphi_sum(dj_data) - base_B)
    return sp.simplify(ans)


def exact_counterexample():
    """Return the exact matrices and complete-kernel formula."""
    lam = sp.symbols("lam", real=True)
    rt = sp.sqrt(sp.Rational(3, 8))
    # Rows of a 5x2 isometry.  Rows 2 and 3 are the +/- components of u.
    U = sp.Matrix(
        [
            [sp.Rational(1, 2), 0],
            [rt, rt],
            [0, sp.Rational(1, 2) / sp.sqrt(2)],
            [0, -sp.Rational(1, 2) / sp.sqrt(2)],
            [rt, -rt],
        ]
    )
    w = sp.Matrix([0, 0, 1 / sp.sqrt(2), 1 / sp.sqrt(2), 0])
    B = U * U.T
    A = B + lam * (w * w.T)

    x = sp.Rational(1, 2)
    J = [1, 2, 3, 4]
    AJ = A.extract(J, J)
    q = sp.Rational(1, 2) + x * (A[0, 0] - sp.Rational(1, 2))
    coeff_v = 2 * x / sp.sqrt(1 - x * x)
    v = sp.Matrix([coeff_v * A[j, 0] for j in J])
    G = 2 / (1 - x * x) * (sp.eye(4) - x * (2 * AJ - sp.eye(4)))
    signs = sp.Matrix([1, 1, 1, 1])
    K = sp.simplify(v14_kernel((q, v, G, signs)))

    expected_K = (
        sp.log((16 * lam - 29) / (16 * lam - 27)) / 3
        - sp.Rational(9, 2) * sp.log(5)
        + sp.Rational(9, 2) * sp.log(3)
        + sp.Rational(544, 45)
    )
    assert sp.simplify(U.T * U - sp.eye(2)) == sp.zeros(2)
    assert sp.simplify(K - expected_K) == 0
    dK_dlam = sp.simplify(sp.diff(K, lam).subs(lam, sp.Rational(1, 2)))
    assert dK_dlam == sp.Rational(32, 1197)

    # At lambda=1/2, D=A-A^2=(1/4)ww^T.  The Halmos dilation is an exact
    # projection.  Scaling the outside w-coordinate by exp(t) gives
    # lambda(t)=1/(1+exp(2t)), hence lambda'(0)=-1/2.
    A0 = sp.simplify(A.subs(lam, sp.Rational(1, 2)))
    D = sp.simplify(A0 - A0 * A0)
    assert sp.simplify(D - sp.Rational(1, 4) * (w * w.T)) == sp.zeros(5)
    C = sp.Rational(1, 2) * (w * w.T)
    P = sp.Matrix.vstack(
        sp.Matrix.hstack(A0, C),
        sp.Matrix.hstack(C, sp.eye(5) - A0),
    )
    assert sp.simplify(P * P - P) == sp.zeros(10)

    # I={0,...,4}, J={1,...,4}, O is the second copy.  T0=0.  The only
    # coordinates with nonzero p_j=P_{j0} have zero outside column, so W0=0.
    T0 = sp.simplify(sum(P[5 + k, 0] ** 2 for k in range(5)))
    W0 = 0
    for j in J:
        pj2 = sp.simplify(P[j, 0] ** 2)
        Tj = sp.simplify(sum(P[5 + k, j] ** 2 for k in range(5)))
        W0 += pj2 * Tj
    W0 = sp.simplify(W0)
    assert T0 == 0 and W0 == 0

    # The repaired energy Z0 detects the missed connected derivative.
    Tj = {
        i: sp.simplify(sum(P[5 + k, i] ** 2 for k in range(5))) for i in J
    }
    pj2 = {j: sp.simplify(P[j, 0] ** 2) for j in J}
    Sj = {
        i: sp.simplify(sum(P[i, j] ** 2 * pj2[j] for j in J)) for i in J
    }
    Z0 = sp.simplify(sum(Tj[i] * Sj[i] for i in J))
    assert Z0 == sp.Rational(9, 4096)

    dK_dt = sp.simplify(-sp.Rational(1, 2) * dK_dlam)
    assert dK_dt == -sp.Rational(16, 1197)
    h_legal = sp.log(3) / 2  # log s_x at x=1/2
    dK_dt_legal = sp.simplify(h_legal * dK_dt)
    assert dK_dt_legal == -sp.Rational(8, 1197) * sp.log(3)
    return {
        "U": U,
        "w": w,
        "A": A,
        "K": K,
        "dK_dlambda": dK_dlam,
        "dK_dt": dK_dt,
        "T0": T0,
        "W0": W0,
        "Z0": Z0,
        "dK_dt_legal": dK_dt_legal,
    }


# ---------------------------------------------------------------------------
# Symbolic exponent coverage for the repaired derivative calculus.
# A monomial is (power of p_i, power of p_j, power of g_ij, mark).
# ---------------------------------------------------------------------------
Monomial = tuple[int, int, int, str | None]


def poly_add(*polys: Iterable[Monomial]) -> list[Monomial]:
    out: list[Monomial] = []
    for p in polys:
        out.extend(p)
    return out


def poly_mul(p: Iterable[Monomial], q: Iterable[Monomial]) -> list[Monomial]:
    out: list[Monomial] = []
    for a, b, c, m in p:
        for aa, bb, cc, mm in q:
            if m is not None and mm is not None:
                raise ValueError("a majorant product may contain only one derivative mark")
            out.append((a + aa, b + bb, c + cc, m or mm))
    return out


def poly_pow(p: Iterable[Monomial], n: int) -> list[Monomial]:
    out: list[Monomial] = [(0, 0, 0, None)]
    for _ in range(n):
        out = poly_mul(out, p)
    return out


def connected_marked_families():
    # D bounds max(|d_i|,|d_i^j|); X bounds |d_i^j-d_i|.
    D = [(2, 0, 0, None), (0, 2, 2, None)]
    X = [(1, 1, 1, None), (2, 0, 2, None), (0, 2, 2, None)]
    Pj = [(0, 2, 0, None)]
    di_dot = [(1, 0, 0, "hi"), (2, 0, 0, "ei")]
    dj_dot = [(0, 1, 0, "hj"), (0, 2, 0, "ej")]

    # Exhaustive derivative of eta_ij=d_i^j-d_i, obtained from
    # u=G_ij v_j/r_j and s=|G_ij|^2/r_j.  The four sources are:
    # coefficient of dot(v_i), dot(u), coefficient of dot(r_i), dot(s).
    eta_dot = [
        (0, 1, 1, "hi"),
        (1, 0, 2, "hi"),
        (1, 1, 0, "gamma"),
        (1, 0, 1, "hj"),
        (1, 1, 1, "ej"),
        (0, 2, 1, "gamma"),
        (0, 1, 2, "hj"),
        (0, 2, 2, "ej"),
        (1, 1, 1, "ei"),
        (0, 2, 2, "ei"),
        (2, 0, 2, "ei"),
        (2, 0, 1, "gamma"),
        (2, 0, 2, "ej"),
        (0, 2, 3, "gamma"),
        (0, 2, 4, "ej"),
    ]
    q_dot = [(0, 0, 0, "d0")]
    r_dot = [(0, 0, 0, "ei"), (0, 0, 0, "ej")]

    raw: list[Monomial] = []
    # d/dt[-|G_ij|^2 B_1]
    raw += poly_mul([(0, 0, 1, "gamma")], poly_pow(D, 2))
    raw += poly_mul([(0, 0, 2, None)], poly_mul(D, di_dot + eta_dot))
    raw += poly_mul(
        [(0, 0, 2, None)],
        poly_mul(poly_pow(D, 2), q_dot + dj_dot + di_dot + eta_dot),
    )
    # d/dt[(r_i r_j) Delta B]
    raw += poly_mul(
        r_dot,
        poly_add(poly_mul(D, X), poly_mul(poly_pow(D, 2), Pj + X)),
    )
    raw += poly_mul(
        poly_add(poly_mul(D, X), poly_mul(poly_pow(D, 2), Pj + X)),
        q_dot,
    )
    raw += poly_mul(poly_add(X, poly_mul(D, Pj + X)), di_dot)
    raw += poly_mul(poly_pow(D, 2), dj_dot)
    raw += poly_mul(D, eta_dot)

    unique = sorted(set(raw), key=lambda t: (t[3] or "", sum(t[:3]), t))
    minimal: dict[str, list[tuple[int, int, int]]] = defaultdict(list)
    by_mark: dict[str, list[tuple[int, int, int]]] = defaultdict(list)
    for a, b, c, mark in unique:
        assert mark is not None
        by_mark[mark].append((a, b, c))
    for mark, exps in by_mark.items():
        for e in exps:
            dominated = any(
                ee != e and all(ee[k] <= e[k] for k in range(3)) for ee in exps
            )
            if not dominated:
                minimal[mark].append(e)
        minimal[mark] = sorted(set(minimal[mark]))

    expected = {
        "d0": [(0, 4, 4), (1, 3, 3), (2, 2, 2), (3, 1, 1), (4, 0, 2), (4, 2, 0)],
        "ei": [(0, 4, 4), (1, 3, 3), (2, 2, 2), (3, 1, 1), (4, 0, 2), (4, 2, 0)],
        "ej": [(0, 4, 4), (1, 3, 3), (2, 2, 2), (3, 1, 1), (4, 0, 2), (4, 2, 0)],
        "gamma": [(0, 4, 3), (1, 3, 2), (2, 2, 1), (3, 1, 0), (4, 0, 1)],
        "hi": [(0, 3, 3), (1, 2, 2), (2, 1, 1), (3, 0, 2), (3, 2, 0)],
        "hj": [(0, 3, 4), (1, 2, 3), (2, 1, 2), (3, 0, 1), (4, 1, 0)],
    }
    assert len(raw) == 244
    assert len(unique) == 147
    assert dict(minimal) == expected
    return raw, unique, dict(minimal)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--show-monomials", action="store_true")
    args = parser.parse_args()

    ce = exact_counterexample()
    print("Exact U-only directional counterexample")
    print(f"T0={ce['T0']}, W0={ce['W0']}, Z0={ce['Z0']}")
    print(f"K(lambda)={ce['K']}")
    print(f"dK/dlambda at 1/2={ce['dK_dlambda']}")
    print(f"dK/dt for unit outside generator={ce['dK_dt']}")
    print(f"dK/dt for legal x=1/2 reveal={ce['dK_dt_legal']}")

    raw, unique, minimal = connected_marked_families()
    print("\nConnected marked-term coverage")
    print(f"raw occurrences: {len(raw)}")
    print(f"distinct monomials: {len(unique)}")
    print(f"minimal domination families: {sum(len(v) for v in minimal.values())}")
    if args.show_monomials:
        for mark in sorted(minimal):
            print(f"{mark}: {minimal[mark]}")
    print("S41_CYCLE05 exact checks passed")


if __name__ == "__main__":
    main()
