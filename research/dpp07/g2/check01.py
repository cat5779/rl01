"""Exact finite checks for the gradient-projection counterexample."""
from fractions import Fraction as F
from collections import deque
from itertools import combinations
from pathlib import Path
import json

adj={0:[]};depth={0:0};edges=[];front=deque([0])
while len(edges)<8:
 u=front.popleft()
 for _ in range(3 if u==0 else 2):
  v=len(adj);adj[v]=[u];adj[u].append(v);depth[v]=depth[u]+1;front.append(v)
  edges.append((u,v) if depth[u]%2==0 else (v,u))
  if len(edges)==8:break
dist={}
for start in adj:
 q=deque([(start,0)]);seen={start}
 while q:
  u,d=q.popleft();dist[start,u]=d
  for v in adj[u]:
   if v not in seen:seen.add(v);q.append((v,d+1))
def green(u,v):return F(2,3)*F(1,2)**dist[u,v]
K=[]
for a,b in edges:
 K.append([green(b,d)-green(b,c)-green(a,d)+green(a,c) for c,d in edges])
def det(a):
 a=[row[:] for row in a];out=F(1)
 for j in range(len(a)):
  k=next((k for k in range(j,len(a)) if a[k][j]),None)
  if k is None:return F(0)
  if k!=j:a[k],a[j]=a[j],a[k];out=-out
  pivot=a[j][j];out*=pivot
  for k in range(j+1,len(a)):
   t=a[k][j]/pivot
   for l in range(j+1,len(a)):a[k][l]-=t*a[j][l]
 return out
determinants={0:F(1)}
connected_checks=0
for mask in range(1,1<<len(edges)):
 indices=[i for i in range(len(edges)) if mask>>i&1]
 val=det([[K[i][j] for j in indices] for i in indices]);assert val>0
 determinants[mask]=val
 reached={indices[0]}
 while True:
  nxt=reached|{i for i in indices if any(set(edges[i])&set(edges[j]) for j in reached)}
  if nxt==reached:break
  reached=nxt
 if len(reached)==len(indices):
  m=len(indices);assert val==F(1,2)**m*(1+F(m,3));connected_checks+=1
def pattern(ones,zeros):
 out=F(0);sub=zeros
 while True:
  out+=(-1)**sub.bit_count()*determinants[ones|sub]
  if sub==0:break
  sub=(sub-1)&zeros
 return out
history_checks=zero_histories=0;minimum=F(1)
for i in range(len(edges)):
 previous=(1<<i)-1
 for ones in range(1<<i):
  zeros=previous^ones;denom=pattern(ones,zeros);assert denom>=0
  if denom==0:zero_histories+=1;continue
  conditional=pattern(ones|(1<<i),zeros)/denom
  assert F(1,2)<=conditional<=1
  minimum=min(minimum,conditional);history_checks+=1
result={'edge_count':len(edges),'principal_determinants_positive':len(determinants)-1,'connected_determinant_formula_checks':connected_checks,'positive_history_conditional_checks':history_checks,'zero_probability_histories_skipped':zero_histories,'minimum_conditional_probability':str(minimum),'required_lower_bound':'1/2','status':'PASS','scope':'FINITE_EXACT_AUXILIARY_CHECK_NOT_A_PROOF_OF_THE_INFINITE_STATEMENT'}
Path(__file__).with_name('check01.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
