"""Exact R=1 check for the genuine three-site Fejer DPP.

No fitting, floating-point sign inference, hash checks, or large enumeration.
The symbolic coupling k is specialized to u*c/(2*pi) in the report.
"""
from itertools import product
import json
from pathlib import Path
import sympy as sp

u = sp.symbols('u', positive=True)
k = sp.symbols('k', positive=True)
delta = sp.symbols('delta', real=True)
h = sp.Rational(1, 2) + u * delta
K = sp.Matrix([[h,k,0],[k,h,k],[0,k,h]])
words = list(product((0,1), repeat=2))

def atom(bits):
    D = sp.diag(*(1-b for b in bits))
    return sp.expand((-1)**(len(bits)-sum(bits)) * (K-D).det())

w, q = {}, {}
for z in words:
    p0 = atom((z[0],0,z[1]))
    p1 = atom((z[0],1,z[1]))
    w[z] = sp.factor(p0+p1)
    q[z] = sp.cancel(p1/w[z])
    expected_w = h**sum(z)*(1-h)**(2-sum(z))
    assert sp.cancel(w[z]-expected_w) == 0
    expected_q = h-k*k*sum(1/(h-(1-b)) for b in z)
    assert sp.cancel(q[z]-expected_q) == 0
assert sp.expand(sum(w.values())-1) == 0

x = sp.symbols('x', positive=True)
phi_expr = (x-sp.Rational(1,2))*sp.log(x/(1-x))
phi1_expr = sp.diff(phi_expr,x)
phi2_expr = sp.diff(phi_expr,x,2)
assert sp.simplify(phi2_expr-1/(2*x*x*(1-x)**2)) == 0

def phi(x_): return phi_expr.subs(x,x_)
def phi1(x_): return phi1_expr.subs(x,x_)
def phi2(x_): return phi2_expr.subs(x,x_)
def flip(z,i): return tuple(1-b if j==i else b for j,b in enumerate(z))
def zero(expr): return sp.factor(sp.cancel(expr.subs(delta,0)))

q0 = {z:zero(q[z]) for z in words}
qp = {z:zero(sp.diff(q[z],delta)) for z in words}
qpp = {z:zero(sp.diff(q[z],delta,2)) for z in words}
w0 = {z:zero(w[z]) for z in words}
wp = {z:zero(sp.diff(w[z],delta)) for z in words}
wpp = {z:zero(sp.diff(w[z],delta,2)) for z in words}
r, rp = {}, {}

for z in words:
    sig = [2*b-1 for b in z]
    A = sp.diag(*(1/(h-(1-b)) for b in z))
    bvec = sp.Matrix([k,k])
    v = A*bvec
    assert sp.cancel(sp.diff(q[z],delta)-u*(1+(v.T*v)[0])) == 0
    for i in range(2):
        zi = flip(z,i)
        rate = -u*sig[i]*w[zi]/w[z]
        assert sp.cancel(rate-u*(sig[i]-A[i,i])) == 0
        r[z,i] = zero(rate)
        rp[z,i] = zero(sp.diff(rate,delta))
        assert rp[z,i] == 4*u*u
    assert sp.simplify(qp[z]+sum(r[z,i]*(q0[flip(z,i)]-q0[z]) for i in range(2))-u) == 0

for z in words:
    incoming = sum(w0[flip(z,i)]*r[flip(z,i),i]-w0[z]*r[z,i] for i in range(2))
    assert sp.simplify(incoming-wp[z]) == 0

# Compare coefficients of independent formal values at all labelled states.
f = {z:sp.Symbol('f_'+''.join(map(str,z))) for z in words}
f1 = {z:sp.Symbol('fp_'+''.join(map(str,z))) for z in words}
f2 = {z:sp.Symbol('fpp_'+''.join(map(str,z))) for z in words}
B, Bp, B_phi1 = {}, {}, {}
for z in words:
    B[z] = 0
    Bp[z] = 0
    B_phi1[z] = 0
    for i in range(2):
        zi = flip(z,i)
        d = q0[zi]-q0[z]
        defect = f[zi]-f[z]-f1[z]*d
        defect_prime = (f1[zi]-f1[z])*qp[zi]-f2[z]*d*qp[z]
        B[z] += r[z,i]*defect
        Bp[z] += rp[z,i]*defect+r[z,i]*defect_prime
        B_phi1[z] += r[z,i]*(f1[zi]-f1[z]-f2[z]*d)

