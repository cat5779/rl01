#!/usr/bin/env python3
"""Independent exact replay of the S11 resumed obstruction certificate.

This file does not import the builder.  It reconstructs every rational row and
all load-bearing comparisons directly from the frozen JSON.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path


def pf(text: str) -> F:
    a, b = text.split("/")
    return F(int(a), int(b))


def threshold_ok(delta: F, cutoff: int) -> bool:
    return 4 * delta**3 * (2 - delta) * (cutoff + 1) ** 2 >= (1 - delta**2) ** 2


def ceil_sqrt_fraction(x: F) -> int:
    num, den = x.numerator, x.denominator
    k = isqrt(num // den)
    while k * k * den < num:
        k += 1
    while k and (k - 1) * (k - 1) * den >= num:
        k -= 1
    return k


def min_cut(delta: F) -> int:
    ratio = (1 - delta**2) ** 2 / (4 * delta**3 * (2 - delta))
    m = max(0, ceil_sqrt_fraction(ratio) - 1)
    assert threshold_ok(delta, m)
    assert m == 0 or not threshold_ok(delta, m - 1)
    return m


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("certificate", type=Path)
    args = ap.parse_args()
    data = json.loads(args.certificate.read_text(encoding="utf-8"))
    assert data["status"] == "DISPROVED_ROUTE_LEMMA"
    assert data["all_checks_pass"] is True

    c0 = F(37, 40)
    cstar = F(463, 500)
    step = F(1, 1000)
    l0 = F(3, 40)
    budget = F(3, 200)
    base = F(1, 50)
    assert cstar - c0 == step

    split = data["split_tail_adaptive_family"]
    rows = split["rows"]
    assert len(rows) == 100
    rebuilt = []
    for i, row in enumerate(rows):
        left = l0 * F(i, 200)
        right = l0 * F(i + 1, 200)
        cutoff = min_cut(right)
        ell = l0 - 2 * left
        coeff = F(24 * cutoff**2, 1) / ell**2
        assert row["index"] == i
        assert pf(row["delta_left"]) == left
        assert pf(row["delta_right"]) == right
        assert row["cutoff_floor"] == cutoff
        assert pf(row["ell_upper"]) == ell
        assert pf(row["coefficient_floor"]) == coeff
        rebuilt.append((coeff, i, cutoff))

    coeff, idx, cutoff = min(rebuilt)
    assert coeff == F(366_368_000_000, 1323)
    assert idx == 58 and cutoff == 107
    assert pf(split["minimum_coefficient"]) == coeff
    assert pf(split["strong_margin_width_ceiling"]) == budget / coeff
    assert pf(split["sign_only_width_ceiling"]) == base / coeff
    assert pf(split["payment_for_c0_to_c_star"]) == step * coeff
    assert step * coeff > base

    mode = data["uniform_mode_separable_family"]
    gap = F(80, 83) ** 4
    whole = 120 * F(17, 20) * gap
    center = 120 * c0 * gap
    assert whole == F(4_177_920_000, 47_458_321)
    assert center == F(4_546_560_000, 47_458_321)
    assert pf(mode["whole_legal_shift_coefficient_floor"]) == whole
    assert pf(mode["center_coefficient_floor"]) == center
    assert pf(mode["whole_shift_payment_for_c0_to_c_star"]) == step * whole
    assert pf(mode["center_payment_for_c0_to_c_star"]) == step * center
    assert step * whole > base
    assert pf(mode["minimum_signed_cancellation_needed_per_unit_for_strong_margin"]) == whole - 15

    x = F(37, 1000)
    pc = F(963, 1000)
    pd = F(481, 500)
    b2 = lambda p: -1 / (p * (1 - p))
    base_curv = F(1, 2) * (b2(pd) + b2(x))
    target_curv = F(1, 2) * (b2(pc) + b2(x))
    full = target_curv - base_curv
    assert base_curv == F(-243_875_000, 8_800_857)
    assert target_curv == F(-1_000_000, 35_631)
    assert pf(mode["base_full_curvature_at_witness"]) == base_curv
    assert pf(mode["target_full_curvature_at_witness"]) == target_curv
    assert x == (1 - cstar) / 2
    assert full == F(-3_125_000, 8_800_857)
    assert full / step == F(-3_125_000_000, 8_800_857)
    assert pf(mode["full_entropy_center_response"]) == full
    assert full < 0

    witness_delta = F(1, 50)
    m2 = 120 * step * c0 / (1 + witness_delta) ** 4
    higher = full - m2
    assert m2 == F(231_250, 2_255_067)
    assert higher == F(-1_009_142_506_250, 2_205_169_132_491)
    assert pf(mode["signed_group_witness_gap"]) == witness_delta
    assert pf(mode["signed_group_m2_response"]) == m2
    assert pf(mode["signed_group_modes_m_ge_3_response"]) == higher
    assert pf(mode["signed_group_modes_m_ge_3_per_unit"]) == higher / step

    print("REBUILT_100_BIN_COVER_PASS")
    print("REBUILT_LOW_MODE_CONSTANTS_PASS")
    print("REBUILT_PRODUCT_WITNESS_PASS")
    print("REBUILT_SIGNED_HIGHER_MODE_CANCELLATION_PASS")
    print("INDEPENDENT_EXACT_REPLAY_PASS")


if __name__ == "__main__":
    main()
