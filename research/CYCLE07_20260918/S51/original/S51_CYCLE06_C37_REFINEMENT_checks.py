#!/usr/bin/env python3
"""Exact rational checks for the S51 c>37/40 refinement.

These checks verify only the displayed arithmetic constants.  They are not an
independent certification of the mathematical source interfaces.
"""
from fractions import Fraction as F


def qceil(x: F) -> int:
    return (x.numerator + x.denominator - 1) // x.denominator


# ---------------------------------------------------------------------------
# 1. Mixed a,a,c response near c*=937/1000.
# Rectangle: c in [0, 471/500], a in [17/1000, 41/1000].
# Spectral gap delta=17/1000, hence r=(1-delta)/(1+delta)=983/1017.
# ---------------------------------------------------------------------------
r3 = F(983, 1017)
S1_3 = r3 / (1 - r3) ** 2
S2_3 = r3 * (1 + r3) / (1 - r3) ** 3
assert S1_3 < 865
assert S2_3 < 50871

# a-angular margin on the moving midpoint a=(1-c)/2.
sigma_a_sq_exact = F(551, 576)
assert sigma_a_sq_exact > F(39, 40) ** 2

# c-angular margin through c*=937/1000+3e-13.
c_star = F(937, 1000)
Delta_c = F(3, 10**13)
c_top = c_star + Delta_c
c_outer_top = F(471, 500)
# ell_c*sigma_c = 2*sqrt(c*(c_outer_top-c)); square the inequality.
assert 4 * c_top * (c_outer_top - c_top) > F(17, 125) ** 2

ell_a = F(3, 125)
ell_c_sigma_c_lower = F(17, 125)
sigma_a_lower = F(39, 40)
L_aac = (
    F(64) * S2_3
    / (ell_c_sigma_c_lower * ell_a**2 * sigma_a_lower**2)
    + F(32) * S1_3
    / (ell_c_sigma_c_lower * ell_a**2 * sigma_a_lower**3)
)
assert L_aac < 45_000_000_000

# ---------------------------------------------------------------------------
# 2. Fourth a derivative on a common rectangle for
#    c in [37/40, 937/1000+3e-13], |a-(1-c)/2| <= 1e-9.
# Use outer c cap 9371/10000 and delta=73/5000.
# ---------------------------------------------------------------------------
delta4 = F(73, 5000)
r4 = (1 - delta4) / (1 + delta4)  # 4927/5073
assert r4 == F(4927, 5073)
S0_4 = r4 / (1 - r4)
S1_4 = r4 / (1 - r4) ** 2
S2_4 = r4 * (1 + r4) / (1 - r4) ** 3
S3_4 = r4 * (1 + 4 * r4 + r4**2) / (1 - r4) ** 4
assert S0_4 < 34
assert S1_4 < 1173
assert S2_4 < 80314
assert S3_4 < 8250807

c_outer4 = F(9371, 10000)
a4_left = delta4
a4_right = 1 - c_outer4 - delta4
ell4 = a4_right - a4_left
assert a4_left == F(146, 10000)
assert a4_right == F(483, 10000)
assert ell4 == F(337, 10000)

# Worst target point for the angular margin is the largest a:
# c=37/40 and s=+1e-9.
x_target_max = F(3, 80) + F(1, 10**9)
sigma4_sq = 4 * (x_target_max - a4_left) * (a4_right - x_target_max) / ell4**2
assert sigma4_sq > F(93, 100) ** 2

sigma4_lower = F(93, 100)
M4 = F(16, 1) / ell4**4 * (
    (16 * S3_4 + 44 * S1_4) / sigma4_lower**4
    + (48 * S2_4 + 12 * S0_4) / sigma4_lower**5
    + (60 * S1_4) / sigma4_lower**6
    + (30 * S0_4) / sigma4_lower**7
)
M4_upper = F(23, 10) * 10**15
assert M4 < M4_upper

# ---------------------------------------------------------------------------
# 3. Final curvature budget.
# Balanced-line seed: -1/50.
# c-extension loss <= 45e9 * 3e-13 = 0.0135.
# off-midpoint loss <= (1/2)*(2.3e15)*(1e-9)^2 = 0.00115.
# ---------------------------------------------------------------------------
midpoint_upper = -F(1, 50) + F(45_000_000_000) * Delta_c
assert midpoint_upper == -F(13, 2000)

off_midpoint_loss = F(1, 2) * M4_upper * F(1, 10**9) ** 2
assert off_midpoint_loss == F(23, 20000)

final_upper = midpoint_upper + off_midpoint_loss
assert final_upper == -F(107, 20000)
assert final_upper <= -F(1, 200)

print("Exact rational checks passed.")
print(f"S1(mixed) = {float(S1_3):.12f}")
print(f"S2(mixed) = {float(S2_3):.12f}")
print(f"L_aac exact bound = {float(L_aac):.6e} < 4.5e10")
print(f"M4 exact bound = {float(M4):.6e} < 2.3e15")
print(f"final normalized curvature upper bound = {float(final_upper):.9f}")
