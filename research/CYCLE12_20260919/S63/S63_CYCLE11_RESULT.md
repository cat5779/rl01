# S63 — Cycle11: two-noise posterior orthogonalization and ordinary-density true-law transfer

**Overall objective: INCOMPLETE.**

**Proved partial result.** The common-shift Fisher term can be normalized at every density with both channel noises retained. Its extensive off-midpoint posterior correction is a nonnegative within-count square. The count-normalization error is bounded independently of volume; for the actual sine Toeplitz blocks the additional latent-count leakage is explicitly sublinear. A full-response argument also proves cyclic-to-true curvature transfer at every fixed density on compact legal interiors.

The remaining unpaid term is the actual-law, ordered conditional log-odds average. No sign bound on that term sufficient for concavity at rho = 1/3, c = 19/20 is proved here. In particular, the requested fixed-interval entropy-concavity theorem and the ultimate whole-interval conjecture remain INCOMPLETE.

All logarithms are natural. A different entropy base multiplies every entropy-curvature formula by the same positive constant.

## 1. Claim and dependency ledger

| Claim | Status | Exact scope / contribution |
|---|---|---|
| T1. Two-noise posterior Ward identity and unequal-noise energy identity | **PROVED** | Finite projection DPP, any rank and diagonal; every strict legal a. The energy identity also has an explicitly stated contraction leakage term. |
| T2. Orthogonal posterior score decomposition | **PROVED** | Any parameter-independent binary prior and independent two-noise channel. The fixed-cardinality specialization pays the off-midpoint overlap correction as a nonnegative square. |
| T3. Count-Fisher normalization | **PROVED** | Independent Bernoulli sums whose parameters all move with slope one and stay in [delta,1-delta]: count Fisher = n^2 / count variance + O_delta(1), including all tails and endpoint counts. |
| T4. Actual-law curvature and posterior-square interface | **PROVED** | Finite Hermitian contraction DPP. All probability acceleration is retained. The error is explicit in the latent count variance. |
| T5. General-density cyclic/true full-response bridge | **PROVED** | Every fixed 0 < rho,c < 1 and every compact I inside (0,1-c). True and contiguous-Fourier cyclic normalized curvatures have the same uniform limit; no endpoint-uniform or effective-volume assertion. |
| T6. Benchmark coercivity and leakage payment | **PROVED, PARTIAL** | Actual rho=1/3 sine Toeplitz law, c=19/20, a in [1/50,3/100]. It pays the Fisher, two-noise, and leakage portions, not the remaining conditional log-odds budget. |
| O1. “The common-shift score is count-only away from balance” | **DISPROVED** | Exact rank-two contiguous Fourier projection on six cyclic sites, density 1/3, including a=1/50 and c=19/20. This is not an entropy-concavity counterexample. |
| Requested ordinary-density fixed-width concavity | **INCOMPLETE** | The missing inequality is displayed in Section 9. |

### Reviewed inputs and scope

The governing packet is `research/CYCLE11_20260918/SOURCE_STATUS.md` [R0]. Its accepted universal whole-interval threshold is c <= 37/40. The following distinctions matter:

* The Ward–Stein result and review [R2–R3] validate a finite positive generator and an averaged Ward budget, not wordwise payment. The proofs below retain that distinction.
* SA02 and its review [R4–R5] distinguish common-shift Fisher from diagonal Fisher. The Fisher quantity below is the common-shift one.
* S55's reviewed cyclic/true curvature bridge [R6] is half-density only. T5 below is a new proof for the ordinary-density hypotheses, not an inherited generalization.
* QWE06 [R7] rules out a rare-bad-layer shortcut for its corrected-law calculation. No corrected law or layer deletion is used here.
* S61's result and independent review [R8–R9] are accepted only at their frozen half-density midpoint target. That target is not reproved or generalized by assumption.
* The all-density QWE02 mutual-information interface listed in [R0] is not needed for the present full-response proof.

The statistical mechanism is conditional expectation of a complete-data score followed by orthogonal regression. Louis [P1], Section 3.1, gives the primary missing-information identities. Here all needed identities are proved directly for finite positive output laws; no maximum-likelihood, asymptotic-likelihood, or EM convergence hypothesis is imported. The Bernoulli-sum entropy theorem of Hillion–Johnson [P2] concerns count entropy and is not used as a theorem about configuration entropy.

The failed-route catalogue [R1] is consistent with the surviving gap: a pointwise Ward budget, a frozen reference, and discarded typical signed layers do not supply the estimate still needed below.

## 2. Notation and the actual channel

Let X be a binary vector on V={1,...,n}, with a law independent of a. Conditional on X, let the Y_i be independent with

\[
 u=a,\qquad v=a+c,\qquad
 \mathbb P(Y_i=1\mid X)=u+cX_i,
 \qquad 0<a<a+c<1.
\]

Define the two Bernoulli variances and the two likelihood products by

\[
 \beta_0=u(1-u),\quad \beta_1=v(1-v),\qquad
 \eta_1=uv,\quad \eta_0=(1-u)(1-v),\quad
 t=1-u-v=\eta_0-\eta_1.
 \tag{2.1}
\]

These products must not be confused: beta_0 and beta_1 are the two channel variances, whereas eta_0 and eta_1 normalize the two posterior responses. Their products agree:

\[
 \beta_0\beta_1=\eta_0\eta_1.
\]

Put

\[
 \gamma=\beta_1^{-1}-\beta_0^{-1}
       =-\frac{ct}{\eta_0\eta_1},
 \qquad \zeta=\frac c{\eta_0}.
 \tag{2.2}
\]

For a DPP input with Hermitian contraction Q, the output is exactly DPP(K), K=aI+cQ. Indeed, for every finite S,

