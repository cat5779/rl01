#!/usr/bin/env python3
"""Collect exact expectation enclosures with complete 11-by-5 node coverage."""
from pathlib import Path
import argparse
from decimal import Decimal
import re

p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');args=p.parse_args()
rows={}
for line in Path(args.input).read_text().splitlines():
    if not line.startswith('NODE '):
        continue
    parts=line.split();j,k,lo,hi,den=map(int,parts[1:6])
    if (j,k) in rows:raise ValueError(f'duplicate node {(j,k)}')
    if den!=10**8 or not 0<=hi-lo<=2:raise ValueError('invalid enclosure width')
    if parts[6:8]!=['leaves','4194304']:raise ValueError('incomplete word coverage')
    match=re.search(r'mass \[([^,]+),([^]]+)\]',line)
    if match is None or not Decimal(match[1])<=1<=Decimal(match[2]):raise ValueError('normalization enclosure')
    rows[j,k]=(lo,hi,den)
if set(rows)!={(j,k) for j in range(11) for k in range(5)}:raise ValueError('incomplete tensor grid')
Path(args.output).write_text('# j k lower_numerator upper_numerator denominator\n'+''.join(f'{j} {k} {lo} {hi} {den}\n' for (j,k),(lo,hi,den) in sorted(rows.items())))
print('COMPLETE: 55 nodes; 4194304 configurations per node; interval width <= 2/100000000')
