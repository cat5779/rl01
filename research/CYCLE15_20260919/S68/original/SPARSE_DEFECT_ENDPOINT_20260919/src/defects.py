"""Finite actual-output sparse resampling algebra (NumPy).

Configuration y is encoded as an integer, coordinate i is its i-th least
significant bit. Pair ordering throughout is (00,10,01,11). Natural logarithms.
Numerical routines do not decide an infinite-volume sign.
"""
from __future__ import annotations
from itertools import combinations
import math
import numpy as np

Array=np.ndarray

def validate(P: Array) -> tuple[Array,int]:
    P=np.asarray(P,dtype=float)
    if P.ndim!=1 or len(P)<2 or (len(P)&(len(P)-1)):
        raise ValueError('P must have 2^n entries, n>=1')
    if not np.all(np.isfinite(P)) or np.min(P)<0 or abs(float(P.sum())-1)>1e-9:
        raise ValueError('P is not a normalized nonnegative law')
    return P,len(P).bit_length()-1

def reset(P: Array,n: int,i: int,p: float) -> Array:
    if not 0<=p<=1:raise ValueError('p outside [0,1]')
    ids=np.arange(1<<n);lo=ids[(ids&(1<<i))==0];hi=lo|(1<<i)
    m=P[lo]+P[hi];out=np.empty_like(P);out[lo]=(1-p)*m;out[hi]=p*m
    return out

def reset_prime(P: Array,n: int,i: int) -> Array:
    ids=np.arange(1<<n);lo=ids[(ids&(1<<i))==0];hi=lo|(1<<i)
    m=P[lo]+P[hi];out=np.empty_like(P);out[lo]=-m;out[hi]=m
    return out

def reset_set(P: Array,n: int,A: tuple[int,...],p: float) -> Array:
    out=P.copy()
    for i in A:out=reset(out,n,i,p)
    return out

def noise_jet(P: Array,epsilon: float,p: float) -> tuple[Array,Array,Array]:
    P,n=validate(P)
    if not 0<=epsilon<=1:raise ValueError('epsilon outside [0,1]')
    q=P.copy();d=np.zeros_like(P);dd=np.zeros_like(P)
    for i in range(n):
        fq=(1-epsilon)*q+epsilon*reset(q,n,i,p)
        fd=(1-epsilon)*d+epsilon*reset(d,n,i,p)+epsilon*reset_prime(q,n,i)
        fdd=(1-epsilon)*dd+epsilon*reset(dd,n,i,p)+2*epsilon*reset_prime(d,n,i)
        q,d,dd=fq,fd,fdd
    return q,d,dd

def entropy(P: Array) -> float:
    z=P[P>0];return -float(np.dot(z,np.log(z)))

def entropy_pp(jet: tuple[Array,Array,Array]) -> float:
    q,d,dd=jet
    if np.min(q)<=0:raise ValueError('positive output law required')
    return -float(np.dot(dd,np.log(q))+np.dot(d,d/q))

def kl(A: Array,B: Array) -> float:
    support=A>0
    if np.any(B[support]<=0):return math.inf
    return float(np.dot(A[support],np.log(A[support]/B[support])))

def coefficient_jets(P: Array,p: float,degree: int=3) -> list[tuple[Array,Array,Array]]:
    """Ordinary epsilon coefficients and their first two p derivatives.

    Product_i (I+epsilon*(T_i^p-I)) is evaluated without finite differences.
    """
    P,n=validate(P);z=np.zeros_like(P)
    coeff=[(P.copy(),z.copy(),z.copy())]+[(z.copy(),z.copy(),z.copy()) for _ in range(degree)]
    for i in range(n):
        old=coeff;coeff=[tuple(a.copy() for a in row) for row in old]
        for k in range(1,min(i+1,degree)+1):
            out=[]
            for r in range(3):
                prev=old[k-1][r]
                val=old[k][r]+reset(prev,n,i,p)-prev
                if r:val=val+r*reset_prime(old[k-1][r-1],n,i)
                out.append(val)
            coeff[k]=tuple(out)
    return coeff

