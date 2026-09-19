#!/usr/bin/env python3
"""Runnable archival copy of the author-supplied S73 check.

The executable logic is preserved; comments and the module docstring are
normalized for this review.  The authoritative original-byte hash is recorded
in S73_CYCLE25_SOURCE.md.
"""

from fractions import Fraction
import itertools
import math
import numpy as np


def exact_m2_certificate():
    c = Fraction(19, 20)
    r = (1 - c * c) / 4
    s = (1 + c * c) / 4
    numerator = (r * r + s * s) ** 2
    denominator = 4 * r * r * s * s
    ratio = numerator / denominator
    assert ratio > 1

    gain2 = float(8 * s) * math.log(float(ratio))
    input2 = 8 * math.log(float(s / r)) - 4 / float(r)
    output2 = input2 + gain2

    print("EXACT M=2 CERTIFICATE")
    print("c =", c, "a =", (1-c)/2)
    print("r =", r, "s =", s)
    print("ratio =", ratio)
    print("integer comparison:",
          ratio.numerator, ">", ratio.denominator,
          "=", ratio.numerator > ratio.denominator)
    print("G'' =", repr(gain2))
    print("H_in'' =", repr(input2))
    print("H_out'' =", repr(output2))
    assert gain2 > 0
    assert output2 < 0


def cyclic_unitary(m: int) -> np.ndarray:
    n = 2 * m
    rows = np.arange(n)[:, None]
    modes = np.arange(m)[None, :]
    F = np.exp(2j * np.pi * rows * modes / n) / np.sqrt(n)
    Q = F @ F.conj().T
    even = np.arange(0, n, 2)
    odd = np.arange(1, n, 2)
    U = 2 * Q[np.ix_(even, odd)]
    err = np.linalg.norm(U.conj().T @ U - np.eye(m), ord=2)
    assert err < 2e-12
    return U


def bit_words(m):
    return list(itertools.product((0, 1), repeat=m))


def exterior_channel(U: np.ndarray):
    m = U.shape[0]
    words = bit_words(m)
    W = np.zeros((2**m, 2**m), dtype=float)
    for iz, z in enumerate(words):
        Z = [i for i, bit in enumerate(z) if bit]
        for it, t in enumerate(words):
            T = [i for i, bit in enumerate(t) if bit]
            if len(Z) != len(T):
                continue
            W[iz, it] = 1.0 if not Z else abs(
                np.linalg.det(U[np.ix_(Z, T)])
            )**2
    assert np.max(abs(W.sum(axis=0) - 1)) < 2e-11
    assert np.max(abs(W.sum(axis=1) - 1)) < 2e-11
    return words, W


def pair_jets(a, c):
    p = a + c / 2
    d = c*c/4
    return {
        (0, 0): ((1-p)**2-d, -2*(1-p), 2.0),
        (0, 1): (p*(1-p)+d, 1-2*p, -2.0),
        (1, 0): (p*(1-p)+d, 1-2*p, -2.0),
        (1, 1): (p*p-d, 2*p, 2.0),
    }


def product_jet(factors):
    v, d1, d2 = 1.0, 0.0, 0.0
    for x, x1, x2 in factors:
        ov, od1, od2 = v, d1, d2
        v = ov*x
        d1 = od1*x + ov*x1
        d2 = od2*x + 2*od1*x1 + ov*x2
    return v, d1, d2


def entropy_second(P, P1, P2):
    mask = P > 0
    return float(-np.sum(P2[mask]*np.log(P[mask]) + P1[mask]**2/P[mask]))


def enumerated_curvature(m, a, c):
    U = cyclic_unitary(m)
    words, W = exterior_channel(U)
    q = pair_jets(a, c)
    n = 2**m
    P = np.zeros((n, n))
    P1 = np.zeros_like(P)
    P2 = np.zeros_like(P)

    for iy, y in enumerate(words):
        for iz, z in enumerate(words):
            jet = product_jet(q[(y[i], z[i])] for i in range(m))
            P[iy, iz], P1[iy, iz], P2[iy, iz] = jet

    Q, Q1, Q2 = P @ W, P1 @ W, P2 @ W
    Hin2 = entropy_second(P, P1, P2)
    Hout2 = entropy_second(Q, Q1, Q2)
    Gdirect = Hout2 - Hin2

    term_acc = 0.0
    term_fisher = 0.0
    for iy in range(n):
        for it in range(n):
            qo = Q[iy, it]
            if qo <= 0:
                continue
            post = []
            scores = []
            for iz in range(n):
                joint = P[iy, iz] * W[iz, it]
                if joint <= 0:
                    continue
                w = joint / qo
                score = P1[iy, iz] / P[iy, iz]
                accel = P2[iy, iz] / P[iy, iz]
                R = math.log(P[iy, iz] / qo)
                post.append(w)
                scores.append(score)
                term_acc += joint * accel * R
            mean_score = sum(w*s for w, s in zip(post, scores))
            term_fisher += qo * sum(
                w*(s-mean_score)**2 for w, s in zip(post, scores)
            )

    residual = Gdirect - term_acc - term_fisher
    return Hin2, Hout2, Gdirect, term_acc, term_fisher, residual


def diagnostics():
    print("\nCYCLIC ENUMERATION, c=.95, midpoint a=.025")
    for m in (1, 2, 3, 4):
        vals = enumerated_curvature(m, 0.025, 0.95)
        print(
            f"m={m}: H_in''={vals[0]: .12f}, "
            f"H_out''={vals[1]: .12f}, G''={vals[2]: .12f}, "
            f"acc={vals[3]: .12f}, FisherLoss={vals[4]: .12e}, "
            f"identity residual={vals[5]: .3e}"
        )
        assert abs(vals[5]) < 2e-9

    print("\nOFF-MIDPOINT IDENTITY CHECK, c=.95, a=.023, m=3")
    vals = enumerated_curvature(3, 0.023, 0.95)
    print(
        f"H_in''={vals[0]: .12f}, H_out''={vals[1]: .12f}, "
        f"G''={vals[2]: .12f}, acc={vals[3]: .12f}, "
        f"FisherLoss={vals[4]: .12f}, residual={vals[5]: .3e}"
    )
    assert abs(vals[5]) < 2e-9


if __name__ == "__main__":
    exact_m2_certificate()
    diagnostics()
