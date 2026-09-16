#!/usr/bin/env python3
"""Exact small coupled DPP checks plus clearly labelled Decimal diagnostics.

The theorem is analytical.  This script only checks its finite algebra and a
nontrivial coupled example.  It deliberately avoids q=2.
"""
from __future__ import annotations

import argparse
import itertools
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Iterable


def det(a: list[list[Fraction]]) -> Fraction:
    n = len(a)
    if n == 0:
        return Fraction(1)
    m = [row[:] for row in a]
    ans = Fraction(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if m[i][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            m[j], m[pivot] = m[pivot], m[j]
            ans = -ans
        p = m[j][j]
        ans *= p
        for k in range(j, n):
            m[j][k] /= p
        for i in range(j + 1, n):
            f = m[i][j]
            if f:
                for k in range(j, n):
                    m[i][k] -= f * m[j][k]
    return ans


def inv(a: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    m = [a[i][:] + [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if m[i][j])
        m[j], m[pivot] = m[pivot], m[j]
        p = m[j][j]
        m[j] = [x / p for x in m[j]]
        for i in range(n):
            if i == j:
                continue
            f = m[i][j]
            if f:
                m[i] = [m[i][k] - f * m[j][k] for k in range(2 * n)]
    return [row[n:] for row in m]


def mmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def principal(a: list[list[Fraction]], mask: int) -> list[list[Fraction]]:
    ids = [i for i in range(len(a)) if mask >> i & 1]
    return [[a[i][j] for j in ids] for i in ids]


def subsets(mask: int) -> Iterable[int]:
    s = mask
    while True:
        yield s
        if s == 0:
            break
        s = (s - 1) & mask


def atoms_from_inclusion(k: list[list[Fraction]]) -> list[Fraction]:
    n = len(k)
    full = (1 << n) - 1
    out = []
    for s in range(1 << n):
        comp = full ^ s
        value = Fraction(0)
        for b in subsets(comp):
            value += (-1 if b.bit_count() & 1 else 1) * det(principal(k, s | b))
        out.append(value)
    return out


def marginal_atoms(k: list[list[Fraction]], ids: list[int]) -> list[Fraction]:
    kb = [[k[i][j] for j in ids] for i in ids]
    return atoms_from_inclusion(kb)


def ftxt(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def dec(x: Fraction) -> Decimal:
    return Decimal(x.numerator) / Decimal(x.denominator)


def dlog(x: Fraction) -> Decimal:
    return dec(x).ln()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    getcontext().prec = 80

    qmat = [
        [Fraction(1, 2), Fraction(1, 8), Fraction(0)],
        [Fraction(1, 8), Fraction(1, 2), Fraction(1, 8)],
        [Fraction(0), Fraction(1, 8), Fraction(1, 2)],
    ]
    a = Fraction(1, 20)
    c = Fraction(19, 20)
    n = 3
    eye = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    k = [[a * eye[i][j] + c * qmat[i][j] for j in range(n)] for i in range(n)]
    imk = [[eye[i][j] - k[i][j] for j in range(n)] for i in range(n)]
    lmat = mmul(k, inv(imk))
    normalizer = det(imk)

    p = atoms_from_inclusion(k)
    p_l = [normalizer * det(principal(lmat, s)) for s in range(1 << n)]

    # Coarse exact spectral strip follows from Gershgorin for Q: 1/4 <= Q <= 3/4.
    delta = Fraction(19, 80)
    lo_ratio = delta / (1 - delta)  # 19/61
    hi_ratio = 1 / lo_ratio

    adjacent_ratios = []
    for s in range(1 << n):
        for i in range(n):
            if not (s >> i) & 1:
                adjacent_ratios.append(p[s | (1 << i)] / p[s])

    blocks = [[0, 1], [2]]
    block_probs = [marginal_atoms(k, ids) for ids in blocks]
    w: list[Fraction] = []
    for s in range(1 << n):
        val = Fraction(1)
        for ids, pb in zip(blocks, block_probs):
            local = sum(((s >> site) & 1) << j for j, site in enumerate(ids))
            val *= pb[local]
        w.append(val)

    w_adjacent_ratios = []
    lr_adjacent_ratios = []
    for s in range(1 << n):
        for i in range(n):
            if not (s >> i) & 1:
                t = s | (1 << i)
                w_adjacent_ratios.append(w[t] / w[s])
                lr_adjacent_ratios.append((p[t] / w[t]) / (p[s] / w[s]))

    exact_checks = {
        "all_atoms_positive": all(x > 0 for x in p),
        "atom_normalization": sum(p) == 1,
        "L_principal_minor_atom_identity": p == p_l,
        "block_reference_normalization": sum(w) == 1,
        "p_information_ratio_lower": min(adjacent_ratios) >= lo_ratio,
        "p_information_ratio_upper": max(adjacent_ratios) <= hi_ratio,
        "w_information_ratio_lower": min(w_adjacent_ratios) >= lo_ratio,
        "w_information_ratio_upper": max(w_adjacent_ratios) <= hi_ratio,
        "likelihood_ratio_flip_lower": min(lr_adjacent_ratios) >= lo_ratio**2,
        "likelihood_ratio_flip_upper": max(lr_adjacent_ratios) <= hi_ratio**2,
    }
    if not all(exact_checks.values()):
        raise SystemExit(f"exact finite check failed: {exact_checks}")

    # Floating/Decimal diagnostics only.  They are not theorem evidence.
    H = -sum(dec(x) * dlog(x) for x in p)
    D = sum(dec(p[i]) * (dlog(p[i]) - dlog(w[i])) for i in range(1 << n))
    Lambda = (dec(1 - delta) / dec(delta)).ln()
    diagnostics = []
    for q_text in ["0.80", "0.95", "1.05", "1.20"]:
        q = Decimal(q_text)
        t = q - 1
        z = sum((q * dlog(x)).exp() for x in p)
        s = t / q
        aa = sum(dec(p[i]) * (s * dlog(w[i])).exp() for i in range(1 << n))
        B = q * aa.ln()
        E = (z.ln() - B) / t
        upper = D + Decimal(2880 * n) * Lambda * Lambda * abs(t)
        diagnostics.append({
            "q": q_text,
            "exact_remainder_slope_E_decimal": str(E),
            "KL_decimal": str(D),
            "proved_upper_decimal": str(upper),
            "nonnegative": E >= 0,
            "below_proved_upper": E <= upper,
        })

    payload = {
        "certificate_type": "finite_coupled_DPP_exact_algebra_and_floating_real_q_diagnostic",
        "classification": {
            "exact": "all fields under exact_checks and exact_ranges",
            "floating_diagnostic_only": "entropy, KL, and q-grid values",
        },
        "example": {
            "Q": [[ftxt(x) for x in row] for row in qmat],
            "a": ftxt(a),
            "c": ftxt(c),
            "spectral_strip_delta_certified_by_Gershgorin": ftxt(delta),
            "block_partition": blocks,
        },
        "exact_checks": exact_checks,
        "exact_ranges": {
            "p_atom_min": ftxt(min(p)),
            "p_atom_max": ftxt(max(p)),
            "p_flip_ratio_min": ftxt(min(adjacent_ratios)),
            "p_flip_ratio_max": ftxt(max(adjacent_ratios)),
            "w_flip_ratio_min": ftxt(min(w_adjacent_ratios)),
            "w_flip_ratio_max": ftxt(max(w_adjacent_ratios)),
            "likelihood_flip_ratio_min": ftxt(min(lr_adjacent_ratios)),
            "likelihood_flip_ratio_max": ftxt(max(lr_adjacent_ratios)),
            "theorem_single_log_ratio_interval": [ftxt(lo_ratio), ftxt(hi_ratio)],
            "theorem_likelihood_ratio_interval": [ftxt(lo_ratio**2), ftxt(hi_ratio**2)],
        },
        "floating_diagnostic": {
            "H_decimal": str(H),
            "KL_decimal": str(D),
            "Lambda_decimal": str(Lambda),
            "q_grid": diagnostics,
        },
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