\[
 \mathbb E\prod_{i\in S}Y_i
 =\mathbb E\prod_{i\in S}(a+cX_i)
 =\sum_{T\subseteq S}a^{|S|-|T|}c^{|T|}\det Q_T
 =\det(aI+cQ)_S.
 \tag{2.3}
\]

Inclusion probabilities determine a binary law. This is the actual independent-channel output, not a corrected cyclic law.

Write

\[
 L=|X|,\quad N=|Y|,\quad T=\sum_iX_iY_i,\quad
 r=\mathbb EL=n\rho,\quad \Lambda=\operatorname{Var}L,
\]

and

\[
 \sigma^2=(1-\rho)\beta_0+\rho\beta_1,
 \qquad \mu=nu+cr,
 \qquad D=n\sigma^2+c^2\Lambda.
 \tag{2.4}
\]

Here sigma^2 is the average conditional channel variance, not the variance of one observed site. Conditional independence gives

\[
 \mathbb EN=\mu,\quad \operatorname{Var}N=D,
 \quad \operatorname{Cov}(N,L)=c\Lambda,
 \quad \operatorname{Cov}(N,T)=r\beta_1+cv\Lambda.
 \tag{2.5}
\]

For DPP(Q), Lambda=Tr(Q-Q^2). If Q is a projection of rank k, then L=k almost surely, rho=k/n, and Lambda=0. None of these fixed-count statements is imposed on a finite sine Toeplitz compression.

## 3. T1 — Two-noise posterior Ward identity (PROVED)

Fix i, put C=V minus {i}, and condition on Y_C=y. For K=aI+cQ define

\[
 B=K_C-\operatorname{diag}(1-y),\qquad
 w=B^{-1}K_{Ci},\qquad
 q=K_{ii}-K_{iC}B^{-1}K_{Ci},\qquad
 d_j=|w_j|^2.
 \tag{3.1}
\]

Then q=P(Y_i=1 | Y_C=y). If Q is a projection, let P^y be the latent posterior projection after this observation and put

\[
 m=P^y_{ii},\qquad \kappa_j=|P^y_{ij}|^2.
\]

The exact two-noise identities are

\[
 q=u+cm,\qquad
 d_j=\begin{cases}
 c^2\kappa_j/\eta_1,&y_j=1,\\
 c^2\kappa_j/\eta_0,&y_j=0,
 \end{cases}
 \qquad
 \partial_aq=1+\sum_{j\in C}d_j.
 \tag{3.2}
\]

Let y^j denote a single flip, o_j=p_C(y^j)/p_C(y), and let [F]_{x,z} denote the divided difference, with [F]_{x,x}=F'(x). For every C^1 function F on [a,a+c],

\[
 \boxed{
 -\mathbb E\big[s_C(Y_C)F(q(Y_C))\big]
 =\mathbb E\sum_{j\in C}d_j(Y_C)
       [F]_{q(Y_C),q(Y_C^j)},
 }
 \qquad s_C=\partial_a\log p_C.
 \tag{3.3}
\]

The expectation in (3.3) is under the actual moving marginal p_C.

There is a positive reversible generator with an explicit score potential:

\[
 (\mathcal L f)(y)=\sum_{j\in C}(1+o_j(y))(f(y^j)-f(y)),
 \qquad -\mathcal L |y|=s_C(y).
 \tag{3.4}
\]

For a rank-k input, a completely explicit biased external score is obtained by defining

\[
 \tau_C(y)=\mathbb E\left[\sum_{j\in C}X_jY_j\mid Y_C=y\right].
\]

It is

\[
 s_C(y)=\frac{|y|-(n-1)u-ck}{\beta_0}
       +\gamma(\tau_C(y)-vk)+\frac c{\eta_0}m(y).
 \tag{3.5}
\]

In particular, the raw count cannot be centered at half filling when k is not n/2. The true score itself has mean zero, as normalization requires.

### Proof

Write Q=VV* with V*V=I_k. The projection DPP gives mass |det V_A|^2 to each k-set A. Observing Y_C multiplies this mass by product weights D_j on A, where

\[
 D_i=1,\qquad D_j=v/u\ (y_j=1),\qquad
 D_j=(1-v)/(1-u)\ (y_j=0).
\]

Cauchy–Binet normalizes these weights by det(V*DV), and their posterior kernel is

\[
 P^y=D^{1/2}V(V^*DV)^{-1}V^*D^{1/2}.
\]

It is a rank-k projection. Thus Cov(X_i,X_j | Y_C)=-kappa_j and sum_{j in C} kappa_j=m(1-m). Differentiating one external likelihood field gives

\[
 \partial_{a_j}\log D_j=-c/\eta_{y_j},\qquad
 \partial_{a_j}m=c\kappa_j/\eta_{y_j}.
\]

On the other hand, differentiating the Schur complement in (3.1) gives partial_{a_j}q=|w_j|^2 and partial_{a_i}q=1. This proves (3.2).

For completeness, the inverse exists uniformly on compact legal interiors. If delta <= a and a+c <= 1-delta, then

\[
 B=S_y/2+(K_C-I/2),\quad S_y=\operatorname{diag}(2y-1),
 \quad \|K_C-I/2\|\le1/2-\delta,
 \quad \|B^{-1}\|\le\delta^{-1}.
 \tag{3.6}
\]

The last bound follows by a Neumann series after factoring S_y/2.

Determinant multilinearity, or direct differentiation of the channel, gives

\[
 \partial_a p_C(y)=\sum_{j\in C}(2y_j-1)p_{C\setminus j}(y_{C\setminus j}).
 \tag{3.7}
\]

Since p_{C minus j}/p_C=1+o_j, (3.4) follows. Detailed balance is the identity

