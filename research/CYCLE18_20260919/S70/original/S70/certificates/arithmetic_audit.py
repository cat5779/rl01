#!/usr/bin/env python3
"""Parse extended-precision hexadecimal numbers as EXACT rationals.
Check outward primitive bounds and log bounds against rational atanh series.
"""
from fractions import Fraction as F
from pathlib import Path
import re,json

def hx(s):
 m=re.fullmatch(r'(-?)0x([0-9a-f]+)\.([0-9a-f]+)p([+-]?\d+)',s);assert m,s
 z=F(int(m[2]+m[3],16),16**len(m[3]));e=int(m[4]);z=z*(2**e if e>=0 else F(1,2**(-e)));return -z if m[1] else z

def atanhs(t,N=100):
 s=F(0);p=t;t2=t*t
 for j in range(N):s+=p/F(2*j+1);p*=t2
 return 2*s,2*(s+p/F(2*N+1)/(1-t2))
LOG2=atanhs(F(1,3))
def logbounds(x):
 assert x>=1;k=0
 while x>=2:x/=2;k+=1
 lo,hi=atanhs((x-1)/(x+1));return lo+k*LOG2[0],hi+k*LOG2[1]
counts={}
for line in Path('../evidence/arithmetic_cases.tsv').read_text().splitlines():
 tag,mode,a,b,l,h=line.split();a,b,l,h=map(hx,[a,b,l,h]);assert l<=h
 if tag in ['add','sub','mul','div']:
  z={'add':lambda:a+b,'sub':lambda:a-b,'mul':lambda:a*b,'div':lambda:a/b}[tag]();assert l<=z<=h,(tag,a,b,l,z,h)
 elif tag=='sqrt':assert h>=0 and h*h>=a
 elif tag=='log':assert h>=logbounds(a)[1]
 elif tag=='L':assert a>0 and h>=(1+a)*logbounds(1+a)[1]/a
 else:raise AssertionError(tag)
 counts[tag]=counts.get(tag,0)+1
out={'status':'PROVED exact audit inequalities','checks':sum(counts.values()),'by_operation':counts,'rounding_modes':4,'log_reference':'100 exact rational atanh terms plus positive geometric tail','scope':'an audit in addition to, not a replacement for, the arithmetic proof'}
Path('../evidence/arithmetic_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
