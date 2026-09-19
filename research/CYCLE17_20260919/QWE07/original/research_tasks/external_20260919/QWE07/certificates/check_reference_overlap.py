#!/usr/bin/env python3
"""Non-load-bearing cross-check with the independently reviewed S63 bias polynomial."""
from fractions import Fraction as F
from pathlib import Path
import argparse
p=argparse.ArgumentParser();p.add_argument('source_coefficients');p.add_argument('nodes');a=p.parse_args()
coeffs=[tuple(map(int,s.split())) for s in Path(a.source_coefficients).read_text().splitlines() if s.strip()]
assert len(coeffs)==10
count=0
for line in Path(a.nodes).read_text().splitlines():
 if not line.strip() or line.startswith('#'):continue
 j,k,lo,hi,den=map(int,line.split())
 if j:continue
 aa=F(84+3*k,4000);t=200*aa-5;L=F(0);U=F(0)
 for i,(l,h) in enumerate(coeffs):
  choices=[F(l,10**8)*t**i,F(h,10**8)*t**i]
  L+=min(choices);U+=max(choices)
 L-=F(1,10**6);U+=F(1,10**6)
 assert max(L,F(lo,den))<=min(U,F(hi,den)),k
 count+=1
assert count==5
print('CONSISTENCY PASS: all five rho=1/3 nodal enclosures overlap S63 polynomial enclosures.')
print('S63 coefficient intervals and its 1e-6 tail allowance are used only in this cross-check.')
