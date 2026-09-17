#!/usr/bin/env python3
"""Finite deterministic regression for the check-2 Fourier tail theorem.

The script exhausts every outside word for n=4,6,8,10 at three a-values.
It checks:
  * the L-ensemble outside law and the exact two-binomial count mixture;
  * the Schur-complement/precision formulas for the bounded t variables;
  * the uniform pointwise size constants used in the proof;
  * several finite Bernstein tail inequalities.

Floating-point regression is not a proof of the growing-n theorem.  The proof is
in RESULT.md.
"""
from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import numpy as np

C = 19.0 / 20.0
KAPPA_STAR = 4753.0 / 3.0
D_STAR = KAPPA_STAR - 1.0
TAU_STAR = (2375.0 / 2378.0) ** 2
V_STAR = 291.0 / 10000.0


def g(t: float) -> float:
    if t <= 0.0:
        return 0.0
    return 2.0 * (-math.log1p(-t) - t)


def rho(t: float) -> float:
    if t <= 0.0:
        return 0.0
    if t < 1.0e-5:
        return 2.0 * sum((m - 2.0) * t**m / m for m in range(3, 40))
    return 2.0 * (t + t / (1.0 - t) + 2.0 * math.log1p(-t))


C_G = g(TAU_STAR) / TAU_STAR
C_RHO = rho(TAU_STAR) / TAU_STAR
C_W = C_RHO * D_STAR
C_E = C_G * C_G * D_STAR * D_STAR / 64.0
C_S = (50.0 / 7.0 + C_G * D_STAR / 4.0) ** 2


def fourier_projection(n: int) -> np.ndarray:
    k = n // 2
    rows = np.arange(n)[:, None]
    cols = np.arange(k)[None, :]
    U = np.exp(2j * np.pi * rows * cols / n) / math.sqrt(n)
    return U @ U.conj().T


def output_L(n: int, a: float) -> np.ndarray:
    P = fourier_projection(n)
    lam0 = a / (1.0 - a)
    lam1 = (a + C) / (1.0 - a - C)
    return lam0 * (np.eye(n) - P) + lam1 * P


def det_pd(A: np.ndarray) -> float:
    if A.size == 0:
        return 1.0
    sign, logdet = np.linalg.slogdet(A)
    if abs(sign.imag) > 1.0e-9 or sign.real <= 0.0:
        raise ArithmeticError(f"nonpositive determinant sign {sign}")
    return float(math.exp(logdet))


def subsets(items: Sequence[int]) -> Iterable[Tuple[int, ...]]:
    for bits in itertools.product((0, 1), repeat=len(items)):
        yield tuple(items[j] for j, bit in enumerate(bits) if bit)


def star_from_L(L: np.ndarray, T_tuple: Tuple[int, ...], i: int):
    n = L.shape[0]
    T = list(T_tuple)
    assert i not in T
    U = [j for j in range(n) if j not in T]

    if T:
        inv_T = np.linalg.inv(L[np.ix_(T, T)])
        Schur = (
            L[np.ix_(U, U)]
            - L[np.ix_(U, T)] @ inv_T @ L[np.ix_(T, U)]
        )
    else:
        Schur = L[np.ix_(U, U)]

    ii = U.index(i)
    ell = float(Schur[ii, ii].real)
    t0: List[float] = []
    for jj, j in enumerate(U):
        if j == i:
            continue
        t = abs(Schur[ii, jj]) ** 2 / (
            Schur[ii, ii].real * Schur[jj, jj].real
        )
        t0.append(float(max(0.0, min(t.real, 1.0 - 1.0e-13))))

    B_idx = T + [i]
    Q = np.linalg.inv(L[np.ix_(B_idx, B_idx)])
    qi = len(B_idx) - 1
    t1: List[float] = []
    for jj, _j in enumerate(T):
        t = abs(Q[qi, jj]) ** 2 / (Q[qi, qi].real * Q[jj, jj].real)
        t1.append(float(max(0.0, min(t.real, 1.0 - 1.0e-13))))

    r = ell / (1.0 + ell)
    s = r * (1.0 - r)
    d = 1.0 - 2.0 * r
    delta = sum(g(t) for t in t1) - sum(g(t) for t in t0)
    W = (1.0 - r) * sum(rho(t) for t in t0) + r * sum(rho(t) for t in t1)
    energy = s * d * d * delta * delta
    square = (1.0 / math.sqrt(s) - 0.25 * d * math.sqrt(s) * delta) ** 2

    return {
        "ell": ell,
        "r": r,
        "t0_sum": sum(t0),
        "t1_sum": sum(t1),
        "t_max": max(t0 + t1 + [0.0]),
        "delta": delta,
        "W": W,
        "energy_over_16": energy / 16.0,
        "square": square,
    }


