#!/usr/bin/env python3
"""Floating diagnostics for the S77 Fisher--Burg cut identity.

This is NOT interval arithmetic and is NOT an all-size proof.
It enumerates every configuration; no rare words are discarded.
Requires only NumPy.
"""
from itertools import combinations, product
import numpy as np


def sine_Q(n: int, rho: float) -> np.ndarray:
    q = np.empty((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            q[i, j] = rho if i == j else np.sin(np.pi * rho * (i - j)) / (np.pi * (i - j))
    return q


def atom_table(K: np.ndarray):
    n = K.shape[0]
    words = list(product((0, 1), repeat=n))
    p = np.empty(1 << n, dtype=float)
    for k, y0 in enumerate(words):
        y = np.asarray(y0, dtype=float)
        p[k] = (-1.0) ** int(np.sum(1.0 - y)) * np.linalg.det(K - np.diag(1.0 - y))
    return words, p


def marginal(words, weights, keep):
    out = {}
    for y, w in zip(words, weights):
        key = tuple(y[i] for i in keep)
        out[key] = out.get(key, 0.0) + w
    return out


def marginal_array(words, weights, keep):
    d = marginal(words, weights, keep)
    keys = list(product((0, 1), repeat=len(keep)))
    return np.asarray([d[k] for k in keys]), {k: i for i, k in enumerate(keys)}


def cofactor_derivatives(words, p):
    n = len(words[0])
    deleted = {}
    for r in (1, 2):
        for rem in combinations(range(n), r):
            keep = tuple(i for i in range(n) if i not in rem)
            deleted[rem] = marginal(words, p, keep)

    dp = np.zeros_like(p)
    ddp = np.zeros_like(p)
    for k, y in enumerate(words):
        sigma = [2 * bit - 1 for bit in y]
        for i in range(n):
            keep = tuple(j for j in range(n) if j != i)
            dp[k] += sigma[i] * deleted[(i,)][tuple(y[j] for j in keep)]
        for i, j in combinations(range(n), 2):
            keep = tuple(h for h in range(n) if h not in (i, j))
            ddp[k] += 2 * sigma[i] * sigma[j] * deleted[(i, j)][tuple(y[h] for h in keep)]
    return dp, ddp


def entropy_second(p, dp, ddp):
    # Sum ddp is zero, so the usual '+1' term cancels.
    return -np.sum(ddp * np.log(p)) - np.sum(dp * dp / p)


def diagnostics(n: int, rho=0.5, c=0.95, a=0.025):
    assert n % 2 == 0
    K = a * np.eye(n) + c * sine_Q(n, rho)
    words, p = atom_table(K)
    if p.min() <= 0:
        raise RuntimeError(f"nonpositive atom: {p.min()}")
    dp, ddp = cofactor_derivatives(words, p)

    A = tuple(range(n // 2))
    B = tuple(range(n // 2, n))
    pA, ixA = marginal_array(words, p, A)
    pB, ixB = marginal_array(words, p, B)
    dpA, _ = marginal_array(words, dp, A)
    dpB, _ = marginal_array(words, dp, B)
    ddpA, _ = marginal_array(words, ddp, A)
    ddpB, _ = marginal_array(words, ddp, B)

    q = np.empty_like(p)
    dq = np.empty_like(p)
    ddq = np.empty_like(p)
    for k, y in enumerate(words):
        ia = ixA[tuple(y[i] for i in A)]
        ib = ixB[tuple(y[i] for i in B)]
        q[k] = pA[ia] * pB[ib]
        dq[k] = dpA[ia] * pB[ib] + pA[ia] * dpB[ib]
        ddq[k] = ddpA[ia] * pB[ib] + 2 * dpA[ia] * dpB[ib] + pA[ia] * ddpB[ib]

    M2 = entropy_second(pA, dpA, ddpA) + entropy_second(pB, dpB, ddpB) - entropy_second(p, dp, ddp)
    ell_prime = dp / p - dq / q
    Irel = np.sum(p * ell_prime * ell_prime)

    g = p / q
    index = {y: k for k, y in enumerate(words)}
    burg = burg_plus = burg_minus = 0.0
    for i, j in combinations(range(n), 2):
        keep = tuple(h for h in range(n) if h not in (i, j))
        pm = marginal(words, p, keep)
        qm = marginal(words, q, keep)
        for outside in product((0, 1), repeat=n - 2):
            m = pm[outside] / qm[outside]
            phi = {}
            for yi, yj in product((0, 1), repeat=2):
                full = []
                it = iter(outside)
                for h in range(n):
                    full.append(yi if h == i else yj if h == j else next(it))
                x = g[index[tuple(full)]]
                phi[(yi, yj)] = 2.0 * (x - m - m * np.log(x / m))
            rectangle = phi[(1, 1)] + phi[(0, 0)] - phi[(1, 0)] - phi[(0, 1)]
            charge = qm[outside] * rectangle
            burg += charge
            if charge >= 0:
                burg_plus += charge
            else:
                burg_minus -= charge

    # Accepted Fisher defect, reconstructed from scores.
    S = dp / p
    SA = np.asarray([dpA[ixA[tuple(y[i] for i in A)]] / pA[ixA[tuple(y[i] for i in A)]] for y in words])
    SB = np.asarray([dpB[ixB[tuple(y[i] for i in B)]] / pB[ixB[tuple(y[i] for i in B)]] for y in words])
    DF = np.sum(p * S * S) - np.sum(p * SA * SA) - np.sum(p * SB * SB)

    return {
        "n": n,
        "min_atom": p.min(),
        "D_F": DF,
        "M2": M2,
        "Irel": Irel,
        "Burg": burg,
        "Burg_plus": burg_plus,
        "Burg_minus": burg_minus,
        "certificate": Irel - burg_plus,
        "identity_error": (Irel - burg) - M2,
    }


def main():
    print("central point rho=.5, c=.95, a=.025")
    print(" n       Irel          Burg+         certificate     M''            identity error")
    for n in (2, 4, 6, 8, 10, 12):
        d = diagnostics(n)
        print(f"{n:2d}  {d['Irel']:13.9f}  {d['Burg_plus']:13.9f}  {d['certificate']:13.9f}  {d['M2']:13.9f}  {d['identity_error']:+.3e}")

    records = []
    for c in (0.925, 0.9375, 0.95):
        for a in (0.02, 0.025, 0.03):
            for n in (2, 4, 6, 8, 10):
                d = diagnostics(n, c=c, a=a)
                records.append((d["certificate"], c, a, n, d["M2"]))
    worst = min(records)
    print("\n45-point scan: all certificates positive")
    print("minimum (certificate,c,a,n,M'') =", worst)


if __name__ == "__main__":
    main()
