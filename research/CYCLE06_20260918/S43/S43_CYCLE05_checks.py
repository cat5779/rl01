#!/usr/bin/env python3
"""S43 cycle05: reproducible finite diagnostics and explicit coefficient evaluation.

These computations are implementation diagnostics, not independent certification
and not asymptotic fitting.  All heat clocks are the prescribed coefficient clocks.
G is the original-rate slice generator; the four endpoint layers contribute zero.

Dependencies: Python 3.10+, numpy, scipy, mpmath.
Usage:
  python S43_CYCLE05_checks.py --sizes 4 6 8 10 --output S43_CYCLE05_checks_output.json
  python S43_CYCLE05_checks.py --sizes 12 --no-heat
There is no theoretical restriction to these diagnostic sizes. Enumeration costs
O(2**n) storage and polynomial times 2**n work; choose sizes to suit the machine.
"""
from __future__ import annotations
import argparse
import json
import math
from itertools import combinations
from pathlib import Path
from typing import Any
import mpmath as mp
import numpy as np
from scipy.special import gammaln, logsumexp
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import expm_multiply


def g(x: Any) -> Any:
    x = np.asarray(x)
    return x * (np.log1p(x) - np.log1p(-x))


def phi(a: float, y: np.ndarray) -> np.ndarray:
    return a / 2 * ((a + y) * np.log((1 + a*a + 2*a*y)/(1-a*a))
                    + (a - y) * np.log((1 + a*a - 2*a*y)/(1-a*a)))


