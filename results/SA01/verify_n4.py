#!/usr/bin/env python3
"""SA01: a tiny exact check on the genuine cyclic projection P_(4,2).

Standard library only. Enumerates 6 input states and 16 output states.
Theorems valid for all dimensions are proved in REPORT.md, not inferred here.
All assertions use fractions.Fraction; logarithms appear only in a separately
labelled, non-certifying diagnostic. No hashes, parameter scan, optimization,
or old six-site certificate is used.

Run:
    python verify_n4.py
    python verify_n4.py --output n4_results.json
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import combinations, product
import json
from math import factorial, log
from pathlib import Path

Bits = tuple[int, ...]
Pair = tuple[int, int]
UV = ((0, 0), (1, 0), (0, 1), (1, 1))
N = 4
A_OFFSET = F(1, 40)
C = F(19, 20)
CHANNEL_HIGH = 1 - A_OFFSET
OMEGA = CHANNEL_HIGH / A_OFFSET
TAU = A_OFFSET * CHANNEL_HIGH
E_WEIGHT = C / TAU
GAMMA = F(9, 5)
S_STAR = (1 - C * C) / 2
S_MAX = (1 + C * C) / 2
B_GEO = 4 * GAMMA * (GAMMA - 1) * E_WEIGHT**2 / OMEGA
PAIRS = tuple(combinations(range(N), 2))


def require(condition: bool, description: str) -> None:
    """Do not disable exact checks when Python is run with -O."""
    if not condition:
        raise AssertionError(description)


def record(value: F) -> dict[str, str | float]:
    return {"fraction": str(value), "decimal": float(value)}


def likelihood(x: Bits, y: Bits, indices: tuple[int, ...]) -> F:
    value = F(1)
    for i in indices:
        value *= CHANNEL_HIGH if x[i] == y[i] else A_OFFSET
    return value


def chi(h: F) -> F:
    require(h >= 0, "chi input must be nonnegative")
    return min(
        GAMMA - 1,
        2 * GAMMA * (GAMMA - 1) * h / (1 + 2 * (GAMMA - 1) * h),
    )


def filled(pair: Pair, exterior: Bits, uv: tuple[int, int]) -> Bits:
    remaining = tuple(k for k in range(N) if k not in pair)
    y = [0] * N
    y[pair[0]], y[pair[1]] = uv
    for k, value in zip(remaining, exterior):
        y[k] = value
    return tuple(y)


def check_compression(
    q_i: F, q_j: F, w_ij: F, delta: F, description: str
) -> None:
    """Exact 2x2 PSD tests for delta I <= R_S <= (1-delta) I."""
    require(q_i >= delta and q_j >= delta, description + ": lower diagonal")
    require((q_i - delta) * (q_j - delta) >= w_ij,
            description + ": lower determinant")
    require(q_i <= 1 - delta and q_j <= 1 - delta,
            description + ": upper diagonal")
    require((1 - delta - q_i) * (1 - delta - q_j) >= w_ij,
            description + ": upper determinant")


def run() -> dict:
    # Algebraic certificates for the two continuum scalar lemmas.
    require(1263**2 < 1596001 < 1264**2, "gamma=9/5 root brackets")
    exp_lower_9_4 = sum((F(9, 4)**k / factorial(k) for k in range(7)), F(0))
    require(exp_lower_9_4 > F(1088, 117), "exp(9/4) lower bound")
    require(F(3249 + 1263, 2000) - F(9, 4) == F(3, 500),
            "gamma=9/5 critical-value margin")
    require(21**2 < 463 < 22**2, "gamma=7/4 root brackets")
    exp_lower_17_8 = sum((F(17, 8)**k / factorial(k) for k in range(7)), F(0))
    require(exp_lower_17_8 > F(58, 7), "exp(17/8) lower bound")
    require(F(14, 9) + F(21, 36) - F(17, 8) == F(1, 72),
            "gamma=7/4 critical-value margin")

    delta_exterior = F(1, 1 + 6 * OMEGA)
    h_min = 2 * delta_exterior * (1 - delta_exterior)
    s_min = S_STAR + C**2 * h_min
    require(delta_exterior == F(1, 235), "neutral exterior spectral constant")
    require(s_min == F(2491671, 44180000) and s_min > F(1, 18),
            "sine/Fourier geometric margin")
    delta_full = F(1, 1 + 6 * OMEGA**2)
    alpha_full = delta_full * (1 - delta_full)
    v_min = OMEGA**2 / (1 + OMEGA**2)**2

    ys = tuple(product((0, 1), repeat=N))
    xs = tuple(x for x in ys if sum(x) == 2)
    mu: dict[Bits, F] = {}
    for x in xs:
        occupied = [i for i, bit in enumerate(x) if bit]
        # P_(4,2)[j,k] = (1 + i**(j-k))/4. A size-two determinant
        # is 1/8 on adjacent pairs and 1/4 on opposite pairs.
        distance = (occupied[1] - occupied[0]) % N
        mu[x] = F(1, 4) if distance == 2 else F(1, 8)
    require(sum(mu.values(), F(0)) == 1, "input normalization")

    py: dict[Bits, F] = {}
    posterior: dict[Bits, dict] = {}
    full_indices = tuple(range(N))
    for y in ys:
        joint = {x: mu[x] * likelihood(x, y, full_indices) for x in xs}
        py[y] = sum(joint.values(), F(0))
        require(py[y] > 0, "positive output atom")
        nu = {x: joint[x] / py[y] for x in xs}
        q = [sum((nu[x] * x[i] for x in xs), F(0)) for i in range(N)]
        v = [q[i] * (1 - q[i]) for i in range(N)]
        w: dict[Pair, F] = {}
        h: dict[Pair, F] = {}
        for i, j in PAIRS:
            p11 = sum((nu[x] * x[i] * x[j] for x in xs), F(0))
            w[i, j] = q[i] * q[j] - p11
            h[i, j] = sum((nu[x] for x in xs if x[i] == x[j]), F(0))
            require(w[i, j] >= 0, "DPP negative covariance")
            require(h[i, j] == 1 - q[i] - q[j] + 2*q[i]*q[j] - 2*w[i, j],
                    "input equality identity")

        def edge(i: int, j: int) -> F:
            return w[tuple(sorted((i, j)))]

        m = [sum((edge(i, j) for j in range(N) if i != j), F(0))
             for i in range(N)]
        require(m == v, "posterior projection row-energy identity")
        overlap = sum(
            (m[i]**2 - sum((edge(i, j)**2 for j in range(N) if j != i), F(0))
             for i in range(N)), F(0)
        )
        frustration = sum((w[p] * h[p] for p in PAIRS), F(0))
        balance = sum((w[i, j] * (q[i]+q[j]-1)**2 for i, j in PAIRS), F(0))
        require(frustration == overlap + balance, "exact rigidity decomposition")
        require(overlap >= alpha_full * sum(v, F(0)),
                "uniform overlap-star bound")
        require(overlap >= F(1, 8)/OMEGA**10,
                "dimension-independent positive-field stability consequence")
        for i in range(N):
            require(F(1, 1+OMEGA**2) <= q[i] <= OMEGA**2/(1+OMEGA**2),
                    "one-site leverage bound")
        for i, j in PAIRS:
            geometric_h = (q[i]+q[j]-1)**2 + sum(
                (edge(i, k)+edge(j, k) for k in range(N) if k not in (i, j)), F(0)
            )
            require(h[i, j] == geometric_h, "pointwise overlapping-pair identity")
            check_compression(q[i], q[j], w[i, j], delta_full,
                              "full-posterior two-site bound")
        posterior[y] = {"nu": nu, "q": q, "v": v, "w": w, "h": h,
                        "W": overlap, "J": frustration}

    require(sum(py.values(), F(0)) == 1, "output normalization")
    psi = E_WEIGHT**2 * sum(
        (py[y] * sum(posterior[y]["v"], F(0)) for y in ys), F(0)
    )
    pair_mass = E_WEIGHT**2 * sum(
        (py[y] * sum(posterior[y]["w"].values(), F(0)) for y in ys), F(0)
    )
    missing_energy = psi - 2 * pair_mass
    require(missing_energy == 0, "fixed-count midpoint tangent is zero")
    expected_W = sum((py[y] * posterior[y]["W"] for y in ys), F(0))
    expected_J = sum((py[y] * posterior[y]["J"] for y in ys), F(0))

    T = F(0)
    T_harmonic = F(0)
    T_squared = F(0)
    table_sum = F(0)
    external_coefficients: dict[tuple[Pair, Bits], F] = {}
    lambda_sum_float = 0.0
    counterexample = None
    for pair in PAIRS:
        remaining = tuple(k for k in range(N) if k not in pair)
        for exterior in product((0, 1), repeat=N-2):
            y_uv = {uv: filled(pair, exterior, uv) for uv in UV}
            exterior_mass = sum((py[y_uv[uv]] for uv in UV), F(0))
            cells = {uv: py[y_uv[uv]]/exterior_mass for uv in UV}
            a00, a10, a01, a11 = (cells[uv] for uv in UV)
            d = a10*a01 - a00*a11
            require(d >= 0 and sum(cells.values(), F(0)) == 1,
                    "actual conditional table legality")
            odds = a10*a01/(a00*a11)
            Gamma = d * sum((1/cells[uv] for uv in UV), F(0))
            Delta = d*d/(a00*a10*a01*a11)
            s = a00+a11
            h = (s-S_STAR)/C**2
            require(0 <= h <= 1, "extrinsic input equality range")
            h_direct_num = F(0)
            for x in xs:
                if x[pair[0]] == x[pair[1]]:
                    sample_y = y_uv[(0, 0)]
                    h_direct_num += mu[x]*likelihood(x, sample_y, remaining)
            require(h == h_direct_num/exterior_mass, "true extrinsic equality")
            require(h >= h_min and s >= F(1, 18), "uniform geometric equal-mass bound")
            q_i = (a10+a11-A_OFFSET)/C
            q_j = (a01+a11-A_OFFSET)/C
            check_compression(q_i, q_j, d/C**2, delta_exterior,
                              "neutral-exterior two-site bound")

            rebased = F(0)
            for uv in UV:
                y = y_uv[uv]
                post = posterior[y]
                w = post["w"][pair]
                h_y = post["h"][pair]
                require(E_WEIGHT**2*w == d/cells[uv]**2, "exact posterior rebasing")
                rebased += cells[uv]*E_WEIGHT**2*w
                require(h_y <= OMEGA*h/(1+(OMEGA-1)*h), "Bayes event-odds bound")
                require(chi(h) >= 2*GAMMA*(GAMMA-1)/OMEGA*h_y,
                        "nonlinear scalar-to-posterior transfer")
            require(rebased == Gamma, "actual conditional average of correlation")
            harmonic = chi(h)*Gamma
            squared = GAMMA*C**2*h*Delta
            external_coefficients[pair, exterior] = (
                max(harmonic, squared)/Gamma if Gamma else F(0)
            )
            T_harmonic += 2*exterior_mass*harmonic
            T_squared += 2*exterior_mass*squared
            T += 2*exterior_mass*max(harmonic, squared)
            table_sum += 2*exterior_mass*Gamma
            lambda_sum_float += 2*float(exterior_mass)*log(float(odds))

            if pair == (0, 1) and exterior == (0, 0):
                expected = tuple(F(k, 351200) for k in (1521, 29679, 29679, 290321))
                require(tuple(cells[uv] for uv in UV) == expected,
                        "explicit legal counterexample table")
                false_rhs = 2*C**2/S_MAX*h*Gamma
                log_lower = 2*(odds-1)/(odds+1)
                false_margin_upper = 2*Gamma-false_rhs-log_lower
                require(false_margin_upper < -F(1, 3), "rational disproof margin")
                counterexample = {
                    "status": "DISPROVED_LOCAL_LEMMA",
                    "pair_zero_based": [0, 1],
                    "exterior": [0, 0],
                    "cells_A00_A10_A01_A11": [str(cells[uv]) for uv in UV],
                    "exterior_probability": record(exterior_mass),
                    "h_exterior": record(h),
                    "Gamma": record(Gamma),
                    "odds_ratio": record(odds),
                    "false_rhs": record(false_rhs),
                    "log_lower_bound": record(log_lower),
                    "false_margin_upper_bound": record(false_margin_upper),
                }

    adaptive_wedges = F(0)
    adaptive_balance = F(0)
    for y in ys:
        post = posterior[y]
        weights: dict[Pair, F] = {}
        for pair in PAIRS:
            remaining = tuple(k for k in range(N) if k not in pair)
            exterior = tuple(y[k] for k in remaining)
            coefficient = external_coefficients[pair, exterior]
            h_y = post["h"][pair]
            if not h_y:
                require(coefficient == 0, "zero-event adaptive coefficient")
                weights[pair] = F(0)
            else:
                weights[pair] = coefficient/h_y
                require(weights[pair] <= F(6498, 5),
                        "adaptive weights have a uniform finite upper bound")
        wedge_value = F(0)
        for i in range(N):
            leaves = tuple(k for k in range(N) if k != i)
            for j, k in combinations(leaves, 2):
                ij = tuple(sorted((i, j)))
                ik = tuple(sorted((i, k)))
                wedge_value += (weights[ij]+weights[ik])*post["w"][ij]*post["w"][ik]
        balance_value = sum(
            (weights[i, j]*post["w"][i, j]*(post["q"][i]+post["q"][j]-1)**2
             for i, j in PAIRS), F(0)
        )
        weighted_J = sum(
            (weights[pair]*post["w"][pair]*post["h"][pair] for pair in PAIRS), F(0)
        )
        require(weighted_J == wedge_value+balance_value,
                "exact adaptive weighted rigidity decomposition")
        adaptive_wedges += py[y]*wedge_value
        adaptive_balance += py[y]*balance_value
    T_overlap = 2*E_WEIGHT**2*adaptive_wedges
    T_balance = 2*E_WEIGHT**2*adaptive_balance
    require(T_overlap+T_balance == T, "adaptive allocation spends exactly T")
    require(T_overlap >= B_GEO*expected_W, "adaptive overlap retains uniform guarantee")
    require(T_overlap > 32, "finite geometric-only payment lower bound")

    M = psi-missing_energy
    require(table_sum == M, "spatial pair sum matches Psi-minus-E")
    require(T >= B_GEO*expected_J >= B_GEO*expected_W, "structural payment chain")
    L = F(1, 5)*M + max(T, F(1, 20)*M)
    complete_budget = F(N, 1)/TAU
    hessian_upper = 2*psi-missing_energy-L-complete_budget
    hessian_overlap_upper = GAMMA*psi-(GAMMA-1)*missing_energy-T_overlap-complete_budget
    require(GAMMA*psi-complete_budget < 11, "finite residual budget upper bound")
    require(hessian_overlap_upper < -21, "overlap-only finite consequence")
    require(T == F(29416022942438399308, 634555434772830493),
            "frozen exact new table certificate")
    require(hessian_upper == -F(67558913439941061604, 1903666304318491479),
            "frozen exact new Hessian upper bound")
    require(hessian_upper < -35, "finite-dimensional consequence of the proved tool")
    all_zero = (0,)*N
    all_one = (1,)*N
    require(py[all_zero] == py[all_one] == TAU**2, "neutral full-output probabilities")
    require(posterior[all_zero]["W"] == posterior[all_one]["W"] == F(1, 8),
            "overlap survives vanishing common tangent")
    two_output_certificate = B_GEO*2*TAU**2*F(1, 8)
    require(two_output_certificate == F(1083, 32500), "two-output finite certificate")
    require(counterexample is not None, "counterexample was constructed")

    return {
        "status": "PASS_EXACT_N4_CHECKS",
        "scope": {
            "input": "genuine contiguous-frequency cyclic projection P_(4,2)",
            "a": str(A_OFFSET), "c": str(C),
            "input_states": len(xs), "output_states": len(ys),
            "proof_location": "REPORT.md",
            "not_a_proof_of": "growing-dimension entropy concavity or an entropy-rate limit",
        },
        "continuum_lemma_rational_checks": {
            "exp_9_4_partial_sum": record(exp_lower_9_4),
            "exp_17_8_partial_sum": record(exp_lower_17_8),
            "neutral_delta": record(delta_exterior),
            "h_min": record(h_min), "s_min": record(s_min),
            "full_delta": record(delta_full),
        },
        "exact_new_certificate": {
            "Psi": record(psi), "E": record(missing_energy),
            "expected_W": record(expected_W), "expected_J": record(expected_J),
            "B_geometry": record(B_GEO),
            "T_harmonic": record(T_harmonic),
            "T_squared": record(T_squared), "T_envelope": record(T),
            "T_adaptive_overlap": record(T_overlap),
            "T_adaptive_balance": record(T_balance),
            "H_second_derivative_overlap_only_upper_bound": record(hessian_overlap_upper),
            "L_SA01": record(L), "complete_budget": record(complete_budget),
            "H_second_derivative_upper_bound": record(hessian_upper),
            "two_output_structural_certificate": record(two_output_certificate),
            "uniform_overlap_payment_per_site": record(
                B_GEO*alpha_full*v_min
            ),
            "uniform_total_reserve_per_site": record(F(1, 4)*(F(760, 761)**2)),
        },
        "legal_counterexample": counterexample,
        "diagnostic_float_NOT_USED_FOR_PROOF": {
            "A_acceleration": lambda_sum_float,
            "R_2": 2*float(psi)-float(missing_energy)-lambda_sum_float,
            "H_second_derivative": lambda_sum_float+float(missing_energy)-float(complete_budget),
            "note": "These logarithmic floating values certify no sign or error bound.",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="optional JSON output path")
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
        print(f"Wrote exact-check results to {args.output}")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
