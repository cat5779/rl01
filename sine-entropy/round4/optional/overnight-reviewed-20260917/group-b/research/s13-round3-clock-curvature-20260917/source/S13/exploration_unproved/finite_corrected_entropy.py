#!/usr/bin/env python3
import itertools, math, argparse, json
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import expm_multiply
from scipy.special import gammaln


def states_of_size(n,l):
    return [sum(1<<i for i in comb) for comb in itertools.combinations(range(n),l)]

def fourier_projection(n,k):
    j=np.arange(n)[:,None]; r=np.arange(k)[None,:]
    U=np.exp(2j*np.pi*j*r/n)/math.sqrt(n)
    return U@U.conj().T

def qmax_probs(n,l,P):
    k=n//2
    if l>k:
        small=qmax_probs(n,n-l,P)
        states_small=states_of_size(n,n-l)
        mp={s:p for s,p in zip(states_small,small)}
        full=(1<<n)-1
        states=states_of_size(n,l)
        return np.array([mp[full^s] for s in states],float)
    states=states_of_size(n,l)
    den=math.comb(k,l)
    out=[]
    for s in states:
        inds=[i for i in range(n) if (s>>i)&1]
        if l==0: det=1.0
        else: det=float(np.linalg.det(P[np.ix_(inds,inds)]).real)
        out.append(max(det,0.0)/den)
    out=np.array(out)
    out/=out.sum()
    return out

def generator(n,l,states):
    idx={s:i for i,s in enumerate(states)}
    rows=[]; cols=[]; vals=[]
    rate=1.0/(l*(n-l)) if 0<l<n else 0.0
    for ii,s in enumerate(states):
        if rate==0: rows.append(ii); cols.append(ii); vals.append(0.0); continue
        occ=[i for i in range(n) if (s>>i)&1]
        emp=[j for j in range(n) if not ((s>>j)&1)]
        rows.append(ii); cols.append(ii); vals.append(-1.0)
        for i in occ:
            for j in emp:
                t=s^(1<<i)^(1<<j)
                rows.append(ii); cols.append(idx[t]); vals.append(rate)
    return csr_matrix((vals,(rows,cols)),shape=(len(states),len(states)))

def layer_mult(n,l,z):
    k=n//2
    if l>k: return layer_mult(n,n-l,z)
    js=np.arange(max(0,l-k),min(k,l)+1,dtype=float)
    logs=(gammaln(k+1)-gammaln(js+1)-gammaln(k-js+1)
          +gammaln(k+1)-gammaln(l-js+1)-gammaln(k-l+js+1)+js*math.log(z))
    mm=np.max(logs); p=np.exp(logs-mm); p/=p.sum()
    mean=float(p@js); var=float(p@((js-mean)**2))
    lam=(2*mean-l)/l if l else 0
    if l<2: theta=1.0
    else: theta=lam*lam+(4*(n-1)*var-l*(n-l)*(1-lam*lam))/(n*l*(l-1))
    return lam,theta,var

def corrected_K(n,l,c,P):
    if l in (0,n): return 0.0,0.0,1.0
    a=(1-c)/2; z=((1+c)/(1-c))**2
    lam,theta,var=layer_mult(n,l,z)
    if l in (1,n-1):
        tau=0.0
    else:
        gamma2=2*(n-1)/(l*(n-l))
        tau=-math.log(theta)/gamma2
    states=states_of_size(n,l)
    q0=qmax_probs(n,l,P)
    if tau>0:
        L=generator(n,l,states)
        q=expm_multiply(tau*L.T,q0)
    else: q=q0
    q=np.maximum(q,0); q/=q.sum()
    K=float(np.sum(q*np.log(q*len(q))))
    return K,tau,theta

def count_pmf(n,c):
    k=n//2; p=(1+c)/2; q=(1-c)/2
    a=np.array([math.comb(k,j)*p**j*(1-p)**(k-j) for j in range(k+1)])
    b=np.array([math.comb(k,j)*q**j*(1-q)**(k-j) for j in range(k+1)])
    return np.convolve(a,b)

def pi_second(n,c):
    # exact product differentiation: 2 sum pairs distributions shifted by +2,+1,+0 finite differences
    k=n//2; p=(1+c)/2; q=(1-c)/2
    out=np.zeros(n+1)
    # polynomial derivative directly via convolution with derivative factors for robust simplicity
    # each of k high and k low factors is (1-p)+p t, derivative wrt a = t-1.
    # second derivative: 2 sum_{pairs}(t-1)^2 product others
    def binpmf(m,r):
        return np.array([math.comb(m,j)*r**j*(1-r)**(m-j) for j in range(m+1)])
    poly=np.array([1.,-2.,1.]) # (1-t)^2 same as (t-1)^2 coefficients ascending
    components=[]
    for nh,nl,mult in [(k-2,k,2*math.comb(k,2)),(k-1,k-1,2*k*k),(k,k-2,2*math.comb(k,2))]:
        base=np.convolve(binpmf(nh,p),binpmf(nl,q))
        comp=np.convolve(base,poly)*mult
        components.append(comp)
    for comp in components: out[:len(comp)]+=comp
    return out

def run(ns,c):
    rows=[]
    for n in ns:
        k=n//2; P=fourier_projection(n,k)
        Ks=[]; taus=[]; th=[]
        for l in range(n+1):
            print('n',n,'l',l,flush=True)
            K,t,theta=corrected_K(n,l,c,P)
            Ks.append(K);taus.append(t);th.append(theta)
        Ks=np.array(Ks); pis=count_pmf(n,c); pi2=pi_second(n,c)
        W=float(pi2@Ks)
        # finite cusp second diff at center
        cusp=Ks[k-1]-2*Ks[k]+Ks[k+1]
        rows.append({'n':n,'Ks':Ks.tolist(),'taus':taus,'thetas':th,'W':W,'W_over_n':W/n,'W_over_n32':W/(n**1.5),'center_second_diff':float(cusp),'center_left_slope':float(Ks[k]-Ks[k-1]),'count_center':float(pis[k])})
    return rows

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--ns',nargs='+',type=int,default=[8,10,12,14]);ap.add_argument('--c',type=float,default=.95);ap.add_argument('--out',required=True)
    args=ap.parse_args(); data=run(args.ns,args.c)
    open(args.out,'w').write(json.dumps(data,indent=2))
