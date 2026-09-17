> **待独立对抗性审查 / PENDING_INDEPENDENT_REVIEW。** 下文保留来源原文；其中 PROVED、PASS、AUDIT 等是作者或既有记录的表述，不代表本次 SA 成果已独立通过。先读本包根目录 REVIEW_REQUEST.md；外部审计与其他 SA 分开进行。

# Full-law score compensation and the critical-scale statistical experiment

**Author theorem, subject to independent review.** This note supplies a second
proof of the second-order compensation in `MESOSCOPIC_COMPENSATION.md` and a
full-configuration likelihood approximation. It does not sign the remaining
order-one entropy curvature. The two proofs are author cross-checks, not two
independent reviews.

## 1. A finite theorem with all spectral defects retained

Let `Q` be an `n x n` Hermitian positive contraction with `Tr Q=n/2`. Fix
`0<c<1`, `0<=u<=1`, and consider the actual diagonal-shift path

\[
 K_\delta=\tfrac12 I+uc(Q-\tfrac12 I)+u\delta I.
 \tag{1.1}
\]

Set

\[
 V=\operatorname{Tr}Q(I-Q),\quad
 v=\frac{1-u^2c^2}{4},\quad v_*=(1-c^2)/4>0.
\]

At `delta=0`, let `P` be the full labelled-configuration law, let `M` be its
particle count, and define its genuine score and atom acceleration by

\[
 s(Y)=\frac{\partial_\delta p_\delta(Y)|_0}{p_0(Y)},\qquad
 a(Y)=\frac{\partial_\delta^2p_\delta(Y)|_0}{p_0(Y)}.
\]

All atoms are strictly positive. Introduce the count-measurable random variable

\[
 W=\frac{u}{v}(M-n/2),
\]

and the explicit quantities

\[
 e_1=\frac{u^3c^2}{2v^{3/2}}\sqrt V,
 \qquad
 w_2=\left(\frac{u^2n}{v}+\frac{u^4c^2V}{v^2}\right)^{1/2},
\]
\[
 e_2=(2w_2+e_1)e_1+
          \frac{u^4c^2V}{v^2}+\frac{u^3c\sqrt n}{v^{3/2}}.
 \tag{1.2}
\]

### Theorem A: full-law score and acceleration estimates

\[
 \boxed{\quad
 \|s-W\|_{L^2(P)}\le e_1,
 \qquad
 \|a-(W^2-u^2n/v)\|_{L^1(P)}\le e_2.
 \quad} \tag{1.3}
\]

In addition,

\[
 \|s\|_2\le u\sqrt{n/v},\qquad \|W\|_2=w_2.
 \tag{1.4}
\]

These are finite, full-configuration statements, not identities for the
entropy of `M`. They also hold for projections (`V=0`); in that case the
score is exactly the displayed count score, while the acceleration still
contains a fluctuation of size at most `u^3 c sqrt(n)/v^(3/2)`.

### Proof: a parameter-independent, count-preserving observation channel

Write `Q=U diag(t_j) U*`, with `0<=t_j<=1`. The eigenvectors do not change
with `delta`. Put

\[
 d_j=t_j(1-t_j),\quad
 \lambda_j=\tfrac12+uc(t_j-\tfrac12),\quad
 v_j=\lambda_j(1-\lambda_j)=v+u^2c^2d_j.
 \tag{1.5}
\]

Draw independent Bernoulli variables `Z_j` with success probabilities
`lambda_j+u delta`. Given the occupied spectral set `S`, draw an observed set
`A` with conditional probabilities

\[
 T_U(A\mid S)=
 \begin{cases}|\det U_{A,S}|^2,&|A|=|S|,\\0,&|A|\ne|S|.\end{cases}
 \tag{1.6}
\]

Cauchy--Binet shows that each column sums to one. Expanding principal minors
(or applying Cauchy--Binet again to the inclusion probabilities) shows that
the resulting observed law is exactly `DPP(K_delta)`. This proves the
representation directly. It is not an assertion that arbitrary unitary
conjugation preserves configuration entropy. The channel is generally
nontrivial, but is independent of `delta` and preserves the particle count
`sum_j Z_j=|A|` in every realization.

The latent Bernoulli score and its derivative at zero are

\[
 S=u\sum_j\frac{Z_j-\lambda_j}{v_j},
\]
\[
 T=-u^2\sum_j\frac1{v_j}
   -u^2\sum_j\frac{(1-2\lambda_j)(Z_j-\lambda_j)}{v_j^2}.
 \tag{1.7}
\]

