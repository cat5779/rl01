#!/usr/bin/env python3
"""Diagnostics for S54 cycle07.

These checks are not proof certificates.  They verify explicit algebraic and
finite-dimensional identities used in S54_CYCLE07_RESULT.md.

Dependencies: mpmath, numpy, scipy; sympy is optional for the exact factor check.
"""
from __future__ import annotations

import argparse
import itertools
import math
from math import comb

import mpmath as mp
import numpy as np


def constants(c: mp.mpf) -> dict[str, mp.mpf]:
    b = (1 - c * c) / 4
    rho = 1 - c * c * mp.log(c) / (2 * b)
    D = (rho - 1 - mp.log(rho)) / 2
    M = 2 * mp.e ** (-mp.mpf("0.5")) / (mp.sqrt(2 * mp.pi) * b)
    tau = (1 - c * c) * (5 * c * c + 3) / ((1 + c * c) * (c * c + 3))
    a = (rho - 1) / (2 * rho)
    d = 1 - 2 * a * tau
    Delta = (rho * d) ** (-mp.mpf("0.5")) * (
        a * tau / d + mp.log(d) / 2
    )
    return {
        "c": c,
        "b": b,
        "rho": rho,
        "D": D,
        "M": M,
        "tau_post": tau,
        "a": a,
        "d": d,
        "Delta": Delta,
        "old_beta": M * D,
        "improvement": M * Delta,
        "new_beta": M * (D - Delta),
    }


def pair_functions(c: float, u: np.ndarray | float):
    chi = 2 * c / (1 + c * c)
    m = ((1 - c) ** 2 / (1 + c * c)) * (1 + chi * u) / (1 - chi * chi * u)
    t = (1 - u) / 2
    v = ((1 - c * c) ** 2 / (2 * (1 + c * c) ** 2)) * (
        (1 - u) * (1 + chi * chi * u) / (1 - chi * chi * u) ** 2
    )
    A = ((1 - c * c) ** 2 * (11 * c * c + 9)) / (
        4 * c * (1 + c * c) * (c * c + 3)
    )
    B = 18 * (1 - c * c) ** 2 / (c * c + 3) ** 2
    rhs = (
        4
        * c**4
        * (1 - c * c) ** 2
        * (1 - u)
        * (6 * u - 1 - c * c) ** 2
        / ((c * c + 3) ** 2 * ((1 + c * c) ** 2 - 4 * c * c * u) ** 2)
    )
    lhs = v - A * (1 - m) + B * t
    return m, t, v, A, B, lhs, rhs


def exact_symbolic_factor_check() -> None:
    try:
        import sympy as sp
    except ImportError:
        print("sympy unavailable: skipping exact symbolic factor check")
        return

    c, u = sp.symbols("c u", positive=True)
    chi = 2 * c / (1 + c**2)
    m = (1 - c) ** 2 / (1 + c**2) * (1 + chi * u) / (1 - chi**2 * u)
    t = (1 - u) / 2
    v = (1 - c**2) ** 2 / (2 * (1 + c**2) ** 2) * (
        (1 - u) * (1 + chi**2 * u) / (1 - chi**2 * u) ** 2
    )
    A = (1 - c**2) ** 2 * (11 * c**2 + 9) / (
        4 * c * (1 + c**2) * (c**2 + 3)
    )
    B = 18 * (1 - c**2) ** 2 / (c**2 + 3) ** 2
    target = (
        4
        * c**4
        * (1 - c**2) ** 2
        * (1 - u)
        * (6 * u - 1 - c**2) ** 2
        / ((c**2 + 3) ** 2 * ((1 + c**2) ** 2 - 4 * c**2 * u) ** 2)
    )
    residual = sp.factor(sp.together(v - A * (1 - m) + B * t - target))
    assert residual == 0
    print("exact symbolic PPVC factorization: PASS")


def fourier_projection(n: int) -> np.ndarray:
    k = n // 2
    sites = np.arange(n)
    freqs = np.arange(k)
    U = np.exp(2j * np.pi * np.outer(sites, freqs) / n) / np.sqrt(n)
    P = U @ U.conj().T
    return (P + P.conj().T) / 2


