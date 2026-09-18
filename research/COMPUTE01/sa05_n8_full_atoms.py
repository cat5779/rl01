"""Independent 256-atom regression for the SA05 n=8 certificate.

The true output law is reconstructed from the rank-four Fourier DPP and the
coordinatewise binary channel.  This path does not use the 70-state formula
for the true layer density.  The corrected law differs only on layer four,
where the handoff's correction is inserted.  Second derivatives are obtained
with forward jets, never finite differences.

This is a binary64 algebraic regression around the separately certified
70-state interval calculation.  It is not an interval certificate by itself.
"""

from __future__ import annotations

import cmath
import json
from fractions import Fraction
from itertools import combinations, permutations
from math import fsum
from pathlib import Path

from sa05_n8_explore import DATA, STATES, Jet2, curvature


N = 8
K = 4
C = 19.0 / 20.0
POINTS = (Fraction(1, 200), Fraction(1, 50), Fraction(1, 40))


def permutation_sign(order: tuple[int, ...]) -> int:
    inversions = sum(
        order[left] > order[right]
        for left in range(len(order))
        for right in range(left + 1, len(order))
    )
    return -1 if inversions % 2 else 1


PERMUTATIONS = tuple((order, permutation_sign(order)) for order in permutations(range(K)))


def projection_entry(row: int, column: int) -> complex:
    return sum(
        cmath.exp(2j * cmath.pi * frequency * (row - column) / N)
        for frequency in range(K)
    ) / N


def principal_minor(state: tuple[int, ...]) -> complex:
    matrix = tuple(
        tuple(projection_entry(row, column) for column in state) for row in state
    )
    determinant = 0j
    for order, sign in PERMUTATIONS:
        term = complex(sign)
        for row, column in enumerate(order):
            term *= matrix[row][column]
        determinant += term
    return determinant


def latent_dpp_weights() -> dict[tuple[int, ...], float]:
    weights: dict[tuple[int, ...], float] = {}
    for state in STATES:
        determinant = principal_minor(state)
        if abs(determinant.imag) > 2e-16:
            raise AssertionError(f"non-real DPP weight at {state}: {determinant}")
        if determinant.real < -2e-16:
            raise AssertionError(f"negative DPP weight at {state}: {determinant.real}")
        weights[state] = determinant.real
    return weights


LATENT_WEIGHTS = latent_dpp_weights()


def polynomial_product(
    left: list[Jet2], right: list[Jet2]
) -> list[Jet2]:
    output = [Jet2(0.0) for _ in range(len(left) + len(right) - 1)]
    for left_degree, left_value in enumerate(left):
        for right_degree, right_value in enumerate(right):
            output[left_degree + right_degree] += left_value * right_value
    return output


def count_weights(a: Jet2) -> list[Jet2]:
    high = a + C
    low = a
    polynomial = [Jet2(1.0)]
    for probability in (high,) * K + (low,) * K:
        polynomial = polynomial_product(
            polynomial, [1.0 - probability, probability]
        )
    return polynomial


def output_state(mask: int) -> tuple[int, ...]:
    return tuple(index for index in range(N) if mask & (1 << index))


OUTPUT_STATES = tuple(output_state(mask) for mask in range(1 << N))


def jet_sum(values: list[Jet2]) -> Jet2:
    return Jet2(
        fsum(value.value for value in values),
        fsum(value.first for value in values),
        fsum(value.second for value in values),
    )


def true_output_atoms(a: Jet2) -> list[Jet2]:
    high = a + C
    low = a
    atoms: list[Jet2] = []
    for output in OUTPUT_STATES:
        output_set = set(output)
        contributions: list[Jet2] = []
        for latent, weight in LATENT_WEIGHTS.items():
            latent_set = set(latent)
            channel = Jet2(1.0)
            for index in range(N):
                probability = high if index in latent_set else low
                channel *= probability if index in output_set else 1.0 - probability
            contributions.append(weight * channel)
        atoms.append(jet_sum(contributions))
    return atoms


def corrected_layer_four_density(a: Jet2, state_index: int) -> Jet2:
    xi = a * (1.0 / 20.0 - a) / C
    q2 = 1.0 + 6.0 * xi + 6.0 * xi**2
    q4 = 1.0 + 20.0 * xi + 90.0 * xi**2 + 140.0 * xi**3 + 70.0 * xi**4
    ratio = q2 / q4
    corrected_ratio = ratio ** (10.0 / 7.0)
    _, v2, v4 = DATA[state_index]
    return 1.0 + ratio * v2 + corrected_ratio * v4


