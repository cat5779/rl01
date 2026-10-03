"""Independent ordered exact verifier for the final C04 far certificate.

Rebuild compression from the original frozen six PMFs. Sum all eight bit
configurations and every ordered side pair. Use a different tridiagonal
denominator factorization, checked by the formal polynomial identity.
"""
from pathlib import Path
from fractions import Fraction as F
from math import lcm
import argparse,json,hashlib,time

pa=argparse.ArgumentParser();pa.add_argument('certificate');pa.add_argument('--output');args=pa.parse_args()
ROOT=Path(__file__).parent
path=Path(args.certificate)
if not path.is_absolute():path=ROOT/path
cert_blob=path.read_bytes();cert=json.loads(cert_blob)
source=path.parent/cert['source'];source_blob=source.read_bytes();data=json.loads(source_blob)
assert hashlib.sha256(source_blob).hexdigest()==cert['source_sha256']
assert data['kind']=='upper'
a=F(cert['a']['p'],cert['a']['q']);b=F(cert['b']['p'],cert['b']['q'])
assert b==F(data['lambda']['p'],data['lambda']['q']) and 1<a<b<F(3,2)
M=data['M'];D=data['probability_denominator'];H=cert['function_denominator']
Q=lcm(a.denominator**4,b.denominator**4);U=M*Q
assert U==cert['common_resistance_units']
W=(data['initial_grid_index']*Q+cert['compression_bins']-1)//cert['compression_bins']
assert W==cert['compression_width_units']
ar=[int(U*a**k) for k in range(5)];br=[int(U*b**k) for k in range(5)]
assert all(ar[k]==U*a**k and br[k]==U*b**k for k in range(5))
pmf={};pi=(1,2,1)
for s in (0,1):
    for k in range(3):
        row=data['pmf'][str(s)+str(k)];assert sum(row['counts'])==D
        pmf[s,k]=dict(zip((i*Q for i in row['indices']),row['counts']))

def mean_bins(values):
    mass={};moment={}
    for value,count in values.items():
        key=value//W;mass[key]=mass.get(key,0)+count;moment[key]=moment.get(key,0)+count*value
    out={}
    for key in sorted(mass):
        val=(moment[key]+mass[key]-1)//mass[key]
        out[val]=out.get(val,0)+mass[key]
    assert sum(out.values())==sum(values.values())
    return out

def mixture(s,degree=None):
    vals={}
    for k in range(3):
        for r,w in pmf[s,k].items():
            x=r+(0 if degree is None else br[degree+k])
            vals[x]=vals.get(x,0)+pi[k]*w
    assert sum(vals.values())==4*D
    return mean_bins(vals)

end={k:mean_bins(pmf[0,k]) for k in range(3)}
openarm=mixture(1);closed={m:mixture(0,m) for m in (0,1)}
def unpack(row):return dict(zip(row['units'],row['counts']))
assert all(end[k]==unpack(cert['compressed_endpoint_messages'][str(k)]) for k in range(3))
assert openarm==unpack(cert['compressed_open_arm'])
assert all(closed[m]==unpack(cert['compressed_closed_arms'][str(m)]) for m in (0,1))

def atoms(m,bit):
    inside=openarm if bit else closed[m]
    out=[]
    for k in range(3):
        r=ar[k+m+bit]
        for exterior,ew in end[k].items():
            for internal,iw in inside.items():
                out.append((r,exterior,internal,pi[k]*ew*iw))
    assert sum(t[3] for t in out)==(4*D)**2
    return out

total=0;records=[];start=time.time()
for m in (0,1):
    for b1 in (0,1):
        for b2 in (0,1):
            r2=0 if m else br[b1+b2]
            left=atoms(m,b1);right=atoms(m,b2)
            # From the independently expanded 21-term polynomial:
            # B0 = r2*(r1+s0+s1)+s1*(r1+s0), B2=r1+s0+s1;
            # Z = B0*(r3+s2+s3)+B2*s2*(r3+s3).
            ll=[(r,r2+s1,r2*(r+s0+s1)+s1*(r+s0),r+s0+s1,r+s0,w)
                for r,s0,s1,w in left]
            rr=[(r,s2,r+s3,r+s2+s3,w) for r,s3,s2,w in right]
            subtotal=0
            for r1,rs,B0,B2,A,w1 in ll:
                for r3,s2,C,Cplus,w3 in rr:
                    numerator=r1*r3*(rs+s2);denominator=B0*Cplus+B2*s2*C
                    if denominator==0:
                        assert m==1 and rs+s2==0
                        numerator=r1*r3;denominator=A*C
                    assert 0<numerator<=denominator
                    subtotal+=w1*w3*(H*numerator//denominator)
            total+=subtotal
            rec={'middle_open':m,'b1':b1,'b2':b2,'numerator':subtotal,
                 'ordered_terms':len(ll)*len(rr),'seconds':time.time()-start}
            records.append(rec);print(json.dumps(rec),flush=True)
den=32*(4*D)**4*H
assert total==cert['lower_numerator'] and den==cert['lower_denominator']
for old in cert['cases']:
    mm,x,y=old['middle_open'],old['b1'],old['b2']
    subtotal=sum(rec['numerator'] for rec in records if rec['middle_open']==mm and
                 ((rec['b1']==x and rec['b2']==y) or (x!=y and rec['b1']==y and rec['b2']==x)))
    assert subtotal==old['weighted_numerator']
margin=48*total-5*den;assert margin==cert['48num_minus_5den'] and margin>0
out={'status':'PASS_INDEPENDENT_ORDERED_FAR_CERTIFICATE','certificate_sha256':hashlib.sha256(cert_blob).hexdigest(),
     'source_sha256':hashlib.sha256(source_blob).hexdigest(),'rebuilt_compressed_messages_match':True,
     'numerator':total,'denominator':den,'48num_minus_5den':margin,'ordered_cases':records,
     'arithmetic':'pure Python integers, eight bit configurations, all ordered pairs; independent expanded-polynomial factorization',
     'not_checked':['infinite bridge','separate convexity','new mathematical proof review'],
     'seconds':time.time()-start}
dst=Path(args.output) if args.output else ROOT/(path.stem+'verify.json');dst.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'output':str(dst),'status':out['status'],'seconds':time.time()-start}),flush=True)
