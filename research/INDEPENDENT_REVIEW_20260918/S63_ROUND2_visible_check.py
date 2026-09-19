"""Checks the exact rational certificate visible in the S63 Round-2 manuscript.

This does not validate the missing 256-pair witness, interval source code,
or the provenance of the displayed polynomial coefficient intervals.
"""

from fractions import Fraction as F
from math import comb, factorial


LOWER = [
    1776012226,
    -82943302,
    -14608797,
    -290978,
    1734,
    -1,
    -1,
    0,
    0,
    -1,
]
UPPER = [
    1776012227,
    -82943301,
    -14608796,
    -290977,
    1735,
    0,
    0,
    1,
    1,
    0,
]
CLAIMED_BERNSTEIN_FLOORS = [
    29091,
    47114,
    61938,
    73573,
    82033,
    87328,
    89474,
    88485,
    84380,
    77175,
    66890,
    53546,
]


def add(left, right):
    size = max(len(left), len(right))
    return [
        (left[i] if i < len(left) else F(0))
        + (right[i] if i < len(right) else F(0))
        for i in range(size)
    ]


def scale(poly, scalar):
    return [scalar * value for value in poly]


def multiply(left, right):
    result = [F(0) for _ in range(len(left) + len(right) - 1)]
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return result


def power(poly, exponent):
    result = [F(1)]
    for _ in range(exponent):
        result = multiply(result, poly)
    return result


def main():
    selected = [
        F(LOWER[k] if k % 2 == 0 else UPPER[k], 10**8)
        for k in range(10)
    ]

    # a = 21/1000 + (3/1000)x, t = 200a - 5 = -4/5 + (3/5)x.
    a = [F(21, 1000), F(3, 1000)]
    t = [F(-4, 5), F(3, 5)]

    p_lower_minus_margin = [F(-1, 10**6) - F(1, 25)]
    for k, coefficient in enumerate(selected):
        p_lower_minus_margin = add(
            p_lower_minus_margin,
            scale(power(t, k), coefficient),
        )

    c = F(19, 20)
    one = [F(1)]
    beta0 = multiply(a, add(one, scale(a, -1)))
    beta1 = multiply(add(a, [c]), add([F(1) - c], scale(a, -1)))
    denominator = multiply(beta0, beta1)
    c0_minus_one = add([F(261, 200) - 1], scale(a, F(51, 10)))
    weighted_beta = add(scale(beta1, F(2, 3)), scale(beta0, F(1, 3)))

    polynomial = add(
        multiply(denominator, p_lower_minus_margin),
        scale(multiply(c0_minus_one, weighted_beta), -1),
    )
    while polynomial and polynomial[-1] == 0:
        polynomial.pop()

    degree = len(polynomial) - 1
    assert degree == 11
    bernstein = [
        sum(
            polynomial[i] * F(comb(k, i), comb(degree, i))
            for i in range(k + 1)
        )
        for k in range(degree + 1)
    ]
    floors = [
        value.numerator * 10**9 // value.denominator
        for value in bernstein
    ]
    assert floors == CLAIMED_BERNSTEIN_FLOORS
    assert all(value > F(1, 40000) for value in bernstein)

    absolute_bound = F(1, 10**6)
    for k in range(10):
        endpoint_magnitude = max(abs(LOWER[k]), abs(UPPER[k]))
        absolute_bound += F(endpoint_magnitude, 10**8) * F(4, 5) ** k
    assert absolute_bound < 19

    tail = (
        F(1550)
        * F(11, 50) ** 9
        / factorial(9)
        / (1 - F(11, 500))
    )
    assert tail < F(1, 10**8)

    print("VISIBLE_RATIONAL_CERTIFICATE_OK")
    print("degree:", degree)
    print("bernstein_floor_numerators_1e9:", " ".join(map(str, floors)))
    print("minimum_bernstein_coefficient:", min(bernstein))
    print("absolute_P_bound:", absolute_bound)
    print("nilpotent_tail_bound:", tail)


if __name__ == "__main__":
    main()
