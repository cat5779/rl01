"""Rigorous rational-interval certificate for three SA05 n=8 points.

Only Python's integer and Fraction arithmetic is used.  Algebraic quantities
are enclosed by rational bisection; logarithms use the atanh series with its
explicit tail bound after power-of-two range reduction.  The output intervals
therefore do not rely on binary floating-point rounding.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations


BITS = 96


@dataclass(frozen=True)
class Interval:
    low: Fraction
    high: Fraction

    def __post_init__(self) -> None:
        if self.low > self.high:
            raise ValueError("reversed interval")

    @staticmethod
    def point(value: int | Fraction) -> "Interval":
        value = Fraction(value)
        return Interval(value, value)

    @staticmethod
    def coerce(value: int | Fraction | "Interval") -> "Interval":
        return value if isinstance(value, Interval) else Interval.point(value)

    def __add__(self, other: int | Fraction | "Interval") -> "Interval":
        other = self.coerce(other)
        return Interval(self.low + other.low, self.high + other.high)

    __radd__ = __add__

    def __neg__(self) -> "Interval":
        return Interval(-self.high, -self.low)

    def __sub__(self, other: int | Fraction | "Interval") -> "Interval":
        return self + (-self.coerce(other))

    def __rsub__(self, other: int | Fraction | "Interval") -> "Interval":
        return self.coerce(other) - self

    def __mul__(self, other: int | Fraction | "Interval") -> "Interval":
        other = self.coerce(other)
        products = (
            self.low * other.low,
            self.low * other.high,
            self.high * other.low,
            self.high * other.high,
        )
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def reciprocal(self) -> "Interval":
        if self.low <= 0 <= self.high:
            raise ZeroDivisionError("interval contains zero")
        return Interval(Fraction(1, 1) / self.high, Fraction(1, 1) / self.low)

    def __truediv__(self, other: int | Fraction | "Interval") -> "Interval":
        return self * self.coerce(other).reciprocal()

    def __rtruediv__(self, other: int | Fraction | "Interval") -> "Interval":
        return self.coerce(other) / self

    def integer_power(self, exponent: int) -> "Interval":
        if exponent < 0:
            return self.integer_power(-exponent).reciprocal()
        if exponent == 0:
            return Interval.point(1)
        if self.low >= 0:
            return Interval(self.low**exponent, self.high**exponent)
        if self.high <= 0:
            if exponent % 2:
                return Interval(self.low**exponent, self.high**exponent)
            return Interval(self.high**exponent, self.low**exponent)
        if exponent % 2:
            return Interval(self.low**exponent, self.high**exponent)
        return Interval(Fraction(0), max((-self.low) ** exponent, self.high**exponent))


def rational_root_bounds(value: Fraction, degree: int, bits: int = BITS) -> Interval:
    if value <= 0:
        raise ValueError("root input must be positive")
    if degree <= 0:
        raise ValueError("root degree must be positive")
    low = Fraction(0)
    high = max(Fraction(1), value)
    for _ in range(bits):
        middle = (low + high) / 2
        if middle**degree <= value:
            low = middle
        else:
            high = middle
    return Interval(low, high)


def interval_root(value: Interval, degree: int, bits: int = BITS) -> Interval:
    low = rational_root_bounds(value.low, degree, bits).low
    high = rational_root_bounds(value.high, degree, bits).high
    return Interval(low, high)


def positive_rational_power(value: Interval, numerator: int, denominator: int) -> Interval:
    if value.low <= 0:
        raise ValueError("positive rational power requires a positive interval")
    root = interval_root(value, denominator)
    return root.integer_power(numerator)


def atanh_log_unit_bounds(value: Fraction, bits: int = BITS) -> Interval:
    """Enclose log(value) for 1 <= value < 2."""
    if not Fraction(1) <= value < Fraction(2):
        raise ValueError("range-reduced log input must lie in [1, 2)")
    t = (value - 1) / (value + 1)
    if t == 0:
        return Interval.point(0)
    target = Fraction(1, 2**bits)
    term = t
    total = Fraction(0)
    index = 0
    while True:
        total += 2 * term / (2 * index + 1)
        next_power = term * t * t
        tail = 2 * next_power / ((2 * index + 3) * (1 - t * t))
        if tail <= target:
            return Interval(total, total + tail)
        term = next_power
        index += 1


def log_two_bounds(bits: int = BITS) -> Interval:
    t = Fraction(1, 3)
    target = Fraction(1, 2**bits)
    term = t
    total = Fraction(0)
    index = 0
    while True:
        total += 2 * term / (2 * index + 1)
        next_power = term * t * t
        tail = 2 * next_power / ((2 * index + 3) * (1 - t * t))
        if tail <= target:
            return Interval(total, total + tail)
        term = next_power
        index += 1


LOG_TWO = log_two_bounds()


def log_fraction_bounds(value: Fraction, bits: int = BITS) -> Interval:
    if value <= 0:
        raise ValueError("log input must be positive")
    exponent = 0
    reduced = value
    while reduced < 1:
        reduced *= 2
        exponent -= 1
    while reduced >= 2:
        reduced /= 2
        exponent += 1
    return atanh_log_unit_bounds(reduced, bits) + exponent * LOG_TWO


def log_interval(value: Interval, bits: int = BITS) -> Interval:
    low = log_fraction_bounds(value.low, bits).low
    high = log_fraction_bounds(value.high, bits).high
    return Interval(low, high)


@dataclass(frozen=True)
class IntervalJet2:
    value: Interval
    first: Interval
    second: Interval

    @staticmethod
    def constant(value: int | Fraction | Interval) -> "IntervalJet2":
        return IntervalJet2(Interval.coerce(value), Interval.point(0), Interval.point(0))

    @staticmethod
    def coerce(value: int | Fraction | Interval | "IntervalJet2") -> "IntervalJet2":
        return value if isinstance(value, IntervalJet2) else IntervalJet2.constant(value)

    def __add__(self, other: int | Fraction | Interval | "IntervalJet2") -> "IntervalJet2":
        other = self.coerce(other)
        return IntervalJet2(
            self.value + other.value,
            self.first + other.first,
            self.second + other.second,
        )

    __radd__ = __add__

    def __neg__(self) -> "IntervalJet2":
        return IntervalJet2(-self.value, -self.first, -self.second)

    def __sub__(self, other: int | Fraction | Interval | "IntervalJet2") -> "IntervalJet2":
        return self + (-self.coerce(other))

    def __rsub__(self, other: int | Fraction | Interval | "IntervalJet2") -> "IntervalJet2":
        return self.coerce(other) - self

    def __mul__(self, other: int | Fraction | Interval | "IntervalJet2") -> "IntervalJet2":
        other = self.coerce(other)
        return IntervalJet2(
            self.value * other.value,
            self.first * other.value + self.value * other.first,
            self.second * other.value
            + 2 * self.first * other.first
            + self.value * other.second,
        )

    __rmul__ = __mul__

    def reciprocal(self) -> "IntervalJet2":
        inverse = self.value.reciprocal()
        return IntervalJet2(
            inverse,
            -self.first * inverse.integer_power(2),
            2 * self.first.integer_power(2) * inverse.integer_power(3)
            - self.second * inverse.integer_power(2),
        )

    def __truediv__(self, other: int | Fraction | Interval | "IntervalJet2") -> "IntervalJet2":
        return self * self.coerce(other).reciprocal()

    def __rtruediv__(self, other: int | Fraction | Interval | "IntervalJet2") -> "IntervalJet2":
        return self.coerce(other) / self

    def integer_power(self, exponent: int) -> "IntervalJet2":
        if exponent == 0:
            return self.constant(1)
        if exponent < 0:
            return self.integer_power(-exponent).reciprocal()
        value_power = self.value.integer_power(exponent)
        first_factor = exponent * self.value.integer_power(exponent - 1)
        second_factor = exponent * (exponent - 1) * self.value.integer_power(exponent - 2)
        return IntervalJet2(
            value_power,
            first_factor * self.first,
            second_factor * self.first.integer_power(2) + first_factor * self.second,
        )

    def rational_power(self, numerator: int, denominator: int) -> "IntervalJet2":
        exponent = Fraction(numerator, denominator)
        value_power = positive_rational_power(self.value, numerator, denominator)
        first_factor = exponent * positive_rational_power(
            self.value, numerator - denominator, denominator
        )
        second_factor = exponent * (exponent - 1) * positive_rational_power(
            self.value, numerator - 2 * denominator, denominator
        )
        return IntervalJet2(
            value_power,
            first_factor * self.first,
            second_factor * self.first.integer_power(2) + first_factor * self.second,
        )

    def logarithm(self) -> "IntervalJet2":
        inverse = self.value.reciprocal()
        return IntervalJet2(
            log_interval(self.value),
            self.first * inverse,
            self.second * inverse - self.first.integer_power(2) * inverse.integer_power(2),
        )


SQRT_TWO = interval_root(Interval.point(2), 2, BITS + 16)


def chord_squared(distance: int) -> Interval:
    distance %= 8
    distance = min(distance, 8 - distance)
    if distance == 1:
        return 2 - SQRT_TWO
    if distance == 2:
        return Interval.point(2)
    if distance == 3:
        return 2 + SQRT_TWO
    if distance == 4:
        return Interval.point(4)
    raise ValueError(f"invalid nonzero distance {distance}")


def projection_entry_squared(distance: int) -> Interval:
    distance %= 8
    distance = min(distance, 8 - distance)
    if distance in (2, 4):
        return Interval.point(0)
    if distance == 1:
        return (2 + SQRT_TWO) / 32
    if distance == 3:
        return (2 - SQRT_TWO) / 32
    raise ValueError(f"invalid nonzero distance {distance}")


def state_data(state: tuple[int, int, int, int]) -> tuple[Interval, Interval, Interval]:
    vandermonde = Interval.point(1)
    pair_defect = Interval.point(0)
    for left, right in combinations(state, 2):
        distance = right - left
        vandermonde *= chord_squared(distance)
        pair_defect += Fraction(1, 28) - projection_entry_squared(distance)
    r0 = Fraction(70, 8**4) * vandermonde
    v2 = Fraction(35, 3) * pair_defect
    v4 = r0 - 1 - v2
    return r0, v2, v4


STATES = tuple(combinations(range(8), 4))
DATA = tuple(state_data(state) for state in STATES)
DATA_COUNTS = Counter(DATA)


def curvature(point: Fraction) -> IntervalJet2:
    c = Fraction(19, 20)
    a = IntervalJet2(Interval.point(point), Interval.point(1), Interval.point(0))
    xi = a * (Fraction(1, 20) - a) / c
    q2 = 1 + 6 * xi + 6 * xi.integer_power(2)
    q4 = (
        1
        + 20 * xi
        + 90 * xi.integer_power(2)
        + 140 * xi.integer_power(3)
        + 70 * xi.integer_power(4)
    )
    ratio = q2 / q4
    corrected_ratio = ratio.rational_power(10, 7)
    epsilon = IntervalJet2.constant(0)
    for (_, v2, v4), multiplicity in DATA_COUNTS.items():
        true_density = 1 + ratio * v2 + IntervalJet2.constant(v4) / q4
        corrected_density = 1 + ratio * v2 + corrected_ratio * v4
        epsilon += Fraction(multiplicity, 70) * (
            true_density * true_density.logarithm()
            - corrected_density * corrected_density.logarithm()
        )
    return c**4 * q4 * epsilon


def outward_decimal(value: Fraction, digits: int, upper: bool) -> str:
    scale = 10**digits
    scaled = value * scale
    if upper:
        integer = -((-scaled.numerator) // scaled.denominator)
    else:
        integer = scaled.numerator // scaled.denominator
    sign = "-" if integer < 0 else ""
    integer = abs(integer)
    whole, remainder = divmod(integer, scale)
    return f"{sign}{whole}.{remainder:0{digits}d}"


def interval_text(value: Interval, digits: int = 14) -> str:
    return (
        "["
        + outward_decimal(value.low, digits, upper=False)
        + ", "
        + outward_decimal(value.high, digits, upper=True)
        + "]"
    )


def main() -> None:
    mean_r0 = sum((row[0] for row in DATA), Interval.point(0)) / 70
    mean_v2 = sum((row[1] for row in DATA), Interval.point(0)) / 70
    mean_v4 = sum((row[2] for row in DATA), Interval.point(0)) / 70
    if not (mean_r0.low <= 1 <= mean_r0.high):
        raise AssertionError("mean r0 interval misses one")
    if not (mean_v2.low <= 0 <= mean_v2.high):
        raise AssertionError("mean v2 interval misses zero")
    if not (mean_v4.low <= 0 <= mean_v4.high):
        raise AssertionError("mean v4 interval misses zero")

    print("FINITE_CERTIFIED rational intervals")
    print(f"BITS={BITS}, states={len(STATES)}, orbit_types={len(DATA_COUNTS)}")
    print(f"mean_r0={interval_text(mean_r0)}")
    print(f"mean_v2={interval_text(mean_v2)}")
    print(f"mean_v4={interval_text(mean_v4)}")
    for point in (Fraction(1, 200), Fraction(1, 50), Fraction(1, 40)):
        result = curvature(point).second
        if result.low > 0:
            sign = "positive"
        elif result.high < 0:
            sign = "negative"
        else:
            sign = "undetermined"
        print(f"a={point} E_second={interval_text(result)} sign={sign}")
        if sign == "undetermined":
            raise AssertionError(f"interval did not decide the sign at {point}")


if __name__ == "__main__":
    main()
