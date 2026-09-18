"""Exact full-word finite-R diagnostics for SA03.

This script enumerates the genuine physical exterior words of the Fejer
Toeplitz DPP.  It evaluates the normalized local kernel (V14), split into
the four residual components requested in COMPUTATION_HANDOFF.md, and then
uses Gauss--Legendre quadrature in u.  It is a finite diagnostic, not an
asymptotic sign certificate for Gamma(c).
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


C = 19.0 / 20.0


def fourier_q(k: int) -> float:
    if k == 0:
        return 0.5
    return math.sin(math.pi * k / 2.0) / (math.pi * k)


def fejer_coefficient(k: int, radius: int) -> float:
    ak = abs(k)
    if ak > radius:
        return 0.0
    return (1.0 - ak / (radius + 1.0)) * fourier_q(k)


def model(radius: int) -> tuple[np.ndarray, np.ndarray]:
    sites = [i for i in range(-radius, radius + 1) if i != 0]
    q_ext = np.array(
        [[fejer_coefficient(i - j, radius) for j in sites] for i in sites],
        dtype=np.float64,
    )
    q_col = np.array([fejer_coefficient(i, radius) for i in sites], dtype=np.float64)
    h0 = C * (q_ext - 0.5 * np.eye(len(sites)))
    b0 = C * q_col
    return h0, b0


def all_words(n: int) -> tuple[np.ndarray, np.ndarray]:
    ids = np.arange(1 << n, dtype=np.uint32)
    shifts = np.arange(n, dtype=np.uint32)
    bits = ((ids[:, None] >> shifts[None, :]) & 1).astype(np.int8)
    sigma = (2 * bits - 1).astype(np.float64)
    return ids, sigma


def phi(q: np.ndarray) -> np.ndarray:
    return (q - 0.5) * np.log(q / (1.0 - q))


def phi1(q: np.ndarray) -> np.ndarray:
    return np.log(q / (1.0 - q)) + (q - 0.5) / (q * (1.0 - q))


def phi2(q: np.ndarray) -> np.ndarray:
    return 1.0 / (2.0 * q * q * (1.0 - q) * (1.0 - q))


def breg_phi(p: np.ndarray, q: np.ndarray) -> np.ndarray:
    return phi(p) - phi(q) - phi1(q) * (p - q)


def breg_phi1(p: np.ndarray, q: np.ndarray) -> np.ndarray:
    return phi1(p) - phi1(q) - phi2(q) * (p - q)


def pointwise(radius: int, u: float, batch_size: int) -> dict[str, float]:
    h0, b0 = model(radius)
    n = h0.shape[0]
    ids = np.arange(1 << n, dtype=np.uint32)
    word_count = ids.size
    shifts = np.arange(n, dtype=np.uint32)
    diagonal = np.arange(n)
    ub = u * b0
    logabsdet = np.empty(word_count, dtype=np.float64)
    q = np.empty(word_count, dtype=np.float64)
    az = np.empty(word_count, dtype=np.float64)
    rbar = np.empty((word_count, n), dtype=np.float64)
    g2diag = np.empty((word_count, n), dtype=np.float64)

    # One batched inverse pass.  Keeping only the quantities used by V14
    # makes R=9 feasible without materializing every 18x18 inverse at once.
    for start in range(0, word_count, batch_size):
        stop = min(word_count, start + batch_size)
        batch_ids = ids[start:stop]
        bits = ((batch_ids[:, None] >> shifts[None, :]) & 1).astype(np.int8)
        sigma = (2 * bits - 1).astype(np.float64)
        matrices = np.broadcast_to(u * h0, (stop - start, n, n)).copy()
        matrices[:, diagonal, diagonal] += 0.5 * sigma
        sign, batch_logabsdet = np.linalg.slogdet(matrices)
        expected_sign = np.where(((n - np.sum(bits, axis=1)) & 1) == 0, 1.0, -1.0)
        if not np.all(sign == expected_sign):
            raise RuntimeError(f"unexpected atom determinant sign at R={radius}, u={u}")
        inverse = np.linalg.inv(matrices)
        v = inverse @ ub
        logabsdet[start:stop] = batch_logabsdet
        q[start:stop] = 0.5 - np.einsum("i,wi->w", ub, v)
        az[start:stop] = 1.0 + np.einsum("wi,wi->w", v, v)
        rbar[start:stop] = sigma - np.diagonal(inverse, axis1=1, axis2=2)
        g2diag[start:stop] = np.einsum("wij,wji->wi", inverse, inverse)

    logabsdet -= np.max(logabsdet)
    weights = np.exp(logabsdet)
    weights /= np.sum(weights)
    if np.min(q) <= 0.0 or np.max(q) >= 1.0:
        raise RuntimeError(f"invalid posterior range at R={radius}, u={u}")

    flip_masks = (np.uint32(1) << shifts)[None, :]
    bbar_phi = np.empty(word_count, dtype=np.float64)
    bbar_phi1 = np.empty(word_count, dtype=np.float64)
    for start in range(0, word_count, batch_size):
        stop = min(word_count, start + batch_size)
        neighbors = ids[start:stop, None] ^ flip_masks
        q_neighbor = q[neighbors]
        base_q = q[start:stop, None]
        bbar_phi[start:stop] = np.sum(
            rbar[start:stop] * breg_phi(q_neighbor, base_q), axis=1
        )
        bbar_phi1[start:stop] = np.sum(
            rbar[start:stop] * breg_phi1(q_neighbor, base_q), axis=1
        )

    expected = np.zeros(4, dtype=np.float64)
    min_total = math.inf
    max_total = -math.inf
    min_word_id = -1
    min_word_components: list[float] | None = None
    for start in range(0, word_count, batch_size):
        stop = min(word_count, start + batch_size)
        neighbors = ids[start:stop, None] ^ flip_masks
        q_neighbor = q[neighbors]
        az_neighbor = az[neighbors]
        base_q = q[start:stop, None]
        delta_q = q_neighbor - base_q
        bphi_edges = breg_phi(q_neighbor, base_q)
        component_curvature = phi2(q[start:stop]) - 8.0
        component_breg_phi1 = bbar_phi1[start:stop]
        component_parameter = np.sum(g2diag[start:stop] * bphi_edges, axis=1)
        component_parameter += np.sum(
            rbar[start:stop]
            * (
                (phi1(q_neighbor) - phi1(q[start:stop])[:, None]) * az_neighbor
                - phi2(q[start:stop])[:, None] * delta_q * az[start:stop, None]
            ),
            axis=1,
        )
        component_transport = np.sum(
            rbar[start:stop]
            * (bbar_phi[neighbors] - bbar_phi[start:stop, None]),
            axis=1,
        )
        components = np.stack(
            [component_curvature, component_breg_phi1, component_parameter, component_transport],
            axis=1,
        )
        expected += weights[start:stop] @ components
        totals = 8.0 + np.sum(components, axis=1)
        local_argmin = int(np.argmin(totals))
        local_min = float(totals[local_argmin])
        if local_min < min_total:
            min_total = local_min
            min_word_id = int(ids[start + local_argmin])
            min_word_components = [float(value) for value in components[local_argmin]]
        max_total = max(max_total, float(np.max(totals)))
    normalized_total = 8.0 + float(np.sum(expected))

    # R=1 has an independent closed formula (SA03_S9_SIGNED_TRANSPORT (8.2)).
    r1_error = None
    if radius == 1:
        t = C * C * u * u / (math.pi * math.pi)
        qp = 0.5 + t
        closed = (
            4.0 * float(phi(np.array(qp)))
            - 4.0 * (1.0 + t) * float(phi1(np.array(qp)))
            + 0.5 * (1.0 + 2.0 * t) ** 2 * (float(phi2(np.array(qp))) + 8.0)
        )
        r1_error = normalized_total - closed
        if abs(r1_error) > 2.0e-10:
            raise RuntimeError(f"R=1 closed-form mismatch: {r1_error}")

    return {
        "u": u,
        "word_count": int(word_count),
        "weight_sum": float(np.sum(weights)),
        "posterior_min": float(np.min(q)),
        "posterior_max": float(np.max(q)),
        "normalized_components": {
            "curvature_minus_8": float(expected[0]),
            "bregman_phi_prime": float(expected[1]),
            "parameter_derivative": float(expected[2]),
            "signed_transport": float(expected[3]),
        },
        "normalized_total": normalized_total,
        "wordwise_min_normalized_total": min_total,
        "wordwise_max_normalized_total": max_total,
        "min_word_little_endian_bits": format(min_word_id, f"0{n}b")[::-1],
        "min_word_normalized_components": {
            "curvature_minus_8": min_word_components[0],
            "bregman_phi_prime": min_word_components[1],
            "parameter_derivative": min_word_components[2],
            "signed_transport": min_word_components[3],
        },
        "r1_closed_form_error": r1_error,
    }


def integrate_radius(radius: int, nodes: int, batch_size: int) -> dict[str, object]:
    lo = 1.0 / (radius + 1.0)
    x, w = np.polynomial.legendre.leggauss(nodes)
    us = lo + 0.5 * (1.0 - lo) * (x + 1.0)
    ws = 0.5 * (1.0 - lo) * w
    rows = [pointwise(radius, float(u), batch_size) for u in us]
    keys = ["curvature_minus_8", "bregman_phi_prime", "parameter_derivative", "signed_transport"]
    integrated = {
        key: float(
            sum(weight * u * row["normalized_components"][key] for weight, u, row in zip(ws, us, rows))
        )
        for key in keys
    }
    baseline = 4.0 * (1.0 - lo * lo)
    total = baseline + sum(integrated.values())
    return {
        "R": radius,
        "N": radius + 1,
        "external_bits": 2 * radius,
        "word_count": 1 << (2 * radius),
        "quadrature_nodes": nodes,
        "u_interval": [lo, 1.0],
        "baseline": baseline,
        "integrated_residual_components": integrated,
        "A_R_second_derivative": total,
        "pointwise_min_normalized_total": min(row["normalized_total"] for row in rows),
        "pointwise_max_normalized_total": max(row["normalized_total"] for row in rows),
        "posterior_min": min(row["posterior_min"] for row in rows),
        "posterior_max": max(row["posterior_max"] for row in rows),
        "quadrature_rows": [
            {
                "u": row["u"],
                "normalized_components": row["normalized_components"],
                "normalized_total": row["normalized_total"],
                "wordwise_min_normalized_total": row["wordwise_min_normalized_total"],
                "min_word_little_endian_bits": row["min_word_little_endian_bits"],
            }
            for row in rows
        ],
        "max_r1_closed_form_error": (
            max(abs(row["r1_closed_form_error"]) for row in rows) if radius == 1 else None
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--radii", nargs="+", type=int, default=[1, 3, 5, 7])
    parser.add_argument("--nodes", type=int, default=32)
    parser.add_argument("--batch-size", type=int, default=8192)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("sa03_exact_finite_result.json"),
    )
    args = parser.parse_args()
    if any(radius < 1 or radius % 2 == 0 for radius in args.radii):
        raise SystemExit("all radii must be positive odd integers")
    results = []
    for radius in args.radii:
        result = integrate_radius(radius, args.nodes, args.batch_size)
        results.append(result)
        print(
            f"R={radius:2d} words={result['word_count']:7d} "
            f"A''={result['A_R_second_derivative']:+.12f} "
            f"transport={result['integrated_residual_components']['signed_transport']:+.12f}",
            flush=True,
        )
    payload = {
        "status": "FINITE_FULL_WORD_DIAGNOSTIC",
        "contrast": C,
        "results": results,
        "limitations": [
            "Finite radii do not determine the sign of Gamma(19/20).",
            "Binary64 linear algebra and Gauss-Legendre quadrature are not interval certificates.",
            "Every reported expectation uses the genuine physical-word DPP law, not spectral Bernoulli words.",
        ],
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
