"""Exact author checks supporting the analytic proofs (not an independent review).

Run with Python 3 and SymPy. This checks finite identities and rational constants;
it does not certify an infinite-volume limit by sampling finite matrices.
"""
from __future__ import annotations
import datetime as dt
import json
from collections import defaultdict
from pathlib import Path
import sympy as sp

Q = sp.Rational


def main() -> None:
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    n = 4
    bits = [[(mask >> j) & 1 for j in range(n)] for mask in range(1 << n)]
    U = sp.Matrix([[sp.I ** (i*j) / 2 for j in range(n)] for i in range(n)])
    assert U.conjugate().T * U == sp.eye(n)
    c, u = Q(19, 20), Q(3, 4)
    cases = [[Q(1), Q(1), Q(0), Q(0)],
             [Q(1, 10), Q(3, 10), Q(7, 10), Q(9, 10)]]
    rows = []
    for eig in cases:
        kernel_Q = sp.simplify(U * sp.diag(*eig) * U.conjugate().T)
        K = sp.eye(n)/2 + u*c*(kernel_Q-sp.eye(n)/2)
        lam = [Q(1, 2)+u*c*(t-Q(1, 2)) for t in eig]
        vv = [(x*(1-x)) for x in lam]
        v = (1-u*u*c*c)/4
        V = sum(t*(1-t) for t in eig)
        latent = []
        latent1 = []
        latent2 = []
        score = []
        logsecond = []
        for z in bits:
            pz = sp.prod(lam[j] if z[j] else 1-lam[j] for j in range(n))
            Sz = u*sum((z[j]-lam[j])/vv[j] for j in range(n))
            Tz = -u*u*sum(1/vv[j]+(1-2*lam[j])*(z[j]-lam[j])/vv[j]**2 for j in range(n))
            latent.append(pz); latent1.append(pz*Sz); latent2.append(pz*(Sz*Sz+Tz))
            score.append(Sz); logsecond.append(Tz)
        channel = sp.zeros(1 << n)
        for out, yy in enumerate(bits):
            A = [j for j in range(n) if yy[j]]
            for inp, zz in enumerate(bits):
                S = [j for j in range(n) if zz[j]]
                if len(A) == len(S):
                    det = U.extract(A, S).det() if A else sp.S.One
                    channel[out, inp] = sp.simplify(det*sp.conjugate(det))
        assert all(sum(channel[:, j]) == 1 for j in range(1 << n))
        assert all(sum(channel[j, :]) == 1 for j in range(1 << n))
        output = channel*sp.Matrix(latent)
        output1 = channel*sp.Matrix(latent1)
        output2 = channel*sp.Matrix(latent2)
        residual2 = sp.S.Zero
        latent_residual2 = sp.S.Zero
        for mask, yy in enumerate(bits):
            A = K-sp.diag(*[1-y for y in yy])
            p = sp.factor((-1)**(n-sum(yy))*A.det())
            inv = A.inv()
            p1 = sp.factor(u*p*sp.trace(inv))
            p2 = sp.factor(u*u*p*(sp.trace(inv)**2-sp.trace(inv*inv)))
            assert sp.simplify(output[mask]-p) == 0
            assert sp.simplify(output1[mask]-p1) == 0
            assert sp.simplify(output2[mask]-p2) == 0
            W = u*(sum(yy)-Q(n, 2))/v
            residual2 += p*(p1/p-W)**2
            latent_residual2 += latent[mask]*(score[mask]-W)**2
        e1sq = u**6*c**4*V/(4*v**3)
        residual2, latent_residual2 = map(sp.factor, (residual2, latent_residual2))
        assert residual2 <= latent_residual2 <= e1sq
        assert sum(output) == 1 and sum(output1) == sum(output2) == 0
        rows.append(dict(eigenvalues=list(map(str,eig)), V=str(V),
                         observed_score_error_squared=str(residual2),
                         latent_score_error_squared=str(latent_residual2),
                         claimed_upper_bound_squared=str(e1sq),
                         complete_atoms=16, all_three_jet_identities_exact=True))

    # Exact four-site external-field witness, now u=1.
    projection = sp.simplify(U[:,:2]*U[:,:2].conjugate().T)
    assert sp.simplify(projection*projection-projection) == sp.zeros(n) and sp.trace(projection) == 2
    K=(1-c)/2*sp.eye(n)+c*projection
    probabilities=[]
    for yy in bits:
        probabilities.append(sp.factor((-1)**(n-sum(yy))*(K-sp.diag(*[1-y for y in yy])).det()))
    v=(1-c*c)/4
    p1=[p*(sum(y)-2) for p,y in zip(probabilities,bits)]
    p2=[p*((sum(y)-2)**2-4*v) for p,y in zip(probabilities,bits)]
    rational=sp.S.Zero
    log_coefficients=defaultdict(lambda:sp.S.Zero)
    for mask in range(0,16,2):
        x,y=probabilities[mask:mask+2]
        x1,y1=p1[mask:mask+2];x2,y2=p2[mask:mask+2]
        rational+=(x+y)/2*(x1/x-y1/y)**2+(1-y/x)*x2/2+(1-x/y)*y2/2
        arg=y/x;coefficient=(y2-x2)/2
        if arg<1:arg=1/arg;coefficient=-coefficient
        log_coefficients[arg]+=coefficient
    log_coefficients={k:sp.factor(vv) for k,vv in log_coefficients.items() if vv}
    assert sp.factor(rational)==Q(39,800)
    assert log_coefficients=={Q(761,39):-Q(39,1600), Q(290321,29679):-Q(11018319,256000000)}
    upper = Q(39,800)-Q(39,1600)*Q(8,3)-Q(11018319,256000000)*2
    assert upper == -Q(13098319,128000000) < -Q(1,10)

    # The explicit asymptotic band-compensation constant.
    gaussian_lower=Q(665,768)*Q(133,440)**4
    difference=sp.factor(gaussian_lower-Q(1,140))
    assert gaussian_lower==Q(41615795893,5757075456000)
    assert difference==Q(3456798451,40299528192000)>0

    # Verify the global lower curvature of the production function.
    q=sp.symbols('q',positive=True)
    phi=(q-Q(1,2))*sp.log(q/(1-q))
    assert sp.simplify(sp.diff(phi,q,2)-1/(2*q*q*(1-q)**2))==0

    result=dict(status='EXACT_AUTHOR_CHECKS_PASS_NOT_INDEPENDENT_REVIEW',
                started_utc=started,finished_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                python_checks='16 complete atoms per finite case; no atom omitted',
                sympy_version=sp.__version__,score_cases=rows,
                external_field_atom_numerators=[int(x*2560000) for x in probabilities],
                external_field_rational_term=str(sp.factor(rational)),
                external_field_log_coefficients={str(k):str(vv) for k,vv in log_coefficients.items()},
                external_field_strict_upper_bound=str(upper),
                band_constant_rational_lower_bound=str(gaussian_lower),
                band_constant_minus_one_over_140=str(difference),
                asymptotic_limits='proved analytically in Markdown, not established by this script')
    Path(__file__).with_name('EXACT_CHECK_RECEIPT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