Differentiation of the finite mixture, with its fixed channel, gives the
**actual observed** identities

\[
 s(Y)=\mathbb E[S\mid Y],\qquad
 a(Y)=\mathbb E[S^2+T\mid Y].
 \tag{1.8}
\]

Because `Tr Q=n/2`, `sum_j lambda_j=n/2`. Count preservation therefore gives
`W=(u/v)sum_j(Z_j-lambda_j)` also on the latent space. Independence yields

\[
 \mathbb E(S-W)^2
 =\frac{u^6c^4}{v^2}\sum_j\frac{d_j^2}{v_j}
 \le\frac{u^6c^4}{4v^3}V=e_1^2,
 \tag{1.9}
\]

where `d_j^2<=d_j/4` and `v_j>=v` were used. Also

\[
 \mathbb ES^2=u^2\sum_jv_j^{-1}\le u^2n/v,
 \quad
 \mathbb EW^2=\frac{u^2}{v^2}\sum_jv_j=w_2^2.
\]

Conditional expectation contracts `L^2`, so the score assertions follow.
For the acceleration, first

\[
 \mathbb E|S^2-W^2|
 \le\|S-W\|_2\|S+W\|_2
 \le e_1(2w_2+e_1).
\]

The mean and fluctuation of the second expression in (1.7) obey

\[
 0\le \mathbb ET+u^2n/v
 =u^4c^2\sum_j\frac{d_j}{v v_j}\le u^4c^2V/v^2,
\]
\[
 \operatorname{Var}T
 =u^4\sum_j\frac{(1-2\lambda_j)^2}{v_j^3}
 \le u^6c^2n/v^3.
\]

Using (1.8), conditional Jensen, and these two estimates proves (1.3).
Every sign-changing atom acceleration remains in the identity. QED.

## 2. Full-law likelihood approximation, not a count-entropy replacement

Keep the finite setup. For a real shift `delta`, put `h=u delta/v` and define
a genuine exponential tilt of the **full** midpoint law:

\[
 \widetilde P_\delta(Y)=
 \frac{P_0(Y)e^{h(M(Y)-n/2)}}{\mathbb E_0e^{h(M-n/2)}}.
 \tag{2.1}
\]

Assume `|h|<=1` and that the shifted kernel is legal. We use the convention
`TV(P,Q)=(1/2)sum|P-Q|`.

### Theorem B: quantitative relative-entropy comparison

\[
 \boxed{\quad
 D(P_\delta\Vert\widetilde P_\delta)
 \le\frac{e}{v_*}
 \left(\frac{h^2u^4c^4}{2}V+\frac{nh^4}{32}\right).
 \quad} \tag{2.2}
\]

Consequently `TV(P_delta,tilde P_delta)` is at most the square root of half
this bound. This total-variation statement is between two finite full laws
on the **same** configuration space; it is not total-variation convergence
of a count lattice to a continuous Gaussian.

### Proof

Since (1.6) preserves count, tilting its observed law by `exp(hM)` is the
same as tilting the latent independent Bernoulli law by `exp(h sum Z_j)` and
then using the unchanged channel. The tilted eigenvalue is

\[
 \kappa_j(h)=\frac{e^h\lambda_j}{1-\lambda_j+e^h\lambda_j}.
\]

The logistic derivatives satisfy `kappa_j'(0)=v_j` and
`|kappa_j''(h)|<=1/4`. Taylor's theorem and (1.5) give

\[
 |\kappa_j(h)-(\lambda_j+u\delta)|
 \le |h|u^2c^2d_j+h^2/8.
\]

Therefore

\[
 \sum_j|\kappa_j(h)-(\lambda_j+u\delta)|^2
 \le\frac{h^2u^4c^4}{2}V+\frac{nh^4}{32}.
 \tag{2.3}
\]

The derivative of `log(kappa_j(1-kappa_j))` in `h` is `1-2kappa_j`, whose
absolute value is at most one. Thus
`kappa_j(h)(1-kappa_j(h))>=e^(-|h|)v_j>=v_*/e`.
For Bernoulli parameters `p,q`, the elementary log bound `log x<=x-1`
gives

\[
 D(\operatorname{Ber}(p)\Vert\operatorname{Ber}(q))
 \le\frac{(p-q)^2}{q(1-q)}.
\]

Sum this inequality over the independent latent coordinates. Relative
entropy cannot increase under a fixed stochastic channel: this follows
directly from the log-sum inequality applied separately at each output of
(1.6). Combining with (2.3) proves (2.2). QED.