original = sum(wpp[z]*f[z]+2*wp[z]*f1[z]*qp[z]
               +w0[z]*(f2[z]*qp[z]**2+f1[z]*qpp[z]) for z in words)
compensated = sum(w0[z]*(u*u*f2[z]+u*B_phi1[z]+Bp[z]
                +sum(r[z,j]*(B[flip(z,j)]-B[z]) for j in range(2))) for z in words)
assert sp.expand(original-compensated) == 0

def L(values):
    return {z:sp.expand(-u*sum((2*z[i]-1)*(values[flip(z,i)]-values[z])
                         for i in range(2))) for z in words}
Ftest = {z:sp.Symbol('test_'+''.join(map(str,z))) for z in words}
LF = L(Ftest)
L2F = L(LF)
Hmat = {z:u*f1[z]+B[z] for z in words}
Gmat = {z:u*u*f2[z]+u*B_phi1[z]+Bp[z]
        +sum(r[z,j]*(B[flip(z,j)]-B[z]) for j in range(2)) for z in words}
weighted_original = sum(Ftest[z]*(wpp[z]*f[z]+2*wp[z]*f1[z]*qp[z]
                          +w0[z]*(f2[z]*qp[z]**2+f1[z]*qpp[z])) for z in words)
weighted_transport = sum(w0[z]*(Ftest[z]*Gmat[z]+2*Hmat[z]*LF[z]
                          +f[z]*L2F[z]) for z in words)
assert sp.expand(weighted_original-weighted_transport) == 0
assert all(value == 0 for value in L({z:sp.Integer(1) for z in words}).values())

t = sp.symbols('t', positive=True)
F, P, D = sp.symbols('F P D', real=True)
formal_subs = {}
for z in words:
    S = sum(2*b-1 for b in z)
    formal_subs[f[z]] = F if S else 0
    formal_subs[f1[z]] = -sp.Rational(S,2)*P
    formal_subs[f2[z]] = D if S else 8
Ipp_formal = sp.expand(original.subs(formal_subs).subs(k*k,t/4)/u**2)
expected_formal = 4*F-4*(1+t)*P+(1+2*t)**2*(D+8)/2
assert sp.expand(Ipp_formal-expected_formal) == 0
B_formal = {z:sp.expand(B[z].subs(formal_subs).subs(k*k,t/4)) for z in words}
TB_formal = {z:sp.expand(sum(r[z,j]*(B_formal[flip(z,j)]-B_formal[z])
                          for j in range(2))) for z in words}
assert all(sp.expand(value+4*u*u*(t*P-F)) == 0 for value in TB_formal.values())

qplus = sp.Rational(1,2)+t
expected = 4*phi(qplus)-4*(1+t)*phi1(qplus)+(1+2*t)**2*(phi2(qplus)+8)/2
assert sp.simplify(t*phi1(qplus)-phi(qplus)-4*t*t/(1-4*t*t)) == 0
x2 = 2*t
rational_log = 4*(1/(1-x2)**2+(1+x2)**2
                    -(2*x2+x2*x2)/(1-x2*x2)
                    -sp.log((1+x2)/(1-x2)))
assert sp.simplify(expected-rational_log) == 0
series = sp.series(expected,t,0,4)
assert sp.expand(series.removeO()-(8+48*t*t+sp.Rational(128,3)*t**3)) == 0

out = {
    'status':'PASS',
    'scope':'R=1, exact 8 joint atoms / 4 external words, symbolic parameters',
    'checks':['normalization and exact Schur posterior','all u factors in jets',
              'signed flux adjoint identity','pointwise compensated posterior drift',
              'second-variation equality for arbitrary formal function jets',
              'weighted boundary-flux equality for arbitrary fixed test values',
              'exact negative signed-flux component in the legal R=1 model',
              'explicit R=1 production curvature formula',
              'exact rational negative budget and positive-total generating formula',
              'small-coupling Taylor coefficients'],
    'r1_curvature_div_u2_series':str(series),
    'negative_flux_component':'T B_phi = -16*u^2*t^2/(1-4*t^2) < 0 pointwise',
    'not_performed':['large-R enumeration','parameter sweeps','asymptotic fitting','hash checks'],
}
print(json.dumps(out,ensure_ascii=False,indent=2))
Path(__file__).with_name('small_check_r1_result.json').write_text(
    json.dumps(out,ensure_ascii=False,indent=2)+'\n')
