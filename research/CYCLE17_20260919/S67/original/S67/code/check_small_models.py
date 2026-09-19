#!/usr/bin/env python3
"""Floating-point adversarial consistency checks, NOT interval certificates.
Checks the actual-law chord identity, the signed leakage identity, the new
uniform bound, and weighted signed-inverse norms. No KL growth enumeration.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss

BREF=0.025
C=0.95
S=BREF*(1-BREF)

def kernel(n:int,a:float)->np.ndarray:
    i=np.arange(n); d=i[:,None]-i[None,:]
    Q=np.empty((n,n),float)
    np.divide(np.sin(np.pi*d/2),np.pi*d,out=Q,where=d!=0)
    np.fill_diagonal(Q,.5)
    return a*np.eye(n)+C*Q

def law(n:int,a:float):
    K=kernel(n,a)
    bits=((np.arange(1<<n)[:,None]>>np.arange(n))&1).astype(float)
    M=np.broadcast_to(K,(1<<n,n,n)).copy()
    ix=np.arange(n);M[:,ix,ix]-=1-bits
    p=np.linalg.det(M)*((-1.)**np.sum(1-bits,axis=1))
    assert np.all(p>0) and abs(p.sum()-1)<1e-10
    return p,np.linalg.inv(M),bits,K

def pair_mass(K:np.ndarray,a:float):
    n=K.shape[0]; total=0.; maxratio=0.
    Ka=K+(a-BREF)*np.eye(n)
    for i in range(n):
      for j in range(i+1,n):
        ids=[i,j];ext=[k for k in range(n) if k not in ids]
        for m in range(1<<len(ext)):
          bits=np.array([(m>>r)&1 for r in range(len(ext))])
          if ext:
            Mb=K[np.ix_(ext,ext)]-np.diag(1-bits)
            Ma=Ka[np.ix_(ext,ext)]-np.diag(1-bits)
            p=np.linalg.det(Ma)*((-1.)**np.sum(1-bits))
            T=K[np.ix_(ids,ids)]-K[np.ix_(ids,ext)]@np.linalg.solve(Mb,K[np.ix_(ext,ids)])
          else:
            p=1.;T=K[np.ix_(ids,ids)]
          u,v,z=T[0,0],T[1,1],T[0,1];t=z*z
          q=np.array([u*v-t,u*(1-v)+t,(1-u)*v+t,(1-u)*(1-v)-t])
          J=np.log(q[1]*q[2]/(q[0]*q[3]));W=t*np.sum(1/q)
          total+=p*J
          if W>1e-18:maxratio=max(maxratio,J/W)
    return total,maxratio

def R(a):
    return (1-a)/(39*a) if a<=BREF else (a+C)/(39*(1-a-C))

def integrate(f):
    nodes,weights=leggauss(8)
    ans=0.
    for lo,hi in ((.02,.025),(.025,.03)):
      for x,w in zip(nodes,weights):
        a=(lo+hi)/2+(hi-lo)*x/2
        G=.5*(a-.02) if a<=.025 else .5*(.03-a)
        ans+=(hi-lo)/2*w*G*f(a)
    return ans

def main():
    rows=[]
    for n in (1,2,3,4,6):
        pb,B,bits,K=law(n,BREF)
        p0,_,_,_=law(n,.02);p1,_,_,_=law(n,.03)
        lpb=np.log(pb)
        Cn=float(pb@lpb-.5*(p0@lpb+p1@lpb))
        mass=2*integrate(lambda a:pair_mass(K,a)[0])
        assert abs(Cn-mass)<2e-11
        Q=(K-BREF*np.eye(n))/C;E=Q-Q@Q
        max_res=0.
        for BB,xx in zip(B,bits):
            SS=np.diag(2*xx-1)
            res=S*(BB@BB)+C*C*BB@E@BB-(SS@BB+BB@SS)/2+np.eye(n)
            max_res=max(max_res,float(np.linalg.norm(res,ord=2)))
        assert max_res<1e-10
        bound=1.5*integrate(lambda a:R(a)**3/S-4*R(a))
        assert Cn/n<=bound+1e-12
        maxratio=pair_mass(K,BREF)[1]
        assert maxratio<=1.5+1e-12
        rows.append({'n':n,'C_n_over_n':Cn/n,'Green_identity_error':Cn-mass,
                     'max_leakage_identity_residual':max_res,
                     'max_conditional_J_over_W':maxratio,'uniform_upper_bound':bound})
    rng=np.random.default_rng(670019)
    locality=[]
    for n in (8,16,32,64,128):
        K=kernel(n,BREF)
        for _ in range(3):
            bits=rng.integers(0,2,n)
            B=np.linalg.inv(K-np.diag(1-bits))
            center=n//2;ww=(1+np.abs(np.arange(n)-center))**.001
            weighted_norm=float(np.linalg.norm(ww[:,None]*B/ww[None,:],2))
            assert weighted_norm<80
            locality.append({'n':n,'weighted_inverse_norm':weighted_norm})
    output={'status':'PASS: floating-point consistency checks only',
            'warning':'These do not replace the analytic proofs or Arb sign certificates.',
            'small_full_law_checks':rows,'weighted_inverse_checks':locality}
    target=Path(__file__).resolve().parents[1]/'certificates'/'small_model_float_checks.json'
    target.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))
if __name__=='__main__':main()
