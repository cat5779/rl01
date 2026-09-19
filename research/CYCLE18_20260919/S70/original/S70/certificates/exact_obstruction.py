#!/usr/bin/env python3
"""Exact enclosure of the fixed witness payment at a point outside the certified rectangle.
This is an obstruction to this chosen sufficient witness, NOT to entropy concavity.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
c,p=F(24,25),F(9,20)
ep,ec=p-F(1,2),c-F(19,20)
s=(1-c)*ep;v=ec/F(19,20);t,u=200*s,1000*ec
lower=upper=F(0)
for line in Path('quad_payment_coefficients_bivariate.txt').read_text().splitlines():
 if not line.strip() or line.startswith('#'):continue
 z=list(map(int,line.split()));k,l=z[:2]
 for j,factor in enumerate([F(1),ep,ec]):
  w=t**k*u**l*factor;lo,hi=F(z[2+2*j],10**9),F(z[3+2*j],10**9)
  lower+=min(lo*w,hi*w);upper+=max(lo*w,hi*w)
norms=list(map(int,Path('quad_payment_norms_integer.txt').read_text().split()))
Vmax=norms[0]+abs(ep)*norms[1]+abs(ec)*norms[2]
beta=22*(2*abs(s)+abs(v));assert beta<10
tail=Vmax*beta**9/F(factorial(9))/(1-beta/10)
lower-=tail;upper+=tail
a=(1-c)*p;d=F(2,3)/(a*(1-a))+F(1,3)/((a+c)*(1-a-c))
C=F(1303,1000)+F(51,200)*p+8*ec
gl,gh=lower-(C-1)*d,upper-(C-1)*d
assert gh<F(-3),gh
out={'status':'PROVED','scope':'payment obstruction for this fixed affine-C four-target witness ONLY; not an entropy-concavity counterexample',
 'c':str(c),'p':str(p),'a':str(a),'t':str(t),'u':str(u),'Vmax':str(Vmax),'beta':str(beta),'tail':str(tail),
 'payment_lower':str(lower),'payment_upper':str(upper),'C':str(C),'d':str(d),'gap_lower':str(gl),'gap_upper':str(gh),
 'simplified_gap_upper':'-3','informational_decimals':{'payment_lower':float(lower),'payment_upper':float(upper),'gap_lower':float(gl),'gap_upper':float(gh),'tail':float(tail)}}
Path('../evidence/fixed_witness_obstruction.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out['informational_decimals']))
