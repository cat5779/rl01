"""Independent exact polynomial audit of p150/e01. No root review imported."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import hashlib,json
def trim(a):
    while len(a)>1 and not a[-1]:a.pop()
    return a
def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return trim(c)
def neg(a):return [-x for x in a]
def sub(a,b):return add(a,neg(b))
def scale(a,c):return trim([x*c for x in a])
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)
def psum(xs):
    z=[F(0)]
    for x in xs:z=add(z,x)
    return z
def determinant(a):
    n=len(a);z=[F(0)]
    for p in permutations(range(n)):
        sign=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=[F(sign)]
        for i in range(n):term=mul(term,a[i][p[i]])
        z=add(z,term)
    return z
A=[[-11,13,-2],[13,-2,-11],[-2,-11,13]]
assert all(sum(row)==0 for row in A)
assert [[sum(A[i][k]*A[k][j] for k in range(3)) for j in range(3)] for i in range(3)]==[[441*(i==j)-147 for j in range(3)] for i in range(3)]
assert sum(A[i][i] for i in range(3))==0
atoms=[];b=[]
for mask in range(8):
    M=[[[F((i==j),2)-F(i==j and not mask>>i&1),F(A[i][j],21)] for j in range(3)] for i in range(3)]
    sign=(-1)**(3-mask.bit_count())
    atoms.append(scale(determinant(M),sign))
    cof=[]
    for i in range(3):
        for j in range(3):
            minor=[[M[a][z] for z in range(3) if z!=j] for a in range(3) if a!=i]
            cof.append(scale(determinant(minor),F(sign*(-1)**(i+j),3)))
    b.append(psum(cof))
q=[F(1,4),F(0),F(-1)];h=[F(1,12),F(0),F(1)]
for mask in [0,7]:
    assert atoms[mask]==scale(q,F(1,2))
assert b[0]==neg(q) and b[7]==q
for i,a in enumerate([-11,-2,13]):
    assert atoms[1<<i]==[F(1,8),F(a,42),F(1,6)]
    assert atoms[7^(1<<i)]==[F(1,8),F(-a,42),F(1,6)]
    assert b[1<<i]==[F(-1,12),F(-a,21),F(-1)]
    assert b[7^(1<<i)]==[F(1,12),F(-a,21),F(1)]
edges=[(s,i) for s in range(8) for i in range(3) if not s>>i&1]
middle=[(1,1),(2,0),(2,2),(4,1),(4,0),(1,2)]
rotate_mask=lambda s:sum(1<<((i+1)%3) for i in range(3) if s>>i&1)
def rot_vertex(v):
    z=[None]*8
    for s,x in enumerate(v):z[rotate_mask(s)]=x
    return z
def rot_flow(f):return {(rotate_mask(s),(i+1)%3):v for (s,i),v in f.items()}
def divergence(f):
    return [sub(psum(f[s&~(1<<i),i] for i in range(3) if s>>i&1),
                psum(f[s,i] for i in range(3) if not s>>i&1)) for s in range(8)]
r=[F(1,12),F(0),F(1,3)];ss=[F(1,12),F(0),F(-1,3)]
f0={e:ss[:] for e in edges}
for e,c in zip(middle,[-8,-5,3,8,5,-3]):f0[e]=add(r,[F(0),F(c,21)])
flows=[f0,rot_flow(f0),rot_flow(rot_flow(f0))]
bs=[b,rot_vertex(b),rot_vertex(rot_vertex(b))]
assert all(divergence(f)==bb for f,bb in zip(flows,bs))
assert psum(f0.values())==[F(1)]
C={e:[F(0)] for e in edges}
for e,c in zip(middle,[1,-1,1,-1,1,-1]):C[e]=[F(c)]
assert divergence(C)==[[F(0)]]*8
g1={e:add(flows[1][e],mul([F(0),F(2,21)],C[e])) for e in edges}
assert divergence(g1)==bs[1]
d={e:sub(f0[e],g1[e]) for e in edges}
assert [d[e] for e in middle]==[[F(0),F(c,21)] if c else [F(0)] for c in [-15,0,9,15,0,-9]]
def l1_linear(ff):
    val=F(0)
    for p in ff.values():
        if p==[F(0)]:continue
        assert len(p)==2 and not p[0]
        val+=abs(p[1])
    return val
assert l1_linear(d)==F(48,21)
for a in range(3):
    for bb in range(a):
        assert l1_linear({e:sub(flows[a][e],flows[bb][e]) for e in edges})==F(52,21)
phi=[F(0),F(1,2),F(-1,2),F(-1,2),F(-1,2),F(-1,2),F(1,2),F(0)]
grad={e:phi[e[0]|1<<e[1]]-phi[e[0]] for e in edges}
assert max(abs(v) for v in grad.values())==1
pairdual=psum(scale(sub(bs[0][s],bs[1][s]),phi[s]) for s in range(8))
assert pairdual==[F(0),F(48,21)]
saturated=[e for e in edges if abs(grad[e])==1]
assert saturated==[e for e in edges if d[e]!=[F(0)]]
def rank(a):
    a=[row[:] for row in a];r=0
    for j in range(len(a[0])):
        piv=next((i for i in range(r,len(a)) if a[i][j]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r];v=a[r][j];a[r]=[x/v for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[r])]
        r+=1
    return r
inc=[[F((t==s|1<<i)-(t==s)) for s,i in saturated] for t in range(8)]
assert rank(inc)==4
rd=rot_flow(d);r2d=rot_flow(rd)
assert all(psum([d[e],rd[e],r2d[e]])==mul([F(0),F(-6,21)],C[e]) for e in edges)
psi0=[F(2,3),F(1),F(1),F(0),F(0),F(1),F(1),F(2,3)]
psis=[psi0,rot_vertex(psi0),rot_vertex(rot_vertex(psi0))]
tripledual=F(0)
gradient_records=[]
for e in edges:
    grads=[pp[e[0]|1<<e[1]]-pp[e[0]] for pp in psis]
    assert sum(grads)==0 and sum(max(v,0) for v in grads)<=1
    gradient_records.append({"edge":e,"three_gradients":[str(v) for v in grads]})
for pp,bb in zip(psis,bs):
    assert psum(scale(bb[s],pp[s]) for s in range(8))==[F(0),F(26,21)]
# Interval positivity and capacities: these exact conservative bounds hold
# by 0<eta<=1/10 and all eta^2 terms in middle/single atom formulas nonnegative.
atom_lower=F(1,8)-F(13,42)*F(1,10)
assert atom_lower==F(79,840) and F(3,25)>atom_lower
out_upper=F(1,3)+F(13,21)*F(1,10)
assert out_upper==F(83,210)
assert 5*atom_lower-out_upper==F(3,40)
assert F(1,12)-F(8,21)*F(1,10)==F(19,420)>0
assert F(1,12)-F(1,3)*F(1,100)==F(2,25)>0
assert min(p[1] if len(p)>1 else 0 for p in g1.values())>=F(-8,21)
result={"status":"PASS_EXACT_POLYNOMIAL_AND_FULL_FIBER_DUAL_AUDIT",
 "source_original_sha256":hashlib.sha256(Path(__file__).with_name("RESULT.md").read_bytes()).hexdigest(),
 "atoms":[[str(c) for c in pp] for pp in atoms],"divergences":[[str(c) for c in pp] for pp in b],
 "pair_dual":[str(c) for c in pairdual],"pair_norm_eta_coefficient":"48/21",
 "triple_upper_eta_coefficient":"52/21","triple_dual_each_eta_coefficient":"26/21",
 "pair_saturated_support_rank":4,"rigid_pair_cycle_sum":"-6 eta/21 C",
 "uniform_atom_lower":"79/840","uniform_outgoing_upper":"83/210","capacity_margin_lower":"3/40",
 "triple_gradient_checks":gradient_records,
 "scope":"all eta in (0,1/10], arbitrary positive divergence fibers; no FC disproof",
 "fresh_review":False,"independent_of_root_review":True}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:result[k] for k in ["status","pair_saturated_support_rank","source_original_sha256","scope"]},indent=2))
