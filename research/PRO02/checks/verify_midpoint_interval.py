"""Certified balanced-channel pair comparison beyond 37/40.

For every ``37/40 <= c <= 937/1000`` at the balanced offset
``a=(1-c)/2``, this script proves

    g_+ <= (199/100) (K + D).

Together with the two directed budgets, the comparison gives the direct
finite-dimensional curvature bound ``H'' <= -(1/50)n``.  Thus the original
two-budget mechanism itself continues beyond 37/40 on the balanced line,
even though its full-offset theorem stops at 37/40.
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


C_LO = F(37, 40)
C_HI = F(937, 1000)
XI_MAX = F(58)
T_MAX = F(1937, 2000)
GAMMA = F(199, 100)
tail_value = trapezoid24(XI_MAX)
tail_floor = (1 - C_HI * C_HI) / 2
assert tail_value < tail_floor


c, t0, t1, xi = sp.symbols("c t0 t1 xi")
a = (1 - c) / 2
b = (1 + c) / 2
j0 = 1 + xi * (1 - t0)
j1 = 1 + xi * (1 - t1)
h = 1 - t0 * t1 * xi / (1 + xi)
n = (1 - t0) * (1 - t1) + t0 * t1 / (1 + xi)
alpha = (1 - c * c) / 4
rows = alpha * (
    t1 / ((t0 - a) * (b - t0))
    + t0 / ((t1 - a) * (b - t1))
    + (1 - t1) * j0**3 / ((t0 - a * j0) * (b * j0 - t0))
    + (1 - t0) * j1**3 / ((t1 - a * j1) * (b * j1 - t1))
)
target = sp.Rational(199, 400) * rows - xi * h * simpson16(xi) + xi * n
numerator, denominator = sp.together(target).as_numer_denom()
assert sp.expand(sp.factor(denominator) - denominator) == 0
poly = sp.Poly(numerator, c, t0, t1, xi)


variables = (c, t0, t1, xi)
lower = (
    sp.Rational(C_LO.numerator, C_LO.denominator),
    sp.Rational(0),
    sp.Rational(0),
    sp.Rational(0),
)
width = (
    sp.Rational((C_HI - C_LO).numerator, (C_HI - C_LO).denominator),
    sp.Rational(T_MAX.numerator, T_MAX.denominator),
    sp.Rational(T_MAX.numerator, T_MAX.denominator),
    sp.Rational(XI_MAX.numerator, XI_MAX.denominator),
)
unit = sp.symbols("u0:4")
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
    other_axes = [j for j in range(4) if j != axis]
    other_shape = tuple(shape[j] for j in other_axes)
    for index in np.ndindex(*other_shape):
        selector = [slice(None)] * 4
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
    uc, ux, uy, uz = [tuple(F(v) for v in interval) for interval in box]
    clo = C_LO + uc[0] * (C_HI - C_LO)
    chi = C_LO + uc[1] * (C_HI - C_LO)
    xlo, xhi = ux[0] * T_MAX, ux[1] * T_MAX
    ylo, yhi = uy[0] * T_MAX, uy[1] * T_MAX
    zlo, zhi = uz[0] * XI_MAX, uz[1] * XI_MAX
    alo, ahi = (1 - chi) / 2, (1 - clo) / 2
    blo, bhi = (1 + clo) / 2, (1 + chi) / 2

    if xhi < alo or yhi < alo or xlo > bhi or ylo > bhi:
        return True
    if xhi * (1 + alo * zlo) - alo * (1 + zlo) < 0:
        return True
    if yhi * (1 + alo * zlo) - alo * (1 + zlo) < 0:
        return True

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

    alpha_lower = (1 - chi * chi) / 4

    def upper_row(tlo, thi, otherlo):
        den_upper = max(F(0), thi - alo) * max(F(0), bhi - tlo)
        num_lower = alpha_lower * max(F(0), otherlo)
        if den_upper == 0:
            return None if num_lower > 0 else F(0)
        return num_lower / den_upper

    def lower_row(tlo, thi, otherhi):
        j_lower = 1 + zlo * (1 - thi)
        den_upper = max(F(0), thi) * max(
            F(0), bhi * (1 + zhi * (1 - tlo)) - tlo
        )
        num_lower = alpha_lower * max(F(0), 1 - otherhi) * j_lower**3
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
    return F(199, 400) * row_lower >= negative_upper


started = time.perf_counter()
stack = [(control, tuple((0.0, 1.0) for _ in range(4)), 0)]
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
    scores = [float(np.max(np.abs(np.diff(net, axis=axis)))) for axis in range(4)]
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


# Strict rational obstruction just above the certified endpoint.  At
# c=15/16 the same pointwise comparison fails even with gamma=2.
def omega(r: F) -> F:
    return (r - F(1, 2)) ** 2 / (r * (1 - r))


cw = F(15, 16)
aw = (1 - cw) / 2
xw, yw, zw = F(51, 1000), F(949, 1000), F(73, 5000)
sw = cw * cw * zw
qw, rw = aw + cw * xw, aw + cw * yw
Aw = (1 - qw) * (1 - rw) - sw
Bw = qw * (1 - rw) + sw
Cw = (1 - qw) * rw + sw
Dw = qw * rw - sw
assert min(Aw, Bw, Cw, Dw) > 0
assert zw < min(xw * yw, (1 - xw) * (1 - yw))
alpha = aw * (aw + cw)
kw = 2 * alpha * zw * (1 / Aw + 1 / Bw + 1 / Cw + 1 / Dw)
ri0 = xw + cw * zw / (1 - rw)
ri1 = xw - cw * zw / rw
rj0 = yw + cw * zw / (1 - qw)
rj1 = yw - cw * zw / qw
dw = alpha * zw * (
    (omega(ri0) + omega(rj0)) / Aw
    + (omega(ri0) + omega(rj1)) / Bw
    + (omega(ri1) + omega(rj0)) / Cw
    + (omega(ri1) + omega(rj1)) / Dw
)
oddsw = Bw * Cw / (Aw * Dw)
nonlogw = sw * (1 / Aw + 1 / Bw + 1 / Cw + 1 / Dw)
atanh_arg = (oddsw - 1) / (oddsw + 1)
log_lower = 2 * sum(
    atanh_arg ** (2 * k + 1) / (2 * k + 1) for k in range(6)
)
obstruction_margin = log_lower - nonlogw - 2 * (kw + dw)
assert obstruction_margin > 0

print("balanced c in [37/40,937/1000], gamma=199/100: PASS")
print(f"tail margin at xi=58: {tail_floor - tail_value} > 0")
print(f"polynomial degree: {degrees}, expanded terms: {len(poly.terms())}")
print(f"Bernstein-positive leaves: {positive_leaves}")
print(f"exactly pruned leaves: {pruned_leaves}")
print(f"maximum subdivision depth: {maximum_depth}")
print(f"gamma=2 obstruction at c=15/16: {obstruction_margin} > 0")
print(f"certificate search seconds: {time.perf_counter() - started:.3f}")