def theta_exact(n: int, c: float, l: int) -> float:
    k = n // 2
    z = ((1 + c) / (1 - c)) ** 2
    lo = max(0, l - k)
    hi = min(k, l)
    Z = sum(comb(k, j) * comb(k, l - j) * z ** (l - j) for j in range(lo, hi + 1))
    m = l - 2
    C = 0.0
    if m >= 0:
        lo2 = max(0, m - (k - 2))
        hi2 = min(k - 2, m)
        C = sum(
            comb(k - 2, j) * comb(k - 2, m - j) * z ** (m - j)
            for j in range(lo2, hi2 + 1)
        )
    alpha = l * (l - 1) / (k * (k - 1))
    return (z - 1) ** 2 * C / (alpha * Z)


def expected_T_formula(n: int, c: float, l: int) -> float:
    k = n // 2
    theta = theta_exact(n, c, l)
    alpha = l * (l - 1) / (k * (k - 1))
    E_uniform = l * (n - l) / (4 * (n - 1))
    E_qmax = l / 4 - alpha * (n / 24 - 1 / (6 * n))
    return (1 - theta) * E_uniform + theta * E_qmax


def finite_slice_check(n: int, c: float) -> dict[str, float]:
    l = n // 2
    P = fourier_projection(n)
    z = ((1 + c) / (1 - c)) ** 2
    Lambda = np.eye(n) + (z - 1) * P
    A = ((1 - c * c) ** 2 * (11 * c * c + 9)) / (
        4 * c * (1 + c * c) * (c * c + 3)
    )
    B = 18 * (1 - c * c) ** 2 / (c * c + 3) ** 2

    subsets = list(itertools.combinations(range(n), l))
    log_weights: list[float] = []
    rows: list[tuple[float, float, float, float]] = []
    all_sites = set(range(n))

    for subset in subsets:
        S = np.array(subset, dtype=int)
        sign, logdet = np.linalg.slogdet(Lambda[np.ix_(S, S)])
        if sign.real <= 0:
            raise AssertionError("nonpositive principal minor")
        log_weights.append(float(logdet.real))

        PS = P[np.ix_(S, S)]
        eigs = np.clip(np.linalg.eigvalsh(PS).real, 0.0, 1.0)
        r = (1 - eigs) / (1 + (z - 1) * eigs)
        M = float(r.sum())
        V = float((r * (1 - r)).sum())

        Cset = np.array(sorted(all_sites.difference(subset)), dtype=int)
        T = float(np.sum(np.abs(P[np.ix_(S, Cset)]) ** 2).real)
        certificate = A * (l / 2 - M) - B * T
        rows.append((T, M, V, V - certificate))

    logs = np.array(log_weights)
    weights = np.exp(logs - logs.max())
    weights /= weights.sum()
    arr = np.array(rows)

    expected_T = float(weights @ arr[:, 0])
    formula_T = expected_T_formula(n, c, l)
    min_slack = float(arr[:, 3].min())

    if abs(expected_T - formula_T) > 5e-10:
        raise AssertionError((expected_T, formula_T))
    if min_slack < -5e-10:
        raise AssertionError(min_slack)

    return {
        "n": float(n),
        "states": float(len(subsets)),
        "E_gamma_T": expected_T,
        "T_formula": formula_T,
        "E_gamma_M": float(weights @ arr[:, 1]),
        "E_gamma_V": float(weights @ arr[:, 2]),
        "min_PPVC_slack": min_slack,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=12, help="largest even n for finite enumeration")
    parser.add_argument("--skip-finite", action="store_true")
    args = parser.parse_args()

    mp.mp.dps = 80
    c_mp = mp.mpf(19) / 20
    vals = constants(c_mp)
    print("high-precision constants for c=19/20")
    for key, value in vals.items():
        print(f"  {key:12s} = {mp.nstr(value, 60)}")

    assert vals["Delta"] > 0
    assert vals["new_beta"] < vals["old_beta"]

    exact_symbolic_factor_check()

    grid = np.linspace(0.0, 1.0, 20001)
    *_, lhs, rhs = pair_functions(0.95, grid)
    max_residual = float(np.max(np.abs(lhs - rhs)))
    min_lhs = float(np.min(lhs))
    assert max_residual < 2e-11
    assert min_lhs > -2e-12
    print(f"numeric PPVC grid: PASS (max residual {max_residual:.3e}, min lhs {min_lhs:.3e})")

    if not args.skip_finite:
        for n in range(4, args.max_n + 1, 2):
            stats = finite_slice_check(n, 0.95)
            print(stats)

    print("All requested diagnostics passed. These checks are not independent certification.")


if __name__ == "__main__":
    main()
