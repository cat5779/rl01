#!/usr/bin/env python3
"""
S79 reproducible computations.

What this script certifies/checks:
  1. An interval-arithmetic certificate that a valid layer-bistochastic channel
     can have positive midpoint entropy curvature.
  2. Direct midpoint calculations for the consecutive-Fourier exterior channel.
  3. The exact shell-curvature decomposition
         H_W'' = H_*'' - Cov(X^2,j)/r^2 - 4(E_W-E_*)/r
     up to floating-point residuals.
  4. The exterior deletion intertwining W_n D_n = D_n W_{n-1}.

No network access and no randomized input are used.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb
import platform
import sys

import mpmath as mp
import numpy as np


def popcounts(m: int) -> np.ndarray:
    return np.array([i.bit_count() for i in range(1 << m)], dtype=int)


def layer_subsets(m: int) -> list[list[int]]:
    layers: list[list[int]] = [[] for _ in range(m + 1)]
    for mask in range(1 << m):
        layers[mask.bit_count()].append(mask)
    return layers


def mask_indices(mask: int, m: int) -> list[int]:
    return [i for i in range(m) if (mask >> i) & 1]


def consecutive_fourier_unitary(m: int) -> np.ndarray:
    """U_m = 2(Q_m)_{EO}, even rows and odd columns."""
    a = np.arange(m)[:, None]
    b = np.arange(m)[None, :]
    ratio = np.exp(1j * np.pi * (2 * (a - b) - 1) / m)
    return 2.0 / (m * (1.0 - ratio))


def exterior_blocks(U: np.ndarray) -> tuple[list[np.ndarray], list[list[int]]]:
    m = U.shape[0]
    layers = layer_subsets(m)
    blocks: list[np.ndarray] = []
    for n, subs in enumerate(layers):
        q = len(subs)
        Wn = np.empty((q, q), dtype=float)
        if n == 0:
            Wn[0, 0] = 1.0
        else:
            inds = [mask_indices(mask, m) for mask in subs]
            for i, rows in enumerate(inds):
                for j, cols in enumerate(inds):
                    Wn[i, j] = abs(np.linalg.det(U[np.ix_(rows, cols)])) ** 2
        blocks.append(Wn)
    return blocks, layers


def full_channel_from_blocks(
    blocks: list[np.ndarray], layers: list[list[int]], m: int
) -> np.ndarray:
    size = 1 << m
    W = np.zeros((size, size), dtype=float)
    for Wn, subs in zip(blocks, layers):
        W[np.ix_(subs, subs)] = Wn
    return W


def shell_channel(m: int, layers: list[list[int]]) -> np.ndarray:
    size = 1 << m
    S = np.zeros((size, size), dtype=float)
    for subs in layers:
        q = len(subs)
        S[np.ix_(subs, subs)] = 1.0 / q
    return S


def deletion_residual(blocks: list[np.ndarray], layers: list[list[int]], m: int) -> float:
    worst = 0.0
    for n in range(1, m + 1):
        upper = layers[n]
        lower = layers[n - 1]
        lower_index = {mask: j for j, mask in enumerate(lower)}
        D = np.zeros((len(upper), len(lower)), dtype=float)
        for i, mask in enumerate(upper):
            for bit in range(m):
                if (mask >> bit) & 1:
                    D[i, lower_index[mask ^ (1 << bit)]] = 1.0 / n
        residual = blocks[n] @ D - D @ blocks[n - 1]
        worst = max(worst, float(np.max(np.abs(residual))))
    return worst


def midpoint_arrays(m: int, c: float) -> dict[str, np.ndarray | float]:
    k = c * c
    r = (1.0 - k) / 4.0
    s = (1.0 + k) / 4.0
    counts = popcounts(m)
    y = np.arange(1 << m)[:, None]
    z = np.arange(1 << m)[None, :]
    D = m - counts[np.bitwise_xor(y, z)]
    X = counts[:, None] + counts[None, :] - m
    P = (r ** D) * (s ** (m - D))
    A = (X * X - D) / (r * r) + (D - 2.0 * m * r) / (r * s)
    P2 = P * A
    return {"k": k, "r": r, "s": s, "counts": counts, "D": D, "X": X, "P": P, "P2": P2}


def number_operator_y(L: np.ndarray, m: int) -> np.ndarray:
    out = np.zeros_like(L)
    for bit in range(m):
        perm = np.arange(1 << m) ^ (1 << bit)
        out += 0.5 * (L - L[perm, :])
    return out


def entropy_curvature_and_shell_data(
    m: int, c: float, W: np.ndarray, S: np.ndarray
) -> dict[str, float]:
    data = midpoint_arrays(m, c)
    r = float(data["r"])
    counts = data["counts"]
    P = data["P"]
    P2 = data["P2"]

    def evaluate(channel: np.ndarray) -> dict[str, object]:
        Q = P @ channel
        Q2 = P2 @ channel
        X = counts[:, None] + counts[None, :] - m
        Q1 = Q * (X / r)
        Hpp = -float(np.sum(Q2 * np.log(Q)) + np.sum((Q1 * Q1) / Q))
        L = (4.0 ** m) * Q
        NL = number_operator_y(L, m)
        edge = float(np.mean(NL * np.log(L)))
        ex2 = float(np.sum(Q * (X * X)))
        elog = float(np.sum(Q * np.log(L)))
        ex2log = float(np.sum(Q * (X * X) * np.log(L)))
        cov_x2_log = ex2log - ex2 * elog
        formula = -cov_x2_log / (r * r) - 4.0 * edge / r - 2.0 * m / r
        return {
            "Q": Q,
            "Hpp": Hpp,
            "L": L,
            "edge": edge,
            "cov_x2_log": cov_x2_log,
            "formula": formula,
        }

    actual = evaluate(W)
    shell = evaluate(S)
    Q = actual["Q"]

    # j(y,n) = D(Q(T|Y=y,N=n) || uniform on the n-shell).
    js = []
    weights = []
    x2s = []
    for ymask in range(1 << m):
        h = int(counts[ymask])
        for n in range(m + 1):
            inds = np.flatnonzero(counts == n)
            mu = float(np.sum(Q[ymask, inds]))
            if mu == 0.0:
                continue
            cond = Q[ymask, inds] / mu
            j = float(np.sum(cond * np.log(cond * len(inds))))
            js.append(j)
            weights.append(mu)
            x2s.append(float((h + n - m) ** 2))
    js = np.asarray(js)
    weights = np.asarray(weights)
    x2s = np.asarray(x2s)
    cov_shell = float(np.sum(weights * x2s * js)
                      - np.sum(weights * x2s) * np.sum(weights * js))

    delta_edge = float(actual["edge"] - shell["edge"])
    Jpp = float(shell["Hpp"] - actual["Hpp"])
    shell_identity_rhs = cov_shell / (r * r) + 4.0 * delta_edge / r

    return {
        "Hpp": float(actual["Hpp"]),
        "Hstarpp": float(shell["Hpp"]),
        "Jpp": Jpp,
        "cov_shell": cov_shell,
        "delta_edge": delta_edge,
        "paid": 4.0 * r * delta_edge,
        "ratio": (-cov_shell / (4.0 * r * delta_edge)) if delta_edge > 1e-14 else float("nan"),
        "curvature_formula_residual": abs(float(actual["Hpp"]) - float(actual["formula"])),
        "shell_identity_residual": abs(Jpp - shell_identity_rhs),
    }


def hybrid_curvature_float(m: int, c: float, identity_layers: set[int]) -> float:
    """Direct finite-sum formula for the identity/mixing hybrid channel."""
    k = c * c
    r = (1.0 - k) / 4.0
    s = (1.0 + k) / 4.0
    ans = 0.0
    for n in range(m + 1):
        if n in identity_layers:
            for h in range(m + 1):
                lo, hi = max(0, h + n - m), min(h, n)
                for b in range(lo, hi + 1):
                    mult = comb(m, h) * comb(h, b) * comb(m - h, n - b)
                    D = m - h - n + 2 * b
                    X = h + n - m
                    p = (r ** D) * (s ** (m - D))
                    A = (X * X - D) / (r * r) + (D - 2 * m * r) / (r * s)
                    ans -= mult * p * (A * np.log(p) + (X / r) ** 2)
        else:
            for h in range(m + 1):
                lo, hi = max(0, h + n - m), min(h, n)
                P = 0.0
                P2 = 0.0
                X = h + n - m
                for b in range(lo, hi + 1):
                    mult_z = comb(h, b) * comb(m - h, n - b)
                    D = m - h - n + 2 * b
                    p = (r ** D) * (s ** (m - D))
                    A = (X * X - D) / (r * r) + (D - 2 * m * r) / (r * s)
                    P += mult_z * p
                    P2 += mult_z * p * A
                ans -= comb(m, h) * (
                    P2 * np.log(P / comb(m, n)) + P * (X / r) ** 2
                )
    return float(ans)



def hybrid_CX_float(m: int, c: float, identity_layers: set[int]) -> float:
    """C_X from its defining expectation; identity layers contribute zero."""
    k = c * c
    r = (1.0 - k) / 4.0
    s = (1.0 + k) / 4.0
    CX = 0.0
    for n in range(m + 1):
        if n in identity_layers:
            continue
        for h in range(m + 1):
            lo, hi = max(0, h + n - m), min(h, n)
            P_hn = 0.0
            atoms = []
            X = h + n - m
            for b in range(lo, hi + 1):
                mult_z = comb(h, b) * comb(m - h, n - b)
                D = m - h - n + 2 * b
                p = (r ** D) * (s ** (m - D))
                P_hn += mult_z * p
                atoms.append((mult_z, D, p))
            q = P_hn / comb(m, n)
            for mult_z, D, p in atoms:
                mult = comb(m, h) * mult_z
                CX += mult * p * (X * X - D) * np.log(p / q) / (r * r)
    return float(CX)


def iv_of_fraction(x: Fraction):
    return mp.iv.mpf(x.numerator) / x.denominator


def hybrid_curvature_interval(
    m: int, identity_layers: set[int], dps: int = 80
):
    """
    Rigorous interval evaluation at c=4/5:
       r=9/100, s=41/100.
    All coefficients are exact rationals; only logarithms use interval arithmetic.
    """
    mp.iv.dps = dps
    r = Fraction(9, 100)
    s = Fraction(41, 100)
    total = mp.iv.mpf([0, 0])

    logr = mp.iv.log(iv_of_fraction(r))
    logs = mp.iv.log(iv_of_fraction(s))

    for n in range(m + 1):
        if n in identity_layers:
            for h in range(m + 1):
                lo, hi = max(0, h + n - m), min(h, n)
                for b in range(lo, hi + 1):
                    mult = comb(m, h) * comb(h, b) * comb(m - h, n - b)
                    D = m - h - n + 2 * b
                    X = h + n - m
                    p = (r ** D) * (s ** (m - D))
                    A = Fraction(X * X - D, 1) / (r * r) + (
                        Fraction(D, 1) - 2 * m * r
                    ) / (r * s)
                    score2 = Fraction(X * X, 1) / (r * r)
                    logp = D * logr + (m - D) * logs
                    total -= mult * iv_of_fraction(p) * (
                        iv_of_fraction(A) * logp + iv_of_fraction(score2)
                    )
        else:
            for h in range(m + 1):
                lo, hi = max(0, h + n - m), min(h, n)
                P = Fraction(0, 1)
                P2 = Fraction(0, 1)
                X = h + n - m
                for b in range(lo, hi + 1):
                    mult_z = comb(h, b) * comb(m - h, n - b)
                    D = m - h - n + 2 * b
                    p = (r ** D) * (s ** (m - D))
                    A = Fraction(X * X - D, 1) / (r * r) + (
                        Fraction(D, 1) - 2 * m * r
                    ) / (r * s)
                    P += mult_z * p
                    P2 += mult_z * p * A
                score2 = Fraction(X * X, 1) / (r * r)
                q = P / comb(m, n)
                total -= comb(m, h) * (
                    iv_of_fraction(P2) * mp.iv.log(iv_of_fraction(q))
                    + iv_of_fraction(P * score2)
                )
    return total


def main() -> None:
    print("S79 computation")
    print("Python:", sys.version.replace("\n", " "))
    print("NumPy:", np.__version__)
    print("mpmath:", mp.__version__)
    print()

    m_ce = 36
    c_ce = 4.0 / 5.0
    band = set(range(16, 21))
    ce_float = hybrid_curvature_float(m_ce, c_ce, band)
    ce_interval = hybrid_curvature_interval(m_ce, band, dps=80)
    print("ARBITRARY LAYER-BISTOCHASTIC COUNTEREXAMPLE")
    print(f"m={m_ce}, c=4/5, identity layers={sorted(band)}, shell-mixed elsewhere")
    print("floating H'' =", repr(ce_float))
    print("interval H'' =", ce_interval)
    print("certified positive =", bool(ce_interval.a > 0))

    # Resolve the shell covariance defect and its Jeffreys payment from the two
    # exact decomposition identities, using floating finite sums.
    Hstar_ce = hybrid_curvature_float(m_ce, c_ce, set())
    CX_ce = hybrid_CX_float(m_ce, c_ce, band)
    CXstar_ce = hybrid_CX_float(m_ce, c_ce, set())
    k_ce = c_ce * c_ce
    r_ce = (1.0 - k_ce) / 4.0
    beta_ce = (1.0 - k_ce * k_ce) / (2.0 * k_ce)
    A_gap = (ce_float - Hstar_ce) * r_ce * r_ce
    B_gap = (CX_ce - CXstar_ce) * r_ce * r_ce
    delta_edge_ce = (A_gap - B_gap) / (beta_ce - 4.0 * r_ce)
    defect_ce = A_gap + 4.0 * r_ce * delta_edge_ce
    print("shell H_*'' =", repr(Hstar_ce))
    print("resolved -Cov(X^2,j) =", repr(defect_ce))
    print("resolved 4r(E_W-E_*) =", repr(4.0 * r_ce * delta_edge_ce))
    print("defect minus payment =", repr(A_gap))
    print()

    c = 0.95
    print("CONSECUTIVE-FOURIER EXTERIOR CHANNEL DIAGNOSTICS AT c=0.95")
    print("m        H_U''             H_*''             J''"
          "              -Cov          4r DeltaE      ratio")
    max_unitarity = 0.0
    max_bistochastic = 0.0
    max_deletion = 0.0
    max_curv_resid = 0.0
    max_shell_resid = 0.0
    for m in range(2, 8):
        U = consecutive_fourier_unitary(m)
        unitary_res = float(np.max(np.abs(U @ U.conj().T - np.eye(m))))
        blocks, layers = exterior_blocks(U)
        W = full_channel_from_blocks(blocks, layers, m)
        S = shell_channel(m, layers)
        bistoch = max(
            float(np.max(np.abs(W.sum(axis=0) - 1.0))),
            float(np.max(np.abs(W.sum(axis=1) - 1.0))),
        )
        deletion = deletion_residual(blocks, layers, m)
        out = entropy_curvature_and_shell_data(m, c, W, S)
        print(
            f"{m:d}  {out['Hpp']: .12f}  {out['Hstarpp']: .12f}"
            f"  {out['Jpp']: .12f}  {-out['cov_shell']: .12f}"
            f"  {out['paid']: .12f}  {out['ratio']: .12f}"
        )
        max_unitarity = max(max_unitarity, unitary_res)
        max_bistochastic = max(max_bistochastic, bistoch)
        max_deletion = max(max_deletion, deletion)
        max_curv_resid = max(max_curv_resid, out["curvature_formula_residual"])
        max_shell_resid = max(max_shell_resid, out["shell_identity_residual"])
    print()
    print("max unitary residual       =", repr(max_unitarity))
    print("max bistochastic residual  =", repr(max_bistochastic))
    print("max deletion residual      =", repr(max_deletion))
    print("max curvature residual     =", repr(max_curv_resid))
    print("max shell identity residual=", repr(max_shell_resid))


if __name__ == "__main__":
    main()
