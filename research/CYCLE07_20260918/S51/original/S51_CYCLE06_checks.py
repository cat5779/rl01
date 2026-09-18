#!/usr/bin/env python3
"""Numerical sanity checks for S51 cycle06.

These are checks only, not a proof or independent certification.
They verify on small exact finite DPPs that

  dH/du = -(1/u) sum_i E phi(q_i)

and that the complete moving-law V14 expression satisfies

  d^2/ds^2 E phi(q_C) = u^2 E barG_C.

Only NumPy is required.
"""

from __future__ import annotations

import itertools
import math
from typing import Dict, Iterable, Sequence, Tuple

import numpy as np

Bits = Tuple[int, ...]


def q_half(sites: Sequence[int]) -> np.ndarray:
    """Half-density sine projection principal block."""
    n = len(sites)
    q = np.empty((n, n), dtype=float)
    for a, i in enumerate(sites):
        for b, j in enumerate(sites):
            if i == j:
                q[a, b] = 0.5
            else:
                k = i - j
                q[a, b] = math.sin(math.pi * k / 2.0) / (math.pi * k)
    return q


def kernel(sites: Sequence[int], u: float, s: float, c: float) -> np.ndarray:
    q = q_half(sites)
    eye = np.eye(len(sites))
    return 0.5 * eye + u * (c * (q - 0.5 * eye) + s * eye)


def atom_probability(k: np.ndarray, bits: Bits) -> float:
    """Exact DPP full atom: (-1)^(#zeros) det(K-diag(1-z))."""
    z = np.asarray(bits, dtype=float)
    b = k - np.diag(1.0 - z)
    return float(((-1) ** int(np.sum(1.0 - z))) * np.linalg.det(b))


def atom_law(k: np.ndarray) -> Dict[Bits, float]:
    n = k.shape[0]
    return {
        bits: atom_probability(k, bits)
        for bits in itertools.product((0, 1), repeat=n)
    }


def shannon_entropy(law: Dict[Bits, float]) -> float:
    return -sum(p * math.log(p) for p in law.values() if p > 0.0)


def phi(q: float) -> float:
    return (q - 0.5) * math.log(q / (1.0 - q))


def phi_prime(q: float) -> float:
    return math.log(q / (1.0 - q)) + (q - 0.5) / (q * (1.0 - q))


def phi_second(q: float) -> float:
    return 1.0 / (2.0 * q * q * (1.0 - q) * (1.0 - q))


def bregman(fun, dfun, p: float, q: float) -> float:
    return fun(p) - fun(q) - dfun(q) * (p - q)


def all_anchor_functionals(k: np.ndarray) -> list[float]:
    """Return E phi(P(Y_i=1 | Y_{-i})) for every anchor."""
    n = k.shape[0]
    law = atom_law(k)
    out: list[float] = []
    for anchor in range(n):
        grouped: Dict[Bits, list[float]] = {}
        for bits, p in law.items():
            ext = bits[:anchor] + bits[anchor + 1 :]
            grouped.setdefault(ext, [0.0, 0.0])[bits[anchor]] += p
        value = 0.0
        for p0, p1 in grouped.values():
            w = p0 + p1
            q = p1 / w
            value += w * phi(q)
        out.append(value)
    return out


def anchor_functional(k: np.ndarray, anchor: int) -> float:
    return all_anchor_functionals(k)[anchor]


def conditional_data(
    k: np.ndarray, anchor: int, ext_bits: Bits
) -> tuple[np.ndarray, np.ndarray, float, float, np.ndarray]:
    """Return G, v, q, A=1+||v||^2, and bar-r for one exterior word."""
    n = k.shape[0]
    exterior = [i for i in range(n) if i != anchor]
    h = float(k[anchor, anchor])
    b = k[np.ix_(exterior, [anchor])].reshape(-1)
    kc = k[np.ix_(exterior, exterior)]
    z = np.asarray(ext_bits, dtype=int)
    sigma = 2 * z - 1
    bmat = kc - np.diag(1 - z)
    g = np.linalg.inv(bmat)
    v = g @ b
    q = h - float(b @ v)
    a = 1.0 + float(v @ v)
    bar_r = sigma - np.diag(g)
    return g, v, q, a, bar_r


