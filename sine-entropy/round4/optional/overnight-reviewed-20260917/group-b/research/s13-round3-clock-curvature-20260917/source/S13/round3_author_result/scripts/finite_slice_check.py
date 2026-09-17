#!/usr/bin/env python3
"""Finite direct checks for the corrected-clock identities.

Enumerates the half-density Fourier DPP and Johnson slice for small even n.
These checks are regression evidence only; the growing theorem is analytic.
"""
from __future__ import annotations
import argparse,itertools,json,math
from pathlib import Path
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import expm_multiply
from scipy.special import gammaln


def states(n,l): return [sum(1<<i for i in C) for C in itertools.combinations(range(n),l)]
def Pmat(n):
    k=n//2; x=np.arange(n)[:,None]; y=np.arange(k)[None,:]
    U=np.exp(2j*np.pi*x*y/n)/math.sqrt(n); return U@U.conj().T

def qmax(n,l,P):
    k=n//2; sts=states(n,l)
    if l>k:
        small_st=states(n,n-l); small=qmax(n,n-l,P); mp=dict(zip(small_st,small)); full=(1<<n)-1
        return np.array([mp[full^s] for s in sts])
    den=math.comb(k,l); q=[]
    for s in sts:
        I=[i for i in range(n) if s>>i&1]
        q.append((1.0 if l==0 else max(0.0,float(np.linalg.det(P[np.ix_(I,I)]).real)))/den)
    q=np.array(q); return q/q.sum()

def gen(n,l,sts):
    idx={s:i for i,s in enumerate(sts)}; rr=[];cc=[];vv=[]; rate=1/(l*(n-l))
    for a,s in enumerate(sts):
        rr.append(a);cc.append(a);vv.append(-1.)
        for i in range(n):
            if not(s>>i&1):continue
            for j in range(n):
                if s>>j&1:continue
                rr.append(a);cc.append(idx[s^(1<<i)^(1<<j)]);vv.append(rate)
    return csr_matrix((vv,(rr,cc)),shape=(len(sts),len(sts)))

def overlap(n,l,z):
    k=n//2; r=min(l,n-l); js=np.arange(max(0,r-k),min(k,r)+1,dtype=float)
    logs=(gammaln(k+1)-gammaln(js+1)-gammaln(k-js+1)+gammaln(k+1)-gammaln(r-js+1)-gammaln(k-r+js+1)+js*math.log(z))
    m=logs.max(); p=np.exp(logs-m);p/=p.sum(); mu=float(p@js);var=float(p@((js-mu)**2))
    lam=(2*mu-r)/r
    theta=lam*lam+(4*(n-1)*var-r*(n-r)*(1-lam*lam))/(n*r*(r-1))
    return theta

def dlogtheta(n,l,z):
    k=n//2;r=min(l,n-l)
    def mean(ka,kb,total):
        js=np.arange(max(0,total-kb),min(ka,total)+1,dtype=float)
        logs=(gammaln(ka+1)-gammaln(js+1)-gammaln(ka-js+1)+gammaln(kb+1)-gammaln(total-js+1)-gammaln(kb-total+js+1)+js*math.log(z))
        mm=logs.max();p=np.exp(logs-mm);p/=p.sum();return float(p@js)
    return 2/(z-1)+(mean(k-2,k-2,r-2)-mean(k,k,r))/z

def check_case(n,c):
    k=n//2;l=k;z=((1+c)/(1-c))**2;zpp=32*c/(1-c)**4
    theta=overlap(n,l,z);gamma=2*(n-1)/(l*(n-l));tau=-math.log(theta)/gamma
    sts=states(n,l);P=Pmat(n);q0=qmax(n,l,P);L=gen(n,l,sts);q=expm_multiply(tau*L.T,q0);q=np.maximum(q,0);q/=q.sum();u=1/len(sts);r=q/u
    K=float(np.sum(q*np.log(r)))
    Lr=L@r
    I=float(-u*np.dot(Lr,np.log(r)))
    mlsi_rhs=2*l*(n-l)/(n+2)*I
    # adjacent pair direct
    direct=sum(qi for s,qi in zip(sts,q) if (s&1) and (s&2))
    alpha=l*(l-1)/(k*(k-1));b=1/(n*n*math.sin(math.pi/n)**2)-1/(4*(n-1));uniform=l*(l-1)/(n*(n-1))
    formula=uniform-theta*alpha*b
    # derivative K_t=-I via centered difference
    h=1e-5
    qm=expm_multiply((tau-h)*L.T,q0);qp=expm_multiply((tau+h)*L.T,q0)
    Km=float(np.sum(qm*np.log(qm/u)));Kp=float(np.sum(qp*np.log(qp/u)));Kd=(Kp-Km)/(2*h)
    mtau2=zpp*dlogtheta(n,l,z)/gamma
    return {'n':n,'states':len(sts),'theta':theta,'tau':tau,'K':K,'entropy_production':I,
      'mlsi_rhs':mlsi_rhs,'mlsi_slack':mlsi_rhs-K,'K_time_derivative_fd':Kd,'Kprime_plus_I':Kd+I,
      'adjacent_pair_direct':direct,'adjacent_pair_formula':formula,'pair_error':direct-formula,
      'minus_tau_second':mtau2,'clock_component_layer':mtau2*I}

def run(out):
    data={'classification':'small-n direct regression only','c':0.95,'rows':[check_case(n,.95) for n in (6,8,10,12)]}
    data['passes']=all(r['mlsi_slack']>-1e-10 and abs(r['Kprime_plus_I'])<1e-7 and abs(r['pair_error'])<1e-10 and r['minus_tau_second']>0 for r in data['rows'])
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();run(a.output)
