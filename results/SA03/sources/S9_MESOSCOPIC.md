> **待独立对抗性审查 / PENDING_INDEPENDENT_REVIEW。** 下文保留来源原文；其中 PROVED、PASS、AUDIT 等是作者或既有记录的表述，不代表本次 SA 成果已独立通过。先读本包根目录 REVIEW_REQUEST.md；外部审计与其他 SA 分开进行。

# Critical-scale signed compensation for the complete production law

**Author theorem, subject to independent review.** This is a scoped structural
compensation result, not a proof of sine entropy-rate concavity. In particular,
no assertion below signs the order-one remainder of the complete production
curvature. The distinction is quantified in Section 9.

## 1. Frozen statement and the actual law

Fix a contrast `0<c<1`, density `rho=1/2`, and the frequency interval
`E=[-1/4,1/4]` on the circle of total mass one. Let `R` tend to infinity through
odd positive integers, put `N=R+1`, and let `p_R=F_R*1_E`, where `F_R` is the
Fejer kernel of degree `R`. Thus both the degree and the conditioning radius
are exactly `R`. The center shift is `a_*=(1-c)/2`.

Write `u=exp(-s)`. At an original shift displacement `delta`, the symbol is

\[
 f_{R,u,\delta}=\tfrac12+u\{c(p_R-\tfrac12)+\delta\}.
\]

All probabilities below are those of this symbol's genuine stationary DPP.
Let `C_R=[-R,R]\\{0}`, let `M_R=sum_{i in C_R}Y_i`, and put

\[
 q_R=\Pr(Y_0=1\mid Y_{C_R}),\qquad
 \phi(q)=(q-\tfrac12)\log\frac q{1-q},\qquad
 X_R=\frac{M_R-R}{\sqrt R}.
\]

The production uses every occupied/vacant word and its actual probability.
For bounded Borel `F`, define

\[
 A_{R,F}(\delta)=\int_{1/N}^1
    \mathbb E_{R,u,\delta}[\phi(q_R)F(X_R)]\,\frac{du}{u},
 \qquad
 \mu_R^\theta(F)=A_{R,F}(\theta/\sqrt R).
 \tag{1.1}
\]

In particular `A_{R,1}=log 2-J_R` for precisely the assigned truncated
functional. It is not `log 2-H_{2R+1}/(2R+1)`.

Let `I_0(u)` be the **full two-sided** production of the true, unregularized
sine symbol `1/2+uc(1_E-1/2)`, not its count entropy. Set

\[
 v(u)=\frac{1-c^2u^2}{2},\qquad
 v_{\min}=\frac{1-c^2}{2}>0,\qquad
 \gamma_v(x)=\frac{e^{-x^2/(2v)}}{\sqrt{2\pi v}}.
\]

The reviewed noise identity and the one-neighbor calculation give

\[
 \int_0^1 I_0(u)\frac{du}{u}
 =D_0:=\log2-h_{1/2}(a_*,c),
 \qquad
 16u^4(c/\pi)^4\le I_0(u)\le M_cu^2,
 \quad M_c=c\operatorname{atanh}c.
 \tag{1.2}
\]

The lower bound is also rederived in Section 7. None of the statements below
assumes a sign for an unknown entropy Jensen deficit.

### Theorem 1: weighted Gaussian limit, uniformly on compact shift scales

For every fixed `T<infinity`, the finite positive measures `mu_R^theta`,
`|theta|<=T`, converge in bounded-Lipschitz distance, uniformly in `theta`, to

\[
 \boxed{\quad
 \mu^\theta(dx)=\int_0^1 I_0(u)
               \gamma_{v(u)}(x-2u\theta)\,\frac{du}{u}\,dx.
 \quad} \tag{1.3}
\]

An explicit uniform error is proved in Section 5. With the local radius
`r=floor(R^(1/3))`, it is `O_{c,T}(R^(-1/6)sqrt(log R))`.
The theorem concerns the production-weighted **complete law**, not just a
central limit theorem for the unweighted particle count.

### Theorem 2: exact leading signed compensation

For fixed real `theta`, put

