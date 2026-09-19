#!/usr/bin/env python3
"""Reproducible finite algebra checks; no external repository/network needed.
Floating-point tests complement, but do not replace, RESULT.md's proofs and
interval_certificate.py's exact rational sign decisions.
"""
from __future__ import annotations
import argparse,json,math,platform,sys
from pathlib import Path
from itertools import combinations
import numpy as np
from defects import *

checks=[]
def check(name: str,error: float,tolerance: float,**extra):
    if not np.isfinite(error) or error>tolerance:
        raise AssertionError((name,error,tolerance,extra))
    checks.append({'name':name,'status':'PASS','error':float(error),'tolerance':float(tolerance),**extra})

def product_law(q):
    n=len(q);return np.array([np.prod([q[i] if (y>>i)&1 else 1-q[i] for i in range(n)]) for y in range(1<<n)])

def shape_constant(P,k):
    _,n=validate(P);g=n-k;h=k*g;d=g-k
    LL=[]
    for target,remove,num in [(k+1,True,1),(k-1,False,1),(k+2,True,2),(k-2,False,2)]:
        weights=[]
        for y in range(1<<n):
            if y.bit_count()!=target:continue
            inds=[i for i in range(n) if bool((y>>i)&1)==remove]
            a=0.
            for A in combinations(inds,num):
                z=y
                for i in A:z^=1<<i
                a+=P[z]
            weights.append(a)
        W=np.array(weights);LL.append(float(np.dot(W[W>0],np.log(W[W>0]))))
    DJ=0.
    for y in range(1<<n):
        if P[y]==0:continue
        for i in range(n):
            if not((y>>i)&1):continue
            for j in range(n):
                if (y>>j)&1:continue
                z=y^(1<<i)^(1<<j);DJ+=P[y]*math.log(P[y]/P[z])
    Cp=(n*n-n-6*h)*entropy(P)-2*DJ+2*(d-1)*LL[0]-2*(d+1)*LL[1]-2*LL[2]-2*LL[3]
    return Cp

