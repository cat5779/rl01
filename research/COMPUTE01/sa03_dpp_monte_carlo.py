"""Monte Carlo scout for the SA03 full-word local residual.

The exterior word is sampled from its genuine marginal-kernel DPP by the
standard eigenvector/projection-DPP algorithm.  Conditional resolvent rank-one
updates then evaluate all four compensated residual components.  The output is
route-selection evidence only; its standard errors do not certify the u
quadrature or rare tails.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

from sa03_exact_finite import C, breg_phi, breg_phi1, model, phi1, phi2


def sample_dpp(
    eigenvalues: np.ndarray,
    eigenvectors: np.ndarray,
    rng: np.random.Generator,
) -> np.ndarray:
    chosen = rng.random(eigenvalues.size) < eigenvalues
    vectors = eigenvectors[:, chosen]
    n = eigenvectors.shape[0]
    word = np.zeros(n, dtype=np.int8)
    while vectors.shape[1]:
        rank = vectors.shape[1]
        probabilities = np.sum(vectors * vectors, axis=1) / rank
        probabilities[word.astype(bool)] = 0.0
        probabilities /= np.sum(probabilities)
        site = int(rng.choice(n, p=probabilities))
        word[site] = 1
        if rank == 1:
            break
        row_mass = vectors[site] * vectors[site]
        row_mass /= np.sum(row_mass)
        pivot_column = int(rng.choice(rank, p=row_mass))
        pivot = vectors[:, pivot_column].copy()
        keep = np.arange(rank) != pivot_column
        reduced = vectors[:, keep] - np.outer(pivot, vectors[site, keep] / pivot[site])
        vectors, _ = np.linalg.qr(reduced, mode="reduced")
    return word


def local_components(h0: np.ndarray, b0: np.ndarray, u: float, word: np.ndarray) -> np.ndarray:
    sigma = (2 * word - 1).astype(np.float64)
    matrix = u * h0 + np.diag(0.5 * sigma)
    inverse = np.linalg.inv(matrix)
    ub = u * b0
    v = inverse @ ub
    q = 0.5 - float(ub @ v)
    az = 1.0 + float(v @ v)
    diagonal = np.diag(inverse)
    odds = sigma * diagonal - 1.0
    rbar = sigma - diagonal
    delta_q = sigma * v * v / odds
    q_neighbor = q + delta_q

    bphi_edges = breg_phi(q_neighbor, q)
    bbar_phi = float(rbar @ bphi_edges)
    component_curvature = float(phi2(q) - 8.0)
    component_breg_phi1 = float(rbar @ breg_phi1(q_neighbor, q))
    g2diag = np.einsum("ij,ji->i", inverse, inverse)
    component_parameter = float(g2diag @ bphi_edges)

    neighbor_a = np.empty(word.size, dtype=np.float64)
    neighbor_bbar_phi = np.empty(word.size, dtype=np.float64)
    for j in range(word.size):
        factor = sigma[j] / odds[j]
        column = inverse[:, j]
        inverse_j = inverse - factor * np.outer(column, column)
        v_j = v - factor * v[j] * column
        q_j = q_neighbor[j]
        neighbor_a[j] = 1.0 + float(v_j @ v_j)
        sigma_j = sigma.copy()
        sigma_j[j] *= -1.0
        diagonal_j = np.diag(inverse_j)
        odds_j = sigma_j * diagonal_j - 1.0
        rbar_j = sigma_j - diagonal_j
        delta_j = sigma_j * v_j * v_j / odds_j
        neighbor_bbar_phi[j] = float(rbar_j @ breg_phi(q_j + delta_j, q_j))

    component_parameter += float(
        rbar
        @ (
            (phi1(q_neighbor) - phi1(q)) * neighbor_a
            - phi2(q) * delta_q * az
        )
    )
    component_transport = float(rbar @ (neighbor_bbar_phi - bbar_phi))
    return np.array(
        [component_curvature, component_breg_phi1, component_parameter, component_transport],
        dtype=np.float64,
    )


def pointwise(radius: int, u: float, samples: int, rng: np.random.Generator) -> dict[str, object]:
    h0, b0 = model(radius)
    kernel = 0.5 * np.eye(2 * radius) + u * h0
    eigenvalues, eigenvectors = np.linalg.eigh(kernel)
    eigenvalues = np.clip(eigenvalues, 0.0, 1.0)
    values = np.empty((samples, 4), dtype=np.float64)
    counts = np.empty(samples, dtype=np.float64)
    for sample in range(samples):
        word = sample_dpp(eigenvalues, eigenvectors, rng)
        counts[sample] = np.sum(word)
        values[sample] = local_components(h0, b0, u, word)
    means = np.mean(values, axis=0)
    standard_errors = np.std(values, axis=0, ddof=1) / math.sqrt(samples)
    totals = 8.0 + np.sum(values, axis=1)
    keys = ["curvature_minus_8", "bregman_phi_prime", "parameter_derivative", "signed_transport"]
    return {
        "u": u,
        "samples": samples,
        "normalized_components": dict(zip(keys, map(float, means))),
        "component_standard_errors": dict(zip(keys, map(float, standard_errors))),
        "normalized_total": float(np.mean(totals)),
        "normalized_total_standard_error": float(np.std(totals, ddof=1) / math.sqrt(samples)),
        "mean_count": float(np.mean(counts)),
        "count_standard_error": float(np.std(counts, ddof=1) / math.sqrt(samples)),
    }


def integrate(radius: int, nodes: int, samples: int, seed: int) -> dict[str, object]:
    lo = 1.0 / (radius + 1.0)
    x, w = np.polynomial.legendre.leggauss(nodes)
    us = lo + 0.5 * (1.0 - lo) * (x + 1.0)
    ws = 0.5 * (1.0 - lo) * w
    rng = np.random.default_rng(seed)
    rows = []
    for index, u in enumerate(us):
        row = pointwise(radius, float(u), samples, rng)
        rows.append(row)
        print(
            f"R={radius} node={index + 1}/{nodes} u={u:.6f} "
            f"Gbar={row['normalized_total']:+.6f} +/- {row['normalized_total_standard_error']:.6f}",
            flush=True,
        )
    keys = ["curvature_minus_8", "bregman_phi_prime", "parameter_derivative", "signed_transport"]
    integrated = {}
    integrated_se = {}
    for key in keys:
        integrated[key] = float(
            sum(weight * u * row["normalized_components"][key] for weight, u, row in zip(ws, us, rows))
        )
        integrated_se[key] = float(
            math.sqrt(
                sum(
                    (weight * u * row["component_standard_errors"][key]) ** 2
                    for weight, u, row in zip(ws, us, rows)
                )
            )
        )
    baseline = 4.0 * (1.0 - lo * lo)
    total = baseline + sum(integrated.values())
    total_se = math.sqrt(
        sum(
            (weight * u * row["normalized_total_standard_error"]) ** 2
            for weight, u, row in zip(ws, us, rows)
        )
    )
    return {
        "R": radius,
        "external_bits": 2 * radius,
        "nodes": nodes,
        "samples_per_node": samples,
        "seed": seed,
        "baseline": baseline,
        "integrated_residual_components": integrated,
        "naive_component_standard_errors": integrated_se,
        "A_R_second_derivative_estimate": total,
        "naive_total_standard_error": total_se,
        "quadrature_rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--radii", nargs="+", type=int, default=[7, 12, 20])
    parser.add_argument("--nodes", type=int, default=12)
    parser.add_argument("--samples", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=20260918)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("sa03_dpp_monte_carlo_result.json"),
    )
    args = parser.parse_args()
    limitations = [
        "Reported errors are iid sampling errors conditional on the quadrature nodes.",
        "They do not certify Gauss-Legendre error or rare-tail control.",
        "The scout chooses an analytic route and does not prove the sign of Gamma(19/20).",
    ]
    results = []
    for radius in args.radii:
        results.append(integrate(radius, args.nodes, args.samples, args.seed + radius))
        payload = {
            "status": "EXPLORATORY_TRUE_DPP_MONTE_CARLO",
            "contrast": C,
            "results": results,
            "limitations": limitations,
        }
        args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
