#!/usr/bin/env python3
"""Deterministic high-precision replay for the check-2 constants.

This script checks arithmetic and prints decimal values.  The proof of the
matrix and probability inequalities is in RESULT.md; numerical evaluation is
not used as proof.
"""
from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
import json
from pathlib import Path

getcontext().prec = 80


def D(q: Fraction) -> Decimal:
    return Decimal(q.numerator) / Decimal(q.denominator)


def main() -> None:
    c = Fraction(19, 20)
    amin = Fraction(1, 50)
    amax = Fraction(3, 100)
    kappa = Fraction(4753, 3)
    dstar = kappa - 1
    tau = ((kappa - 1) / (kappa + 1)) ** 2
    assert tau == Fraction(2375 * 2375, 2378 * 2378)

    td = D(tau)
    gd = Decimal(2) * (-(Decimal(1) - td).ln() - td)
    rhod = Decimal(2) * (
        td + td / (Decimal(1) - td) + Decimal(2) * (Decimal(1) - td).ln()
    )
    cg = gd / td
    crho = rhod / td
    dd = D(dstar)

    c_w = crho * dd
    c_e = cg * cg * dd * dd / Decimal(64)
    c_theta = Decimal(3) * crho * dd * dd / Decimal(32)
    c_s = (Decimal(50) / Decimal(7) + cg * dd / Decimal(4)) ** 2
    c_abs = c_e + c_w / Decimal(2) + c_s
    vstar = Fraction(291, 10000)

    # Endpoint condition-number checks.
    def kap(a: Fraction) -> Fraction:
        return (a + c) * (1 - a) / (a * (1 - a - c))

    assert kap(amin) == kappa
    assert kap(amax) == kappa
    assert Fraction(49, 2500) == amin * (1 - amin)

    record = {
        "scope": "Arithmetic replay only; analytical proof is in RESULT.md.",
        "c": str(c),
        "J": [str(amin), str(amax)],
        "kappa_star_exact": str(kappa),
        "D_star_exact": str(dstar),
        "tau_star_exact": str(tau),
        "v_star_exact": str(vstar),
        "kappa_star_decimal": str(D(kappa)),
        "tau_star_decimal": str(td),
        "C_g": str(cg),
        "C_rho": str(crho),
        "C_W": str(c_w),
        "C_E": str(c_e),
        "C_Theta": str(c_theta),
        "C_S": str(c_s),
        "C_abs": str(c_abs),
    }

    out = Path(__file__).resolve().parents[1] / "replay" / "constants.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