\[
 p_C(y)(1+o_j(y))=p_C(y)+p_C(y^j).
\]

Sherman–Morrison applied to the flip gives

\[
 q(y^j)-q(y)=(2y_j-1)d_j(y)/o_j(y),
 \qquad d_j(y^j)=d_j(y)/o_j(y)^2.
 \tag{3.8}
\]

Condition on all coordinates of C except j and write pi_t=P(Y_j=t | Y_{C minus j}) and q_t=q(Y_j=t). Equation (3.8) gives

\[
 \pi_0d_j(0)+\pi_1d_j(1)=q_0-q_1.
\]

Meanwhile (3.7) gives E[s_C F(q)]=sum_j E[F(q_1)-F(q_0)]. Combining these identities proves (3.3), with the actual endpoint probabilities retained. Formula (3.5) follows by writing the complete score on C using the latent count k-X_i and then taking its posterior expectation. QED.

### Unequal-noise energy and contraction leakage

Let W=sum_j d_j and W_0=sum_{j:y_j=0}d_j. For a projection,

\[
 \boxed{q(1-q)=\eta_1(1+W)+t(q+W_0).}
 \tag{3.9}
\]

Indeed eta_1 sum_{y_j=1}d_j + eta_0 sum_{y_j=0}d_j=c^2m(1-m), and

\[
 q(1-q)-tq-\eta_1=(q-u)(v-q)=c^2m(1-m).
\]

For any Hermitian contraction Q, the exact replacement is

\[
 \boxed{
 q(1-q)=\eta_1(1+W)+t(q+W_0)
          +c^2x^*(Q-Q^2)x,
 \qquad x=(1,-w).
 }
 \tag{3.10}
\]

To prove it, use K(I-K)=eta_1 I+tK+c^2(Q-Q^2), Kx=(q,-diag(1-y)w), and x*K(I-K)x=q(1-q).

The last term is nonnegative and generally nonzero for a finite Toeplitz compression. Dividing (3.10) to solve for (1+W)/[q(1-q)] shows why simply deleting that term would give the wrong lower-bound direction. Its averaged payment is supplied below, not assumed.

## 4. T2 — Orthogonal posterior score tool (PROVED)

This theorem applies to any binary prior independent of a, without a determinantal assumption. Define

\[
 \tau(Y)=\mathbb E[T\mid Y],\qquad
 \lambda(Y)=\mathbb E[L\mid Y],\qquad
 s(Y)=\partial_a\log p_a(Y),\qquad J=\mathbb Es(Y)^2.
\]

Then

\[
 s(Y)=\frac{N-\mu}{\beta_0}
      +\gamma(\tau-vr)-\zeta(\lambda-r).
 \tag{4.1}
\]

Define the two count-orthogonal residuals

\[
 R_T=\tau-vr-\frac{r\beta_1+cv\Lambda}{D}(N-\mu),
 \qquad
 R_L=\lambda-r-\frac{c\Lambda}{D}(N-\mu).
 \tag{4.2}
\]

The exact normalized interface is

\[
 \boxed{
 s=\frac nD(N-\mu)+\gamma R_T-\zeta R_L,
 \qquad
 J=\frac{n^2}{D}+\mathbb E(\gamma R_T-\zeta R_L)^2.
 }
 \tag{4.3}
\]

In addition,

\[
 J\le n\left(\frac{1-\rho}{\beta_0}+\frac{\rho}{\beta_1}\right).
 \tag{4.4}
\]

### Fixed-cardinality output

If L=k almost surely, put rho=k/n. Then

\[
 R=\tau-kv-\frac{\rho\beta_1}{\sigma^2}(N-\mu)
\]

satisfies

\[
 \boxed{J=\frac n{\sigma^2}+\gamma^2\mathbb ER^2,}
 \qquad
 0\le\mathbb ER^2
 \le\frac{n\rho(1-\rho)\beta_0\beta_1}{\sigma^2}.
 \tag{4.5}
\]

This is the signed payment: the additional posterior-overlap contribution cannot reduce the common-shift Fisher coercivity.

If J_N is the Fisher information of the actual count law and m_T(N)=E[T | N], then, still exactly,

\[
 \boxed{J=J_N+\gamma^2\mathbb E\operatorname{Var}(\tau(Y)\mid N).}
 \tag{4.6}
\]

All count layers, including 0 and n, occur with their actual probabilities in this formula.

### Proof

Given X, the successes on latent ones and zeros contribute the complete score

\[
 S=\frac{T-vL}{\beta_1}
   +\frac{N-T-u(n-L)}{\beta_0}.
\]

Using c/beta_0+gamma v=c/eta_0 rewrites this as

\[
 S=\frac{N-\mu}{\beta_0}
   +\gamma(T-vr)-\zeta(L-r).
\]

Finite differentiation gives s=E[S | Y], proving (4.1). Equation (2.5) shows that R_T and R_L have mean zero and are orthogonal in L^2 to N-mu. Differentiating E N=mu gives E[s(N-mu)]=n. Therefore the coefficient of N-mu after orthogonalization is n/D, proving both identities in (4.3).

Conditional on X, the summands of S are independent and centered. Hence E S^2=(n-r)/beta_0+r/beta_1, and conditional-expectation contraction proves (4.4).

When L=k, T and N-T are independent Bin(k,v) and Bin(n-k,u), even though their site locations depend on the prior. The complete residual T-kv-(k beta_1/D)(N-mu) has variance

\[
 k\beta_1-(k\beta_1)^2/D
 =n\rho(1-\rho)\beta_0\beta_1/\sigma^2.
\]

