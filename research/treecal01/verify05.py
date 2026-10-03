"""Independent pure-int64 one-step CDF verifier for grid05 PMFs.

No author module is imported. Every Cartesian product is counted in its
ordered form using integer add.at; the fast float64 chunk method is not
used. This verifies final sub/supersolutions, not a search iteration log.
"""
from pathlib import Path
from fractions import Fraction
import argparse, json, hashlib, time
import numpy as np

ap=argparse.ArgumentParser(); ap.add_argument('input');ap.add_argument('--output');args=ap.parse_args()
ROOT=Path(__file__).parent
src=Path(args.input)
if not src.is_absolute():src=ROOT/src
source_blob=src.read_bytes();raw=json.loads(source_blob)
M=int(raw['M']);Q=int(raw['Q']);D=int(raw['probability_denominator'])
P=int(raw['initial_grid_index']);kind=raw['kind'];started=time.time()
lam=Fraction(raw['lambda']['p'],raw['lambda']['q']);U=M*Q
assert kind in ('upper','lower') and P==-( -(M*lam**4).numerator//(M*lam**4).denominator)
rr=[]
for k in range(5):
    f=U*lam**k
    rr.append((f.numerator+f.denominator-1)//f.denominator if kind=='upper'
              else f.numerator//f.denominator)
assert rr==raw['closed_resistance_upper_units' if kind=='upper' else 'closed_resistance_lower_units']
assert 16*D*D<2**63
laws={}
for s in (0,1):
    for k in range(3):
        law=raw['pmf'][str(s)+str(k)]
        a=np.zeros(P+1,dtype=np.int64)
        ix=law['indices'];ws=law['counts']
        assert len(set(ix))==len(ix) and all(0<=i<=P for i in ix)
        assert all(isinstance(w,int) and w>0 for w in ws) and sum(ws)==D
        a[ix]=ws;laws[s,k]=a

def arms(s,d=None):
    merged={}
    for k,mult in enumerate((1,2,1)):
        a=laws[s,k]
        for i in np.flatnonzero(a):
            r=int(i)*Q+(0 if d is None else rr[d+k])
            merged[r]=merged.get(r,0)+mult*int(a[i])
    keys=sorted(merged)
    return np.array(keys,dtype=np.int64),np.array([merged[i] for i in keys],dtype=np.int64)

def exact_next(one,two):
    ai,aw=one;bi,bw=two
    assert int(ai[-1])*int(bi[-1])+Q*(int(ai[-1])+int(bi[-1]))<2**63
    sums=np.zeros(P+1,dtype=np.int64)
    for pos in range(0,len(ai),32):
        a=ai[pos:pos+32,None]
        denom=Q*(a+bi[None,:]);safe=np.maximum(denom,1)
        numer=a*bi[None,:]
        ix=((numer+safe-1)//safe if kind=='upper' else numer//safe)
        assert int(ix.max())<=P
        ww=aw[pos:pos+32,None]*bw[None,:]
        np.add.at(sums,ix.ravel(),ww.ravel())
    assert int(sums.sum())==16*D*D
    cdf=np.cumsum(sums,dtype=np.int64)
    counts=(cdf//(16*D) if kind=='upper' else (cdf+16*D-1)//(16*D))
    return counts

openarm=arms(1);closed=[arms(0,d) for d in range(3)]
pairs={(0,0):(closed[0],closed[0]),(1,0):(closed[1],closed[1]),
       (0,1):(openarm,closed[1]),(1,1):(openarm,closed[2]),
       (0,2):(openarm,openarm)}
checks=[];nextlaws={}
for key,pair in pairs.items():
    cdf=exact_next(*pair)
    before=np.cumsum(laws[key],dtype=np.int64)
    delta=cdf-before if kind=='upper' else before-cdf
    passed=bool(np.all(delta>=0))
    rec={'state':str(key[0])+str(key[1]),'pass':passed,'minimum_directed_cdf_difference':int(delta.min()),
         'maximum_directed_cdf_difference':int(delta.max()),'seconds':time.time()-started}
    print(json.dumps(rec),flush=True);checks.append(rec)
    nx=np.diff(cdf,prepend=np.int64(0));ix=np.flatnonzero(nx)
    nextlaws[rec['state']]={'indices':[int(i) for i in ix],'counts':[int(nx[i]) for i in ix]}
assert np.array_equal(laws[0,2],laws[1,2]);nextlaws['12']=nextlaws['02']
checks.append({'state':'12','pass':checks[-1]['pass'],'same_as':'02'})
out={'status':'PASS_EXACT_ONE_STEP_MESSAGE_ENCLOSURE' if all(c['pass'] for c in checks) else 'FAIL_ONE_STEP',
     'source_sha256':hashlib.sha256(source_blob).hexdigest(),'source':src.name,'checks':checks,
     'arithmetic':'ordered Cartesian products; pure int64 arithmetic with sum/product overflow checks; no floating-point arithmetic',
     'next_pmf':nextlaws,'elapsed_seconds':time.time()-started,
     'bridge_required':'BRIDGE.md bounded quotient-message uniqueness; not verified by this program'}
dst=Path(args.output) if args.output else ROOT/(src.stem+'verify.json')
dst.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'output':str(dst),'status':out['status'],'seconds':time.time()-started}),flush=True)
