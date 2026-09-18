#!/usr/bin/env python3
"""S44 diagnostic checks for the projection-completed finite jet.

The script uses finite cyclic half-rank Fourier projections.  It checks algebraic
identities that are dimension-independent; it is not a proof and it does not
attempt to certify Gamma(19/20).
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Iterable

import numpy as np


@dataclass
class CheckSummary:
    max_projection_error: float = 0.0
    max_v_error: float = 0.0
    max_g_error: float = 0.0
    max_full_closure_error: float = 0.0
    max_completion_error: float = 0.0
    max_schur_ratio: float = 0.0
    min_hidden_tail: float = math.inf


def half_fourier_projection(n: int) -> tuple[np.ndarray, np.ndarray]:
    """Return U,Q for a cyclic rank-n/2 Fourier projection."""
    if n < 4 or n % 2:
        raise ValueError("n must be even and at least 4")
    rank = n // 2
    sites = np.arange(n)[:, None]
    freqs = np.arange(rank)[None, :]
    U = np.exp(2j * np.pi * sites * freqs / n) / math.sqrt(n)
    Q = U @ U.conj().T
    return U, Q



def sine_projection(indices: list[int]) -> np.ndarray:
    """Exact principal matrix of the half-density sine projection."""
    idx = np.asarray(indices, dtype=int)
    diff = idx[:, None] - idx[None, :]
    Q = np.empty(diff.shape, dtype=float)
    Q[diff == 0] = 0.5
    mask = diff != 0
    Q[mask] = np.sin(0.5 * np.pi * diff[mask]) / (np.pi * diff[mask])
    return Q


def sine_window_certificate(
    radius: int, bits: Iterable[int], x: float, theta: float
) -> dict[str, float]:
    """Evaluate the S44 finite object on one exact sine-window word.

    `bits` is ordered as [-R,...,-1,1,...,R].  The returned `completed_jet`
    is psi_x,theta(r_R); `finite_optimizer_jet` is the derivative of the
    optimizer for the finite output marginal.  Their difference is the
    nonnegative hidden covariance completion from equation (8.4).
    """
    if radius < 1:
        raise ValueError("radius must be positive")
    if not (0.0 < x < 1.0):
        raise ValueError("x must lie in (0,1)")
    if not (-2.0 <= theta <= 2.0):
        raise ValueError("theta must lie in [-2,2]")
    sites = list(range(-radius, 0)) + list(range(1, radius + 1))
    z = np.asarray(list(bits), dtype=int)
    if z.shape != (2 * radius,) or np.any((z != 0) & (z != 1)):
        raise ValueError("bits must contain exactly 2*radius zeros/ones")
    sigma = 2.0 * z - 1.0

    all_sites = [0] + sites
    Q = sine_projection(all_sites)
    Qcc = Q[1:, 1:]
    b = x * Q[1:, 0]
    B = x * Qcc.copy()
    B[np.diag_indices_from(B)] += (sigma - x) / 2.0
    G = np.linalg.inv(B)
    v = G @ b
    r = float(np.real(np.vdot(b, v)))
    q = 0.5 - r

    det_b = float(np.real(np.linalg.det(B)))
    zeros = int(np.count_nonzero(z == 0))
    atom_weight = ((-1.0) ** zeros) * det_b

    finite_jet = 4.0 * (np.vdot(v, v).real + 4.0 * r * r) / (1.0 + theta * r) ** 2
    completed_jet = psi(x, theta, r)
    p_hidden = 0.5 - r / x
    hidden_tail = p_hidden * (1.0 - p_hidden) - (1.0 - x * x) / (4.0 * x * x) * np.vdot(v, v).real
    completion = 16.0 * x * x / (1.0 - x * x) * hidden_tail / (1.0 + theta * r) ** 2

    return {
        "atom_weight": atom_weight,
        "q_R": q,
        "r_R": r,
        "finite_optimizer_jet": float(finite_jet),
        "hidden_covariance_tail": float(hidden_tail),
        "completion": float(completion),
        "completed_jet": float(completed_jet),
    }

def posterior_projection(
    U: np.ndarray,
    observed: Iterable[int],
    sigma: np.ndarray,
    x: float,
) -> np.ndarray:
    """Hidden posterior projection after BSC observations on `observed`."""
    n = U.shape[0]
    d = np.ones(n, dtype=float)
    for i in observed:
        d[i] = math.sqrt((1.0 + sigma[i] * x) / (1.0 - sigma[i] * x))
    DU = d[:, None] * U
    middle = U.conj().T @ ((d * d)[:, None] * U)
    return DU @ np.linalg.solve(middle, DU.conj().T)


def output_data(
    Q: np.ndarray,
    center: int,
    observed: list[int],
    sigma: np.ndarray,
    x: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, float, float]:
    """Return B,G,v,r,q for the exact output principal marginal."""
    idx = np.asarray(observed, dtype=int)
    B = x * Q[np.ix_(idx, idx)].copy()
    # B = diag((sigma_i-x)/2) + x Q_I, so its final diagonal is sigma_i/2.
    B[np.diag_indices_from(B)] += (sigma[idx] - x) / 2.0
    b = x * Q[idx, center]
    G = np.linalg.inv(B)
    v = G @ b
    r = float(np.real(np.vdot(b, v)))
    q = 0.5 - r
    return B, G, v, r, q


def psi(x: float, theta: float, r: float) -> float:
    return 4.0 * x * x * (1.0 - 4.0 * r * r) / (
        (1.0 - x * x) * (1.0 + theta * r) ** 2
    )


def vq_exact(L: int) -> float:
    if L < 1:
        raise ValueError("L must be positive")
    first = sum(1.0 / n for n in range(1, L + 1, 2))
    # A safe numerical tail truncation plus an integral bound for display.
    cutoff = max(100000, 100 * L)
    first_odd_after_L = L + 1 + (1 - ((L + 1) % 2))
    tail_partial = sum(1.0 / (n * n) for n in range(first_odd_after_L, cutoff, 2))
    tail_bound = 1.0 / max(cutoff - 2, 1)
    return 2.0 / math.pi**2 * (first + L * (tail_partial + tail_bound))


def run_checks(n: int, radius: int, x: float, trials: int, seed: int) -> CheckSummary:
    if not (0.0 < x < 1.0):
        raise ValueError("x must lie in (0,1)")
    if radius < 1 or 2 * radius + 1 >= n:
        raise ValueError("need 1 <= radius and 2*radius+1 < n")

    rng = np.random.default_rng(seed)
    U, Q = half_fourier_projection(n)
    center = 0
    full_ext = list(range(1, n))
    local = sorted({k % n for k in range(-radius, radius + 1) if k % n != center})
    local_set = set(local)
    outside = [i for i in full_ext if i not in local_set]

    result = CheckSummary()
    D_x = 1.0 + x * x / (1.0 - x) ** 2

    for _ in range(trials):
        sigma = rng.choice(np.array([-1.0, 1.0]), size=n)

        # Full exterior identities.
        _, G_full, v_full, r_full, _ = output_data(Q, center, full_ext, sigma, x)
        Pi_full = posterior_projection(U, full_ext, sigma, x)
        result.max_projection_error = max(
            result.max_projection_error,
            float(np.linalg.norm(Pi_full @ Pi_full - Pi_full, ord=2)),
        )

        for pos, i in enumerate(full_ext):
            rhs = 2.0 * x * sigma[i] / math.sqrt(1.0 - x * x) * Pi_full[i, center]
            result.max_v_error = max(result.max_v_error, abs(v_full[pos] - rhs))

        # Off-diagonal resolvent dictionary.
        for a in range(min(4, len(full_ext))):
            for b in range(min(4, len(full_ext))):
                if a == b:
                    continue
                i, j = full_ext[a], full_ext[b]
                rhs = -4.0 * x * sigma[i] * sigma[j] / (1.0 - x * x) * Pi_full[i, j]
                result.max_g_error = max(result.max_g_error, abs(G_full[a, b] - rhs))

        full_numerator = np.vdot(v_full, v_full).real + 4.0 * r_full * r_full
        closed_numerator = x * x * (1.0 - 4.0 * r_full * r_full) / (1.0 - x * x)
        result.max_full_closure_error = max(
            result.max_full_closure_error,
            abs(full_numerator - closed_numerator),
        )

        # Finite observation and exact hidden-tail completion.
        _, G_R, v_R, r_R, _ = output_data(Q, center, local, sigma, x)
        Pi_R = posterior_projection(U, local, sigma, x)
        p_R = float(np.real(Pi_R[center, center]))
        hidden_tail = p_R * (1.0 - p_R) - (1.0 - x * x) / (4.0 * x * x) * np.vdot(v_R, v_R).real
        result.min_hidden_tail = min(result.min_hidden_tail, hidden_tail)

        theta = float(rng.uniform(-2.0, 2.0))
        finite_jet = 4.0 * (np.vdot(v_R, v_R).real + 4.0 * r_R * r_R) / (1.0 + theta * r_R) ** 2
        completion = 16.0 * x * x / (1.0 - x * x) * hidden_tail / (1.0 + theta * r_R) ** 2
        result.max_completion_error = max(
            result.max_completion_error,
            abs(psi(x, theta, r_R) - finite_jet - completion),
        )

        # Deterministic Schur-domain inequality using the same full word.
        local_positions = [full_ext.index(i) for i in local]
        outside_positions = [full_ext.index(i) for i in outside]
        v_embed = np.zeros_like(v_full)
        v_embed[local_positions] = v_R
        lhs = float(np.vdot(v_full - v_embed, v_full - v_embed).real)
        tau = float(np.vdot(v_full[outside_positions], v_full[outside_positions]).real)
        if tau > 1e-15:
            result.max_schur_ratio = max(result.max_schur_ratio, lhs / (D_x * tau))
        elif lhs > 1e-12:
            raise AssertionError("zero tail but nonzero Schur error")

    return result


def constants(x: float, R: int) -> dict[str, float]:
    L = R + 1
    D_x = 1.0 + x * x / (1.0 - x) ** 2
    vq_bound = (math.log(L) + 4.0) / math.pi**2
    eta_coeff = x**4 * D_x / (1.0 - x * x) ** 2
    jet_coeff = 128.0 * x**8 * D_x / ((1.0 - x) ** 8 * (1.0 + x) ** 4)
    return {
        "D_x": D_x,
        "V_Q_upper": vq_bound,
        "eta_upper": eta_coeff * vq_bound / L,
        "jet_loss_upper": jet_coeff * vq_bound / L,
        "L_psi": 16.0 * x * x / ((1.0 - x) ** 3 * (1.0 + x)),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=16)
    parser.add_argument("--radius", type=int, default=3)
    parser.add_argument("--x", type=float, default=0.7)
    parser.add_argument("--trials", type=int, default=100)
    parser.add_argument("--seed", type=int, default=44)
    parser.add_argument("--bound-radius", type=int, default=1000)
    parser.add_argument("--show-sine-demo", action="store_true")
    args = parser.parse_args()

    summary = run_checks(args.n, args.radius, args.x, args.trials, args.seed)
    print("S44 finite projection diagnostics")
    print(f"  max ||Pi^2-Pi||              = {summary.max_projection_error:.3e}")
    print(f"  max response identity error  = {summary.max_v_error:.3e}")
    print(f"  max G offdiag identity error = {summary.max_g_error:.3e}")
    print(f"  max full closure error        = {summary.max_full_closure_error:.3e}")
    print(f"  max completion error          = {summary.max_completion_error:.3e}")
    print(f"  max Schur ratio (must <= 1)   = {summary.max_schur_ratio:.12f}")
    print(f"  min hidden tail (must >= 0)   = {summary.min_hidden_tail:.3e}")

    print("\nDisplayed analytic constants")
    for key, value in constants(args.x, args.bound_radius).items():
        print(f"  {key:20s} = {value:.12g}")

    L = args.bound_radius + 1
    approx_vq = vq_exact(L)
    simple_vq = (math.log(L) + 4.0) / math.pi**2
    print(f"  V_Q({L}) numerical upper approximation = {approx_vq:.12g}")
    print(f"  (log L + 4)/pi^2             = {simple_vq:.12g}")
    if approx_vq > simple_vq + 1e-8:
        raise AssertionError("number-variance diagnostic exceeded the stated bound")

    tol = 5e-10

    if args.show_sine_demo:
        demo_bits = [0, 1] * args.radius
        demo = sine_window_certificate(args.radius, demo_bits, args.x, theta=0.0)
        print("\nExact sine-window witness demo (theta=0)")
        for key, value in demo.items():
            print(f"  {key:24s} = {value:.12g}")
        if demo["hidden_covariance_tail"] < -tol:
            raise AssertionError("sine-window hidden tail became negative")
        if abs(demo["completed_jet"] - demo["finite_optimizer_jet"] - demo["completion"]) > tol:
            raise AssertionError("sine-window completion identity failed")

    if summary.max_projection_error > tol:
        raise AssertionError("posterior projection check failed")
    if summary.max_v_error > tol:
        raise AssertionError("response identity check failed")
    if summary.max_g_error > tol:
        raise AssertionError("resolvent dictionary check failed")
    if summary.max_full_closure_error > tol:
        raise AssertionError("full scalar closure check failed")
    if summary.max_completion_error > tol:
        raise AssertionError("finite completion check failed")
    if summary.max_schur_ratio > 1.0 + 1e-9:
        raise AssertionError("Schur inequality check failed")
    if summary.min_hidden_tail < -tol:
        raise AssertionError("hidden covariance tail became negative")


if __name__ == "__main__":
    main()
