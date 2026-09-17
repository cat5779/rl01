"""Author floating diagnostic, NOT a DPP counterexample or a proof.

The analytic theorem is SPECTRAL_CHANNEL_OBSTRUCTION.md.
"""
import numpy as np, math, json
import datetime as dt
from pathlib import Path
from scipy.special import gammaln, logsumexp

def poly_power(p,r):
 a=np.array([1.])
 for _ in range(r):a=np.convolve(a,p)
 return a

def evaluate(n,c):
 r=n//2;alpha=(1-c)/2;beta=(1+c)/2;v=alpha*beta
 base=np.array([v,1-2*v,v]);pi=poly_power(base,r)
 pp=2*r*np.convolve(poly_power(base,r-1),[1,-2,1])
 if r>1:pp+=r*(r-1)*np.convolve(poly_power(base,r-2),[1,0,-2,0,1])
 k=np.arange(n+1);score=(k-r)/v
 logC=gammaln(n+1)-gammaln(k+1)-gammaln(n-k+1)
 nz=pi>0
 Hsym2=-np.sum(pp[nz]*(np.log(pi[nz])-logC[nz])+pi[nz]*score[nz]**2)
 j=np.arange(r+1);logmultip=2*(gammaln(r+1)-gammaln(j+1)-gammaln(r-j+1))
 logatom=2*j*np.log(beta)+2*(r-j)*np.log(alpha)
 logprobr=logsumexp(logatom+logmultip);w=np.exp(logatom+logmultip-logprobr)
 Hcond=-sum(w*logatom)+logprobr;D=logC[r]-Hcond
 B=2*c/v**2;varj=np.sum(w*(j-sum(w*j))**2)
 D2=B*2*np.log(beta/alpha)*varj
 Hout2=Hsym2-pp[r]*D-pi[r]*D2
 lim=(math.log(2)+alpha*math.log(alpha)+beta*math.log(beta))/(v*math.sqrt(2*math.pi*v))
 return dict(n=n,c=c,Hsym2=float(Hsym2),D=float(D),D2=float(D2),pi_r=float(pi[r]),pi_r_second=float(pp[r]),Hout2=float(Hout2),normalized=float(Hout2/n**1.5),lim=lim)
def main():
 started=dt.datetime.now(dt.timezone.utc).isoformat()
 rows=[evaluate(n,c) for c in [.5,.95] for n in [4,8,16,32,64,128,256,512]]
 result=dict(status='FLOATING_DIAGNOSTIC_NOT_PROOF',started_utc=started,
             ended_utc=dt.datetime.now(dt.timezone.utc).isoformat(),rows=rows)
 Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
 for x in rows:print(x['n'],x['c'],x['Hout2'],x['normalized'],x['lim'])

if __name__=='__main__':main()
