#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEN = 10**8
coeff = []
for line in (ROOT / 'payment_coefficients_s69_integer.txt').read_text().splitlines():
    lo, hi = map(int, line.split())
    assert lo <= hi
    coeff.append((F(lo, DEN), F(hi, DEN)))
assert len(coeff) == 9

# Exact transcendental input: alpha0=sqrt(3)/(2*pi).
def atan_bracket(x, m=64):
    assert m % 2 == 0
    partial = sum(((-1)**k * x**(2*k+1) / F(2*k+1) for k in range(m)), F(0))
    return partial, partial + x**(2*m+1)/F(2*m+1)
l5,u5=atan_bracket(F(1,5)); l239,u239=atan_bracket(F(1,239))
pi_lo=16*l5-4*u239; pi_hi=16*u5-4*l239
al,ah,aden=map(int,(ROOT/'alpha60.txt').read_text().split())
assert 4*F(al,aden)**2*pi_hi**2 < 3 < 4*F(ah,aden)**2*pi_lo**2
al19=F(2756644477108960247,10**19); ah19=F(2756644477108960248,10**19)
assert 4*al19**2*pi_hi**2 < 3 < 4*ah19**2*pi_lo**2
print('ALPHA PASS exact 19- and 60-place brackets')

# Elementary exact polynomial utilities, coefficients in ascending power order.
def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def add(p, q):
    r = [F(0) for _ in range(max(len(p), len(q)))]
    for i, x in enumerate(p): r[i] += x
    for i, x in enumerate(q): r[i] += x
    return trim(r)

def sub(p, q):
    return add(p, [-x for x in q])

def mul(p, q):
    r = [F(0) for _ in range(len(p) + len(q) - 1)]
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i+j] += x*y
    return trim(r)

def scale(p, s):
    return trim([s*x for x in p])

def compose_affine(p, a0, h):
    # p(a0+h*x), exact expansion.
    out = [F(0)]
    power = [F(1)]
    lin = [a0, h]
    for ak in p:
        out = add(out, scale(power, ak))
        power = mul(power, lin)
    return trim(out)

def power_to_bernstein(p):
    n = len(p)-1
    p = p + [F(0)]*(n+1-len(p))
    return [sum(p[k]*F(comb(j,k), comb(n,k)) for k in range(j+1)) for j in range(n+1)]

def split_bernstein_half(b):
    levels = [list(b)]
    while len(levels[-1]) > 1:
        prev = levels[-1]
        levels.append([(prev[i]+prev[i+1])/2 for i in range(len(prev)-1)])
    left = [levels[i][0] for i in range(len(b))]
    right = [levels[len(b)-1-i][i] for i in range(len(b))]
    return left, right

def certify_positive_bernstein(b, max_depth=30):
    stack = [(b, 0, F(0), F(1))]
    leaves = 0
    min_coeff = None
    worst_interval = None
    while stack:
        bb, depth, l, r = stack.pop()
        m = min(bb)
        if m > 0:
            leaves += 1
            if min_coeff is None or m < min_coeff:
                min_coeff = m; worst_interval = (l, r)
            continue
        if max(bb) <= 0:
            raise AssertionError(f'nonpositive polynomial certified on [{l},{r}]')
        if depth >= max_depth:
            raise AssertionError(f'Bernstein refinement exhausted on [{l},{r}], min={m}')
        bl, br = split_bernstein_half(bb)
        mid = (l+r)/2
        stack.append((br, depth+1, mid, r))
        stack.append((bl, depth+1, l, mid))
    return leaves, min_coeff, worst_interval

# Remainder from the omitted q_8,q_9,... terms.
x = F(11,50)  # 2*m*max|a-a*| = 44/200 on K
raw_tail = F(1550)*x**8/F(factorial(8))/(1-x/F(9))
assert raw_tail < F(1,10**6)
REMAINDER = F(1,10**6)
ETA = F(1,1000)

