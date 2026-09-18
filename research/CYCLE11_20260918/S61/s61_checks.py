#!/usr/bin/env python3
"""Finite cross-checks for S61 (not independent review or an asymptotic proof).

Requirements: Python 3.10+, numpy, scipy.  Run e.g.
  python s61_checks.py --max-n 16 --radial-max 8192 --out checks

Checks the frozen Fourier spatial laws (not a radial substitute), both deletion
normalizations, the entropy chain rule, exact polynomial identities, latent
mixtures, the heat-overlap moment identities, and a posterior covering coupling.
"""
from __future__ import annotations
import argparse, csv, json, math
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.special import gammaln, logsumexp
from scipy.sparse import coo_matrix, diags
from scipy.sparse.linalg import expm_multiply

XI = F(1, 1520)
Z = 1521.0
C_FIXED = 19/20


def qcoeff(r: int, d: int) -> list[F]:
    a=[F(1)]
    for s in range(1,r+1):
        a.append(a[-1]*F((r-s+1)*(r+2*d+s-2),(d+s-1)*s))
    return a


def peval(a: list[F], x: F) -> F:
    out=F(0)
    for c in reversed(a): out=out*x+c
    return out


def exact_polynomial_checks() -> dict:
    count=0
    for n in range(8,42,2):
        k=n//2
        for l in range(4,k+1):
            d=k-l+1
            q=qcoeff(l,d); qm=qcoeff(l-2,d)
            qc=qcoeff(l-2,d+1)
            for ss in range(l+1):
                lhs=q[ss]-(qm[ss] if ss<len(qm) else F(0))
                rhs=F(2*(n-1),d)*((qc[ss-1] if 0<=ss-1<len(qc) else F(0))+(qc[ss-2] if 0<=ss-2<len(qc) else F(0)))
                assert lhs==rhs,(n,l,ss,'contiguous identity')
            h0=F(n*l*(l-1),4*(n-1))
            for s in range(l+3):
                get=lambda i:q[i] if 0<=i<len(q) else F(0)
                rhs=(h0-k*s)*get(s)+k*(2*l-3*s+3)*get(s-1)+2*k*(l-s+2)*get(s-2)
                lhs=h0*(qm[s] if s<len(qm) else F(0))
                assert lhs==rhs,(n,l,s,lhs,rhs)
            # Independently expand xi^l Z_l((1+xi)/xi).
            for s in range(l+1):
                val=sum(math.comb(k,l-u)*math.comb(k,u)*math.comb(l-u,s-u)
                        for u in range(s+1))
                assert F(val,math.comb(k,l))==q[s]
            count+=1
    return {'cases':count,'arithmetic':'exact rational','passed':True}


def logcomb(n: int, r: np.ndarray) -> np.ndarray:
    return gammaln(n+1)-gammaln(r+1)-gammaln(n-r+1)


def radial(n: int,l: int) -> tuple[dict,np.ndarray,np.ndarray,np.ndarray]:
    k=n//2; cc=l*(n-l); j=np.arange(l+1,dtype=float)
    logmult=logcomb(k,j)+logcomb(k,l-j)
    lw=logmult+j*math.log(Z); lw-=logsumexp(lw)
    w=np.exp(lw); mu=float(w@j); var=float(w@((j-mu)**2))
    h0=n*l*(l-1)/(4*(n-1))
    hh=float(w@((j-l/2)**2))-cc/(4*(n-1))
    theta=hh/h0
    if not 0<theta<1: raise ArithmeticError(('theta',n,l,theta))
    tau=-math.log(theta)*cc/(2*(n-1))
    up=(l-j)*(k-j)/cc
    down=j*(k-l+j)/cc
    generator=diags([up[:-1],-(up+down),down[1:]],[-1,0,1],format='csr')
    initial=np.zeros(l+1);initial[l]=1
    wh=expm_multiply(tau*generator,initial)
    muh=float(wh@j); vh=float(wh@((j-muh)**2))
    expected_mu=l/2*(1+theta**(n/(2*(n-1))))
    expected_v=cc/(4*(n-1))*(1-theta)+l*l/4*(theta-theta**(n/(n-1)))
    lo=cc/(4*Z*(n-1))
    assert var>=lo*(1-1e-6),(n,l,var,lo)
    assert vh>=lo*(1-1e-6),(n,l,vh,lo)
    assert abs(mu-muh)<=1/(2*C_FIXED)+1e-5
    row=dict(n=n,l=l,mean=mu,variance=var,heat_mean=muh,heat_variance=vh,
             mean_difference=mu-muh,theta=theta,tau=tau,
             heat_mass_error=abs(float(wh.sum())-1),
             heat_mean_formula_error=abs(muh-expected_mu),
             heat_variance_formula_error=abs(vh-expected_v),
             variance_lower_bound=lo)
    return row,w,wh,logmult


