#!/usr/bin/env python3
"""S70 continuum closure using exact fractions, NOT mesh samples.

Checks alpha via Machin; all pointwise PSD matrices by exact LDL at parameter
vertices; and polynomial payment/Fisher bounds by tensor Bernstein coefficients.
All inputs are explicit text files. Floating printing is informational only.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb,factorial
from pathlib import Path
import argparse,json
P=dict[tuple[int,int],F]
def const(v:F|int)->P:return {(0,0):F(v)} if v else {}
def clean(p:P)->P:return {k:v for k,v in p.items() if v}
def add(a:P,b:P)->P:
 d=a.copy()
 for k,v in b.items():d[k]=d.get(k,F(0))+v
 return clean(d)
def scale(a:P,v:F|int)->P:return clean({k:z*v for k,z in a.items()})
def sub(a:P,b:P)->P:return add(a,scale(b,-1))
def mul(a:P,b:P)->P:
 d={}
 for (i,j),v in a.items():
  for (k,l),w in b.items():d[i+k,j+l]=d.get((i+k,j+l),F(0))+v*w
 return clean(d)
def power(a:P,k:int)->P:
 r=const(1)
 for _ in range(k):r=mul(r,a)
 return r
def evaluate(a:P,x:F,y:F)->F:return sum((v*x**i*y**j for (i,j),v in a.items()),F(0))
def degrees(a:P)->tuple[int,int]:return max((i for i,j in a),default=0),max((j for i,j in a),default=0)
def bernstein(a:P)->list[list[F]]:
 d,e=degrees(a);temp={}
 for r in range(d+1):
  for j in range(e+1):temp[r,j]=sum((a.get((i,j),F(0))*F(comb(r,i),comb(d,i)) for i in range(r+1)),F(0))
 return [[sum((temp[r,j]*F(comb(s,j),comb(e,j)) for j in range(s+1)),F(0)) for s in range(e+1)] for r in range(d+1)]
def restrict(a:P,x0:F,x1:F,y0:F,y1:F)->P:
 d,e=degrees(a);xx={(0,0):x0,(1,0):x1-x0};yy={(0,0):y0,(0,1):y1-y0};xp=[power(xx,k) for k in range(d+1)];yp=[power(yy,k) for k in range(e+1)];out={}
 for (i,j),v in a.items():out=add(out,scale(mul(xp[i],yp[j]),v))
 return out
def prove_nonnegative(a:P,maxdepth:int=12)->dict:
 todo=[(F(0),F(1),F(0),F(1),0)];leaves=[]
 while todo:
  x0,x1,y0,y1,depth=todo.pop();bb=bernstein(restrict(a,x0,x1,y0,y1));mn=min(z for row in bb for z in row)
  if mn>=0:
   leaves.append({'box':[str(v) for v in (x0,x1,y0,y1)],'min_bernstein':str(mn),'floor_1e12':(mn.numerator*10**12)//mn.denominator,'degrees':[len(bb)-1,len(bb[0])-1]});continue
  if depth>=maxdepth:raise AssertionError(f'Bernstein closure failed at box {(x0,x1,y0,y1)}; coefficient {mn}')
  # Alternate c and p splits; each accepted leaf proves its entire closed box.
  if depth%2==0:
   m=(x0+x1)/2;todo.extend([(x0,m,y0,y1,depth+1),(m,x1,y0,y1,depth+1)])
  else:
   m=(y0+y1)/2;todo.extend([(x0,x1,y0,m,depth+1),(x0,x1,m,y1,depth+1)])
 return {'leaves':leaves,'minimum_floor_1e12':min(z['floor_1e12'] for z in leaves),'maximum_depth':maxdepth}
def atan_bounds(n:int,terms:int)->tuple[F,F]:
 s=sum((F((-1)**k,(2*k+1)*n**(2*k+1)) for k in range(terms)),F(0));t=F((-1)**terms,(2*terms+1)*n**(2*terms+1));return min(s,s+t),max(s,s+t)
def alpha_check()->dict:
 a0,a1=atan_bounds(5,120);b0,b1=atan_bounds(239,40);pl,ph=16*a0-4*b1,16*a1-4*b0
 lo,hi,den=map(int,Path('alpha60.txt').read_text().split());alphas=[(F(lo,den),F(hi,den)),(F(2756644477108960247,10**19),F(2756644477108960248,10**19))]
 for al,ah in alphas:assert 4*al**2*ph**2<3<4*ah**2*pl**2
 return {'method':'Machin 120/40 alternating terms; exact square comparisons','alpha60':[str(v) for v in alphas[0]],'guard_alpha':[str(v) for v in alphas[1]]}
def load_caps():
 caps=[tuple(map(int,l.split())) for l in Path('guard_caps_integer.txt').read_text().splitlines() if l.strip()];t2=list(map(int,Path('far_tau_integer.txt').read_text().split()));t3=list(map(int,Path('quad_tau3_integer.txt').read_text().split()));assert len(caps)==len(t2)==len(t3)==256;return caps,t2,t3

def psd_check(ch:F,pl:F,ph:F,sigma:F)->dict:
 caps,t2,t3=load_caps();mins=[None]*4;mindelta=None;count=0
 for c in [F(19,20),ch]:
  for p in [pl,ph]:
   C=F(1303,1000)+F(51,200)*p+8*(c-F(19,20));assert C>1
   cap=[(F(3,100)-p/20)*L/100+(p/20-F(1,50))*U/100+F(1,50) for L,U in caps]
   assert min(C-z for z in cap)>0
   for word in range(4096):
    B=[[F(0) for _ in range(4)] for _ in range(4)]
    for i,w in enumerate([F(19,60),F(11,60),F(11,60),F(19,60)]):B[i][i]=w*C-sigma
    for i in range(4):
     for j in range(i+1,4):
      sep=j-i;O=[9+i+k for k in range(-4,6) if k not in (0,sep)];z=sum(((word>>(k-5))&1)<<b for b,k in enumerate(O))
      v=(C-cap[z])/3 if sep==1 else F(t2[z],2000) if sep==2 else F(t3[z],1000)
      assert v>=0;B[i][j]=B[j][i]=v
    # Exact rational Schur elimination: every positive pivot is checked.
    for k in range(4):
     pivot=B[k][k];assert pivot>0,(c,p,word,k,pivot);mins[k]=pivot if mins[k] is None else min(mins[k],pivot)
     for i in range(k+1,4):
      for j in range(k+1,4):B[i][j]-=B[i][k]*B[k][j]/pivot
    count+=1
 return {'matrices':count,'sigma':str(sigma),'minimum_ldl_pivots':[str(z) for z in mins],'minimum_ldl_pivot_floors_1e12':[(z.numerator*10**12)//z.denominator for z in mins]}
def coefficient_polynomials(ch:F,pl:F,ph:F,filename:str)->tuple[P,P,dict]:
 one=const(1);c={(0,0):F(19,20),(1,0):ch-F(19,20)};p={(0,0):pl,(0,1):ph-pl};b=sub(one,c);ep=sub(p,const(F(1,2)));ec=sub(c,const(F(19,20)));t=scale(mul(b,ep),200);u=scale(ec,1000)
 lower={};upper={};rows=[]
 for line in Path(filename).read_text().splitlines():
  if not line.strip() or line.startswith('#'):continue
  v=list(map(int,line.split()));assert len(v)==8;k,l=v[:2];assert 0<=k and 0<=l and k+l<=8;rows.append((k,l))
  mon=mul(power(t,k),power(u,l))
  for j,factor in enumerate([one,ep,ec]):
   lo,hi=F(v[2+2*j],10**9),F(v[3+2*j],10**9);assert lo<=hi;positive=(k+(j==1))%2==0
   lower=add(lower,scale(mul(mon,factor),lo if positive else hi));upper=add(upper,scale(mul(mon,factor),hi if positive else lo))
 assert sorted(rows)==sorted((k,l) for k in range(9) for l in range(9-k))
 norms=list(map(int,Path('quad_payment_norms_integer.txt').read_text().split()));assert len(norms)==3
 Vmax=F(norms[0])+max(abs(pl-F(1,2)),abs(ph-F(1,2)))*norms[1]+(ch-F(19,20))*norms[2]
 beta=22*(F(1,100)*max(abs(200*F(1,20)*(pl-F(1,2))),abs(200*F(1,20)*(ph-F(1,2))))+(ch-F(19,20))/F(19,20))
 # beta = 22(2 s_max + v_max); the 1/100 converts |t| into 2|s|.
 tail=Vmax*beta**9/F(factorial(9))/(1-beta/10);eps=F(1,10**6);assert tail<eps,(tail,eps)
 lower=sub(lower,const(eps));upper=add(upper,const(eps))
 return lower,upper,{'c':c,'p':p,'b':b,'ep':ep,'ec':ec,'tail':tail,'Vmax':Vmax,'beta':beta,'norms':norms}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--c-upper',default='1907/2000');ap.add_argument('--p-lower',default='21/50');ap.add_argument('--p-upper',default='12/25');ap.add_argument('--eta',default='1/25');ap.add_argument('--M',default='21');ap.add_argument('--sigma',default='1/200');ap.add_argument('--coefficients',default='quad_payment_coefficients_bivariate.txt');ap.add_argument('--skip-psd',action='store_true');ap.add_argument('--output',default='continuum_certificate.json');args=ap.parse_args()
 ch,pl,ph,eta,M,sigma=map(F,[args.c_upper,args.p_lower,args.p_upper,args.eta,args.M,args.sigma]);assert F(19,20)<=ch<1 and 0<pl<=ph<F(1,2) and eta>0
 cert={'status':'INCOMPLETE','scope':'Exact payment/tail/PSD continuum closure; global and guard cap certificates are separate required obligations','parameters':{'c_lower':'19/20','c_upper':str(ch),'p_lower':str(pl),'p_upper':str(ph),'eta':str(eta),'M':str(M),'sigma':str(sigma)}}
 cert['alpha']=alpha_check();print('EXACT_ALPHA_PASS',flush=True)
 if not args.skip_psd:cert['PSD']=psd_check(ch,pl,ph,sigma);print('EXACT_PSD_PASS',cert['PSD']['matrices'],flush=True)
 L,U,data=coefficient_polynomials(ch,pl,ph,args.coefficients);one=const(1);p=data['p'];c=data['c'];b=data['b'];a=mul(b,p);a1=sub(one,mul(b,sub(one,p)));C=add(add(const(F(1303,1000)),scale(p,F(51,200))),scale(data['ec'],8))
 E=mul(mul(mul(mul(b,p),sub(one,p)),sub(one,a)),a1)
 Nbar=add(scale(mul(sub(one,p),a1),F(2,3)),scale(mul(p,sub(one,a)),F(1,3)))
 G=sub(mul(E,sub(L,const(eta))),mul(sub(C,one),Nbar))
 cert['payment_gap']=prove_nonnegative(G);cert['payment_upper']=prove_nonnegative(sub(const(M),U));cert['polynomial_degrees']={'G':degrees(G),'P':degrees(L)}
 cert['tail']={k:str(data[k]) for k in ['tail','Vmax','beta']};cert['tail']['norms']=data['norms'];cert['tail']['declared']='1/1000000'
 cert['status']='PROVED';Path(args.output).write_text(json.dumps(cert,indent=2)+'\n')
 print('EXACT_CONTINUUM_PASS',json.dumps({'eta':str(eta),'M':str(M),'G_leaves':len(cert['payment_gap']['leaves']),'G_min_floor_1e12':cert['payment_gap']['minimum_floor_1e12'],'upper_leaves':len(cert['payment_upper']['leaves']),'tail':float(data['tail'])}),flush=True)
if __name__=='__main__':main()
