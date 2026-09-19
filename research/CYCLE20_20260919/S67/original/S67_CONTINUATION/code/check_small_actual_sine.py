#!/usr/bin/env python3
"""High-precision diagnostics on actual sine DPPs; NOT interval certificates.

The proof and its acceptance checks are independent of this optional program.
Every configuration is included for n=2,4,6. No large-volume extrapolation,
endpoint expansion, or entropy-rate conclusion is made from these checks.
"""
from pathlib import Path
from itertools import product
import json, time, datetime


def main():
    output=Path(__file__).resolve().parents[1]/"certificates"/"small_actual_sine_diagnostics.json"
    output.parent.mkdir(parents=True,exist_ok=True)
    start=time.monotonic()
    try:
        import mpmath as mp
    except ImportError:
        result={"status":"SKIPPED","reason":"Optional mpmath dependency unavailable","proof_impact":"NONE"}
        output.write_text(json.dumps(result,indent=2)+"\n")
        print(json.dumps(result,indent=2)); return
    mp.mp.dps=60
    tol=mp.mpf("1e-42")
    c,b=mp.mpf(19)/20,mp.mpf(1)/40
    Mb=mp.mpf(761)/39
    def flips(x,*sites):
        x=list(x)
        for i in sites: x[i]=1-x[i]
        return tuple(x)
    def kernel(n,a):
        Q=mp.matrix(n)
        for i in range(n):
            for j in range(n):
                Q[i,j]=mp.mpf(1)/2 if i==j else mp.sin(mp.pi*(i-j)/2)/(mp.pi*(i-j))
        return a*mp.eye(n)+c*Q,Q
    def law(K):
        n=K.rows; probs={}
        for x in product((0,1),repeat=n):
            A=K.copy()
            for i in range(n): A[i,i]-=1-x[i]
            probs[x]=(-1)**(n-sum(x))*mp.det(A)
            assert probs[x]>0
        assert abs(sum(probs.values())-1)<tol
        return probs
    def Bmat(K,x):
        A=K.copy()
        for i,bit in enumerate(x): A[i,i]-=1-bit
        return A**-1
    def pair_J(P,x,i,j):
        return (2*x[i]-1)*(2*x[j]-1)*(mp.log(P[flips(x,i)])+mp.log(P[flips(x,j)])-mp.log(P[x])-mp.log(P[flips(x,i,j)]))
    def Fsum(P,x):
        return sum((pair_J(P,x,i,j) for i in range(len(x)) for j in range(i+1,len(x))),mp.mpf(0))
    records=[]
    for n in (2,4,6):
        Kb,Q=kernel(n,b); Pb=law(Kb)
        E=Q-Q*Q
        chord_probs={}
        for astr in (".02",".025",".03"):
            a=mp.mpf(astr); d=a-b
            z=mp.sqrt((a*(a+c))/((1-a)*(1-a-c)))
            R2=(1-d*d/(1-b)**2)/(1-d*d/b**2)
            R=mp.sqrt(R2)
            u=z/(39+z); v=39*z/(1+39*z); m=u+v
            sp,sm=u*v,(1-u)*(1-v)
            Ka,_=kernel(n,a); Pa=law(Ka); chord_probs[astr]=Pa
            Kh=u*mp.eye(n)+(v-u)*Q; Ph=law(Kh)
            Kt=z*Kb*(mp.eye(n)+(z-1)*Kb)**-1; Pt=law(Kt)
            max_gauge_error=mp.mpf(0)
            max_matrix_error=mp.mpf(0)
            min_weighted_slack=mp.inf
            min_pair_slack=mp.inf
            max_pair_ratio=mp.mpf(0)
            min_pair_ratio=mp.inf
            fish=mp.mpf(0); J_actual=mp.mpf(0)
            for x in Pa:
                max_gauge_error=max(max_gauge_error,abs(Fsum(Pb,x)-Fsum(Pt,x)))
                Ba=Bmat(Ka,x); Bh=Bmat(Kh,x)
                fish+=Pa[x]*sum((Ba[i,i]**2 for i in range(n)),mp.mpf(0))/n
                J_actual+=Pa[x]*Fsum(Pb,x)/n
                weights=[sp if bit else sm for bit in x]
                W=mp.diag(weights); S=mp.diag([2*bit-1 for bit in x])
                left=Bh*W*Bh+(v-u)**2*Bh*E*Bh
                right=(S*Bh+Bh*S)/2+(m-1)*Bh-mp.eye(n)
                max_matrix_error=max(max_matrix_error,max(abs(left[i,j]-right[i,j]) for i in range(n) for j in range(n)))
                off=sum((Bh[i,j]**2 for i in range(n) for j in range(n) if i!=j),mp.mpf(0))
                leakage=(v-u)**2*sum(((Bh*E*Bh)[i,i]/weights[i] for i in range(n)),mp.mpf(0))
                alloc=sum((((m-2*(1-x[i]))*Bh[i,i]-1)/weights[i]-Bh[i,i]**2 for i in range(n)),mp.mpf(0))-leakage
                min_weighted_slack=min(min_weighted_slack,alloc-off)
                for i in range(n):
                    if x[i]==0:
                        odds=Ph[flips(x,i)]/Ph[x]
                        assert odds>=z/Mb-tol and odds<=z*Mb+tol
                    for j in range(i+1,n):
                        if x[i] or x[j]: continue
                        states=(x,flips(x,j),flips(x,i),flips(x,i,j))
                        qa=[Pa[y]/sum(Pa[w] for w in states) for y in states]
                        qh=[Ph[y]/sum(Ph[w] for w in states) for y in states]
                        for aa,hh in zip(qa,qh):
                            ratio=aa/hh
                            min_pair_ratio=min(min_pair_ratio,ratio)
                            max_pair_ratio=max(max_pair_ratio,ratio)
                            assert ratio>=1/R2-tol and ratio<=R2+tol
                        D,C,B,A=qh
                        t=B*C-A*D
                        J=mp.log(B*C/(A*D))
                        Wpair=t*sum(1/q for q in qh)
                        min_pair_slack=min(min_pair_slack,mp.mpf(3)/2*Wpair-J)
            assert max_gauge_error<tol
            assert max_matrix_error<tol
            assert min_weighted_slack>=-tol
            assert min_pair_slack>=-tol
            if n>=3:
                assert fish >= mp.mpf(63)/10-mp.mpf(23)/(5*n)-tol
            records.append({
                "n":n,"a":astr,"all_configurations_included":2**n,
                "gauge_J_sum_max_abs_error":str(max_gauge_error),
                "weighted_matrix_identity_max_abs_error":str(max_matrix_error),
                "weighted_allocation_min_slack":str(min_weighted_slack),
                "odds_width_pair_min_slack":str(min_pair_slack),
                "conditional_pair_ratio_min":str(min_pair_ratio),
                "conditional_pair_ratio_max":str(max_pair_ratio),
                "allowed_conditional_pair_ratio_interval":[str(1/R2),str(R2)],
                "actual_diagonal_Fisher_per_site":str(fish),
                "actual_expectation_reference_J_sum_per_site":str(J_actual)
            })
        Cn=sum((Pb[x]*mp.log(Pb[x])-(chord_probs[".02"][x]+chord_probs[".03"][x])*mp.log(Pb[x])/2 for x in Pb),mp.mpf(0))
        records.append({"n":n,"finite_C_n_over_n":str(Cn/n),"status":"FINITE-VOLUME DIAGNOSTIC ONLY"})
    result={"status":"PASS_DIAGNOSTIC_NOT_CERTIFICATE","precision_decimal_digits":mp.mp.dps,
            "records":records,"wall_seconds":time.monotonic()-start,
            "completed_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "entropy_rate_claim":"NONE","n15_n16_original_verifier":"NOT RERUN"}
    output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))

if __name__=="__main__": main()
