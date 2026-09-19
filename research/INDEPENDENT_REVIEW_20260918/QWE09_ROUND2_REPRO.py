#!/usr/bin/env python3
"""Independent reproduction of the exploratory QWE09 round-2 claims.

This program does not import the author's first-round checker and does not use
any retained round-2 server state.  It reconstructs the finite DPP atoms and
the complete/mixed logarithmic potentials directly from their definitions.
"""

from __future__ import annotations

import json
import math

import numpy as np


A = 1.0 / 40.0
C = 19.0 / 20.0


def sine_projection(n: int) -> np.ndarray:
    q = np.empty((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            d = i - j
            q[i, j] = 0.5 if d == 0 else math.sin(math.pi * d / 2.0) / (math.pi * d)
    return q


def pair_term(g: np.ndarray, i: int, j: int) -> float:
    h = float(g[i, j] * g[j, i])
    if abs(h) < 1.0e-28:
        return 0.0
    v = float(g[i, i] * g[j, j])
    argument = 1.0 - h / v
    if argument <= 0.0:
        raise ArithmeticError((i, j, h, v, argument))
    return h + (v - h) * math.log(argument)


def complete_potential(g: np.ndarray) -> float:
    value = float(np.sum(np.diag(g) ** 2))
    for i in range(len(g)):
        for j in range(len(g)):
            if i != j:
                value += pair_term(g, i, j)
    return value


def word(bits: int, n: int) -> np.ndarray:
    return np.array([(bits >> i) & 1 for i in range(n)], dtype=float)


def toeplitz_word_scan(n: int, a: float = A) -> dict[str, object]:
    k = a * np.eye(n) + C * sine_projection(n)
    values: list[tuple[float, str]] = []
    for bits in range(1 << n):
        y = word(bits, n)
        masked = k - np.diag(1.0 - y)
        value = complete_potential(np.linalg.inv(masked))
        values.append((value, "".join(str(int(x)) for x in y)))
    values.sort()
    negatives = [(value, y) for value, y in values if value < 0.0]
    return {
        "a": a,
        "n": n,
        "minimum": values[0][0],
        "minimum_word_site_order": values[0][1],
        "negative_count": len(negatives),
        "largest_negative": negatives[-1][0] if negatives else None,
        "smallest_nonnegative": values[len(negatives)][0],
        "negative_words": [y for _, y in negatives],
    }


def bipartite_projection(u: np.ndarray) -> np.ndarray:
    m = len(u)
    return 0.5 * np.block([[np.eye(m), u], [u.T, np.eye(m)]])


def bipartite_curvatures(u: np.ndarray) -> dict[str, object]:
    m = len(u)
    n = 2 * m
    q = bipartite_projection(u)
    k = A * np.eye(n) + C * q
    pair_contributions = np.zeros((m, m), dtype=float)
    expected_phi = 0.0
    expected_chi = 0.0
    probability_sum = 0.0

    for bits in range(1 << n):
        y = word(bits, n)
        masked = k - np.diag(1.0 - y)
        probability = ((-1.0) ** (n - int(np.sum(y)))) * float(np.linalg.det(masked))
        g = np.linalg.inv(masked)
        probability_sum += probability
        expected_phi += probability * complete_potential(g)

        chi = 0.0
        for i in range(m):
            for j in range(m):
                term = pair_term(g, i, m + j)
                chi += term
                pair_contributions[i, j] -= probability * term
        expected_chi += probability * chi

    return {
        "common_curvature": -expected_phi,
        "aggregate_mixed_curvature": -expected_chi,
        "pair_mixed_curvatures": pair_contributions.tolist(),
        "probability_sum": probability_sum,
        "kernel_eigenvalues": np.linalg.eigvalsh(q).tolist(),
    }


def random_orthogonal(rng: np.random.Generator, m: int) -> np.ndarray:
    raw = rng.normal(size=(m, m))
    q, r = np.linalg.qr(raw)
    signs = np.where(np.diag(r) >= 0.0, 1.0, -1.0)
    return q @ np.diag(signs)


def random_probe_summary() -> dict[str, object]:
    rng = np.random.default_rng(20260919)
    common: list[float] = []
    mixed: list[float] = []
    maximum_pairs: list[float] = []
    mass_residuals: list[float] = []

    for index in range(320):
        m = 2 if index < 160 else 3
        if index == 0:
            u = np.zeros((m, m))
        else:
            left = random_orthogonal(rng, m)
            right = random_orthogonal(rng, m)
            singular_values = np.ones(m) if index % 4 == 0 else rng.uniform(0.0, 1.0, m)
            u = left @ np.diag(singular_values) @ right.T
        result = bipartite_curvatures(u)
        common.append(float(result["common_curvature"]))
        mixed.append(float(result["aggregate_mixed_curvature"]))
        maximum_pairs.append(float(np.max(result["pair_mixed_curvatures"])))
        mass_residuals.append(abs(float(result["probability_sum"]) - 1.0))

    return {
        "sample_count": 320,
        "common_curvature_range": [min(common), max(common)],
        "nonnegative_common_count_at_1e-10": sum(x >= -1.0e-10 for x in common),
        "aggregate_mixed_range": [min(mixed), max(mixed)],
        "positive_aggregate_count_at_1e-10": sum(x > 1.0e-10 for x in mixed),
        "maximum_individual_pair": max(maximum_pairs),
        "models_with_positive_pair_at_1e-10": sum(x > 1.0e-10 for x in maximum_pairs),
        "maximum_probability_mass_residual": max(mass_residuals),
    }


def main() -> None:
    word_scans = [toeplitz_word_scan(n) for n in range(2, 15)]
    endpoint_checks = [
        toeplitz_word_scan(n, a)
        for a in (1.0 / 50.0, 3.0 / 100.0)
        for n in (11, 12)
    ]

    # This is a new explicit witness, not a recovered author seed.  Because U
    # is a planar rotation, Q=1/2[[I,U],[U^T,I]] is exactly a rank-two
    # projection in exact real arithmetic.
    theta = 0.0733179141207703
    u = np.array(
        [
            [math.cos(theta), -math.sin(theta)],
            [math.sin(theta), math.cos(theta)],
        ]
    )
    explicit_pair_witness = {
        "theta": theta,
        "u": u.tolist(),
        **bipartite_curvatures(u),
    }

    report = {
        "parameters": {"rho": 0.5, "a": A, "c": C},
        "toeplitz_word_scans": word_scans,
        "toeplitz_endpoint_checks": endpoint_checks,
        "explicit_pair_witness": explicit_pair_witness,
        "independent_random_probe": random_probe_summary(),
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
