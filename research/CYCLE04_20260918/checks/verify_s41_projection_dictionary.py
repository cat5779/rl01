#!/usr/bin/env python3
"""Exact finite checks for the algebra supporting S41 cycle04 sections 4--7 and 9.

The example uses a rational 7-by-7 projection, balanced channel x=3/5
(so s_x=2), exact SymPy arithmetic, every word on a five-site interval,
and every anchor in that interval.  It checks the posterior projection and
Schur dictionary, anchor energy comparison, outside-flow direction, and the
random-anchor conditional-count-variance compression.  It intentionally does
not claim to verify complete-result Lemma 5.1 (partial-export Lemmas 8.1/8.2).
"""

from __future__ import annotations

from itertools import product

import sympy as sp


X = sp.Rational(3, 5)
S_X = sp.Rational(2)  # sqrt((1+x)/(1-x))
N = 7
INTERVAL = [1, 2, 3, 4, 5]
OUTSIDE = [0, 6]


U = sp.Matrix(
    [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 2, 3],
    ]
)
Q = sp.simplify(U * (U.T * U).inv() * U.T)
IDENTITY = sp.eye(N)
K = (1 - X) * IDENTITY / 2 + X * Q


def principal(matrix: sp.Matrix, rows: list[int], cols: list[int] | None = None) -> sp.Matrix:
    if cols is None:
        cols = rows
    return matrix.extract(rows, cols)


def posterior(observations: dict[int, int]) -> sp.Matrix:
    diagonal = [S_X ** observations.get(i, 0) for i in range(N)]
    d = sp.diag(*diagonal)
    weighted = d * U
    return sp.simplify(weighted * (weighted.T * weighted).inv() * weighted.T)


