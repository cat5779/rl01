#!/usr/bin/env python3
"""Exact rational-log enclosure proving the full Hessian of the obstruction example is negative."""
from fractions import Fraction
import sys,json
sys.set_int_max_str_digits(0)
from pathlib import Path
import sympy as sp
R=sp.Rational;I=sp.eye
T=sp.Matrix([[R(7,27),-R(1,14),R(10,49)],
             [R(13,48),-R(3,22),R(13,50)],
             [R(5,36),-R(3,32),R(3,41)]])
D=(I(3)+T.T*T).inv();V=T.col_join(I(3));P=sp.simplify(V*D*V.T)
c=R(99,100);a=R(1,200)

def log2_interval(N=18):
 z=Fraction(1,3);lo=sum(Fraction(2,2*j+1)*z**(2*j+1) for j in range(N+1));
 return lo,lo+Fraction(2,2*N+3)*z**(2*N+3)/(1-z*z)
def log_gt1(x,N=18):
 k=x.numerator.bit_length()-x.denominator.bit_length()
 while x<Fraction(2)**k:k-=1
 while x>=Fraction(2)**(k+1):k+=1
 m=x/Fraction(2)**k;z=(m-1)/(m+1)
 lo=sum(Fraction(2,2*j+1)*z**(2*j+1) for j in range(N+1))
 hi=lo+Fraction(2,2*N+3)*z**(2*N+3)/(1-z*z)
 l2,u2=log2_interval(N)
 return k*l2+lo,k*u2+hi

lo=Fraction(0);hi=Fraction(0);norm=R(0);fish=R(0)
for mask in range(64):
 y=[(mask>>(5-i))&1 for i in range(6)]
 M=a*I(6)+c*P-sp.diag(*[1-v for v in y]);det=sp.cancel(M.det());p=abs(det);norm+=p
 Inv=M.inv();tr=sp.trace(Inv);tr2=sp.trace(Inv*Inv)
 p1=sp.cancel(p*tr);p2=sp.cancel(p*(tr**2-tr2));fish+=sp.cancel(p1**2/p)
 Llo,Lhi=log_gt1(Fraction(int(p.q),int(p.p)),22) # -log p
 coeff=Fraction(int(p2.p),int(p2.q))
 # -p2 log p = p2*(-log p)
 if coeff>=0: lo+=coeff*Llo;hi+=coeff*Lhi
 else: lo+=coeff*Lhi;hi+=coeff*Llo
fishF=Fraction(int(fish.p),int(fish.q));lo-=fishF;hi-=fishF
assert norm==1
assert hi<Fraction(-1000)
out={'statement':'The complete 64-atom entropy Hessian of the rational projection example is strictly below -1000.',
     'H2_lower':str(lo),'H2_upper':str(hi),
     'H2_decimal_lower':format(float(lo),'.12f'),'H2_decimal_upper':format(float(hi),'.12f'),
     'normalization':'1','series_terms':23}
root=Path(__file__).resolve().parents[1];(root/'evidence/global_negative_hessian.json').write_text(json.dumps(out,indent=2))
print('PASS_GLOBAL_NEGATIVE')
print(out['H2_decimal_lower'],out['H2_decimal_upper'])
