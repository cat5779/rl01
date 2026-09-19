#!/usr/bin/env python3
"""Finite actual-sine stress test for the S71 acceleration term.

Every law is the genuine finite Toeplitz DPP K(a)=aI+cQ_rho.  The program
enumerates every output word, evaluates the Fisher defect D_F, acceleration
term C_acc, and M''=D_F+C_acc, and cross-checks against a second entropy
curvature calculation obtained from determinant polynomials rather than
resolvent traces.

The output is a finite diagnostic.  Positivity on this grid is not a theorem.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import platform
from dataclasses import dataclass
from pathlib import Path

import numpy as np


def sine_projection(n: int, rho: float) -> np.ndarray:
    sites = np.arange(n)
    distance = sites[:, None] - sites[None, :]
    return rho * np.sinc(rho * distance)


def word_bits(word: int, n: int) -> np.ndarray:
    return np.asarray([(word >> i) & 1 for i in range(n)], dtype=int)


@dataclass
class LawTable:
    n: int
    probability: np.ndarray
    score: np.ndarray
    acceleration: np.ndarray
    p1_polynomial: np.ndarray
    p2_polynomial: np.ndarray
    fisher: float
    entropy_second_resolvent: float
    entropy_second_polynomial: float
    diagnostics: dict


def law_table(n: int, rho: float, c: float, a: float) -> LawTable:
    q = sine_projection(n, rho)
    kernel = a * np.eye(n) + c * q
    count = 1 << n
    probabilities = np.empty(count)
    scores = np.empty(count)
    accelerations = np.empty(count)
    p1_poly = np.empty(count)
    p2_poly = np.empty(count)
    maximum_condition = 0.0
    maximum_probability_relative_error = 0.0
    maximum_p1_relative_error = 0.0
    maximum_p2_relative_error = 0.0

    for word in range(count):
        y = word_bits(word, n)
        parity = -1.0 if (n - int(y.sum())) % 2 else 1.0
        base = c * q - np.diag(1 - y)
        masked = base + a * np.eye(n)
        sign, logabs = np.linalg.slogdet(masked)
        probability = parity * sign * math.exp(float(logabs))
        if probability <= 0.0:
            raise ArithmeticError({"n": n, "word": word, "probability": probability})
        inverse = np.linalg.inv(masked)
        score = float(np.real(np.trace(inverse)))
        acceleration = float(score * score - np.real(np.trace(inverse @ inverse)))

        # Independent derivative path: det(aI+base) is reconstructed as a
        # scalar polynomial from the Hermitian eigenvalues of base.
        eigenvalues = np.linalg.eigvalsh(base)
        coefficients = np.poly(-eigenvalues)
        derivative1 = np.polyder(coefficients, 1)
        derivative2 = np.polyder(coefficients, 2)
        p_poly = parity * float(np.polyval(coefficients, a))
        p1 = parity * float(np.polyval(derivative1, a))
        p2 = parity * float(np.polyval(derivative2, a))

        probabilities[word] = probability
        scores[word] = score
        accelerations[word] = acceleration
        p1_poly[word] = p1
        p2_poly[word] = p2
        maximum_condition = max(maximum_condition, float(np.linalg.cond(masked)))
        maximum_probability_relative_error = max(
            maximum_probability_relative_error,
            abs(p_poly - probability) / probability,
        )
        maximum_p1_relative_error = max(
            maximum_p1_relative_error,
            abs(p1 - probability * score) / max(1.0, abs(p1), abs(probability * score)),
        )
        maximum_p2_relative_error = max(
            maximum_p2_relative_error,
            abs(p2 - probability * acceleration) / max(1.0, abs(p2), abs(probability * acceleration)),
        )

    fisher = float(np.dot(probabilities, scores * scores))
    entropy_second_resolvent = float(
        -np.dot(probabilities * accelerations, np.log(probabilities)) - fisher
    )
    entropy_second_polynomial = float(
        -np.dot(p2_poly, np.log(probabilities))
        - np.sum(p1_poly * p1_poly / probabilities)
    )
    diagnostics = {
        "probability_mass_error": abs(float(probabilities.sum()) - 1.0),
        "p1_sum_error": abs(float(p1_poly.sum())),
        "p2_sum_error": abs(float(p2_poly.sum())),
        "maximum_masked_condition_number": maximum_condition,
        "maximum_probability_relative_error_polynomial_vs_determinant": maximum_probability_relative_error,
        "maximum_scaled_p1_error": maximum_p1_relative_error,
        "maximum_scaled_p2_error": maximum_p2_relative_error,
        "entropy_second_crosscheck_error": abs(entropy_second_resolvent - entropy_second_polynomial),
    }
    return LawTable(
        n=n,
        probability=probabilities,
        score=scores,
        acceleration=accelerations,
        p1_polynomial=p1_poly,
        p2_polynomial=p2_poly,
        fisher=fisher,
        entropy_second_resolvent=entropy_second_resolvent,
        entropy_second_polynomial=entropy_second_polynomial,
        diagnostics=diagnostics,
    )


def one_case(
    joint: LawTable,
    left: LawTable,
    right: LawTable,
    rho: float,
    c: float,
    bias: float,
) -> dict:
    m, n = left.n, right.n
    left_mask = (1 << m) - 1
    log_ratio = np.empty_like(joint.probability)
    for word in range(1 << (m + n)):
        left_word = word & left_mask
        right_word = word >> m
        log_ratio[word] = math.log(
            joint.probability[word]
            / (left.probability[left_word] * right.probability[right_word])
        )

    weighted_acceleration = joint.probability * joint.acceleration * log_ratio
    c_acc = float(weighted_acceleration.sum())
    c_acc_positive = float(np.maximum(weighted_acceleration, 0.0).sum())
    c_acc_negative = float(np.maximum(-weighted_acceleration, 0.0).sum())
    d_f = float(joint.fisher - left.fisher - right.fisher)
    m_second_decomposition = d_f + c_acc
    m_second_direct_resolvent = float(
        left.entropy_second_resolvent
        + right.entropy_second_resolvent
        - joint.entropy_second_resolvent
    )
    m_second_direct_polynomial = float(
        left.entropy_second_polynomial
        + right.entropy_second_polynomial
        - joint.entropy_second_polynomial
    )
    negative_payment_ratio = d_f / (-c_acc) if c_acc < 0 else None
    return {
        "rho": rho,
        "c": c,
        "bias_p": bias,
        "a": (1.0 - c) * bias,
        "m": m,
        "n": n,
        "N": m + n,
        "D_F": d_f,
        "C_acc": c_acc,
        "C_acc_positive_part": c_acc_positive,
        "C_acc_negative_part": c_acc_negative,
        "M_second_decomposition": m_second_decomposition,
        "M_second_direct_resolvent": m_second_direct_resolvent,
        "M_second_direct_polynomial": m_second_direct_polynomial,
        "decomposition_vs_direct_error": abs(m_second_decomposition - m_second_direct_resolvent),
        "resolvent_vs_polynomial_error": abs(m_second_direct_resolvent - m_second_direct_polynomial),
        "D_F_over_minus_C_acc_when_negative": negative_payment_ratio,
        "D_F_fraction_of_absolute_terms": d_f / (d_f + abs(c_acc)) if d_f + abs(c_acc) > 0 else 0.0,
    }


def pick_minimum(rows: list[dict], key: str) -> dict:
    return min(rows, key=lambda row: row[key])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    started = dt.datetime.now(dt.timezone.utc)

    rhos = (0.25, 0.5, 0.75)
    contrasts = (0.93, 0.95, 0.99)
    biases = (0.1, 0.25, 0.5, 0.75, 0.9)
    block_pairs = (
        (1, 1), (1, 2), (2, 1), (1, 3), (3, 1), (2, 2),
        (2, 3), (3, 2), (1, 5), (5, 1), (3, 3), (2, 4),
        (4, 2), (3, 4), (4, 3), (4, 4), (2, 6), (6, 2),
        (4, 6), (6, 4), (5, 5),
    )

    rows = []
    table_diagnostics = []
    for rho in rhos:
        for c in contrasts:
            for bias in biases:
                a = (1.0 - c) * bias
                needed_sizes = sorted({size for pair in block_pairs for size in (pair[0], pair[1], sum(pair))})
                tables = {size: law_table(size, rho, c, a) for size in needed_sizes}
                for size, table in tables.items():
                    table_diagnostics.append({
                        "rho": rho, "c": c, "bias_p": bias, "a": a, "n": size,
                        **table.diagnostics,
                    })
                for m, n in block_pairs:
                    rows.append(one_case(tables[m + n], tables[m], tables[n], rho, c, bias))

    negative_cacc = [row for row in rows if row["C_acc"] < 0.0]
    negative_msecond = [row for row in rows if row["M_second_decomposition"] < 0.0]
    smallest_negative_cacc = min(
        negative_cacc,
        key=lambda row: (row["N"], max(row["m"], row["n"]), row["m"], row["rho"], row["c"], row["bias_p"]),
    ) if negative_cacc else None
    smallest_negative_msecond = min(
        negative_msecond,
        key=lambda row: (row["N"], max(row["m"], row["n"]), row["m"], row["rho"], row["c"], row["bias_p"]),
    ) if negative_msecond else None
    negative_payment_rows = [row for row in negative_cacc if row["D_F_over_minus_C_acc_when_negative"] is not None]

    checks = {
        "all_probability_masses_normalized": max(row["probability_mass_error"] for row in table_diagnostics) < 2e-8,
        "all_first_derivative_masses_zero": max(row["p1_sum_error"] for row in table_diagnostics) < 2e-7,
        "all_second_derivative_masses_zero": max(row["p2_sum_error"] for row in table_diagnostics) < 2e-5,
        "all_fisher_defects_nonnegative_on_grid": min(row["D_F"] for row in rows) > -2e-7,
        "decomposition_matches_direct_resolvent": max(row["decomposition_vs_direct_error"] for row in rows) < 2e-7,
        "resolvent_matches_polynomial_entropy_curvature": max(row["resolvent_vs_polynomial_error"] for row in rows) < 2e-5,
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    summary = {
        "case_count": len(rows),
        "law_table_count": len(table_diagnostics),
        "negative_C_acc_case_count": len(negative_cacc),
        "negative_M_second_case_count": len(negative_msecond),
        "minimum_C_acc": pick_minimum(rows, "C_acc"),
        "minimum_M_second": pick_minimum(rows, "M_second_decomposition"),
        "minimum_D_F": pick_minimum(rows, "D_F"),
        "smallest_negative_C_acc_case": smallest_negative_cacc,
        "smallest_negative_M_second_case": smallest_negative_msecond,
        "closest_compensation_when_C_acc_negative": (
            min(negative_payment_rows, key=lambda row: row["D_F_over_minus_C_acc_when_negative"])
            if negative_payment_rows else None
        ),
        "largest_compensation_ratio_when_C_acc_negative": (
            max(negative_payment_rows, key=lambda row: row["D_F_over_minus_C_acc_when_negative"])
            if negative_payment_rows else None
        ),
    }

    report = {
        "status": (
            "FINITE_COUNTEREXAMPLE_TO_C_ACC_NONNEGATIVITY"
            if negative_cacc else "FINITE_GRID_NO_NEGATIVE_C_ACC_NOT_A_THEOREM"
        ),
        "execution": {
            "started_utc": started.isoformat(),
            "finished_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "python": platform.python_version(),
            "numpy": np.__version__,
        },
        "scope": {
            "object": "actual finite Toeplitz DPP K=aI+cQ_rho with adjacent blocks",
            "rhos": list(rhos),
            "contrasts": list(contrasts),
            "biases_p_where_a_equals_(1-c)p": list(biases),
            "block_pairs": [list(pair) for pair in block_pairs],
            "maximum_total_size": max(sum(pair) for pair in block_pairs),
            "warning": "finite exhaustive word enumeration on the listed grid only",
        },
        "formula": {
            "D_F": "E S^2 - E S_A^2 - E S_B^2",
            "C_acc": "E[((tr R)^2-tr(R^2))*log(P/(P_A P_B))]",
            "M_second": "D_F+C_acc",
            "independent_crosscheck": "differentiate scalar determinant polynomials for every atom, then form H_A''+H_B''-H_AB''",
        },
        "checks": checks,
        "summary": summary,
        "all_cases": rows,
        "law_table_diagnostics": table_diagnostics,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": report["status"],
        "checks": checks,
        "summary": summary,
    }, indent=2))


if __name__ == "__main__":
    main()
