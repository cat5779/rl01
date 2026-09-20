#!/usr/bin/env python3
"""Interval certificate for S78 center-addition obstruction and barrier compensation.

Geometry (rho=1/2, c=19/20, a=1/40, hence d=1/2):
  core pair P={0,-3}; old exterior leaves {1,3}; add same-parity center -4.

The script certifies
  E f_new - E f_old < 0,
and, for ell(C)=log det C + log det(I-C) of the exact conditional pair kernel,
  (E f_new-E f_old) - (E ell_new-E ell_old) > 0.

All actual DPP words are retained.  mpmath.iv performs outward-rounded interval
arithmetic.  At half density all off-diagonal sine values are exactly 0 or
+/- c/(pi n).
"""
from itertools import product
from mpmath import iv

iv.dps = 80

C = iv.mpf(19) / 20
A = iv.mpf(1) / 40
D = A + C / 2
PAIR = [0, -3]
OLD = [0, -3, 1, 3]
NEW = [0, -3, 1, 3, -4]
OLD_EXT = [1, 3]
NEW_EXT = [1, 3, -4]


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
                K[p, q] = C * sine_sign_half_density(diff) / (iv.pi * diff)
    return K


def word_probability(K, bits):
    M = iv.matrix(K)
    zeros = 0
    for j, bit in enumerate(bits):
        if bit == 0:
            M[j, j] -= 1
            zeros += 1
    det = iv.det(M)
    return -det if zeros % 2 else det


def expected_pair_f(indices):
    K = kernel(indices)
    pos = {site: k for k, site in enumerate(indices)}
    p, q = pos[PAIR[0]], pos[PAIR[1]]
    total = iv.mpf([0, 0])
    mass = iv.mpf([0, 0])
    for bits in product((0, 1), repeat=len(indices)):
        M = iv.matrix(K)
        zeros = 0
        for j, bit in enumerate(bits):
            if bit == 0:
                M[j, j] -= 1
                zeros += 1
        det = iv.det(M)
        prob = -det if zeros % 2 else det
        G = M ** -1
        h = G[p, q] ** 2
        x = G[p, p] * G[q, q]
        f = h + (x - h) * iv.log(1 - h / x)
        total += prob * f
        mass += prob
    return total, mass


def expected_pair_barrier(exterior):
    # Work in the marginal on P union exterior; unlisted sites are marginalized.
    indices = PAIR + exterior
    K = kernel(indices)
    Kpp = iv.matrix([[K[0, 0], K[0, 1]], [K[1, 0], K[1, 1]]])
    epos = list(range(2, len(indices)))
    Kee = iv.matrix(len(epos))
    Kpe = iv.matrix(2, len(epos))
    Kep = iv.matrix(len(epos), 2)
    for a, ia in enumerate(epos):
        for b, ib in enumerate(epos):
            Kee[a, b] = K[ia, ib]
        for r in range(2):
            Kpe[r, a] = K[r, ia]
            Kep[a, r] = K[ia, r]

    total = iv.mpf([0, 0])
    mass = iv.mpf([0, 0])
    for bits in product((0, 1), repeat=len(exterior)):
        Me = iv.matrix(Kee)
        zeros = 0
        for j, bit in enumerate(bits):
            if bit == 0:
                Me[j, j] -= 1
                zeros += 1
        det_e = iv.det(Me)
        prob = -det_e if zeros % 2 else det_e
        Cpair = Kpp - Kpe * (Me ** -1) * Kep
        Iminus = iv.matrix([[1 - Cpair[0, 0], -Cpair[0, 1]],
                            [-Cpair[1, 0], 1 - Cpair[1, 1]]])
        ell = iv.log(iv.det(Cpair)) + iv.log(iv.det(Iminus))
        total += prob * ell
        mass += prob
    return total, mass


def main():
    old_f, old_mass = expected_pair_f(OLD)
    new_f, new_mass = expected_pair_f(NEW)
    old_l, old_ext_mass = expected_pair_barrier(OLD_EXT)
    new_l, new_ext_mass = expected_pair_barrier(NEW_EXT)

    drift_f = new_f - old_f
    drift_l = new_l - old_l
    compensated = drift_f - drift_l

    print("old_expected_f       =", old_f)
    print("new_expected_f       =", new_f)
    print("center_add_f_drift   =", drift_f)
    print("old_expected_ell     =", old_l)
    print("new_expected_ell     =", new_l)
    print("barrier_drift        =", drift_l)
    print("compensated_drift    =", compensated)
    print("full_word_masses     =", old_mass, new_mass)
    print("exterior_word_masses =", old_ext_mass, new_ext_mass)

    masses_ok = all(m.a <= 1 <= m.b for m in
                    (old_mass, new_mass, old_ext_mass, new_ext_mass))
    if drift_f.b < 0 and compensated.a > 0 and masses_ok:
        print("PASS_CENTER_ADD_NEGATIVE_AND_BARRIER_COMPENSATED")
        return 0
    print("FAIL_CENTER_ADD_NEGATIVE_AND_BARRIER_COMPENSATED")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
