#!/usr/bin/env python3
"""Exact-rational continuum closure for the QWE07 density certificate.
No third-party modules. Every input numerator has its mathematical meaning
in QWE07_RESULT.md; checks are mathematical coverage, not file hashes.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import argparse, json


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    r = [F(0)] * max(len(p), len(q))
    for i, v in enumerate(p): r[i] += v
    for i, v in enumerate(q): r[i] += v
    return trim(r)


def scale(p, v): return trim([x*v for x in p])


def mul(p, q):
    r = [F(0)]*(len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q): r[i+j] += x*y
    return trim(r)


def value(p, x):
    out = F(0)
    for v in reversed(p): out = out*x + v
    return out


def compose_affine(p, l, h):
    out = [F(0)]
    for v in reversed(p): out = add(mul(out, [l, h-l]), [v])
    return out


def bernstein(p, n=None):
    n = len(p)-1 if n is None else n
    assert n >= len(p)-1
    return [sum((p[i]*F(comb(k,i), comb(n,i)) for i in range(min(k+1,len(p)))), F(0)) for k in range(n+1)]


def certify_upper(p, bound, l=F(0), h=F(1), depth=0):
    b = bernstein(compose_affine(p,l,h))
    if max(b) <= bound: return 1, max(b)
    assert depth < 20, ("unresolved polynomial upper bound", l, h)
    m = (l+h)/2
    n0,b0 = certify_upper(p,bound,l,m,depth+1)
    n1,b1 = certify_upper(p,bound,m,h,depth+1)
    return n0+n1,max(b0,b1)


def lagrange(n):
    out = []
    for j in range(n+1):
        p = [F(1)]; denominator = F(1)
        for k in range(n+1):
            if j == k: continue
            p = mul(p,[-F(k,n),F(1)])
            denominator *= F(j-k,n)
        out.append(scale(p,1/denominator))
    return out


def lebesgue_certificate(n, bound):
    basis = lagrange(n); total = 0; worst = F(0)
    for cell in range(n):
        mid = F(2*cell+1,2*n)
        signed_sum = [F(0)]
        for p in basis:
            s = 1 if value(p,mid)>0 else -1
            signed_sum = add(signed_sum,scale(p,s))
        boxes, b = certify_upper(signed_sum,bound,F(cell,n),F(cell+1,n))
        total += boxes; worst = max(worst,b)
    return total,worst


def product_certificate(n,bound):
    p=[F(1)]
    for k in range(n+1): p=mul(p,[-F(k,n),F(1)])
    n0,b0=certify_upper(p,bound);n1,b1=certify_upper(scale(p,-1),bound)
    return n0+n1,max(b0,b1)


def atan_box(q, count=80):
    s=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(count)),F(0))
    next_term=F((-1)**count,(2*count+1)*q**(2*count+1))
    return min(s,s+next_term),max(s,s+next_term)


def constants():
    a5,b5=atan_box(5);a239,b239=atan_box(239)
    pi_lo,pi_hi=16*a5-4*b239,16*b5-4*a239
    assert F(3141592653589793238,10**18)<pi_lo<pi_hi<F(3141592653589793239,10**18)
    assert pi_hi < F(22,7)
    assert F(8,5)**25/F(factorial(25)) < F(1,10**20)
    x=F(33,50)
    s=sum((x**(2*k)/factorial(2*k+1) for k in range(20)),F(0))
    tail=x**40/F(factorial(41))/(1-x*x/F(42*43))
    assert s+tail<F(27,25)
    e11=sum((F(11)**k/factorial(k) for k in range(100)),F(0))
    e11 += F(11)**100/F(factorial(100))/(1-F(11,101))
    assert e11 < 60000
    assert F(19,20)*22*F(1,100)*F(27,25)/F(21,1000)==F(1881,175)<11
    prod4=product_certificate(4,F(1,250))
    prod10=product_certificate(10,F(1,200000))
    leb4=lebesgue_certificate(4,F(3))
    leb10=lebesgue_certificate(10,F(32))
    erho=F(1540*60000)*F(3,10)**11*F(1,200000)
    ea=F(44**5*1540+5*44**4*10000,factorial(5))*F(3,1000)**5*F(1,250)
    enode=32*3*F(1,10**8)
    total=erho+32*ea+enode
    assert total<F(1,1000)
    caps=[]
    for line in Path('guard_caps_integer.txt').read_text().splitlines():
        if line.strip(): caps.append(tuple(map(int,line.split())))
    assert len(caps)==256 and all(len(z)==2 for z in caps)
    mineig=F(100);mindelta=F(100)
    for lo,hi in caps:
        for a in (F(21,1000),F(3,125)):
            C=F(261,200)+F(51,10)*a
            cap=((F(3,100)-a)*lo+(a-F(1,50))*hi)/100
            delta=C-cap
            assert delta>=0 and C/2-delta>=0
            mineig=min(mineig,C/2-delta);mindelta=min(mindelta,delta)
    print('SINE: exact Machin enclosure and degree-23 remainder proved')
    print('ANALYTIC: trace/gap <= 1881/175 < 11; exp(11) < 60000 proved')
    for name,obj in [('product_4',prod4),('product_10',prod10),('Lebesgue_4',leb4),('Lebesgue_10',leb10)]:
        print(name,'certified boxes',obj[0],'upper',float(obj[1]))
    print('ERROR density',erho,'bias',ea,'nodal',enode,'TOTAL',total,'=',float(total),'< 1/1000')
    print('PSD minimum eigenvalue',mineig,'minimum improvement',mindelta)
    return total


def bernstein2(p,nr,na):
    return [[sum((p.get((i,j),F(0))*F(comb(k,i),comb(nr,i))*F(comb(l,j),comb(na,j))
                  for i in range(k+1) for j in range(l+1)),F(0))
             for l in range(na+1)] for k in range(nr+1)]


def prove_payment():
    rows={}
    for line in Path('nodes_integer.txt').read_text().splitlines():
        if not line.strip() or line.startswith('#'): continue
        j,k,lo,hi,den=map(int,line.split())
        assert (j,k) not in rows and den==10**8 and 0<=hi-lo<=2
        rows[j,k]=F(lo+hi,2*den)
    assert set(rows)=={(j,k) for j in range(11) for k in range(5)}
    lr,la=lagrange(10),lagrange(4)
    T={(i,j):F(0) for i in range(11) for j in range(5)}
    for (r,a),mid in rows.items():
        for i,cr in enumerate(lr[r]):
            for j,ca in enumerate(la[a]): T[i,j] += mid*cr*ca
    # a=21/1000+(3/1000)x, rho=1/3+(3/1000)t.
    ap=[F(21,1000),F(3,1000)]; one_minus_a=add([1],scale(ap,-1))
    v=add(ap,[F(19,20)]); one_minus_v=add([1],scale(v,-1))
    beta0=mul(ap,one_minus_a);beta1=mul(v,one_minus_v);D=mul(beta0,beta1)
    Cminus1=add([F(61,200)],scale(ap,F(51,10)))
    eta=F(1,25);error=F(1,1000)
    # G = D(T-error-eta) - (C0-1)((1-rho) beta1 + rho beta0).
    G={}
    for (i,j),q in T.items():
        for k,d in enumerate(D):G[i,j+k]=G.get((i,j+k),F(0))+q*d
    for k,d in enumerate(D):G[0,k]=G.get((0,k),F(0))-(eta+error)*d
    budget0=mul(Cminus1,add(scale(beta1,F(2,3)),scale(beta0,F(1,3))))
    budget1=mul(Cminus1,scale(add(beta0,scale(beta1,-1)),F(3,1000)))
    for k,q in enumerate(budget0):G[0,k]=G.get((0,k),F(0))-q
    for k,q in enumerate(budget1):G[1,k]=G.get((1,k),F(0))-q
    bc=bernstein2(G,10,8)
    minimum=min(q for row in bc for q in row)
    assert minimum>0,('payment Bernstein obstruction',minimum)
    upper={key:-q for key,q in T.items()};upper[0,0]+=19-error
    ubc=bernstein2(upper,10,4)
    upper_min=min(q for row in ubc for q in row)
    assert upper_min>0,('P upper Bernstein obstruction',upper_min)
    # Store explicit rational coefficient arrays, not only success messages.
    Path('payment_bernstein_exact.json').write_text(json.dumps([[str(q) for q in row]for row in bc],indent=2)+'\n')
    Path('upper_bernstein_exact.json').write_text(json.dumps([[str(q) for q in row]for row in ubc],indent=2)+'\n')
    floored=[[q.numerator*10**9//q.denominator for q in row]for row in bc]
    Path('payment_bernstein_lower_numerators.txt').write_text('\n'.join(' '.join(map(str,row))for row in floored)+'\n')
    print('PAYMENT Bernstein size 11 x 9; minimum',minimum,'=',float(minimum))
    print('PAYMENT minimum numerator floor at denominator 1e9',min(v for row in floored for v in row))
    print('UPPER Bernstein size 11 x 5; minimum',upper_min,'=',float(upper_min))
    print('PROVED: P - (C0-1)d >= 1/25 and P <= 19 on the entire rectangle.')


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--constants-only',action='store_true');args=parser.parse_args()
    constants()
    if not args.constants_only:prove_payment()