\[
 \nu_R^\theta=\tfrac12(\mu_R^\theta+\mu_R^{-\theta})-\mu_R^0.
\]

Then `nu_R^theta` converges weakly to the signed measure

\[
 \boxed{\quad
 \nu^\theta(dx)=\int_0^1 I_0(u)
 \left[\frac{\gamma_{v(u)}(x-2u\theta)+\gamma_{v(u)}(x+2u\theta)}2
              -\gamma_{v(u)}(x)\right]\frac{du}{u}\,dx.
 \quad} \tag{1.4}
\]

Its total mass is exactly zero. If `theta!=0` and `b>0`,

\[
 \nu^\theta([-b,b])<0,
 \qquad
 \nu^\theta(\mathbb R\setminus[-b,b])=-\nu^\theta([-b,b])>0.
 \tag{1.5}
\]

Moreover the first, positive measure in (1.4) is a mean-preserving spread of
`mu^0`: a concrete martingale coupling is given in Section 6. Its quadratic
transport cost is

\[
 4\theta^2\int_0^1u I_0(u)\,du,
 \quad
 \frac{32}{3}\theta^2(c/\pi)^4
 \le 4\theta^2\int_0^1u I_0(u)du\le M_c\theta^2.
 \tag{1.6}
\]

This is the cost of the specified coupling, not a claim of optimal Wasserstein
cost. No total-variation-distance convergence of finite grid measures to
continuous measures is asserted.

### Theorem 3: midpoint curvature of the positive and negative bands

For every bounded continuous `F`, and also for indicators of finite intervals,

\[
 \boxed{\quad
 \frac{A_{R,F}''(0)}R\longrightarrow
 \int_{\mathbb R}F(x)\,\eta_c(dx),\qquad
 \eta_c(dx)=4\int_0^1u I_0(u)\gamma_{v(u)}''(x)du\,dx.
 \quad} \tag{1.7}
\]

In fact all fixed derivative orders follow from the complex-parameter argument
in Section 8, with scaling `R^(-k/2)`. This is **not** obtained by differentiating
the real value error in Theorem 1.

For `B_R(b)={|M_R-R|<=b sqrt(R)}`, write `A_{R,B}` for (1.1) with
`F=1_{[-b,b]}` and `A_{R,B^c}=A_{R,1}-A_{R,B}`. Then

\[
 \frac{A_{R,B}''(0)}R\longrightarrow-C_b(c),\qquad
 \frac{A_{R,B^c}''(0)}R\longrightarrow+C_b(c),\qquad
 \frac{A_{R,1}''(0)}R\longrightarrow0,
 \tag{1.8}
\]

where

\[
 C_b(c)=8b\int_0^1u I_0(u)\frac{\gamma_{v(u)}(b)}{v(u)}du>0.
 \tag{1.9}
\]

For the assignment's fixed contrast `c=19/20` and `b=1/2`,

\[
 C_{1/2}(19/20)>\frac1{140}.
 \tag{1.10}
\]

Consequently, for all sufficiently large odd `R`, the central band's actual
midpoint curvature is `<-R/140`, and the complement's curvature is `>R/140`.
The existence of the threshold is proved; no numerical threshold for this new
assertion is claimed. In particular the earlier `160001` threshold belongs to
a different, fixed-chord theorem and is not reused here.

## 2. Uniform all-word bounds and the conditional count comparison

Fix `T`, and suppose `R>=(4T/(1-c))^2`. Set

\[
 \epsilon=\frac{1-c}{4},\quad D=\frac{1+c}{2}<1,\quad
 M_D=D\operatorname{atanh}D,
 \quad
 L_D=2\left(\operatorname{atanh}D+\frac{D}{1-D^2}\right).
 \tag{2.1}
\]

Every real kernel with `|delta|<=T/sqrt(R)` has spectrum in
`[epsilon,1-epsilon]`. Its binary-channel representation gives, for every
complete finite or infinite exterior conditioning event,

\[
 |2q-1|\le uD,\qquad 0\le\phi(q)\le M_Du^2,
 \qquad |\phi'(q)|\le uL_D.
 \tag{2.2}
\]

