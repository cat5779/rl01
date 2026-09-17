#!/usr/bin/env python3
"""Exact replay of Theorem 6.1 on a rigorously non-DPP half-size law.

The theorem checker is imported from the frozen author packet.  The only new
input is a positive law on the six 2-subsets of [4].  It cannot be a complex
rank-2 projection DPP: the magnitudes in the Pluecker relation would be
5/12, 1/24, 1/24, so the largest exceeds the sum of the other two.
"""
from __future__ import annotations

from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
AUTHOR_CHECKER = HERE / "exact_midpoint_check.py"


def load_author_checker():
    spec = importlib.util.spec_from_file_location("author_exact_midpoint_check", AUTHOR_CHECKER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load frozen author checker")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    checker = load_author_checker()
    # Bit masks 0011,0101,1001,0110,1010,1100 correspond to
    # pairs 12,13,14,23,24,34.
    mu = {
        0b0011: F(10, 24),
        0b0101: F(1, 24),
        0b1001: F(1, 24),
        0b0110: F(1, 24),
        0b1010: F(1, 24),
        0b1100: F(10, 24),
    }
    assert sum(mu.values(), F(0)) == 1

    # Exact Pluecker obstruction.  If p_ij=|z_ij|^2 came from a complex
    # decomposable 2-form, z12*z34, z13*z24, z14*z23 would close a triangle.
    dominant_squared = 10 * 10
    other_root_sum_squared = (1 + 1) ** 2
    assert dominant_squared > other_root_sum_squared

    result = checker.check_case(mu, 4, 2, F(19, 20))
    out = {
        "case": "strictly_non_dpp_positive_rational_half_size_law",
        "weights_in_mask_order": {format(mask, "04b"): str(mass) for mask, mass in mu.items()},
        "non_dpp_certificate": {
            "criterion": "rank-2 complex projection DPP weights must satisfy the Pluecker triangle condition",
            "scaled_edge_product_magnitudes": ["10", "1", "1"],
            "strict_violation": "10 > 1 + 1",
        },
        "theorem_6_1_exact_replay": result,
    }
    output = HERE.parent / "evidence" / "strict_non_dpp_exact.json"
    output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
