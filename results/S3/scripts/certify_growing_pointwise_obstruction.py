#!/usr/bin/env python3
"""Exact certificate for a growing-family failure of one atomwise total Fisher allocation.

All matrix and nonlogarithmic calculations are exact sympy rationals.  The only
transcendental is log of one positive rational; it is enclosed by a rational
atanh series after exact power-of-two range reduction.
"""
from __future__ import annotations
from fractions import Fraction
import sys
sys.set_int_max_str_digits(0)
from pathlib import Path
import json
import sympy as sp

R=sp.Rational
I=sp.eye

T=sp.Matrix([
 [R(7,27), R(-1,14), R(10,49)],
 [R(13,48), R(-3,22), R(13,50)],
 [R(5,36), R(-3,32), R(3,41)],
])
D=(I(3)+T.T*T).inv()
V=T.col_join(I(3))
P=sp.simplify(V*D*V.T)
assert sp.simplify(P*P-P)==sp.zeros(6)
assert P.rank()==3 and P.trace()==3

c=R(99,100); a=(1-c)/2; tau=a*(1-a)
y=[1,1,1,0,0,0]; s=[R(2*v-1) for v in y]
M=a*I(6)+c*P-sp.diag(*[1-v for v in y])
assert M.det()!=0
Inv=sp.simplify(M.inv())
r=[sp.cancel(s[i]*Inv[i,i]) for i in range(6)]
g=[sp.cancel(v-1) for v in r]
assert all(v>0 for v in g)
f=sp.cancel(sum(r[i]**2/g[i] for i in range(6)))

prod_odds=R(1); rational_rest=R(0); pair_rows=[]
for i in range(6):
    for j in range(i):
        eps=s[i]*s[j]
        w=sp.cancel(Inv[i,j]**2)
        x=sp.cancel(w/(g[i]*g[j]))
        N=sp.cancel(r[i]*r[j]-eps*w)
        if eps>0:
            odds=sp.cancel(1-x)
            same=sp.cancel((1+g[i]*g[j]-w)/N)
        else:
            odds=sp.cancel(1/(1+x))
            same=sp.cancel((g[i]+g[j])/N)
        assert odds>0
        rest=sp.cancel(-(1-odds)-same*(1-odds)**2/odds)
        prod_odds=sp.cancel(prod_odds*odds)
        rational_rest=sp.cancel(rational_rest+2*rest)
        pair_rows.append({
            'i':i+1,'j':j+1,'same_sign':bool(eps>0),
            'odds':str(odds),'rational_rest':str(rest)
        })
qrat=sp.cancel(rational_rest-f)
# pointwise defect Delta = -2 log(prod_odds) + qrat
assert 0<prod_odds<1

# Exact rational log enclosure. For x>1 choose k with m=x/2^k in [1,2),
# then log x=k log2+2 sum z^(2j+1)/(2j+1), z=(m-1)/(m+1).
def atanh_log_unit_interval(m: Fraction, N: int):
    assert Fraction(1)<=m<Fraction(2)
    z=(m-1)/(m+1)
    lo=Fraction(0)
    for j in range(N+1):
        lo += Fraction(2,2*j+1)*z**(2*j+1)
    rem=Fraction(2,2*N+3)*z**(2*N+3)/(1-z*z)
    return lo,lo+rem

def log2_interval(N:int):
    z=Fraction(1,3);lo=Fraction(0)
    for j in range(N+1):
        lo += Fraction(2,2*j+1)*z**(2*j+1)
    rem=Fraction(2,2*N+3)*z**(2*N+3)/(1-z*z)
    return lo,lo+rem

def log_rational_gt1(x: Fraction, N=24):
    assert x>1
    k=x.numerator.bit_length()-x.denominator.bit_length()
    # repair to floor(log_2 x)
    while x < Fraction(2)**k: k-=1
    while x >= Fraction(2)**(k+1): k+=1
    m=x/Fraction(2)**k
    mlo,mhi=atanh_log_unit_interval(m,N)
    l2lo,l2hi=log2_interval(N)
    return k*l2lo+mlo,k*l2hi+mhi,k,m

x=Fraction(int(prod_odds.q),int(prod_odds.p))
llo,lhi,k,m=log_rational_gt1(x,30)
qF=Fraction(int(qrat.p),int(qrat.q))
dlo=2*llo+qF; dhi=2*lhi+qF
assert dlo>Fraction(6,5), (float(dlo),float(dhi))

atom=abs(sp.cancel(M.det()))
assert atom>0

out={
 'statement':'For the exact rank-3 projection P and y=111000 at c=99/100, a=1/200, the atomwise total pair debt minus the once-only diagonal Fisher payment exceeds 6/5. Direct sums of k copies have defect exceeding 6k/5.',
 'scope':'This disproves only the specified atomwise aggregate payment. It is not a counterexample to expected projection entropy concavity, the conditioned leaf-volume sign, or sine entropy-rate concavity.',
 'parameters':{'a':str(a),'c':str(c),'tau':str(tau),'y':'111000'},
 'graph_matrix_T':[[str(v) for v in row] for row in T.tolist()],
 'projection_P':[[str(v) for v in row] for row in P.tolist()],
 'checks':{'P_squared_equals_P':True,'rank':3,'trace':'3','atom_probability':str(atom)},
 'exact_reduction':{
   'prod_odds':str(prod_odds),
   'rational_term_q':str(qrat),
   'diagonal_payment_f':str(f),
   'defect_formula':'Delta=-2*log(prod_odds)+qrat'
 },
 'log_range_reduction':{'power_of_two_k':k,'mantissa':str(m),'series_terms':31},
 'certified_intervals':{
   'log_inverse_prod_lower':str(llo),'log_inverse_prod_upper':str(lhi),
   'defect_lower':str(dlo),'defect_upper':str(dhi),
   'defect_decimal_lower':format(float(dlo),'.12f'),
   'defect_decimal_upper':format(float(dhi),'.12f'),
   'claimed_rational_margin':'6/5'
 },
 'direct_sum':{
   'proof':'For P^(k)=diag(P,...,P) and y^(k)=(111000)^k, the atom inverse is block diagonal. Cross-copy inverse entries vanish, while every r_i,g_i, within-copy odds, pair debt, and f_i is copied. Hence Delta_k=k Delta>6k/5.',
   'all_dimensions':'n=6k, rank=3k, k>=1'
 },
 'pair_rows':pair_rows,
}
root=Path(__file__).resolve().parents[1] / 'evidence'
root.mkdir(parents=True, exist_ok=True)
(root/'exact_growing_pointwise_obstruction.json').write_text(json.dumps(out,indent=2))
print('PASS')
print('P exact projection rank',P.rank())
print('atom probability ~',sp.N(atom,18))
print('defect interval',float(dlo),float(dhi))
print('margin > 6/5:',dlo>Fraction(6,5))
