#!/usr/bin/env python3
"""Independent replay for the S75 one-center star theorem and certificates.

This program safely imports and runs the author's exact certificate through
its main() function (so the author's directory is not written), then performs
separate full-word DPP enumerations and moment/tail checks.
"""
from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import itertools
import json
import math
import platform
import sys
from pathlib import Path

import numpy as np


def sine_kernel(sites: list[int], rho: float, c: float, a: float) -> np.ndarray:
    x = np.asarray(sites, dtype=float)
    distance = x[:, None] - x[None, :]
    return a * np.eye(len(sites)) + c * rho * np.sinc(rho * distance)


def star_kernel(d: float, weights: np.ndarray) -> np.ndarray:
    kernel = np.eye(len(weights) + 1) * d
    kernel[0, 1:] = np.sqrt(weights)
    kernel[1:, 0] = np.sqrt(weights)
    return kernel


def pair_potential(matrix: np.ndarray, i: int, j: int) -> float:
    h = float(abs(matrix[i, j]) ** 2)
    x = float(np.real(matrix[i, i]) * np.real(matrix[j, j]))
    argument = 1.0 - h / x
    if argument <= 0.0:
        raise ArithmeticError({"x": x, "h": h, "argument": argument})
    return h + (x - h) * math.log(argument)


def atom(kernel: np.ndarray, word: tuple[int, ...]) -> tuple[float, np.ndarray]:
    y = np.asarray(word)
    masked = kernel - np.diag(1 - y)
    sign, logabs = np.linalg.slogdet(masked)
    probability = ((-1) ** (len(word) - sum(word))) * sign * math.exp(float(logabs))
    if probability <= 0.0:
        raise ArithmeticError({"word": word, "probability": probability})
    return float(probability), np.linalg.inv(masked)


def expected_pair(
    kernel: np.ndarray,
    pair: tuple[int, int],
    fixed: dict[int, int] | None = None,
) -> dict:
    weighted = 0.0
    mass = 0.0
    for word in itertools.product((0, 1), repeat=len(kernel)):
        if fixed and any(word[position] != bit for position, bit in fixed.items()):
            continue
        probability, inverse = atom(kernel, word)
        mass += probability
        weighted += probability * pair_potential(inverse, *pair)
    if mass <= 0.0:
        raise ArithmeticError("zero conditioning mass")
    return {"conditional_mean": weighted / mass, "conditioning_mass": mass, "weighted_sum": weighted}


def pair_mean(alpha: float, beta: float, s: float) -> float:
    cells = (
        alpha * beta - s,
        alpha * (1.0 - beta) + s,
        (1.0 - alpha) * beta + s,
        (1.0 - alpha) * (1.0 - beta) - s,
    )
    if min(cells) <= 0.0:
        raise ArithmeticError({"alpha": alpha, "beta": beta, "s": s, "cells": cells})
    odds = cells[0] * cells[3] / (cells[1] * cells[2])
    return s * sum(1.0 / p for p in cells) + math.log(odds)


def direct_star_mean(d: float, weights: np.ndarray, core_leaves: tuple[int, ...]) -> float:
    kernel = star_kernel(d, weights)
    result = 0.0
    mass = 0.0
    for word in itertools.product((0, 1), repeat=len(kernel)):
        probability, inverse = atom(kernel, word)
        mass += probability
        result += probability * sum(pair_potential(inverse, 0, i + 1) for i in core_leaves)
    if abs(mass - 1.0) > 3e-12:
        raise AssertionError(mass)
    return result


def reduced_star_mean(d: float, weights: np.ndarray, core_leaves: tuple[int, ...]) -> float:
    total = 0.0
    for i in core_leaves:
        other_weights = [float(weight) for k, weight in enumerate(weights) if k != i]
        for word in itertools.product((0, 1), repeat=len(other_weights)):
            probability = math.prod(d if bit else 1.0 - d for bit in word)
            beta = d + sum(
                weight * ((1 - bit) / (1.0 - d) - bit / d)
                for weight, bit in zip(other_weights, word)
            )
            total += probability * pair_mean(d, beta, float(weights[i]))
    return total


def load_and_run_author_certificate(source_dir: Path) -> dict:
    module_name = "s75_author_certificate_replay"
    spec = importlib.util.spec_from_file_location(module_name, source_dir / "s75_certificate.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load author certificate")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    actual = module.main()
    supplied = json.loads((source_dir / "S75_CERTIFICATES.json").read_text(encoding="utf-8"))
    return {
        "status": actual["status"],
        "matches_supplied_json_exactly": actual == supplied,
        "result": actual,
    }


