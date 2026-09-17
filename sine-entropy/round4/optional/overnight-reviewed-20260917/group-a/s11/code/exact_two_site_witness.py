#!/usr/bin/env python3
"""Exact rational replay of the two-site product witness and signed tail."""
from fractions import Fraction as F

c0=F(37,40)
c1=F(463,500)
h=c1-c0
x=(1-c1)/2
delta=F(1,50)

def b2(p:F)->F:
    return -1/(p*(1-p))

pc=x+c1
pd=x+c0
base=F(1,2)*(b2(pd)+b2(x))
target=F(1,2)*(b2(pc)+b2(x))
full=target-base
m1=F(0)
m2=120*h*c0/(1+delta)**4
higher=full-m1-m2

assert x==F(37,1000)
assert pc==F(963,1000)
assert pd==F(481,500)
assert base==F(-243_875_000,8_800_857)
assert target==F(-1_000_000,35_631)
assert full==F(-3_125_000,8_800_857)
assert m2==F(231_250,2_255_067)
assert higher==F(-1_009_142_506_250,2_205_169_132_491)
assert full<0<m2 and higher<0
print("x",x)
print("base_full_curvature",base)
print("target_full_curvature",target)
print("full_response",full)
print("mode1_response",m1)
print("mode2_response_at_delta_1_over_50",m2)
print("modes_m_ge_3_response",higher)
print("EXACT_TWO_SITE_SIGNED_CANCELLATION_PASS")
