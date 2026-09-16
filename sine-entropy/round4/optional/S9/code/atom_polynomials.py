"""Integer complete-atom polynomials for the exactly aligned R=3 witness.
K(u,d) = I/2 + u*(B+d I), B_ij = 45/192 for |i-j|=1,
-5/192 for |i-j|=3 and zero otherwise. d is ORIGINAL common shift.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import comb
from dyadic import IV,horner
N=7
D=192
DEN=D**N
POSITIONS=[(k,l) for k in range(N+1) for l in range(k+1) if (k-l)%2==0]

def det_int(A):
    a=[row[:] for row in A];n=len(a)
    if not n:return 1
    sign=1;prev=1
    for k in range(n-1):
        if a[k][k]==0:
            t=next((j for j in range(k+1,n) if a[j][k]),None)
            if t is None:return 0
            a[k],a[t]=a[t],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                val=a[i][j]*pivot-a[i][k]*a[k][j]
                if val%prev:raise ArithmeticError('Bareiss exact division')
                a[i][j]=val//prev
        for i in range(k+1,n):a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

def b_integer():
    return [[45 if abs(i-j)==1 else -5 if abs(i-j)==3 else 0 for j in range(N)]for i in range(N)]

def fwht(v):
    z=v[:];h=1
    while h<len(z):
        for j in range(0,len(z),2*h):
            for i in range(j,j+h):
                a,b=z[i],z[i+h];z[i],z[i+h]=a+b,a-b
        h*=2
    return z

def build():
    B=b_integer();dm=[]
    for m in range(1<<N):
        ids=[i for i in range(N)if m>>i&1]
        dm.append(det_int([[B[i][j]for j in ids]for i in ids]))
    out=[[0 for _ in POSITIONS]for _ in range(1<<N)]
    for ci,(k,l) in enumerate(POSITIONS):
        co=[0]*(1<<N)
        for s in range(1<<N):
            if s.bit_count()!=k:continue
            e=0;t=s
            while True:
                if t.bit_count()==k-l:e+=dm[t]
                if not t:break
                t=(t-1)&s
            co[s]=(-1)**k * (D//2)**(N-k)*D**l*e
        co=fwht(co)
        for m in range(1<<N):out[m][ci]=co[m]
    return out

def jets_fraction(coeff,u:Q,d:Q):
    ans=[Q(0),Q(0),Q(0)]
    for v,(k,l) in zip(coeff,POSITIONS):
        if not v:continue
        for j in range(min(2,l)+1):
            ans[j]+=Q(v, DEN)*u**k*d**(l-j)*(1 if j==0 else l if j==1 else l*(l-1))
    return ans

def interval_coefficients(all_coeff,delta:IV):
    """Produce u polynomials of the three ORIGINAL-shift derivative layers."""
    ans=[]
    for row in all_coeff:
        by=[[IV.point(0)for _ in range(N+1)]for _ in range(3)]
        for j in range(3):
            for k in range(N+1):
                coef=[Q(0)]*(N+1)
                for v,(kk,l)in zip(row,POSITIONS):
                    if kk!=k or l<j:continue
                    coef[l-j]=Q(v*(1 if j==0 else l if j==1 else l*(l-1)),DEN)
                by[j][k]=horner(coef,delta)
        ans.append(by)
    return ans

def evaluate_u(all_iv_coeff,u):
    return [[horner(co,u)for co in row]for row in all_iv_coeff]

def center_curvature(js):
    layers=[IV.point(0)for _ in range(N)]
    fisher=IV.point(0);acc=IV.point(0)
    for m in range(1<<N):
        if m&(1<<(N//2)):continue
        x,x1,x2=js[m];y,y1,y2=js[m+(1<<(N//2))]
        if x.lo<=0 or y.lo<=0:raise ArithmeticError('atom positivity enclosure failed')
        z=y/x;l=z.log()
        sq=(x+y)/2*(x1/x-y1/y).sq()
        ac=(-l+1-z)*x2/2+(l+1-1/z)*y2/2
        layers[m.bit_count()]=layers[m.bit_count()]+sq+ac
        fisher=fisher+sq;acc=acc+ac
    return layers,fisher,acc
