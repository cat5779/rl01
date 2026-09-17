#!/usr/bin/env python3
"""Finite diagnostics for the proved coefficient inequalities.

These checks are evidence only; the proof is symbolic in S13_Cn_upper_bound.md.
"""
from __future__ import annotations

import math
from dataclasses import dataclass


C = 19 / 20
Z = 1521.0
ZPP = 4_864_000.0
BETA = 2.0 * math.log(761 / 760)
KSTAR = 1600.0 * math.log(2.0) / math.log(761 / 760)


@dataclass(frozen=True)
class Stats:
    theta: float
    dlog: float
    quotient: float


def _logcomb(n: int, r: int) -> float:
    if r < 0 or r > n:
        return float("-inf")
    return math.lgamma(n + 1) - math.lgamma(r + 1) - math.lgamma(n - r + 1)


def _weighted_mean(logweights: list[tuple[int, float]]) -> tuple[float, float]:
    peak = max(v for _, v in logweights)
    weights = [(j, math.exp(v - peak)) for j, v in logweights]
    total = sum(w for _, w in weights)
    mean = sum(j * w for j, w in weights) / total
    logsum = peak + math.log(total)
    return mean, logsum


def stats(k: int, m: int, z: float = Z) -> Stats:
    if not (2 <= m <= k):
        raise ValueError("need 2 <= m <= k")

    z_terms = [
        (j, _logcomb(k, j) + _logcomb(k, m - j) + j * math.log(z))
        for j in range(m + 1)
    ]
    ez, log_zsum = _weighted_mean(z_terms)

    a_terms = [
        (
            j,
            _logcomb(k - 2, j)
            + _logcomb(k - 2, m - 2 - j)
            + j * math.log(z),
        )
        for j in range(max(0, m - k), min(k - 2, m - 2) + 1)
    ]
    ea, log_asum = _weighted_mean(a_terms)

    alpha = m * (m - 1) / (k * (k - 1))
    log_theta = 2 * math.log(z - 1) + log_asum - math.log(alpha) - log_zsum
    theta = math.exp(log_theta)
    dlog = 2 / (z - 1) + (ea - ez) / z
    quotient = dlog / (-log_theta)
    return Stats(theta, dlog, quotient)


def main() -> None:
    derivative_bound = 2 / (Z - 1)
    quotient_bound = 2 / ((Z - 1) * BETA)
    theta_bound = ((Z - 1) / (Z + 1)) ** 2

    worst_q = (-1.0, None)
    for k in [2, 3, 4, 5, 10, 20, 50, 100, 200, 500, 1000]:
        for m in range(2, k + 1):
            s = stats(k, m)
            assert 0 < s.theta <= theta_bound * (1 + 1e-10)
            assert 0 <= s.dlog <= derivative_bound * (1 + 1e-8)
            assert 0 <= s.quotient <= quotient_bound * (1 + 1e-8)
            if s.quotient > worst_q[0]:
                worst_q = (s.quotient, (k, m, s))

    print(f"z={Z:g}")
    print(f"z''={ZPP:g}")
    print(f"beta={BETA:.16g}")
    print(f"K_*={KSTAR:.16g}")
    print(f"theta upper={theta_bound:.16g}")
    print(f"dlog upper={derivative_bound:.16g}")
    print(f"quotient upper={quotient_bound:.16g}")
    print(f"largest sampled quotient={worst_q[0]:.16g} at {worst_q[1][:2]}")


if __name__ == "__main__":
    main()
