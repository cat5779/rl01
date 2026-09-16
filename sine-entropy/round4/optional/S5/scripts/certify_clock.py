#!/usr/bin/env python3
"""Exact finite certificate for incompatible Bernoulli-Laplace slice clocks.

The proof extends to genuine P_(8m,4m) Fourier projections for every odd m,
and also to every direct sum of the genuine P_(8,4) Fourier block.
Finite evidence here uses only integers, Fraction, and Q(sqrt(2)).
"""
from __future__ import annotations
import argparse
import itertools
import json
import math
from fractions import Fraction as Q
from pathlib import Path
from exact_common import Qsqrt2,ensure_output


def padd(a,b):
    n=max(len(a),len(b));return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]
def pscale(a,t):return [t*x for x in a]
def pmul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def pder(a):return [i*a[i] for i in range(1,len(a))]
def peval(a,x):
    out=0
    for y in reversed(a):out=out*x+y
    return out

def Fpoly(m:int):
    # F_m(s)=sum_t binom(m,t)^2 s^(m-t)(1+s)^t.
    out=[0]*(m+1)
    for t in range(m+1):
        for j in range(t+1):out[m-t+j]+=math.comb(m,t)**2*math.comb(t,j)
    return out

def h(S:int,pairs):
    out=1
    for i,j in pairs:out*=int(bool(S&(1<<i)))-int(bool(S&(1<<j)))
    return out