Its conditional expectation given Y is R, proving (4.5). Finally, E[s | N] is the actual count score. Subtracting it from (4.1) and using the orthogonal decomposition of a score under conditioning proves (4.6). QED.

### Which cancellations are density-specific?

Set

\[
 a_*=(1-c)/2,\qquad d=a-a_*,\qquad b_*=(1-c^2)/4.
\]

Then

\[
 \frac\mu n-\frac12=d+c(\rho-\tfrac12),
 \qquad
 \sigma^2=b_*+c(1-2\rho)d-d^2,
 \qquad
 \gamma=\frac{2cd}{\beta_0\beta_1}.
 \tag{4.7}
\]

The linear variance-bias term c(1-2rho)d disappears only at half density. It is kept exactly in sigma^2. By contrast, the overlap-score coefficient gamma vanishes at channel balance at every density, not just at half density. The remaining finite-projection correction obeys

\[
 0\le \frac Jn-\frac1{\sigma^2}
 \le
 \frac{\rho(1-\rho)(\beta_1-\beta_0)^2}
      {\beta_0\beta_1\sigma^2}.
 \tag{4.8}
\]

Thus the unknown posterior part is nonnegative and quadratic in d on any compact legal interval; the linear density bias is explicit.

## 5. T3 — Uniform count-Fisher normalization (PROVED)

**Inputs.** Fix 0 < delta < 1/2. Let Z_1,...,Z_n be independent Bernoulli variables with parameters p_i(a)=a+t_i, where the t_i are fixed and every p_i lies in [delta,1-delta]. Let N=sum_i Z_i, mu=sum_i p_i, V=sum_i p_i(1-p_i), and let J_N denote Fisher information for the common parameter a.

**Output.** There is a finite constant C_delta, independent of n and the offsets t_i, such that

\[
 \boxed{0\le J_N-\frac{n^2}{V}\le C_\delta.}
 \tag{5.1}
\]

The proof below constructs the bound using constants depending only on delta. No asymptotic normality is used without a tail or derivative estimate.

### Proof

Let s_N(l)=partial_a log P(N=l) and

\[
 R(l)=s_N(l)-\frac nV(l-\mu).
\]

Score normalization and differentiation of the count mean imply

\[
 \mathbb ER(N)=0,\quad \mathbb E[R(N)(N-\mu)]=0,
 \quad J_N=n^2/V+\mathbb ER(N)^2.
 \tag{5.2}
\]

It suffices to bound the final expectation uniformly.

Define the cumulant generating function

\[
 \psi(a,z)=\sum_i\log(1-p_i+p_ie^z).
\]

Choose a sufficiently small eta_delta>0. Whenever |l-mu| <= eta_delta n, there is a unique tilt z=z(a,l), |z|<=1, with psi_z=l. Indeed, on |z|<=1 all tilted parameters

\[
 r_i=\frac{p_ie^z}{1-p_i+p_ie^z}
\]

stay in [epsilon_delta,1-epsilon_delta], so psi_zz is bounded below by a positive constant times n. One may take epsilon_delta=delta/e and eta_delta=delta/(4e).

Taylor expansion at z=0, with bounded Bernoulli cumulants, gives

\[
 \left|z-\frac{l-\mu}{V}\right|
 \le C_\delta\frac{(l-\mu)^2}{n^2},
 \qquad
 \left|\psi_a(a,z)-\frac nV(l-\mu)\right|
 \le C_\delta\frac{(l-\mu)^2}{n}.
 \tag{5.3}
\]

Let q_l(a) be the mass at l of the tilted Bernoulli sum. Its mean remains exactly l as a varies along z(a,l), and

\[
 \mathbb P_a(N=l)=e^{\psi(a,z)-zl}q_l(a).
\]

The saddle-point derivative cancels because psi_z=l. Consequently

\[
 s_N(l)=\psi_a(a,z)+\partial_a\log q_l(a).
 \tag{5.4}
\]

We now pay the derivative of the centered mass. Differentiating the tilted mean gives

\[
 \sum_i\dot r_i=0,\qquad
 \dot r_i=r_i(1-r_i)
 \left(\frac1{p_i(1-p_i)}+\dot z\right),
\]

where dot z is minus a weighted average of 1/[p_i(1-p_i)]. Hence |dot r_i| <= C_delta.

Write g_i(t)=1-r_i+r_i e^{it}. For |t|<=1/2, cancellation of sum_i dot r_i gives

\[
 \partial_a\log\prod_i g_i(t)
 =-(e^{it}-1)^2\sum_i\frac{\dot r_i r_i}{g_i(t)},
\]

whose absolute value is at most C_delta n t^2. Also

\[
 \left|\prod_i g_i(t)\right|\le e^{-c_\delta n t^2}
 \qquad (|t|\le\pi).
 \tag{5.5}
\]

For |t|>1/2, differentiate the product rather than dividing by an individual factor. Its derivative has absolute value at most C_delta n exp[-c_delta(n-1)]. Fourier inversion therefore gives

\[
 |q_l'(a)|\le C_\delta n^{-1/2}.
 \tag{5.6}
\]

For clarity, the required lower bound on q_l is also uniform. Since the tilted mean is the integer l,

\[
 e^{-ilt}\prod_i g_i(t)
 =\exp\{-V_r t^2/2+O(n|t|^3)\}
\]

near zero, with c_delta n <= V_r <= n/4. In Fourier inversion, first take |t|<=A/sqrt(n). After scaling, this integral is a positive Gaussian integral plus an error tending uniformly to zero as n grows. By (5.5), the absolute value of the complementary integral is at most C_delta exp(-c_delta A^2)/sqrt(n). Choose A so that this tail is smaller than half the positive central integral, then take n sufficiently large. This proves q_l >= c_delta/sqrt(n). The remaining finitely many n are covered by q_l >= epsilon_delta^n. Thus

