#!/usr/bin/env python3
"""Independent finite replay for the visible S77 Fisher--Burg prefix.

The primary derivative path reconstructs each DPP atom as the scalar
determinant polynomial det(aI+B_y); it does not use the author's cofactor
routine.  The author routine is imported only for an end-of-run comparison.
All numerical results remain floating diagnostics, not interval certificates.
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


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    raise TypeError(f"not JSON serializable: {type(value)!r}")


def sine_q(n: int, rho: float) -> np.ndarray:
    sites = np.arange(n)
    distance = sites[:, None] - sites[None, :]
    return rho * np.sinc(rho * distance)


def bits(word: int, n: int) -> tuple[int, ...]:
    return tuple((word >> i) & 1 for i in range(n))


def atom_polynomial_table(n: int, rho: float, c: float, a: float) -> dict:
    q = sine_q(n, rho)
    probabilities = np.empty(1 << n)
    first = np.empty(1 << n)
    second = np.empty(1 << n)
    determinant_error = 0.0
    words = [bits(word, n) for word in range(1 << n)]
    for word, y0 in enumerate(words):
        y = np.asarray(y0)
        parity = -1.0 if (n - int(y.sum())) % 2 else 1.0
        base = c * q - np.diag(1 - y)
        eigenvalues = np.linalg.eigvalsh(base)
        coefficients = np.poly(-eigenvalues)
        p = parity * float(np.polyval(coefficients, a))
        p1 = parity * float(np.polyval(np.polyder(coefficients, 1), a))
        p2 = parity * float(np.polyval(np.polyder(coefficients, 2), a))
        direct = parity * float(np.linalg.det(base + a * np.eye(n)))
        if p <= 0.0 or direct <= 0.0:
            raise ArithmeticError({"n": n, "word": word, "p": p, "direct": direct})
        determinant_error = max(determinant_error, abs(p - direct) / direct)
        probabilities[word] = p
        first[word] = p1
        second[word] = p2
    return {
        "n": n,
        "words": words,
        "p": probabilities,
        "p1": first,
        "p2": second,
        "mass_error": abs(float(probabilities.sum()) - 1.0),
        "first_mass_error": abs(float(first.sum())),
        "second_mass_error": abs(float(second.sum())),
        "determinant_relative_error": determinant_error,
    }


def marginal_array(table: dict, keep: tuple[int, ...], key: str) -> tuple[np.ndarray, dict]:
    keys = list(itertools.product((0, 1), repeat=len(keep)))
    index = {value: position for position, value in enumerate(keys)}
    values = np.zeros(len(keys))
    for word, weight in zip(table["words"], table[key]):
        values[index[tuple(word[i] for i in keep)]] += weight
    return values, index


def entropy_second(p: np.ndarray, p1: np.ndarray, p2: np.ndarray) -> float:
    return float(-np.dot(p2, np.log(p)) - np.sum(p1 * p1 / p))


def mutual_information_from_table(table: dict) -> float:
    n = table["n"]
    left = tuple(range(n // 2))
    right = tuple(range(n // 2, n))
    p_a, ix_a = marginal_array(table, left, "p")
    p_b, ix_b = marginal_array(table, right, "p")
    value = 0.0
    for word, probability in zip(table["words"], table["p"]):
        ia = ix_a[tuple(word[i] for i in left)]
        ib = ix_b[tuple(word[i] for i in right)]
        value += probability * math.log(probability / (p_a[ia] * p_b[ib]))
    return value


def fisher_burg(n: int, rho: float, c: float, a: float) -> dict:
    if n % 2:
        raise ValueError("equal halves require even n")
    table = atom_polynomial_table(n, rho, c, a)
    words = table["words"]
    p, p1, p2 = table["p"], table["p1"], table["p2"]
    left = tuple(range(n // 2))
    right = tuple(range(n // 2, n))
    p_a, ix_a = marginal_array(table, left, "p")
    p_b, ix_b = marginal_array(table, right, "p")
    p1_a, _ = marginal_array(table, left, "p1")
    p1_b, _ = marginal_array(table, right, "p1")
    p2_a, _ = marginal_array(table, left, "p2")
    p2_b, _ = marginal_array(table, right, "p2")

    q = np.empty_like(p)
    q1 = np.empty_like(p)
    q2 = np.empty_like(p)
    score_a = np.empty_like(p)
    score_b = np.empty_like(p)
    for k, word in enumerate(words):
        ia = ix_a[tuple(word[i] for i in left)]
        ib = ix_b[tuple(word[i] for i in right)]
        q[k] = p_a[ia] * p_b[ib]
        q1[k] = p1_a[ia] * p_b[ib] + p_a[ia] * p1_b[ib]
        q2[k] = p2_a[ia] * p_b[ib] + 2.0 * p1_a[ia] * p1_b[ib] + p_a[ia] * p2_b[ib]
        score_a[k] = p1_a[ia] / p_a[ia]
        score_b[k] = p1_b[ib] / p_b[ib]

    score = p1 / p
    relative_score = score - q1 / q
    i_rel = float(np.dot(p, relative_score * relative_score))
    d_f = float(np.dot(p, score * score) - np.dot(p, score_a * score_a) - np.dot(p, score_b * score_b))
    score_cross = float(np.dot(p, score_a * score_b))
    c_acc = float(np.dot(p2, np.log(p / q)))

    g = p / q
    word_index = {word: k for k, word in enumerate(words)}
    burg = 0.0
    burg_positive = 0.0
    burg_negative = 0.0
    rectangle_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            keep = tuple(h for h in range(n) if h not in (i, j))
            p_minus, ix_minus = marginal_array(table, keep, "p")
            # q is a normalized finite law; build its deleted marginal directly.
            q_table = {"words": words, "p": q}
            q_minus, _ = marginal_array(q_table, keep, "p")
            for outside in itertools.product((0, 1), repeat=n - 2):
                idx = ix_minus[outside]
                m = p_minus[idx] / q_minus[idx]
                phi = {}
                for yi, yj in itertools.product((0, 1), repeat=2):
                    full = []
                    outside_iterator = iter(outside)
                    for h in range(n):
                        full.append(yi if h == i else yj if h == j else next(outside_iterator))
                    x = g[word_index[tuple(full)]]
                    phi[(yi, yj)] = 2.0 * (x - m - m * math.log(x / m))
                rectangle = phi[(1, 1)] + phi[(0, 0)] - phi[(1, 0)] - phi[(0, 1)]
                charge = q_minus[idx] * rectangle
                burg += charge
                burg_positive += max(charge, 0.0)
                burg_negative += max(-charge, 0.0)
                rectangle_count += 1

    h2_joint = entropy_second(p, p1, p2)
    h2_a = entropy_second(p_a, p1_a, p2_a)
    h2_b = entropy_second(p_b, p1_b, p2_b)
    m2 = h2_a + h2_b - h2_joint
    return {
        "n": n,
        "rho": rho,
        "c": c,
        "a": a,
        "min_atom": float(p.min()),
        "D_F": d_f,
        "score_cross_covariance": score_cross,
        "C_acc": c_acc,
        "Irel": i_rel,
        "Burg": burg,
        "Burg_plus": burg_positive,
        "Burg_minus": burg_negative,
        "floating_sufficient_condition_value": i_rel - burg_positive,
        "M_second": m2,
        "rectangle_count": rectangle_count,
        "checks": {
            "DF_relation_error": abs(d_f - (i_rel - 2.0 * score_cross)),
            "Cacc_relation_error": abs(c_acc - (2.0 * score_cross - burg)),
            "Fisher_Burg_identity_error": abs(m2 - (i_rel - burg)),
            "old_decomposition_error": abs(m2 - (d_f + c_acc)),
            "q_mass_error": abs(float(q.sum()) - 1.0),
            "q1_mass_error": abs(float(q1.sum())),
            "q2_mass_error": abs(float(q2.sum())),
            "p_mass_error": table["mass_error"],
            "p1_mass_error": table["first_mass_error"],
            "p2_mass_error": table["second_mass_error"],
            "determinant_relative_error": table["determinant_relative_error"],
        },
    }


def finite_difference_m2(n: int, rho: float, c: float, a: float, step: float = 5e-4) -> dict:
    values = []
    for multiplier in (-2, -1, 0, 1, 2):
        values.append(mutual_information_from_table(atom_polynomial_table(n, rho, c, a + multiplier * step)))
    second = (-values[0] + 16.0 * values[1] - 30.0 * values[2] + 16.0 * values[3] - values[4]) / (12.0 * step * step)
    return {"step": step, "values": values, "five_point_second": second}


def scalar_integral_replay() -> dict:
    nodes, weights = np.polynomial.legendre.leggauss(160)
    s = (nodes + 1.0) / 2.0
    quadrature_weights = weights / 2.0
    errors_23 = []
    for g in (0.17, 0.55, 1.0, 1.8, 5.2):
        d = 1.0 + s * (g - 1.0)
        numeric = float(np.dot(quadrature_weights, 2.0 * (1.0 - s) / d ** 3))
        errors_23.append({"g": g, "numeric": numeric, "closed": 1.0 / g, "error": abs(numeric - 1.0 / g)})
    errors_26 = []
    for g, m in ((0.2, 0.7), (0.7, 0.2), (1.3, 0.6), (4.0, 1.4), (1.0, 1.0)):
        dg = 1.0 + s * (g - 1.0)
        dm = 1.0 + s * (m - 1.0)
        numeric = float(np.dot(quadrature_weights, 2.0 * (g - m) ** 2 * (1.0 - s) / (dg ** 2 * dm)))
        closed = 2.0 * (g - m - m * math.log(g / m))
        errors_26.append({"g": g, "m": m, "numeric": numeric, "closed": closed, "error": abs(numeric - closed)})
    return {
        "formula_23": errors_23,
        "formula_26": errors_26,
        "maximum_error_23": max(row["error"] for row in errors_23),
        "maximum_error_26": max(row["error"] for row in errors_26),
    }


def midpoint_two_site(d: float) -> dict:
    x = 4.0 * d
    d_f = 8.0 * x / (1.0 - x)
    c_acc = 4.0 * (math.log1p(-x) - math.log1p(x))
    return {"d": d, "D_F": d_f, "C_acc": c_acc, "ratio": -c_acc / d_f, "M_second": d_f + c_acc}


def general_two_site(u: float, d: float) -> dict:
    v = u * (1.0 - u)
    d_f = (
        4.0 * u * u / (u * u - d)
        + 2.0 * (1.0 - 2.0 * u) ** 2 / (v + d)
        + 4.0 * (1.0 - u) ** 2 / ((1.0 - u) ** 2 - d)
        - 2.0 / v
    )
    c_acc = 2.0 * math.log(((u * u - d) * ((1.0 - u) ** 2 - d)) / (v + d) ** 2)
    lower = (3.0 - 10.0 * v) / v ** 4 * d * d
    return {"u": u, "d": d, "M_second": d_f + c_acc, "lower": lower, "slack": d_f + c_acc - lower}


def two_site_replay() -> dict:
    weak = [midpoint_two_site(d) for d in (1e-2, 1e-4, 1e-6, 1e-8)]
    lower_rows = []
    for u in (0.1, 0.25, 0.5, 0.75, 0.9):
        maximum = min(u * u, (1.0 - u) ** 2)
        for fraction in (0.01, 0.1, 0.5, 0.9):
            lower_rows.append(general_two_site(u, fraction * maximum))
    return {
        "weak_coupling": weak,
        "lower_bound_rows": lower_rows,
        "minimum_lower_bound_slack": min(row["slack"] for row in lower_rows),
    }


def merge_tree_replay() -> list[dict]:
    rho, c, leaf_length, q_leaves = 0.37, 0.91, 2, 8
    n = leaf_length * q_leaves
    q = sine_q(n, rho)
    levels = {}
    for level in range(1, 4):
        side = 2 ** (level - 1) * leaf_length
        total = 0.0
        for start in range(0, n, 2 * side):
            left = tuple(range(start, start + side))
            right = tuple(range(start + side, start + 2 * side))
            total += c * c * float(np.sum(abs(q[np.ix_(left, right)]) ** 2))
        levels[level] = total
    rows = []
    for k in (0, 1, 2):
        direct = sum(levels[level] for level in range(k + 1, 4))
        block = 2 ** k * leaf_length
        q_block = sine_q(block, rho)
        formula = c * c / 2.0 * (
            float(np.trace(q @ q))
            - q_leaves / (2 ** k) * float(np.trace(q_block @ q_block))
        )
        rows.append({"K": k, "direct_tail_charge": direct, "trace_formula": formula, "error": abs(direct - formula)})
    return rows


def load_author(author_script: Path, sizes: tuple[int, ...]) -> dict:
    name = "s77_author_diagnostic_replay"
    spec = importlib.util.spec_from_file_location(name, author_script)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load author script")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return {str(n): module.diagnostics(n) for n in sizes}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--author-script", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = dt.datetime.now(dt.timezone.utc)

    central_sizes = (2, 4, 6, 8, 10, 12)
    independent_central = [fisher_burg(n, 0.5, 0.95, 0.025) for n in central_sizes]
    author_central = load_author(args.author_script, central_sizes)
    scan = []
    for c in (0.925, 0.9375, 0.95):
        for a in (0.02, 0.025, 0.03):
            for n in (2, 4, 6, 8, 10):
                scan.append(fisher_burg(n, 0.5, c, a))
    scalar = scalar_integral_replay()
    finite_difference = finite_difference_m2(6, 0.5, 0.95, 0.025)
    two_site = two_site_replay()
    merge = merge_tree_replay()

    author_errors = []
    for row in independent_central:
        other = author_central[str(row["n"])]
        author_errors.extend([
            abs(row["Irel"] - other["Irel"]),
            abs(row["Burg"] - other["Burg"]),
            abs(row["Burg_plus"] - other["Burg_plus"]),
            abs(row["M_second"] - other["M2"]),
        ])
    all_rows = independent_central + scan
    all_check_values = [value for row in all_rows for value in row["checks"].values()]
    direct_n6 = next(row for row in independent_central if row["n"] == 6)
    checks = {
        "scalar_integral_23": scalar["maximum_error_23"] < 2e-12,
        "scalar_integral_26": scalar["maximum_error_26"] < 2e-12,
        "Fisher_Burg_and_score_identities": max(all_check_values) < 2e-8,
        "independent_matches_author_diagnostic": max(author_errors) < 2e-8,
        "finite_difference_M_second": abs(finite_difference["five_point_second"] - direct_n6["M_second"]) < 2e-5,
        "all_floating_Bplus_sufficient_values_positive_on_scan": min(row["floating_sufficient_condition_value"] for row in scan) > 0.0,
        "weak_coupling_ratio_tends_to_one": two_site["weak_coupling"][-1]["ratio"] > 0.999999,
        "two_site_d2_lower_bound": two_site["minimum_lower_bound_slack"] > -2e-9,
        "merge_tail_trace_identity": max(row["error"] for row in merge) < 2e-12,
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    report = {
        "status": "PASS_FLOATING_REPLAY_SUPPORTS_VISIBLE_S77_CORE_NOT_A_CERTIFICATE",
        "source_scope": "visible Sections 1-7 and only the visible prefix of Section 8; source is truncated",
        "execution": {
            "started_utc": started.isoformat(),
            "finished_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "python": platform.python_version(),
            "numpy": np.__version__,
        },
        "checks": checks,
        "scalar_integrals": scalar,
        "central_point_independent": independent_central,
        "central_point_author": author_central,
        "maximum_independent_vs_author_error": max(author_errors),
        "finite_difference_n6": finite_difference,
        "scan": {
            "case_count": len(scan),
            "minimum_floating_sufficient_condition": min(scan, key=lambda row: row["floating_sufficient_condition_value"]),
            "all_cases": scan,
        },
        "two_site": two_site,
        "merge_tree": merge,
        "evidence_warning": "all numeric values are double-precision diagnostics; none is an interval-certified lower bound",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, default=json_default) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": report["status"],
        "checks": checks,
        "maximum_independent_vs_author_error": max(author_errors),
        "n6": direct_n6,
        "scan_minimum": report["scan"]["minimum_floating_sufficient_condition"],
        "weak_coupling": two_site["weak_coupling"],
        "two_site_minimum_slack": two_site["minimum_lower_bound_slack"],
        "merge_tree": merge,
    }, indent=2, default=json_default))


if __name__ == "__main__":
    main()
