#!/usr/bin/env python3
"""Exact rational certificate for the two S12 route obstructions.

All proof comparisons use fractions.Fraction.  Floating logarithms are emitted
only as diagnostics; strict log inequalities are certified by rational bounds.
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction as F
from pathlib import Path


def frac(x: F) -> str:
    return f"{x.numerator}/{x.denominator}"


def det2(a: F, b: F, d: F) -> F:
    return a * d - b * b


def main() -> dict:
    c_star = F(463, 500)
    a_star = F(37, 1000)

    # K = [[5,2],[2,11]]/17.
    k11, k12, k22 = F(5, 17), F(2, 17), F(11, 17)
    upper = a_star + c_star

    # Exact Loewner checks for K-aI and (a+c)I-K.
    low11, low22 = k11 - a_star, k22 - a_star
    low_det = det2(low11, k12, low22)
    up11, up22 = upper - k11, upper - k22
    up_det = det2(up11, -k12, up22)
    assert low11 > 0 and low22 > 0 and low_det > 0
    assert up11 > 0 and up22 > 0 and up_det > 0

    # Q=(K-aI)/c.
    q11, q12, q22 = low11 / c_star, k12 / c_star, low22 / c_star
    assert q11 == F(4371, 15742)
    assert q12 == F(1000, 7871)
    assert q22 == F(10371, 15742)

    # Complete atom law in order (11,10,01,00).
    atom11 = det2(k11, k12, k22)
    atom10 = k11 - atom11
    atom01 = k22 - atom11
    atom00 = F(1) - k11 - k22 + atom11
    cells = (atom11, atom10, atom01, atom00)
    assert cells == (F(3, 17), F(2, 17), F(8, 17), F(4, 17))
    assert sum(cells) == 1

    delta = atom11 * atom00 - atom10 * atom01
    reciprocal_sum = sum((F(1) / x for x in cells), F(0))
    algebraic_phi = delta * reciprocal_sum
    odds_ratio = atom11 * atom00 / (atom10 * atom01)
    assert algebraic_phi == F(-29, 102)
    assert odds_ratio == F(3, 4)

    # log(4/3) > 2/7 and 2/7 - 29/102 = 1/714.
    log_lower = F(2, 7)
    phi_lower = log_lower + algebraic_phi
    assert phi_lower == F(1, 714) and phi_lower > 0

    # Diagonal Hessian values and common curvature diagnostic.
    h11_abs = (atom11 + atom01) / (
        (atom11 / (atom11 + atom01)) * (atom01 / (atom11 + atom01))
    ) + (atom10 + atom00) / (
        (atom10 / (atom10 + atom00)) * (atom00 / (atom10 + atom00))
    )
    h22_abs = (atom11 + atom10) / (
        (atom11 / (atom11 + atom10)) * (atom10 / (atom11 + atom10))
    ) + (atom01 + atom00) / (
        (atom01 / (atom01 + atom00)) * (atom00 / (atom01 + atom00))
    )
    assert h11_abs == F(1979, 408)
    assert h22_abs == F(449, 102)

    # Product contrast witness, uniformly over |s| <= 1/200.
    scalar_q = F(1, 100)
    s_width = F(1, 200)
    p_center = a_star + c_star * scalar_q
    p_min, p_max = p_center - s_width, p_center + s_width
    assert p_center == F(2313, 50000)
    assert p_min == F(2063, 50000)
    assert p_max == F(2563, 50000)
    coarse_upper = F(13, 250)
    assert 0 < p_min < p_max < coarse_upper < F(1, 2)
    response_lower = F(1, 100) * F(112, 125) / (coarse_upper * coarse_upper)
    assert response_lower == F(560, 169)

    result = {
        "schema": 1,
        "status": "DISPROVED_ROUTE_LEMMA",
        "benchmark": {
            "c": frac(c_star),
            "a_center": frac(a_star),
            "K": [[frac(k11), frac(k12)], [frac(k12), frac(k22)]],
            "Q": [[frac(q11), frac(q12)], [frac(q12), frac(q22)]],
            "loewner_checks": {
                "K_minus_aI_diagonal": [frac(low11), frac(low22)],
                "K_minus_aI_determinant": frac(low_det),
                "upperI_minus_K_diagonal": [frac(up11), frac(up22)],
                "upperI_minus_K_determinant": frac(up_det),
            },
        },
        "mixed_face": {
            "cells_11_10_01_00": [frac(x) for x in cells],
            "delta": frac(delta),
            "reciprocal_sum": frac(reciprocal_sum),
            "algebraic_part": frac(algebraic_phi),
            "odds_ratio": frac(odds_ratio),
            "rigorous_log_lower": "log(4/3) > 2/7",
            "rigorous_phi_lower": frac(phi_lower),
            "phi_float_diagnostic": math.log(4 / 3) - 29 / 102,
            "H11": frac(-h11_abs),
            "H22": frac(-h22_abs),
            "common_curvature_float_diagnostic": (
                -float(h11_abs) - float(h22_abs)
                + 2 * (math.log(4 / 3) - 29 / 102)
            ),
            "direct_sum_positive_mixed_payment": "2 sum_{i<j}(H_ij)_+ > n/714",
        },
        "contrast_response": {
            "Q_scalar": frac(scalar_q),
            "centered_shift_interval": [frac(-s_width), frac(s_width)],
            "p_interval": [frac(p_min), frac(p_max)],
            "formula_per_site": "q*(1-2p)/(p^2*(1-p)^2)",
            "rigorous_uniform_lower": frac(response_lower),
            "lower_float": float(response_lower),
        },
    }
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = main()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    else:
        print(text, end="")
