#!/usr/bin/env python3
"""Exact obstruction for the unchanged sufficient payment, not for entropy."""
from fractions import Fraction as F
from decimal import Decimal
from pathlib import Path
import re
for name,expected_rho in [('probe_034.log',F(17,50)),('probe_half.log',F(1,2))]:
    text=Path(name).read_text();s=text.split()
    assert s[0]=='PROBE'
    rho=F(int(s[1]),int(s[2]));a=F(int(s[3]),int(s[4]));assert rho==expected_rho and a==F(3,125)
    assert s[5]=='P_interval'
    lo,hi,den=map(int,s[6:9]);assert lo<=hi and den==10**8
    assert s[9:11]==['leaves','4194304']
    m=re.search(r'mass \[([^,]+),([^]]+)\]',text)
    assert m and Decimal(m[1])<=1<=Decimal(m[2])
    c=F(19,20);C=F(261,200)+F(51,10)*a
    budget=(C-1)*((1-rho)/(a*(1-a))+rho/((a+c)*(1-a-c)))
    L,U=F(lo,den)-budget,F(hi,den)-budget
    assert U<0
    print('rho',rho,'a',a,'P enclosure',F(lo,den),F(hi,den))
    print('exact budget',budget,'; exact payment gap enclosure',L,U,'< 0')
    scale=10**8
    nlo=L.numerator*scale//L.denominator
    nhi=-((-U.numerator*scale)//U.denominator)
    print('gap outward integer enclosure:',nlo,nhi,'/',scale)
print('DISPROVED: unchanged-test sufficient payment at the two stated points.')
print('No entropy-concavity counterexample is asserted.')
