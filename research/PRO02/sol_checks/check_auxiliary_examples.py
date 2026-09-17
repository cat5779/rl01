from fractions import Fraction as F
from itertools import combinations, product


def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def inv2(m):
    d = det2(m)
    return [[m[1][1] / d, -m[0][1] / d], [-m[1][0] / d, m[0][0] / d]]


def determinant(m):
    if len(m) == 1:
        return m[0][0]
    total = F(0)
    for j in range(len(m)):
        minor = [row[:j] + row[j + 1 :] for row in m[1:]]
        total += (-1 if j % 2 else 1) * m[0][j] * determinant(minor)
    return total


def t_potential(x):
    return sum(
        x[i][j] ** 4 / (x[i][i] * x[j][j])
        for i in range(2)
        for j in range(2)
    )


# Section 11.1: exact two-site counterexample.
a = F(1, 40)
c = F(19, 20)
C = [[F(1, 20), None], [None, F(19, 20)]]
off_sq = F(2, 400)

atoms = {
    (0, 0): (1 - C[0][0]) * (1 - C[1][1]) - off_sq,
    (1, 0): C[0][0] * (1 - C[1][1]) + off_sq,
    (0, 1): (1 - C[0][0]) * C[1][1] + off_sq,
    (1, 1): C[0][0] * C[1][1] - off_sq,
}
assert [atoms[b] for b in ((0, 0), (1, 0), (0, 1), (1, 1))] == [
    F(17, 400), F(3, 400), F(363, 400), F(17, 400)
]

# Latent two-site DPP kernel R=(C-aI)/c, represented by its diagonal and |off|^2.
rq = (C[0][0] - a) / c
rr = (C[1][1] - a) / c
roff_sq = off_sq / c**2
latent = {
    (1, 1): rq * rr - roff_sq,
    (1, 0): rq - (rq * rr - roff_sq),
    (0, 1): rr - (rq * rr - roff_sq),
}
latent[(0, 0)] = 1 - sum(latent.values())


def channel_prob(y, x):
    ans = F(1)
    for yi, xi in zip(y, x):
        p = a + c * xi
        ans *= p if yi else 1 - p
    return ans


rhs = F(0)
for y in product((0, 1), repeat=2):
    weights = {x: latent[x] * channel_prob(y, x) for x in latent}
    py = sum(weights.values())
    assert py == atoms[y]
    post = {x: w / py for x, w in weights.items()}
    r0 = sum(w for x, w in post.items() if x[0])
    r1 = sum(w for x, w in post.items() if x[1])
    r11 = post[(1, 1)]
    post_off_sq = r0 * r1 - r11

    # The output mask inverse uses only |off|^2 in its diagonal entries.
    d0 = C[0][0] - (1 - y[0])
    d1 = C[1][1] - (1 - y[1])
    det = d0 * d1 - off_sq
    g00, g11 = d1 / det, d0 / det
    rhs += py * post_off_sq * (
        g00**2 / (r0 * (1 - r0)) + g11**2 / (r1 * (1 - r1))
    )

assert rhs == F(3044288, 4362897)
z = F(400, 689)
log_lower = 2 * sum(z ** (2 * k + 1) / (2 * k + 1) for k in range(8))
rational_subtrahend = 4 * (F(2, 17) + F(1, 3) + F(1, 363))
gap_lower = 2 * log_lower - rational_subtrahend - rhs
assert gap_lower > 0


# Section 11.2: exact three-site reveal and the raw-potential decrement.
eps = F(1, 100)
K = [
    [F(1, 10), -F(1, 5), -F(1, 1000)],
    [-F(1, 5), F(9, 10), -F(3, 1000)],
    [-F(1, 1000), -F(3, 1000), F(1, 2)],
]
lo = [[K[i][j] - (a if i == j else 0) for j in range(3)] for i in range(3)]
hi = [[(F(39, 40) if i == j else 0) - K[i][j] for j in range(3)] for i in range(3)]
for matrix in (lo, hi):
    for size in range(1, 4):
        for idx in combinations(range(3), size):
            principal = [[matrix[i][j] for j in idx] for i in idx]
            assert determinant(principal) > 0

G0 = [[F(2), F(-4)], [F(-4), F(-2)]]
V = [[F(1), F(1)], [F(1), F(1)]]
u = F(12501, 25000)


def add_scaled(x, scale, v):
    return [[x[i][j] + scale * v[i][j] for j in range(2)] for i in range(2)]


x_plus = eps**2 / u
x_minus = -eps**2 / (1 - u)
delta_t = (
    u * t_potential(add_scaled(G0, x_plus, V))
    + (1 - u) * t_potential(add_scaled(G0, x_minus, V))
    - t_potential(G0)
)
quadratic_variation = 4 * (u * x_plus**2 + (1 - u) * x_minus**2)
assert delta_t < 0
assert (-delta_t) / quadratic_variation > 19

assert t_potential(G0) == -120
# Along G0+tV, T(t)=(2+t)^2+(-2+t)^2+2(-4+t)^4/(t^2-4).
# Its exact Taylor coefficients through t^2 are -120, 128, -78.
assert 2 * F(-78) == -156

print(f"11.1_rhs={rhs}")
print(f"11.1_positive_gap_lower={gap_lower}")
print(f"11.2_delta_T={delta_t}")
print(f"11.2_ratio={(-delta_t) / quadratic_variation}")
print("all_exact_checks_passed=true")
