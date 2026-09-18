"""Importance-sampling scout for the SA04 central bridge entropy cost.

The exact layer density is evaluated from DPP overlap-count polynomials, while
Metropolis chains sample from that density rather than from the uniform layer.
This avoids the rare-event failure of naive uniform-subset Monte Carlo.

Exploratory only: mixing and floating-point errors are diagnosed but not
certified.
"""

from __future__ import annotations

import argparse
import json
from math import comb, exp, log, sqrt
from pathlib import Path

import numpy as np

from sa04_central_scale import (
    birth_death_generator,
    original_time,
    poisson_binomial,
    projection_matrix,
    stationary_shell_law,
)


def relaxed_chain_law(n: int, layer: int, time: float) -> np.ndarray:
    generator = birth_death_generator(n, layer)
    uniform_rate = float(np.max(-np.diag(generator)))
    transition = np.eye(layer + 1) + generator / uniform_rate
    if transition.min() < -2e-15:
        raise AssertionError(f"invalid uniformized transition: min={transition.min()}")
    transition[transition < 0.0] = 0.0
    poisson_mean = uniform_rate * time
    state = np.zeros(layer + 1, dtype=np.float64)
    state[0] = 1.0
    weight = exp(-poisson_mean)
    cumulative = weight
    law = weight * state
    for jump_count in range(1, 10_000):
        state = state @ transition
        weight *= poisson_mean / jump_count
        law += weight * state
        cumulative += weight
        if jump_count > poisson_mean and 1.0 - cumulative < 2e-15:
            break
    else:
        raise AssertionError("uniformization did not converge")
    law[np.abs(law) < 1e-16] = 0.0
    if law.min() < -1e-15:
        raise AssertionError(f"unstable uniformized chain law: min={law.min()}")
    return law / law.sum()


