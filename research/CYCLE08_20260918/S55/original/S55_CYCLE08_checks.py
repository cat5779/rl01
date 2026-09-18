#!/usr/bin/env python3
"""Finite diagnostics for S55 cycle08. Numerical checks are not limit proofs.

Run: OPENBLAS_NUM_THREADS=1 python S55_CYCLE08_checks.py
Requires Python 3 and NumPy. Writes S55_CYCLE08_checks_output.json beside itself.
All entropy derivatives below are analytic determinant/transport derivatives,
not derivatives of fitted thermodynamic values.
"""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any
import numpy as np


def require_close(name: str, x: Any, y: Any, tol: float = 2e-8) -> float:
    error = float(np.max(np.abs(np.asarray(x) - np.asarray(y))))
    scale = max(1.0, float(np.max(np.abs(np.asarray(x)))),
                float(np.max(np.abs(np.asarray(y)))))
    if not np.isfinite(error) or error > tol * scale:
        raise AssertionError(f"{name}: error={error:.4g}, scale={scale:.4g}")
    return error


def cyclic_projection(n: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if n < 2 or n % 2:
        raise ValueError("n must be a positive even integer, at least two")
    labels = np.arange(-n // 2, n // 2)
    frequencies = np.arange(n // 2)
    u = np.exp(2j * np.pi * labels[:, None] * frequencies[None, :] / n) / np.sqrt(n)
    p = u @ u.conj().T
    gauge = np.exp(-1j * np.pi * (n // 2 - 1) * labels / n)
    pg = gauge[:, None] * p * gauge.conj()[None, :]
    delta = labels[:, None] - labels[None, :]
    formula = np.zeros((n, n), dtype=float)
    nonzero = delta != 0
    formula[nonzero] = np.sin(np.pi * delta[nonzero] / 2) / (n * np.sin(np.pi * delta[nonzero] / n))
    np.fill_diagonal(formula, 0.5)
    require_close("gauge formula", pg, formula, 2e-12)
    require_close("projection", pg @ pg, pg, 2e-12)
    return labels, p, pg


def sine_block(labels: np.ndarray) -> np.ndarray:
    delta = labels[:, None] - labels[None, :]
    q = np.zeros(delta.shape, dtype=float)
    nonzero = delta != 0
    q[nonzero] = np.sin(np.pi * delta[nonzero] / 2) / (np.pi * delta[nonzero])
    np.fill_diagonal(q, 0.5)
    return q


def signed_transport(p: np.ndarray, n: int) -> np.ndarray:
    words = np.arange(1 << n)
    out = np.zeros_like(p)
    for i in range(n):
        sigma = 2 * ((words >> i) & 1) - 1
        out += sigma * (p + p[words ^ (1 << i)])
    return out


def law_jets(k: np.ndarray) -> dict[str, Any]:
    n = len(k)
    prob = np.empty(1 << n)
    dp = np.empty_like(prob)
    ddp = np.empty_like(prob)
    for word in range(1 << n):
        bits = np.array([(word >> i) & 1 for i in range(n)])
        b = k - np.diag(1 - bits)
        sign, log_abs = np.linalg.slogdet(b)
        atom_sign = (-1) ** int(n - bits.sum()) * sign
        require_close("positive atom sign", atom_sign, 1.0, 2e-10)
        p = float(np.exp(log_abs))
        g = np.linalg.inv(b)
        tr = float(np.trace(g).real)
        tr2 = float(np.trace(g @ g).real)
        prob[word] = p
        dp[word] = p * tr
        ddp[word] = p * (tr * tr - tr2)
    require_close("normalization", prob.sum(), 1.0, 2e-11)
    require_close("first normalization jet", dp.sum(), 0.0, 2e-9)
    require_close("second normalization jet", ddp.sum(), 0.0, 2e-8)
    require_close("complete first transport", dp, signed_transport(prob, n), 2e-9)
    require_close("complete second transport", ddp, signed_transport(dp, n), 2e-8)
    logp = np.log(prob)
    return dict(p=prob, dp=dp, ddp=ddp,
                H=float(-np.dot(prob, logp)),
                H1=float(-np.dot(dp, logp)),
                H2=float(-np.dot(ddp, logp) - np.sum(dp * dp / prob)))


def insert_word(word: int, sites: list[int]) -> int:
    return sum(((word >> j) & 1) << site for j, site in enumerate(sites))


def anchor_response(k: np.ndarray, law: dict[str, Any], anchor: int,
                    midpoint_c: float | None = None,
                    toeplitz_q: np.ndarray | None = None) -> dict[str, Any]:
    n = len(k)
    sites = [j for j in range(n) if j != anchor]
    root_col = k[sites, anchor]
    kc = k[np.ix_(sites, sites)]
    count = 1 << (n - 1)
    weights = np.empty(count)
    qs = np.empty(count)
    avec = np.empty(count)
    vabs2 = np.empty((count, n - 1))
    eig = np.linalg.eigvalsh(k)
    epsilon = float(min(eig.min(), 1 - eig.max()))
    if epsilon <= 0:
        raise ValueError("The diagnostic needs a positive spectral gap")
    max_ward = 0.0
    max_leakage_identity = 0.0
    max_leakage = 0.0
    for word in range(count):
        z = np.array([(word >> j) & 1 for j in range(n - 1)])
        base = insert_word(word, sites)
        one = base | (1 << anchor)
        p0, p1 = law['p'][base], law['p'][one]
        weights[word] = p0 + p1
        q_prob = p1 / (p0 + p1)
        g = np.linalg.inv(kc - np.diag(1 - z))
        v = g @ root_col
        q = float((k[anchor, anchor] - np.vdot(root_col, v)).real)
        a = float(1 + np.vdot(v, v).real)
        require_close("Schur posterior", q, q_prob, 2e-9)
        hprime_prob = law['dp'][one] / p1 - law['dp'][base] / p0
        require_close("fixed-word log-odds derivative", a / (q * (1 - q)), hprime_prob, 2e-8)
        qs[word], avec[word] = q, a
        vabs2[word, :] = np.abs(v) ** 2
        if midpoint_c is not None:
            bscalar = (1 - midpoint_c ** 2) / 4
            residual = q * (1 - q) - bscalar * a
            if toeplitz_q is None:
                max_ward = max(max_ward, abs(residual))
            else:
                x = np.zeros(n, dtype=complex)
                x[anchor] = 1
                x[sites] = -v
                leakage = float((midpoint_c ** 2 * np.vdot(x, (toeplitz_q - toeplitz_q @ toeplitz_q) @ x)).real)
                max_leakage_identity = max(max_leakage_identity, abs(residual - leakage))
                max_leakage = max(max_leakage, leakage)
                if leakage < -2e-9:
                    raise AssertionError("Toeplitz leakage must be nonnegative")
    h = np.log(qs / (1 - qs))
    words = np.arange(count)
    cross_sum = np.zeros(count)
    pair_direct = 0.0
    for pos, other in enumerate(sites):
        ell = h[words & ~(1 << pos)] - h[words | (1 << pos)]
        odds = weights[words ^ (1 << pos)] / weights
        sigma = 2 * ((words >> pos) & 1) - 1
        require_close("rank-one posterior flip", qs[words ^ (1 << pos)] - qs,
                      sigma * vabs2[:, pos] / odds, 2e-9)
        if np.max(ell - vabs2[:, pos] / epsilon ** 2) > 2e-8:
            raise AssertionError("squared-response influence bound failed")
        if ell.min() < -2e-9:
            raise AssertionError("conditional cross-ratio must be nonnegative")
        cross_sum += ell
        remainder = [j for j in range(n) if j not in (anchor, other)]
        direct = 0.0
        for rw in range(1 << (n - 2)):
            base = insert_word(rw, remainder)
            p00 = law['p'][base]
            p10 = law['p'][base | (1 << anchor)]
            p01 = law['p'][base | (1 << other)]
            p11 = law['p'][base | (1 << anchor) | (1 << other)]
            mass = p00 + p10 + p01 + p11
            direct += mass * np.log((p10 * p01) / (p00 * p11))
        require_close("actual pair marginal", direct, np.dot(weights, ell), 2e-9)
        pair_direct += direct
    drift = avec / (qs * (1 - qs))
    result = dict(response=float(np.dot(weights, -drift + cross_sum)),
                  first_response=float(-np.dot(weights, h)),
                  Janchor=float(np.dot(weights, cross_sum)),
                  drift=float(np.dot(weights, drift)),
                  ward_residual=max_ward,
                  leakage_identity_residual=max_leakage_identity,
                  maximum_leakage=max_leakage)
    require_close("sum of actual pair marginals", pair_direct, result['Janchor'], 2e-9)
    if midpoint_c is not None and toeplitz_q is None:
        require_close("finite projection Ward", max_ward, 0.0, 2e-9)
    if toeplitz_q is not None:
        require_close("Toeplitz Ward with leakage", max_leakage_identity, 0.0, 2e-9)
    return result


def run() -> dict[str, Any]:
    cyclic_rows = []
    gauge_rows = []
    for n in (2, 4, 6, 8, 10, 16, 32, 64):
        labels, original, gauged = cyclic_projection(n)
        gauge_rows.append(dict(n=n, projection_error=float(np.linalg.norm(gauged @ gauged - gauged)),
                               imaginary_part=float(np.max(np.abs(gauged.imag)))))
        if n > 10:
            continue
        for c in (0.2, 0.65, 0.95):
            for d in (0.0, 0.2 * (1 - c)):
                k = (0.5 * (1 - c) + d) * np.eye(n) + c * gauged
                law = law_jets(k)
                anchor = int(np.flatnonzero(labels == 0)[0])
                response = anchor_response(k, law, anchor, c if d == 0 else None)
                require_close("cyclic Hessian response", law['H2'] / n, response['response'], 3e-8)
                require_close("cyclic first response", law['H1'] / n, response['first_response'], 3e-8)
                row = dict(n=n, c=c, d=d, H2_per_site=law['H2'] / n, **response)
                if d == 0:
                    b = (1 - c * c) / 4
                    j = response['Janchor']
                    r = c * c / b - j
                    require_close("midpoint identity", law['H2'] / n, -1 / b + j, 3e-8)
                    require_close("R normalization", law['H2'] / n, -4 - r, 3e-8)
                    row['R_per_site'] = r
                    require_close("midpoint first derivative", law['H1'], 0.0, 2e-8)
                    if n == 2:
                        require_close("two-site ordered-pair factor", law['H2'] / 2,
                            -1 / b + 2 * np.log((1 + c*c)/(1 - c*c)), 3e-8)
                cyclic_rows.append(row)
    # Genuine principal Toeplitz blocks: use EVERY anchor, not a center proxy.
    toeplitz_rows = []
    for n in (1, 3, 5, 7):
        q = sine_block(np.arange(n))
        for c, d in ((0.65, 0.0), (0.95, 0.0), (0.65, 0.04)):
            k = (0.5 * (1 - c) + d) * np.eye(n) + c * q
            law = law_jets(k)
            responses = [anchor_response(k, law, i, c if d == 0 else None,
                                          q if d == 0 else None) for i in range(n)]
            total = sum(r['response'] for r in responses)
            require_close("all-anchor Toeplitz Hessian", law['H2'], total, 3e-8)
            require_close("all-anchor Toeplitz first response", law['H1'],
                          sum(r['first_response'] for r in responses), 3e-8)
            toeplitz_rows.append(dict(n=n, c=c, d=d, H2_per_site=law['H2']/n,
                response_per_site=total/n,
                max_leakage=max(r['maximum_leakage'] for r in responses),
                max_leakage_identity_error=max(r['leakage_identity_residual'] for r in responses)))
    # The local-response identity also holds without a projection ansatz.
    rng = np.random.default_rng(5508)
    raw = rng.normal(size=(5, 5)) + 1j * rng.normal(size=(5, 5))
    unitary, _ = np.linalg.qr(raw)
    random_k = unitary @ np.diag(np.linspace(0.14, 0.82, 5)) @ unitary.conj().T
    random_law = law_jets(random_k)
    random_responses = [anchor_response(random_k, random_law, i) for i in range(5)]
    require_close('general gapped Hessian', random_law['H2'],
                  sum(r['response'] for r in random_responses), 3e-8)
    result = dict(status='PASS: finite diagnostics only; not an asymptotic proof',
                  cyclic=cyclic_rows, toeplitz=toeplitz_rows, gauge=gauge_rows,
                  general_gapped_H2=random_law['H2'])
    output = Path(__file__).resolve().with_name('S55_CYCLE08_checks_output.json')
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(result['status'])
    print('c=0.95, d=0:')
    print(' n      Hdd/n                 J_n                  R_n/n')
    for row in cyclic_rows:
        if row['c'] == 0.95 and row['d'] == 0:
            print(f"{row['n']:2d} {row['H2_per_site']:21.12f} {row['Janchor']:21.12f} {row['R_per_site']:21.12f}")
    print(f"{len(cyclic_rows)} cyclic parameter cases; {len(toeplitz_rows)} all-anchor Toeplitz cases.")
    print(f'Wrote {output.name}')
    return result


if __name__ == '__main__':
    run()
