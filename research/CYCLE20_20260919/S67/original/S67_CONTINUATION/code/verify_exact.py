#!/usr/bin/env python3
"""S67 continuation: exact rational verification of the analytic constants.

Python standard library only. This is NOT a finite-volume n=15/16 rerun,
not a numerical entropy-rate certificate, and not a session-duration claim.
The mathematical proof is in S67_ACCELERATION_CONTINUATION_RESULT.md.
"""
from __future__ import annotations
from fractions import Fraction as F
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from pathlib import Path
from itertools import product
import argparse, datetime, json, math, time


def enclosure(q: F, digits: int = 65) -> dict[str, str]:
    out = {}
    for label, rounding in (("lower", ROUND_FLOOR), ("upper", ROUND_CEILING)):
        with localcontext() as ctx:
            ctx.prec = digits
            ctx.rounding = rounding
            out[label] = str(Decimal(q.numerator) / Decimal(q.denominator))
    return out


def atan_interval(x: F, count: int) -> tuple[F, F]:
    assert 0 < x < 1 and count > 0
    partial = sum(((-1)**k * x**(2*k+1) / (2*k+1)
                   for k in range(count)), F(0))
    nxt = (-1)**count * x**(2*count+1) / (2*count+1)
    return min(partial, partial+nxt), max(partial, partial+nxt)


def exp_partial(x: F, degree: int) -> F:
    return sum((x**k / math.factorial(k) for k in range(degree+1)), F(0))


