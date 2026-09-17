#!/usr/bin/env python3
"""Exploratory binary64 diagnostics for PRO03 Round 2.

This script stays within the corrected law.  It computes:
  * the exact coefficient-defined central clock ratio 2 delta_k / epsilon_k;
  * the fixed-latent birth--death radial entropies at the two central layers.

The calculations are diagnostics, not interval certificates.  The proofs in
ROUND2_RESULT.md do not depend on the numerical table emitted by this script.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import expm_multiply
from scipy.special import gammaln

C = 19.0 / 20.0
Z = 1521  # (p/q)^2 with p=39/40, q=1/40


def coefficient(power: int, degree: int, z: int = Z) -> int:
    """Coefficient of t^degree in (1+t)^power (1+z t)^power."""
    if degree < 0 or degree > 2 * power:
        return 0
    lo = max(0, degree - power)
    hi = min(power, degree)
    return sum(
        math.comb(power, degree - r) * math.comb(power, r) * (z**r)
        for r in range(lo, hi + 1)
    )


def theta(k: int, layer: int) -> float:
    """The prescribed coefficient multiplier theta_layer, evaluated stably."""
    if not (2 <= layer <= k):
        raise ValueError("theta is used only for 2 <= layer <= k")
    num = coefficient(k - 2, layer - 2)
    den = coefficient(k, layer)
    alpha = layer * (layer - 1) / (k * (k - 1))
    # Convert the exact integer ratio only at the final step.
    return float(((Z - 1) ** 2 * num) / den) / alpha


def corrected_time(n: int, layer: int) -> float:
    return -math.log(theta(n // 2, layer)) / (2.0 * (n - 1))


def stationary_log_probabilities(n: int, layer: int) -> np.ndarray:
    """Log hypergeometric shell probabilities for R=0,...,layer."""
    k = n // 2
    r = np.arange(layer + 1, dtype=float)
    # pi(R)=C(k,layer-R) C(k,R) / C(2k,layer)
    log_pi = (
        gammaln(k + 1)
        - gammaln(layer - r + 1)
        - gammaln(k - layer + r + 1)
        + gammaln(k + 1)
        - gammaln(r + 1)
        - gammaln(k - r + 1)
        - gammaln(n + 1)
        + gammaln(layer + 1)
        + gammaln(n - layer + 1)
    )
    # Remove harmless roundoff in normalization.
    m = float(np.max(log_pi))
    norm = m + math.log(float(np.exp(log_pi - m).sum()))
    return log_pi - norm


def birth_death_generator(n: int, layer: int) -> csr_matrix:
    r"""Generator for R=|S\A| when A is a fixed k-set."""
    k = n // 2
    size = layer + 1
    rows: list[int] = []
    cols: list[int] = []
    data: list[float] = []
    for r in range(size):
        birth = (layer - r) * (k - r)
        death = r * (k - layer + r)
        rows.append(r)
        cols.append(r)
        data.append(float(-(birth + death)))
        if r < layer:
            rows.append(r)
            cols.append(r + 1)
            data.append(float(birth))
        if r > 0:
            rows.append(r)
            cols.append(r - 1)
            data.append(float(death))
    return csr_matrix((data, (rows, cols)), shape=(size, size))


def radial_law(n: int, layer: int, time: float) -> np.ndarray:
    """Row law delta_0 exp(time Q), returned as a probability vector."""
    q = birth_death_generator(n, layer)
    initial = np.zeros(layer + 1, dtype=float)
    initial[0] = 1.0
    law = np.asarray(expm_multiply(time * q.transpose(), initial), dtype=float)
    # Numerical cleanup only; negative mass is at roundoff scale.
    law[np.abs(law) < 1e-15] = 0.0
    law = np.maximum(law, 0.0)
    total = float(law.sum())
    if not math.isfinite(total) or total <= 0.0:
        raise RuntimeError("invalid radial transition law")
    return law / total


def radial_entropy(n: int, layer: int, time: float) -> float:
    law = radial_law(n, layer, time)
    log_pi = stationary_log_probabilities(n, layer)
    mask = law > 0.0
    return float(np.sum(law[mask] * (np.log(law[mask]) - log_pi[mask])))


@dataclass
class Row:
    n: int
    k: int
    theta_k: float
    theta_k_minus_1: float
    s_k: float
    s_k_minus_1: float
    two_delta_over_epsilon: float
    radial_A: float
    radial_E: float
    radial_d: float
    limiting_cost: float


def compute_row(n: int) -> Row:
    if n < 6 or n % 2:
        raise ValueError("n must be even and at least 6")
    k = n // 2
    th_k = theta(k, k)
    th_prev = theta(k, k - 1)
    s_k = corrected_time(n, k)
    s_prev = corrected_time(n, k - 1)
    delta = s_k - s_prev
    epsilon = 1.0 / (k * (k + 1))

    f_k_at_k = radial_entropy(n, k, s_k)
    f_prev_at_k = radial_entropy(n, k - 1, s_k)
    f_prev_at_prev = radial_entropy(n, k - 1, s_prev)
    a_cost = f_k_at_k - f_prev_at_k
    e_cost = f_prev_at_prev - f_prev_at_k

    return Row(
        n=n,
        k=k,
        theta_k=th_k,
        theta_k_minus_1=th_prev,
        s_k=s_k,
        s_k_minus_1=s_prev,
        two_delta_over_epsilon=2.0 * delta / epsilon,
        radial_A=a_cost,
        radial_E=e_cost,
        radial_d=a_cost - e_cost,
        limiting_cost=C * math.log((1.0 + C) / (1.0 - C)),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--n",
        nargs="*",
        type=int,
        default=[20, 40, 60, 100, 200, 500, 1000],
        help="even sizes to evaluate",
    )
    parser.add_argument(
        "--output",
        default="/mnt/data/round2_radial_clock_diagnostics.json",
    )
    args = parser.parse_args()

    rows = [compute_row(n) for n in args.n]
    payload = {
        "status": "EXPLORATORY_BINARY64_NOT_INTERVAL_CERTIFIED",
        "formula_limit": "c*log((1+c)/(1-c))",
        "rows": [asdict(row) for row in rows],
    }
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")

    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
