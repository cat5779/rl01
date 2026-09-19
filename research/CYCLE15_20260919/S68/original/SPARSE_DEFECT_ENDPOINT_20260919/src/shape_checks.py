#!/usr/bin/env python3
"""Checks of the actual-insertion entropy formula and cyclic growth bounds."""
from pathlib import Path
import json,math
import numpy as np
from defects import projection_probabilities,projection_expansion,insertion_entropy_shape

def main():
    checks=0;rows=[];rng=np.random.default_rng(20260919)
    # The entropy formula holds for every strictly positive k-slice law.
    for n,k in [(3,1),(4,2),(5,2),(6,4)]:
        P=np.zeros(1<<n);ids=[y for y in range(1<<n) if y.bit_count()==k]
        P[ids]=rng.uniform(.1,2,len(ids));P/=P.sum();r=insertion_entropy_shape(P,k)
        assert r['swap_energy']>=-1e-10;checks+=1
        for p in [.23,.5,.74]:
            h=k*(n-k)
            expected=h/(p*(1-p))-2*h*math.log(p*(1-p))-4*h-n+r['shape_constant']
            assert abs(projection_expansion(P,k,p)['B2pp']-expected)<1e-9;checks+=1
    for n in range(2,17,2):
        k=n//2;P=projection_probabilities(n,k);r=insertion_entropy_shape(P,k)
        assert abs(r['swap_energy']-r['cyclic_swap_formula'])<2e-8;checks+=1
        assert abs(r['h_plus']-r['h_minus'])<1e-10;checks+=1
        assert abs(r['h_plus_plus']-r['h_minus_minus'])<1e-10;checks+=1
        B=projection_expansion(P,k,.5)['B2pp']
        B_alt=n*n*math.log(2)-n-2*r['swap_energy']-2*n*r['h_plus']-(n*n/2-n)*r['h_plus_plus']
        assert abs(B-B_alt)<2e-8;checks+=1
        assert r['h_plus']>=math.log(2)-1e-10;checks+=1
        if k>=2:
            assert r['h_plus_plus']>=2*math.log(2)-1e-10;checks+=1
        assert B<=-n-2*r['swap_energy']+2e-8;checks+=1
        lower=-n*n*math.log(n)+n*n*math.log(2)-n-2*n*math.log(k+1)
        if k>=2:lower-=(n*n/2-n)*math.log(math.comb(k+2,2))
        upper=-n*n*math.log(n)+n*n*math.log(2)-n+4*(n-1)*math.log(math.comb(n,k))
        assert lower-1e-8<=B<=upper+1e-8;checks+=1
        rows.append({'n':n,'k':k,**r,'B2pp_midpoint':B,'lower_bound':lower,'upper_bound':upper,
                     'geometry_upper_bound':-n-2*r['swap_energy'],'B2pp_over_n_squared':B/(n*n),'B2pp_over_n_squared_log_n':B/(n*n*math.log(n))})
    for k in [2,3,4]:
        n=2*k;A=rng.normal(size=(k,k))+1j*rng.normal(size=(k,k));V,_=np.linalg.qr(A)
        K=.5*np.block([[np.eye(k),V],[V.conj().T,np.eye(k)]])
        P=np.zeros(1<<n)
        for y in range(1<<n):
            if y.bit_count()==k:
                ix=[i for i in range(n) if (y>>i)&1];P[y]=np.linalg.det(K[np.ix_(ix,ix)]).real
        rr=insertion_entropy_shape(P,k);bb=projection_expansion(P,k,.5)['B2pp']
        assert rr['h_plus']>=math.log(2)-1e-10;checks+=1
        assert rr['h_minus']>=math.log(2)-1e-10;checks+=1
        assert rr['h_plus_plus']>=2*math.log(2)-1e-10;checks+=1
        assert rr['h_minus_minus']>=2*math.log(2)-1e-10;checks+=1
        assert bb<=-n-2*rr['swap_energy']+2e-8;checks+=1
    out=Path(__file__).resolve().parents[1]/'results'/'projection_shape_growth.json'
    out.write_text(json.dumps({'status':'PASS','checks':checks,'kind':'floating-point checks of proved entropy identities and growth bounds','rows':rows},indent=2))
    print('PASS:',checks,'actual-insertion entropy and cyclic growth checks')
if __name__=='__main__':main()
