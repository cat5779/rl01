#!/usr/bin/env python3
"""Numerical/algebraic checks for S52 cycle06.

The proof is in S52_CYCLE06_RESULT.md.  This script checks constants, the local
Bregman identity, the sharp BSC gain-cell cap on random tables, and (optionally)
finite cyclic DPP decompositions for small even n.
"""

from __future__ import annotations

import argparse
import math
from fractions import Fraction
from itertools import product

import numpy as np


def phi(u: float) -> float:
    return -math.log1p(-u) - u


def psi(v: float) -> float:
    return v - math.log1p(v)


def constants(c: float = 19 / 20) -> dict[str, float]:
    c2 = c * c
    b = (1 - c2) / 4
    ph = phi(c2)
    q = c**4
    m2 = Fraction(1, 3)
    m4 = Fraction(71, 315)
    m6 = Fraction(24587, 155925)
    d3 = 4 * (q * float(m2) + q**2 * float(m4) + q**3 * float(m6))
    fstar = (32 * c2 / math.pi**4) / (1 + 2 * c**4 / math.pi**2)
    lower = d3 - ph / (2 * b) + 2 * ph * fstar

    rho = 1 - c2 * math.log(c) / (2 * b)
    dc = (rho - 1 - math.log(rho)) / 2
    mb = 2 * math.exp(-0.5) / (math.sqrt(2 * math.pi) * b)
    threshold = mb * dc - 4
    return {
        "c": c,
        "b": b,
        "phi(c^2)": ph,
        "universal_lower_per_site": -ph / (2 * b),
        "d3": d3,
        "fstar": fstar,
        "cyclic_lower_per_site": lower,
        "M_b D_c": mb * dc,
        "target_threshold": threshold,
        "remaining_gap": threshold - lower,
    }


def local_terms(A: float, B: float, C: float, D: float) -> dict[str, float]:
    """A,B,C,D correspond to 11,10,01,00 and sum to one."""
    total = A + B + C + D
    if abs(total - 1.0) > 1e-12:
        raise ValueError("table must sum to one")
    delta = B * C - A * D
    if delta < -1e-14:
        raise ValueError("table is not negatively associated")
    delta = max(delta, 0.0)
    cost = math.log((B * C) / (A * D))
    observed = delta * (1 / A + 1 / B + 1 / C + 1 / D)
    uB, uC = delta / B, delta / C
    vA, vD = delta / A, delta / D
    bregman = phi(uB) + phi(uC) - psi(vA) - psi(vD)
    return {
        "delta": delta,
        "log_odds_cost": cost,
        "observed_fisher": observed,
        "skew": cost - observed,
        "bregman_skew": bregman,
        "uB": uB,
        "uC": uC,
        "vA": vA,
        "vD": vD,
    }


def bsc_table(table: np.ndarray, c: float) -> np.ndarray:
    eps = (1 - c) / 2
    q = (1 + c) / 2
    T = np.array([[q, eps], [eps, q]], dtype=float)
    return T @ table @ T.T


def random_bsc_cap_check(c: float = 19 / 20, trials: int = 10000) -> None:
    rng = np.random.default_rng(5206)
    for _ in range(trials):
        x = rng.dirichlet(np.ones(4)).reshape(2, 2)
        # Orient as A=11, B=10, C=01, D=00.  Relabeling rows/columns does not
        # affect the determinant calculation used here.
        A, B, C, D = x[0, 0], x[0, 1], x[1, 0], x[1, 1]
        delta_x = B * C - A * D
        if delta_x < 0:
            continue
        y = bsc_table(x, c)
        A2, B2, C2, D2 = y[0, 0], y[0, 1], y[1, 0], y[1, 1]
        delta_y = B2 * C2 - A2 * D2
        assert abs(delta_y - c * c * delta_x) < 2e-12
        assert delta_y / B2 <= c * c + 2e-12
        assert delta_y / C2 <= c * c + 2e-12


def cyclic_projection(n: int) -> np.ndarray:
    if n % 2:
        raise ValueError("n must be even")
    k = n // 2
    s = np.arange(n)[:, None]
    r = np.arange(k)[None, :]
    U = np.exp(2j * np.pi * s * r / n) / math.sqrt(n)
    P = U @ U.conj().T
    return (P + P.conj().T) / 2


