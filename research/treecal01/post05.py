"""Pure-integer star enclosure from a frozen six-state grid PMF.

The summation uses ordered pairs, in contrast to the search helper's
symmetry-folded sum. No grid-generation module is imported.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,time

pa=argparse.ArgumentParser();pa.add_argument('input');pa.add_argument('--bins',type=int,default=128);pa.add_argument('--output')
args=pa.parse_args();ROOT=Path(__file__).parent
src=Path(args.input)
if not src.is_absolute():src=ROOT/src
blob=src.read_bytes();data=json.loads(blob)
M=data['M'];Q=data['Q'];U=M*Q;P=data['initial_grid_index'];D=data['probability_denominator']
H=1<<40;lam=F(data['lambda']['p'],data['lambda']['q']);kind=data['kind'];pi=(1,2,1)
assert kind in ('upper','lower')
upper=kind=='upper'
lo=[];hi=[]
for k in range(5):
    f=U*lam**k;lo.append(f.numerator//f.denominator);hi.append(-(-f.numerator//f.denominator))
assert lo==data['closed_resistance_lower_units'] and hi==data['closed_resistance_upper_units']
closed=hi if upper else lo;selected=lo if upper else hi
pmf={}
for s in (0,1):
    for k in range(3):
        row=data['pmf'][str(s)+str(k)]
        assert len(set(row['indices']))==len(row['indices']) and sum(row['counts'])==D
        assert all(0<=i<=P for i in row['indices']) and min(row['counts'])>0
        pmf[s,k]={i*Q:w for i,w in zip(row['indices'],row['counts'])}
W=(P*Q+args.bins-1)//args.bins
assert W>0

def compress(values):
    out={}
    if not upper:
        for i,w in values.items():
            low=i//W*W;high=low+W
            out[low]=out.get(low,0)+w*(high-i)
            out[high]=out.get(high,0)+w*(i-low)
    else:
        groups={}
        for i,w in values.items():
            key=i//W;mass,moment=groups.get(key,(0,0));groups[key]=(mass+w,moment+w*i)
        for mass,moment in groups.values():
            value=(moment+mass-1)//mass;out[value]=out.get(value,0)+mass
    out={i:w for i,w in sorted(out.items()) if w}
    assert sum(out.values())==sum(values.values())*(1 if upper else W)
    return out

def arm(s,degree=None):
    allv={}
    for k in range(3):
        offset=0 if degree is None else closed[degree+k]
        for i,w in pmf[s,k].items():
            allv[i+offset]=allv.get(i+offset,0)+pi[k]*w
    assert sum(allv.values())==4*D
    return compress(allv)

ends={k:compress(pmf[0,k]) for k in range(3)}
tails=[arm(0,0),arm(1)]
first=[(k,i,pi[k]*w) for k in range(3) for i,w in ends[k].items()]
mass=4*D*(1 if upper else W)
assert sum(t[2] for t in first)==mass
assert all(sum(t.values())==mass for t in tails)
num=0;cases=[];started=time.time()
for m in (0,1):
    subtotal=0;terms=0
    for k,i,wi in first:
        a=selected[k+m]
        for j,z,wz in first:
            b=selected[j+m];base=(a+i)*(b+z);slope=a+b+i+z
            for t,wt in tails[m].items():
                den=base+slope*t;numer=a*b*H
                f=numer//den if upper else (numer+den-1)//den
                subtotal+=wi*wz*wt*f;terms+=1
    num+=subtotal;cases.append({'third_open':m,'numerator':subtotal,'terms':terms})
den=8*mass**3*H;margin=12*num-den
out={'status':'EXACT_ORDERED_STAR_ENCLOSURE','source':src.name,'source_sha256':hashlib.sha256(blob).hexdigest(),
     'lambda':data['lambda'],'direction':'lower' if upper else 'upper','numerator':num,'denominator':den,
     '12num_minus_den':margin,'desired_strict_sign_pass':margin>0 if upper else margin<0,
     'compression_bins':args.bins,'compression_width_units':W,'cases':cases,
     'arithmetic':'pure Python integers; ordered Cartesian sum; separately convex conditional Jensen or secant compression; directed selected/closed resistance and function rounding',
     'seconds':time.time()-started}
dst=Path(args.output) if args.output else ROOT/(src.stem+f'star{args.bins}.json')
dst.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'output':str(dst),'bound':num/den,'12num_minus_den':margin,'pass':out['desired_strict_sign_pass'],'seconds':time.time()-started}),flush=True)
