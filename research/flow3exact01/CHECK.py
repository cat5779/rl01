"""Independent symbolic verification of the exact three-input certificates.
All matrix atoms, directional derivatives and duals are rebuilt from the
frozen task. No result file or external author's code is executed.
"""
from pathlib import Path
import sympy as S
import json,hashlib
eta,h=S.symbols('eta h', real=True);t=eta/21
A=S.Matrix([[-11,13,-2],[13,-2,-11],[-2,-11,13]])
P=S.ones(3)/3;K=S.eye(3)/2+t*A
assert A*S.ones(3,1)==S.zeros(3,1)
assert A*A==441*(S.eye(3)-P)
assert A.trace()==0 and K*P==P/2 and P*K==P/2
edges=[(x,i) for x in range(8) for i in range(3) if not x>>i&1]
def atom(L,x):return S.expand((-1)**(3-x.bit_count())*(L-S.diag(*[int(not(x>>i&1)) for i in range(3)])).det())
p=S.Matrix([atom(K,x) for x in range(8)])
b=S.Matrix([S.diff(atom(K+h*P,x),h).subs(h,0) for x in range(8)])
q=S.Rational(1,4)-eta**2;hh=S.Rational(1,12)+eta**2
for i,ai in enumerate([-11,-2,13]):
 assert S.expand(p[1<<i]-(S.Rational(1,8)+ai*t/2+eta**2/6))==0
 assert S.expand(p[7^(1<<i)]-(S.Rational(1,8)-ai*t/2+eta**2/6))==0
 assert S.expand(b[1<<i]-(-hh-ai*t))==0
 assert S.expand(b[7^(1<<i)]-(hh-ai*t))==0
assert p[0]==p[7]==q/2 and b[0]==-q and b[7]==q
D=S.zeros(8,12)
for j,(x,i) in enumerate(edges):D[x,j]=-1;D[x|1<<i,j]=1
def rot(x):return ((x<<1)&7)|(x>>2)
def rv(v):
 out=S.zeros(8,1)
 for x in range(8):out[rot(x)]=v[x]
 return out
def re(v):
 out=S.zeros(12,1)
 for j,(x,i) in enumerate(edges):out[edges.index((rot(x),(i+1)%3))]=v[j]
 return out
middle=[(1,1),(2,0),(2,2),(4,1),(4,0),(1,2)]
ss=S.Rational(1,12)-eta**2/3;rr=S.Rational(1,12)+eta**2/3
f=S.Matrix([ss]*12);cyc=S.zeros(12,1)
for edge,coef,sgn in zip(middle,[-8,-5,3,8,5,-3],[1,-1,1,-1,1,-1]):
 j=edges.index(edge);f[j]=rr+t*coef;cyc[j]=sgn
fs=[f,re(f),re(re(f))];bs=[b,rv(b),rv(rv(b))]
assert D*cyc==S.zeros(8,1)
for ff,bb in zip(fs,bs):assert all(S.expand(x)==0 for x in D*ff-bb)
g=fs[1]+2*t*cyc
assert all(S.expand(x)==0 for x in D*g-bs[1])
# Lower estimates valid uniformly 0 <= eta <= 1/10, dropping positive eta^2 terms.
assert S.Rational(1,12)-S.Rational(1,300)>0
assert S.Rational(1,12)-8*S.Rational(1,210)==S.Rational(19,420)
assert min([5+2,-3-2,-8+2,-5-2,3+2,8-2])>=-8
atom_lower=S.Rational(1,8)-13*S.Rational(1,420)
assert atom_lower==S.Rational(79,840)
assert S.Rational(1,8)-S.Rational(1,200)>atom_lower
out_upper=S.Rational(1,3)+13*S.Rational(1,210)
assert out_upper==S.Rational(83,210)
assert 5*atom_lower-out_upper==S.Rational(3,40)
assert S.expand(sum(x.bit_count()*b[x] for x in range(8)))==1
phi=S.zeros(8,1)
for i,v in enumerate([S.Rational(1,2),-S.Rational(1,2),-S.Rational(1,2)]):phi[1<<i]=v;phi[7^(1<<i)]=v
grad=D.T*phi;assert all(abs(v)<=1 for v in grad)
assert S.expand((phi.T*(bs[0]-bs[1]))[0])==48*t
d=fs[0]-g
coefs=[S.simplify(v/t) for v in d]
assert sum(abs(v) for v in coefs)==48
active=[j for j,v in enumerate(grad) if abs(v)==1]
assert len(active)==4 and D[:,active].rank()==4
assert all(d[j]==0 for j in range(12) if j not in active)
assert all(S.simplify(d[j]/t)*grad[j]>=0 for j in active)
assert all(S.expand(x)==0 for x in d+re(d)+re(re(d))+6*t*cyc)
psi=S.Matrix([S.Rational(2,3),1,1,0,0,1,1,S.Rational(2,3)])
psis=[psi,rv(psi),rv(rv(psi))];grads=[D.T*v for v in psis]
for j in range(12):
 vals=[v[j] for v in grads]
 assert sum(vals)==0 and sum(max(v,0) for v in vals)<=1
for vv,bb in zip(psis,bs):assert S.expand((vv.T*bb)[0])==26*t
for i,j in [(0,1),(0,2),(1,2)]:assert sum(abs(S.simplify(v/t)) for v in fs[i]-fs[j])==52
perm=S.zeros(3,3)
for i in range(3):perm[(i+1)%3,i]=1
assert K*(perm*K*perm.T)-(perm*K*perm.T)*K!=S.zeros(3,3)
result=dict(status='PASS_EXACT_SYMBOLIC_UNIFORM_INTERVAL_CERTIFICATES',matrix_spectrum='1/2-eta,1/2,1/2+eta',atoms=[str(v) for v in p],divergence=[str(v) for v in b],edges=edges,pair_dual=[str(v) for v in phi],pair_difference_coefficients=[str(v) for v in coefs],pair_saturated_incidence_rank=4,triple_dual=[str(v) for v in psi],triple_edge_gradients=[[str(v[j]) for v in grads] for j in range(12)],pair_optimum='48 eta/21',triple_optimum='52 eta/21',capacity_margin_lower='3/40',interval='0<eta<=1/10',scope='fixed three-input subproblem only; not general FC or novelty')
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','pair_optimum','triple_optimum','capacity_margin_lower']}))
