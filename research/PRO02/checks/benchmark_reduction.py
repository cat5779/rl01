"""Numerical evaluation of the proved reserve/tail reductions.

Only elementary closed formulas are evaluated.  This file does not certify
the unknown window term W_{m,L}.
"""

from __future__ import annotations

import math
from fractions import Fraction as F


c = F(19, 20)
beta = F(39, 1600)
kappa = F(361, 39)
gamma_ro = F(296960000, 6591)
A_ro = F(50251200, 2197)
A_ro_reserved = c * c * A_ro


def odd_number_variance(m: int) -> float:
    """Var of the number of points in m consecutive sites at density 1/2."""
    return m / 4 - (2 / math.pi**2) * sum(
        (m - r) / (r * r) for r in range(1, m) if r % 2
    )


ell = (400 * math.log(400 / 39) - 361) / 361
C_pair = float(c * c / (beta * beta)) * ell
C_old = float(3 * c * c / (2 * beta * beta)) * math.log(1521)

print(f"beta={beta}")
print(f"kappa={kappa}")
print(f"Gamma_ro={gamma_ro} ~= {float(gamma_ro):.12f}")
print(f"A_ro={A_ro} ~= {float(A_ro):.12f}")
print(f"A_ro_with_reserve={A_ro_reserved} ~= {float(A_ro_reserved):.12f}")
print(f"reserve_factor={c*c} ~= {float(c*c):.12f}")
print(f"C_pair={C_pair:.12f}")
print(f"C_old={C_old:.12f}")
print("m,var_m,new_pair_per_site,old_tail_per_site")
for m in (4, 8, 16, 64, 256, 1000, 5000, 100000):
    var = odd_number_variance(m)
    old = C_old * sum(1 / k for k in range(1, m + 1)) / m
    new = C_pair * var / m
    print(f"{m},{var:.12f},{new:.12f},{old:.12f}")
