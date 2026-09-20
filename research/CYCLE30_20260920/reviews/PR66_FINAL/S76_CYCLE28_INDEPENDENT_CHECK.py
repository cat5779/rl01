#!/usr/bin/env python3
"""Independent standard-library diagnostics for S76 Cycle28.

The script constructs the actual consecutive-Fourier exterior channel, then
enumerates every midpoint atom.  It also checks the Jeffreys-energy identity
and the posterior-variance lower bound.  Floating-point enumeration is a
diagnostic; the general signs are proved analytically in the review.
"""

import cmath
import itertools
import math


def determinant(matrix):
    n = len(matrix)
    if n == 0:
        return 1.0 + 0.0j
    a = [row[:] for row in matrix]
    out = 1.0 + 0.0j
    sign = 1
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(a[row][col]))
        if abs(a[pivot][col]) < 1e-15:
            return 0.0 + 0.0j
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


def indices(mask, m):
    return [i for i in range(m) if mask >> i & 1]


def cyclic_unitary(m):
    # U=2 Q_EO for the first m Fourier modes on the 2m-cycle.
    out = []
    for erow in range(m):
        e = 2 * erow
        row = []
        for ocol in range(m):
            o = 2 * ocol + 1
            value = sum(
                cmath.exp(2j * math.pi * (e - o) * mode / (2 * m))
                for mode in range(m)
            ) / m
            row.append(value)
        out.append(row)
    return out


def exterior_channel(u):
    m = len(u)
    n = 1 << m
    w = [[0.0] * n for _ in range(n)]
    for z in range(n):
        rows = indices(z, m)
        for t in range(n):
            cols = indices(t, m)
            if len(rows) != len(cols):
                continue
            minor = [[u[i][j] for j in cols] for i in rows]
            w[z][t] = abs(determinant(minor)) ** 2
    row_err = max(abs(sum(row) - 1.0) for row in w)
    col_err = max(abs(sum(w[z][t] for z in range(n)) - 1.0) for t in range(n))
    assert row_err < 2e-12
    assert col_err < 2e-12
    return w, row_err, col_err


def pair_probability(y_bit, z_bit, r, s):
    return r if y_bit == z_bit else s


def conditional_z_given_y(y, z, m, r, s):
    value = 1.0
    for i in range(m):
        value *= 2.0 * pair_probability(y >> i & 1, z >> i & 1, r, s)
    return value


def evaluate(m, c):
    k = c * c
    r = (1.0 - k) / 4.0
    s = (1.0 + k) / 4.0
    ell = math.log(s / r)
    n = 1 << m
    w, row_err, col_err = exterior_channel(cyclic_unitary(m))

    pyz = [[0.0] * n for _ in range(n)]
    pz_given_y = [[0.0] * n for _ in range(n)]
    pt_given_y = [[0.0] * n for _ in range(n)]
    pyt = [[0.0] * n for _ in range(n)]
    for y in range(n):
        for z in range(n):
            cond = conditional_z_given_y(y, z, m, r, s)
            pz_given_y[y][z] = cond
            pyz[y][z] = cond / n
        for t in range(n):
            pt_given_y[y][t] = sum(pz_given_y[y][z] * w[z][t] for z in range(n))
            pyt[y][t] = pt_given_y[y][t] / n

    c_x = 0.0
    c_d = 0.0
    for y in range(n):
        for z in range(n):
            dcount = m - (y ^ z).bit_count()
            for t in range(n):
                joint = pyz[y][z] * w[z][t]
                if joint == 0.0:
                    continue
                x = y.bit_count() + t.bit_count() - m
                info = math.log(pyz[y][z] / pyt[y][t])
                c_x += joint * ((x * x - dcount) / (r * r)) * info
                c_d += joint * ((dcount - 2 * m * r) / (r * s)) * info

    e_w = 0.0
    vbar = 0.0
    for i in range(m):
        for y in range(n):
            yf = y ^ (1 << i)
            jdiv = 0.0
            for t in range(n):
                p = pt_given_y[y][t]
                q = pt_given_y[yf][t]
                jdiv += (p - q) * math.log(p / q)
            e_w += 0.25 * jdiv / n

            # M=(P_y+P_yi)/2 on Z; zeta uses the unflipped y reference.
            variance_payment = 0.0
            for t in range(n):
                mt = 0.0
                signed = 0.0
                for z in range(n):
                    mz = 0.5 * (pz_given_y[y][z] + pz_given_y[yf][z])
                    contribution = mz * w[z][t]
                    zeta = 1.0 if ((y >> i) & 1) == ((z >> i) & 1) else -1.0
                    mt += contribution
                    signed += contribution * zeta
                if mt > 0.0:
                    mean = signed / mt
                    variance_payment += mt * (1.0 - mean * mean)
            vbar += variance_payment / (m * n)

    e_id = m * k * ell / 2.0
    eta_energy = 2.0 * (e_id - e_w) / (m * k * ell)
    eta_cd = -c_d / (4.0 * m * ell)
    assert abs(eta_energy - eta_cd) < 2e-10, (eta_energy, eta_cd, c_d, e_w, e_id)
    assert eta_energy + 2e-12 >= vbar

    g2 = c_x + c_d
    h_in2 = m * (4.0 * ell - 2.0 / r)
    h_out2 = h_in2 + g2
    return {
        "m": m,
        "C_X": c_x,
        "C_D": c_d,
        "G2": g2,
        "H_out2": h_out2,
        "eta_energy": eta_energy,
        "eta_cd": eta_cd,
        "Vbar": vbar,
        "eta_minus_Vbar": eta_energy - vbar,
        "row_error": row_err,
        "column_error": col_err,
    }


def binary_inequality_grid():
    # atanh(k m) <= m atanh(k) for 0<=m<=1; evenness covers signed m.
    minimum_gap = float("inf")
    for ik in range(1, 100):
        k = ik / 100.0
        for im in range(101):
            mean = im / 100.0
            gap = mean * math.atanh(k) - math.atanh(k * mean)
            minimum_gap = min(minimum_gap, gap)
            assert gap >= -2e-15
    return minimum_gap


def obstruction(c):
    k = c * c
    r = (1.0 - k) / 4.0
    s = (1.0 + k) / 4.0
    return math.log((r * r + s * s) / (2.0 * r * r))


def main():
    print("BINARY JEFFREYS/PER-EDGE INEQUALITY DIAGNOSTIC")
    print("minimum sampled convexity gap =", binary_inequality_grid())

    print("\nACTUAL CYCLIC ENUMERATION, c=0.95")
    for m in (2, 3, 4, 5):
        row = evaluate(m, 0.95)
        print(
            "m={m}: C_X={C_X:.10f}, C_D={C_D:.10f}, G''={G2:.10f}, "
            "H_out''={H_out2:.10f}, eta={eta_energy:.9f}, "
            "Vbar={Vbar:.9f}, eta-Vbar={eta_minus_Vbar:.9f}, "
            "row_err={row_error:.2e}, col_err={column_error:.2e}".format(**row)
        )

    threshold = math.sqrt(
        (math.sqrt(2.0 * math.e - 1.0) - 1.0)
        / (math.sqrt(2.0 * math.e - 1.0) + 1.0)
    )
    print("\nFOUR-SITE POINTWISE OBSTRUCTION")
    print("threshold c =", repr(threshold))
    print("Xi/delta at threshold =", obstruction(threshold))
    print("Xi/delta at c=0.95 =", obstruction(0.95))
    assert abs(obstruction(threshold) - 1.0) < 2e-15
    assert obstruction(0.95) > 1.0


if __name__ == "__main__":
    main()
