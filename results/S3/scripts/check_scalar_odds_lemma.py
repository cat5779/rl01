#!/usr/bin/env python3
"""Random arithmetic check of Lemma 5.1; diagnostic, not the proof."""
import math, random, json
from pathlib import Path
random.seed(20260917)
worst=1e99; record=None
for _ in range(200000):
    eps=random.uniform(1e-4,.499); c=1-2*eps; tau=eps*(1-eps)
    x=random.random(); y=random.random()
    dmax=min(x*y,(1-x)*(1-y))
    d=random.random()*dmax
    q=eps+c*x; r=eps+c*y; z=c*c*d
    A=(1-q)*(1-r)-z; B=(1-q)*r+z; C=q*(1-r)+z; D=q*r-z
    if min(A,B,C,D)<=0: continue
    lhs=math.log(B*C/(A*D))
    rhs=z/(2*tau)*(1/(q*(1-q))+1/(r*(1-r)))
    gap=rhs-lhs
    if gap<worst: worst=gap;record=[eps,x,y,d,lhs,rhs]
out={'trials':200000,'minimum_rhs_minus_lhs':worst,'record':record,
     'evidentiary_limit':'Diagnostic only; the proof is the interpolation argument in proof.md.'}
root=Path(__file__).resolve().parents[1]
(root/'evidence/scalar_odds_random_check.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
