DISPROVED_ROUTE_LEMMA

# S4: exact obstructions to two globally averaged localization closures

This document gives **complete scoped proofs**, supported by an **exact finite certificate**. It does not prove or disprove the sine-kernel target. The obstructions concern explicitly stated auxiliary curvature inequalities, not entropic independence or localization as general tools.

The new results are a positive *globally averaged Gaussian-localization completion excess* and a positive *globally averaged sparse-pinning entropy-contraction slack curvature*. They hold at fixed contrast `c=19/20`, on an explicit growing projection family of dimension `n=4m` and rank `k=2m`. Every compatible posterior has entropic-independence constant 1. Nevertheless, the normalized posterior first derivatives vanish exactly at the test point. The actual configuration-entropy Hessian there is negative.

All logarithms are natural. A prime denotes differentiation in the common offset `a`, holding `c`, the input law, and the auxiliary localization mechanism fixed. Entropy always means full configuration entropy, not count entropy or a matrix trace. Sources [A], [CE], and [JPV] are identified in `references.md`; the connecting calculations and obstructions below are proved here.

## 1. The exact entropy-functional conversion, before any inequality

Let `mu` be a fixed law on the `k`-subsets of `[n]`, with `1<=k<=n`. Write `x_A` for the indicator vector of `A`. Work in the legal interior `0<a<1-c`, with `0<c<1`. For an output configuration `y`, put

\[
 f_y(A)=\Pr_a(Y=y\mid X=A),\qquad
 p_y=\mu(f_y),\qquad
 \nu_y(A)=\frac{\mu(A)f_y(A)}{p_y}.
\]

All these likelihoods and output masses are positive. On the fixed support of `mu`, define

\[
 \operatorname{Ent}_\mu(f)
 =\mu(f\log f)-\mu(f)\log\mu(f),
 \qquad
 B(a)=(n-k)b(a)+k b(a+c).
\]

The first exact identity is

\[
 \boxed{H_\mu(a)=B(a)+\mathcal I(a),\qquad
 \mathcal I(a)=\sum_y\operatorname{Ent}_\mu(f_y)
             =\sum_y p_y D(\nu_y\Vert\mu)=I(X;Y).}
 \tag{1}
\]

Indeed, summing `mu(f_y log f_y)` over `y` gives `-H(Y|X)=-B`, and summing `-p_y log p_y` gives `H(Y)`. In particular, the entropy functional in (1) uses the **actual product-channel likelihood**, not an affine approximation to a configuration probability.

Let

\[
 s_y(A)=\partial_a\log f_y(A),\quad
 t_y(A)=\partial_a^2\log f_y(A),\quad
 g_y=p_y'/p_y=\nu_y(s_y),\quad
 v_y=s_y-g_y=\nu_y'/\nu_y.
\]

Twice differentiating the entropy functional gives

