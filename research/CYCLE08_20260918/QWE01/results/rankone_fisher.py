"""Exploratory test, not a proof certificate."""
import os;os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np
from pathlib import Path
import time,json
rng=np.random.default_rng(510332);root=Path(__file__).parent

def fisher2(K,v):
 n=len(K);ids=np.arange(1<<n);bits=((ids[:,None]>>np.arange(n))&1)
 M=np.broadcast_to(K,(len(ids),n,n)).copy();M[:,np.arange(n),np.arange(n)]-=1-bits
 sg,lp=np.linalg.slogdet(M);p=np.exp(lp);V=np.linalg.inv(M)
 if not np.all(sg*(-1.)**(n-bits.sum(1))>0):raise RuntimeError('atom sign')
 s=np.trace(V,axis1=1,axis2=2);tr2=np.einsum('bij,bji->b',V,V)
 Vv=V@v;u=np.einsum('bi,i->b',Vv,v);z=np.einsum('bi,bi->b',Vv,Vv)
 t=np.einsum('bi,bij,bj->b',Vv,V,Vv)
 terms=(s*s-tr2)*u*u-4*s*u*z+2*z*z+4*u*t
 return p@terms,p@(u*u)

if __name__=='__main__':
 out=[];st=time.monotonic()
 for n in [3,4,6,8,10]:
  for c in [.95,.999]:
   for typ in ['projection','balanced','contraction']:
    best=(np.inf,None)
    for run in range(1000 if n<8 else 200 if n==8 else 50):
     U,_=np.linalg.qr(rng.normal(size=(n,n)))
     if typ=='projection':Q=U[:,:n//2]@U[:,:n//2].T
     elif typ=='balanced':
      B=rng.normal(size=(n,n));B=(B+B.T)/2;np.fill_diagonal(B,0)
      B*=.5*rng.uniform(.5,1)/np.max(abs(np.linalg.eigvalsh(B)));Q=.5*np.eye(n)+B
     else:Q=(U*rng.beta(.2,.2,n))@U.T
     K=(1-c)/2*np.eye(n)+c*Q;v=rng.normal(size=n);v/=np.linalg.norm(v)
     z,f=fisher2(K,v)
     if z<best[0]:best=(z,dict(K=K.tolist(),v=v.tolist(),fisher=f))
    row=dict(n=n,c=c,kind=typ,fisher_second=best[0],witness=best[1],status='FLOAT DIAGNOSTIC')
    out.append(row);print(n,c,typ,best[0],time.monotonic()-st,flush=True)
    (root/'rankone_fisher_diagnostic.json').write_text(json.dumps(out,indent=2))
