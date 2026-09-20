#!/usr/bin/env python3
"""Outward-rounded independent certificates for the visible S78 claims.

No author attachment is used.  Pi is enclosed from Machin's formula with exact
rational alternating-series bounds.  All subsequent arithmetic, including
logarithms, uses directed Decimal rounding.
"""
from __future__ import annotations

import itertools
import json
import math
from decimal import (
    Context,
    Decimal,
    ROUND_CEILING,
    ROUND_FLOOR,
    getcontext,
    localcontext,
)
from fractions import Fraction


PREC = 85
getcontext().prec = PREC
DOWN = Context(prec=PREC, rounding=ROUND_FLOOR)
UP = Context(prec=PREC, rounding=ROUND_CEILING)
D = Decimal


def frac_dec(x: Fraction, upward: bool) -> Decimal:
    with localcontext(UP if upward else DOWN):
        return D(x.numerator) / D(x.denominator)


class I:
    __slots__ = ("lo", "hi")

    def __init__(self, lo: Decimal | int | str, hi: Decimal | int | str | None = None):
        self.lo = D(lo)
        self.hi = D(lo if hi is None else hi)
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    @classmethod
    def fraction(cls, x: Fraction) -> "I":
        return cls(frac_dec(x, False), frac_dec(x, True))

    def __add__(self, other: "I" | int) -> "I":
        other = as_i(other)
        with localcontext(DOWN):
            lo = self.lo + other.lo
        with localcontext(UP):
            hi = self.hi + other.hi
        return I(lo, hi)

    __radd__ = __add__

    def __neg__(self) -> "I":
        return I(-self.hi, -self.lo)

    def __sub__(self, other: "I" | int) -> "I":
        return self + (-as_i(other))

    def __rsub__(self, other: "I" | int) -> "I":
        return as_i(other) - self

    def __mul__(self, other: "I" | int) -> "I":
        other = as_i(other)
        with localcontext(DOWN):
            lows = [
                self.lo * other.lo,
                self.lo * other.hi,
                self.hi * other.lo,
                self.hi * other.hi,
            ]
        with localcontext(UP):
            highs = [
                self.lo * other.lo,
                self.lo * other.hi,
                self.hi * other.lo,
                self.hi * other.hi,
            ]
        return I(min(lows), max(highs))

    __rmul__ = __mul__

    def reciprocal(self) -> "I":
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("interval contains zero")
        with localcontext(DOWN):
            lows = [D(1) / self.lo, D(1) / self.hi]
        with localcontext(UP):
            highs = [D(1) / self.lo, D(1) / self.hi]
        return I(min(lows), max(highs))

    def __truediv__(self, other: "I" | int) -> "I":
        return self * as_i(other).reciprocal()

    def __rtruediv__(self, other: "I" | int) -> "I":
        return as_i(other) / self

    def __pow__(self, n: int) -> "I":
        if n < 0:
            return (self.reciprocal()) ** (-n)
        result = I(1)
        base = self
        exponent = n
        while exponent:
            if exponent & 1:
                result = result * base
            base = base * base
            exponent >>= 1
        return result

    def ln(self) -> "I":
        if self.lo <= 0:
            raise ValueError("log of nonpositive interval")
        with localcontext(DOWN):
            lo = self.lo.ln()
        with localcontext(UP):
            hi = self.hi.ln()
        return I(lo, hi)

    def contains_zero(self) -> bool:
        return self.lo <= 0 <= self.hi

    def json(self) -> list[str]:
        return [str(self.lo), str(self.hi)]


def as_i(x: I | int) -> I:
    return x if isinstance(x, I) else I(x)


def arctan_reciprocal_bounds(q: int, odd_last: int) -> tuple[Fraction, Fraction]:
    if odd_last % 2 != 1:
        raise ValueError("odd_last must be odd")
    terms = [Fraction((-1) ** k, (2 * k + 1) * q ** (2 * k + 1)) for k in range(odd_last + 1)]
    lower = sum(terms, Fraction(0))
    upper = sum(terms[:-1], Fraction(0))
    return lower, upper


def pi_interval() -> I:
    a_lo, a_hi = arctan_reciprocal_bounds(5, 149)
    b_lo, b_hi = arctan_reciprocal_bounds(239, 49)
    lo = 16 * a_lo - 4 * b_hi
    hi = 16 * a_hi - 4 * b_lo
    return I(frac_dec(lo, False), frac_dec(hi, True))