### Corollary: the aligned Fejer family's critical-scale local experiment

For the exterior matrix in `MESOSCOPIC_COMPENSATION.md`, `n=2R` and
`V<=mathcal V_R=O(log R)`. Put `delta=theta/sqrt(R)`, with `|theta|<=T`.
For all sufficiently large `R`, legality and `|h|<=1` hold uniformly. The
complete-law relative-entropy error is

\[
 D(P_{\theta/\sqrt R}\Vert\widetilde P_{\theta/\sqrt R})
 \le \frac{3}{v_*}
 \left[\frac{u^6c^4T^2\mathcal V_R}{2v_*^2R}
       +\frac{u^4T^4}{16v_*^4R}\right]
 =O_{c,T}(\log R/R).
 \tag{2.4}
\]

We used `e<3` only to display elementary constants. For each fixed `u>0`,
let `X_R=(M_R-R)/sqrt(R)`. Under the midpoint law,

\[
 X_R\Rightarrow N(0,2v),\qquad v=(1-u^2c^2)/4.
\]

The full-configuration likelihood ratio then has the local expansion

\[
 \boxed{\quad
 \log\frac{p_{\theta/\sqrt R}(Y)}{p_0(Y)}
 =\frac{\theta u}{v}X_R-\frac{u^2\theta^2}{v}
       +o_{P_0}(1).
 \quad} \tag{2.5}
\]

Here is the justification, including the observation-channel issue. The
count log moment-generating function has third derivative bounded in absolute
value by `n/4`, since it is a sum of tilted Bernoulli log mgfs. Its first
moment is zero and its variance is `nv+u^2c^2V`. Hence, for `h=u theta/(v sqrt R)`,

\[
 \log\mathbb E_0e^{h(M_R-R)}
 =\tfrac12h^2(2Rv+u^2c^2V)+O(n|h|^3)
 =u^2\theta^2/v+o(1).
\]

The logarithm of the tilted likelihood ratio is therefore the right side
of (2.5), with a deterministic `o(1)`. Its exponential is bounded away from
zero in `P_0` probability, by the count CLT. Equation (2.4) and Pinsker give

\[
 \mathbb E_0\left|\frac{p_{\theta/\sqrt R}}{p_0}
          -\frac{\widetilde p_{\theta/\sqrt R}}{p_0}\right|
 =2\,TV(P_{\theta/\sqrt R},\widetilde P_{\theta/\sqrt R})\to0.
\]

The difference divided by the tilted likelihood ratio thus converges to zero
in `P_0` probability; continuity of the logarithm proves (2.5). The argument
also holds for bounded convergent sequences of `theta`. At `u=0`, both laws
are the same fair product law and the expansion is identically zero.

The limiting information for the original shift on the `1/sqrt(R)` scale is
`2u^2/v=8u^2/(1-u^2c^2)`. This says that count contains the **leading local
parameter information**. It does not say that count contains the full
configuration entropy, nor that the spatial conditional entropy has favorable
curvature. In particular, one cannot infer entropy concavity from (2.5).

## 3. Applying the exact score decomposition to complete production

Return to the half-density aligned family and use the same notation as
`MESOSCOPIC_COMPENSATION.md`. This section proves its Theorem 3 for bounded
continuous tests and interval indicators without differentiating a limit.
It is a parallel author proof, not a claim of independent review.

At `delta=0`, put `g_delta(Y)=phi(q_delta(Y))F(X_R)`, where `Y` is the full
exterior word. The count test does not depend on `delta`. The exact finite
identity is

