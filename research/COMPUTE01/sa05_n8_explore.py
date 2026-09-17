"""Exploratory SA05 n=8 curvature calculation.

This script implements the complete 70-state formula from
results/SA05/SA05_HANDOFF.md.  It uses a second-order forward jet, so the
reported curvature is not a finite-difference estimate.  Floating arithmetic
is still exploratory: a separate interval implementation is required before
any sign is labelled FINITE_CERTIFIED.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import log, sqrt


@dataclass(frozen=True)
class Jet2:
    value: float
    first: float = 0.0
    second: float = 0.0

    @staticmethod
    def coerce(other: float | "Jet2") -> "Jet2":
        return other if isinstance(other, Jet2) else Jet2(float(other))

    def __add__(self, other: float | "Jet2") -> "Jet2":
        other = self.coerce(other)
        return Jet2(
            self.value + other.value,
            self.first + other.first,
            self.second + other.second,
        )

    __radd__ = __add__

    def __neg__(self) -> "Jet2":
        return Jet2(-self.value, -self.first, -self.second)

    def __sub__(self, other: float | "Jet2") -> "Jet2":
        return self + (-self.coerce(other))

    def __rsub__(self, other: float | "Jet2") -> "Jet2":
        return self.coerce(other) - self

    def __mul__(self, other: float | "Jet2") -> "Jet2":
        other = self.coerce(other)
        return Jet2(
            self.value * other.value,
            self.first * other.value + self.value * other.first,
            self.second * other.value
            + 2.0 * self.first * other.first
            + self.value * other.second,
        )

    __rmul__ = __mul__

    def reciprocal(self) -> "Jet2":
        if self.value == 0.0:
            raise ZeroDivisionError("jet reciprocal at zero")
        inv = 1.0 / self.value
        return Jet2(
            inv,
            -self.first * inv * inv,
            2.0 * self.first * self.first * inv**3
            - self.second * inv * inv,
        )

    def __truediv__(self, other: float | "Jet2") -> "Jet2":
        return self * self.coerce(other).reciprocal()

    def __rtruediv__(self, other: float | "Jet2") -> "Jet2":
        return self.coerce(other) / self

    def __pow__(self, exponent: float) -> "Jet2":
        if self.value <= 0.0 and exponent != int(exponent):
            raise ValueError("fractional jet power requires positive base")
        value = self.value**exponent
        first = exponent * self.value ** (exponent - 1.0) * self.first
        second = (
            exponent
            * (exponent - 1.0)
            * self.value ** (exponent - 2.0)
            * self.first**2
            + exponent * self.value ** (exponent - 1.0) * self.second
        )
        return Jet2(value, first, second)

    def logarithm(self) -> "Jet2":
        if self.value <= 0.0:
            raise ValueError("jet logarithm requires positive base")
        ratio = self.first / self.value
        return Jet2(log(self.value), ratio, self.second / self.value - ratio**2)


def chord_squared(distance: int) -> float:
    distance %= 8
    distance = min(distance, 8 - distance)
    if distance == 1:
        return 2.0 - sqrt(2.0)
    if distance == 2:
        return 2.0
    if distance == 3:
        return 2.0 + sqrt(2.0)
    if distance == 4:
        return 4.0
    raise ValueError(f"invalid nonzero distance {distance}")


def projection_entry_squared(distance: int) -> float:
    distance %= 8
    distance = min(distance, 8 - distance)
    if distance in (2, 4):
        return 0.0
    if distance == 1:
        return (2.0 + sqrt(2.0)) / 32.0
    if distance == 3:
        return (2.0 - sqrt(2.0)) / 32.0
    raise ValueError(f"invalid nonzero distance {distance}")


def state_data(state: tuple[int, int, int, int]) -> tuple[float, float, float]:
    pair_list = list(combinations(state, 2))
    vandermonde = 1.0
    pair_defect = 0.0
    for left, right in pair_list:
        distance = right - left
        vandermonde *= chord_squared(distance)
        pair_defect += 1.0 / 28.0 - projection_entry_squared(distance)
    r0 = 70.0 * vandermonde / 8.0**4
    v2 = (35.0 / 3.0) * pair_defect
    v4 = r0 - 1.0 - v2
    return r0, v2, v4


STATES = tuple(combinations(range(8), 4))
DATA = tuple(state_data(state) for state in STATES)


def curvature(a_value: float) -> Jet2:
    c = 19.0 / 20.0
    a = Jet2(a_value, 1.0, 0.0)
    xi = a * (1.0 / 20.0 - a) / c
    q2 = 1.0 + 6.0 * xi + 6.0 * xi**2
    q4 = 1.0 + 20.0 * xi + 90.0 * xi**2 + 140.0 * xi**3 + 70.0 * xi**4
    ratio = q2 / q4
    corrected_ratio = ratio ** (10.0 / 7.0)

    epsilon = Jet2(0.0)
    for _, v2, v4 in DATA:
        true_density = 1.0 + ratio * v2 + v4 / q4
        corrected_density = 1.0 + ratio * v2 + corrected_ratio * v4
        epsilon += (
            true_density * true_density.logarithm()
            - corrected_density * corrected_density.logarithm()
        ) / 70.0
    return c**4 * q4 * epsilon


def data_checks() -> dict[str, float]:
    return {
        "state_count": float(len(STATES)),
        "mean_r0_minus_one": sum(row[0] for row in DATA) / 70.0 - 1.0,
        "mean_v2": sum(row[1] for row in DATA) / 70.0,
        "mean_v4": sum(row[2] for row in DATA) / 70.0,
    }


def rational_grid(denominator: int = 20_000) -> list[tuple[Fraction, float]]:
    results: list[tuple[Fraction, float]] = []
    for numerator in range(1, denominator // 20):
        point = Fraction(numerator, denominator)
        results.append((point, curvature(float(point)).second))
    return results


def main() -> None:
    checks = data_checks()
    print("data checks")
    for key, value in checks.items():
        print(f"  {key}: {value:.17g}")

    midpoint = Fraction(1, 40)
    mid_jet = curvature(float(midpoint))
    print("midpoint")
    print(f"  a={midpoint} E={mid_jet.value:.17g} E''={mid_jet.second:.17g}")

    grid = rational_grid()
    most_positive = max(grid, key=lambda item: item[1])
    most_negative = min(grid, key=lambda item: item[1])
    print("grid extrema (EXPLORATORY)")
    print(f"  positive: a={most_positive[0]} E''={most_positive[1]:.17g}")
    print(f"  negative: a={most_negative[0]} E''={most_negative[1]:.17g}")

    sign_changes: list[tuple[Fraction, Fraction]] = []
    for (left_a, left_y), (right_a, right_y) in zip(grid, grid[1:]):
        if left_y == 0.0 or left_y * right_y < 0.0:
            sign_changes.append((left_a, right_a))
    print("sign-change brackets (EXPLORATORY)")
    for left, right in sign_changes:
        print(f"  [{left}, {right}]")


if __name__ == "__main__":
    main()

