#!/usr/bin/env python3
"""Reproduce all finite-chord sign certificates using exact integer intervals.
Default: verify arithmetic deductions from the retained raw interval outputs.
--recompute: also regenerate every entropy enclosure from all binary words.
The logarithms, pi, determinants, and interval endpoints never use floats.
"""
from pathlib import Path
from fractions import Fraction
import argparse,json
from certify_s64 import IV,SCALE,entropy_interval
ROOT=Path(__file__).resolve().parent
CASES=[('002',Fraction(1,50),(1,2,4,8,16)),
       ('0025',Fraction(1,40),(1,2,4,8,16)),
       ('00205',Fraction(41,2000),(2,4,8,16)),
       ('0021',Fraction(21,1000),(2,4,8,16))]

def read_h(n,suffix):
    out=json.loads((ROOT/f'cert_n{n}_a{suffix}.json').read_text())
    assert out['n']==n and out['leaves']==2**n and out['precision_bits']==256
    a,b=map(int,out['mass_raw']);assert a<=SCALE<=b
    return IV(*map(int,out['H_raw']))

def certify(recompute=False):
    if recompute:
        for suffix,a,ns in CASES:
            for n in ns:
                old=read_h(n,suffix);out=entropy_interval(n,a)
                new=IV(*map(int,out['H_raw']))
                assert max(old.lo,new.lo)<=min(old.hi,new.hi)
                (ROOT/f'cert_n{n}_a{suffix}.json').write_text(json.dumps(out,indent=2)+'\n')
    # Complement/gauge identity proves H(.03)=H(.02); it is not an assumption.
    g={n:read_h(n,'0025')-read_h(n,'002') for n in (1,2,4,8,16)}
    p={n:g[2*n]/(2*n)-g[n]/n for n in (1,2,4,8)}
    w={n:p[n]+p[2*n] for n in (1,2,4)}
    assert all(x.lo>0 for x in p.values())
    assert (w[2]-w[1]).lo>0 and (w[4]-w[2]).hi<0
    retained=-sum(p.values(),IV(0));normalized=g[16]/16
    out={'gap_H':{str(n):x.decimal() for n,x in g.items()},
         'favorable_payment_P_L':{str(n):x.decimal() for n,x in p.items()},
         'adjacent_window_W_L':{str(n):x.decimal() for n,x in w.items()},
         'W2_minus_W1':(w[2]-w[1]).decimal(),
         'W4_minus_W2':(w[4]-w[2]).decimal(),
         'retained_sum_L1_2_4_8':retained.decimal(),
         'normalized_gap_H16':normalized.decimal()}
    (ROOT/'finite_chord_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    g2={n:read_h(n,'00205')-(read_h(n,'002')+read_h(n,'0021'))/2 for n in (2,4,8,16)}
    w2={n:g2[4*n]/(4*n)-g2[n]/n for n in (2,4)}
    assert (w2[4]-w2[2]).lo>0
    out2={'gap_H':{str(n):x.decimal() for n,x in g2.items()},
          'W2':w2[2].decimal(),'W4':w2[4].decimal(),
          'W4_minus_W2':(w2[4]-w2[2]).decimal()}
    (ROOT/'second_chord_certificate.json').write_text(json.dumps(out2,indent=2)+'\n')
    # Independent chain-rule entropy computation, already retained, must intersect.
    pair=json.loads((ROOT/'pair_n16.json').read_text())
    for suffix,name in [('002','H_u'),('0025','H_v')]:
        a=read_h(16,suffix);b=IV(*map(int,pair['raw'][name]))
        assert max(a.lo,b.lo)<=min(a.hi,b.hi)
    # New finite-core all-volume KL extrapolation: independently check both methods.
    ds={}
    for n in (15,16):
        chain=json.loads((ROOT/f'pair_n{n}.json').read_text())
        atoms=json.loads((ROOT/f'pair_atoms_n{n}.json').read_text())
        for key in ('H_u','H_v','D_u_v','cross_entropy_u_v','acceleration_cost'):
            a=IV(*map(int,chain['raw'][key]));b=IV(*map(int,atoms['raw'][key]))
            assert max(a.lo,b.lo)<=min(a.hi,b.hi)
        ds[n]=IV(*map(int,atoms['raw']['D_u_v']))
    slope=ds[16]-ds[15];credit=slope-ds[16]/16
    assert credit.lo>0
    cc={'slope_D16_minus_D15':slope.decimal(),'slope_raw':slope.raw(),
        'KL_cross_scale_budget_B16':credit.decimal(),'B16_raw':credit.raw(),
        'gap_H16_over16_plus_B16':(normalized+credit).decimal(),
        'normalized_gap_H16':normalized.decimal()}
    (ROOT/'convex_length_certificate.json').write_text(json.dumps(cc,indent=2)+'\n')
    print('B16 exact interval:',credit.decimal())
    print('PROVED: all retained exact interval deductions and independent-check intersections.')
    print('C0 W4-W2:',out['W4_minus_W2'])
    print('C1 W4-W2:',out2['W4_minus_W2'])
    print('C0 Gap H16 /16:',out['normalized_gap_H16'])

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--recompute',action='store_true')
    certify(ap.parse_args().recompute)
