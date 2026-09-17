#!/usr/bin/env python3
"""Exact, low-degree cross-layer checks for SA05.
No configuration enumeration, scanning, or hashing.
Uses only k=4 and layers m=2,3,4 as polynomial identities.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as s


def zero(expr: s.Expr, name: str) -> None:
    if s.cancel(s.expand(expr)) != 0:
        raise AssertionError(name)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    x = s.symbols("xi", positive=True)
    k, n = 4, 8
    z, A = 1+1/x, x*(1+x)

    def Q(r: int, d: int) -> s.Expr:
        return sum(s.ff(r,h)*s.rf(r+2*d-1,h)
                   /(s.rf(d,h)*s.factorial(h))*x**h for h in range(r+1))

    def theta(m: int, j: int) -> s.Expr:
        return s.cancel(Q(m-j,k-m+1)/Q(m,k-m+1))

    Z = {m: s.cancel(sum(s.binomial(k,j)*s.binomial(k,m-j)*z**j
                for j in range(m+1))) for m in (2,3,4)}
    eta = {}
    for m in (2,3):
        weights = [s.binomial(k,j)*s.binomial(k,m-j)*z**j/Z[m]
                   for j in range(m+1)]
        mu = s.cancel(sum(j*weights[j] for j in range(m+1)))
        var = s.cancel(sum((j-mu)**2*weights[j] for j in range(m+1)))
        V = s.cancel(k*z+k-m-(z-1)*mu)
        denom = s.cancel(k-m+(m-mu)+x*(n-m))
        eta[m] = s.cancel(A/denom)
        zero((m+1)*Z[m+1]/Z[m]-V, f"kernel mass identity m={m}")
        zero(eta[m]-A*(z-1)/V, f"eta normalization m={m}")
        zero(s.diff(mu,x)+var/A, f"overlap mean derivative m={m}")
        eta_prime = (1+2*x)/denom-(var+A*(n-m))/denom**2
        zero(s.diff(eta[m],x)-eta_prime, f"eta moving derivative m={m}")
        for j in range(m+1):
            zero(theta(m+1,j)-theta(m,j)-eta[m]*s.diff(theta(m,j),x),
                 f"all available contiguous modes m={m}, j={j}")
        xm = -eta[m]*s.diff(theta(m,2),x)/theta(m,2)
        zero(theta(m+1,2)/theta(m,2)-(1-xm),
             f"matched clock ratio m={m}")
        xmid = s.cancel(xm.subs(x,s.Rational(1,1520)))
        assert 0 < xmid < 1

    for j in range(3):
        y = theta(2,j)
        composed = (y+(eta[2]+eta[3]+eta[3]*s.diff(eta[2],x))*s.diff(y,x)
                    +eta[2]*eta[3]*s.diff(y,x,2))
        zero(theta(4,j)-composed, f"two-step second-jet identity j={j}")

    xs = s.Rational(1,1520)
    chi_const = 1/(20*xs**2)
    M = 4*(1+xs)/xs
    zero(chi_const-115520, "chi-square constant")
    zero(M-6084, "fixed-mode scale constant")
    results = {
        "status": "EXACT_PASS",
        "n": 8,
        "layers": [2,3,4],
        "configuration_enumeration": False,
        "kernel_normalization": "EXACT_PASS",
        "contiguous_mode_identity": "EXACT_PASS",
        "moving_eta_derivative": "EXACT_PASS",
        "two_step_second_jet_identity": "EXACT_PASS",
        "matched_clock_ratio": "EXACT_PASS",
        "static_chi_square_constant": str(chi_const),
        "fixed_mode_M_constant": str(M),
        "not_proved_by_this_check": [
            "all-n asymptotic entropy bridge",
            "sign or scale of cross-layer second KL differences"
        ]
    }
    text = json.dumps(results, ensure_ascii=False, indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
