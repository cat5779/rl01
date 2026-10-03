"""Exact Jensen lower bound for the mixed-resistance C04 interval.

Selected edge resistances are evaluated at a; all unselected resistances
and conditional half-tree messages use b. Input must be an upper grid.
No floating point value enters any certificate arithmetic.
"""
from pathlib import Path
from fractions import Fraction as F
from math import lcm
import argparse,json,time,hashlib

ROOT=Path(__file__).parent
pa=argparse.ArgumentParser()
pa.add_argument('p',type=int);pa.add_argument('q',type=int)
pa.add_argument('input');pa.add_argument('--bins',type=int,default=24)
args=pa.parse_args()
src=Path(args.input)
if not src.is_absolute():src=ROOT/src
data=json.loads(src.read_text(encoding='utf-8'))
assert data['kind']=='upper'
ap,aq=args.p,args.q
bp,bq=data['lambda']['p'],data['lambda']['q']
assert 1<F(ap,aq)<F(bp,bq)<F(3,2)
M=data['M'];D=data['probability_denominator'];H=1<<40
Q=lcm(aq**4,bq**4);U=M*Q
PI=(1,2,1);P=data['initial_grid_index']
ra=[int(U*F(ap,aq)**k) for k in range(5)]
rb=[int(U*F(bp,bq)**k) for k in range(5)]
assert all(U*F(ap,aq)**k==ra[k] for k in range(5))
assert all(U*F(bp,bq)**k==rb[k] for k in range(5))
pmf={}
for s in (0,1):
    for k in range(3):
        d=data['pmf'][str(s)+str(k)]
        assert len(d['indices'])==len(d['counts']) and sum(d['counts'])==D
        assert min(d['counts'])>0 and 0<=min(d['indices'])<=max(d['indices'])<=P
        pmf[s,k]={i*Q:w for i,w in zip(d['indices'],d['counts'])}
W=(P*Q+args.bins-1)//args.bins
assert W>0


def mean_compress(values):
    bins={}
    for i,wi in values.items():
        key=i//W
        mass,weighted=bins.get(key,(0,0))
        bins[key]=(mass+wi,weighted+wi*i)
    out={}
    for mass,weighted in bins.values():
        mean=(weighted+mass-1)//mass
        out[mean]=out.get(mean,0)+mass
    assert sum(out.values())==sum(values.values())
    return dict(sorted(out.items()))


def mix(s,deg=None):
    out={}
    for k in range(3):
        add=0 if deg is None else rb[deg+k]
        for i,wi in pmf[s,k].items():
            out[i+add]=out.get(i+add,0)+PI[k]*wi
    assert sum(out.values())==4*D
    return out


ends={k:mean_compress(pmf[0,k]) for k in range(3)}
op=mean_compress(mix(1))
closed={m:mean_compress(mix(0,m)) for m in (0,1)}


def side(m,b):
    internal=op if b else closed[m]
    out=[]
    for k in range(3):
        r=ra[k+m+b]
        for s0,w0 in ends[k].items():
            A=r+s0
            for si,wi in internal.items():
                out.append((r,A,si,PI[k]*w0*wi))
    assert sum(t[3] for t in out)==(4*D)**2
    return out


num=0;terms=0;started=time.time();case_records=[]
for m in (0,1):
    for b1,b2 in ((0,0),(0,1),(1,1)):
        left=side(m,b1);right=side(m,b2)
        same=b1==b2
        r2=rb[b1+b2] if m==0 else 0
        case=0;ncase=0
        for pos,(r1,A,s1,w1) in enumerate(left):
            for r3,B,s2,w3 in (right[pos:] if same else right):
                symmetry=1
                if same and (r1,A,s1)!=(r3,B,s2):symmetry=2
                elif not same:symmetry=2 # accounts for b1,b2=(1,0)
                ss=s1*s2;C=r2+s1+s2
                if C:
                    numerator=r1*r3*C
                    denominator=A*B*C+r2*(s1*B+s2*A+ss)+ss*(A+B)
                else:
                    assert m==1
                    numerator=r1*r3;denominator=A*B
                assert denominator>=numerator>0
                value=numerator*H//denominator
                case+=symmetry*w1*w3*value
                ncase+=1
        num+=case;terms+=ncase
        rec={'middle_open':m,'b1':b1,'b2':b2,'terms':ncase,'weighted_numerator':case,
             'seconds':time.time()-started}
        case_records.append(rec);print(json.dumps(rec),flush=True)
den=32*(4*D)**4*H
margin=48*num-5*den
out={'status':'EXACT_MIXED_INTERVAL_CANDIDATE','a':{'p':ap,'q':aq},'b':{'p':bp,'q':bq},
     'source':src.name,'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
     'grid_M':M,'common_resistance_units':U,'probability_denominator':D,
     'function_denominator':H,'compression_bins':args.bins,'compression_width_units':W,
     'lower_numerator':num,'lower_denominator':den,'48num_minus_5den':margin,
     'strictly_above_target':margin>0,'terms':terms,'cases':case_records,
     'compression':'conditional endpoint counts retained; internal arm mixtures compressed by upward-rounded bin means; separate Jensen; function rounded down',
     'compressed_endpoint_messages':{str(k):{'units':list(ends[k]),'counts':list(ends[k].values())} for k in range(3)},
     'compressed_open_arm':{'units':list(op),'counts':list(op.values())},
     'compressed_closed_arms':{str(m):{'units':list(closed[m]),'counts':list(closed[m].values())} for m in (0,1)},
     'elapsed_seconds':time.time()-started}
path=ROOT/f'far04a{ap}q{aq}b{bp}q{bq}m{M}k{args.bins}.json'
path.write_text(json.dumps(out,indent=2)+"\n",encoding='utf-8')
print(json.dumps({'output':str(path),'lower':num/den,'target':5/48,'strictly_above':margin>0,'terms':terms,'seconds':time.time()-started}),flush=True)
