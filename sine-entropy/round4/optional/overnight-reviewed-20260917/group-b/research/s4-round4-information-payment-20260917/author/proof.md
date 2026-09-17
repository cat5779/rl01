PROVED_SCOPED_LEMMA

# S4 round 4: completed-information payment by log odds and missing Fisher information

## 0. Result, scope, and unchanged target

This round proves a new bound on the **completed** information-curvature correction in Gaussian localization. It does not attempt to bound that correction by a normalized-posterior first-tangent energy. Instead it combines the true unnormalized-likelihood acceleration with the off-diagonal part of the missing Fisher information before estimating either one. The resulting cost is a diagonally weighted, actually averaged posterior uncertainty.

The bound gives a new strong-concavity region for the true sine entropy rate: fixed densities up to **one percent** or at least ninety-nine percent, contrasts from 37/40 through 959/1000, and the central half of the legal offset interval. The density stays fixed as dimension and rank grow. The full all-density, all-offset target remains unresolved.

The preceding round's delta^-5 MMSE theorem is an **author claim in the preceding conversation**, not an independently reviewed input in the supplied packet. This proof is independent of that theorem and its proof. The reviewed four-site positive-excess result is only a regression gate, not this round's advance. `DELTA_FROM_LAST_ROUND.md` gives the comparison and provenance.

### 0.1 Definitions and the frozen target

All logarithms are natural, and 0 log 0=0. Put b(x)=-x log x-(1-x)log(1-x). For a finite Hermitian contraction 0<=K<=I_n, DPP(K) is the binary law satisfying

    Pr(A subset X) = det K_A.

Its full atom is

    p_K(S) = sum_{B subset [n]\S} (-1)^|B| det K_(S union B),

and its entropy is the full configuration entropy -sum_S p_K(S)log p_K(S). No count entropy or spectral trace replaces this entropy anywhere below.

For fixed 0<rho<1, the true Toeplitz block is

\[
(Q_n)_{ii}=\rho,\qquad
(Q_n)_{ij}=\frac{\sin(\pi\rho(i-j))}{\pi(i-j)}\quad(i\ne j).
\]

The unchanged target asks that

\[
h_\rho(a,c)=\lim_{n\to\infty}\frac1nH(\operatorname{DPP}(aI+cQ_n))
\]

be concave on all of [0,1-c], for every fixed 0<rho<1 and 0<c<1. The supplied unresolved contrast range is 37/40<c<1. This proof settles only the subregion expressly stated in Theorem C.

The genuine contiguous cyclic projection P_(n,k)=UU* has

\[
U_{j,l}=n^{-1/2}e^{2\pi\mathrm i jl/n},\quad 0\le j<n,\quad0\le l<k.
\]

It is not a direct sum of small blocks. The results below apply to it with explicit k,n dependence, and apply directly to Q_n without pretending that Q_n is a finite projection.

### 0.2 Channel notation

Let X~DPP(K) and, conditionally independently across sites,

\[
\Pr(Y_{a,i}=1\mid X)=a+cX_i,\qquad0<c<1,\quad0<a<1-c.
\]

Define

\[
g_x(1)=a+cx,\quad g_x(0)=1-a-cx,\quad s_u=2u-1,
\]
\[
f_y(x)=\prod_i g_{x_i}(y_i),\quad p_y=\mathbb E f_y(X),\quad
\nu_y=\mathcal L(X\mid Y=y).
\]

In particular every derivative in this proof comes from the full product likelihood f_y; the full output atoms are not assumed affine in a. Write

\[
q_i=K_{ii},\quad r=\frac1n\operatorname{Tr}K,\quad
\mathcal D=\sum_i\left\{\frac{1-q_i}{a(1-a)}+
\frac{q_i}{(a+c)(1-a-c)}\right\},
\tag{0.1}
\]
\[
F_{\rm marg}=\sum_i\frac1{(a+cq_i)(1-a-cq_i)},\qquad
V(K)=\sum_i q_i(1-q_i).
\tag{0.2}
\]

Here D (calligraphic) is the **complete channel Fisher budget**; it is not a matrix or an unknown Hessian. Let

\[
\tau_1=a(a+c),\quad\tau_0=(1-a)(1-a-c),\quad
\tau_{\min}=\min(\tau_0,\tau_1),\quad e_u=c/\tau_u.
\tag{0.3}
\]

For the actual full posterior let C_y=Cov(X|Y=y), and define

\[
\Psi_K(a,c)=\mathbb E_Y\sum_i e_{Y_i}^{\,2}(C_Y)_{ii}.
\tag{0.4}
\]

Psi is a sum of **individual score-coordinate variances**, with the actual output averaging law and compatible full posterior. It is not the variance of the sum of those score coordinates. It need not vanish when the normalized posterior's common-offset tangent vanishes.

Put

\[
\theta=\log\frac{(a+c)(1-a)}{a(1-a-c)},
\]
\[
\kappa(a,c)=\min\left\{\frac1{\sqrt{1-c^4}},\
\frac{\theta}{1-e^{-\theta}},\
2\ \text{if }c^2\le23/25\right\}.
\tag{0.5}
\]

The last candidate is omitted when its condition fails. Every candidate is at least one. In particular, kappa<=2 throughout the range c^2<=23/25, and for every fixed c<1 kappa is bounded independently of a.

### Theorem A: completed-information payment

For every finite n, every Hermitian contraction K, and every legal interior (a,c) as above, let I_K(a)=I(X;Y_a). Then

\[
\boxed{
0\le I_K''(a)\le\kappa\Psi_K(a,c)
\le\kappa(\mathcal D-F_{\rm marg}).
}
\tag{A1}
\]

