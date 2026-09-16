#!/usr/bin/env python3
"""Exact rational certificate for the high-contrast response constants.

Writes UTF-8/LF JSON to a caller-selected output path.  It never modifies the
frozen evidence directory.
"""
from __future__ import annotations

import argparse
import json
from decimal import Decimal, ROUND_FLOOR, ROUND_CEILING, getcontext
from fractions import Fraction
from pathlib import Path


def frac_text(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def decimal_interval(x: Fraction, places: int = 18) -> tuple[str, str]:
    getcontext().prec = places + 80
    value = Decimal(x.numerator) / Decimal(x.denominator)
    quantum = Decimal(1).scaleb(-places)
    lo = value.quantize(quantum, rounding=ROUND_FLOOR)
    hi = value.quantize(quantum, rounding=ROUND_CEILING)
    return format(lo, "f"), format(hi, "f")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    c0 = Fraction(37, 40)
    eta = Fraction(1, 10**13)
    c1 = c0 + eta
    delta = Fraction(9, 500)
    half_width = Fraction(1, 200)
    ell_exact = 1 - c1 - 2 * delta
    ell_lower = Fraction(389, 10_000)
    sigma_lower = Fraction(24, 25)
    r = Fraction(1, 1)
    r = (1 - delta) / (1 + delta)  # 491/509
    epsilon = Fraction(1, 500_000_000_000)  # 2e-12
    M = 768
    A = 2

    # Geometry: sigma^2 = 1-(2w/ell)^2.  The lower ell bound implies
    # sigma^2 > 1-(100/389)^2 > (24/25)^2.
    sigma_sq_proxy = 1 - Fraction(100, 389) ** 2
    sigma_sq_lower = sigma_lower**2

    one_minus_r = 1 - r
    rp = r ** (M + 1)
    V = rp / ((M + 1) * one_minus_r)
    S0 = rp / one_minus_r
    S1 = rp * ((M + 1) - M * r) / (one_minus_r**2)

    pref_low = (
        Fraction(16 * M * M, 1) / (ell_lower**2 * sigma_lower**2)
        + Fraction(8 * M, 1) / (ell_lower**2 * sigma_lower**3)
    )
    tail = A * (
        Fraction(16, 1) * S1 / (ell_lower**2 * sigma_lower**2)
        + Fraction(8, 1) * S0 / (ell_lower**2 * sigma_lower**3)
    )
    response = pref_low * (epsilon + A * V) + tail
    response_target = Fraction(3, 200)
    final_curvature = -Fraction(1, 50) + response_target

    # Elementary logarithm bounds used for b(eta/2): e>2 and e^(5/2)>10.
    # The latter is certified by the first five nonzero Taylor terms through k=4.
    x = Fraction(5, 2)
    exp_5_2_partial = sum((x**k) / __import__("math").factorial(k) for k in range(5))

    checks = {
        "ell_exact_gt_lower": ell_exact > ell_lower,
        "sigma_proxy_gt_lower": sigma_sq_proxy > sigma_sq_lower,
        "exp_5_2_partial_gt_10": exp_5_2_partial > 10,
        "r_is_491_over_509": r == Fraction(491, 509),
        "response_lt_3_over_200": response < response_target,
        "transported_curvature_at_most_minus_1_over_200": final_curvature == -Fraction(1, 200),
    }
    if not all(checks.values()):
        raise SystemExit(f"certificate check failed: {checks}")

    response_lo, response_hi = decimal_interval(response, 18)
    deficit = response_target - response
    deficit_lo, deficit_hi = decimal_interval(deficit, 18)

    payload = {
        "certificate_type": "exact_rational_high_contrast_response",
        "parameters": {
            "c0": frac_text(c0),
            "c1": frac_text(c1),
            "contrast_width": frac_text(eta),
            "outer_delta": frac_text(delta),
            "inner_half_width": frac_text(half_width),
            "M": M,
            "coefficient_envelope_A": A,
            "r": frac_text(r),
            "epsilon_value_bound": frac_text(epsilon),
            "ell_lower": frac_text(ell_lower),
            "sigma_lower": frac_text(sigma_lower),
        },
        "checks": checks,
        "exact": {
            "ell_exact": frac_text(ell_exact),
            "sigma_squared_proxy": frac_text(sigma_sq_proxy),
            "sigma_squared_lower": frac_text(sigma_sq_lower),
            "exp_5_2_taylor_k0_to_k4": frac_text(exp_5_2_partial),
            "V_M": frac_text(V),
            "S0_M": frac_text(S0),
            "S1_M": frac_text(S1),
            "response_bound": frac_text(response),
            "response_target": frac_text(response_target),
            "response_deficit": frac_text(deficit),
            "final_curvature_upper_after_reviewed_margin": frac_text(final_curvature),
        },
        "outward_decimal_intervals": {
            "response_bound": [response_lo, response_hi],
            "response_deficit": [deficit_lo, deficit_hi],
        },
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
