"""Adversarial finite scan of expectation-level SA03 closure candidates.

This deliberately searches for failures of simple coefficient inequalities.
It reuses exhaustive physical-word expectations and does not claim a
continuous-u or infinite-volume proof.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from sa03_exact_finite import pointwise


def scan_radius(radius: int, grid: int, batch_size: int) -> dict[str, object]:
    lo = 1.0 / (radius + 1.0)
    worst_half = (float("inf"), None)
    worst_compensated = (float("inf"), None)
    worst_residual = (float("inf"), None)
    largest_required_parameter_fraction = (-float("inf"), None)
    for index in range(grid):
        u = lo + (1.0 - lo) * index / (grid - 1)
        row = pointwise(radius, u, batch_size)
        component = row["normalized_components"]
        curvature = component["curvature_minus_8"]
        bregman = component["bregman_phi_prime"]
        parameter = component["parameter_derivative"]
        transport = component["signed_transport"]
        half_margin = transport + 0.5 * parameter
        compensated_margin = bregman + half_margin
        residual = curvature + bregman + parameter + transport
        required_fraction = (-transport - bregman) / parameter if parameter > 0.0 else 0.0
        record = {
            "u": u,
            "curvature_minus_8": curvature,
            "bregman_phi_prime": bregman,
            "parameter_derivative": parameter,
            "signed_transport": transport,
        }
        if half_margin < worst_half[0]:
            worst_half = (half_margin, record)
        if compensated_margin < worst_compensated[0]:
            worst_compensated = (compensated_margin, record)
        if residual < worst_residual[0]:
            worst_residual = (residual, record)
        if required_fraction > largest_required_parameter_fraction[0]:
            largest_required_parameter_fraction = (required_fraction, record)
    return {
        "R": radius,
        "grid_points": grid,
        "worst_transport_plus_half_parameter": {
            "margin": worst_half[0],
            "components": worst_half[1],
        },
        "worst_bregman_plus_transport_plus_half_parameter": {
            "margin": worst_compensated[0],
            "components": worst_compensated[1],
        },
        "worst_complete_residual": {
            "margin": worst_residual[0],
            "components": worst_residual[1],
        },
        "largest_required_parameter_fraction": {
            "fraction": largest_required_parameter_fraction[0],
            "components": largest_required_parameter_fraction[1],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--radii", nargs="+", type=int, default=[1, 3, 5, 7, 9])
    parser.add_argument("--grid", type=int, default=25)
    parser.add_argument("--batch-size", type=int, default=4096)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("sa03_expectation_budget_scan_result.json"),
    )
    args = parser.parse_args()
    results = []
    for radius in args.radii:
        result = scan_radius(radius, args.grid, args.batch_size)
        results.append(result)
        print(
            f"R={radius} half={result['worst_transport_plus_half_parameter']['margin']:+.6e} "
            f"compensated={result['worst_bregman_plus_transport_plus_half_parameter']['margin']:+.6e} "
            f"alpha={result['largest_required_parameter_fraction']['fraction']:.6f}",
            flush=True,
        )
    payload = {
        "status": "FINITE_GRID_COUNTEREXAMPLE_SEARCH",
        "results": results,
        "conclusion": (
            "The coefficient-1/2 transport/parameter inequality is false on the finite grid. "
            "Adding the expected Bregman-phi-prime term survives this scan, but remains unproved."
        ),
        "limitations": [
            "The u grid is finite and binary64; positive margins are not certificates.",
            "Only radii explicitly listed in the receipt are covered.",
        ],
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
