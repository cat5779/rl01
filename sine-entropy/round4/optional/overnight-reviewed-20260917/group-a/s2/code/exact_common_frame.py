#!/usr/bin/env python3
"""Finite exact tests of the FIRST frozen common-outside-frame extension.

These finite certificates do not prove the all-rank comparison. They account for
all 64 complete output atoms and retain every output-law derivative.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json,time,argparse
from exact_certificate import require,det_real,entropy_curvature_interval,sub_interval,decimal_enclosure

U=[
 [F(1,2),F(14,25),F(0)], [F(1,2),F(-14,25),F(0)],
 [F(1,2),F(2,25),F(0)], [F(1,2),F(-2,25),F(0)],
 [F(0),F(12,25),F(3,5)], [F(0),F(-9,25),F(4,5)],
]


def atoms(U):
 n=len(U);k=len(U[0]);G=[[sum(row[i]*row[j] for row in U) for j in range(k)] for i in range(k)]
 require(G==[[F(i==j) for j in range(k)] for i in range(k)],'isometry')
 mu=[F(0)]*(1<<n)
 for S in combinations(range(n),k):mu[sum(1<<i for i in S)]=det_real([U[i] for i in S])**2
 require(sum(mu)==1,'input normalization');return mu


def swap(mu):
 out=[F(0)]*len(mu)
 for S,p in enumerate(mu):
  T=S
  if bool(S&1)!=bool(S&2):T^=3
  out[T]=p
 return out


def jets(mu,n,a,c):
 out=[]
 for T in range(1<<n):
  row=[F(0)]*3
  for S,p in enumerate(mu):
   if not p:continue
   l,d,e=F(1),F(0),F(0)
   for i in range(n):
    pi=a+c*bool(S&(1<<i));y=bool(T&(1<<i));w=pi if y else 1-pi;s=1 if y else -1
    l,d,e=l*w,d*w+s*l,e*w+2*s*d
   for j,z in enumerate([l,d,e]):row[j]+=p*z
  out.append(row)
 require(sum(r[0] for r in out)==1 and sum(r[1] for r in out)==0 and sum(r[2] for r in out)==0,'all jet normalizations')
 return out


def main():
 pa=argparse.ArgumentParser();pa.add_argument('--out',default='data/common_exact.json');args=pa.parse_args();start=time.monotonic()
 mu=atoms(U);ms=swap(mu);mid=[(x+y)/2 for x,y in zip(mu,ms)]
 f=[[F(1,2)] for _ in range(4)];fg=[[F(1,2),g] for g in [F(7,10),F(-7,10),F(1,10),F(-1,10)]]
 B=[[F(3,5)],[F(4,5)]];muF=atoms(f);muFG=atoms(fg);muB=atoms(B)
 factor=[F(0)]*64
 for T in range(64):
  L=T&15;R=T>>4
  factor[T]=F(16,25)*muFG[L]*muB[R]+F(9,25)*muF[L]*F(R==3)
 require(mu==factor,'exact common-frame nested-law disintegration')
 records=[]
 for a in [F(1,200),F(1,40),F(9,200)]:
  J0=jets(mu,6,a,F(19,20));Jh=jets(mid,6,a,F(19,20))
  H0,H02=entropy_curvature_interval(J0);Hh,Hh2=entropy_curvature_interval(Jh);diff=sub_interval(Hh2,H02)
  require(diff[0]>0,'finite frozen-extension fixture positive curvature difference')
  records.append({'a':str(a),'c':'19/20','difference':decimal_enclosure(diff),'q0_jets':[[str(x) for x in row] for row in J0],'qh_jets':[[str(x) for x in row] for row in Jh]})
  print('PASS exact connected n=6,k=3 shared-frame fixture',a,decimal_enclosure(diff),flush=True)
 out=Path(args.out);out.parent.mkdir(exist_ok=True,parents=True);out.write_text(json.dumps({'status':'finite exact tests only, not an all-rank theorem','frame':[[str(x) for x in row] for row in U],'beta':'9/25','rank':3,'n':6,'records':records,'runtime_seconds':time.monotonic()-start},indent=2)+'\n')
if __name__=='__main__':main()
