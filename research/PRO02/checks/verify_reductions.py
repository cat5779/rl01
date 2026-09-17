"""Independent numerical stress checks for proved_reductions.md.

These tests are diagnostics supporting algebraic proofs; they are not the
proof of the general inequalities.
"""

from __future__ import annotations

import itertools
import math

import numpy as np


A = 1.0 / 40.0
C = 19.0 / 20.0
BETA = A * (A + C)
KAPPA = C * C / (1.0 - C * C)
ELL = ((1.0 + KAPPA) * math.log1p(KAPPA) - KAPPA) / KAPPA
CPAIR = C * C * ELL / (BETA * BETA)


def sine_kernel(n: int) -> np.ndarray:
    q = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            r = i - j
            q[i, j] = 0.5 if r == 0 else math.sin(math.pi * r / 2) / (math.pi * r)
    return q


def psi(v: float, h: float) -> float:
    return 0.0 if h == 0 else h + (v - h) * math.log1p(-h / v)


def number_variance(m: int) -> float:
    q = sine_kernel(m)
    return float(np.trace(q - q @ q))


def posterior_from_g(g: np.ndarray, bits: tuple[int, ...]) -> np.ndarray:
    n = len(bits)
    r = np.empty((n, n))
    for i in range(n):
        sigma_i = 2 * bits[i] - 1
        alpha_i = A if bits[i] else 1 - A
        r[i, i] = (BETA / C) * (1 / (sigma_i * alpha_i) - g[i, i])
        for j in range(i):
            sigma_j = 2 * bits[j] - 1
            r[i, j] = r[j, i] = -(BETA / C) * sigma_i * sigma_j * g[i, j]
    return r


def check_pair_cut(n: int, m: int) -> tuple[float, float, float]:
    q = sine_kernel(n)
    k = A * np.eye(n) + C * q
    blocks = [list(range(s, min(s + m, n))) for s in range(0, n, m)]
    label = {i: b for b, block in enumerate(blocks) for i in block}
    expected_positive_cut = 0.0
    expected_ordered_energy = 0.0
    mass = 0.0
    for bits in itertools.product((0, 1), repeat=n):
        mat = k - np.diag([1 - b for b in bits])
        sign, logdet = np.linalg.slogdet(mat)
        p = ((-1.0) ** (n - sum(bits))) * sign * math.exp(logdet)
        g = np.linalg.inv(mat)
        r = posterior_from_g(g, bits)
        cut = 0.0
        energy = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if label[i] == label[j]:
                    continue
                h = g[i, j] ** 2
                v = g[i, i] * g[j, j]
                cut += max(-2.0 * psi(v, h), 0.0)
                energy += 2.0 * r[i, j] ** 2
        mass += p
        expected_positive_cut += p * cut
        expected_ordered_energy += p * energy
    variance_budget = sum(number_variance(len(block)) for block in blocks)
    assert abs(mass - 1) < 2e-12
    assert expected_positive_cut <= CPAIR * expected_ordered_energy + 2e-10
    assert expected_ordered_energy <= variance_budget + 2e-10
    return expected_positive_cut, CPAIR * expected_ordered_energy, CPAIR * variance_budget


def update_remove(r: np.ndarray, j: int, y: int) -> tuple[float, np.ndarray]:
    q = float(r[j, j])
    p = A + C * q
    prob = p if y else 1 - p
    gamma = -C / p if y else C / (1 - p)
    keep = [k for k in range(len(r)) if k != j]
    u = r[np.ix_(keep, [j])]
    nxt = r[np.ix_(keep, keep)] + gamma * (u @ u.T)
    return prob, nxt


def enumerate_reveals(r0: np.ndarray, core_size: int) -> tuple[float, float]:
    s0 = float(np.sum(r0[:core_size, core_size:] ** 2))
    total_qv = 0.0

    def rec(r: np.ndarray, weight: float) -> None:
        nonlocal total_qv
        if len(r) == core_size:
            return
        j = core_size
        a0 = r[:core_size, :core_size]
        for y in (0, 1):
            prob, nxt = update_remove(r, j, y)
            da = nxt[:core_size, :core_size] - a0
            total_qv += weight * prob * float(np.sum(da * da))
            rec(nxt, weight * prob)

    rec(r0, 1.0)
    assert total_qv <= C * C * s0 + 2e-11
    return total_qv, C * C * s0


def random_contraction(n: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    z = rng.normal(size=(n, n))
    u, _ = np.linalg.qr(z)
    eig = rng.uniform(0.05, 0.95, size=n)
    return (u * eig) @ u.T


def main() -> None:
    print("pair_cut_checks")
    for n, m in ((6, 2), (8, 3), (10, 4)):
        got = check_pair_cut(n, m)
        print(f"n={n} m={m} actual={got[0]:.12g} energy_bound={got[1]:.12g} variance_bound={got[2]:.12g}")
    print("reserve_checks")
    for seed in range(10):
        got, bound = enumerate_reveals(random_contraction(6, seed), 2)
        print(f"seed={seed} qv={got:.12g} c2S0={bound:.12g} ratio={got/bound:.9g}")
    print("all_stress_checks_passed=true")


if __name__ == "__main__":
    main()
