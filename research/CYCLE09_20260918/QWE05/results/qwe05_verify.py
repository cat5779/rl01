"""QWE05 finite-model checks. No numerical calculation here is an asymptotic proof.
Requires Python 3.10+, NumPy and SciPy. Run: python qwe05_verify.py --small-max 16
"""
from __future__ import annotations
import argparse, csv, json, math, time
from itertools import combinations
from pathlib import Path
import numpy as np
from scipy.special import gammaln, logsumexp
from scipy.sparse import csr_matrix, diags
from scipy.sparse.linalg import expm_multiply

XI = 1.0 / 1520.0
C_CONTRAST = 19.0 / 20.0

def log_q(r: int, d: int, xi: float = XI) -> tuple[float, float]:
    """log Q_r^(d) and its logarithmic derivative, using positive coefficients."""
    if r == 0:
        return 0.0, 0.0
    s = np.arange(r, dtype=float)
    inc = np.log(r-s) + np.log(r+2*d-1+s) - np.log(d+s) - np.log(s+1) + math.log(xi)
    logs = np.r_[0.0, np.cumsum(inc)]
    z = float(logsumexp(logs))
    deriv = float(np.dot(np.arange(r+1), np.exp(logs-z))/xi)
    return z, deriv

def clock(n: int, m: int, xi: float = XI) -> dict[str, float]:
    assert n % 2 == 0 and 2 <= m <= n//2
    d = n//2-m+1
    qm, dm = log_q(m,d,xi)
    q2, d2 = log_q(m-2,d,xi)
    gamma = 2.0*(n-1)/(m*(n-m))
    return dict(tau=(qm-q2)/gamma, tau_xi=(dm-d2)/gamma, gamma=gamma)

def radial_log_heat(n: int, m: int, tau: float, extra: int=80) -> np.ndarray:
    """Positive log-space uniformization, including at least m jumps.
    This is floating-point verification, not a certified interval enclosure.
    """
    k=n//2; r=np.arange(m+1,dtype=float); j=m-r; C=m*(n-m)
    up=j*(k-m+j)/C;down=(m-j)*(k-j)/C
    stay=np.maximum(0.0,1.0-up-down)
    def safelog(x):
        y=np.full_like(x,-np.inf); mask=x>0;y[mask]=np.log(x[mask]);return y
    lu,ld,ls=safelog(up),safelog(down),safelog(stay)
    v=np.full(m+1,-np.inf);v[0]=0
    ans=v-tau; lp=-tau
    steps=m+int(math.ceil(tau+12*math.sqrt(tau+1)))+extra
    for it in range(1,steps+1):
        vv=v+ls
        vv[1:]=np.logaddexp(vv[1:],v[:-1]+lu[:-1])
        vv[:-1]=np.logaddexp(vv[:-1],v[1:]+ld[1:])
        v=vv;lp+=math.log(tau)-math.log(it)
        ans=np.logaddexp(ans,lp+v)
    return ans

def radial(n: int, m: int, xi: float = XI) -> dict:
    """Exact conditional-on-input radial model, states r=m-|S intersection A|."""
    k=n//2
    r=np.arange(m+1, dtype=float)
    logcomb=lambda nn, rr: gammaln(nn+1)-gammaln(rr+1)-gammaln(nn-rr+1)
    logs=logcomb(k,m-r)+logcomb(k,r)-r*math.log((1+xi)/xi)
    logs-=logsumexp(logs)
    w=np.exp(logs)
    cm=clock(n,m,xi)
    j=m-r
    up=j*(k-m+j)/(m*(n-m))
    down=(m-j)*(k-j)/(m*(n-m))
    gen=diags([up[:-1],-(up+down),down[1:]],[-1,0,1],format='csr')
    start=np.zeros(m+1);start[0]=1
    wh=np.asarray(expm_multiply(cm['tau']*gen,start))
    logwh=radial_log_heat(n,m,cm['tau'])
    kl=float(np.sum(w*(logs-logwh)))
    chi=float(np.expm1(logsumexp(2*logs-logwh)))
    return dict(n=n,m=m,tau=cm['tau'],radial_kl=kl,radial_chi2=chi,
                true_mass=float(w.sum()),heat_mass=float(np.exp(logsumexp(logwh))),
                heat_crosscheck_l1=float(np.sum(np.abs(np.exp(logwh)-wh))),
                max_log_likelihood=float(np.max(logs-logwh)),
                w=w,wh=np.exp(logwh),gen=gen,clock=cm)