def conditional_floor(P: Array) -> float:
    P,n=validate(P)
    if np.min(P)<=0:return 0.
    ids=np.arange(1<<n);ans=1.
    for i in range(n):
        lo=ids[(ids&(1<<i))==0];hi=lo|(1<<i);m=P[lo]+P[hi]
        ans=min(ans,float(np.min(P[lo]/m)),float(np.min(P[hi]/m)))
    return ans

def full_support_coefficients(P: Array,p: float) -> dict:
    if not 0<p<1:raise ValueError('p must be strictly interior for KL derivatives')
    P,n=validate(P)
    if np.min(P)<=0:raise ValueError('P0 must have FULL support; do not regularize by clipping')
    singles=[reset(P,n,i,p) for i in range(n)]
    primes=[reset_prime(P,n,i) for i in range(n)]
    ds=[kl(A,P) for A in singles]
    hs=[A-P for A in singles]
    self_chi=[float(np.dot(v,v/P)) for v in hs]
    pairs=[]
    for i,j in combinations(range(n),2):
        A=reset(singles[i],n,j,p)
        Ap=reset(primes[i],n,j,p)+reset_prime(singles[i],n,j)
        App=2*reset_prime(primes[i],n,j)
        Dij=kl(A,P);cross=float(np.dot(hs[i],hs[j]/P))
        second_Dij=float(np.dot(App,np.log(A/P))+np.dot(Ap,Ap/A))
        Jpp=second_Dij-2/(p*(1-p))-2*float(np.dot(primes[i],primes[j]/P))
        pairs.append({'i':i,'j':j,'J':Dij-ds[i]-ds[j]-cross,'Jpp_kl_formula':Jpp})
    B1=sum(ds);B2=sum(x['J'] for x in pairs)-.5*sum(self_chi)
    jets=coefficient_jets(P,p,3);v,vp,_=jets[1];w,wp,wpp=jets[2];t,tp,tpp=jets[3]
    third_pp=-float(np.dot(tpp,np.log(P)))-float(np.sum((v*wpp+2*vp*wp)/P))+float(np.sum(v*vp*vp/(P*P)))
    triple_kl=0.
    for A in combinations(range(n),3):
        val=kl(reset_set(P,n,A,p),P)
        val-=sum(kl(reset_set(P,n,B,p),P) for B in combinations(A,2))
        val+=sum(ds[i] for i in A);triple_kl+=val
    B3=triple_kl-float(np.dot(v,w/P))+float(np.sum(v*v*v/(P*P)))/6
    return {'B1':B1,'B2':B2,'B3':B3,'self_chi_sum':sum(self_chi),'pairs':pairs,'third_entropy_coefficient_pp':third_pp}

def mutual_information(P: Array,epsilon: float,p: float) -> float:
    """Direct actual-output KL mixture; intended only for small n."""
    P,n=validate(P);q,_,_=noise_jet(P,epsilon,p);out=0.
    for mask in range(1<<n):
        A=tuple(i for i in range(n) if (mask>>i)&1);k=len(A)
        weight=epsilon**k*(1-epsilon)**(n-k)
        if weight:out+=weight*kl(reset_set(P,n,A,p),q)
    return out

