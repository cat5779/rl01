#!/usr/bin/env python3
"""Independent finite-dimensional replay for the S72 one-sided-payment theorem.

The program uses only genuine finite compressions of the sine DPP.  It checks
the signed Ward identities, the exact reachable rank-one pair Hessian split,
the one-reveal inequality, the expected resolvent tail, and the published
constants.  Floating enumeration is a consistency check, not a replacement
for the analytic proof recorded in the accompanying review.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import platform
from pathlib import Path

import numpy as np


def sine_kernel(n: int, rho: float, c: float, a: float) -> np.ndarray:
    ids = np.arange(n)
    distance = ids[:, None] - ids[None, :]
    q = rho * np.sinc(rho * distance)
    return a * np.eye(n) + c * q


def bits(word: int, n: int) -> np.ndarray:
    return np.asarray([(word >> i) & 1 for i in range(n)], dtype=int)


def atom_probability(kernel: np.ndarray, y: np.ndarray) -> float:
    masked = kernel - np.diag(1 - y)
    sign, logabs = np.linalg.slogdet(masked)
    probability = ((-1) ** (len(y) - int(y.sum()))) * sign * math.exp(float(logabs))
    if probability <= 0:
        raise ArithmeticError(f"nonpositive atom probability {probability}")
    return float(probability)


def potential(matrix: np.ndarray, sites: tuple[int, ...], kind: str) -> float:
    diagonal = np.real(np.diag(matrix))
    value = float(diagonal @ diagonal) if kind == "phi" else 0.0
    for i in range(len(sites)):
        for j in range(i + 1, len(sites)):
            if kind == "chi" and (sites[i] - sites[j]) % 2 == 0:
                continue
            h = float(abs(matrix[i, j]) ** 2)
            x = float(diagonal[i] * diagonal[j])
            argument = 1.0 - h / x
            if argument <= 0:
                raise ArithmeticError("left logarithmic score domain")
            pair = h + (x - h) * math.log(argument)
            value += 2.0 * pair if kind == "phi" else pair
    return value


def pair_value(matrix: np.ndarray, i: int, j: int) -> float:
    h = float(abs(matrix[i, j]) ** 2)
    x = float(np.real(matrix[i, i]) * np.real(matrix[j, j]))
    return h + (x - h) * math.log(1.0 - h / x)


def exact_pair_hessian_formula(matrix: np.ndarray, vector: np.ndarray, i: int, j: int) -> float:
    sigma_i = 1.0 if np.real(matrix[i, i]) > 0 else -1.0
    sigma_j = 1.0 if np.real(matrix[j, j]) > 0 else -1.0
    u_i = sigma_i * float(np.real(matrix[i, i]))
    u_j = sigma_j * float(np.real(matrix[j, j]))
    t_i = float(abs(vector[i]) ** 2)
    t_j = float(abs(vector[j]) ** 2)
    alpha_i = t_i / u_i
    alpha_j = t_j / u_j
    s = u_i * u_j
    h = float(abs(matrix[i, j]) ** 2)
    r = h / s
    cross = matrix[i, j].conjugate() * vector[i] * vector[j].conjugate()
    cos_omega = float(np.real(cross) / math.sqrt(h * t_i * t_j)) if h * t_i * t_j > 0 else 0.0
    root = 2.0 * math.sqrt(max(r * alpha_i * alpha_j, 0.0)) * cos_omega
    if sigma_i == sigma_j:
        square = root - sigma_i * r * (alpha_i + alpha_j)
        return 2.0 * r * t_i * t_j + s * square * square / (1.0 - r)
    # For opposite signs the printed S72 formula assumes that i is the
    # positive-sign site.  The sigma_i form below is the label-invariant one.
    square = root - sigma_i * r * (alpha_i - alpha_j)
    return -2.0 * r * t_i * t_j - s * square * square / (1.0 + r)


def direct_pair_hessian(matrix: np.ndarray, vector: np.ndarray, i: int, j: int) -> float:
    """Differentiate f(x,h) directly, independently of the sign split."""
    t_i = float(abs(vector[i]) ** 2)
    t_j = float(abs(vector[j]) ** 2)
    x_i = float(np.real(matrix[i, i]))
    x_j = float(np.real(matrix[j, j]))
    x = x_i * x_j
    h = float(abs(matrix[i, j]) ** 2)
    e_ij = vector[i] * vector[j].conjugate()
    dx = t_i * x_j + t_j * x_i
    ddx = 2.0 * t_i * t_j
    dh = 2.0 * float(np.real(matrix[i, j].conjugate() * e_ij))
    ddh = 2.0 * t_i * t_j
    argument = 1.0 - h / x
    f_x = h / x + math.log(argument)
    f_h = -math.log(argument)
    f_xx = h * h / (x * x * (x - h))
    f_xh = -h / (x * (x - h))
    f_hh = 1.0 / (x - h)
    return f_xx * dx * dx + 2.0 * f_xh * dx * dh + f_hh * dh * dh + f_x * ddx + f_h * ddh


def constants(delta: float, c: float) -> dict:
    kappa = c * c / (4.0 * delta * (delta + c))
    theta = kappa / (1.0 + kappa)
    beta = (1.0 - 2.0 * delta) / delta

    def a_term(lam: float) -> float:
        return 2.0 * kappa + 4.0 * theta * (1.0 + lam)

    def b_term(lam: float) -> float:
        return theta * beta * (1.0 + 1.0 / lam)

    def root(which: str) -> float:
        lo, hi = 1.0e-12, 1.0
        def gap(lam: float) -> float:
            if which == "phi":
                return a_term(lam) - (2.0 * b_term(lam) - 2.0)
            return a_term(lam) / 2.0 - b_term(lam)
        while gap(hi) < 0:
            hi *= 2.0
        for _ in range(200):
            mid = math.sqrt(lo * hi)
            if gap(mid) < 0:
                lo = mid
            else:
                hi = mid
        return math.sqrt(lo * hi)

    lambda_phi = root("phi")
    lambda_chi = root("chi")
    c_phi = max(a_term(lambda_phi), 2.0 * b_term(lambda_phi) - 2.0)
    c_chi = max(a_term(lambda_chi) / 2.0, b_term(lambda_chi))
    return {
        "delta": delta,
        "c": c,
        "kappa": kappa,
        "theta": theta,
        "beta_delta": beta,
        "eta_delta": beta / 2.0,
        "lambda_phi": lambda_phi,
        "lambda_chi": lambda_chi,
        "C_phi": c_phi,
        "C_chi": c_chi,
        "Gamma_phi": c_phi / 2.0,
        "Gamma_chi": c_chi / 2.0,
        "C_log": max(1.0, math.log1p(kappa)),
        "B_hat": 2.0 * max(1.0, math.log1p(kappa)) / delta,
    }


def check_full_law(kernel: np.ndarray, delta: float, c: float) -> dict:
    n = len(kernel)
    identity = np.eye(n)
    expected_r = np.zeros((n, n), dtype=complex)
    expected_g2 = np.zeros((n, n), dtype=complex)
    expected_offdiag_energy = 0.0
    mass = 0.0
    minimum_ward_eigenvalue = math.inf
    maximum_row_violation = 0.0
    words = []
    for word in range(1 << n):
        y = bits(word, n)
        probability = atom_probability(kernel, y)
        masked = kernel - np.diag(1 - y)
        g = np.linalg.inv(masked)
        signs = np.diag(2 * y - 1)
        rmat = (signs @ g + g @ signs) / 2.0
        minimum_ward_eigenvalue = min(
            minimum_ward_eigenvalue,
            float(np.linalg.eigvalsh(rmat - delta * (g @ g)).min()),
        )
        u = (2 * y - 1) * np.real(np.diag(g))
        rows = np.sum(abs(g) ** 2, axis=1)
        maximum_row_violation = max(maximum_row_violation, float(np.max(delta * rows - u)))
        expected_r += probability * rmat
        expected_g2 += probability * (g @ g)
        expected_offdiag_energy += probability * float(np.sum(abs(g) ** 2) - np.sum(abs(np.diag(g)) ** 2))
        mass += probability
        words.append((probability, g))

    ward_expectation_error = float(np.max(abs(expected_r - 2.0 * identity)))
    g2_bound_max_eigenvalue = float(np.linalg.eigvalsh(expected_g2 - (2.0 / delta) * identity).max())
    diagonal_square_lower_error = float(
        max(0.0, 4.0 * n - sum(p * float(np.sum(abs(np.diag(g)) ** 2)) for p, g in words))
    )

    tail_rows = []
    for radius in range(1, n + 1):
        weights = np.minimum(abs(np.arange(n)[:, None] - np.arange(n)[None, :]) / radius, 1.0)
        lhs = sum(p * float(np.sum(weights * abs(g) ** 2)) / n for p, g in words)
        harmonic = sum(1.0 / k for k in range(1, radius))
        harmonic_bound = 4.0 * c * c / (math.pi * math.pi * delta ** 3) * (harmonic + 2.0) / radius
        cap = 2.0 / delta - 4.0
        bound = min(cap, harmonic_bound)
        tail_rows.append({"R": radius, "lhs": lhs, "bound": bound, "slack": bound - lhs})
    return {
        "n": n,
        "word_count": 1 << n,
        "probability_mass_error": abs(mass - 1.0),
        "minimum_eigenvalue_R_minus_delta_G2": minimum_ward_eigenvalue,
        "maximum_row_coercivity_violation": maximum_row_violation,
        "maximum_abs_E_R_minus_2I": ward_expectation_error,
        "maximum_eigenvalue_E_G2_minus_2_over_delta_I": g2_bound_max_eigenvalue,
        "diagonal_square_lower_error": diagonal_square_lower_error,
        "expected_offdiagonal_energy_per_site": expected_offdiag_energy / n,
        "tail": tail_rows,
    }


def reveal_checks(kernel: np.ndarray, core: tuple[int, ...], revealed: int, delta: float, const: dict) -> dict:
    observed = tuple(i for i in range(len(kernel)) if i != revealed)
    coupling = kernel[np.ix_(observed, (revealed,))][:, 0]
    core_positions = tuple(observed.index(i) for i in core)
    mass = 0.0
    worst_hessian_absolute_error = 0.0
    worst_hessian_relative_error = 0.0
    minimum_equal_sign_formula = math.inf
    maximum_opposite_sign_formula = -math.inf
    maximum_interpolation_row_violation = 0.0
    maximum_weighted_row_violation = 0.0
    maximum_pair_ratio_minus_kappa = -math.inf
    minimum_weighted_phi_hessian_margin = math.inf
    minimum_weighted_chi_hessian_margin = math.inf
    minimum_uniform_phi_hessian_margin = math.inf
    minimum_uniform_chi_hessian_margin = math.inf
    minimum_phi_margin = math.inf
    minimum_chi_margin = math.inf
    worst_phi_ratio = 0.0
    worst_chi_ratio = 0.0
    e_delta_phi = 0.0
    e_delta_chi = 0.0
    e_qv = 0.0

    for word in range(1 << len(observed)):
        y = bits(word, len(observed))
        probability = atom_probability(kernel[np.ix_(observed, observed)], y)
        masked = kernel[np.ix_(observed, observed)] - np.diag(1 - y)
        inverse = np.linalg.inv(masked)
        q = float(kernel[revealed, revealed] - coupling.conjugate() @ inverse @ coupling)
        if not delta - 2e-11 <= q <= 1.0 - delta + 2e-11:
            raise AssertionError({"q": q, "delta": delta})
        m = inverse[np.ix_(core_positions, core_positions)]
        v = (inverse @ coupling)[list(core_positions)]
        direction = np.outer(v, v.conjugate())
        m1 = m + direction / q
        m0 = m - direction / (1.0 - q)
        qv = float(np.linalg.norm(v) ** 4 / (q * (1.0 - q)))
        delta_phi = q * potential(m1, core, "phi") + (1.0 - q) * potential(m0, core, "phi") - potential(m, core, "phi")
        delta_chi = q * potential(m1, core, "chi") + (1.0 - q) * potential(m0, core, "chi") - potential(m, core, "chi")
        phi_margin = delta_phi + const["Gamma_phi"] * qv
        chi_margin = delta_chi + const["Gamma_chi"] * qv
        minimum_phi_margin = min(minimum_phi_margin, phi_margin)
        minimum_chi_margin = min(minimum_chi_margin, chi_margin)
        if qv > 1e-24:
            worst_phi_ratio = max(worst_phi_ratio, max(-delta_phi, 0.0) / qv)
            worst_chi_ratio = max(worst_chi_ratio, max(-delta_chi, 0.0) / qv)
        e_delta_phi += probability * delta_phi
        e_delta_chi += probability * delta_chi
        e_qv += probability * qv
        mass += probability

        # Test both actual interpolation segments at interior points.
        signs = 2 * y[list(core_positions)] - 1
        for endpoint, length, direction_sign in ((m1, 1.0 / q, 1.0), (m0, 1.0 / (1.0 - q), -1.0)):
            del endpoint
            for fraction in (0.0, 0.25, 0.5, 0.75, 1.0):
                x = m + direction_sign * fraction * length * direction
                u = signs * np.real(np.diag(x))
                row_squares = np.sum(abs(x) ** 2, axis=1)
                maximum_interpolation_row_violation = max(
                    maximum_interpolation_row_violation,
                    float(np.max(row_squares - u / delta)),
                )
                t = abs(v) ** 2
                total_t = float(np.sum(t))
                sum_t2 = float(np.sum(t ** 2))
                exact_pairs = {}
                for i in range(len(core)):
                    offdiag_weight = float((np.sum(abs(x[i, :]) ** 2) - abs(x[i, i]) ** 2) / (u[i] ** 2))
                    maximum_weighted_row_violation = max(
                        maximum_weighted_row_violation,
                        offdiag_weight - (1.0 / (delta * u[i]) - 1.0),
                    )
                    for j in range(i + 1, len(core)):
                        ratio = float(abs(x[i, j]) ** 2 / (u[i] * u[j]))
                        maximum_pair_ratio_minus_kappa = max(maximum_pair_ratio_minus_kappa, ratio - const["kappa"])
                        exact = exact_pair_hessian_formula(x, v, i, j)
                        direct = direct_pair_hessian(x, v, i, j)
                        exact_pairs[(i, j)] = direct
                        error = abs(exact - direct)
                        worst_hessian_absolute_error = max(worst_hessian_absolute_error, error)
                        worst_hessian_relative_error = max(
                            worst_hessian_relative_error,
                            error / max(1.0, abs(exact), abs(direct)),
                        )
                        if signs[i] == signs[j]:
                            minimum_equal_sign_formula = min(minimum_equal_sign_formula, exact)
                        else:
                            maximum_opposite_sign_formula = max(maximum_opposite_sign_formula, exact)

                weighted_sum = float(np.sum((1.0 / (delta * u) - 1.0) * t ** 2))
                lam_phi = const["lambda_phi"]
                a_phi = 2.0 * const["kappa"] + 4.0 * const["theta"] * (1.0 + lam_phi)
                phi_hessian = 2.0 * sum_t2 + 2.0 * sum(exact_pairs.values())
                phi_rhs = (
                    -a_phi * total_t ** 2
                    + (a_phi + 2.0) * sum_t2
                    - 2.0 * const["theta"] * (1.0 + 1.0 / lam_phi) * weighted_sum
                )
                minimum_weighted_phi_hessian_margin = min(
                    minimum_weighted_phi_hessian_margin, phi_hessian - phi_rhs
                )
                minimum_uniform_phi_hessian_margin = min(
                    minimum_uniform_phi_hessian_margin,
                    phi_hessian + const["C_phi"] * total_t ** 2,
                )

                lam_chi = const["lambda_chi"]
                a_chi = 2.0 * const["kappa"] + 4.0 * const["theta"] * (1.0 + lam_chi)
                chi_hessian = sum(
                    value for (i, j), value in exact_pairs.items() if (core[i] - core[j]) % 2
                )
                chi_rhs = (
                    -0.5 * a_chi * total_t ** 2
                    + 0.5 * a_chi * sum_t2
                    - const["theta"] * (1.0 + 1.0 / lam_chi) * weighted_sum
                )
                minimum_weighted_chi_hessian_margin = min(
                    minimum_weighted_chi_hessian_margin, chi_hessian - chi_rhs
                )
                minimum_uniform_chi_hessian_margin = min(
                    minimum_uniform_chi_hessian_margin,
                    chi_hessian + const["C_chi"] * total_t ** 2,
                )

    return {
        "observed_word_count": 1 << len(observed),
        "probability_mass_error": abs(mass - 1.0),
        "core": list(core),
        "revealed": revealed,
        "maximum_pair_hessian_absolute_error": worst_hessian_absolute_error,
        "maximum_pair_hessian_relative_error_scaled": worst_hessian_relative_error,
        "minimum_equal_sign_hessian_formula": minimum_equal_sign_formula,
        "maximum_opposite_sign_hessian_formula": maximum_opposite_sign_formula,
        "maximum_interpolation_row_coercivity_violation": maximum_interpolation_row_violation,
        "maximum_weighted_row_violation": maximum_weighted_row_violation,
        "maximum_pair_ratio_minus_kappa": maximum_pair_ratio_minus_kappa,
        "minimum_weighted_phi_hessian_margin": minimum_weighted_phi_hessian_margin,
        "minimum_weighted_chi_hessian_margin": minimum_weighted_chi_hessian_margin,
        "minimum_uniform_phi_hessian_margin": minimum_uniform_phi_hessian_margin,
        "minimum_uniform_chi_hessian_margin": minimum_uniform_chi_hessian_margin,
        "minimum_phi_one_reveal_margin": minimum_phi_margin,
        "minimum_chi_one_reveal_margin": minimum_chi_margin,
        "worst_word_phi_negative_ratio": worst_phi_ratio,
        "worst_word_chi_negative_ratio": worst_chi_ratio,
        "E_delta_phi": e_delta_phi,
        "E_delta_chi": e_delta_chi,
        "E_quadratic_variation": e_qv,
    }


def benchmark(const: dict) -> dict:
    old = 1.763690e15
    prefactor = 4.0 * const["c"] ** 2 / (math.pi * math.pi * const["delta"] ** 3)
    phi = const["Gamma_phi"] * const["eta_delta"] * prefactor
    chi = const["Gamma_chi"] * const["eta_delta"] * prefactor
    return {
        "harmonic_prefactor": prefactor,
        "phi_harmonic_coefficient": phi,
        "chi_harmonic_coefficient": chi,
        "old_coefficient_used_for_comparison": old,
        "phi_improvement_factor": old / phi,
        "chi_improvement_factor": old / chi,
    }


def finite_window_diagnostic() -> list[dict]:
    """Small exact-law trend check at the c=.95 half-density seed.

    This is deliberately labelled diagnostic: it does not certify the very
    large windows required by the theorem's current uniform error budget.
    """
    rows = []
    for n in (6, 8, 10, 12):
        kernel = sine_kernel(n, 0.5, 0.95, 0.025)
        for core_size in (2, 4):
            start = (n - core_size) // 2
            core = tuple(range(start, start + core_size))
            e_phi = 0.0
            e_chi = 0.0
            mass = 0.0
            for word in range(1 << n):
                y = bits(word, n)
                probability = atom_probability(kernel, y)
                g = np.linalg.inv(kernel - np.diag(1 - y))
                x = g[np.ix_(core, core)]
                e_phi += probability * potential(x, core, "phi")
                e_chi += probability * potential(x, core, "chi")
                mass += probability
            rows.append({
                "n_observed": n,
                "core_size": core_size,
                "halo_each_side": (n - core_size) // 2,
                "probability_mass_error": abs(mass - 1.0),
                "W_diagnostic": -e_phi / core_size,
                "V_diagnostic": e_chi / core_size,
            })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = dt.datetime.now(dt.timezone.utc)
    delta = 0.02
    c = 0.95
    a = delta
    rho = 0.5
    const = constants(delta, c)

    full_law = []
    reveal = []
    for n in (4, 6, 8):
        kernel = sine_kernel(n, rho, c, a)
        full_law.append(check_full_law(kernel, delta, c))
        if n >= 6:
            reveal.append(reveal_checks(kernel, (n // 2 - 1, n // 2, n // 2 + 1), n - 1, delta, const))

    # Additional legal parameters test that the replay is not tuned to the
    # half-density benchmark.  The theorem itself is analytic and uniform on
    # compact legal parameter sets; these remain floating spot checks.
    for case in (
        {"n": 6, "rho": 0.2, "c": 0.93, "a": 0.03},
        {"n": 6, "rho": 0.8, "c": 0.97, "a": 0.01},
    ):
        case_delta = min(case["a"], 1.0 - case["a"] - case["c"])
        case_const = constants(case_delta, case["c"])
        kernel = sine_kernel(case["n"], case["rho"], case["c"], case["a"])
        law_row = check_full_law(kernel, case_delta, case["c"])
        law_row.update({"rho": case["rho"], "c": case["c"], "a": case["a"], "delta": case_delta})
        full_law.append(law_row)
        reveal_row = reveal_checks(kernel, (2, 3, 4), 5, case_delta, case_const)
        reveal_row.update({"rho": case["rho"], "c": case["c"], "a": case["a"], "delta": case_delta})
        reveal.append(reveal_row)

    checks = {
        "ward_pointwise": min(row["minimum_eigenvalue_R_minus_delta_G2"] for row in full_law) >= -2e-8,
        "ward_expectation": max(row["maximum_abs_E_R_minus_2I"] for row in full_law) <= 2e-8,
        "expected_G2": max(row["maximum_eigenvalue_E_G2_minus_2_over_delta_I"] for row in full_law) <= 2e-8,
        "tail": min(t["slack"] for row in full_law for t in row["tail"]) >= -2e-8,
        "rank_one_hessian": max(row["maximum_pair_hessian_relative_error_scaled"] for row in reveal) <= 3e-5,
        "sign_dichotomy": min(row["minimum_equal_sign_hessian_formula"] for row in reveal) >= -2e-10 and max(row["maximum_opposite_sign_hessian_formula"] for row in reveal) <= 2e-10,
        "interpolation_row_coercivity": max(row["maximum_interpolation_row_coercivity_violation"] for row in reveal) <= 2e-8,
        "weighted_row_bound": max(row["maximum_weighted_row_violation"] for row in reveal) <= 2e-8,
        "pair_ratio_bound": max(row["maximum_pair_ratio_minus_kappa"] for row in reveal) <= 2e-8,
        "weighted_hessian_phi": min(row["minimum_weighted_phi_hessian_margin"] for row in reveal) >= -2e-8,
        "weighted_hessian_chi": min(row["minimum_weighted_chi_hessian_margin"] for row in reveal) >= -2e-8,
        "uniform_hessian_phi": min(row["minimum_uniform_phi_hessian_margin"] for row in reveal) >= -2e-8,
        "uniform_hessian_chi": min(row["minimum_uniform_chi_hessian_margin"] for row in reveal) >= -2e-8,
        "one_reveal_phi": min(row["minimum_phi_one_reveal_margin"] for row in reveal) >= -2e-8,
        "one_reveal_chi": min(row["minimum_chi_one_reveal_margin"] for row in reveal) >= -2e-8,
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    report = {
        "status": "PASS_FLOATING_REPLAY_SUPPORTS_SCOPED_THEOREM",
        "execution": {
            "started_utc": started.isoformat(),
            "finished_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "python": platform.python_version(),
            "numpy": np.__version__,
        },
        "scope": {
            "model": "finite compressions of K=aI+cQ_rho",
            "rho": rho,
            "c": c,
            "a": a,
            "delta": delta,
            "sizes": [4, 6, 8],
            "warning": "floating finite checks support but do not prove the all-volume theorem",
        },
        "constants": const,
        "benchmark": benchmark(const),
        "finite_window_diagnostic": finite_window_diagnostic(),
        "checks": checks,
        "full_law": full_law,
        "reveals": reveal,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": report["status"],
        "checks": checks,
        "constants": const,
        "benchmark": report["benchmark"],
        "reveal_summary": reveal,
    }, indent=2))


if __name__ == "__main__":
    main()
