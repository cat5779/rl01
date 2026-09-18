#!/usr/bin/env python3
"""Independent Arb rebuild of the visible S18 round-2 finite claims.

This deliberately does not use the missing author attachments or the earlier
same-author marginal certificate.  For every output word it differentiates
the signed determinant atom directly:

    p_y(a) = (-1)^(# zeros) det(K(a) - I_{zeros}).

All asserted signs are checked with python-flint Arb ball arithmetic.  The
    six-coordinate Hessian is certified negative definite by an interval LDL^T
    factorization of ``-H - 4.85 I``.  The neighborhood is covered by exact
rational subintervals and each subinterval is evaluated as one Arb ball.
"""

from __future__ import annotations

import argparse
from itertools import product
from time import perf_counter

from flint import arb, arb_mat, ctx, fmpq


ctx.prec = 256
C = arb(19) / 20
A0 = arb(1) / 40


def sine_q(n: int) -> arb_mat:
    q = arb_mat(n, n)
    pi = arb.pi()
    for i in range(n):
        for j in range(n):
            r = i - j
            if r == 0:
                q[i, j] = arb(1) / 2
            elif r % 2 == 0:
                q[i, j] = 0
            else:
                # sin(pi*r/2) is exactly +/-1 for odd integral r.
                q[i, j] = arb(1 if r % 4 == 1 else -1) / (pi * r)
    return q


def atom_data(q: arb_mat, a: arb, bits: tuple[int, ...]):
    n = len(bits)
    m = arb_mat(n, n)
    zeros = 0
    for i in range(n):
        for j in range(n):
            m[i, j] = C * q[i, j] + (a if i == j else 0)
        if bits[i] == 0:
            m[i, i] -= 1
            zeros += 1
    sign = -1 if zeros % 2 else 1
    p = sign * m.det()
    if not p > 0:
        raise ArithmeticError(f"atom positivity not certified: bits={bits}, p={p}")
    g = m.inv()
    diag = [g[i, i] for i in range(n)]
    tr_g = sum(diag, arb(0))
    tr_g2 = sum((g[i, j] * g[j, i] for i in range(n) for j in range(n)), arb(0))
    p1 = p * tr_g
    p2 = p * (tr_g * tr_g - tr_g2)
    return p, p1, p2, g, diag


def entropy_curvature(n: int, a: arb, full_hessian: bool = False):
    q = sine_q(n)
    total_p = arb(0)
    total_p1 = arb(0)
    total_p2 = arb(0)
    hpp = arb(0)
    hess = [[arb(0) for _ in range(n)] for _ in range(n)] if full_hessian else None
    for bits in product((0, 1), repeat=n):
        p, p1, p2, g, diag = atom_data(q, a, bits)
        total_p += p
        total_p1 += p1
        total_p2 += p2
        hpp -= p2 * p.log() + p1 * p1 / p
        if hess is not None:
            logp = p.log()
            for i in range(n):
                # p_{ii}=0 by determinant multi-affinity.
                hess[i][i] -= p * diag[i] * diag[i]
                for j in range(i + 1, n):
                    pij = p * (diag[i] * diag[j] - g[i, j] * g[j, i])
                    hij = -(p * diag[i] * diag[j] + pij * logp)
                    hess[i][j] += hij
                    hess[j][i] += hij
    return total_p, total_p1, total_p2, hpp, hess


def interval_ldlt_positive(a: list[list[arb]]) -> list[arb]:
    """Return positive interval pivots, or fail if positivity is not proved."""
    n = len(a)
    ell = [[arb(0) for _ in range(n)] for _ in range(n)]
    pivots: list[arb] = []
    for k in range(n):
        d = a[k][k] - sum((ell[k][s] * ell[k][s] * pivots[s] for s in range(k)), arb(0))
        if not d > 0:
            raise ArithmeticError(f"LDL pivot {k} not certified positive: {d}")
        pivots.append(d)
        ell[k][k] = 1
        for i in range(k + 1, n):
            numer = a[i][k] - sum(
                (ell[i][s] * ell[k][s] * pivots[s] for s in range(k)), arb(0)
            )
            ell[i][k] = numer / d
    return pivots


def benchmark() -> tuple[arb, arb]:
    t0 = perf_counter()
    p6, p61, p62, h6, hess = entropy_curvature(6, A0, full_hessian=True)
    assert h6 < arb("-49.5655")
    assert hess is not None
    assert hess[0][5] > arb("0.000379092")
    hessian_direction = sum((hess[i][j] for i in range(6) for j in range(6)), arb(0))
    assert (hessian_direction - h6).contains(0)
    shifted_minus_h = [
        [-(hess[i][j]) - (arb("4.85") if i == j else 0) for j in range(6)]
        for i in range(6)
    ]
    pivots = interval_ldlt_positive(shifted_minus_h)
    print("n=6 benchmark: PASS")
    print(f"sum_p={p6}")
    print(f"sum_p1={p61}")
    print(f"sum_p2={p62}")
    print(f"H6pp={h6}")
    print(f"ones_direction_minus_H6pp={hessian_direction - h6}")
    print(f"Hessian_1_6={hess[0][5]}")
    print("lambda_max(Hessian)<-4.85 via interval LDL^T")
    print("LDL_pivots=" + ", ".join(str(x) for x in pivots))
    print(f"n6_seconds={perf_counter() - t0:.3f}")

    t1 = perf_counter()
    p12, p121, p122, h12, _ = entropy_curvature(12, A0)
    assert h12 < arb("-126.1801")
    tc = 2 * h6 - h12
    assert tc > arb("27.0490")
    print("n=12 benchmark and 6->12 interface: PASS")
    print(f"sum_p={p12}")
    print(f"sum_p1={p121}")
    print(f"sum_p2={p122}")
    print(f"H12pp={h12}")
    print(f"TC66pp=2*H6pp-H12pp={tc}")
    print(f"n12_seconds={perf_counter() - t1:.3f}")
    return h6, h12


def neighborhood(parts: int) -> None:
    """Cover [3/200,7/200] by rational Arb balls and prove H6''<0."""
    q = sine_q(6)
    lo = fmpq(3, 200)
    hi = fmpq(7, 200)
    width = (hi - lo) / parts
    worst_upper = None
    worst_index = None
    t0 = perf_counter()
    for k in range(parts):
        left = lo + k * width
        right = left + width
        a = arb((left + right) / 2, (right - left) / 2)
        hpp = arb(0)
        for bits in product((0, 1), repeat=6):
            p, p1, p2, _, _ = atom_data(q, a, bits)
            hpp -= p2 * p.log() + p1 * p1 / p
        if not hpp < arb("-44.9"):
            raise ArithmeticError(
                f"neighborhood cell {k}/{parts} misses Hpp<-44.9: a={a}, Hpp={hpp}"
            )
        upper = hpp.upper()
        if worst_upper is None or upper > worst_upper:
            worst_upper = upper
            worst_index = k
    print("n=6 neighborhood: PASS")
    print(f"cover=[3/200,7/200], parts={parts}")
    print(f"largest_certified_upper={worst_upper}, cell={worst_index}")
    print(f"neighborhood_seconds={perf_counter() - t0:.3f}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parts", type=int, default=512)
    parser.add_argument("--skip-benchmark", action="store_true")
    parser.add_argument("--skip-neighborhood", action="store_true")
    args = parser.parse_args()
    if not args.skip_benchmark:
        benchmark()
    if not args.skip_neighborhood:
        neighborhood(args.parts)


if __name__ == "__main__":
    main()
