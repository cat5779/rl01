#!/usr/bin/env python3
"""Exact dyadic interval certificate. Python standard library only.

No floating-point operation is used to decide a sign. True Toeplitz and
cyclic models are constructed separately. pi is enclosed by
Machin's identity and alternating-series bounds. log uses an atanh series with
an explicit positive tail. Every arithmetic operation rounds outwards.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from decimal import Decimal, localcontext
from pathlib import Path
import argparse, json
from math import isqrt

BITS = 256
SCALE = 1 << BITS

def ceildiv(a: int, b: int) -> int:
    return -((-a) // b)

@dataclass(frozen=True)
class I:
    lo: int
    hi: int
    def __post_init__(self):
        if self.lo > self.hi: raise ValueError('inverted interval')
    @staticmethod
    def rat(a: int, b: int = 1) -> 'I':
        if b == 0: raise ZeroDivisionError
        if b < 0: a,b=-a,-b
        return I((a*SCALE)//b, ceildiv(a*SCALE,b))
    @staticmethod
    def coerce(x) -> 'I':
        if isinstance(x,I): return x
        if isinstance(x,int): return I.rat(x)
        if isinstance(x,Fraction): return I.rat(x.numerator,x.denominator)
        raise TypeError(type(x))
    def __add__(self,other):
        b=I.coerce(other);return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,other): return self+-I.coerce(other)
    def __rsub__(self,other): return I.coerce(other)+-self
    def __mul__(self,other):
        b=I.coerce(other);c=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
        return I(min(c)//SCALE,ceildiv(max(c),SCALE))
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi: raise ZeroDivisionError('interval contains zero')
        # reciprocal is decreasing on either component of R\{0}
        return I((SCALE*SCALE)//self.hi,ceildiv(SCALE*SCALE,self.lo))
    def __truediv__(self,other): return self*I.coerce(other).inv()
    def __rtruediv__(self,other): return I.coerce(other)*self.inv()
    def __pow__(self,n: int):
        if n<0:return (self.inv())**(-n)
        z=I.rat(1);a=self
        while n:
            if n&1:z=z*a
            a=a*a;n>>=1
        return z
    def sqrt(self):
        if self.lo<0:raise ValueError('sqrt needs nonnegative interval')
        lo=isqrt(self.lo*SCALE);hi=isqrt(self.hi*SCALE)
        if hi*hi<self.hi*SCALE:hi+=1
        return I(lo,hi)
    def inside(self,a: Fraction,b: Fraction) -> bool:
        return self.lo*a.denominator >= a.numerator*SCALE and self.hi*b.denominator <= b.numerator*SCALE
    def display(self,digits: int=30):
        with localcontext() as c:
            c.prec=digits+8
            return [str(Decimal(self.lo)/Decimal(SCALE)),str(Decimal(self.hi)/Decimal(SCALE))]
    def exact(self):
        return {'lo_numerator':str(self.lo),'hi_numerator':str(self.hi),'denominator_power_of_two':BITS,'decimal_display_only':self.display()}

def atan_reciprocal(q: int) -> I:
    ans=I.rat(0);j=0
    while True:
        den=(2*j+1)*q**(2*j+1)
        ans += I.rat(1 if j%2==0 else -1,den)
        j+=1
        next_den=(2*j+1)*q**(2*j+1)
        if next_den > (1 << (BITS+24)):
            tail=I.rat(1,next_den)
            return ans+(I(0,tail.hi) if j%2==0 else I(-tail.hi,0))

def pi_interval() -> I:
    return 16*atan_reciprocal(5)-4*atan_reciprocal(239)

# 3^(2N+1) > 2^(BITS+32) is an exact stopping rule.
LOG_N=1
while 3**(2*LOG_N+1) <= 1 << (BITS+32): LOG_N+=1

def atanh_log_series(t: I) -> I:
    # Called only for an exact t in [0,1/3], enclosed by the interval.
    ans=I.rat(0);power=t;t2=t*t
    for j in range(LOG_N):
        ans += 2*power/(2*j+1);power=power*t2
    # 2 sum_{j=N}inf t^(2j+1)/(2j+1) <= 9/[4(2N+1)3^(2N+1)].
    tail=I.rat(9,4*(2*LOG_N+1)*3**(2*LOG_N+1))
    return ans+I(0,tail.hi)

LOG2=atanh_log_series(I.rat(1,3))

def log_endpoint(u: int) -> I:
    if u<=0:raise ValueError('log needs positive endpoint')
    k=u.bit_length()-1-BITS
    if k>=0:num,den=u,SCALE*(1<<k)
    else:num,den=u*(1<<(-k)),SCALE
    assert den<=num<2*den
    return k*LOG2+atanh_log_series(I.rat(num-den,num+den))

def log(x: I) -> I:
    if x.lo<=0:raise ValueError('log interval not positive')
    a=log_endpoint(x.lo);b=log_endpoint(x.hi)
    return I(a.lo,b.hi)

def determinant(a: list[list[I]]) -> I:
    a=[r[:] for r in a];n=len(a);out=I.rat(1)
    for k in range(n):
        pivot=a[k][k]
        if pivot.lo<=0<=pivot.hi: raise ArithmeticError('uncertified pivot')
        out=out*pivot
        for i in range(k+1,n):
            factor=a[i][k]/pivot
            for j in range(k+1,n): a[i][j]=a[i][j]-factor*a[k][j]
    return out

def probabilities(n: int=6,contrast: Fraction=Fraction(1)) -> list[I]:
    pi=pi_interval();K=[]
    for i in range(n):
        row=[]
        for j in range(n):
            d=i-j
            if d==0:v=I.rat(1,2)
            elif d%2==0:v=I.rat(0)
            else:v=I.rat(1 if d%4==1 else -1,d)/pi
            if d!=0:v=v*contrast
            row.append(v)
        K.append(row)
    return probabilities_from_kernel(K)

def probabilities_from_kernel(K: list[list[I]]) -> list[I]:
    n=len(K)
    P=[]
    for y in range(1<<n):
        A=[r[:] for r in K]
        for i in range(n):A[i][i]-=1-((y>>i)&1)
        p=((-1)**(n-y.bit_count()))*determinant(A)
        assert p.lo>0
        P.append(p)
    assert sum(P,I.rat(0)).lo<=SCALE<=sum(P,I.rat(0)).hi
    return P

def cyclic8_probabilities(contrast: Fraction=Fraction(19,20)) -> list[I]:
    """Rank-four cyclic projection, using only exact square-root enclosures."""
    root2=I.rat(2).sqrt();small=(2-root2).sqrt()/2;large=(2+root2).sqrt()/2
    K=[]
    for i in range(8):
        row=[]
        for j in range(8):
            d=abs(i-j)
            if d==0:v=I.rat(1,2)
            elif d%2==0:v=I.rat(0)
            else:
                den=small if d in (1,7) else large
                v=(1 if d%4==1 else -1)/(8*den)*contrast
            row.append(v)
        K.append(row)
    return probabilities_from_kernel(K)

def pair_terms(P: list[I],n: int,i: int,j: int):
    total=I.rat(0);locals_=[]
    for base in range(1<<n):
        if base&((1<<i)|(1<<j)):continue
        a,b,c,d=[P[z] for z in [base,base|(1<<i),base|(1<<j),base|(1<<i)|(1<<j)]]
        m=a+b+c+d;delta=b*c-a*d
        ell=log(b)+log(c)-log(a)-log(d)
        # G = m*ell - Delta*sum(1/global_cell); local skew is G/m.
        G=m*ell-delta*(1/a+1/b+1/c+1/d)
        total+=2*G
        locals_.append((base,m,G/m))
    return total,locals_

def main(output: str | None=None):
    P=probabilities(6);pair,local=pair_terms(P,6,1,4)
    _,mass,skew=next(z for z in local if z[0]==5)
    assert skew.inside(Fraction(28952216,10**8),Fraction(28952217,10**8))
    assert mass.inside(Fraction(9455357,10**8),Fraction(9455358,10**8))
    assert pair.hi<0
    D=I.rat(0)
    for i in range(6):
        for base in range(64):
            if base&(1<<i):continue
            a,b=P[base],P[base|(1<<i)];m=a+b
            D+=m*m*(1/a+1/b)
    ps=I.rat(0);pairs=[]
    for i in range(6):
        for j in range(i+1,6):
            value,_=pair_terms(P,6,i,j);ps+=value
            assert value.hi<0
            pairs.append({'i':i,'j':j,'Jpp':value.exact()})
    L=(ps-D)/6
    assert L.inside(Fraction(-26511794,10**6),Fraction(-26511793,10**6))
    report={'status':'PASS: exact integer/rational interval decisions','scope':'true sine Toeplitz n=6 at c=1 and 19/20; cyclic rank-four n=8 at c=19/20; no infinite-volume conclusion','bits':BITS,'pi':pi_interval().exact(),'witness':{'pair_zero_based':[1,4],'outside_zeroed_mask':5,'outside_bits_0_2_3_5':[1,1,0,0],'skew':skew.exact(),'certified_skew_decimal_enclosure':['0.28952216','0.28952217'],'outside_mass':mass.exact()},'actual_averaged_same_pair_Jpp':pair.exact(),'all_15_averaged_pairs_negative':True,'L_per_n':L.exact(),'pairs':pairs,'series_terms_log':LOG_N}
    noisy=probabilities(6,Fraction(19,20));noisy_pair,noisy_cells=pair_terms(noisy,6,1,4)
    _,noisy_mass,noisy_skew=next(z for z in noisy_cells if z[0]==5)
    assert noisy_skew.inside(Fraction(12980507,10**8),Fraction(12980508,10**8))
    assert noisy_pair.hi<0
    report['noisy_true_toeplitz_c19_over20']={'n':6,'pair_zero_based':[1,4],'outside_zeroed_mask':5,
        'skew':noisy_skew.exact(),'outside_mass':noisy_mass.exact(),'actual_averaged_pair':noisy_pair.exact(),
        'certified_skew_decimal_enclosure':['0.12980507','0.12980508']}
    cyclic=cyclic8_probabilities();cpair,ccells=pair_terms(cyclic,8,1,6)
    _,cmass,cskew=next(z for z in ccells if z[0]==13)
    assert cskew.inside(Fraction(56496630,10**8),Fraction(56496632,10**8))
    assert cpair.hi<0
    report['actual_cyclic_c19_over20']={'n':8,'rank':4,'pair_zero_based':[1,6],'outside_zeroed_mask':13,
        'outside_bits_0_2_3_4_5_7':[1,1,1,0,0,0],'skew':cskew.exact(),'outside_mass':cmass.exact(),
        'actual_averaged_pair':cpair.exact(),'certified_skew_decimal_enclosure':['0.56496630','0.56496632']}
    if output:Path(output).write_text(json.dumps(report,indent=2),encoding='utf-8')
    print('PASS: local skew > 0; the same actual-weight averaged pair < 0.')
    print('PASS: all 15 averaged pairs < 0 at n=6 only.')
    print('PASS: -26.511794 < L_6/6 < -26.511793.')
    print('PASS: positive actual conditional skew at c=19/20: true Toeplitz n=6 and cyclic n=8.')
    return report

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();main(args.output)
