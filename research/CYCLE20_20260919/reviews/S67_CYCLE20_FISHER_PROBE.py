"""Floating diagnostic for the unproved S67 Cycle20 Fisher input.

Every exterior occupied set of the odd sine-DPP window is enumerated using its
L-ensemble principal determinants.  This is not an interval certificate.
"""
from itertools import combinations
from math import exp
import json
import numpy as np


def logdet_principal(matrix, subset):
    if not subset:
        return 0.0
    sign, value = np.linalg.slogdet(matrix[np.ix_(subset, subset)])
    if sign <= 0:
        raise ArithmeticError("nonpositive principal determinant")
    return float(value)


def logadd(x, y):
    top = max(x, y)
    return top + np.log(np.exp(x - top) + np.exp(y - top))


def local_fisher(m, a):
    c = 19.0 / 20.0
    idx = np.arange(m)
    delta = idx[:, None] - idx[None, :]
    q = np.empty((m, m), dtype=np.float64)
    q[delta == 0] = 0.5
    nz = delta != 0
    q[nz] = np.sin(np.pi * delta[nz] / 2.0) / (np.pi * delta[nz])
    k = a * np.eye(m) + c * q
    ell = np.linalg.solve(np.eye(m) - k, k)
    ell = (ell + ell.T) / 2.0
    _, log_z = np.linalg.slogdet(np.eye(m) + ell)
    center = m // 2
    exterior = tuple(i for i in range(m) if i != center)
    total = 0.0
    for size in range(len(exterior) + 1):
        for chosen in combinations(exterior, size):
            log_a = logdet_principal(ell, chosen)
            log_b = logdet_principal(ell, tuple(sorted(chosen + (center,))))
            total += exp(3 * logadd(log_a, log_b) - log_z - log_a - log_b)
    return total


def main():
    rows = []
    for m in (3, 5, 7, 9, 11, 13, 15, 17, 19):
        for a in (0.02, 0.025, 0.03):
            rows.append({"m": m, "a": a, "d_m": local_fisher(m, a)})
    rows.append({"m": 21, "a": 0.025, "d_m": local_fisher(21, 0.025)})
    print(json.dumps({"status": "FLOATING_DIAGNOSTIC_ONLY", "rows": rows}, indent=2))


if __name__ == "__main__":
    main()

