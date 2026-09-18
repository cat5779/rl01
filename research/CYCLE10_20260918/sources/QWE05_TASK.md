# QWE05 — Create a cross-layer relative-entropy transport bound under exact count weights

Read CONTRACT.md first.

## Fixed true/corrected model for this task

Let n=2k, c=19/20, a in (0,1-c), and a_*=(1-c)/2=1/40.
The cyclic Fourier projection is
P_st=n^{-1} sum_{r=0}^{k-1} exp(2*pi*i*r*(s-t)/n), 0<=s,t<n.
Draw A with Pr(A)=det(P_A), |A|=k. Independently conditional on A,
Pr(Y_i=1|A)=a+c*1_{i in A}. The true output law is DPP(aI+cP).
Let pi_l=Pr(|Y|=l), q_l=Law(Y||Y|=l), and u_l be uniform on l-subsets.
The exact count generating polynomial is
sum_l pi_l(a)t^l=[1-a-c+(a+c)t]^k[1-a+at]^k.
Put f_l=q_l/u_l, m=min(l,n-l), C_l=l(n-l), and xi=a(1-c-a)/c.
In particular xi_*=1/1520, xi_a=(1-c-2a)/c, xi_aa=-2/c.

For 0<l<n let L_l be the Johnson generator with total jump rate one:
(L_l h)(S)=C_l^{-1} sum_{i in S,j notin S}[h(S-i+j)-h(S)].
Its j-th harmonic eigenvalue is -gamma_{j,l}, with
gamma_{j,l}=j(n-j+1)/C_l. Let r_l^max be the density relative to u_l of
the following law: given A, sample a uniform l-subset of A if l<=k,
or a uniform l-superset of A if l>=k, then average over the SAME prior of A.
Equivalently r_l^max(S)=binom(n,l)det(P_S)/binom(k,l) for l<=k.
Use complementation for l>=k.

For m>=2 set d=k-m+1 and
Q_r^(d)(xi)=sum_{s=0}^r [r_falling_s*(r+2d-1)_rising_s /
                         (d_rising_s*s!)] xi^s.
Let v_{l,j} be the orthogonal j-harmonic projection of r_l^max in L2(u_l),
theta_{l,j}=Q_{m-j}^(d)/Q_m^(d),
tau_l=-log(theta_{l,2})/gamma_{2,l},
psi_{l,j}=theta_{l,2}^{gamma_{j,l}/gamma_{2,l}}.
The designated corrected density is g_l=exp(tau_l L_l)r_l^max,
and the corrected full law is p_hat(S)=pi_|S|(a)u_|S|(S)g_|S|(S).
It uses the exact same true counts; do not redesign it in this assignment.
At m<=1 take f_l=g_l=1 and all defect terms zero.

The source establishes the mode representation f_l=sum_j theta_{l,j}v_{l,j}
and g_l=sum_j psi_{l,j}v_{l,j}. Odd modes vanish by Fourier complement symmetry;
the matched modes are 0 and 2. Thus delta_l=f_l-g_l has only even modes j>=4.
All inner products below use u_l. Define
R_l=D(q_l||u_l g_l),
L_n(a)=sum_l pi_l <delta_l,log g_l>,
E_n(a)=H_hat_n(a)-H_n(a)=L_n(a)+sum_l pi_l R_l.
The exact decomposition is
E_n''=L_n''+sum_l pi_l''R_l+
             sum_l pi_l[R_{l,aa}+2(pi_l'/pi_l)R_{l,a}].
Neither E_n nor one of these three terms has a granted global sign.

Source status matters: SA05 is an author manuscript, and its AUDIT is a self
audit. The independent S14 review validates its specified repaired source
calculation and count-transport results; it does not certify all SA05 claims.
Use S14_REPAIR.md and S14_INDEPENDENT_REVIEW.md whenever the original SA05
sections 5.3–5.4 moment calculation is used. The reviewed weighted response
estimate is one-sided, not an absolute O(sqrt(n)) estimate. Any additional
source lemma essential to your new theorem must be checked or kept explicit
as a conditional input. Do not turn this into a complete re-audit of history.

## Single research objective

Pay ONLY W_n^rel=sum_l pi_l''(a_*) R_l(a_*) for the actual true/corrected
conditional laws. Prove W_n^rel>=-r_n with r_n/n->0, or give an actual-model
asymptotic obstruction. This is distinct from L_n'' and from the corrected
entropy-defect W_n currently studied by S43: R_l is the KL between the two
conditional laws, not D(g_l u_l||u_l) or their entropy difference.

## Reviewed count-transport reduction

Set p_0(t)=alpha(1+t^2)+beta*t, alpha=(1-c^2)/4, beta=(1+c^2)/2.
For n=2k, define positive coefficients B_{n,r} by
B_n(t)=2k p_0(t)^(k-1)+k(k-1)(1+t)^2 p_0(t)^(k-2).
Then sum_l pi_l'' h_l=sum_{r=0}^{n-2} B_{n,r}(h_r-2h_{r+1}+h_{r+2})
for every real sequence h. Its total B-mass is n(n-1). Thus a sufficient,
stronger goal is sum_r B_{n,r}(Delta^2 R_r)_-=o(n). You may instead exploit
signed cancellations to prove the weaker requested lower bound directly.

SA05_CROSS_LAYER.md supplies true deletion transport and its mismatch with
the designated corrected semigroup. For m<k, uniform deletion K_m satisfies
K_m q_{m+1}=q_m+eta_m partial_xi q_m,
while on densities D_m g_{m+1}=exp(Delta beta_m Omega_m)g_m,
Omega_m=m(n-m)L_m. The same letter beta in that source is its layer heat time,
not the coefficient beta of p_0 above. Use the exact definitions in the source.
The induced defect has an explicit source that vanishes at degrees 0 and 2.
Deletion density normalization is 1/(n-m); deletion probability normalization
is 1/(m+1). These must not be interchanged. Crossing the central layer requires
its own complement/boundary argument, not a lower-half formula pasted through.

## Tool properties and transfers

Try a modulated KL along a deletion chain, quantitative data processing with a
moving reference, a discrete Stein/Poisson transport, or an entropic profile
estimate on the count's diffusion scale. The tool must constrain the ACTUAL
R_l sequence and keep the heat-time mismatch and signed count acceleration.
Ordinary monotonicity of KL under one common Markov map does not identify two
different layer evolutions. Static chi-square closeness cannot be differentiated.
The supplied S14 repair and review contain useful exact transport identities.

## A proved trap that a new tool must overcome

Nonnegativity, complement symmetry, and R_l=O(1) alone do not imply o(n).
For a generic sequence h_l=H((l-k)/sigma_n),
sigma_n^2=n(1-c^2)/4, the reviewed diffusion-profile calculation gives
n^-1 sum_l pi_l'' h_l -> [4/(1-c^2)] E[H''(Z)], Z~N(0,1),
under its stated smoothness and domination assumptions. H(x)=exp(-x^2/2)
gives a negative nonzero limit. This is an obstruction to a generic rule, not
an actual R_l counterexample. Establish the missing Fourier-specific regularity
or cancellation; assuming it as a new premise is not completion.

A useful partial result proves a new quantitative deletion defect or actual
profile theorem strong enough to reduce the unpaid budget. An O(1) bound on
each R_l or another formal summation-by-parts identity is already available
and by itself is not a new payment. No result here alone settles the other
two bridge terms, the corrected law's total sign, or entropy-rate concavity.
