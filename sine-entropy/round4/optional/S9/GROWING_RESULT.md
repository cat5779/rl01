DISPROVED_ROUTE_LEMMA

# S9 round two: a nonvanishing signed count-layer obstruction on the aligned family

The high-contrast **S-sine entropy-rate concavity target is neither proved nor
disproved here**. The result disproves a named stronger route: convexity of the
noise-integrated, complete exterior-count layers, or even an `o(1)` budget for
the sum of their negative Jensen contributions. This failure occurs on the
actual `degree = radius = R` Fejer family, at a fixed positive density, fixed
high contrast, and fixed endpoints. It survives complementary-layer pooling
and subtraction of the one-site Bernoulli production.

There are three different new proof units.

* An analytic growing-family theorem: for `c=19/20`, `rho=1/2`, and the fixed
  shifts `1/200, 1/40, 9/200`, a specified central band of exterior counts has
  integrated Jensen contribution **less than -1/40** for every odd
  `R >= 160,001`. This is an analytic threshold, not a claim to have
  enumerated configurations at that size. More generally the total negative
  mass of this layer decomposition has an identified, strictly positive limit.
* A small exact certificate: at `R=3`, `c=5*pi/16`, `rho=1/2`, the combined
  exterior-count layers `1+5` have integrated production curvature `<-1/150`
  throughout `|a-(1-c)/2| <= 1/10000`. The **full** integrated production has
  curvature `>4`, and the complete seven-site Shannon entropy has negative
  curvature at the same parameters. Thus the finite witness is explicitly a
  route counterexample, not an entropy counterexample.

* A positive full-production theorem: for **every** `37/40<=c<=1` and
  every legal shift, the half-density **R=3** aligned family satisfies
  `partial_a^2 I_3 >= 6 exp(-2s)` at every noise time. Therefore its assigned
  `J_3` is strongly concave with curvature at most `-45/16`. The proof uses
  an exact 2922-leaf cover of a rational auxiliary kernel box and is given in
  `FULL_R3_PRODUCTION.md`. This covers an entire contrast/shift continuum,
  but its fixed radius is not promoted to a growing-radius or rate theorem.

All new claims are author proofs/certificates, pending independent review.
No literature-priority claim is made. Reviewed main is
`6242dc3206ff196dc15b9dbfb0e41971844cecdc`; the starting round-two branch head is
`9eacaec5459afd8419a97dc7450af116e68a5e27`. The repaired first-round proofs are
not overwritten. See `DEPENDENCY_DELTA.md` and the pre-existing `BASELINE.md`.

## 1. The weakest remaining full signed estimate

We use natural logarithms. Let `b` be binary entropy and

\[
 \phi(q)=(q-\tfrac12)\log\frac q{1-q}.
\]

For one fixed interval `E_rho`, contrast `c`, and legal shift `a`, set

\[
 f_{a,R}=a+c(F_R*1_{E_\rho}),\qquad
 f_{a,R,s}=\tfrac12+e^{-s}(f_{a,R}-\tfrac12),
\]
\[
 I_R(f)=\mathbb E_f\phi\bigl(\Pr_f(Y_0=1\mid
               Y_{[-R,R]\setminus\{0\}})\bigr),\quad
 J_R(a)=\log2-\int_0^{\log(R+1)} I_R(f_{a,R,s})\,ds.
\]

For each fixed legal chord `a_t=(1-t)a_0+t a_1`, write

\[
 G_R=J_R(a_t)-(1-t)J_R(a_0)-tJ_R(a_1).
\]

The accepted first-round bound, imported unchanged from main RESULT section
6.3, is

\[
 |G_R-[h(f_{a_t})-(1-t)h(f_{a_0})-th(f_{a_1})]|
 \le E_R,\qquad E_R\longrightarrow0,                         \tag{1}
\]

where, with `N=R+1`,

\[
 E_R=A_N(c)+2b(d_R)+\tau(\log N),
\]
\[
 A_N(c)=c\,b\!\left(\min\{\tfrac12,
                4(\mathsf H_N+1)/(\pi^2N)\}\right),\quad
 d_R=c\min\{\tfrac12,(\log N+1/2)/N\},\quad
 \tau(\log N)\le N^{-2}\log2.
\]

Thus it would suffice to prove `G_R >= -eta_R`, with `eta_R -> 0`, for every
fixed chord. Equivalently, `liminf G_R >= 0` would suffice. **This is the
remaining obligation, not a new theorem of this paper.** No finite-radius
convexity or rate Hessian convergence is assumed. The obstruction below
concerns a stronger attempt to prove this signed sum by controlling its
individual count layers.

