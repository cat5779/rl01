#!/usr/bin/env python3
"""Interval certificate for the S78 two-center reveal counterexample.

Uses mpmath.iv interval arithmetic at rho=1/2, where every off-diagonal
sine value is exactly 0 or +/-1/(pi n). It enumerates all actual DPP words
for the old and refined observed sets and evaluates Chi from the true
principal compression.
"""
from itertools import product
from mpmath import iv

iv.dps = 80

RHO = iv.mpf(1) / 2
C = iv.mpf(19) / 20
A = iv.mpf(1) / 40
D = A + C / 2

OLD = [0, 10, 7, -3]
NEW = [0, 10, 7, -3, -1]
CORE = [0, 10, 7]


def sine_sign_half_density(diff: int) -> int:
    if diff % 2 == 0:
        return 0
    return 1 if diff % 4 == 1 else -1


def kernel(indices):
    n = len(indices)
    K = iv.matrix(n)
    for p, i in enumerate(indices):
        for q, j in enumerate(indices):
            if i == j:
                K[p, q] = D
            else:
                diff = i - j
                sg = sine_sign_half_density(diff)
                K[p, q] = C * sg / (iv.pi * diff)
    return K


def expected_chi(indices, core):
    K = kernel(indices)
    pos = {site: k for k, site in enumerate(indices)}
    pairs = []
    for a in range(len(core)):
        for b in range(a + 1, len(core)):
            if (core[a] - core[b]) % 2:
                pairs.append((pos[core[a]], pos[core[b]]))

    total = iv.mpf([0, 0])
    total_probability = iv.mpf([0, 0])
    n = len(indices)
    for bits in product((0, 1), repeat=n):
        M = iv.matrix(K)
        zeros = 0
        for j, bit in enumerate(bits):
            if bit == 0:
                M[j, j] -= 1
                zeros += 1
        det = iv.det(M)
        probability = -det if zeros % 2 else det
        G = M ** -1

        chi = iv.mpf([0, 0])
        for p, q in pairs:
            h = G[p, q] ** 2
            x = G[p, p] * G[q, q]
            chi += h + (x - h) * iv.log(1 - h / x)

        total += probability * chi
        total_probability += probability
    return total, total_probability


def main():
    old_value, old_mass = expected_chi(OLD, CORE)
    new_value, new_mass = expected_chi(NEW, CORE)
    drift = new_value - old_value

    print("old_expected_chi =", old_value)
    print("new_expected_chi =", new_value)
    print("reveal_drift     =", drift)
    print("old_total_mass   =", old_mass)
    print("new_total_mass   =", new_mass)

    # mpmath.iv intervals expose endpoints through .a and .b.
    if drift.b < 0 and old_mass.a <= 1 <= old_mass.b and new_mass.a <= 1 <= new_mass.b:
        print("PASS_INTERVAL_K2_NEGATIVE_REVEAL")
        return 0
    print("FAIL_INTERVAL_K2_NEGATIVE_REVEAL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
