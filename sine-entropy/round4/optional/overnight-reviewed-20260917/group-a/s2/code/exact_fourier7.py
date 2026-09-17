#!/usr/bin/env python3
"""Exact algebraic/interval certificate for two quadrature steps on Pi_(7,3).

Arithmetic lives in Q[x]/(8*x^3+4*x^2-4*x-1), x=cos(2*pi/7).
Only rational interval enclosures, never floating arithmetic, certify signs.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
from functools import lru_cache
import argparse,json,time,sys,hashlib
from exact_certificate import require,log_interval,decimal_enclosure

Z=(F(0),F(0),F(0));O=(F(1),F(0),F(0));X=(F(0),F(1),F(0))

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def scale(a,t):return tuple(x*t for x in a)
def mul(a,b):
    p=[F(0)]*5
    for i in range(3):
        for j in range(3):p[i+j]+=a[i]*b[j]
    for d in [4,3]:
        v=p[d];p[d]=F(0)
        # x^3=1/8+x/2-x^2/2.
        p[d-3]+=v/8;p[d-2]+=v/2;p[d-1]-=v/2
    return tuple(p[:3])

CZ=(Z,Z);CO=(O,Z)
def ca(a,b):return add(a[0],b[0]),add(a[1],b[1])
def cn(a):return neg(a[0]),neg(a[1])
def cm(a,b):return sub(mul(a[0],b[0]),mul(a[1],b[1])),add(mul(a[0],b[1]),mul(a[1],b[0]))
def cc(a):return a[0],neg(a[1])
def cs(a,t):return scale(a[0],t),scale(a[1],t)


def determinant_complex(a):
    n=len(a);v=CZ
    for perm in permutations(range(n)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        term=CO
        for i,j in enumerate(perm):term=cm(term,a[i][j])
        v=ca(v,term if sign==1 else cn(term))
    return v


def determinant_real(a):
    n=len(a);v=Z
    for perm in permutations(range(n)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        term=O
        for i,j in enumerate(perm):term=mul(term,a[i][j])
        v=add(v,term if sign==1 else neg(term))
    return v


def isum(xs):
    s=Z
    for x in xs:s=add(s,x)
    return s


def poly(t):return 8*t*t*t+4*t*t-4*t-1

def root_interval(bits=140):
    lo,hi=F(1,2),F(1)
    require(poly(lo)<0<poly(hi),'root starts bracketed')
    for _ in range(bits):
        mid=(lo+hi)/2
        if poly(mid)<0:lo=mid
        else:hi=mid
    require(poly(lo)<0<poly(hi),'strict rational root isolation')
    return lo,hi


def ia(a,b):return a[0]+b[0],a[1]+b[1]
def ins(a):return -a[1],-a[0]
def iss(a,b):return ia(a,ins(b))
def im(a,b):
    vals=[x*y for x in a for y in b];return min(vals),max(vals)
def isc(a,c):return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def idiv(a,b):
    require(b[0]>0,'interval division by positive denominator')
    return im(a,(1/b[1],1/b[0]))
def square(a):
    if a[0]<=0<=a[1]:return F(0),max(a[0]**2,a[1]**2)
    return min(a[0]**2,a[1]**2),max(a[0]**2,a[1]**2)

def evaluate(a,root):
    x2=(root[0]**2,root[1]**2)
    return ia((a[0],a[0]),ia(isc(root,a[1]),isc(x2,a[2])))


def base_kernel():
    coords=[0,1,-1,2,-2,3,-3]
    cos={0:O,1:X,2:(F(-1),F(0),F(2)),3:(F(1,2),F(-1),F(-2))}
    K=[]
    for i in coords:
        row=[]
        for j in coords:
            d=(i-j)%7;d=min(d,7-d)
            row.append(scale(add(O,scale(cos[d],2)),F(1,7)))
        K.append(row)
    for i in range(7):
        for j in range(7):require(isum(mul(K[i][r],K[r][j]) for r in range(7))==K[i][j],'exact Fourier projection identity')
    require(isum(K[i][i] for i in range(7))==scale(O,3),'exact Fourier rank')
    return K


def physical_kernel_scaled(P,pairs):
    # M=D R P R* D, where D=diag(sqrt2 on rotated rows,1 elsewhere).
    B=[[((O if i==j else Z),Z) for j in range(7)] for i in range(7)]
    rotated=set()
    for i,j in pairs:
        rotated.update([i,j]);B[i][i]=CO;B[i][j]=(Z,O);B[j][j]=CO;B[j][i]=(Z,O)
    M=[]
    for i in range(7):
        row=[]
        for j in range(7):
            val=CZ
            for r in range(7):
                if B[i][r]==CZ:continue
                for s in range(7):
                    if B[j][s]==CZ:continue
                    val=ca(val,cm(cm(B[i][r],(P[r][s],Z)),cc(B[j][s])))
            row.append(val)
        M.append(row)
    for i in range(7):
        for j in range(7):
            v=CZ
            for r in range(7):v=ca(v,cs(cm(M[i][r],M[r][j]),F(1,2) if r in rotated else F(1)))
            require(v==M[i][j],'scaled exact physical projection identity')
    for i in range(7):
        require(M[i][i][1]==Z, 'real physical leverage')
        diag=scale(M[i][i][0],F(1,2) if i in rotated else F(1))
        require(diag==scale(O,F(3,7)), 'every physical leverage remains 3/7')
        for j in range(7):
            require(M[i][j]==cc(M[j][i]), 'exact physical Hermitian identity')
    return M,rotated


def law(P,pairs):
    M,rot=physical_kernel_scaled(P,pairs);mu=[Z]*128
    for S in combinations(range(7),3):
        d=determinant_complex([[M[i][j] for j in S] for i in S]);require(d[1]==Z,'real algebraic input minor')
        mu[sum(1<<i for i in S)]=scale(d[0],F(1,2**len(set(S)&rot)))
    require(isum(mu)==O,'algebraic normalization')
    return mu


def independent_jets_from_kernel(P,pairs):
    """Independent inclusion-minor polynomial and Boolean Möbius inversion."""
    M,rot=physical_kernel_scaled(P,pairs)
    moments=[]
    for A in range(128):
        S=[i for i in range(7) if A&(1<<i)]
        if len(S)>3:
            moments.append(Z)  # Rank is exactly three by unitary conjugation.
        else:
            d=determinant_complex([[M[i][j] for j in S] for i in S])
            require(d[1]==Z,'real algebraic inclusion minor')
            moments.append(scale(d[0],F(1,2**len(set(S)&rot))))
    a,c=F(1,200),F(19,20)
    out=[]
    for A in range(128):
        q=[Z,Z,Z];B=A
        while True:
            m=B.bit_count();d=A.bit_count()-m
            fac=[a**d*c**m, F(d)*a**(d-1)*c**m if d else F(0),
                 F(d*(d-1))*a**(d-2)*c**m if d>=2 else F(0)]
            q=[add(x,scale(moments[B],v)) for x,v in zip(q,fac)]
            if B==0:break
            B=(B-1)&A
        out.append(q)
    # Inclusion moments m(A)=sum_{T superset A} q(T).
    for i in range(7):
        for A in range(128):
            if not (A&(1<<i)):
                out[A]=[sub(x,y) for x,y in zip(out[A],out[A|(1<<i)])]
    return out


def swap(mu,pair):
    i,j=pair;res=[Z]*128
    for S,p in enumerate(mu):
        T=S
        if bool(S&(1<<i))!=bool(S&(1<<j)):T^=(1<<i)|(1<<j)
        res[T]=p
    return res

def sym(mu,pair):return [scale(add(x,y),F(1,2)) for x,y in zip(mu,swap(mu,pair))]


@lru_cache(None)
def channel_likelihood_jet(S,T):
    a,c=F(1,200),F(19,20);q,q1,q2=F(1),F(0),F(0)
    for i in range(7):
        pi=a+c*bool(S&(1<<i));bit=bool(T&(1<<i));v=pi if bit else 1-pi;s=1 if bit else -1
        q,q1,q2=q*v,q1*v+s*q,q2*v+2*s*q1
    return q,q1,q2


def jets(mu):
    out=[]
    for T in range(128):
        val=[Z,Z,Z]
        for S,p in enumerate(mu):
            if p==Z:continue
            v=channel_likelihood_jet(S,T)
            val=[add(z,scale(p,t)) for z,t in zip(val,v)]
        out.append(val)
    require(isum(row[0] for row in out)==O,'algebraic output normalization')
    require(isum(row[1] for row in out)==Z,'algebraic derivative normalization')
    require(isum(row[2] for row in out)==Z,'algebraic acceleration normalization')
    return out


def round_interval(interval,bits=160):
    scale=1<<bits;lo,hi=interval
    flo=(lo.numerator*scale)//lo.denominator
    cei=-((-hi.numerator*scale)//hi.denominator)
    return F(flo,scale),F(cei,scale)


def entropy_intervals(J,root,terms=24):
    H=(F(0),F(0));H2=(F(0),F(0))
    for row in J:
        q,qp,qpp=[evaluate(z,root) for z in row]
        require(q[0]>0,'positive entire rational atom enclosure')
        llo=log_interval(q[0],terms)[0];lhi=log_interval(q[1],terms)[1];L=round_interval((llo,lhi))
        H=round_interval(iss(H,im(q,L)))
        H2=round_interval(iss(H2,ia(im(qpp,L),idiv(square(qp),q))))
    return H,H2


def main():
    pa=argparse.ArgumentParser();pa.add_argument('--out',default='data/fourier7');pa.add_argument('--bits',type=int,default=140);pa.add_argument('--terms',type=int,default=24);args=pa.parse_args()
    require(args.bits>=100 and args.terms>=20,'certificate precision floors')
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True);start=time.monotonic();root=root_interval(args.bits);P=base_kernel();pairs=[(1,2),(3,4),(5,6)]
    laws={f'P{i}':law(P,pairs[:i]) for i in range(4)}
    require(laws['P1']==sym(laws['P0'],pairs[0]),'first affine Fourier chord')
    require(laws['P3']==laws['P0'],'Fourier reflection cycle full law')
    laws['ideal_second']=sym(laws['P1'],pairs[1]);require(laws['P2']!=laws['ideal_second'],'Fourier physical second is not affine')
    results={};ints={}
    for name,mu in laws.items():
        for p in mu:
            if p!=Z:require(evaluate(p,root)[0]>=0,'nonnegative algebraic input law')
        J=jets(mu)
        if name in ['P0','P1','P2','P3']:
            independently=independent_jets_from_kernel(P,pairs[:int(name[1])])
            require(J==independently,'all independent algebraic complete output atom jets')
        H,H2=entropy_intervals(J,root,args.terms);ints[name]=(H,H2)
        results[name]={'input_law_coefficients':[[str(x) for x in p] for p in mu],'complete_output_jets_coefficients':[[[str(x) for x in z] for z in row] for row in J],'entropy_interval':decimal_enclosure(H),'curvature_interval':decimal_enclosure(H2)}
        print('PASS',name,'exact Fourier projection/input/output checks; H2',decimal_enclosure(H2),flush=True)
    diff1=iss(ints['P1'][1],ints['P0'][1]);diff2=iss(ints['P2'][1],ints['P1'][1]);diffi=iss(ints['ideal_second'][1],ints['P1'][1]);payment=iss(diff2,diffi)
    require(diff1[0]>2,'strict first Fourier curvature gain')
    require(diff2[1]<-F(4,5),'strict reversed second Fourier curvature gain')
    require(diffi[0]>F(4,5),'strict positive ideal second Fourier comparison')
    require(payment[1]<-F(17,10),'nonzero unpaid actual-minus-affine Fourier curvature')
    require(all(ints[x][1][1]<0 for x in ['P0','P1','P2']),'individual Fourier Hessians remain negative')
    data={'status':'author exact algebraic arithmetic with rational interval sign certificate; no independent audit','field_polynomial':'8*x^3+4*x^2-4*x-1','field_basis':['1','x','x^2'],'root_identification':'x=cos(2*pi/7), unique polynomial root in (1/2,1)','root_interval':[str(x) for x in root],'parameters':{'a':'1/200','c':'19/20','n':7,'k':3},'coordinates':[0,1,-1,2,-2,3,-3],'pairs_zero_based_row_indices':pairs,'differences':{'first':decimal_enclosure(diff1),'second_physical':decimal_enclosure(diff2),'second_ideal':decimal_enclosure(diffi),'actual_minus_affine':decimal_enclosure(payment)},'states':results}
    text=json.dumps(data,indent=2)+'\n';(out/'certificate.json').write_text(text)
    receipt={'runtime_seconds':time.monotonic()-start,'finished_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'python':sys.version,'command':sys.argv,'all_checks_passed':True,'sha256':hashlib.sha256(text.encode()).hexdigest(),'evidence':'all certified arithmetic rational or exact cubic-field arithmetic; elapsed time is metadata'}
    (out/'run_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(data['differences'],indent=2));print('ALL EXACT FOURIER CHECKS PASSED',receipt['runtime_seconds'],flush=True)
if __name__=='__main__':main()
