#!/usr/bin/env python3
"""Deterministic non-probative diagnostics for the live TC'' payment.

The exact route obstructions do not depend on this file.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np


def dpp_probs(K: np.ndarray) -> tuple[list[tuple[int, ...]], np.ndarray]:
    n = K.shape[0]
    ys = list(itertools.product((-1, 1), repeat=n))
    p = np.empty(2**n, dtype=float)
    for idx, y in enumerate(ys):
        bits = np.array([1 if v == 1 else 0 for v in y])
        B = K - np.diag(1 - bits)
        sign, logabs = np.linalg.slogdet(B)
        value = ((-1) ** (n - int(bits.sum()))) * sign * math.exp(logabs)
        p[idx] = float(np.real(value))
    if np.min(p) <= 0 or abs(float(p.sum()) - 1.0) > 2e-10:
        raise RuntimeError("invalid numerical atom law")
    return ys, p


def hessian_common(K: np.ndarray) -> float:
    ys, p = dpp_probs(K)
    n = K.shape[0]
    index = {y: k for k, y in enumerate(ys)}
    lis = np.zeros((n, len(ys)))
    for i in range(n):
        for k, y in enumerate(ys):
            yf = list(y)
            yf[i] *= -1
            lis[i, k] = y[i] * (p[k] + p[index[tuple(yf)]])
    H = np.zeros((n, n))
    for i in range(n):
        H[i, i] = -np.sum(lis[i] ** 2 / p)
        for j in range(i):
            lij = np.empty(len(ys))
            for k, y in enumerate(ys):
                yi, yj, yij = list(y), list(y), list(y)
                yi[i] *= -1
                yj[j] *= -1
                yij[i] *= -1
                yij[j] *= -1
                face = p[k] + p[index[tuple(yi)]] + p[index[tuple(yj)]] + p[index[tuple(yij)]]
                lij[k] = y[i] * y[j] * face
            H[i, j] = H[j, i] = -np.dot(lij, np.log(p)) - np.dot(lis[i] * lis[j], 1 / p)
    return float(H.sum())


def tc_second(K: np.ndarray) -> float:
    h2 = hessian_common(K)
    mu = np.real(np.diag(K))
    product_h2 = -float(np.sum(1 / (mu * (1 - mu))))
    return product_h2 - h2


def toeplitz_q(n: int, rho: float) -> np.ndarray:
    Q = np.empty((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            d = i - j
            Q[i, j] = rho if d == 0 else math.sin(math.pi * rho * d) / (math.pi * d)
    return Q


def main() -> dict:
    c = 0.926
    rows = []
    for n in range(2, 9):
        Q = toeplitz_q(n, 0.5)
        for s in (-0.005, 0.0, 0.005):
            K = 0.5 * np.eye(n) + s * np.eye(n) + c * (Q - 0.5 * np.eye(n))
            rows.append({"n": n, "s": s, "tc_second": tc_second(K)})

    rng = np.random.default_rng(20260917)
    random_min = math.inf
    random_arg = None
    for n in range(2, 8):
        for trial in range(40):
            z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
            U, R = np.linalg.qr(z)
            phases = np.diag(R)
            U = U @ np.diag(np.conjugate(phases / np.abs(phases)))
            lam = rng.uniform(0, 1, n)
            Q = U @ np.diag(lam) @ U.conj().T
            for s in (-0.005, 0.0, 0.005):
                K = 0.5 * np.eye(n) + s * np.eye(n) + c * (Q - 0.5 * np.eye(n))
                val = tc_second(K)
                if val < random_min:
                    random_min = val
                    random_arg = [n, trial, s]

    return {
        "schema": 1,
        "warning": "FLOATING DIAGNOSTIC ONLY; not proof evidence",
        "numpy": np.__version__,
        "benchmark_c": c,
        "toeplitz_half_density": rows,
        "seeded_random_contractions": {
            "seed": 20260917,
            "minimum_tc_second": random_min,
            "arg_n_trial_s": random_arg,
            "samples": sum(40 * 3 for _ in range(2, 8)),
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = main()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    else:
        print(text, end="")