def table_metrics(P: Array,details: bool=True) -> dict:
    P,n=validate(P)
    if np.min(P)<=0:raise ValueError('full support required; zero cells are not clipped')
    ids=np.arange(1<<n);diag=0.;score=np.zeros_like(P);accel=np.zeros_like(P)
    for i in range(n):
        lo=ids[(ids&(1<<i))==0];hi=lo|(1<<i);a=P[lo];b=P[hi];m=a+b
        diag+=float(np.sum(m*m*(1/a+1/b)));score[lo]-=m;score[hi]+=m
    pair_sum=ell_sum=edge_sum=pos_pay=neg_pay=0.;per_pair=[];profile={d:0. for d in range(1,n)}
    for i,j in combinations(range(n),2):
        base=ids[((ids&(1<<i))==0)&((ids&(1<<j))==0)]
        inds=[base,base|(1<<i),base|(1<<j),base|(1<<i)|(1<<j)]
        cells=np.array([P[v] for v in inds]);m=cells.sum(axis=0);q=cells/m
        a,b,c,d=q;delta=b*c-a*d
        ell=np.log(b)+np.log(c)-np.log(a)-np.log(d)
        edge=delta*(1/a+1/b+1/c+1/d);skew=ell-edge
        Jpp=2*float(np.dot(m,skew));pair_sum+=Jpp
        ell_sum+=2*float(np.dot(m,ell));edge_sum+=2*float(np.dot(m,edge))
        pos_pay+=2*float(np.dot(m,np.maximum(skew,0)));neg_pay+=2*float(np.dot(m,np.minimum(skew,0)))
        profile[j-i]+=Jpp/n
        for t,s in zip(inds,[1,-1,-1,1]):accel[t]+=2*s*m
        if details:per_pair.append({'i':i,'j':j,'Jpp':Jpp,'mean_ell':float(np.dot(m,ell)),'mean_edge':float(np.dot(m,edge))})
    direct=-float(np.dot(accel,np.log(P))+np.dot(score,score/P))
    return {'n':n,'mass':float(P.sum()),'D':diag,'pair_sum':pair_sum,'L':pair_sum-diag,'direct_L':direct,'ell_directed':ell_sum,'edge_directed':edge_sum,'positive_payment':pos_pay,'negative_payment':neg_pay,'distance_profile_per_n':profile,'pairs':per_pair}

def sine_kernel(n: int,rho: float=.5) -> Array:
    if not 0<rho<1:raise ValueError('rho must be strictly interior')
    d=np.arange(n)[:,None]-np.arange(n)[None,:];K=rho*np.sinc(rho*d)
    if rho==.5:K[(d!=0)&(d%2==0)]=0.
    return K

def cyclic_block(period: int,rank: int,block: int | None=None) -> Array:
    if not 0<rank<period:raise ValueError('rank must be interior')
    if block is None:block=period
    if not 1<=block<=period:raise ValueError('invalid block size')
    d=np.arange(block)[:,None]-np.arange(block)[None,:]
    K=np.full((block,block),rank/period,dtype=float);nz=d!=0
    K[nz]=np.sin(np.pi*rank*d[nz]/period)/(period*np.sin(np.pi*d[nz]/period))
    return K

def dpp_probabilities(K: Array,chunk: int=4096) -> Array:
    n=len(K);out=np.empty(1<<n)
    for start in range(0,1<<n,chunk):
        ids=np.arange(start,min(1<<n,start+chunk));bits=(ids[:,None]>>np.arange(n))&1
        mats=np.broadcast_to(K,(len(ids),n,n)).copy();mats[:,np.arange(n),np.arange(n)]-=1-bits
        det=np.linalg.det(mats)*(-1.)**(n-bits.sum(axis=1))
        if np.max(abs(det.imag))>1e-10:raise ArithmeticError('non-real probability')
        out[ids]=det.real
    if np.min(out)<=0:raise ArithmeticError('nonpositive computed atom; use higher precision, never clip')
    validate(out);return out

def projection_probabilities(n: int,k: int) -> Array:
    """All k-subset probabilities of contiguous Fourier projection.
    Zero atoms outside the k-slice are exact, rather than numerical determinants.
    """
    if not 0<k<n:raise ValueError('need 0<k<n')
    P=np.zeros(1<<n)
    for A in combinations(range(n),k):
        logp=-k*math.log(n)
        for i,j in combinations(A,2):logp+=2*math.log(2*math.sin(math.pi*(j-i)/n))
        P[sum(1<<i for i in A)]=math.exp(logp)
    validate(P);return P

