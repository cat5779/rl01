#!/usr/bin/env python3
"""Self-contained rigorous fixed-point interval certificates for QWE08.

All arithmetic endpoints are integers divided by 2**BITS.  No floating-point
quantity is used in an acceptance inequality.  No hashes or checksums.

Certificates use full configuration probabilities of true sine Toeplitz
compressions, a common-shift polynomial identity, and an analytic tail bound.
See QWE08_RESULT.md for the mathematical soundness proof.
"""
from __future__ import annotations
import argparse, json, math, time
from pathlib import Path
from decimal import Decimal, localcontext

BITS=256
S=1<<BITS

class I:
    __slots__=('lo','hi')
    def __init__(self,lo:int,hi:int|None=None):
        self.lo=int(lo);self.hi=int(lo if hi is None else hi)
        if self.lo>self.hi:raise ValueError('reversed interval')
    @classmethod
    def rat(cls,a:int,b:int=1):
        if b<0:a,b=-a,-b
        if not b:raise ZeroDivisionError
        return cls(a*S//b,-((-a*S)//b))
    def __add__(self,o):
        if isinstance(o,int):o=I.rat(o)
        return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):
        if isinstance(o,int):o=I.rat(o)
        return I(self.lo-o.hi,self.hi-o.lo)
    def __rsub__(self,o):return -self+o
    def __mul__(self,o):
        if isinstance(o,int):
            return I(self.lo*o,self.hi*o) if o>=0 else I(self.hi*o,self.lo*o)
        q=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(q)//S,-((-max(q))//S))
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi:raise ZeroDivisionError('interval contains zero')
        return I(S*S//self.hi,-((-S*S)//self.lo))
    def __truediv__(self,o):
        if isinstance(o,int):
            if o<0:return (-self)/(-o)
            if o==0:raise ZeroDivisionError
            return I(self.lo//o,-((-self.hi)//o))
        return self*o.inv()
    def __pow__(self,n):
        if n<0:return (self.inv())**(-n)
        out=ONE;b=self
        while n:
            if n&1:out=out*b
            b=b*b;n//=2
        return out
    def contains(self,a:int,b:int=1):return self.lo*b<=a*S<=self.hi*b
    def dump(self):return [str(self.lo),str(self.hi)]
    @classmethod
    def load(cls,x):return cls(int(x[0]),int(x[1]))
    def decimal(self,digits=18):
        # Reporting only; not used to decide a sign.
        with localcontext() as c:
            c.prec=digits
            return '['+str(Decimal(self.lo)/Decimal(S))+', '+str(Decimal(self.hi)/Decimal(S))+']'

ZERO=I(0);ONE=I(S)

def atan_recip(q:int,N:int)->I:
    x=I.rat(1,q);x2=x*x;power=x;out=ZERO
    for k in range(N):
        term=power/(2*k+1)
        out=out+term if k%2==0 else out-term
        power=power*x2
    rem=power/(2*N+1)
    return I(out.lo-rem.hi,out.hi+rem.hi)

# Machin identity; the alternating-series remainder is enclosed explicitly.
PI=16*atan_recip(5,80)-4*atan_recip(239,30)

# log(2)=2 atanh(1/3), with a positive geometric tail.
def log_atanh(x:I,N:int=100)->I:
    z=(x-ONE)/(x+ONE);z2=z*z;power=z;out=ZERO
    if z.lo<0 or z.hi*3>S+4:raise ValueError('log reduction failed')
    for k in range(N):
        out=out+power/(2*k+1);power=power*z2
    rem=2*power/((2*N+1)*(ONE-z2))
    return I((2*out).lo,(2*out).hi+rem.hi)

LN2=log_atanh(I.rat(2))

def log_endpoint(v:int)->I:
    if v<=0:raise ValueError('log of non-positive interval endpoint')
    k=v.bit_length()-1-BITS
    if k>=0:x=I(v//(1<<k),-((-v)//(1<<k)))
    else:x=I(v*(1<<(-k)))
    return log_atanh(x)+k*LN2

def log(x:I)->I:
    return I(log_endpoint(x.lo).lo,log_endpoint(x.hi).hi)


def center_kernel(n:int)->list[list[I]]:
    out=[]
    c=I.rat(19,20)
    for i in range(n):
        row=[]
        for j in range(n):
            d=abs(i-j)
            if d==0:row.append(I.rat(1,2))
            elif d%2==0:row.append(ZERO)
            else:row.append((c/(PI*d))*(1 if d%4==1 else -1))
        out.append(row)
    return out


def all_probabilities(K:list[list[I]])->list[I]:
    n=len(K);out=[ZERO]*(1<<n)
    def visit(A:list[list[I]],w:I,mask:int,depth:int):
        d=len(A)
        if d==0:
            out[mask]=w;return
        q=A[0][0]
        if not (q.lo>0 and q.hi<S):
            raise ArithmeticError('conditional probability not certified in (0,1)')
        r=ONE-q
        if d==1:
            out[mask]=w*r;out[mask|(1<<depth)]=w*q;return
        products=[[A[i][0]*A[0][j] for j in range(1,d)] for i in range(1,d)]
        qi=q.inv();ri=r.inv()
        A0=[[A[i+1][j+1]+products[i][j]*ri for j in range(d-1)] for i in range(d-1)]
        A1=[[A[i+1][j+1]-products[i][j]*qi for j in range(d-1)] for i in range(d-1)]
        visit(A0,w*r,mask,depth+1)
        visit(A1,w*q,mask|(1<<depth),depth+1)
    visit(K,ONE,0,0)
    total=sum(out,ZERO)
    if not total.contains(1):raise ArithmeticError('mass normalization check failed')
    if min(v.lo for v in out)<=0:raise ArithmeticError('positive atom enclosure failed')
    return out


def derivative(p:list[I])->list[I]:
    n=len(p).bit_length()-1;out=[ZERO]*len(p)
    for bit in range(n):
        stride=1<<bit
        for base in range(0,len(p),stride*2):
            for j in range(stride):
                k=base+j;s=p[k]+p[k+stride]
                out[k]=out[k]-s;out[k+stride]=out[k+stride]+s
    return out


def entropy_coefficients(n:int,order:int)->list[I]:
    P=[all_probabilities(center_kernel(n))]
    for k in range(1,n+1):P.append([v/k for v in derivative(P[-1])])
    # Exact nilpotence D^(n+1)=0 is used, rather than differentiating interval noise.
    H=[ZERO]*(order+1)
    for atom in range(1<<n):
        p=[P[j][atom] for j in range(n+1)]
        inv=p[0].inv();ell=[log(p[0])]
        for k in range(1,order+1):
            acc=p[k]*k if k<=n else ZERO
            for j in range(1,min(n,k-1)+1):
                acc=acc-p[j]*ell[k-j]*(k-j)
            ell.append((acc*inv)/k)
        H[0]=H[0]-p[0]*ell[0]
        for k in range(1,order+1):
            acc=ZERO
            for j in range(1,min(n,k)+1):
                term=ell[k-j]+ONE if k==j else ell[k-j]
                acc=acc+p[j]*j*term
            H[k]=H[k]-acc/k
    for k in range(1,order+1,2):
        if not H[k].contains(0):raise ArithmeticError('complement-symmetry check failed')
    return H


def analytic_entropy_bound(n:int)->I:
    # R=1/50, delta=1/40: B_n=n*(9/5)^n*log(10).
    return n*(I.rat(9,5)**n)*log(I.rat(10))


def curvature_tail(n:int,m:int,order:int)->I:
    if order%2:raise ValueError('even truncation required')
    L=order//2;k=L+1;t=I.rat(1,16);one_minus=ONE-t
    series=(4*k*k-2*k)/one_minus if False else I.rat(4*k*k-2*k)/one_minus
    series=series+I.rat(8*k-2)*t/(one_minus**2)+4*t*(ONE+t)/(one_minus**3)
    B=analytic_entropy_bound(n)+analytic_entropy_bound(m)+analytic_entropy_bound(n+m)
    return B*2500*(t**L)*series


def entropy_curvature_tail(n:int,order:int)->I:
    L=order//2;k=L+1;t=I.rat(1,16);one_minus=ONE-t
    series=I.rat(4*k*k-2*k)/one_minus+I.rat(8*k-2)*t/(one_minus**2)+4*t*(ONE+t)/(one_minus**3)
    return analytic_entropy_bound(n)*2500*(t**L)*series


def self_tests():
    assert (I.rat(1,3)*I.rat(3)).contains(1)
    assert (I.rat(-2,3).inv()*I.rat(-2,3)).contains(1)
    assert (log(I.rat(1))).contains(0)
    assert PI.lo*10000000000>31415926535*S
    assert PI.hi*10000000000<31415926536*S
    h=entropy_coefficients(1,8)
    assert h[0].lo<=LN2.hi and LN2.lo<=h[0].hi
    for k in range(1,5):
        exact=I.rat(-(2**(2*k)),(2*k)*(2*k-1))
        assert h[2*k].lo<=exact.hi and exact.lo<=h[2*k].hi


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--max-n',type=int,default=12)
    ap.add_argument('--order',type=int,default=24)
    ap.add_argument('--directory',default=str(Path(__file__).parent/'evidence'/'rigorous'))
    args=ap.parse_args()
    if args.max_n<2 or args.order<4 or args.order%2:raise ValueError('invalid certificate parameters')
    folder=Path(args.directory);folder.mkdir(parents=True,exist_ok=True)
    self_tests();H={};start=time.monotonic()
    for n in range(1,args.max_n+1):
        file=folder/f'entropy_coefficients_n{n}_order{args.order}.json'
        # Every run recomputes the mathematical objects; saved data are outputs, not acceptance gates.
        H[n]=entropy_coefficients(n,args.order)
        file.write_text(json.dumps(dict(bits=BITS,n=n,order=args.order,coefficients=[x.dump() for x in H[n]]),indent=2))
        lower=(-2*H[n][2])-entropy_curvature_tail(n,args.order)
        higher_negative=all(H[n][k].hi<=0 for k in range(4,args.order+1,2))
        print('n',n,'F(mid)',(-2*H[n][2]).decimal(14),'higher_even_H_negative',higher_negative,'uniform_F_lower',lower.decimal(14),'seconds',round(time.monotonic()-start,2),flush=True)
    certificates=[];min_lower=None
    for total in range(2,args.max_n+1):
        for m in range(1,total//2+1):
            n=total-m
            coef=[H[m][k]+H[n][k]-H[total][k] for k in range(args.order+1)]
            positive=all(coef[k].lo>=0 for k in range(4,args.order+1,2))
            tail=curvature_tail(m,n,args.order)
            lower=2*coef[2]-tail
            if not positive or lower.lo<=0:
                raise ArithmeticError(f'MI convexity certificate failed for {(m,n)}')
            certificates.append(dict(m=m,n=n,lower=lower.dump(),tail=tail.dump(),even_coefficients=[coef[k].dump() for k in range(2,args.order+1,2)]))
            if min_lower is None or lower.lo<min_lower.lo:min_lower=lower
    result=dict(status='PROVED_FINITE_CONTINUUM',max_total=args.max_n,order=args.order,bits=BITS,a_interval=['1/50','3/100'],rho='1/2',c='19/20',minimum_certified_curvature=min_lower.dump(),certificates=certificates)
    (folder/'mi_continuum_certificates.json').write_text(json.dumps(result,indent=2))
    print('All adjacent splits certified; minimum lower enclosure:',min_lower.decimal(20),flush=True)
    print('Elapsed seconds:',time.monotonic()-start,flush=True)

if __name__=='__main__':main()