\[
 |\partial_a\log q_l(a)|\le C_\delta.
 \tag{5.7}
\]

Combining (5.3), (5.4), and (5.7), on the central window,

\[
 |R(l)|\le C_\delta\left(1+\frac{(l-\mu)^2}{n}\right).
 \tag{5.8}
\]

For independent Bernoulli sums, E(N-mu)^4 <= Cn^2: expand the fourth moment, retaining the single-coordinate fourth moments and the paired variances. Hence the central contribution to E R^2 is bounded by C_delta.

For the complement, the complete count score has absolute value at most n/delta, so |R|<=C_delta n. The bound psi_zz<=n/4 and exponential Markov inequality give

\[
 \mathbb P(|N-\mu|>\eta_\delta n)
 \le2e^{-2\eta_\delta^2n}.
\]

Therefore its contribution is at most C_delta n^2 exp(-2 eta_delta^2 n), uniformly bounded. This includes both extreme counts. Equation (5.2) now proves (5.1). QED.

## 6. T4 — Full curvature and a true-law posterior-square interface (PROVED)

For the actual output DPP(K), define the ordered conditional log-odds sum

\[
 \mathcal A_n(a)=\sum_{i\ne j}\mathbb E_{Y_R}
 \log\frac{p_{10\mid R}p_{01\mid R}}
               {p_{00\mid R}p_{11\mid R}},
 \qquad R=V\setminus\{i,j\}.
 \tag{6.1}
\]

All four entries are probabilities in the actual conditional table. Then

\[
 \boxed{H_n''=\mathcal A_n-J,\qquad \mathcal A_n\ge0.}
 \tag{6.2}
\]

Combining (4.3) with D=n sigma^2+c^2 Lambda gives the unconditional finite-volume inequality

\[
 \boxed{
 H_n''\le\mathcal A_n-\frac n{\sigma^2}
                     +\frac{c^2\Lambda}{\sigma^4}.
 }
 \tag{6.3}
\]

Here sigma^4 means (sigma^2)^2.

### Probability acceleration is retained

Introduce separate channel shifts a_i temporarily. Direct differentiation gives

\[
 \partial_i p(y)=(2y_i-1)p_{-i}(y_{-i}),\qquad
 \partial_{ij}p(y)=(2y_i-1)(2y_j-1)p_{-i,-j}(y_{-i,-j}),
 \quad i\ne j,
\]

and partial_ii p=0. Therefore

