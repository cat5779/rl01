#!/usr/bin/env python3
from pathlib import Path
import json,math
from defects import projection_probabilities,projection_residues,diagonal_projection_finite_part,noise_jet,table_metrics

def main():
    rows=[];checks=0
    for n,k in [(2,1),(4,2),(5,2),(6,3),(8,4),(10,5)]:
      P=projection_probabilities(n,k)
      for p0 in [.23,.5,.74]:
        r=projection_residues(P,k,p0);d=diagonal_projection_finite_part(P,k,p0);g=n-k
        assert d['gamma_plus_plus']<=g*(g-1)+1e-9;checks+=1
        assert d['gamma_minus_minus']<=k*(k-1)+1e-9;checks+=1
        errors=[]
        for eta in [1e-3,1e-4,1e-5]:
          m=table_metrics(noise_jet(P,eta,p0)[0],False)
          observed=m['pair_sum']+r['negative_pair_residue']/eta-4*k*g*math.log(1/eta)
          err=abs(observed-d['pair_finite_part']);errors.append(err)
          rows.append({'n':n,'k':k,'p0':p0,'eta':eta,**d,'observed_subtracted_pair':observed,'absolute_error':err})
        assert errors[2]<.2*errors[1]+1e-7;checks+=1
    out=Path(__file__).resolve().parents[1]/'results'/'projection_finite_parts.json'
    out.write_text(json.dumps({'status':'PASS','checks':checks,'kind':'floating-point checks of exact finite-part formulas','rows':rows},indent=2))
    print('PASS:',checks,'finite-part checks')
if __name__=='__main__':main()