\[
 \partial_\delta^2\mathbb E_\delta g_\delta\big|_0
 =\mathbb E_0[a g_0+2s g'_0+g''_0].
 \tag{3.1}
\]

No term on the right is removed merely for having an inconvenient sign.
Let `gamma=(1-c)/2` and let `b` be the midpoint center-to-exterior row of
`c(T(p_R)-I/2)`. It has squared norm at most `c^2/4`. For the complete exterior
event matrix `A_delta`, the Schur formula reads

\[
 q_\delta=\tfrac12+u\delta-u^2 b^*A_\delta^{-1}b,
 \qquad A'_\delta=uI.
\]

Its exact derivatives are

\[
 q'_0=u+u^3 b^*A_0^{-2}b,
 \qquad q''_0=-2u^4 b^*A_0^{-3}b.
\]

The event matrix has inverse norm at most `1/gamma`. Consequently

\[
 |q'_0|\le uQ_1,\quad |q''_0|\le u^4Q_2,\qquad
 Q_1=1+\frac{c^2}{4\gamma^2},\quad Q_2=\frac{c^2}{2\gamma^3}.
\]

Define

\[
 L=2\left(\operatorname{atanh}c+\frac{c}{1-c^2}\right),\qquad
 B_\phi=\frac1{2\gamma^2(1-\gamma)^2},\qquad
 G_2=B_\phi Q_1^2+LQ_2.
\]

The all-word bounds on `phi`, its derivatives, and `q` imply

\[
 |g_0|\le M_cu^2\|F\|_\infty,
 \quad |g'_0|\le LQ_1u^2\|F\|_\infty,
 \quad |g''_0|\le G_2u^2\|F\|_\infty.
 \tag{3.2}
\]

Thus Theorem A bounds the difference between `A_{R,F}''(0)/R` and

\[
 \int_{1/N}^1\mathbb E_0\left[
 \phi(q_R)F(X_R)\frac{u^2}{v^2}(X_R^2-2v)\right]\frac{du}{u}
 \tag{3.3}
\]

by an explicit quantity tending to zero. To display a uniform majorant, set
`n=2R`, `V=mathcal V_R`, replace `v` by `v_*` and `u` by one in (1.2), and
call the resulting quantities `e_1^*,w_2^*,e_2^*`. Then `e_2(u)<=u^3 e_2^*`
and the integrated error is at most

\[
 \boxed{\quad
 \|F\|_\infty\left[
 \frac{M_c e_2^*}{5R}
 +\frac{2LQ_1}{3R}\sqrt{\frac{2R}{v_*}}
 +\frac{G_2}{2R}\right]
 =O_c\left(\sqrt{\frac{\log R}{R}}\right)\|F\|_\infty.
 \quad} \tag{3.4}
\]

The factors `1/5`, `1/3`, and `1/2` are the integrals of `u^4`, `u^2`,
and `u`, respectively. The small-noise factors therefore prevent an
artificial logarithmic divergence at zero.

The weighted CLT in the companion note also applies to tests `F(u,x)` whose
bounded-Lipschitz norm in `x` is uniformly bounded in `u`; its proof bounds
every replacement pointwise in `u` before an absolute integral. No continuity
in `u` is required. For truncated `x^2`, it therefore applies to the test in
(3.3). Removing that truncation is legitimate uniformly in `R`: the count is
Poisson-binomial, `Var M_R<=R/2`, and its fourth central moment is at most
`3(Var M_R)^2+Var M_R`. Hence

\[
 \mathbb E X_R^4\le3/4+1/(2R),\qquad
 \mathbb E[X_R^2 1_{|X_R|>L_0}]\le\frac{3/4+1/(2R)}{L_0^2}.
\]

The multiplier `phi(q_R)<=M_cu^2` and `v>=v_*` make this an integrable
uniform bound also in (3.3). Gaussian moments give the corresponding limit
bound. For interval indicators use bounded continuous upper and lower
approximations; the limiting weighted Gaussian density has no mass on the
endpoints, and the same moment bounds control tails.

The limit of (3.3) is accordingly

\[
 \int_0^1 I_0(u)\int F(x)\frac{u^2}{v^2}(x^2-2v)
                    \gamma_{2v}(x)\,dx\,\frac{du}{u}
 =4\int_0^1u I_0(u)\int F(x)\gamma_{2v}''(x)dx\,du.
\]

Since `2v=(1-u^2c^2)/2`, this is exactly Theorem 3 of the companion note.
The proof has accounted separately for score error, atom acceleration,
predictor derivatives, the moving exterior law, and every noise factor.

## 4. What these estimates do and do not pay

At fixed `c<1`, the defect `V=O(log R)` makes the normalized score error
vanish and makes the normalized acceleration error in (3.4) vanish. These
are full-law estimates on a growing fixed-density family. They explain why
a central count band has negative curvature of order `R` while its exterior
has the opposite order-`R` contribution, even though the complete order-`R`
term is zero.

Neither the `O(log R/R)` likelihood KL bound nor the score estimate bounds
the **sign** of the order-one entropy or production curvature. Relative
entropy closeness is not a curvature comparison; the exponential tilt is
not the actual affine kernel path. In fact finite Fourier diagnostics in the
candidate ledger show that the tilt's own entropy/production curvature can
have the opposite sign to the actual shift curvature. No such sign is
imported in the proof above.

The remaining obligation is the subleading complete signed aggregate. No
count-entropy replacement, projection assumption for a finite Toeplitz block,
or independent-review claim is made.
