"""Small exact algebra checks for interacting exterior sites.

Generic 3-site identities, not a replacement of the assigned Fejer model.
The actual R=1 model is checked in small_check_r1.py.
No scans, fitting, large enumeration, or hash operations are performed.
"""
from itertools import product
from pathlib import Path
import json
import sympy as sp

h, k, b1, b2, u = sp.symbols('h k b1 b2 u', real=True)
KC = sp.Matrix([[h,k],[k,h]])
b = sp.Matrix([b1,b2])
K = sp.Matrix([[h,b1,b2],[b1,h,k],[b2,k,h]])
words = list(product((0,1),repeat=2))

def flip(z,i):
    return tuple(1-x if j==i else x for j,x in enumerate(z))

def zero(x):
    return sp.cancel(x) == 0

Gs, ws, qs = {}, {}, {}
for z in words:
    D = sp.diag(*(1-x for x in z))
    B = KC-D
    Gs[z] = B.inv()
    ws[z] = sp.expand((-1)**(2-sum(z))*B.det())
    qs[z] = sp.cancel(h-(b.T*Gs[z]*b)[0])
assert sp.expand(sum(ws.values())-1) == 0

for z in words:
    G = Gs[z]
    D = sp.diag(*(1-x for x in z))
    S = sp.diag(*(2*x-1 for x in z))
    v = G*b
    x = sp.Matrix([1,-v[0],-v[1]])
    assert zero((x.T*K*(sp.eye(3)-K)*x)[0]-qs[z]*(1-qs[z]))
    weighted_rows = G*KC*(sp.eye(2)-KC)*G-(S*G+G*S)/2+sp.eye(2)
    assert all(zero(entry) for entry in weighted_rows)
    TG = sp.zeros(2)
    Tq = sp.Integer(0)
    for i in range(2):
        zi = flip(z,i)
        sig = 2*z[i]-1
        odds = sp.cancel(ws[zi]/ws[z])
        assert zero(odds-(sig*G[i,i]-1))
        rate = -u*sig*odds
        e = sp.eye(2)[:,i]
        flip_formula = G-sig/odds*G*e*e.T*G
        assert all(zero(entry) for entry in Gs[zi]-flip_formula)
        TG += rate*(Gs[zi]-G)
        Tq += rate*(qs[zi]-qs[z])
        birth = u*(1+odds) if z[i] == 0 else sp.Integer(0)
        reversible = u if z[i] == 0 else u*odds
        assert zero(birth-reversible-rate)
        rev_at_flip = u if zi[i] == 0 else u*ws[z]/ws[zi]
        assert zero(ws[z]*reversible-ws[zi]*rev_at_flip)
    assert all(zero(entry) for entry in u*G.diff(h)+TG)
    assert zero(u*sp.diff(qs[z],h)+Tq-u)
    for i in range(2):
        sig = 2*z[i]-1
        odds_i = sp.cancel(ws[flip(z,i)]/ws[z])
        rate_i = -u*sig*odds_i
        T_rate_i = sp.Integer(0)
        T_odds_i = sp.Integer(0)
        for j in range(2):
            zj = flip(z,j)
            rate_j = -u*(2*z[j]-1)*ws[zj]/ws[z]
            odds_i_at_j = sp.cancel(ws[flip(zj,i)]/ws[zj])
            rate_i_at_j = -u*(2*zj[i]-1)*odds_i_at_j
            T_rate_i += rate_j*(rate_i_at_j-rate_i)
            T_odds_i += rate_j*(odds_i_at_j-odds_i)
        assert zero(u*sp.diff(rate_i,h)+T_rate_i-2*u*u*odds_i)
        assert zero(u*sp.diff(odds_i,h)+T_odds_i+2*u*G[i,i])

out = {
    'status':'PASS',
    'scope':'generic 3-site kernel; 2 interacting exterior sites; symbolic identities',
    'checks':[
        'external word normalization',
        'exact Schur energy identity',
        'odds-weighted row energy identity',
        'rank-one flip update including exterior interaction',
        'matrix material drift D G = 0',
        'posterior material drift D q = u',
        'positive birth minus reversible Poisson generator equals signed transport',
        'detailed balance for the reversible generator',
        'material rate drift D r_i = 2*u^2*o_i',
        'material odds drift D o_i = -2*u*G_ii',
    ],
    'not_a_claim':'This auxiliary check does not replace the actual Fejer R=1 check or prove a sign.'
}
print(json.dumps(out,ensure_ascii=False,indent=2))
Path(__file__).with_name('check_resolvent_algebra_result.json').write_text(
    json.dumps(out,ensure_ascii=False,indent=2)+'\n')