More precisely, if E_K is the full normalized-posterior score energy defined in Section 3, then

\[
I_K''\le\kappa\Psi_K-(\kappa-1)E_K.
\tag{A2}
\]

Consequently the actual configuration-entropy Hessian obeys

\[
\boxed{
H(\operatorname{DPP}(aI+cK))''
\le(\kappa-1)\mathcal D-\kappa F_{\rm marg}.
}
\tag{A3}
\]

Neither (A1) nor (A3) asserts full entropy concavity for all the parameters covered by the bound. The right side of (A3) can be positive.

A coarser MMSE formulation answers the initially frozen candidate directly. With delta=min(a,1-a-c), tau_min>=c delta, so

\[
I_K''\le \frac{\kappa}{\delta^2}\,
\mathbb E\operatorname{Tr}\operatorname{Cov}(X\mid Y_a)
\le \frac{\theta}{(1-e^{-\theta})\delta^2}\,
\mathbb E\operatorname{Tr}\operatorname{Cov}(X\mid Y_a).
\tag{A4}
\]

For fixed c the first coefficient is O(delta^-2); when c approaches one along a proportional-offset interior interval, the second is O(delta^-2 log(1/delta)). The more informative weighted Psi bound, not this coarser replacement, is what proves Theorem C. Equation (A4) is about completed information; no sharper bound for the instantaneous Q_t'' is claimed.

### Theorem B: Gaussian correction and a rank/time-resolved truncation error

Let B_t be standard n-dimensional Brownian motion independent of X and all channel randomness, and set

\[
Z_t=tX+B_t,\quad \mathcal F_t=\sigma(Z_s:0\le s\le t),\quad
J_T(a)=I(Y_a;\mathcal F_T).
\]

The schedule is observation of every coordinate with unit diffusion, stopped at a deterministic T>=0. The law of $(X,\mathcal F_T)$ is independent of a. Then

\[
\boxed{
J_T''\le I_K''\le\kappa\Psi_K\le\kappa(\mathcal D-F_{\rm marg}).
}
\tag{B1}
\]

Define the remaining conditional information $R_T=I_K-J_T=I(X;Y_a\mid\mathcal F_T)$, with conditional mutual information already including the average over $\mathcal F_T$. It satisfies the sharper actual-average estimate

\[
\boxed{
0\le R_T''\le
\kappa\,\mathbb E_{Y,\mathcal F_T}\sum_i e_{Y_i}^{\,2}
\operatorname{Var}(X_i\mid Y,\mathcal F_T).
}
\tag{B2}
\]

In particular,

\[
\boxed{
0\le I_K''-J_T''\le
\frac{\kappa c^2}{\tau_{\min}^2}
\min\left\{V(K),\frac12\sqrt{nV(K)}e^{-T/8}\right\}.
}
\tag{B3}
\]

For a rank-k projection replace the minimum by

\[
\min\left\{k(1-k/n),\frac12\sqrt{k(n-k)}e^{-T/8}\right\}.
\tag{B4}
\]

For P_(n,k) the first variance bound is exact. For Q_n, V(Q_n)=n rho(1-rho). These are growing-family estimates with rank, dimension, contrast, offset, and time explicit.

No sign is asserted for J_T'' itself, for its t derivative, or for any individual pinning completion excess. In particular, positive Gaussian information-curvature excesses from the reviewed example are retained. Bounds (B2)-(B3) concern a **completed conditional-information remainder**, not a pointwise bound on the instantaneous Q_t'' from the preceding author theorem.

On a compact offset interval with delta=min(a,1-a-c)>=d>0, choosing T_n=16 log n gives a uniform O(n^-1) bound on the unnormalized curvature R_(T_n)''. This controls the Gaussian truncation remainder, not the entire target Jensen defect; the curvature of J_(T_n) still has to be paid. Section 8 gives the exact Jensen statement for this remainder.

### Theorem C: a new percent-density sine-rate region

For every n>=1, every Hermitian contraction K with mean diagonal r, and

\[
\frac{37}{40}\le c\le\frac{959}{1000},\quad d=\frac{1-c}{4},\quad
 d\le a\le3d,
\]
\[
r\in[0,1/100]\ \text{or}\ r\in[99/100,1],
\]

one has

\[
\boxed{
H(\operatorname{DPP}(aI+cK))''\le-\frac{11}{250}n.
}
\tag{C1}
\]

Hence for every fixed 0<rho<=1/100 or 99/100<=rho<1, every fixed contrast in this range, all a_0,a_1 in [d,3d], and every lambda in [0,1],

\[
\boxed{\begin{aligned}
h_\rho((1-\lambda)a_0+\lambda a_1,c)
\ge{}&(1-\lambda)h_\rho(a_0,c)+\lambda h_\rho(a_1,c)\\
&+\frac{11}{500}\lambda(1-\lambda)(a_1-a_0)^2.
\end{aligned}}
\tag{C2}
\]

The portion c<=37/40 was already covered by the supplied baseline; the new high-contrast portion is 37/40<c<=959/1000. A concrete example is rho=1/100, c=19/20, with a in [1/80,3/80]. Unlike a fixed-rank example, rank grows proportionally to n. The theorem applies directly to Q_n for every n, so the Fourier bridge is not needed.

## 1. Exact Gaussian experiment and literature matching

### 1.1 Posterior, martingale, and entropy functional

The likelihood of a Brownian path observation, relative to zero drift, is