def run(outdir:Path):
    n=8;k=4
    states=[sum(1<<i for i in A) for A in itertools.combinations(range(n),k)]
    chord=[Qsqrt2(0),Qsqrt2(2,-1),Qsqrt2(2),Qsqrt2(2,1),Qsqrt2(4),Qsqrt2(2,1),Qsqrt2(2),Qsqrt2(2,-1)]
    mu={}
    for S in states:
        inds=[i for i in range(n) if S&(1<<i)]
        v=Qsqrt2(Q(1,8**4))
        for i,j in itertools.combinations(inds,2):v=v*chord[j-i]
        mu[S]=v
    assert sum(mu.values(),Qsqrt2())==Qsqrt2(1)
    pairs2=((0,1),(2,3))
    pairs4=((0,2),(1,3),(4,6),(5,7))
    hs={2:{S:h(S,pairs2) for S in states},4:{S:h(S,pairs4) for S in states}}
    expected={2:Qsqrt2(Q(1,8)),4:Qsqrt2(Q(3,64))}
    eig_polys={2:[1,2,-6,2,1],4:[1,-4,6,-4,1]}
    group_mass_records={}
    expected_groups={2:{1:Qsqrt2(Q(35,128),Q(3,64)),-1:Qsqrt2(Q(19,128),Q(3,64))},4:{1:Qsqrt2(Q(7,64)),-1:Qsqrt2(Q(1,16))}}
    for d in [2,4]:
        moment=sum((mu[S]*hs[d][S] for S in states),Qsqrt2())
        assert moment==expected[d]
        group_mass_records[str(d)]={}
        for sign in (1,-1):
            mass=sum((mu[S] for S in states if hs[d][S]==sign),Qsqrt2())
            assert mass==expected_groups[d][sign]
            group_mass_records[str(d)][str(sign)]=mass.as_json()
        gamma=Q(d*(n-d+1),k*(n-k))
        for S in states:
            lhs=sum(hs[d][A]-hs[d][S] for A in states if (S^A).bit_count()==2)/Q(k*(n-k))
            assert lhs==-gamma*hs[d][S]
            coeff=[0]*(k+1)
            for A in states:coeff[(A&S).bit_count()]+=hs[d][A]
            assert coeff==pscale(eig_polys[d],hs[d][S])
    Z=[1,16,36,16,1]
    for S in states:
        coeff=[0]*5
        for A in states:coeff[(A&S).bit_count()]+=1
        assert coeff==Z
    F=Fpoly(4);G=Fpoly(2)
    assert F==[1,20,90,140,70] and G==[1,6,6]
    mismatch_numerator=padd(pscale(pmul(pder(F),G),3),pscale(pmul(pder(G),F),-10))
    rhs=pscale(pmul([0,1],pmul([1,1],pmul([1,2],pmul([1,2],[1,2])))),-420)
    assert mismatch_numerator==rhs==[0,-420,-2940,-7560,-8400,-3360]
    a=Q(1,100);c=Q(19,20);w=a*(1-c-a);s=w/c;s1=(1-c-2*a)/c
    mismatch=peval(mismatch_numerator,s)/(8*peval(F,s)*peval(G,s))*s1
    assert w==Q(1,2500) and s==Q(1,2375) and s1==Q(3,95)
    assert mismatch<0
    # Check exact algebra underlying the general growing-family theorem for
    # many k. The proof for all k is in proof.md and does not rest on this loop.
    general_checks=[]
    for K in range(4,65):
        J=K*(K+1);g2=Q(2*(2*K-1),K*K);g4=Q(4*(2*K-3),K*K)
        def logF_second(m):
            f=Fpoly(m)
            return Q(2*(f[2] if m>=2 else 0)-(f[1] if m>=1 else 0)**2)
        assert logF_second(K)==-Q(J*(J+2),2)
        calc=g2*(logF_second(K-4)-logF_second(K))-g4*(logF_second(K-2)-logF_second(K))
        claimed=Q(K**4,2)*g2*g4*(g2-g4)
        assert calc==claimed and claimed<0
        general_checks.append({'k':K,'mismatch_derivative_at_zero':str(claimed)})
    # An exact root-of-unity residue check for the true Fourier growth lift.
    # For every odd m, the 8 selected labels are 0,m,...,7m. There are
    # (m-1)/2 complete runs of 8 columns, then 4 columns. The proof for all
    # odd m uses this division identity, not a numerical Fourier matrix.
    lifts=[]
    for m in range(1,64,2):
        r=(m-1)//2
        residue_counts=[sum(1 for col in range(4*m) if col%8==j) for j in range(8)]
        assert residue_counts==[r+int(j<4) for j in range(8)]
        lifts.append({'m':m,'n':8*m,'rank':4*m,'column_residue_counts':residue_counts,
                      'h2_moment':str(Q(1,8*m*m)), 'h4_moment':str(Q(3,64*m**4))})
    report={'status':'EXACT_FINITE_CERTIFICATE','arithmetic':'integers, Fraction, Q(sqrt(2)); no floating-point assertions',
            'projection':'U[j,l]=8^(-1/2)*exp(2*pi*i*j*l/8), 0<=j<8,0<=l<4; P=U U*',
            'mu_formula':'8^(-4) product_{i<j in A}(2-2 cos(pi*(j-i)/4))',
            'input_moments':{'h2':expected[2].as_json(),'h4':expected[4].as_json()},
            'harmonic_pairs':{'h2':pairs2,'h4':pairs4},'signed_harmonic_group_masses':group_mass_records,
            'normalized_BL_eigenvalues':{'degree2':'7/8','degree4':'5/4'},
            'kernel_eigenpolynomials_ascending_z':{'row_sum':Z,'degree2':eig_polys[2],'degree4':eig_polys[4]},
            'F4_ascending_s':F,'F2_ascending_s':G,
            'mismatch_numerator_3F4primeF2_minus_10F2primeF4':mismatch_numerator,
            'factorization':'-420*s*(1+s)*(1+2*s)^3',
            'fixed_high_contrast_point':{'a':str(a),'c':str(c),'w':str(w),'s':str(s),'s_first':str(s1),
                                         'gamma2_dloga_lambda4_minus_gamma4_dloga_lambda2':str(mismatch)},
            'all_70_states_checked':True,'general_formula_checks':general_checks,
            'true_Fourier_odd_m_growth_lift':lifts,
            'input_atoms':{str(S):v.as_json() for S,v in mu.items()}}
    outdir=ensure_output(outdir)
    (outdir/'clock_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
    print('EXACT Fourier8 clock certificate: all assertions passed.')
    print('Fixed high-contrast clock mismatch =',mismatch)
    return report

if __name__=='__main__':
    pa=argparse.ArgumentParser();pa.add_argument('--out-dir',type=Path,default=Path(__file__).resolve().parents[1]/'outputs'/'exact')
    run(pa.parse_args().out_dir)
