#!/usr/bin/env python3
"""Independent checks for the S74 Cycle26 review.

This uses only the Python standard library.  It is not an interval proof: the
six-site calculations are 80-digit Decimal diagnostics, kept separate from
the exact rational checks of the published constants.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
import itertools


getcontext().prec = 90
D = Decimal


def arctan_inv(n: int, terms: int = 150) -> Decimal:
    x = D(1) / D(n)
    x2 = x * x
    power = x
    total = D(0)
    sign = 1
    for k in range(terms):
        term = power / D(2 * k + 1)
        total = total + term if sign > 0 else total - term
        power *= x2
        sign = -sign
    return total


PI = 16 * arctan_inv(5) - 4 * arctan_inv(239)


def determinant(matrix):
    n = len(matrix)
    if n == 0:
        return D(1)
    a = [row[:] for row in matrix]
    out = D(1)
    sign = 1
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(a[row][col]))
        if a[pivot][col] == 0:
            return D(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            sign = -sign
        p = a[col][col]
        out *= p
        for row in range(col + 1, n):
            factor = a[row][col] / p
            for j in range(col + 1, n):
                a[row][j] -= factor * a[col][j]
    return out if sign > 0 else -out


def principal(matrix, keep):
    return [[matrix[i][j] for j in keep] for i in keep]


def atom(kernel, word):
    n = len(word)
    masked = [row[:] for row in kernel]
    zeros = 0
    for i, bit in enumerate(word):
        if not bit:
            masked[i][i] -= 1
            zeros += 1
    value = determinant(masked)
    return -value if zeros % 2 else value


def delete_tuple(word, deleted):
    deleted = set(deleted)
    return tuple(bit for i, bit in enumerate(word) if i not in deleted)


def atom_derivatives(kernel, word):
    n = len(word)
    p = atom(kernel, word)
    first = []
    for i in range(n):
        keep = tuple(j for j in range(n) if j != i)
        first.append((2 * word[i] - 1) * atom(principal(kernel, keep), delete_tuple(word, (i,))))
    second = {}
    for i in range(n):
        for j in range(i + 1, n):
            keep = tuple(k for k in range(n) if k not in (i, j))
            second[i, j] = (
                (2 * word[i] - 1)
                * (2 * word[j] - 1)
                * atom(principal(kernel, keep), delete_tuple(word, (i, j)))
            )
    return p, first, second


def sine_kernel(n=6):
    beta = D(19) / (D(20) * PI)
    kernel = [[D(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        kernel[i][i] = D(1) / 2
        for j in range(i):
            r = i - j
            if r % 2:
                sign = 1 if ((r - 1) // 2) % 2 == 0 else -1
                kernel[i][j] = kernel[j][i] = D(sign) * beta / D(r)
    return kernel


def law_with_jets(kernel):
    n = len(kernel)
    data = {}
    for word in itertools.product((0, 1), repeat=n):
        data[word] = atom_derivatives(kernel, word)
    return data


def six_site_diagnostic():
    kernel = sine_kernel(6)
    data = law_with_jets(kernel)
    total = sum(item[0] for item in data.values())
    min_p = min(item[0] for item in data.values())
    assert abs(total - 1) < D("1e-80")
    assert min_p > 0

    mixed = D(0)
    fisher_joint = D(0)
    c_acc = D(0)
    marg_a = {}
    marg_b = {}
    for word, (p, first, second) in data.items():
        ya, yb = word[:3], word[3:]
        marg_a[ya] = marg_a.get(ya, D(0)) + p
        marg_b[yb] = marg_b.get(yb, D(0)) + p
        mixed += first[0] * first[5] / p + second[0, 5] * p.ln()
        p1 = sum(first)
        p2 = 2 * sum(second.values())
        fisher_joint += p1 * p1 / p
        # c_acc is completed after the marginal atoms are available.

    data_a = law_with_jets(principal(kernel, (0, 1, 2)))
    data_b = law_with_jets(principal(kernel, (3, 4, 5)))
    fisher_a = sum(sum(v[1]) ** 2 / v[0] for v in data_a.values())
    fisher_b = sum(sum(v[1]) ** 2 / v[0] for v in data_b.values())
    d_f = fisher_joint - fisher_a - fisher_b

    for word, (p, first, second) in data.items():
        p2 = 2 * sum(second.values())
        c_acc += p2 * (p / (marg_a[word[:3]] * marg_b[word[3:]])).ln()

    return total, min_p, mixed, d_f, c_acc, d_f + c_acc


def rational_constants():
    delta = Fraction(1, 50)
    r = delta / (1 - delta)
    ell = 2 / (r * r * delta) + 1 / (r**5 * delta**2) + 1 / (r**6 * delta**3)
    b = 4 * ell / delta**3 + 2 / (r**4 * delta**4)
    coarse = 6 * delta**-12
    product_kappa = 4 - 3 * Fraction(19, 20) ** 2 * 50**12 * Fraction(1, 10**21)
    assert product_kappa == Fraction(27353, 8192)
    assert b <= coarse
    return b, coarse, product_kappa


def toeplitz_q_half(n):
    out = [[D(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        out[i][i] = D(1) / 2
        for j in range(i):
            r = i - j
            if r % 2:
                sign = 1 if ((r - 1) // 2) % 2 == 0 else -1
                value = D(sign) / (PI * D(r))
            else:
                value = D(0)
            out[i][j] = out[j][i] = value
    return out


def hs_cut(q, left, right):
    return sum(q[i][j] * q[i][j] for i in left for j in right)


def trace_square(q):
    return sum(value * value for row in q for value in row)


def merge_tree_diagnostic():
    # Four adjacent leaves of length two; balanced binary merge tree.
    q = toeplitz_q_half(8)
    leaves = [tuple(range(0, 2)), tuple(range(2, 4)), tuple(range(4, 6)), tuple(range(6, 8))]
    cuts = [
        (leaves[0], leaves[1]),
        (leaves[2], leaves[3]),
        (leaves[0] + leaves[1], leaves[2] + leaves[3]),
    ]
    charged = sum(hs_cut(q, a, b) for a, b in cuts)
    q2 = principal(q, (0, 1))
    rhs = (trace_square(q) - 4 * trace_square(q2)) / 2
    assert abs(charged - rhs) < D("1e-80")
    return charged, rhs


def main():
    b, coarse, product_kappa = rational_constants()
    b_dec = D(b.numerator) / D(b.denominator)
    print("EXACT RATIONAL CONSTANTS")
    print("B_(1/50) =", b)
    print("B_(1/50) decimal =", b_dec)
    print("6 delta^-12 =", coarse)
    print("product kappa lower bound =", product_kappa)
    print("chord coefficient =", product_kappa / 2)

    c = D(19) / 20
    d = c * c / (PI * PI)
    seed_c = D(2) / (D(1) / 4 - d) + D(4) * (
        (D(1) / 4 - d) / (D(1) / 4 + d)
    ).ln() - D(8)
    leakage_two = D(1) / 2 - D(2) / (PI * PI)
    kappa_two = (D(8) + seed_c) / 2 - b_dec * c * c * leakage_two / 4
    print("two-site half-density kappa candidate =", kappa_two)

    charged, rhs = merge_tree_diagnostic()
    print("\nMERGE-TREE DIAGNOSTIC")
    print("sum cut HS^2 =", charged)
    print("half trace-square difference =", rhs)

    total, min_p, mixed, d_f, c_acc, m2 = six_site_diagnostic()
    print("\nSIX-SITE 80-DIGIT DIAGNOSTIC (NOT AN INTERVAL CERTIFICATE)")
    print("probability sum =", total)
    print("minimum atom =", min_p)
    print("mixed coordinate M_1,6 =", mixed)
    print("D_F =", d_f)
    print("C_acc =", c_acc)
    print("M_3,3'' =", m2)
    assert mixed < 0
    assert c_acc < 0
    assert m2 > 0


if __name__ == "__main__":
    main()