\[
\exp\{x\cdot Z_t-t\|x\|^2/2\}
=\prod_i\exp(Z_{t,i}-t/2)^{x_i},
\tag{1.1}
\]

because x_i^2=x_i. The endpoint Z_t is a sufficient statistic for the path. Therefore

\[
\pi_t(x)=\Pr(X=x\mid\mathcal F_t)
\propto\mu(x)\exp\{x\cdot Z_t-t|x|/2\}.
\tag{1.2}
\]

For projection input the factor exp(-t|x|/2) is constant on the support. For nonprojection input it is still a positive sitewise field and must not be discarded. Section 2 proves that every such law is a DPP.

Write q_t=E[X|mathcal F_t], p_(t,y)=pi_t(f_y), and r_(t,y)=E[X|mathcal F_t,Y=y]. With the innovation Brownian motion

\[
W_t=Z_t-\int_0^t q_s\,ds,
\]

Bayes filtering gives

\[
d\pi_t(x)=\pi_t(x)(x-q_t)\cdot dW_t,\qquad
dp_{t,y}=p_{t,y}(r_{t,y}-q_t)\cdot dW_t.
\tag{1.3}
\]

Thus Ito's formula for the configuration entropy -sum_y p_(t,y)log p_(t,y) has drift -Q_t dt, where

\[
Q_t(a)=\frac12\mathbb E_{\mathcal F_t}\sum_y
p_{t,y}\|r_{t,y}-q_t\|^2.
\tag{1.4}
\]

The precise localization entropy identity is

\[
H(Y_a)=\mathbb E H(Y_a\mid\mathcal F_T)+J_T(a),\qquad
J_T(a)=\int_0^T Q_t(a)\,dt.
\tag{1.5}
\]

This uses the actual conditional output entropy, not a product approximation.

### 1.2 Conditional I-MMSE, with its parameter direction and factor

For t>0, Z_t/sqrt(t)=sqrt(t)X+N with standard Gaussian N. The Markov property Y-X-mathcal F_t gives

\[
J_t=I(X;\mathcal F_t)-I(X;\mathcal F_t\mid Y).
\]

Guo--Shamai--Verdu [GSV], Theorem 2, Eq. (22), applies with matrix H=I, independent standard Gaussian coordinates, bounded binary input, and natural logarithms. Applying it separately at each value of Y, **holding a fixed**, yields

\[
\partial_tJ_t=\tfrac12\{\operatorname{mmse}(X\mid\mathcal F_t)
-\operatorname{mmse}(X\mid Y,\mathcal F_t)\}=Q_t.
\tag{1.6}
\]

The final equality is conditional total variance. Also

\[
\partial_t I(X;\mathcal F_t\mid Y)=\tfrac12\mathbb E\operatorname{Tr}
\operatorname{Cov}(X\mid Y,\mathcal F_t).
\tag{1.7}
\]

The same factor 1/2 follows independently from (1.3). It matches Chen--Eldan [CE], Eq. (27), with identity diffusion matrix and fixed f=f_y at each fixed a. Neither source supplies an a-curvature sign or this round's payment.

The adjacent coding-theory tool inspected is Measson--Montanari--Richardson--Urbanke [MMRU], Theorem 1 (General Area Theorem), Eq. (3): for an arbitrary input distribution, coordinatewise smooth memoryless channels, and additional observation Omega conditionally independent of the channel given X,

\[
dH(X\mid Y,\Omega)=\sum_i\partial_{a_i}H(X_i\mid Y,\Omega)\,da_i.
\tag{1.8}
\]

Here the channels are g_x with sitewise offsets a_i, the path is a_i=a, and Omega is mathcal F_T. Converting that paper's bit-valued entropies to nats leaves the identity unchanged. The theorem is not restricted to a degraded binary-symmetric channel path; its later BMS decoding comparisons are not invoked. The second-order pair log-odds identity and the signed Fisher payment below are new connecting steps, not claims imported from the area theorem. They are derived explicitly so (1.8) is not a black-box proof premise.

### 1.3 Every a derivative that can change

At fixed t, pi_t, q_t, and the distribution of mathcal F_t are independent of a. The compatible posterior after Y and the output averaging weights do depend on a. Let

\[
\sigma_y(x)=\partial_a\log f_y(x),\quad
\bar\sigma_y=p_y'/p_y,\quad u_y(x)=f_y''(x)/f_y(x).
\]

Direct Bayes differentiation gives

\[
\nu_y'=\nu_y(\sigma_y-\bar\sigma_y),
\]
\[
\nu_y''=\nu_y\left\{u_y-p_y''/p_y
-2\bar\sigma_y(\sigma_y-\bar\sigma_y)\right\}.
\tag{1.9}
\]

These identities also apply conditionally on pi_t. Differentiating (1.4) twice, with d_y=r_(t,y)-q_t, gives the entire mixed derivative

