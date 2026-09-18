"""Quantitative comparison of the old and refined localization costs at c=37/40."""

from __future__ import annotations

from fractions import Fraction as F
import math


C = F(37, 40)
A = F(3, 80)
BETA = A * (A + C)
KAPPA = C * C / (4 * BETA)
GAMMA_RO = (3 * KAPPA - 1) / (BETA * BETA)


def ell(x: float) -> float:
    return ((1 + x) * math.log1p(x) - x) / x


def number_variance(m: int) -> float:
    return m / 4 - (2 / math.pi**2) * sum(
        (m - r) / r**2 for r in range(1, m, 2)
    )


def harmonic(m: int) -> float:
    return sum(1 / k for k in range(1, m + 1))


def constants() -> tuple[float, float, float, float]:
    c = float(C)
    beta = float(BETA)
    kappa = float(KAPPA)
    c_pair = c * c * ell(kappa) / (beta * beta)
    observation = float(GAMMA_RO * C**4)
    c_star = min(
        3 * c**4 / (16 * float(A) ** 8),
        3 * c * c * max(1.0, math.log(((float(A) + c) * (1 - float(A))) / float(A) ** 2))
        / (2 * beta * beta),
    )
    a_ro = float(F(9, 16) * C * C * GAMMA_RO)
    return c_pair, observation, c_star, a_ro


def refined_cost(m: int, ratio: float) -> float:
    c_pair, observation, _, _ = constants()
    variance = number_variance(m)
    spatial = 9 / 16 * (1 + 1 / ratio)
    return c_pair * variance / m + observation * min(variance, spatial) / m


def s18_cost(m: int, ratio: float) -> float:
    _, _, c_star, a_ro = constants()
    return c_star * harmonic(m) / m + a_ro * (1 + 1 / ratio) / m


def first_below_one(cost, ratio: float) -> int:
    lo, hi = 1, 2
    while cost(hi, ratio) >= 1:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if cost(mid, ratio) < 1:
            hi = mid
        else:
            lo = mid
    assert cost(hi, ratio) < 1 <= cost(hi - 1, ratio)
    return hi


def main() -> None:
    c_pair, observation, c_star, a_ro = constants()
    assert A == (1 - C) / 2
    assert BETA == F(231, 6400)
    assert KAPPA == F(1369, 231)
    print(f"a={float(A):.15g} c={float(C):.15g} beta={float(BETA):.15g}")
    print(f"kappa={float(KAPPA):.15g} Gamma_ro={float(GAMMA_RO):.15g}")
    print(f"C_pair={c_pair:.15g} Gamma_ro_c4={observation:.15g}")
    print(f"C_star={c_star:.15g} A_ro={a_ro:.15g}")
    for m in (1_000, 2_000, 5_000, 10_000, 100_000):
        print(
            f"m={m} L/m=16 refined={refined_cost(m, 16):.12g} "
            f"S18={s18_cost(m, 16):.12g}"
        )
    new_threshold = first_below_one(refined_cost, 16)
    old_threshold = first_below_one(s18_cost, 16)
    print(
        f"using certified W<=-1 and L/m=16: refined closes at m={new_threshold}, "
        f"S18 closes at m={old_threshold}"
    )
    print(f"window-scale improvement={old_threshold/new_threshold:.12g}x")
    print(
        f"at m=10000 the localized refined modulus is at least "
        f"{1-refined_cost(10_000,16):.12g}, while the direct midpoint "
        "two-budget certificate gives modulus 1"
    )


if __name__ == "__main__":
    main()
