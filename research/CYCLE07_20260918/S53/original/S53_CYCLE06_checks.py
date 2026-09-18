#!/usr/bin/env python3
"""Exact symbolic checks for S53 cycle06.

These checks verify algebraic identities only; they are not independent
certification of the imported S41/S44 analytic estimates.
"""
from __future__ import annotations

import sympy as sp


def check_normalization_bridge() -> None:
    h, q = sp.symbols("h q", positive=True)
    ell = lambda z: sp.log(z / (1 - z))
    Phi = sp.Rational(1, 4) * (q - h) / (h * (1 - h)) * (ell(q) - ell(h))
    phi = (q - sp.Rational(1, 2)) * ell(q)
    chi = 2 - 4 * q - ell(q)
    assert sp.simplify(Phi.subs(h, sp.Rational(1, 2)) - phi) == 0
    assert sp.simplify(sp.diff(Phi, h).subs(h, sp.Rational(1, 2)) - chi) == 0
    assert sp.simplify(
        sp.diff(Phi, h, 2).subs(h, sp.Rational(1, 2)) - (8 + 8 * phi)
    ) == 0
    print("normalization bridge: OK")


def check_covariant_galerkin_identity() -> None:
    h = sp.symbols("h")
    p0 = [sp.Rational(1, 5), sp.Rational(1, 4), sp.Rational(3, 10), sp.Rational(1, 4)]
    p1 = [sp.Rational(1, 20), -sp.Rational(1, 40), sp.Rational(1, 50), -sp.Rational(9, 200)]
    p2 = [sp.Rational(1, 100), -sp.Rational(1, 200), sp.Rational(1, 250), -sp.Rational(9, 1000)]
    d0 = [sp.Rational(1, 20), -sp.Rational(1, 25), sp.Rational(3, 100), -sp.Rational(1, 25)]
    d1 = [sp.Rational(1, 100), sp.Rational(1, 200), -sp.Rational(1, 125), -sp.Rational(7, 1000)]
    d2 = [sp.Rational(1, 500), -sp.Rational(1, 1000), sp.Rational(3, 2000), -sp.Rational(1, 400)]
    assert sum(p0) == 1 and sum(p1) == 0 and sum(p2) == 0
    assert sum(d0) == 0 and sum(d1) == 0 and sum(d2) == 0

    p = [p0[i] + h * p1[i] + h**2 * p2[i] / 2 for i in range(4)]
    d = [d0[i] + h * d1[i] + h**2 * d2[i] / 2 for i in range(4)]
    groups = [[0, 1], [2, 3]]
    full = sum(d[i] ** 2 / p[i] for i in range(4))
    coarse = sum(
        sum(d[i] for i in block) ** 2 / sum(p[i] for i in block)
        for block in groups
    )
    exact = sp.simplify(sp.diff(full - coarse, h, 2).subs(h, 0))

    f = sp.Matrix([d0[i] / p0[i] for i in range(4)])
    g_list = [sp.Rational(0)] * 4
    for block in groups:
        gv = sum(d0[i] for i in block) / sum(p0[i] for i in block)
        for i in block:
            g_list[i] = sp.simplify(gv)
    g = sp.Matrix(g_list)
    e = f - g
    s = sp.Matrix([p1[i] / p0[i] for i in range(4)])
    t = sp.Matrix([p2[i] / p0[i] for i in range(4)])
    u = sp.Matrix([d1[i] / p0[i] for i in range(4)])
    v = sp.Matrix([d2[i] / p0[i] for i in range(4)])
    k = sp.Matrix([u[i] - s[i] * g[i] for i in range(4)])

    pk = [sp.Rational(0)] * 4
    for block in groups:
        kv = sum(p0[i] * k[i] for i in block) / sum(p0[i] for i in block)
        for i in block:
            pk[i] = sp.simplify(kv)
    z = k - sp.Matrix(pk)

    def inner(a: sp.Matrix, b: sp.Matrix) -> sp.Expr:
        return sp.simplify(sum(p0[i] * a[i] * b[i] for i in range(4)))

    forcing = sp.Matrix([v[i] - t[i] * g[i] - 2 * s[i] * k[i] for i in range(4)])
    metric = sp.Matrix([(2 * s[i] ** 2 - t[i]) * e[i] for i in range(4)])
    rhs = sp.simplify(2 * inner(z, z) + 2 * inner(e, forcing) + inner(e, metric))
    assert sp.simplify(exact - rhs) == 0
    print("covariant Galerkin identity: OK")
    print("exact rational test value:", exact)


def check_channel_kernel_grouping() -> None:
    f2, A = sp.symbols("f2 A")
    r = sp.symbols("r0:3")
    d = sp.symbols("d0:3")
    Delta = sp.symbols("Delta0:3")
    Ai = sp.symbols("Ai0:3")
    Bp = [Delta[i] - f2 * d[i] for i in range(3)]
    raw = (
        f2 * A
        + A * sum(r[i] * Bp[i] for i in range(3))
        + sum(r[i] * Delta[i] * (Ai[i] - A + 1) for i in range(3))
    )
    grouped = (
        f2
        + sum(r[i] * Bp[i] for i in range(3))
        + sum(r[i] * (Delta[i] * Ai[i] - f2 * d[i] * A) for i in range(3))
    )
    constraint = {A: 1 - sum(r[i] * d[i] for i in range(3))}
    assert sp.simplify((raw - grouped).subs(constraint)) == 0
    print("channel-kernel grouping: OK")


def check_first_jet_obstruction() -> None:
    r, j, c, h = sp.symbols("r j c h", real=True)
    value = 4 * (r + j * h + c * h**2 / 2) ** 2
    curvature = sp.simplify(sp.diff(value, h, 2).subs(h, 0))
    assert curvature == 8 * (j**2 + r * c)
    print("first-jet obstruction: OK; D''(0) =", curvature)


if __name__ == "__main__":
    check_normalization_bridge()
    check_covariant_galerkin_identity()
    check_channel_kernel_grouping()
    check_first_jet_obstruction()
