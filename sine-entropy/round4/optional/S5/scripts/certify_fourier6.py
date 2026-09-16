#!/usr/bin/env python3
"""Exact rational/logarithm certificate for the complete aggregate remainder.

Main counterexample: genuine Fourier projection n=6,k=2,c=1/2,a=49/100.
All inequalities use fractions and rigorously bounded logarithms. Floating
geometry is tested separately in transport_diagnostic.py.
"""
from __future__ import annotations
import argparse
import json
import itertools
import math
from pathlib import Path
from fractions import Fraction as Q
from exact_common import Interval,Jet,log_q,channel_jets,count_jets,ensure_output,LOG_TERMS


def fourier2_rational(n:int)->dict[int,Q]:
    if n==4:
        pair_weights={1:Q(1,8),2:Q(1,4)}
    elif n==6:
        pair_weights={1:Q(1,36),2:Q(1,12),3:Q(1,9)}
    else:raise ValueError('This certificate supports n=4 or 6 only.')
    return {(1<<i)|(1<<j):pair_weights[min(j-i,n-j+i)] for i,j in itertools.combinations(range(n),2)}


def check_case(n:int,k:int,law:dict[int,Q],a:Q,c:Q,kind:str):
    atoms=channel_jets(n,k,law,a,c)
    pi=count_jets(n,k,a,c)
    by_layer=[[S for S in range(1<<n) if S.bit_count()==ell] for ell in range(n+1)]
    for ell,states in enumerate(by_layer):
        assert sum((atoms[S] for S in states),Jet(Q(0)))==pi[ell]
    I_full=sum(x.first*x.first/x.value for x in atoms)
    H2=-sum((x.second*log_q(x.value) for x in atoms),Interval.point(0))-I_full
    I_count=sum(x.first*x.first/x.value for x in pi)
    Phi2=-sum((pi[l].second*log_q(pi[l].value/Q(math.comb(n,l))) for l in range(n+1)),Interval.point(0))-I_count
    D2=Interval.point(0);Btotal=Interval.point(0);Rtotal=Interval.point(0)
    I_spatial=Q(0);layer_records=[]
    Acc_total=Interval.point(0);Weight_total=Interval.point(0)
    R_constant=Q(0);R_log_coefficients={}
    w=a*(1-c-a);w1=1-c-2*a
    for ell,states in enumerate(by_layer):
        N=Q(len(states));p=pi[ell]
        r={S:N*atoms[S].value/p.value for S in states}
        v={S:N*atoms[S].first/p.value-p.first/p.value*r[S] for S in states}
        r2={S:N*atoms[S].second/p.value-2*p.first/p.value*v[S]-p.second/p.value*r[S] for S in states}
        assert sum(r.values())==N and sum(v.values())==0 and sum(r2.values())==0
        # Exact atom-acceleration coefficient check; log p=log(pi/N)+log r.
        for S in states:
            assert atoms[S].value==p.value*r[S]/N
            assert atoms[S].second==(p.value*r2[S]+2*p.first*v[S]+p.second*r[S])/N
        F=sum((r[S]*log_q(r[S]) for S in states),Interval.point(0))/N
        F1=sum((v[S]*log_q(r[S]) for S in states),Interval.point(0))/N
        I=sum(v[S]*v[S]/r[S] for S in states)/N
        F2=sum((r2[S]*log_q(r[S]) for S in states),Interval.point(0))/N+I
        I_spatial+=p.value*I
        if all(r[S]==1 and v[S]==0 and r2[S]==0 for S in states):
            B=Interval.point(0);acc=Interval.point(0);beta1=None
        else:
            if kind=='rank1':
                d=c*ell/n
                lam=d/(w+d)
                loglam1=-w1/(w+d)
                loglam2=2/(w+d)+w1*w1/(w+d)**2
                f={S:Q(n,ell)*sum(mu for A,mu in law.items() if A&S)-1 for S in states}
                gamma=Q(n,ell*(n-ell))
            elif kind=='rank2_uniform':
                alpha=Q(ell*(ell-1),n*(n-1))
                den=w*w+Q(2)*c*ell/n*w+c*c*alpha
                dw=2*w+Q(2)*c*ell/n
                lam=c*c*alpha/den
                loglam1=-dw*w1/den
                loglam2=2*dw/den+(dw*dw-2*den)*w1*w1/den**2
                f={S:sum(mu for A,mu in law.items() if A&S==A)/alpha-1 for S in states}
                gamma=Q(2*(n-1),ell*(n-ell))
            else:raise ValueError('A nonconstant slice requires a supported single-mode kind.')
            lam1=lam*loglam1;lam2=lam*(loglam2+loglam1*loglam1)
            assert loglam2>0
            for S in states:
                assert r[S]==1+lam*f[S]
                assert v[S]==lam1*f[S] and r2[S]==lam2*f[S]
                # EXACT normalized Bernoulli-Laplace eigenvector check.
                Lf=sum((f[T]-f[S]) for T in states if (T^S).bit_count()==2)/Q(ell*(n-ell))
                assert Lf==-gamma*f[S]
            Fx=sum((f[S]*log_q(r[S]) for S in states),Interval.point(0))/N
            Fxx=sum(f[S]*f[S]/r[S] for S in states)/N
            B=lam1*lam1/Q(2)*(Fxx+Fx/lam)
            beta1=loglam2/gamma
            J=gamma*lam*Fx
            acc=B+beta1*J
            # Coefficient identity F''=2 B+beta' J, not just an interval check.
            assert lam1*lam1/lam+beta1*gamma*lam==lam2
            # Export an independently evaluable exact log-linear expression
            # for the aggregate remainder, using acc=B+beta_prime*J plus
            # the actual changing-weight terms (not H or D as a definition).
            R_constant+=p.value*lam1*lam1/Q(2)*Fxx
            coeff_factor=p.value*(lam1*lam1/(2*lam)+beta1*gamma*lam)+2*p.first*lam1
            for S in states:
                coeff=(coeff_factor*f[S]+p.second*r[S])/N
                if r[S]!=1 and coeff:
                    R_log_coefficients[r[S]]=R_log_coefficients.get(r[S],Q(0))+coeff
            residual=F2-B-acc
            assert residual.contains_zero() and residual.width()<Q(1,10**50)
        weight=2*p.first*F1+p.second*F
        D2+=p.value*F2+weight
        Btotal+=p.value*B
        Rtotal+=p.value*acc+weight
        Acc_total+=p.value*acc;Weight_total+=weight
        layer_records.append({'ell':ell,'pi':str(p.value),'pi_first':str(p.first),'pi_second':str(p.second),
                              'F':F.outward(),'F_first':F1.outward(),'F_second':F2.outward(),
                              'Bochner':B.outward(),'acceleration':acc.outward(),'layer_weight':weight.outward(),
                              'beta_prime':None if beta1 is None else str(beta1)})
    R_expression=Interval.point(R_constant)+sum((coef*log_q(arg) for arg,coef in R_log_coefficients.items()),Interval.point(0))
    R_expression_residual=R_expression-Rtotal
    assert R_expression_residual.contains_zero() and R_expression_residual.width()<Q(1,10**50)
    assert I_full==I_count+I_spatial
    eq1=H2-(Phi2-D2);eq2=H2-(Phi2-Btotal-Rtotal)
    assert eq1.contains_zero() and eq1.width()<Q(1,10**50)
    assert eq2.contains_zero() and eq2.width()<Q(1,10**50)
    report={'n':n,'k':k,'a':str(a),'c':str(c),'input_law':{str(A):str(p) for A,p in law.items()},
            'kind':kind,'H_second':H2.outward(),'Phi_second':Phi2.outward(),'D_second':D2.outward(),
            'total_Bochner':Btotal.outward(),'aggregate_remainder':Rtotal.outward(),
            'total_acceleration':Acc_total.outward(),'total_layer_weight_correction':Weight_total.outward(),
            'aggregate_remainder_exact_log_expression':{
                'constant':str(R_constant),
                'terms':[{'argument':str(arg),'coefficient':str(coef)} for arg,coef in sorted(R_log_coefficients.items()) if coef],
                'expression':'constant + sum(coefficient*log(argument))',
                'independent_expression_enclosure':R_expression.outward()},
            'full_Fisher':str(I_full),'count_Fisher':str(I_count),'weighted_slice_Fisher':str(I_spatial),
            'exact_rational_checks':['input/count normalization','count generating function','atom acceleration coefficients',
                                     'full=count+slice Fisher','single-mode density jets','normalized BL eigenvectors',
                                     'single-mode Bochner/acceleration coefficients'],
            'direct_vs_slice_interval_residual':eq1.outward(55),
            'direct_vs_transport_interval_residual':eq2.outward(55),
            'layers':layer_records,
            'atoms':[{'mask':S,'p':str(x.value),'p_first':str(x.first),'p_second':str(x.second)} for S,x in enumerate(atoms)]}
    return report,{'H2':H2,'Phi2':Phi2,'D2':D2,'B':Btotal,'R':Rtotal}


