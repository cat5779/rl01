from pathlib import Path
from itertools import permutations
import sympy as S,json
r1,r2,r3,s0,s1,s2,s3=S.symbols('r1 r2 r3 s0 s1 s2 s3', positive=True)
vs=(r1,r2,r3,s0,s1,s2,s3)
L=S.zeros(4)
for i,r in enumerate((r1,r2,r3)):
 L[i,i]+=1/r;L[i+1,i+1]+=1/r;L[i,i+1]-=1/r;L[i+1,i]-=1/r
def det4(m):
 return S.expand(sum((-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))*S.prod(m[i,p[i]] for i in range(4)) for p in permutations(range(4))))
detpoly=S.expand(det4(S.eye(4)+S.diag(s0,s1,s2,s3)*L)*r1*r2*r3)
A=r1+s0;B=r3+s3;C=r2+s1+s2
Z=S.expand(A*B*C+r2*(s1*B+s2*A+s1*s2)+s1*s2*(A+B))
assert S.expand(detpoly-Z)==0
assert len(S.Poly(Z,vs).terms())==21
Zalt=(r2*(r1+s0+s1)+s1*(r1+s0))*(r3+s2+s3)+(r1+s0+s1)*s2*(r3+s3)
assert S.expand(Z-Zalt)==0
G=r1*r3*C/Z;records={}
for x in vs:
 sign=1 if x in (r1,r3) else -1
 num=S.Poly(S.cancel(sign*S.diff(G,x)).as_numer_denom()[0],vs)
 assert all(c>=0 for c in num.coeffs())
 records[str(x)]={'monotonicity':'increasing' if sign==1 else 'decreasing','numerator_nonnegative_coefficients':True}
 if sign==-1:
  num2=S.Poly(S.cancel(S.diff(G,x,2)).as_numer_denom()[0],vs)
  assert all(c>=0 for c in num2.coeffs())
  records[str(x)]['separately_convex']=True
assert S.cancel(G.subs(r2,0)-r1*r3/(A*B+(A+B)*s1*s2/(s1+s2)))==0
# Weighted spanning trees after the two selected conductances are removed:
full=L+S.diag(1/s0,1/s1,1/s2,1/s3)
empty_selected=full.copy()
for i,r in [(0,r1),(2,r3)]:
 empty_selected[i,i]-=1/r;empty_selected[i+1,i+1]-=1/r
 empty_selected[i,i+1]+=1/r;empty_selected[i+1,i]+=1/r
assert S.cancel(det4(empty_selected)/det4(full)-G)==0
green=lambda d:S.Rational(2,3)*S.Rational(1,2)**d
kdiag=2*green(0)-2*green(1)
kadj=2*green(1)-green(0)-green(2)
kfar=2*green(2)-green(1)-green(3)
assert (1-kdiag)**2-kadj**2==S.Rational(1,12)
assert (1-kdiag)**2-kfar**2==S.Rational(5,48)
out=dict(status='PASS_ROOT_SYMBOLIC_NETWORK_AND_DERIVATIVE_CHECK',determinant_terms=21,derivatives=records,selected_vacancy_tree_ratio=True,adjacent_target='1/12',distance_two_target='5/48',scope='finite circuit identities and signs only; infinite bridge separately read')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
