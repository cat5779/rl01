"""Paired MCMC scout across the SA04 central sqrt(n) window.

The central-only script identifies the likely inverse-root scale.  This helper
keeps the same paired deletion and bidirectional bridge estimators but permits
layers l=k-offset, which is the actual input needed by the weighted W_n bound.
"""

from __future__ import annotations

import argparse
import json
from math import sqrt
from pathlib import Path

import numpy as np

from sa04_bridge_mcmc_scout import (
    Density,
    original_time,
    run_bridge,
    run_deletion_loss,
)


def combine_bridge(forward: dict[str, object], reverse: dict[str, object]) -> tuple[float, float]:
    forward_variance = float(forward["batch_se"]) ** 2
    reverse_variance = float(reverse["batch_se"]) ** 2
    forward_weight = 1.0 / forward_variance
    reverse_weight = 1.0 / reverse_variance
    estimate = (
        forward_weight * float(forward["E_k_estimate"])
        + reverse_weight * float(reverse["E_k_estimate"])
    ) / (forward_weight + reverse_weight)
    return estimate, sqrt(1.0 / (forward_weight + reverse_weight))


def diagnose_layer(n: int, layer: int, args: argparse.Namespace) -> dict[str, object]:
    previous = layer - 1
    seed = args.seed + 1000 * n + layer
    rng = np.random.default_rng(seed)
    earlier = Density(n, previous, original_time(n, previous))
    later = Density(n, previous, original_time(n, layer))
    forward = run_bridge(
        earlier, later, True, args.chains, args.burn, args.draws, args.thin, rng
    )
    reverse = run_bridge(
        later, earlier, False, args.chains, args.burn, args.draws, args.thin, rng
    )
    bridge, bridge_se = combine_bridge(forward, reverse)
    current = Density(n, layer, original_time(n, layer))
    deletion = run_deletion_loss(
        current, later, args.chains, args.burn, args.draws, args.thin, rng
    )
    difference = float(deletion["A_k_estimate"]) - bridge
    difference_se = sqrt(float(deletion["batch_se"]) ** 2 + bridge_se**2)
    return {
        "n": n,
        "k": n // 2,
        "layer": layer,
        "offset": n // 2 - layer,
        "scaled_offset": (n // 2 - layer) / sqrt(n),
        "seed": seed,
        "forward_bridge": forward,
        "reverse_bridge": reverse,
        "paired_deletion_loss": deletion,
        "E_l_estimate": bridge,
        "E_l_batch_se": bridge_se,
        "d_l_estimate": difference,
        "d_l_naive_se": difference_se,
        "sqrt_n_d_l": sqrt(n) * difference,
        "sqrt_n_d_l_naive_se": sqrt(n) * difference_se,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--offsets", nargs="+", type=int, default=[0, 2, 4, 6, 8])
    parser.add_argument("--chains", type=int, default=4)
    parser.add_argument("--burn", type=int, default=1500)
    parser.add_argument("--draws", type=int, default=4000)
    parser.add_argument("--thin", type=int, default=4)
    parser.add_argument("--seed", type=int, default=20260918)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("sa04_window_mcmc_result.json"),
    )
    args = parser.parse_args()
    if args.n % 2 or args.n < 8:
        raise SystemExit("n must be even and at least 8")
    layers = [args.n // 2 - offset for offset in args.offsets]
    if any(layer < 3 for layer in layers):
        raise SystemExit("every requested layer must be at least 3")
    results = []
    limitations = [
        "Batch errors do not certify Markov-chain mixing.",
        "The scan is finite and does not prove a uniform central-window bound.",
        "The corrected-law conclusions do not transfer automatically to the true output law.",
    ]
    for layer in layers:
        result = diagnose_layer(args.n, layer, args)
        results.append(result)
        payload = {"status": "EXPLORATORY_WINDOW_MCMC", "results": results, "limitations": limitations}
        args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(
            f"n={args.n} offset={result['offset']} A={result['paired_deletion_loss']['A_k_estimate']:+.6f} "
            f"E={result['E_l_estimate']:+.6f} d={result['d_l_estimate']:+.6f} "
            f"sqrt(n)d={result['sqrt_n_d_l']:+.6f}",
            flush=True,
        )


if __name__ == "__main__":
    main()
