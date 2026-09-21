#!/usr/bin/env python3
"""Independent finite checks for the S78 Cycle31 visible manuscripts.

This program is separate from the unavailable author certificates. It uses
direct DPP determinant enumeration and a closed moment/cumulant recurrence.
The analytic all-size claims are proved in the accompanying review; decimal
output here is a high-precision diagnostic, not an interval certificate.
"""
from __future__ import annotations

import itertools
import json
import math
from decimal import Decimal, getcontext
from fractions import Fraction


getcontext().prec = 100
D = Decimal
PI = D(
    "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117068"
)


def dec_fraction(x: Fraction) -> Decimal:
    return D(x.numerator) / D(x.denominator)


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


def zeta_even(order: int) -> Decimal:
    """Euler's Bernoulli formula, evaluated at the fixed decimal pi."""
    assert order >= 2 and order % 2 == 0
    n = order // 2
    sign = 1 if n % 2 == 1 else -1
    rational = Fraction(sign, 2 * math.factorial(order)) * BERNOULLI[order]
    return dec_fraction(rational) * (2 * PI) ** order


Matrix = list[list[Decimal]]


def transpose(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a)]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def matsub(a: Matrix, b: Matrix) -> Matrix:
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def det(a: Matrix) -> Decimal:
    n = len(a)
    if n == 0:
        return D(1)
    m = [row[:] for row in a]
    ans = D(1)
    for col in range(n):
        pivot = next(i for i in range(col, n) if m[i][col] != 0)
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
            ans = -ans
        p = m[col][col]
        ans *= p
        for i in range(col + 1, n):
            factor = m[i][col] / p
            for j in range(col + 1, n):
                m[i][j] -= factor * m[col][j]
    return ans


