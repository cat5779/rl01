#!/usr/bin/env python3
"""Exact finite certificates for the S4 route obstruction.

Only Python's standard library is required. All probability derivatives use
fractions.Fraction. Logarithms are enclosed by rational atanh-series bounds;
no floating-point number determines a pass/fail result.

Runtime output goes to a NEW directory, never to frozen evidence.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from datetime import datetime, timezone
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path
import platform
import sys
from typing import Iterable


@dataclass(frozen=True)
class Jet:
    """Value, first derivative, and actual second derivative (not Taylor coefficient)."""
    x: F
    d: F = F(0)
    dd: F = F(0)

    def __add__(self, other: Jet) -> Jet:
        return Jet(self.x + other.x, self.d + other.d, self.dd + other.dd)

    def __neg__(self) -> Jet:
        return Jet(-self.x, -self.d, -self.dd)

    def __sub__(self, other: Jet) -> Jet:
        return self + (-other)

    def __mul__(self, other: Jet) -> Jet:
        return Jet(self.x * other.x,
                   self.d * other.x + self.x * other.d,
                   self.dd * other.x + 2 * self.d * other.d + self.x * other.dd)

    def scale(self, c: F) -> Jet:
        return Jet(c * self.x, c * self.d, c * self.dd)

    def inv(self) -> Jet:
        if self.x == 0:
            raise ZeroDivisionError("Cannot invert a jet with zero value")
        return Jet(1 / self.x, -self.d / self.x**2,
                   2 * self.d**2 / self.x**3 - self.dd / self.x**2)

    def __truediv__(self, other: Jet) -> Jet:
        return self * other.inv()

    def json(self) -> list[str]:
        return [str(self.x), str(self.d), str(self.dd)]


def sum_jets(xs: Iterable[Jet]) -> Jet:
    ans = Jet(F(0))
    for x in xs:
        ans = ans + x
    return ans


@lru_cache(maxsize=None)
def factor_integer(n: int) -> tuple[tuple[int, int], ...]:
    """Trial division is sufficient for the small, explicitly enumerated seed."""
    if n < 1:
        raise ValueError("Expected a positive integer")
    factors: list[tuple[int, int]] = []
    p = 2
    while p * p <= n:
        count = 0
        while n % p == 0:
            n //= p
            count += 1
        if count:
            factors.append((p, count))
        p = 3 if p == 2 else p + 2
    if n > 1:
        factors.append((n, 1))
    return tuple(factors)


@dataclass
class LogLinear:
    """Exact rational constant plus a rational linear combination of log(primes)."""
    constant: F = F(0)
    terms: dict[int, F] = field(default_factory=dict)

    @staticmethod
    def log(x: F) -> LogLinear:
        if x <= 0:
            raise ValueError("Logarithm argument must be positive")
        terms: dict[int, F] = {}
        for prime, multiplicity in factor_integer(x.numerator):
            terms[prime] = terms.get(prime, F(0)) + multiplicity
        for prime, multiplicity in factor_integer(x.denominator):
            terms[prime] = terms.get(prime, F(0)) - multiplicity
        return LogLinear(F(0), {p: c for p, c in terms.items() if c})

    def __add__(self, other: LogLinear) -> LogLinear:
        terms = dict(self.terms)
        for p, c in other.terms.items():
            terms[p] = terms.get(p, F(0)) + c
        return LogLinear(self.constant + other.constant,
                         {p: c for p, c in terms.items() if c})

    def __neg__(self) -> LogLinear:
        return self.scale(F(-1))

    def __sub__(self, other: LogLinear) -> LogLinear:
        return self + (-other)

    def scale(self, c: F) -> LogLinear:
        return LogLinear(self.constant * c,
                         {p: v * c for p, v in self.terms.items() if v * c})

    def is_zero(self) -> bool:
        return self.constant == 0 and not self.terms

    def json(self) -> dict:
        return {"constant": str(self.constant),
                "log_prime_coefficients": {str(p): str(c)
                                           for p, c in sorted(self.terms.items())}}


def sum_logs(xs: Iterable[LogLinear]) -> LogLinear:
    ans = LogLinear()
    for x in xs:
        ans = ans + x
    return ans


LogJet = tuple[LogLinear, LogLinear, LogLinear]


def add_logjets(x: LogJet, y: LogJet) -> LogJet:
    return tuple(a + b for a, b in zip(x, y))  # type: ignore[return-value]


def scale_logjet(x: LogJet, c: F) -> LogJet:
    return tuple(a.scale(c) for a in x)  # type: ignore[return-value]


def weight_logjet(p: Jet, x: LogJet) -> LogJet:
    return (x[0].scale(p.x),
            x[0].scale(p.d) + x[1].scale(p.x),
            x[0].scale(p.dd) + x[1].scale(2 * p.d) + x[2].scale(p.x))


def entropy_jet(law: dict[int, Jet]) -> LogJet:
    total = sum_jets(law.values())
    assert total == Jet(F(1)), total
    val = sum_logs(LogLinear.log(p.x).scale(-p.x) for p in law.values())
    der = sum_logs(LogLinear.log(p.x).scale(-p.d) for p in law.values())
    sec = sum_logs(LogLinear.log(p.x).scale(-p.dd) for p in law.values())
    sec.constant -= sum((p.d**2 / p.x for p in law.values()), F(0))
    return val, der, sec


def kl_jet(law: dict[int, Jet], reference: dict[int, Jet]) -> LogJet:
    """KL between TWO moving laws: includes all reference-score derivatives."""
    assert set(law) == set(reference)
    assert sum_jets(law.values()) == Jet(F(1))
    assert sum_jets(reference.values()) == Jet(F(1))
    val, der, sec = LogLinear(), LogLinear(), LogLinear()
    for state, r in law.items():
        s = reference[state]
        v, w = r.d / r.x, s.d / s.x
        log_ratio = LogLinear.log(r.x) - LogLinear.log(s.x)
        val = val + log_ratio.scale(r.x)
        der = der + log_ratio.scale(r.d)
        der.constant -= r.x * w
        sec = sec + log_ratio.scale(r.dd)
        sec.constant += r.x * ((v - w)**2 - s.dd / s.x)
    return val, der, sec


def likelihood(A: int, Y: int, n_observed: int, a: F, c: F) -> Jet:
    ans = Jet(F(1))
    for i in range(n_observed):
        theta = a + c * ((A >> i) & 1)
        bit = Jet(theta, F(1)) if (Y >> i) & 1 else Jet(1 - theta, F(-1))
        ans = ans * bit
    return ans


def channel(mu: dict[int, F], n: int, a: F, c: F) -> tuple[dict[int, Jet], dict[int, dict[int, Jet]]]:
    out: dict[int, Jet] = {}
    post: dict[int, dict[int, Jet]] = {}
    for y in range(1 << n):
        joint = {A: likelihood(A, y, n, a, c).scale(w) for A, w in mu.items()}
        out[y] = sum_jets(joint.values())
        post[y] = {A: p / out[y] for A, p in joint.items()}
        assert sum_jets(post[y].values()) == Jet(F(1))
    assert sum_jets(out.values()) == Jet(F(1))
    return out, post


def marginals(law: dict[int, Jet], n: int) -> list[Jet]:
    return [sum_jets(v for A, v in law.items() if (A >> i) & 1) for i in range(n)]


def noise_entropy(n: int, k: int, a: F, c: F) -> LogJet:
    def b(t: F) -> LogJet:
        return entropy_jet({0: Jet(t, F(1)), 1: Jet(1 - t, F(-1))})
    return add_logjets(scale_logjet(b(a), F(n - k)), scale_logjet(b(a + c), F(k)))


def exact_atanh_log_unit(x: F, terms: int = 40) -> tuple[F, F]:
    """Enclose log(x), 1 <= x <= 2, by a finite positive atanh series."""
    assert 1 <= x <= 2
    z = (x - 1) / (x + 1)
    partial = F(0)
    power = z
    for j in range(terms):
        partial += 2 * power / (2 * j + 1)
        power *= z * z
    remainder = 2 * power / ((2 * terms + 1) * (1 - z * z))
    return partial, partial + remainder


def round_interval(lo: F, hi: F, digits: int) -> tuple[F, F]:
    den = 10**digits
    lower = (lo.numerator * den) // lo.denominator
    upper = -((-hi.numerator * den) // hi.denominator)
    return F(lower, den), F(upper, den)


@lru_cache(maxsize=None)
def log_interval(x: F) -> tuple[F, F]:
    if x <= 0:
        raise ValueError("Log argument must be positive")
    exponent = 0
    reduced = x
    while reduced >= 2:
        reduced /= 2
        exponent += 1
    while reduced < 1:
        reduced *= 2
        exponent -= 1
    a, b = exact_atanh_log_unit(reduced)
    l2, u2 = exact_atanh_log_unit(F(2))
    if exponent >= 0:
        lo, hi = a + exponent * l2, b + exponent * u2
    else:
        lo, hi = a + exponent * u2, b + exponent * l2
    return round_interval(lo, hi, 30)


def evaluate_interval(expr: LogLinear, digits: int = 12) -> tuple[F, F]:
    lo = hi = expr.constant
    for p, coefficient in sorted(expr.terms.items()):
        left, right = log_interval(F(p))
        if coefficient >= 0:
            lo += coefficient * left
            hi += coefficient * right
        else:
            lo += coefficient * right
            hi += coefficient * left
    return round_interval(lo, hi, digits)


def describe(expr: LogLinear) -> dict:
    lo, hi = evaluate_interval(expr)
    return {"exact_expression": expr.json(), "rational_enclosure": [str(lo), str(hi)]}


def seed_law() -> dict[int, F]:
    """Fourier U[j,l] = i**(j*l)/2, j=0..3, l=0,1, checked exactly."""
    phases = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    assert sum(x for x, _ in phases) == 0
    assert sum(y for _, y in phases) == 0
    assert all(x*x + y*y == 1 for x, y in phases)
    mu: dict[int, F] = {}
    for i, j in combinations(range(4), 2):
        re = phases[j][0] - phases[i][0]
        im = phases[j][1] - phases[i][1]
        mu[(1 << i) | (1 << j)] = F(re*re + im*im, 16)
    assert sum(mu.values()) == 1
    assert all(sum(w for A, w in mu.items() if A >> i & 1) == F(1, 2) for i in range(4))
    return mu


def conditional_seed(mu: dict[int, F]) -> dict[int, F]:
    q = sum(w for A, w in mu.items() if A & 1)
    ans = {(A >> 1): w/q for A, w in mu.items() if A & 1}
    assert ans == {1: F(1, 4), 2: F(1, 2), 4: F(1, 4)}
    return ans


def test_moving_references(mu: dict[int, F], a: F, c: F) -> dict:
    """Exact chain-rule verification through noisy-coordinate localization.

    Reference = posterior after the previous noisy observation, hence genuinely
    a-dependent. The sum is compared as rational + rational log(prime) forms.
    """
    n, k = 4, 2
    total: LogJet = (LogLinear(), LogLinear(), LogLinear())
    previous_post = {0: {A: Jet(w) for A, w in mu.items()}}
    for j in range(1, n+1):
        out, post = channel(mu, j, a, c)
        for y, p in out.items():
            previous_y = y & ((1 << (j-1))-1)
            d = kl_jet(post[y], previous_post[previous_y])
            total = add_logjets(total, weight_logjet(p, d))
        previous_post = post
    out, _ = channel(mu, n, a, c)
    direct = add_logjets(entropy_jet(out), scale_logjet(noise_entropy(n, k, a, c), F(-1)))
    assert all((x-y).is_zero() for x, y in zip(total, direct))
    return {"a": str(a), "c": str(c), "all_three_orders_equal_exactly": True,
            "reference_law": "posterior after previous noisy coordinate",
            "retained_terms": ["p'' D", "2 p' D'", "p D''", "reference score", "reference acceleration"]}


def build_certificate() -> dict:
    mu = seed_law()
    n, k = 4, 2
    a, c = F(1, 40), F(19, 20)
    u = a + c
    out, post = channel(mu, n, a, c)
    out3, _ = channel(conditional_seed(mu), 3, a, c)
    h4, h3 = entropy_jet(out), entropy_jet(out3)
    reference = {A: Jet(w) for A, w in mu.items()}
    q = marginals(reference, n)
    assert all(x == Jet(F(1, 2)) for x in q)
    assert all(r.d == 0 for law in post.values() for r in law.values())

    full_info: LogJet = (LogLinear(), LogLinear(), LogLinear())
    one_info: LogJet = (LogLinear(), LogLinear(), LogLinear())
    gap_weight, gap_mixed, gap_internal = LogLinear(), LogLinear(), LogLinear()
    acceleration = LogLinear()
    fisher = F(0)
    gaussian_jet = Jet(F(0))
    gaussian_second_alternative = F(0)
    atom_details = []
    for y, p in out.items():
        d = kl_jet(post[y], reference)
        r = marginals(post[y], n)
        down = {i: r[i].scale(F(1, k)) for i in range(n)}
        down_reference = {i: q[i].scale(F(1, k)) for i in range(n)}
        md = scale_logjet(kl_jet(down, down_reference), F(k))
        full_info = add_logjets(full_info, weight_logjet(p, d))
        one_info = add_logjets(one_info, weight_logjet(p, md))
        gap = add_logjets(d, scale_logjet(md, F(-1)))
        gap_weight = gap_weight + gap[0].scale(p.dd)
        gap_mixed = gap_mixed + gap[1].scale(2*p.d)
        gap_internal = gap_internal + gap[2].scale(p.x)
        for A, rr in post[y].items():
            joint = likelihood(A, y, n, a, c).scale(mu[A])
            acceleration = acceleration + (LogLinear.log(rr.x)-LogLinear.log(mu[A])).scale(joint.dd)
            fisher += p.x * rr.d**2 / rr.x
        for i in range(n):
            delta = r[i] - q[i]
            gaussian_jet = gaussian_jet + (p * delta * delta).scale(F(1, 2))
            nn = p * r[i]
            gaussian_second_alternative += nn.x * nn.dd/p.x - nn.x**2*p.dd/(2*p.x**2)
        atom_details.append({"occupied_output": [i for i in range(n) if y >> i & 1],
                             "output_jet": p.json(),
                             "posterior_jets": {str(A): rr.json() for A, rr in post[y].items()},
                             "inclusion_marginal_jets": [rj.json() for rj in r]})

    direct_info = add_logjets(h4, scale_logjet(noise_entropy(n, k, a, c), F(-1)))
    assert all((x-y).is_zero() for x, y in zip(full_info, direct_info))
    assert (full_info[2] - acceleration - LogLinear(fisher)).is_zero()
    assert fisher == 0
    assert gaussian_jet.dd == gaussian_second_alternative

    gap_second = full_info[2] - one_info[2]
    # From 2 I(J;Y) = 2 H4 - 2[b(a+c)+H3] and I(X;Y) = H4 - 2b(a)-2b(a+c).
    b_second = -1/(a*(1-a))
    gap_second_entropy_formula = -h4[2] + h3[2].scale(F(2)) + LogLinear(-2*b_second)
    assert (gap_second - gap_second_entropy_formula).is_zero()
    assert (gap_second - gap_weight - gap_mixed - gap_internal).is_zero()
    assert gap_mixed.is_zero()
    gap_lo, gap_hi = evaluate_interval(gap_second)
    assert F(31355, 10000) < gap_lo <= gap_hi < F(31356, 10000)
    h_lo, h_hi = evaluate_interval(h4[2])
    assert F(-123) < h_lo <= h_hi < F(-122)
    assert F(3378, 1000) < gaussian_jet.dd < F(3379, 1000)

    lower_likelihood = F(1, 40**4)
    lipschitz = F(4224)/lower_likelihood
    stopping_bound = 1/(144*lipschitz*lipschitz)
    report = {
        "status": "EXACT_FINITE_CERTIFICATE_PLUS_ANALYTICAL_EXTENSION",
        "not_independent_certification": True,
        "parameters": {"n": n, "k": k, "a": str(a), "c": str(c), "a_plus_c": str(u)},
        "projection_seed": {"U_formula": "U[j,l]=i**(j*l)/2, j=0..3, l=0,1",
                            "orthonormal_columns_checked_exactly": True,
                            "input_atoms": {str(A): str(w) for A, w in mu.items()},
                            "conditional_remaining_rank_one_weights": ["1/4", "1/2", "1/4"]},
        "output_atoms_and_posteriors": atom_details,
        "conditional_three_site_output_jets": {str(y): p.json() for y, p in out3.items()},
        "complete_entropy_hessian": describe(h4[2]),
        "posterior_entropy_conversion": {"I_second": describe(full_info[2]),
                                         "acceleration_term": describe(acceleration),
                                         "averaged_posterior_fisher_exact": str(fisher),
                                         "conversion_identity_exact": True},
        "entropic_independence_gap": {"gap_value": describe(full_info[0] - one_info[0]),
                                     "gap_second": describe(gap_second),
                                     "weight_acceleration": describe(gap_weight),
                                     "mixed_weight_posterior": describe(gap_mixed),
                                     "internal_posterior_acceleration": describe(gap_internal),
                                     "entropy_formula_identity_exact": True,
                                     "all_posterior_first_derivatives_exactly_zero": True,
                                     "growing_sparse_factor": "m*(2*m-r)/(2*m-1); n=4*m, k=2*m, 1<=r<=2*m",
                                     "quarter_dimension_pinning_second": "m*m/(2*m-1) times seed_gap_second"},
        "gaussian_localization": {"Q_at_zero": str(gaussian_jet.x),
                                  "Q_first_at_zero": str(gaussian_jet.d),
                                  "Q_second_at_zero_exact": str(gaussian_jet.dd),
                                  "strict_rational_bounds_for_Q_second": ["3378/1000", "3379/1000"],
                                  "Q_second_checked_by_two_exact_formulas": True,
                                  "likelihood_lower_bound": str(lower_likelihood),
                                  "prior_L1_lipschitz_bound_L": str(lipschitz),
                                  "explicit_T0": str(stopping_bound),
                                  "analytical_average_bound": "Q_t_second > 2 for all 0<=t<=T0 (one block)",
                                  "growing_completion_excess_bound": "H_m_second - E[H_posterior_T_second] > 2*m*T for every m>=1 and 0<T<=T0",
                                  "integrated_posterior_fisher": "0 exactly at a=1/40, c=19/20"},
        "moving_reference_test": test_moving_references(mu, F(1,80), c),
        "log_bound_method": {"series": "log(x)=2 sum_{j=0}^{N-1} z^(2j+1)/(2j+1)+R; z=(x-1)/(x+1), 1<=x<=2",
                             "N": 40,
                             "tail": "0<=R<=2*z^(2*N+1)/((2*N+1)*(1-z*z))",
                             "range_reduction": "powers of 2, with exact rational arithmetic",
                             "per_log_outward_decimal_digits": 30,
                             "reported_outward_decimal_digits": 12},
    }
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=None, help="NEW output directory; frozen evidence is forbidden")
    args = parser.parse_args()
    if not __debug__:
        parser.error("Do not run with -O: exact assertions must remain enabled")
    root = Path(__file__).resolve().parents[1]
    out = args.out or root / "output" / datetime.now(timezone.utc).strftime("certificate_%Y%m%dT%H%M%S_%fZ")
    out = out.resolve()
    protected = [(root / "evidence").resolve(), (root / "scripts").resolve()]
    if out == root or any(out == p or p in out.parents for p in protected):
        parser.error("Output must not overwrite the package root, scripts, or frozen evidence")
    if out.exists():
        parser.error("Output directory already exists; choose a new directory")
    result = build_certificate()
    out.mkdir(parents=True, exist_ok=False)
    (out / "certificate.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    runtime = {"completed_utc": datetime.now(timezone.utc).isoformat(),
               "python": sys.version, "platform": platform.platform(),
               "external_dependencies": [], "floating_point_used_for_acceptance": False}
    (out / "runtime.json").write_text(json.dumps(runtime, indent=2)+"\n", encoding="utf-8")
    print("PASS: exact probability, moving-reference, and Hessian identities")
    print("PASS: 3.1355 < averaged EI slack second derivative < 3.1356")
    print("PASS: 3.378 < Gaussian-localization integrand second derivative < 3.379")
    print("PASS: all terminal posterior first derivatives equal zero exactly")
    print("PASS: -123 < full channel entropy second derivative < -122")
    print(f"Exact certificate written to {out / 'certificate.json'}")


if __name__ == "__main__":
    main()
