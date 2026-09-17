#!/usr/bin/env python3
"""Optional binary64 diagnostics; not evidence for an exact or asymptotic sign.

Uses true contiguous Fourier projections, actual Toeplitz principal blocks,
and finite Gaussian observation draws. No finite difference approximates the
common-offset derivatives: full product-likelihood jets are evaluated instead.
"""
from __future__ import annotations
import argparse
import itertools
import json
import math
from pathlib import Path
import numpy as np
from math_core import safe_output
ROOT=Path(__file__).resolve().parents[1]

def configurations(n):
    return np.array(list(itertools.product((0,1),repeat=n)),dtype=float)

def fourier_law(n,k):
    U=np.exp(2j*np.pi*np.arange(n)[:,None]*np.arange(k)[None,:]/n)/np.sqrt(n)
    X=[];mu=[]
    for A in itertools.combinations(range(n),k):
        x=np.zeros(n);x[list(A)]=1;X.append(x)
        mu.append(abs(np.linalg.det(U[list(A),:]))**2)
    mu=np.array(mu);mu/=mu.sum()
    return np.array(X),mu,U@U.conj().T

def toeplitz_law(n,rho):
    delta=np.arange(n)[:,None]-np.arange(n)[None,:]
    K=rho*np.sinc(rho*delta)
    X=configurations(n);mu=[]
    for x in X:
        S=np.flatnonzero(x).tolist();rest=np.flatnonzero(1-x).tolist();total=0.
        for b in itertools.product((0,1),repeat=len(rest)):
            A=S+[i for i,yes in zip(rest,b) if yes]
            total+=(-1)**sum(b)*np.linalg.det(K[np.ix_(A,A)])
        mu.append(total)
    mu=np.array(mu);minimum=float(mu.min())
    if minimum < -1e-11:raise ArithmeticError('Atom cancellation too severe for this floating diagnostic')
    clipped=int(np.sum(mu<0));mu=np.maximum(mu,0);mu/=mu.sum()
    return X,mu,K,dict(minimum_raw_atom=minimum,negative_atoms_clipped=clipped,
                     eigenvalue_range=np.linalg.eigvalsh(K)[[0,-1]].tolist())

def fixed_likelihood(X,a,c):
    n=X.shape[1];Y=configurations(n)
    g=np.where(Y[:,None,:]>0,a+c*X[None,:,:],1-a-c*X[None,:,:])
    f=np.prod(g,axis=2);term=(2*Y[:,None,:]-1)/g
    s=term.sum(axis=2);u=s*s-(term*term).sum(axis=2)
    return Y,f,f*s,f*u

def stats(X,mu,a,c,data=None,full=False):
    if data is None:data=fixed_likelihood(X,a,c)
    Y,f,f1,f2=data
    W=f*mu[None,:];p=W.sum(axis=1);p1=f1@mu;p2=f2@mu
    if not np.all(p>0):raise ArithmeticError('Underflowed floating output atom')
    r=W@X/p[:,None];h1=(f1*mu[None,:])@X;h2=(f2*mu[None,:])@X
    r1=(h1-p1[:,None]*r)/p[:,None]
    r2=(h2-p2[:,None]*r-2*p1[:,None]*r1)/p[:,None]
    q=mu@X;D=np.sum((1-q)/(a*(1-a))+q/((a+c)*(1-a-c)))
    F=np.sum(p1*p1/p);A=-np.dot(p2,np.log(p));I2=A+D-F;H2=A-F
    e=np.where(Y>0,c/(a*(a+c)),c/((1-a)*(1-a-c)))
    psi=float(np.sum(p[:,None]*e*e*r*(1-r)))
    M=float(np.sum(p[:,None]*r*(1-r)))
    fm=np.sum(1/((a+c*q)*(1-a-c*q)))
    theta=np.log((a+c)*(1-a)/(a*(1-a-c)))
    kap=min(1/np.sqrt(1-c**4),theta/(-np.expm1(-theta)),2 if c*c<=23/25 else np.inf)
    d=r-q[None,:]
    Q2=float(np.sum(p2*np.sum(d*d,axis=1)/2+2*p1*np.sum(d*r1,axis=1)
                    +p*(np.sum(r1*r1,axis=1)+np.sum(d*r2,axis=1))))
    result=dict(n=X.shape[1],mean_density=float(q.mean()),a=a,c=c,entropy_second=float(H2),
                information_second=float(I2),acceleration=float(A),complete_Fisher=float(D),
                actual_output_Fisher=float(F),missing_Fisher=float(D-F),diagonal_score_uncertainty=psi,
                completed_information_upper=float(kap*psi),explicit_entropy_upper=float((kap-1)*D-kap*fm),
                posterior_MMSE=M,instantaneous_Q_second=Q2,kappa=float(kap),
                normalization_jet_residuals=[float(p.sum()-1),float(p1.sum()),float(p2.sum())])
    if full:
        result['posterior_kernel_error']=None
    return result

