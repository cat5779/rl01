#!/usr/bin/env python3
"""High-precision validation of the full 64-atom center Hessian decomposition.
Diagnostic cross-check; the obstruction certificate itself is exact rational.
"""
from pathlib import Path
import json, mpmath as mp, sympy as sp
mp.mp.dps=80
R=sp.Rational; I=sp.eye
T=sp.Matrix([[R(7,27),-R(1,14),R(10,49)],
             [R(13,48),-R(3,22),R(13,50)],
             [R(5,36),-R(3,32),R(3,41)]])
D=(I(3)+T.T*T).inv(); V=T.col_join(I(3)); Ps=sp.simplify(V*D*V.T)
P=mp.matrix([[mp.mpf(str(sp.N(Ps[i,j],90))) for j in range(6)] for i in range(6)])
c=mp.mpf(99)/100; a=(1-c)/2
H2=mp.mpf('0'); dec=mp.mpf('0'); total=mp.mpf('0'); minp=mp.inf
for mask in range(64):
    y=[(mask>>(5-i))&1 for i in range(6)]; s=[2*v-1 for v in y]
    M=a*mp.eye(6)+c*P-mp.diag([1-v for v in y])
    det=mp.det(M); p=abs(det); minp=min(minp,p); total+=p
    Inv=M**-1
    tr=sum(Inv[i,i] for i in range(6)); tr2=sum(Inv[i,j]*Inv[j,i] for i in range(6) for j in range(6))
    p1=p*tr; p2=p*(tr*tr-tr2)
    H2 += -p2*mp.log(p)-p1*p1/p
    rr=[s[i]*Inv[i,i] for i in range(6)]; g=[rr[i]-1 for i in range(6)]
    f=sum(rr[i]**2/g[i] for i in range(6)); hs=mp.mpf('0')
    for i in range(6):
      for j in range(i):
        eps=s[i]*s[j]; w=Inv[i,j]**2; x=w/(g[i]*g[j]); N=rr[i]*rr[j]-eps*w
        if eps>0: odds=1-x; same=(1+g[i]*g[j]-w)/N
        else: odds=1/(1+x); same=(g[i]+g[j])/N
        hs += -mp.log(odds)-(1-odds)-same*(1-odds)**2/odds
    dec += p*(-f+2*hs)
out={'normalization':mp.nstr(total,60),'minimum_atom':mp.nstr(minp,40),
     'direct_H2':mp.nstr(H2,60),'decomposition_H2':mp.nstr(dec,60),
     'absolute_difference':mp.nstr(abs(H2-dec),20),
     'evidentiary_limit':'High-precision cross-check. Exact rational certification of the bad atom is separate.'}
root=Path(__file__).resolve().parents[1]
(root/'evidence/center_decomposition_validation.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
assert abs(total-1)<mp.mpf('1e-60')
assert abs(H2-dec)<mp.mpf('1e-55')
