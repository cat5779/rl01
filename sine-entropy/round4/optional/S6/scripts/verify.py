#!/usr/bin/env python3
"""Reproduce S6 exact finite certificates; standard library only.

Run from the bundle root:
    python scripts/verify.py
or supply --output-dir output/reproduction-name.  No frozen evidence file is
modified.  Existing nonempty output directories and paths inside evidence/
are rejected.  Rational assertions, not displayed decimals, certify signs.
"""
from __future__ import annotations
import argparse
import datetime as dt
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import sys
import time

from exact_arithmetic import (QC, Jet, adjoint, berezin_replica_polynomial,
    determinant, eye, iadd, inverse, iscale, isum, log_interval, matmul, principal)

ROOT = Path(__file__).resolve().parent.parent


def rational(x: F) -> str:
    return f"{x.numerator}/{x.denominator}"


def coarse_interval(interval: tuple[F, F], digits: int = 8) -> dict:
    scale = 10**digits
    lo = F(math.floor(interval[0]*scale), scale)
    hi = F(math.ceil(interval[1]*scale), scale)
    return {"lower": rational(lo), "upper": rational(hi),
            "decimal_lower": finite_decimal(lo, digits),
            "decimal_upper": finite_decimal(hi, digits),
            "status": "exact outward rational enclosure"}


def finite_decimal(x: F, digits: int) -> str:
    y = x*10**digits
    if y.denominator != 1:
        raise ValueError("Not a finite decimal at requested precision")
    integer = y.numerator
    sign = "-" if integer < 0 else ""
    integer = abs(integer)
    return f"{sign}{integer // 10**digits}.{integer % 10**digits:0{digits}d}"


def interval_full(interval: tuple[F, F]) -> dict:
    return {"rational_lower": rational(interval[0]),
            "rational_upper": rational(interval[1]),
            "display": coarse_interval(interval)}


