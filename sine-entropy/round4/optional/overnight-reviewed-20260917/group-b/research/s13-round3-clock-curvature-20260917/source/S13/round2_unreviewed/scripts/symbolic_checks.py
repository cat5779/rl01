#!/usr/bin/env python3
"""Exact symbolic checks for the new S13 formulas."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def run(output: Path) -> None:
    n, k, l = sp.symbols("n k l", positive=True)
    lam, v = sp.symbols("lambda v", positive=True)
    m = l * (1 + lam) / 2
    ej2 = v + m**2
    h_expect = (
        (ej2 - m + l**2 - 2 * l * m + ej2 - l + m) / (k * (k - 1))
        - 2 * (l * m - ej2) / k**2
    )
    alpha = l * (l - 1) / (k * (k - 1))
    theta = sp.factor(h_expect / alpha)
    claimed = sp.factor(
        lam**2
        + (4 * (2 * k - 1) * v - l * (2 * k - l) * (1 - lam**2))
        / (2 * k * l * (l - 1))
    )

    x, z, L = sp.symbols("x z L", positive=True)
    relation = x * (z - 1) * L**2 - (z + 1) * L + (1 - x) * (z - 1)
    Lx = -sp.diff(relation, x) / sp.diff(relation, L)
    d = L**2 * (
        -2 * sp.log(L)
        - (1 - L**2) * (1 - 2 * x) / (1 - x * (1 + L**2))
    )
    f = 4 * x**2 * d
    z_center = ((1 + L) / (1 - L)) ** 2
    fx_center = sp.simplify(
        (sp.diff(f, x) + sp.diff(f, L) * Lx).subs({x: sp.Rational(1, 2), z: z_center})
    )
    lx_center = sp.simplify(Lx.subs({x: sp.Rational(1, 2), z: z_center}))

    p = x * (1 + L)
    q = x * (1 - L)
    A = p * (1 - p)
    B = q * (1 - q)
    sigma2 = sp.Rational(1, 2) * A * B / (A + B)
    variance_correction = sp.factor(
        (4 * sigma2 - x * (1 - x) * (1 - L**2)) / x**2
    )
    variance_claimed = sp.factor(
        L**2 * (1 - L**2) * (1 - 2 * x) / (1 - x * (1 + L**2))
    )

    data = {
        "theta_variance_identity": bool(sp.simplify(theta - claimed) == 0),
        "variance_correction_identity": bool(
            sp.simplify(variance_correction - variance_claimed) == 0
        ),
        "center_lambda_x": str(lx_center),
        "center_f_x": str(fx_center),
        "center_lambda_x_expected": "-2*L",
        "center_f_x_expected": "8*L**2",
        "center_derivatives_pass": bool(lx_center == -2 * L and fx_center == 8 * L**2),
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    run(args.output)


if __name__ == "__main__":
    main()
