#!/usr/bin/env python3
"""Check complete recorded covers and their exact parameter/input bookkeeping.
This is NOT a replacement for the interval algorithms or exact polynomial proof.
No hashes, checksums, manifests, or file-identity gates are used.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import argparse,json,re

def C(c:F,p:F)->F:return F(1303,1000)+F(51,200)*p+8*(c-F(19,20))
def main()->None:
 ap=argparse.ArgumentParser();ap.add_argument('--logs',type=Path,default=Path('../logs'));ap.add_argument('--output',type=Path,default=Path('../evidence/coverage.json'));args=ap.parse_args()
 caps=[tuple(map(int,l.split())) for l in Path('guard_caps_integer.txt').read_text().splitlines() if l.strip()]
 t2=list(map(int,Path('far_tau_integer.txt').read_text().split()));t3=list(map(int,Path('quad_tau3_integer.txt').read_text().split()))
 assert len(caps)==len(t2)==len(t3)==256 and min(t2+t3)>=0
 result={'status':'INCOMPLETE','scope':'exact cover/input bookkeeping; the finite inequalities themselves are proved by the accompanying interval/exact-rational source algorithms'}
 text=(args.logs/'global.log').read_text();assert 'ERROR' not in text and 'FAIL' not in text
 pat=re.compile(r'^GLOBAL cell (\d+) ic (\d+) ip (\d+) PASS nodes (\d+) cap (\S+)$',re.M)
 cells=set();nodes=0
 for cell,ic,ip,nn,cap in pat.findall(text):
  cell,ic,ip,nn=map(int,[cell,ic,ip,nn]);assert 0<=ic<140 and 0<=ip<240 and cell==ic*240+ip and nn>0 and cell not in cells
  exact=C(F(19,20)+F(ic,40000),F(21,50)+F(ip,4000));printed=F(cap);assert 0<=exact-printed<F(1,10**10)
  cells.add(cell);nodes+=nn
 assert cells==set(range(33600))
 summary=re.search(r'SUMMARY global passed (\d+) failed (\d+) cells (\d+) nodes (\d+)',text);assert summary and tuple(map(int,summary.groups()))==(33600,0,33600,nodes)
 result['global']={'cells':len(cells),'nodes':nodes,'c_step':'1/40000','p_step':'1/4000'}
 pat=re.compile(r'^GUARD sep (\d+) job (\d+) word (\d+) ic (\d+) ip (\d+) PASS nodes (\d+) cap (\S+) worst (\S+)$',re.M)
 result['guards']={}
 for sep in [1,2,3]:
  text=(args.logs/f'guard_distance{sep}.log').read_text();assert 'ERROR' not in text and 'FAIL' not in text
  covered=set();nodes=0
  for d,job,z,ic,ip,nn,cap,worst in pat.findall(text):
   d,job,z,ic,ip,nn=map(int,[d,job,z,ic,ip,nn]);assert d==sep and job==(ic*6+ip)*256+z and 0<=ic<7 and 0<=ip<6 and 0<=z<256 and nn>0
   key=(ic,ip,z);assert key not in covered;covered.add(key);nodes+=nn;assert F(worst)==0
   cl=F(19,20)+F(ic,2000);pl=F(21,50)+F(ip,100);ph=pl+F(1,100)
   if sep==1:
    L,U=caps[z]
    def kappa(p:F)->F:return ((F(3,100)-p/20)*L+(p/20-F(1,50))*U)/100+F(1,50)
    exact=min(kappa(pl),kappa(ph))
   else:exact=C(cl,pl)-F((t2 if sep==2 else t3)[z],1000)
   assert 0<=exact-F(cap)<F(1,10**10),(sep,job,exact,cap)
  assert covered=={(ic,ip,z) for ic in range(7) for ip in range(6) for z in range(256)}
  summary=re.search(r'SUMMARY sep (\d+) range (\d+) (\d+) passed (\d+) failed (\d+) nodes (\d+)',text)
  assert summary and tuple(map(int,summary.groups()))==(sep,0,10752,10752,0,nodes)
  result['guards'][str(sep)]={'cells':len(covered),'words':256,'nodes':nodes,'c_step':'1/2000','p_step':'1/100'}
 for prefix in range(4):
  text=(args.logs/f'prob22_{prefix}.log').read_text();pat0=rf'PROBABILITY PASS n 22 prefixbits 2 prefix {prefix} leaves 1048576 mass'
  assert re.search(pat0,text)
 text=(args.logs/'payment.log').read_text();assert 'FULL_WORDS 4194304 MASS' in text and 'COEFFICIENT_ENCLOSURES_COMPLETE degree 8 normalization 1/4194304' in text and 'ERROR' not in text
 result['reference_words']=4194304;result['status']='PROVED complete recorded cover'
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result))
if __name__=='__main__':main()
