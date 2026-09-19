#!/usr/bin/env python3
"""Check exact rectangular guard coverage; this does not replace the interval proof."""
from pathlib import Path
from fractions import Fraction as F
import argparse
p=argparse.ArgumentParser();p.add_argument('input');a=p.parse_args()
leaves={z:[] for z in range(256)};jobs=set();nodes=0
for line in Path(a.input).read_text().splitlines():
    if 'FAILED' in line or line.startswith('ERROR'):raise ValueError(line)
    s=line.split()
    if not s:continue
    if s[0]=='JOB':
        j=int(s[1]);assert s[2]=='PROVED' and j not in jobs;jobs.add(j)
    if s[0]=='LEAF':
        z,al,ah,ad,rl,rh,rd=map(int,s[1:8]);assert z in leaves
        l,h,r,t=F(al,ad),F(ah,ad),F(rl,rd),F(rh,rd)
        assert F(21,1000)<=l<h<=F(3,125)
        assert F(1,3)<=r<t<=F(1009,3000)
        leaves[z].append((l,h,r,t));nodes+=int(s[9])
assert jobs==set(range(1536))
for z,rects in leaves.items():
    xs=sorted({F(21,1000),F(3,125)}|{x for q in rects for x in q[:2]})
    ys=sorted({F(1,3),F(1009,3000)}|{y for q in rects for y in q[2:]})
    for x0,x1 in zip(xs,xs[1:]):
        for y0,y1 in zip(ys,ys[1:]):
            x,y=(x0+x1)/2,(y0+y1)/2
            assert sum(l<x<h and r<y<t for l,h,r,t in rects)==1,(z,x,y)
print('COVERAGE PROVED: 256 guard words, 1536 jobs,',sum(map(len,leaves.values())),'interior-disjoint closed leaves')
print('All 256 parameter rectangles exactly equal [21/1000,3/125] x [1/3,1009/3000].')
print('Completed-leaf inner nodes:',nodes,'(excludes subdivided parent attempts).')
