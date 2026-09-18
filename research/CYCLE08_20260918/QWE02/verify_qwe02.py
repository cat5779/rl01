#!/usr/bin/env python3
"""Reproducible QWE02 falsification checks (floating-point, not interval proofs).

Requires Python >= 3.10 and numpy. Run:
  OPENBLAS_NUM_THREADS=1 python verify_qwe02.py --output checks.json
The theorem is proved in RESULT.md; these tests do not certify it.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import numpy as np


def sine(n: int, rho: float = 0.5) -> np.ndarray:
    if n < 1 or not 0 < rho < 1:
        raise ValueError('n must be positive and rho must lie in (0,1)')
    d = np.arange(n)[:, None] - np.arange(n)[None, :]
    return rho * np.sinc(rho * d)


def words(n: int) -> np.ndarray:
    return ((np.arange(1 << n)[:, None] >> np.arange(n)) & 1).astype(float)


def atom_data(K: np.ndarray, ys: np.ndarray) -> tuple:
    n = K.shape[0]
    if K.shape != (n, n) or ys.shape[-1] != n:
        raise ValueError('shape mismatch')
    M = np.broadcast_to(K, (*ys.shape[:-1], n, n)).copy()
    ix = np.arange(n)
    M[..., ix, ix] -= 1 - ys
    sign, lp = np.linalg.slogdet(M)
    expected = (-1.0) ** np.sum(1 - ys, axis=-1)
    if np.max(np.abs(sign - expected)) > 1e-8:
        raise ArithmeticError('atom determinant sign failure')
    return np.exp(lp), lp, np.linalg.inv(M)


def energy(R: np.ndarray, ys: np.ndarray) -> tuple:
    n = R.shape[-1]
    sigma = 1 - 2 * ys
    diag = np.diagonal(R, axis1=-2, axis2=-1).real
    t = -1 - sigma * diag
    q = np.abs(R) ** 2
    eps = sigma[..., :, None] * sigma[..., None, :]
    prod = t[..., :, None] * t[..., None, :]
    x = -eps * q / prod
    ix = np.arange(n)
    x[..., ix, ix] = 0.0
    if np.min(t) <= 0 or np.min(1+x) <= 0:
        raise ArithmeticError('invalid flip-ratio domain')
    A = np.sum(eps * np.log1p(x), axis=(-2,-1))
    trR2 = np.sum(q, axis=(-2,-1))
    return A + trR2, A, trR2


def block(K: np.ndarray) -> dict:
    ys = words(len(K))
    p, lp, R = atom_data(K, ys)
    T, A, tr2 = energy(R, ys)
    score = np.trace(R, axis1=-2, axis2=-1).real
    pp = p * (score**2 - tr2)
    H = -float(np.dot(p, lp))
    Hpp = -float(np.dot(pp, lp) + np.dot(p, score**2))
    Hpp_tool = -float(np.dot(p, T))
    # Independently form G^2 log(p) from all four corner values of each pair.
    idx = np.arange(len(ys))
    sigma = 1-2*ys
    A_cube = np.zeros(len(ys))
    for i in range(len(K)):
        for j in range(i+1,len(K)):
            mixed = lp[idx ^ (1<<i) ^ (1<<j)]-lp[idx ^ (1<<i)]-lp[idx ^ (1<<j)]+lp
            A_cube += 2*sigma[:,i]*sigma[:,j]*mixed
    cube_error = float(np.max(np.abs(A_cube-A)))
    return dict(H=H, Hpp=Hpp, Hpp_tool=Hpp_tool,
                mass_error=float(abs(p.sum()-1)),
                score_error=float(abs(np.dot(p,score))),
                acceleration_error=float(abs(pp.sum())),
                fisher_identity_error=float(abs(np.dot(p, score**2-tr2))),
                curvature_identity_error=float(abs(Hpp-Hpp_tool)),
                cube_identity_error=cube_error,
                p=p, ys=ys, R=R, T=T, lp=lp)


def A_differentials(R: np.ndarray, y: np.ndarray, Z: np.ndarray) -> tuple[float,float]:
    """Analytic first and second Frechet differentials, including complex Z."""
    n = len(y)
    sig = 1 - 2*y
    t = -1-sig*np.diag(R).real
    h = -sig*np.diag(Z).real
    first = second = 0.0
    for i in range(n):
        for j in range(i+1,n):
            r, z = R[i,j], Z[i,j]
            q = abs(r)**2
            v = float(np.real(np.conj(r)*z))
            eps = sig[i]*sig[j]
            ti,tj = t[i],t[j]
            hi,hj = h[i],h[j]
            d = ti*tj-eps*q
            first += 2*(q*hi/(ti*d)+q*hj/(tj*d)-2*v/d)
            second += 2*(
                -q*(1/(ti*ti*d)+tj/(ti*d*d))*hi*hi
                -q*(1/(tj*tj*d)+ti/(tj*d*d))*hj*hj
                -2*q*hi*hj/(d*d)
                +4*(tj*hi+ti*hj)*v/(d*d)
                -2*abs(z)**2/d -4*eps*v*v/(d*d))
    return float(first),float(second)


def plain(d: dict) -> dict:
    return {k:v for k,v in d.items() if not isinstance(v,np.ndarray)}


def main() -> dict:
    rng = np.random.default_rng(20260918)
    out: dict = {'status':'FLOATING_POINT_FALSIFICATION_TESTS_NOT_PROOF',
                 'seed':20260918,'benchmark':[], 'random_gapped':[],
                 'differential_checks':[], 'large_word_checks':[]}
    cache = {}
    for a in (0.015,0.025,0.035):
        for n in range(1,13):
            cache[a,n] = block(a*np.eye(n)+0.95*sine(n))
        for L in range(1,7):
            small, full = cache[a,L],cache[a,2*L]
            ys=full['ys']
            K=a*np.eye(2*L)+.95*sine(2*L)
            _,_,ra=atom_data(K[:L,:L],ys[:,:L])
            _,_,rb=atom_data(K[L:,L:],ys[:,L:])
            defect=full['T']-energy(ra,ys[:,:L])[0]-energy(rb,ys[:,L:])[0]
            direct=2*small['Hpp']-full['Hpp']
            via_defect=float(np.dot(full['p'],defect))
            out['benchmark'].append(dict(a=a,L=L,J=2*small['H']-full['H'],
                Jpp=direct,Jpp_defect=via_defect,
                defect_identity_error=abs(direct-via_defect),
                word_defect_min=float(defect.min()),word_defect_max=float(defect.max()),
                negative_defect_words=int(np.count_nonzero(defect<0)),
                cross_HS2=float(np.sum(abs(K[:L,L:])**2))))
    out['max_normalization_error']=max(v['mass_error'] for v in cache.values())
    out['max_entropy_curvature_identity_error']=max(v['curvature_identity_error'] for v in cache.values())
    out['max_cube_identity_error']=max(v['cube_identity_error'] for v in cache.values())
    out['max_fisher_identity_error']=max(v['fisher_identity_error'] for v in cache.values())
    out['benchmark_chords']=[]
    for L in range(1,7):
        Js=[2*cache[a,L]['H']-cache[a,2*L]['H'] for a in (.015,.025,.035)]
        out['benchmark_chords'].append(dict(L=L,delta_J=Js[0]+Js[2]-2*Js[1]))
    # Generic Hermitian gapped DPPs: unequal blocks and complex kernels.
    for n in (3,5,8,10):
        X=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        U,_=np.linalg.qr(X)
        eig=np.linspace(.1,.9,n)
        K=(U*eig)@U.conj().T
        b=block(K)
        cut=n//2
        ka,kb=K[:cut,:cut],K[cut:,cut:]
        ba,bb=block(ka),block(kb)
        ys=b['ys']
        _,_,ra=atom_data(ka,ys[:,:cut]); _,_,rb=atom_data(kb,ys[:,cut:])
        de=b['T']-energy(ra,ys[:,:cut])[0]-energy(rb,ys[:,cut:])[0]
        Jpp=ba['Hpp']+bb['Hpp']-b['Hpp']
        out['random_gapped'].append(dict(n=n,cut=cut,Jpp=Jpp,
            defect_identity_error=abs(Jpp-float(np.dot(b['p'],de))),
            word_defect_min=float(de.min()),word_defect_max=float(de.max())))
        # Check analytic differentials against finite differences of their lower orders.
        for repeat in range(4):
            y=rng.integers(0,2,n).astype(float)
            _,_,R=atom_data(K,y)
            X=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
            Z=(X+X.conj().T)/2
            Z/=np.linalg.norm(Z,'fro')
            d1,d2=A_differentials(R,y,Z)
            step=1e-5
            ap=energy(R+step*Z,y)[1]; am=energy(R-step*Z,y)[1]
            fd1=(ap-am)/(2*step)
            fd2=(A_differentials(R+step*Z,y,Z)[0]-A_differentials(R-step*Z,y,Z)[0])/(2*step)
            out['differential_checks'].append(dict(n=n,
                first_error=abs(float(fd1)-d1),second_error=abs(float(fd2)-d2)))
    # Actual sine kernels at substantially larger volumes; pointwise checks need no enumeration.
    for L in (8,16,32,64,128):
        K=.025*np.eye(2*L)+.95*sine(2*L)
        K0=K.copy(); K0[:L,L:]=0;K0[L:,:L]=0
        V=K-K0; e=float(np.linalg.norm(K[:L,L:],'fro')**2)
        for kind in ('empty','full','alternating','random'):
            if kind=='empty':y=np.zeros(2*L)
            elif kind=='full':y=np.ones(2*L)
            elif kind=='alternating':y=np.arange(2*L)%2
            else:y=rng.integers(0,2,2*L).astype(float)
            _,_,R0=atom_data(K0,y)
            T0=float(energy(R0,y)[0])
            vals={}
            for theta in (0.0001,0.001,0.01,.1,.5,1.):
                _,_,R=atom_data(K0+theta*V,y)
                val=float(energy(R,y)[0]-T0)
                vals[str(theta)]=val/(theta*theta*e)
            out['large_word_checks'].append(dict(L=L,word=kind,cross_HS2=e,
                defect_over_theta2_energy=vals))
    # Independence is an exact limiting check, not an assumption of a signed response.
    independent = block(np.diag([.2,.35,.6,.75]))
    out['independence_check']=dict(curvature=independent['Hpp'],
        expected=-sum(1/(x*(1-x)) for x in [.2,.35,.6,.75]),
        A_max=float(np.max(np.abs(energy(independent['R'],independent['ys'])[1]))))
    out['constant_I']=64*(.95**2)/(math.pi**2*(.015**12))
    assert out['max_normalization_error']<1e-10
    assert out['max_entropy_curvature_identity_error']<1e-7
    assert out['max_fisher_identity_error']<1e-7
    assert out['max_cube_identity_error']<1e-7
    assert max(v['defect_identity_error'] for v in out['benchmark'])<1e-7
    assert max(v['second_error'] for v in out['differential_checks'])<1e-5
    return out


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('checks.json'))
    args=parser.parse_args()
    result=main()
    args.output.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['large_word_checks','differential_checks']},indent=2))
    print('Saved',args.output)