def inverse(a: Matrix) -> Matrix:
    n = len(a)
    m = [a[i][:] + [D(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if m[i][col] != 0)
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


def sine_entry(i: int, j: int, c: Decimal) -> Decimal:
    if i == j:
        return D("0.5")
    r = i - j
    if r % 2 == 0:
        return D(0)
    sign = 1 if r % 4 == 1 else -1
    return c * sign / (PI * r)


def sine_kernel(sites: list[int], c: Decimal) -> Matrix:
    return [[sine_entry(i, j, c) for j in sites] for i in sites]


def submatrix(a: Matrix, rows: list[int], cols: list[int]) -> Matrix:
    return [[a[i][j] for j in cols] for i in rows]


def word_probability(k: Matrix, word: tuple[int, ...]) -> Decimal:
    a = [row[:] for row in k]
    zeros = 0
    for i, bit in enumerate(word):
        if bit == 0:
            a[i][i] -= 1
            zeros += 1
    return D((-1) ** zeros) * det(a)


def conditional_pair_kernel(
    k: Matrix, pair_idx: list[int], exterior_idx: list[int], word: tuple[int, ...]
) -> Matrix:
    c = submatrix(k, pair_idx, pair_idx)
    if not exterior_idx:
        return c
    a = submatrix(k, exterior_idx, exterior_idx)
    for j, bit in enumerate(word):
        if bit == 0:
            a[j][j] -= 1
    w = submatrix(k, pair_idx, exterior_idx)
    return matsub(c, matmul(matmul(w, inverse(a)), transpose(w)))


def pair_cells(c: Matrix) -> tuple[Decimal, Decimal, Decimal, Decimal]:
    alpha, beta = c[0][0], c[1][1]
    s = c[0][1] * c[1][0]
    return (
        alpha * beta - s,
        alpha * (1 - beta) + s,
        (1 - alpha) * beta + s,
        (1 - alpha) * (1 - beta) - s,
    )


def pair_f(c: Matrix) -> Decimal:
    p11, p10, p01, p00 = pair_cells(c)
    s = c[0][1] * c[1][0]
    return s * (1 / p11 + 1 / p10 + 1 / p01 + 1 / p00) + (
        p11 * p00 / (p10 * p01)
    ).ln()


def pair_ell(c: Matrix) -> Decimal:
    p11, _, _, p00 = pair_cells(c)
    return p11.ln() + p00.ln()


def expected_pair_f(sites: list[int], pair: tuple[int, int], c: Decimal) -> Decimal:
    k = sine_kernel(sites, c)
    pair_idx = [sites.index(pair[0]), sites.index(pair[1])]
    exterior_idx = [i for i in range(len(sites)) if i not in pair_idx]
    k_ext = submatrix(k, exterior_idx, exterior_idx)
    total = D(0)
    for word in itertools.product((0, 1), repeat=len(exterior_idx)):
        probability = word_probability(k_ext, word)
        cp = conditional_pair_kernel(k, pair_idx, exterior_idx, word)
        total += probability * pair_f(cp)
    return total


def reverse_kl_check(sites: list[int], pair: tuple[int, int], c: Decimal) -> dict[str, str]:
    k = sine_kernel(sites, c)
    pair_idx = [sites.index(pair[0]), sites.index(pair[1])]
    exterior_idx = [i for i in range(len(sites)) if i not in pair_idx]
    k_ext = submatrix(k, exterior_idx, exterior_idx)
    coarse = submatrix(k, pair_idx, pair_idx)
    p11_coarse, _, _, p00_coarse = pair_cells(coarse)
    delta_ell = D(0)
    kl11 = D(0)
    kl00 = D(0)
    for word in itertools.product((0, 1), repeat=len(exterior_idx)):
        pr = word_probability(k_ext, word)
        cp = conditional_pair_kernel(k, pair_idx, exterior_idx, word)
        p11, _, _, p00 = pair_cells(cp)
        delta_ell += pr * (pair_ell(cp) - pair_ell(coarse))
        pr11 = pr * p11 / p11_coarse
        pr00 = pr * p00 / p00_coarse
        kl11 += pr * (pr / pr11).ln()
        kl00 += pr * (pr / pr00).ln()
    return {
        "delta_ell": str(delta_ell),
        "minus_reverse_kl": str(-(kl11 + kl00)),
        "identity_error": str(delta_ell + kl11 + kl00),
    }


def rademacher_cumulant(order: int) -> Fraction:
    if order % 2 or order == 0:
        return Fraction(0)
    n = order // 2
    return Fraction(2 ** (2 * n) * (2 ** (2 * n) - 1), 2 * n) * BERNOULLI[2 * n]


def star_moments_and_barrier(c: Decimal, delta: Decimal, max_n: int = 21) -> dict[str, str]:
    """Moments of u=sum_{odd l != 1} 2 w_l epsilon_l at d=1/2."""
    max_order = 2 * max_n
    cumulants = [D(0)] * (max_order + 1)
    scale = 2 * c * c / (PI * PI)
    for r in range(1, max_n + 1):
        order = 2 * r
        power_sum = scale**order * (
            2 * (1 - D(2) ** (-2 * order)) * zeta_even(2 * order) - 1
        )
        cumulants[order] = dec_fraction(rademacher_cumulant(order)) * power_sum

    moments = [D(0)] * (max_order + 1)
    moments[0] = D(1)
    for n in range(1, max_order + 1):
        moments[n] = sum(
            D(math.comb(n - 1, j - 1)) * cumulants[j] * moments[n - j]
            for j in range(1, n + 1)
        )

    s = c * c / (PI * PI)
    a0 = D("0.25") - s
    total_other_weight = c * c / 4 - s
    support_ratio = total_other_weight / a0
    partial = sum(
        moments[2 * n] / (D(n) * (4 * a0 * a0) ** n) for n in range(1, max_n)
    )
    first_omitted_normalized = moments[2 * max_n] / (4 * a0 * a0) ** max_n
    tail = first_omitted_normalized / (D(max_n) * (1 - support_ratio * support_ratio))
    base = 2 * a0.ln() - 2 * (delta * (1 - delta)).ln()
    upper = base - partial
    lower = upper - tail
    return {
        "s": str(s),
        "A0": str(a0),
        "T": str(total_other_weight),
        "support_ratio_T_over_A0": str(support_ratio),
        "barrier_lower": str(lower),
        "barrier_upper": str(upper),
        "tail_bound": str(tail),
        "moment_42": str(moments[42]),
    }


def r4_quantifier_probe(c: Decimal) -> list[dict[str, str | int]]:
    rows: list[dict[str, str | int]] = []
    p = 0
    for q in (10, 20, 40, 80):
        fixed_i = 1
        moving_i = q + 1
        fixed_direct = abs(sine_entry(q, fixed_i, c)) ** 4
        moving_direct = abs(sine_entry(q, moving_i, c)) ** 4
        rows.append(
            {
                "R": q - p,
                "fixed_i_direct_fourth": str(fixed_direct),
                "R4_times_fixed": str(D((q - p) ** 4) * fixed_direct),
                "moving_i_q_plus_1_direct_fourth": str(moving_direct),
            }
        )
    return rows


def main() -> None:
    c = D(19) / 20

    center_old = [0, -3, 1, 3]
    center_new = [0, -3, 1, 3, -4]
    center_drift = expected_pair_f(center_new, (0, -3), c) - expected_pair_f(
        center_old, (0, -3), c
    )

    leaf_old = [0, 10, 7, -3]
    leaf_new = [0, 10, 7, -3, -1]
    old_chi = expected_pair_f(leaf_old, (0, 7), c) + expected_pair_f(
        leaf_old, (10, 7), c
    )
    new_chi = expected_pair_f(leaf_new, (0, 7), c) + expected_pair_f(
        leaf_new, (10, 7), c
    )
    leaf_drift = new_chi - old_chi

    result = {
        "precision_decimal_digits": getcontext().prec,
        "center_addition_drift": str(center_drift),
        "two_center_leaf_addition_chi_drift": str(leaf_drift),
        "reverse_kl_check": reverse_kl_check(center_new, (0, -3), c),
        "star_barrier_20_moments_plus_21st_tail": star_moments_and_barrier(
            c, D(1) / 50
        ),
        "r4_quantifier_probe": r4_quantifier_probe(c),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
