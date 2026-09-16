#!/usr/bin/env python3
"""Independent exact reconstructions of the R=3 complete atoms and jets.
The polynomial engine uses integer principal minors and a Walsh transform.
This checker reconstructs each entire bivariate determinant by a separate
column-subset Leibniz algorithm, then uses Fraction Gauss--Jordan and
inclusion/Mobius inversion for further value and jet reconstructions.
"""
from __future__ import annotations
import argparse,json,math,random,time
from fractions import Fraction as Q
from pathlib import Path
from atom_polynomials import build,jets_fraction,POSITIONS,DEN,N,b_integer
from dyadic import IV,SCALE

def need(ok,msg):
    if not ok:raise ArithmeticError(msg)

def determinant_inverse(a):
    n=len(a)
    if n==0:return Q(1),[]
    z=[[Q(v)for v in row]+[Q(i==j)for j in range(n)]for i,row in enumerate(a)]
    det=Q(1)
    for k in range(n):
        j=next((j for j in range(k,n)if z[j][k]),None)
        if j is None:return Q(0),None
        if j!=k:z[k],z[j]=z[j],z[k];det=-det
        piv=z[k][k];det*=piv;z[k]=[v/piv for v in z[k]]
        for i in range(n):
            if i==k:continue
            p=z[i][k]
            if p:z[i]=[x-p*y for x,y in zip(z[i],z[k])]
    return det,[row[n:]for row in z]

def mobius_values(K):
    p=[]
    for s in range(1<<N):
        idx=[i for i in range(N)if s>>i&1]
        p.append(determinant_inverse([[K[i][j]for j in idx]for i in idx])[0])
    for i in range(N):
        for s in range(1<<N):
            if not s>>i&1:p[s]-=p[s|(1<<i)]
    return p

def exact_log(q):
    # Independent rational-series enclosure, without using fixed-point ops.
    if q<1:
        l,h=exact_log(1/q);return -h,-l
    k=0
    while q>=2:q/=2;k+=1
    def s(z):
        v=2*sum((z**(2*j+1)/Q(2*j+1)for j in range(48)),Q(0))
        return v,v+2*z**97/(97*(1-z*z))
    l,h=s((q-1)/(q+1));a,b=s(Q(1,3))
    return l+k*a,h+k*b

def arithmetic_checks():
    rng=random.Random(9137);count=0
    for _ in range(80):
        a=Q(rng.randint(-10000,10000),rng.randint(1,701));b=Q(rng.randint(-10000,10000),rng.randint(1,701))
        for v,z in [(a+b,IV.point(a)+b),(a-b,IV.point(a)-b),(a*b,IV.point(a)*b),(a*a,IV.point(a).sq())]:
            need(Q(z.lo,SCALE)<=v<=Q(z.hi,SCALE),'dyadic basic arithmetic');count+=1
        if b:
            z=IV.point(a)/b;need(Q(z.lo,SCALE)<=a/b<=Q(z.hi,SCALE),'dyadic division');count+=1
    for q in [Q(1),Q(2),Q(1,2),Q(199),Q(39),Q(1,10**12),Q(10**12),Q(13,7),Q(117,941)]:
        l,h=exact_log(q);z=IV.point(q).log()
        need(Q(z.lo,SCALE)<=l and Q(z.hi,SCALE)>=h,'independent rational log enclosure');count+=1
    try:IV.bounds(-1,1).inv()
    except ArithmeticError:count+=1
    else:raise ArithmeticError('division across zero did not fail')
    return count

def direct_polynomial(y):
    # Leibniz determinant via column-subset dynamic programming. This does
    # not call principal-minor expansion, Bareiss, or the Walsh transform.
    dp={0:{(0,0):1}}
    for row in range(N):
        nd={}
        for mask,poly in dp.items():
            for col in range(N):
                if mask>>col&1:continue
                sg=(-1)**(row-(mask&((1<<col)-1)).bit_count())
                if row==col:terms=[(0,0,96*(2*((y>>row)&1)-1)),(1,1,192)]
                elif abs(row-col)==1:terms=[(1,0,45)]
                elif abs(row-col)==3:terms=[(1,0,-5)]
                else:continue
                dest=nd.setdefault(mask|(1<<col),{})
                for (k,l),coef in poly.items():
                    for ku,ld,c in terms:
                        key=(k+ku,l+ld);dest[key]=dest.get(key,0)+sg*c*coef
        dp=nd
    sg=(-1)**(N-y.bit_count())
    return {key:sg*v for key,v in dp[(1<<N)-1].items()if v}

