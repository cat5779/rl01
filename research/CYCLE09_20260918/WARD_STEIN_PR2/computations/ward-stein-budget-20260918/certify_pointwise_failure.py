"""Exact-rational counterexample to the pointwise budget B<=1.
Only the lower bound on B is certified; no claim about its expectation.
"""
import sympy as sp
from fractions import Fraction as F
from pathlib import Path
import json

if not __debug__:
    raise RuntimeError("Certificate checks require Python without -O or -OO.")


def hadamard(n):
 H=sp.ones(1)
 while H.rows<n:H=H.row_join(H).col_join(H.row_join(-H))
 return H

def frac(x):return F(int(sp.numer(x)),int(sp.denom(x)))
def floorq(x,bits=100):
 D=1<<bits;return F((x.numerator*D)//x.denominator,D)
def ceilq(x,bits=100):return -floorq(-x,bits)
def atanh_interval(x,terms=200):
 if x<0:
  a,b=atanh_interval(-x,terms);return -b,-a
 lo=floorq(x);hi=ceilq(x);p=lo;q=hi;L=F(0);U=F(0)
 for k in range(terms):
  L+=floorq(p/(2*k+1));U+=ceilq(q/(2*k+1))
  p=floorq(p*lo*lo);q=ceilq(q*hi*hi)
 # True omitted tail <= x^(2terms+1)/((2terms+1)(1-x^2)).
 U+=ceilq(q/F(2*terms+1)/(1-hi*hi))
 return L,U

def run():
 c=sp.Rational(19,20);r=c*c;m=16;n=32;U=hadamard(m)/4
 J=sp.zeros(n);J[:m,m:]=U;J[m:,:m]=U.T;assert J*J==sp.eye(n)
 s=[-1,1,-1,-1,-1,1,-1,-1,-1,1,1,-1,-1,1,1,-1,1,-1,1,-1,1,1,1,-1,-1,-1,1,1,1,1,1,1]
 K=(sp.eye(n)+c*J)/2;B=K[1:,1:]-sp.diag(*[sp.Rational(1-x,2) for x in s[1:]])
 G=B.inv(method='DM');b=K[1:,0];v=G*b;q=sp.Rational(1,2)-(b.T*v)[0]
 A0=atanh_interval(frac(2*q-1));low=F(0);high=F(0)
 for j in range(n-1):
  o=s[j+1]*G[j,j]-1;dq=sp.cancel(s[j+1]*v[j]**2/o)
  if dq==0:continue
  qj=q+dq;Aj=atanh_interval(frac(2*qj-1))
  a=Aj[0]-A0[1];bnd=Aj[1]-A0[0]
  d=frac(dq)
  if d<0:a,bnd=bnd/d,a/d
  else:a,bnd=a/d,bnd/d
  # B=(1-r)/4 * sum v_j^2 * [logit(qj)-logit(q)]/(qj-q)
  # logit(q)=2 atanh(2q-1).
  w=frac((1-r)*v[j]**2/2);low+=w*a;high+=w*bnd
 assert low>F(117,100),float(low)
 out={'status':'EXACT_RATIONAL_PASS','domain':'finite genuine half-rank projection DPP; pointwise only',
      'n':n,'c':'19/20','U':'Sylvester Hadamard(16)/4','word':s,
      'budget_lower':str(low),'budget_upper':str(high),'certified_B_gt':'117/100'}
 (Path(__file__).resolve().parents[1] / 'checks' / 'pointwise_failure_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
 print('B in',float(low),float(high),'EXACT: B>117/100>1')
if __name__=='__main__':run()