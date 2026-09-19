from decimal import Decimal as D, getcontext

getcontext().prec = 100


def atan_inverse(q: int) -> D:
    qd = D(q)
    total = D(0)
    power = D(1) / qd
    q2 = qd * qd
    sign = D(1)
    k = 0
    while True:
        term = sign * power / (2 * k + 1)
        total += term
        if abs(term) < D("1e-105"):
            return total
        power /= q2
        sign = -sign
        k += 1


def inverse_and_determinant(matrix):
    n = len(matrix)
    table = [row[:] + [D(i == j) for j in range(n)]
             for i, row in enumerate(matrix)]
    determinant = D(1)
    sign = 1
    for j in range(n):
        pivot = max(range(j, n), key=lambda k: abs(table[k][j]))
        if pivot != j:
            table[j], table[pivot] = table[pivot], table[j]
            sign *= -1
        diagonal = table[j][j]
        determinant *= diagonal
        table[j] = [value / diagonal for value in table[j]]
        for k in range(n):
            if k == j:
                continue
            factor = table[k][j]
            table[k] = [left - factor * right
                        for left, right in zip(table[k], table[j])]
    return [row[n:] for row in table], D(sign) * determinant


pi = 16 * atan_inverse(5) - 4 * atan_inverse(239)
t = D(19) / (20 * pi)
masked = [
    [-D("0.5"), t, D(0), -t / 3, D(0)],
    [t, -D("0.5"), t, D(0), -t / 3],
    [D(0), t, -D("0.5"), t, D(0)],
    [-t / 3, D(0), t, D("0.5"), t],
    [D(0), -t / 3, D(0), t, D("0.5")],
]
coupling = [t / 5, D(0), -t / 3, D(0), t]
inverse, determinant = inverse_and_determinant(masked)
inverse_coupling = [
    sum(inverse[i][j] * coupling[j] for j in range(5))
    for i in range(5)
]
q = D("0.5") - sum(coupling[i] * inverse_coupling[i]
                       for i in range(5))
core_sites = [2, 3]
coarse = [[inverse[i][j] for j in core_sites] for i in core_sites]
vector = [inverse_coupling[i] for i in core_sites]


def fine(sign: int):
    denominator = q if sign == 1 else 1 - q
    return [[coarse[i][j] + D(sign) * vector[i] * vector[j] / denominator
             for j in range(2)] for i in range(2)]


def pair_potential(matrix):
    off_diagonal_square = matrix[0][1] ** 2
    diagonal_product = matrix[0][0] * matrix[1][1]
    return (off_diagonal_square
            + (diagonal_product - off_diagonal_square)
            * (D(1) - off_diagonal_square / diagonal_product).ln())


def full_potential(matrix):
    return (matrix[0][0] ** 2 + matrix[1][1] ** 2
            + 2 * pair_potential(matrix))


fine_one, fine_zero = fine(1), fine(-1)
full_gap = (q * full_potential(fine_one)
            + (1 - q) * full_potential(fine_zero)
            - full_potential(coarse))
cross_gap = (q * pair_potential(fine_one)
             + (1 - q) * pair_potential(fine_zero)
             - pair_potential(coarse))
variance = ((vector[0] ** 2 + vector[1] ** 2) ** 2 / (q * (1 - q)))

for name, value in [
    ("observed_probability", -determinant),
    ("q", q),
    ("full_gap", full_gap),
    ("cross_gap", cross_gap),
    ("variance", variance),
    ("payment", -full_gap / variance),
]:
    print(name, f"{value:.60f}")
