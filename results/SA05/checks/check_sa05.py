#!/usr/bin/env python3
"""SA05 exact, deliberately tiny checks.

Run: python checks/check_sa05.py --output checks/results.json
Dependency: sympy. No network, hashing, scans, or n=8 configuration enumeration.
Only n=4 uses full configurations (16 output atoms, 6 input atoms).
The n=8 checks use a single analytic witness, degree-4 polynomials, and
the five-value overlap distribution, not the 70-state layer.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Any

import sympy as s


def zero(expr: s.Expr, label: str) -> None:
    if s.cancel(s.expand(expr)) != 0:
        raise AssertionError(f"Exact identity failed: {label}")


def check_n4() -> dict[str, Any]:
    a, t = s.symbols("a t")
    c = s.Rational(19, 20)
    astar = s.Rational(1, 40)
    n, k = 4, 2
    sites = range(n)
    inputs = [frozenset(v) for v in itertools.combinations(sites, k)]
    atoms = [frozenset(v) for r in range(n+1)
             for v in itertools.combinations(sites, r)]
    nu = {A: (s.Rational(1, 4) if abs(max(A)-min(A)) == 2
              else s.Rational(1, 8)) for A in inputs}
    zero(sum(nu.values())-1, "input normalization")
    pgf = s.Poly(s.expand((1-a-c+(a+c)*t)**k*(1-a+a*t)**k), t)
    pi = {l: pgf.nth(l) for l in range(n+1)}
    p: dict[frozenset[int], s.Expr] = {}
    for S in atoms:
        l = len(S)
        p[S] = s.expand(sum(
            nu[A]*(a+c)**len(A&S)*(1-a-c)**(k-len(A&S))
            *a**(l-len(A&S))*(1-a)**(k-l+len(A&S))
            for A in inputs))
    zero(sum(p.values())-1, "full atoms sum to one")
    zero(sum(s.diff(v, a) for v in p.values()), "full first jets sum to zero")
    zero(sum(s.diff(v, a, 2) for v in p.values()), "full second jets sum to zero")

    z = (a+c)*(1-a)/(a*(1-a-c))
    theta = s.cancel((z-1)**2/(1+4*z+z*z))
    q: dict[frozenset[int], s.Expr] = {}
    qhat: dict[frozenset[int], s.Expr] = {}
    phat: dict[frozenset[int], s.Expr] = {}
    for S in atoms:
        l = len(S)
        q[S] = s.cancel(p[S]/pi[l])
        if l == 2:
            qhat[S] = s.cancel((1+theta*(6*nu[S]-1))/6)
        else:
            qhat[S] = s.Rational(1, int(s.binomial(n, l)))
        phat[S] = s.cancel(pi[l]*qhat[S])
        zero(p[S]-phat[S], f"true/corrected full atom {sorted(S)}")
        # Compute true conditional jets via p=pi*q, not by misnormalizing p.
        q1 = s.cancel((s.diff(p[S], a)-s.diff(pi[l], a)*q[S])/pi[l])
        q2 = s.cancel((s.diff(p[S], a, 2)-s.diff(pi[l], a, 2)*q[S]
                       -2*s.diff(pi[l], a)*q1)/pi[l])
        zero(q1-s.diff(qhat[S], a), f"conditional first jet {sorted(S)}")
        zero(q2-s.diff(qhat[S], a, 2), f"conditional second jet {sorted(S)}")

    for l in range(n+1):
        layer = [S for S in atoms if len(S) == l]
        zero(sum(p[S] for S in layer)-pi[l], f"atom layer mass {l}")
        for label, law in [("true", q), ("corrected", qhat)]:
            zero(sum(law[S] for S in layer)-1, f"{label} layer norm {l}")
            for order in (1, 2):
                zero(sum(s.diff(law[S], a, order) for S in layer),
                     f"{label} layer jet sum {l}/{order}")

    # Independently assemble the complete-atom and weighted-layer Hessian defect.
    atom_defect = s.S.Zero
    for S in atoms:
        p0, p1, p2 = [s.diff(p[S], a, r).subs(a, astar) for r in range(3)]
        h0, h1, h2 = [s.diff(phat[S], a, r).subs(a, astar) for r in range(3)]
        atom_defect += p2*s.log(p0)+p1*p1/p0-h2*s.log(h0)-h1*h1/h0

    layer_defect = s.S.Zero
    for l in range(n+1):
        eps0 = eps1 = eps2 = s.S.Zero
        for S in (S for S in atoms if len(S) == l):
            u = s.Rational(1, int(s.binomial(n, l)))
            q0,q1,q2 = [s.diff(q[S],a,r).subs(a,astar) for r in range(3)]
            h0,h1,h2 = [s.diff(qhat[S],a,r).subs(a,astar) for r in range(3)]
            eps0 += q0*s.log(q0/u)-h0*s.log(h0/u)
            eps1 += q1*s.log(q0/u)-h1*s.log(h0/u)
            eps2 += q2*s.log(q0/u)+q1*q1/q0-h2*s.log(h0/u)-h1*h1/h0
        layer_defect += (s.diff(pi[l],a,2).subs(a,astar)*eps0
                         +2*s.diff(pi[l],a).subs(a,astar)*eps1
                         +pi[l].subs(a,astar)*eps2)
    zero(atom_defect-layer_defect, "complete-atom vs layer defect")
    zero(layer_defect, "n=4 E''=0")
    return {"input_atoms": 6, "output_atoms": 16,
            "all_atom_and_layer_normalizations": "EXACT_PASS",
            "all_conditional_jets": "EXACT_PASS",
            "true_equals_corrected_symbolically_in_a": True,
            "complete_atom_E_second_at_midpoint": str(atom_defect),
            "weighted_layer_E_second_at_midpoint": str(layer_defect)}


def check_algebra() -> dict[str, Any]:
    x, t = s.symbols("xi t")
    Q4 = 1+20*x+90*x*x+140*x**3+70*x**4
    Q2 = 1+6*x+6*x*x
    A = x*(1+x)
    for r, Q in [(0,s.S.One),(2,Q2),(4,Q4)]:
        zero(A*s.diff(Q,x,2)+(1+2*x)*s.diff(Q,x)-r*(r+1)*Q,
             f"Jacobi equation n=8 r={r}")
    B = 1+2*x+2*A*s.diff(Q4,x)/Q4
    for j, theta in [(2,Q2/Q4),(4,1/Q4)]:
        eig = j*(9-j)
        zero(A*s.diff(theta,x,2)+B*s.diff(theta,x)+eig*theta,
             f"true multiplier ODE j={j}")
    gamma2 = s.Rational(7,8)
    tau1 = s.cancel((s.diff(Q4,x)/Q4-s.diff(Q2,x)/Q2)/gamma2)
    zero(A*s.diff(tau1,x)+B*tau1-A*gamma2*tau1*tau1-16,
         "clock Riccati identity")

    poly = s.Poly(s.expand((t+6)**10-t**4*(t*t+20*t+70)**3),t)
    expected = [210,9520,173460,1665552,9454760,33592320,
                75582720,100776960,60466176]
    assert poly.all_coeffs() == expected
    assert all(v > 0 for v in poly.all_coeffs())
    pair_factor = s.Rational(3,14)-2*s.Rational(1,14)+s.Rational(1,70)
    zero(pair_factor-s.Rational(3,35), "pair-projection coefficient")
    r0_even = s.Rational(70,16)
    v2_even = s.Rational(35,3)*6*s.Rational(1,28)
    v4_even = r0_even-1-v2_even
    zero(v4_even-s.Rational(7,8), "single n=8 degree-4 witness")

    # Five-value overlap calculation: exact identities only, no layer enumeration.
    xs = s.Rational(1,1520)
    zs = 1+1/xs
    weights = [s.binomial(4,j)**2*zs**j for j in range(5)]
    Z = sum(weights)
    weights = [v/Z for v in weights]
    mu = sum(weights[j]*j for j in range(5))
    moments = {r: sum(weights[j]*(j-mu)**r for j in range(5))
               for r in (2,3,4)}
    v,m3,m4 = moments[2],moments[3],moments[4]
    clock = tau1.subs(x,xs)
    beta = 2*mu-8-8*xs
    b = beta+16/clock
    b_mom = -(m4-v*v+(2*mu-4)*m3)/(m3+(2*mu-4)*v)
    zero(b-b_mom, "degree-two covariance cancellation")
    kappa = clock/(xs*(1+xs)*16)
    W = [-kappa*((j-mu)**2-v+b*(j-mu)) for j in range(5)]
    zero(sum(weights[j]*W[j] for j in range(5)), "overlap source norm")
    zero(sum(weights[j]*W[j]*((j-2)**2-s.Rational(4,7))
             for j in range(5)), "overlap source annihilates degree two")
    ew2 = sum(weights[j]*W[j]**2 for j in range(5))
    zero(ew2-kappa*kappa*(m4-v*v+2*b*m3+b*b*v), "source variance formula")
    assert abs(m3) <= v
    assert m4 <= 3*v*v+v
    assert v <= s.Rational(4,40)
    assert abs(b) <= s.Rational(13,7)
    assert 16/(7*(1+xs)) <= clock <= 16/(7*xs)

    c = s.Rational(19,20)
    As = xs*(1+xs)
    KW = (s.Rational(4,7))**2*(2*s.Rational(1,40)**2
                 +s.Rational(20,7)**2/s.Integer(160))/(As**2*xs**2)
    Csrc = s.factor(zs*(1+xs)/c*KW)
    zero(Csrc-s.Rational(349998584954880000,2401), "uniform source constant")
    assert ew2 <= KW
    return {"n8_configuration_enumeration": False,
            "n8_degree_four_witness": str(v4_even),
            "positive_polynomial_coefficients_descending": expected,
            "n8_overlap_support_size": 5,
            "jacobi_clock_and_residual_checks": "EXACT_PASS",
            "overlap_score_and_degree_two_cancellation": "EXACT_PASS",
            "uniform_source_constant_exact": str(Csrc)}


def check_moving_reference() -> dict[str, Any]:
    a = s.symbols("a")
    ref = [s.Rational(1,2)+a,s.Rational(1,2)-a]
    val = sum(s.Rational(1,2)*s.log(s.Rational(1,2)/r) for r in ref)
    second = s.diff(val,a,2).subs(a,0)
    zero(second-4,"moving-reference sanity check")
    # Generic scalar Bregman Hessian (normalization is not needed for the integrand).
    f,g,f1,g1,f2,g2 = s.symbols("f g f1 g1 f2 g2",positive=True)
    vars0,vars1,vars2 = [f,g],[f1,g1],[f2,g2]
    B = f*s.log(f/g)-f+g
    B2 = sum(s.diff(B,v0)*v2 for v0,v2 in zip(vars0,vars2))
    B2 += sum(s.diff(B,v0,w0)*v1*w1
              for v0,v1 in zip(vars0,vars1)
              for w0,w1 in zip(vars0,vars1))
    delta,delta1,delta2=f-g,f1-g1,f2-g2
    rhs = delta2*s.log(f/g)+g2*(s.log(f/g)-delta/g)
    rhs += (delta1-g1/g*delta)**2/f
    zero(B2-rhs,"generic moving Bregman Hessian")
    return {"moving_reference_second": str(second),
            "generic_Bregman_second_identity": "EXACT_PASS"}


def check_two_law_graph_identity() -> dict[str, Any]:
    """Two rational densities verify graph factors and the second-order ledger.
    This is an algebra check, not a counterexample in the fixed DPP model.
    """
    f = s.Matrix([s.Rational(3,5), s.Rational(7,5)])
    g = s.Matrix([s.Rational(4,5), s.Rational(6,5)])
    L = s.Matrix([[-1,1],[1,-1]])
    ell = s.Matrix([s.log(f[i]/g[i]) for i in range(2)])
    def inner(x: s.Matrix, y: s.Matrix) -> s.Expr:
        return (x.dot(y))/2
    def quotient(x: s.Matrix, y: s.Matrix) -> s.Matrix:
        return s.Matrix([x[i]/y[i] for i in range(2)])
    d = ell[1]-ell[0]
    ed = f[1]*g[0]/(f[0]*g[1])
    Kp, Km = (ed-1-d)/d**2, (1/ed-1+d)/d**2
    conductance = (f[0]*Kp+f[1]*Km)/2
    dissipation = (f[0]*(ed-1-d)+f[1]*(1/ed-1+d))/2
    zero(conductance*d**2-dissipation, "ordered-edge graph factor")
    zero(inner(L*f,ell)-inner(f,quotient(L*g,g))+dissipation,
         "two-moving-law entropy dissipation")

    Ap,Bp,Cp,tau,gamma,r = s.symbols("A B C tau gamma r")
    f1 = s.Matrix([r,-r])
    g1 = tau*L*g
    Z = L*(L+gamma*s.eye(2))*g
    f2 = (Cp*L*f-Bp*f1)/Ap
    g2 = (Cp*L*g-Bp*g1)/Ap+tau**2*Z
    residual = f1-tau*L*f
    R1 = inner(f1,ell)-inner(f,quotient(g1,g))
    Qrel = sum((f1[i]-f[i]*g1[i]/g[i])**2/f[i]
               for i in range(2))/2
    R2 = inner(f2,ell)-inner(f,quotient(g2,g))+Qrel
    zero(R1+tau*dissipation-inner(residual,ell),
         "first-order modulated identity")
    zero(Ap*R2+Bp*R1+Cp*dissipation-Ap*Qrel
         +Ap*tau**2*inner(f-g,quotient(Z,g)),
         "second-order modulated Jacobi identity")
    return {"rational_two_state_densities": True,
            "ordered_edge_energy_factor": "EXACT_PASS",
            "two_moving_law_dissipation": "EXACT_PASS",
            "second_order_modulated_Jacobi_identity": "EXACT_PASS"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=None)
    args = parser.parse_args()
    results = {"status":"EXACT_PASS","n4":check_n4(),
               "algebra":check_algebra(),"moving_reference":check_moving_reference(),
               "two_law_graph":check_two_law_graph_identity(),
               "not_tested":["n8 E_second numeric parameter locations",
                             "all-n midpoint sign","o(n) bridge",
                             "large configuration or parameter scans"]}
    text = json.dumps(results,ensure_ascii=False,indent=2)
    if args.output is not None:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text+"\n",encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
