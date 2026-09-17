#!/usr/bin/env python3
"""Exact checks for constants used in PROOF.md; standard library only."""
from fractions import Fraction as F
from datetime import datetime, timezone
from pathlib import Path
import hashlib, json


def require(ok, description):
    if not ok: raise ArithmeticError(description)

def check():
    c=F(19,20);tmax=F(1,200);delta0=F(1,50)
    Dmin=(1+c*c)/4-tmax*tmax
    require(Dmin==F(1189,2500) and Dmin>F(19,40), 'Dmin==F(1189,2500) and Dmin>F(19,40)')
    # ||A_*|| <= |t|+sqrt((1+c^2)/4) < 1, using a rational square comparison.
    require((1+c*c)/4<(1-tmax)**2, '(1+c*c)/4<(1-tmax)**2')
    tail_coefficient=4/(9*F(19,40)**2)
    require(tail_coefficient==F(6400,3249) and tail_coefficient<2, 'tail_coefficient==F(6400,3249) and tail_coefficient<2')
    require(1+2/delta0==101, '1+2/delta0==101')
    inverse_constant=2*(1+2/delta0)
    require(inverse_constant==202, 'inverse_constant==202')
    E_lower=F(1,4)-tmax*tmax
    require(E_lower==F(9999,40000) and E_lower>F(1,5), 'E_lower==F(9999,40000) and E_lower>F(1,5)')
    require(F(1,4)+F(1,15)**2<F(51,100)**2, 'F(1,4)+F(1,15)**2<F(51,100)**2')
    Sstar_bound=((1+c*c)/4)/E_lower*(tmax+F(51,100))
    require(Sstar_bound==F(1959575,1999800) and Sstar_bound<1, 'Sstar_bound==F(1959575,1999800) and Sstar_bound<1')
    zeta_star_bound=F(1,2)*F(1,15)/F(1,5)
    require(zeta_star_bound==F(1,6) and c/2+zeta_star_bound<1, 'zeta_star_bound==F(1,6) and c/2+zeta_star_bound<1')
    L0=2020000;N0=2*L0+4
    require(inverse_constant/L0==F(1,10000), 'inverse_constant/L0==F(1,10000)')
    require(N0==4040004, 'N0==4040004')
    finite_linear_threshold=4*L0+10
    require(finite_linear_threshold==8080010, 'finite_linear_threshold==8080010')
    require(finite_linear_threshold-2*L0-5==F(finite_linear_threshold,2), 'finite_linear_threshold-2*L0-5==F(finite_linear_threshold,2)')
    require(F(3,100)/156==F(1,5200), 'F(3,100)/156==F(1,5200)')
    # Machin branch: all steps in these bounds are rational.
    # arctan(x) lies in [x/(1+x^2),x]. Its stated angle lies in (0,pi/2),
    # using pi>3 and 4/5<3/2 for the upper bound.
    require(4*F(1,5)/(1+F(1,5)**2)-F(1,239)>0, '4*F(1,5)/(1+F(1,5)**2)-F(1,239)>0')
    require(4*F(1,5)<F(3,2), '4*F(1,5)<F(3,2)')
    tan4=F(120,119)
    require((tan4-F(1,239))/(1+tan4*F(1,239))==1, '(tan4-F(1,239))/(1+tan4*F(1,239))==1')
    return {'status':'PASS','arithmetic':'exact fractions','c':str(c),
            'D0_lower':str(Dmin),'tail_coefficient_upper':str(tail_coefficient),
            'reference_inverse_constant':str(inverse_constant),
            'Sstar_norm_upper':str(Sstar_bound),'L0':L0,'cylinder_sites':N0,
            'finite_n_half_linear_threshold':finite_linear_threshold,
            'kappa_exact':f'1/(12*50**{N0})',
            'fisher_refund_fraction_upper':'1/(5200*(R-1))',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'utc':datetime.now(timezone.utc).isoformat()}

if __name__=='__main__':print(json.dumps(check(),indent=2))
