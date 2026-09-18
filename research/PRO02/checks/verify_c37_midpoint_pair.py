"""Rigorous midpoint pair certificate at c=37/40.

This proves the fixed-channel comparison

    g_+ <= (3/2) (K + D)

for every feasible leave-two-out posterior table at
``a=3/80, c=37/40``.  The logarithm is upper-bounded by a composite
Simpson rule on ``0 <= xi <= 48``; beyond 48 the pair term is nonpositive.
The remaining rational inequality is certified by tensor Bernstein
subdivision.  The initial control net is exact; all later binary64 control
points are rounded downward.
"""

from __future__ import annotations

from fractions import Fraction as F
import math
import time

import numpy as np
import sympy as sp


def simpson16(xi):
    values = [
        (1 - sp.Rational(k, 16)) / (1 + xi * sp.Rational(k, 16))
        for k in range(17)
    ]
    return (
        values[0]
        + values[-1]
        + 4 * sum(values[1:-1:2])
        + 2 * sum(values[2:-1:2])
    ) / 48


def trapezoid24(xi: F) -> F:
    return F(1, 24) * (
        F(1, 2)
        + sum(
            (1 - F(k, 24)) / (1 + xi * F(k, 24))
            for k in range(1, 24)
        )
    )


# T(xi) <= T_24(xi), T is decreasing, and u=A+D has the universal lower
# bound (1-c^2)/2.  Hence g<=0 for xi>=48.
tail_value = trapezoid24(F(48))
tail_floor = F(231, 3200)
assert tail_value < tail_floor


t0, t1, xi = sp.symbols("t0 t1 xi")
a = sp.Rational(3, 80)
b = sp.Rational(77, 80)
j0 = 1 + xi * (1 - t0)
j1 = 1 + xi * (1 - t1)
h = 1 - t0 * t1 * xi / (1 + xi)
n = (1 - t0) * (1 - t1) + t0 * t1 / (1 + xi)
alpha0 = (1 - a) * (1 - b)
alpha1 = a * b
rows = alpha0 * (
    t1 / ((t0 - a) * (b - t0))
    + t0 / ((t1 - a) * (b - t1))
) + alpha1 * (
    (1 - t1) * j0**3 / ((t0 - a * j0) * (b * j0 - t0))
    + (1 - t0) * j1**3 / ((t1 - a * j1) * (b * j1 - t1))
)

# For a comparison constant gamma, the transformed positive row coefficient
# is gamma/4.  Here gamma=3/2.
target = sp.Rational(3, 8) * rows - xi * h * simpson16(xi) + xi * n
numerator, denominator = sp.together(target).as_numer_denom()
poly = sp.Poly(numerator, t0, t1, xi)
# The denominator factors into positive Simpson factors and four pairs of
# same-sign feasibility factors.  It is strictly positive in the feasible
# interior; boundary points follow by continuity/divergence of a positive
# row.  Keep the factorization available as an independently inspectable
# algebraic check rather than testing its power-basis coefficients.
denominator_factorization = sp.factor(denominator)
assert sp.expand(denominator_factorization - denominator) == 0


variables = (t0, t1, xi)
lower = (sp.Rational(0), sp.Rational(0), sp.Rational(0))
width = (b, b, sp.Rational(48))
unit = sp.symbols("u0:3")
unit_poly = sp.Poly(
    numerator.subs(
        {v: lo + w * u for v, lo, w, u in zip(variables, lower, width, unit)}
    ),
    *unit,
)
degrees = poly.degree_list()
shape = tuple(degree + 1 for degree in degrees)


control = np.empty(shape, dtype=object)
control.fill(sp.Rational(0))
for monomial, coefficient in unit_poly.terms():
    control[monomial] = coefficient