PI = pi_interval()
Matrix = list[list[I]]


def transpose(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a)]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), I(0)) for col in bt] for row in a]


def matsub(a: Matrix, b: Matrix) -> Matrix:
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def det(a: Matrix) -> I:
    n = len(a)
    if n == 0:
        return I(1)
    m = [[I(x.lo, x.hi) for x in row] for row in a]
    ans = I(1)
    for col in range(n):
        pivot = next(i for i in range(col, n) if not m[i][col].contains_zero())
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
            ans = -ans
        p = m[col][col]
        ans = ans * p
        for i in range(col + 1, n):
            factor = m[i][col] / p
            for j in range(col + 1, n):
                m[i][j] = m[i][j] - factor * m[col][j]
    return ans


def inverse(a: Matrix) -> Matrix:
    n = len(a)
    m = [[I(x.lo, x.hi) for x in a[i]] + [I(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if not m[i][col].contains_zero())
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
        p = m[col][col]
        m[col] = [x / p for x in m[col]]
        for i in range(n):
            if i == col:
                continue
            factor = m[i][col]
            m[i] = [x - factor * y for x, y in zip(m[i], m[col])]
    return [row[n:] for row in m]


def sine_entry(i: int, j: int, c: I) -> I:
    if i == j:
        return I("0.5")
    r = i - j
    if r % 2 == 0:
        return I(0)
    sign = 1 if r % 4 == 1 else -1
    return c * sign / (PI * r)


def sine_kernel(sites: list[int], c: I) -> Matrix:
    return [[sine_entry(i, j, c) for j in sites] for i in sites]


def submatrix(a: Matrix, rows: list[int], cols: list[int]) -> Matrix:
    return [[a[i][j] for j in cols] for i in rows]


def word_probability(k: Matrix, word: tuple[int, ...]) -> I:
    a = [[I(x.lo, x.hi) for x in row] for row in k]
    zeros = 0
    for i, bit in enumerate(word):
        if bit == 0:
            a[i][i] = a[i][i] - 1
            zeros += 1
    probability = det(a) * ((-1) ** zeros)
    if probability.lo <= 0:
        raise AssertionError(f"probability not strictly positive: {probability.json()}")
    return probability


def conditional_pair_kernel(k: Matrix, pair_idx: list[int], ext_idx: list[int], word: tuple[int, ...]) -> Matrix:
    c = submatrix(k, pair_idx, pair_idx)
    if not ext_idx:
        return c
    a = submatrix(k, ext_idx, ext_idx)
    for j, bit in enumerate(word):
        if bit == 0:
            a[j][j] = a[j][j] - 1
    w = submatrix(k, pair_idx, ext_idx)
    return matsub(c, matmul(matmul(w, inverse(a)), transpose(w)))


def pair_cells(c: Matrix) -> tuple[I, I, I, I]:
    alpha, beta = c[0][0], c[1][1]
    s = c[0][1] * c[1][0]
    cells = (
        alpha * beta - s,
        alpha * (1 - beta) + s,
        (1 - alpha) * beta + s,
        (1 - alpha) * (1 - beta) - s,
    )
    if any(x.lo <= 0 for x in cells):
        raise AssertionError("pair cell lost positivity")
    return cells


def pair_f(c: Matrix) -> I:
    p11, p10, p01, p00 = pair_cells(c)
    s = c[0][1] * c[1][0]
    return s * (1 / p11 + 1 / p10 + 1 / p01 + 1 / p00) + (p11 * p00 / (p10 * p01)).ln()


def pair_ell(c: Matrix) -> I:
    p11, _, _, p00 = pair_cells(c)
    return p11.ln() + p00.ln()


def expected_pair(sites: list[int], pair: tuple[int, int], c: I, functional) -> I:
    k = sine_kernel(sites, c)
    pair_idx = [sites.index(pair[0]), sites.index(pair[1])]
    ext_idx = [i for i in range(len(sites)) if i not in pair_idx]
    k_ext = submatrix(k, ext_idx, ext_idx)
    total = I(0)
    for word in itertools.product((0, 1), repeat=len(ext_idx)):
        probability = word_probability(k_ext, word)
        cp = conditional_pair_kernel(k, pair_idx, ext_idx, word)
        total = total + probability * functional(cp)
    return total


def bernoulli_numbers(n: int) -> list[Fraction]:
    work = [Fraction(0) for _ in range(n + 1)]
    out = [Fraction(0) for _ in range(n + 1)]
    for m in range(n + 1):
        work[m] = Fraction(1, m + 1)
        for j in range(m, 0, -1):
            work[j - 1] = j * (work[j - 1] - work[j])
        out[m] = work[0]
    return out


BERNOULLI = bernoulli_numbers(84)


def zeta_even(order: int) -> I:
    n = order // 2
    sign = 1 if n % 2 == 1 else -1
    rational = Fraction(sign, 2 * math.factorial(order)) * BERNOULLI[order]
    return I.fraction(rational) * (2 * PI) ** order


def rademacher_cumulant(order: int) -> Fraction:
    n = order // 2
    return Fraction(2 ** (2 * n) * (2 ** (2 * n) - 1), 2 * n) * BERNOULLI[2 * n]


def star_barrier(c: I, delta: I, max_n: int = 21) -> I:
    max_order = 2 * max_n
    cumulants = [I(0) for _ in range(max_order + 1)]
    scale = 2 * c * c / (PI * PI)
    for r in range(1, max_n + 1):
        order = 2 * r
        power_sum = scale**order * (2 * (1 - I.fraction(Fraction(1, 2 ** (2 * order)))) * zeta_even(2 * order) - 1)
        cumulants[order] = I.fraction(rademacher_cumulant(order)) * power_sum

    moments = [I(0) for _ in range(max_order + 1)]
    moments[0] = I(1)
    for n in range(1, max_order + 1):
        moments[n] = sum(
            (I(math.comb(n - 1, j - 1)) * cumulants[j] * moments[n - j] for j in range(1, n + 1)),
            I(0),
        )

    s = c * c / (PI * PI)
    a0 = I.fraction(Fraction(1, 4)) - s
    total_other = c * c / 4 - s
    ratio = total_other / a0
    partial = sum(
        (moments[2 * n] / (n * (4 * a0 * a0) ** n) for n in range(1, max_n)),
        I(0),
    )
    normalized_42 = moments[42] / (4 * a0 * a0) ** 21
    tail_bound = normalized_42 / (21 * (1 - ratio * ratio))
    base = 2 * a0.ln() - 2 * (delta * (1 - delta)).ln()
    partial_barrier = base - partial
    return partial_barrier - I(0, tail_bound.hi)


def main() -> None:
    c = I.fraction(Fraction(19, 20))
    delta = I.fraction(Fraction(1, 50))

    center_old = [0, -3, 1, 3]
    center_new = [0, -3, 1, 3, -4]
    center_f = expected_pair(center_new, (0, -3), c, pair_f) - expected_pair(center_old, (0, -3), c, pair_f)
    center_ell = expected_pair(center_new, (0, -3), c, pair_ell) - expected_pair(center_old, (0, -3), c, pair_ell)
    center_compensated = center_f - center_ell

    leaf_old = [0, 10, 7, -3]
    leaf_new = [0, 10, 7, -3, -1]
    old_chi = expected_pair(leaf_old, (0, 7), c, pair_f) + expected_pair(leaf_old, (10, 7), c, pair_f)
    new_chi = expected_pair(leaf_new, (0, 7), c, pair_f) + expected_pair(leaf_new, (10, 7), c, pair_f)
    leaf_drift = new_chi - old_chi

    result = {
        "decimal_precision": PREC,
        "pi_interval": PI.json(),
        "center_addition_f_drift": center_f.json(),
        "center_addition_ell_drift": center_ell.json(),
        "center_addition_compensated_drift": center_compensated.json(),
        "two_center_leaf_addition_chi_drift": leaf_drift.json(),
        "star_barrier_20_moments_plus_21st_tail": star_barrier(c, delta).json(),
        "passes": {
            "center_raw_negative": center_f.hi < 0,
            "center_compensated_positive": center_compensated.lo > 0,
            "two_center_leaf_negative": leaf_drift.hi < 0,
        },
    }
    print(json.dumps(result, indent=2))
    if not all(result["passes"].values()):
        raise SystemExit("FAIL_INTERVAL_CERTIFICATE")
    print("PASS_INDEPENDENT_S78_INTERVAL_CERTIFICATE")


if __name__ == "__main__":
    main()
