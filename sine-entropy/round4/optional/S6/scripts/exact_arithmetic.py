"""Small, exact arithmetic utilities; Python standard library only.

Nothing in this module writes files.  Gaussian rationals, matrix operations,
second-order jets, sparse Grassmann multiplication, and logarithm enclosures
are independent of floating-point arithmetic.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from typing import Iterable


@dataclass(frozen=True)
class QC:
    re: F = F(0)
    im: F = F(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "re", F(self.re))
        object.__setattr__(self, "im", F(self.im))

    @staticmethod
    def coerce(other: object) -> "QC":
        if isinstance(other, QC):
            return other
        if isinstance(other, (int, F)):
            return QC(F(other))
        return NotImplemented

    def __add__(self, other: object) -> "QC":
        z = self.coerce(other)
        if z is NotImplemented:
            return NotImplemented
        return QC(self.re + z.re, self.im + z.im)

    __radd__ = __add__

    def __neg__(self) -> "QC":
        return QC(-self.re, -self.im)

    def __sub__(self, other: object) -> "QC":
        z = self.coerce(other)
        if z is NotImplemented:
            return NotImplemented
        return self + (-z)

    def __rsub__(self, other: object) -> "QC":
        z = self.coerce(other)
        if z is NotImplemented:
            return NotImplemented
        return z + (-self)

    def __mul__(self, other: object) -> "QC":
        z = self.coerce(other)
        if z is NotImplemented:
            return NotImplemented
        return QC(self.re*z.re - self.im*z.im, self.re*z.im + self.im*z.re)

    __rmul__ = __mul__

    def conjugate(self) -> "QC":
        return QC(self.re, -self.im)

    def abs2(self) -> F:
        return self.re*self.re + self.im*self.im

    def __truediv__(self, other: object) -> "QC":
        z = self.coerce(other)
        if z is NotImplemented:
            return NotImplemented
        norm = z.abs2()
        if norm == 0:
            raise ZeroDivisionError("Gaussian rational division by zero")
        return self*z.conjugate()*QC(F(1)/norm)

    def __bool__(self) -> bool:
        return bool(self.re or self.im)

    def real(self) -> F:
        if self.im != 0:
            raise ArithmeticError(f"Expected real Gaussian rational, got {self}")
        return self.re


def eye(n: int) -> list[list[QC]]:
    return [[QC(int(i == j)) for j in range(n)] for i in range(n)]


def adjoint(a: list[list[QC]]) -> list[list[QC]]:
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def matmul(a: list[list[QC]], b: list[list[QC]]) -> list[list[QC]]:
    if len(a[0]) != len(b):
        raise ValueError("Incompatible matrix dimensions")
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), QC())
             for j in range(len(b[0]))] for i in range(len(a))]


def inverse(a: list[list[QC]]) -> list[list[QC]]:
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("Matrix must be square")
    b = [row[:] + ident for row, ident in zip(a, eye(n))]
    for j in range(n):
        pivot = next((i for i in range(j, n) if b[i][j]), None)
        if pivot is None:
            raise ArithmeticError("Singular matrix")
        b[j], b[pivot] = b[pivot], b[j]
        p = b[j][j]
        b[j] = [v/p for v in b[j]]
        for i in range(n):
            if i != j and b[i][j]:
                p = b[i][j]
                b[i] = [x - p*y for x, y in zip(b[i], b[j])]
    return [row[n:] for row in b]


def determinant(a: list[list[QC]]) -> QC:
    n = len(a)
    if n == 0:
        return QC(1)
    if any(len(row) != n for row in a):
        raise ValueError("Matrix must be square")
    b = [row[:] for row in a]
    result = QC(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if b[i][j]), None)
        if pivot is None:
            return QC()
        if pivot != j:
            b[j], b[pivot] = b[pivot], b[j]
            result = -result
        p = b[j][j]
        result *= p
        for i in range(j+1, n):
            if b[i][j]:
                r = b[i][j]/p
                for k in range(j+1, n):
                    b[i][k] -= r*b[j][k]
    return result


def principal(a: list[list[QC]], mask: int) -> list[list[QC]]:
    indices = [i for i in range(len(a)) if (mask >> i) & 1]
    return [[a[i][j] for j in indices] for i in indices]


@dataclass(frozen=True)
class Jet:
    """Value, first derivative, second derivative (not Taylor coefficients)."""
    v: F
    d1: F = F(0)
    d2: F = F(0)

    def __add__(self, other: "Jet") -> "Jet":
        return Jet(self.v+other.v, self.d1+other.d1, self.d2+other.d2)

    def __mul__(self, other: "Jet") -> "Jet":
        return Jet(self.v*other.v,
                   self.d1*other.v+self.v*other.d1,
                   self.d2*other.v+2*self.d1*other.d1+self.v*other.d2)

    def scale(self, w: F) -> "Jet":
        return Jet(w*self.v, w*self.d1, w*self.d2)


Interval = tuple[F, F]


def iadd(a: Interval, b: Interval) -> Interval:
    return a[0]+b[0], a[1]+b[1]


def iscale(c: F, a: Interval) -> Interval:
    return (c*a[0], c*a[1]) if c >= 0 else (c*a[1], c*a[0])


def isum(items: Iterable[Interval]) -> Interval:
    out = (F(0), F(0))
    for item in items:
        out = iadd(out, item)
    return out


def _log_unit_interval(x: F, terms: int) -> Interval:
    """Enclose log(x) for 1 <= x <= 2, using positive atanh terms."""
    if not F(1) <= x <= F(2):
        raise ValueError("Range reduction failure")
    z = (x-1)/(x+1)
    z2 = z*z
    power = z
    lower = F(0)
    for j in range(terms):
        lower += 2*power/(2*j+1)
        power *= z2
    # First omitted power is z**(2*terms+1).
    tail = 2*power/((2*terms+1)*(1-z2))
    return lower, lower+tail


def log_interval(x: F, terms: int = 40) -> Interval:
    """A rigorous rational enclosure of log(x), x positive rational.

    The remainder uses 1/(2j+1) <= 1/(2N+1), j >= N.  No external
    transcendental routine and no floating-point arithmetic are used.
    """
    x = F(x)
    if x <= 0 or terms < 1:
        raise ValueError("Need x > 0 and terms >= 1")
    exponent = 0
    while x < 1:
        x *= 2
        exponent -= 1
    while x > 2:
        x /= 2
        exponent += 1
    return iadd(_log_unit_interval(x, terms),
                iscale(F(exponent), _log_unit_interval(F(2), terms)))


def mul_mask(a: int, b: int) -> tuple[int, int] | None:
    """Product of canonical Grassmann monomials; returns mask and sign."""
    if a & b:
        return None
    swaps = 0
    aa = a
    while aa:
        bit = aa & -aa
        swaps += (b & (bit-1)).bit_count()
        aa ^= bit
    return a | b, (-1 if swaps % 2 else 1)


def multiply_binomial(poly: dict[int, QC], mask: int, coefficient: QC) -> dict[int, QC]:
    """Multiply a Grassmann polynomial by 1 + coefficient * monomial."""
    out = poly.copy()
    for old, value in poly.items():
        product = mul_mask(old, mask)
        if product is not None:
            new, sign = product
            out[new] = out.get(new, QC()) + sign*value*coefficient
    return {mask: value for mask, value in out.items() if value}


def berezin_replica_polynomial(a: list[list[QC]], replicas: int = 2) -> tuple[list[F], dict[str, int]]:
    """Exact coefficients of integral exp(Q + t*sum_i product_r eta_ir).

    Canonical variable order is (bar_0,chi_0,...,bar_{n-1},chi_{n-1})
    within each replica, with replica 0 first.  The integral extracts the
    top monomial in that order.  Matrix entries may be Gaussian rationals.
    """
    n = len(a)
    if replicas < 1:
        raise ValueError("Positive integer replica count required")
    poly: dict[int, QC] = {0: QC(1)}
    max_terms = 1
    for r in range(replicas):
        for i in range(n):
            for j in range(n):
                if not a[i][j]:
                    continue
                first, second = 2*(r*n+i), 2*(r*n+j)+1
                sign = 1 if first < second else -1
                mask = (1 << first) | (1 << second)
                poly = multiply_binomial(poly, mask, sign*a[i][j])
                max_terms = max(max_terms, len(poly))
    gaussian_terms = len(poly)
    extended: dict[tuple[int, int], QC] = {(mask, 0): value for mask, value in poly.items()}
    for i in range(n):
        mask = sum(3 << (2*(r*n+i)) for r in range(replicas))
        out = extended.copy()
        for (old, degree), value in extended.items():
            product = mul_mask(old, mask)
            if product is not None:
                new, sign = product
                key = (new, degree+1)
                out[key] = out.get(key, QC()) + sign*value
        extended = {key: value for key, value in out.items() if value}
    top = (1 << (2*n*replicas))-1
    result = [extended.get((top, degree), QC()).real() for degree in range(n+1)]
    return result, {"gaussian_terms": gaussian_terms,
                    "final_terms": len(extended), "max_gaussian_terms": max_terms}
