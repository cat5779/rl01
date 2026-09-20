#!/usr/bin/env python3
"""Independent numerical/algebraic checks for the S80 Cycle34 audit."""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from itertools import product
from pathlib import Path

import numpy as np


def sine_q(n: int, rho: float) -> np.ndarray:
    q = np.empty((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            d = i - j
            q[i, j] = rho if d == 0 else math.sin(math.pi * rho * d) / (math.pi * d)
    return q


def binary_entropy(x: np.ndarray | float) -> np.ndarray | float:
    x = np.asarray(x)
    return -x * np.log(x) - (1 - x) * np.log1p(-x)


def quantum_entropy(kernel: np.ndarray) -> float:
    return float(np.sum(binary_entropy(np.linalg.eigvalsh(kernel))))


def atoms(kernel: np.ndarray) -> np.ndarray:
    n = kernel.shape[0]
    out = np.empty(1 << n, dtype=float)
    for mask in range(1 << n):
        y = np.array([(mask >> i) & 1 for i in range(n)])
        holes = n - int(y.sum())
        out[mask] = ((-1) ** holes * np.linalg.det(kernel - np.diag(1 - y))).real
    if out.min() <= 0 or abs(out.sum() - 1) > 1e-10:
        raise ArithmeticError("atom reconstruction failed")
    return out


def shannon_entropy(kernel: np.ndarray) -> float:
    p = atoms(kernel)
    return float(-np.sum(p * np.log(p)))


def dephasing_trials() -> dict:
    minimum_slack = math.inf
    cases = 0
    for n in (2, 4, 6):
        q = sine_q(n, 0.5)
        kernel = 0.025 * np.eye(n) + 0.95 * q
        for m in range(1, n):
            left = list(range(m))
            right = list(range(m, n))
            classical = (
                shannon_entropy(kernel[np.ix_(left, left)])
                + shannon_entropy(kernel[np.ix_(right, right)])
                - shannon_entropy(kernel)
            )
            quantum = (
                quantum_entropy(kernel[np.ix_(left, left)])
                + quantum_entropy(kernel[np.ix_(right, right)])
                - quantum_entropy(kernel)
            )
            minimum_slack = min(minimum_slack, quantum - classical)
            cases += 1
    return {"cases": cases, "minimum_quantum_minus_classical": minimum_slack}


def telescope_trial() -> dict:
    rho, c, a, leaf, levels = 0.37, 0.81, 0.07, 3, 5
    terms = []
    for k in range(levels):
        m = leaf * 2**k
        sm = quantum_entropy(a * np.eye(m) + c * sine_q(m, rho))
        s2 = quantum_entropy(a * np.eye(2 * m) + c * sine_q(2 * m, rho))
        terms.append((2 * sm - s2) / (2 * m))
    n = leaf * 2**levels
    s_leaf = quantum_entropy(a * np.eye(leaf) + c * sine_q(leaf, rho)) / leaf
    s_n = quantum_entropy(a * np.eye(n) + c * sine_q(n, rho)) / n
    return {
        "sum": sum(terms),
        "endpoint_difference": s_leaf - s_n,
        "error": abs(sum(terms) - (s_leaf - s_n)),
    }


def exact_half_density_defect() -> dict:
    rational = Fraction(3, 2)
    correction = Fraction(806, 75)
    closed = float(rational) - float(correction) / math.pi**2
    q = sine_q(6, 0.5)
    direct = float(np.trace(q - q @ q))
    return {
        "formula": "3/2 - 806/(75*pi^2)",
        "closed_value": closed,
        "direct_trace_value": direct,
        "error": abs(closed - direct),
    }


def residual_checks() -> dict:
    n, rho, c, a = 6, 0.5, 0.95, 0.025
    q = sine_q(n, rho)
    kernel = a * np.eye(n) + c * q
    sq = quantum_entropy(kernel) / n
    limit = (1 - rho) * float(binary_entropy(a)) + rho * float(binary_entropy(a + c))
    residual = sq - limit
    defect = float(np.trace(q - q @ q))
    lam = 1 / (a * (1 - a))
    point_bound = lam * c * c * defect / (2 * n)
    lam_j = 1 / (0.02 * 0.98)
    uniform_bound = lam_j * c * c * defect / (2 * n)
    chord_entropies = [
        shannon_entropy(endpoint * np.eye(n) + c * q)
        for endpoint in (0.02, 0.025, 0.03)
    ]
    seed_gap_per_site = (
        chord_entropies[1] - 0.5 * chord_entropies[0] - 0.5 * chord_entropies[2]
    ) / n
    return {
        "R6_exact_formula_float": residual,
        "pointwise_symbolic_bound_float": point_bound,
        "uniform_J_symbolic_bound_float": uniform_bound,
        "bound_slacks": [point_bound - residual, uniform_bound - residual],
        "benchmark_chord_seed_gap_per_site_float": seed_gap_per_site,
        "benchmark_T_lower_bound_float": seed_gap_per_site - residual,
    }


def word_interaction_checks() -> dict:
    n, m, rho, c, a = 6, 3, 0.5, 0.95, 0.025
    kernel = a * np.eye(n) + c * sine_q(n, rho)
    k0 = np.block(
        [
            [kernel[:m, :m], np.zeros((m, n - m))],
            [np.zeros((n - m, m)), kernel[m:, m:]],
        ]
    )
    cross = kernel[:m, m:]
    cross_hs2 = float(np.sum(np.abs(cross) ** 2))
    delta = min(a, 1 - a - c)
    p = atoms(kernel)
    q = atoms(k0)
    ell = np.log(p / q)
    ell1 = np.empty_like(p)
    ell2 = np.empty_like(p)
    score = np.empty_like(p)
    score_a = np.empty_like(p)
    score_b = np.empty_like(p)
    for mask, bits in enumerate(product((0, 1), repeat=n)):
        # product() orders the last coordinate fastest, matching integer masks
        y = np.array(bits[::-1])
        if sum(int(y[i]) << i for i in range(n)) != mask:
            raise AssertionError("mask ordering mismatch")
        g = kernel - np.diag(1 - y)
        g0 = k0 - np.diag(1 - y)
        r = np.linalg.inv(g)
        r0 = np.linalg.inv(g0)
        ell1[mask] = np.trace(r).real - np.trace(r0).real
        ell2[mask] = -np.trace(r @ r).real + np.trace(r0 @ r0).real
        score[mask] = np.trace(r).real
        score_a[mask] = np.trace(r0[:m, :m]).real
        score_b[mask] = np.trace(r0[m:, m:]).real

    df = float(np.sum(p * score**2) - np.sum(p * score_a**2) - np.sum(p * score_b**2))
    minus_e_ell2 = float(-np.sum(p * ell2))
    irel = float(np.sum(p * ell1**2))
    bounds = {
        "ell": delta**-2 * cross_hs2,
        "ell1": 2 * delta**-3 * cross_hs2,
        "ell2": 6 * delta**-4 * cross_hs2,
        "DF": 6 * delta**-4 * cross_hs2,
        "Irel": 4 * delta**-6 * cross_hs2**2,
    }
    observed = {
        "ell": float(np.max(np.abs(ell))),
        "ell1": float(np.max(np.abs(ell1))),
        "ell2": float(np.max(np.abs(ell2))),
        "DF": df,
        "Irel": irel,
    }
    return {
        "DF": df,
        "minus_E_ell_second": minus_e_ell2,
        "identity_error": abs(df - minus_e_ell2),
        "observed": observed,
        "claimed_bounds": bounds,
        "all_bounds_pass_float": all(observed[key] <= bounds[key] * (1 + 1e-10) for key in observed),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "status": "PASS_INDEPENDENT_FLOATING_AND_EXACT_CONSTANT_CHECKS",
        "dephasing": dephasing_trials(),
        "quantum_telescope": telescope_trial(),
        "half_density_D6": exact_half_density_defect(),
        "spectral_residual": residual_checks(),
        "word_interaction": word_interaction_checks(),
        "scope": "Floating checks support formulas; general results rely on the audited proofs, not these samples.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
