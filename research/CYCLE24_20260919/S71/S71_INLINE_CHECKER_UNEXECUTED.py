#!/usr/bin/env python3
"""Exact checks for the AFFINE-MIXTURE obstruction, not the actual kernel path."""

from fractions import Fraction as F
from math import factorial
import json


def positive_exp_partial_sum(x: int, degree: int) -> F:
    return sum(
        (F(x**k, factorial(k)) for k in range(degree + 1)),
        F(0),
    )


def main() -> None:
    c = F(19, 20)
    a0, a1 = F(1, 50), F(3, 100)
    rho, weight = F(1, 2), F(1, 2)
    block_length = 20000
    delta = a1 - a0

    assert 0 < a0 < a1 < 1 - c

    mean0, mean1 = a0 + c * rho, a1 + c * rho
    variance_bulk0 = mean0 * (1 - mean0) - c * c / 4
    variance_bulk1 = mean1 * (1 - mean1) - c * c / 4
    assert variance_bulk0 == variance_bulk1 == F(487, 20000)

    # Positive Taylor remainders then prove log(20)<3 and log(20000)<10.
    assert positive_exp_partial_sum(3, 8) > 20
    assert positive_exp_partial_sum(10, 21) > 20000

    # Analytic ingredients in the report:
    # pi>3 and D_L <= (log(L)+4)/pi^2 < 14/9.
    variance_upper = (
        block_length * variance_bulk0 + c * c * F(14, 9)
    )
    error_upper = (
        4 * variance_upper / (block_length**2 * delta**2)
    )

    assert variance_upper == F(879127, 1800)
    assert error_upper == F(879127, 18000000)
    assert error_upper < F(1, 20)

    # The report proves log(2)>1/2 and hb(1/20)<1/5.
    gap_lower = F(1, 2) - 2 * F(1, 5)
    assert gap_lower == F(1, 10)

    pair_covariance = weight * (1 - weight) * delta**2
    assert pair_covariance == F(1, 40000)

    print(json.dumps({
        "object": "Affine mixture of actual endpoint sine laws",
        "not_the_object": "Actual intermediate kernel-shift DPP",
        "block_lengths": [block_length, block_length],
        "count_variance_strict_upper": str(variance_upper),
        "classification_error_strict_upper": str(error_upper),
        "MI_chord_gap_strict_lower_nats": str(gap_lower),
        "same_parity_covariance_in_mixture": str(pair_covariance),
        "original_all_size_conjecture": "UNRESOLVED",
    }, indent=2))


if __name__ == "__main__":
    main()