def run(outdir:Path):
    cases=[]
    for params in [
        (2,1,{1:Q(1,100),2:Q(99,100)},Q(1,1000),Q(19,20),'rank1'),
        (3,1,{1:Q(1)},Q(1,1000),Q(19,20),'rank1'),
        (3,0,{0:Q(1)},Q(1,1000),Q(19,20),'constant'),
        (4,2,fourier2_rational(4),Q(1,100),Q(19,20),'rank2_uniform'),
        (6,2,fourier2_rational(6),Q(49,100),Q(1,2),'rank2_uniform')]:
        report,vals=check_case(*params);cases.append(report)
    cert=vals
    assert Q(-184,1000)<cert['R'].lo<=cert['R'].hi<Q(-183,1000)
    assert cert['H2'].hi<Q(-37)
    assert cert['D2'].lo>Q(164,100) and cert['B'].lo>Q(183,100)
    # Every nonconstant conditional layer has strictly favorable acceleration,
    # not merely a nonnegative sum. This is separate from the aggregate claim.
    for rec in cases[-1]['layers']:
        if rec['ell'] in (2,3,4):
            assert Q(rec['F_second']['lower'])>0
            assert Q(rec['acceleration']['lower'])>0
            assert Q(rec['beta_prime'])>0
    result={'status':'EXACT_FINITE_CERTIFICATE','arithmetic':'fractions.Fraction only; no floating-point assertions',
            'log_bound':{'series_terms':LOG_TERMS,'formula':'log(y)=2 sum z^(2j+1)/(2j+1), z=(y-1)/(y+1), 1<=y<=2; omitted tail <=2*z^(2N+1)/((2N+1)*(1-z^2)); scale by powers of 2'},
            'certified_main_inequalities':['-184/1000 < aggregate remainder < -183/1000','H_second < -37','D_second > 164/100','total_Bochner > 183/100'],
            'cases':cases}
    outdir=ensure_output(outdir)
    (outdir/'fourier6_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print('EXACT Fourier6 certificate: all assertions passed.')
    print(json.dumps({key:value.outward() for key,value in cert.items()},indent=2))
    return result

if __name__=='__main__':
    pa=argparse.ArgumentParser();pa.add_argument('--out-dir',type=Path,default=Path(__file__).resolve().parents[1]/'outputs'/'exact')
    run(pa.parse_args().out_dir)