def exact_enumeration(n: int, c: float = 19 / 20) -> dict[str, float]:
    if n > 14:
        raise ValueError("exact enumeration is intended for n<=14")
    P = cyclic_projection(n)
    H = 2 * P - np.eye(n)
    K = (np.eye(n) + c * H) / 2
    b = (1 - c * c) / 4
    size = 1 << n
    probs = np.zeros(size)
    invs: list[np.ndarray] = []

    for mask in range(size):
        y = np.array([(mask >> i) & 1 for i in range(n)], dtype=float)
        A = K - np.diag(1 - y)
        sign, logabs = np.linalg.slogdet(A)
        probs[mask] = math.exp(logabs)
        invs.append(np.linalg.inv(A))
    probs /= probs.sum()

    susceptibility_cost = 0.0
    observed = 0.0
    xi = 0.0
    gain = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            bit_i, bit_j = 1 << i, 1 << j
            for base in range(size):
                if base & bit_i or base & bit_j:
                    continue
                p00 = probs[base]
                p10 = probs[base | bit_i]
                p01 = probs[base | bit_j]
                p11 = probs[base | bit_i | bit_j]
                m = p00 + p10 + p01 + p11
                delta = p10 * p01 - p11 * p00
                if delta < 0 and delta > -1e-13:
                    delta = 0.0
                assert delta >= -1e-12
                cost = m * math.log((p10 * p01) / (p11 * p00))
                obs = delta * (1 / p00 + 1 / p10 + 1 / p01 + 1 / p11)
                susceptibility_cost += 2 * cost
                observed += 2 * obs
                xi += 2 * (cost - obs)
                gain += 2 * delta * (1 / p10 + 1 / p01)

    D = 0.0
    Vstat = 0.0
    for i in range(n):
        bit = 1 << i
        for base in range(size):
            if base & bit:
                continue
            p0, p1 = probs[base], probs[base | bit]
            m = p0 + p1
            r = p1 / m
            D += m / (r * (1 - r))
            Vstat += m * (2 * r - 1) ** 2

    FH = 0.0
    Fa_obs = 0.0
    O_matrix = 0.0
    G_matrix = 0.0
    for mask, (p, Bmat) in enumerate(zip(probs, invs)):
        score_h = 0.5 * np.trace(Bmat @ H).real
        FH += p * score_h**2
        Fa_obs += p * np.trace(Bmat @ Bmat).real
        y = np.array([(mask >> i) & 1 for i in range(n)], dtype=int)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                z = abs(Bmat[i, j]) ** 2
                O_matrix += p * z
                if y[i] != y[j]:
                    G_matrix += p * z

    compensation = n * c * c / b
    R = compensation - susceptibility_cost
    alpha = phi(c * c) / (c * c)
    theorem_rhs = 4 * (D / 4 - n) - n * phi(c * c) / (2 * b) + 2 * phi(c * c) * FH

    checks = {
        "probability_sum": probs.sum(),
        "R": R,
        "susceptibility_cost": susceptibility_cost,
        "observed_square": observed,
        "observed_matrix": O_matrix,
        "Xi": xi,
        "D": D,
        "V": Vstat,
        "Fa_observed": Fa_obs,
        "n_over_b": n / b,
        "gain_square": gain,
        "gain_matrix": G_matrix,
        "FH": FH,
        "gain_identity_rhs": 0.5 * (n / b - 4 * n - 4 * c * c * FH),
        "R_identity_rhs": D - 4 * n - xi,
        "theorem_rhs": theorem_rhs,
        "Xi_minus_alphaG": xi - alpha * gain,
    }
    tol = 2e-7
    assert abs(observed - O_matrix) < tol
    assert abs(Fa_obs - n / b) < tol
    assert abs(gain - G_matrix) < tol
    assert abs(gain - checks["gain_identity_rhs"]) < tol
    assert abs(R - checks["R_identity_rhs"]) < tol
    assert R + tol >= theorem_rhs
    assert checks["Xi_minus_alphaG"] <= tol
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--enumerate", type=int, default=0,
                        help="exactly enumerate an even cyclic block, n<=14")
    args = parser.parse_args()

    for key, value in constants().items():
        print(f"{key:30s} {value:.12g}")

    example = local_terms(0.089, 0.811, 0.011, 0.089)
    print("\nPointwise endpoint-Fisher ansatz counterexample:")
    for key, value in example.items():
        print(f"{key:30s} {value:.12g}")
    assert example["skew"] > 0
    assert abs(example["skew"] - example["bregman_skew"]) < 1e-12

    random_bsc_cap_check()
    print("\nRandom BSC gain-cell cap checks passed.")

    if args.enumerate:
        print(f"\nExact cyclic enumeration n={args.enumerate}:")
        out = exact_enumeration(args.enumerate)
        for key, value in out.items():
            print(f"{key:30s} {value:.12g}")


if __name__ == "__main__":
    main()
