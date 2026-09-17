#!/usr/bin/env python3
"""Exact standard-library certificates for rank-three quadrature composition.

No float is used to certify a sign. Complete laws and two a-derivatives are
rational; logarithms are enclosed by a range-reduced atanh series with a proved
tail. Independent inclusion-determinant reconstruction checks every atom jet.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations, product
from functools import lru_cache
from pathlib import Path
import argparse, json, hashlib, time, platform, sys

W = [
    [1, 85, 0],
    [1, 51, 68],
    [1, 51, -68],
    [1, 0, 85],
    [1, 0, -85],
    [1, -75, 40],
    [1, -75, -40],
]
PAIRS = [(1, 2), (3, 4), (5, 6)]
N, K = 7, 3
A, C = F(1, 200), F(19, 20)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def det_real(matrix):
    a=[[F(v) for v in row] for row in matrix]
    n=len(a); result=F(1)
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        if pivot is None: return F(0)
        if pivot!=j: a[j],a[pivot]=a[pivot],a[j]; result=-result
        value=a[j][j];result*=value
        for i in range(j+1,n):
            ratio=a[i][j]/value
            for z in range(j+1,n): a[i][z]-=ratio*a[j][z]
            a[i][j]=F(0)
    return result


def inv_real(matrix):
    n=len(matrix)
    a=[[F(v) for v in row]+[F(i==j) for j in range(n)] for i,row in enumerate(matrix)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if a[i][j])
        a[j],a[pivot]=a[pivot],a[j]
        val=a[j][j];a[j]=[z/val for z in a[j]]
        for i in range(n):
            if i==j:continue
            val=a[i][j];a[i]=[u-val*v for u,v in zip(a[i],a[j])]
    return [row[n:] for row in a]


# Gaussian rational arithmetic, represented by (real, imaginary).
ZERO=(F(0),F(0));ONE=(F(1),F(0))
def za(x,y):return (x[0]+y[0],x[1]+y[1])
def zn(x):return (-x[0],-x[1])
def zs(x,y):return za(x,zn(y))
def zm(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def zc(x):return (x[0],-x[1])
def zd(x,y):
    norm=y[0]*y[0]+y[1]*y[1]
    require(norm>0,'complex division by zero')
    return ((x[0]*y[0]+x[1]*y[1])/norm,(x[1]*y[0]-x[0]*y[1])/norm)
def zscale(x,t):return (x[0]*t,x[1]*t)


def det_complex(matrix):
    a=[list(row) for row in matrix];n=len(a);res=ONE
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]!=ZERO),None)
        if pivot is None:return ZERO
        if pivot!=j:a[j],a[pivot]=a[pivot],a[j];res=zn(res)
        val=a[j][j];res=zm(res,val)
        for i in range(j+1,n):
            ratio=zd(a[i][j],val)
            for z in range(j+1,n):a[i][z]=zs(a[i][z],zm(ratio,a[j][z]))
            a[i][j]=ZERO
    return res


def gram(W):
    return [[sum(F(row[i])*row[j] for row in W) for j in range(K)] for i in range(K)]


def physical_law(W, pairs):
    """Squared minors after disjoint (I+i swap)/sqrt(2) row rotations."""
    G=gram(W);den=det_real(G);require(den>0,'positive frame Gram determinant')
    mu=[F(0)]*(1<<N)
    for S in combinations(range(N),K):
        active=[pair for pair in pairs if len(set(S)&set(pair))==1]
        re=F(0);im=F(0)
        for flips in product([0,1],repeat=len(active)):
            rows=list(S);power=sum(flips)
            for pair,flip in zip(active,flips):
                if flip:
                    pos=next(j for j,x in enumerate(rows) if x in pair)
                    rows[pos]=pair[1] if rows[pos]==pair[0] else pair[0]
            d=det_real([W[x] for x in rows])
            if power%4==0:re+=d
            elif power%4==1:im+=d
            elif power%4==2:re-=d
            else:im-=d
        mask=sum(1<<i for i in S)
        mu[mask]=(re*re+im*im)/(2**len(active)*den)
    require(sum(mu)==1,'input law normalization')
    require(all(p>=0 for p in mu),'input nonnegative')
    return mu


def permute_law(mu, pair):
    i,j=pair;res=[F(0)]*len(mu)
    for mask,v in enumerate(mu):
        dest=mask
        if bool(mask&(1<<i))!=bool(mask&(1<<j)): dest^=(1<<i)|(1<<j)
        res[dest]=v
    return res


def average_law(mu, pair):
    other=permute_law(mu,pair)
    return [(x+y)/2 for x,y in zip(mu,other)]


def product_channel_jets(mu):
    """Direct product rule, with all output and acceleration weights retained."""
    J=[]
    for T in range(1<<N):
        out=[F(0)]*3
        for S,weight in enumerate(mu):
            if not weight:continue
            l,l1,l2=F(1),F(0),F(0)
            for i in range(N):
                pi=A+C*bool(S&(1<<i));bit=bool(T&(1<<i))
                value=pi if bit else 1-pi;sign=1 if bit else -1
                l,l1,l2=l*value,l1*value+sign*l,l2*value+2*sign*l1
            out[0]+=weight*l;out[1]+=weight*l1;out[2]+=weight*l2
        J.append(out)
    require(sum(row[0] for row in J)==1,'output normalization')
    require(sum(row[1] for row in J)==0,'score normalization')
    require(sum(row[2] for row in J)==0,'acceleration normalization')
    require(all(row[0]>0 for row in J),'strictly positive interior output atoms')
    return J


def inclusion_determinants(W,pairs):
    """Independent kernel reconstruction in Q(i), avoiding sqrt(2).

    M=D P D with D_ii=sqrt(2) on rotated rows. Its entries are Gaussian
    rationals; divide each principal minor by 2^(number of rotated rows).
    """
    Gi=inv_real(gram(W));B=[[(F(x),F(0)) for x in row] for row in W]
    rotated=set()
    for i,j in pairs:
        rotated.update([i,j]);B[i]=[(F(x),F(y)) for x,y in zip(W[i],W[j])];B[j]=[(F(y),F(x)) for x,y in zip(W[i],W[j])]
    M=[]
    for i in range(N):
        row=[]
        for j in range(N):
            val=ZERO
            for r in range(K):
                for s in range(K):val=za(val,zscale(zm(B[i][r],zc(B[j][s])),Gi[r][s]))
            row.append(val)
        M.append(row)
    inc=[]
    for mask in range(1<<N):
        S=[i for i in range(N) if mask&(1<<i)]
        z=det_complex([[M[i][j] for j in S] for i in S])
        require(z[1]==0,'real principal determinant')
        inc.append(z[0]/(2**len(set(S)&rotated)))
    return inc


def independent_output_jets(inc):
    moments=[]
    for mask in range(1<<N):
        d=mask.bit_count();val=[F(0)]*3;sub=mask
        while True:
            j=sub.bit_count();power=d-j;coef=C**j*inc[sub]
            val[0]+=coef*A**power
            if power>=1:val[1]+=coef*power*A**(power-1)
            if power>=2:val[2]+=coef*power*(power-1)*A**(power-2)
            if sub==0:break
            sub=(sub-1)&mask
        moments.append(val)
    # Boolean-lattice Mobius inversion.
    jets=[row[:] for row in moments]
    for i in range(N):
        for mask in range(1<<N):
            if not mask&(1<<i):
                jets[mask]=[u-v for u,v in zip(jets[mask],jets[mask|(1<<i)])]
    return jets


@lru_cache(None)
def log_unit_interval(q,terms):
    """Enclosure for log(q), 1<=q<=2. Positive atanh-series tail."""
    require(F(1)<=q<=F(2),'range-reduced log input')
    z=(q-1)/(q+1);z2=z*z;power=z;partial=F(0)
    for j in range(terms):partial+=2*power/F(2*j+1);power*=z2
    tail=2*power/(F(2*terms+1)*(1-z2))
    return partial,partial+tail


@lru_cache(None)
def log_interval(q,terms=24):
    require(q>0,'positive log argument')
    e=q.numerator.bit_length()-q.denominator.bit_length()
    scale=F(2**e) if e>=0 else F(1,2**(-e))
    r=q/scale
    if r<1:r*=2;e-=1
    if r>2:r/=2;e+=1
    lo,hi=log_unit_interval(r,terms);l2,h2=log_unit_interval(F(2),terms)
    if e>=0:return lo+e*l2,hi+e*h2
    return lo+e*h2,hi+e*l2


def scale_interval(interval,coef):
    lo,hi=interval
    return (coef*lo,coef*hi) if coef>=0 else (coef*hi,coef*lo)

def add_interval(a,b):return a[0]+b[0],a[1]+b[1]
def sub_interval(a,b):return a[0]-b[1],a[1]-b[0]


def entropy_curvature_interval(jets,terms=24):
    H=(F(0),F(0));H2=(F(0),F(0))
    for q,qp,qpp in jets:
        L=log_interval(q,terms)
        H=add_interval(H,scale_interval(L,-q))
        H2=add_interval(H2,scale_interval(L,-qpp))
        fisher=qp*qp/q;H2=(H2[0]-fisher,H2[1]-fisher)
    return H,H2


def decimal_enclosure(interval,places=12):
    scale=10**places;lo,hi=interval
    flo=(lo.numerator*scale)//lo.denominator
    cei=-((-hi.numerator*scale)//hi.denominator)
    def fmt(v):
        sign='-' if v<0 else '';v=abs(v)
        return f'{sign}{v//scale}.{v%scale:0{places}d}'
    return [fmt(flo),fmt(cei)]


def conditional_rank_two(mu,site=0):
    mass=sum(p for S,p in enumerate(mu) if S&(1<<site));require(mass>0,'positive conditioning event')
    others=[i for i in range(N) if i!=site]
    pair={(i,j):mu[(1<<site)|(1<<i)|(1<<j)]/mass for i,j in combinations(others,2)}
    h={i:sum(p for (j,k),p in pair.items() if i==j or i==k) for i in others}
    require(sum(pair.values())==1,'rank-two conditional law normalization')
    G=[[F(1) if i==j else 1-2*pair[tuple(sorted((i,j)))]/(h[i]*h[j]) for j in others] for i in others]
    return mass,pair,h,G


def moment_curve_certificate():
    ts=[0,1,-1,2,-2,3,-3];Wm=[[1,t,t*t] for t in ts]
    m0=physical_law(Wm,[]);m1=average_law(m0,(1,2));mid=average_law(m1,(3,4))
    mass,pair,h,G=conditional_rank_two(mid)
    inds=[0,1,2,4] # sites 1,-1,2,3 in the conditional ordering
    d=det_real([[G[i][j] for j in inds] for i in inds])
    require(mass==F(1,3),'moment-curve conditioning mass')
    require(d==F(27783,30976),'positive rank-four conditional Gram minor')
    require(d>F(508032,10**6),'explicit robust TV-separation payment')
    return {'frame':Wm,'conditioning_site':0,'conditioning_mass':str(mass),'conditional_leverages':{str(i):str(x) for i,x in h.items()},'conditional_Gram':[[str(x) for x in row] for row in G],'Gram_minor_sites':[1,2,3,5],'Gram_minor_determinant':str(d),'TV_separation_lower_bound':'1/1000000','ideal_input_law':[str(x) for x in mid]}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',default='data/exact');parser.add_argument('--terms',type=int,default=24);args=parser.parse_args()
    require(args.terms>=16,'at least 16 log terms are required')
    out=Path(args.out);out.mkdir(exist_ok=True,parents=True);start=time.monotonic()
    G=gram(W);detG=det_real(G)
    require(G==[[F(7),F(37),F(0)],[F(37),F(23677),F(0)],[F(0),F(0),F(26898)]],'integer frame Gram')
    laws={'P0':physical_law(W,[]),'P1':physical_law(W,PAIRS[:1]),'P2':physical_law(W,PAIRS[:2]),'P3':physical_law(W,PAIRS)}
    require(laws['P1']==average_law(laws['P0'],PAIRS[0]),'first quadrature is exactly an affine law chord')
    require(laws['P3']==laws['P0'],'three-step reflection cycle closes in the full law')
    laws['ideal_second']=average_law(laws['P1'],PAIRS[1])
    require(laws['ideal_second']!=laws['P2'],'second physical law is not the affine chord')
    tv=sum(abs(x-y) for x,y in zip(laws['ideal_second'],laws['P2']))/2
    print('PASS exact normalized input minors, first chord, physical second-step defect, and full-law cycle',flush=True)
    data={};intervals={}
    for name,mu in laws.items():
        jets=product_channel_jets(mu)
        if name in ['P0','P1','P2','P3']:
            inc=inclusion_determinants(W,PAIRS[:int(name[1])])
            for mask,moment in enumerate(inc):
                require(moment==sum(p for S,p in enumerate(mu) if S&mask==mask),f'{name} independent inclusion moment {mask}')
            require(jets==independent_output_jets(inc),f'{name} all independent complete output atom jets')
        H,H2=entropy_curvature_interval(jets,args.terms);intervals[name]=(H,H2)
        data[name]={'input_law':[str(x) for x in mu],'output_jets':[[str(x) for x in row] for row in jets],'entropy_interval':decimal_enclosure(H),'curvature_interval':decimal_enclosure(H2)}
        print('PASS',name,'all 128 complete jets;', 'H2',decimal_enclosure(H2),flush=True)
    first=sub_interval(intervals['P1'][1],intervals['P0'][1]);second=sub_interval(intervals['P2'][1],intervals['P1'][1]);third=sub_interval(intervals['P3'][1],intervals['P2'][1]);ideal=sub_interval(intervals['ideal_second'][1],intervals['P1'][1]);defect=sub_interval(second,ideal)
    gainH=sub_interval(intervals['P2'][0],intervals['P1'][0])
    require(first[0]>F(37,10),'strict positive first curvature difference')
    require(second[1]<-F(13,5),'negative higher-rank second curvature difference')
    require(ideal[0]>0,'ideal affine second law has positive curvature difference in this fixture')
    require(gainH[1]<0,'recorded entropy orientation')
    require(all(intervals[x][1][1]<0 for x in ['P0','P1','P2']),'no individual entropy-concavity counterexample')
    moment=moment_curve_certificate();print('PASS exact conditional rank-four obstruction and robust TV separation',flush=True)
    cert={'status':'exact rational arithmetic and proved logarithm-tail enclosures; author certificate, not independent audit','parameters':{'a':str(A),'c':str(C),'n':N,'k':K},'frame':W,'Gram':[[str(x) for x in row] for row in G],'det_Gram':str(detG),'pairs':PAIRS,'log_terms':args.terms,'physical_second_vs_ideal_input_TV':str(tv),'curvature_differences':{'first':decimal_enclosure(first),'second_physical':decimal_enclosure(second),'third_physical':decimal_enclosure(third),'second_ideal':decimal_enclosure(ideal),'second_physical_minus_ideal':decimal_enclosure(defect)},'entropy_second_physical_difference':decimal_enclosure(gainH),'states':data,'moment_curve_obstruction':moment}
    payload=json.dumps(cert,indent=2)+'\n';(out/'certificate.json').write_text(payload)
    receipt={'utc_finished':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'runtime_seconds':time.monotonic()-start,'python':sys.version,'platform':platform.platform(),'certificate_sha256':hashlib.sha256(payload.encode()).hexdigest(),'command':sys.argv,'all_checks_passed':True,'output_atoms_per_state':1<<N,'number_physical_states_with_independent_jet_reconstruction':4,'independently_reconstructed_scalar_jet_values':4*(1<<N)*3,'evidence':'no floating-point input to any certified mathematical check; floating elapsed time is metadata only'}
    (out/'run_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'differences':cert['curvature_differences'],'entropy_second_gain':cert['entropy_second_physical_difference'],'runtime_seconds':receipt['runtime_seconds']},indent=2))
    print('ALL EXACT CHECKS PASSED',flush=True)
if __name__=='__main__':main()
