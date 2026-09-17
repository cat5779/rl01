#!/usr/bin/env python3
"""Exact finite checks for S4 round 4. Standard library only; fresh outputs.

Every logarithm is enclosed with rational series and a rigorous rational tail.
Finite checks supplement the all-dimension proofs; they do not replace them.
"""
from __future__ import annotations
import argparse
import itertools
import json
import math
from pathlib import Path
from math_core import (F, ZERO, ONE, bits, dot, fs, require, fourier_law,
                       contraction_law, moments, likelihood, jets, tilt,
                       log_interval, interval_add, interval_scale,
                       show_interval, safe_output)

ROOT = Path(__file__).resolve().parents[1]

def kappa_interval(a: F, c: F):
    """Rigorous interval for the minimum of the three proved constants."""
    rad = 1-c**4
    scale = 10**24
    k = math.isqrt((rad.numerator*scale*scale)//rad.denominator)
    sl, sh = F(k,scale), F(k+1,scale)
    require(sl*sl <= rad <= sh*sh and sl > 0, 'Sqrt enclosure')
    candidates = [(1/sh, 1/sl)]
    theta = log_interval((a+c)*(1-a)/(a*(1-a-c)))
    one_minus = 1-a*(1-a-c)/((a+c)*(1-a))
    candidates.append((theta[0]/one_minus, theta[1]/one_minus))
    if c*c <= F(23,25):
        candidates.append((F(2),F(2)))
    return min(x[0] for x in candidates), min(x[1] for x in candidates)

def add_coeff(dct, key, value):
    dct[key] = dct.get(key, ZERO)+value

def check_case(name, xs, mu, a: F, c: F):
    n = len(xs[0])
    require(0 < c < 1 and 0 < a < 1-c, 'Legal interior parameters')
    q, prior_C = moments(xs, mu)
    for i in range(n):
        for j in range(n):
            require(i == j or prior_C[i][j] <= 0, 'Prior negative covariance')
    rows = jets(xs, mu, a, c)
    D = sum(((1-z)/(a*(1-a))+z/((a+c)*(1-a-c)) for z in q), ZERO)
    marginal_F = sum((1/((a+c*z)*(1-a-c*z)) for z in q), ZERO)
    total_F, Psi, energy, S, M, Q2, mean_tangent = [ZERO]*7
    atom_acc = (ZERO, ZERO)
    coeff_atoms = {}
    for y, row in rows.items():
        p, p1, p2 = row['p']
        C, r = row['C'], row['r']
        e = [c/(a*(a+c)) if yi else c/((1-a)*(1-a-c)) for yi in y]
        total_F += p1*p1/p
        Psi += p*sum((e[i]*e[i]*C[i][i] for i in range(n)), ZERO)
        energy += p*sum((e[i]*e[j]*C[i][j] for i in range(n) for j in range(n)), ZERO)
        S += p*sum((-e[i]*e[j]*C[i][j] for i in range(n) for j in range(i+1,n)), ZERO)
        M += p*sum((C[i][i] for i in range(n)), ZERO)
        require(all(C[i][j] <= 0 for i in range(n) for j in range(n) if i != j),
                'Compatible full-posterior negative covariance')
        atom_acc = interval_add(atom_acc, interval_scale(log_interval(p), -p2))
        add_coeff(coeff_atoms, p, -p2)
        d = [r[i]-q[i] for i in range(n)]
        mean_tangent += p*dot(row['r1'], row['r1'])
        Q2 += p2*dot(d,d)/2+2*p1*dot(d,row['r1'])+p*(dot(row['r1'],row['r1'])+dot(d,row['r2']))
    require(D-total_F == energy, 'Complete / observed / missing Fisher identity')
    require(energy >= 0 and Psi-energy == 2*S, 'Signed covariance energy decomposition')
    require(Psi <= D-marginal_F, 'Actual-average scalar Bayes variance payment')
    kap = kappa_interval(a,c)
    pair_acc, pair_S = (ZERO, ZERO), ZERO
    p2_from_pairs = {y: ZERO for y in rows}
    coeff_pairs = {}
    pairs = rebasings = 0
    smallest_pair_margin = None
    s0 = (1-c*c)/2
    for i,j in itertools.combinations(range(n),2):
        rest = [l for l in range(n) if l != i and l != j]
        for yrest in bits(len(rest)):
            base = [0]*n
            for l, yi in zip(rest,yrest):
                base[l] = yi
            weights = [m*likelihood(x,base,a,c,rest) for x,m in zip(xs,mu)]
            prest = sum(weights)
            post = [w/prest for w in weights]
            qr, Cr = moments(xs,post)
            w = -Cr[i][j]
            require(w >= 0, 'Extrinsic covariance sign')
            pp = {}
            for u,v in bits(2):
                y = list(base)
                y[i],y[j] = u,v
                y = tuple(y)
                p = rows[y]['p'][0]/prest
                pp[u,v] = p
                su, sv = F(2*u-1), F(2*v-1)
                alpha = a+c*qr[i] if u else 1-a-c*qr[i]
                beta = a+c*qr[j] if v else 1-a-c*qr[j]
                require(p == alpha*beta-c*c*su*sv*w, 'True two-site probability')
                ti = a*(a+c) if u else (1-a)*(1-a-c)
                tj = a*(a+c) if v else (1-a)*(1-a-c)
                wp = -rows[y]['C'][i][j]
                require(wp == w*ti*tj/(p*p), 'Exact binary/DPP compatible tilt rebasing')
                p2_from_pairs[y] += 2*su*sv*prest
                add_coeff(coeff_pairs, rows[y]['p'][0], -2*su*sv*prest)
                rebasings += 1
            require(sum(pp.values()) == 1, 'Two-site normalization')
            qd, qc = pp[0,0]*pp[1,1], pp[0,1]*pp[1,0]
            d = qc-qd
            require(d == c*c*w >= 0, 'Negative determinant')
            diag = pp[0,0]+pp[1,1]
            require(diag >= s0, 'Channel corner sum lower bound')
            ratio = qc/qd
            log_odds = log_interval(ratio)
            den = d*sum((1/p for p in pp.values()), ZERO)
            if d:
                require(log_odds[1] <= kap[0]*den,
                        'Rational certificate of scalar log-odds inequality')
                margin = kap[0]*den-log_odds[1]
                smallest_pair_margin = margin if smallest_pair_margin is None else min(smallest_pair_margin,margin)
            else:
                require(log_odds == (ZERO,ZERO) and den == 0, 'Independent-pair zero limit')
            # The identity is rational, with exp(t) represented by ratio.
            require(den == (ratio-1)*diag+(1-1/ratio)*(1-diag), 'Scalar log-mean denominator identity')
            pair_acc = interval_add(pair_acc, interval_scale(log_odds, 2*prest))
            pair_S += prest*den
            pairs += 1
    require(all(p2_from_pairs[y] == row['p'][2] for y,row in rows.items()), 'Full multi-affine probability acceleration')
    require({k:v for k,v in coeff_atoms.items() if v} == {k:v for k,v in coeff_pairs.items() if v},
            'Exact log-linear coefficient identity, not a numerical log comparison')
    require(pair_S == S, 'All pairs rebased before actual-output averaging')
    require(atom_acc[0] <= pair_acc[1] and pair_acc[0] <= atom_acc[1], 'Independent rational log enclosures overlap')
    require(pair_acc[0] >= 0, 'Nonnegative complete acceleration')
    require(pair_acc[1] <= 2*kap[0]*S or S == 0, 'Accelerative payment')
    I2 = (pair_acc[0]+energy,pair_acc[1]+energy)
    H2 = (pair_acc[0]-total_F,pair_acc[1]-total_F)
    require(I2[0] >= 0, 'Input/output information curvature is nonnegative')
    require(I2[1] <= kap[0]*Psi or Psi == 0, 'New completed information-curvature bound')
    rank = sum(xs[0]) if len({sum(x) for x in xs}) == 1 else None
    if rank is not None and a == (1-c)/2:
        require(energy == 0 and mean_tangent == 0, 'Midpoint tangents vanish but are not the payment')
    rbar = sum(q)/n
    dcentral = (1-c)/4
    regional = F(37,40) <= c <= F(959,1000) and dcentral <= a <= 3*dcentral and (rbar <= F(1,100) or rbar >= F(99,100))
    if regional:
        require(H2[1] <= -F(11,250)*n, 'New uniform regional theorem checked at this finite fixture')
    return dict(case=name,n=n,rank=rank,a=fs(a),c=fs(c),mean_density=fs(rbar),
                complete_Fisher=fs(D),actual_output_Fisher=fs(total_F),missing_Fisher=fs(energy),
                diagonal_score_uncertainty=fs(Psi),weighted_edge_sum=fs(S),posterior_MMSE=fs(M),
                one_site_missing_budget=fs(D-marginal_F),kappa=show_interval(kap),
                acceleration=show_interval(pair_acc),information_second=show_interval(I2),entropy_second=show_interval(H2),
                instantaneous_Q_second=fs(Q2),mean_posterior_tangent=fs(mean_tangent),
                factor_one_fails_at_this_fixture=I2[0] > Psi,
                pair_extrinsic_checks=pairs,compatible_rebasing_checks=rebasings,
                minimum_nonzero_pair_slack=show_interval((smallest_pair_margin,smallest_pair_margin)) if smallest_pair_margin is not None else None,
                in_new_region=regional,all_checks_passed=True)

def scalar_and_region_certificate():
    # Uniform scalar proof: e^(12/5)>11 supplies the minimum test in proof.md.
    exp_lower = sum((F(12,5)**j/math.factorial(j) for j in range(9)),ZERO)
    require(exp_lower > 11, 'Exact exponential-series certificate')
    require(15**2 < 241 < 16**2, 'Exact critical-root bracket')
    require(F(25+16,4) < 11, 'Critical z lies below 11')
    require(F(61,25)-F(12,5) == F(1,25), 'Strict positive local minimum margin')
    cmax,rmax = F(959,1000),F(1,100)
    dmin = (1-cmax)/4
    require((1-cmax*cmax)/2 >= F(1,25), 'Factor-2 channel range')
    require(cmax/(dmin*(1-dmin)) <= 95, 'Uniform channel reciprocal-variance bound')
    product = (1+2*rmax)*(1+95*rmax)
    require(product == F(1989,1000), 'Uniform density product')
    strength = 4*(2-product)
    require(strength == F(11,250), 'Uniform curvature strength')
    old_threshold = F(1,80)**5/(5*F(19,20)*F(1,20))
    entropy_lower = 2*rmax*(1-rmax)
    require(entropy_lower > old_threshold, 'New density is not covered by the old author criterion')
    return dict(scalar_s_threshold='1/25',exp_argument='12/5',exp_truncation_degree=8,
                exp_lower=fs(exp_lower),exp_lower_minus_11=fs(exp_lower-11),
                critical_root_square='241',critical_root_bracket=['15','16'],
                strict_scalar_minimum_margin='1/25',c_interval=['37/40',fs(cmax)],
                density_intervals=[['0',fs(rmax)],['99/100','1']],
                offset_interval='[(1-c)/4, 3(1-c)/4]',
                s_min_at_cmax=fs((1-cmax*cmax)/2),
                cmax_over_d_variance=fs(cmax/(dmin*(1-dmin))),
                reciprocal_bound_slack=fs(95*dmin*(1-dmin)-cmax),
                product_bound=fs(product),curvature_strength_per_site=fs(strength),
                strong_Jensen_coefficient=fs(strength/2),
                old_round3_entropy_threshold_at_c95_d1over80=fs(old_threshold),
                binary_entropy_lower_at_density_one_percent=fs(entropy_lower),all_checks_passed=True)

def non_dpp_scope_gate():
    xs=[(1,1,0,0,0),(0,0,1,1,0)]
    mu=[F(1,2),F(1,2)]
    q,C=moments(xs,mu)
    require(C[0][1] == F(1,4) > 0, 'Non-DPP homogeneous gate violates covariance hypothesis')
    # It is intentionally not fed to check_case as if the DPP hypothesis held.
    return dict(states=[list(x) for x in xs],weights=['1/2','1/2'],rank=2,
                positive_covariance_pair=[0,1],covariance='1/4',
                conclusion='Excluded by a required structural hypothesis; no universal homogeneous-law claim.',
                all_checks_passed=True)

def fixture_list(quick: bool):
    out=[]
    for a in [F(1,40),F(1,80),F(1,1000)]:
        xs,mu=fourier_law(4,2);out.append(('contiguous_P_4_2',xs,mu,a,F(19,20)))
    for a in [F(1,40),F(1,1000)]:
        out.append(('nonuniform_rank_one_2',[(1,0),(0,1)],[F(1,100),F(99,100)],a,F(19,20)))
    xs=bits(4);xs=[x for x in xs if sum(x)==1]
    mu=[F(89,100),F(7,100),F(3,100),F(1,100)]
    out.append(('nonuniform_rank_one_4',xs,mu,F(1,40),F(19,20)))
    xs,mu=contraction_law();out.append(('strict_contraction',xs,mu,F(1,40),F(19,20)))
    out.append(('strict_contraction_high_c_general_kappa',xs,mu,F(1,200),F(99,100)))
    # Tr(original K)=13/10; scaling by 3/130 gives mean diagonal exactly 1/100.
    xs,mu=contraction_law(F(3,130))
    for a in [F(41,4000),F(123,4000)]:
        out.append(('one_percent_strict_contraction',xs,mu,a,F(959,1000)))
    if not quick:
        for n,k,a,c in [(6,2,F(1,40),F(19,20)),(6,3,F(1,40),F(19,20)),
                        (6,3,F(41,4000),F(959,1000)),(6,3,F(1,200),F(99,100))]:
            xs,mu=fourier_law(n,k);out.append((f'contiguous_P_{n}_{k}',xs,mu,a,c))
        xs,mu=fourier_law(6,3)
        multipliers=[F(1,10**6),F(10**6),F(2,3),F(5,2),F(9),F(1,11)]
        mm=tilt(xs,mu,multipliers)
        for a in [F(1,40),F(1,80)]:
            out.append(('contiguous_P_6_3_positive_field',xs,mm,a,F(19,20)))
    return out

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out-dir',type=Path,default=ROOT/'output'/'exact_run')
    ap.add_argument('--quick',action='store_true')
    args=ap.parse_args()
    out=safe_output(args.out_dir,ROOT)
    results=[]
    for spec in fixture_list(args.quick):
        result=check_case(*spec)
        results.append(result)
        print(f"PASS {result['case']}, a={result['a']}, c={result['c']}",flush=True)
    report=dict(format='S4-round4-completed-information-v1',
                assurance='Exact finite checks and analytic-constant certificates; the growing-family proof is analytical.',
                log_enclosure='52-term rational atanh series with rigorous tail, power-of-two reduction, outward rational rounding',
                quick=args.quick,scalar_and_region=scalar_and_region_certificate(),cases=results,
                non_DPP_scope_gate=non_dpp_scope_gate(),
                total_pair_extrinsic_checks=sum(r['pair_extrinsic_checks'] for r in results),
                total_compatible_rebasing_checks=sum(r['compatible_rebasing_checks'] for r in results),
                all_checks_passed=True)
    target=out/'exact_certificate.json'
    with target.open('w',encoding='utf-8',newline='\n') as f:
        json.dump(report,f,ensure_ascii=False,indent=2)
        f.write('\n')
    print(f'WROTE {target}',flush=True)

if __name__ == '__main__':
    main()