def explicit_counterexamples() -> dict:
    # General-rho sparse actual sine mask.
    coarse_kernel = sine_kernel([0, 3], 9 / 20, 19 / 20, 1 / 200)
    fine_kernel = sine_kernel([0, 3, 4], 9 / 20, 19 / 20, 1 / 200)
    coarse = expected_pair(coarse_kernel, (0, 1))
    fine = expected_pair(fine_kernel, (0, 1))

    # Half-density star conditional on old leaves {-1,1}=00.
    coarse_sites = [0, 7, -1, 1]
    fine_sites = [0, 7, -1, 1, -3]
    coarse_star = sine_kernel(coarse_sites, 0.5, 0.95, 1 / 2000)
    fine_star = sine_kernel(fine_sites, 0.5, 0.95, 1 / 2000)
    conditional_coarse = expected_pair(coarse_star, (0, 1), {2: 0, 3: 0})
    conditional_fine = expected_pair(fine_star, (0, 1), {2: 0, 3: 0})
    unconditional_coarse = expected_pair(coarse_star, (0, 1))
    unconditional_fine = expected_pair(fine_star, (0, 1))

    return {
        "general_rho_sparse_mask": {
            "rho": 0.45,
            "c": 0.95,
            "a": 0.005,
            "coarse_sites": [0, 3],
            "fine_sites": [0, 3, 4],
            "coarse_expectation": coarse["conditional_mean"],
            "fine_expectation": fine["conditional_mean"],
            "unconditional_pair_drift": fine["conditional_mean"] - coarse["conditional_mean"],
        },
        "half_density_star_background": {
            "rho": 0.5,
            "c": 0.95,
            "a": 0.0005,
            "coarse_sites": coarse_sites,
            "fine_sites": fine_sites,
            "old_background_word": [0, 0],
            "conditioning_mass_coarse": conditional_coarse["conditioning_mass"],
            "conditioning_mass_fine": conditional_fine["conditioning_mass"],
            "conditional_drift": conditional_fine["conditional_mean"] - conditional_coarse["conditional_mean"],
            "unconditional_drift": unconditional_fine["conditional_mean"] - unconditional_coarse["conditional_mean"],
        },
    }


def random_star_replay() -> dict:
    rng = np.random.default_rng(7526)
    records = []
    maximum_formula_error = 0.0
    minimum_drift_surplus = math.inf
    for _ in range(36):
        d = float(rng.uniform(0.055, 0.945))
        weights = rng.dirichlet(np.ones(6)) * min(d, 1.0 - d) ** 2 * float(rng.uniform(0.08, 0.96))
        core = (0, 2)
        old = weights[:5]
        direct_old = direct_star_mean(d, old, core)
        reduced_old = reduced_star_mean(d, old, core)
        direct_new = direct_star_mean(d, weights, core)
        reduced_new = reduced_star_mean(d, weights, core)
        formula_error = max(abs(direct_old - reduced_old), abs(direct_new - reduced_new))
        coefficient = 256.0 * (d ** -3 + (1.0 - d) ** -3) / (d * (1.0 - d))
        lower_bound = coefficient * sum(float(weights[i]) ** 3 for i in core) * float(weights[-1]) ** 2
        drift = direct_new - direct_old
        surplus = drift - lower_bound
        maximum_formula_error = max(maximum_formula_error, formula_error)
        minimum_drift_surplus = min(minimum_drift_surplus, surplus)
        records.append({
            "d": d,
            "drift": drift,
            "lower_bound": lower_bound,
            "surplus": surplus,
            "formula_error": formula_error,
        })
    return {
        "seed": 7526,
        "case_count": len(records),
        "maximum_formula_error": maximum_formula_error,
        "minimum_drift_minus_bound": minimum_drift_surplus,
        "records": records,
    }


def moment(d: float, weight: float, degree: int) -> float:
    if degree == 0:
        return 1.0
    return weight ** degree * (((-1) ** degree) * d ** (1 - degree) + (1.0 - d) ** (1 - degree))


def coefficient_b(d: float, s: float, k: int, n_limit: int = 240) -> float:
    u = 1.0 - d
    total = 0.0
    for n in range(2, n_limit + 1):
        if (n + k) % 2 == 0:
            continue
        total += (
            (n - 1.0) / n
            * s ** n
            * 2.0 ** (n + k + 1)
            * math.comb(n + k - 1, k)
            * (u ** -n + ((-1) ** k) * d ** -n)
        )
    return total


