#!/usr/bin/env python3
"""Assemble published A_k boxes from direct outward integer enclosures.
Each raw file contains integer lower/upper enclosures for
<q_k,V0> and <q_k,V1>, followed by the common denominator.
All arithmetic below is exact. One additional 1e-8 publication unit is
added on each side.
"""
from fractions import Fraction as F
from pathlib import Path
R=Path(__file__).resolve().parent
raw=[]
for k in range(8):
    al,ah,bl,bh,den=map(int,(R/f'raw_integer_s69_{k}.txt').read_text().split())
    assert al<=ah and bl<=bh and den>0
    raw.append((F(al,den),F(ah,den),F(bl,den),F(bh,den)))
A=[(raw[0][0],raw[0][1])]
for k in range(1,8):
    A.append((raw[k][0]+raw[k-1][2]/200,
              raw[k][1]+raw[k-1][3]/200))
A.append((raw[7][2]/200,raw[7][3]/200))
PUB=10**8
out=[]
for lo,hi in A:
    L=(lo*PUB).numerator//(lo*PUB).denominator-1
    # exact ceiling
    x=hi*PUB; U=-((-x.numerator)//x.denominator)+1
    out.append((L,U))
text=''.join(f'{L} {U}\n' for L,U in out)
path=R/'payment_coefficients_s69_integer.txt'
if path.exists():
    assert path.read_text()==text, 'published coefficient file differs'
else:
    path.write_text(text)
for k,(L,U) in enumerate(out):
    print(f'COEFFICIENT {k} {L} {U} denominator 100000000')
print('ASSEMBLE PAYMENT COEFFICIENTS PASS (exact raw-integer path)')