def finite_bar_g(k: np.ndarray, anchor: int, ext_bits: Bits) -> float:
    """Complete normalized finite V14 kernel for one exterior word."""
    n = k.shape[0]
    m = n - 1
    z = np.asarray(ext_bits, dtype=int)
    g, _, q, a_z, bar_r = conditional_data(k, anchor, ext_bits)

    q_i: list[float] = []
    a_i: list[float] = []
    for i in range(m):
        zi = z.copy()
        zi[i] ^= 1
        _, _, qi, ai, _ = conditional_data(k, anchor, tuple(int(x) for x in zi))
        q_i.append(qi)
        a_i.append(ai)

    def bar_b(bits: Bits, derivative_level: int) -> float:
        zz = np.asarray(bits, dtype=int)
        _, _, qq, _, rr = conditional_data(k, anchor, bits)
        total = 0.0
        for i in range(m):
            zi = zz.copy()
            zi[i] ^= 1
            _, _, qqi, _, _ = conditional_data(
                k, anchor, tuple(int(x) for x in zi)
            )
            if derivative_level == 0:
                total += rr[i] * bregman(phi, phi_prime, qqi, qq)
            elif derivative_level == 1:
                total += rr[i] * bregman(phi_prime, phi_second, qqi, qq)
            else:
                raise ValueError("derivative_level must be 0 or 1")
        return total

    bar_b_phi = bar_b(ext_bits, 0)
    value = phi_second(q) + bar_b(ext_bits, 1)
    g2 = g @ g

    for i in range(m):
        d_i = q_i[i] - q
        value += g2[i, i] * bregman(phi, phi_prime, q_i[i], q)
        value += bar_r[i] * (
            (phi_prime(q_i[i]) - phi_prime(q)) * a_i[i]
            - phi_second(q) * d_i * a_z
        )

    for j in range(m):
        zj = z.copy()
        zj[j] ^= 1
        value += bar_r[j] * (
            bar_b(tuple(int(x) for x in zj), 0) - bar_b_phi
        )

    return float(value)


def expected_finite_bar_g(k: np.ndarray, anchor: int) -> float:
    n = k.shape[0]
    exterior = [i for i in range(n) if i != anchor]
    kc = k[np.ix_(exterior, exterior)]
    total = 0.0
    for ext_bits in itertools.product((0, 1), repeat=n - 1):
        w = atom_probability(kc, ext_bits)
        total += w * finite_bar_g(k, anchor, ext_bits)
    return total


def check_entropy_production() -> float:
    sites = list(range(5))
    c, u, s = 0.70, 0.60, 0.08
    eps = 1.0e-5
    h_plus = shannon_entropy(atom_law(kernel(sites, u + eps, s, c)))
    h_minus = shannon_entropy(atom_law(kernel(sites, u - eps, s, c)))
    numerical = (h_plus - h_minus) / (2.0 * eps)
    exact = -sum(all_anchor_functionals(kernel(sites, u, s, c))) / u
    error = abs(numerical - exact)
    print("entropy-production check")
    print(f"  finite-difference dH/du : {numerical:.15e}")
    print(f"  -sum_i F_i/u           : {exact:.15e}")
    print(f"  absolute error          : {error:.3e}")
    return error


def check_complete_v14() -> float:
    sites = [-2, -1, 0, 1, 2]
    anchor = 2
    c, u, s = 0.70, 0.60, 0.08
    eps = 1.0e-4
    f0 = anchor_functional(kernel(sites, u, s, c), anchor)
    f_plus = anchor_functional(kernel(sites, u, s + eps, c), anchor)
    f_minus = anchor_functional(kernel(sites, u, s - eps, c), anchor)
    numerical = (f_plus + f_minus - 2.0 * f0) / (eps * eps)
    exact = u * u * expected_finite_bar_g(kernel(sites, u, s, c), anchor)
    error = abs(numerical - exact)
    print("complete V14 moving-law check")
    print(f"  finite-difference d2F/ds2 : {numerical:.15e}")
    print(f"  u^2 E[barG]               : {exact:.15e}")
    print(f"  absolute error             : {error:.3e}")
    return error


def main() -> None:
    entropy_error = check_entropy_production()
    v14_error = check_complete_v14()

    # The second derivative uses a finite difference and is therefore less sharp.
    if entropy_error > 1.0e-7:
        raise SystemExit("entropy-production check failed")
    if v14_error > 2.0e-6:
        raise SystemExit("complete V14 check failed")
    print("all checks passed")


if __name__ == "__main__":
    main()