# Common exact burden ingredients.
c = F(19,20)
C = [F(6501,5000), F(2067,400)]  # C(a)
Cm1 = [C[0]-1, C[1]]
a_poly = [F(0), F(1)]
b0 = mul(a_poly, [F(1),F(-1)])
b1 = mul([c, F(1)], [F(1)-c, F(-1)])
D = mul(b0,b1)
N = add(scale(b1,F(2,3)), scale(b0,F(1,3)))

# Convert the t-polynomial lower envelope to an a-polynomial.
# t=200(a-1/40) = -5 + 200a.
def tpoly_to_apoly(pk):
    out=[F(0)]
    power=[F(1)]
    tlin=[F(-5),F(200)]
    for v in pk:
        out=add(out,scale(power,v))
        power=mul(power,tlin)
    return trim(out)

segments = [
    ('lower', F(1,50), F(1,40), [lo if k%2==0 else hi for k,(lo,hi) in enumerate(coeff)]),
    ('upper', F(1,40), F(51,2000), [lo for lo,hi in coeff]),
]

print(f'TAIL exact upper = {raw_tail} = {float(raw_tail):.18g} < 1/1000000')
bern_out=[]
for name,a0,a1,pk in segments:
    P = tpoly_to_apoly(pk)
    Pminus = list(P)
    Pminus[0] -= REMAINDER + ETA
    G = sub(mul(Pminus,D), mul(Cm1,N))
    Gx = compose_affine(G,a0,a1-a0)
    bern = power_to_bernstein(Gx)
    leaves,mn,where = certify_positive_bernstein(bern)
    print(f'PAYMENT {name} PASS interval [{a0},{a1}] degree {len(bern)-1} leaves {leaves} min_Bernstein {mn} ~ {float(mn):.18g} local_x {where}')
    bern_out.append(f'[{name}] a0={a0} a1={a1} degree={len(bern)-1}\n')
    bern_out.extend(f'{j} {v.numerator} {v.denominator}\n' for j,v in enumerate(bern))
(ROOT/'bernstein_payment_s69.txt').write_text(''.join(bern_out))

# Uniform payment upper M=19 by absolute coefficient sum on |t|<=1.
Pabs = sum(max(abs(lo),abs(hi)) for lo,hi in coeff) + REMAINDER
assert Pabs < 19
print(f'PAYMENT UPPER PASS abs_sum {Pabs} ~ {float(Pabs):.18g} < 19')

# PSD and no-double-spending endpoint checks for all 256 guard words.
caps=[]
for line in (ROOT/'guard_caps_integer.txt').read_text().splitlines():
    L,U=map(int,line.split()); caps.append((L,U))
assert len(caps)==256
K0,K1=F(1,50),F(51,2000)
min_delta=None; min_slack=None; arg_delta=None; arg_slack=None
for z,(L,U) in enumerate(caps):
    # c_z(a)=100*((.03-a)L/10000+(a-.02)U/10000)
    # = ((3/100-a)L + (a-1/50)U)/100
    cap=[F(3*L,10000)-F(L,100)*F(0) - F(U,5000), F(U-L,100)]
    # Simpler exact intercept: (3L/100 -? derive directly by evaluating affine endpoints below)
    def cz(a):
        return F(1,100)*((F(3,100)-a)*L + (a-F(1,50))*U)
    for a in (K0,K1):
        cc=C[0]+C[1]*a
        delta=cc-cz(a)
        slack=cc/2-delta
        if min_delta is None or delta<min_delta: min_delta,arg_delta=delta,(z,a)
        if min_slack is None or slack<min_slack: min_slack,arg_slack=slack,(z,a)
        assert delta >= 0
        assert slack >= 0
print(f'PSD PASS min_delta {min_delta} ~ {float(min_delta):.18g} at {arg_delta}')
print(f'PSD PASS min_halfdiag_minus_delta {min_slack} ~ {float(min_slack):.18g} at {arg_slack}')

# Endpoint legality and denominator positivity are exact.
assert K0>0 and K1<F(1,20)
for a in (K0,K1):
    assert a*(1-a)>0 and (a+c)*(1-a-c)>0
print('RATIONAL S69 PASS eta 1/1000 M 19 K [1/50,51/2000]')
