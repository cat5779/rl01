#!/usr/bin/env python3
"""Exact and finite diagnostics for S59 Cycle 09.

The exact part uses only Python's standard library.  Optional finite cyclic
DPP diagnostics require NumPy and are enabled with --cycles.
"""
from __future__ import annotations

from fractions import Fraction as F
from decimal import Decimal, getcontext
from math import log
import argparse
import itertools

# Frozen constants
c = F(19, 20)
b = F(39, 1600)
m = 2 * b
R = (1 - m) / m  # 761/39
C = F(59, 40)


def trim(p):
    p = list(p)
    while len(p) > 1 and p[0] == 0:
        p.pop(0)
    return p


def pder(p):
    n = len(p) - 1
    return trim([p[i] * (n - i) for i in range(n)]) or [F(0)]


def pdivmod(a, d):
    a = trim(a)
    d = trim(d)
    if d == [0]:
        raise ZeroDivisionError
    q = [F(0)] * max(1, len(a) - len(d) + 1)
    r = a[:]
    while len(r) >= len(d) and r != [0]:
        coeff = r[0] / d[0]
        shift = len(r) - len(d)
        qi = len(q) - shift - 1
        q[qi] += coeff
        sub = [coeff * x for x in d] + [F(0)] * shift
        r = trim([x - y for x, y in zip(r, sub)])
    return trim(q), trim(r)


def peval(p, x):
    out = F(0)
    for a in p:
        out = out * x + a
    return out


def sturm_sequence(p):
    seq = [trim(p), pder(p)]
    while seq[-1] != [0]:
        _, rem = pdivmod(seq[-2], seq[-1])
        if rem == [0]:
            break
        seq.append([-x for x in rem])
    return seq


def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def variations(seq, x):
    signs = [sign(peval(p, x)) for p in seq]
    nz = [s for s in signs if s]
    return signs, sum(a != d for a, d in zip(nz, nz[1:]))


def A_of_t(t):
    return (t - 1) * (R * R + (2 * R + 1) * t) / (t * (R * R + t + 2 * R))


def atanh_log_upper(x, N=20):
    """Rational upper bound for log(x), x>1, using N+1 atanh terms."""
    z = (x - 1) / (x + 1)
    s = sum((2 * z ** (2 * k + 1) / F(2 * k + 1) for k in range(N + 1)), F(0))
    remainder = 2 * z ** (2 * N + 3) / (F(2 * N + 3) * (1 - z * z))
    return s + remainder


def atanh_log_lower(x, N=5):
    z = (x - 1) / (x + 1)
    return sum((2 * z ** (2 * k + 1) / F(2 * k + 1) for k in range(N + 1)), F(0))


