#!/usr/bin/env python3
"""Independent chain-rule and full-law KL/cross-entropy interval check."""
from certify_s64 import IV,ZERO,ONE,SCALE,PREC,log_interval,half_sine_kernel
from fractions import Fraction
from pathlib import Path
import json,argparse,time

def children(K):
    q=K[0][0]; r=ONE-q
    assert 0<q.lo<=q.hi<SCALE
    if len(K)==1:return q,r,[],[]
    iq=q.reciprocal(); ir=r.reciprocal(); kk=len(K)-1
    A=[[ZERO]*kk for _ in range(kk)]; B=[[ZERO]*kk for _ in range(kk)]
    for i in range(kk):
        for j in range(i,kk):
            v=K[i+1][0]*K[0][j+1]; b=K[i+1][j+1]
            A[i][j]=A[j][i]=b+v*ir
            B[i][j]=B[j][i]=b-v*iq
    return q,r,A,B

def pair(n,u=Fraction(1,50),v=Fraction(1,40),prefix=""):
    # Exact probability chain rule; no atom-log entropy summation.
    Hu=ZERO; Hv=ZERO; Du=ZERO; Xuv=ZERO; massu=ZERO; massv=ZERO; leaves=0
    def visit(Ku,Kv,wu,wv,remaining=""):
        nonlocal Hu,Hv,Du,Xuv,massu,massv,leaves
        if not Ku:
            massu=massu+wu;massv=massv+wv;leaves+=1;return
        qu,ru,Au,Bu=children(Ku);qv,rv,Av,Bv=children(Kv)
        if remaining:
            if remaining[0]=="0":visit(Au,Av,wu*ru,wv*rv,remaining[1:])
            else:visit(Bu,Bv,wu*qu,wv*qv,remaining[1:])
            return
        lqu,lru,lqv,lrv=map(log_interval,(qu,ru,qv,rv))
        bu=-qu*lqu-ru*lru;bv=-qv*lqv-rv*lrv
        cross=-qu*lqv-ru*lrv
        Hu=Hu+wu*bu;Hv=Hv+wv*bv;Xuv=Xuv+wu*cross
        Du=Du+wu*(qu*(lqu-lqv)+ru*(lru-lrv))
        visit(Au,Av,wu*ru,wv*rv);visit(Bu,Bv,wu*qu,wv*qv)
    st=time.monotonic();visit(half_sine_kernel(n,u),half_sine_kernel(n,v),ONE,ONE,prefix)
    assert leaves==2**(n-len(prefix))
    if not prefix:assert massu.lo<=SCALE<=massu.hi and massv.lo<=SCALE<=massv.hi
    values={'H_u':Hu,'H_v':Hv,'D_u_v':Du,'cross_entropy_u_v':Xuv,'acceleration_cost':Xuv-Hv,
            'gap_H_symmetric_chord':Hv-Hu,'KL_minus_cost':Du-(Xuv-Hv)}
    return {'n':n,'prefix':prefix,'u':str(u),'v':str(v),'precision_bits':PREC,'leaves':leaves,
            'values':{k:x.decimal() for k,x in values.items()},
            'raw':{k:x.raw() for k,x in values.items()},'seconds':time.monotonic()-st}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,required=True);ap.add_argument('--output');ap.add_argument('--prefix',default='')
    ar=ap.parse_args();out=pair(ar.n,prefix=ar.prefix);text=json.dumps(out,indent=2)+'\n'
    if ar.output:Path(ar.output).write_text(text)
    print(text)
