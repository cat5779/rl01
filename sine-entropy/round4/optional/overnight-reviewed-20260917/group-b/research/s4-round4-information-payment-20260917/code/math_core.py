#!/usr/bin/env python3
"""Finite rational product-channel calculations; no third-party dependencies.

The elementary determinant, Fourier Vandermonde weights, and likelihood-jet
routines adapt the assistant's round-3 exact checker. They are infrastructure,
not this round's new result. All payment/log-odds tests are in exact_check.py.
"""
from __future__ import annotations
import itertools
import math
import sys
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from typing import Iterable

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
ZERO, ONE = F(0), F(1)

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def fs(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f'{x.numerator}/{x.denominator}'

def bits(n: int) -> list[tuple[int, ...]]:
    return list(itertools.product((0, 1), repeat=n))

def dot(x: Iterable[F], y: Iterable[F]) -> F:
    return sum((a*b for a, b in zip(x, y)), ZERO)

def determinant(a: list[list[F]]) -> F:
    n = len(a)
    m = [list(row) for row in a]
    out = ONE
    for j in range(n):
        pivot = next((r for r in range(j, n) if m[r][j]), None)
        if pivot is None:
            return ZERO
        if pivot != j:
            m[j], m[pivot] = m[pivot], m[j]
            out = -out
        value = m[j][j]
        out *= value
        for r in range(j+1, n):
            fac = m[r][j] / value
            for l in range(j+1, n):
                m[r][l] -= fac*m[j][l]
    return out

def fourier_law(n: int, k: int):
    """Exact consecutive Fourier atoms for n=4 or 6 via squared chords."""
    chords = {4: [0, 2, 4, 2], 6: [0, 1, 3, 4, 3, 1]}[n]
    xs, ws = [], []
    for A in itertools.combinations(range(n), k):
        weight = F(1, n**k)
        for i, j in itertools.combinations(A, 2):
            weight *= chords[(j-i) % n]
        xs.append(tuple(int(i in A) for i in range(n)))
        ws.append(weight)
    require(sum(ws) == 1, 'Fourier atom normalization')
    return xs, ws

def kernel_law(K: list[list[F]]):
    n = len(K)
    for i in range(n):
        off = sum((abs(K[i][j]) for j in range(n) if j != i), ZERO)
        require(0 < K[i][i]-off and K[i][i]+off < 1,
                'Strict contraction certified by Gershgorin')
    xs, ws = bits(n), []
    for x in xs:
        S = [i for i in range(n) if x[i]]
        rest = [i for i in range(n) if not x[i]]
        value = ZERO
        for z in bits(len(rest)):
            A = S+[i for i, yes in zip(rest, z) if yes]
            value += (-1)**sum(z)*determinant([[K[i][j] for j in A] for i in A])
        ws.append(value)
    require(min(ws) > 0 and sum(ws) == 1, 'Positive contraction atoms')
    return xs, ws

def contraction_law(scale: F = ONE):
    K = [[F(2,5), F(1,10), F(1,20)],
         [F(1,10), F(3,10), F(-7,100)],
         [F(1,20), F(-7,100), F(3,5)]]
    return kernel_law([[scale*x for x in row] for row in K])

def moments(xs, ws):
    n = len(xs[0])
    q = [sum((w*x[i] for x, w in zip(xs, ws)), ZERO) for i in range(n)]
    C = [[sum((w*x[i]*x[j] for x, w in zip(xs, ws)), ZERO)-q[i]*q[j]
          for j in range(n)] for i in range(n)]
    return q, C

def tilt(xs, ws, multipliers):
    weights = [w*math.prod(multipliers[i] for i in range(len(x)) if x[i])
               for x, w in zip(xs, ws)]
    total = sum(weights)
    return [w/total for w in weights]

def likelihood(x, y, a: F, c: F, coords=None) -> F:
    indices = range(len(x)) if coords is None else coords
    return math.prod((a+c*x[i]) if y[i] else (1-a-c*x[i]) for i in indices)

def jets(xs, mu, a: F, c: F):
    """Full p,p',p'', posterior and its first/second response. No affine atoms."""
    n = len(xs[0])
    result = {}
    for y in bits(n):
        p = [ZERO]*3
        h = [[ZERO]*n for _ in range(3)]
        weights = []
        for x, m in zip(xs, mu):
            f0, f1, f2 = ONE, ZERO, ZERO
            for i in range(n):
                g = a+c*x[i] if y[i] else 1-a-c*x[i]
                s = F(2*y[i]-1)
                f0, f1, f2 = f0*g, f1*g+f0*s, f2*g+2*f1*s
            weights.append(m*f0)
            for j, f in enumerate((f0, f1, f2)):
                p[j] += m*f
                for i in range(n):
                    h[j][i] += m*f*x[i]
        require(p[0] > 0, 'Positive interior output atom')
        r = [z/p[0] for z in h[0]]
        r1 = [(h[1][i]-p[1]*r[i])/p[0] for i in range(n)]
        r2 = [(h[2][i]-p[2]*r[i]-2*p[1]*r1[i])/p[0] for i in range(n)]
        post = [w/p[0] for w in weights]
        _, C = moments(xs, post)
        result[y] = dict(p=p, h=h, r=r, r1=r1, r2=r2, mu=post, C=C)
    require([sum(v['p'][j] for v in result.values()) for j in range(3)]
            == [ONE, ZERO, ZERO], 'Probability jets normalize')
    return result

# Every interval below is rational. No floating logarithm is used.
LOG_SCALE = 10**42
LOG_TERMS = 52

def floor_fraction(x: F) -> int:
    return x.numerator // x.denominator

def ceil_fraction(x: F) -> int:
    return -((-x.numerator)//x.denominator)

def quantize(lo: F, hi: F, digits: int = 36):
    scale = 10**digits
    return F(floor_fraction(lo*scale), scale), F(ceil_fraction(hi*scale), scale)

def _series_log(r: F):
    z = (r-1)/(r+1)
    require(0 <= z <= F(1,3), 'Log reduction interval')
    z2, power, total = z*z, z, ZERO
    for j in range(LOG_TERMS):
        total += 2*power/(2*j+1)
        power *= z2
    tail = 2*power/((2*LOG_TERMS+1)*(1-z2))
    return total, total+tail

_LN2 = _series_log(F(2))

@lru_cache(maxsize=None)
def log_interval(q: F):
    require(q > 0, 'Positive logarithm argument')
    if q == 1:
        return ZERO, ZERO
    if q < 1:
        lo, hi = log_interval(1/q)
        return -hi, -lo
    k = q.numerator.bit_length()-q.denominator.bit_length()
    r = q / (F(2)**k)
    while r < 1:
        r *= 2
        k -= 1
    while r > 2:
        r /= 2
        k += 1
    lo, hi = _series_log(r)
    if k >= 0:
        lo, hi = lo+k*_LN2[0], hi+k*_LN2[1]
    else:
        lo, hi = lo+k*_LN2[1], hi+k*_LN2[0]
    return quantize(lo, hi, 42)

def interval_add(x, y):
    return x[0]+y[0], x[1]+y[1]

def interval_scale(x, a: F):
    return (a*x[0], a*x[1]) if a >= 0 else (a*x[1], a*x[0])

def show_interval(x, digits: int = 30):
    lo, hi = quantize(*x, digits)
    return {'lower': fs(lo), 'upper': fs(hi), 'meaning': 'closed rational enclosure'}

def safe_output(path: Path, root: Path) -> Path:
    result = path.resolve()
    protected = [(root/'evidence').resolve(), (root/'receipts').resolve()]
    if any(result == folder or folder in result.parents for folder in protected):
        raise ValueError('Refusing to write in frozen evidence; choose an output directory.')
    result.mkdir(parents=True, exist_ok=True)
    return result