For the derivative bound, use `z=2q-1` and
`phi'(q)=2[atanh(z)+z/(1-z^2)]`; convexity of `atanh` at zero gives the factor
`u`. These bounds do not discard low-probability exterior words.

Let `Q_R` now denote the restriction of `T(p_R)` to the exterior `C_R` and put
`V_R=Tr Q_R(I-Q_R)`. Since its diagonal is `1/2`, direct expansion gives

\[
 \mathbb E M_R=R+2u\theta\sqrt R,
 \qquad
 \operatorname{Var}M_R
 =Rv(u)+u^2c^2V_R-2u^2\theta^2
 \quad(\delta=\theta/\sqrt R).
 \tag{2.3}
\]

This is a trace identity for a count. It is not a diagonalization of the
complete configuration law.

Here is a uniform defect bound. Write

\[
 \eta_R=\min\{1/2,(\log N+1/2)/N\},\quad
 \mathcal V_R=(2R+1)\eta_R+\frac{2\mathsf H_R}{\pi^2}+\frac14.
 \tag{2.4}
\]

For clarity, the interval Fejer estimate used here is valid at every fixed
interval density. On the normalized circle, translations satisfy
`||1_E(. - t)-1_E||_1<=2|t|`, while
`F_R(t)<=min(N,1/(4Nt^2))` for `0<|t|<=1/2`. Splitting the integral at
`1/(2N)` gives

\[
 \|p_R-1_E\|_1
 \le4\int_0^{1/2}tF_R(t)dt
 \le(\log N+1/2)/N.
\]

Also `||p_R-1_E||_1=2rho-2 int 1_E p_R<=2rho(1-rho)<=1/2`, because the
nonnegative Fejer Fourier multipliers imply `int 1_E p_R>=rho^2`. This
proves the minimum in (2.4) without an endpoint-strip assumption.

Then `V_R<=mathcal V_R=O(log R)`. Indeed, on the contiguous block of length
`n=2R+1`, Parseval and the Toeplitz trace formula give

\[
 \operatorname{Tr}Q_n(I-Q_n)
 =n\int p_R(1-p_R)+2\sum_{k\ge1}\min(k,n)|\widehat p_R(k)|^2.
\]

Pointwise `p_R(1-p_R)<=|p_R-1_E|`, whose integral is at most `eta_R`.
The remaining sum is at most `2 H_R/pi^2`, since the coefficients vanish
above `R` and `|p_hat_R(k)|<=1/(pi k)`. Removing the center changes the count
variance by at most `1/4`: for a contraction split into a singleton and its
complement, the cross-row squared norm is at most the singleton variance.
This proves (2.4).

Choose a local exterior `S=C_r`, `1<=r<=R`, of size `s=2r`, and condition on an
arbitrary complete word `w` there. The conditional law on `C_R\\S` is a DPP
with a Hermitian contraction kernel `L_w`. Conditioning on one occupied or
vacant site is a rank-one kernel update. Iteration, or the complete-event
Schur formula, shows

\[
 \operatorname{rank}(L_w-K_{C_R\setminus S})\le s,
 \qquad
 \|L_w-K_{C_R\setminus S}\|_1\le s.
 \tag{2.5}
\]

The second assertion uses that both matrices are contractions, so their
self-adjoint difference has norm at most one. It follows that

\[
 |\mathbb E(M_R\mid w)-\mathbb EM_R|\le2s,
 \qquad
 |\operatorname{Var}(M_R\mid w)-\operatorname{Var}M_R|\le5s/4.
 \tag{2.6}
\]

For the variance assertion, first compare the two kernels on the complement.
For contractions `L,K`,

\[
 \operatorname{Tr}(L-L^2-K+K^2)
 =\operatorname{Tr}[(L-K)(I-L-K)],
 \qquad \|I-L-K\|\le1.
\]

Thus that comparison costs at most `s`. Removing the local block from the
unconditioned count costs at most `s/4`: writing the kernel in blocks gives
`Var(M_R)-Var(M_{C_R\\S})=Var(M_S)-2||K_{S,C_R\\S}||_HS^2`, and
`0<=||K_{S,C_R\\S}||_HS^2<=Var(M_S)<=s/4`.
The mean estimate is the sum of two terms bounded by `s`: the observed local
count minus its mean and the trace change in (2.5). All bounds hold for every
word, not merely with high probability.

