#!/usr/bin/env python3
"""Exact rational falsification/identity tests for the new tool, not asymptotics.
Q is a true finite compression of a rank-two projection in dimension six.
It is deliberately NOT a projection after compression, and need not be sine.
"""
from fractions import Fraction as F
from math import comb
import json
from pathlib import Path
n=4;N=1<<n
v=[1,2,3,-1,-2,-3]
Q=[[F(1,6)+F(v[i]*v[j],28) for j in range(n)] for i in range(n)]
def invdet(A):
 A=[r[:] for r in A];B=[[F(i==j) for j in range(n)] for i in range(n)];d=F(1)
 for k in range(n):
  h=next(i for i in range(k,n) if A[i][k])
  if h!=k:A[h],A[k]=A[k],A[h];B[h],B[k]=B[k],B[h];d=-d
  p=A[k][k];d*=p;A[k]=[z/p for z in A[k]];B[k]=[z/p for z in B[k]]
  for i in range(n):
   if i==k:continue
   z=A[i][k];A[i]=[x-z*y for x,y in zip(A[i],A[k])];B[i]=[x-z*y for x,y in zip(B[i],B[k])]
 return B,d

def law(c,p):
 a=(1-c)*p;prob=[];G=[]
 for w in range(N):
  A=[[c*Q[i][j]+F(i==j)*(a-F(1-((w>>i)&1))) for j in range(n)] for i in range(n)]
  g,d=invdet(A);z=(-1)**(n-w.bit_count())*d;assert z>0;prob.append(z);G.append(g)
 assert sum(prob)==1
 return prob,G

def walsh(x):
 x=x[:]
 for bit in range(n):
  h=1<<bit
  for b in range(0,N,2*h):
   for j in range(h):a,c=x[b+j],x[b+j+h];x[b+j],x[b+j+h]=a+c,a-c
 return x

def transport(prob,s,v0):
 q=prob[:]
 for bit in range(n):
  h=1<<bit
  for b in range(0,N,2*h):
   for j in range(h):
    x,y=q[b+j],q[b+j+h];delta=-s*(x+y)+v0*(x-y)/2;q[b+j],q[b+j+h]=x+delta,y-delta
 return q
p0,G0=law(F(19,20),F(1,2));count=0
# A genuinely spatial test: not a count function and not a kernel trace.
V=[F(7,3)*(((w>>0)&1)-((w>>2)&1))+F(5,7)*((w>>1)&1)*((w>>3)&1)+F(11,5)*(((w>>0)&1)^((w>>3)&1)) for w in range(N)]
qhat=walsh(p0);Vhat=walsh(V);co={}
for k in range(n+1):
 for l in range(n-k+1):
  co[k,l]=sum((qhat[w]*Vhat[w]*comb(w.bit_count()-k,l)/F(N*950**l) for w in range(N) if w.bit_count()>=k+l),F(0))
 work=[F(0)]*N
 for w in range(N):work[w]=sum((qhat[w^(1<<i)] for i in range(n) if (w>>i)&1),F(0))
 qhat=[-x/F(100*(k+1)) for x in work]
for c,p in [(F(951,1000),F(113,250)),(F(119,125),F(21,50)),(F(24,25),F(9,20))]:
 pi,G=law(c,p);s=(1-c)*(p-F(1,2));v0=(c-F(19,20))/F(19,20)
 assert transport(p0,s,v0)==pi;count+=N
 t=200*s;u=1000*(c-F(19,20));E=sum((pi[w]*V[w] for w in range(N)),F(0));Epoly=sum((z*t**k*u**l for (k,l),z in co.items()),F(0));assert E==Epoly;count+=1
 Z=[[G[w][i][i] for i in range(n)] for w in range(N)]
 for w in range(N):
  for i in range(n):assert Z[w][i]==F(2*((w>>i)&1)-1)*(1+pi[w^(1<<i)]/pi[w]);count+=1
 for i in range(n):
  g=[F((w+3)**2,17) for w in range(N)];lhs=sum((pi[w]*Z[w][i]*g[w] for w in range(N)),F(0));rhs=sum((pi[w]*(g[w|(1<<i)]-g[w&~(1<<i)]) for w in range(N)),F(0));assert lhs==rhs;count+=1
 for i in range(n):
  for j in range(i+1,n):
   k=next(k for k in range(n) if k not in (i,j));delta=[F(1,7)+F((w>>k)&1,13) for w in range(N)]
   assert sum((pi[w]*delta[w]*(Z[w][i]*Z[w][j]-G[w][i][j]**2) for w in range(N)),F(0))==0;count+=1
 # Marginal score martingale for A={0,1,2}: target-dependent B is measurable in A.
 pm=[pi[w]+pi[w|8] for w in range(8)]
 for w in range(8):
  for i in range(3):
   z=F(2*((w>>i)&1)-1)*(1+pm[w^(1<<i)]/pm[w]);assert pi[w]*Z[w][i]+pi[w|8]*Z[w|8][i]==pm[w]*z;count+=1
# Exact counterexample to a nilpotent contrast generator and to stochastic transport.
D=[[-1,-1],[1,1]];FF=[[F(1,2),F(-1,2)],[F(-1,2),F(1,2)]]
def mm(A,B):return [[sum((A[i][k]*B[k][j] for k in range(2)),F(0)) for j in range(2)] for i in range(2)]
assert mm(D,D)==[[0,0],[0,0]] and mm(FF,FF)==FF and FF!=[[0,0],[0,0]]
assert mm(D,FF)==[[0,0],[0,0]] and mm(FF,D)==D
# At s=0, positive v has negative off-diagonal transport entries.
assert F(-1,2)*F(1,950)<0
out={'status':'PROVED exact finite identities','checks':count,'configurations_per_law':N,'Q':[[str(z) for z in r] for r in Q],'scope':'tool unit tests only, not a sine entropy-rate theorem','falsifications':['F^2=F !=0: contrast generator is not nilpotent','positive contrast transport is signed, not a Markov post-processing kernel']}
Path('../evidence/exact_small_tests.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