\[
Q_t''=\mathbb E\sum_y\left[
\tfrac12p_{t,y}''\|d_y\|^2+2p_{t,y}'d_y\cdot r_{t,y}'
+p_{t,y}\{\|r_{t,y}'\|^2+d_y\cdot r_{t,y}''\}\right].
\tag{1.10}
\]

There is no deletion of p'', of the cross term, or of the second posterior response.

For another exact form, set p_y=E p_(T,y), F=sum(p_y')^2/p_y, and

\[
\overline F_T=\mathbb E\sum_y(p_{T,y}')^2/p_{T,y}.
\]

Differentiating the two moving output laws gives

\[
\boxed{
J_T''=\mathbb E\sum_y p_{T,y}''\log\frac{p_{T,y}}{p_y}
+\overline F_T-F.
}
\tag{1.11}
\]

For completeness, start from J_T=E sum_y p_(T,y)log p_(T,y)-sum_y p_y log p_y. Its second derivative is

\[
\mathbb E\sum_y\{p_{T,y}''(1+\log p_{T,y})+(p_{T,y}')^2/p_{T,y}\}
-\sum_y\{p_y''(1+\log p_y)+(p_y')^2/p_y\}.
\]

The terms without a logarithm cancel by normalization, and p_y''=E p_(T,y)'' because the observation law is independent of a. This gives (1.11), including the changing unconditional reference. In particular the unconditional-reference contribution -F is retained. If A_T=-sum p_(T,y)''log p_(T,y), then

\[
H(Y_a)''=\mathbb E A_T-\overline F_T+J_T''.
\tag{1.12}
\]

For fixed n and a compact legal interior interval, all output atoms under every input prior are at least delta^n. Likelihood jets through order two and entropy/normalized-moment jets are bounded uniformly over the finite prior simplex. These bounds justify differentiating finite sums, the Gaussian expectation, and finite-time integrals. No differentiability of a thermodynamic entropy rate is assumed.

## 2. Required determinantal compatibility, proved rather than named

From the supplied inclusion probabilities, the generating polynomial is

\[
G_K(z)=\mathbb E\prod_i z_i^{X_i}
=\det(I+(D_z-I)K).
\tag{2.1}
\]

Indeed expand product_i[1+(z_i-1)X_i] and use the principal-minor determinant expansion. For any positive diagonal D, multiplying the atom of x by product_i d_i^(x_i) and normalizing produces a DPP with kernel

\[
K_D=D^{1/2}K[I+(D-I)K]^{-1}D^{1/2}.
\tag{2.2}
\]

For 0<K<I, this follows from the L-ensemble L=K(I-K)^(-1): the tilt replaces L by D^(1/2)LD^(1/2). It also proves that (2.2) is Hermitian and between zero and I. For general contractions use K_epsilon=(1-2epsilon)K+epsilon I and let epsilon decrease to zero. The normalizing determinant is the expectation of a strictly positive weight under a probability law, hence remains positive; the inverse in (2.2) exists. This proves the boundary cases, including projections, without a hidden invertible-L hypothesis.

For a rank-k projection K=UU*, Cauchy--Binet gives the more explicit formula

\[
K_D=D^{1/2}U(U^*DU)^{-1}U^*D^{1/2}.
\tag{2.3}
\]

It is a rank-k projection. The actual full posterior combines (1.1) with the output fields

\[
d_i=g_1(y_i)/g_0(y_i).
\tag{2.4}
\]

Partial output observations use the same fields only on observed sites. Gaussian fields are not bounded or replaced by a rare-branch supremum. Every finite field is admissible.

For any compatible posterior kernel P,

\[
C_{ii}=P_{ii}(1-P_{ii}),\quad C_{ij}=-|P_{ij}|^2\quad(i\ne j).
\tag{2.5}
\]

The covariance matrix C is positive semidefinite because it is an actual probability covariance matrix. These two facts, plus exact positive tilting, are all the determinantal structure needed by Theorem A. In particular the proof uses **no projection-minor recursion**, no universal completion inequality (C), no third-cumulant closure, and no all-pinnings mixing estimate.

## 3. Complete, observed, and missing Fisher information

The complete likelihood score is

\[
\sigma_y(x)=\sum_i\frac{s_{y_i}}{g_{x_i}(y_i)}
=\sum_i\frac{s_{y_i}}{g_0(y_i)}-\sum_i e_{y_i}x_i.
\tag{3.1}
\]

The second equality follows since the input-one minus input-zero score is -c/[g_0(y_i)g_1(y_i)]=-e_(y_i). Conditional on X, the summands are independent and each has mean zero. Therefore

\[
\mathbb E\sigma_Y(X)^2=\mathcal D.
\tag{3.2}
\]

The actual output score is E[sigma_Y(X)|Y]=p_Y'/p_Y. Conditional total variance yields the exact missing-information identity

\[
F=\mathcal D-E_K,\qquad
E_K=\mathbb E_Y e_Y^TC_Ye_Y
=\sum_y p_y\sum_x\frac{(\nu_y'(x))^2}{\nu_y(x)}\ge0.
\tag{3.3}
\]

Terms on atoms outside the fixed prior support are interpreted as zero. This is proved directly; no statistical missing-information theorem with unverified parameter hypotheses is being imported.

Let

\[
S_K=\mathbb E_Y\sum_{i<j}e_{Y_i}e_{Y_j}|(P_Y)_{ij}|^2.
\]

Using (2.5),

\[
\boxed{E_K=\Psi_K-2S_K.}
\tag{3.4}
\]

In particular 0<=2S_K<=Psi_K. This signed covariance contribution is essential to the payment.

The conditional channel entropy given X is

\[
B_K(a)=\sum_i[(1-q_i)b(a)+q_i b(a+c)],\quad B_K''=-\mathcal D.
\]

With

\[
A_K=-\sum_y p_y''\log p_y,
\]

the supplied complete-entropy identity and (3.3) give

\[
\boxed{
I_K''=H(Y_a)''-B_K''=A_K+E_K,
\qquad H(Y_a)''=-\mathcal D+I_K''.
}
\tag{3.5}
\]

So A_K, not just E_K, must be paid. The next sections bound it without discarding its sign-sensitive structure.

## 4. Exact unnormalized acceleration as an actual-average log-odds sum

Since partial_a g_x(u)=s_u and partial_a^2 g_x(u)=0, the complete probability acceleration is

\[
p_y''=2\sum_{i<j}s_{y_i}s_{y_j}\,p_{-ij}(y_{-ij}).
\tag{4.1}
\]

For a pair i,j condition on the actual Y_-ij, and let R be the kernel of the extrinsic law X|Y_-ij. Write q_i=R_ii and q_j=R_jj just within this pair calculation, w=|R_ij|^2, and

\[
\alpha_u=g_{q_i}(u),\quad\beta_v=g_{q_j}(v),\quad
p_{uv}=\Pr(Y_i=u,Y_j=v\mid Y_{-ij}).
\]

The two-point determinant identity gives

\[
p_{uv}=\alpha_u\beta_v-c^2s_us_vw.
\tag{4.2}
\]

These are the full actual four conditional probabilities. Their negative determinant is

\[
D_{ij}:=p_{01}p_{10}-p_{00}p_{11}=c^2w\ge0.
\tag{4.3}
\]

Use (4.1) in A_K, and write log p_y=log p_-ij+log p_uv. The log p_-ij term cancels because sum_(u,v) s_u s_v=0. Hence

\[
\boxed{
A_K=2\sum_{i<j}\mathbb E_{Y_{-ij}}
\log\frac{p_{01}p_{10}}{p_{00}p_{11}}\ge0.
}
\tag{4.4}
\]

The extrinsic law and its outer weight change with a, but (4.4) is obtained **after differentiating the full unnormalized likelihood**. No derivative of a moving reference has been suppressed. It is an exact regrouping of the entire p'' term, not an affine-atom approximation.

## 5. Scalar log-odds lemma and its explicit factor two

### Lemma 5.1

Let p_uv>0 sum to one and satisfy d=p_01 p_10-p_00 p_11>=0. Suppose p_00+p_11>=s_0, with 0<s_0<=1/2. Then

\[
\log\frac{p_{01}p_{10}}{p_{00}p_{11}}
\le\frac{d\sum_{u,v}p_{uv}^{-1}}{2\sqrt{s_0(1-s_0)}}.
\tag{5.1}
\]

If in addition the log odds is at most theta>0, it is bounded by

\[
\frac{\theta}{1-e^{-\theta}}\,d\sum p_{uv}^{-1}.
\tag{5.2}
\]

If p_00+p_11>=1/25, then the sharper concrete bound

\[
\boxed{\log\frac{p_{01}p_{10}}{p_{00}p_{11}}
\le2d\sum p_{uv}^{-1}}
\tag{5.3}
\]

holds for all such four-cell laws.

### Proof

The case d=0 is immediate. Otherwise put t=log(p_01 p_10/(p_00 p_11))>0 and s=p_00+p_11. Direct algebra gives

\[
d\sum p_{uv}^{-1}
=s(e^t-1)+(1-s)(1-e^{-t})
=(1-e^{-t})\{1+s(e^t-1)\}.
\tag{5.4}
\]

The expression is increasing in s. Since t<=2sinh(t/2), putting z=e^(t/2) gives

\[
\frac{t}{d\sum p^{-1}}
\le\frac{z}{1-s_0+s_0z^2}
\le\frac1{2\sqrt{s_0(1-s_0)}}.
\]

The second inequality is the elementary square inequality
1-s_0+s_0z^2>=2z sqrt(s_0(1-s_0)). This proves (5.1). Dropping the brace in (5.4) gives t/(d sum 1/p)<=t/(1-e^-t); the last function is increasing because e^t>=1+t. This proves (5.2).

For (5.3), it suffices by monotonicity in s to prove, for all t>=0,

\[
F(t):=\frac2{25}e^t-\frac{48}{25}e^{-t}+\frac{46}{25}-t\ge0.
\tag{5.5}
\]

We have F(0)=0. The derivative has the sign of 2z^2-25z+48, z=e^t. Its positive roots are

\[
z_\pm=(25\pm\sqrt{241})/4.
\]

Both exceed one. The derivative is positive, then negative, then positive, so the global minimum on t>=0 is at 0 or at log z_+. At the latter point,

\[
F(\log z_+)=\frac{46+\sqrt{241}}{25}-\log z_+.
\]

Now 15<sqrt(241)<16 and z_+<41/4<11. Moreover,

\[
e^{12/5}>\sum_{j=0}^{8}\frac{(12/5)^j}{j!}
=\frac{150577583}{13671875}>11.
\tag{5.6}
\]

It follows that F(log z_+)>61/25-12/5=1/25>0. This proves (5.3) on the entire continuum, not just a finite grid. The accompanying checker verifies the rational arithmetic in (5.6) and the root brackets. QED.

### 5.2 The hypotheses are deterministic properties of the actual channel

For any prior on the pair of input bits, the probability of equal output bits is a convex combination of

\[
a^2+(1-a)^2,\quad (a+c)^2+(1-a-c)^2,\quad
 a(a+c)+(1-a)(1-a-c).
\]

The first two are at least 1/2. The third equals

\[
1-c-2a(1-a-c)\ge\frac{1-c^2}{2}.
\]

Thus every extrinsic pair in (4.2) satisfies

\[
p_{00}+p_{11}\ge s_0=(1-c^2)/2.
\tag{5.7}
\]

Also each conditional probability Pr(Y_i=1|Y_j=u,Y_-ij) lies in [a,a+c]. The positive log odds in (4.4) is therefore at most logit(a+c)-logit(a)=theta. Apply (5.1)-(5.2); since 2sqrt(s_0(1-s_0))=sqrt(1-c^4), these give the first two constants in (0.5). If c^2<=23/25, then s_0>=1/25, and (5.3) supplies the factor two.

This scalar estimate does not impose a lower bound on posterior input marginals. Rare and highly polarized posterior branches are permitted. All subsequent sums retain their actual weights.

## 6. Exact compatible rebasing and the new signed payment

Fix an extrinsic pair law from Section 4, and then observe the two remaining output bits u,v. Its compatible full posterior kernel P_y satisfies

\[
\boxed{|(P_y)_{ij}|^2=\frac{\tau_u\tau_v}{p_{uv}^{\,2}}|R_{ij}|^2.}
\tag{6.1}
\]

One direct proof uses only a binary 2x2 table. Positive tilts d_i,d_j multiply its covariance determinant by d_i d_j/Z^2. Here d_i=g_1(u)/g_0(u), d_j=g_1(v)/g_0(v), and Z=p_uv/[g_0(u)g_0(v)]. Substitution gives (6.1). The full law is a DPP by Section 2, so the negative covariance determinant is exactly minus the indicated squared kernel entry. This derivation works for general contractions as well as projections.

Multiply (6.1) by e_u e_v=c^2/(tau_u tau_v) and average over the actual four probabilities p_uv. Then

\[
\mathbb E[e_{Y_i}e_{Y_j}|(P_Y)_{ij}|^2\mid Y_{-ij}]
=c^2|R_{ij}|^2\sum_{u,v}p_{uv}^{-1}
=D_{ij}\sum p_{uv}^{-1}.
\tag{6.2}
\]

Thus all pair-dependent extrinsic laws have been converted, exactly and with their changing output weights, to the **same full-output compatible posterior** before the spatial sum is estimated.

Apply Lemma 5.1 to (4.4), and use (6.2):

\[
A_K\le2\kappa S_K.
\tag{6.3}
\]

Combining it with the exact signed missing-Fisher identity (3.4) gives

\[
\begin{aligned}
I_K''&=A_K+E_K\\
&\le2\kappa S_K+(\Psi_K-2S_K)\\
&=\kappa\Psi_K-(\kappa-1)E_K\le\kappa\Psi_K.
\end{aligned}
\tag{6.4}
\]

Nonnegativity follows from A_K>=0 and E_K>=0. This proves the first part of Theorem A.

Equation (6.4) is the new connecting estimate. It is not the identity I''<=-B'' with a renamed unknown. Its right side is an actually averaged diagonal posterior uncertainty, and the next section bounds that uncertainty by explicit scalar-channel quantities. In particular it retains the term that the preceding tangent-only method lost.

### Midpoint falsification gate

For homogeneous input, at a_*=(1-c)/2 the coefficients e_0,e_1 coincide and |X| is fixed. Thus E_K=0, and every normalized posterior first a tangent vanishes. However Psi_K generally stays positive. In the posterior parametrization

\[
\nu_y(A)\propto\mu(A)\exp\{\theta(a)|A\cap y|\},
\]

one has theta'(a_*)=0 but

\[
\theta''(a_*)=2\{a_*^{-2}-(1-a_*)^{-2}\}>0,
\]
\[
\nu_y''(A)=\theta''(a_*)\bigl(|A\cap y|-E_{\nu_y}|A\cap y|\bigr)\nu_y(A).
\]

The acceleration A_K in (4.4) remains. For the reviewed P_(4,2) at c=19/20,a=1/40, the exact checker retains the previously known positive instantaneous Gaussian Q_0'', rather than forcing it to zero. The new upper bound holds there but is too coarse to certify its full entropy sign by itself. That known finite entropy sign is not this round's claimed advance.

## 7. A separately estimable one-site budget

For each i, conditioning on all of Y can only reduce the expected conditional variance relative to conditioning on Y_i alone. Because e_(Y_i)^2 is measurable with respect to Y_i,

\[
\mathbb E e_{Y_i}^2\operatorname{Var}(X_i\mid Y)
\le\mathbb E e_{Y_i}^2\operatorname{Var}(X_i\mid Y_i).
\tag{7.1}
\]

The right side is an explicitly soluble binary Bayes problem with prior q_i. Its complete Fisher budget is

\[
D_i=\frac{1-q_i}{a(1-a)}+
\frac{q_i}{(a+c)(1-a-c)}.
\]

Its output is Bernoulli(a+cq_i), so its observed Fisher is 1/[(a+cq_i)(1-a-cq_i)]. Applying the elementary conditional-variance calculation of (3.1)-(3.3) in one dimension gives

\[
\mathbb E e_{Y_i}^2\operatorname{Var}(X_i\mid Y_i)
=D_i-\frac1{(a+cq_i)(1-a-cq_i)}.
\tag{7.2}
\]

Alternatively, insert Var(X_i|Y_i=u)=q_i(1-q_i)tau_u/Pr(Y_i=u)^2 and check (7.2) algebraically. Sum (7.1)-(7.2):

\[
\Psi_K\le\mathcal D-F_{\rm marg}.
\tag{7.3}
\]

This proves (A1), and (3.5) proves (A3). It is an actual-averaged Bayes variance comparison, not a supremum over rare posterior branches and not a replacement of H by product entropy.

The actual full-output Fisher is also retained in the derivation: F=D-E_K. Since E_K<=Psi_K, (7.3) independently implies F>=F_marg. The proof never assumes that independent marginal scores equal the true vector score.

## 8. Gaussian completion, rank/time bound, and truncation Jensen error

The independent-observation chain rule is

\[
I_K(a)=J_T(a)+\mathbb E_{\mathcal F_T}I_{\pi_T}(a).
\tag{8.1}
\]

Every pi_T is a DPP and is independent of a as a random reference law. Applying Theorem A inside the expectation, with the same channel constant kappa, gives

\[
0\le I_K''-J_T''
\le\kappa\mathbb E_{Y,\mathcal F_T}\sum_i
 e_{Y_i}^2\operatorname{Var}(X_i\mid Y,\mathcal F_T).
\tag{8.2}
\]

This proves (B1)-(B2) with all posterior and output-weight derivatives already retained by Sections 1 and 3-6. It does not say that the instantaneous Q_t'' is nonnegative. Subtracting two positive completed remainders need not preserve order in time.

Let M_T=E Tr Cov(X|Y,mathcal F_T). Dropping only the deterministic factor e_u<=c/tau_min gives R_T''<=kappa c^2 M_T/tau_min^2. Total variance gives M_T<=V(K).

For a sharper time bound, retain just the scalar observation Z_(T,i). If q=Pr(X_i=1), its two Gaussian densities f_0,f_1 have means 0,T and common variance T. For T>0,

\[
\mathbb E\operatorname{Var}(X_i\mid Z_{T,i})
=q(1-q)\int\frac{f_0 f_1}{(1-q)f_0+qf_1}.
\]

The denominator is at least 2sqrt(q(1-q)f_0f_1), so

\[
\mathbb E\operatorname{Var}(X_i\mid Z_{T,i})
\le\frac12\sqrt{q(1-q)}\int\sqrt{f_0f_1}
=\frac12\sqrt{q(1-q)}e^{-T/8}.
\tag{8.3}
\]

The affinity integral is obtained by completing the square; its exponent is -T^2/(8T)=-T/8. Degenerate q=0,1 give zero directly, and T=0 follows by the limit. Conditioning additionally on all other Gaussian observations and Y only decreases the averaged variance. Therefore

\[
M_T\le\frac12\sum_i\sqrt{q_i(1-q_i)}e^{-T/8}
\le\frac12\sqrt{nV(K)}e^{-T/8}.
\tag{8.4}
\]

This proves (B3). For rank k, sum_i q_i=k and sum_i q_i^2>=k^2/n, giving V(K)<=k(1-k/n) and (B4). For the actual contiguous projection all q_i=k/n. For the true Q_n all q_i=rho.

If a ranges over [d,1-c-d], then tau_min>=cd, because

\[
\tau_1=a(a+c)\ge cd,\qquad
\tau_0=(1-a)(1-a-c)\ge cd.
\]

One may bound kappa by the channel-only kappa_0(c)=1/sqrt(1-c^4), or by 2 when permitted. Thus

\[
0\le R_T''(a)\le L_T:=
\frac{\kappa_0(c)}{2d^2}\sqrt{nV(K)}e^{-T/8}
\tag{8.5}
\]

uniformly on the interval. Integrating this finite-dimensional bound yields the exact paid truncation Jensen defect

\[
0\le(1-\lambda)R_T(a_0)+\lambda R_T(a_1)-R_T(a_\lambda)
\le\frac{L_T}{2}\lambda(1-\lambda)(a_1-a_0)^2.
\tag{8.6}
\]

For T_n=16 log n, L_(T_n)=O(n^-1), uniformly at fixed density and fixed interior channel parameters. This is an explicit vanishing **localization-remainder** curvature/Jensen error on growing contiguous projections and Q_n. It is not a vanishing estimate for the whole target's Jensen defect: J_(T_n) still contains the main information curvature. Theorem C pays that main term only on its stated region.

## 9. Uniform regional proof and passage to the true sine rate

Use kappa=2 in (A3). The function x->1/[x(1-x)]=1/x+1/(1-x) is convex on (0,1). Jensen's inequality on the diagonal numbers q_i therefore gives

\[
\frac1nF_{\rm marg}\ge\frac1{v(a+cr)},\qquad v(x)=x(1-x).
\]

Since D/n=(1-r)/v(a)+r/v(a+c), write

\[
B=\frac{1-r}{v(a)}+\frac r{v(a+c)}.
\]

Then

\[
\frac1nH''\le B-\frac2{v(a+cr)}
=\frac{Bv(a+cr)-2}{v(a+cr)}.
\tag{9.1}
\]

This use of marginal Fisher information is a proved lower budget, not an equality between product entropy and full entropy.

Assume 37/40<=c<=959/1000, d=(1-c)/4, and a in [d,3d]. Put epsilon=1-c-a, so epsilon also lies in [d,3d] and v(a+c)=v(epsilon). On these small intervals v is increasing, and

\[
\frac{v(a)}{v(a+c)}\le
\frac{3d(1-3d)}{d(1-d)}\le3.
\tag{9.2}
\]

Also

\[
\frac c{v(a)}\le\frac c{d(1-d)}\le95.
\tag{9.3}
\]

For the last inequality, c/[d(1-d)]=16c/[(1-c)(3+c)] is increasing in c: its derivative is 16(3+c^2)/[(1-c)(3+c)]^2>0. At c=959/1000 it equals 15344000/162319<95; equivalently the rational slack 95d(1-d)-c is 15261/3200000>0. The channel factor-two condition also holds uniformly because c^2<=919681/1000000<23/25.

For 0<=r<=1/100,

\[
B\le\frac{1+2r}{v(a)},\qquad
v(a+cr)=v(a)+cr(1-2a)-c^2r^2\le v(a)(1+95r).
\]

Therefore

\[
Bv(a+cr)\le(1+2r)(1+95r)
\le\frac{102}{100}\frac{195}{100}=\frac{1989}{1000}.
\tag{9.4}
\]

In (9.1), v(a+cr)<=1/4, so

\[
H''/n\le-\frac{11}{1000}\frac1{v(a+cr)}
\le-\frac{11}{250}.
\]

Complementation sends (K,a) to (I-K,1-c-a), preserves configuration entropy, and preserves this offset interval. Applying the already proved case to mean density 1-r establishes the high-density case. This proves (C1).

For Q_n, its integral representation over the interval E_rho gives 0<=Q_n<=I: the quadratic form is the integral over E_rho of the squared trigonometric polynomial, bounded by its integral over the full unit circle. Also trace(Q_n)/n=rho exactly, so (C1) holds for **every n**, without a projection replacement. Integrate the finite-volume inequality first: a twice differentiable function with second derivative at most -gamma has strong Jensen gain (gamma/2)lambda(1-lambda)(a_1-a_0)^2. Divide by n and pass to the supplied pointwise entropy-rate limit at the three offsets. This proves (C2). No derivative of the limiting h is taken, and no Hessian is inferred from a value-error estimate.

For contiguous P_(n,k), the same finite theorem holds whenever k/n is in the region. If fixed rho<1/100 and k=round(nrho), the condition holds for all sufficiently large n; both k and n-k grow linearly. At rho=1/100 it holds on the divisible subsequence, while the direct Q_n statement has no rounding restriction.

## 10. Evidence, contribution, and unresolved gates

### What is proved analytically

The proofs of (A1)-(A3), (B1)-(B4), the uniform truncation estimate (8.6), and (C1)-(C2) cover their stated continua and all dimensions. The determinant tilt formula, score identity, scalar log-mean lemma, exact posterior rebasing, conditional-variance payment, Gaussian affinity calculation, and finite-to-rate integration are all given above. No step assumes the preceding author's MMSE theorem.

### Exact finite certificates

`exact_check.py` uses rational full likelihood jets and outward rational log enclosures. It checks: the complete/missing/output Fisher identities; every pair probability and acceleration coefficient; log-linear identity before evaluating logarithms; pair-to-full posterior rebasing; the new scalar inequality and global payment; midpoint zero tangents with nonzero acceleration; nonuniform rank-one gates; true P_(6,2) and P_(6,3); extreme positive fields; strict nonprojection kernels; and a one-percent-trace nonprojection case. A separate exact checker tests the two moving output-reference laws and both posterior responses under a two-outcome observation of X_0 through a fixed BSC(1/7), at nonmidpoint offsets. It verifies identity (1.11) by equality of rational log coefficients and the full Fisher constant, not by approximate differentiation. This finite experiment is only an identity regression; it does not replace the Gaussian analysis. The scalar continuum proof uses the exact rational critical-point certificate (5.6), not a grid. The parameter-region arithmetic is exact. Counts and recorded values are in frozen evidence.

These checks supplement the analytical proof. They are not an exhaustive numerical proof of a growing family. Reproducing them is self-review, not independent certification.

### Floating diagnostics

Any larger Fourier/Toeplitz or Gaussian-sampling tests are labelled floating diagnostics in separate files. They are not premises. No approximate zero, fitted asymptotic, or Monte Carlo estimate is used to prove an inequality.

### What remains open here

At ordinary densities such as rho=1/2, the bound (A3) can be positive even when the actual entropy Hessian is strongly negative. At the newly certified one-percent densities, the two outer quarters of the legal offset interval are not proved. The regional contrast endpoint 959/1000 does not settle all 37/40<c<1. General bounds (A)-(B) remain valid beyond it, but the explicit negative-budget comparison of Section 9 does not.

The remainder bound (8.6) controls only I_K-J_T; it does not pay J_T on the missing parameter regimes. Calling that truncation estimate a solution of the sine target would be incorrect. No recursion-node completion sign, sparse-pinning supremum, unrestricted homogeneous-law concavity, or common-clock hypothesis is imposed.

## Primary sources: exact use and limitations

- [GSV] D. Guo, S. Shamai (Shitz), S. Verdu, *Mutual Information and Minimum Mean-square Error in Gaussian Channels*, arXiv:cs/0412108v1. Theorem 2, Eq. (22), PDF page 3: finite-power vector input, independent standard Gaussian noise, deterministic channel matrix. Applied with H=I and natural logarithms, then conditionally at fixed a. https://arxiv.org/pdf/cs/0412108
- [CE] Y. Chen, R. Eldan, *Localization Schemes: A Framework for Proving Mixing Bounds for Markov Chains*, arXiv:2203.04163v2. Eq. (27): fixed nonnegative likelihood functional, the normalized tilted law, and stochastic entropy drift. Used as a convention check for the independently derived (1.3)-(1.5), not as an offset-curvature theorem. https://arxiv.org/html/2203.04163v2
- [MMRU] C. Measson, A. Montanari, T. Richardson, R. Urbanke, *The Generalized Area Theorem and Some of its Consequences*, arXiv:cs/0511039v1. Theorem 1, Eq. (3), PDF page 3: arbitrary input, coordinatewise smooth memoryless channels, independent-given-input extra observation. This matches our sitewise offsets and Gaussian observation after converting bits to nats. No later BMS/degradation comparison is invoked. The new second-order payment is derived here. https://arxiv.org/pdf/cs/0511039

The public packet was read at commit c307fe1bcf46b56e4755655c90f60a681979bf13. Mandatory reads and optional-evidence decisions are recorded in `sources/reading_record.md`. No private workspace or other route's unavailable theorem is a dependency.