## 2. Exact complete-atom and moving-weight bookkeeping

Fix a finite window and write `u=e^{-s}`. Along an original common shift
parameter `delta`, its genuine kernel has the form

\[
 K(u,\delta)=\tfrac12 I+u(B+\delta I).
\]

For a labelled configuration `y`, put

\[
 A_y=K-\operatorname{diag}(1-y),\quad
 p_y=(-1)^{\#\{i:y_i=0\}}\det A_y.
\]

On a strict legal domain, the actual derivatives with respect to **the
original** `delta` are

\[
 p_y'=u p_y\operatorname{Tr} A_y^{-1},\qquad
 p_y''=u^2p_y\{(\operatorname{Tr} A_y^{-1})^2
                              -\operatorname{Tr} A_y^{-2}\}.       \tag{2}
\]

The factors `u` and `u^2` cannot be omitted. For an exterior word `w`, let
`x=p(0,w)`, `y=p(1,w)`, `W=x+y`, `q=y/W`. Its entire production contribution is

\[
 F(x,y)=W\phi(q)=\tfrac12(y-x)\log(y/x).
\]

Direct differentiation gives

\[
 F''=\frac{x+y}{2}\left(\frac{x'}x-\frac{y'}y\right)^2
       +\frac{\log(x/y)+1-y/x}{2}\,x''
       +\frac{\log(y/x)+1-x/y}{2}\,y''.                         \tag{3}
\]

Equivalently this is

\[
 W''\phi(q)+2W'\phi'(q)q'
       +W\{\phi''(q)(q')^2+\phi'(q)q''\}.
\]

We retain all these terms. Equation (3) is not a probability-affine shortcut.
For full Shannon entropy we separately retain

\[
 H''=-\sum_y p_y''\log p_y-\sum_y(p_y')^2/p_y.                  \tag{4}
\]

Every finite integral below uses

\[
 \int_0^{\log(R+1)} (\cdots)\,ds
       =\int_{1/(R+1)}^1(\cdots)\,\frac{du}{u}.              \tag{5}
\]

All count layers are sums of the original weighted complete words. We do
**not** replace these words by a uniform count layer, normalized layer entropy,
count entropy, or spectral entropy.

## 3. The live strengthening tested and refuted

From now on let `rho=1/2`, `a_*=(1-c)/2`, and write `delta=a-a_*`. Fix
`0<d<(1-c)/2`. For odd positive integers `R`, the half-interval Fejer
polynomial has actual degree `R`; its top odd Fourier coefficient is nonzero.
The condition radius is also exactly `R`.

Let

\[
 M_R=\sum_{i\in[-R,R]\setminus\{0\}}Y_i,\qquad
 A_{R,k}(\delta)=\int_{1/(R+1)}^1
       \mathbb E_{u,\delta}[\phi(q_R)1_{\{M_R=k\}}]\,\frac{du}{u},
 \quad 0\le k\le2R,
\]
\[
 g_{R,k}=\tfrac12[A_{R,k}(-d)+A_{R,k}(d)]-A_{R,k}(0),\qquad
 N_R^- =\sum_{k=0}^{2R}(-g_{R,k})_+ .                         \tag{6}
\]

Then the **full** desired midpoint gap is `G_R=sum_k g_{R,k}`. The proposed
stronger interfaces are:

- each completed layer has `g_{R,k}>=0`; or
- after summing all adverse layers, `N_R^- = o(1)`.

Neither is necessary for full concavity. The second still allows negative
finite layers and would make discarding their signs compatible with the known
vanishing approximation error. **Both are false.** Complement pooling and a
one-site-product subtraction, considered below, do not repair these versions.
This is a newly tested S9 proof interface, not an assertion that it was a
published conjecture.

### Theorem A (explicit growing aligned counterexample)

Fix

\[
 c=19/20,\quad \rho=1/2,\quad
 a_-=1/200,\quad a_*=1/40,\quad a_+=9/200,
 \qquad d=1/50.
\]

For every odd `R>=160,001`, let

\[
 w_R=\lceil3\sqrt R\rceil,\qquad
 \mathcal B_R=\{k:|k-R|\le w_R\}.
\]

Then

\[
 \boxed{\quad
 \sum_{k\in\mathcal B_R}g_{R,k}
   \le -\frac{4100517395332877}{147456000000000000}
   <-\frac1{40},\qquad N_R^->\frac1{40}.
 \quad}                                                       \tag{7}
\]

All parameters other than `R` are fixed. This is the exact assigned noise-time
schedule, not an off-alignment example. The band is invariant under
`k -> 2R-k`, so even complementary-count pooling cannot turn its sum positive.
There is no claim that the sum over **all** counts is negative.

## 4. Proof of Theorem A

### 4.1 Uniform complete conditional production bound

The underlying input to the channel is the DPP with symbol `F_R*1_E`.
Conditional on the input, the output bits use independent binary channels.
After the additional fair noise, the conditional success probabilities are

\[
 \tfrac12+u\delta+uc(X_i-\tfrac12).
\]

Condition on any exterior output word and average over the input. The same
interval bounds remain valid. With `D=c+2d<1`, this gives

\[
 |2q_R-1|\le uD\quad (|\delta|\le d).
\]

For `0<=z<1`, `phi((1+z)/2)=z atanh z`. Convexity of `atanh` at zero implies
`atanh(uz)<=u atanh z`, and therefore

\[
 0\le\phi(q_R)\le M_Du^2,\qquad M_D=D\operatorname{atanh}D.    \tag{8}
\]

At the midpoint `delta=0`, use the sharper `M_c=c atanh c`.
These estimates hold for **every complete exterior word**; no typical-word
or rare-word exclusion is used.

### 4.2 Count concentration, used only for the original weights

An `m`-coordinate marginal of a DPP with kernel `L` has count generating
function

\[
 \mathbb E z^M=\det(I+(z-1)L)
              =\prod_{j=1}^m(1-\lambda_j+\lambda_j z).
\]

Thus its count has the law of a sum of independent Bernoulli variables.
This diagonalization identifies a **count distribution only**. It is not a
rotation of the observed configuration or a formula for its Shannon entropy.

For a centered Bernoulli variable, the second derivative of its log moment
generating function is the variance of a tilted Bernoulli, at most `1/4`.
The log mgf and its first derivative vanish at zero. Twice integrating yields
`log E exp(t(B-EB)) <= t^2/8` for every real `t`. Multiplying the `m=2R` mgfs
and applying Chernoff, with the optimizing positive or negative `t`, gives

\[
 \Pr(M-\mathbb EM\ge x),\ \Pr(M-\mathbb EM\le-x)
                         \le e^{-x^2/R}\qquad(x\ge0).         \tag{9}
\]

All noised kernels here are legal contractions. Their exterior means are
exactly

\[
 \mathbb E_{u,\delta}M_R=R+2Ru\delta.                         \tag{10}
\]

The constants in (8)--(10) do not grow with bandwidth or context size.

### 4.3 The midpoint retains a definite complete production

The true nearest-neighbor entry of the aligned kernel at the midpoint is
`u gamma_R`, where

\[
 \gamma_R=\frac c\pi\frac R{R+1}.
\]

Both marginal occupancies are `1/2`. The two-point DPP determinant therefore
gives the conditional probabilities `1/2 +/- 2u^2 gamma_R^2`, each with exterior
weight `1/2`. Conditional Jensen, since the full context includes this one
neighbor, implies

\[
 I_R(u,0)\ge z\operatorname{atanh}z\ge z^2
                     =16u^4\gamma_R^4,
 \qquad z=4u^2\gamma_R^2.                                   \tag{11}
\]

Let `A_R^B=sum_{k in B_R} A_{R,k}`. At `delta=0`, (9) gives
`Pr(M_R notin B_R)<=2 exp(-w_R^2/R)`. Equations (8), (11), and (5) imply

\[
 \boxed{\quad
 A_R^B(0)\ge4\gamma_R^4[1-(R+1)^{-4}]
                     -M_c e^{-w_R^2/R}.
 \quad}                                                       \tag{12}
\]

The loss term integrates the discarded words with their real probabilities.
It is not a claim that each discarded word has a favorable curvature.

### 4.4 The same fixed count band loses both endpoints

Put `v=w_R/(Rd)`. For `u>=v`, the distance from the endpoint mean in (10) to
the band is at least `Rud`. The appropriate one-sided form of (9) gives

\[
 \Pr_{u,\pm d}(M_R\in\mathcal B_R)\le e^{-Rd^2u^2}.
\]

For `u<v`, use the bound one. Extending the positive upper integrals when
necessary, (8) yields

\[
 \begin{aligned}
 A_R^B(\pm d)
 &\le M_D\left[\int_0^v u\,du+
                         \int_v^\infty u e^{-Rd^2u^2}\,du\right]\\
 &=\frac{M_D}{2Rd^2}
                     \left[\frac{w_R^2}{R}+e^{-w_R^2/R}\right]
 =: U_R.                                                     \tag{13}
 \end{aligned}
\]

This also gives a valid upper bound when `v>1`; in that case the first upper
integral alone already covers `[0,1]`. The small-noise-retention part is
integrable because the complete production is `O(u^2)`. One cannot instead
integrate a constant count-error bound against `du/u` down to zero.

### 4.5 Explicit rational constants

For the parameters in Theorem A, `D=99/100`, and

\[
 M_c=\tfrac{19}{40}\log39<7/4,\qquad
 M_D=\tfrac{99}{200}\log199<21/8,\qquad e^{-9}<1/8000.
\]

These elementary strict inequalities are certified by the standard-library
program `code/verify_constants.py` using rational log intervals and the positive
series for `exp(9)`. It also checks `3<pi<22/7` by Machin's arctangent formula.
For the elementary preliminary threshold `R_0=4,000,001`, every `R>=R_0` has

\[
 9\le w_R^2/R\le(301/100)^2,
\]

because `R_0>=10000`. Monotonicity of the two rational factors in (12), followed
by exact evaluation at `R_0`, gives

\[
 4\left(\frac{19}{20}\frac7{22}\right)^4
    \left(\frac{R}{R+1}\right)^4[1-(R+1)^{-4}]>1/30.           \tag{14}
\]

Hence the midpoint outside loss is `<7/32000`, while

\[
 U_R\le U_*=
 \frac{21}{8}\frac{(301/100)^2+1/8000}{2R_0(1/50)^2}
 =\frac{7610589}{1024000256}.
\]

Combining (12)--(14) proves

\[
 \frac{A_R^B(-d)+A_R^B(d)}2-A_R^B(0)
 \le U_* -\frac1{30}+\frac7{32000}
 =-\frac{616377019}{24000006000}<-\frac1{40}.
\]

Finally `sum_k(-g_k)_+ >= -sum_{k in B}g_k`. This proves the weaker threshold `R>=4,000,001`. Section 4.6 proves (7)
with the sharper threshold and margin stated in Theorem A.
The only large integers processed by the constants checker is in rational
inequalities such as (14). It performs no `2^(2R+1)`-configuration computation
at the analytic threshold.

### 4.6 A sharper threshold from the complete conditional Schur formula

This section reduces the threshold without enumerating a large window. It
uses only a finite conditional inverse bound, not a spatial posterior-tail
theorem. At half density the input Fejer contraction `Q` has diagonal `1/2`.
Since `Q^2<=Q`, its off-diagonal row energy is at most `1/4`. For the row `b`
of `B=c(Q-I/2)` joining the center to its exterior, therefore
`||b||^2<=c^2/4`.

Let `A_C=diag(2w-1)/2+u(B_C+delta I)` be the signed exterior event matrix.
Its inverse norm is at most `2/(1-uD)`, because
`||B_C+delta I||<=D/2`, with `D=99/100`. The **complete-word** Schur formula is

\[
 q_R=\tfrac12+u\delta-u^2 b^*A_C^{-1}b.
\]

Consequently, on both endpoints and for `u<=1/2`,

\[
 |2q_R-1|\le 2du+\frac{c^2u^2}{1-uD}
 \le\frac{u}{25}+\frac{91u^2}{50}<\frac12.                 \tag{14a}
\]

The constants use `c^2/(1-D/2)=361/202<91/50`; at `u=1/2` the last
polynomial is `19/40`. Since `z atanh z<=z^2/(1-z^2)`, we obtain

\[
 \phi(q_R)\le\frac{4u^2+364u^3+8281u^4}{1875}
                         \qquad(0\le u\le1/2).             \tag{14b}
\]

Write `W=w_R/sqrt(R)` and `b_0=2d sqrt(R)`. The sharper direct count bound is

\[
 \Pr_{u,\pm d}(M_R\in\mathcal B_R)
   \le P(u):=\exp[-((b_0u-W)_+)^2].                         \tag{14c}
\]

For `j=1,2,3`, integrate `u^j P(u)` over `[0,infinity)`. Splitting at
`W/b_0`, changing variable `x=b_0u-W` afterwards, and using elementary
Gaussian moments gives respectively

\[
 L_1=\frac{W^2+1+\sqrt\pi W}{8Rd^2},
\]
\[
 L_2=\frac{W^3/3+W+\sqrt\pi(1/4+W^2/2)}{8d^3R^{3/2}},
\]
\[
 L_3=\frac{W^4+2+6W^2+\sqrt\pi(3W+2W^3)}{64R^2d^4}.       \tag{14d}
\]

Extending the positive integrals only enlarges the bound. For `R>=160,001`,
use `R>=160000=400^2`, `W<=301/100`, and `sqrt(pi)<9/5`. At these conservative
rational endpoints, the three upper bounds are

\[
 L_1\le154781/5120000,\quad
 L_2\le62113171/12288000000,\quad
 L_3\le25287525561/26214400000000.
\]

For the remaining interval `u>=1/2`,
`b_0u-W >= d sqrt(R)-W >= 499/100`, whose square exceeds `24`.
Thus (8) and (14c) give its contribution at most
`(21/16)exp(-24)<21/(16*10^10)`. The strict exponential bound follows from
a finite positive partial sum for `exp(24)` and is checked exactly.
Combining this tail with (14b)--(14d),

\[
 A_R^B(\pm d)\le
 \frac{4L_1+364L_2+8281L_3}{1875}+\frac{21}{16\cdot10^{10}}
 \le\frac{782426604667123}{147456000000000000}.              \tag{14e}
\]

The midpoint bound `4 gamma_R^4[1-(R+1)^(-4)]>1/30` already holds at
`R=160,001`, as the rational checker verifies, and is increasing thereafter.
Subtract it and add the same outside loss `7/32000` to (14e). The result is
exactly the stronger rational upper bound in (7). This proves Theorem A.
No derivative of a count-tail inequality has been taken; the count tail is
used only as a weight in complete production values.

### 4.7 The adverse band exceeds the existing transfer allowance

This compares magnitudes; it does **not** apply a full-entropy rate bracket to
an isolated count band. For the same radii `R>=160001`, the already reviewed
full Jensen allowance `E_R` in (1) satisfies the explicit bound

\[
 E_R<1/400.
\]

Indeed put `N_0=160002`, `eta_0=25/(2N_0)`, and `beta_0=56/(9N_0)`.
The rational exponential-series checks prove `exp(12)>N_0`,
`exp(10)>1/eta_0`, and `exp(11)>1/beta_0`. Since `(log N+1/2)/N` and
`(log N+2)/N` decrease for `N>=N_0`, while `pi>3` and
`H_N^harm<=1+log N`, the arguments in `b(d_R)` and `A_N(c)` are at most
`eta_0` and `beta_0`. Both lie below one half. The elementary bound
`b(x)<=x log(e/x)` therefore gives

\[
 E_R\le 12\beta_0+22\eta_0+N_0^{-2}
       =\frac{1049}{3N_0}+\frac1{N_0^2}<\frac1{400}.
\]

Thus the magnitude of the adverse band, already `>1/40`, is more than ten
times this full comparison allowance. It cannot be discarded as an error
already paid by the first-round transfer. Compensation from the other count
layers remains indispensable for any proof using this decomposition. The
**total** signed Jensen gap is still not signed by this observation.

## 5. Exact asymptotic negative mass, not just one large-radius bound

### Theorem B (asymptotic separation of layer signs)

Fix any `0<c<1` and `0<d<(1-c)/2`, still at `rho=1/2` and along odd radii.
Let

\[
 D(\delta)=\log2-h(f_{a_*+\delta}).
\]

For the exact individual layers in (6),

\[
 \boxed{\begin{aligned}
 \lim_R\sum_k(-g_{R,k})_+ &=D(0),\\
 \lim_R\sum_k(g_{R,k})_+ &=\tfrac12[D(-d)+D(d)],\\
 D(0)&\ge 4(c/\pi)^4>0.
 \end{aligned}}                                               \tag{15}
\]

In particular, the negative mass is not an approximation tail. It converges to
a positive entropy deficit at the center, even for contrasts where the full
concavity theorem is already known. This does not determine the difference
of the two limits, which is exactly the remaining full Jensen question.

**Proof.** Choose integer bands with
`w_R/sqrt(R) -> infinity` and `w_R/R -> 0`, for example
`w_R=ceil(R^(3/4))`. The midpoint outside loss in (12) tends to zero, and the
endpoint upper bound (13) tends to zero. The already accepted S9 uniform
value/integral convergence gives, at each of the three fixed shifts,

\[
 \sum_k A_{R,k}(\delta)\longrightarrow D(\delta).              \tag{16}
\]

Thus `A_R^B(0)->D(0)`, whereas `A_R^B(-d),A_R^B(d)->0`. Consequently the
negative mass is at least `-sum_{k in B}g_{R,k}->D(0)`. Conversely all
`A_{R,k}` are nonnegative, so

\[
 (-g_{R,k})_+\le A_{R,k}(0),\qquad
 \sum_k(-g_{R,k})_+\le\sum_k A_{R,k}(0)\longrightarrow D(0).
\]

This proves the first limit. The identity
`sum g_+ - sum(-g)_+ = sum g` and (16) prove the second. Integrating (11) and
then taking `R->infinity` gives the last inequality in (15). No entropy-rate
second derivative is used. QED.

### 5.1 Complement pooling does not reduce this negative mass

For a half-interval symbol, all nonzero off-diagonal lags are odd. The actual
coordinate-diagonal gauge `D_ii=(-1)^i`, combined with output complementation,
therefore sends the law at `delta` to the law at `-delta`. It does not rotate
the observed coordinates. Since `phi(1-q)=phi(q)`,

\[
 A_{R,k}(\delta)=A_{R,2R-k}(-\delta),\qquad
 g_{R,k}=g_{R,2R-k}.
\]

Combining complementary layers doubles equal-sign contributions. It preserves
the total negative mass exactly. In particular Theorems A and B remain an
obstruction after this natural symmetry reduction.

### 5.2 Removing the independent Bernoulli contribution also does not repair it

The one-site marginal is `p(u,delta)=1/2+u delta`. Define instead

\[
 \widetilde A_{R,k}(\delta)=\int_{1/(R+1)}^1
  \mathbb E[(\phi(q_R)-\phi(p(u,\delta)))1_{\{M_R=k\}}]du/u.
\]

These are still genuinely moving weighted layers, not conditional expectations
with frozen count weights. At the midpoint, `phi(p)=0`, so their central-band
sum equals `A_R^B(0)`. At the endpoints, `phi(p)>=0`, so each band sum is at
most `A_R^B(+-d)`. Thus **the same explicit bound (7)** holds for the Jensen
sum of these product-subtracted bands. For the broader bands used in Theorem B,
its endpoints tend to zero in absolute value: use
`|phi(q_R)-phi(p)|<=2M_Du^2` in (13). Therefore their total negative Jensen
mass has `liminf >= D(0)>0`. We do not assert an exact negative-mass limit for
this signed excess decomposition, whose endpoint layers need not be positive.

### 5.3 A quantitative failure of uniform lower curvature for the selected bands

Keep `c=19/20`, `rho=1/2`, and the same bands
`|M_R-R|<=ceil(3 sqrt R)`, but now use the shrinking half-chord
`h_R=R^(-1/4)`. For every odd `R>=6,250,001`, this half-chord is at most
`1/50`, so the same complete-word bound `M_D<21/8` applies. In (13), replace
`d` by `h_R`. The endpoint upper bound is at most

\[
 \frac{21}{8}\frac{(301/100)^2+1/8000}{2\sqrt R}
 <\frac{7610589}{1600000000}.
\]

Together with the midpoint lower bound, this is again a band Jensen
contribution less than `-1/40`. For each finite `R`, the band functional
`A_R^B(delta)` is `C^2` on this strictly legal interval: it is a finite sum of
positive-atom analytic expressions integrated over a compact positive `u`
interval. The ordinary symmetric second-derivative integral identity then
forces some `|delta_R|<h_R` with

\[
 \boxed{\qquad (A_R^B)''(\delta_R)<-\frac{\sqrt R}{20},
                 \qquad \delta_R\longrightarrow0.\qquad}       \tag{17a}
\]

Indeed a lower bound `-sqrt(R)/20=-1/(20h_R^2)` on the entire interval would
make the Jensen contribution at least `-1/40`, a contradiction. This is a
curvature obstruction for a **selected, moving-weight count band**, not for
the sum of all bands. It does not claim the adverse point is exactly zero,
and does not differentiate any limiting entropy-rate formula. The fixed-chord
Theorem A remains separate; the present shrinking-chord corollary is not used
as a rate counterexample.

### 5.4 The negative-mass phenomenon is not confined to one frequency density

Theorem B also holds whenever `0<rho<1`,

\[
 a_*=\tfrac12-c\rho,\qquad
 0<d<\tfrac12-c\max\{\rho,1-\rho\}.
\]

These inequalities make all three shifts strictly legal and make the center
output density exactly `1/2`. Use the same exterior count bands and replace
`gamma_R` in (11) by
`c sin(pi rho) R/[pi(R+1)]`. The common conditional bound (8) uses
`D=2c max(rho,1-rho)+2d<1`. For the midpoint outside-band bound,
use this finite `M_D` in place of the half-density-specific `M_c`; its
exponential outside loss still tends to zero. Equations (9)--(13), with
these stated replacements, give the same negative-mass sandwich. No
half-density numerical threshold is asserted for this extension. In particular

\[
 \lim_R N_R^-=\log2-h(f_{a_*})
       \ge4\left(\frac{c\sin(\pi\rho)}\pi\right)^4>0.        \tag{17b}
\]

For the strict wording `degree=radius=R`, take any unbounded subsequence with
`sin(pi rho R)!=0`; the top Fejer coefficient is then nonzero. Such a
subsequence exists for every fixed `0<rho<1`. All-radii statements without
this restriction have degree **at most** `R` and are still valid, but are not
mislabelled as exact-degree statements. At half density this condition is
precisely the odd-radius convention already used. The exact complement
identity of section 5.1 is asserted only at half density; the central band
itself is always a union of complementary-count pairs.

The supplement `LAYER_MEASURE.md` identifies the entire limiting signed
count-layer measure and supplies a bounded-Lipschitz estimate. It distinguishes
weak convergence of the two Jordan parts from the stronger, unclaimed total
variation convergence of measures.

## 6. Genuine growing-rank Fourier projections

The obstruction is not caused only by Fejer inputs having fractional
eigenvalues. Let `n` run through multiples of four and let `P_n` be the actual
projection onto the first `n/2` Fourier modes on the `n`-cycle. Keep the same
fixed channel parameters as in Theorem A. The projection has rank `n/2` and
constant diagonal `1/2`; its nearest-neighbor magnitude is

\[
 |(P_n)_{01}|=\frac1{n\sin(\pi/n)}\ge1/\pi.
\]

Its nonzero nearest-neighbor edges connect the whole cycle. This is not a
union of independent two-site blocks or a rank-one/co-rank-one limit.
Condition the center on all `n-1` other coordinates, integrate over
`u in [1/n,1]`, and select the count band

\[
 |M-(n-1)/2|\le\lceil3\sqrt{(n-1)/2}\rceil.
\]

Apply the proof of Theorem A with the real number `L=(n-1)/2` in place of `R`
in the mgf and count bounds. Integer `L` was not needed there. The midpoint
neighbor integral is now at least `4(c/pi)^4(1-n^(-4))`, which is greater than
the rational lower bound (14) when `L>=160,001`; the truncation starts at `1/n`
rather than `1/(L+1)`, which only increases that lower bound. The row energy is exactly `c^2/4`, so the sharper Schur and Gaussian-moment
bounds in section 4.6 also apply with `L` replacing `R`. The same constants
therefore prove a band Jensen contribution `<-1/40` whenever `n` is a multiple
of four and `n>=320,004`.

For the exact negative-mass limit, take wider bands as in Theorem B. Circular
translation symmetry equates center production with total production divided
by `n`. The finite noise identity and its `n^(-2) log2` truncation bound compare
the integrated total with `log2-H(DPP(aI+cP_n))/n`. The **reviewed S8**
circle-to-Toeplitz entropy transfer then identifies its limit with `D(delta)`.
The same sandwich proves (15) for these genuine rank-`n/2` projections.
This use of S8 is a transfer of already established entropy **values**, not a
new transfer theorem or a transfer of finite Hessians.

## 7. A complete small certificate inside the exactly aligned family

The analytic result above needs no large configuration search. Independently,
the following small witness certifies that the same sign loss is already
visible after integrating the precise finite-noise schedule.

Set `R=3`, `rho=1/2`, `c_0=5*pi/16`, `a_0=(1-c_0)/2`, and
`a=a_0+delta`, `|delta|<=h_0=1/10000`. The three-degree Fejer symbol is exactly

\[
 f_{a_0,3}(\theta)=\tfrac12+\frac{15}{32}\cos(2\pi\theta)
                            -\frac5{96}\cos(6\pi\theta).
\]

Putting `t=cos(2*pi*theta)`, its nonconstant part is
`5t/8-5t^3/24`, increasing on `[-1,1]`, with endpoints `+-5/12`.
Hence the whole parameter interval is strictly legal. Also
`37/40<c_0<1` and `a_0>h_0`, as certified using rational bounds on pi.

On the seven physical coordinates `[-3,3]`, write

\[
 K(u,\delta)=\tfrac12I+u(B+\delta I),\quad
 B_{ij}=\begin{cases}45/192&|i-j|=1,\\-5/192&|i-j|=3,\\0&\text{otherwise.}\end{cases}
\]

The pi in the original contrast cancels in these actual kernel entries.
Nothing has been rounded to a nearby non-Fejer kernel. All `128` complete
atoms are bivariate rational polynomials with the common denominator

\[
 192^7=9618527719784448.
\]

The certificate lists every atom as

\[
 p_y(u,\delta)=192^{-7}
       \sum_{0\le l\le k\le7,\ k-l\text{ even}} C_{y,k,l}u^k\delta^l,
                                                                    \tag{17}
\]

with all integer coefficients `C` present in `outputs/aligned_certificate.json`.
The first two derivatives are the literal derivatives of (17), so they retain
all noise-time factors. There are twenty coefficient positions per atom.

### 7.1 Independent reconstruction of all probability and derivative layers

The production engine obtains (17) from integer principal minors followed by
a Walsh transform. In `code/check_exact_atoms.py`, a separate column-subset
Leibniz determinant algorithm reconstructs **all 128 entire bivariate
polynomials**, without calling the principal-minor expansion, Bareiss, or Walsh
code. A Fraction Gauss--Jordan implementation also computes each signed event
determinant and its inverse, applies (2), and compares all three jets at three
rational nodes. A further value construction uses inclusion-minor Mobius
inversion. All 128
atoms at every node are positive; all three total jets are exactly `1,0,0`.
Coefficientwise normalization and the complement identity are checked too.
This is independent **implementation** within the same author session, not
independent mathematical review.

### 7.2 Outward continuum integration, including changing layer weights

Use 128-bit directed dyadic interval arithmetic. The whole rectangle

\[
 1/4\le u\le1,\qquad -1/10000\le\delta\le1/10000
\]

is covered by 2048 consecutive rational `u` cells and the entire common
`delta` interval in every cell. Each cell evaluates all 128 polynomials and
both derivative layers, then all 64 complete center pairs by (3). All atom
lower bounds stay positive. The integrand is enclosed after division by `u`,
and its rectangle enclosure is multiplied by the cell width. Thus there is
no uncertified numerical-quadrature or interpolation remainder.

For logarithms, range-reduce a positive rational to `2^k m`, `1<=m<=2`, and use

\[
 \log m=2\sum_{j=0}^{47}\frac{z^{2j+1}}{2j+1}+r,
 \quad z=(m-1)/(m+1),\quad
 0\le r\le\frac{2z^{97}}{97(1-z^2)}.
\]

All operations and the remainder bound are outward. An independent rational
series checks the logarithm implementation at fixed test inputs. Complete
covering is checked when the eight execution segments are combined: no gap,
overlap, mixed parameters, missing layer, or altered coefficient table is
accepted. Partial executions are not global sign certificates.

### 7.3 Certified signs and their exact meaning

Let `A(delta)=sum_{k=0}^6 A_{3,k}(delta)` for this witness. The outward bounds,
displayed here with extra outward decimal rounding, are

\[
 (A_{3,1}+A_{3,5})''\in[-0.086786714070,-0.007332534473]
                                      \subset(-\infty,-1/150),
\]
\[
 A''\in[4.267649730085,4.489398095299]\subset(4,\infty).
                                                                    \tag{18}
\]

Both are uniform throughout the stated `delta` interval, not samples at its
center. For the fixed chord with endpoints `+-h_0`, twice integrating these
bounds gives

\[
 \frac{(A_{3,1}+A_{3,5})(-h_0)+(A_{3,1}+A_{3,5})(h_0)}2
 -(A_{3,1}+A_{3,5})(0)<-h_0^2/300<0,
\]
\[
 \frac{A(-h_0)+A(h_0)}2-A(0)>2h_0^2>0.                      \tag{19}
\]

The second expression is exactly the midpoint gap of the **full** `J_3`.
The six external coordinates and both center completions have all been
retained before selecting layers. The first expression disproves
complement-paired, noise-integrated layer convexity; the second prevents it
from being misreported as a complete-`J_3` counterexample.

Separately, at `u=1`, the full Shannon formula (4), using the same entire
`delta` interval and all 128 atoms, certifies

\[
 H_7''\in[-32.045785638019,-31.138133309497]<0.                \tag{20}
\]

Neither (18) nor (20) is promoted to an entropy-rate derivative. The accepted
rate-value allowance still has to be paid for a proposed rate counterexample;
none is claimed here.

## 8. What has and has not been eliminated

The growing-family result is stronger than a negative single-word curvature,
a non-DPP partition example, or a degree-two/radius-one mismatch. It fixes the
original S-sine density and endpoints, uses the exact aligned approximants,
and proves an order-one adverse count-layer budget. The finite witness retains
full Fisher and acceleration, is stable on an interval, and remains adverse
after complementary-layer pooling and the actual noise-time integration.

This eliminates **only** the specified layerwise / negligible-negative-layer
interfaces. It does not eliminate direct full-sum compensation, transport
between count layers, parameter-dependent regroupings with their correct
weight derivatives, or a different nonlocal representation. It does not prove
that every successful method must average across all words.

The exact unresolved full obligation is still (1) together with
`liminf G_R>=0` on every fixed legal chord. Theorem B makes the boundary
particularly explicit: the negative and positive masses have separate
nonzero limits, and one must compare those full limits rather than declaring
the negative part negligible. This comparison is not supplied here.

Finite probes are classified separately in `PROBES.md`; their absence of a
complete sign violation is not a theorem. Source review, author proof,
finite outward certification, and future independent review remain distinct.
