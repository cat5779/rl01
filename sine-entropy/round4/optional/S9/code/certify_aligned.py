#!/usr/bin/env python3
"""Rigorous outward certificate for an integrated *route* obstruction.
No numerical quadrature assumptions: integrate the enclosing rectangle on
EVERY rational cell covering u in [1/4,1]; ds = -du/u is retained.
"""
from __future__ import annotations
import argparse,json,time,platform,hashlib
from pathlib import Path
from fractions import Fraction as Q
from atom_polynomials import *
from dyadic import *

def run(cells:int,delta:Q,begin:int=0,end:int|None=None):
    if end is None:end=cells
    if not 0<=begin<end<=cells:raise ValueError("bad covering segment")
    if delta < 0:raise ValueError('delta radius must be nonnegative')
    start=time.time();C=build();ivs=interval_coefficients(C,IV.bounds(-delta,delta))
    acc=[IV.point(0)for _ in range(N)];fisher=IV.point(0);acceler=IV.point(0)
    minp=SCALE;lo=Q(1,4);width=Q(3,4*cells)
    for j in range(begin,end):
        u=IV.bounds(lo+j*width,lo+(j+1)*width)
        js=evaluate_u(ivs,u)
        minp=min(minp,min(p[0].lo for p in js))
        layers,F,A=center_curvature(js)
        for k in range(N):acc[k]=acc[k]+width*layers[k]/u
        fisher=fisher+width*F/u;acceler=acceler+width*A/u
        if (j+1)%128==0:print("cells",j+1,"of",cells,"elapsed",round(time.time()-start,3),flush=True)
    total=sum(acc);paired=acc[1]+acc[N-2]
    return dict(schema=1,classification=('AUTHOR_FULL_COVER' if begin==0 and end==cells else 'PARTIAL_COVER_NOT_A_GLOBAL_SIGN_CERTIFICATE'),R=3,n=N,rho='1/2',c='5*pi/16',a='(1-5*pi/16)/2 + delta',delta_interval=[str(-delta),str(delta)],u_interval=['1/4','1'],cells=cells,begin_cell=begin,end_cell=end,bits=BITS,log_terms=TERMS,min_atom_lower=str(Q(minp,SCALE)),positions=POSITIONS,denominator=str(DEN),atom_polynomials=[[str(z)for z in row]for row in C],layer_integral_second_derivative=[z.rational()for z in acc],layer_display=[z.outward_decimal()for z in acc],complement_paired_layer_1_5=paired.rational(),total=total.rational(),total_display=total.outward_decimal(),fisher=fisher.rational(),acceleration=acceler.rational(),strict_tests={'all_atoms_positive':minp>0,'segment_paired_integral_curvature_negative':paired.hi<0,'segment_full_integral_curvature_positive':total.lo>0},elapsed_seconds=time.time()-start,python=platform.python_version())

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--cells',type=int,default=1024);p.add_argument('--delta',default='0');p.add_argument('--output',type=Path);p.add_argument('--begin',type=int,default=0);p.add_argument('--end',type=int)
    a=p.parse_args()
    if a.cells<=0:raise ValueError('cells must be positive')
    result=run(a.cells,Q(a.delta),a.begin,a.end)
    print(json.dumps({k:v for k,v in result.items()if k not in ['atom_polynomials','positions','layer_integral_second_derivative','total','fisher','acceleration']},indent=2))
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2)+'\n')