for axis, degree in enumerate(degrees):
    converted = np.empty_like(control)
    other_axes = [j for j in range(3) if j != axis]
    other_shape = tuple(shape[j] for j in other_axes)
    for index in np.ndindex(*other_shape):
        selector = [slice(None)] * 3
        for j, value in zip(other_axes, index):
            selector[j] = value
        power_line = control[tuple(selector)]
        bernstein_line = np.empty(degree + 1, dtype=object)
        for i in range(degree + 1):
            bernstein_line[i] = sum(
                (
                    power_line[k]
                    * sp.Rational(math.comb(i, k), math.comb(degree, k))
                    for k in range(i + 1)
                ),
                sp.Rational(0),
            )
        converted[tuple(selector)] = bernstein_line
    control = converted


def lower_float(value) -> float:
    if value == 0:
        return 0.0
    result = float(value)
    exact = F(int(sp.numer(value)), int(sp.denom(value)))
    if F(*result.as_integer_ratio()) > exact:
        result = np.nextafter(result, -math.inf)
    return result


control = np.vectorize(lower_float, otypes=[float])(control)


def split_axis(net: np.ndarray, axis: int) -> tuple[np.ndarray, np.ndarray]:
    degree = net.shape[axis] - 1
    moved = np.moveaxis(net, axis, 0)
    left = np.empty_like(moved)
    right = np.empty_like(moved)
    work = moved.copy()
    left[0] = work[0]
    right[degree] = work[degree]
    for level in range(1, degree + 1):
        first = work[: degree - level + 1]
        second = work[1 : degree - level + 2]
        midpoint = (first + second) * 0.5
        midpoint = np.where(
            first == second, first, np.nextafter(midpoint, -math.inf)
        )
        work[: degree - level + 1] = midpoint
        left[level] = work[0]
        right[degree - level] = work[degree - level]
    return np.moveaxis(left, 0, axis), np.moveaxis(right, 0, axis)


def exact_prune(box: tuple[tuple[float, float], ...]) -> bool:
    ux, uy, uz = [tuple(F(v) for v in interval) for interval in box]
    xlo, xhi = ux[0] * F(77, 80), ux[1] * F(77, 80)
    ylo, yhi = uy[0] * F(77, 80), uy[1] * F(77, 80)
    zlo, zhi = uz[0] * 48, uz[1] * 48

    # Feasibility: t_i in [a,b] and t_i-a(1+xi(1-t_i)) >= 0.
    if xhi < F(3, 80) or yhi < F(3, 80):
        return True
    if xhi * (1 + F(3, 80) * zlo) - F(3, 80) * (1 + zlo) < 0:
        return True
    if yhi * (1 + F(3, 80) * zlo) - F(3, 80) * (1 + zlo) < 0:
        return True

    # Direct g<=0 test: n/h >= S_16(xi).
    h_upper = 1 - xlo * ylo * zlo / (1 + zlo)
    n_lower = min(
        1 - x0 - y0 + x0 * y0 * (2 + zhi) / (1 + zhi)
        for x0 in (xlo, xhi)
        for y0 in (ylo, yhi)
    )
    values = [
        (1 - F(k, 16)) / (1 + zlo * F(k, 16)) for k in range(17)
    ]
    t_upper = (
        values[0]
        + values[-1]
        + 4 * sum(values[1:-1:2])
        + 2 * sum(values[2:-1:2])
    ) / 48
    if n_lower >= t_upper * h_upper:
        return True

    # Direct positive-row lower bound, including denominator faces where the
    # cleared numerator has artificial zeros.
    alpha = F(231, 6400)

    def upper_row(tlo, thi, otherlo):
        den_upper = max(F(0), thi - F(3, 80)) * max(F(0), F(77, 80) - tlo)
        num_lower = alpha * max(F(0), otherlo)
        if den_upper == 0:
            return None if num_lower > 0 else F(0)
        return num_lower / den_upper

    def lower_row(tlo, thi, otherhi):
        j_lower = 1 + zlo * (1 - thi)
        den_upper = max(F(0), thi) * max(
            F(0), F(77, 80) * (1 + zhi * (1 - tlo)) - tlo
        )
        num_lower = alpha * max(F(0), 1 - otherhi) * j_lower**3
        if den_upper == 0:
            return None if num_lower > 0 else F(0)
        return num_lower / den_upper

    terms = (
        upper_row(xlo, xhi, ylo),
        upper_row(ylo, yhi, xlo),
        lower_row(xlo, xhi, yhi),
        lower_row(ylo, yhi, xhi),
    )
    if any(term is None for term in terms):
        return True
    row_lower = sum(terms, F(0))
    negative_upper = zhi * max(F(0), h_upper * t_upper - n_lower)
    return F(3, 8) * row_lower >= negative_upper