def run():
    start=time.time();C=build();B=[[45 if abs(i-j)==1 else -5 if abs(i-j)==3 else 0 for j in range(N)]for i in range(N)];count=arithmetic_checks();nodes=[]
    for y in range(1<<N):
        direct=direct_polynomial(y)
        expected={key:v for key,v in zip(POSITIONS,C[y])if v}
        need(direct==expected,'full bivariate determinant polynomial mismatch');count+=1
    # Coefficientwise normalization and exact output-complement symmetry.
    for j,(k,l)in enumerate(POSITIONS):
        need(sum(row[j]for row in C)==(DEN if (k,l)==(0,0) else 0),'polynomial normalization')
        for s in range(1<<N):need(C[s][j]==(-1)**l*C[s^((1<<N)-1)][j],'complement coefficient identity')
        count+=1+(1<<N)
    for u,d in [(Q(1,4),Q(0)),(Q(3,5),Q(1,10000)),(Q(1),-Q(1,10000))]:
        K=[[Q(i==j,2)+u*(Q(B[i][j],192)+(d if i==j else 0))for j in range(N)]for i in range(N)]
        incl=mobius_values(K);rows=[]
        for y in range(1<<N):
            A=[[K[i][j]-(1-(y>>i&1) if i==j else 0)for j in range(N)]for i in range(N)]
            det,inv=determinant_inverse(A);sign=(-1)**(N-y.bit_count());p=sign*det
            need(p>0 and inv is not None,'positive complete atom')
            tr=sum(inv[i][i]for i in range(N));tr2=sum(inv[i][j]*inv[j][i]for i in range(N)for j in range(N))
            jets=[p,p*u*tr,p*u*u*(tr*tr-tr2)]
            need(jets==jets_fraction(C[y],u,d),'direct signed determinant jet mismatch')
            need(p==incl[y],'inclusion Mobius mismatch')
            rows.append([str(v)for v in jets]);count+=3
        need([sum(Q(r[k])for r in rows)for k in range(3)]==[1,0,0],'normalization of actual jets');count+=1
        # Differentiate d*log(y/x)/2 directly, then compare its exact rational
        # and logarithmic coefficients to the perspective-Hessian formula.
        jr=[[Q(z)for z in row]for row in rows];center=N//2
        for mask in range(1<<N):
            if mask>>center&1:continue
            x,x1,x2=jr[mask];y,y1,y2=jr[mask|(1<<center)]
            d0=y-x;d1=y1-x1;d2=y2-x2
            rat_direct=d1*(y1/y-x1/x)+d0*(y2/y-y1*y1/(y*y)-x2/x+x1*x1/(x*x))/2
            rat_perspective=(x+y)*(x1/x-y1/y)**2/2+((1-y/x)*x2+(1-x/y)*y2)/2
            need(rat_direct==rat_perspective,'complete production Hessian rational part')
            need(d2/2==(y2-x2)/2,'complete production log coefficient');count+=2
        occ=[Q(sum((mask>>i)&1 for i in range(N)if i!=center))for mask in range(1<<N)]
        mean=sum(occ[mask]*jr[mask][0]for mask in range(1<<N))
        var=sum((occ[mask]-mean)**2*jr[mask][0]for mask in range(1<<N))
        need(mean==3+6*u*d and var<=Q(3,2),'exterior count mean/variance');count+=1
        nodes.append({'u':str(u),'delta':str(d),'all_128_atom_jets':rows,'exterior_count_mean':str(mean),'exterior_count_variance':str(var)})
    return {'status':'PASS_EXACT_FULL_ATOMS_AND_JETS','grouped_comparisons':count,'nodes':nodes,
      'elapsed_seconds':time.time()-start,
      'scope':'Independent algorithms within the same author session; not independent mathematical review, all-radius enumeration, or a sine-rate sign certificate.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);a=p.parse_args();r=run()
    if a.output:a.output.write_text(json.dumps(r,indent=2)+'\n')
    print(r['status'],r['grouped_comparisons'],'comparisons;',round(r['elapsed_seconds'],3),'seconds')