def projection_expansion(P: Array,k: int,p: float) -> dict:
    if not 0<p<1:raise ValueError('p must be strictly interior for the singular expansion')
    P,n=validate(P)
    if not 0<k<n:raise ValueError('need 0<k<n')
    counts=np.array([i.bit_count() for i in range(1<<n)])
    S0=counts==k;S1=np.abs(counts-k)==1;S2=np.abs(counts-k)==2
    if np.any(P[~S0]!=0) or np.any(P[S0]<=0):raise ValueError('must have full support on the k-slice only')
    jets=coefficient_jets(P,p,2);v,vp,vpp=jets[1];w,wp,wpp=jets[2]
    B1=-float(np.dot(v[S0],1+np.log(P[S0])))-float(np.dot(v[S1],np.log(v[S1])))
    B2=-float(np.dot(w[S0],1+np.log(P[S0])))-.5*float(np.sum(v[S0]**2/P[S0]))
    B2-=float(np.dot(w[S1],1+np.log(v[S1])))+float(np.dot(w[S2],np.log(w[S2])))
    B2pp=-float(np.dot(wpp[S0],1+np.log(P[S0])))-float(np.sum(vp[S0]**2/P[S0]))
    B2pp-=float(np.sum(wpp[S1]*(1+np.log(v[S1]))+2*wp[S1]*vp[S1]/v[S1]-w[S1]*(vp[S1]/v[S1])**2))
    B2pp-=float(np.sum(wpp[S2]*(1+np.log(w[S2]))+wp[S2]**2/w[S2]))
    return {'A1':float(v[S1].sum()),'A2':float(w[S1].sum()+2*w[S2].sum()),'B1':B1,'B2':B2,'B2pp':B2pp,'r':k*(1-p)+(n-k)*p,'A2_expected':-2*k*(n-k)*p*(1-p),'B1pp':-(n-k)/p-k/(1-p)}

def transfer_bound(K: Array,L: Array,delta: float) -> float:
    """Bound for |L_n(K)/n-L_n(L)/n|, given a proved common spectral gap."""
    if not 0<delta<=.5:raise ValueError('invalid common gap')
    n=len(K);alpha=delta**2
    LD=4/delta+1/delta**2
    LG=2*math.log(1/alpha)+5/alpha+1/(4*alpha**2)
    return (LD+(n-1)*LG)*min(2.,float(np.linalg.norm(K-L,'fro'))/delta)

def explicit_sine_gap(n: int,rho: float) -> float:
    tau=min(rho,1-rho)
    if n==1:return tau
    return (tau/(2*math.e))**(3*(n-1))/(8*math.pi*n**1.5)

def projection_residues(P: Array,k: int,p0: float=.5) -> dict:
    """Actual one-error-output deletion weights; no posterior reweighting.

    The pair residue below is for the natural J_{ij} of the regularized full
    support base (1-eta)P_projection+eta*p0*I, not an undefined KL at eta=0.
    """
    P,n=validate(P)
    if not 0<k<n:raise ValueError('need 0<k<n')
    if not 0<p0<1:raise ValueError('p0 must be interior')
    counts=np.array([y.bit_count() for y in range(1<<n)])
    S0=counts==k
    if np.any(P[~S0]!=0) or np.any(P[S0]<=0):raise ValueError('full k-slice support required')
    plus=minus=0.
    for y in range(1<<n):
        if counts[y]==k+1:
            parent=np.array([P[y^(1<<i)] for i in range(n) if (y>>i)&1]);a=float(parent.sum())
            plus+=float(np.dot(parent,parent))/a
        if counts[y]==k-1:
            parent=np.array([P[y^(1<<i)] for i in range(n) if not((y>>i)&1)]);a=float(parent.sum())
            minus+=float(np.dot(parent,parent))/a
    g=n-k
    D=plus/p0+minus/(1-p0)
    A=(g-plus)/p0+(k-minus)/(1-p0)
    return {'alpha_plus':plus,'alpha_minus':minus,'diagonal_residue':D,'negative_pair_residue':A,'negative_total_residue':g/p0+k/(1-p0),'log_pair_coefficient':4*k*g,'constant_diagonal_projection_lower_bound':k*g/(n*p0*(1-p0))}

