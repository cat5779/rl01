"""Exploratory actual-law enumeration for the S18 exact logarithmic potential.

This is a floating-point probe, not a sign certificate.  It enumerates every
output word of a finite half-density sine Toeplitz marginal and weights by its
true determinant probability.
"""

from __future__ import annotations

import argparse
import itertools
import math
from dataclasses import dataclass

import numpy as np


A0 = 1.0 / 40.0
C0 = 19.0 / 20.0


def sine_kernel(n: int) -> np.ndarray:
    q = np.empty((n, n), dtype=np.float64)
    for i in range(n):
        for j in range(n):
            r = i - j
            q[i, j] = 0.5 if r == 0 else math.sin(math.pi * r / 2) / (math.pi * r)
    return q


def exact_pair_atom(v: float, h: float) -> float:
    # The expression is continuous at h=0.  log1p is essential when h/|v|
    # is small.  Strict channel atoms guarantee v and v-h are nonzero and
    # have the same sign.
    if h == 0.0:
        return 0.0
    z = -h / v
    return h + (v - h) * math.log1p(z)


def phi_core(g: np.ndarray, core: range) -> float:
    ans = sum(float(g[i, i] ** 2) for i in core)
    for i in core:
        for j in core:
            if i >= j:
                continue
            h = float(g[i, j] ** 2)
            v = float(g[i, i] * g[j, j])
            ans += 2.0 * exact_pair_atom(v, h)
    return ans


@dataclass
class Result:
    n: int
    m: int
    ell: int
    total_mass: float
    expected_phi: float
    w: float
    min_probability: float
    max_probability: float
    expected_diag: float
    expected_pair_same: float
    expected_pair_opp: float
    expected_posterior_opp_energy: float
    expected_quartic_bracket: float
    u_old: float
    expected_external_storage: float


def enumerate_window(m: int, ell: int) -> Result:
    n = m + 2 * ell
    q = sine_kernel(n)
    k = A0 * np.eye(n) + C0 * q
    core = range(ell, ell + m)
    mass = 0.0
    ephi = 0.0
    minp = math.inf
    maxp = 0.0
    ediag = 0.0
    epsame = 0.0
    epopp = 0.0
    eropp = 0.0
    equartic = 0.0
    estorage = 0.0
    outside_gram = q - q @ q
    beta = A0 * (A0 + C0)
    for bits in itertools.product((0, 1), repeat=n):
        mat = k - np.diag([1 - b for b in bits])
        sign, logabsdet = np.linalg.slogdet(mat)
        parity = -1.0 if (n - sum(bits)) % 2 else 1.0
        p = parity * sign * math.exp(logabsdet)
        if p <= 0.0:
            raise ArithmeticError((bits, p, sign, logabsdet))
        g = np.linalg.inv(mat)
        alpha = np.array([A0 if b else 1 - A0 for b in bits])
        sigma = np.array([1.0 if b else -1.0 for b in bits])
        field = (alpha + sigma * C0) / alpha
        transfer = np.linalg.inv(
            np.eye(n) + q @ np.diag(field - 1.0)
        )
        left = np.diag(np.sqrt(field)) @ transfer
        posterior_outside_gram = left @ outside_gram @ left.T
        storage = sum(float(posterior_outside_gram[i, i]) for i in core)
        val = phi_core(g, core)
        diag = sum(float(g[i, i] ** 2) for i in core)
        quartic_bracket = diag
        for i in core:
            for j in core:
                quartic_bracket += float(
                    g[i, j] ** 4 / (g[i, i] * g[j, j])
                )
        psame = 0.0
        popp = 0.0
        ropp = 0.0
        for i in core:
            for j in core:
                if i >= j:
                    continue
                h = float(g[i, j] ** 2)
                v = float(g[i, i] * g[j, j])
                atom = 2.0 * exact_pair_atom(v, h)
                if bits[i] == bits[j]:
                    psame += atom
                else:
                    popp += atom
                    ropp += (beta * beta / (C0 * C0)) * h
        mass += p
        ephi += p * val
        ediag += p * diag
        epsame += p * psame
        epopp += p * popp
        eropp += p * ropp
        equartic += p * quartic_bracket
        estorage += p * storage
        minp = min(minp, p)
        maxp = max(maxp, p)
    return Result(n, m, ell, mass, ephi, -ephi / m, minp, maxp,
                  ediag, epsame, epopp, eropp, equartic,
                  -equartic / (2 * m), estorage)


def main() -> None:
    global A0, C0
    parser = argparse.ArgumentParser()
    parser.add_argument("--c", type=float, default=C0)
    parser.add_argument(
        "--a",
        type=float,
        default=None,
        help="channel offset; defaults to the balanced value (1-c)/2",
    )
    parser.add_argument("pairs", nargs="*", help="m,L pairs such as 4,2")
    args = parser.parse_args()
    C0 = args.c
    A0 = (1.0 - C0) / 2.0 if args.a is None else args.a
    print(f"channel a={A0:.17g} c={C0:.17g}")
    pairs = []
    for item in args.pairs or ["6,0", "4,2"]:
        m, ell = map(int, item.split(","))
        pairs.append((m, ell))
    for m, ell in pairs:
        r = enumerate_window(m, ell)
        print(
            f"m={r.m} L={r.ell} N={r.n} mass={r.total_mass:.16g} "
            f"Ephi={r.expected_phi:.16g} W={r.w:.16g} "
            f"pmin={r.min_probability:.3e} pmax={r.max_probability:.3e}"
        )
        print(
            f"  per_site diag={r.expected_diag/r.m:.12g} "
            f"pair_same={r.expected_pair_same/r.m:.12g} "
            f"pair_opp={r.expected_pair_opp/r.m:.12g} "
            f"Ropp={r.expected_posterior_opp_energy/r.m:.12g}"
        )
        print(
            f"  old_U={r.u_old:.12g} exact_W={r.w:.12g} "
            f"W_minus_U={r.w-r.u_old:.12g} "
            f"external_storage={r.expected_external_storage:.12g}"
        )


if __name__ == "__main__":
    main()
