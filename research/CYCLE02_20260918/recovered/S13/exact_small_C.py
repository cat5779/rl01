#!/usr/bin/env python3
from __future__ import annotations
import itertools, math
import numpy as np
from scipy.linalg import expm

c=19/20
a=(1-c)/2
z=((a+c)*(1-a))/(a*(1-a-c))
zpp=32*c/(1-c)**4


def subsets(n,l):
    return list(itertools.combinations(range(n),l))

def projection(n):
    k=n//2
    U=np.exp(2j*np.pi*np.arange(n)[:,None]*np.arange(k)[None,:]/n)/np.sqrt(n)
    return U@U.conj().T

def qmax(n,l,P):
    k=n//2
    states=subsets(n,l)
    if l==0 or l==n:
        return np.ones(1)
    if l<=k:
        vals=np.array([max(0.0,float(np.linalg.det(P[np.ix_(S,S)]).real))/math.comb(k,l) for S in states])
    else:
        m=n-l
        Pc=np.eye(n)-P
        comps=[tuple(i for i in range(n) if i not in set(S)) for S in states]
        vals=np.array([max(0.0,float(np.linalg.det(Pc[np.ix_(T,T)]).real))/math.comb(k,m) for T in comps])
    vals/=vals.sum()
    return vals

def Gmatrix(n,l):
    states=subsets(n,l); idx={S:i for i,S in enumerate(states)}
    N=len(states); G=np.zeros((N,N))
    for ii,S in enumerate(states):
        SS=set(S)
        for x in S:
            for y in range(n):
                if y not in SS:
                    T=tuple(sorted((SS-{x})|{y}))
                    G[ii,idx[T]] += 1
                    G[ii,ii] -= 1
    return G

def theta_stats(k,m,z):
    Z=0.; Zd=0.; A=0.; Ad=0.
    for j in range(m+1):
        w=math.comb(k,j)*math.comb(k,m-j)*z**j
        Z+=w; Zd+=j*w/z
    for j in range(m-1):
        w=math.comb(k-2,j)*math.comb(k-2,m-2-j)*z**j
        A+=w; Ad+=j*w/z
    alpha=m*(m-1)/(k*(k-1))
    th=(z-1)**2*A/(alpha*Z)
    dlog=2/(z-1)+Ad/A-Zd/Z
    return th,dlog

def count_probs(n):
    k=n//2; p=a+c; q=a
    arr=np.array([1.0])
    for prob in [p]*k+[q]*k:
        arr=np.convolve(arr,[1-prob,prob])
    return arr

def calc(n):
    k=n//2; P=projection(n); pis=count_probs(n); C=0.
    rows=[]
    for l in range(n+1):
        if l in (0,1,n-1,n):
            rows.append((l,0,0,0,0)); continue
        m=min(l,n-l)
        th,dlog=theta_stats(k,m,z)
        s=-math.log(th)/(2*(n-1))
        q0=qmax(n,l,P)
        G=Gmatrix(n,l)
        qt=q0@expm(s*G)
        N=len(qt); f=qt*N
        Gf=G@f
        IG=-np.mean(Gf*np.log(f))
        # depending row/col symmetry G is symmetric, okay
        minus_spp=zpp/(2*(n-1))*dlog
        term=pis[l]*minus_spp*IG
        C+=term
        rows.append((l,th,s,IG,term))
    return C,rows

for n in [4,6,8,10]:
    Cn,rows=calc(n)
    print('n',n,'C',Cn,'C/n',Cn/n)
    print(' center',rows[n//2])
