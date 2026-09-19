#!/usr/bin/env python3
"""High-precision actual sine-DPP probability recursion and distance profiles.

Cached .npy files are float64 probabilities generated with 70/80-digit mpmath;
these are diagnostics, not interval-certified probabilities. No clipping.
"""
from __future__ import annotations
import argparse,json,math,time
from pathlib import Path
from itertools import combinations
import numpy as np
import mpmath as mp

def mp_sine(n,rho):
    rho=mp.mpf(str(rho))
    def entry(i,j):
        d=i-j
        if d==0:return rho
        # exact zeros at half density
        if rho==mp.mpf('.5') and d%2==0:return mp.mpf(0)
        return mp.sin(mp.pi*rho*d)/(mp.pi*d)
    return [[entry(i,j) for j in range(n)] for i in range(n)]

def allprob_recursive(K):
    n=len(K);out=[mp.mpf(0)]*(1<<n)
    def visit(M,depth,mask,weight):
        k=len(M)
        if k==0:out[mask]=weight;return
        q=M[0][0]
        if not (0<q<1):raise ArithmeticError(('non-interior conditional',depth,q))
        if k==1:
            out[mask]=weight*(1-q);out[mask|(1<<depth)]=weight*q;return
        b=M[0][1:];base=[r[1:] for r in M[1:]]
        bb=[[b[i]*b[j] for j in range(k-1)] for i in range(k-1)]
        zero=[[base[i][j]+bb[i][j]/(1-q) for j in range(k-1)] for i in range(k-1)]
        one=[[base[i][j]-bb[i][j]/q for j in range(k-1)] for i in range(k-1)]
        visit(zero,depth+1,mask,weight*(1-q))
        visit(one,depth+1,mask|(1<<depth),weight*q)
    visit(K,0,0,mp.mpf(1))
    return out

def metrics(P,n,details=False):
    if np.min(P)<=0:raise ValueError(('nonpositive',np.min(P)))
    ids=np.arange(1<<n);diag=0.;score=np.zeros_like(P);accel=np.zeros_like(P)
    for i in range(n):
        lo=ids[(ids&(1<<i))==0];hi=lo|(1<<i);a=P[lo];b=P[hi];m=a+b
        diag+=np.sum(m*m*(1/a+1/b))
        score[lo]-=m;score[hi]+=m
    pair_sum=0.;ell_sum=0.;edge_sum=0.;pos_mass=0.;pos_pay=0.;neg_pay=0.
    per_pair=[];profile={d:0. for d in range(1,n)}
    max_pair=-np.inf;min_pair=np.inf;max_local=-np.inf;witness=None
    for i,j in combinations(range(n),2):
        base=ids[((ids&(1<<i))==0)&((ids&(1<<j))==0)]
        inds=[base,base|(1<<i),base|(1<<j),base|(1<<i)|(1<<j)]
        cells=np.array([P[v] for v in inds]);m=cells.sum(axis=0);q=cells/m
        a,b,c,d=q;delta=b*c-a*d
        ell=np.log(b)+np.log(c)-np.log(a)-np.log(d)
        edge=delta*(1/a+1/b+1/c+1/d)
        skew=ell-edge;val=2*float(np.dot(m,skew))
        pair_sum+=val;ell_sum+=2*float(np.dot(m,ell));edge_sum+=2*float(np.dot(m,edge))
        pos_mass+=float(m[skew>0].sum());pos_pay+=2*float(np.dot(m,np.maximum(skew,0)));neg_pay+=2*float(np.dot(m,np.minimum(skew,0)))
        profile[j-i]+=val/n
        max_pair=max(max_pair,val);min_pair=min(min_pair,val)
        if skew.max()>max_local:
            k=int(skew.argmax());max_local=float(skew[k]);witness={'i':i,'j':j,'outside_zeroed_index':int(base[k]),'q00_q10_q01_q11':q[:,k].tolist(),'outside_mass':float(m[k]),'skew':float(skew[k])}
        for t,s in zip(inds,[1,-1,-1,1]):accel[t]+=2*s*m
        if details:per_pair.append({'i':i,'j':j,'Jpp':val,'Eell':float(np.dot(m,ell)),'Eedge':float(np.dot(m,edge))})
    direct=-np.dot(accel,np.log(P))-np.dot(score,score/P)
    out={'n':n,'sum_prob':float(P.sum()),'min_atom':float(P.min()),'D_per_n':diag/n,'pair_per_n':pair_sum/n,'L_per_n':(pair_sum-diag)/n,'direct_L_per_n':float(direct)/n,'decomp_error':float(direct-(pair_sum-diag)),'ell_directed_per_n':ell_sum/n,'edge_directed_per_n':edge_sum/n,'max_pair_Jpp':max_pair,'min_pair_Jpp':min_pair,'positive_skew_mass_sum':pos_mass,'positive_skew_payment_per_n':pos_pay/n,'negative_skew_payment_per_n':neg_pay/n,'max_local_skew':max_local,'witness':witness,'distance_profile':profile}
    if details:out['pairs']=per_pair
    return out

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--rho',default='0.5')
    parser.add_argument('--ns',default='2,4,6,8,10,12')
    parser.add_argument('--dps',type=int,default=80)
    parser.add_argument('--cached',action='store_true',help='read provided float64 probability files')
    parser.add_argument('--save-probabilities',action='store_true')
    parser.add_argument('--output',default=None)
    args=parser.parse_args();rho=float(args.rho)
    if not 0<rho<1:parser.error('rho must be in (0,1)')
    ns=[int(x) for x in args.ns.split(',')]
    if any(n<2 for n in ns):parser.error('profile requires n>=2')
    if args.dps<30:parser.error('use at least 30 decimal digits')
    root=Path(__file__).resolve().parents[1];mp.mp.dps=args.dps;rows=[]
    for n in ns:
        start=time.monotonic();path=root/'data'/f'P_sine_rho{rho}_n{n}.npy'
        if args.cached:
            if not path.exists():raise FileNotFoundError(path)
            P=np.load(path,allow_pickle=False);method='provided float64 probabilities; actual weighted sums recomputed'
        else:
            raw=allprob_recursive(mp_sine(n,args.rho));P=np.array([float(v) for v in raw]);method='mpmath conditional recursion, then float64 weighted sums'
        if np.min(P)<=0 or abs(float(P.sum())-1)>1e-10:raise ArithmeticError('invalid law; no clipping or renormalization is performed')
        m=metrics(P,n,True);m.update(rho=rho,working_dps=(None if args.cached else args.dps),method=method,elapsed_seconds=time.monotonic()-start)
        rows.append(m)
        if args.save_probabilities:np.save(path,P)
        print('n',n,'D/n',m['D_per_n'],'S/n',m['pair_per_n'],'L/n',m['L_per_n'],flush=True)
    out=Path(args.output) if args.output else root/'results'/'profile_recomputed.json'
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(rows,indent=2))
if __name__=='__main__':main()