def corrected_output_atoms(
    a: Jet2, true_atoms: list[Jet2], pi: list[Jet2]
) -> list[Jet2]:
    state_to_index = {state: index for index, state in enumerate(STATES)}
    corrected: list[Jet2] = []
    for state, true_atom in zip(OUTPUT_STATES, true_atoms):
        if len(state) != K:
            corrected.append(true_atom)
            continue
        density = corrected_layer_four_density(a, state_to_index[state])
        corrected.append(pi[K] * density / 70.0)
    return corrected


def jet_fields(value: Jet2) -> dict[str, float]:
    return {
        "value": value.value,
        "first": value.first,
        "second": value.second,
    }


def jet_max_abs(value: Jet2) -> float:
    return max(abs(value.value), abs(value.first), abs(value.second))


def entropy(atoms: list[Jet2]) -> Jet2:
    return -jet_sum([atom * atom.logarithm() for atom in atoms])


def layer_mass(atoms: list[Jet2], layer: int) -> Jet2:
    return jet_sum(
        [atom for atom, state in zip(atoms, OUTPUT_STATES) if len(state) == layer]
    )


def evaluate(point: Fraction) -> dict[str, object]:
    a = Jet2(float(point), 1.0, 0.0)
    pi = count_weights(a)
    true_atoms = true_output_atoms(a)
    corrected_atoms = corrected_output_atoms(a, true_atoms, pi)

    true_mass = jet_sum(true_atoms)
    corrected_mass = jet_sum(corrected_atoms)
    layer_errors = [layer_mass(true_atoms, layer) - pi[layer] for layer in range(N + 1)]

    true_q_errors: list[Jet2] = []
    corrected_q_errors: list[Jet2] = []
    for layer in range(N + 1):
        true_q_mass = layer_mass(true_atoms, layer) / pi[layer]
        corrected_q_mass = layer_mass(corrected_atoms, layer) / pi[layer]
        true_q_errors.append(true_q_mass - 1.0)
        corrected_q_errors.append(corrected_q_mass - 1.0)

    full_entropy_difference = entropy(corrected_atoms) - entropy(true_atoms)
    reduced_formula = curvature(float(point))
    formula_error = full_entropy_difference - reduced_formula

    tolerance = 3e-11
    rare_layer_q_tolerance = 2e-8
    checks = {
        "latent_weight_sum_error": abs(sum(LATENT_WEIGHTS.values()) - 1.0),
        "latent_min_weight": min(LATENT_WEIGHTS.values()),
        "latent_max_imaginary_part": max(
            abs(principal_minor(state).imag) for state in STATES
        ),
        "true_total_mass_error": jet_max_abs(true_mass - 1.0),
        "corrected_total_mass_error": jet_max_abs(corrected_mass - 1.0),
        "max_count_weight_error": max(map(jet_max_abs, layer_errors)),
        "max_true_layer_q_mass_error": max(map(jet_max_abs, true_q_errors)),
        "max_corrected_layer_q_mass_error": max(
            map(jet_max_abs, corrected_q_errors)
        ),
        "min_true_atom": min(atom.value for atom in true_atoms),
        "min_corrected_atom": min(atom.value for atom in corrected_atoms),
        "max_formula_component_error": jet_max_abs(formula_error),
    }
    if any(
        checks[key] > tolerance
        for key in (
            "latent_weight_sum_error",
            "true_total_mass_error",
            "corrected_total_mass_error",
            "max_count_weight_error",
            "max_formula_component_error",
        )
    ):
        raise AssertionError(f"256-atom regression failed at a={point}: {checks}")
    if (
        checks["max_true_layer_q_mass_error"] > rare_layer_q_tolerance
        or checks["max_corrected_layer_q_mass_error"] > rare_layer_q_tolerance
    ):
        raise AssertionError(f"rare-layer q regression failed at a={point}: {checks}")
    if checks["min_true_atom"] <= 0.0 or checks["min_corrected_atom"] <= 0.0:
        raise AssertionError(f"non-positive atom at a={point}: {checks}")

    return {
        "a": str(point),
        "full_entropy_difference": jet_fields(full_entropy_difference),
        "reduced_70_state_formula": jet_fields(reduced_formula),
        "difference": jet_fields(formula_error),
        "checks": checks,
    }


def main() -> None:
    results = [evaluate(point) for point in POINTS]
    receipt = {
        "status": "BINARY64_INDEPENDENT_REGRESSION",
        "model": {
            "n": N,
            "rank": K,
            "c": "19/20",
            "latent_states": len(STATES),
            "output_atoms": len(OUTPUT_STATES),
        },
        "method": (
            "Direct 4x4 Fourier projection minors, latent DPP mixture, "
            "and coordinatewise channel; second-order forward jets."
        ),
        "points": results,
        "limitation": (
            "This cross-check uses binary64 arithmetic. Rigorous signs come from "
            "sa05_n8_interval.py, not from this regression."
        ),
    }
    output_path = Path(__file__).with_name("sa05_n8_full_atoms_result.json")
    output_path.write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
