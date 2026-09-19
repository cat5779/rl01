#!/usr/bin/env python3
"""Directed fixed-point interval certificate; Python integers only.
Certifies a mixed diagonal MI Hessian entry at an actual sine kernel.
It does NOT disprove common-identity-direction convexity.
"""
from dataclasses import dataclass
from fractions import Fraction
import json

DIGITS=65
SCALE=10**DIGITS

def ceildiv(a,b):
    assert b>0
    return -((-a)//b)

@dataclass(frozen=True)
class IV:
    lo:int
    hi:int
    def __post_init__(self):
        assert self.lo<=self.hi
    @staticmethod
    def q(a,b=1):
        assert b>0
        return IV(a*SCALE//b,ceildiv(a*SCALE,b))
    @staticmethod
    def co(x):
        return x if isinstance(x,IV) else IV.q(x)
    def __add__(self,other):
        o=IV.co(other);return IV(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return IV(-self.hi,-self.lo)
    def __sub__(self,o):return self+-IV.co(o)
    def __rsub__(self,o):return IV.co(o)+-self
    def __mul__(self,other):
        o=IV.co(other)
        vals=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return IV(min(vals)//SCALE,ceildiv(max(vals),SCALE))
    __rmul__=__mul__
    def inv(self):
        assert self.lo>0 or self.hi<0
        if self.hi<0:return -(-self).inv()
        return IV(SCALE*SCALE//self.hi,ceildiv(SCALE*SCALE,self.lo))
    def __truediv__(self,o):return self*IV.co(o).inv()
    def __rtruediv__(self,o):return IV.co(o)*self.inv()
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        z=IV.q(1);x=self
        while n:
            if n&1:z=z*x
            x=x*x;n//=2
        return z
    def contains(self,x):
        q=IV.co(x);return self.lo<=q.lo and self.hi>=q.hi
    def decimals(self,places=22):
        def fmt(k):
            sign='-' if k<0 else '';k=abs(k)
            return sign+str(k//(10**places))+'.'+str(k%(10**places)).zfill(places)
        f=10**(DIGITS-places)
        return [fmt(self.lo//f),fmt(ceildiv(self.hi,f))]

def arctan_inv(q,n=90):
    x=IV.q(1,q);x2=x*x;power=x;z=IV.q(0)
    for k in range(n):
        term=power/(2*k+1)
        z=z+term if k%2==0 else z-term
        power=power*x2
    rem=power/(2*n+1)
    # alternating series remainder has sign (-1)^n and magnitude <= next term
    return IV(z.lo-rem.hi if n%2 else z.lo,
              z.hi if n%2 else z.hi+rem.hi)

PI=16*arctan_inv(5)-4*arctan_inv(239)

def log_atanh_unit(x,n=85):
    # 1 <= x <= 2, with interval widths allowed at endpoints
    z=(x-1)/(x+1);assert z.lo>=0 and z.hi<SCALE
    zz=z*z;power=z;ans=IV.q(0)
    for k in range(n):
        ans+=2*power/(2*k+1)
        power=power*zz
    rem=2*power/((2*n+1)*(1-zz))
    return IV(ans.lo,ans.hi+rem.hi)
LOG2=log_atanh_unit(IV.q(2))

def log_point(k):
    assert k>0
    x=IV(k,k);shift=0
    while x.lo<SCALE:
        x=x*2;shift-=1
    while x.hi>2*SCALE:
        x=x/2;shift+=1
    return log_atanh_unit(x)+shift*LOG2

def log_iv(x):
    assert x.lo>0
    return IV(log_point(x.lo).lo,log_point(x.hi).hi)

def determinant(mat):
    n=len(mat);dp={0:IV.q(1)}
    for mask in range(1,1<<n):
        k=mask.bit_count();ans=IV.q(0);pos=0
        for j in range(n):
            if mask>>j&1:
                term=mat[k-1][j]*dp[mask^(1<<j)]
                ans=ans-term if (k-1+pos)%2 else ans+term
                pos+=1
        dp[mask]=ans
    return dp[(1<<n)-1]

def atoms(n,rect=False):
    beta=IV.q(19,20)/PI
    eps=IV.q(1,10**10)
    ps=[]
    for mask in range(1<<n):
        mat=[]
        for i in range(n):
            row=[]
            for j in range(n):
                if i==j:
                    z=IV.q(1,2)-(0 if mask>>i&1 else 1)
                    if rect and i in (0,n-1):z+=IV(0,eps.hi)
                else:
                    r=abs(i-j)
                    z=IV.q(0) if r%2==0 else beta*((-1)**((r-1)//2))/r
                row.append(z)
            mat.append(row)
        p=determinant(mat)*((-1)**(n-mask.bit_count()))
        assert p.lo>0
        ps.append(p)
    assert sum(ps,IV.q(0)).contains(1)
    return ps

def deriv_i(ps,i):
    return [(1 if mask>>i&1 else -1)*(ps[mask&~(1<<i)]+ps[mask|(1<<i)])
            for mask in range(len(ps))]

def deriv_ij(ps,i,j):
    out=[]
    for mask in range(len(ps)):
        base=mask&~((1<<i)|(1<<j))
        m=sum((ps[base|a*(1<<i)|b*(1<<j)] for a in range(2) for b in range(2)),IV.q(0))
        out.append(m*((1 if mask>>i&1 else -1)*(1 if mask>>j&1 else -1)))
    return out

def stats(ps):
    n=(len(ps)-1).bit_length();zero=IV.q(0)
    first=[zero for _ in ps];second=[zero for _ in ps]
    for i in range(n):
        di=deriv_i(ps,i)
        first=[x+y for x,y in zip(first,di)]
        for j in range(i):
            dij=deriv_ij(ps,i,j)
            second=[x+2*y for x,y in zip(second,dij)]
    fisher=sum((v*v/p for p,v in zip(ps,first)),zero)
    acc=sum((v*log_iv(p) for p,v in zip(ps,second)),zero)
    return fisher,acc,fisher+acc

def mixed(ps,i,j):
    di=deriv_i(ps,i);dj=deriv_i(ps,j);dij=deriv_ij(ps,i,j)
    return sum((u*v/p+w*log_iv(p) for p,u,v,w in zip(ps,di,dj,dij)),IV.q(0))

def main():
    ps=atoms(6);p3=atoms(3)
    entry=mixed(ps,0,5)
    assert entry.hi<IV.q(-379,10**6).lo
    assert entry.lo>IV.q(-380,10**6).hi
    rect_entry=mixed(atoms(6,rect=True),0,5)
    assert rect_entry.hi<IV.q(-3,10000).lo
    st6=stats(ps);st3=stats(p3)
    merge=[u-2*v for u,v in zip(st6,st3)]
    assert merge[-1].lo>0
    result={
      'arithmetic':'directed integer fixed-point intervals; 65 decimal places',
      'pi_source':'Machin identity 16 atan(1/5)-4 atan(1/239); alternating-series remainder',
      'pi_interval':PI.decimals(55),
      'kernel':{'N':6,'rho':'1/2','c':'19/20','a':'1/40','partition':[3,3]},
      'mixed_MI_Hessian_1_6':entry.decimals(),
      'same_entry_on_diagonal_rectangle_0_to_1e-10':rect_entry.decimals(),
      'Fisher_defect':merge[0].decimals(),
      'acceleration':merge[1].decimals(),
      'common_identity_MI_curvature':merge[2].decimals(),
      'meaning':'Mixed entry is negative; common identity curvature is positive. No counterexample to all-size M double prime >= 0 is asserted.'
    }
    text=json.dumps(result,indent=2)
    print(text)
    with open('/mnt/data/S74/certificate.json','w') as f:f.write(text+'\n')
if __name__=='__main__':main()