def atom_probability(sites: list[int], signs: tuple[int, ...]) -> sp.Rational:
    z = [(value + 1) // 2 for value in signs]
    matrix = sp.Matrix(principal(K, sites))
    zeros = 0
    for i, bit in enumerate(z):
        if bit == 0:
            matrix[i, i] -= 1
            zeros += 1
    value = sp.simplify((-1 if zeros % 2 else 1) * matrix.det())
    assert value > 0
    return value


def boundary_energy(projection: sp.Matrix, anchor: int) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    t = sp.simplify(sum(projection[k, anchor] ** 2 for k in OUTSIDE))
    w = sp.Rational(0)
    for j in INTERVAL:
        if j == anchor:
            continue
        t_j = sum(projection[k, j] ** 2 for k in OUTSIDE)
        w += projection[j, anchor] ** 2 * t_j
    w = sp.simplify(w)
    return t, w, sp.simplify(t + w)


def check_dictionary() -> None:
    anchor = 3
    sites = [i for i in INTERVAL if i != anchor]
    for signs in product((-1, 1), repeat=len(sites)):
        observations = dict(zip(sites, signs))
        pi = posterior(observations)
        assert sp.simplify(pi * pi - pi) == sp.zeros(N)

        z = [(value + 1) // 2 for value in signs]
        bmat = sp.Matrix(principal(K, sites))
        for i, bit in enumerate(z):
            if bit == 0:
                bmat[i, i] -= 1
        g = sp.simplify(bmat.inv())
        b = principal(X * Q, sites, [anchor])
        v = sp.simplify(g * b)
        q = sp.simplify(K[anchor, anchor] - (b.T * g * b)[0])

        sign_matrix = sp.diag(*signs)
        pi_j = principal(pi, sites)
        expected_g = sp.simplify(
            sp.Rational(2, 1) / (1 - X**2)
            * (sign_matrix - X * sign_matrix * (2 * pi_j - sp.eye(len(sites))) * sign_matrix)
        )
        expected_v = sp.Matrix(
            [
                sp.Rational(2, 1) * X / sp.sqrt(1 - X**2) * signs[k] * pi[site, anchor]
                for k, site in enumerate(sites)
            ]
        )
        expected_q = sp.simplify((1 - X) / 2 + X * pi[anchor, anchor])
        assert sp.simplify(g - expected_g) == sp.zeros(len(sites))
        assert sp.simplify(v - expected_v) == sp.zeros(len(sites), 1)
        assert sp.simplify(q - expected_q) == 0


def check_anchor_and_outside_flow() -> None:
    anchor = 3
    sites = [i for i in INTERVAL if i != anchor]
    h = sp.Rational(2, 5)
    hmat = sp.diag(sp.Rational(1, 3), 0, 0, 0, 0, 0, -h)
    for signs in product((-1, 1), repeat=len(sites)):
        observations = dict(zip(sites, signs))
        minus = posterior(observations)
        _, _, u_minus = boundary_energy(minus, anchor)

        direction = sp.simplify((IDENTITY - minus) * hmat * minus + minus * hmat * (IDENTITY - minus))
        for i in INTERVAL:
            derivative_norm_sq = sp.simplify((direction[:, i].T * direction[:, i])[0])
            t_i = sp.simplify(sum(minus[k, i] ** 2 for k in OUTSIDE))
            assert sp.simplify(h**2 * t_i - derivative_norm_sq) >= 0

        for anchor_sign in (-1, 1):
            plus = posterior({**observations, anchor: anchor_sign})
            _, _, u_plus = boundary_energy(plus, anchor)
            assert sp.simplify(S_X**4 * u_plus - u_minus) >= 0


def check_random_anchor_average() -> None:
    prior_variance = sp.simplify(
        sp.trace(principal(Q, INTERVAL) * (sp.eye(len(INTERVAL)) - principal(Q, INTERVAL)))
    )

    expected_full_u_sum = sp.Rational(0)
    expected_conditional_variance = sp.Rational(0)
    for signs in product((-1, 1), repeat=len(INTERVAL)):
        probability = atom_probability(INTERVAL, signs)
        pi = posterior(dict(zip(INTERVAL, signs)))
        conditional_variance = sp.simplify(
            sum(sum(pi[k, i] ** 2 for k in OUTSIDE) for i in INTERVAL)
        )
        u_sum = sp.simplify(sum(boundary_energy(pi, anchor)[2] for anchor in INTERVAL))
        assert sp.simplify(2 * conditional_variance - u_sum) >= 0
        expected_full_u_sum += probability * u_sum
        expected_conditional_variance += probability * conditional_variance

    expected_full_u_sum = sp.simplify(expected_full_u_sum)
    expected_conditional_variance = sp.simplify(expected_conditional_variance)
    assert sp.simplify(prior_variance - expected_conditional_variance) >= 0
    assert sp.simplify(2 * prior_variance - expected_full_u_sum) >= 0

    expected_minus_average = sp.Rational(0)
    for anchor in INTERVAL:
        sites = [i for i in INTERVAL if i != anchor]
        for signs in product((-1, 1), repeat=len(sites)):
            probability = atom_probability(sites, signs)
            pi = posterior(dict(zip(sites, signs)))
            expected_minus_average += probability * boundary_energy(pi, anchor)[2] / len(INTERVAL)

    expected_minus_average = sp.simplify(expected_minus_average)
    assert sp.simplify(2 * S_X**4 * prior_variance / len(INTERVAL) - expected_minus_average) >= 0
    print(f"prior_count_variance={prior_variance} ~= {sp.N(prior_variance, 16)}")
    print(f"expected_conditional_variance~={sp.N(expected_conditional_variance, 16)}")
    print(f"expected_full_U_average~={sp.N(expected_full_u_sum / len(INTERVAL), 16)}")
    print(f"expected_minus_U_average~={sp.N(expected_minus_average, 16)}")
    theorem_bound = 2 * S_X**4 * prior_variance / len(INTERVAL)
    print(f"theorem_bound={theorem_bound} ~= {sp.N(theorem_bound, 16)}")


def main() -> None:
    assert sp.simplify(Q * Q - Q) == sp.zeros(N)
    check_dictionary()
    check_anchor_and_outside_flow()
    check_random_anchor_average()
    print("S41 projection/Schur/anchor/count-variance finite checks: PASS")
    print("scope excludes complete-result Lemma 5.1 (partial-export Lemmas 8.1/8.2)")


if __name__ == "__main__":
    main()
