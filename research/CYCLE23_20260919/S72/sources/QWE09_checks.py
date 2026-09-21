#!/usr/bin/env python3
"""QWE09: exact-input, directed-rounding certificates and optional diagnostics.

Default: only Python standard library. The certificate uses integer dyadic
intervals; pi and log are enclosed by proved convergent series. No floating
transcendental evaluation enters a certificate. Run:
    python QWE09_checks.py --certificate
Optional floating diagnostics (requires NumPy; never used as certificates):
    python QWE09_checks.py --diagnostics --max-n 10
    python QWE09_checks.py --witness 2 2 --a 1/40 --c 19/20
"""
from __future__ import annotations
import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable

PRECISION = 256
SCALE = 1 << PRECISION

def ceil_div(a: int, b: int) -> int:
    if b == 0:
        raise ZeroDivisionError
    return -((-a) // b)

@dataclass(frozen=True)
class IV:
    lo: int
    hi: int

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("Reversed interval")

    @staticmethod
    def rat(x: int | Fraction, denominator: int = 1) -> "IV":
        f = Fraction(x, denominator) if isinstance(x, int) else x / denominator
        return IV((f.numerator * SCALE) // f.denominator,
                  ceil_div(f.numerator * SCALE, f.denominator))

    @staticmethod
    def coerce(x: "IV | int | Fraction") -> "IV":
        return x if isinstance(x, IV) else IV.rat(x)

    def __add__(self, other: "IV | int | Fraction") -> "IV":
        o = IV.coerce(other)
        return IV(self.lo + o.lo, self.hi + o.hi)
    __radd__ = __add__

    def __neg__(self) -> "IV":
        return IV(-self.hi, -self.lo)

    def __sub__(self, other: "IV | int | Fraction") -> "IV":
        return self + (-IV.coerce(other))

    def __rsub__(self, other: "IV | int | Fraction") -> "IV":
        return IV.coerce(other) - self

    def __mul__(self, other: "IV | int | Fraction") -> "IV":
        o = IV.coerce(other)
        p = (self.lo * o.lo, self.lo * o.hi,
             self.hi * o.lo, self.hi * o.hi)
        return IV(min(p) // SCALE, ceil_div(max(p), SCALE))
    __rmul__ = __mul__

    def reciprocal(self) -> "IV":
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("Interval contains zero")
        return IV((SCALE*SCALE) // self.hi,
                  ceil_div(SCALE*SCALE, self.lo))

    def __truediv__(self, other: "IV | int | Fraction") -> "IV":
        return self * IV.coerce(other).reciprocal()

    def __rtruediv__(self, other: "IV | int | Fraction") -> "IV":
        return IV.coerce(other) / self

    def __pow__(self, power: int) -> "IV":
        if not isinstance(power, int) or power < 0:
            raise ValueError("Only nonnegative integer powers")
        result, base = IV.rat(1), self
        k = power
        while k:
            if k & 1:
                result = result * base
            base = base * base
            k //= 2
        return result

    def contains(self, x: int | Fraction) -> bool:
        f = Fraction(x)
        return self.lo * f.denominator <= f.numerator*SCALE <= self.hi*f.denominator

    def strict_inside(self, lo: Fraction, hi: Fraction) -> bool:
        return (self.lo * lo.denominator > lo.numerator * SCALE and
                self.hi * hi.denominator < hi.numerator * SCALE)

    def decimal_bounds(self, places: int = 18) -> list[str]:
        factor = 10**places
        lower = (self.lo * factor) // SCALE
        upper = ceil_div(self.hi * factor, SCALE)
        def fmt(x: int) -> str:
            sign = '-' if x < 0 else ''
            q, r = divmod(abs(x), factor)
            return f"{sign}{q}.{r:0{places}d}"
        return [fmt(lower), fmt(upper)]


def atan_reciprocal(q: int, terms: int = 96) -> IV:
    """Alternating series, including a two-sided next-term enclosure."""
    if q <= 1 or terms < 1:
        raise ValueError
    total = sum((Fraction((-1)**k, (2*k+1)*q**(2*k+1))
                 for k in range(terms)), Fraction())
    next_term = Fraction((-1)**terms, (2*terms+1)*q**(2*terms+1))
    left, right = sorted((total, total + next_term))
    return IV(IV.rat(left).lo, IV.rat(right).hi)


def certified_pi() -> IV:
    return 16*atan_reciprocal(5) - 4*atan_reciprocal(239)


def ilog(x: IV, terms: int = 384) -> IV:
    """Log by the atanh series with an explicit absolute tail bound."""
    if x.lo <= 0:
        raise ValueError("log requires a strictly positive interval")
    z = (x-1)/(x+1)
    radius_int = max(abs(z.lo), abs(z.hi))
    if radius_int >= SCALE:
        raise ValueError("log reduction did not produce |z|<1")
    radius = IV(radius_int, radius_int)
    z2, term, total = z*z, z, IV.rat(0)
    for k in range(terms):
        total += term / (2*k+1)
        term *= z2
    tail = 2*(radius**(2*terms+1))/((2*terms+1)*(1-radius*radius))
    return 2*total + IV(-tail.hi, tail.hi)

Matrix = list[list[IV]]

def transpose(a: Matrix) -> Matrix:
    return [list(x) for x in zip(*a)]


def mm(a: Matrix, b: Matrix) -> Matrix:
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("Matrix dimensions")
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), IV.rat(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def inverse(a: Matrix) -> Matrix:
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("Square matrix required")
    t = [row[:] + [IV.rat(i == j) for j in range(n)] for i, row in enumerate(a)]
    for j in range(n):
        candidates = [k for k in range(j, n) if not(t[k][j].lo <= 0 <= t[k][j].hi)]
        if not candidates:
            raise ArithmeticError("No certifiably nonzero Gaussian pivot")
        pivot = max(candidates, key=lambda k: min(abs(t[k][j].lo), abs(t[k][j].hi)))
        t[j], t[pivot] = t[pivot], t[j]
        d = t[j][j]
        t[j] = [v/d for v in t[j]]
        for k in range(n):
            if k == j:
                continue
            d = t[k][j]
            t[k] = [u-d*v for u, v in zip(t[k], t[j])]
    return [row[n:] for row in t]


def determinant(a: Matrix) -> IV:
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("Square matrix required")
    t = [row[:] for row in a]
    det = IV.rat(1)
    for j in range(n):
        candidates = [k for k in range(j, n) if not(t[k][j].lo <= 0 <= t[k][j].hi)]
        if not candidates:
            raise ArithmeticError("No certifiably nonzero determinant pivot")
        pivot = max(candidates, key=lambda k: min(abs(t[k][j].lo), abs(t[k][j].hi)))
        if pivot != j:
            t[j], t[pivot] = t[pivot], t[j]
            det = -det
        d = t[j][j]
        det *= d
        for k in range(j+1, n):
            factor = t[k][j]/d
            for h in range(j+1, n):
                t[k][h] -= factor*t[j][h]
    return det


def phi2(x: Matrix, cross: bool = False) -> IV:
    if len(x) != 2 or len(x[0]) != 2:
        raise ValueError
    h = x[0][1]*x[0][1]
    v = x[0][0]*x[1][1]
    z = h/v
    f = h+(v-h)*ilog(1-z)
    return f if cross else x[0][0]**2+x[1][1]**2+2*f


def jensen_certificate() -> dict:
    pi = certified_pi()
    c = IV.rat(19, 20)
    n = 6
    kernel: Matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            r = abs(i-j)
            if r == 0:
                row.append(IV.rat(1, 2))
            elif r % 2 == 0:
                row.append(IV.rat(0))
            else:
                sign = 1 if r % 4 == 1 else -1
                row.append(sign*c/(pi*r))
        kernel.append(row)
    word = [0, 0, 0, 1, 1]
    a = [[kernel[i][j] - (1-word[i] if i == j else 0)
          for j in range(5)] for i in range(5)]
    p_observed = -determinant(a)
    assert p_observed.strict_inside(Fraction(0), Fraction(1))
    g = inverse(a)
    b = [[kernel[i][5]] for i in range(5)]
    gb = mm(g, b)
    q = IV.rat(1, 2)-mm(transpose(b), gb)[0][0]
    if not q.strict_inside(Fraction(0), Fraction(1)):
        raise ArithmeticError("Conditional probability not enclosed in (0,1)")
    core = [2, 3]
    m = [[g[i][j] for j in core] for i in core]
    v = [[gb[i][0]] for i in core]
    vv = mm(v, transpose(v))
    m1 = [[m[i][j]+vv[i][j]/q for j in range(2)] for i in range(2)]
    m0 = [[m[i][j]-vv[i][j]/(1-q) for j in range(2)] for i in range(2)]
    full_gap = q*phi2(m1)+(1-q)*phi2(m0)-phi2(m)
    cross_gap = q*phi2(m1, True)+(1-q)*phi2(m0, True)-phi2(m, True)
    variance = (v[0][0]**2+v[1][0]**2)**2/(q*(1-q))
    assert full_gap.strict_inside(Fraction(-107, 1000), Fraction(-106, 1000))
    assert cross_gap.strict_inside(Fraction(-97, 1000), Fraction(-96, 1000))
    assert variance.strict_inside(Fraction(170, 1000), Fraction(171, 1000))
    payment = -full_gap/variance
    assert payment.strict_inside(Fraction(5,8), Fraction(626,1000))
    for i in range(2):
        for j in range(2):
            assert (q*m1[i][j]+(1-q)*m0[i][j]-m[i][j]).contains(0)
    return {
        "arithmetic": "integer dyadic intervals with outward rounding",
        "precision_bits": PRECISION,
        "pi_series_terms_each": 96,
        "log_series_terms_each": 384,
        "inputs": {"rho": "1/2", "c": "19/20", "a": "1/40", "n": n,
                   "observed_sites": list(range(5)), "observed_word": word,
                   "core_sites": core, "revealed_site": 5},
        "enclosures": {"pi": pi.decimal_bounds(), "observed_word_probability": p_observed.decimal_bounds(),
                       "Pr_Y5_eq_1_given_word": q.decimal_bounds(),
                       "full_potential_Jensen_gap": full_gap.decimal_bounds(),
                       "cross_potential_Jensen_gap": cross_gap.decimal_bounds(),
                       "quadratic_variation": variance.decimal_bounds(),
                       "necessary_full_potential_payment_coefficient": payment.decimal_bounds()},
        "strict_rational_bounds": {"full_gap": ["-107/1000", "-106/1000"],
                                  "cross_gap": ["-97/1000", "-96/1000"],
                                  "variance": ["170/1000", "171/1000"],
                                  "necessary_payment": ["5/8", "626/1000"]}}


def diagnostics(max_n: int) -> list[dict]:
    """Floating-point identity checks; not an interval/sign certificate."""
    import numpy as np
    def potential(g, cross=False):
        d = np.real(np.diag(g))
        ans = 0.0 if cross else float(d@d)
        for i in range(len(g)):
            for j in range(i+1, len(g)):
                if cross and (i-j) % 2 == 0:
                    continue
                h = float(abs(g[i,j])**2)
                v = float(d[i]*d[j])
                z = h/v
                f = h+(v-h)*np.log1p(-z)
                ans += f if cross else 2*f
        return ans
    out = []
    for n in range(2, max_n+1, 2):
        idx = np.arange(n)
        dd = idx[:,None]-idx[None,:]
        qmat = .5*np.sinc(.5*dd)
        for a in (.02, .025, .03):
            c = .95
            k = a*np.eye(n)+c*qmat
            p = a+c/2
            H2 = ph = ch = Hst = norm = 0.0
            ee = idx[::2]; oo = idx[1::2]
            for word in range(1 << n):
                bits = (word >> idx) & 1
                aa = k-np.diag(1-bits)
                sign, logabs = np.linalg.slogdet(aa)
                prob = (-1)**int(n-bits.sum())*sign*np.exp(logabs)
                if prob <= 0:
                    raise ArithmeticError("Unexpected nonpositive floating atom")
                g = np.linalg.inv(aa)
                tr = np.trace(g)
                tr2 = np.trace(g@g)
                H2 -= prob*(tr*tr+(tr*tr-tr2)*np.log(prob))
                ph += prob*potential(g)
                ch += prob*potential(g, True)
                te = np.trace(g[np.ix_(ee,ee)])
                to = np.trace(g[np.ix_(oo,oo)])
                ec = np.sum(abs(g[np.ix_(ee,oo)])**2)
                Hst -= prob*(te*to+(te*to-ec)*np.log(prob))
                norm += prob
            combined2 = mask_mass = cross_weight = 0.0
            U = 2*qmat[np.ix_(ee,oo)]
            C = c*U/2
            m = len(ee)
            for mask in range(1 << m):
                y = (mask >> np.arange(m)) & 1
                kval = int(y.sum())
                w = p**kval*(1-p)**(m-kval)
                score = kval/p-(m-kval)/(1-p)
                w1 = w*score
                w2 = w*(score**2-kval/p**2-(m-kval)/(1-p)**2)
                D = p-1+y
                mmask = p*np.eye(len(oo))-C.T@np.diag(1/D)@C
                m1 = np.eye(len(oo))+C.T@np.diag(1/D**2)@C
                m2 = -2*C.T@np.diag(1/D**3)@C
                F = F1 = F2 = 0.0
                for oddword in range(1 << len(oo)):
                    z = (oddword >> np.arange(len(oo))) & 1
                    bb = mmask-np.diag(1-z)
                    sign, lp = np.linalg.slogdet(bb)
                    prob = (-1)**int(len(oo)-z.sum())*sign*np.exp(lp)
                    g = np.linalg.inv(bb)
                    l1 = np.trace(g@m1)
                    l2 = np.trace(g@m2-g@m1@g@m1)
                    prob1 = prob*l1
                    prob2 = prob*(l1*l1+l2)
                    F -= prob*np.log(prob)
                    F1 -= prob1*(np.log(prob)+1)
                    F2 -= prob2*(np.log(prob)+1)+prob1*prob1/prob
                combined2 += w*F2+2*w1*F1+w2*F
                cross_weight += 2*w1*F1+w2*F
                mask_mass += w
            out.append({"n": n, "a": a, "c": c, "H_second": float(H2),
                        "H_second_plus_EPhi": float(H2+ph),
                        "H_even_odd_mixed": float(Hst),
                        "H_mixed_plus_EChi": float(Hst+ch),
                        "combined_second_from_masks": float(combined2),
                        "combined_identity_error": float(combined2-H2-len(ee)/(p*(1-p))),
                        "moving_mask_terms": float(cross_weight),
                        "normalization_error": float(norm-1),
                        "mask_normalization_error": float(mask_mass-1)})
    return out


def local_witness(m: int, halo: int, a: Fraction, c: Fraction) -> dict:
    """Floating actual-mask evaluation of W_mL and V_mL, not a certificate.

    Cost is exponential in m+2*halo. No clipping or rare-word deletion.
    """
    import numpy as np
    if m < 1 or halo < 1:
        raise ValueError("The proved interface requires m>=1 and L>=1")
    if not (0 < c < 1 and 0 < a < 1-c):
        raise ValueError("Need 0<c<1 and 0<a<1-c")
    af, cf = float(a), float(c)
    n = m+2*halo
    ids = np.arange(n)
    ee, oo = ids[::2], ids[1::2]
    core = ids[halo:halo+m]
    q = .5*np.sinc(.5*(ids[:,None]-ids[None,:]))
    C = cf*q[np.ix_(ee,oo)]
    p = af+cf/2
    def pots(g):
        diag = np.real(np.diag(g))
        phi, chi = float(diag@diag), 0.0
        for i in range(m):
            for j in range(i+1,m):
                h, v = float(abs(g[i,j])**2), float(diag[i]*diag[j])
                f = h+(v-h)*np.log1p(-h/v)
                phi += 2*f
                if (core[i]-core[j]) % 2:
                    chi += f
        return phi, chi
    ph = ch = mass = 0.0
    for mask in range(1 << len(ee)):
        y = (mask >> np.arange(len(ee))) & 1
        k = int(y.sum())
        w = p**k*(1-p)**(len(ee)-k)
        dinv = np.diag(1/(p-1+y))
        dc = dinv@C
        M = p*np.eye(len(oo))-C.T@dc
        for oddword in range(1 << len(oo)):
            z = (oddword >> np.arange(len(oo))) & 1
            odd_masked = M-np.diag(1-z)
            sign, logdet = np.linalg.slogdet(odd_masked)
            conditional_mass = (-1)**int(len(oo)-z.sum())*sign*np.exp(logdet)
            if conditional_mass <= 0:
                raise ArithmeticError("Nonpositive floating conditional atom; use higher precision")
            T = np.linalg.inv(odd_masked)
            G = np.zeros((n,n))
            G[np.ix_(oo,oo)] = T
            G[np.ix_(ee,oo)] = -dc@T
            G[np.ix_(oo,ee)] = (-dc@T).T
            G[np.ix_(ee,ee)] = dinv+dc@T@dc.T
            f, x = pots(G[np.ix_(core,core)])
            probability = w*conditional_mass
            ph += probability*f
            ch += probability*x
            mass += probability
    return {"status": "FLOATING_DIAGNOSTIC_NOT_A_CERTIFICATE",
            "m": m, "L": halo, "a": str(a), "c": str(c), "rho": "1/2",
            "observation_length": n, "W_mL": -ph/m, "V_mL": ch/m,
            "normalization_error": mass-1}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate', action='store_true')
    parser.add_argument('--diagnostics', action='store_true')
    parser.add_argument('--max-n', type=int, default=10)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--witness', type=int, nargs=2, metavar=('M','L'))
    parser.add_argument('--a', type=Fraction, default=Fraction(1,40))
    parser.add_argument('--c', type=Fraction, default=Fraction(19,20))
    args = parser.parse_args()
    if args.max_n < 2:
        parser.error('--max-n must be at least 2; enumeration has exponential cost')
    report: dict = {}
    if args.certificate or not (args.diagnostics or args.witness):
        report['certificate'] = jensen_certificate()
    if args.diagnostics:
        report['floating_diagnostics_NOT_certificates'] = diagnostics(args.max_n)
    if args.witness:
        report['local_witness_NOT_a_certificate'] = local_witness(*args.witness, args.a, args.c)
    text = json.dumps(report, indent=2)
    print(text)
    if args.output:
        args.output.write_text(text+'\n', encoding='utf-8')

if __name__ == '__main__':
    main()
