#!/usr/bin/env python3
"""Exact/rational and Arb verification for S67's PROVED, non-closing bounds.

Requirements: Python 3.10+, python-flint. No network, hashes, or manifests.
The mathematical proof is in S67_ACCELERATION_RESULT.md. This program checks
its rational sign certificates and evaluates its explicit constants outwardly.
It does not certify entropy-rate concavity or re-run the accepted n=16 input.
"""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path
from flint import arb, ctx


def ar(x: F | int) -> arb:
    x = F(x)
    return arb(x.numerator) / arb(x.denominator)


def positive(x: arb, label: str) -> None:
    if not (x > 0):
        raise AssertionError(f"Could not certify positivity: {label}: {x}")


def p(r: F) -> F:
    return -2*r**3 + 51283*r**2 - 384800*r + 528000


def w(r: F) -> F:
    return (r-1)*(41*r+400)/(r*(r+440))


def run(prec: int) -> dict:
    ctx.prec = prec
    # Binary comparison J <= (3/2) W for conditional odds in [1/20,20].
    # phi' has sign p. p decreases then increases on [1,400].
    assert p(F(1)) > 0 and p(F(2)) < 0
    assert p(F(569,100)) < 0 and p(F(57,10)) > 0
    assert p(F(400)) > 0
    assert -6+102566-384800 < 0
    assert -6*400**2+102566*400-384800 > 0
    assert 102566-12*400 > 0  # p'' positive on [1,400]
    rational_minimum = F(3,2)*w(F(569,100)) - F(7,4)
    assert rational_minimum > 0
    exp_lower = sum((F(7,4)**k)/factorial(k) for k in range(7))
    assert exp_lower > F(57,10)  # log(5.7) < 7/4

    c, b, s = F(19,20), F(1,40), F(39,1600)
    eta, M, R = F(39,800), F(761,39), F(49,39)
    assert s == b*(1-b)
    assert eta == 1/(1+M)
    assert M == (1+c*c)/(1-c*c) and M < 20
    assert R == (1-F(1,50))/(39*F(1,50))

    # Explicit weighted Schur bound: alpha=1/40, theta=1/1000.
    theta = F(1,1000)
    commutator_bound = F(19,30)*theta*(2/(F(1,2)-theta)**2+11)
    assert commutator_bound == F(90041209,7470030000)
    assert commutator_bound < F(1,80)
    assert 1/(b-commutator_bound) < 80

    # Exact antiderivatives for the all-volume acceleration bound.
    a0, a1, kappa = F(1,50), F(3,100), F(3,2)
    def f1(x: F) -> arb:
        ax = ar(x)
        return ((1+ar(a0))*ax-ax*ax/2-ar(a0)*ax.log())/39
    def f3(x: F) -> arb:
        ax = ar(x)
        return (ar(a0)/(2*ax*ax)-(1+3*ar(a0))/ax
                -3*(1+ar(a0))*ax.log()+(3+ar(a0))*ax-ax*ax/2)/(39**3)
    I1, I3 = f1(b)-f1(a0), f3(b)-f3(a0)
    positive(I1, 'I1'); positive(I3, 'I3')
    C_bound = ar(kappa)*(I3/ar(s)-4*I1)
    positive(C_bound, 'uniform C/n upper bound')
    assert C_bound < ar(F(887,1_000_000))

    # Accepted source intervals. Endpoints are exact decimal rationals.
    Blo = F('0.000104188037840358653653185471')
    Bhi = F('0.000104188037840358653653185472')
    glo = F('0.000141743962555442975188447184')
    ghi = F('0.000141743962555442975188447185')
    Clo = F('0.000146680480325883947552193048')
    Chi = F('0.000146680480325883947552193049')
    budget_lo, budget_hi = Blo+glo, Bhi+ghi
    C_cap_lo, C_cap_hi = budget_lo+Clo, budget_hi+Chi
    A_bound = C_bound-ar(Clo)
    excess = C_bound-ar(C_cap_hi)
    positive(excess, 'remaining excess: this method does NOT close the chord')
    assert A_bound < ar(F('0.000740319519674116052447806952'))
    # The factor-1 hypothetical, by itself, still does not pay this interface.
    positive(C_bound/ar(kappa)-ar(C_cap_hi), 'even kappa=1 alone is insufficient')

    coarse = ar(kappa)/40000*((2+ar(R)**3)/(6*ar(s))-2)
    assert C_bound < coarse
    return {
        'status': 'PASS: analytic bounds verified; entropy-rate target INCOMPLETE',
        'precision_bits': prec,
        'binary_comparison_constant': '3/2',
        'binary_critical_point_positive_margin_rational': str(rational_minimum),
        'exp_7_over_4_partial_sum_0_to_6': str(exp_lower),
        'conditional_odds_bound': str(M),
        'conditional_probability_lower_bound': str(eta),
        'endpoint_odds_stability_factor': str(R),
        'weighted_commutator_upper_bound': str(commutator_bound),
        'weighted_inverse_norm_upper_bound': '80',
        'weighted_column_square_upper_bound': '6400',
        'resolvent_tail_power': '1/500',
        'local_interaction_error_coefficient': '204800000',
        'local_interaction_error_power': '1/1000',
        'I1_arb': str(I1),
        'I3_arb': str(I3),
        'uniform_C_over_n_bound_arb': str(C_bound),
        'uniform_A_n_bound_arb': str(A_bound),
        'accepted_gamma_plus_B_interval': [str(budget_lo), str(budget_hi)],
        'required_C_over_n_cap_interval': [str(C_cap_lo), str(C_cap_hi)],
        'bound_excess_over_required_cap_arb': str(excess),
        'coarse_secant_C_bound_arb': str(coarse),
        'negative_entropy_rate_chord_lower_bound_arb': str(ar(C_cap_lo)-C_bound),
        'warning': 'Upper bounds, not estimates of the true acceleration. No positive rate chord is proved.'
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--precision', type=int, default=192)
    ap.add_argument('--output', type=Path)
    args = ap.parse_args()
    if args.precision < 96:
        ap.error('Use at least 96 bits to make cancellation in the antiderivatives harmless.')
    result = run(args.precision)
    text = json.dumps(result, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text+'\n')
    print(text)

if __name__ == '__main__':
    main()