def gaussian_diagnostic(X,mu,K,a,c,seed=481271,draws=96):
    rng=np.random.default_rng(seed);data=fixed_likelihood(X,a,c)
    initial=stats(X,mu,a,c,data);n=X.shape[1];q=mu@X;V=float(np.sum(q*(1-q)))
    results=[];field_kernel_errors=[]
    for T in [0.25,2.0,8.0]:
        vals=[];mm=[];pis=[]
        for _ in range(draws):
            ind=rng.choice(len(mu),p=mu);z=T*X[ind]+np.sqrt(T)*rng.normal(size=n)
            logfield=z-T/2
            lw=X@logfield
            lw-=lw.max();pi=mu*np.exp(lw);pi/=pi.sum()
            st=stats(X,pi,a,c,data);vals.append(st['information_second']);mm.append(st['posterior_MMSE'])
            # Independent matrix tilt check against enumerated Gaussian posterior marginals.
            dv=np.exp(logfield);sq=np.sqrt(dv)
            KD=(sq[:,None]*(K@np.linalg.inv(np.eye(n)+(dv[:,None]-1)*K)))*sq[None,:]
            field_kernel_errors.append(float(np.max(np.abs(np.diag(KD)-pi@X))))
        tau=min(a*(a+c),(1-a)*(1-a-c))
        bound=initial['kappa']*c*c/(tau*tau)*min(V,0.5*np.sqrt(n*V)*np.exp(-T/8))
        vals=np.array(vals);mean=float(vals.mean());se=float(vals.std(ddof=1)/np.sqrt(draws))
        results.append(dict(T=T,draws=draws,conditional_information_second_sample_mean=mean,
                            sample_standard_error=se,gaussian_information_second_estimate=initial['information_second']-mean,
                            theorem_remainder_upper=float(bound),posterior_MMSE_sample_mean=float(np.mean(mm))))
    return dict(assurance='Monte Carlo diagnostics only; not interval-certified and not a proof.',seed=seed,
                initial=initial,results=results,maximum_matrix_tilt_marginal_error=max(field_kernel_errors))

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out-dir',type=Path,default=ROOT/'output'/'floating_run')
    args=ap.parse_args();out=safe_output(args.out_dir,ROOT)
    direct=[]
    for n,k,a,c in [(8,4,.025,.95),(10,5,.0125,.95),(10,3,.025,.95),(8,4,.005,.99)]:
        X,mu,K=fourier_law(n,k);row=stats(X,mu,a,c)
        row.update(input=f'true_contiguous_P_{n}_{k}',min_kernel_eigen=float(np.linalg.eigvalsh(K).min()))
        direct.append(row)
    q_specs=[(6,.5,.025,.95),(6,.2,.0125,.95),(4,.01,.01025,.959)]
    for n,rho,a,c in q_specs:
        X,mu,K,checks=toeplitz_law(n,rho);row=stats(X,mu,a,c)
        row.update(input=f'true_Q_{n}_rho_{rho}',atom_diagnostics=checks);direct.append(row)
    X,mu,K=fourier_law(4,2);gauss1=gaussian_diagnostic(X,mu,K,.025,.95)
    X,mu,K,_=toeplitz_law(6,.5);gauss2=gaussian_diagnostic(X,mu,K,.0125,.95,seed=481272,draws=64)
    # This non-DPP input is only an exclusion/falsification gate, not a theorem fixture.
    X=np.array([[1,1,0,0,0],[0,0,1,1,0]],dtype=float);mu=np.array([.5,.5])
    non=stats(X,mu,.025,.95);non['scope']='Non-DPP: positive covariance 1/4 for sites 0,1; no theorem claimed.'
    obj=dict(assurance='All numbers in this file are floating diagnostics only. No analytic theorem depends on them.',
             numpy_version=np.__version__,direct=direct,gaussian=[gauss1,gauss2],non_DPP_gate=non)
    with (out/'floating_diagnostics.json').open('w',encoding='utf-8',newline='\n') as f:
        json.dump(obj,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
    print('WROTE optional floating Fourier/Toeplitz/Gaussian diagnostics')
if __name__=='__main__':main()
