#!/usr/bin/env python3
"""Exact finite falsification tests of endpoint-only PSD allocation and Jensen.
These tests are not the sine-law continuum certificate. All arithmetic is rational.
"""
from fractions import Fraction as F
from pathlib import Path
import json
v=[1,2,3,-1,-2,-3]
Q=[[F(1,6)+F(v[i]*v[j],28) for j in range(4)] for i in range(4)]
def invdet(A):
 n=len(A);A=[r[:] for r in A];B=[[F(i==j) for j in range(n)] for i in range(n)];det=F(1)
 for k in range(n):
  h=next(i for i in range(k,n) if A[i][k])
  if h!=k:A[h],A[k]=A[k],A[h];B[h],B[k]=B[k],B[h];det=-det
  pivot=A[k][k];det*=pivot;A[k]=[z/pivot for z in A[k]];B[k]=[z/pivot for z in B[k]]
  for i in range(n):
   if i==k:continue
   z=A[i][k];A[i]=[x-z*y for x,y in zip(A[i],A[k])];B[i]=[x-z*y for x,y in zip(B[i],B[k])]
 return B,det

def law(c,p):
 a=(1-c)*p;pi=[];G=[]
 for w in range(16):
  A=[[c*Q[i][j]+F(i==j)*(a-F(1-((w>>i)&1))) for j in range(4)] for i in range(4)]
  g,d=invdet(A);pi.append((-1)**(4-w.bit_count())*d);G.append(g)
 assert min(pi)>0 and sum(pi)==1
 return pi,G

def bits(w,W):return sum(((w>>i)&1)<<j for j,i in enumerate(W))
def marginal(pi,W):return [sum((pi[w] for w in range(16) if bits(w,W)==z),F(0)) for z in range(8)]
def scores(pi):return [[F(2*((z>>i)&1)-1)*(1+pi[z^(1<<i)]/pi[z]) for i in range(3)] for z in range(8)]
def matrix(z):
 B=[[F(i==j) for j in range(3)] for i in range(3)]
 B[0][1]=B[1][0]=F(1,10)+F((z>>2)&1,100)
 B[0][2]=B[2][0]=F(1,9)+F((z>>1)&1,101)
 B[1][2]=B[2][1]=F(1,8)+F(z&1,103)
 return B

def quad(x,B,y=None):
 if y is None:y=x
 return sum((x[i]*B[i][j]*y[j] for i in range(3) for j in range(3)),F(0))
B=[matrix(z) for z in range(8)]
# Strict diagonal dominance is a rational PSD proof: split each off-diagonal
# pair into a rank-one PSD block and leave positive diagonal residuals.
for z in range(8):
 for i in range(3):assert B[z][i][i]-sum((abs(B[z][i][j]) for j in range(3) if j!=i),F(0))>0
 for i in range(3):
  for j in range(3):
   if i!=j:assert B[z][i][j]==B[z^(1<<i)][i][j]==B[z^(1<<j)][i][j]
# Explicitly NOT measurable outside the entire three-target set.
assert B[0][0][1]!=B[4][0][1]
pi0,_=law(F(19,20),F(1,2));windows=[(0,1,2),(1,2,3)]
fixed=[scores(marginal(pi0,W)) for W in windows]
results=[]
for c,p in [(F(951,1000),F(113,250)),(F(119,125),F(21,50)),(F(24,25),F(9,20))]:
 pi,G=law(c,p);Z=[[G[w][i][i] for i in range(4)] for w in range(16)]
 full_quadratics=F(0);local_quadratics=F(0);payments=F(0);jensen_gaps=[];dual_gaps=[]
 for W,f in zip(windows,fixed):
  pm=marginal(pi,W);zloc=scores(pm)
  g=[[sum((B[z][i][j]*f[z][j] for j in range(3)),F(0)) for i in range(3)] for z in range(8)]
  potential=[]
  for z in range(8):
   V=2*sum((g[z|(1<<i)][i]-g[z&~(1<<i)][i] for i in range(3)),F(0))-quad(f[z],B[z])
   factored=sum((B[z][i][i]*(2*(f[z|(1<<i)][i]-f[z&~(1<<i)][i])-f[z][i]**2) for i in range(3)),F(0))
   factored+=sum((2*B[z][i][j]*(f[z|(1<<i)][j]-f[z&~(1<<i)][j]+f[z|(1<<j)][i]-f[z&~(1<<j)][i]-f[z][i]*f[z][j]) for i in range(3) for j in range(i+1,3)),F(0))
   assert V==factored
   potential.append(V)
  fq=sum((pi[w]*quad([Z[w][i] for i in W],B[bits(w,W)]) for w in range(16)),F(0))
  lq=sum((pm[z]*quad(zloc[z],B[z]) for z in range(8)),F(0))
  P=sum((pm[z]*potential[z] for z in range(8)),F(0))
  variance=sum((pi[w]*quad([Z[w][i]-zloc[bits(w,W)][j] for j,i in enumerate(W)],B[bits(w,W)]) for w in range(16)),F(0))
  sq=sum((pm[z]*quad([zloc[z][i]-f[z][i] for i in range(3)],B[z]) for z in range(8)),F(0))
  assert fq-lq==variance>=0 and lq-P==sq>=0
  full_quadratics+=fq;local_quadratics+=lq;payments+=P;jensen_gaps.append(str(variance));dual_gaps.append(str(sq))
 # C=2, constant delta=3/10 on the five pairs appearing in the two windows.
 edges=sorted(set((W[i],W[j]) for W in windows for i in range(3) for j in range(i+1,3)))
 for w in range(16):
  for i in range(4):assert sum(F(1) for W in windows if i in W)<=2
  for i,j in edges:
   allocation=sum((B[bits(w,W)][W.index(i)][W.index(j)] for W in windows if i in W and j in W),F(0))
   assert F(3,10)-allocation>=0
 budget=2*sum((pi[w]*Z[w][i]**2 for w in range(16) for i in range(4)),F(0))
 budget+=2*F(3,10)*sum((pi[w]*G[w][i][j]**2 for w in range(16) for i,j in edges),F(0))
 assert budget>=full_quadratics>=local_quadratics>=payments
 results.append({'c':str(c),'p':str(p),'allocation_residual':str(budget-full_quadratics),'jensen_gaps':jensen_gaps,'dual_gaps':dual_gaps})
out={'status':'PROVED exact finite identities and inequalities','scope':'combined endpoint-only PSD allocation, score martingale and variational-payment unit tests; not an entropy-rate theorem','Q':[[str(x) for x in row] for row in Q],'windows':[list(W) for W in windows],'C':'2','pair_delta':'3/10','matrix_rule':'diag=1; B01=1/10+y2/100; B02=1/9+y1/101; B12=1/8+y0/103','parameter_cases':results}
Path('../evidence/exact_block_test.json').write_text(json.dumps(out,indent=2)+'\n')
print('EXACT_BLOCK_TOOL_PASS parameter_cases 3 windows_per_case 2; complete rational residuals in evidence')
