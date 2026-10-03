"""Exact formal determinant check of the distance-two circuit polynomial."""
from itertools import permutations
from pathlib import Path
import json

ZERO=(0,)*7
def add(a,b):
    c=dict(a)
    for key,val in b.items():
        c[key]=c.get(key,0)+val
        if not c[key]:del c[key]
    return c
def mul(a,b):
    c={}
    for ka,va in a.items():
        for kb,vb in b.items():
            key=tuple(x+y for x,y in zip(ka,kb))
            c[key]=c.get(key,0)+va*vb
    return {k:v for k,v in c.items() if v}
def neg(a):return {k:-v for k,v in a.items()}
def monomial(index,power=1):
    exps=list(ZERO);exps[index]=power
    return {tuple(exps):1}
ONE={ZERO:1}
r=[monomial(i) for i in range(3)]
rr=[monomial(i,-1) for i in range(3)]
s=[monomial(i+3) for i in range(4)]
matrix=[[{} for _ in range(4)] for _ in range(4)]
for i in range(4):matrix[i][i]=ONE
for edge in range(3):
    a=mul(s[edge],rr[edge]);b=mul(s[edge+1],rr[edge])
    matrix[edge][edge]=add(matrix[edge][edge],a)
    matrix[edge+1][edge+1]=add(matrix[edge+1][edge+1],b)
    matrix[edge][edge+1]=neg(a)
    matrix[edge+1][edge]=neg(b)
det={}
for order in permutations(range(4)):
    sign=(-1)**sum(order[i]>order[j] for i in range(4) for j in range(i+1,4))
    term={ZERO:sign}
    for i,j in enumerate(order):term=mul(term,matrix[i][j])
    det=add(det,term)
den=mul(mul(mul(r[0],r[1]),r[2]),det)
expected={}
def term(*variables):
    out=ONE
    for a in variables:out=mul(out,a)
    return out
for t in (
    term(*r),term(r[1],r[2],add(s[0],s[1])),
    term(r[0],r[2],add(s[1],s[2])),term(r[0],r[1],add(s[2],s[3])),
    term(r[2],add(add(term(s[0],s[1]),term(s[0],s[2])),term(s[1],s[2]))),
    term(r[1],add(s[0],s[1]),add(s[2],s[3])),
    term(r[0],add(add(term(s[1],s[2]),term(s[1],s[3])),term(s[2],s[3]))),
    term(s[0],s[1],s[2]),term(s[0],s[1],s[3]),
    term(s[0],s[2],s[3]),term(s[1],s[2],s[3])):
    expected=add(expected,t)
assert den==expected
assert all(all(a>=0 for a in k) for k in den)
A=add(r[0],s[0]); B=add(r[2],s[3]); C=add(add(r[1],s[1]),s[2])
compact=add(term(A,B,C),add(term(r[1],add(add(term(s[1],B),term(s[2],A)),term(s[1],s[2]))),term(s[1],s[2],add(A,B))))
assert compact==den
left2=add(add(r[0],s[0]),s[1])
left0=add(term(r[1],left2),term(s[1],add(r[0],s[0])))
different=add(term(left0,add(add(r[2],s[2]),s[3])),term(left2,s[2],add(r[2],s[3])))
assert different==den
contracted={k:v for k,v in den.items() if k[1]==0}
# Division by s1+s2 is deliberately not formalized at its zero locus.
# The exact r2=0 denominator is AB(s1+s2)+(A+B)s1s2.
assert contracted==add(term(A,B,add(s[1],s[2])),term(add(A,B),s[1],s[2]))
record={'status':'PROVED','scope':'finite formal Laurent-polynomial determinant and condensed/contracted denominator identities only','denominator_terms':len(den),'variables':['r1','r2','r3','s0','s1','s2','s3'],'no_probabilistic_or_uniform_lambda_claim':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print(json.dumps(record))
