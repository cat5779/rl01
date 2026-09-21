#!/usr/bin/env python3
"""Independent small-window replay of S75's star identity and drift bound.
These are floating-point diagnostics, NOT the proof or sign certificates.
"""
from __future__ import annotations
import itertools
import json
import math
from pathlib import Path
import numpy as np


def pair_mean(alpha: float, beta: float, s: float) -> float:
    p = np.array([alpha*beta-s, alpha*(1-beta)+s,
                  (1-alpha)*beta+s, (1-alpha)*(1-beta)-s])
    if np.min(p) <= 0:
        raise ValueError('Nonpositive pair probability')
    logs = (np.log1p(-s/(alpha*beta))
            + np.log1p(-s/((1-alpha)*(1-beta)))
            - np.log1p(s/(alpha*(1-beta)))
            - np.log1p(s/((1-alpha)*beta)))
    return float(s*np.sum(1/p) + logs)


def direct_star_mean(d: float, weights: np.ndarray, core_leaves: list[int]) -> float:
    n = len(weights)+1
    K = np.eye(n)*d
    K[0,1:] = K[1:,0] = np.sqrt(weights)
    result = 0.0
    mass = 0.0
    for word in itertools.product((0,1), repeat=n):
        A = K-np.diag(1-np.asarray(word))
        sign, logdet = np.linalg.slogdet(A)
        p = sign * (-1)**(n-sum(word)) * math.exp(logdet)
        if p <= 0:
            raise AssertionError('Invalid actual word probability')
        G = np.linalg.inv(A)
        potential = 0.0
        for i in core_leaves:
            h = float(G[0,i+1]**2)
            x = float(G[0,0]*G[i+1,i+1])
            potential += h+(x-h)*math.log1p(-h/x)
        result += p*potential
        mass += p
    assert abs(mass-1) < 2e-12
    return result


def reduced_star_mean(d: float, weights: np.ndarray, core_leaves: list[int]) -> float:
    total = 0.0
    for i in core_leaves:
        others = [float(w) for k,w in enumerate(weights) if k != i]
        for word in itertools.product((0,1), repeat=len(others)):
            ones = sum(word)
            p = d**ones*(1-d)**(len(others)-ones)
            beta = d + sum(w*((1-y)/(1-d)-y/d) for w,y in zip(others,word))
            total += p*pair_mean(d,beta,float(weights[i]))
    return total


def main():
    rng = np.random.default_rng(7504)
    records=[]
    max_error=0.0
    min_surplus=float('inf')
    for trial in range(60):
        d=float(rng.uniform(.06,.94))
        weights=rng.dirichlet(np.ones(6))*min(d,1-d)**2*float(rng.uniform(.1,.94))
        old=weights[:5]
        core=[0,2]
        direct=direct_star_mean(d,old,core)
        reduced=reduced_star_mean(d,old,core)
        direct_fine=direct_star_mean(d,weights,core)
        reduced_fine=reduced_star_mean(d,weights,core)
        err=max(abs(direct-reduced),abs(direct_fine-reduced_fine))
        max_error=max(max_error,err)
        coeff=256*(d**-3+(1-d)**-3)/(d*(1-d))
        bound=coeff*sum(float(weights[i])**3 for i in core)*float(weights[-1])**2
        surplus=direct_fine-direct-bound
        min_surplus=min(min_surplus,surplus)
        assert err < 2e-9
        assert surplus > -2e-10
        records.append({'d':d, 'drift':direct_fine-direct,
                        'proved_lower_bound':bound,'formula_error':err})
    result={'status':'PASS_FLOAT_DIAGNOSTICS_NOT_CERTIFICATE',
            'seed':7504,'random_legal_star_cases':60,
            'largest_full_word_volume':7,
            'maximum_formula_error':max_error,
            'minimum_drift_minus_theorem_bound':min_surplus,
            'numpy_version':np.__version__,'records':records}
    Path(__file__).with_name('S75_DIAGNOSTICS.json').write_text(
        json.dumps(result,indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))

if __name__=='__main__':
    main()
