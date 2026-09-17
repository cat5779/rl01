#!/usr/bin/env python3
"""Exact rational checks for the balanced-midpoint adjacent-layer identity.

No floating arithmetic is used for the asserted identities.  Logarithmic
expressions are compared after reducing log(rational) to rational coefficients
of log(prime).
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict
import json, math, sys


def subsets(n: int, k: int | None = None):
    for s in range(1 << n):
        if k is None or s.bit_count() == k:
            yield s


def factor_integer(x: int) -> dict[int, int]:
    x = abs(x)
    out: dict[int, int] = {}
    p = 2
    while p * p <= x:
        while x % p == 0:
            out[p] = out.get(p, 0) + 1
            x //= p
        p += 1 if p == 2 else 2
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def log_fraction_vector(x: F) -> dict[int, int]:
    assert x > 0
    out: dict[int, int] = defaultdict(int)
    for p, e in factor_integer(x.numerator).items():
        out[p] += e
    for p, e in factor_integer(x.denominator).items():
        out[p] -= e
    return dict(out)


def add_log_term(dst: dict[int, F], coeff: F, x: F) -> None:
    for p, e in log_fraction_vector(x).items():
        dst[p] = dst.get(p, F(0)) + coeff * e
        if dst[p] == 0:
            del dst[p]


def channel_jets(mu: dict[int, F], n: int, a: F, c: F):
    p0 = [F(0) for _ in range(1 << n)]
    p1 = [F(0) for _ in range(1 << n)]
    p2 = [F(0) for _ in range(1 << n)]
    for A, mass_mu in mu.items():
        for S in range(1 << n):
            atom = mass_mu
            score = F(0)
            squares = F(0)
            for i in range(n):
                x = (A >> i) & 1
                y = (S >> i) & 1
                prob = a + c * x
                f = prob if y else 1 - prob
                sg = F(1, 1) / prob if y else -F(1, 1) / (1 - prob)
                atom *= f
                score += sg
                squares += sg * sg
            p0[S] += atom
            p1[S] += atom * score
            p2[S] += atom * (score * score - squares)
    return p0, p1, p2


def fourier_P42_mu() -> dict[int, F]:
    # Genuine first-two-column Fourier projection P_{4,2}.
    # Adjacent pairs have determinant 1/8; opposite pairs 1/4.
    out: dict[int, F] = {}
    for i, j in combinations(range(4), 2):
        d = min((i - j) % 4, (j - i) % 4)
        out[(1 << i) | (1 << j)] = F(1, 4) if d == 2 else F(1, 8)
    assert sum(out.values(), F(0)) == 1
    return out


def uniform_mu(n: int, k: int) -> dict[int, F]:
    ids = list(subsets(n, k))
    return {s: F(1, len(ids)) for s in ids}


def check_case(mu: dict[int, F], n: int, k: int, c: F):
    assert n == 2 * k
    a = (1 - c) / 2
    v = (1 - c * c) / 4
    p0, p1, p2 = channel_jets(mu, n, a, c)
    q0, q1, q2 = channel_jets(uniform_mu(n, k), n, a, c)
    assert sum(p0, F(0)) == 1 and sum(p1, F(0)) == 0 and sum(p2, F(0)) == 0
    assert sum(q0, F(0)) == 1 and sum(q1, F(0)) == 0 and sum(q2, F(0)) == 0
    # Common score at the midpoint.
    common_score = []
    for s in range(1 << n):
        assert p1[s] / p0[s] == q1[s] / q0[s]
        common_score.append(p1[s] / p0[s])
        assert common_score[-1] == F(s.bit_count() - k, 1) / v

    pi = [sum((p0[s] for s in subsets(n, l)), F(0)) for l in range(n + 1)]
    pi1 = [sum((p1[s] for s in subsets(n, l)), F(0)) for l in range(n + 1)]
    pi2 = [sum((p2[s] for s in subsets(n, l)), F(0)) for l in range(n + 1)]
    for l in range(n + 1):
        assert pi[l] == sum((q0[s] for s in subsets(n, l)), F(0))
        assert pi1[l] == sum((q1[s] for s in subsets(n, l)), F(0))
        assert pi2[l] == sum((q2[s] for s in subsets(n, l)), F(0))
        left = v * v * pi2[l]
        pm = pi[l - 1] if l else F(0)
        pp = pi[l + 1] if l < n else F(0)
        right = pi[l] * ((l - k) ** 2 - n * v) + v * (
            n * pi[l] - (n - l + 1) * pm - (l + 1) * pp
        )
        assert left == right

    r = [p0[s] / q0[s] for s in range(1 << n)]
    direct: dict[int, F] = {}
    rhs: dict[int, F] = {}
    # v^2 D'' = sum v^2 p'' log r because the p/q scores coincide.
    for s in range(1 << n):
        add_log_term(direct, v * v * p2[s], r[s])
        l = s.bit_count()
        add_log_term(rhs, p0[s] * ((l - k) ** 2 - n * v), r[s])
    # Compatible actual adjacent-layer production.
    for s in range(1 << n):
        for i in range(n):
            if not ((s >> i) & 1):
                t = s | (1 << i)
                coeff = v * (p0[t] - p0[s])
                add_log_term(rhs, coeff, r[t])
                add_log_term(rhs, -coeff, r[s])
    assert direct == rhs

    # Direct full-entropy midpoint Hessian equals the all-square conditional
    # log-odds formula.  The non-logarithmic Fisher term is exactly -n/v.
    h_direct: dict[int, F] = {}
    h_faces: dict[int, F] = {}
    for s in range(1 << n):
        add_log_term(h_direct, -p2[s], p0[s])
    fisher = sum((p1[s] * p1[s] / p0[s] for s in range(1 << n)), F(0))
    assert fisher == F(n, 1) / v
    for i in range(n):
        for j in range(i + 1, n):
            other = [h for h in range(n) if h not in (i, j)]
            for zbits in range(1 << (n - 2)):
                base = 0
                for hpos, h in enumerate(other):
                    if (zbits >> hpos) & 1:
                        base |= 1 << h
                s00 = base
                s10 = base | (1 << i)
                s01 = base | (1 << j)
                s11 = base | (1 << i) | (1 << j)
                marginal = p0[s00] + p0[s10] + p0[s01] + p0[s11]
                add_log_term(h_faces, -2 * marginal, p0[s00])
                add_log_term(h_faces,  2 * marginal, p0[s10])
                add_log_term(h_faces,  2 * marginal, p0[s01])
                add_log_term(h_faces, -2 * marginal, p0[s11])
    assert h_direct == h_faces

    # Boundary Jeffreys decomposition is exact.
    edge_form: dict[int, F] = {}
    edge_kl_form: dict[int, F] = {}
    for l in range(n):
        aa = F(l + 1) * pi[l + 1]
        bb = F(n - l) * pi[l]
        for s in subsets(n, l):
            for i in range(n):
                if not ((s >> i) & 1):
                    t = s | (1 << i)
                    # raw edge form
                    add_log_term(edge_form, p0[t] - p0[s], r[t] / r[s])
                    # a D(A||B)+b D(B||A), atom by atom
                    Aedge = p0[t] / aa
                    Bedge = p0[s] / bb
                    add_log_term(edge_kl_form, p0[t], Aedge / Bedge)
                    add_log_term(edge_kl_form, p0[s], Bedge / Aedge)
    assert edge_form == edge_kl_form

    # Exact obstruction to a convex upper/lower identity mixture at l=0.
    # Feasibility would require m^2 <= 3 n v; for n=2m>=4 and v<=1/4 this fails.
    m = k
    convex_cancel_obstruction = F(m * m) - 3 * n * v
    assert convex_cancel_obstruction > 0

    # Decimal values are diagnostics only.
    def eval_log_form(form: dict[int, F]) -> float:
        return sum(float(c0) * math.log(p) for p, c0 in form.items())

    return {
        "n": n,
        "k": k,
        "c": str(c),
        "a_mid": str(a),
        "v": str(v),
        "prime_log_coefficients": {str(p): str(x) for p, x in sorted(direct.items())},
        "full_entropy_face_log_coefficients": {str(p): str(x) for p, x in sorted(h_faces.items())},
        "full_entropy_fisher_exact": str(fisher),
        "scaled_D_second_float_diagnostic": eval_log_form(direct),
        "D_second_float_diagnostic": eval_log_form(direct) / float(v * v),
        "convex_cancel_obstruction_exact": str(convex_cancel_obstruction),
        "all_exact_assertions_passed": True,
    }


def main() -> int:
    out = {
        "description": "Exact balanced-midpoint identity checks; floating fields are explicitly diagnostic.",
        "P_4_2_c_19_20": check_case(fourier_P42_mu(), 4, 2, F(19, 20)),
        "non_dpp_rational_mu": check_case(
            {
                0b0011: F(1, 20), 0b0101: F(2, 20), 0b1001: F(3, 20),
                0b0110: F(4, 20), 0b1010: F(5, 20), 0b1100: F(5, 20),
            }, 4, 2, F(19, 20)
        ),
    }
    path = sys.argv[1] if len(sys.argv) > 1 else "exact_midpoint.json"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
