"""Floating independent-channel jets; diagnostics only.
Input projection probabilities are all physical-coordinate squared minors.
No spectral Shannon entropy or probability clipping is used.
"""
from __future__ import annotations
from itertools import combinations
import numpy as np
from float_engine import words,prod_center

def projection_law(U):
    n,r=U.shape
    err=np.max(np.abs(U.conj().T@U-np.eye(r)))
    if err>1e-10:raise FloatingPointError('nonorthonormal frame')
    subsets=np.array(list(combinations(range(n),r)),dtype=np.int64)
    p=np.zeros(1<<n)
    det=np.linalg.det(U[subsets,:]); masses=np.abs(det)**2
    masks=np.sum(1<<subsets,axis=1);p[masks]=masses
    if abs(p.sum()-1)>1e-10:raise FloatingPointError('projection input law normalization')
    return p

def apply_matrix(x,T,bit):
    z=x.reshape(-1,2,1<<bit)
    return np.einsum('ij,bjk->bik',T,z).reshape(-1)

def channel_jets(p,n,a,c,speed=1.):
    if not 0<a<a+c<1:raise FloatingPointError('non-strict channel parameters')
    T=np.array([[1-a,1-a-c],[a,a+c]])
    B=speed*np.array([[-1.,-1.],[1.,1.]])
    dp=np.zeros_like(p);pp=np.zeros_like(p);p=p.copy()
    for bit in range(n):
        new=apply_matrix(p,T,bit)
        new1=apply_matrix(dp,T,bit)+apply_matrix(p,B,bit)
        new2=apply_matrix(pp,T,bit)+2*apply_matrix(dp,B,bit)
        p,dp,pp=new,new1,new2
    if np.any(p<=0) or not np.isfinite([p,dp,pp]).all():raise FloatingPointError('invalid output atom/jet')
    return p,dp,pp

def evaluate_source(p,n,a,c,u=1,center=None):
    if center is None:center=n//2
    an=(1-u)/2+u*a;cn=u*c
    out,dp,pp=channel_jets(p,n,an,cn,u)
    F=float(np.sum(dp**2/out));A=float(-np.sum(pp*np.log(out)))
    I=prod_center(out,dp,pp,n,center)
    m=float(out @ words(n)[:,center])
    I['excess_d2']=I['d2']-u*u/(2*m*m*(1-m)*(1-m))
    return {'I':I,'H':float(-np.sum(out*np.log(out))),'H2':A-F,'H_F':F,'H_A':A,
            'pmin':float(out.min()),'marginal':m,'normalizations':[float(out.sum()),float(dp.sum()),float(pp.sum())]}