\[
 H_n''=-\sum_y\frac{p'(y)^2}{p(y)}-\sum_y p''(y)\log p(y).
\]

Summing the four entries of every ordered pair in the second term gives exactly (6.1), proving (6.2). Positivity follows from q_0>=q_1 in (3.8). This argument does not freeze the output weights or discard p''.

### Exact count-conditioned decomposition

For a general contraction input, set

\[
 m_T(N)=\mathbb E[T\mid N],\quad m_L(N)=\mathbb E[L\mid N],
 \quad A=\tau-m_T(N),\quad B=\lambda-m_L(N),
 \quad W_n=\mathbb E\operatorname{Var}(\tau(Y)\mid N)=\mathbb EA^2.
\]

Conditioning the score (4.1) on N gives the exact identity

\[
 \boxed{J=J_N+\mathbb E(\gamma A-\zeta B)^2.}
 \tag{6.4}
\]

The DPP count generating function is

\[
 \mathbb E z^N=\det(I-K+zK)
 =\prod_{j=1}^n(1-\kappa_j+\kappa_j z),\qquad
 \kappa_j=a+c\lambda_j(Q).
\]

Thus T3 applies to the actual count: its Bernoulli parameters all have slope one and lie in [delta,1-delta]. In particular,

\[
 0\le J_N-n^2/D\le C_\delta.
 \tag{6.5}
\]

Conditional-expectation contraction gives

\[
 \mathbb EB^2\le\Lambda,\qquad
 \mathbb EA^2\le\operatorname{Var}T=r\beta_1+v^2\Lambda.
\]

Consequently, with

\[
 \mathcal E_n=C_\delta+\frac{c^2\Lambda}{\sigma^4}
  +2|\gamma\zeta|\sqrt{(n\rho\beta_1+v^2\Lambda)\Lambda}
  +\zeta^2\Lambda,
 \tag{6.6}
\]

we obtain the useful output interface

\[
 \boxed{
 H_n''=\mathcal A_n-\frac n{\sigma^2}-\gamma^2W_n+e_n,
 \qquad |e_n|\le\mathcal E_n.
 }
 \tag{6.7}
\]

For a projection, Lambda=0 and, more strongly, -C_delta <= e_n <= 0. For a true sine Toeplitz block, Section 8 proves Lambda=O(log n), so e_n=o(n) uniformly on compact legal a-intervals. The weaker inequality (6.3) has the sharper O(log n) error when the positive posterior square is not retained.

This is a true-law statement. No half-density bridge, corrected posterior, frozen count law, or unproved typical-layer sign is required.

## 7. T5 — General-density full-response curvature bridge (PROVED)

**Theorem.** Fix 0<rho,c<1 and a compact interval I inside (0,1-c). Let H_n be the entropy of the actual sine Toeplitz output. Let H_n^cyc be the entropy for a cyclic projection onto k_n contiguous Fourier modes, with k_n/n tending to rho, observed through the same channel. Then there are continuous functions f,j on I such that, uniformly for a in I,

\[
 \frac{J_n}{n}\longrightarrow f(a),\qquad
 \frac{\mathcal A_n}{n}\longrightarrow j(a),\qquad
 \frac{(H_n^{\rm cyc})''}{n},\ \frac{H_n''}{n}
 \longrightarrow j(a)-f(a).
 \tag{7.1}
\]

The true entropy rate exists, belongs to C^2 in the strict legal interior, and satisfies

\[
 h_{\rho,c}''(a)=j(a)-f(a).
 \tag{7.2}
\]

The same f,j are obtained from cyclic common Fisher and cyclic conditional log-odds sums. In particular, finite cyclic chords divided by n converge to the corresponding true entropy-rate chords. No quantitative rate or endpoint-uniform assertion is included.

### Proof: local responses

For a finite configuration y let

\[
 G=(K-\operatorname{diag}(1-y))^{-1}.
\]

The determinant formula for a DPP mass gives s=Tr G and partial_a s=-Tr G^2. Normalization yields

\[
 J=\mathbb E\operatorname{Tr}G^2.
\]

Conditioning on Y_{-i} and using the Schur inverse shows that the i-th row contributes

\[
 \Phi_i(y_{-i})=\frac{1+\|w_i\|_2^2}{q_i(1-q_i)}.
 \tag{7.3}
\]

Thus J=sum_i E Phi_i. Let ell(q)=log(q/(1-q)) and define

\[
 \Psi_i(y_{-i})=\sum_{j\ne i}|(w_i)_j|^2
          [\ell]_{q_i(y),q_i(y^j)}.
 \tag{7.4}
\]

For a fixed pair-rest table, averaging the j flip with its actual endpoint probabilities as in (3.3) gives

\[
 \mathbb E_{Y_j\mid Y_R}
    |(w_i)_j|^2[\ell]_{q_i,q_i^j}
 =\ell(q_0)-\ell(q_1)
 =\log\frac{p_{10\mid R}p_{01\mid R}}
                {p_{00\mid R}p_{11\mid R}}.
\]

Therefore A_n=sum_i E Psi_i, with no pointwise identification of an averaged table budget.

### Proof: compact response lemma

Choose delta>0 with a>=delta and a+c<=1-delta on I. On the infinite complement of the origin let

\[
 B_z=S_z/2+T(a),\quad T(a)=K_{\mathbb Z\setminus0}(a)-I/2,
 \quad b(a)=K_{\mathbb Z\setminus0,0}(a),\quad
 w(a,z)=B_z^{-1}b(a).
\]

We have ||T(a)||<=1/2-delta. A coordinatewise-converging sequence of sign words gives strong convergence of S_z. Uniform invertibility therefore makes (a,z) -> w(a,z) continuous into ell^2. Its domain, I times the product sign-word space, is compact. Consequently its image is compact and

\[
 \sup_{a,z}\sum_{|j|>R}|w_j(a,z)|^2\longrightarrow0.
 \tag{7.5}
\]

Here is the approximation step in detail. Extend a finite-volume response by zero and its masked matrix outside the volume by S_z/2. Its perturbation T_m still satisfies the same norm bound. If T_m tends strongly to T and b_m tends in norm to b, then

\[
 w_m-w=B_m^{-1}\big[(b_m-b)+(T-T_m)w\big].
 \tag{7.6}
\]

Uniformly bounded strongly convergent operators converge uniformly on compact vector sets. Applying this to the compact response image proves w_m -> w uniformly over all sign words and a in I.

For ordinary compressions, this is uniform over every interval containing a growing neighborhood of the origin. To see it, if P is its coordinate projection, then for any x,

\[
 \|(T-PTP)x\|
 \le\|(I-P)Tx\|+\|T\|\|(I-P)x\|.
\]

Both tails vanish uniformly on the relevant compact families. This proves the claim without requiring operator-norm convergence of the compressions.

All finite conditional probabilities lie in [a,a+c] by the channel representation, so their infinite limits lie in [delta,1-delta]. Thus

\[
 0<[\ell]_{q,q'}\le[\delta(1-\delta)]^{-1}.
\]

Equations (7.5)-(7.6) make Phi a continuous bounded infinite-word observable. They also make Psi continuous and bounded: first truncate the sum in (7.4), then bound its remaining tail by [delta(1-delta)]^{-1} times the squared response tail. Every finite-volume Phi and Psi converges uniformly in the word when its anchor recedes from the boundary. This pays the full curvature response, not just entropy values.

### Proof: actual blocks and identification of h''

The infinite sine operator is the Fourier multiplier by the indicator of [-rho/2,rho/2]; it is an orthogonal projection with the displayed sine kernel. Its finite compressions are contractions. Their DPP laws are consistent marginals of a stationary process. The channel preserves consistency and stationarity.

For a block of length n, all but at most 2R anchors have distance at least R from its boundary. The uniform response convergence above, and boundedness of the responses, imply

\[
 \sup_{a\in I}\left|\frac{J_n}{n}-\mathbb E\Phi_0\right|
 \le\omega_R+C_\delta R/n,
\]

and the same estimate for A_n/n with Psi_0, where omega_R tends to zero. Finite cylinder probabilities depend continuously on a through determinants. Uniform cylinder approximation of Phi and Psi then proves continuity of their expectations. This gives the true-block limits f and j in (7.1).

The first derivative is H_n'=-sum_i E ell(q_i), obtained by summing partial_i p=(2y_i-1)p_{-i} against -log p. Thus H_n'/n converges uniformly to -E ell(q_0), by the same argument without a flip sum. Stationarity gives H_{n+m}<=H_n+H_m, so h=lim H_n/n exists. Integrating the uniform first-derivative convergence identifies h', and integrating the uniform second-derivative convergence identifies its derivative j-f. This proves C^2 regularity without differentiating an entropy-value error.

### Proof: ordinary-density cyclic approximation

After a diagonal unitary gauge, the cyclic rank-k_n projection has local entries

\[
 Q_n^{\rm cyc}(i,j)=
 \frac{\sin(\pi k_n(i-j)/n)}{n\sin(\pi(i-j)/n)},\qquad
 Q_n^{\rm cyc}(i,i)=k_n/n.
\]

The gauge does not change the DPP law or the response observables. Embed a centered period in the integers and extend its projection by zero. Each fixed matrix entry converges to the sine kernel. Furthermore

\[
 \|Q_n^{\rm cyc}e_j\|_2^2=k_n/n\longrightarrow\rho
 =\|Q_\rho e_j\|_2^2.
\]

Coordinatewise convergence plus these norm limits gives strong convergence on every basis vector, and hence on ell^2 because the operator norms are at most one. Equation (7.6) supplies all-word uniform convergence of the masked responses. Actual finite-cylinder probabilities converge by their determinant formulas. Cyclic translation invariance identifies normalized sums of anchor responses with a single-anchor expectation. This proves the cyclic limits in (7.1).

Finally, the second-derivative representation of a chord depends only on these curvatures, so their uniform convergence transfers every fixed chord. No affine normalization of cyclic entropy values is required for this conclusion. QED.

## 8. T6 — True sine leakage and the benchmark (PROVED, PARTIAL)

Let q_d=sin(pi rho d)/(pi d) for d!=0 and q_0=rho. Since the infinite operator is a projection,

\[
 \Lambda_n=\operatorname{Tr}(Q_{\rho,n}-Q_{\rho,n}^2)
 =2\sum_{d=1}^{n-1}d|q_d|^2
  +2n\sum_{d=n}^{\infty}|q_d|^2.
 \tag{8.1}
\]

Using |q_d|<=1/(pi d), the harmonic-sum bound, and n sum_{d>=n} d^{-2}<=2 for n>=2, gives

\[
 \boxed{0\le\Lambda_n\le\frac2{\pi^2}(\log n+3).}
 \tag{8.2}
\]

The n=1 case follows directly from rho(1-rho)<=1/4. Thus (6.6) is O_{I,c}(sqrt(n log(n+1))) and (6.3) has an O_{I,c}(log(n+1)) error. Both are uniform over a in I.

### Exact true-law rate identity

Combining T4 and T5 proves the uniform limit

\[
 \Xi(a)=\lim_{n\to\infty}\frac{\gamma(a)^2}{n}
       \mathbb E_a\operatorname{Var}(\tau(Y)\mid N)
       =f(a)-\frac1{\sigma^2(a)}\ge0.
 \tag{8.3}
\]

Every posterior and expectation on the left is for the true finite Toeplitz input and its actual observed output. The limit is continuous, including at a=a_*, where its multiplier gamma is zero. Data processing (4.4) supplies the explicit upper bound

\[
 \boxed{
 0\le\Xi(a)\le
 \frac{\rho(1-\rho)(\beta_1-\beta_0)^2}
      {\beta_0\beta_1\sigma^2}.
 }
 \tag{8.4}
\]

The promised ordinary-density posterior / conditional-table identity is

\[
 \boxed{
 h_{\rho,c}''(a)=j(a)-\frac1{\sigma^2(a)}-\Xi(a).
 }
 \tag{8.5}
\]

Both unequal-noise posterior and latent-count terms have now been paid: the former is the nonpositive contribution -Xi; the latter is sublinear by (8.2). Equation (4.7) keeps the nonzero ordinary-density linear bias explicitly.

As one additional consequence, the common-Fisher density, not the entropy curvature, has the rigorously determined first-order behavior

\[
 f(a_*+d)=\frac1{b_*+c(1-2\rho)d-d^2}+O(d^2),
\]

and hence

\[
 f(a_*)=1/b_*,\qquad
 f'(a_*)=-c(1-2\rho)/b_*^2.
 \tag{8.6}
\]

This follows by squeezing between zero and (8.4), not by differentiating a lower bound.

### Benchmark constants

For rho=1/3, c=19/20, and a in I=[1/50,3/100],

\[
 \frac{683}{30000}\le\sigma^2(a)\le\frac{389}{15000},
 \qquad
 \frac1{\sigma^2(a)}\ge\frac{15000}{389}.
 \tag{8.7}
\]

The variance is increasing on this interval because its derivative is 1-2(a+c/3)>0. From (6.3), for every n>=1 and every a in I,

\[
 \boxed{
 H_n''(a)\le\mathcal A_n(a)-\frac{15000}{389}n
       +\frac{812250000}{466489}\Lambda_n.
 }
 \tag{8.8}
\]

In particular,

\[
 H_n''(a)\le\mathcal A_n(a)-\frac{15000}{389}n
 +\frac{1624500000}{466489\pi^2}(\log n+3).
 \tag{8.9}
\]

The positive Fisher correction also has a uniform explicit bound:

\[
 0\le\Xi(a)\le\frac{45125000}{29216691}.
 \tag{8.10}
\]

To check (8.10), use |d|<=1/200, (beta_1-beta_0)^2<=c^2/10000, and sigma^2>=683/30000. The product beta_0 beta_1=(b_*-d^2)^2-c^2d^2 decreases as d^2 increases on this interval, so its minimum is (49/2500)(291/10000). Substitution in (8.4) gives the stated rational constant.

## 9. Precise remaining gap

**INCOMPLETE:** no estimate proved here establishes, for some epsilon>0,

\[
 \sup_{a\in I}\left[j(a)-\Xi(a)-\frac1{\sigma^2(a)}\right]
 \le-\varepsilon.
 \tag{9.1}
\]

A stronger sufficient input would be

\[
 \sup_{a\in I}j(a)<15000/389.
 \tag{9.2}
\]

Neither (9.1) nor (9.2) is asserted. The term j is the concrete actual-law conditional log-odds sum from (6.1), localized by (7.4). Its typical signed contribution cannot be removed by the corrected-law tail obstruction, particle-hole symmetry, or the fixed-count Fisher normalization.

For a_0<a_1 in I, a_lambda=(1-lambda)a_0+lambda a_1, define the nonnegative tent kernel

\[
 G_\lambda(t)=
 \begin{cases}
 (1-\lambda)(t-a_0),&a_0\le t\le a_\lambda,\\
 \lambda(a_1-t),&a_\lambda\le t\le a_1.
 \end{cases}
\]

Then the exact remaining chord budget is

\[
 \operatorname{Gap}_\lambda h
 =\int_{a_0}^{a_1}G_\lambda(t)
   \left[\frac1{\sigma^2(t)}+\Xi(t)-j(t)\right]dt.
 \tag{9.3}
\]

Since integral G_lambda=lambda(1-lambda)(a_1-a_0)^2/2, a bound (9.1) would give the requested strictly positive chord margin. T5 pays the cyclic-to-true transfer for such a bound, but does not supply its sign.

## 10. O1 — A count-only score fails in the actual cyclic geometry (DISPROVED)

Consider the rank-two contiguous Fourier projection on six cyclic sites,

\[
 Q_{rs}=\frac{1+e^{2\pi i(r-s)/6}}6.
\]

Its diagonal is 1/3. A latent pair at cyclic distance 1, 2, or 3 has respective probability 1/36, 1/12, or 1/9, by its two-by-two principal minor.

For an observed two-set Y, let h=P(X=Y). Before observing Y, the overlap T has masses

\[
 P(T=2)=h,\quad P(T=1)=2/3-2h,\quad P(T=0)=1/3+h.
\]

Conditional on this observed configuration the likelihood tilts these masses by z^T, where

\[
 z=\frac{v(1-u)}{u(1-v)}>1.
\]

Thus

\[
 \tau_h=\frac{2hz(z-1)+(2/3)z}
              {h(z-1)^2+(2z+1)/3}.
\]

If Z_h denotes the denominator, then for h_2>h_1,

\[
 \tau_{h_2}-\tau_{h_1}
 =\frac{(h_2-h_1)(2/3)z(z-1)(z+2)}{Z_{h_1}Z_{h_2}}>0.
 \tag{10.1}
\]

Take Y={0,1} and Y'={0,3}. They have the same count, but h=1/36 and h'=1/9, so their posterior overlaps differ. Formula (4.1) for a rank-two prior shows their common-shift scores differ whenever gamma!=0, equivalently a!=(1-c)/2. In particular this holds at c=19/20, a=1/50, where z=4753/3.

Therefore a count-only score formula away from balance is false even in the requested ordinary-density contiguous-Fourier observation geometry. The nonzero posterior square in the proved tool is necessary. This does not disprove entropy concavity, nor does a cyclic six-site calculation establish a true Toeplitz counterexample.

## 11. Exact checks and evidence scope

The companion Python scripts use exact rational arithmetic, not floating sign scans. `check_s63.py` checks probability acceleration, score normalization, the orthogonal square, and information upper bounds on all configurations of the six-site projection at a=1/50,1/40,3/100. It also checks the random-count formula for the genuine contraction Q=[[1/3,1/6],[1/6,1/3]]. `check_s63_ward.py` checks the biased posterior, flip, energy, and Ward identities for all 192 anchor words of the six-site model at a=1/50.

All checks passed. These checks are finite algebra audits; the proofs above, rather than those checks, justify the stated quantifiers. No numerical calculation is offered as evidence for the missing entropy-concavity sign.

## References and packet access

All nine required packet files were accessible and read in the prescribed order. The independent S61 review and archived proposal were also read. Repository-relative paths below refer to the user's branch `research/sa-cycle11-pr128-20260918` in `cat5779/rl01`.

[R0] `research/CYCLE11_20260918/SOURCE_STATUS.md`.

[R1] `research/CYCLE11_20260918/sources/FAILED_ROUTES.md`.

[R2] `research/CYCLE11_20260918/sources/WARD_STEIN_RESULT.md`.

[R3] `research/CYCLE11_20260918/sources/WARD_STEIN_REVIEW.md`.

[R4] `research/CYCLE11_20260918/sources/SA02_FULL_BLOCK.md`.

[R5] `research/CYCLE11_20260918/sources/SA02_REVIEW.md`.

[R6] `research/CYCLE11_20260918/sources/S55_REVIEW.md`.

[R7] `research/CYCLE11_20260918/sources/QWE06_REVIEW.md`.

[R8] `research/CYCLE11_20260918/S61/S61_CYCLE10_RESULT.md`.

[R9] `research/CYCLE11_20260918/sources/S61_REVIEW.md`; independent RL01 PR44 review.

[R10] `research/CYCLE11_20260918/PR128_original/WEB_PRO_02_GENERAL_DENSITY_OFF_MIDPOINT.md`.

[P1] Thomas A. Louis, “Finding the Observed Information Matrix when Using the EM Algorithm,” Journal of the Royal Statistical Society, Series B, 44(2), 226–233 (1982), Section 3.1 and Appendix. DOI: 10.1111/j.2517-6161.1982.tb01203.x. The conditional-score formula and its regularity scope were checked in the primary paper; the finite-law version used here is reproved in Section 4.

[P2] Erwan Hillion and Oliver Johnson, “A proof of the Shepp–Olkin entropy concavity conjecture,” Bernoulli 23(4B), 3638–3649 (2017); arXiv:1503.01570. Its target is the entropy of a Bernoulli sum, not complete-configuration entropy; no concavity conclusion is imported from it.
