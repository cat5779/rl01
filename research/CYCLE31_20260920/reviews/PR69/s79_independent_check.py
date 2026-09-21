#!/usr/bin/env python3
"""Independent checks for the S79 visible-prefix audit.

The m=36 obstruction is recomputed with standard-library, outward-rounded
Decimal interval arithmetic.  A separate exact-rational m=3 channel checks the
posterior/number-operator and paid-shell identities.  No author code is imported.
"""
from __future__ import annotations

import itertools
import json
import math
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, getcontext, localcontext
from fractions import Fraction


PREC = 80
getcontext().prec = PREC
DOWN = Context(prec=PREC, rounding=ROUND_FLOOR)
UP = Context(prec=PREC, rounding=ROUND_CEILING)
D = Decimal


def frac_dec(x: Fraction, upward: bool = False) -> Decimal:
    with localcontext(UP if upward else DOWN):
        return D(x.numerator) / D(x.denominator)


class Interval:
    __slots__ = ("lo", "hi")

    def __init__(self, lo: Decimal | int | str, hi: Decimal | int | str | None = None):
        self.lo = D(lo)
        self.hi = D(lo if hi is None else hi)
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    @classmethod
    def fraction(cls, x: Fraction) -> "Interval":
        return cls(frac_dec(x, False), frac_dec(x, True))

    def __add__(self, other: "Interval" | int) -> "Interval":
        other = as_interval(other)
        with localcontext(DOWN):
            lo = self.lo + other.lo
        with localcontext(UP):
            hi = self.hi + other.hi
        return Interval(lo, hi)

    __radd__ = __add__

    def __neg__(self) -> "Interval":
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other: "Interval" | int) -> "Interval":
        return self + (-as_interval(other))

    def __mul__(self, other: "Interval" | int) -> "Interval":
        other = as_interval(other)
        with localcontext(DOWN):
            low_candidates = [
                self.lo * other.lo,
                self.lo * other.hi,
                self.hi * other.lo,
                self.hi * other.hi,
            ]
        with localcontext(UP):
            high_candidates = [
                self.lo * other.lo,
                self.lo * other.hi,
                self.hi * other.lo,
                self.hi * other.hi,
            ]
        return Interval(min(low_candidates), max(high_candidates))

    __rmul__ = __mul__

    def ln(self) -> "Interval":
        if self.lo <= 0:
            raise ValueError("logarithm requires a positive interval")
        with localcontext(DOWN):
            lo = self.lo.ln()
        with localcontext(UP):
            hi = self.hi.ln()
        return Interval(lo, hi)

    def json(self) -> list[str]:
        return [str(self.lo), str(self.hi)]


def as_interval(x: Interval | int) -> Interval:
    return x if isinstance(x, Interval) else Interval(x)


def hybrid_curvature_interval(m: int, identity_layers: set[int]) -> Interval:
    r = Fraction(9, 100)
    s = Fraction(41, 100)
    logr = Interval.fraction(r).ln()
    logs = Interval.fraction(s).ln()
    total = Interval(0)

    for n in range(m + 1):
        if n in identity_layers:
            for h in range(m + 1):
                lo, hi = max(0, h + n - m), min(h, n)
                for b in range(lo, hi + 1):
                    multiplicity = math.comb(m, h) * math.comb(h, b) * math.comb(m - h, n - b)
                    equal = m - h - n + 2 * b
                    x = h + n - m
                    probability = (r**equal) * (s ** (m - equal))
                    acceleration = Fraction(x * x - equal, 1) / (r * r) + (
                        Fraction(equal, 1) - 2 * m * r
                    ) / (r * s)
                    score2 = Fraction(x * x, 1) / (r * r)
                    log_probability = equal * logr + (m - equal) * logs
                    total = total - multiplicity * Interval.fraction(probability) * (
                        Interval.fraction(acceleration) * log_probability
                        + Interval.fraction(score2)
                    )
        else:
            for h in range(m + 1):
                lo, hi = max(0, h + n - m), min(h, n)
                probability = Fraction(0)
                probability2 = Fraction(0)
                x = h + n - m
                for b in range(lo, hi + 1):
                    multiplicity_z = math.comb(h, b) * math.comb(m - h, n - b)
                    equal = m - h - n + 2 * b
                    atom = (r**equal) * (s ** (m - equal))
                    acceleration = Fraction(x * x - equal, 1) / (r * r) + (
                        Fraction(equal, 1) - 2 * m * r
                    ) / (r * s)
                    probability += multiplicity_z * atom
                    probability2 += multiplicity_z * atom * acceleration
                score2 = Fraction(x * x, 1) / (r * r)
                shell_atom = probability / math.comb(m, n)
                total = total - math.comb(m, h) * (
                    Interval.fraction(probability2) * Interval.fraction(shell_atom).ln()
                    + Interval.fraction(probability * score2)
                )
    return total