def run() -> dict:
    n = 4
    a, c = F(1, 40), F(19, 20)
    u = [[QC(F(1, 2)), z*F(1, 2)]
         for z in [QC(1), QC(0, 1), QC(-1), QC(0, -1)]]
    pmat = matmul(u, adjoint(u))
    assert matmul(adjoint(u), u) == eye(2)
    assert matmul(pmat, pmat) == pmat
    assert pmat == adjoint(pmat)
    assert sum(pmat[i][i].real() for i in range(n)) == 2
    k = [[a*int(i == j)+c*pmat[i][j] for j in range(n)] for i in range(n)]
    imk = [[int(i == j)-k[i][j] for j in range(n)] for i in range(n)]
    ell = matmul(k, inverse(imk))
    g = inverse(ell)
    dnorm = determinant(imk).real()
    assert dnorm == F(1521, 2560000)
    assert determinant(ell).real() == 1
    assert all(k[i][i].real() == F(1, 2) for i in range(n))

    latent = {}
    for occupied in itertools.combinations(range(n), 2):
        mask = sum(1 << i for i in occupied)
        minor = determinant([u[i][:] for i in occupied])
        latent[mask] = minor.abs2()
    assert sum(latent.values()) == 1
    assert sorted(latent.values()) == [F(1,8)]*4+[F(1,4)]*2

    lminors = {s: determinant(principal(ell, s)).real() for s in range(1 << n)}
    kminors = {s: determinant(principal(k, s)).real() for s in range(1 << n)}
    atoms = {}
    jets = {}
    table = []
    full = (1 << n)-1
    for s in range(1 << n):
        jet = Jet(F(0))
        for latent_mask, weight in latent.items():
            term = Jet(F(1))
            for i in range(n):
                success = a+c*((latent_mask >> i) & 1)
                if (s >> i) & 1:
                    factor = Jet(success, F(1))
                else:
                    factor = Jet(1-success, F(-1))
                term = term*factor
            jet = jet+term.scale(weight)
        inc_exc = F(0)
        comp = full ^ s
        b = comp
        while True:
            inc_exc += (-1)**b.bit_count()*kminors[s | b]
            if b == 0:
                break
            b = (b-1) & comp
        assert jet.v == inc_exc == dnorm*lminors[s]
        assert jet.v > 0
        atoms[s], jets[s] = jet.v, jet
        table.append({"mask": s, "occupied_sites": [i for i in range(n) if (s >> i) & 1],
                      "p": rational(jet.v), "p_prime": rational(jet.d1),
                      "p_second": rational(jet.d2), "L_minor": rational(lminors[s])})
    assert sum(atoms.values()) == 1
    assert sum(j.d1 for j in jets.values()) == 0
    assert sum(j.d2 for j in jets.values()) == 0
    numerators = sorted(int(p*2560000) for p in atoms.values())
    assert numerators == sorted([1521]*2+[29679]*8+[290321]*4+[579121]*2)

    # Independent Grassmann coefficient extraction: not a determinant expansion.
    coefficients, stats = berezin_replica_polynomial(ell, 2)
    expected = [sum(lminors[full ^ mask]**2 for mask in range(1 << n)
                    if mask.bit_count() == degree) for degree in range(n+1)]
    assert coefficients == expected
    m2 = sum(l*l for l in lminors.values())
    assert sum(coefficients) == m2
    z2 = sum(p*p for p in atoms.values())
    assert z2 == dnorm**2*m2
    one_replica, _ = berezin_replica_polynomial(ell, 1)
    assert dnorm*sum(one_replica) == 1

    # Independent discrete auxiliary-field identity (paper Eq. 31).
    sign_det_sum = F(0)
    for signs in itertools.product([-1, 1], repeat=n):
        shifted = [[ell[i][j]+int(i == j)*signs[i] for j in range(n)] for i in range(n)]
        sign_det_sum += determinant(shifted).real()**2
    assert sign_det_sum/F(2**n) == m2

    diag = [g[i][i].real() for i in range(n)]
    assert diag == [F(761,39)]*n
    mean_v = sum(x*x for x in diag)
    variance = -sum(x**4 for x in diag)
    for i in range(n):
        for j in range(n):
            if i != j:
                x = g[i][j].abs2()
                variance += x*x-2*diag[i]*diag[j]*x
                assert 0 <= x <= diag[i]*diag[j]
    log_second = 2*coefficients[2]/coefficients[0]-(coefficients[1]/coefficients[0])**2
    assert log_second == variance
    assert variance <= -sum(x**4 for x in diag) < 0
    assert coefficients[1]/coefficients[0] == mean_v

    # A rigorous, simple extensive gap, valid for every even n at these a,c.
    x = F(761,39)**2
    lower_gap_per_site = x*x/(2*(1+x))
    assert lower_gap_per_site > 180
    # Exact rational enclosure of the actual four-site logarithmic error.
    trial_gap = iadd((mean_v, mean_v), iscale(F(-1), log_interval(m2)))
    assert trial_gap[0] > 4*lower_gap_per_site > 720

    entropy = isum(iscale(-p, log_interval(p)) for p in atoms.values())
    fisher = sum(j.d1*j.d1/j.v for j in jets.values())
    acceleration = isum(iscale(-j.d2, log_interval(j.v)) for j in jets.values())
    entropy_second = iadd(acceleration, (-fisher, -fisher))
    assert entropy_second[1] < 0

    # At q=1 the repaired product-Holder tangent is -sum b(K_ii).
    product_entropy = iscale(F(4), log_interval(F(2)))
    product_gap = iadd(product_entropy, iscale(F(-1), entropy))
    delta = c*c/8  # cyclic P_4,2; NOT the true Toeplitz rho=1/2 value c^2/pi^2.
    pair_probs = [F(1,4)-delta, F(1,4)+delta, F(1,4)+delta, F(1,4)-delta]
    pair_entropy = isum(iscale(-p, log_interval(p)) for p in pair_probs)
    pair_mi = iadd(iscale(F(2), log_interval(F(2))), iscale(F(-1), pair_entropy))
    assert pair_mi[0] >= 8*delta*delta
    assert product_gap[0] > 2*pair_mi[1]

    # Cauchy-Schwarz repair for density-only MF, at z_i=1.
    shifted = [[ell[i][j]+int(i == j) for j in range(n)] for i in range(n)]
    repaired_m2_bound = determinant(shifted).real()**2/F(2**n)
    assert m2 >= repaired_m2_bound
    assert dnorm**2*repaired_m2_bound == F(1,16)

    return {
        "status": "exact finite certificate; all assertions passed",
        "scope": "P_{4,2}, a=1/40, c=19/20; exact rational and rational-log enclosures",
        "parameters": {"n": n, "k": 2, "a": rational(a), "c": rational(c)},
        "normalization_D": rational(dnorm),
        "latent_weights": [{"mask": mask, "weight": rational(weight)} for mask, weight in latent.items()],
        "atoms_and_derivatives": table,
        "field_polynomial_coefficients_in_t": [rational(v) for v in coefficients],
        "grassmann_statistics": stats,
        "M_2_L": rational(m2), "Z_2": rational(z2),
        "gaussian_trial_mean_V": rational(mean_v),
        "gaussian_trial_variance_V": rational(variance),
        "universal_Fourier_log_gap_lower_bound_per_site": rational(lower_gap_per_site),
        "four_site_log_trial_overestimate": interval_full(trial_gap),
        "H_4": interval_full(entropy), "Fisher": rational(fisher),
        "negative_acceleration_log_term": interval_full(acceleration),
        "H_4_second_derivative": interval_full(entropy_second),
        "product_site_entropy_minus_H_4": interval_full(product_gap),
        "cyclic_pair_delta": rational(delta), "cyclic_pair_mutual_information": interval_full(pair_mi),
        "repaired_Cauchy_Schwarz_normalized_Z2_lower_bound": "1/16",
        "log_enclosure_terms": 40,
        "no_floating_sign_tests": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    out = (args.output_dir if args.output_dir else ROOT/"output"/stamp).resolve()
    frozen = (ROOT/"evidence").resolve()
    if out == frozen or frozen in out.parents:
        parser.error("Refusing to write into frozen evidence/")
    if out.exists() and any(out.iterdir()):
        parser.error("Refusing to overwrite a nonempty output directory")
    out.mkdir(parents=True, exist_ok=True)
    start = time.perf_counter()
    result = run()
    result["run_metadata"] = {
        "utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "elapsed_seconds": time.perf_counter()-start,
        "python": sys.version, "platform": platform.platform(),
        "third_party_dependencies": [],
        "scripts_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                           for p in sorted((ROOT/"scripts").glob("*.py"))},
    }
    (out/"certificate.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    summary = {"status": result["status"], "Z_2": result["Z_2"],
               "H_4_second_derivative": result["H_4_second_derivative"]["display"],
               "log_trial_overestimate": result["four_site_log_trial_overestimate"]["display"],
               "output_directory": str(out)}
    (out/"summary.json").write_text(json.dumps(summary, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