def projection(n: int) -> np.ndarray:
    if n < 4 or n % 2:
        raise ValueError('n must be even and at least 4')
    u = np.exp(2j*np.pi*np.outer(np.arange(n), np.arange(n//2))/n)/np.sqrt(n)
    return u @ u.conj().T


def logcomb(n: int, j: int) -> float:
    if not 0 <= j <= n:
        return -math.inf
    return float(gammaln(n+1)-gammaln(j+1)-gammaln(n-j+1))


def coeff_logmean(k: int, l: int, z: float) -> tuple[float, float]:
    js = np.arange(max(0, l-k), min(k, l)+1)
    if len(js) == 0:
        raise ValueError('coefficient index outside support')
    terms = np.array([logcomb(k, int(j))+logcomb(k, l-int(j))
                      + int(j)*math.log(z) for j in js])
    logz = float(logsumexp(terms))
    mean = float(np.dot(js, np.exp(terms-logz)))
    return logz, mean


def clock(n: int, l: int, c: float) -> dict[str, float]:
    if l in (0, 1, n-1, n):
        return {'s': 0.0, 'acceleration': 0.0, 'theta': 1.0, 'logZ': 0.0}
    k = n//2
    l = min(l, n-l)
    z = ((1+c)/(1-c))**2
    logz, mz = coeff_logmean(k, l, z)
    loga, ma = coeff_logmean(k-2, l-2, z)
    alpha = l*(l-1)/(k*(k-1))
    logtheta = 2*math.log(z-1)+loga-math.log(alpha)-logz
    dlogtheta = 2/(z-1)+(ma-mz)/z
    zpp = 32*c/(1-c)**4  # derivative in a, at a=(1-c)/2 with c fixed
    return {'s': -logtheta/(2*(n-1)),
            'acceleration': zpp*dlogtheta/(2*(n-1)),
            'theta': math.exp(logtheta), 'logZ': logz,
            'dlogtheta_dz': dlogtheta}


def binpoly(k: int, p: float) -> np.ndarray:
    return np.array([math.exp(logcomb(k,j)+j*math.log(p)+(k-j)*math.log1p(-p))
                     for j in range(k+1)])


def count_weights(n: int, c: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    k = n//2; p=(1+c)/2; q=(1-c)/2
    pi = np.convolve(binpoly(k,p), binpoly(k,q))
    B = k*(k-1)*(np.convolve(binpoly(k-2,p),binpoly(k,q))
                    + np.convolve(binpoly(k,p),binpoly(k-2,q)))
    B += 2*k*k*np.convolve(binpoly(k-1,p),binpoly(k-1,q))
    kap = np.convolve(B, np.array([1., -2., 1.]))
    return pi, B, kap


def full_law(n: int, c: float, P: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    p=(1+c)/2; q=(1-c)/2; b=p*q
    L=(q/p)*np.eye(n)+(c/b)*P
    lognorm=(n//2)*(math.log1p(p/q)+math.log1p(q/p))
    logp=np.empty(1<<n)
    for mask in range(1<<n):
        S=[i for i in range(n) if mask>>i&1]
        if not S:
            val=0.0
        else:
            sign,val=np.linalg.slogdet(L[np.ix_(S,S)])
            if abs(sign-1)>1e-8:
                raise ArithmeticError('nonpositive or inaccurate principal determinant')
        logp[mask]=val-lognorm
    prob=np.exp(logp)
    if abs(prob.sum()-1)>1e-9:
        raise ArithmeticError('full-law mass check failed')
    return prob, logp, L


def full_diagnostics(n: int, c: float, P: np.ndarray) -> dict[str, Any]:
    prob,logp,L=full_law(n,c,P)
    masks=np.arange(1<<n,dtype=np.int64)
    b=(1-c*c)/4; a=c*c; r=(1+c)/(1-c)
    I=0.; X2=0.; cross=0.; max_range_error=0.; max_row=0.
    for i in range(n):
        base=masks&~(1<<i)
        h=logp[base|(1<<i)]-logp[base]
        x=np.tanh(h/2)
        I+=float(prob@(x*h)); X2+=float(prob@(x*x))
        row=np.zeros_like(h)
        for j in range(n):
            if i==j: continue
            bb=base&~(1<<j)
            dh=logp[bb|(1<<i)|(1<<j)]-logp[bb|(1<<j)]-logp[bb|(1<<i)]+logp[bb]
            cross+=float(prob@dh)
            row+=np.abs(h[masks^(1<<j)]-h)
        max_row=max(max_row,float(row.max()))
        opp=np.array([j for j in range(n) if (i-j)%2])
        weights=4*np.abs(P[i,opp])**2
        y=np.zeros(1<<n)
        for j,w in zip(opp,weights):
            y+=w*(1-2*((masks>>j)&1))
        lower=a*(y-a)/(1-a*y); upper=a*(y+a)/(1+a*y)
        max_range_error=max(max_range_error,float(np.max(lower-x)),float(np.max(x-upper)))
    N=np.array([int(m).bit_count() for m in masks]); xx=N-n/2
    Ex2=float(prob@(xx*xx)); meanlog=float(prob@logp)
    cov=float(prob@((xx*xx)*(logp-meanlog)))
    field_second=cov+n*b*c*c
    field_stein=b*b*cross-b*I+n*b*c*c
    compensator=cross+n*c*c/b
    vn=1/3+8/(3*n*n)
    neighbor=8*c*c/(n*n*math.sin(math.pi/n)**2)
    Ilower=.5*float(g(neighbor))
    Iupper=(1-vn)*float(g(c**4))+vn*float(g(c*c))
    x2lower=c**4*vn
    x2upper=(1-vn)*c**8+vn*c**4
    assert max_range_error < 1e-9
    assert I/n >= Ilower-1e-9 and I/n <= Iupper+1e-9
    assert x2lower-1e-9 <= X2/n <= x2upper+1e-9
    assert max_row <= 2*r*r+1e-8
    assert abs(field_second-field_stein) < 1e-8*(1+abs(field_second))
    return {'mass':float(prob.sum()),'count_variance':Ex2,
            'flip_production_per_site':I/n,'flip_over_b_per_site':I/(b*n),
            'compensator_per_site':compensator/n,'predictor_second_moment':X2/n,
            'finite_flip_lower':Ilower,'finite_flip_upper':Iupper,
            'finite_predictor_lower':x2lower,'finite_predictor_upper':x2upper,
            'parity_weight_square_sum':float(np.sum((4*np.abs(P[0,1::2])**2)**2)),
            'parity_weight_square_sum_formula':vn,
            'max_conditional_range_violation':max_range_error,
            'largest_logodds_flip_row_sum':max_row,
            'logodds_flip_row_bound':2*r*r,
            'Stein_identity_residual':field_second-field_stein,
            'field_second_derivative_per_site':field_second/n,
            'finite_exact_cancellation_residual':field_second/(b*b)+I/b-compensator}


def slice_generator(n: int, l: int) -> tuple[list[tuple[int,...]], csr_matrix]:
    states=list(combinations(range(n),l)); index={S:i for i,S in enumerate(states)}
    rows=[]; cols=[]; data=[]
    degree=l*(n-l)
    for idx,S in enumerate(states):
        ss=set(S)
        rows.append(idx);cols.append(idx);data.append(-degree)
        for i in S:
            for j in range(n):
                if j in ss: continue
                T=tuple(sorted((ss-{i})|{j}))
                rows.append(idx);cols.append(index[T]);data.append(1)
    G=csr_matrix((np.array(data,float),(rows,cols)),shape=(len(states),len(states)))
    return states,G


def corrected_diagnostics(n: int, c: float, P: np.ndarray) -> dict[str, Any]:
    k=n//2; pi,B,kap=count_weights(n,c)
    z=((1+c)/(1-c))**2
    Lam=np.eye(n)+(z-1)*P
    F=np.zeros(n+1); J=np.zeros(n+1); acc=np.zeros(n+1)
    FG=np.zeros(n+1); UKL=np.zeros(n+1); evidence=np.zeros(n+1)
    layer_rows=[]
    for l in range(2,k+1):
        states,G=slice_generator(n,l)
        q0=[]; logdet=[]
        for S in states:
            ix=np.ix_(S,S)
            q0.append(math.exp(np.linalg.slogdet(P[ix])[1]-logcomb(k,l)))
            logdet.append(float(np.linalg.slogdet(Lam[ix])[1]))
        q0=np.array(q0); logdet=np.array(logdet)
        if abs(q0.sum()-1)>1e-8: raise ArithmeticError('initial mass check failed')
        cl=clock(n,l,c); s=cl['s']
        mu=expm_multiply(s*G,q0)
        if np.any(mu<=0): raise ArithmeticError('heat probability nonpositive')
        logu=-logcomb(n,l)
        f=float(mu@(np.log(mu)-logu))
        ep=-float((G@mu)@np.log(mu))
        gamma=np.exp(logdet-cl['logZ'])
        fg=float(gamma@(np.log(gamma)-logu))
        ukl=float(mu@(np.log(mu)-np.log(gamma)))
        vv=float((mu-gamma)@logdet)
        for j in set((l,n-l)):
            F[j]=f;J[j]=ep;acc[j]=cl['acceleration'];FG[j]=fg;UKL[j]=ukl;evidence[j]=vv
        layer_rows.append({'l':l,'s':s,'n_s':n*s,'theta':cl['theta'],
                           'n_clock_acceleration':n*cl['acceleration'],
                           'F':f,'J_G_over_n2':ep/n**2,
                           'F_minus_FG':f-fg,'output_KL':ukl,'evidence':vv,
                           'entropy_ledger_residual':f-fg-ukl-vv})
        assert abs(f-fg-ukl-vv)<1e-8
        assert ep>=-1e-8
    W=float(kap@F); C=float(pi@(acc*J)); WG=float(kap@FG)
    return {'W_over_n':W/n,'C_over_n':C/n,'W_plus_C_over_n':(W+C)/n,
            'WG_over_n':WG/n,'weighted_output_KL_over_n':float(kap@UKL)/n,
            'weighted_evidence_over_n':float(kap@evidence)/n,
            'pi_mass':float(pi.sum()),'B_mass':float(B.sum()),
            'kappa_mass':float(kap.sum()),'layers':layer_rows,
            'note':'These are pre-asymptotic values at exact clocks, not fits.'}


def explicit_coefficients(c_text: str) -> dict[str, Any]:
    mp.mp.dps=65
    c=mp.mpf(c_text);b=(1-c*c)/4;a=c*c
    gm=lambda x:x*mp.log((1+x)/(1-x))
    rho=1-c*c*mp.log(c)/(2*b);D=(rho-1-mp.log(rho))/2
    M=2*mp.exp(-mp.mpf('0.5'))/(mp.sqrt(2*mp.pi)*b)
    A=16*c**4/(b*mp.pi**4)
    ans={'c':str(c),'clock_lower':str(gm(8*a/mp.pi**2)/(2*b)),
         'clock_upper':str((2*gm(a*a)+gm(a))/(3*b)),
         'old_pair_A':str(A),'analytic_clock_lower_floor_4A':str(4*A),
         'joint_lower':str((c**4/3-c**6)/(b*(1-c**4))-M*D),
         'joint_upper':str((2*c**8+c**4)/(3*b)+M*D),
         'M_times_D':str(M*D),
         'decimals_are':'high precision evaluations of explicit formulas, not interval certificates'}
    # Optional sharper, finite-sum parity upper bounds; proof in manuscript.
    cf=float(c);af=cf*cf;bf=(1-cf*cf)/4
    refinements=[]
    for pairs in (1,2,3,4,6,8):
        weights=np.repeat(4/(np.pi*np.pi*(2*np.arange(pairs)+1)**2),2)
        vals=np.array([0.])
        for w in weights: vals=np.r_[vals+w,vals-w]
        d=1-float(weights.sum())
        upper=float(np.mean((phi(af,vals+d)+phi(af,vals-d))/2))/bf
        lower=float(np.mean(g(af*vals)))/bf
        refinements.append({'opposite_parity_neighbor_pairs':pairs,
                            'finite_sum_upper':upper,'finite_sum_lower':lower,
                            'remaining_weight':d})
    ans['optional_parity_refinements']=refinements
    return ans


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sizes',nargs='+',type=int,default=[4,6,8,10])
    parser.add_argument('--c',default='0.95')
    parser.add_argument('--no-heat',action='store_true')
    parser.add_argument('--output',default='S43_CYCLE05_checks_output.json')
    args=parser.parse_args()
    c=float(args.c)
    if not 0<c<1: raise ValueError('c must be strictly between zero and one')
    report={'label':'S43_CYCLE05','status':'finite diagnostics, not independent verification',
            'constants':explicit_coefficients(args.c),'finite_cases':[]}
    for n in args.sizes:
        P=projection(n)
        row={'n':n,'full_Gibbs':full_diagnostics(n,c,P)}
        if not args.no_heat:
            row['corrected']=corrected_diagnostics(n,c,P)
            row['terminal_transfer_difference_per_site']=(row['corrected']['C_over_n']
                    -row['full_Gibbs']['flip_over_b_per_site'])
        report['finite_cases'].append(row)
        print(json.dumps(row,ensure_ascii=False),flush=True)
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(f'Wrote {path}')

if __name__=='__main__':
    main()
