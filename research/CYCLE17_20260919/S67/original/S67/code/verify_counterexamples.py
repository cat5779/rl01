#!/usr/bin/env python3
"""Independent Arb counterexamples to J <= W in actual sine DPP laws.
All indices are zero-based; exterior masks use ascending exterior indices.
No sampling or approximate eigenvalue entropy is used.
"""
from __future__ import annotations
import argparse
import json
from itertools import combinations
from pathlib import Path
from flint import arb, arb_mat, ctx


def kernel(n: int) -> list[list[arb]]:
    c = arb(19)/20
    pi = arb.pi()
    def entry(i: int, j: int) -> arb:
        if i == j:
            return arb(1)/2
        d = i-j
        if d % 2 == 0:
            return arb(0)
        # sin(pi*d/2) is exactly +/-1 for odd integral d.
        sign = 1 if d % 4 == 1 else -1
        return c*sign/(pi*d)
    return [[entry(i,j) for j in range(n)] for i in range(n)]


def conditional(K: list[list[arb]], pair: tuple[int,int], mask: int) -> dict:
    n = len(K)
    ext = [k for k in range(n) if k not in pair]
    bits = [(mask >> k) & 1 for k in range(len(ext))]
    Me = arb_mat([[K[i][j] - (1-bits[ii] if ii == jj else 0)
                   for jj,j in enumerate(ext)] for ii,i in enumerate(ext)])
    pext = Me.det()*((-1)**(len(ext)-sum(bits)))
    assert pext > 0
    C = arb_mat([[K[i][j] for j in ext] for i in pair])
    CT = arb_mat([[K[i][j] for j in pair] for i in ext])
    T = arb_mat([[K[i][j] for j in pair] for i in pair])-C*Me.inv()*CT
    u, v, z = T[0,0], T[1,1], T[0,1]
    t = z*z
    q11, q10 = u*v-t, u*(1-v)+t
    q01, q00 = (1-u)*v+t, (1-u)*(1-v)-t
    qs = (q11,q10,q01,q00)
    assert all(q > 0 for q in qs)
    J = (q10*q01/(q11*q00)).log()
    W = t*sum((1/q for q in qs),arb(0))
    return {'exterior_indices': ext, 'exterior_mask': mask,
            'exterior_bits': bits, 'p_exterior': pext,
            'u': u, 'v': v, 'z': z, 't': t,
            'q_11_10_01_00': qs, 'J': J, 'W': W, 'W_minus_J': W-J}


def serial(rec: dict) -> dict:
    ans = {}
    for k,v in rec.items():
        if isinstance(v,arb): ans[k] = str(v)
        elif isinstance(v,tuple): ans[k] = [str(x) if isinstance(x,arb) else x for x in v]
        else: ans[k] = v
    return ans


def run(precision: int) -> dict:
    ctx.prec = precision
    pointwise = None
    K = kernel(4)
    for pair in combinations(range(4),2):
        for mask in range(4):
            rec = conditional(K,pair,mask)
            if rec['W_minus_J'] < 0:
                pointwise = {'n': 4, 'pair': list(pair), **serial(rec)}
                break
        if pointwise is not None: break
    if pointwise is None:
        raise AssertionError('No certified n=4 pointwise counterexample was found.')

    averaged = None
    aggregate_J, aggregate_W = arb(0), arb(0)
    pair_summaries = []
    K = kernel(6)
    for pair in combinations(range(6),2):
        rows = [conditional(K,pair,mask) for mask in range(16)]
        norm = sum((r['p_exterior'] for r in rows),arb(0))
        assert abs(norm-1) < arb('1e-20')
        EJ = sum((r['p_exterior']*r['J'] for r in rows),arb(0))
        EW = sum((r['p_exterior']*r['W'] for r in rows),arb(0))
        aggregate_J += EJ
        aggregate_W += EW
        pair_summaries.append({'pair':list(pair),'E_J':str(EJ),'E_W':str(EW),'E_W_minus_E_J':str(EW-EJ)})
        if averaged is None and EW-EJ < 0:
            averaged = {'n': 6, 'pair': list(pair),
                        'exterior_indices': rows[0]['exterior_indices'],
                        'sum_exterior_probabilities': str(norm),
                        'E_J': str(EJ), 'E_W': str(EW),
                        'E_W_minus_E_J': str(EW-EJ),
                        'all_exterior_terms': [serial(r) for r in rows]}
    if averaged is None:
        raise AssertionError('No certified n=6 averaged counterexample was found.')
    return {'status':'PASS: both factor-one statements are DISPROVED',
            'precision_bits':precision,
            'parameters':{'rho':'1/2','c':'19/20','a_reference':'1/40'},
            'convention':'zero-based indices; exterior bits in ascending index order',
            'pointwise_counterexample':pointwise,
            'actual_law_averaged_counterexample':averaged,
            'finite_n6_all_pairs_compensation':{
                'sum_E_J':str(aggregate_J),'sum_E_W':str(aggregate_W),
                'sum_E_W_minus_E_J':str(aggregate_W-aggregate_J),
                'sign':('POSITIVE' if aggregate_W-aggregate_J>0 else 'NEGATIVE' if aggregate_W-aggregate_J<0 else 'UNRESOLVED'),
                'scope':'finite n=6 only; not an all-volume or entropy-rate assertion',
                'all_pair_summaries':pair_summaries}}


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--precision',type=int,default=192)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    if args.precision<96: ap.error('Use at least 96 bits.')
    result=run(args.precision)
    text=json.dumps(result,indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text+'\n')
    print(text)

if __name__=='__main__': main()
