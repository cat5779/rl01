#!/usr/bin/env python3
"""Independent finite enumerator for the S76 midpoint identities.

Dependencies: Python 3 and NumPy.  It constructs the actual 2m-site
consecutive-Fourier parity unitary U=2 Q_EO, its exterior channel
W(z,t)=|det U[z,t]|^2, and enumerates the midpoint law.

This is a floating-point diagnostic, not an infinite-volume proof.
"""
from __future__ import annotations

import argparse
import itertools
import math
from dataclasses import dataclass

import numpy as np


def words(m: int) -> np.ndarray:
    return np.asarray(list(itertools.product((0, 1), repeat=m)), dtype=np.int8)


def cyclic_unitary(m: int) -> np.ndarray:
    """U=2 Q_EO for modes 0,...,m-1 on the 2m-cycle."""
    n = 2 * m
    sites = np.arange(n)
    modes = np.arange(m)
    fourier = np.exp(2j * np.pi * np.outer(sites, modes) / n) / math.sqrt(n)
    q = fourier @ fourier.conj().T
    even = np.arange(0, n, 2)
    odd = np.arange(1, n, 2)
    return 2.0 * q[np.ix_(even, odd)]


def exterior_channel(u: np.ndarray, ws: np.ndarray) -> np.ndarray:
    m = u.shape[0]
    n = 1 << m
    by_weight = [np.flatnonzero(ws.sum(axis=1) == j) for j in range(m + 1)]
    w = np.zeros((n, n), dtype=float)
    for j, ids in enumerate(by_weight):
        for iz in ids:
            rows = np.flatnonzero(ws[iz])
            for it in ids:
                cols = np.flatnonzero(ws[it])
                det = 1.0 if j == 0 else np.linalg.det(u[np.ix_(rows, cols)])
                w[iz, it] = abs(det) ** 2
    return w


def midpoint_input(m: int, c: float, ws: np.ndarray) -> tuple[np.ndarray, float, float]:
    k = c * c
    r = (1.0 - k) / 4.0
    s = (1.0 + k) / 4.0
    n = 1 << m
    p = np.empty((n, n), dtype=float)
    for iy, y in enumerate(ws):
        for iz, z in enumerate(ws):
            d = int(np.count_nonzero(y == z))
            p[iy, iz] = r**d * s ** (m - d)
    return p, r, s


def mutual_information(q: np.ndarray) -> float:
    py = q.sum(axis=1)
    pt = q.sum(axis=0)
    den = py[:, None] * pt[None, :]
    mask = q > 0.0
    return float(np.sum(q[mask] * np.log(q[mask] / den[mask])))


def fair_gain(m: int, k: float, w: np.ndarray, ws: np.ndarray) -> float:
    c = math.sqrt(k)
    p, _, _ = midpoint_input(m, c, ws)
    i_out = mutual_information(p @ w)
    i_one = 0.5 * (1.0 - k) * math.log(1.0 - k) + 0.5 * (1.0 + k) * math.log(1.0 + k)
    return m * i_one - i_out


@dataclass
class Result:
    cx: float
    cd: float
    gpp: float
    hpp: float
    eta_j: float
    cd_fd_residual: float
    unitary_residual: float
    row_residual: float
    col_residual: float


def enumerate_components(m: int, c: float, fd_step: float = 1e-6) -> Result:
    if not (0.0 < c < 1.0):
        raise ValueError("c must lie in (0,1)")
    k = c * c
    ws = words(m)
    u = cyclic_unitary(m)
    w = exterior_channel(u, ws)
    p, r, s = midpoint_input(m, c, ws)
    q = p @ w

    cx = 0.0
    cd = 0.0
    for iy, y in enumerate(ws):
        for iz, z in enumerate(ws):
            d = int(np.count_nonzero(y == z))
            x = int(y.sum() + z.sum() - m)
            for it in range(1 << m):
                mass = p[iy, iz] * w[iz, it]
                if mass == 0.0:
                    continue
                info = math.log(p[iy, iz] / q[iy, it])
                cx += mass * (x * x - d) * info / (r * r)
                cd += mass * (d - 2.0 * m * r) * info / (r * s)

    ell = math.log(s / r)
    eta_j = -cd / (4.0 * m * ell)
    gpp = cx + cd
    hpp = m * (4.0 * ell - 2.0 / r) + gpp

    eps = min(fd_step, 0.1 * (1.0 - k), 0.1 * k)
    dg = (fair_gain(m, k + eps, w, ws) - fair_gain(m, k - eps, w, ws)) / (2.0 * eps)
    cd_fd_residual = cd + 8.0 * dg  # theorem predicts zero

    return Result(
        cx=cx,
        cd=cd,
        gpp=gpp,
        hpp=hpp,
        eta_j=eta_j,
        cd_fd_residual=cd_fd_residual,
        unitary_residual=float(np.max(np.abs(u.conj().T @ u - np.eye(m)))),
        row_residual=float(np.max(np.abs(w.sum(axis=1) - 1.0))),
        col_residual=float(np.max(np.abs(w.sum(axis=0) - 1.0))),
    )


def obstruction(c: float) -> tuple[float, float, float, float]:
    """Exact m=2 count-one atom: Xi/delta = log((r^2+s^2)/(2r^2))."""
    k = c * c
    r = (1.0 - k) / 4.0
    s = (1.0 + k) / 4.0
    alpha = r * r / (r * r + s * s)
    delta = 2.0 * alpha
    var_d = 4.0 * alpha * (1.0 - alpha)
    ratio = math.log((r * r + s * s) / (2.0 * r * r))
    xi = delta * ratio
    return delta, var_d, xi, ratio


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--c", type=float, default=0.95)
    parser.add_argument("--max-m", type=int, default=5)
    args = parser.parse_args()

    print(f"c={args.c:.12g}")
    print("m       C_X               C_D              G''              H_out''          eta_J       CD+8 dG/dk")
    for m in range(2, args.max_m + 1):
        z = enumerate_components(m, args.c)
        print(
            f"{m:1d}  {z.cx: .12f}  {z.cd: .12f}  {z.gpp: .12f}  "
            f"{z.hpp: .12f}  {z.eta_j: .9f}  {z.cd_fd_residual: .3e}"
        )
        print(
            f"   residuals: unitary={z.unitary_residual:.3e}, "
            f"row={z.row_residual:.3e}, col={z.col_residual:.3e}"
        )

    delta, var_d, xi, ratio = obstruction(args.c)
    print("\nActual m=2 count-one pointwise obstruction")
    print(f"delta={delta:.15g}, Var(D|O)={var_d:.15g}")
    print(f"Xi={xi:.15g}, Xi/delta={ratio:.15g}")


if __name__ == "__main__":
    main()
