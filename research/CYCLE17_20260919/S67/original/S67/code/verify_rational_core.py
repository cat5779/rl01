#!/usr/bin/env python3
"""Python-standard-library-only exact rational checks for S67.

No floating-point arithmetic is used for acceptance.  Machin's formula and
alternating arctangent series enclose pi; an atanh series encloses logarithms.
Reported decimal endpoints are rounded outwards from exact Fractions.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import argparse
import json

@dataclass(frozen=True)
class I:
    lo: F
    hi: F
    def __post_init__(self):
        if self.lo > self.hi:
            raise ValueError('reversed interval')
        # Exact outward grid rounding prevents denominator blow-up.
        scale = 10**70
        lower = F((self.lo.numerator*scale)//self.lo.denominator, scale)
        upper = F(-((-self.hi.numerator*scale)//self.hi.denominator), scale)
        object.__setattr__(self, 'lo', lower)
        object.__setattr__(self, 'hi', upper)
    @staticmethod
    def of(x):
        return x if isinstance(x, I) else I(F(x), F(x))
    def __add__(self, other):
        b = I.of(other)
        return I(self.lo + b.lo, self.hi + b.hi)
    __radd__ = __add__
    def __neg__(self):
        return I(-self.hi, -self.lo)
    def __sub__(self, other):
        return self + (-I.of(other))
    def __rsub__(self, other):
        return I.of(other) + (-self)
    def __mul__(self, other):
        b = I.of(other)
        values = (self.lo*b.lo, self.lo*b.hi, self.hi*b.lo, self.hi*b.hi)
        return I(min(values), max(values))
    __rmul__ = __mul__
    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError('interval contains zero')
        return I(1/self.hi, 1/self.lo)
    def __truediv__(self, other):
        return self * I.of(other).reciprocal()
    def __rtruediv__(self, other):
        return I.of(other) * self.reciprocal()
    def __pow__(self, n: int):
        if n < 0:
            return self.reciprocal() ** (-n)
        out = I.of(1)
        base = self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n //= 2
        return out

def atan_reciprocal(q: int, terms: int = 36) -> I:
    """Alternating-series enclosure for atan(1/q), q>1."""
    if q <= 1 or terms < 1:
        raise ValueError('q>1 and terms>=1 required')
    total = sum((F((-1)**k, (2*k+1)*q**(2*k+1)) for k in range(terms)), F(0))
    next_term = F((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return I(min(total, total + next_term), max(total, total + next_term))

def log_ge_one(x: I, terms: int = 32) -> I:
    """For x>=1, log(x)=2*atanh((x-1)/(x+1)), with a geometric tail."""
    if x.lo < 1:
        raise ValueError('log_ge_one requires x>=1')
    z = (x-1)/(x+1)
    if not (0 <= z.lo <= z.hi < 1):
        raise ArithmeticError('atanh argument out of range')
    def partial(v: F) -> F:
        return 2*sum((v**(2*k+1)/F(2*k+1) for k in range(terms)), F(0))
    lower = partial(z.lo)
    upper = partial(z.hi) + 2*z.hi**(2*terms+1)/(F(2*terms+1)*(1-z.hi**2))
    return I(lower, upper)

def decimal_bound(x: F, digits: int, upward: bool) -> str:
    scale = 10**digits
    if upward:
        scaled = -((-x.numerator*scale)//x.denominator)
    else:
        scaled = (x.numerator*scale)//x.denominator
    sign = '-' if scaled < 0 else ''
    scaled = abs(scaled)
    return f'{sign}{scaled//scale}.{scaled%scale:0{digits}d}'

def show(x: I, digits: int = 35) -> dict:
    return {'lower': decimal_bound(x.lo, digits, False),
            'upper': decimal_bound(x.hi, digits, True),
            'arithmetic': 'exact Fraction; decimal endpoints rounded outwards'}

def run() -> dict:
    pi = 16*atan_reciprocal(5) - 4*atan_reciprocal(239)
    assert pi.lo > 3 and pi.hi < F(22,7)
    assert pi.lo > F('3.14159265358979323846')
    assert pi.hi < F('3.14159265358979323847')
    c = F(19,20)
    h = c/pi
    den = F(1,4)+h**2
    # Pair sites 0,3; exterior sites 1,2 fixed to (1,0).
    u = F(1,8)/den
    v = 1-u
    z = -h/3 - h**3/den
    t = z**2
    A = u*v-t
    B = u*(1-v)+t
    C = (1-u)*v+t
    D = (1-u)*(1-v)-t
    assert min(A.lo, B.lo, C.lo, D.lo) > 0
    J = log_ge_one((B*C)/(A*D))
    W = t*(1/A+1/B+1/C+1/D)
    counter = J-W
    assert counter.lo > 0, 'the claimed four-site comparison failure was not certified'
    scalar_slack = F(3,2)*W-J
    assert scalar_slack.lo > 0

    # Closed integral formula, combining logarithms before evaluating them.
    a0, b, s = F(1,50), F(1,40), F(39,1600)
    log_ratio = log_ge_one(I.of(b/a0))
    assert log_ratio.lo > F('0.223143551314209755766')
    assert log_ratio.hi < F('0.223143551314209755767')
    dF1 = ((1+a0)*(b-a0)-(b*b-a0*a0)/2-a0*log_ratio)/39
    dF3 = (a0/2*(1/(b*b)-1/(a0*a0))
           -(1+3*a0)*(1/b-1/a0)
           -3*(1+a0)*log_ratio
           +(3+a0)*(b-a0)-(b*b-a0*a0)/2)/(39**3)
    U = F(3,2)*(dF3/s-4*dF1)
    assert 0 < U.lo <= U.hi < F(887,1000000)
    c16 = I(F('0.000146680480325883947552193048'),
            F('0.000146680480325883947552193049'))
    budget = I(F('0.000245932000395801628841632655'),
               F('0.000245932000395801628841632657'))
    cap = c16 + budget
    A_bound = U-c16
    deficit = U-cap
    assert deficit.lo > 0, 'this particular bound is asserted to fall short, not to close'

    tau = h**2
    assert tau.lo > F(9,100) and tau.hi < F(23,250)
    d3 = 2 + 2/(1-64*tau**2)
    U3 = F(3,2)*(dF3/s-d3/80000)
    beta3 = 3*(d3-4)/80000
    improvement3 = U-U3
    deficit3 = U3-cap
    assert U3.hi < F(85,100000)
    assert improvement3.lo > 0 and deficit3.lo > 0
    assert beta3.lo > 0 and beta3.hi < F(87,1000000)
    actual_M_max = F(2378,97)
    actual_D_max = F(2475**2, 97*2378)
    diagonal_route_floor = F(3,2)*(dF3/s-actual_D_max/80000)
    assert diagonal_route_floor.lo > F(469,1000000)
    assert (diagonal_route_floor-cap).lo > 0

    # Exact finite algebra checks for the three-site Fisher decomposition.
    fisher_algebra_checks = 0
    for pp in (F(99,200), F(199,400), F(1,2), F(201,400), F(101,200)):
        for tt in (F(9,100), F(91,1000), F(23,250)):
            vv = pp*(1-pp)
            xx = (2*pp-1)**2
            direct = F(0)
            for kk, multiplicity in ((0,1),(1,2),(2,1)):
                rr = pp-tt*(F(kk)/pp-F(2-kk)/(1-pp))
                assert 0 < rr < 1
                direct += multiplicity*pp**kk*(1-pp)**(2-kk)/(rr*(1-rr))
            EE = (1-8*tt)**2-(2+16*tt)*xx+xx**2
            split = (2*(1+xx+8*tt)/(1-xx+8*tt)
                     +128*tt**2*(1+xx-8*tt)/((1-xx+8*tt)*EE)
                     +2*vv**3/(vv**3-xx*tt*(vv+tt)))
            assert direct == split
            assert direct >= 2+2/(1-64*tt**2)
            fisher_algebra_checks += 1

    # Exact constants in the binary comparison and weighted resolvent bound.
    def p(r):
        return -2*r**3+51283*r**2-384800*r+528000
    assert p(F(1)) > 0 and p(F(2)) < 0
    assert p(F(569,100)) < 0 and p(F(57,10)) > 0 and p(F(400)) > 0
    r = F(569,100)
    w = (r-1)*(41*r+400)/(r*(r+440))
    assert F(3,2)*w > F(7,4)
    exp_partial = sum((F(7,4)**k/F(__import__('math').factorial(k)) for k in range(7)), F(0))
    assert exp_partial > F(57,10)
    theta = F(1,1000)
    commutator_upper = F(19,30)*theta*(2/(F(1,2)-theta)**2+2+9)
    assert commutator_upper == F(90041209,7470030000)
    assert commutator_upper < F(1,80)

    return {
        'status': 'PASS',
        'acceptance_arithmetic': 'exact rational arithmetic only',
        'pi_machin_enclosure': show(pi),
        'uniform_C_over_n_bound': show(U),
        'three_site_local_diagonal_Fisher_lower_bound': show(d3),
        'three_site_improved_limsup_C_over_n_bound': show(U3),
        'three_site_finite_boundary_coefficient_beta3': show(beta3),
        'three_site_improvement_over_uniform_bound': show(improvement3),
        'three_site_limsup_A_n_upper_bound_interval': show(U3-c16),
        'three_site_bound_excess_over_required_cap': show(deficit3),
        'all_window_actual_diagonal_Fisher_upper_bound': show(I.of(actual_D_max)),
        'best_possible_diagonal_only_route_lower_floor': show(diagonal_route_floor),
        'diagonal_only_route_floor_excess_over_required_cap': show(diagonal_route_floor-cap),
        'diagonal_only_route_obstruction': 'PROVED: increasing only the local Fisher window cannot close with the present kappa=3/2 and transport allocation',
        'uniform_A_n_upper_bound_interval': show(A_bound),
        'required_C_cap': show(cap),
        'bound_excess_over_required_cap': show(deficit),
        'four_site_actual_sine_counterexample': {
            'rho': '1/2', 'c': '19/20', 'b': '1/40', 'n': 4,
            'pair_zero_based': [0,3], 'exterior_sites_zero_based': [1,2],
            'exterior_bits_in_that_order': [1,0],
            'exterior_pattern_probability': show(den),
            'J': show(J), 'W': show(W), 'J_minus_W': show(counter),
            'J_over_W': show(J/W),
            'three_halves_W_minus_J': show(scalar_slack),
            'scope': 'pointwise conditional pair; NOT an entropy-rate counterexample'
        },
        'rational_binary_comparison_and_locality_constants': 'PASS',
        'three_site_exact_algebra_checks': {'status': 'PASS', 'cases': fisher_algebra_checks, 'scope': 'finite cross-checks; the uniform theorem is proved analytically in the manuscript'},
        'entropy_rate_chord_status': 'INCOMPLETE'
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text)
