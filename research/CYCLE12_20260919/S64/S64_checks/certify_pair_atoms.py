#!/usr/bin/env python3
"""Independent atom-sum verification of the full-law KL finite core."""
from certify_s64 import IV,ZERO,ONE,SCALE,PREC,log_interval,half_sine_kernel
from certify_pair import children
from fractions import Fraction
from pathlib import Path
import json,argparse,time

def atom_pair(n,u=Fraction(1,50),v=Fraction(1,40)):
    Hu=ZERO;Hv=ZERO;D=ZERO;X=ZERO;total_u=ZERO;total_v=ZERO;leaves=0
    def visit(Ku,Kv,pu,pv):
        nonlocal Hu,Hv,D,X,total_u,total_v,leaves
        if not Ku:
            assert pu.lo>0 and pv.lo>0
            lu=log_interval(pu);lv=log_interval(pv)
            Hu=Hu-pu*lu;Hv=Hv-pv*lv;D=D+pu*(lu-lv);X=X-pu*lv
            total_u=total_u+pu;total_v=total_v+pv;leaves+=1;return
        qu,ru,Au,Bu=children(Ku);qv,rv,Av,Bv=children(Kv)
        visit(Au,Av,pu*ru,pv*rv);visit(Bu,Bv,pu*qu,pv*qv)
    start=time.monotonic();visit(half_sine_kernel(n,u),half_sine_kernel(n,v),ONE,ONE)
    assert leaves==2**n and total_u.lo<=SCALE<=total_u.hi and total_v.lo<=SCALE<=total_v.hi
    vals={'H_u':Hu,'H_v':Hv,'D_u_v':D,'cross_entropy_u_v':X,'acceleration_cost':X-Hv,
          'gap_H_symmetric_chord':Hv-Hu}
    return {'n':n,'u':str(u),'v':str(v),'precision_bits':PREC,'leaves':leaves,
            'method':'all full atoms, not conditional KL chain rule',
            'values':{k:a.decimal() for k,a in vals.items()},'raw':{k:a.raw() for k,a in vals.items()},
            'mass_u_raw':total_u.raw(),'mass_v_raw':total_v.raw(),'seconds':time.monotonic()-start}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--n',required=True,type=int);ap.add_argument('--output')
    ar=ap.parse_args();out=atom_pair(ar.n);s=json.dumps(out,indent=2)+'\n'
    if ar.output:Path(ar.output).write_text(s)
    print(s)