def popcount(x: int) -> int:
    return x.bit_count()


def make_layer_channel(m: int, identity_layers: set[int]) -> list[list[Fraction]]:
    size = 1 << m
    channel = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    layers = [[mask for mask in range(size) if popcount(mask) == n] for n in range(m + 1)]
    for n, masks in enumerate(layers):
        if n in identity_layers:
            for mask in masks:
                channel[mask][mask] = Fraction(1)
        else:
            weight = Fraction(1, len(masks))
            for z in masks:
                for t in masks:
                    channel[z][t] = weight
    return channel


def matmul_fraction(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    bt = list(zip(*b))
    return [[sum((x * y for x, y in zip(row, col)), Fraction(0)) for col in bt] for row in a]


def number_operator(values: list[list[Fraction]], m: int) -> list[list[Fraction]]:
    size = 1 << m
    return [
        [
            sum((values[y][t] - values[y ^ (1 << bit)][t] for bit in range(m)), Fraction(0)) / 2
            for t in range(size)
        ]
        for y in range(size)
    ]


def log_fraction(x: Fraction) -> Decimal:
    return (D(x.numerator) / D(x.denominator)).ln()


def evaluate_small_channel(m: int, channel: list[list[Fraction]]) -> dict[str, object]:
    size = 1 << m
    r = Fraction(9, 100)
    s = Fraction(41, 100)
    k = Fraction(16, 25)
    beta = (1 - k * k) / (2 * k)

    probability = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    probability2 = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    equal_count = [[0 for _ in range(size)] for _ in range(size)]
    x_value = [[0 for _ in range(size)] for _ in range(size)]
    for y in range(size):
        for z in range(size):
            equal = m - popcount(y ^ z)
            x = popcount(y) + popcount(z) - m
            atom = (r**equal) * (s ** (m - equal))
            acceleration = Fraction(x * x - equal, 1) / (r * r) + (
                Fraction(equal, 1) - 2 * m * r
            ) / (r * s)
            probability[y][z] = atom
            probability2[y][z] = atom * acceleration
            equal_count[y][z] = equal
            x_value[y][z] = x

    q = matmul_fraction(probability, channel)
    q2 = matmul_fraction(probability2, channel)
    scale = 4**m
    density = [[scale * q[y][t] for t in range(size)] for y in range(size)]
    number = number_operator(density, m)

    max_posterior_residual = Fraction(0)
    for y in range(size):
        for t in range(size):
            numerator = sum(
                (equal_count[y][z] * probability[y][z] * channel[z][t] for z in range(size)),
                Fraction(0),
            )
            delta_density = scale * numerator
            residual = delta_density - 2 * m * r * density[y][t] + beta * number[y][t]
            max_posterior_residual = max(max_posterior_residual, abs(residual))

    hpp = D(0)
    edge = D(0)
    ex2 = D(0)
    elog = D(0)
    ex2log = D(0)
    for y in range(size):
        for t in range(size):
            x = popcount(y) + popcount(t) - m
            logq = log_fraction(q[y][t])
            logdensity = log_fraction(density[y][t])
            hpp -= frac_dec(q2[y][t]) * logq
            hpp -= frac_dec(q[y][t] * Fraction(x * x, 1) / (r * r))
            edge += frac_dec(number[y][t]) * logdensity / D(4**m)
            ex2 += frac_dec(q[y][t] * x * x)
            elog += frac_dec(q[y][t]) * logdensity
            ex2log += frac_dec(q[y][t] * x * x) * logdensity
    covariance = ex2log - ex2 * elog
    formula = -covariance / (frac_dec(r) ** 2) - 4 * edge / frac_dec(r) - D(2 * m) / frac_dec(r)
    return {
        "q": q,
        "hpp": hpp,
        "edge": edge,
        "formula": formula,
        "posterior_residual_exact": str(max_posterior_residual),
        "curvature_formula_residual": str(abs(hpp - formula)),
    }


def paid_shell_small_check() -> dict[str, str]:
    m = 3
    actual_channel = make_layer_channel(m, {1})
    shell_channel = make_layer_channel(m, set())
    actual = evaluate_small_channel(m, actual_channel)
    shell = evaluate_small_channel(m, shell_channel)
    q = actual["q"]
    r = Fraction(9, 100)

    weighted_j: list[tuple[Fraction, int, Decimal]] = []
    for y in range(1 << m):
        h = popcount(y)
        for n in range(m + 1):
            masks = [t for t in range(1 << m) if popcount(t) == n]
            mu = sum((q[y][t] for t in masks), Fraction(0))
            if mu == 0:
                continue
            shell_size = len(masks)
            j_value = D(0)
            for t in masks:
                conditional = q[y][t] / mu
                j_value += frac_dec(conditional) * log_fraction(conditional * shell_size)
            weighted_j.append((mu, (h + n - m) ** 2, j_value))

    mean_x2 = sum((frac_dec(mu * x2) for mu, x2, _ in weighted_j), D(0))
    mean_j = sum((frac_dec(mu) * j for mu, _, j in weighted_j), D(0))
    mean_x2j = sum((frac_dec(mu * x2) * j for mu, x2, j in weighted_j), D(0))
    covariance_shell = mean_x2j - mean_x2 * mean_j
    delta_edge = actual["edge"] - shell["edge"]
    rhs_difference = -covariance_shell / (frac_dec(r) ** 2) - 4 * delta_edge / frac_dec(r)
    lhs_difference = actual["hpp"] - shell["hpp"]

    jpp = shell["hpp"] - actual["hpp"]
    jpp_rhs = covariance_shell / (frac_dec(r) ** 2) + 4 * delta_edge / frac_dec(r)
    return {
        "actual_hpp": str(actual["hpp"]),
        "shell_hpp": str(shell["hpp"]),
        "posterior_residual_exact": actual["posterior_residual_exact"],
        "actual_curvature_formula_residual": actual["curvature_formula_residual"],
        "paid_shell_identity_residual": str(abs(lhs_difference - rhs_difference)),
        "relative_entropy_curvature_residual": str(abs(jpp - jpp_rhs)),
        "delta_edge": str(delta_edge),
        "signed_shell_covariance": str(covariance_shell),
    }


def permutation_deletion_exact(m: int) -> bool:
    permutation = {i: (i + 1) % m for i in range(m)}
    layers = [list(itertools.combinations(range(m), n)) for n in range(m + 1)]
    for n in range(1, m + 1):
        upper = layers[n]
        lower = layers[n - 1]
        for a in upper:
            image_a = tuple(sorted(permutation[i] for i in a))
            for c in lower:
                lhs = Fraction(int(set(c).issubset(image_a)), n)
                preimage_c = tuple(sorted((i - 1) % m for i in c))
                rhs = Fraction(int(set(preimage_c).issubset(a)), n)
                if lhs != rhs:
                    return False
    return True


def main() -> None:
    obstruction = hybrid_curvature_interval(36, set(range(16, 21)))
    shell_baseline = hybrid_curvature_interval(36, set())
    shell_gap = obstruction - shell_baseline
    small = paid_shell_small_check()
    result = {
        "python_decimal_precision": PREC,
        "m36_c4_over_5_curvature_interval": obstruction.json(),
        "m36_strictly_positive": obstruction.lo > 0,
        "m36_shell_baseline_curvature_interval": shell_baseline.json(),
        "m36_curvature_minus_shell_interval": shell_gap.json(),
        "m36_paid_shell_strictly_fails": shell_gap.lo > 0,
        "m3_exact_rational_paid_shell_check": small,
        "permutation_exterior_deletion_exact_m4": permutation_deletion_exact(4),
    }
    print(json.dumps(result, indent=2))
    if not result["m36_strictly_positive"]:
        raise SystemExit("FAIL_M36_INTERVAL")
    if not result["m36_paid_shell_strictly_fails"]:
        raise SystemExit("FAIL_M36_PAID_SHELL_GAP")
    if small["posterior_residual_exact"] != "0":
        raise SystemExit("FAIL_POSTERIOR_IDENTITY")
    if not result["permutation_exterior_deletion_exact_m4"]:
        raise SystemExit("FAIL_DELETION_INDEXING")
    print("PASS_INDEPENDENT_S79_CHECKS")


if __name__ == "__main__":
    main()
