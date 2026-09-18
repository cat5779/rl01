"""Stress tests of the new analytic lemmas, not an asymptotic proof.
Run beside qwe05_verify.py. Only actual given-input radial kernels are used here;
these are not substituted for the complete Fourier output KL.
"""
from __future__ import annotations
import csv, json, math
from pathlib import Path
import numpy as np
from scipy.special import gammaln, logsumexp
from qwe05_verify import XI, clock, radial_log_heat

D0=1000/261; B0=13/7

def true_radial(n:int,m:int,xi:float):
    k=n//2;r=np.arange(m+1,dtype=float)
    lc=lambda x,y: gammaln(x+1)-gammaln(y+1)-gammaln(x-y+1)
    logs=lc(k,r)+lc(k,m-r)-r*math.log((1+xi)/xi)
    logs-=logsumexp(logs);w=np.exp(logs)
    y=float(w@r);X=y-r;v=float(w@(X*X))
    mu3=float(w@(X**3));mu4=float(w@(X**4))
    return logs,w,r,y,X,v,mu3,mu4

def main():
    out=Path(__file__).resolve().parent
    rows=[];anchors=[];interp=[]
    for n in (40,64,128,512,2048,4096):
        k=n//2
        ms=sorted(set([4, min(8,k),max(4,k-int(math.sqrt(n))),k-1,k]))
        for m in ms:
            d=k-m+1;C=m*(n-m);xi0=n**-2
            for xi in np.geomspace(xi0,XI,9):
                logs,w,r,y,X,v,mu3,mu4=true_radial(n,m,float(xi))
                cm=clock(n,m,float(xi));A=xi*(1+xi);mu=m-y;u=2*mu-m
                b=-(mu4-v*v+u*mu3)/(mu3+u*v)
                bd=2*mu-m-k-n*xi+C/cm['tau_xi']
                kappa=cm['tau_xi']/(A*C)
                src=-kappa*(X*X-v+b*X)
                K=D0*(m/((n-1)*A)+B0*B0/(4*(n-1)*A**1.5))
                H=u*u/4+v-C/(4*(n-1))
                rows.append(dict(n=n,m=m,xi=float(xi),b=b,b_direct=bd,
                    b_discrepancy=abs(b-bd),source_peak=float(max(src)),source_bound=float(K),
                    source_ratio=float(max(src)/K),y_over_m=y/m,
                    H_ratio=H/((261/1600)*m*m),
                    lower_clock_ratio=cm['tau_xi']/(C/((n-1)*(1+xi))),
                    upper_clock_ratio=cm['tau_xi']/(C/((n-1)*xi)),
                    moment_error=y*y+(k-m+n*xi)*y+v-m*k*xi))
            l0,w0,*_=true_radial(n,m,xi0)
            c0=clock(n,m,xi0);lh0=radial_log_heat(n,m,c0['tau'])
            anchors.append(dict(n=n,m=m,max_log_ratio=float(max(l0-lh0)),
                    anchor_bound=math.log(9)+.25,heat_mass=float(np.exp(logsumexp(lh0))),
                    tau0=c0['tau']))
            if m==k:
                continue
            logs,w,r,y,X,v,mu3,mu4=true_radial(n,m,XI)
            cm=clock(n,m);tau=cm['tau'];A=XI*(1+XI);gamma=cm['gamma']
            tm=1/(k-m+y+XI*(n-m));eta=A*tm
            xx=eta*gamma*cm['tau_xi'];h=-math.log1p(-xx)/gamma
            lg=radial_log_heat(n,m,tau);lg1=radial_log_heat(n,m,tau+h)
            # Forward probability generator applied to the radial heat law.
            j=m-r;up=j*(k-m+j)/C;down=(m-j)*(k-j)/C
            score=-(up+down)
            score[1:]+=up[:-1]*np.exp(lg[:-1]-lg[1:])
            score[:-1]+=down[1:]*np.exp(lg[1:]-lg[:-1])
            R=float(w@(logs-lg))
            Rxi=float((w*(-X/A))@(logs-lg)-w@(cm['tau_xi']*score))
            factor=1-tm*X
            if np.min(factor)<=0: raise ArithmeticError('True deletion not positive')
            w1=w*factor;l1=logs+np.log(factor)
            J=float(w1@(l1-lg1)-R-eta*Rxi)
            logM=math.log(9)+.25+D0*B0*B0+2*D0*math.log(n)
            uu=1+math.log(2*(1+1/XI))+h+logM
            aa=32*(uu/tau+uu*uu/(tau*tau));ss=xx/(gamma*(1-xx))
            bound=2*tm*tm*v+ss*ss/2*(3*aa+gamma*math.sqrt(aa))
            interp.append(dict(n=n,m=m,radial_J=J,bound=bound,ratio=J/bound,
                  x=xx,heat_mass=float(np.exp(logsumexp(lg))),true_deleted_mass=float(w1.sum())))
    for name,data in [('analytic_source_checks',rows),('anchor_checks',anchors),('interpolation_checks',interp)]:
        with (out/(name+'.csv')).open('w',newline='') as fh:
            writer=csv.DictWriter(fh,fieldnames=data[0].keys());writer.writeheader();writer.writerows(data)
    summary=dict(source_cases=len(rows),anchor_cases=len(anchors),interpolation_cases=len(interp),
       max_abs_b=max(abs(z['b']) for z in rows),b_bound=B0,
       max_b_identity_discrepancy=max(z['b_discrepancy'] for z in rows),
       max_source_ratio=max(z['source_ratio'] for z in rows),
       min_H_ratio=min(z['H_ratio'] for z in rows),
       max_y_over_m=max(z['y_over_m'] for z in rows),
       min_lower_clock_ratio=min(z['lower_clock_ratio'] for z in rows),
       max_upper_clock_ratio=max(z['upper_clock_ratio'] for z in rows),
       max_abs_moment_error=max(abs(z['moment_error']) for z in rows),
       max_anchor_log_ratio=max(z['max_log_ratio'] for z in anchors),anchor_log_bound=math.log(9)+.25,
       max_interpolation_ratio=max(z['ratio'] for z in interp),
       max_heat_mass_error=max(abs(z['heat_mass']-1) for z in anchors+interp))
    (out/'analytic_check_summary.json').write_text(json.dumps(summary,indent=2))
    print(json.dumps(summary,indent=2))
    assert summary['max_abs_b']<=B0+1e-8
    assert summary['max_source_ratio']<=1+1e-8
    assert summary['min_H_ratio']>=1-1e-8
    assert summary['min_lower_clock_ratio']>=1-1e-8
    assert summary['max_upper_clock_ratio']<=1+1e-8
    assert summary['max_anchor_log_ratio']<=summary['anchor_log_bound']+1e-8
    assert summary['max_interpolation_ratio']<=1+1e-8

if __name__=='__main__': main()
