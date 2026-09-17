"""Complete-atom FLOATING diagnostics, not a sign certificate.

Preserves each occupied/vacant event, the actual original-shift derivatives
(including u and u^2), and all center-pair moving-weight/acceleration terms.
"""
from __future__ import annotations
import argparse
import datetime as dt
import json
from pathlib import Path
import numpy as np


def kernel(radius: int, c: float, delta: float, u: float,
           degree: int | None = None) -> np.ndarray:
    if radius < 0 or not (0 < c < 1) or not (0 < u <= 1):
        raise ValueError("Invalid parameters")
    if abs(delta) >= (1-c)/2:
        raise ValueError("Use strictly legal original shifts")
    degree = radius if degree is None else degree
    n = 2*radius+1
    lag = np.arange(n)[:,None]-np.arange(n)[None,:]
    coeff = np.zeros((n,n), dtype=float)
    nz = lag != 0
    coeff[nz] = np.sin(np.pi*lag[nz]/2)/(np.pi*lag[nz])
    coeff *= np.maximum(0., 1.-np.abs(lag)/(degree+1))
    return (.5+u*delta)*np.eye(n)+u*c*coeff


def evaluate(radius: int, c: float, delta: float, u: float,
             degree: int | None = None) -> dict:
    K = kernel(radius,c,delta,u,degree)
    n = len(K)
    ids = np.arange(1<<n, dtype=np.int64)
    bits = (ids[:,None] >> np.arange(n)) & 1
    p = np.empty(1<<n)
    p1 = np.empty_like(p)
    p2 = np.empty_like(p)
    for lo in range(0, 1<<n, 4096):
        hi = min(1<<n, lo+4096)
        A = np.broadcast_to(K,(hi-lo,n,n)).copy()
        A[:,np.arange(n),np.arange(n)] -= 1-bits[lo:hi]
        signs,logs = np.linalg.slogdet(A)
        probs = signs*np.where(((n-bits[lo:hi].sum(1)) % 2)==0,1.,-1.)*np.exp(logs)
        inv = np.linalg.inv(A)
        tr = np.trace(inv,axis1=1,axis2=2)
        tr2 = np.einsum('bij,bji->b',inv,inv)
        p[lo:hi] = probs
        p1[lo:hi] = u*probs*tr
        p2[lo:hi] = u*u*probs*(tr*tr-tr2)
    if p.min() <= 0:
        raise ArithmeticError("Numerical nonpositive atom")
    zero = ids[(ids & (1<<radius))==0]
    one = zero | (1<<radius)
    x,y=p[zero],p[one]
    x1,y1=p1[zero],p1[one]
    x2,y2=p2[zero],p2[one]
    logratio=np.log(y)-np.log(x)
    F=.5*(y-x)*logratio
    F2=.5*(x+y)*(x1/x-y1/y)**2 \
       +.5*(-logratio+1-y/x)*x2 \
       +.5*(logratio+1-x/y)*y2
    layers=bits[zero].sum(1)
    return dict(radius=radius,degree=radius if degree is None else degree,
                c=c,delta=delta,u=u,n=n,
                atom_count=len(p),mass=float(p.sum()),
                mass_d1=float(p1.sum()),mass_d2=float(p2.sum()),
                min_atom=float(p.min()),
                I=float(F.sum()),I_d2=float(F2.sum()),
                I_d2_over_u2=float(F2.sum()/(u*u)),
                H=float(-np.sum(p*np.log(p))),
                H_d2=float(-np.sum(p2*np.log(p)+p1*p1/p)),
                layer_I=[float(F[layers==k].sum()) for k in range(2*radius+1)],
                layer_I_d2=[float(F2[layers==k].sum()) for k in range(2*radius+1)])


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--radii',type=int,nargs='+',default=[3,5])
    ap.add_argument('--c',type=float,default=.95)
    ap.add_argument('--deltas',type=float,nargs='+',default=[0.,.02])
    ap.add_argument('--u',type=float,nargs='+',default=[.25,.5,.75,1.])
    args=ap.parse_args()
    start=dt.datetime.now(dt.timezone.utc).isoformat()
    data=[evaluate(r,args.c,d,u) for r in args.radii for d in args.deltas for u in args.u]
    out=dict(status='FLOATING_DIAGNOSTIC_NOT_PROOF',started_utc=start,
             ended_utc=dt.datetime.now(dt.timezone.utc).isoformat(),rows=data)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    for row in data:
        print(row['radius'],row['delta'],row['u'],row['I'],row['I_d2_over_u2'],row['H_d2'])

if __name__=='__main__':
    main()