## 3. A conditional Gaussian estimate with elementary constants

A finite DPP count has generating function

\[
 \mathbb E z^M=\det(I+(z-1)K)
             =\prod_j(1-\lambda_j+\lambda_j z).
 \tag{3.1}
\]

Consequently it is distributed as a sum of independent Bernoulli variables.
Only this scalar count representation is used. Applying it to `L_w`, there
are at most `2R` Bernoulli summands after conditioning.

We record an elementary Lindeberg bound, rather than assuming a CLT transfers
unchanged to production weights. If `F` is one-Lipschitz, let
`F_h(x)=E F(x+hG)` for a standard Gaussian `G`. Then

\[
 \|F_h-F\|_\infty\le h,
 \qquad \|F_h'''\|_\infty\le2/h^2.
\]

The latter follows by differentiating the Gaussian convolution of the bounded
almost-everywhere derivative of `F` twice and using `E|G^2-1|<=2`.
Replace each centered Bernoulli summand by an independent Gaussian with the
same variance. Their first two moments agree. For a Bernoulli with variance
`sigma^2<=1/4`, its centered third absolute moment is at most `sigma^2`, and
the corresponding Gaussian's is also at most `sigma^2` since
`E|G|^3<2` and `sigma<=1/2`. The sum of the two moments is at most `1/2`.
Taylor's formula, after division by `sqrt(R)`, therefore costs at most

\[
 \frac1{3h^2\sqrt R}.
\]

Both smoothing errors cost at most `2h`. With `h=R^(-1/6)`, the total is at
most `(7/3)R^(-1/6)`. This bound is uniform even if some Bernoulli variances
vanish.

Comparing the resulting normal distribution to `N(2u theta,v(u))`, (2.3) and
(2.6), with the same standard Gaussian coupling, now give

\[
 \left|\mathbb E[F(X_R)\mid w]
       -\int F(x)\gamma_{v(u)}(x-2u\theta)dx\right|
 \le\mathcal B_{R,r},
 \tag{3.2}
\]

where, for `Lip(F)<=1`,

\[
 \boxed{\quad
 \mathcal B_{R,r}=
 \frac73R^{-1/6}+\frac{4r}{\sqrt R}
 +\frac{c^2\mathcal V_R+2T^2+(5/2)r}{R\sqrt{v_{\min}}}.
 \quad} \tag{3.3}
\]

For the standard-deviation comparison we used
`|sqrt(x)-sqrt(v)|<=|x-v|/sqrt(v_min)` for `x>=0` and `v>=v_min`.
The same estimate therefore covers degenerate conditional count variances.

## 4. Replacing the full predictor by a local predictor without losing weights

Let `q_r=Pr(Y_0=1|Y_{C_r})` under the same, radius-`R` Fejer kernel. This is
not the predictor for the degree-`r` kernel. Conditional expectation gives
`q_r=E(q_R|Y_{C_r})`. Since `phi''>=8`, the Bregman remainder satisfies

\[
 \mathbb E(q_R-q_r)^2\le\frac{I_R-I_r}{4}.
 \tag{4.1}
\]

The reviewed integrated localization theorem, applied to this one stationary
process, and its strict-strip Fourier block bound imply

\[
 \int_0^1(I_R-I_r)\frac{du}{u}
 \le E_{r+1},\qquad
 E_n=\frac{c^2(\mathsf H_n+1)}{\pi^2\epsilon(1-\epsilon)n}.
 \tag{4.2}
\]

The block length here is `r+1`, not `2r+1`. The nonzero Fourier coefficients
of every Fejer approximation are bounded in magnitude by those of the true
interval, which makes the bound independent of `R`.

From (2.2), (4.1), and Cauchy--Schwarz,

\[
 \int_0^1\mathbb E|\phi(q_R)-\phi(q_r)|\frac{du}{u}
 \le\frac{L_D}{2}\int_0^1\sqrt{I_R-I_r}\,du
 \le\frac{L_D}{2\sqrt2}\sqrt{E_{r+1}}.
 \tag{4.3}
\]

This controls the replacement even after multiplication by any `|F|<=1`.
It does not assert independence of the full predictor and the exterior count.

Now `phi(q_r)` is measurable with respect to `Y_{C_r}` and is nonnegative.
Multiplying the all-word estimate (3.2) by this actual weight and averaging
therefore costs at most `M_D u^2 mathcal B_{R,r}`. Integrating costs at most
`(M_D/2)mathcal B_{R,r}`. This is the essential new step connecting local
complete production to the count CLT.

## 5. Kernel changes, noise tails, and an explicit error

Denote by `I_{R,delta}^infinity(u)` the full production of the actual degree-`R`
Fejer process. The localization bound yields

\[
 \int_0^1|I_{R,\delta}^{\infty}-I_r|\frac{du}{u}\le E_{r+1}.
\]

The reviewed common-flip stability theorem is for the **full** production and
gives, provided `c eta_R+T/sqrt(R)<=1/2`,

\[
 \int_0^1|I_{R,\theta/\sqrt R}^{\infty}(u)-I_0(u)|\frac{du}{u}
 \le2b(c\eta_R+T/\sqrt R).
 \tag{5.1}
\]

Here `b` denotes binary entropy. The input symbols differ in `L^1` by at most
the displayed argument. This comparison pays both the change of Fejer kernel
and the changing original shift. It does not apply the stability theorem
incorrectly to a finite center contribution.

Let the bounded-Lipschitz norm convention be `||F||_infinity<=1`, `Lip(F)<=1`.
Combining (3.2), (4.3), and (5.1), and paying the omitted Gaussian-limit tail
by `I_0(u)<=M_c u^2`, proves

\[
 \sup_{|\theta|\le T}|\mu_R^\theta(F)-\mu^\theta(F)|
 \le\mathcal E_{R,r},
 \tag{5.2}
\]

\[
 \boxed{\quad
 \mathcal E_{R,r}=
 \frac{L_D}{2\sqrt2}\sqrt{E_{r+1}}
 +\frac{M_D}{2}\mathcal B_{R,r}
 +E_{r+1}+2b(c\eta_R+T/\sqrt R)
 +\frac{M_c}{2N^2}.
 \quad} \tag{5.3}
\]

The same bound holds for a measurable test `F(u,x)` whose bounded-Lipschitz
norm in `x` is at most one uniformly in `u`. Every step above bounds the
error before the absolute `u` integral, and the stability estimate (5.1)
is already an absolute integral. No continuity or differentiability of the
test in `u` is needed. This joint-test version is used in the separate
full-law score proof in `SCORE_COMPENSATION.md`.

No radius-dependent or noise-dependent term has been suppressed. For fixed
`c,T`, choose `r=floor(R^(1/3))` for sufficiently large `R`. Every term tends
to zero; the stated `O_{c,T}(R^(-1/6)sqrt(log R))` follows. The constants are
not uniform as `c` approaches one. The contrast-one singleton shift domain is
not covered by this theorem.

The signed bounded-Lipschitz error for (1.4) is at most `2 mathcal E_{R,r}`.
Because the limiting Gaussian mixture has a continuous density, the same
weak convergence determines every fixed interval with finite endpoints.
This also follows directly by approximating an interval indicator from above
and below by Lipschitz functions; on a fixed `theta` compact set the densities
are bounded by `M_c/(2 sqrt(2 pi v_min))`.

## 6. Constructive signed compensation and transport

Each measure `mu^theta` has total mass `D_0`. For the symmetrized endpoint
measure, use the following joint finite measure: first give `u in (0,1]`
weight `I_0(u)du/u`; conditional on `u`, take

\[
 Z\sim N(0,v(u)),\qquad S\in\{-1,1\}\text{ fair and independent},
 \qquad Y=Z+2u\theta S.
\]

The first marginal is `mu^0`, and the second is
`(mu^theta+mu^(-theta))/2`. Moreover `E(Y|Z,u)=Z`, hence `E(Y|Z)=Z`.
This is a martingale coupling, so conditional Jensen proves nonnegativity
against any convex test for which the integrals exist. Its squared cost is
exactly (1.6). Formula (1.2) gives the two explicit cost bounds.

For an interval centered at zero, a nondegenerate centered Gaussian places
strictly more mass there than any nonzero translate. The translation
`2u theta` is nonzero for `u>0`, and `I_0(u)>0` there. Integrating proves the
strict negative central mass in (1.5). The positive complementary mass is
exactly its negative because the complete limiting signed mass is zero.

This construction neither pools complementary finite count layers to erase
negative mass nor subtracts a product reference. It transports the complete
leading production mass and retains the negative central contribution.

## 7. An explicit nonzero curvature-compensation constant

For the true sine midpoint process, the center and its nearest neighbor both
have mean `1/2`, and their off-diagonal kernel entry has magnitude `uc/pi`.
The two conditional probabilities are

\[
 1/2\pm2u^2(c/\pi)^2,
\]

with equal exterior weights. Conditional Jensen when refining this one-site
context to the full exterior therefore gives

\[
 I_0(u)\ge z\operatorname{atanh}z\ge z^2
 =16u^4(c/\pi)^4,\qquad z=4u^2(c/\pi)^2.
\]

This proves the lower bound in (1.2) without assuming entropy concavity.
The upper bound follows from the channel conditional interval.

The derivative of the Gaussian integral on `[-b,b]` is

\[
 \int_{-b}^b\gamma_v''(x)dx=-\frac{2b}{v}\gamma_v(b).
\]

Applying this to (1.7) yields (1.8)--(1.9). For `b=1/2` and
`1/2<=u<=3/4`, one has `7/32<=v(u)<=1/2` for every `0<c<1`. On this rectangle,

\[
 \gamma_v(1/2)>1/4,\qquad 1/v\ge2.
\]

For example, the first bound follows from `1/sqrt(2 pi v)>=1/sqrt(pi)>1/2`
and `exp(-1/(8v))>=exp(-4/7)>1/2`. The last exponential inequality follows
from `log 2>2/3>4/7`. Thus

\[
 C_{1/2}(c)
 >32(c/\pi)^4\int_{1/2}^{3/4}u^5du
 =\frac{665}{768}(c/\pi)^4.
 \tag{7.1}
\]

At `c=19/20`, using `pi<22/7`, the right side is strictly larger than

\[
 \frac{665}{768}\left(\frac{133}{440}\right)^4
 =\frac{41615795893}{5757075456000}>\frac1{140}.
\]

The difference from `1/140` is
`3456798451/40299528192000`. These rational calculations are supporting
checks of the displayed analytic inequalities, not a finite configuration
certificate or an independent review.

## 8. Why differentiating the mesoscopic limit is legitimate

Real uniform value convergence would not suffice. Here a separate
complete-event determinant bound supplies a locally bounded holomorphic
family on the mesoscopic scale.

Fix a complex `theta` disk `|theta|<=T`, write `delta=x+iy=theta/sqrt(R)`, and
keep `epsilon=(1-c)/4`. At the real displacement `x`, every complete exterior
event matrix

\[
 A_w(x)=K_{C_R}(x)-\operatorname{diag}(1-w)
\]

is Hermitian and has all eigenvalues outside `(-epsilon,epsilon)`. To see
this, let `z` be the number of vacant coordinates. Weyl's inequalities place
the first `z` ordered eigenvalues between `-1+epsilon` and `-epsilon`, and
the others between `epsilon` and `1-epsilon`.

The complete word probability has the exact factorization

\[
 p_w(x+iy)=p_w(x)\det(I+iuy A_w(x)^{-1}).
\]

Taking the product over its `2R` real eigenvalues gives

\[
 |p_w(x+iy)|
 \le p_w(x)\exp\{R u^2y^2/\epsilon^2\},\qquad
 \sum_w|p_w(x+iy)|\le\exp\{u^2(\Im\theta)^2/\epsilon^2\}.
 \tag{8.1}
\]

In particular there is no exponential-in-volume loss: `R y^2` is bounded on
the fixed `theta` disk. All actual exterior words are still present.

The complete conditional predictor is the Schur expression

\[
 q_w(x+iy)=K_{00}(x+iy)-b_u^*A_w(x+iy)^{-1}b_u,
 \qquad \|b_u\|^2\le u^2c^2/4.
\]

Since `A_w(x)` is Hermitian, both resolvents at `x` and `x+iy` have norm at
most `epsilon^(-1)`. The resolvent identity therefore implies

\[
 |q_w(x+iy)-q_w(x)|\le u L_c|y|,
 \qquad L_c=1+\frac{c^2}{4\epsilon^2}.
 \tag{8.2}
\]

Set `D_1=(3+c)/4<1`. If

\[
 R\ge\left(\frac{8L_cT}{1-c}\right)^2,
 \tag{8.3}
\]

then (2.2) and (8.2) give `|2q_w(x+iy)-1|<=uD_1`. Define the complex
production by its single-valued power series

\[
 \phi(q)=(2q-1)\operatorname{atanh}(2q-1).
\]

It agrees with the real production and satisfies
`|phi(q_w)|<=M_{D_1}u^2`. Thus, for any fixed bounded Borel `F`,

\[
 |\mu_R^\theta(F)|
 \le\frac{M_{D_1}}2\|F\|_\infty\exp(T^2/\epsilon^2).
 \tag{8.4}
\]

Each such function is holomorphic on the disk once (8.3) holds. The finite
sum and the integral are holomorphic because the same bound is integrable
against `du/u`. The complex Gaussian formula in (1.3) is also holomorphic on
every fixed disk, using `v>=v_min` and the integrable bound (1.2).

For completeness, the normal-family step does not import a derivative
convergence assumption. Local boundedness (8.4) and Cauchy's estimates make
any subsequence relatively compact uniformly on smaller disks. Any such
limit agrees on the real interval with (1.3), by Theorem 1 (or its interval
indicator consequence). The identity theorem makes that holomorphic limit
unique. Every subsequence therefore has the same locally uniform limit.
Cauchy's integral formula now gives convergence of every fixed derivative.

Finally, the original parameter relation is exact:

\[
 \partial_\theta^k\mu_R^\theta(F)|_{\theta=0}
 =R^{-k/2}A_{R,F}^{(k)}(0).
\]

For `k=2`, differentiating the **limiting Gaussian** translation gives
`4u^2 gamma_v''`, which proves (1.7). The noise factor `u^2`, the exterior
probability derivatives, and the predictor derivatives have all been retained
by differentiating the complete holomorphic expression. No score,
acceleration, or changing-layer-weight term was thrown away.

## 9. Exact scope and the remaining sign estimate

The finite full signed sum for a symmetric chord `delta=+-theta/sqrt(R)` is
`nu_R^theta(R)`. This theorem proves its leading limit is zero, while every
fixed central count band has a strictly negative limiting contribution and
its complement supplies exactly the opposite positive limit. At the
midpoint, both corresponding curvature contributions are of order `R`, with
opposite leading constants. This is a genuine signed compensation theorem
for a growing, fixed-density, fixed-contrast family.

It does **not** prove `A_{R,1}''>=0`, `J_R''<=0`, or a nonnegative limiting
Jensen gap at a fixed nonshrinking chord. Equation (1.8) only says that the
complete curvature is `o(R)`. Determining its sign requires the next term,
not another assertion that the leading divergent terms cancel.

This limitation also prevents a hidden value-to-Hessian shortcut. At the
critical chord scale, a fixed-radius strong-concavity margin is of order
`1/R`. The reviewed uniform value-transfer error is `O(log^2 R/R)` (or
`O_{epsilon,c}(log R/R)` on a fixed interior strip), neither of which is
`o(1/R)`. The explicit weighted-CLT error here is larger still. Thus those
errors cannot pay the required order-`1/R` signed remainder or identify a
rate Hessian. The fixed-chord value bridge remains valid but does not supply
that missing sign.

No contrast threshold extension, full sine-target proof, target
counterexample, total-variation-distance limit, or independent review is
claimed. Constants are explicit for fixed `c<1` and fixed bounded mesoscopic
shift scales; the limit `c->1` is not interchanged with `R->infinity`.
