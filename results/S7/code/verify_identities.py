#!/usr/bin/env python3
"""Exact rational checks for the finite DPP/output/posterior identities used in PR111.

Standard library only.  Every mathematical comparison is exact Fraction arithmetic;
`python -O` removes no validation because this file does not use assert.
"""
from __future__ import annotations
import argparse, json, time
from collections import defaultdict
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path


def I(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def diag(v): return [[F(v[i]) if i==j else F(0) for j in range(len(v))] for i in range(len(v))]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def scale(s,A): return [[s*x for x in row] for row in A]
def mm(A,B): return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A): return [list(x) for x in zip(*A)]
def minor(A, rows, cols): return [[A[i][j] for j in cols] for i in rows]
def principal(A,S): return minor(A,S,S)

def det(A):
    n=len(A)
    if n==0: return F(1)
    B=[row[:] for row in A]; out=F(1)
    for k in range(n):
        p=next((i for i in range(k,n) if B[i][k]),None)
        if p is None: return F(0)
        if p!=k: B[k],B[p]=B[p],B[k]; out=-out
        piv=B[k][k]; out*=piv
        for i in range(k+1,n):
            if not B[i][k]: continue
            q=B[i][k]/piv
            for j in range(k+1,n): B[i][j]-=q*B[k][j]
    return out

def inv(A):
    n=len(A); B=[A[i][:]+I(n)[i][:] for i in range(n)]
    for k in range(n):
        p=next((i for i in range(k,n) if B[i][k]),None)
        if p is None: raise ZeroDivisionError('singular')
        B[k],B[p]=B[p],B[k]
        q=B[k][k]; B[k]=[x/q for x in B[k]]
        for i in range(n):
            if i==k: continue
            q=B[i][k]
            if q: B[i]=[B[i][j]-q*B[k][j] for j in range(2*n)]
    return [row[n:] for row in B]

def eq(A,B): return A==B

def word_atom(K,w):
    n=len(K); A=[row[:] for row in K]
    for i,b in enumerate(w): A[i][i]-=1-b
    return F((-1)**(n-sum(w)))*det(A)

def all_words(n): return list(product((0,1), repeat=n))
def bits_to_int(w): return sum(b<<i for i,b in enumerate(w))

def subset_prob_from_atoms(atoms,S):
    return sum((p for w,p in atoms.items() if all(w[i] for i in S)),F(0))

def check_posdef_3(A):
    return A[0][0]>0 and det(principal(A,[0,1]))>0 and det(A)>0

class Audit:
    def __init__(self): self.n=0; self.sections=defaultdict(int)
    def check(self, cond, section, detail=''):
        if not cond: raise ArithmeticError(f'{section}: {detail}')
        self.n+=1; self.sections[section]+=1


