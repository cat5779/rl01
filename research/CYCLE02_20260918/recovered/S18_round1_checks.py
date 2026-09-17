#!/usr/bin/env python3
"""Diagnostic checks for PRO02 RESULT.md.

These checks support, but do not replace, the analytic proofs in RESULT.md.
They include one exact symbolic identity, exact rational constants, high-precision
finite enumeration, and floating-point stress tests of the reveal inequalities.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
import math

import mpmath as mp
import numpy as np
import sympy as sp


def symbolic_rank_one_identity() -> None:
    s = sp.symbols("s", real=True)
    v0, v1, v2, d0, d1 = sp.symbols(
        "v0 v1 v2 d0 d1", nonzero=True, real=True
    )
    v = v0 + v1 * s + v2 * s**2
    d = d0 + d1 * s  # rank-one direction gives d''=0
    h = v - d
    L = h + d * sp.log(d / v)
    target = sp.diff(v, s, 2) * h / v + d * (
        sp.diff(v, s) / v - sp.diff(d, s) / d
    ) ** 2
    assert sp.simplify(sp.diff(L, s, 2) - target) == 0


def exact_benchmark_constants() -> dict[str, F]:
    delta = F(1, 40)
    c = F(19, 20)
    beta = delta * (delta + c)
    kappa = c * c / (4 * beta)
    gamma_normalized = 3 * kappa - 1
    gamma_weighted = gamma_normalized / (beta * beta)
    new_A = F(9, 16) * gamma_weighted * c * c

    r_delta = (1 - delta) / delta
    old_gamma = kappa * (6 + 8 * r_delta + 3 * r_delta * r_delta)
    old_B = min(3 * c * c / (8 * delta**4), 3 * c * c / (2 * beta**2))
    old_observation_coefficient = old_gamma * old_B / (4 * delta * delta)

    lower_gamma_normalized = c * c / (16 * delta * (1 + c / 2)) - 1
    return {
        "beta": beta,
        "kappa": kappa,
        "gamma_normalized": gamma_normalized,
        "gamma_weighted": gamma_weighted,
        "new_A": new_A,
        "old_observation_coefficient": old_observation_coefficient,
        "lower_gamma_normalized_exact_potential_HS_class": lower_gamma_normalized,
    }


def sine_q_mp(n: int, rho: mp.mpf = mp.mpf("0.5")) -> mp.matrix:
    q = mp.matrix(n)
    for i in range(n):
        for j in range(n):
            r = i - j
            q[i, j] = rho if r == 0 else mp.sin(mp.pi * rho * r) / (mp.pi * r)
    return q


def pair_L(v: mp.mpf, h: mp.mpf) -> mp.mpf:
    if abs(h) < mp.mpf("1e-70"):
        return mp.mpf("0")
    d = v - h
    return h + d * mp.log(d / v)


def phi_sub_mp(g: mp.matrix, core: list[int]) -> mp.mpf:
    ans = mp.mpf("0")
    for i in core:
        ans += g[i, i] ** 2
    for aa, i in enumerate(core):
        for j in core[aa + 1 :]:
            h = abs(g[i, j]) ** 2
            v = g[i, i] * g[j, j]
            ans += 2 * pair_L(v, h)
    return mp.re(ans)


def enumerate_sine(n: int, core: list[int] | None = None) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    mp.mp.dps = 60
    a = mp.mpf(1) / 40
    c = mp.mpf(19) / 20
    q = sine_q_mp(n)
    k = a * mp.eye(n) + c * q
    if core is None:
        core = list(range(n))
    prob_sum = mp.mpf("0")
    hessian = mp.mpf("0")
    negative_phi = mp.mpf("0")
    for bits in product((0, 1), repeat=n):
        mat = mp.matrix(k)
        for i, bit in enumerate(bits):
            mat[i, i] -= 1 - bit
        p = (-1) ** (n - sum(bits)) * mp.det(mat)
        g = mat**-1
        tr_g = sum(g[i, i] for i in range(n))
        tr_g2 = sum(g[i, j] * g[j, i] for i in range(n) for j in range(n))
        p1 = p * tr_g
        p2 = p * (tr_g**2 - tr_g2)
        prob_sum += p
        hessian += -p2 * mp.log(p) - p1**2 / p
        negative_phi += -p * phi_sub_mp(g, core)
    return prob_sum, hessian, negative_phi


def local_window(m: int, radius: int) -> mp.mpf:
    n = m + 2 * radius
    _, _, negative_phi = enumerate_sine(n, list(range(radius, radius + m)))
    return negative_phi / m


def random_positive_contraction(rng: np.random.Generator, n: int) -> np.ndarray:
    a = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    _, u = np.linalg.eigh(a @ a.conj().T)
    vals = 0.02 + 0.96 * rng.random(n)
    return (u * vals) @ u.conj().T


def phi_np(x: np.ndarray) -> float:
    n = x.shape[0]
    ans = float(np.sum(np.real(np.diag(x)) ** 2))
    for i in range(n):
        for j in range(i + 1, n):
            h = abs(x[i, j]) ** 2
            v = float(np.real(x[i, i] * x[j, j]))
            d = v - h
            L = 0.0 if h < 1e-15 else h + d * math.log(d / v)
            ans += 2 * L
    return ans


def reveal_stress_test(trials: int = 500) -> float:
    rng = np.random.default_rng(20260917)
    delta = 1 / 40
    c = 19 / 20
    beta = delta * (delta + c)
    kappa = c * c / (4 * beta)
    gamma = 3 * kappa - 1
    smallest_slack = float("inf")
    for _ in range(trials):
        rmat = random_positive_contraction(rng, 6)
        core = [0, 1, 2]
        k = 3
        signs = rng.choice((-1, 1), size=len(core))
        diag = np.where(signs > 0, 1 - delta, -delta)
        x = np.diag(diag) - c * rmat[np.ix_(core, core)]
        rr = float(np.real(rmat[k, k]))
        p = delta + c * rr
        u = rmat[core, k]
        hmat = c * c * np.outer(u, u.conj())
        xp = x + hmat / p
        xm = x - hmat / (1 - p)
        defect = p * phi_np(xp) + (1 - p) * phi_np(xm) - phi_np(x)
        qv = np.linalg.norm(hmat, "fro") ** 2 / (p * (1 - p))
        smallest_slack = min(smallest_slack, defect + gamma * qv)
    return smallest_slack


def obstruction_diagnostic(eps: float = 0.02) -> tuple[float, float, float]:
    delta = 1 / 40
    c = 19 / 20
    e = delta / c
    lam = 0.5 - 2 * eps * eps
    rmat = np.array(
        [
            [1 - e, math.sqrt(lam * e), eps * math.sqrt(e)],
            [math.sqrt(lam * e), 0.5, 0.0],
            [eps * math.sqrt(e), 0.0, 0.5],
        ]
    )
    min_r = float(np.linalg.eigvalsh(rmat).min())
    min_ir = float(np.linalg.eigvalsh(np.eye(3) - rmat).min())

    core = [0, 1]
    x = np.diag([1 - delta, -delta]) - c * rmat[np.ix_(core, core)]
    p = 0.5
    u = rmat[core, 2]
    hmat = c * c * np.outer(u, u)
    defect = p * phi_np(x + hmat / p) + (1 - p) * phi_np(x - hmat / (1 - p)) - phi_np(x)
    qv = np.linalg.norm(hmat, "fro") ** 2 / (p * (1 - p))
    return min_r, min_ir, defect / qv


def main() -> None:
    symbolic_rank_one_identity()
    print("symbolic_rank_one_identity=true")
    for key, value in exact_benchmark_constants().items():
        print(f"{key}={value} ~= {float(value):.15g}")

    prob_sum, hessian, negative_phi = enumerate_sine(6)
    print(f"n6_probability_sum={mp.nstr(prob_sum, 30)}")
    print(f"n6_Hpp={mp.nstr(hessian, 30)}")
    print(f"n6_minus_E_Phi={mp.nstr(negative_phi, 30)}")
    print(f"n6_identity_error={mp.nstr(hessian-negative_phi, 8)}")
    print(f"W_4_2={mp.nstr(local_window(4, 2), 25)}")
    print(f"random_minimum_Jensen_slack={reveal_stress_test():.12g}")
    min_r, min_ir, ratio = obstruction_diagnostic()
    print(f"obstruction_min_eig_R={min_r:.12g}")
    print(f"obstruction_min_eig_I_minus_R={min_ir:.12g}")
    print(f"obstruction_finite_defect_over_qv={ratio:.12g}")


if __name__ == "__main__":
    main()
