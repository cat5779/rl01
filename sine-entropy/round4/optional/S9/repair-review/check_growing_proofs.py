"""Independent bounded checks for the S9 growing-radius proof constants.

This does not enumerate DPP configurations and does not reproduce the omitted
author helper.  It checks the rational reductions used in Theorem A and the
integrated prefactor in LAYER_MEASURE (M2).
"""

from fractions import Fraction as Q


def exp_lower(x: Q, terms: int) -> Q:
    term = Q(1)
    total = term
    for n in range(1, terms):
        term *= x / n
        total += term
    return total


def atan_interval(x: Q, terms: int) -> tuple[Q, Q]:
    total = Q(0)
    for n in range(terms):
        total += (-1 if n % 2 else 1) * x ** (2 * n + 1) / (2 * n + 1)
    next_term = (-1 if terms % 2 else 1) * x ** (2 * terms + 1) / (2 * terms + 1)
    return (total, total + next_term) if next_term > 0 else (total + next_term, total)


def main() -> None:
    # Machin intervals: pi = 16 atan(1/5) - 4 atan(1/239).
    a5_lo, a5_hi = atan_interval(Q(1, 5), 20)
    a239_lo, a239_hi = atan_interval(Q(1, 239), 6)
    pi_lo = 16 * a5_lo - 4 * a239_hi
    pi_hi = 16 * a5_hi - 4 * a239_lo
    assert Q(3) < pi_lo < pi_hi < Q(22, 7)
    assert pi_hi < Q(81, 25)  # hence sqrt(pi) < 9/5

    # Elementary exponential certificates used to upper-bound logarithms/tails.
    assert exp_lower(Q(70, 19), 20) > 39       # (19/40) log 39 < 7/4
    assert exp_lower(Q(175, 33), 24) > 199     # (99/200) log 199 < 21/8
    assert exp_lower(Q(9), 32) > 8000
    assert exp_lower(Q(24), 48) > 10**10

    # Conservative endpoint substitutions in (14d).
    W = Q(301, 100)
    sqrt_pi = Q(9, 5)
    d = Q(1, 50)
    sqrt_R = Q(400)
    R_floor = sqrt_R**2
    L1 = (W**2 + 1 + sqrt_pi * W) / (8 * R_floor * d**2)
    L2 = (W**3 / 3 + W + sqrt_pi * (Q(1, 4) + W**2 / 2)) / (
        8 * d**3 * sqrt_R**3
    )
    L3 = (W**4 + 2 + 6 * W**2 + sqrt_pi * (3 * W + 2 * W**3)) / (
        64 * R_floor**2 * d**4
    )
    assert L1 == Q(154781, 5120000)
    assert L2 == Q(62113171, 12288000000)
    assert L3 == Q(25287525561, 26214400000000)

    endpoint = (4 * L1 + 364 * L2 + 8281 * L3) / 1875 + Q(21, 16 * 10**10)
    stated_endpoint = Q(782426604667123, 147456000000000000)
    assert endpoint == stated_endpoint

    # The monotone midpoint lower bound is smallest at R=160001.
    R0 = 160001
    midpoint = 4 * (Q(19, 20) * Q(7, 22) * Q(R0, R0 + 1)) ** 4 * (
        1 - Q(1, (R0 + 1) ** 4)
    )
    assert midpoint > Q(1, 30)

    final_margin = endpoint - Q(1, 30) + Q(7, 32000)
    stated_margin = -Q(4100517395332877, 147456000000000000)
    assert final_margin == stated_margin < -Q(1, 40)

    # The tail separation in section 4.6 follows already from sqrt(R)>=400:
    # d sqrt(R) - W_R >= 400/50 - 3 - 1/400 = 1999/400 > 499/100.
    tail_distance = Q(400, 50) - 3 - Q(1, 400)
    assert tail_distance > Q(499, 100)
    assert tail_distance**2 > 24

    # M2: integral_{1/N}^1 u^2 du/u = (1-N^-2)/2 <= 1/2.
    N = 160002
    integrated_factor = (1 - Q(1, N**2)) / 2
    assert 0 < integrated_factor <= Q(1, 2)

    print("PASS_INDEPENDENT_GROWING_PROOF_CHECKS")
    print(f"endpoint_upper={endpoint}")
    print(f"midpoint_lower_at_R0={midpoint}")
    print(f"band_margin={final_margin}")
    print(f"m2_integrated_factor={integrated_factor}")


if __name__ == "__main__":
    main()
