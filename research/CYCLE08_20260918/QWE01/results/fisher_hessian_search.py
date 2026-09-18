"""Falsify matrix/entrywise positivity, float only."""
import os;os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json
from pathlib import Path
rng=np.random.default_rng(5472671);root=Path(__file__).parent

def calc(K,v):
 n=len(K);ids=np.arange(1<<n);bits=((ids[:,None]>>np.arange(n))&1)
 M=np.broadcast_to(K,(len(ids),n,n)).copy();M[:,np.arange(n),np.arange(n)]-=1-bits
 sg,lp=np.linalg.slogdet(M);p=np.exp(lp);V=np.linalg.inv(M)
 W=V@v;z=W**2;u=W@v;d=np.diagonal(V,axis1=1,axis2=2)
 T=(u[:,None]*d-2*z)
 mat=T[:,:,None]*T[:,None,:]-2*z[:,:,None]*z[:,None,:]-(u*u)[:,None,None]*V*V+4*u[:,None,None]*W[:,:,None]*V*W[:,None,:]
 return np.einsum('b,bij->ij',p,mat)

if __name__=='__main__':
 out=[]
 for n in [3,4,6,8]:
  minentry=(np.inf,None);mineig=(np.inf,None);minsum=(np.inf,None)
  for t in range(3000):
   U,_=np.linalg.qr(rng.normal(size=(n,n)));vals=rng.uniform(.025,.975,n);K=(U*vals)@U.T
   v=rng.normal(size=n);v/=np.linalg.norm(v);F=calc(K,v)
   off=F.copy();np.fill_diagonal(off,np.inf)
   e=off.min();ev=np.linalg.eigvalsh(F).min();ds=F.sum()-np.trace(F)
   data=dict(K=K.tolist(),v=v.tolist(),F=F.tolist())
   if e<minentry[0]:minentry=(e,data)
   if ev<mineig[0]:mineig=(ev,data)
   if ds<minsum[0]:minsum=(ds,data)
  r=dict(n=n,minentry=minentry,mineig=mineig,minsum=minsum,status='FLOAT DIAGNOSTIC');out.append(r)
  print(n,minentry[0],mineig[0],minsum[0],flush=True)
  (root/'fisher_hessian_diagnostic.json').write_text(json.dumps(out,indent=2))
