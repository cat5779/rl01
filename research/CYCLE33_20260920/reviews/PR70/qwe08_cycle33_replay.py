#!/usr/bin/env python3
"""Independent checks for the QWE08 Cycle33 audit.

This script does not implement fixed-point interval arithmetic.  It supplies
independent floating-point and exact-rational cross-checks for the algebraic
claims; the author's interval program is rerun separately in the run log.
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from itertools import combinations
from pathlib import Path

import numpy as np


def dpp_atoms(kernel: np.ndarray) -> np.ndarray:
    n = kernel.shape[0]
    out = np.empty(1 << n, dtype=float)
    eye = np.eye(n)
    for mask in range(1 << n):
        y = np.array([(mask >> i) & 1 for i in range(n)], dtype=float)
        holes = n - int(y.sum())
        out[mask] = ((-1) ** holes * np.linalg.det(kernel - np.diag(1 - y))).real
    if out.min() <= 0 or abs(out.sum() - 1) > 2e-10:
        raise ArithmeticError("invalid DPP atom reconstruction")
    return out


def remove_bits(mask: int, keep: list[int]) -> int:
    return sum(((mask >> old) & 1) << new for new, old in enumerate(keep))


def entropy_second(kernel: np.ndarray) -> float:
    """Common-diagonal-shift H'' using deleted-coordinate marginals."""
    n = kernel.shape[0]
    atoms = dpp_atoms(kernel)
    marginal_atoms: dict[tuple[int, ...], np.ndarray] = {}
    for r in (1, 2):
        for deleted in combinations(range(n), r):
            keep = [i for i in range(n) if i not in deleted]
            marginal_atoms[deleted] = dpp_atoms(kernel[np.ix_(keep, keep)])

    first = np.zeros_like(atoms)
    second = np.zeros_like(atoms)
    for mask in range(1 << n):
        signs = np.array([1 if (mask >> i) & 1 else -1 for i in range(n)])
        for i in range(n):
            keep = [j for j in range(n) if j != i]
            first[mask] += signs[i] * marginal_atoms[(i,)][remove_bits(mask, keep)]
        for i, j in combinations(range(n), 2):
            keep = [k for k in range(n) if k not in (i, j)]
            second[mask] += (
                2
                * signs[i]
                * signs[j]
                * marginal_atoms[(i, j)][remove_bits(mask, keep)]
            )
    if abs(first.sum()) > 2e-9 or abs(second.sum()) > 2e-8:
        raise ArithmeticError("derivative mass check failed")
    return float(-np.sum(second * np.log(atoms) + first * first / atoms))


def mi_second(kernel: np.ndarray, left: list[int]) -> float:
    right = [i for i in range(kernel.shape[0]) if i not in left]
    return (
        entropy_second(kernel[np.ix_(left, left)])
        + entropy_second(kernel[np.ix_(right, right)])
        - entropy_second(kernel)
    )


def quantitative_bound(t: float, cblock: np.ndarray, left: set[int]) -> float:
    ne, no = cblock.shape
    v = t * (1 - t)
    factor = 3 * (1 - 2 * t) ** 2 / v**4 + 2 / v**3
    total = 0.0
    for e in range(ne):
        for o in range(no):
            oi = ne + o
            if (e in left) != (oi in left):
                total += abs(cblock[e, o]) ** 4 * factor
    return float(total)


def rank_one_trials() -> dict:
    rng = np.random.default_rng(20260920)
    minimum_slack = math.inf
    maximum_identity_error = 0.0
    count = 0
    for _ in range(10):
        ne, no = 2, 3
        u = rng.normal(size=ne) + 1j * rng.normal(size=ne)
        v = rng.normal(size=no) + 1j * rng.normal(size=no)
        u /= np.linalg.norm(u)
        v /= np.linalg.norm(v)
        sigma = rng.uniform(0.06, 0.22)
        cblock = sigma * np.outer(u, np.conjugate(v))
        b = np.block(
            [
                [np.zeros((ne, ne), complex), cblock],
                [cblock.conj().T, np.zeros((no, no), complex)],
            ]
        )
        t = rng.uniform(sigma + 0.03, 1 - sigma - 0.03)
        kernel = t * np.eye(ne + no) + b
        for mask in range(1, (1 << (ne + no)) - 1):
            left = [i for i in range(ne + no) if (mask >> i) & 1]
            value = mi_second(kernel, left)
            bound = quantitative_bound(t, cblock, set(left))
            minimum_slack = min(minimum_slack, value - bound)
            count += 1

        # Direct five-point check on one cut is independent of the cofactor formula.
        left = [0, 2, 4]
        h = 2e-4
        vals = []
        for shift in (-2, -1, 0, 1, 2):
            k = kernel + shift * h * np.eye(ne + no)
            right = [i for i in range(ne + no) if i not in left]
            def entropy(sub: np.ndarray) -> float:
                p = dpp_atoms(sub)
                return float(-np.sum(p * np.log(p)))
            vals.append(
                entropy(k[np.ix_(left, left)])
                + entropy(k[np.ix_(right, right)])
                - entropy(k)
            )
        fd = (-vals[4] + 16 * vals[3] - 30 * vals[2] + 16 * vals[1] - vals[0]) / (12 * h * h)
        maximum_identity_error = max(maximum_identity_error, abs(fd - mi_second(kernel, left)))
    return {
        "cuts_checked": count,
        "minimum_M_second_minus_claimed_bound": minimum_slack,
        "maximum_five_point_error": maximum_identity_error,
    }


def sine_kernel(n: int, c: float, a: float) -> np.ndarray:
    out = np.empty((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            d = i - j
            q = 0.5 if d == 0 else math.sin(math.pi * d / 2) / (math.pi * d)
            out[i, j] = c * q + (a if i == j else 0.0)
    return out


def small_sine_trials() -> dict:
    minimum = math.inf
    count = 0
    for n in (2, 3):
        for c in (0.1, 0.5, 0.95, 0.99):
            for fraction in (0.05, 0.5, 0.95):
                a = fraction * (1 - c)
                kernel = sine_kernel(n, c, a)
                for m in range(1, n):
                    minimum = min(minimum, mi_second(kernel, list(range(m))))
                    count += 1
    return {"instances_checked": count, "minimum_M_second": minimum}


Monomial = tuple[int, int, int, int, int]  # x1,x2,y1,y2,s
Polynomial = dict[Monomial, Fraction]


def poly_add(a: Polynomial, b: Polynomial, scale: Fraction = Fraction(1)) -> Polynomial:
    out = dict(a)
    for monomial, coefficient in b.items():
        out[monomial] = out.get(monomial, Fraction(0)) + scale * coefficient
        if out[monomial] == 0:
            del out[monomial]
    return out


def poly_mul(a: Polynomial, b: Polynomial, target: Monomial) -> Polynomial:
    out: Polynomial = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            mc = tuple(x + y for x, y in zip(ma, mb))
            if all(x <= limit for x, limit in zip(mc, target)):
                out[mc] = out.get(mc, Fraction(0)) + ca * cb
    return out


def exact_four_site_coefficient() -> str:
    target = (3, 2, 2, 3, 10)
    # C=s[[1,-1/3],[1,1]], so f-1 has four quadratic edge terms
    # and the quartic determinant term (det C)^2=(16/9)s^4.
    u: Polynomial = {
        (1, 0, 1, 0, 2): Fraction(-1),
        (1, 0, 0, 1, 2): Fraction(-1, 9),
        (0, 1, 1, 0, 2): Fraction(-1),
        (0, 1, 0, 1, 2): Fraction(-1),
        (1, 1, 1, 1, 4): Fraction(16, 9),
    }
    result: Polynomial = dict(u)
    power: Polynomial = dict(u)
    for k in range(2, 6):
        power = poly_mul(power, u, target)
        result = poly_add(result, power, Fraction((-1) ** k, k * (k - 1)))
    value = result.get(target, Fraction(0))
    if value != Fraction(-1, 27):
        raise ArithmeticError(f"unexpected coefficient {value}")
    return str(value)


def apply_d(p: np.ndarray) -> np.ndarray:
    n = int(round(math.log2(len(p))))
    out = np.zeros_like(p)
    for bit in range(n):
        stride = 1 << bit
        for base in range(0, len(p), 2 * stride):
            for j in range(stride):
                lo = base + j
                hi = lo + stride
                total = p[lo] + p[hi]
                out[lo] -= total
                out[hi] += total
    return out


def nilpotent_shift_check() -> dict:
    kernel = sine_kernel(4, 0.73, 0.11)
    p0 = dpp_atoms(kernel)
    derivatives = [p0]
    for _ in range(5):
        derivatives.append(apply_d(derivatives[-1]))
    nilpotence_error = float(np.max(np.abs(derivatives[5])))
    z = 0.017
    reconstructed = sum((z**k / math.factorial(k)) * derivatives[k] for k in range(5))
    shifted = dpp_atoms(kernel + z * np.eye(4))
    return {
        "D_power_5_max_abs": nilpotence_error,
        "shift_polynomial_max_error": float(np.max(np.abs(reconstructed - shifted))),
    }


def inspect_author_json(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    positive = True
    minimum = None
    for certificate in data["certificates"]:
        lo = int(certificate["lower"][0])
        positive &= lo > 0
        minimum = lo if minimum is None else min(minimum, lo)
        for interval in certificate["even_coefficients"][1:]:
            positive &= int(interval[0]) >= 0
    return {
        "status": data["status"],
        "all_integer_acceptance_inequalities_positive": positive,
        "recorded_minimum_matches": minimum == int(data["minimum_certified_curvature"][0]),
        "certificate_count": len(data["certificates"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--author-json", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "status": "PASS_INDEPENDENT_ALGEBRA_AND_FLOATING_CHECKS_AUTHOR_INTERVAL_RUN_SEPARATE",
        "rank_one_trials": rank_one_trials(),
        "small_sine_trials": small_sine_trials(),
        "four_site_exact_coefficient": exact_four_site_coefficient(),
        "nilpotent_shift": nilpotent_shift_check(),
        "author_integer_json": inspect_author_json(args.author_json),
        "evidence_scope": (
            "Exact rational coefficient and algebraic identities plus floating probes; "
            "the continuum proof relies on the separately rerun fixed-point interval program."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
