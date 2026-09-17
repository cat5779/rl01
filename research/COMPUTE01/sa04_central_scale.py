"""Exploratory central-layer diagnostics for SA04.

For a fixed latent k-set A, the Bernoulli--Laplace heat flow is reduced to the
birth--death chain R=|S intersect A^c|.  The mixture over the Fourier projection
DPP is recovered from the determinantal overlap-count generating polynomial.

All times are the report's original times s_l.  The output keeps A_l, E_l,
d_l, w_l, and W_n separate.  Binary64 finite-n data are exploratory and do not
prove an asymptotic scale.
"""

from __future__ import annotations

import argparse
import cmath
import json
from fractions import Fraction
from itertools import combinations
from math import comb, log, sqrt
from pathlib import Path

import numpy as np


Z = 1521
B = Fraction(39, 1600)


def polynomial_coefficient(power: int, degree: int, z: int = Z) -> int:
    if degree < 0 or degree > 2 * power:
        return 0
    return sum(
        comb(power, degree - right) * comb(power, right) * z**right
        for right in range(max(0, degree - power), min(power, degree) + 1)
    )


def theta(k: int, layer: int) -> float:
    if not 2 <= layer <= k:
        raise ValueError("theta is defined here only for 2 <= layer <= k")
    numerator_coefficient = polynomial_coefficient(k - 2, layer - 2)
    partition_coefficient = polynomial_coefficient(k, layer)
    alpha = Fraction(layer * (layer - 1), k * (k - 1))
    value = Fraction((Z - 1) ** 2 * numerator_coefficient, 1) / (
        alpha * partition_coefficient
    )
    return float(value)


