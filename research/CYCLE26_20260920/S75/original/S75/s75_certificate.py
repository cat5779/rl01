#!/usr/bin/env python3
"""S75: exact-rational outward interval certificates, standard library only.

All endpoints are integers on a 10^-80 grid. Every arithmetic operation
rounds outward. Transcendental bounds use Taylor series with explicit tails.
There are no floating-point decisions in the sign certificates.
"""
from __future__ import annotations
from dataclasses import dataclass
import json
import math
from pathlib import Path

DIGITS = 80
SCALE = 10 ** DIGITS

def ceildiv(n: int, d: int) -> int:
    if d < 0:
        n, d = -n, -d
    return -((-n) // d)

@dataclass(frozen=True)
class IV:
    lo: int
    hi: int

    def __post_init__(self):
        if self.lo > self.hi:
            raise ValueError("Reversed interval")

    @staticmethod
    def rat(n: int, d: int = 1) -> 'IV':
        if d == 0:
            raise ZeroDivisionError
        if d < 0:
            n, d = -n, -d
        return IV(n * SCALE // d, ceildiv(n * SCALE, d))

    @staticmethod
    def exact_grid(n: int) -> 'IV':
        return IV(n, n)

    def __add__(self, other) -> 'IV':
        other = coerce(other)
        return IV(self.lo + other.lo, self.hi + other.hi)
    __radd__ = __add__

    def __neg__(self) -> 'IV':
        return IV(-self.hi, -self.lo)

    def __sub__(self, other) -> 'IV':
        return self + (-coerce(other))

    def __rsub__(self, other) -> 'IV':
        return coerce(other) - self

    def __mul__(self, other) -> 'IV':
        other = coerce(other)
        v = [self.lo * other.lo, self.lo * other.hi,
             self.hi * other.lo, self.hi * other.hi]
        return IV(min(v) // SCALE, ceildiv(max(v), SCALE))
    __rmul__ = __mul__

    def __truediv__(self, other) -> 'IV':
        other = coerce(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError("Interval denominator contains zero")
        floors, ceils = [], []
        for a in (self.lo, self.hi):
            for b in (other.lo, other.hi):
                n, den = a * SCALE, b
                if den < 0:
                    n, den = -n, -den
                floors.append(n // den)
                ceils.append(ceildiv(n, den))
        return IV(min(floors), max(ceils))

    def __rtruediv__(self, other) -> 'IV':
        return coerce(other) / self

    def __pow__(self, n: int) -> 'IV':
        if n < 0:
            return IV.rat(1) / (self ** (-n))
        out = IV.rat(1)
        base = self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n //= 2
        return out

    def abs_upper(self) -> 'IV':
        return IV.exact_grid(max(abs(self.lo), abs(self.hi)))

    def enlarge(self, radius: 'IV') -> 'IV':
        if radius.hi < 0:
            raise ValueError("Negative error bound")
        return IV(self.lo - radius.hi, self.hi + radius.hi)

    def decimal(self, places: int = 24) -> list[str]:
        """Outward decimal display, not a floating-point conversion."""
        den = 10 ** (DIGITS - places)
        lower = self.lo // den
        upper = ceildiv(self.hi, den)
        def fmt(n):
            sign = '-' if n < 0 else ''
            n = abs(n)
            whole, frac = divmod(n, 10 ** places)
            return f'{sign}{whole}.{frac:0{places}d}'
        return [fmt(lower), fmt(upper)]


def coerce(x) -> IV:
    if isinstance(x, IV):
        return x
    if isinstance(x, int):
        return IV.rat(x)
    raise TypeError(f"Unsupported nonexact input {type(x)!r}")


def atan_small(x: IV, terms: int = 80) -> IV:
    assert 0 <= x.lo and x.hi < SCALE
    total = IV.rat(0)
    power = x
    square = x * x
    for k in range(terms):
        term = power / (2 * k + 1)
        total = total + (term if k % 2 == 0 else -term)
        power = power * square
    tail = x.abs_upper() ** (2 * terms + 1) / (2 * terms + 1)
    return total.enlarge(tail)


def sin_small(x: IV, terms: int = 32) -> IV:
    assert 0 <= x.lo and x.hi <= SCALE
    total = IV.rat(0)
    for k in range(terms):
        term = x ** (2 * k + 1) / math.factorial(2 * k + 1)
        total = total + (term if k % 2 == 0 else -term)
    tail = x.abs_upper() ** (2 * terms + 1) / math.factorial(2 * terms + 1)
    return total.enlarge(tail)


def cos_small(x: IV, terms: int = 32) -> IV:
    assert 0 <= x.lo and x.hi <= SCALE
    total = IV.rat(0)
    for k in range(terms):
        term = x ** (2 * k) / math.factorial(2 * k)
        total = total + (term if k % 2 == 0 else -term)
    tail = x.abs_upper() ** (2 * terms) / math.factorial(2 * terms)
    return total.enlarge(tail)


def log_positive(x: IV, terms: int = 320) -> IV:
    assert x.lo > 0
    z = (x - 1) / (x + 1)
    r = z.abs_upper()
    assert r.hi < SCALE
    total = IV.rat(0)
    power = z
    square = z * z
    for k in range(terms):
        total = total + power / (2 * k + 1)
        power = power * square
    tail = 2 * r ** (2 * terms + 1) / ((2 * terms + 1) * (1 - r * r))
    return (2 * total).enlarge(tail)


def F(alpha: IV, beta: IV, s: IV) -> IV:
    p11 = alpha * beta - s
    p10 = alpha * (1 - beta) + s
    p01 = (1 - alpha) * beta + s
    p00 = (1 - alpha) * (1 - beta) - s
    assert min(p.lo for p in (p11, p10, p01, p00)) > 0
    odds = p11 * p00 / (p10 * p01)
    return s * sum((1 / p for p in (p11, p10, p01, p00)), IV.rat(0)) + log_positive(odds)


def inside(x: IV, low_n: int, high_n: int, den: int) -> bool:
    return x.lo * den >= low_n * SCALE and x.hi * den <= high_n * SCALE


def main() -> dict:
    # Machin's identity: pi = 16 atan(1/5) - 4 atan(1/239).
    pi = 16 * atan_small(IV.rat(1, 5)) - 4 * atan_small(IV.rat(1, 239))
    c = IV.rat(19, 20)

    # Unconditional true-sine counterexample: rho=9/20, a=1/200;
    # pair {0,3}, reveal 4.  These are genuine principal compressions.
    d = IV.rat(173, 400)
    z = -c * cos_small(3 * pi / 20) / (3 * pi)
    b0 = -c * sin_small(pi / 5) / (4 * pi)
    b3 = c * cos_small(pi / 20) / pi
    coarse = F(d, d, z * z)
    after1 = F(d - b0 * b0 / d,
               d - b3 * b3 / d,
               (z - b0 * b3 / d) ** 2)
    after0 = F(d + b0 * b0 / (1 - d),
               d + b3 * b3 / (1 - d),
               (z + b0 * b3 / (1 - d)) ** 2)
    drift = d * after1 + (1 - d) * after0 - coarse
    assert inside(drift, -177080, -177078, 10 ** 9)
    assert drift.hi < 0

    # A conditional-on-background strengthening of the star theorem is false.
    # rho=1/2, c=19/20, a=1/2000; center 0, core leaf 7,
    # old leaves {-1,1} fixed to 00, new leaf -3.
    ds = IV.rat(951, 2000)
    w = c * c / (pi * pi)
    s = w / 49
    wr = w / 9
    beta = ds + 2 * w / (1 - ds)
    cond_drift = (ds * F(ds, beta - wr / ds, s)
                  + (1 - ds) * F(ds, beta + wr / (1 - ds), s)
                  - F(ds, beta, s))
    assert inside(cond_drift, -74327, -74325, 10 ** 11)
    assert cond_drift.hi < 0

    # The corresponding unconditional drift, averaging ALL four old-leaf words.
    uncond_drift = IV.rat(0)
    for y1 in (0, 1):
        for y2 in (0, 1):
            p = (ds if y1 else 1-ds) * (ds if y2 else 1-ds)
            bb = ds + w * ((1-y1)/(1-ds) - y1/ds
                          + (1-y2)/(1-ds) - y2/ds)
            gap = (ds * F(ds, bb - wr/ds, s)
                   + (1-ds) * F(ds, bb + wr/(1-ds), s)
                   - F(ds, bb, s))
            uncond_drift = uncond_drift + p * gap
    assert uncond_drift.lo > 0

    # Infinite half-density midpoint star, nearest pair:
    # sum_{odd n in Z} |K(0,n)|^4 = c^4/48.
    half = IV.rat(1, 2)
    nearest_s = c*c/(pi*pi)
    base = F(half, half, nearest_s)
    lower_bound = base + 16384 * nearest_s ** 3 * (c ** 4 / 48 - nearest_s ** 2)
    assert lower_bound.lo * 100000 > 26275 * SCALE

    result = {
        "status": "PASS_EXACT_RATIONAL_INTERVAL_CERTIFICATES",
        "arithmetic": "outward-rounded integer intervals on a 10^-80 grid",
        "transcendentals": "Machin/alternating sin-cos/atanh-log Taylor bounds",
        "pi": pi.decimal(40),
        "unconditional_sine_pair_counterexample": {
            "rho": "9/20", "c": "19/20", "a": "1/200",
            "core": [0, 3], "reveal": 4,
            "coarse_pair_mean": coarse.decimal(),
            "after_reveal_1_pair_mean": after1.decimal(),
            "after_reveal_0_pair_mean": after0.decimal(),
            "unconditional_drift": drift.decimal(),
            "coarse_rational_enclosure": ["-0.000177080", "-0.000177078"]
        },
        "conditional_background_star_counterexample": {
            "rho": "1/2", "c": "19/20", "a": "1/2000",
            "core": [0, 7], "old_background": [-1, 1],
            "background_word": [0, 0], "reveal": -3,
            "conditional_background_drift": cond_drift.decimal(),
            "unconditional_drift": uncond_drift.decimal(),
            "coarse_rational_enclosure": ["-0.00000074327", "-0.00000074325"]
        },
        "infinite_midpoint_nearest_star_lower_bound": {
            "rho": "1/2", "c": "19/20", "a": "1/40",
            "base_pair_mean": base.decimal(),
            "proved_lower_bound_value": lower_bound.decimal(),
            "certified_statement": "star pair expectation > 0.26275"
        }
    }
    return result

if __name__ == '__main__':
    data = main()
    out = Path(__file__).with_name('S75_CERTIFICATES.json')
    out.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(data, indent=2))
