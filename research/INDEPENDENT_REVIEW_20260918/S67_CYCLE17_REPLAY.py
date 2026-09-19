#!/usr/bin/env python3
"""Independent decimal replay for the S67 Cycle17 review.

This is deliberately separate from the author programs.  It rebuilds the
half-density sine kernels, conditional two-site laws, and the scalar analytic
ledger using only the Python standard library.  It is a high-precision
cross-check, not a replacement for the rigorous rational/Arb enclosures.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
from itertools import combinations
import json


getcontext().prec = 80
D = Decimal
ZERO = D(0)
ONE = D(1)
PI = D("3.141592653589793238462643383279502884197169399375105820974944592307816406286")


def det(matrix: list[list[Decimal]]) -> Decimal:
    a = [row[:] for row in matrix]
    value = ONE
    for col in range(len(a)):
        pivot = next(row for row in range(col, len(a)) if a[row][col] != 0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            value = -value
        q = a[col][col]
        value *= q
        for row in range(col + 1, len(a)):
            factor = a[row][col] / q
            for k in range(col + 1, len(a)):
                a[row][k] -= factor * a[col][k]
    return value


def inverse(matrix: list[list[Decimal]]) -> list[list[Decimal]]:
    n = len(matrix)
    a = [row[:] + [ONE if i == j else ZERO for j in range(n)]
         for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(row for row in range(col, n) if a[row][col] != 0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
        q = a[col][col]
        a[col] = [x / q for x in a[col]]
        for row in range(n):
            if row == col:
                continue
            factor = a[row][col]
            a[row] = [x - factor * y for x, y in zip(a[row], a[col])]
    return [row[n:] for row in a]


def matmul(a: list[list[Decimal]], b: list[list[Decimal]]) -> list[list[Decimal]]:
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), ZERO)
             for j in range(len(b[0]))] for i in range(len(a))]


def sine_kernel(n: int) -> list[list[Decimal]]:
    c = D(19) / 20
    out = [[ZERO for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                out[i][j] = ONE / 2
            else:
                d = i - j
                if d % 2:
                    sign = 1 if d % 4 == 1 else -1
                    out[i][j] = c * sign / (PI * d)
    return out


def conditional_pair(kernel: list[list[Decimal]], pair: tuple[int, int], mask: int) -> dict:
    exterior = [i for i in range(len(kernel)) if i not in pair]
    bits = [(mask >> k) & 1 for k in range(len(exterior))]
    m = [[kernel[i][j] - (ONE - bits[ii] if ii == jj else ZERO)
          for jj, j in enumerate(exterior)] for ii, i in enumerate(exterior)]
    p_exterior = det(m) * ((-ONE) ** (len(exterior) - sum(bits)))
    m_inv = inverse(m)
    c = [[kernel[i][j] for j in exterior] for i in pair]
    ct = [[kernel[i][j] for j in pair] for i in exterior]
    correction = matmul(matmul(c, m_inv), ct)
    tmat = [[kernel[pair[i]][pair[j]] - correction[i][j]
             for j in range(2)] for i in range(2)]
    u, v, z = tmat[0][0], tmat[1][1], tmat[0][1]
    t = z * z
    q11 = u * v - t
    q10 = u * (ONE - v) + t
    q01 = (ONE - u) * v + t
    q00 = (ONE - u) * (ONE - v) - t
    cells = [q11, q10, q01, q00]
    if p_exterior <= 0 or min(cells) <= 0:
        raise ArithmeticError("nonpositive conditional atom")
    j_value = (q10 * q01 / (q11 * q00)).ln()
    w_value = t * sum((ONE / q for q in cells), ZERO)
    return {
        "exterior_bits": bits,
        "p_exterior": p_exterior,
        "J": j_value,
        "W": w_value,
    }


def finite_counterexamples() -> dict:
    k4 = sine_kernel(4)
    point = conditional_pair(k4, (0, 3), 1)

    k6 = sine_kernel(6)
    pair_summaries = []
    total_j = ZERO
    total_w = ZERO
    selected = None
    for pair in combinations(range(6), 2):
        rows = [conditional_pair(k6, pair, mask) for mask in range(16)]
        norm = sum((row["p_exterior"] for row in rows), ZERO)
        ej = sum((row["p_exterior"] * row["J"] for row in rows), ZERO)
        ew = sum((row["p_exterior"] * row["W"] for row in rows), ZERO)
        total_j += ej
        total_w += ew
        pair_summaries.append((pair, ew - ej))
        if pair == (0, 5):
            selected = {"normalization": norm, "E_J": ej, "E_W": ew}

    assert point["J"] - point["W"] > D("0.00078")
    assert selected is not None
    assert selected["E_J"] - selected["E_W"] > D("0.00037")
    assert total_w - total_j > D(5)
    return {
        "pointwise_n4_pair_0_3_bits_1_0": {
            "J": point["J"],
            "W": point["W"],
            "J_minus_W": point["J"] - point["W"],
        },
        "actual_law_n6_pair_0_5": {
            **selected,
            "E_J_minus_E_W": selected["E_J"] - selected["E_W"],
        },
        "finite_n6_all_pairs": {
            "sum_E_J": total_j,
            "sum_E_W": total_w,
            "sum_E_W_minus_E_J": total_w - total_j,
            "minimum_pair_E_W_minus_E_J": min(v for _, v in pair_summaries),
        },
    }


def analytic_ledger() -> dict:
    a0 = D(1) / 50
    b = D(1) / 40
    s = D(39) / 1600
    h = (D(19) / 20) / PI
    tau = h * h
    log_ratio = (b / a0).ln()
    df3 = (
        a0 / 2 * (ONE / (b * b) - ONE / (a0 * a0))
        - (ONE + 3 * a0) * (ONE / b - ONE / a0)
        - 3 * (ONE + a0) * log_ratio
        + (3 + a0) * (b - a0)
        - (b * b - a0 * a0) / 2
    ) / (D(39) ** 3)
    d3 = 2 + 2 / (ONE - 64 * tau * tau)
    u3 = D(3) / 2 * (df3 / s - d3 / D(80000))
    beta3 = 3 * (d3 - 4) / D(80000)
    c16 = D("0.000146680480325883947552193049")
    required_cap = D("0.000392612480721685576393825706")
    limsup_a = u3 - c16
    dmax = D(2475) ** 2 / (D(97) * D(2378))
    diagonal_floor = D(3) / 2 * (df3 / s - dmax / D(80000))

    assert limsup_a < D("0.000703319519674")
    assert u3 - required_cap > D("0.000456")
    assert diagonal_floor - required_cap > D("0.000076")
    return {
        "d3": d3,
        "U3": u3,
        "beta3": beta3,
        "limsup_A_upper": limsup_a,
        "required_C_cap": required_cap,
        "U3_minus_required_cap": u3 - required_cap,
        "diagonal_only_route_floor": diagonal_floor,
        "diagonal_floor_minus_required_cap": diagonal_floor - required_cap,
    }


def encode(value):
    if isinstance(value, Decimal):
        return format(value, "f")
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(item) for item in value]
    return value


def main() -> None:
    result = {
        "status": "PASS",
        "scope": "independent 80-digit decimal cross-check; rigorous acceptance remains with proof audit and rational/Arb enclosures",
        "finite_counterexamples": finite_counterexamples(),
        "analytic_ledger": analytic_ledger(),
    }
    print(json.dumps(encode(result), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
