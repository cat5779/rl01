#!/usr/bin/env python3
from pathlib import Path
import json, math
from defects import projection_probabilities,projection_residues,noise_jet,table_metrics

def main():
    rows=[];checks=0
    for n,k in [(2,1),(4,2),(5,2),(6,3),(8,4),(10,5)]:
        P=projection_probabilities(n,k)
        for p0 in [.23,.5,.74]:
            r=projection_residues(P,k,p0)
            assert r['alpha_plus']<=(n-k)**2/n+1e-10
            assert r['alpha_minus']<=k*k/n+1e-10
            assert r['negative_pair_residue']>=r['constant_diagonal_projection_lower_bound']-1e-10
            assert abs(r['diagonal_residue']+r['negative_pair_residue']-r['negative_total_residue'])<1e-10
            checks+=4
            vals=[]
            for eta in [.001,.0001,.00001]:
                q=noise_jet(P,eta,p0)[0];m=table_metrics(q,False)
                reg=m['pair_sum']+r['negative_pair_residue']/eta-4*k*(n-k)*math.log(1/eta)
                vals.append(reg)
                rows.append({'n':n,'k':k,'p0':p0,'eta':eta,**r,'pair_sum':m['pair_sum'],'eta_times_pair_sum':eta*m['pair_sum'],'pair_sum_after_pole_and_log_subtraction':reg,'eta_times_diagonal':eta*m['D'],'eta_times_L':eta*m['L']})
            assert abs(vals[2]-vals[1])<=abs(vals[1]-vals[0])*.25+1e-6
            checks+=1
    out=Path(__file__).resolve().parents[1]/'results'/'projection_residues.json'
    out.write_text(json.dumps({'status':'PASS','checks':checks,'kind':'finite floating-point check of proved residue formulas','rows':rows},indent=2))
    print('PASS:',checks,'residue and asymptotic checks')

if __name__=='__main__':main()
