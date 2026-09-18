#!/usr/bin/env python3
import sympy as sp

z,t,y=sp.symbols('z t y', positive=True)

def coeff(poly, var, j):
    if j<0: return sp.Integer(0)
    return sp.expand(poly).coeff(var,j)

for k in range(2,8):
    f=(1+t)*(1+z*t)
    base=sp.expand(f**(k-2))
    for m in range(2,k+1):
        Z=sum(sp.binomial(k,j)*sp.binomial(k,m-j)*z**j for j in range(m+1))
        A=sum(sp.binomial(k-2,j)*sp.binomial(k-2,m-2-j)*z**j for j in range(m-1))
        alpha=sp.Rational(m*(m-1),k*(k-1))
        theta=(z-1)**2*A/(alpha*Z)
        a2=coeff(base,t,m-2)
        rhs=(z+1)**2+sp.Rational(2,k-1)*z
        rhs += z*(z+1)*(4+sp.Rational(2,k-1))*coeff(base,t,m-3)/a2
        rhs += z**2*(4+sp.Rational(2,k-1))*coeff(base,t,m-4)/a2
        assert sp.simplify((z-1)**2/theta-rhs)==0,(k,m)

        Zy=sp.expand(sum(sp.binomial(k,j)*sp.binomial(k,m-j)*(1+y)**j for j in range(m+1)))
        Ay=sp.expand(y**2*sum(sp.binomial(k-2,j)*sp.binomial(k-2,m-2-j)*(1+y)**j for j in range(m-1)))
        for r in range(m+1):
            cr=sp.binomial(k,r)*sp.binomial(2*k-r,m-r)
            qr=sp.Rational(r*(r-1)*(2*k-m)*(2*k-m-1), k*(k-1)*(2*k-r)*(2*k-r-1)) if r>=2 else 0
            assert sp.simplify(coeff(Zy,y,r)-cr)==0,(k,m,r,'Z')
            assert sp.simplify(coeff(Ay,y,r)-cr*qr)==0,(k,m,r,'A')
print('all symbolic identities passed')
