"""Reuse the same four genuine R=1 exterior states for two refinements.

No larger model, parameter scan, floating-point fit, or sign inference.
"""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
import sympy as sp

with redirect_stdout(StringIO()):
    import small_check_r1 as ck

Bi = {}
for z in ck.words:
    for i in range(2):
        zi = ck.flip(z, i)
        di = ck.q0[zi]-ck.q0[z]
        Bi[z, i] = ck.f[zi]-ck.f[z]-ck.f1[z]*di

for z in ck.words:
    rhs = ck.u**2*ck.f2[z]+2*ck.u*ck.B_phi1[z]
    rhs += 2*ck.u**2*sum(Bi[z, i] for i in range(2))
    for i in range(2):
        zi = ck.flip(z, i)
        di = ck.q0[zi]-ck.q0[z]
        Ci = sum((ck.r[z,j]-ck.r[zi,j])
                 *(ck.q0[ck.flip(zi,j)]-ck.q0[zi]) for j in range(2))
        rhs += ck.r[z,i]*(ck.f1[zi]-ck.f1[z])*Ci
        for j in range(2):
            zj = ck.flip(z,j)
            dij = ck.q0[ck.flip(zi,j)]-ck.q0[zi]
            dj = ck.q0[zj]-ck.q0[z]
            Xi = (Bi[zj,i]-Bi[z,i]
                  -(ck.f1[zi]-ck.f1[z])*dij+ck.f2[z]*di*dj)
            rhs += ck.r[z,i]*ck.r[z,j]*Xi
            rhs += ck.r[z,j]*(ck.r[zj,i]-ck.r[z,i])*(Bi[zj,i]-Bi[z,i])
    assert sp.expand(rhs-ck.Gmat[z]) == 0

coefficients = {}
for z in ck.words:
    formal = sp.expand((ck.Gmat[z]/ck.u**2).subs(ck.formal_subs).subs(ck.k**2,ck.t/4))
    actual = formal.subs({ck.F:ck.phi(ck.qplus), ck.P:ck.phi1(ck.qplus),
                         ck.D:ck.phi2(ck.qplus)})
    expansion = sp.series(actual,ck.t,0,3)
    coefficient = 16*((sum(2*bit-1 for bit in z))**2+1)
    assert sp.expand(expansion.removeO()-8-coefficient*ck.t**2) == 0
    coefficients[''.join(map(str,z))] = coefficient

result = {
    'status':'PASS',
    'scope':'same four genuine R=1 exterior words, no additional enumeration',
    'checks':['S6 second Bregman decomposition, exact formal function jets',
              'S10 pointwise coefficient, exact symbolic Taylor expansion'],
    'normalized_kernel':'Gcal/u^2 = 8 + coefficient*t^2 + O(t^3)',
    't':'c^2*u^2/pi^2',
    'coefficients':coefficients,
    'limitation':'The uniform complex bound W9 is proved analytically, not by this check.'
}
print(json.dumps(result,ensure_ascii=False,indent=2))
Path(__file__).with_name('check_r1_refinement_result.json').write_text(
    json.dumps(result,ensure_ascii=False,indent=2)+'\n')