\[
 \left(\operatorname{Ent}_\mu(f_y)\right)''
 =\mu\!\left(f_y''\log\frac{f_y}{p_y}\right)
  +\mu\!\left(\frac{(f_y')^2}{f_y}\right)
  -\frac{(p_y')^2}{p_y}.
\]

Consequently, with

\[
 \begin{split}
 \mathcal A(a)&=\sum_y p_y\nu_y\!\left[(t_y+s_y^2)
                                      \log\frac{\nu_y}{\mu}\right],\\
 \mathcal E(a)&=\sum_y p_y\nu_y(v_y^2),
 \end{split}
\]

we obtain

\[
 \boxed{\mathcal I''=\mathcal A+\mathcal E,\qquad
 H_\mu''=B''+\mathcal A+\mathcal E,\qquad
 B''=-\frac{n-k}{a(1-a)}-\frac{k}{(a+c)(1-a-c)}.}
 \tag{2}
\]

This is also an exact conversion back to the supplied complete-entropy Hessian. The complete-data Fisher information is `-B''`; conditional variance gives

\[
 \mathcal E=-B''-\mathcal F_Y,\qquad
 \mathcal F_Y=\sum_y(p_y')^2/p_y.
\]

Furthermore, differentiating conditional entropy shows

\[
 \sum_y\mu(f_y''\log f_y)=0.
\]

For clarity, the last equality follows from
`B''=-sum_y mu(f_y'' log f_y)-sum_y mu((f_y')^2/f_y)`
and the equality of the second sum with `-B''`; the conditional product channel has affine one-bit success probabilities and independent conditional scores. Thus

\[
 \boxed{\mathcal A=-\sum_y p_y''\log p_y,\qquad
 H_\mu''=\mathcal A-\mathcal F_Y.}
 \tag{3}
\]

The unpaid acceleration term is therefore exactly the acceleration term of the desired Hessian. It has not been replaced by a different entropy or discarded.

### 1.1 All moving-reference and moving-weight derivatives

Here is a general identity useful when the reference itself is a previous posterior. Let `r_a,tau_a` be smooth positive probability laws on a common fixed finite support, and let `w_a>0` be a smooth branch weight. Set

\[
 L=\log(r/\tau),\quad v=r'/r,\quad z=r''/r,\quad
 u=\tau'/\tau,\quad j=\tau''/\tau,\quad
 g=w'/w,\quad h=w''/w.
\]

Then

\[
 \begin{split}
 D(r\Vert\tau)'&=E_r[vL-u],\\
 D(r\Vert\tau)''&=E_r[zL+(v-u)^2-j],\\
 \boxed{(wD(r\Vert\tau))''
 &=w\{hD(r\Vert\tau)+2gE_r[vL-u]
                  +E_r[zL+(v-u)^2-j]\}.}
 \end{split}
 \tag{4}
\]

In particular, (4) includes the reference-score cross term, the reference acceleration, `w''D`, and `2w'D'`. To verify it, differentiate `sum r log(r/tau)` twice, use `sum r'=sum r''=0`, and expand `(v-u)^2`. No sign is assigned to the terms involving `z`, `j`, or `h`.

For the channel posterior in (1), write `h_y=p_y''/p_y`. Its acceleration is

\[
 z_y=\nu_y''/\nu_y
     =v_y^2+t_y-\nu_y(t_y)-\operatorname{Var}_{\nu_y}(s_y),
\]

and `f_y''/f_y=h_y+2g_yv_y+z_y`. Therefore

\[
 \mathcal A=\sum_y p_y\left\{
 h_yD(\nu_y\Vert\mu)
 +2g_y\nu_y\!\left[v_y\log(\nu_y/\mu)\right]
 +\nu_y\!\left[z_y\log(\nu_y/\mu)\right]\right\}.
 \tag{5}
\]

This displays the output-weight acceleration and the posterior acceleration separately.

For an explicitly changing reference, reveal noisy coordinates in a fixed order and let
`nu_{j,a}=Law(X|Y_1,...,Y_j)`. The measures `nu_{j,a}` form a finite probability-valued martingale for each fixed `a`, and

\[
 \mathcal I(a)=\sum_{j=1}^n E_a D(\nu_{j,a}\Vert\nu_{j-1,a}).
 \tag{6}
\]

At each prefix in (6), use (4) with its actual prefix probability and its actual previous posterior. The exact script verifies (6), including both derivatives, at the nonstationary point `a=1/80,c=19/20`. This test deliberately does not use the midpoint where many first derivatives vanish.

## 2. Compatible DPP posteriors, exact constants, and the stationary-posterior point

### 2.1 The tilting formula

Suppose `mu=DPP(P)` for `P=UU*`, where `U*U=I_k`. For positive diagonal `D=diag(d_i)`, define

\[
 Z_D=\det(U^*DU),\qquad
 P_D=D^{1/2}U(U^*DU)^{-1}U^*D^{1/2}.
 \tag{7}
\]

`P_D` is a rank-`k` orthogonal projection, and its input-atom law is

\[
 \mu_D(A)=\frac{|\det U_A|^2\prod_{i\in A}d_i}{Z_D}.
 \tag{8}
\]

Proof: `V=D^{1/2}U(U*DU)^{-1/2}` has orthonormal columns; its squared minors give (8), and Cauchy--Binet gives their normalization. This is a change of law by an explicitly computed spatial external field, not an entropy-preserving arbitrary unitary change of basis.

For the full channel output, take

\[
 d_i=\begin{cases}(a+c)/a,&y_i=1,\\
 (1-a-c)/(1-a),&y_i=0.
 \end{cases}
\]

Then

\[
 p_y=a^{|y|}(1-a)^{n-|y|}\det(U^*D_yU),\qquad
 \nu_y=\operatorname{DPP}(P_{D_y}).
 \tag{9}
\]

For partially observed outputs, use the same weights at observed sites and weight 1 at unobserved sites. Positive latent pins reduce the remaining rank by one each; negative pins leave that remaining rank unchanged. The supplied conditional-projection formulas, iterated only on feasible branches, establish the corresponding projection laws. A fixed occupied pin and its output likelihood are not dropped from an entropy expression.

### 2.2 Entropic independence is exactly 1 under the required fields

For any projection law `pi`, let `q_i=Pr_pi(i in X)`. Its generating polynomial is

\[
 g_\pi(z)=\det(V^*\operatorname{diag}(z)V).
\]

The eigenvalue arithmetic--geometric mean inequality gives

\[
 g_\pi(z)^{1/k}\le \frac1k\operatorname{Tr}(V^*\operatorname{diag}(z)V)
                  =\sum_i\frac{q_i}{k}z_i.
 \tag{10}
\]

This is the `alpha=1` tangent criterion of [A, Theorem 4]. A direct proof of the needed KL statement avoids any reliance on an implicit conditional constant. For a law `eta<<pi`, write `r_i=Pr_eta(i in X)` and set `z_i=r_i/q_i` on positive coordinates, using limits if some `r_i=0`. The variational inequality for KL and (10) imply

\[
 D(\eta\Vert\pi)
 \ge\sum_i r_i\log(r_i/q_i)-\log g_\pi(z)
 \ge\sum_i r_i\log(r_i/q_i)
 =kD(m_\eta\Vert m_\pi).
 \tag{11}
\]

Thus all the projection posteriors and feasible residual projection laws used here have constant **1**, independently of rank, field strength, or small marginals.

The infinitesimal form of (11), with the compatible posterior as reference, is only

\[
 \sum_i\frac{(r_i')^2}{r_i}\le\sum_A\frac{(\nu_y'(A))^2}{\nu_y(A)}.
 \tag{12}
\]

It controls a quadratic first-derivative quantity; it does not control the acceleration in (5).

There is also strong quadratic entropic stability. For any projection law, its `0/1` covariance is a weighted graph Laplacian with edge weights `|P_ij|^2`. Hence

\[
 \operatorname{Cov}(X)\preceq
 2\operatorname{diag}(q_i(1-q_i))\preceq\tfrac12 I.
 \tag{13}
\]

The same inequality holds after every positive external field. Integrating the logarithmic moment-generating-function Hessian gives
`log E_pi exp(v.(X-E_pi X)) <= ||v||^2/4`.
Its variational consequence is

\[
 \|E_\eta X-E_\pi X\|_2^2\le D(\eta\Vert\pi).
 \tag{14}
\]

In the `0/1` coordinates used below, this is entropic stability with constant `1/2` for the functional `(1/2)||mean difference||^2`, in the convention of [CE, Definition 29 and Lemma 40]. The direct argument just given also avoids any issue with the covariance being singular on the homogeneous affine subspace.

### 2.3 A common-offset stationary posterior, not a stationary output law

For any fixed homogeneous input law, not necessarily a DPP, put

\[
 R(a)=\frac{(a+c)(1-a)}{a(1-a-c)},\quad
 \theta(a)=\log R(a),\quad h_y(A)=|A\cap y|.
\]

Homogeneity gives the exact formula

\[
 \nu_y(A)=\frac{\mu(A)e^{\theta h_y(A)}}{
                         \mu(e^{\theta h_y})}.
 \tag{15}
\]

At

\[
 a_*=(1-c)/2,\qquad u_*=(1+c)/2,
\]

we have

\[
 \theta'(a_*)=0,\qquad
 \theta''(a_*)=2(a_*^{-2}-u_*^{-2})>0,
\]

and therefore

\[
 \boxed{\nu_y'(a_*)=0,\qquad
 \nu_y''(a_*)=\theta''(a_*)
       (h_y-E_{\nu_y}h_y)\nu_y.}
 \tag{16}
\]

The output law is not stationary:

\[
 \frac{p_y'}{p_y}(a_*)=
 \frac{|y|-(na_*+ck)}{a_*u_*}.
 \tag{17}
\]

For example, with fixed reference `mu`,
`D(nu_y||mu)''=theta theta'' Var_nu_y(h_y)` at the midpoint. This can be positive even though (12) reads `0<=0`. We do not stop at this pointwise observation: the following results retain all output weights and average completely.

## 3. Exact stochastic localization and its full Hessian correction

Use isotropic Gaussian observation, in `0/1` coordinates:

\[
 X\sim\mu,\qquad Z_t=t x_X+B_t,
\]

where `B_t` is standard `n`-dimensional Brownian motion independent of `X`. Let

\[
 \pi_t=\operatorname{Law}(X\mid Z_s,0\le s\le t),\qquad q_t=E_{\pi_t}x_X.
\]

Bayes' formula makes `Z_t` sufficient and gives

\[
 \pi_t(A)\propto\mu(A)
 \exp\{Z_t\cdot x_A-t\|x_A\|^2/2\}
 \propto\mu(A)e^{Z_t\cdot x_A},
 \tag{18}
\]

because `||x_A||^2=k`. Thus every finite-time reference law is exactly the projection tilt (7), with `D=diag(exp Z_t)`. This particular isotropic localization is important: an arbitrary nondiagonal quadratic localization weight need not preserve the DPP family.

The process is a probability-valued martingale. With innovation Brownian motion
`bar B_t=Z_t-integral_0^t q_s ds`, its finite-state equations are

\[
 d\pi_t(A)=\pi_t(A)(x_A-q_t)\cdot d\bar B_t.
 \tag{19}
\]

These follow by differentiating the finite Bayes formula; the innovation has zero conditional drift and quadratic variation `tI`. Also `Z_t/t -> x_X` almost surely, so this is a full localization scheme when continued to infinity. Our stopping schedule is a deterministic time `T`, specified explicitly in Theorem G below.

For any fixed positive function `f`, set `M_t=pi_t(f)` and `pi_t^f=f pi_t/M_t`. From (19),

\[
 dM_t=M_t(E_{\pi_t^f}x_X-q_t)\cdot d\bar B_t.
\]

Applying Itô's formula to `pi_t(f log f)-M_t log M_t` gives the fixed-function entropy identity

\[
 d\operatorname{Ent}_{\pi_t}(f)
 =-\tfrac12\pi_t(f)\|E_{\pi_t^f}x_X-q_t\|^2dt+d\mathsf M_t.
 \tag{20}
\]

This is [CE, equation (27)], here rederived on the finite state space. The martingale has zero expected increment, since all functions involved are bounded on this finite support for a fixed legal interior `a`.

Now take the **actual** likelihood `f=f_y(a)`. Conditional on the Gaussian observation, write

\[
 p_{t,y}(a)=\pi_t(f_y(a)),\qquad
 \nu_{t,y,a}=\frac{f_y(a)\pi_t}{p_{t,y}(a)},\qquad
 r_{t,y}(a)=E_{\nu_{t,y,a}}x_X,
\]

and define the globally averaged Dirichlet/mean-displacement functional

\[
 \mathcal Q_t(a)=\frac12 E_{Z}\sum_y p_{t,y}(a)
                          \|r_{t,y}(a)-q_t\|^2.
 \tag{21}
\]

The outer Gaussian observation law is generated from the fixed input and is independent of `a`. The inner weights are exactly the actual conditional output law, not a substituted reference law.

Summing and integrating (20), then using (1), yields

\[
 \boxed{H_\mu(a)=E_Z H_{\pi_T}(a)+\int_0^T\mathcal Q_t(a)\,dt.}
 \tag{22}
\]

Equivalently the integral is `I(Y;Z_T)`. No pointwise conditional completion inequality has been used.

For `d=r_{t,y}-q_t`, all changing-output terms in its second derivative are

\[
 \boxed{\mathcal Q_t''=
 E_Z\sum_y\left\{
 \tfrac12p_{t,y}''\|d\|^2
 +2p_{t,y}'d\cdot r_{t,y}'
 +p_{t,y}(\|r_{t,y}'\|^2+d\cdot r_{t,y}'')\right\}.}
 \tag{23}
\]

Here `q_t'=q_t''=0` specifically because of the chosen `a`-independent Gaussian-reference coupling. For an `a`-dependent reference within a fixed outer coupling, use `d'=r'-q'` and `d''=r''-q''`. If the outer coupling law also moves, write its density as `w_a(z)` and the inner functional as `G_a(z)`: its second derivative is the integral of `w''G+2w'G'+wG''`, with none of these terms suppressed. Equation (4) gives the corresponding KL reference/weight derivatives. In (23), the conditional posterior derivatives themselves are the derivatives of the normalized Bayes law, including its normalizer.

On any compact interior interval, channel atoms are bounded uniformly below over all priors on this finite support. Derivatives in (22) can therefore pass through the Gaussian expectation and the finite-time integral. We obtain the exact Hessian identity

\[
 \boxed{H_\mu''(a)-E_Z H_{\pi_T}''(a)
       =\int_0^T\mathcal Q_t''(a)\,dt.}
 \tag{24}
\]

At the midpoint, (16) applies for every fixed Gaussian reference `pi_t`. Hence `r_{t,y}'=0` and the correction in (23) consists entirely of the output-weight acceleration and posterior acceleration. It is not a negative quadratic form.

## 4. Theorem G: a globally averaged Gaussian completion inequality is false

Let

\[
 U_0=\frac12\begin{pmatrix}1&1\\1&i\\1&-1\\1&-i\end{pmatrix},
 \qquad P_0=U_0U_0^*,\qquad
 P^{[m]}=\bigoplus_{b=1}^m P_0.
\]

Thus `P_0` is precisely the first-two-columns Fourier projection on four sites, and `P^[m]` has dimension `4m`, rank `2m`. Its input law is the product of `m` copies of the seed law. Fix

\[
 c=19/20,\qquad a_*=1/40,\qquad
 L=10813440000,\qquad
 T_0=\frac{1}{144L^2}
     =\frac{1}{16837989787238400000000}.
 \tag{25}
\]

Apply the isotropic Gaussian localization (18) to this product input, and denote its random projection at time `T` by `P_T^[m]`.

**Theorem G.** For every integer `m>=1` and every `0<T<=T_0`,

\[
 \boxed{
 H_{P^{[m]}}''(a_*)-E_Z H_{P_T^{[m]}}''(a_*)>2mT>0.}
 \tag{26}
\]

Nevertheless,

\[
 \boxed{\int_0^T E_Z\sum_y p_{t,y}(a_*)
           \sum_A\frac{(\partial_a\nu_{t,y,a}(A)|_{a_*})^2}
                        {\nu_{t,y,a_*}(A)}\,dt=0,}
 \tag{27}
\]

and the original, unlocalized entropy satisfies

\[
 -123m<H_{P^{[m]}}''(a_*)<-122m.
 \tag{28}
\]

This disproves both a nonpositive **globally averaged** Gaussian completion excess and its domination by any finite multiple of the integrated normalized-posterior Fisher energy in (27). It also rules out payment solely by any quadratic form of these zero posterior tangent vectors, including a down-up Dirichlet form of the normalized posterior score. It does **not** rule out functionals of the unnormalized likelihood, output scores, or posterior accelerations.

### Proof of Theorem G

#### G.1 Exact finite calculation at localization time zero

The seed input masses are `1/8` on the four cyclically adjacent pairs and `1/4` on the two opposite pairs. This follows directly from the squared minors of `U_0`; its columns are orthonormal. In particular the input is a genuine projection DPP and has full support on its six two-subsets.

For any prior `pi` on these six sets, define, at `a=a_*`,

\[
 p_y=\sum_A\pi(A)f_y(A),\qquad
 N_{i,y}=\sum_A\pi(A)x_{A,i}f_y(A),\qquad
 F(\pi)=\left.\partial_a^2\frac12\sum_y p_y
                 \|E[X\mid Y=y]-E_\pi X\|^2\right|_{a_*}.
\]

Because every normalized posterior has zero first derivative at the midpoint,

\[
 \boxed{F(\pi)=\sum_{i,y}
   \left\{\frac{N_{i,y}N_{i,y}''}{p_y}
          -\frac{N_{i,y}^2p_y''}{2p_y^2}\right\}.}
 \tag{29}
\]

For example, this follows by writing the mean-displacement functional as
`(1/2)sum_{i,y} N_{i,y}^2/p_y - (1/2)||E_pi X||^2`.
The normally present square
`(N_{i,y}'-N_{i,y}p_y'/p_y)^2/p_y`
is zero here, not omitted.

The following orbit table gives a small rational certificate for the seed. The last column is the contribution of **one** output in that class to the centered formula (23) at `t=0`. For this seed `q_i=1/2` and `k=2`, it equals the corresponding uncentered summand of (29) minus `p_y''/2`. This difference sums to zero over the complete output law, so the table still sums to `F(mu_0)`. Complements of singletons have the same entry. Probabilities have denominator `2560000=40^4`.

| Output class | Multiplicity | Probability numerator | `p_y''` | One-output centered contribution to (23) |
|---|---:|---:|---:|---:|
| empty or full | 2 | 1521 | `839/400` | `0` |
| singleton or triple | 8 | 29679 | `361/400` | `108300/579121` |
| cyclic adjacent pair | 4 | 290321 | `-761/400` | `39669712400/84286283041` |
| opposite pair | 2 | 579121 | `-761/400` | `0` |

All table entries follow by multiplying the four affine channel factors and differentiating the products. The exact certificate additionally records every individual output, every posterior jet, and every inclusion-marginal jet. Thus (29) can be checked without reconstructing any unstated measure.

The table gives

\[
 \begin{split}
 F(\mu_0)
 &=\frac{866400}{579121}
   +\frac{158678849600}{84286283041}\\
 &=\frac{164919889685924000}{48811956520986961},\\
 \frac{3378}{1000}&<F(\mu_0)<\frac{3379}{1000}.
 \end{split}
 \tag{30}
\]

The last comparison is an integer cross-multiplication, not a floating diagnostic. In particular `F(mu_0)>3`.

#### G.2 An explicit uniform continuity bound, not a guessed stopping time

For any prior on the six seed states, at the specified channel point every likelihood is at least

\[
 \varepsilon=40^{-4}=1/2560000.
\]

Every likelihood is at most 1 and its second derivative has absolute value at most `4*3=12`: the latter is the sum of the 12 ordered-pair derivatives of four affine factors, each remaining product bounded by 1.

For any two such priors `pi,pi_tilde`, along their line segment write `d_1=||pi-pi_tilde||_1`. Then

\[
 |dN|,|dp|\le d_1,\qquad |dN''|,|dp''|\le12d_1,
 \qquad 0\le N\le p,\quad p\ge\varepsilon.
\]

For one summand in (29), differentiation with respect to the prior yields the bounds

\[
 \left|d\frac{NN''}{p}\right|
 \le(24/\varepsilon+12)d_1,
 \qquad
 \left|d\frac{N^2p''}{2p^2}\right|
 \le(24/\varepsilon+6)d_1.
\]

There are `4*16=64` summands. Therefore

\[
 |F(\pi)-F(\widetilde\pi)|
 \le 64(48/\varepsilon+18)\|\pi-\widetilde\pi\|_1
 \le L\|\pi-\widetilde\pi\|_1,
 \quad L=4224\,40^4.
 \tag{31}
\]

This bound is deliberately conservative, but entirely explicit and independent of `m` because it is a one-block bound.

For one block, (19) and Itô isometry give, for each of its six states,

\[
 E(\pi_t(A)-\mu_0(A))^2
 =E\int_0^t\pi_s(A)^2\|x_A-q_s\|^2ds\le4t.
\]

Cauchy--Schwarz and summation imply

\[
 E\|\pi_t-\mu_0\|_1\le12\sqrt t.
 \tag{32}
\]

Combining (30)--(32), for `0<=t<=T_0`,

\[
 \mathcal Q_t''(a_*)=E F(\pi_t)
 \ge F(\mu_0)-12L\sqrt t
 \ge F(\mu_0)-1>2.
 \tag{33}
\]

Thus (24) gives a completion excess strictly greater than `2T` for one block. This step proves the sign at an explicitly positive stopping time; it does not infer a finite-time sign from a numerical derivative at zero.

#### G.3 Growing dimension and the sign of the actual Hessian

For `m` independent blocks, the Gaussian observations and their posteriors factor by block. The channel also factors. Configuration entropy, the averaged conditional entropy, and the correction (21) are additive. Therefore the completion excess is exactly `m` times the one-block excess. This proves (26) for every `m` at the same `T_0`.

Equation (16), applied to every Gaussian reference of rank `2m`, proves (27) exactly.

Finally, the seed output table gives

\[
 H_{P_0}''(a_*)=-\frac{6400}{39}
 +\frac{761}{100}\log290321
 +\frac{39}{100}\log761
 -\frac{1561}{100}\log39.
 \tag{34}
\]

The rational logarithm enclosures in Section 6 prove `-123<H_{P_0}''<-122`. Additivity proves (28). This completes the proof of Theorem G.

The same calculation directly obstructs a tangent-only bound for the unpaid term of the original Hessian, not just a localization remainder. At the seed,

\[
 \mathcal E=0,\qquad \mathcal F_Y=\frac{6400}{39},\qquad
 \frac{41123540034652}{10^{12}}
 <\mathcal A=H_{P_0}''+\frac{6400}{39}
 <\frac{41123540034653}{10^{12}}.
\]

Thus `A<=C E` is false for every finite `C`. All three quantities add over independent blocks. The negative actual Hessian comes from the larger output Fisher term, which is not available in a bound using only the zero normalized-posterior tangent energy. The displayed strict enclosure follows from the exact logarithm-series bounds; using non-strict endpoints instead would also suffice for the conclusion.


## 5. Theorem S: sparse localization does not remove the averaged curvature slack

Here the localization object and stopping schedule are discrete and explicitly sparse. Given `X~mu`, choose a uniform random ordering of its `k` occupied sites. Let `J_j` be the set of the first `j` sites and let

\[
 \mu_{J_j}=\operatorname{Law}(X\mid J_j).
\]

Use the filtration generated by the revealed ordered occupied sites. Conditional on their set, the order carries no further information about `X`, so the displayed law is also the posterior for this filtration. It is a probability-valued martingale on the full input state space, ending in a point mass at `j=k`. Stop at a deterministic `ell` with `1<=ell<=k`; only occupied coordinates have been pinned. After `j` pins the remaining projection has rank `k-j`. The likelihood remains the entire `f_y` on the full output space.

Let `pi_ell=Law(J_ell)=mu D_{k->ell}` and

\[
 (T_\ell f)(J)=E_\mu[f(X)\mid J\subseteq X].
\]

The precise entropy decomposition is

\[
 \operatorname{Ent}_\mu(f)
 =\operatorname{Ent}_{\pi_\ell}(T_\ell f)
  +E_{J_\ell}\operatorname{Ent}_{\mu_{J_\ell}}(f).
 \tag{35}
\]

At each feasible step `j`, (11) for the remaining rank `k-j` law bounds the entropy loss by `1/(k-j)` times its current entropy. Multiplying the factors
`(k-j-1)/(k-j)` gives

\[
 \operatorname{Ent}_{\pi_\ell}(T_\ell f)
 \le\frac\ell k\operatorname{Ent}_\mu(f).
 \tag{36}
\]

For `ell<k`, this is the `alpha=1` down-contraction in [A, Theorem 5], with its needed link hypotheses explicitly established above; the case `ell=k` is the trivial identity. It is an entropy-value inequality for fixed `f`, not a curvature statement.

Averaging (35)--(36) over the actual likelihoods `f_y(a)`, define

\[
 I_\ell(a)=I(J_\ell;Y),\qquad
 \Phi_\ell(a)=I(X;Y)-\frac{k}{\ell}I_\ell(a)\ge0.
\]

The exact Hessian identity is

\[
 \boxed{H_\mu''=B''+\frac{k}{\ell}I_\ell''+\Phi_\ell''.}
 \tag{37}
\]

Equivalently,

\[
 \Phi_\ell=
 \sum_y p_y\left\{
 D(\nu_y\Vert\mu)-\frac{k}{\ell}
 D(\nu_yD_{k\to\ell}\Vert\mu D_{k\to\ell})\right\}.
 \tag{38}
\]

Thus (38) is an average under the actual output law of its compatible posterior. Differentiating it requires (4), not simply the Hessian of one divergence. Its tangent Fisher inequality is

\[
 \frac{k}{\ell}\mathcal E_\ell\le\mathcal E,
\quad
 \mathcal E_\ell=\sum_y p_y\sum_J
 \frac{(\partial_a(\nu_yD_{k\to\ell})(J))^2}
      {(\nu_yD_{k\to\ell})(J)}.
 \tag{39}
\]

Both sides of (39) vanish at the midpoint.

**Theorem S.** On the same family `P^[m]`, at `c=19/20,a=1/40`, choose the stopping schedule

\[
 n=4m,\quad k=2m,\quad \ell=m=n/4.
\]

Then all paths use at most one quarter of the coordinates as occupied pins, but

\[
 \boxed{\Phi_m''(a_*)
 =\frac{m^2}{2m-1}\,\delta_0
 >\frac{3m^2}{2m-1}>\frac38n,}
 \tag{40}
\]

where

\[
 \delta_0=\frac1{100}\left(
 741\log39+780\log381+20\log1141+361\log761-761\log290321
 \right),
 \quad 3.1355<\delta_0<3.1356.
 \tag{41}
\]

Consequently, the unpaid slack curvature cannot be bounded above by zero, by a finite multiple of `E`, or by a finite multiple of the nonnegative Fisher deficit in (39).

### Proof of Theorem S

For the seed let `J_1` be a single uniformly selected occupied site, and put

\[
 \Delta(a)=I(X;Y)-2I(J_1;Y).
\]

All site inclusion probabilities are `1/2`. Conditioning on a fixed occupied site leaves a three-site rank-one law with weights `(1/4,1/2,1/4)`, and the pinned site's output has entropy `b(a+c)`. Write `H_4` for the seed output entropy and `H_3` for that remaining three-site output entropy. The entropy chain rule gives

\[
 2I(J_1;Y)=2H_4-2[b(a+c)+H_3],
\]

and therefore

\[
 \boxed{\Delta''=-H_4''+2H_3''-2b''(a).}
 \tag{42}
\]

The pinned site's output factor has been retained in the first equality before its exact cancellation in (42).

For completeness, the eight conditional three-site output jets `(p,p',p'')` at the test point are:

| Output mask on three sites | `p` | `p'` | `p''` |
|---:|---:|---:|---:|
| 0 | `1521/64000` | `-1599/1600` | `79/20` |
| 1 | `14859/64000` | `-381/1600` | `-39/20` |
| 2 | `29679/64000` | `-761/1600` | `-39/20` |
| 3 | `1141/64000` | `1141/1600` | `-1/20` |
| 4 | `14859/64000` | `-381/1600` | `-39/20` |
| 5 | `761/64000` | `761/1600` | `-1/20` |
| 6 | `1141/64000` | `1141/1600` | `-1/20` |
| 7 | `39/64000` | `79/1600` | `41/20` |

Substitution into the complete entropy Hessian and (42) gives exactly (41). The logarithm bounds in Section 6 prove its sign.

There is also an explicit audit of the moving-output terms. For
`Delta_y=D(nu_y||mu)-2D(m_nu_y||m_mu)`, the mixed term is exactly zero, while the following are rational enclosures, with common denominator `10^12`:

\[
 \begin{array}{rcl}
 \sum_y p_y''\Delta_y
 &\in&[-3701368164138,-3701368164137]/10^{12},\\
 2\sum_y p_y'\Delta_y'&=&0,\\
 \sum_y p_y\Delta_y''
 &\in&[6836923258629,6836923258630]/10^{12},\\
 \Delta''
 &\in&[3135555094492,3135555094493]/10^{12}.
 \end{array}
 \tag{43}
\]

Thus actual output-weight acceleration does compensate part of the positive internal term, but the **net global average is positive**. The certificate is not a claim that each branch has the same sign.

For the growing family, let `K_b=|J_ell intersect block b|`. These block counts are independent of `(X,Y)`, since each block has exactly two occupied sites. With total rank `k=2m`,

\[
 \Pr(K_b=1)=\frac{2\ell(k-\ell)}{k(k-1)},\qquad
 \Pr(K_b=2)=\frac{\ell(\ell-1)}{k(k-1)}.
\]

Conditional on these counts, the selected subsets and channels factor by block. Therefore, for every legal interior `a,c`, not just the test point,

\[
 I_\ell^{[m]}
 =m\left\{\frac{2\ell(k-\ell)}{k(k-1)}I_1^{[1]}
          +\frac{\ell(\ell-1)}{k(k-1)}I(X^{[1]};Y^{[1]})\right\}.
\]

Since `I(X^[m];Y^[m])=m I(X^[1];Y^[1])`,

\[
 \boxed{\Phi_\ell^{[m]}(a)
       =m\frac{k-\ell}{k-1}\Delta(a).}
 \tag{44}
\]

Setting `ell=m` and using (41) proves (40). Equation (16) proves that both energies in (39) are zero. This completes the proof.

### 5.1 Checking the sparse-localization hypotheses rather than assuming them

Use sparse fraction `s=1/4`, distinct from channel contrast `c`. In the convention of [JPV, Definitions 3.1--3.2], the influence matrix on active coordinates is

\[
 \Psi=\operatorname{Cov}(X)\operatorname{diag}(\operatorname{Var}X_i)^{-1}.
\]

For the growing block family, after any feasible signed pinning of at most `ceil(sn)=m` coordinates and after any positive external field, the law still factors into blocks of at most four active coordinates. Every influence entry is a conditional-probability difference in `[-1,1]`. Each block's Frobenius norm, and hence its operator norm, is at most 4. The full matrix is block diagonal, so

\[
 \|\Psi\|_{\rm op}\le4
 \tag{45}
\]

for every pinning in the required sparse family, uniformly in `m`. This verifies the actual **operator norm**, not merely a spectral radius or a correlation-matrix bound.

Accordingly [JPV, Theorem 1.5] gives the `+/-1` mean bound with constant `8*4/(1/4)=128`. For the original input, the nonzero inclusion marginals have lower bound `b=1/2`. For its actual full-output posteriors at the test point one may use

\[
 b\ge\frac1{2\,39^4}.
\]

Indeed within a block the maximum/minimum likelihood ratio is at most `39^4`, and each prior inclusion probability is `1/2`. Thus [JPV, Theorem 1.2] gives respectively the dimension-independent but weaker constants `64` and `64*39^4=148060224`. The determinant argument (11) gives the sharper constant 1.

The last marginal lower bound is **not** asserted uniformly along arbitrary Gaussian external fields; Gaussian fields are unbounded. Along that localization, the proofs use (11) and (14), which do hold uniformly under the actual fields, not a fictitious uniform marginal lower bound. No sparse hypothesis for the increasing-size contiguous Fourier projections is claimed here.

## 6. Exact certification and reproducibility

The seed calculation uses only six input atoms and the full product likelihood. `scripts/exact_certificate.py` uses `fractions.Fraction` for every probability, derivative, and Gaussian integrand calculation. Its entropy expressions are rational linear combinations of logarithms of primes. The following identities are checked algebraically, not by a numerical tolerance:

- the input squared minors and normalization;
- the vanishing of every terminal posterior first derivative;
- the entropy/Fisher/acceleration conversion (2);
- the conditional-entropy formula (42);
- every output-weight term in (43);
- the noisy-coordinate moving-reference identity (6), through second order, at a nonmidpoint parameter;
- two separate rational formulas for (30).

The logarithms are enclosed using, after reduction to `1<=x<=2`,

\[
 z=(x-1)/(x+1),\qquad
 \log x=2\sum_{j=0}^{N-1}\frac{z^{2j+1}}{2j+1}+R_N,
 \quad 0\le R_N\le\frac{2z^{2N+1}}{(2N+1)(1-z^2)}.
 \tag{46}
\]

The script uses `N=40`, exact powers-of-two range reduction, and outward rational rounding. The following convenient enclosures have denominator `10^12`; each row means that the logarithm lies between the two displayed numerators divided by that denominator.

| Argument | Lower numerator | Upper numerator |
|---:|---:|---:|
| 39 | 3663561646129 | 3663561646130 |
| 381 | 5942799375126 | 5942799375127 |
| 1141 | 7039660349862 | 7039660349863 |
| 761 | 6634633357861 | 6634633357862 |
| 290321 | 12578742486356 | 12578742486357 |

These enclosures alone prove the strict signs in (34) and (41). The machine-readable exact certificate contains tighter combined enclosures and all atom jets.

The Brownian finite-time result is **an analytical proof using the exact finite calculation plus the explicit modulus (31)--(33)**. It is not an alleged exact enumeration of a continuous distribution. The growing-family and sparse-pinning extensions are analytical tensorization proofs, not evidence from a bounded list of dimensions.

Optional numerical diagnostics check the posterior matrix formula and the `m=2` sparse-pinning tensorization against separate direct enumeration. They are explicitly labeled **floating diagnostics**, and no theorem depends on them. No tiny-time Monte Carlo, finite-difference Hessian, or cancellation-prone subtraction is used to establish (26).

## 7. Exact scope and remaining gap

The precise false closures are:

\[
 H_P''-E H_{P_T}''\le0,
 \qquad
 H_P''-E H_{P_T}''\le C\int_0^T E_{Z,Y}
                      \|\partial_a\nu_{t,Y}\|_{\nu_{t,Y}^{-1}}^2dt,
\]

for the specified isotropic Gaussian scheme, and

\[
 \Phi_\ell''\le0,
 \qquad \Phi_\ell''\le C\mathcal E,
 \qquad \Phi_\ell''\le C(\mathcal E-(k/\ell)\mathcal E_\ell),
\]

for the specified sparse occupied-pinning scheme. Every finite coefficient fails at the certified point, because the relevant normalized-posterior tangent energies are zero and the corrections are strictly positive.

The newly exhibited mechanism is acceleration with a stationary normalized posterior: a common-offset perturbation has nonzero second-order likelihood and output-weight effects even when the entropy-contraction tangent functional vanishes. The stochastic obstruction is a **global average over the entire Gaussian localization law and the compatible actual output law**. The sparse obstruction pins a linear number of sites and also retains the complete output average. Neither result repeats or assumes the supplied branchwise completion inequality (C).

This does not contradict any fixed-function entropy-conservation theorem in [A], [CE], or [JPV]. Those theorems remain applicable; it is the additional common-offset curvature closure that fails. Nor does it exclude a different averaged estimate retaining posterior acceleration, output Fisher information, or a different localization schedule.

The family has growing rank and fixed density `1/2`, but it is a block-direct-sum family. Except for its four-site seed, it is **not** the contiguous Fourier projection `P_{n,k}` from the target. The supplied sublinear Fourier--Toeplitz bridge therefore cannot transfer these statements to the sine process. No entropy-rate Hessian, thermodynamic Jensen sign, or concavity conclusion for fixed-density contiguous Fourier projections has been established.

The actual entropy Hessian in the certificate is strictly negative, as (28) emphasizes. The supplied Fourier endpoint obstruction to (C) remains fully consistent with this separate midpoint, continuous-localization obstruction. In fact, at this seed and midpoint every coordinate completion excess from (C) is negative: complement symmetry gives equal second derivatives for the two three-site conditional laws, and (42) yields

\[
 R_{P_0}=H_4''-H_3''
 =\tfrac12(H_4''-\delta_0+3200/39)\in(-23,-21).
\]

Thus the positive Gaussian averaged completion excess is not obtained by simply reusing a bad first coordinate at the same seed and channel point. Signed compensation involving additional curvature terms remains open. There are no conjectural steps in Theorems G and S; the sine target and more general compensation strategies remain unresolved.
