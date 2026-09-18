"""Finite sine checks for reveal monotonicity at c=37/40.

The first check is a high-precision, fully specified *pointwise* counterexample
to convexity of the exact potential under one genuine sine reveal.  The
second exhaustively averages every prefix word for the same n=8 experiment;
the average drift is positive at every reveal step.  The latter is numerical
evidence only, not a general sign certificate.
"""

from __future__ import annotations

import itertools
import math

import mpmath as mp
import numpy as np


A = mp.mpf(3) / 80
C = mp.mpf(37) / 40
N = 8
CORE = [3, 4]
ORDER = [2, 5, 1, 6, 0, 7]
PREFIX = [3, 4, 2, 5, 1, 6, 0]
PREFIX_BITS = [1, 0, 1, 0, 0, 1, 1]
REVEAL = 7


def sine_kernel_mp(n: int) -> mp.matrix:
    q = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            q[i, j] = (
                mp.mpf(1) / 2
                if i == j
                else mp.sin(mp.pi * (i - j) / 2) / (mp.pi * (i - j))
            )
    return q


def psi(v, h):
    if h == 0:
        return mp.mpf(0)
    return h + (v - h) * mp.log((v - h) / v)


def phi(g: mp.matrix, core_positions: list[int]):
    value = sum(g[i, i] ** 2 for i in core_positions)
    for ii, i in enumerate(core_positions):
        for j in core_positions[ii + 1 :]:
            value += 2 * psi(g[i, i] * g[j, j], abs(g[i, j]) ** 2)
    return value


def principal(mat: mp.matrix, indices: list[int]) -> mp.matrix:
    return mp.matrix([[mat[i, j] for j in indices] for i in indices])


def inverse_for_word(k: mp.matrix, indices: list[int], bits: list[int]) -> mp.matrix:
    block = principal(k, indices)
    for i, bit in enumerate(bits):
        block[i, i] -= 1 - bit
    return block**-1


def pointwise_counterexample():
    mp.mp.dps = 90
    q = sine_kernel_mp(N)
    k = A * mp.eye(N) + C * q
    g0 = inverse_for_word(k, PREFIX, PREFIX_BITS)
    core_positions = [PREFIX.index(i) for i in CORE]
    column = mp.matrix([k[i, REVEAL] for i in PREFIX])
    p = k[REVEAL, REVEAL] - (column.T * g0 * column)[0]
    values = []
    branch_core_blocks = []
    for bit in (1, 0):
        indices = PREFIX + [REVEAL]
        bits = PREFIX_BITS + [bit]
        gb = inverse_for_word(k, indices, bits)
        values.append(phi(gb, core_positions))
        branch_core_blocks.append(
            mp.matrix([[gb[i, j] for j in core_positions] for i in core_positions])
        )
    before = phi(g0, core_positions)
    defect = p * values[0] + (1 - p) * values[1] - before

    # Matrix martingale quadratic variation on the core block, evaluated
    # directly from the two exact branch inverses.
    parent_core = mp.matrix(
        [[g0[i, j] for j in core_positions] for i in core_positions]
    )
    hs1 = sum(
        abs(branch_core_blocks[0][i, j] - parent_core[i, j]) ** 2
        for i in range(len(core_positions))
        for j in range(len(core_positions))
    )
    hs0 = sum(
        abs(branch_core_blocks[1][i, j] - parent_core[i, j]) ** 2
        for i in range(len(core_positions))
        for j in range(len(core_positions))
    )
    qv = p * hs1 + (1 - p) * hs0
    return p, before, values[0], values[1], defect, qv, defect / qv


def sine_kernel_np(n: int) -> np.ndarray:
    q = np.empty((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            r = i - j
            q[i, j] = 0.5 if r == 0 else math.sin(math.pi * r / 2) / (math.pi * r)
    return q


def phi_np(g: np.ndarray, core_positions: list[int]) -> float:
    value = sum(float(g[i, i] ** 2) for i in core_positions)
    for ii, i in enumerate(core_positions):
        for j in core_positions[ii + 1 :]:
            h = float(g[i, j] ** 2)
            v = float(g[i, i] * g[j, j])
            value += 2 * (h + (v - h) * math.log1p(-h / v))
    return value


def word_probability(block: np.ndarray, bits: tuple[int, ...]) -> float:
    mat = block - np.diag([1 - bit for bit in bits])
    sign, logabs = np.linalg.slogdet(mat)
    return ((-1) ** (len(bits) - sum(bits))) * sign * math.exp(logabs)


def expected_phi(k: np.ndarray, indices: list[int]) -> float:
    block = k[np.ix_(indices, indices)]
    core_positions = [indices.index(i) for i in CORE]
    answer = 0.0
    for bits in itertools.product((0, 1), repeat=len(indices)):
        probability = word_probability(block, bits)
        mat = block - np.diag([1 - bit for bit in bits])
        answer += probability * phi_np(np.linalg.inv(mat), core_positions)
    return answer


def averaged_prefix_drifts():
    q = sine_kernel_np(N)
    k = float(A) * np.eye(N) + float(C) * q
    indices = CORE.copy()
    previous = expected_phi(k, indices)
    rows = []
    for site in ORDER:
        indices = indices + [site]
        current = expected_phi(k, indices)
        rows.append((site, current - previous, current))
        previous = current
    return rows


def main():
    p, before, branch1, branch0, defect, qv, ratio = pointwise_counterexample()
    assert defect < 0
    print("sine pointwise reveal counterexample: PASS")
    print(f"prefix={PREFIX} bits={PREFIX_BITS} reveal={REVEAL}")
    print(f"p={mp.nstr(p, 40)}")
    print(f"phi_before={mp.nstr(before, 40)}")
    print(f"phi_branch1={mp.nstr(branch1, 40)}")
    print(f"phi_branch0={mp.nstr(branch0, 40)}")
    print(f"defect={mp.nstr(defect, 40)}")
    print(f"quadratic_variation={mp.nstr(qv, 40)}")
    print(f"defect_over_qv={mp.nstr(ratio, 40)}")
    rows = averaged_prefix_drifts()
    assert all(drift > 0 for _, drift, _ in rows)
    print("n=8 exhaustive actual-law average drifts: PASS")
    for site, drift, current in rows:
        print(f"reveal={site} average_drift={drift:.16g} expected_phi={current:.16g}")


if __name__ == "__main__":
    main()