def subsets(n: int,l: int) -> tuple[list[tuple[int,...]],list[int]]:
    ts=list(combinations(range(n),l))
    return ts,[sum(1<<x for x in t) for t in ts]


def kl(p: np.ndarray,q: np.ndarray) -> float:
    if np.any(q<=0) or np.any(p<0): raise ArithmeticError('Nonpositive mass in KL')
    mask=p>0
    return float(np.sum(p[mask]*(np.log(p[mask])-np.log(q[mask]))))


def fourier(n: int) -> np.ndarray:
    v=np.exp(2j*np.pi*np.arange(n)[:,None]*np.arange(n//2)[None,:]/n)/np.sqrt(n)
    return v@v.conj().T


def determinants(mat: np.ndarray,ts: list[tuple[int,...]]) -> np.ndarray:
    ans=[]
    for t in ts:
        d=np.linalg.det(mat[np.ix_(t,t)])
        if abs(d.imag)>1e-6*max(1,abs(d.real)): raise ArithmeticError(('imaginary determinant',d))
        ans.append(float(d.real))
    ans=np.array(ans)
    if np.any(ans < -1e-12): raise ArithmeticError('Negative determinant')
    return np.maximum(ans,0)


def spatial(n: int,l: int,check_mixture: bool) -> dict:
    k=n//2; cc=l*(n-l)
    ts,masks=subsets(n,l); idx={m:i for i,m in enumerate(masks)}
    pp=fourier(n); lam=39*pp+(np.eye(n)-pp)/39
    p=determinants(lam,ts); p/=p.sum()
    initial=determinants(pp,ts)/math.comb(k,l)
    assert abs(initial.sum()-1)<1e-10
    row,wr,whr,logmult=radial(n,l)
    theta_exact=float(peval(qcoeff(l-2,k-l+1),XI)/peval(qcoeff(l,k-l+1),XI))
    assert abs(theta_exact-row['theta'])<1e-10
    tau=-math.log(theta_exact)*cc/(2*(n-1))
    rr=[];cols=[];vv=[]
    for u,(t,mask) in enumerate(zip(ts,masks)):
        rr.append(u);cols.append(u);vv.append(-1.)
        outside=[x for x in range(n) if not mask>>x&1]
        for i in t:
            for x in outside:
                rr.append(u);cols.append(idx[mask^(1<<i)^(1<<x)]);vv.append(1/cc)
    L=coo_matrix((vv,(rr,cols)),shape=(len(ts),len(ts))).tocsr()
    ph=expm_multiply(tau*L,initial)
    assert np.min(ph)>0 and abs(ph.sum()-1)<1e-10
    ss,smasks=subsets(n,l-1); sidx={s:i for i,s in enumerate(smasks)}
    dp=np.zeros(len(ss));dq=np.zeros(len(ss))
    fibers=[[] for _ in ss]
    for ti,(t,mask) in enumerate(zip(ts,masks)):
        for i in t:
            si=sidx[mask^(1<<i)]
            dp[si]+=p[ti]/l;dq[si]+=ph[ti]/l
            fibers[si].append(ti)
    c_direct=0.; ent=0.;c_per=[]
    for si,fib in enumerate(fibers):
        a=p[fib]/(l*dp[si]);b=ph[fib]/(l*dq[si])
        csi=kl(a,b);c_direct+=dp[si]*csi;c_per.append(csi)
        r=p[fib]/ph[fib];mean=float(b@r)
        ent+=dq[si]*(float(b@(r*np.log(r)))-mean*math.log(mean))
    c_chain=kl(p,ph)-kl(dp,dq)
    assert c_direct>=-1e-12 and abs(c_direct-c_chain)<1e-10
    assert abs(c_direct-ent)<1e-10
    # Density deletion has the distinct normalization n-l+1.
    f=p*math.comb(n,l)
    df=np.array([f[fib].sum()/(n-l+1) for fib in fibers])
    assert np.max(abs(df-dp*math.comb(n,l-1)))<1e-9
    out=dict(n=n,l=l,m=l-1,states=len(ts),C=c_direct,R=kl(p,ph),
             chain_rule_error=abs(c_direct-c_chain),fiber_entropy_error=abs(c_direct-ent),
             prior_mass_error=abs(initial.sum()-1),heat_mass_error=abs(ph.sum()-1),
             max_p_over_phat=float(np.max(p/ph)),max_conditional_KL=float(max(c_per)),
             theta_polynomial_error=abs(theta_exact-row['theta']))
    if check_mixture:
        ats,amasks=subsets(n,k);mu=determinants(pp,ats);mu/=mu.sum()
        # Full sum over the ACTUAL Fourier prior, no uniform replacement.
        mixp=np.zeros_like(p);mixq=np.zeros_like(p);mixtail=np.zeros_like(p)
        tp=wr/np.exp(logmult);th=whr/np.exp(logmult)
        # Also verify the finite posterior-to-fiber bound with an explicit window.
        width=3.5;center=row['heat_mean'];d=3;delta=.2
        tail_ind=np.abs(np.arange(l+1)-center)>width-d
        for ai,amask in enumerate(amasks):
            jj=np.array([(amask&tm).bit_count() for tm in masks])
            mixp+=mu[ai]*tp[jj];mixq+=mu[ai]*th[jj]
            mixtail+=mu[ai]*th[jj]*tail_ind[jj]
        ep=float(np.max(abs(mixp-p)));eq=float(np.max(abs(mixq-ph)))
        assert max(ep,eq)<1e-10,(n,l,ep,eq)
        out['actual_latent_mixture_error']=ep
        out['corrected_latent_mixture_error']=eq
        posterior_tail=mixtail/mixq
        good=posterior_tail<=delta
        eta=float(whr@tail_ind)
        mm=float(np.max(p/ph));pbad=float(p[~good].sum())
        assert pbad<=mm*eta/delta+1e-12
        logh=np.log(whr)-np.log(wr)
        jr=np.arange(l)
        local=(abs(jr-center)<=width)&(abs(jr+1-center)<=width)
        ell_local=float(np.max(abs(np.diff(logh)[local]))) if local.any() else 0.
        log_r=np.log(p/ph)
        max_good_grad=0.
        for a,b in zip(*L.nonzero()):
            if a!=b and good[a] and good[b]:max_good_grad=max(max_good_grad,abs(float(log_r[a]-log_r[b])))
        gradient_bound=3*ell_local-math.log(1-delta)
        assert max_good_grad<=gradient_bound+1e-10
        bad_fiber=np.array([not bool(np.all(good[fib])) for fib in fibers])
        fiber_bad_mass=float(dp[bad_fiber].sum())
        assert fiber_bad_mass<=(1+Z*(n-l))*pbad+1e-10
        pmin_bound=1/(math.comb(n,l)*Z**l)
        hbound=math.log(mm/pmin_bound)
        finite_bound=gradient_bound**2/8+hbound*min(1.,(1+Z*(n-l))*mm*eta/delta)
        assert c_direct<=finite_bound+1e-10
        out['truncated_tool_bound']=finite_bound
        out['good_endpoint_max_gradient']=max_good_grad
        out['good_endpoint_gradient_bound']=gradient_bound
        out['bad_output_mass']=pbad
        out['bad_fiber_mass']=fiber_bad_mass
        # A full-support window makes the deterministic finite lemma directly testable.
        width=l+4.;center=l/2
        ell=float(np.max(abs(np.diff(np.log(whr)-np.log(wr)))))
        finite_bound=(3*ell-math.log(1-delta))**2/8
        assert c_direct<=finite_bound+1e-10
        out['finite_full_window_tool_bound']=finite_bound
    return out


def field_coupling(rho: np.ndarray,masks: list[int],site: int,factor: float) -> tuple[np.ndarray,np.ndarray]:
    present=np.array([bool(m>>site&1) for m in masks])
    pr=float(rho[present].sum())
    target=rho*np.where(present,factor,1.);target/=target.sum()
    nr=float(target[present].sum())
    zeros=np.flatnonzero(~present);ones=np.flatnonzero(present)
    r0=rho[zeros]/(1-pr);r1=rho[ones]/pr
    edges=[]
    for i,a in enumerate(zeros):
        for j,b in enumerate(ones):
            rest=masks[b]^(1<<site)
            if rest&masks[a]==rest:edges.append((i,j))
    ar=[];ac=[];av=[]
    for e,(i,j) in enumerate(edges):
        ar += [i,len(zeros)+j];ac += [e,e];av += [1.,1.]
    Aeq=coo_matrix((av,(ar,ac)),shape=(len(zeros)+len(ones),len(edges))).tocsr()
    sol=linprog(np.zeros(len(edges)),A_eq=Aeq,b_eq=np.r_[r0,r1],bounds=(0,None),method='highs',
                options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
    if not sol.success:raise ArithmeticError(sol.message)
    coupling=np.zeros((len(masks),len(masks)))
    coupling[ones,ones]=min(pr,nr)*r1
    coupling[zeros,zeros]=min(1-pr,1-nr)*r0
    for amount,(i,j) in zip(sol.x,edges):
        if nr>=pr:coupling[zeros[i],ones[j]]+=(nr-pr)*amount
        else:coupling[ones[j],zeros[i]]+=(pr-nr)*amount
    assert np.max(abs(coupling.sum(axis=1)-rho))<1e-8
    assert np.max(abs(coupling.sum(axis=0)-target))<1e-8
    return coupling,target


def posterior_coupling_check() -> dict:
    n=8;k=4;l=4
    ats,masks=subsets(n,k);mu=determinants(fourier(n),ats);mu/=mu.sum()
    tmask=sum(1<<i for i in [0,1,2,3]);tp=tmask^(1<<0)^(1<<7)
    j=np.array([(a&tmask).bit_count() for a in masks])
    jp=np.array([(a&tp).bit_count() for a in masks])
    rho=mu*Z**j;rho/=rho.sum()
    c1,mid=field_coupling(rho,masks,0,1/Z)
    c2,rhop=field_coupling(mid,masks,7,Z)
    glued=(c1/mid[None,:])@c2
    intended=mu*Z**jp;intended/=intended.sum()
    marginal_error=max(float(np.max(abs(glued.sum(axis=1)-rho))),
                       float(np.max(abs(glued.sum(axis=0)-intended))))
    max_j=0;max_swaps=0
    for a,b in zip(*np.nonzero(glued>1e-14)):
        max_j=max(max_j,abs(int(j[a])-int(jp[b])))
        max_swaps=max(max_swaps,(masks[a]^masks[b]).bit_count()//2)
    assert marginal_error<1e-8 and max_j<=3 and max_swaps<=2
    return dict(n=n,l=l,marginal_error=marginal_error,max_overlap_displacement=max_j,
                max_latent_swaps=max_swaps,passed=True)


def save_csv(path: Path,rows: list[dict]) -> None:
    keys=list(dict.fromkeys(key for row in rows for key in row))
    with path.open('w',newline='') as fh:
        w=csv.DictWriter(fh,fieldnames=keys);w.writeheader();w.writerows(rows)


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--max-n',type=int,default=16)
    ap.add_argument('--radial-max',type=int,default=8192)
    ap.add_argument('--out',type=Path,default=Path('checks'))
    args=ap.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    if args.max_n<8 or args.max_n%2:ap.error('--max-n must be even and at least 8')
    summary={'status':'FINITE_CHECKS_PASS_NOT_AN_ASYMPTOTIC_PROOF',
             'polynomial':exact_polynomial_checks(),
             'posterior_coupling':posterior_coupling_check()}
    rows=[]
    for n in range(8,args.max_n+1,2):
        for l in range(4,n//2+1):
            row=spatial(n,l,check_mixture=n<=12);rows.append(row)
            print('SPATIAL',json.dumps(row),flush=True)
    save_csv(args.out/'actual_spatial_checks.csv',rows)
    radial_rows=[]
    n=32
    while n<=args.radial_max:
        for l in sorted({n//4,3*n//8,n//2}):
            row,*_=radial(n,l);radial_rows.append(row)
        n*=4
    save_csv(args.out/'radial_moment_checks.csv',radial_rows)
    summary['spatial_cases']=len(rows)
    summary['radial_cases']=len(radial_rows)
    summary['max_chain_rule_error']=max(r['chain_rule_error'] for r in rows)
    summary['max_fiber_entropy_error']=max(r['fiber_entropy_error'] for r in rows)
    summary['max_latent_mixture_error']=max(max(r.get('actual_latent_mixture_error',0),r.get('corrected_latent_mixture_error',0)) for r in rows)
    summary['max_radial_heat_moment_error']=max(max(r['heat_mean_formula_error'],r['heat_variance_formula_error']) for r in radial_rows)
    summary['scope']='Exact rational identities and floating-point finite spatial/coupling checks; not certification of the asymptotic theorem.'
    (args.out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print('SUMMARY',json.dumps(summary,indent=2),flush=True)

if __name__=='__main__':main()
