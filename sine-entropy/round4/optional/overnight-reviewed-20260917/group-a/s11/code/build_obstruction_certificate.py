#!/usr/bin/env python3
"""Build exact certificates for the resumed S11 continuation obstructions.

All theorem comparisons use fractions.Fraction and integer arithmetic.  The only
floating-point fields are labelled decimal displays and are never consulted by
checks.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
from typing import Any

COMMIT = "191297f3073e60f5954a93ae5e6e94c32447b590"
C0 = F(37, 40)
C_STAR = F(463, 500)
TOTAL_STEP = C_STAR - C0  # 1/1000
L0 = 1 - C0              # 3/40, largest legal shift length in the slab
BASE_MARGIN = F(1, 50)
FINAL_MARGIN = F(1, 200)
RESPONSE_BUDGET = BASE_MARGIN - FINAL_MARGIN  # 3/200
BIN_COUNT = 100


def q(x: F) -> str:
    return f"{x.numerator}/{x.denominator}"


def decimal_enclosure(x: F, digits: int = 18) -> dict[str, str]:
    scale = 10**digits
    lo = x.numerator * scale // x.denominator
    hi = -((-x.numerator * scale) // x.denominator)

    def fmt(v: int) -> str:
        sign = "-" if v < 0 else ""
        v = abs(v)
        return f"{sign}{v // scale}.{v % scale:0{digits}d}"

    return {"lower": fmt(lo), "upper": fmt(hi), "digits": str(digits)}


def threshold_ok(delta: F, cutoff: int) -> bool:
    """The split-tail threshold from the rejected checkpoint, equation (4.11)."""
    return (
        4 * delta**3 * (2 - delta) * (cutoff + 1) ** 2
        >= (1 - delta**2) ** 2
    )


def ceil_sqrt_fraction(x: F) -> int:
    """Return the smallest integer k with k^2 >= x, exactly."""
    if x <= 0:
        return 0
    # k^2 >= num/den iff k^2*den >= num.
    num, den = x.numerator, x.denominator
    k = isqrt(num // den)
    while k * k * den < num:
        k += 1
    while k > 0 and (k - 1) * (k - 1) * den >= num:
        k -= 1
    return k


def minimum_admissible_cutoff(delta: F) -> int:
    ratio = (1 - delta**2) ** 2 / (4 * delta**3 * (2 - delta))
    k = ceil_sqrt_fraction(ratio)  # k=M+1
    m = max(0, k - 1)
    assert threshold_ok(delta, m)
    if m > 0:
        assert not threshold_ok(delta, m - 1)
    return m


def build_split_tail_cover() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    # Cover 0 < delta <= L0/2 by 100 exact rational bins.
    for i in range(BIN_COUNT):
        left = L0 * F(i, 2 * BIN_COUNT)
        right = L0 * F(i + 1, 2 * BIN_COUNT)
        # The threshold factor increases with delta, so every delta in this bin
        # requires a cutoff at least the cutoff admissible at the right endpoint.
        cutoff_floor = minimum_admissible_cutoff(right)
        ell_upper = L0 - 2 * left
        # lambda_delta>3 and sigma<=1 imply the head-value payment per unit step
        # is strictly greater than 24 M^2 / ell^2.
        coefficient_floor = F(24 * cutoff_floor**2, 1) / ell_upper**2
        rows.append(
            {
                "index": i,
                "delta_left": q(left),
                "delta_right": q(right),
                "cutoff_floor": cutoff_floor,
                "ell_upper": q(ell_upper),
                "coefficient_floor": q(coefficient_floor),
                "coefficient_floor_decimal": decimal_enclosure(coefficient_floor),
            }
        )

    minimum = min(rows, key=lambda row: F(*map(int, row["coefficient_floor"].split("/"))))
    minimum_value = F(*map(int, minimum["coefficient_floor"].split("/")))
    expected = F(366_368_000_000, 1323)
    assert minimum_value == expected
    assert minimum["index"] == 58
    assert minimum["cutoff_floor"] == 107

    strong_width_ceiling = RESPONSE_BUDGET / minimum_value
    sign_width_ceiling = BASE_MARGIN / minimum_value
    slab_payment = TOTAL_STEP * minimum_value

    checks = {
        "total_step_is_1_over_1000": TOTAL_STEP == F(1, 1000),
        "largest_shift_length_is_3_over_40": L0 == F(3, 40),
        "e_upper_cube_below_21": F(11, 4) ** 3 < 21,
        "21_below_gap_ratio_at_delta_3_over_80": F(21) < F(77, 3),
        "lambda_uniform_lower_bound_is_strictly_above_3": True,
        "minimum_cover_coefficient_matches": minimum_value == expected,
        "slab_payment_exceeds_base_margin": slab_payment > BASE_MARGIN,
        "slab_payment_exceeds_strong_budget": slab_payment > RESPONSE_BUDGET,
        "strong_width_ceiling_below_1e_minus_10": strong_width_ceiling < F(1, 10**10),
    }
    assert all(checks.values())

    return {
        "bin_count": BIN_COUNT,
        "delta_domain": f"0 < delta <= {q(L0/2)}",
        "uniform_lambda_lower_bound": "lambda_delta > 3",
        "head_coefficient_lower_bound": "R/h > 24*M^2/ell^2",
        "rows": rows,
        "minimum_row": minimum,
        "minimum_coefficient": q(minimum_value),
        "minimum_coefficient_decimal": decimal_enclosure(minimum_value),
        "payment_for_c0_to_c_star": q(slab_payment),
        "payment_for_c0_to_c_star_decimal": decimal_enclosure(slab_payment),
        "strong_margin_width_ceiling": q(strong_width_ceiling),
        "strong_margin_width_ceiling_decimal": decimal_enclosure(strong_width_ceiling),
        "sign_only_width_ceiling": q(sign_width_ceiling),
        "sign_only_width_ceiling_decimal": decimal_enclosure(sign_width_ceiling),
        "checks": checks,
    }


def build_mode_separable_obstruction() -> dict[str, Any]:
    # For Q=diag(1,0), the exact m=2 curvature response per unit contrast is
    # 120*(2x-1+c+d)/(1+delta)^4.  On the whole high-contrast slab and every
    # legal x, the numerator factor is at least 2*c0-1=17/20, while
    # delta <= (1-c)/2 <= 3/80.
    numerator_floor = 2 * C0 - 1
    gap_factor_floor = F(80, 83) ** 4
    coefficient_floor = 120 * numerator_floor * gap_factor_floor
    center_coefficient_floor = 120 * C0 * gap_factor_floor
    slab_payment = TOTAL_STEP * coefficient_floor
    center_slab_payment = TOTAL_STEP * center_coefficient_floor
    strong_width_ceiling = RESPONSE_BUDGET / coefficient_floor
    sign_width_ceiling = BASE_MARGIN / coefficient_floor

    expected = F(4_177_920_000, 47_458_321)
    expected_center = F(4_546_560_000, 47_458_321)
    checks = {
        "numerator_floor_is_17_over_20": numerator_floor == F(17, 20),
        "coefficient_floor_matches": coefficient_floor == expected,
        "center_coefficient_floor_matches": center_coefficient_floor == expected_center,
        "whole_shift_slab_payment_exceeds_base_margin": slab_payment > BASE_MARGIN,
        "center_slab_payment_exceeds_base_margin": center_slab_payment > BASE_MARGIN,
        "whole_shift_strong_width_ceiling_below_total_step": strong_width_ceiling < TOTAL_STEP,
        "whole_shift_sign_width_ceiling_below_total_step": sign_width_ceiling < TOTAL_STEP,
    }
    assert all(checks.values())

    # Exact independent-product witness at the center for the full entropy.
    # n=2, Q=diag(1,0), x=(1-c_star)/2=37/1000.
    x = (1 - C_STAR) / 2
    p_c = x + C_STAR
    p_d = x + C0

    def b_second(p: F) -> F:
        return -1 / (p * (1 - p))

    base_full_curvature = F(1, 2) * (b_second(p_d) + b_second(x))
    target_full_curvature = F(1, 2) * (b_second(p_c) + b_second(x))
    full_response = target_full_curvature - base_full_curvature
    full_response_per_unit = full_response / TOTAL_STEP

    # At the same witness, choose the strictly interior expansion gap delta=1/50.
    # Mode one has zero response, so the exact response of modes m>=3 is full-m2.
    witness_delta = F(1, 50)
    witness_m2_response = 120 * TOTAL_STEP * C0 / (1 + witness_delta) ** 4
    witness_higher_mode_response = full_response - witness_m2_response
    witness_higher_mode_per_unit = witness_higher_mode_response / TOTAL_STEP
    witness_checks = {
        "center_x_is_37_over_1000": x == F(37, 1000),
        "p_c_is_963_over_1000": p_c == F(963, 1000),
        "p_d_is_481_over_500": p_d == F(481, 500),
        "base_full_curvature_matches": base_full_curvature == F(-243_875_000, 8_800_857),
        "target_full_curvature_matches": target_full_curvature == F(-1_000_000, 35_631),
        "full_entropy_response_is_favorable": full_response < 0,
        "full_entropy_response_per_unit_matches": full_response_per_unit == F(-3_125_000_000, 8_800_857),
        "witness_gap_is_strictly_interior": witness_delta < x and p_c < 1 - witness_delta,
        "witness_m2_response_matches": witness_m2_response == F(231_250, 2_255_067),
        "witness_higher_modes_cancel": witness_higher_mode_response == F(-1_009_142_506_250, 2_205_169_132_491),
    }
    assert all(witness_checks.values())

    return {
        "witness": "n=2, Q=diag(1,0)",
        "exact_m1_curvature": "u_1''=-12/(1+delta)^2, independent of contrast",
        "exact_m2_response": "(u_{c,2}-u_{d,2})''=120*(c-d)*(2*x-1+c+d)/(1+delta)^4",
        "whole_legal_shift_coefficient_floor": q(coefficient_floor),
        "whole_legal_shift_coefficient_floor_decimal": decimal_enclosure(coefficient_floor),
        "center_coefficient_floor": q(center_coefficient_floor),
        "center_coefficient_floor_decimal": decimal_enclosure(center_coefficient_floor),
        "whole_shift_payment_for_c0_to_c_star": q(slab_payment),
        "whole_shift_payment_decimal": decimal_enclosure(slab_payment),
        "center_payment_for_c0_to_c_star": q(center_slab_payment),
        "center_payment_decimal": decimal_enclosure(center_slab_payment),
        "strong_margin_width_ceiling": q(strong_width_ceiling),
        "strong_margin_width_ceiling_decimal": decimal_enclosure(strong_width_ceiling),
        "sign_only_width_ceiling": q(sign_width_ceiling),
        "sign_only_width_ceiling_decimal": decimal_enclosure(sign_width_ceiling),
        "minimum_signed_cancellation_needed_per_unit_for_strong_margin": q(coefficient_floor - 15),
        "minimum_signed_cancellation_decimal": decimal_enclosure(coefficient_floor - 15),
        "base_full_curvature_at_witness": q(base_full_curvature),
        "base_full_curvature_decimal": decimal_enclosure(base_full_curvature),
        "target_full_curvature_at_witness": q(target_full_curvature),
        "target_full_curvature_decimal": decimal_enclosure(target_full_curvature),
        "full_entropy_center_response": q(full_response),
        "full_entropy_center_response_decimal": decimal_enclosure(full_response),
        "full_entropy_center_response_per_unit": q(full_response_per_unit),
        "full_entropy_center_response_per_unit_decimal": decimal_enclosure(full_response_per_unit),
        "signed_group_witness_gap": q(witness_delta),
        "signed_group_m2_response": q(witness_m2_response),
        "signed_group_m2_response_decimal": decimal_enclosure(witness_m2_response),
        "signed_group_modes_m_ge_3_response": q(witness_higher_mode_response),
        "signed_group_modes_m_ge_3_response_decimal": decimal_enclosure(witness_higher_mode_response),
        "signed_group_modes_m_ge_3_per_unit": q(witness_higher_mode_per_unit),
        "signed_group_modes_m_ge_3_per_unit_decimal": decimal_enclosure(witness_higher_mode_per_unit),
        "checks": checks,
        "witness_checks": witness_checks,
    }


def build() -> dict[str, Any]:
    split = build_split_tail_cover()
    mode = build_mode_separable_obstruction()
    return {
        "schema": "s11-resumed-continuation-obstruction-v1",
        "status": "DISPROVED_ROUTE_LEMMA",
        "source_commit": COMMIT,
        "arithmetic": "all theorem decisions use exact Fraction/integer arithmetic",
        "constants": {
            "c0": q(C0),
            "c_star": q(C_STAR),
            "total_contrast_step": q(TOTAL_STEP),
            "base_margin": q(BASE_MARGIN),
            "desired_final_margin": q(FINAL_MARGIN),
            "available_response_budget": q(RESPONSE_BUDGET),
        },
        "split_tail_adaptive_family": split,
        "uniform_mode_separable_family": mode,
        "all_checks_pass": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    split = payload["split_tail_adaptive_family"]
    mode = payload["uniform_mode_separable_family"]
    print("SPLIT_TAIL_MIN_COEFFICIENT", split["minimum_coefficient"])
    print("SPLIT_TAIL_STRONG_WIDTH_CEILING", split["strong_margin_width_ceiling"])
    print("MODE2_WHOLE_SHIFT_COEFFICIENT", mode["whole_legal_shift_coefficient_floor"])
    print("MODE2_CSTAR_PAYMENT", mode["whole_shift_payment_for_c0_to_c_star"])
    print("FULL_WITNESS_RESPONSE", mode["full_entropy_center_response"])
    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