def binomial_pmf(n: int, p: float) -> List[float]:
    return [
        math.comb(n, j) * p**j * (1.0 - p) ** (n - j)
        for j in range(n + 1)
    ]


def convolution(x: Sequence[float], y: Sequence[float]) -> List[float]:
    out = [0.0] * (len(x) + len(y) - 1)
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            out[i + j] += a * b
    return out


def count_mixture(n: int, a: float) -> List[float]:
    k = n // 2
    p0 = a
    p1 = a + C
    x0 = convolution(binomial_pmf(k, p1), binomial_pmf(k - 1, p0))
    x1 = convolution(binomial_pmf(k - 1, p1), binomial_pmf(k, p0))
    return [(u + v) / 2.0 for u, v in zip(x0, x1)]


def run_case(n: int, a: float) -> Dict[str, float]:
    L = output_L(n, a)
    Z = det_pd(np.eye(n) + L)
    i = 0
    outside = [j for j in range(n) if j != i]
    count_prob = [0.0] * n
    total = 0.0
    maxima = {
        "t_max": 0.0,
        "T0_max": 0.0,
        "T1_max": 0.0,
        "W_max": 0.0,
        "E16_max": 0.0,
        "S_max": 0.0,
    }

    for T in subsets(outside):
        dT = det_pd(L[np.ix_(T, T)]) if T else 1.0
        Ti = T + (i,)
        dTi = det_pd(L[np.ix_(Ti, Ti)])
        nu = (dT + dTi) / Z
        total += nu
        count_prob[len(T)] += nu
        st = star_from_L(L, T, i)
        maxima["t_max"] = max(maxima["t_max"], st["t_max"])
        maxima["T0_max"] = max(maxima["T0_max"], st["t0_sum"])
        maxima["T1_max"] = max(maxima["T1_max"], st["t1_sum"])
        maxima["W_max"] = max(maxima["W_max"], st["W"])
        maxima["E16_max"] = max(maxima["E16_max"], st["energy_over_16"])
        maxima["S_max"] = max(maxima["S_max"], st["square"])

    mix = count_mixture(n, a)
    count_diff = max(abs(x - y) for x, y in zip(count_prob, mix))

    assert abs(total - 1.0) < 2.0e-9
    assert count_diff < 2.0e-9
    assert maxima["t_max"] <= TAU_STAR + 2.0e-9
    assert maxima["T0_max"] <= D_STAR + 2.0e-8
    assert maxima["T1_max"] <= D_STAR + 2.0e-8
    assert maxima["W_max"] <= C_W + 2.0e-6
    assert maxima["E16_max"] <= C_E + 2.0e-5
    assert maxima["S_max"] <= C_S + 2.0e-5

    mu = (n - 1) * (a + C / 2.0)
    tail_checks = []
    for u in (0.25, 0.5, 1.0):
        exact = sum(
            p for m, p in enumerate(count_prob)
            if abs(m - mu) >= C / 2.0 + u
        )
        bern = 2.0 * math.exp(
            -u * u / (2.0 * ((n - 1) * V_STAR + u / 3.0))
        )
        assert exact <= bern + 2.0e-12
        tail_checks.append((u, exact, bern))

    return {
        "n": n,
        "a": a,
        "outside_law_total": total,
        "count_mixture_max_error": count_diff,
        **maxima,
        "tail_checks": tail_checks,
    }


def main() -> None:
    records = []
    for n in (4, 6, 8, 10):
        for a in (1.0 / 50.0, 1.0 / 40.0, 3.0 / 100.0):
            records.append(run_case(n, a))

    result = {
        "scope": "Finite floating-point regression only; RESULT.md is the proof.",
        "constants": {
            "kappa_star": KAPPA_STAR,
            "tau_star": TAU_STAR,
            "C_g": C_G,
            "C_rho": C_RHO,
            "C_W": C_W,
            "C_E": C_E,
            "C_S": C_S,
        },
        "cases": records,
    }
    out = Path(__file__).resolve().parents[1] / "replay" / "fourier_tail_regression.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