def matmul(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[x+y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a, t):
    return [[t*x for x in ar] for ar in a]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def inverse(a):
    n = len(a)
    aug = [list(ar)+ir for ar, ir in zip(a, eye(n))]
    for j in range(n):
        pivot = next((i for i in range(j, n) if aug[i][j]), None)
        if pivot is None:
            raise ArithmeticError("Singular exact-rational matrix")
        aug[j], aug[pivot] = aug[pivot], aug[j]
        p = aug[j][j]
        aug[j] = [v/p for v in aug[j]]
        for i in range(n):
            if i != j:
                p = aug[i][j]
                aug[i] = [v-p*w for v, w in zip(aug[i], aug[j])]
    return [row[n:] for row in aug]


def det(a):
    a = [row[:] for row in a]
    n, ans = len(a), F(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            ans = -ans
        p = a[j][j]
        ans *= p
        for i in range(j+1, n):
            q = a[i][j]/p
            for k in range(j+1, n):
                a[i][k] -= q*a[j][k]
    return ans


def law(k):
    n = len(k)
    out = {}
    for x in product((0, 1), repeat=n):
        a = [row[:] for row in k]
        for i in range(n):
            a[i][i] -= 1-x[i]
        p = (-1)**(n-sum(x))*det(a)
        assert p > 0
        out[x] = p
    assert sum(out.values(), F(0)) == 1
    return out


def flips(x, *sites):
    x = list(x)
    for i in sites:
        x[i] = 1-x[i]
    return tuple(x)


def run() -> dict:
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    clock = time.monotonic()
    checks = []
    c, s, radius = F(19, 20), F(39, 1600), F(1, 200)
    a5l, a5u = atan_interval(F(1, 5), 44)
    a239l, a239u = atan_interval(F(1, 239), 14)
    pil, piu = 16*a5l-4*a239u, 16*a5u-4*a239l
    assert F(157, 50) < pil < piu < F(3927, 1250)
    taul, tauu = c*c/piu**2, c*c/pil**2
    assert F(9, 100) < taul < tauu < F(23, 250)
    dl = 2+2/(1-64*taul**2)
    du = 2+2/(1-64*tauu**2)
    assert dl > F(63, 10) and du < 7
    checks.append("Machin pi enclosure and uniform three-site Fisher input d_3 > 63/10")

    def P(r):
        return -2*r**3+51283*r**2-384800*r+528000
    def w(r):
        return (r-1)*(41*r+400)/(r*(r+440))
    assert P(F(1)) > 0 and P(F(2)) < 0
    assert P(F(569, 100)) < 0 < P(F(57, 10))
    assert P(F(400)) > 0
    assert 102566-12*400 > 0
    assert -6+102566-384800 < 0
    assert -6*400**2+102566*400-384800 > 0
    assert F(3, 2)*w(F(569, 100)) > F(7, 4)
    assert exp_partial(F(7, 4), 6) > F(57, 10)
    checks.append("Exact derivative signs and exponential comparison for the odds-width pair lemma")

    assert F(147, 97) < F(25, 16)
    assert F(4753, 4563) < F(25, 24)
    r2_slope = F(1520, 1521)*1600/F(24, 25)
    assert r2_slope < 1666
    t_slope = (1/s)*(1+F(64, 3*(1521-64)))
    assert t_slope < 42
    ymax = F(21, 100)
    # cosh(y) <= 1/(1-y^2/2); sinh(y)/y <= 1/(1-y^2/6).
    assert 1/(1-ymax*ymax/2) < F(103, 100)
    assert 1/(1-ymax*ymax/6) < F(101, 100)
    yy = 2*ymax
    sinh_ratio_upper = 1+yy**2/6+yy**4/(120*(1-yy**2/42))
    assert sinh_ratio_upper < F(103, 100)
    c0_slope = (40*F(103, 200)-2)*42**2+2*(40*F(101, 100)+2*F(103, 100))*42
    assert c0_slope < 37000
    assert 2+(1/s-2)*F(5, 4) < 51
    envelope_slope = 1666*42+F(25, 24)*(37000+833*51)
    assert envelope_slope < 153000
    checks.append("All count-gauge, transport, hyperbolic-function, and compensated scalar envelope constants")

    # Exact algebra checks for the non-centered conditional allocation.
    for z in (F(4, 5), F(1), F(6, 5), F(5, 4)):
        u, v = z/(39+z), 39*z/(1+39*z)
        sp, sm, m, kappa0 = u*v, (1-u)*(1-v), u+v, 1/s-2
        assert m/sp == 2+kappa0/z
        assert (2-m)/sm == 2+kappa0*z
        for p in (F(99, 200), F(1, 2), F(101, 200)):
            direct = (m-p)/sp+(1-m+p)/sm
            closed = 3+kappa0*(p*z+(1-p)/z)-(1-p)*z*z-p/(z*z)
            assert direct == closed
        for r in (F(1, 10), F(1, 3), F(1, 2), F(4, 5)):
            for q in (F(1, 9), F(2, 5), F(3, 4)):
                lhs = q*(m/r-1)/sp+(1-q)*((2-m)/(1-r)-1)/sm
                rhs = (m-q)/sp+(1-m+q)/sm+(q-r)*(m/(sp*r)-(2-m)/(sm*(1-r)))
                assert lhs == rhs
    checks.append("Exact conditional compensation and C0 algebra")

    # Matrix algebra checks: rational positive contractions, not sine numerical certificates.
    n = 3
    I = eye(n)
    Q = [[F(1,2),F(1,4),F(0)], [F(1,4),F(1,2),F(1,4)], [F(0),F(1,4),F(1,2)]]
    E = add(Q, scale(matmul(Q,Q), -1))
    Kb = add(scale(I,F(1,40)),scale(Q,c))
    pb = law(Kb)
    matrix_cases = 0
    for z in (F(4,5),F(1),F(6,5),F(5,4)):
        u, v = z/(39+z),39*z/(1+39*z)
        m, sp, sm = u+v,u*v,(1-u)*(1-v)
        Kh = add(scale(I,u),scale(Q,v-u))
        Kt = matmul(scale(Kb,z),inverse(add(I,scale(Kb,z-1))))
        pt = law(Kt)
        Z = sum((pb[x]*z**sum(x) for x in pb),F(0))
        for x in pb:
            assert pt[x] == pb[x]*z**sum(x)/Z
            for i in range(n):
                for j in range(i+1,n):
                    ob = pb[flips(x,i)]*pb[flips(x,j)]/(pb[x]*pb[flips(x,i,j)])
                    ot = pt[flips(x,i)]*pt[flips(x,j)]/(pt[x]*pt[flips(x,i,j)])
                    assert ob == ot
            D = [[F((1-x[i]) if i==j else 0) for j in range(n)] for i in range(n)]
            S = [[F((2*x[i]-1) if i==j else 0) for j in range(n)] for i in range(n)]
            B = inverse(add(Kh,scale(D,-1)))
            weights = [sp if bit else sm for bit in x]
            W = [[weights[i] if i==j else F(0) for j in range(n)] for i in range(n)]
            left = add(matmul(matmul(B,W),B),scale(matmul(matmul(B,E),B),(v-u)**2))
            right = add(add(scale(add(matmul(S,B),matmul(B,S)),F(1,2)),scale(B,m-1)),scale(I,-1))
            assert left == right
            lhs_off = sum((B[i][j]**2 for i in range(n) for j in range(n) if i != j),F(0))
            leak = (v-u)**2*sum((matmul(matmul(B,E),B)[i][i]/weights[i] for i in range(n)),F(0))
            rhs_off = sum((((m-2*(1-x[i]))*B[i][i]-1)/weights[i]-B[i][i]**2 for i in range(n)),F(0))-leak
            assert lhs_off <= rhs_off and leak >= 0
            matrix_cases += 1
    checks.append(f"{matrix_cases} exact rational matrix/configuration checks, including nonzero contraction leakage and count-gauge invariance")

    I0, I2 = radius**2/2, radius**4/12
    assert I0 == F(1,80000) and I2 == F(1,19200000000)
    U = F(3,2)*((1/s-F(63,10))*I0+153000*I2)
    assert U == F(110333,166400000)
    assert U < F(664,1000000)
    beta = F(3,2)*2*(F(63,10)-4)*I0
    assert beta == F(69,800000)
    c16lo=F(".000146680480325883947552193048")
    c16hi=F(".000146680480325883947552193049")
    g16lo=F(".000141743962555442975188447184")
    g16hi=F(".000141743962555442975188447185")
    b16lo=F(".000104188037840358653653185471")
    b16hi=F(".000104188037840358653653185472")
    caplo, caphi = c16lo+g16lo+b16lo,c16hi+g16hi+b16hi
    assert U > caphi
    # A sufficient finite-window input, NOT proved to hold for the sine model.
    sufficient_d = F(83,4)
    U_if_input = F(3,2)*((1/s-sufficient_d)*I0+153000*I2)
    delta_if_input = caplo-U_if_input
    assert delta_if_input > F(49,100000000)
    # The simple actual-odds ceiling at b does not itself rule this input out.
    eta_b = F(39,800)
    ceiling_b = 1/(eta_b*(1-eta_b))
    assert sufficient_d < ceiling_b
    checks.append("Exact improved all-volume asymptotic bound, unpaid deficit, and explicitly conditional finite-window threshold")

    return {
        "status":"PASS",
        "proof_status":"PROVED analytic acceleration bound; entropy-rate objective INCOMPLETE",
        "checks": checks,
        "pi_interval":{"lower":enclosure(pil)["lower"],"upper":enclosure(piu)["upper"]},
        "three_site_d_star_interval":{"lower":enclosure(dl)["lower"],"upper":enclosure(du)["upper"]},
        "U_C_fraction":str(U),"U_C_interval":enclosure(U),
        "finite_fisher_boundary_beta_fraction":str(beta),
        "A_limsup_upper_interval":enclosure(U-c16lo),
        "required_C_cap_interval":{"lower":enclosure(caplo)["lower"],"upper":enclosure(caphi)["upper"]},
        "deficit_lower_interval":enclosure(U-caphi),
        "conditional_input_d_fraction":str(sufficient_d),
        "conditional_input_status":"UNVERIFIED: not asserted for any finite window or infinite model",
        "U_if_conditional_input_interval":enclosure(U_if_input),
        "delta_if_conditional_input_interval":enclosure(delta_if_input),
        "local_fisher_ceiling_at_b_interval":enclosure(ceiling_b),
        "started_utc":started,
        "finished_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "verification_wall_seconds":time.monotonic()-clock,
        "research_session_120_minutes":"NOT_CERTIFIED; verification runtime is not research duration",
        "original_n15_n16_certificate":"ACCEPTED INPUT; NOT RERUN"
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=(Path(__file__).resolve().parent.parent if Path(__file__).resolve().parent.name == "code" else Path(__file__).resolve().parent)/"certificates"/"exact_verification.json")
    args=parser.parse_args()
    result=run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))

if __name__=="__main__":
    main()
