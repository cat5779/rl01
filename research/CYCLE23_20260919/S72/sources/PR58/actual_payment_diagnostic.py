#!/usr/bin/env python3
"""Actual-word single-reveal Taylor-payment diagnostics for QWE09/S72.

This program enumerates every coarse output word of genuine finite sine-DPPs.
It never substitutes random matrices for score inverses.  Results are floating
diagnostics, except that the original six-site word is compared against the
separately certified dyadic intervals from QWE09.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import platform
from pathlib import Path

import numpy as np


LAMBDA_QWE09 = 1486648002527 / 1204352
SIX_POINT_INTERVALS = {
    "probability": (0.014232864029787238, 0.014232864029787239),
    "conditional_q": (0.291967352633421847, 0.291967352633421848),
    "delta_phi": (-0.106585307859143407, -0.106585307859143406),
    "delta_chi": (-0.096395465271827624, -0.096395465271827623),
    "quadratic_variation": (0.170309619791317635, 0.170309619791317636),
}


def sine_kernel(n: int, c: float, noise_p: float) -> tuple[np.ndarray, float]:
    """Return K=aI+cQ at rho=1/2 and a=(1-c)*noise_p."""
    if not (0 < c < 1 and 0 < noise_p < 1):
        raise ValueError("need 0<c<1 and 0<noise_p<1")
    a = (1.0 - c) * noise_p
    ids = np.arange(n)
    delta = ids[:, None] - ids[None, :]
    q = 0.5 * np.sinc(0.5 * delta)
    return a * np.eye(n) + c * q, a


def atom_probability(masked: np.ndarray, ones: int) -> float:
    sign, logabs = np.linalg.slogdet(masked)
    n = masked.shape[0]
    probability = ((-1) ** (n - ones)) * sign * math.exp(float(logabs))
    if not probability > 0:
        raise ArithmeticError(f"nonpositive actual atom {probability}")
    return float(probability)


def potentials(matrix: np.ndarray, sites: tuple[int, ...]) -> tuple[float, float]:
    """QWE09 Phi and Chi on one fixed-sign actual core score matrix."""
    diag = np.real(np.diag(matrix))
    phi = float(diag @ diag)
    chi = 0.0
    for i in range(len(sites)):
        for j in range(i + 1, len(sites)):
            h = float(abs(matrix[i, j]) ** 2)
            v = float(diag[i] * diag[j])
            argument = 1.0 - h / v
            if not argument > 0:
                raise ArithmeticError("left logarithmic score domain")
            pair = h + (v - h) * math.log(argument)
            phi += 2.0 * pair
            if (sites[i] - sites[j]) % 2:
                chi += pair
    return phi, chi


def geometry(n: int, name: str) -> tuple[int, ...]:
    if name == "balanced_pair":
        return (n // 2 - 1, n // 2)
    if name == "balanced_triple":
        return (n // 2 - 1, n // 2, n // 2 + 1)
    raise ValueError(name)


def word_bits(word: int, length: int) -> tuple[int, ...]:
    return tuple((word >> i) & 1 for i in range(length))


def one_word(
    coarse_inverse: np.ndarray,
    coupling: np.ndarray,
    conditional_q: float,
    core: tuple[int, ...],
) -> dict[str, float]:
    m = coarse_inverse[np.ix_(core, core)]
    v = (coarse_inverse @ coupling)[list(core)]
    vv = np.outer(v, v)
    m1 = m + vv / conditional_q
    m0 = m - vv / (1.0 - conditional_q)
    coarse = potentials(m, core)
    fine1 = potentials(m1, core)
    fine0 = potentials(m0, core)
    deltas = tuple(
        conditional_q * fine1[k] + (1.0 - conditional_q) * fine0[k] - coarse[k]
        for k in range(2)
    )
    qv = float((v @ v) ** 2 / (conditional_q * (1.0 - conditional_q)))
    martingale_error = float(np.max(np.abs(conditional_q * m1 + (1.0 - conditional_q) * m0 - m)))
    return {
        "delta_phi": deltas[0],
        "delta_chi": deltas[1],
        "quadratic_variation": qv,
        "martingale_max_abs_error": martingale_error,
    }


def rare_negative_share(rows: list[dict], key: str, probability_mass: float) -> float:
    """Share of E negative part carried by the rarest given actual mass.

    The last word is fractionally included only to make the probability-mass
    cutoff comparable across n; this is a descriptive statistic.
    """
    total_negative = sum(row["probability"] * max(-row[key], 0.0) for row in rows)
    if total_negative == 0:
        return 0.0
    remaining = probability_mass
    captured = 0.0
    for row in sorted(rows, key=lambda item: item["probability"]):
        take = min(row["probability"], remaining)
        if take <= 0:
            break
        captured += take * max(-row[key], 0.0)
        remaining -= take
    return captured / total_negative


def summarize(rows: list[dict], key: str) -> dict:
    q_key = "quadratic_variation"
    e_delta = sum(row["probability"] * row[key] for row in rows)
    e_q = sum(row["probability"] * row[q_key] for row in rows)
    e_negative = sum(row["probability"] * max(-row[key], 0.0) for row in rows)
    e_positive = sum(row["probability"] * max(row[key], 0.0) for row in rows)
    negative_mass = sum(row["probability"] for row in rows if row[key] < 0)
    positive_mass = sum(row["probability"] for row in rows if row[key] > 0)

    for row in rows:
        qv = row[q_key]
        row[f"{key}_negative_ratio"] = max(-row[key], 0.0) / qv
        row[f"{key}_positive_ratio"] = max(row[key], 0.0) / qv

    worst_negative = max(rows, key=lambda row: row[f"{key}_negative_ratio"])
    worst_positive = max(rows, key=lambda row: row[f"{key}_positive_ratio"])
    weighted_negative_word_ratio = sum(
        row["probability"] * row[f"{key}_negative_ratio"] for row in rows
    )
    return {
        "E_delta": e_delta,
        "E_quadratic_variation": e_q,
        "E_negative_part": e_negative,
        "E_positive_part": e_positive,
        "negative_word_probability": negative_mass,
        "positive_word_probability": positive_mass,
        "minimum_lambda_signed_average": max(-e_delta / e_q, 0.0),
        "minimum_lambda_negative_part_average": e_negative / e_q,
        "ratio_of_positive_average_to_Eq": e_positive / e_q,
        "actual_weighted_mean_wordwise_negative_ratio": weighted_negative_word_ratio,
        "conditional_mean_wordwise_negative_ratio_given_negative": (
            weighted_negative_word_ratio / negative_mass if negative_mass else 0.0
        ),
        "worst_word_negative_ratio": worst_negative[f"{key}_negative_ratio"],
        "worst_negative_word": {
            "word": worst_negative["word"],
            "bits_site_order": worst_negative["bits_site_order"],
            "probability": worst_negative["probability"],
            "delta": worst_negative[key],
            "quadratic_variation": worst_negative[q_key],
        },
        "worst_word_positive_ratio": worst_positive[f"{key}_positive_ratio"],
        "worst_positive_word": {
            "word": worst_positive["word"],
            "bits_site_order": worst_positive["bits_site_order"],
            "probability": worst_positive["probability"],
            "delta": worst_positive[key],
            "quadratic_variation": worst_positive[q_key],
        },
        "negative_share_from_rarest_1pct_actual_mass": rare_negative_share(rows, key, 0.01),
        "negative_share_from_rarest_5pct_actual_mass": rare_negative_share(rows, key, 0.05),
    }


def evaluate_case(n: int, c: float, noise_p: float) -> list[dict]:
    kernel, a = sine_kernel(n, c, noise_p)
    observed = tuple(range(n - 1))
    revealed = n - 1
    coupling = kernel[np.ix_(observed, (revealed,))][:, 0]
    rows_by_geometry = {name: [] for name in ("balanced_pair", "balanced_triple")}
    mass = 0.0
    conditional_reveal_mass = 0.0
    minimum_probability = 1.0
    maximum_inverse_condition = 0.0
    maximum_martingale_error = 0.0
    maximum_fine_factorization_error = 0.0
    original_word = None

    for word in range(1 << (n - 1)):
        bits = word_bits(word, n - 1)
        masked = kernel[np.ix_(observed, observed)] - np.diag(1 - np.asarray(bits))
        probability = atom_probability(masked, sum(bits))
        inverse = np.linalg.inv(masked)
        conditional_q = float(kernel[revealed, revealed] - coupling @ inverse @ coupling)
        if not 0 < conditional_q < 1:
            raise ArithmeticError(f"illegal conditional probability {conditional_q}")
        mass += probability
        conditional_reveal_mass += probability * conditional_q
        minimum_probability = min(minimum_probability, probability)
        maximum_inverse_condition = max(maximum_inverse_condition, float(np.linalg.cond(masked)))
        for revealed_bit, conditional_probability in ((0, 1.0 - conditional_q), (1, conditional_q)):
            full_bits = np.asarray(bits + (revealed_bit,))
            full_masked = kernel - np.diag(1 - full_bits)
            fine_probability = atom_probability(full_masked, sum(bits) + revealed_bit)
            maximum_fine_factorization_error = max(
                maximum_fine_factorization_error,
                abs(fine_probability - probability * conditional_probability),
            )

        for name in rows_by_geometry:
            core = geometry(n, name)
            result = one_word(inverse, coupling, conditional_q, core)
            maximum_martingale_error = max(maximum_martingale_error, result["martingale_max_abs_error"])
            row = {
                "word": word,
                "bits_site_order": "".join(str(bit) for bit in bits),
                "probability": probability,
                "conditional_q": conditional_q,
                **result,
            }
            rows_by_geometry[name].append(row)
            if n == 6 and name == "balanced_pair" and word == 24 and abs(c - 0.95) < 1e-14 and abs(noise_p - 0.5) < 1e-14:
                original_word = row | {"core": list(core), "revealed": revealed}

    if abs(mass - 1.0) > 5e-10:
        raise ArithmeticError(f"coarse actual law did not normalize: {mass}")

    output = []
    for name, rows in rows_by_geometry.items():
        core = geometry(n, name)
        output.append({
            "n": n,
            "rho": 0.5,
            "c": c,
            "noise_p": noise_p,
            "a": a,
            "output_marginal": a + c / 2.0,
            "geometry": name,
            "core": list(core),
            "observed": list(observed),
            "revealed": revealed,
            "nearest_reveal_distance": min(abs(revealed - site) for site in core),
            "left_halo_sites": sum(site < min(core) for site in observed),
            "right_halo_sites": sum(site > max(core) for site in observed),
            "actual_coarse_words": len(rows),
            "actual_probability_mass": mass,
            "minimum_actual_word_probability": minimum_probability,
            "unconditional_reveal_one_probability": conditional_reveal_mass,
            "maximum_masked_condition_number": maximum_inverse_condition,
            "maximum_martingale_error": maximum_martingale_error,
            "maximum_fine_factorization_error": maximum_fine_factorization_error,
            "phi": summarize(rows, "delta_phi"),
            "chi": summarize(rows, "delta_chi"),
        })
    return output, original_word


def inside(value: float, interval: tuple[float, float], tolerance: float = 5e-15) -> bool:
    return interval[0] - tolerance <= value <= interval[1] + tolerance


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = dt.datetime.now(dt.timezone.utc)
    cases = []
    six_point = None
    for n in (6, 8, 10, 12):
        for c in (0.95, 0.99):
            for noise_p in (0.25, 0.5, 0.75):
                records, candidate = evaluate_case(n, c, noise_p)
                cases.extend(records)
                if candidate is not None:
                    six_point = candidate
    if six_point is None:
        raise AssertionError("original six-point word was not evaluated")

    six_checks = {
        "probability": six_point["probability"],
        "conditional_q": six_point["conditional_q"],
        "delta_phi": six_point["delta_phi"],
        "delta_chi": six_point["delta_chi"],
        "quadratic_variation": six_point["quadratic_variation"],
    }
    containment = {key: inside(value, SIX_POINT_INTERVALS[key]) for key, value in six_checks.items()}
    if not all(containment.values()):
        raise AssertionError({"six_point": six_checks, "containment": containment})

    candidates = {}
    for potential in ("phi", "chi"):
        candidates[potential] = {
            "lambda_signed_average_over_tested_family": max(
                case[potential]["minimum_lambda_signed_average"] for case in cases
            ),
            "lambda_negative_part_average_over_tested_family": max(
                case[potential]["minimum_lambda_negative_part_average"] for case in cases
            ),
            "lambda_wordwise_negative_over_tested_family": max(
                case[potential]["worst_word_negative_ratio"] for case in cases
            ),
        }

    report = {
        "status": "PASS_FLOATING_ACTUAL_WORD_DIAGNOSTIC_NOT_A_CERTIFICATE",
        "execution": {
            "started_utc": started.isoformat(),
            "finished_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "python": platform.python_version(),
            "numpy": np.__version__,
            "case_count": len(cases),
            "all_words_enumerated": sum(case["actual_coarse_words"] for case in cases) // 2,
        },
        "frozen_variables": {
            "rho": "1/2",
            "c": ["19/20", "99/100"],
            "noise_p_definition": "a/(1-c)",
            "noise_p": ["1/4", "1/2", "3/4"],
            "n": [6, 8, 10, 12],
            "revealed_site": "n-1",
            "observed_sites": "0,...,n-2",
            "geometries": ["balanced_pair", "balanced_triple"],
        },
        "formula": {
            "coarse_probability": "P_A(y)=(-1)^(|A|-|y|) det(K_A-diag(1-y))",
            "conditional_q": "K_rr-K_rA (K_A-diag(1-y))^-1 K_Ar",
            "fine_scores": "M1=M+vv^T/q; M0=M-vv^T/(1-q)",
            "delta": "q Psi(M1)+(1-q) Psi(M0)-Psi(M)",
            "quadratic_variation": "||v||^4/[q(1-q)]",
        },
        "qwe09_global_hessian_lambda": LAMBDA_QWE09,
        "six_point_independent_reproduction": {
            "inputs": {"n": 6, "c": 0.95, "noise_p": 0.5, "a": 0.025,
                       "observed_word_site_order": "00011", "core": [2, 3], "revealed": 5},
            "floating_values": six_checks,
            "inside_certified_intervals": containment,
        },
        "candidate_minimum_constants_on_tested_family": candidates,
        "cases": cases,
        "scope": "all actual coarse words for the listed finite models; floating diagnostics only; no entropy sign theorem",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": report["status"],
        "execution": report["execution"],
        "six_point": report["six_point_independent_reproduction"],
        "candidate_constants": candidates,
    }, indent=2))


if __name__ == "__main__":
    main()
