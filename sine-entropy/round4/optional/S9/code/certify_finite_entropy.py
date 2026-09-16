#!/usr/bin/env python3
"""Whole-delta-interval complete Shannon curvature for the exact R=3 fixture.
All 128 probability jets are retained. This is a finite block, not a rate.
"""
from __future__ import annotations
import argparse, json
from fractions import Fraction as Q
from pathlib import Path
from atom_polynomials import build, interval_coefficients, evaluate_u, N
from dyadic import IV


def run():
    jets=evaluate_u(interval_coefficients(build(),IV.bounds(-Q(1,10000),Q(1,10000))),IV.point(1))
    if len(jets)!=1<<N or any(p.lo<=0 for p,_,_ in jets):
        raise ArithmeticError('all complete atoms must be strictly positive')
    fisher=sum((p1.sq()/p for p,p1,p2 in jets),IV.point(0))
    acceleration=sum((-p2*p.log() for p,p1,p2 in jets),IV.point(0))
    curvature=acceleration-fisher
    if curvature.hi>=0: raise ArithmeticError('finite complete entropy sign not certified')
    return {'classification':'AUTHOR_INTERVAL_FINITE_COMPLETE_ENTROPY_NOT_RATE',
            'u':'1','delta':['-1/10000','1/10000'],
            'H_second':curvature.rational(),'H_second_display':curvature.outward_decimal(),
            'Fisher':fisher.rational(),'acceleration':acceleration.rational(),
            'all_128_atom_jets':[[v.rational() for v in row] for row in jets]}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);parser.add_argument('--verify',type=Path)
    args=parser.parse_args();result=run()
    if args.verify and result!=json.loads(args.verify.read_text()):
        raise ArithmeticError('fresh complete-entropy certificate differs from frozen output')
    if args.output:args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS_FINITE_COMPLETE_ENTROPY_NOT_RATE',result['H_second_display'])
