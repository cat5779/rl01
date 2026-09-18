#!/usr/bin/env python3
"""Finite algebra checks for S51 endpoint renormalization.

The sine tests use true finite Toeplitz compressions and RETAIN projection
leakage.  A separate finite cyclic orthogonal projection is used only to
check exact projection algebra; it is not a surrogate proof for the sine
entropy rate.  Floating-point checks are not independent certification.
"""
from __future__ import annotations

from dataclasses import dataclass
import json
import math
from pathlib import Path
import numpy as np
from numpy.typing import NDArray

Array = NDArray[np.complex128]


def real(z: complex | float, tolerance: float = 2e-8) -> float:
    if abs(float(np.imag(z))) > tolerance * max(1.0, abs(z)):
        raise ArithmeticError(f"Unexpected imaginary part: {z}")
    return float(np.real(z))


def sine_block(n: int) -> Array:
    delta = np.arange(n)[:, None] - np.arange(n)[None, :]
    return (0.5 * np.sinc(delta / 2)).astype(complex)


def cyclic_projection(n: int = 6) -> Array:
    if n % 2:
        raise ValueError("Use even n.")
    j = np.arange(n)[:, None]
    k = np.arange(n // 2)[None, :]
    U = np.exp(2j * np.pi * j * k / n) / math.sqrt(n)
    return U @ U.conj().T


def atom_and_score(K: Array, bits: list[int], direction: Array) -> tuple[float, float]:
    n = len(bits)
    if n == 0:
        return 1.0, 0.0
    B = K - np.diag(1 - np.asarray(bits))
    p = real(((-1) ** (n - sum(bits))) * np.linalg.det(B))
    if p <= 0:
        raise ArithmeticError(f"Nonpositive atom: {p}")
    score = real(np.trace(np.linalg.solve(B, direction)))
    return p, score


def words(n: int):
    for mask in range(1 << n):
        yield mask, [(mask >> k) & 1 for k in range(n)]


def phi(q: NDArray[np.float64]) -> NDArray[np.float64]:
    return (q - 0.5) * (np.log(q) - np.log1p(-q))


def phi1(q: NDArray[np.float64]) -> NDArray[np.float64]:
    return np.log(q) - np.log1p(-q) + (q - 0.5) / (q * (1 - q))


def phi2(q: NDArray[np.float64]) -> NDArray[np.float64]:
    return 0.5 / (q * (1 - q)) ** 2


@dataclass
class AnchorResult:
    mass_error: float
    energy_identity_error: float
    mprime_transport_error: float
    edge_measure_error: float
    v14_average_error: float
    normalized_response_mean: float
    expected_leakage_fraction: float
    gamma: float
    pair_sum: float
    pair_sum_x: float
    F2: float
    fisher_part: float
    nu_mass: float
    min_pair_gap: float


def anchor_check(Q: Array, x: float, anchor: int) -> AnchorResult:
    n = len(Q)
    K = 0.5 * np.eye(n) + x * (Q - 0.5 * np.eye(n))
    T = Q - 0.5 * np.eye(n)
    kappa = (1 - x*x) / 4
    C = [i for i in range(n) if i != anchor]
    m = len(C)
    KC = K[np.ix_(C, C)]
    b = K[C, anchor]
    nw = 1 << m
    w = np.empty(nw)
    q = np.empty(nw)
    qp = np.empty(nw)
    qpp = np.empty(nw)
    score = np.empty(nw)
    score2 = np.empty(nw)
    v = np.empty((nw, m), dtype=complex)
    G = np.empty((nw, m, m), dtype=complex)
    leak = np.empty(nw)
    r = np.empty((nw, m))
    for mask, bits in words(m):
        B = KC - np.diag(1 - np.asarray(bits))
        G[mask] = np.linalg.inv(B)
        v[mask] = G[mask] @ b
        w[mask] = real(((-1)**(m-sum(bits))) * np.linalg.det(B))
        q[mask] = real(K[anchor, anchor] - np.vdot(b, v[mask]))
        qp[mask] = 1 + real(np.vdot(v[mask], v[mask]))
        qpp[mask] = -2 * real(np.vdot(v[mask], G[mask] @ v[mask]))
        score[mask] = real(np.trace(G[mask]))
        score2[mask] = score[mask]**2 - real(np.trace(G[mask] @ G[mask]))
        xi = np.zeros(n, dtype=complex)
        xi[anchor] = 1
        xi[C] = -v[mask]
        leak[mask] = x*x*real(np.vdot(xi, (Q - Q @ Q) @ xi))
        r[mask] = 2*np.asarray(bits)-1 - np.real(np.diag(G[mask]))
    if np.any(q <= 0) or np.any(q >= 1):
        raise ArithmeticError("Posterior outside (0,1).")
    D = q*(1-q)
    ell = np.log(q)-np.log1p(-q)
    f, f1, f2 = phi(q), phi1(q), phi2(q)
    F2 = float(np.dot(w, score2*f + 2*score*f1*qp + f2*qp**2 + f1*qpp))
    fisher = float(np.dot(w, f2*qp**2))
    mp = float(np.dot(w, score*ell + qp/D))

    # Full V14, with every moving-law term included.
    flips = np.asarray([[z ^ (1 << i) for i in range(m)] for z in range(nw)])
    jumps = q[flips]-q[:, None]
    bphi = f[flips]-f[:, None]-f1[:, None]*jumps
    bphi1 = f1[flips]-f1[:, None]-f2[:, None]*jumps
    Bphi = np.sum(r*bphi, axis=1)
    G2diag = np.asarray([np.real(np.diag(g@g)) for g in G])
    v14 = f2 + np.sum(r*bphi1, axis=1) + np.sum(G2diag*bphi, axis=1)
    v14 += np.sum(r*((f1[flips]-f1[:, None])*qp[flips]
                    -f2[:, None]*jumps*qp[:, None]), axis=1)
    v14 += np.sum(r*(Bphi[flips]-Bphi[:, None]), axis=1)

    pair_sum = 0.0
    pair_x = 0.0
    edge_energy = 0.0
    min_gap = math.inf
    for site in C:
        rest = [j for j in range(n) if j not in (anchor, site)]
        for _, zrest in words(n-2):
            masses = np.empty((2, 2))
            scores_x = np.empty((2, 2))
            for a in (0, 1):
                for bb in (0, 1):
                    z = [0]*n
                    z[anchor], z[site] = a, bb
                    for j, zz in zip(rest, zrest):
                        z[j] = zz
                    masses[a, bb], scores_x[a, bb] = atom_and_score(K, z, T)
            W = float(masses.sum())
            pp = masses/W
            gap = pp[1, 0]*pp[0, 1]-pp[0, 0]*pp[1, 1]
            min_gap = min(min_gap, gap)
            jval = math.log(pp[1, 0])+math.log(pp[0, 1])-math.log(pp[0, 0])-math.log(pp[1, 1])
            ee = gap*float(np.sum(1/pp))
            Wx = float(np.sum(masses*scores_x))
            jx = scores_x[1, 0]+scores_x[0, 1]-scores_x[0, 0]-scores_x[1, 1]
            pair_sum += W*jval
            pair_x += Wx*jval+W*jx
            edge_energy += W*ee
    nu = kappa*edge_energy
    leakage_fraction = float(np.dot(w, leak/D))
    nu_rhs = 1-kappa*float(np.dot(w, 1/D))-leakage_fraction
    return AnchorResult(
        mass_error=abs(float(w.sum())-1),
        energy_identity_error=float(np.max(np.abs(D-kappa*qp-leak))),
        mprime_transport_error=abs(mp-(float(np.dot(w, qp/D))-pair_sum)),
        edge_measure_error=abs(nu-nu_rhs),
        v14_average_error=abs(float(np.dot(w, v14))-F2),
        normalized_response_mean=float(np.dot(w, kappa*qp/D)),
        expected_leakage_fraction=leakage_fraction,
        gamma=mp, pair_sum=pair_sum, pair_sum_x=pair_x,
        F2=F2, fisher_part=fisher, nu_mass=nu,
        min_pair_gap=min_gap,
    )


def check_all() -> dict:
    report: dict = {"warning": "Finite floating-point algebra only; not independent certification or an endpoint-limit proof.",
                    "true_sine_compressions": [], "finite_projection_algebra_only": []}
    for n, x in [(5, .6), (5, .95), (7, .99), (5, .9999), (5, .9999999)]:
        r = anchor_check(sine_block(n), x, n//2)
        record = {"n": n, "x": x, **vars(r)}
        report["true_sine_compressions"].append(record)
        assert r.mass_error < 1e-10
        assert r.energy_identity_error < 2e-9
        assert r.mprime_transport_error < 2e-6
        assert r.edge_measure_error < 2e-8
        assert r.v14_average_error < 2e-5
        assert abs(r.normalized_response_mean+r.expected_leakage_fraction-1) < 2e-8
        assert r.min_pair_gap > -1e-10
    P = cyclic_projection(6)
    for x in (.3, .6, .93):
        r = anchor_check(P, x, 0)
        kappa = (1-x*x)/4
        identity_error = abs(r.F2-(1/(2*kappa*kappa)-2*r.pair_sum-x*r.pair_sum_x))
        fisher_error = abs(r.fisher_part-1/(2*kappa*kappa))
        report["finite_projection_algebra_only"].append({
            "n": 6, "x": x, "projection_defect": float(np.linalg.norm(P@P-P)),
            "renormalized_identity_error": identity_error,
            "fisher_identity_error": fisher_error, **vars(r)})
        assert r.energy_identity_error < 1e-10
        assert abs(r.normalized_response_mean-1) < 1e-10
        assert abs(r.gamma-(1/kappa-r.pair_sum)) < 1e-8
        assert identity_error < 1e-7
        assert fisher_error < 1e-8
    return report


if __name__ == "__main__":
    data = check_all()
    out = Path(__file__).with_name("S51_C1_check_results.json")
    out.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(json.dumps(data, indent=2))