def original_time(n: int, layer: int) -> float:
    return -log(theta(n // 2, layer)) / (2.0 * (n - 1))


def projection_matrix(n: int) -> np.ndarray:
    k = n // 2
    matrix = np.empty((n, n), dtype=np.complex128)
    for row in range(n):
        for column in range(n):
            matrix[row, column] = sum(
                cmath.exp(2j * cmath.pi * frequency * (row - column) / n)
                for frequency in range(k)
            ) / n
    return matrix


def stationary_shell_law(n: int, layer: int) -> np.ndarray:
    k = n // 2
    denominator = comb(n, layer)
    return np.array(
        [comb(k, layer - radius) * comb(k, radius) / denominator for radius in range(layer + 1)],
        dtype=np.float64,
    )


def birth_death_generator(n: int, layer: int) -> np.ndarray:
    k = n // 2
    generator = np.zeros((layer + 1, layer + 1), dtype=np.float64)
    for radius in range(layer + 1):
        birth = (layer - radius) * (k - radius)
        death = radius * (k - layer + radius)
        if radius < layer:
            generator[radius, radius + 1] = birth
        if radius > 0:
            generator[radius, radius - 1] = death
        generator[radius, radius] = -(birth + death)
    return generator


def chain_law(n: int, layer: int, time: float) -> np.ndarray:
    stationary = stationary_shell_law(n, layer)
    generator = birth_death_generator(n, layer)
    root = np.sqrt(stationary)
    symmetric = root[:, None] * generator / root[None, :]
    eigenvalues, eigenvectors = np.linalg.eigh(symmetric)
    exponential = (eigenvectors * np.exp(time * eigenvalues)) @ eigenvectors.T
    transition = exponential * root[None, :] / root[:, None]
    law = transition[0].copy()
    law[np.abs(law) < 5e-15] = 0.0
    if law.min() < -5e-13 or abs(law.sum() - 1.0) > 5e-13:
        raise AssertionError(
            f"invalid birth-death law n={n}, l={layer}, s={time}: "
            f"min={law.min()}, mass={law.sum()}"
        )
    return law / law.sum()


def poisson_binomial(eigenvalues: np.ndarray) -> np.ndarray:
    coefficients = np.array([1.0], dtype=np.float64)
    for eigenvalue in eigenvalues:
        value = float(np.clip(eigenvalue, 0.0, 1.0))
        updated = np.zeros(len(coefficients) + 1, dtype=np.float64)
        updated[:-1] += coefficients * (1.0 - value)
        updated[1:] += coefficients * value
        coefficients = updated
    return coefficients


def cyclic_orbit(state: tuple[int, ...], n: int) -> set[tuple[int, ...]]:
    return {
        tuple(sorted((index + shift) % n for index in state))
        for shift in range(n)
    }


def overlap_laws(
    projection: np.ndarray, layer: int
) -> tuple[np.ndarray, np.ndarray]:
    rows: list[np.ndarray] = []
    multiplicities: list[int] = []
    n = projection.shape[0]
    for state in combinations(range(projection.shape[0]), layer):
        orbit = cyclic_orbit(state, n)
        if state != min(orbit):
            continue
        principal = projection[np.ix_(state, state)]
        eigenvalues = np.linalg.eigvalsh(principal)
        count_in_state = poisson_binomial(eigenvalues)
        rows.append(count_in_state[::-1])  # radius = layer - |A intersect S|
        multiplicities.append(len(orbit))
    laws = np.stack(rows)
    weights = np.array(multiplicities, dtype=np.float64)
    mass_error = float(np.max(np.abs(laws.sum(axis=1) - 1.0)))
    if mass_error > 2e-13 or laws.min() < -2e-15:
        raise AssertionError(
            f"invalid overlap laws l={layer}: mass error={mass_error}, min={laws.min()}"
        )
    if int(weights.sum()) != comb(n, layer):
        raise AssertionError(
            f"cyclic orbit sizes do not cover layer n={n}, l={layer}"
        )
    return laws, weights


def layer_entropy(
    n: int,
    layer: int,
    time: float,
    overlap_data: tuple[np.ndarray, np.ndarray],
) -> tuple[float, dict[str, float]]:
    overlap, multiplicities = overlap_data
    chain = chain_law(n, layer, time)
    shell_sizes = np.array(
        [comb(n // 2, layer - radius) * comb(n // 2, radius) for radius in range(layer + 1)],
        dtype=np.float64,
    )
    density = comb(n, layer) * (overlap @ (chain / shell_sizes))
    if density.min() <= 0.0:
        raise AssertionError(f"non-positive layer density n={n}, l={layer}")
    state_count = comb(n, layer)
    mean_error = float(abs(np.dot(multiplicities, density) / state_count - 1.0))
    if mean_error > 5e-12:
        raise AssertionError(
            f"layer density does not normalize n={n}, l={layer}: {mean_error}"
        )
    entropy = float(
        np.dot(multiplicities, density * np.log(density)) / state_count
    )
    diagnostics = {
        "density_mean_error": mean_error,
        "density_min": float(density.min()),
        "density_max": float(density.max()),
        "chain_mass_error": float(abs(chain.sum() - 1.0)),
        "cyclic_orbit_count": float(len(density)),
    }
    return entropy, diagnostics


def layer_entropy_dissipation(
    n: int,
    layer: int,
    time: float,
    overlap_data: tuple[np.ndarray, np.ndarray],
) -> float:
    """Return -d/ds F_l(s) at the specified original time."""
    overlap, multiplicities = overlap_data
    chain = chain_law(n, layer, time)
    chain_derivative = chain @ birth_death_generator(n, layer)
    shell_sizes = np.array(
        [comb(n // 2, layer - radius) * comb(n // 2, radius) for radius in range(layer + 1)],
        dtype=np.float64,
    )
    state_count = comb(n, layer)
    density = state_count * (overlap @ (chain / shell_sizes))
    density_derivative = state_count * (
        overlap @ (chain_derivative / shell_sizes)
    )
    mass_derivative = float(np.dot(multiplicities, density_derivative) / state_count)
    if abs(mass_derivative) > 2e-9:
        raise AssertionError(
            f"density derivative has nonzero mass n={n}, l={layer}: {mass_derivative}"
        )
    entropy_derivative = float(
        np.dot(multiplicities, density_derivative * np.log(density)) / state_count
    )
    return -entropy_derivative


def convolve(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    output = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for left_degree, left_value in enumerate(left):
        for right_degree, right_value in enumerate(right):
            output[left_degree + right_degree] += left_value * right_value
    return output


def b_weights(n: int) -> list[float]:
    k = n // 2
    eta = Fraction(k - 1, 1) + 2 * B
    eta /= 2 * (2 * k - 1)
    phi = [B, 1 - 2 * B, B]
    psi = [eta, 1 - 2 * eta, eta]
    polynomial = [Fraction(1)]
    for _ in range(k - 2):
        polynomial = convolve(polynomial, phi)
    polynomial = convolve(polynomial, psi)
    return [float(n * (n - 1) * coefficient) for coefficient in polynomial]


def diagnose_n(n: int) -> dict[str, object]:
    if n < 6 or n % 2:
        raise ValueError("n must be even and at least 6")
    k = n // 2
    projection = projection_matrix(n)
    projection_errors = {
        "hermitian": float(np.max(np.abs(projection - projection.conj().T))),
        "idempotent": float(np.max(np.abs(projection @ projection - projection))),
        "trace": float(abs(np.trace(projection).real - k)),
    }

    times = {layer: original_time(n, layer) for layer in range(2, k + 1)}
    entropies_at_own_time = {0: 0.0, 1: 0.0}
    records: list[dict[str, float | int | dict[str, float]]] = []
    max_density_mass_error = 0.0

    overlap_cache: dict[int, tuple[np.ndarray, np.ndarray]] = {}
    for layer in range(2, k + 1):
        overlap_cache[layer] = overlap_laws(projection, layer)
        own_entropy, own_diag = layer_entropy(
            n, layer, times[layer], overlap_cache[layer]
        )
        entropies_at_own_time[layer] = own_entropy
        max_density_mass_error = max(
            max_density_mass_error, own_diag["density_mean_error"]
        )

    weights = b_weights(n)
    previous_b = weights[0]
    d_values = {1: 0.0}
    for layer in range(2, k + 1):
        weight = weights[layer - 1] - previous_b
        previous_b = weights[layer - 1]
        if layer == 2:
            deletion = entropies_at_own_time[2]
            bridge = 0.0
        else:
            previous_layer_same_time, same_time_diag = layer_entropy(
                n, layer - 1, times[layer], overlap_cache[layer - 1]
            )
            max_density_mass_error = max(
                max_density_mass_error, same_time_diag["density_mean_error"]
            )
            deletion = entropies_at_own_time[layer] - previous_layer_same_time
            bridge = (
                entropies_at_own_time[layer - 1] - previous_layer_same_time
            )
        difference = deletion - bridge
        d_values[layer] = difference
        records.append(
            {
                "layer": layer,
                "s_l": times[layer],
                "h_l": entropies_at_own_time[layer],
                "A_l": deletion,
                "E_l": bridge,
                "d_l": difference,
                "sqrt_n_times_d_l": sqrt(n) * difference,
                "w_l": weight,
                "w_l_times_d_l": weight * difference,
            }
        )

    weighted_transport = -2.0 * sum(
        record["w_l_times_d_l"] for record in records
    )
    h = [0.0] * (n + 1)
    for layer in range(k + 1):
        h[layer] = entropies_at_own_time[layer]
        h[n - layer] = entropies_at_own_time[layer]
    direct_curvature = sum(
        weights[index] * (h[index + 2] - 2.0 * h[index + 1] + h[index])
        for index in range(n - 1)
    )

    central_previous_layer = k - 1
    central_gap = times[k] - times[central_previous_layer]
    central_rate = central_previous_layer * (n - central_previous_layer)
    initial_bridge_dissipation = layer_entropy_dissipation(
        n,
        central_previous_layer,
        times[central_previous_layer],
        overlap_cache[central_previous_layer],
    )
    central_bridge = {
        "time_gap": central_gap,
        "mean_jump_count": central_rate * central_gap,
        "initial_entropy_dissipation": initial_bridge_dissipation,
        "initial_per_jump_entropy_dissipation": (
            initial_bridge_dissipation / central_rate
        ),
        "monotonicity_upper_bound_for_E_k": (
            central_gap * initial_bridge_dissipation
        ),
        "actual_E_k": records[-1]["E_l"],
    }

    return {
        "n": n,
        "k": k,
        "projection_errors": projection_errors,
        "max_density_mean_error": max_density_mass_error,
        "layers": records,
        "central": records[-1],
        "central_bridge": central_bridge,
        "W_from_weighted_transport": weighted_transport,
        "W_from_direct_curvature": direct_curvature,
        "W_identity_error": weighted_transport - direct_curvature,
        "B_mass_error": sum(weights) - n * (n - 1),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sizes",
        nargs="+",
        type=int,
        default=[6, 8, 10, 12, 14, 16],
        help="even dimensions to diagnose",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("sa04_central_scale_result.json"),
    )
    arguments = parser.parse_args()
    results = [diagnose_n(n) for n in arguments.sizes]
    receipt = {
        "status": "EXPLORATORY",
        "scope": "CORRECTED_LAW_ONLY",
        "method": (
            "fixed-A overlap birth-death chain plus determinantal overlap-count "
            "mixture; original times s_l; binary64 eigensolvers"
        ),
        "results": results,
        "limitations": [
            "Finite-n binary64 diagnostics do not prove an asymptotic order.",
            "A_l and E_l are reported separately because their cancellation is the target.",
            "No interval error certificate is attached to these exploratory values.",
        ],
    }
    arguments.output.write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
