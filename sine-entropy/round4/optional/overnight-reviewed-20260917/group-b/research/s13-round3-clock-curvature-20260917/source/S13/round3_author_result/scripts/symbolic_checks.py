#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
import sympy as sp

def run(out:Path):
    a,c=sp.symbols('a c', positive=True)
    b=1-c; astar=b/2
    z=1+c/(a*(b-a))
    zp=sp.simplify(sp.diff(z,a).subs(a,astar))
    zpp=sp.factor(sp.diff(z,a,2).subs(a,astar))

    x,Z,L=sp.symbols('x Z L', positive=True)
    F=x*(Z-1)*L**2-(Z+1)*L+(1-x)*(Z-1)
    Lz=sp.simplify(-sp.diff(F,Z)/sp.diff(F,L))
    Zstar=((1+c)/(1-c))**2
    lz_center=sp.factor(Lz.subs({x:sp.Rational(1,2),L:c,Z:Zstar}))
    dlogtheta=sp.factor(2*lz_center/c)
    clock=sp.factor((sp.Rational(1,8))*zpp*dlogtheta)

    k,l,r=sp.symbols('k l r', integer=True, positive=True)
    q=lambda rr: rr*(rr-1)*(2*k-l)*(2*k-l-1)/(k*(k-1)*(2*k-rr)*(2*k-rr-1))
    qdiff=sp.factor(q(r+1)-q(r))

    n,lam,v=sp.symbols('n lam v', positive=True)
    m=l*(1+lam)/2
    ej2=v+m**2
    h=(ej2-m + (l**2-2*l*m+ej2)-l+m)/(k*(k-1))-2*(l*m-ej2)/k**2
    alpha=l*(l-1)/(k*(k-1))
    theta=sp.factor(h/alpha)
    claimed=sp.factor(lam**2+(4*(2*k-1)*v-l*(2*k-l)*(1-lam**2))/(2*k*l*(l-1)))

    data={
      'z_prime_midpoint':str(zp),
      'z_second_midpoint':str(zpp),
      'lambda_z_center':str(lz_center),
      'dlogtheta_limit_center':str(dlogtheta),
      'minus_tau_second_over_n_limit':str(clock),
      'q_r_increment_factor':str(qdiff),
      'theta_variance_identity':bool(sp.simplify(theta-claimed)==0),
      'passes':bool(zp==0 and sp.simplify(zpp-32*c/(1-c)**4)==0 and sp.simplify(clock-2/(1-c**2))==0 and sp.simplify(theta-claimed)==0)
    }
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args();run(args.output)
