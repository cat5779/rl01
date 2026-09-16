#!/usr/bin/env python3
"""Independent rational check of scaled-noise jets, including the u=0 extension.
The wide auxiliary box is a legal kernel box, not a claim of negative noise time.
"""
from __future__ import annotations
import argparse,json,time
from fractions import Fraction as Q
from pathlib import Path
from atom_polynomials import build,jets_fraction,b_integer,DEN,N
from check_exact_atoms import determinant_inverse
from certify_full_r3 import scaled_coefficients
from dyadic import IV,horner,SCALE


def need(ok,msg):
    if not ok:raise ArithmeticError(msg)


def run():
    start=time.time();C=build();B=b_integer();nodes=[];count=0
    for u,d in [(Q(0),Q(0)),(Q(0),Q(1,24)),(Q(1,4),Q(1,24)),(Q(1),-Q(1,24)),(Q(21,20),Q(0)),(Q(21,20),Q(1,24))]:
        bounds=[[horner(co,IV.point(u))for co in row]for row in scaled_coefficients(C,IV.point(d))]
        K=[[Q(i==j,2)+u*(Q(B[i][j],192)+(d if i==j else 0))for j in range(N)]for i in range(N)]
        rows=[]
        for y in range(1<<N):
            M=2*y.bit_count()-N
            if u==0:
                wanted=[Q(1,1<<N),Q(2*M,1<<N),Q(4*(M*M-N),1<<N)]
            else:
                A=[[K[i][j]-(1-(y>>i&1) if i==j else 0)for j in range(N)]for i in range(N)]
                det,inv=determinant_inverse(A);p=(-1)**(N-y.bit_count())*det
                need(p>0 and inv is not None,'wide-box exact atom positivity')
                tr=sum(inv[i][i]for i in range(N));tr2=sum(inv[i][j]*inv[j][i]for i in range(N)for j in range(N))
                wanted=[p,p*tr,p*(tr*tr-tr2)]
                actual=jets_fraction(C[y],u,d)
                need(wanted==[actual[j]/u**j for j in range(3)],'wide exact scaled determinant jets');count+=1
            for j in range(3):
                z=bounds[y][j];need(Q(z.lo,SCALE)<=wanted[j]<=Q(z.hi,SCALE),'scaled interval does not enclose exact jet');count+=1
            rows.append(wanted)
        need([sum(row[j]for row in rows)for j in range(3)]==[1,0,0],'scaled normalization');count+=1
        if not u:
            total=Q(0)
            for y in range(1<<N):
                if y&(1<<(N//2)):continue
                x,x1,_=rows[y];z,z1,_=rows[y+(1<<(N//2))]
                need(x==z,'fair reference pair');total+=(x+z)*(x1/x-z1/z)**2/2
            need(total==8,'fair limit is exactly 8');count+=1
        nodes.append({'u':str(u),'delta':str(d),'all_128_scaled_atom_jets':[[str(q)for q in row]for row in rows]})
    return {'status':'PASS_SCALED_JETS_AND_FAIR_LIMIT','grouped_comparisons':count,'nodes':nodes,'elapsed_seconds':time.time()-start,
            'scope':'Direct rational signed matrices cross-check the polynomial interval engine, including u=0. Not an independent reviewer.'}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);a=p.parse_args();r=run()
    if a.output:a.output.write_text(json.dumps(r,indent=2)+'\n')
    print(r['status'],r['grouped_comparisons'])
