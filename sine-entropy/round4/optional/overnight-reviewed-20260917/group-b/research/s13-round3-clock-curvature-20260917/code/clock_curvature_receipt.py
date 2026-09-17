#!/usr/bin/env python3
"""Deterministic numerical receipt for the S13 corrected-clock theorem.

The proof is analytic. This script evaluates exact finite-n overlap sums,
the exact adjacent-pair marginal, the slice mLSI lower bound, and the resulting
clock-curvature contribution. Floating values are diagnostics, not proof.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np
from scipy.special import gammaln


def logsumexp(a: np.ndarray) -> float:
    m=float(np.max(a)); return m+math.log(float(np.exp(a-m).sum()))

def logbinom(n: int, j: np.ndarray) -> np.ndarray:
    return gammaln(n+1)-gammaln(j+1)-gammaln(n-j+1)

def overlap(n:int,l:int,z:float):
    k=n//2
    r=min(l,n-l)
    js=np.arange(max(0,r-k),min(k,r)+1,dtype=float)
    logs=logbinom(k,js)+logbinom(k,r-js)+js*math.log(z)
    logZ=logsumexp(logs); p=np.exp(logs-logZ)
    mean=float(p@js); centered=js-mean
    var=float(p@(centered**2)); mu3=float(p@(centered**3))
    lam=(2*mean-r)/r
    theta=lam*lam+(4*(n-1)*var-r*(n-r)*(1-lam*lam))/(n*r*(r-1))
    return r,lam,theta,var,mu3,mean

def dlogtheta(n:int,l:int,z:float)->float:
    k=n//2; r=min(l,n-l)
    _,_,theta,_,_,meanZ=overlap(n,l,z)
    js=np.arange(max(0,r-2-(k-2)),min(k-2,r-2)+1,dtype=float)
    logs=logbinom(k-2,js)+logbinom(k-2,r-2-js)+js*math.log(z)
    logB=logsumexp(logs); p=np.exp(logs-logB); meanB=float(p@js)
    return 2/(z-1)+(meanB-meanZ)/z

def pair_quantities(n:int,l:int,c:float,theta:float):
    k=n//2; r=min(l,n-l); x=r/n
    alpha=r*(r-1)/(k*(k-1))
    b=1/(n*n*math.sin(math.pi/n)**2)-1/(4*(n-1))
    delta=theta*alpha*b
    s=r*(r-1)/(n*(n-1))
    probs=[s-delta, x-s+delta, x-s+delta, 1-2*x+s-delta]
    H=-sum(p*math.log(p) for p in probs if p>0)
    K_lower=gammaln(n+1)-gammaln(r+1)-gammaln(n-r+1)-n*H/2
    I_lower=(n+2)/(2*r*(n-r))*K_lower
    return {'x':x,'alpha':alpha,'b_n':b,'delta':delta,'pair_probs':probs,
            'pair_entropy':H,'K_pair_lower':K_lower,'K_pair_lower_over_n':K_lower/n,
            'I_mlsi_lower':I_lower}

def run(out:Path):
    c=19/20
    z=((1+c)/(1-c))**2
    z2=32*c/(1-c)**4
    d=c*c/math.pi**2
    pm=0.25-d; pp=0.25+d
    J=math.log(2)+pm*math.log(pm)+pp*math.log(pp)
    Dpair=2*J
    Gamma=2*Dpair/(1-c*c)
    rows=[]
    for n in [50,100,200,400,800,1600,3200,6400]:
        l=n//2
        r,lam,theta,var,mu3,mean=overlap(n,l,z)
        dl=dlogtheta(n,l,z)
        gamma2=2*(n-1)/(l*(n-l))
        minus_tau2_over_n=z2*dl/(n*gamma2)
        pq=pair_quantities(n,l,c,theta)
        product=minus_tau2_over_n*pq['I_mlsi_lower']
        rows.append({'n':n,'l':l,'lambda':lam,'theta':theta,'var_over_n':var/n,
                     'third_central_scaled':mu3/(n**1.5),'dlogtheta_dz':dl,
                     'minus_tau_second_over_n':minus_tau2_over_n,
                     'pair':pq,'certified_layer_product_lower_over_n':product})
    data={'classification':'floating deterministic diagnostics; analytic proof in proof.md',
          'c':'19/20','z_star':z,'z_second':z2,
          'limits':{'lambda':c,'theta':c*c,'variance_over_n':(1-c*c)/16,
                    'minus_tau_second_over_n':2/(1-c*c),
                    'd_pair':d,'J_pair_entropy_deficit_per_site':J,
                    'D_pair':Dpair,'aggregate_clock_lower_coefficient':Gamma},
          'rows':rows}
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args();run(args.output)
