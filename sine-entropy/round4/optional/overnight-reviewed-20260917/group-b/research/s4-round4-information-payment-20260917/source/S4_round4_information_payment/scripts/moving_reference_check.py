#!/usr/bin/env python3
"""Exact check of all changing-output-reference terms under a finite experiment.

This supplemental two-outcome experiment is not a numerical substitute for the
Gaussian proof. It tests the independent-observation chain and second jets at a
nonmidpoint, with actual changing output weights and compatible tilted priors.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from math_core import (F, ZERO, ONE, bits, fs, require, fourier_law,
                       contraction_law, moments, likelihood, jets,
                       log_interval, interval_add, interval_scale,
                       show_interval, safe_output)
from exact_check import add_coeff, kappa_interval
ROOT = Path(__file__).resolve().parents[1]

def compact(d):
    return {k: v for k, v in d.items() if v}

def info_data(xs, mu, a, c):
    n=len(xs[0]); rows=jets(xs,mu,a,c); q,_=moments(xs,mu)
    D=sum(((1-qi)/(a*(1-a))+qi/((a+c)*(1-a-c)) for qi in q),ZERO)
    Fisher=sum((r['p'][1]**2/r['p'][0] for r in rows.values()),ZERO)
    A={}; psi=ZERO
    for y,row in rows.items():
        add_coeff(A,row['p'][0],-row['p'][2])
        e=[c/(a*(a+c)) if yi else c/((1-a)*(1-a-c)) for yi in y]
        psi+=row['p'][0]*sum((e[i]**2*row['C'][i][i] for i in range(n)),ZERO)
    return dict(rows=rows,D=D,Fisher=Fisher,A=compact(A),constant=D-Fisher,Psi=psi)

def evaluate(coeff, constant=ZERO):
    ans=(constant,constant)
    for arg,weight in coeff.items():
        ans=interval_add(ans,interval_scale(log_interval(arg),weight))
    return ans

def run_case(name,xs,mu,a,c):
    n=len(xs[0]); original=info_data(xs,mu,a,c)
    # Omega sees X_0 through a separate fixed BSC(1/7), independent of a.
    omega=[]
    for z in (0,1):
        w=[m*(F(6,7) if z==x[0] else F(1,7)) for x,m in zip(xs,mu)]
        prob=sum(w); post=[u/prob for u in w]
        omega.append((z,prob,post,info_data(xs,post,a,c)))
    require(sum(prob for _,prob,_,_ in omega)==1,'Omega normalization')
    require(all(sum(prob*post[j] for _,prob,post,_ in omega)==mu[j] for j in range(len(xs))),
            'Actual posterior-weight compatibility, before applying channel')
    for y, row in original['rows'].items():
        require(all(sum(prob*data['rows'][y]['p'][j] for _,prob,_,data in omega)==row['p'][j]
                    for j in range(3)), 'Changing output mixture agrees at orders 0,1,2')
    require(sum(prob*data['D'] for _,prob,_,data in omega)==original['D'],
            'Complete Fisher budget averages linearly')
    chain_coeff=dict(original['A']); remainder_coeff={}
    chain_const=original['constant']; remconst=ZERO; psibar=ZERO
    direct_coeff={}; Fbar=ZERO; response_mass=ZERO; first_response_mass=ZERO
    posterior_checks=0
    for z,prob,post,data in omega:
        for arg,coef in data['A'].items():
            add_coeff(chain_coeff,arg,-prob*coef)
            add_coeff(remainder_coeff,arg,prob*coef)
        chain_const-=prob*data['constant']; remconst+=prob*data['constant']
        psibar+=prob*data['Psi'];Fbar+=prob*data['Fisher']
        for y, row in data['rows'].items():
            p,p1,p2=row['p']; output_p=original['rows'][y]['p'][0]
            # Entire Eq (1.11): p_z'' log(p_z/p) + Fbar - F.
            add_coeff(direct_coeff,p,prob*p2)
            add_coeff(direct_coeff,output_p,-prob*p2)
            # Independently recover posterior second responses using full likelihood jets.
            nuprime=[];nusecond=[]
            for x,prior_mass,nu in zip(xs,post,row['mu']):
                g=[a+c*xi if yi else 1-a-c*xi for xi,yi in zip(x,y)]
                t=[F(2*yi-1)/gi for yi,gi in zip(y,g)]
                score=sum(t); accel=score*score-sum(ti*ti for ti in t)
                first=nu*(score-p1/p)
                second=nu*(accel-p2/p-2*(p1/p)*(score-p1/p))
                nuprime.append(first);nusecond.append(second)
            require(sum(nuprime)==0 and sum(nusecond)==0,'Posterior derivative normalization')
            for i in range(n):
                require(sum(v*x[i] for v,x in zip(nuprime,xs))==row['r1'][i],
                        'First posterior response from independent score formula')
                require(sum(v*x[i] for v,x in zip(nusecond,xs))==row['r2'][i],
                        'Second posterior response from independent score formula')
            first_response_mass+=prob*p*sum(abs(v) for v in nuprime)
            response_mass+=prob*p*sum(abs(v) for v in nusecond)
            posterior_checks+=len(xs)
    direct_const=Fbar-original['Fisher']
    require(compact(chain_coeff)==compact(direct_coeff),
            'Chain and moving-reference formulas have exactly identical log coefficients')
    require(chain_const==direct_const,'All changing-reference Fisher terms retained exactly')
    rem=evaluate(compact(remainder_coeff),remconst)
    kap=kappa_interval(a,c)
    require(rem[0]>=0 and rem[1]<=kap[0]*psibar,'Completed conditional correction is nonnegative and paid')
    require(first_response_mass>0 and response_mass>0,'Nonmidpoint really tests first and second responses')
    direct=evaluate(compact(direct_coeff),direct_const)
    # Omission of -F would add the nonzero actual output Fisher; record this explicitly.
    require(original['Fisher']>0,'The changing unconditional reference is not constant')
    return dict(name=name,n=n,a=fs(a),c=fs(c),experiment='Omega=X_0 xor Bernoulli(1/7), independent channel randomness',
                experiment_weights=[fs(prob) for _,prob,_,_ in omega],
                actual_output_Fisher=fs(original['Fisher']),conditional_output_Fisher=fs(Fbar),
                moving_reference_constant=fs(direct_const),mutual_information_second=show_interval(direct),
                conditional_information_second=show_interval(rem),averaged_diagonal_score_uncertainty=fs(psibar),
                first_response_l1_average=fs(first_response_mass),second_response_l1_average=fs(response_mass),
                exact_log_coefficient_identity=True,posterior_atom_response_checks=posterior_checks,
                omission_of_minus_output_Fisher_would_add=fs(original['Fisher']),all_checks_passed=True)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out-dir',type=Path,default=ROOT/'output'/'reference_run')
    args=ap.parse_args();out=safe_output(args.out_dir,ROOT)
    specs=[]
    xs,mu=fourier_law(4,2);specs.append(('contiguous_P_4_2_nonmid',xs,mu,F(1,80),F(19,20)))
    xs,mu=contraction_law();specs.append(('strict_contraction_nonmid',xs,mu,F(1,100),F(19,20)))
    results=[run_case(*args) for args in specs]
    data=dict(assurance='Exact finite reference and posterior-jet tests; not a replacement for the Gaussian analytic proof.',
              cases=results,all_checks_passed=True)
    with (out/'moving_reference_certificate.json').open('w',encoding='utf-8',newline='\n') as f:
        json.dump(data,f,ensure_ascii=False,indent=2);f.write('\n')
    print('PASS exact changing-reference and posterior-response identities in 2 nonmidpoint experiments')
if __name__=='__main__':main()
