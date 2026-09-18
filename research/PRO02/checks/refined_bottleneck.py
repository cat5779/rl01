"""Exact constants and stress checks for the refined PRO02 bottleneck."""

from __future__ import annotations

from fractions import Fraction
import math
import random


C = Fraction(19, 20)
BETA = Fraction(39, 1600)
GAMMA = Fraction(296_960_000, 6_591)


def number_variance(m: int) -> float:
    return m / 4 - (2 / math.pi**2) * sum(
        (m - r) / r**2 for r in range(1, m, 2)
    )


def constants() -> tuple[float, float]:
    c = float(C)
    beta = float(BETA)
    kappa = 361 / 39
    ell = ((1 + kappa) * math.log1p(kappa) - kappa) / kappa
    c_pair = c * c * ell / (beta * beta)
    observation_prefactor = float(GAMMA * C**4)
    return c_pair, observation_prefactor


def stress_reserve() -> None:
    rng = random.Random(20260918)
    c = float(C)
    a = 1 / 40
    worst = 0.0
    for _ in range(100_000):
        r = rng.random()
        row_budget = r * (1 - r)
        s = rng.random() * row_budget
        t = rng.random() * (row_budget - s)
        p = a + c * r
        pq = p * (1 - p)
        drop = s * (1 - c * c * t / pq)
        qv = c * c * s * s / pq
        if qv > c * c * drop + 1e-14:
            raise AssertionError((r, s, t, qv, drop))
        if drop:
            worst = max(worst, qv / drop)
    print(f"random_max_Q_over_drop={worst:.15g}")
    for eps in (1e-1, 1e-2, 1e-4, 1e-8):
        s = (1 - eps) ** 2 / 4
        ratio = 4 * c * c * s
        print(f"sharp_family_eps={eps:.0e} ratio={ratio:.15g}")


def benchmark_table() -> None:
    c_pair, obs_prefactor = constants()
    print(f"C_pair={c_pair:.15g}")
    print(f"Gamma_c4={obs_prefactor:.15g}")
    for m, ratio in ((5_000, 1), (5_000, 16), (10_000, 16), (100_000, 16)):
        variance = number_variance(m)
        spatial = 9 / 16 * (1 + 1 / ratio)
        budget = min(variance, spatial)
        pair = c_pair * variance / m
        observation = obs_prefactor * budget / m
        print(
            f"m={m} L_over_m={ratio} V={variance:.12f} B={budget:.12f} "
            f"pair={pair:.12f} observation={observation:.12f} "
            f"total={pair + observation:.12f}"
        )


def main() -> None:
    assert GAMMA * C**2 * Fraction(9, 16) == Fraction(50_251_200, 2_197)
    assert C**2 * Fraction(50_251_200, 2_197) == Fraction(45_351_708, 2_197)
    stress_reserve()
    benchmark_table()
    print("all_refined_checks_passed=true")


if __name__ == "__main__":
    main()
