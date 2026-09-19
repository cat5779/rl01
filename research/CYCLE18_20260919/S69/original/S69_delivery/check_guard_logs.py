#!/usr/bin/env python3
"""Verify that supplied guard logs contain a PASS for every word in every requested cell.
Usage: check_guard_logs.py CELLS LOG [LOG ...]
CELLS is comma/range syntax, e.g. 0-10 or 0,1,8-10.
"""
import re,sys
from pathlib import Path
if len(sys.argv)<3: raise SystemExit(__doc__)
def parse_cells(s):
    out=[]
    for part in s.split(','):
        if '-' in part:
            a,b=map(int,part.split('-',1));out.extend(range(a,b+1))
        else:out.append(int(part))
    return sorted(set(out))
cells=parse_cells(sys.argv[1])
pat=re.compile(r'^guard\s+(\d+)\s+cell\s+(\d+)\s+(PASS|FAIL)\s+nodes\s+(\d+)')
state={c:{} for c in cells};nodes={c:{} for c in cells}
for fn in sys.argv[2:]:
    for line in Path(fn).read_text().splitlines():
        m=pat.match(line)
        if not m:continue
        w,c,st,n=m.groups();w=int(w);c=int(c);n=int(n)
        if c not in state:continue
        if st=='PASS':state[c][w]='PASS';nodes[c][w]=n
        elif w not in state[c]:state[c][w]='FAIL';nodes[c][w]=n
for c in cells:
    missing=[w for w in range(256) if state[c].get(w)!='PASS']
    if missing:raise AssertionError(f'cell {c} missing/failing {missing}')
    print(f'GUARD LOG CHECK cell {c} PASS words 256 nodes {sum(nodes[c].values())}')
print(f'GUARD LOG CHECK ALL PASS cells {cells} words {256*len(cells)}')