def layer(n: int, m: int, projection: np.ndarray) -> dict:
    masks=[sum(1<<i for i in S) for S in combinations(range(n),m)]
    sets=list(combinations(range(n),m));N=len(sets)
    if m<=1:
        arr=np.ones(N)/N
        return dict(m=m,masks=masks,sets=sets,q=arr.copy(),g=arr.copy(),R=0.,xi_score=np.zeros(N))
    cm=clock(n,m)
    Lmat=(np.eye(n)/39.0)+(39.0-1.0/39.0)*projection
    logweights=np.array([np.linalg.slogdet(Lmat[np.ix_(S,S)])[1] for S in sets])
    q=np.exp(logweights-logsumexp(logweights))
    initial=np.array([np.linalg.det(projection[np.ix_(S,S)]).real/math.comb(n//2,m) for S in sets])
    assert np.min(initial)>-1e-12
    assert abs(initial.sum()-1)<1e-9
    ind={s:i for i,s in enumerate(masks)}
    rows=[];cols=[]
    for ii,mask in enumerate(masks):
        occupied=[j for j in range(n) if mask>>j&1]
        empty=[j for j in range(n) if not mask>>j&1]
        for a in occupied:
            for b in empty:
                rows.append(ii);cols.append(ind[mask^(1<<a)^(1<<b)])
    C=m*(n-m)
    gen=csr_matrix((np.full(len(rows),1.0/C),(rows,cols)),shape=(N,N))-diags(np.ones(N))
    g=np.asarray(expm_multiply(cm['tau']*gen,initial))
    assert np.min(q)>0 and np.min(g)>0
    R=float(np.dot(q,np.log(q/g)))
    return dict(m=m,masks=masks,sets=sets,q=q,g=g,R=R,gen=gen,clock=cm,initial=initial)

def delete(n: int, above: dict, values: np.ndarray, below: dict) -> np.ndarray:
    m=below['m']; ind={s:i for i,s in enumerate(below['masks'])}
    out=np.zeros(len(ind))
    for mask,val in zip(above['masks'],values):
        for j in range(n):
            if mask>>j&1:
                out[ind[mask^(1<<j)]]+=val/(m+1)
    return out

def count_hessian(n: int) -> tuple[np.ndarray,np.ndarray]:
    k=n//2;a=(1-C_CONTRAST*C_CONTRAST)/4;b=(1+C_CONTRAST*C_CONTRAST)/2
    p0=np.array([a,b,a])
    power=lambda r: np.polynomial.polynomial.polypow(p0,r)
    B=2*k*power(k-1)
    B+=k*(k-1)*np.convolve([1.,2.,1.],power(k-2))
    h=np.convolve(B,[1.,-2.,1.])
    return h,B

def full_check(n: int) -> tuple[dict,list[dict]]:
    k=n//2;x=np.arange(n)
    U=np.exp(2j*np.pi*np.outer(x,np.arange(k))/n)/math.sqrt(n)
    P=U@U.conj().T
    layers=[layer(n,m,P) for m in range(k+1)]
    RR=np.array([layers[min(l,n-l)]['R'] for l in range(n+1)])
    hh,B=count_hessian(n)
    W=float(hh@RR)
    omega=np.r_[B[0],np.diff(B[:k])]
    ledger=[]
    for m in range(3,k):
        lo,hi=layers[m],layers[m+1]
        dq=delete(n,hi,hi['q'],lo); dg=delete(n,hi,hi['g'],lo)
        downKL=float(np.dot(dq,np.log(dq/dg)))
        reverse=hi['R']-downKL
        radial_data=radial(n,m)
        r=np.arange(m+1);mu=m-float(radial_data['w']@r)
        tm=1/(k-m+(m-mu)+XI*(n-m));eta=XI*(1+XI)*tm
        qxi=(dq-lo['q'])/eta
        gxi=lo['clock']['tau_xi']*(lo['gen']@lo['g'])
        response=float(np.dot(qxi,np.log(lo['q']/lo['g']))-np.dot(lo['q'],gxi/lo['g']))
        J=downKL-lo['R']-eta*response
        gamma=lo['clock']['gamma']
        s=eta*lo['clock']['tau_xi']
        h=(m*(n-m))*(hi['clock']['tau']/((m+1)*(n-m-1))-lo['clock']['tau']/(m*(n-m)))
        gp=np.asarray(expm_multiply(h*lo['gen'],lo['g']))
        src=lo['g']+s*(lo['gen']@lo['g'])-gp
        fnorm=float(np.sum(src*src/lo['g']))
        t=lo['clock']['tau'];u=h*h/t
        paid=float(np.expm1(u)-u+(h-s)**2/t)
        mismatch=float(np.sum((gp-lo['g'])**2/lo['g']))
        ledger.append(dict(n=n,m=m,R=lo['R'],R_next=hi['R'],C_reverse=reverse,
                           eta_R_xi=eta*response,J=J,omega=float(omega[m]),
                           source_fisher2=fnorm,poisson_source_bound=paid,
                           corrected_chi2=mismatch,poisson_chi2_bound=float(np.expm1(u)),
                           correction_transport_error=float(np.max(np.abs(dg-gp))),
                           ledger_error=hi['R']-lo['R']-reverse-eta*response-J))
    wc=2*sum(z['omega']*z['C_reverse'] for z in ledger)
    wj=2*sum(z['omega']*z['J'] for z in ledger)
    wr=2*sum(z['omega']*z['eta_R_xi'] for z in ledger)
    return dict(n=n,W_rel=W,W_over_n=W/n,R_center=layers[k]['R'],
                twice_reverse_flux=wc,twice_J_flux=wj,twice_response_flux=wr,
                ledger_error=W+wc+wj+wr,
                count_mass_error=float(B.sum()-n*(n-1))),ledger

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--small-max',type=int,default=16)
    ap.add_argument('--radial-max',type=int,default=4096);args=ap.parse_args()
    out=Path(__file__).resolve().parent
    full=[];led=[]
    for n in range(8,args.small_max+1,2):
        t=time.time();row,ll=full_check(n);full.append(row);led+=ll
        print('FULL',json.dumps(row),'seconds',round(time.time()-t,3),flush=True)
    radial_rows=[]
    for n in [32,64,128,256,512,1024,2048,4096,8192,16384]:
        if n>args.radial_max:continue
        for offset in [0,int(math.sqrt(n)),int(n**(2/3))]:
            m=n//2-offset
            if m<4:continue
            rr=radial(n,m)
            row={a:b for a,b in rr.items() if a not in ('w','wh','gen','clock')}
            radial_rows.append(row);print('RADIAL',json.dumps(row),flush=True)
    for name,rows in [('full_model.csv',full),('deletion_ledger.csv',led),('radial_checks.csv',radial_rows)]:
        if rows:
            with (out/name).open('w',newline='') as fh:
                wr=csv.DictWriter(fh,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)
    (out/'verification_summary.json').write_text(json.dumps(dict(full_model=full,radial=radial_rows),indent=2))

if __name__=='__main__':main()
