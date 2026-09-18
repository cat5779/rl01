#!/usr/bin/env python3
"""Rigorous finite first-doubling chord check for the S42 benchmark.

This script has deliberately finite scope.  It enumerates the 64 six-site and
4096 twelve-site atoms at a=3/200, 1/40, 7/200 using 256-bit Arb balls.  It
certifies Delta_eta J_6 for J_6=2 H_6-H_12.  It does not inspect or replace any
of the remaining dyadic scales in M_12 or M_13.
"""

from __future__ import annotations

from itertools import product

from flint import arb, arb_mat, ctx


ctx.prec = 256
C = arb(19) / 20
A_MINUS = arb(3) / 200
A_ZERO = arb(1) / 40
A_PLUS = arb(7) / 200


def sine_q(n: int) -> arb_mat:
    q = arb_mat(n, n)
    pi = arb.pi()
    for i in range(n):
        for j in range(n):
            r = i - j
            if r == 0:
                q[i, j] = arb(1) / 2
            elif r % 2 == 0:
                q[i, j] = 0
            else:
                q[i, j] = arb(1 if r % 4 == 1 else -1) / (pi * r)
    return q


def entropy(n: int, a: arb) -> tuple[arb, arb]:
    q = sine_q(n)
    total_p = arb(0)
    value = arb(0)
    for bits in product((0, 1), repeat=n):
        matrix = arb_mat(n, n)
        zeros = 0
        for i in range(n):
            for j in range(n):
                matrix[i, j] = C * q[i, j] + (a if i == j else 0)
            if bits[i] == 0:
                matrix[i, i] -= 1
                zeros += 1
        probability = (-1 if zeros % 2 else 1) * matrix.det()
        if not probability > 0:
            raise ArithmeticError(
                f"atom positivity not certified: n={n}, a={a}, bits={bits}, p={probability}"
            )
        total_p += probability
        value -= probability * probability.log()
    return value, total_p


def sharp_tail(length: int) -> arb:
    c_bal = 2 * C * ((1 + C) / (1 - C)).log()
    ell = arb(length)
    return (
        2
        * c_bal
        / (arb.pi() ** 2 * ell)
        * (ell.log() + arb.const_euler() + 1 + 2 * arb.const_log2())
        + 8 * c_bal / (21 * arb.pi() ** 2 * ell**3)
    )


def main() -> None:
    h6: dict[str, arb] = {}
    h12: dict[str, arb] = {}
    for label, a in (("minus", A_MINUS), ("zero", A_ZERO), ("plus", A_PLUS)):
        h6[label], p6 = entropy(6, a)
        h12[label], p12 = entropy(12, a)
        assert (p6 - 1).contains(0)
        assert (p12 - 1).contains(0)
        print(f"a_{label}={a}")
        print(f"  H6={h6[label]}")
        print(f"  H12={h12[label]}")
        print(f"  sum_p6={p6}")
        print(f"  sum_p12={p12}")

    j6 = {label: 2 * h6[label] - h12[label] for label in h6}
    delta_j6 = j6["plus"] + j6["minus"] - 2 * j6["zero"]
    weighted = delta_j6 / 12
    delta_h6_over_6 = (h6["plus"] + h6["minus"] - 2 * h6["zero"]) / 6

    assert delta_j6 > arb("0.0027861")
    assert weighted > arb("0.00023217")
    assert delta_h6_over_6 < arb("-0.000748333333333333")

    print("finite first-doubling chord: PASS")
    print(f"Delta_eta_H6_over_6={delta_h6_over_6}")
    print(f"Delta_eta_J6={delta_j6}")
    print(f"Delta_eta_J6_over_12={weighted}")

    for depth in (12, 13):
        tail = sharp_tail(6 * 2**depth)
        full_threshold = delta_h6_over_6 + tail
        after_first = full_threshold - weighted
        assert full_threshold < 0
        print(f"R_sharp_J{depth}={tail}")
        print(f"sufficient_M{depth}_threshold={full_threshold}")
        print(f"sufficient_remaining_after_first_threshold={after_first}")
    print("scope=finite n=6,12 first doubling only; no claim for later dyadic scales")


if __name__ == "__main__":
    main()