class Density:
    def __init__(self, n: int, layer: int, time: float):
        self.n = n
        self.layer = layer
        self.projection = projection_matrix(n)
        shell = np.array(
            [comb(n // 2, layer - radius) * comb(n // 2, radius) for radius in range(layer + 1)],
            dtype=np.float64,
        )
        self.kernel = relaxed_chain_law(n, layer, time) / shell
        self.scale = float(comb(n, layer))
        self._cache: dict[tuple[int, ...], float] = {}
        self._cache_limit = 200_000

    def log_density(self, state: tuple[int, ...]) -> float:
        cached = self._cache.get(state)
        if cached is not None:
            return cached
        principal = self.projection[np.ix_(state, state)]
        overlap = poisson_binomial(np.linalg.eigvalsh(principal))[::-1]
        value = self.scale * float(overlap @ self.kernel)
        if value <= 0.0:
            raise AssertionError(f"non-positive density at {state}: {value}")
        result = log(value)
        if len(self._cache) < self._cache_limit:
            self._cache[state] = result
        return result


def summarize_batches(values: list[float]) -> tuple[float, float]:
    array = np.array(values, dtype=np.float64)
    return float(array.mean()), float(array.std(ddof=1) / sqrt(len(array)))


def split_rhat(chain_batches: list[list[float]]) -> float:
    usable = min(len(values) for values in chain_batches)
    if usable < 4:
        return float("nan")
    usable -= usable % 2
    split = []
    for values in chain_batches:
        array = np.asarray(values[:usable], dtype=np.float64)
        split.extend([array[: usable // 2], array[usable // 2 :]])
    matrix = np.stack(split)
    length = matrix.shape[1]
    within = float(np.mean(np.var(matrix, axis=1, ddof=1)))
    between = float(length * np.var(np.mean(matrix, axis=1), ddof=1))
    if within == 0.0:
        return 1.0 if between == 0.0 else float("inf")
    variance = (length - 1.0) * within / length + between / length
    return sqrt(variance / within)


def initial_states(n: int, layer: int, chains: int, rng: np.random.Generator) -> list[tuple[int, ...]]:
    states: list[tuple[int, ...]] = []
    alternating = list(range(0, n, 2))
    for chain in range(chains):
        if chain < 2:
            shifted = [((value + chain) % n) for value in alternating]
            state = tuple(sorted(shifted[:layer]))
        else:
            state = tuple(sorted(rng.choice(n, size=layer, replace=False).tolist()))
        states.append(state)
    return states


def run_bridge(
    target: Density,
    other: Density,
    target_is_earlier: bool,
    chains: int,
    burn: int,
    draws: int,
    thin: int,
    rng: np.random.Generator,
) -> dict[str, object]:
    n = target.n
    layer = target.layer
    bridge_batches: list[float] = []
    weight_batches: list[float] = []
    ess_batches: list[float] = []
    acceptances = 0
    proposals = 0
    chain_estimates: list[float] = []
    chain_bridge_batches: list[list[float]] = []
    target_entropy_batches: list[float] = []
    other_entropy_batches: list[float] = []

    for state in initial_states(n, layer, chains, rng):
        occupied = set(state)
        log_value = target.log_density(state)
        target_logs: list[float] = []
        other_logs: list[float] = []
        total_steps = burn + draws * thin
        for step in range(total_steps):
            leaving = int(rng.choice(tuple(occupied)))
            outside = tuple(index for index in range(n) if index not in occupied)
            entering = int(rng.choice(outside))
            proposal_set = occupied.copy()
            proposal_set.remove(leaving)
            proposal_set.add(entering)
            proposal = tuple(sorted(proposal_set))
            proposal_log = target.log_density(proposal)
            proposals += 1
            if log(rng.random()) < min(0.0, proposal_log - log_value):
                occupied = proposal_set
                log_value = proposal_log
                acceptances += 1
            if step >= burn and (step - burn) % thin == 0:
                current = tuple(sorted(occupied))
                target_logs.append(log_value)
                other_logs.append(other.log_density(current))
        target_values = np.array(target_logs, dtype=np.float64)
        other_values = np.array(other_logs, dtype=np.float64)
        batch_size = max(10, len(target_values) // 20)
        chain_batch_estimates: list[float] = []
        for start in range(0, len(target_values) - batch_size + 1, batch_size):
            target_batch = target_values[start : start + batch_size]
            other_batch = other_values[start : start + batch_size]
            weights = np.exp(other_batch - target_batch)
            target_entropy = float(target_batch.mean())
            other_entropy = float(np.dot(weights, other_batch) / weights.sum())
            estimate = (
                target_entropy - other_entropy
                if target_is_earlier
                else other_entropy - target_entropy
            )
            bridge_batches.append(estimate)
            chain_batch_estimates.append(estimate)
            target_entropy_batches.append(target_entropy)
            other_entropy_batches.append(other_entropy)
            weight_batches.append(float(weights.mean()))
            ess_batches.append(float(weights.sum() ** 2 / np.dot(weights, weights)))
        chain_estimates.append(float(np.mean(chain_batch_estimates)))
        chain_bridge_batches.append(chain_batch_estimates)

    batch_array = np.array(bridge_batches, dtype=np.float64)
    target_mean, target_se = summarize_batches(target_entropy_batches)
    other_mean, other_se = summarize_batches(other_entropy_batches)
    return {
        "E_k_estimate": float(batch_array.mean()),
        "batch_se": float(batch_array.std(ddof=1) / sqrt(len(batch_array))),
        "acceptance_rate": acceptances / proposals,
        "chain_estimates": chain_estimates,
        "chain_estimate_spread": max(chain_estimates) - min(chain_estimates),
        "mean_importance_weight": float(np.mean(weight_batches)),
        "mean_batch_ess_fraction": float(
            np.mean(ess_batches) / max(10, draws // 20)
        ),
        "batch_count": len(bridge_batches),
        "split_rhat": split_rhat(chain_bridge_batches),
        "target_entropy_estimate": target_mean,
        "target_entropy_batch_se": target_se,
        "other_entropy_importance_estimate": other_mean,
        "other_entropy_importance_batch_se": other_se,
    }


def run_entropy(
    target: Density,
    chains: int,
    burn: int,
    draws: int,
    thin: int,
    rng: np.random.Generator,
) -> dict[str, object]:
    n = target.n
    layer = target.layer
    batches: list[float] = []
    chain_batches: list[list[float]] = []
    acceptances = 0
    proposals = 0
    for state in initial_states(n, layer, chains, rng):
        occupied = set(state)
        log_value = target.log_density(state)
        logs: list[float] = []
        total_steps = burn + draws * thin
        for step in range(total_steps):
            leaving = int(rng.choice(tuple(occupied)))
            outside = tuple(index for index in range(n) if index not in occupied)
            entering = int(rng.choice(outside))
            proposal_set = occupied.copy()
            proposal_set.remove(leaving)
            proposal_set.add(entering)
            proposal = tuple(sorted(proposal_set))
            proposal_log = target.log_density(proposal)
            proposals += 1
            if log(rng.random()) < min(0.0, proposal_log - log_value):
                occupied = proposal_set
                log_value = proposal_log
                acceptances += 1
            if step >= burn and (step - burn) % thin == 0:
                logs.append(log_value)
        batch_size = max(10, len(logs) // 20)
        current: list[float] = []
        for start in range(0, len(logs) - batch_size + 1, batch_size):
            value = float(np.mean(logs[start : start + batch_size]))
            batches.append(value)
            current.append(value)
        chain_batches.append(current)
    mean, se = summarize_batches(batches)
    return {
        "entropy_estimate": mean,
        "batch_se": se,
        "acceptance_rate": acceptances / proposals,
        "split_rhat": split_rhat(chain_batches),
        "batch_count": len(batches),
    }


def run_deletion_loss(
    central: Density,
    deleted: Density,
    chains: int,
    burn: int,
    draws: int,
    thin: int,
    rng: np.random.Generator,
) -> dict[str, object]:
    """Estimate A_k through the paired law J(T,x), avoiding two large entropies."""
    n = central.n
    layer = central.layer
    batches: list[float] = []
    chain_batches: list[list[float]] = []
    acceptances = 0
    proposals = 0
    for state in initial_states(n, layer, chains, rng):
        occupied = set(state)
        log_value = central.log_density(state)
        paired_losses: list[float] = []
        total_steps = burn + draws * thin
        for step in range(total_steps):
            leaving = int(rng.choice(tuple(occupied)))
            outside = tuple(index for index in range(n) if index not in occupied)
            entering = int(rng.choice(outside))
            proposal_set = occupied.copy()
            proposal_set.remove(leaving)
            proposal_set.add(entering)
            proposal = tuple(sorted(proposal_set))
            proposal_log = central.log_density(proposal)
            proposals += 1
            if log(rng.random()) < min(0.0, proposal_log - log_value):
                occupied = proposal_set
                log_value = proposal_log
                acceptances += 1
            if step >= burn and (step - burn) % thin == 0:
                removed = int(rng.choice(tuple(occupied)))
                deleted_state = tuple(sorted(index for index in occupied if index != removed))
                paired_losses.append(log_value - deleted.log_density(deleted_state))
        batch_size = max(10, len(paired_losses) // 20)
        current: list[float] = []
        for start in range(0, len(paired_losses) - batch_size + 1, batch_size):
            value = float(np.mean(paired_losses[start : start + batch_size]))
            batches.append(value)
            current.append(value)
        chain_batches.append(current)
    mean, se = summarize_batches(batches)
    return {
        "A_k_estimate": mean,
        "batch_se": se,
        "acceptance_rate": acceptances / proposals,
        "split_rhat": split_rhat(chain_batches),
        "batch_count": len(batches),
    }


def precision_average(values: list[tuple[float, float]]) -> tuple[float, float]:
    precisions = [1.0 / (standard_error * standard_error) for _, standard_error in values]
    mean = sum(precision * value for precision, (value, _) in zip(precisions, values)) / sum(precisions)
    return mean, sqrt(1.0 / sum(precisions))


def diagnose(n: int, arguments: argparse.Namespace) -> dict[str, object]:
    k = n // 2
    layer = k - 1
    seed = arguments.seed + n
    rng = np.random.default_rng(seed)
    earlier = Density(n, layer, original_time(n, layer))
    later = Density(n, layer, original_time(n, k))
    forward_result = run_bridge(
        earlier,
        later,
        True,
        arguments.chains,
        arguments.burn,
        arguments.draws,
        arguments.thin,
        rng,
    )
    reverse_result = run_bridge(
        later,
        earlier,
        False,
        arguments.chains,
        arguments.burn,
        arguments.draws,
        arguments.thin,
        rng,
    )
    central = Density(n, k, original_time(n, k))
    central_result = run_entropy(
        central,
        arguments.chains,
        arguments.burn,
        arguments.draws,
        arguments.thin,
        rng,
    )
    deletion_result = run_deletion_loss(
        central,
        later,
        arguments.chains,
        arguments.burn,
        arguments.draws,
        arguments.thin,
        rng,
    )
    forward_variance = forward_result["batch_se"] ** 2
    reverse_variance = reverse_result["batch_se"] ** 2
    forward_weight = 1.0 / forward_variance
    reverse_weight = 1.0 / reverse_variance
    e_estimate = (
        forward_weight * forward_result["E_k_estimate"]
        + reverse_weight * reverse_result["E_k_estimate"]
    ) / (forward_weight + reverse_weight)
    e_se = sqrt(1.0 / (forward_weight + reverse_weight))
    earlier_entropy, earlier_se = precision_average(
        [
            (forward_result["target_entropy_estimate"], forward_result["target_entropy_batch_se"]),
            (
                reverse_result["other_entropy_importance_estimate"],
                reverse_result["other_entropy_importance_batch_se"],
            ),
        ]
    )
    later_entropy, later_se = precision_average(
        [
            (
                forward_result["other_entropy_importance_estimate"],
                forward_result["other_entropy_importance_batch_se"],
            ),
            (reverse_result["target_entropy_estimate"], reverse_result["target_entropy_batch_se"]),
        ]
    )
    central_entropy = central_result["entropy_estimate"]
    central_se = central_result["batch_se"]
    return {
        "n": n,
        "k": k,
        "seed": seed,
        "forward_bridge": forward_result,
        "reverse_bridge": reverse_result,
        "combined_E_k_estimate": e_estimate,
        "combined_batch_se": e_se,
        "central_layer_entropy": central_result,
        "paired_deletion_loss": deletion_result,
        "paired_central_increment": {
            "d_k_estimate": deletion_result["A_k_estimate"] - e_estimate,
            "naive_se": sqrt(deletion_result["batch_se"] ** 2 + e_se**2),
        },
        "combined_entropy_estimates": {
            "F_k_at_s_k": central_entropy,
            "F_k_at_s_k_batch_se": central_se,
            "F_k_minus_1_at_s_k_minus_1": earlier_entropy,
            "F_k_minus_1_at_s_k_minus_1_batch_se": earlier_se,
            "F_k_minus_1_at_s_k": later_entropy,
            "F_k_minus_1_at_s_k_batch_se": later_se,
            "A_k_estimate": central_entropy - later_entropy,
            "A_k_naive_se": sqrt(central_se**2 + later_se**2),
            "E_k_from_entropies": earlier_entropy - later_entropy,
            "E_k_from_entropies_naive_se": sqrt(earlier_se**2 + later_se**2),
            "d_k_estimate": central_entropy - earlier_entropy,
            "d_k_naive_se": sqrt(central_se**2 + earlier_se**2),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", nargs="+", type=int, default=[20, 30, 40])
    parser.add_argument("--chains", type=int, default=4)
    parser.add_argument("--burn", type=int, default=1000)
    parser.add_argument("--draws", type=int, default=1000)
    parser.add_argument("--thin", type=int, default=5)
    parser.add_argument("--seed", type=int, default=20260918)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("sa04_bridge_mcmc_scout_result.json"),
    )
    args = parser.parse_args()
    limitations = [
        "Batch errors do not certify Markov-chain mixing.",
        "Relaxed binary64 birth-death tails are used beyond exact-enumeration sizes.",
        "The output selects an analytic route and is not a proof of a limit.",
    ]
    results = []
    for n in args.sizes:
        result = diagnose(n, args)
        results.append(result)
        receipt = {"status": "EXPLORATORY_MCMC", "results": results, "limitations": limitations}
        args.output.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
        paired = result["paired_central_increment"]
        deletion = result["paired_deletion_loss"]
        print(
            f"n={n} A={deletion['A_k_estimate']:+.6f} +/- {deletion['batch_se']:.6f} "
            f"E={result['combined_E_k_estimate']:+.6f} +/- {result['combined_batch_se']:.6f} "
            f"d={paired['d_k_estimate']:+.6f} +/- {paired['naive_se']:.6f}",
            flush=True,
        )


if __name__ == "__main__":
    main()
