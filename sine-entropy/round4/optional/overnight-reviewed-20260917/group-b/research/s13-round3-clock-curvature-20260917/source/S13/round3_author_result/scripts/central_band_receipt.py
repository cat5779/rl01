#!/usr/bin/env python3
"""Exact-sum diagnostics at the center and edges of the n^(2/3) count band."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.special import gammaln


def logbinom(n: int, j: np.ndarray) -> np.ndarray:
    return gammaln(n + 1) - gammaln(j + 1) - gammaln(n - j + 1)


def moments(n: int, r: int, z: float) -> dict[str, float]:
    k = n // 2
    js = np.arange(0, r + 1, dtype=float)
    logs = logbinom(k, js) + logbinom(k, r - js) + js * math.log(z)
    top = float(logs.max())
    p = np.exp(logs - top)
    p /= p.sum()
    mean = float(p @ js)
    centered = js - mean
    var = float(p @ centered**2)
    third_abs = float(p @ np.abs(centered) ** 3)
    lam = (2 * mean - r) / r
    theta = lam**2 + (4 * (n - 1) * var - r * (n - r) * (1 - lam**2)) / (n * r * (r - 1))

    js2 = np.arange(0, r - 1, dtype=float)
    logs2 = logbinom(k - 2, js2) + logbinom(k - 2, r - 2 - js2) + js2 * math.log(z)
    top2 = float(logs2.max())
    p2 = np.exp(logs2 - top2)
    p2 /= p2.sum()
    mean2 = float(p2 @ js2)
    dlogtheta = 2 / (z - 1) + (mean2 - mean) / z
    return {
        "r": r,
        "x": r / n,
        "lambda": lam,
        "variance_over_n": var / n,
        "third_abs_over_n_3_2": third_abs / n**1.5,
        "theta": theta,
        "dlogtheta_dz": dlogtheta,
    }


def run(output: Path) -> None:
    c = 19 / 20
    z = ((1 + c) / (1 - c)) ** 2
    z_second = 32 * c / (1 - c) ** 4
    rows = []
    for n in (200, 400, 800, 1600):
        edge = int(n ** (2 / 3))
        offsets = sorted({0, edge // 2, edge})
        for offset in offsets:
            r = n // 2 - offset
            m = moments(n, r, z)
            gamma2 = 2 * (n - 1) / (r * (n - r))
            m["n"] = n
            m["offset"] = offset
            m["minus_tau_second_over_n"] = z_second * m["dlogtheta_dz"] / (n * gamma2)
            rows.append(m)
    data = {
        "classification": "finite exact-sum diagnostics; not proof",
        "c": c,
        "central_limits": {
            "lambda": c,
            "variance_over_n": (1 - c**2) / 16,
            "theta": c**2,
            "minus_tau_second_over_n": 2 / (1 - c**2),
        },
        "rows": rows,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    run(args.output)