def moment_tail_replay() -> dict:
    d = 0.63
    u = 1.0 - d
    s = 0.02
    other = [0.015, 0.01, 0.008]
    degree = 12
    moments = [(d - 0.5) ** k for k in range(degree + 1)]
    for weight in other:
        updated = []
        for k in range(degree + 1):
            updated.append(sum(math.comb(k, ell) * moments[k - ell] * moment(d, weight, ell) for ell in range(k + 1)))
        moments = updated

    coefficients = [coefficient_b(d, s, k) for k in range(degree + 1)]
    lower = sum(coefficients[k] * moments[k] for k in range(degree + 1))
    exact = 0.0
    for word in itertools.product((0, 1), repeat=len(other)):
        probability = math.prod(d if bit else u for bit in word)
        beta = d + sum(weight * ((1 - bit) / u - bit / d) for weight, bit in zip(other, word))
        exact += probability * pair_mean(d, beta, s)

    total_other = sum(other)
    radius_support = d - 0.5 + total_other / u
    radius_convergence = 0.5 - s / u
    radius_prime = (radius_support + radius_convergence) / 2.0
    tail_bound = (
        (radius_support / radius_prime) ** (degree + 1)
        * pair_mean(d, 0.5 + radius_prime, s)
    )
    return {
        "d": d,
        "selected_weight_s": s,
        "other_weights": other,
        "degree": degree,
        "support_radius": radius_support,
        "chosen_R_prime": radius_prime,
        "convergence_radius": radius_convergence,
        "exact_expectation_by_word_enumeration": exact,
        "moment_series_lower_sum": lower,
        "actual_remainder": exact - lower,
        "theorem_tail_bound": tail_bound,
        "tail_slack": tail_bound - (exact - lower),
        "minimum_moment": min(moments),
        "minimum_coefficient": min(coefficients),
    }


def endpoint_and_spatial_tail_replay() -> dict:
    c = 0.95
    pi = math.pi
    s = c * c / (pi * pi)
    base = pair_mean(0.5, 0.5, s)
    lower = base + 16384.0 * s ** 3 * (c ** 4 / 48.0 - s ** 2)
    gamma = 0.25 - c * c / 4.0
    rows = []
    cutoff = 200000
    for radius in (2, 5, 10, 20):
        distances = [n for n in range(1, cutoff) if n % 2 and n >= radius]
        exact_general_envelope_sum = 2.0 * sum(
            4.0 * (c * c / (pi * pi * n * n)) ** 2 / gamma ** 2 for n in distances
        )
        exact_midpoint_envelope_sum = 2.0 * sum(
            4.0 * (c * c / (pi * pi * n * n)) ** 3 / gamma ** 3 for n in distances
        )
        general_remainder_upper = (
            8.0 * c ** 4 / (pi ** 4 * gamma ** 2)
            / (3.0 * (cutoff - 1) ** 3)
        )
        midpoint_remainder_upper = (
            8.0 * c ** 6 / (pi ** 6 * gamma ** 3)
            / (5.0 * (cutoff - 1) ** 5)
        )
        infinite_general_upper = exact_general_envelope_sum + general_remainder_upper
        infinite_midpoint_upper = exact_midpoint_envelope_sum + midpoint_remainder_upper
        general_formula = 8.0 * c ** 4 / (3.0 * pi ** 4 * gamma ** 2 * (radius - 1) ** 3)
        midpoint_formula = 8.0 * c ** 6 / (5.0 * pi ** 6 * gamma ** 3 * (radius - 1) ** 5)
        rows.append({
            "R": radius,
            "summed_general_pair_envelope_below_cutoff": exact_general_envelope_sum,
            "general_remainder_above_cutoff_upper": general_remainder_upper,
            "infinite_general_pair_envelope_upper": infinite_general_upper,
            "formula_22": general_formula,
            "general_slack": general_formula - infinite_general_upper,
            "summed_midpoint_pair_envelope_below_cutoff": exact_midpoint_envelope_sum,
            "midpoint_remainder_above_cutoff_upper": midpoint_remainder_upper,
            "infinite_midpoint_pair_envelope_upper": infinite_midpoint_upper,
            "formula_23": midpoint_formula,
            "midpoint_slack": midpoint_formula - infinite_midpoint_upper,
        })
    return {
        "midpoint_base_pair": base,
        "midpoint_infinite_star_lower_bound": lower,
        "gamma_star": gamma,
        "tail_rows": rows,
    }


