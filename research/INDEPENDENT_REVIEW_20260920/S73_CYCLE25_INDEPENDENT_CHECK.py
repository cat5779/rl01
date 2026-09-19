#!/usr/bin/env python3
"""Independent standard-library checks for the S73 Cycle25 audit.

This is deliberately not a copy of ``s73_checks.py``.  It reconstructs the
four-site midpoint certificate from exact second-order jets and checks the
two rational endpoints used by the corrected diagonal-baseline range.
Floating-point/Decimal values below are diagnostics; exact signs are printed
from Fraction comparisons.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
import itertools


getcontext().prec = 80


def dfrac(x: Fraction) -> Decimal:
    return Decimal(x.numerator) / Decimal(x.denominator)


def mul_jet(j1, j2):
    """Multiply (value, first derivative, second derivative) jets exactly."""
    x, x1, x2 = j1
    y, y1, y2 = j2
    return x * y, x1 * y + x * y1, x2 * y + 2 * x1 * y1 + x * y2


def determinant(matrix):
    """Exact determinant over Fraction via permutation expansion (tiny only)."""
    n = len(matrix)
    if n == 0:
        return Fraction(1)
    total = Fraction(0)
    for perm in itertools.permutations(range(n)):
        inversions = sum(
            perm[i] > perm[j] for i in range(n) for j in range(i + 1, n)
        )
        term = Fraction(-1 if inversions % 2 else 1)
        for i, j in enumerate(perm):
            term *= matrix[i][j]
        total += term
    return total


def principal(matrix, indices):
    return [[matrix[i][j] for j in indices] for i in indices]


def subsets(n):
    return [
        tuple(i for i in range(n) if mask & (1 << i))
        for mask in range(1 << n)
    ]


def finite_disintegration_check():
    """Exact m=2 diagnostic for Theorem 2.1 and exterior bistochasticity."""
    u = [[Fraction(3, 5), Fraction(4, 5)],
         [Fraction(4, 5), Fraction(-3, 5)]]
    m = 2
    ident = [[Fraction(i == j) for j in range(m)] for i in range(m)]
    qblock = [
        [
            (ident[i][j] if i < m and j < m else
             u[i][j - m] if i < m <= j else
             u[j][i - m] if j < m <= i else
             ident[i - m][j - m]) / 2
            for j in range(2 * m)
        ]
        for i in range(2 * m)
    ]

    for aset in subsets(m):
        for bset in subsets(m):
            lhs = Fraction(0)
            for x in itertools.product((0, 1), repeat=m):
                if any(x[i] == 0 for i in aset):
                    continue
                px = [
                    [
                        sum(u[k][i] * (1 - x[k]) * u[k][j] for k in range(m))
                        for j in range(m)
                    ]
                    for i in range(m)
                ]
                lhs += Fraction(1, 2**m) * determinant(principal(px, bset))
            combined = aset + tuple(m + j for j in bset)
            rhs = determinant(principal(qblock, combined))
            assert lhs == rhs

    words = list(itertools.product((0, 1), repeat=m))
    channel = [[Fraction(0) for _ in words] for _ in words]
    for iz, z in enumerate(words):
        zset = tuple(i for i, bit in enumerate(z) if bit)
        for it, t in enumerate(words):
            tset = tuple(i for i, bit in enumerate(t) if bit)
            if len(zset) != len(tset):
                continue
            minor = [[u[i][j] for j in tset] for i in zset]
            channel[iz][it] = determinant(minor) ** 2
    assert all(sum(row) == 1 for row in channel)
    assert all(sum(channel[i][j] for i in range(len(words))) == 1 for j in range(len(words)))
    return len(subsets(m)) ** 2, len(words)


def entropy_second_zero_score(atoms):
    """Entropy second derivative when every supplied atom has zero score."""
    total = Decimal(0)
    for value, first, second in atoms:
        assert first == 0
        total -= dfrac(second) * dfrac(value).ln()
    return total


def four_site_midpoint(c: Fraction):
    r = (1 - c * c) / 4
    s = (1 + c * c) / 4

    # At a=(1-c)/2: u=v=r, q=s; u'=1, v'=-1, q'=0;
    # u''=v''=2, q''=-2.
    u = (r, Fraction(1), Fraction(2))
    v = (r, Fraction(-1), Fraction(2))
    q = (s, Fraction(0), Fraction(-2))
    uv = mul_jet(u, v)
    qq = mul_jet(q, q)
    mixed = tuple((uv[i] + qq[i]) / 2 for i in range(3))

    assert uv[1] == qq[1] == mixed[1] == 0
    assert uv[2] == qq[2] == mixed[2] == -4 * s

    # Two y-words are changed.  Each has input atoms uv,q^2 and two output
    # atoms equal to their average.
    hin_changed = entropy_second_zero_score([uv, qq, uv, qq])
    hout_changed = entropy_second_zero_score([mixed] * 4)
    gain_direct = hout_changed - hin_changed

    ratio = (r * r + s * s) ** 2 / (4 * r * r * s * s)
    gain_formula = dfrac(8 * s) * dfrac(ratio).ln()
    assert ratio > 1
    assert abs(gain_direct - gain_formula) < Decimal("1e-70")

    # The unchanged atoms cancel in the gain.  The complete two-pair input
    # curvature and output curvature are reconstructed independently.
    hpair = Decimal(4) * (dfrac(s) / dfrac(r)).ln() - Decimal(2) / dfrac(r)
    hin_total = Decimal(2) * hpair
    hout_total = hin_total + gain_direct

    return r, s, ratio, gain_direct, hin_total, hout_total


def main():
    correlation_checks, channel_size = finite_disintegration_check()
    print("FINITE DISINTEGRATION/EXTERIOR-CHANNEL DIAGNOSTIC")
    print("exact inclusion-correlation identities checked =", correlation_checks)
    print("exact doubly-stochastic channel size =", channel_size, "x", channel_size)

    c = Fraction(19, 20)
    r, s, ratio, gain, hin, hout = four_site_midpoint(c)
    print("INDEPENDENT FOUR-SITE MIDPOINT CHECK")
    print("c =", c, "a =", (1 - c) / 2)
    print("r =", r, "s =", s)
    print("ratio =", ratio)
    print("exact gain sign =", ratio.numerator > ratio.denominator)
    print("G'' =", gain)
    print("H_in'' =", hin)
    print("H_out'' =", hout)
    assert gain > 0
    assert hout < 0

    c_lo = Fraction(37, 40)
    c_hi = Fraction(74, 77)
    b_half_lo = (1 - c_lo * c_lo) / 2
    alpha_sup_hi = c_hi / (2 - c_hi)
    print("\nEXACT DIAGONAL-BASELINE ENDPOINTS")
    print("b(1/2; c=37/40) =", b_half_lo, "< 3/40 =", b_half_lo < Fraction(3, 40))
    print("sup alpha(c=74/77) =", alpha_sup_hi, "= 37/40 =", alpha_sup_hi == Fraction(37, 40))
    assert b_half_lo < Fraction(3, 40)
    assert alpha_sup_hi == Fraction(37, 40)

    # Diagnostic only: sample the analytic all-c expression from Theorem 8.2.
    worst = None
    for k in range(1, 1000):
        cc = Decimal(k) / Decimal(1000)
        x = (1 + cc * cc) / (1 - cc * cc)
        total = (
            Decimal(8) * x.ln()
            - Decimal(8) * (1 + x)
            + Decimal(8) * x / (1 + x) * ((x * x + 1) / (2 * x)).ln()
        )
        worst = total if worst is None else max(worst, total)
        assert total < 0
    print("sampled all-c maximum H_out'' =", worst)
    print("sample grid is diagnostic; the strict all-c sign uses the analytic inequalities in the review")

    print("\nNORMALIZATION INTERFACE")
    print("n=2m and H_st=-I_st, so v=lim I_st/(2m), not an unnormalized finite I_st bound")


if __name__ == "__main__":
    main()
