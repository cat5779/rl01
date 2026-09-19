#!/usr/bin/env python3
"""Exact rational sign certificate for the smallest S71 acceleration example.

The model is the genuine adjacent two-site half-density sine DPP with
c=93/100 and the legal midpoint a=(1-c)/2=7/200.  Only the elementary bounds
3 < pi < 22/7 are used for the rational numerical enclosure.  The decisive
signs are symbolic for every 0<d<1/4.
"""
from __future__ import annotations

import json
import argparse
from fractions import Fraction as F
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    c = F(93, 100)
    a = F(7, 200)
    u = a + c / 2
    assert u == F(1, 2)

    # d=c^2/pi^2.  From pi<22/7 and pi>3:
    d_lower = c * c * F(49, 484)
    d_upper = c * c / 9
    assert 0 < d_lower < d_upper < F(1, 4)

    # C_acc = -8*atanh(4d).  For 0<x<1,
    # x < atanh(x) < x/(1-x^2).
    cacc_lower = -32 * d_upper / (1 - 16 * d_upper * d_upper)
    cacc_upper = -32 * d_lower
    assert cacc_lower < cacc_upper < 0

    # D_F = 32d/(1-4d), an increasing rational function of d.
    df_lower = 32 * d_lower / (1 - 4 * d_lower)
    df_upper = 32 * d_upper / (1 - 4 * d_upper)
    assert 0 < df_lower < df_upper

    # M''(d)=2/(1/4-d)+4log((1/4-d)/(1/4+d))-8.
    # M''(0)=0 and its derivative with respect to d is
    # 4d/[(1/4-d)^2(1/4+d)]>0, hence M''(d)>0 for d>0.
    derivative_numerator_lower = 4 * d_lower
    assert derivative_numerator_lower > 0

    output = {
        "status": "EXACT_SIGN_CERTIFICATE",
        "actual_model": {
            "rho": "1/2",
            "c": str(c),
            "a": str(a),
            "adjacent_blocks": [1, 1],
            "marginal_u": str(u),
            "correlation_d": "c^2/pi^2",
        },
        "rational_inputs": {
            "pi_lower": "3",
            "pi_upper": "22/7",
            "d_lower": str(d_lower),
            "d_upper": str(d_upper),
        },
        "exact_formulas": {
            "C_acc": "4 log((1/4-d)/(1/4+d)) = -8 atanh(4d) < 0",
            "D_F": "2/(1/4-d)-8 = 32d/(1-4d) > 0",
            "M_second": "D_F+C_acc",
            "d_derivative_of_M_second": "4d/((1/4-d)^2(1/4+d)) > 0",
            "M_second_at_d_zero": "0",
        },
        "rational_enclosures": {
            "C_acc_lower": str(cacc_lower),
            "C_acc_upper": str(cacc_upper),
            "D_F_lower": str(df_lower),
            "D_F_upper": str(df_upper),
        },
        "decimal_display_only": {
            "C_acc_interval": [float(cacc_lower), float(cacc_upper)],
            "D_F_interval": [float(df_lower), float(df_upper)],
        },
        "certified_conclusions": {
            "C_acc_nonnegative": False,
            "D_F_positive": True,
            "M_second_positive": True,
        },
    }
    rendered = json.dumps(output, indent=2) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