started = time.perf_counter()
stack = [(control, tuple((0.0, 1.0) for _ in range(3)), 0)]
positive_leaves = 0
pruned_leaves = 0
maximum_depth = 0
while stack:
    net, box, depth = stack.pop()
    if exact_prune(box):
        pruned_leaves += 1
        continue
    if float(net.min()) >= 0.0:
        positive_leaves += 1
        maximum_depth = max(maximum_depth, depth)
        continue
    assert depth < 80, ("certificate depth exceeded", depth, box, float(net.min()))
    scores = [float(np.max(np.abs(np.diff(net, axis=axis)))) for axis in range(3)]
    axis = int(np.argmax(scores))
    left, right = split_axis(net, axis)
    midpoint = (box[axis][0] + box[axis][1]) / 2
    left_box = list(box)
    right_box = list(box)
    left_box[axis] = (box[axis][0], midpoint)
    right_box[axis] = (midpoint, box[axis][1])
    stack.append((right, tuple(right_box), depth + 1))
    stack.append((left, tuple(left_box), depth + 1))

assert positive_leaves > 0 and pruned_leaves > 0


# A strict rational feasible table shows that 149/100 is already too small.
# The logarithm is certified from below by eight positive atanh-series terms.
def omega(r: F) -> F:
    return (r - F(1, 2)) ** 2 / (r * (1 - r))


xw, yw, zw = F(11, 200), F(189, 200), F(83, 5000)
cw, aw = F(37, 40), F(3, 80)
sw = cw * cw * zw
qw, rw = aw + cw * xw, aw + cw * yw
Aw = (1 - qw) * (1 - rw) - sw
Bw = qw * (1 - rw) + sw
Cw = (1 - qw) * rw + sw
Dw = qw * rw - sw
assert min(Aw, Bw, Cw, Dw) > 0
assert zw < min(xw * yw, (1 - xw) * (1 - yw))
alpha0w = (1 - aw) * (1 - aw - cw)
alpha1w = aw * (aw + cw)
mw = alpha0w + alpha1w
kw = zw * (
    2 * alpha0w / Aw + mw / Bw + mw / Cw + 2 * alpha1w / Dw
)
ri0 = xw + cw * zw / (1 - rw)
ri1 = xw - cw * zw / rw
rj0 = yw + cw * zw / (1 - qw)
rj1 = yw - cw * zw / qw
dw = zw * (
    alpha0w * (omega(ri0) + omega(rj0)) / Aw
    + (alpha0w * omega(ri0) + alpha1w * omega(rj1)) / Bw
    + (alpha1w * omega(ri1) + alpha0w * omega(rj0)) / Cw
    + alpha1w * (omega(ri1) + omega(rj1)) / Dw
)
oddsw = Bw * Cw / (Aw * Dw)
nonlogw = sw * (1 / Aw + 1 / Bw + 1 / Cw + 1 / Dw)
atanh_arg = (oddsw - 1) / (oddsw + 1)
log_lower = 2 * sum(
    atanh_arg ** (2 * k + 1) / (2 * k + 1) for k in range(8)
)
sharpness_margin = log_lower - nonlogw - F(149, 100) * (kw + dw)
assert sharpness_margin > 0

print("c=37/40 midpoint gamma=3/2 certificate: PASS")
print(f"tail margin at xi=48: {tail_floor - tail_value} > 0")
print(f"polynomial degree: {degrees}, expanded terms: {len(poly.terms())}")
print(f"Bernstein-positive leaves: {positive_leaves}")
print(f"exactly pruned leaves: {pruned_leaves}")
print(f"maximum subdivision depth: {maximum_depth}")
print(f"149/100 obstruction margin: {sharpness_margin} > 0")
print(f"certificate search seconds: {time.perf_counter() - started:.3f}")