def rate_budget_replay() -> dict:
    c = 0.95
    delta = 0.02
    kappa = c * c / (4.0 * delta * (delta + c))
    theta = kappa / (1.0 + kappa)
    beta = (1.0 - 2.0 * delta) / delta
    eta = beta / 2.0

    def a_term(lam: float) -> float:
        return 2.0 * kappa + 4.0 * theta * (1.0 + lam)

    def b_term(lam: float) -> float:
        return theta * beta * (1.0 + 1.0 / lam)

    lo, hi = 1.0e-12, 1.0
    while a_term(hi) / 2.0 < b_term(hi):
        hi *= 2.0
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if a_term(mid) / 2.0 < b_term(mid):
            lo = mid
        else:
            hi = mid
    lam = math.sqrt(lo * hi)
    c_chi = max(a_term(lam) / 2.0, b_term(lam))
    gamma_chi = c_chi / 2.0
    c_log = max(1.0, math.log1p(kappa))
    cap = 2.0 / delta - 4.0
    full_score_pair_core = 2.0 * c_log * cap
    missing_parity = gamma_chi * eta * (2.0 * cap)
    return {
        "c": c,
        "delta": delta,
        "lambda_chi": lam,
        "Gamma_chi": gamma_chi,
        "eta_delta": eta,
        "C_log": c_log,
        "tail_cap": cap,
        "full_score_pair_core_payment": full_score_pair_core,
        "missing_parity_payment": missing_parity,
        "combined_residual_envelope": full_score_pair_core + missing_parity,
        "interpretation": "uniform residual envelope in the S72 rate interface, not the actual full-line V",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = dt.datetime.now(dt.timezone.utc)

    author = load_and_run_author_certificate(args.source_dir)
    counterexamples = explicit_counterexamples()
    random_stars = random_star_replay()
    moment_tail = moment_tail_replay()
    endpoint_tail = endpoint_and_spatial_tail_replay()
    rate_budget = rate_budget_replay()

    checks = {
        "author_certificate_passed": author["status"] == "PASS_EXACT_RATIONAL_INTERVAL_CERTIFICATES",
        "author_certificate_matches_supplied_json": author["matches_supplied_json_exactly"],
        "general_rho_unconditional_pair_drift_negative": counterexamples["general_rho_sparse_mask"]["unconditional_pair_drift"] < 0.0,
        "star_conditioned_background_drift_negative": counterexamples["half_density_star_background"]["conditional_drift"] < 0.0,
        "star_unconditional_drift_positive": counterexamples["half_density_star_background"]["unconditional_drift"] > 0.0,
        "independent_random_star_formula": random_stars["maximum_formula_error"] < 2e-9,
        "independent_random_star_bound": random_stars["minimum_drift_minus_bound"] > -2e-10,
        "moment_coefficients_nonnegative": moment_tail["minimum_coefficient"] >= -1e-14,
        "actual_bias_moments_nonnegative": moment_tail["minimum_moment"] >= -1e-14,
        "whole_support_inside_convergence_disk": moment_tail["support_radius"] < moment_tail["chosen_R_prime"] < moment_tail["convergence_radius"],
        "moment_tail_bound_holds": moment_tail["tail_slack"] >= -2e-10,
        "midpoint_star_lower_exceeds_0_26275": endpoint_tail["midpoint_infinite_star_lower_bound"] > 0.26275,
        "general_tail_formula_holds": min(row["general_slack"] for row in endpoint_tail["tail_rows"]) >= 0.0,
        "midpoint_tail_formula_holds": min(row["midpoint_slack"] for row in endpoint_tail["tail_rows"]) >= 0.0,
        "rate_budget_reproduces_107974_scale": 107974.0 < rate_budget["combined_residual_envelope"] < 107975.5,
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    report = {
        "status": "PASS_INDEPENDENT_REPLAY_SUPPORTS_SCOPED_STAR_THEOREM",
        "execution": {
            "started_utc": started.isoformat(),
            "finished_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "python": platform.python_version(),
            "numpy": np.__version__,
        },
        "scope_warning": "finite floating replay plus a separately rerun exact author certificate; not a full-line entropy-rate proof",
        "checks": checks,
        "author_certificate_replay": author,
        "independent_full_word_counterexamples": counterexamples,
        "independent_random_star_replay": random_stars,
        "moment_and_tail_replay": moment_tail,
        "endpoint_and_spatial_tail_replay": endpoint_tail,
        "rate_budget_replay": rate_budget,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": report["status"],
        "checks": checks,
        "counterexamples": counterexamples,
        "random_star_summary": {k: v for k, v in random_stars.items() if k != "records"},
        "moment_tail": moment_tail,
        "endpoint_tail": endpoint_tail,
        "rate_budget": rate_budget,
    }, indent=2))


if __name__ == "__main__":
    main()
