#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
R=Path(__file__).resolve().parent
caps=[tuple(map(int,s.split())) for s in (R/'guard_caps_integer.txt').read_text().splitlines()]
assert len(caps)==256
for a in (F(51,2000),F(13,500)):
    C=F(6501,5000)+F(2067,400)*a+F(1,1000)
    for L,U in caps:
        cap=((F(3,100)-a)*L+(a-F(1,50))*U)/100
        delta=C-cap
        assert 0<=delta<=C/2
print('TIGHT 026 PROBE PSD PASS Cdagger=Cbar+1/1000 on [51/2000,13/500]')
