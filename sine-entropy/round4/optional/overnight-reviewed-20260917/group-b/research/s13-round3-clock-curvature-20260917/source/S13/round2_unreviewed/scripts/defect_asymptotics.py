#!/usr/bin/env python3
"""Numerical diagnostics for the S13 growing potential-transfer theorem.

The theorem is analytic.  This script evaluates its exact finite-n spectral
formula in floating arithmetic and checks the predicted logarithmic and
midpoint boundary-layer scalings.  It never promotes a decimal sign to proof.
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
from scipy.signal import fftconvolve
from scipy.special import gammaln


def logsumexp(values: np.ndarray) -> float:
    m = float(np.max(values))
    return m + math.log(float(np.exp(values - m).sum()))


def binom_logpmf(n: int, p: float) -> np.ndarray:
    j = np.arange(n + 1, dtype=float)
    return (
        gammaln(n + 1)
        - gammaln(j + 1)
        - gammaln(n - j + 1)
        + j * math.log(p)
        + (n - j) * math.log1p(-p)
    )


def two_binom_pmf(n1: int, p1: float, n2: int, p2: float) -> np.ndarray:
    a = np.exp(binom_logpmf(n1, p1))
    b = np.exp(binom_logpmf(n2, p2))
    out = fftconvolve(a, b)
    out[out < 0] = 0.0
    out /= out.sum()
    return out


def count_pmf(n: int, a: float, c: float) -> np.ndarray:
    k = n // 2
    return two_binom_pmf(k, a + c, k, a)


def direct_layer_multipliers(n: int, l: int, z: float) -> tuple[float, float, float]:
    """Return lambda_1, theta_2, Var(J), using the exact overlap weights."""
    k = n // 2
    if not (2 <= l <= n - 2):
        return 0.0, 0.0, 0.0
    if l > k:
        return direct_layer_multipliers(n, n - l, z)

    js = np.arange(max(0, l - k), min(k, l) + 1, dtype=float)
    logs = (
        gammaln(k + 1)
        - gammaln(js + 1)
        - gammaln(k - js + 1)
        + gammaln(k + 1)
        - gammaln(l - js + 1)
        - gammaln(k - l + js + 1)
        + js * math.log(z)
    )
    log_zpart = logsumexp(logs)
    probs = np.exp(logs - log_zpart)
    mean = float(np.dot(probs, js))
    var = float(np.dot(probs, (js - mean) ** 2))
    lam = (2.0 * mean - l) / l
    theta = lam * lam + (
        4.0 * (n - 1) * var - l * (n - l) * (1.0 - lam * lam)
    ) / (n * l * (l - 1))
    return lam, theta, var


def layer_gap(n: int, l: int, z: float) -> float:
    if not (2 <= l <= n - 2):
        return 0.0
    k = n // 2
    r = min(l, n - l)
    alpha = r * (r - 1) / (k * (k - 1))
    lam, theta, _ = direct_layer_multipliers(n, l, z)
    exponent = 2.0 * (n - 1) / n
    return alpha * (lam**exponent - theta)


def fourier_amplitude(n: int) -> float:
    d = np.arange(1, n, dtype=float)
    s = np.sin(math.pi * d / n)
    phi = np.log(4.0 * s * s)
    kernel_sq = np.zeros(n - 1)
    odd = (d.astype(int) % 2) == 1
    kernel_sq[odd] = 1.0 / (n * n * s[odd] * s[odd])
    pair_difference = 1.0 / (4.0 * (n - 1)) - kernel_sq
    return float((n / 2.0) * np.dot(phi, pair_difference))


def lambda_limit(x: float, z: float) -> float:
    disc = (z + 1.0) ** 2 - 4.0 * x * (1.0 - x) * (z - 1.0) ** 2
    return 2.0 * (1.0 - x) * (z - 1.0) / (z + 1.0 + math.sqrt(disc))


def d_limit(x: float, z: float) -> float:
    lam = lambda_limit(x, z)
    return lam * lam * (
        -2.0 * math.log(lam)
        - (1.0 - lam * lam)
        * (1.0 - 2.0 * x)
        / (1.0 - x * (1.0 + lam * lam))
    )


def C_limit(a: float, c: float) -> float:
    x = min(a + c / 2.0, 1.0 - a - c / 2.0)
    z = 1.0 + c / (a * (1.0 - c - a))
    return x * x * d_limit(x, z)


def T_limit(a: float, c: float) -> float:
    x = min(a + c / 2.0, 1.0 - a - c / 2.0)
    z = 1.0 + c / (a * (1.0 - c - a))
    lam = lambda_limit(x, z)
    return x * (1.0 - x) * d_limit(x, z) / (2.0 * lam * lam)


def average_clock_gap(n: int, a: float, c: float) -> float:
    z = 1.0 + c / (a * (1.0 - c - a))
    exponent = 2.0 * (n - 1) / n
    gaps = np.zeros(n + 1)
    for l in range(2, n - 1):
        lam, theta, _ = direct_layer_multipliers(n, l, z)
        gamma2 = 2.0 * (n - 1) / (l * (n - l))
        gaps[l] = abs(math.log(lam**exponent / theta) / gamma2)
    return float(np.dot(count_pmf(n, a, c), gaps))


def aggregate_multiplier(n: int, a: float, c: float) -> float:
    z = 1.0 + c / (a * (1.0 - c - a))
    gaps = np.array([layer_gap(n, l, z) for l in range(n + 1)])
    return float(np.dot(count_pmf(n, a, c), gaps))


def defect(n: int, a: float, c: float) -> float:
    return fourier_amplitude(n) * aggregate_multiplier(n, a, c)


def midpoint_second_response(n: int, c: float) -> dict[str, float]:
    """Evaluate Delta'' at a_* using exact Bernoulli finite differences.

    The z-derivative contribution is evaluated by a centered floating
    difference.  It is lower order and is reported separately.
    """
    k = n // 2
    a = (1.0 - c) / 2.0
    p = (1.0 + c) / 2.0
    q = (1.0 - c) / 2.0
    z = ((1.0 + c) / (1.0 - c)) ** 2
    gaps = np.array([layer_gap(n, l, z) for l in range(n + 1)])
    second_diff = gaps[2:] - 2.0 * gaps[1:-1] + gaps[:-2]

    hh = two_binom_pmf(k - 2, p, k, q)
    hl = two_binom_pmf(k - 1, p, k - 1, q)
    ll = two_binom_pmf(k, p, k - 2, q)
    parameter_part = 2.0 * (
        math.comb(k, 2) * float(np.dot(hh, second_diff))
        + k * k * float(np.dot(hl, second_diff))
        + math.comb(k, 2) * float(np.dot(ll, second_diff))
    )

    dz = z * 1.0e-5
    gaps_plus = np.array([layer_gap(n, l, z + dz) for l in range(n + 1)])
    gaps_minus = np.array([layer_gap(n, l, z - dz) for l in range(n + 1)])
    gap_z = (gaps_plus - gaps_minus) / (2.0 * dz)
    z_second = 32.0 * c / (1.0 - c) ** 4
    explicit_part = z_second * float(np.dot(count_pmf(n, a, c), gap_z))

    amp = fourier_amplitude(n)
    total_a_second = parameter_part + explicit_part
    delta_second = amp * total_a_second
    predicted = -4.0 * c * c * math.sqrt(2.0 / math.pi) / math.sqrt(1.0 - c * c)
    return {
        "n": n,
        "fourier_amplitude": amp,
        "fourier_amplitude_over_n_log_n": amp / (n * math.log(n)),
        "A_second_parameter_part": parameter_part,
        "A_second_explicit_z_part_floating_difference": explicit_part,
        "Delta_second": delta_second,
        "Delta_second_over_sqrt_n_log_n": delta_second / (math.sqrt(n) * math.log(n)),
        "predicted_limit": predicted,
    }


def kappa_constant() -> float:
    # Equivalent to the exact zeta-derivative formula in proof.md; this
    # truncated positive series is used only as a numerical diagnostic.
    total = 0.0
    for m in range(1, 1_000_000, 2):
        total += math.log(2.0 * math.pi * m) / (m * m)
    return 2.0 * total / (math.pi * math.pi)


def run(output: Path) -> None:
    rows: dict[str, object] = {
        "classification": "floating diagnostics only; proofs are in proof.md",
        "kappa_truncated_odd_series": kappa_constant(),
        "value_scaling": [],
        "midpoint_scaling": [],
        "potential_clock_scaling": [],
    }
    cases = [(0.5, 0.10), (0.95, 0.01), (0.95, 0.02)]
    for c, a in cases:
        case = {"c": c, "a": a, "C_limit": C_limit(a, c), "rows": []}
        for n in (50, 100, 200, 400, 800, 1600):
            multiplier = aggregate_multiplier(n, a, c)
            amp = fourier_amplitude(n)
            value = amp * multiplier
            x = min(a + c / 2.0, 1.0 - a - c / 2.0)
            f_lim = 4.0 * C_limit(a, c)
            case["rows"].append(
                {
                    "n": n,
                    "Delta": value,
                    "Delta_over_log_n": value / math.log(n),
                    "ratio_to_C": value / (math.log(n) * C_limit(a, c)),
                    "V_over_n_log_n": amp / (n * math.log(n)),
                    "nA_over_f_limit": n * multiplier / f_lim,
                }
            )
        rows["value_scaling"].append(case)

    for c in (0.5, 0.95):
        case = {"c": c, "rows": []}
        for n in (50, 100, 200, 400, 800):
            case["rows"].append(midpoint_second_response(n, c))
        rows["midpoint_scaling"].append(case)

    clock_cases = [(0.5, 0.10), (0.95, 0.01), (0.95, 0.025)]
    for c, a in clock_cases:
        case = {"c": c, "a": a, "T_limit": T_limit(a, c), "rows": []}
        for n in (50, 100, 200, 400, 800):
            avg = average_clock_gap(n, a, c)
            case["rows"].append(
                {
                    "n": n,
                    "average_absolute_clock_gap": avg,
                    "ratio_to_T": avg / T_limit(a, c),
                    "hamming_bound_2T": 2.0 * avg,
                }
            )
        rows["potential_clock_scaling"].append(case)

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    run(args.output)


if __name__ == "__main__":
    main()