def insertion_entropy_shape(P: Array,k: int) -> dict:
    """Reverse entropies of actual uniform vacant/occupied-site changes.

    No uniform averaging over output configurations is used. The one- and
    two-insertion output weights are respectively A/(n-k), C/binom(n-k,2).
    """
    P,n=validate(P)
    if not 0<k<n:raise ValueError('need 0<k<n')
    ids=np.arange(1<<n);counts=np.array([y.bit_count() for y in ids])
    if np.any(P[counts!=k]!=0) or np.any(P[counts==k]<=0):
        raise ValueError('full support on exactly the k-slice required')
    g=n-k;d=g-k;H=entropy(P)
    def add(U):
        out=np.zeros_like(U)
        for i in range(n):
            lo=ids[(ids&(1<<i))==0];hi=lo|(1<<i);out[hi]+=U[lo]
        return out
    def remove(U):
        out=np.zeros_like(U)
        for i in range(n):
            lo=ids[(ids&(1<<i))==0];hi=lo|(1<<i);out[lo]+=U[hi]
        return out
    A=add(P);B=remove(P);C=add(A)/2;D=remove(B)/2
    hp=H+math.log(g)-entropy(A/g)
    hm=H+math.log(k)-entropy(B/k)
    hpp=H+math.log(math.comb(g,2))-entropy(C/math.comb(g,2)) if g>=2 else 0.
    hmm=H+math.log(math.comb(k,2))-entropy(D/math.comb(k,2)) if k>=2 else 0.
    # Incoming swap mass at every original k-configuration.
    incoming=remove(A)-(n-k)*P
    support=P>0
    swap_energy=-float(np.dot(incoming[support]-k*g*P[support],np.log(P[support])))
    shape=-2*swap_energy+2*g*(d-1)*hp-2*k*(d+1)*hm-g*(g-1)*hpp-k*(k-1)*hmm
    return {'H':H,'h_plus':hp,'h_minus':hm,'h_plus_plus':hpp,'h_minus_minus':hmm,
            'swap_energy':swap_energy,'shape_constant':shape,
            'cyclic_swap_formula':2*k*g*math.log(n)-2*(n-1)*H}

def diagonal_projection_finite_part(P: Array,k: int,p0: float=.5) -> dict:
    """Constant term of D_n(mu_eta) after its explicit 1/eta pole."""
    P,n=validate(P);r=projection_residues(P,k,p0);ids=np.arange(1<<n)
    def add(U):
        out=np.zeros_like(U)
        for i in range(n):
            lo=ids[(ids&(1<<i))==0];hi=lo|(1<<i);out[hi]+=U[lo]
        return out
    def remove(U):
        out=np.zeros_like(U)
        for i in range(n):
            lo=ids[(ids&(1<<i))==0];hi=lo|(1<<i);out[lo]+=U[hi]
        return out
    plus=add(P);minus=remove(P);twoplus=add(plus)/2;twominus=remove(minus)/2
    gp=gm=0.
    for i in range(n):
        lo=ids[(ids&(1<<i))==0];hi=lo|(1<<i)
        ok=twoplus[hi]>0;gp+=float(np.sum(plus[lo[ok]]**2/twoplus[hi[ok]]))
        ok=twominus[lo]>0;gm+=float(np.sum(minus[hi[ok]]**2/twominus[lo[ok]]))
    rate=k*(1-p0)+(n-k)*p0
    constant=3*n-rate*r['diagonal_residue']-r['alpha_plus']-r['alpha_minus']+gp+gm
    return {'gamma_plus_plus':gp,'gamma_minus_minus':gm,'diagonal_finite_part':constant,
            'pair_finite_part':constant+projection_expansion(P,k,p0)['B2pp']}