def main(outdir: Path):
    outdir.mkdir(parents=True,exist_ok=True);rng=np.random.default_rng(20260919)
    # A product law makes every genuine off-site pair exactly zero.
    q=[.23,.46,.71,.62];P=product_law(q);co=full_support_coefficients(P,.37);met=table_metrics(P)
    check('product-law pair coefficients vanish',max(abs(z['J']) for z in co['pairs']),1e-12)
    check('product-law L=-sum Bernoulli Fisher',abs(met['L']+sum(1/(x*(1-x)) for x in q)),1e-10)
    # The missing diagonal cannot be hidden in a pair sum at n=1.
    P1=np.array([.7,.3]);p=.61;c1=full_support_coefficients(P1,p)
    check('n=1 missing diagonal coefficient',abs(c1['B2']+(p-.3)**2/(2*.3*.7)),1e-14)
    check('n=1 genuine pair list empty',float(len(c1['pairs'])),0.)
    # Purely probabilistic pair identity, even without a DPP hypothesis.
    for n in [2,3,4,5]:
        P=rng.uniform(.2,1.,1<<n);P/=P.sum();met=table_metrics(P)
        for p in [.19,.43,.81]:
            co=full_support_coefficients(P,p)
            err=max(abs(x['Jpp_kl_formula']-y['Jpp']) for x,y in zip(co['pairs'],met['pairs']))
            check(f'actual weighted Jpp identity random n={n},p={p}',err,2e-10)
        check(f'normalization/Fisher decomposition n={n}',abs(met['L']-met['direct_L']),2e-10)
    # DPP channel identity and independent common-diagonal Hessian.
    K=sine_kernel(4,.37);P=dpp_probabilities(K);eps=.14;p=.31
    out=noise_jet(P,eps,p);target=dpp_probabilities((1-eps)*K+eps*p*np.eye(4))
    check('DPP kernel equals actual resampling output',float(np.max(abs(out[0]-target))),2e-13)
    check('H_pp=epsilon^2 actual diagonal Hessian',abs(entropy_pp(out)-eps**2*table_metrics(target)['L']),2e-10)
    # MI coefficients, polynomiality in p, and explicit remainders.
    P=product_law([.3,.4,.6])
    # Perturb the product law but retain a moderate conditional floor.
    P=.7*P+.3*np.array([.05,.08,.12,.25,.2,.1,.11,.09]);P/=P.sum()
    n=3;p=.38;co=full_support_coefficients(P,p);met=table_metrics(P);beta=conditional_floor(P)
    for tau in [.02,.05,.10]:
        eps=tau/(n*(1+1/beta));Iactual=mutual_information(P,eps,p)
        R=Iactual-eps*co['B1']-eps**2*co['B2']
        bound=(4*math.log(1/beta)+4)*tau**3
        check(f'MI value remainder tau={tau}',abs(R)/bound,1.)
        Rpp=entropy_pp(noise_jet(P,eps,p))-eps**2*met['L']
        boundpp=(2*entropy(P)+10)*tau**3
        check(f'curvature remainder tau={tau}',abs(Rpp)/boundpp,1.)
    eps_values=[.002,.001,.0005];third_errors=[]
    for eps in eps_values:
        res=(entropy_pp(noise_jet(P,eps,p))-eps**2*met['L'])/eps**3
        third_errors.append(abs(res-co['third_entropy_coefficient_pp']))
    check('third-coefficient curvature convergence',third_errors[-1],third_errors[0]*.35,errors=third_errors)
    errors=[]
    for eps in [.02,.01]:
        err=abs(mutual_information(P,eps,p)-(eps*co['B1']+eps**2*co['B2']+eps**3*co['B3']));errors.append(err)
    check('third MI coefficient leaves fourth-order error',errors[1],errors[0]*.08,errors=errors)
    vals=[]
    for p in [.15,.3,.5,.7,.85]:vals.append([x['J'] for x in full_support_coefficients(P,p)['pairs']])
    vals=np.array(vals);pp=np.array([.15,.3,.5,.7,.85]);err=0.
    for j in range(vals.shape[1]):
        fit=np.polyfit(pp,vals[:,j],2);err=max(err,float(np.max(abs(np.polyval(fit,pp)-vals[:,j]))))
    check('all natural pair coefficients quadratic in p',err,2e-12)
    # Singular projection: universal leading and epsilon^2 log coefficient.
    proj_rows=[]
    for n,k in [(2,1),(4,2),(5,2),(6,3),(8,4)]:
        P=projection_probabilities(n,k);C=shape_constant(P,k);h=k*(n-k)
        for p in [.23,.5,.74]:
            ex=projection_expansion(P,k,p)
            check(f'projection A1 n={n},p={p}',abs(ex['A1']-ex['r']),2e-12)
            check(f'projection A2 n={n},p={p}',abs(ex['A2']-ex['A2_expected']),2e-11)
            formula=h/(p*(1-p))-2*h*math.log(p*(1-p))-4*h-n+C
            check(f'projection explicit B2pp n={n},p={p}',abs(ex['B2pp']-formula),2e-9)
            rr=[]
            for eps in [.001,.0001,.00001]:
                exact=entropy_pp(noise_jet(P,eps,p))
                approx=eps*ex['B1pp']+4*h*eps**2*math.log(1/eps)+eps**2*ex['B2pp']
                res=exact-approx;rr.append(abs(res)/(eps**3*(1+abs(math.log(eps)))))
                proj_rows.append({'n':n,'k':k,'p':p,'epsilon':eps,'Hpp':exact,'first_two_stratified_orders':approx,'remainder':res,'scaled_remainder':rr[-1],'B2pp':ex['B2pp'],'shape_constant':C})
            check(f'projection remainder bounded across three eps n={n},p={p}',max(rr),1e5,scaled_remainders=rr)
    # Small exact projection with a closed elementary expression.
    eps=.007;P=projection_probabilities(2,1);b=eps/2-eps**2/4
    closed=4*eps**2*math.log((.5-b)/b)-2*eps**2/b
    check('n=2 singular projection closed Hessian',abs(entropy_pp(noise_jet(P,eps,.5))-closed),1e-13)
    # Gap-dependent probability-to-curvature transfer, including kernel step.
    trans=[]
    for m in [2,4,6,8]:
        K=sine_kernel(m,.5);PK=dpp_probabilities(K);Lk=table_metrics(PK)['L']/m
        d=explicit_sine_gap(m,.5)
        for N in [32,64,128,256]:
            Q=cyclic_block(N,N//2,m);PQ=dpp_probabilities(Q);lq=table_metrics(PQ)['L']/m
            ker=float(np.linalg.norm(Q-K,'fro'))
            entry_bound=math.pi**2*m*m/(12*N*N)
            check(f'cyclic-to-sine kernel estimate m={m},N={N}',ker,entry_bound)
            # For small sizes use a numerically verified common gap ONLY as a diagnostic.
            eigs=np.concatenate([np.linalg.eigvalsh(K),np.linalg.eigvalsh(Q)])
            gap=.49*min(float(eigs.min()),float((1-eigs).min()))
            bound=transfer_bound(K,Q,gap);actual=abs(lq-Lk)
            check(f'actual interaction transfer diagnostic m={m},N={N}',actual,bound)
            trans.append({'m':m,'period':N,'normalized_L_difference':actual,'kernel_Frobenius_error':ker,'diagnostic_gap':gap,'transfer_upper_bound_using_diagnostic_gap':bound,'proved_sine_gap_floor':d,'scope':'numerical illustration; theorem does not rely on numerical eigenvalues'})
    outdir.joinpath('projection_profile.json').write_text(json.dumps(proj_rows,indent=2))
    outdir.joinpath('transfer_examples.json').write_text(json.dumps(trans,indent=2))
    report={'status':'PASS','kind':'floating-point algebra and finite-model diagnostics; not an infinite-volume proof','checks_passed':len(checks),'python':platform.python_version(),'numpy':np.__version__,'checks':checks}
    outdir.joinpath('verification.json').write_text(json.dumps(report,indent=2))
    print(f'PASS: {len(checks)} finite checks.');return report

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--outdir',type=Path,default=Path(__file__).resolve().parents[1]/'results');args=ap.parse_args();main(args.outdir)
