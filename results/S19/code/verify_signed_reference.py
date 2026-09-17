#!/usr/bin/env python3
"""Author supplement: signed lag-1 plus lag-5 compensation near the reference.

This is not a global signed expectation or entropy-rate certificate. It
reuses the delivered rigorous interval primitives and records that dependency.
"""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json
from verify_reference_payment import I,S,pi_enclosure,excess_box


def box(a,pi,lag):
    c=I.of(F(19,20));t=a-F(1,40)
    den=(1+c.square())/4-t.square();qr=1/(lag*pi)
    e=F(1,4)+c.square()*qr.square()-t.square()
    rad=I.hull(-F(1,10000),F(1,10000))
    return (den*(F(1,2)+t)/e+rad,
            1+den*(-F(1,2)+t)/e+rad,(den*c*qr/e).square()+rad)


def check():
    pi=pi_enclosure();rows=[]
    for k in range(200):
        lo=F(1,50)+F(k,20000);hi=lo+F(1,20000);a=I.hull(lo,hi)
        _,g1,_,_,_=excess_box(a,*box(a,pi,1))
        _,g5,_,_,_=excess_box(a,*box(a,pi,5))
        total=g1+g5
        if total.hi>=-5*S:raise ArithmeticError('Signed reference margin unresolved')
        rows.append({'a_lo':str(lo),'a_hi':str(hi),'g1':g1.pack(),
                     'g5':g5.pack(),'sum':total.pack()})
    emin=F(9999,40000)+F(19,20)**2*F(7,22)**2
    star_norm=F(761,1600)/emin*(F(1,200)+F(3,5))
    if not emin>F(1,3) or not star_norm<1:raise ArithmeticError('lag-1 Schur bound')
    if not F(1,4)+F(19,20)**2/F(9)<F(3,5)**2:raise ArithmeticError('square-root upper')
    return {'status':'PASS','classification':'AUTHOR_SCOPED_SIGNED_REFERENCE_ONLY',
            'a_interval':['1/50','3/100'],'radius':'1/10000','cells':200,
            'signed_bound':'g_lag1 + g_lag5 < -5','lag1_E_lower':str(emin),
            'lag1_Sstar_norm_upper':str(star_norm),'rows':rows,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'interval_source_sha256':hashlib.sha256(Path(__file__).with_name('verify_reference_payment.py').read_bytes()).hexdigest(),
            'utc':datetime.now(timezone.utc).isoformat()}


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args();fresh=check();text=json.dumps(fresh,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    else:print(text,end='')