def exact_certificate():
    # F'(t) has the sign of P(t) on t>0.
    P = [
        F(-92537640),
        F(2169131175861),
        F(-16202277858802),
        F(21815639220581),
    ]
    seq = sturm_sequence(P)
    a1 = F(110133, 62500)          # 1.762128
    b1 = F(1762129, 10**6)        # 1.762129
    a2 = F(5709301, 10**6)        # 5.709301
    b2 = F(2854651, 500000)       # 5.709302
    pts = [("1", F(1)), ("a1", a1), ("b1", b1), ("a2", a2),
           ("b2", b2), ("R^2", R * R)]

    print("EXACT STURM VARIATIONS")
    vals = {}
    for name, x in pts:
        signs, v = variations(seq, x)
        vals[name] = v
        print(f"  {name:>3}: signs={signs}, variations={v}")
    assert vals == {"1": 3, "a1": 3, "b1": 2, "a2": 2, "b2": 1, "R^2": 1}
    assert peval(P, F(1)) > 0

    log_b2_upper = atanh_log_upper(b2, 20)
    lower = C * A_of_t(a2) - log_b2_upper
    target = F(709, 10_000_000)
    assert lower > target
    print("\nSCALAR ENVELOPE CERTIFICATE")
    print("  (59/40) A(a2) - upper_log(b2) > 709/10^7")
    print(f"  exact excess over 709/10^7 = {lower - target}")
    print(f"  decimal lower bound = {float(lower):.16g}")

    # Exact failure witness for Phi_*(q)=1/(q(1-q)-b).
    t0 = F(6)
    Z = 2 + R + t0 / R
    p00 = 1 / Z
    p01 = (t0 / R) / Z
    p10 = R / Z
    p11 = 1 / Z
    assert (p00, p01, p10, p11) == (
        F(29679, 647605), F(9126, 647605),
        F(579121, 647605), F(29679, 647605))
    s = p01 + p11
    q0 = p10 / (p00 + p10)
    q1 = p11 / (p01 + p11)
    a = q0 - q1
    D0 = q0 * (1 - q0)
    D1 = q1 * (1 - q1)
    rhs_star = a * (s / (D0 - b) + (1 - s) / (D1 - b))
    assert rhs_star == F(19311189939680, 11811914073463)
    assert rhs_star < F(5, 3)
    # log 6 = log 2 + log 3 > 2/3 + 1 = 5/3.
    # log 2 > 2*(1/3), and e<3 implies log 3>1.
    print("\nLOCAL CEMETERY-BELLMAN FAILURE")
    print(f"  table = {[p00, p01, p10, p11]}")
    print(f"  q0={q0}, q1={q1}, s={s}")
    print(f"  Phi_* RHS = {rhs_star} = {float(rhs_star):.15f}")
    print("  log(6) > 5/3 > Phi_* RHS, so the candidate fails exactly.")

    # The witness is an independent BSC image of a legal two-site DPP.
    eps = F(1, 40)
    cc = F(19, 20)
    A = p10 + p11
    B = p01 + p11
    Delta = p10 * p01 - p00 * p11
    alpha = (A - eps) / cc
    beta = (B - eps) / cc
    delta = Delta / (cc * cc)
    latent = (
        (1 - alpha) * (1 - beta) - delta,
        (1 - alpha) * beta + delta,
        alpha * (1 - beta) + delta,
        alpha * beta - delta,
    )
    assert all(x > 0 for x in latent)
    assert sum(latent, F(0)) == 1
    assert delta > 0
    print("  latent BSC preimage atoms:")
    print(f"    {latent}")

    # It also proves the local relaxation permits r>1.47.
    E = a * (s / D0 + (1 - s) / D1)
    assert E == F(944395, 777126)
    lower_log6 = atanh_log_lower(F(6), 5)
    assert lower_log6 > F(147, 100) * E
    print(f"  E={E}; six positive atanh terms certify log(6)/E > 147/100.")

    getcontext().prec = 60
    Rd = Decimal(R.numerator) / Decimal(R.denominator)
    Md = Decimal(361) / (Decimal(800) * Rd.ln())
    nud = Decimal(1) - Decimal(39) * Rd.ln() / Decimal(722)
    Bd = Decimal(59) * nud / Decimal(40)
    Gd = (Decimal(1) - Bd) / (Decimal(39) / Decimal(1600))
    old = (Decimal(1) + (Decimal(19) / Decimal(20)) ** 2) ** 2 * Rd.ln() / Decimal(2)
    print("\nACTUAL-LAW NUMERICAL INSERTION")
    print(f"  M              = {Md}")
    print(f"  nu upper       = {nud}")
    print(f"  (59/40)nu      = {Bd}")
    print(f"  bGamma lower   = {Decimal(1)-Bd}")
    print(f"  Gamma lower    = {Gd}")
    print(f"  old endpoint bJ upper = {old}")


def cyclic_diagnostics(max_n=14):
    try:
        import numpy as np
    except ImportError as e:
        raise SystemExit("NumPy is required for --cycles") from e

    cf = float(c)
    bf = float(b)
    epsf = (1 - cf) / 2
    print("\nFINITE CYCLIC DIAGNOSTICS (NOT PART OF THE INFINITE PROOF)")
    print(" n        bJ             nu             max_r")
    for n in range(2, max_n + 1, 2):
        # Contiguous half of the Fourier modes: genuine rank-n/2 projection.
        j = np.arange(n)
        Fm = np.exp(2j * np.pi * np.outer(j, j) / n) / np.sqrt(n)
        modes = np.arange(n // 2)
        P = Fm[:, modes] @ Fm[:, modes].conj().T
        K = epsf * np.eye(n) + cf * P
        L = K @ np.linalg.inv(np.eye(n) - K)
        det_norm = np.linalg.det(np.eye(n) + L).real
        probs = np.empty(1 << n)
        for mask in range(1 << n):
            S = [k for k in range(n) if (mask >> k) & 1]
            probs[mask] = (np.linalg.det(L[np.ix_(S, S)]).real if S else 1.0) / det_norm
        probs = np.maximum(probs, 0.0)
        probs /= probs.sum()

        J = 0.0
        Esum = 0.0
        maxr = 1.0
        for i in range(1, n):
            groups = {}
            for mask, pr in enumerate(probs):
                ext = mask & ~(1 << 0) & ~(1 << i)
                a0 = (mask >> 0) & 1
                ai = (mask >> i) & 1
                arr = groups.setdefault(ext, [0.0, 0.0, 0.0, 0.0])
                arr[2 * a0 + ai] += pr  # 00,01,10,11
            for arr in groups.values():
                w = sum(arr)
                p00, p01, p10, p11 = [x / w for x in arr]
                Delta = p10 * p01 - p00 * p11
                if Delta <= 1e-15:
                    continue
                ell = log((p10 * p01) / (p00 * p11))
                Ei = Delta * sum(1 / x for x in (p00, p01, p10, p11))
                J += w * ell
                Esum += w * Ei
                maxr = max(maxr, ell / Ei)
        print(f"{n:2d}  {bf*J: .12f}  {bf*Esum: .12f}  {maxr: .12f}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--cycles", action="store_true", help="run optional finite cyclic diagnostics")
    ap.add_argument("--max-n", type=int, default=14)
    args = ap.parse_args()
    exact_certificate()
    if args.cycles:
        cyclic_diagnostics(args.max_n)
