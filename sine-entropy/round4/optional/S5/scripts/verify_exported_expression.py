#!/usr/bin/env python3
"""Second exact arithmetic check of the exported nine-log remainder.

Uses an alternating log(1+t) series and powers of 3/2. This does not import
or use exact_common.log_q, which uses an atanh series and powers of 2.
It independently evaluates the exported expression; its identification with
the geometric remainder is proved in proof.md and checked by the generator.
This is an internal cross-check, not independent external certification.
"""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as Q
from pathlib import Path

TERMS=120

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def scale(x,c):return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def unit_log(y):
    if not Q(1)<=y<=Q(3,2):raise ValueError('Argument outside reduction interval.')
    t=y-1;power=t;partial=Q(0)
    for j in range(1,TERMS+1):
        partial+=power/j if j%2 else -power/j
        power*=t
    # TERMS is even: the even partial sum is a lower bound; the next odd
    # partial sum is an upper bound, by the alternating-series theorem.
    return (partial,partial+power/(TERMS+1))

LOG_BASE=unit_log(Q(3,2))
def log_bounds(x):
    if x<=0:raise ValueError('Positive rational required.')
    m=0;y=x
    while y>=Q(3,2):y/=Q(3,2);m+=1
    while y<1:y*=Q(3,2);m-=1
    return add(unit_log(y),scale(LOG_BASE,m))

def outward(bounds,digits=30):
    scale10=10**digits
    nums=[(bounds[0]*scale10).__floor__(),(bounds[1]*scale10).__ceil__()]
    def fmt(n):
        sign='-' if n<0 else '';n=abs(n)
        return f'{sign}{n//scale10}.{n%scale10:0{digits}d}'
    return {'lower':fmt(nums[0]),'upper':fmt(nums[1])}

def main():
    if not __debug__:raise RuntimeError('Run without -O; assertions must be enabled.')
    root=Path(__file__).resolve().parents[1]
    parser=argparse.ArgumentParser()
    parser.add_argument('--certificate',type=Path,default=root/'evidence'/'fourier6_certificate.json')
    parser.add_argument('--out-dir',type=Path,default=root/'outputs'/'second_arithmetic')
    args=parser.parse_args();out=args.out_dir.resolve()
    if out==root or any(out==p or p in out.parents for p in [root/'scripts',root/'evidence']):
        raise ValueError('Output may not overwrite sources or frozen evidence.')
    doc=json.loads(args.certificate.read_text())
    row=next(x for x in doc['cases'] if (x['n'],x['k'],x['a'],x['c'])==(6,2,'49/100','1/2'))
    expr=row['aggregate_remainder_exact_log_expression'];c=Q(expr['constant'])
    bounds=(c,c)
    for item in expr['terms']:
        bounds=add(bounds,scale(log_bounds(Q(item['argument'])),Q(item['coefficient'])))
    assert len(expr['terms'])==9
    assert Q(-184,1000)<bounds[0]<=bounds[1]<Q(-183,1000)
    report={'status':'EXACT_FINITE_CERTIFICATE_CROSSCHECK','terms':len(expr['terms']),
            'method':'alternating log(1+t), 120 even terms plus next odd term; powers of 3/2 range reduction',
            'aggregate_remainder':outward(bounds),
            'certified_inequality':'-184/1000 < R_tr < -183/1000',
            'limitation':'Arithmetic cross-check by the same authoring agent; not external certification.'}
    out.mkdir(parents=True,exist_ok=True)
    (out/'exported_expression_check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