def main_checks():
    au=Audit(); n=3
    Q=[[F(1,2),F(1,10),F(-1,20)],
       [F(1,10),F(2,5),F(1,12)],
       [F(-1,20),F(1,12),F(3,5)]]
    a=F(1,5); c=F(3,5); d=F(1,5); tau2=F(16,25)
    K=add(scale(a,I(n)),scale(c,Q))
    au.check(check_posdef_3(Q),'fixture_strip','Q>0')
    au.check(check_posdef_3(sub(I(n),Q)),'fixture_strip','I-Q>0')
    au.check(check_posdef_3(K),'fixture_strip','K>0')
    au.check(check_posdef_3(sub(I(n),K)),'fixture_strip','I-K>0')

    words=all_words(n)
    xatoms={x:word_atom(Q,x) for x in words}
    yatoms={y:word_atom(K,y) for y in words}
    au.check(sum(xatoms.values(),F(0))==1,'normalization','latent')
    au.check(sum(yatoms.values(),F(0))==1,'normalization','output')
    for x,p in xatoms.items(): au.check(p>0,'atom_positivity',f'X={x}')
    for y,p in yatoms.items(): au.check(p>0,'atom_positivity',f'Y={y}')

    def like(y,x):
        z=F(1)
        for yi,xi in zip(y,x):
            py1=a+c*xi
            z*=py1 if yi else 1-py1
        return z

    postkern={}
    postatoms={}
    for y in words:
        py=sum((xatoms[x]*like(y,x) for x in words),F(0))
        au.check(py==yatoms[y],'channel_normalizer',str(y))
        D=[F(4) if b else F(1,4) for b in y]
        sqrtD=[F(2) if b else F(1,2) for b in y]
        M=add(I(n),mm(diag([z-1 for z in D]),Q))
        R=mm(mm(diag(sqrtD),Q),mm(inv(M),diag(sqrtD)))
        postkern[y]=R
        pa={x:xatoms[x]*like(y,x)/py for x in words}
        postatoms[y]=pa
        au.check(sum(pa.values(),F(0))==1,'posterior_normalization',str(y))
        for mask in range(1<<n):
            S=[i for i in range(n) if mask>>i&1]
            au.check(det(principal(R,S))==subset_prob_from_atoms(pa,S),
                     'posterior_principal_minors',f'y={y},S={S}')

        A=[row[:] for row in K]
        for i,b in enumerate(y): A[i][i]-=1-b
        G=inv(A)
        Hinv=diag([F(5) if b else F(-5,4) for b in y])
        J=diag([F(1) if b else F(-1) for b in y])
        rhs=sub(Hinv,scale(F(15,4),mm(mm(J,R),J)))
        for i in range(n):
            for j in range(n):
                au.check(G[i][j]==rhs[i][j],'inverse_posterior_bridge',f'y={y},{i},{j}')
        for i in range(n):
            for j in range(n):
                if i!=j:
                    au.check(G[i][j]**2==c*c*R[i][j]**2/F(4,25)**2,
                             'offdiag_square_bridge',f'y={y},{i},{j}')

        X=diag([F(i+1) for i in range(n)])
        comm=lambda A,B: sub(mm(A,B),mm(B,A))
        lhs=comm(X,G); rhs2=scale(-c,mm(mm(G,comm(X,Q)),G))
        for i in range(n):
            for j in range(n): au.check(lhs[i][j]==rhs2[i][j],'inverse_commutator',f'y={y},{i},{j}')
        L=inv(add(I(n),mm(Q,diag([z-1 for z in D]))))
        RR=inv(add(I(n),mm(diag([z-1 for z in D]),Q)))
        rhs3=mm(mm(mm(mm(diag(sqrtD),L),comm(X,Q)),RR),diag(sqrtD))
        lhs3=comm(X,R)
        for i in range(n):
            for j in range(n): au.check(lhs3[i][j]==rhs3[i][j],'posterior_commutator',f'y={y},{i},{j}')

        S=[i for i,b in enumerate(y) if b]
        Lk=mm(K,inv(sub(I(n),K)))
        rhsj=det(sub(I(n),K))*det(principal(Lk,S))
        au.check(rhsj==yatoms[y],'janossy_complete_word',str(y))

    meanR=[[sum((yatoms[y]*postkern[y][i][j] for y in words),F(0)) for j in range(n)] for i in range(n)]
    target=add(scale(tau2,Q),scale(1-tau2,diag([Q[i][i] for i in range(n)])))
    for i in range(n):
        for j in range(n): au.check(meanR[i][j]==target[i][j],'posterior_mean_response',f'{i},{j}')

    for y in words:
        sign=F((-1)**(n-sum(y))); A=[row[:] for row in K]
        for i,b in enumerate(y): A[i][i]-=1-b
        p1=sign*sum((det(principal(A,[j for j in range(n) if j!=i])) for i in range(n)),F(0))
        p2=sign*2*sum((det(principal(A,[k for k in range(n) if k not in (i,j)])) for i,j in combinations(range(n),2)),F(0))
        p1f=F(0); p2f=F(0)
        for i in range(n):
            yf=list(y); yf[i]^=1
            p1f+=(1 if y[i] else -1)*(yatoms[y]+yatoms[tuple(yf)])
        for i,j in combinations(range(n),2):
            s=(1 if y[i] else -1)*(1 if y[j] else -1)
            sm=F(0)
            for bi,bj in product((0,1),repeat=2):
                z=list(y); z[i]=bi; z[j]=bj; sm+=yatoms[tuple(z)]
            p2f+=2*s*sm
        au.check(p1==p1f,'full_word_first_jet',str(y))
        au.check(p2==p2f,'full_word_second_jet',str(y))
    au.check(sum((yatoms[y] for y in words),F(0))==1,'jet_sums','p')
    def jets(y):
        p1f=F(0); p2f=F(0)
        for i in range(n):
            z=list(y); z[i]^=1
            p1f+=(1 if y[i] else -1)*(yatoms[y]+yatoms[tuple(z)])
        for i,j in combinations(range(n),2):
            s=(1 if y[i] else -1)*(1 if y[j] else -1); sm=F(0)
            for bi,bj in product((0,1),repeat=2):
                z=list(y); z[i]=bi; z[j]=bj; sm+=yatoms[tuple(z)]
            p2f+=2*s*sm
        return p1f,p2f
    au.check(sum((jets(y)[0] for y in words),F(0))==0,'jet_sums','p1')
    au.check(sum((jets(y)[1] for y in words),F(0))==0,'jet_sums','p2')

    for i,j in combinations(range(n),2):
        O=[k for k in range(n) if k not in (i,j)]
        for oz in product((0,1), repeat=len(O)):
            Aoo=principal(K,O)
            for t,b in enumerate(oz): Aoo[t][t]-=1-b
            C=sub(principal(K,[i,j]),mm(mm(minor(K,[i,j],O),inv(Aoo)),minor(K,O,[i,j])))
            q,r=C[0][0],C[1][1]; s=C[0][1]*C[1][0]
            ps={(0,0):(1-q)*(1-r)-s,(1,0):q*(1-r)+s,(0,1):(1-q)*r+s,(1,1):q*r-s}
            au.check(sum(ps.values(),F(0))==1,'pair_table','sum')
            au.check(ps[(1,0)]*ps[(0,1)]-ps[(0,0)]*ps[(1,1)]==s,'pair_table','BC-AD=s')
            au.check(sum((1/v for v in ps.values()),F(0))>0,'pair_table','positive reciprocal sum')
            for b in ps:
                y=[0]*n
                for k,z in zip(O,oz): y[k]=z
                y[i],y[j]=b
                yy=tuple(y); Ay=[row[:] for row in K]
                for k,z in enumerate(yy): Ay[k][k]-=1-z
                G=inv(Ay)
                outside=F(0)
                for bi,bj in product((0,1),repeat=2):
                    z=list(yy); z[i]=bi; z[j]=bj; outside+=yatoms[tuple(z)]
                pcond=yatoms[yy]/outside
                au.check(pcond==ps[b],'pair_completion_probability',f'{i},{j},{oz},{b}')
                au.check(G[i][j]*G[j][i]==s/(pcond*pcond),'pair_inverse_completion',f'{i},{j},{oz},{b}')
            avg=F(0)
            for b,pb in ps.items():
                yy=[0]*n
                for k,z in zip(O,oz): yy[k]=z
                yy[i],yy[j]=b
                Ay=[row[:] for row in K]
                for k,z in enumerate(yy): Ay[k][k]-=1-z
                G=inv(Ay); avg+=pb*G[i][j]*G[j][i]
            au.check(avg==s*sum((1/v for v in ps.values()),F(0)),'completion_average','s Lambda prime')

    def variance_identity(R,f):
        mu=sum((f[i]*R[i][i] for i in range(n)),F(0))
        e2=sum((f[i]*f[i]*R[i][i] for i in range(n)),F(0))
        for i,j in combinations(range(n),2):
            e2+=2*f[i]*f[j]*det(principal(R,[i,j]))
        var=e2-mu*mu
        rhs=F(0)
        for i in range(n):
            for j in range(n): rhs+=F(1,2)*R[i][j]*R[j][i]*(f[i]-f[j])**2
        R2=mm(R,R)
        rhs+=sum((f[i]*f[i]*(R[i][i]-R2[i][i]) for i in range(n)),F(0))
        return var==rhs
    k=0
    while au.n<1004:
        y=words[k%len(words)]
        f=[F((k+1)*(i+2)+(-1)**i, (k%7)+3+i) for i in range(n)]
        au.check(variance_identity(postkern[y],f),'variance_decomposition',f'k={k},y={y}')
        k+=1
    if au.n!=1004: raise ArithmeticError(f'check count {au.n} != 1004')
    return au,Q,K,a,c


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,required=True); args=ap.parse_args()
    start=time.perf_counter(); au,Q,K,a,c=main_checks()
    out={
      'status':'PASS','individual_checks':au.n,
      'fixture':{'n':3,'a':str(a),'c':str(c),'nonprojection_Q':[[str(x) for x in r] for r in Q]},
      'sections':dict(sorted(au.sections.items())),
      'exact_arithmetic':'fractions.Fraction only for all sign/equality decisions',
      'optimized_mode_safe':'no assert statements are used for validation',
      'review_status':'same-author exact certificate; independent review pending',
      'elapsed_seconds_diagnostic':time.perf_counter()-start,
    }
    args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(out,indent=2)+'\n')
    print('PASS',au.n)

if __name__=='__main__': main()
