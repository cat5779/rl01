# S54 cycle07 — Conditional-likelihood projection and paired spectral payment

## Strongest theorem first

### Theorem S54 (strict paid improvement for the actual signed output KL)

Fix any `0<c<1`, let `n=2k` tend to infinity through even integers, and use exactly the laws, normalization, count weights, and layer clock in the assignment. Put

\[
\rho_c=1-\frac{c^2\log c}{2b},\qquad
D_c=\frac{\rho_c-1-\log\rho_c}{2},\qquad
M_b=\frac{2e^{-1/2}}{\sqrt{2\pi}\,b},
\]

and define the new posterior-variance and entropy-payment constants

\[
\tau_c^{\rm post}
 :=\frac{(1-c^2)(5c^2+3)}{(1+c^2)(c^2+3)},
\qquad
 a_c:=\frac{\rho_c-1}{2\rho_c},
\qquad
 d_c:=1-2a_c\tau_c^{\rm post},
\]

\[
\boxed{
\Delta_c
 :=\frac1{\sqrt{\rho_c d_c}}
 \left(
   \frac{a_c\tau_c^{\rm post}}{d_c}
   +\frac12\log d_c
 \right)>0.}
\tag{T1}
\]

Then, for every fixed finite `K`,

\[
\boxed{
\liminf_{n\to\infty}
\inf_{|l-k|\le K\sqrt n}
\left\{
D(p_l^H\Vert q_l^G)-U_{n,l}(c)
\right\}
\ge \Delta_c,}
\tag{T2}
\]

and hence

\[
\boxed{
\limsup_{n\to\infty}
\sup_{|l-k|\le K\sqrt n}
U_{n,l}(c)
\le D_c-\Delta_c.}
\tag{T3}
\]

Using the actual signed coefficients `kappa_l`, their reviewed positive/negative mass, and the reviewed all-layer quadratic tail payment gives

\[
\boxed{
\liminf_{n\to\infty}\Psi_n(c)
\ge -M_b\bigl(D_c-\Delta_c\bigr).}
\tag{T4}
\]

This is a strict improvement over the reviewed lower bound `-M_b D_c` for every fixed `0<c<1`.

At `c=19/20`,

\[
\begin{aligned}
\rho_c&=1.9495835525079867983\ldots,\\
D_c&=0.14098388277826699493\ldots,\\
M_b&=19.854008165673300496\ldots,\\
\tau_c^{\rm post}&=0.09865555032699985942\ldots,\\
\Delta_c&=0.00045242392331566235904\ldots,
\end{aligned}
\]

so

\[
\boxed{
\liminf_{n\to\infty}\Psi_n(19/20)
\ge -2.7901127316401852086\ldots.}
\tag{T5}
\]

The previous loss was `2.7990951599080403202...`; the rigorous formula improves it by

\[
M_b\Delta_c=0.00898242826785511160\ldots.
\tag{T6}
\]

Consequently, in the already reviewed compensated ledger, the corresponding sufficient S52 threshold would become the strict condition

\[
\liminf R_n(c)/n>-1.2098872683598147914\ldots
\quad(c=19/20),
\]

not a boundary equality.

**Status:** (T1)–(T6) are **PROVED**, conditional only on the explicitly reviewed cycle03/cycle05 inputs listed in the assignment and the standard strong-Rayleigh concentration theorem quoted below. No computation is used as an asymptotic premise.

---

## 1. Reusable tool I: conditional-likelihood projection

It suffices first to treat `l<=k`; the exact complement symmetry gives the other half.

Let

\[
J_H(A,S)=\nu(A)T_l^H(S\mid A),\qquad
J_G(A,S)=\nu(A)T_l^G(S\mid A),
\]

where

\[
T_l^G(S\mid A)=\frac{z^{|A\cap S|}}{Z_l(z)},\qquad |S|=l.
\]

Write

\[
R=|S\cap A^c|=l-|A\cap S|,
\]

and let `p_l^H` and `q_l^G` be the two radial laws. Both conditional channels are uniform inside every overlap orbit, so

\[
\frac{dJ_H}{dJ_G}(A,S)
 =h_{n,l}(R),
\qquad
h_{n,l}(r):=\frac{p_l^H(r)}{q_l^G(r)}.
\tag{1.1}
\]

For a spatial output `S`, let

\[
Q_{n,l,S}:=\operatorname{Law}_{J_G}(R\mid S).
\]

Then the actual output likelihood ratio in the required direction is

\[
\frac{\mu_l(S)}{\gamma_l(S)}
 =E_{Q_{n,l,S}}h_{n,l}(R).
\tag{1.2}
\]

For a probability law `Q` and a nonnegative function `h`, set

\[
\operatorname{Ent}_Q(h)
 :=E_Q[h\log h]-(E_Qh)\log(E_Qh).
\]

Taking entropy before and after the conditional projection in (1.2) gives the exact identity

\[
\boxed{
D(p_l^H\Vert q_l^G)-D(\mu_l\Vert\gamma_l)
 =E_{\gamma_l}
   \operatorname{Ent}_{Q_{n,l,S}}(h_{n,l}).}
\tag{CLP}
\]

This is the **conditional-likelihood projection (CLP) identity**. It preserves the KL orientation required in the assignment: throughout, the output term is `D(mu_l || gamma_l)`, never the reverse KL.

Two elementary localization inequalities make CLP reusable:

1. For every event `A`,
   \[
   \operatorname{Ent}_Q(h)
   \ge Q(A)\operatorname{Ent}_{Q(\cdot\mid A)}(h).
   \tag{1.3}
   \]
   This follows by decomposing over `A,A^c` and using convexity of `x log x` for the two conditional means.

2. One also has the rough but sometimes useful Hellinger payment
   \[
   \operatorname{Ent}_Q(h)\ge \operatorname{Var}_Q(\sqrt h).
   \tag{1.4}
   \]
   Indeed, `x log x-x+1 >= (sqrt(x)-1)^2` and `E h` is the normalizing mean.

The proof below uses the sharper localized entropy in (1.3), not merely (1.4).

**Status:** CLP, (1.3), and (1.4) are **PROVED** exactly.

---

## 2. Exact Gibbs posterior and its Poisson-binomial variance

The reviewed Cauchy–Binet identity gives

\[
\gamma_l(S)=\frac{\det[I+(z-1)P]_S}{Z_l(z)},
\qquad
\nu^G(A\mid S)
 =\frac{\nu(A)z^{|A\cap S|}}
        {\det[I+(z-1)P]_S}.
\tag{2.1}
\]

Let `lambda_1,...,lambda_l` be the eigenvalues of `P_S`. Under the posterior in (2.1), with `X=|A cap S|`,

\[
E[w^X\mid S]
 =\frac{\det(I+(zw-1)P_S)}
        {\det(I+(z-1)P_S)}
 =\prod_{i=1}^l
 \left(
 1-\frac{z\lambda_i}{1+(z-1)\lambda_i}
 +\frac{z\lambda_i}{1+(z-1)\lambda_i}w
 \right).
\tag{2.2}
\]

Thus `X|S` is exactly Poisson-binomial. Equivalently, `R=l-X` is a sum of independent Bernoulli variables with parameters

\[
r_i=\frac{1-\lambda_i}{1+(z-1)\lambda_i}.
\tag{2.3}
\]

Write

\[
M_S=E(R\mid S)=\sum_i r_i,
\qquad
V_S=\operatorname{Var}(R\mid S)=\sum_i r_i(1-r_i).
\tag{2.4}
\]

The Fourier half-projection satisfies

\[
D_S P_S D_S=I_S-P_S,
\qquad D_{jj}=(-1)^j,
\tag{2.5}
\]

so the spectrum of `P_S` is paired under `lambda <-> 1-lambda`.

---

## 3. Reusable tool II: a sharp paired mean–leakage certificate

For one spectral pair `lambda,1-lambda`, put

\[
u=(2\lambda-1)^2\in[0,1],
\qquad
\chi=\frac{2c}{1+c^2}.
\]

Let `m_c(u)` be the pair contribution to the posterior mean `M_S`, `v_c(u)` the pair contribution to `V_S`, and `t(u)` the pair contribution to

\[
T(S):=\operatorname{Tr}(P_S(I-P_S))
     =\sum_{i\in S,j\notin S}|P_{ij}|^2.
\tag{3.1}
\]

Direct substitution into (2.3) gives

\[
 m_c(u)=
 \frac{(1-c)^2}{1+c^2}
 \frac{1+\chi u}{1-\chi^2u},
\tag{3.2}
\]

\[
 t(u)=\frac{1-u}{2},
\tag{3.3}
\]

\[
 v_c(u)=
 \frac{(1-c^2)^2}{2(1+c^2)^2}
 (1-u)\frac{1+\chi^2u}{(1-\chi^2u)^2}.
\tag{3.4}
\]

Define

\[
\mathsf A_c=
\frac{(1-c^2)^2(11c^2+9)}
     {4c(1+c^2)(c^2+3)},
\qquad
\mathsf B_c=
\frac{18(1-c^2)^2}{(c^2+3)^2}.
\tag{3.5}
\]

The following identity is the central algebraic tool:

\[
\begin{aligned}
&v_c(u)-\mathsf A_c\bigl(1-m_c(u)\bigr)
          +\mathsf B_c t(u)\\
&\quad=
\frac{4c^4(1-c^2)^2(1-u)(6u-1-c^2)^2}
{(c^2+3)^2\bigl((1+c^2)^2-4c^2u\bigr)^2}
\ge0.
\end{aligned}
\tag{3.6}
\]

Therefore, summing over all spectral pairs (and assigning half weight to a self-paired eigenvalue `1/2` when `l` is odd),

\[
\boxed{
V_S\ge
\mathsf A_c\left(\frac l2-M_S\right)
-\mathsf B_c T(S).}
\tag{PPVC}
\]

This is the **paired posterior-variance certificate (PPVC)**.

It is sharp if one knows only the pair-averaged posterior mean and leakage. Equality in (3.6) occurs at

\[
u=1,
\qquad
u_0=\frac{1+c^2}{6}.
\]

The central target pair moments are attained by the mixture placing weight

\[
\omega_c=\frac{3+c^2}{5-c^2}
\]

at `u_0` and the remaining weight at `u=1`. Hence no uniformly stronger lower bound can be obtained from only these two spectral moments; further improvement along this route requires additional information about the actual compression spectrum of `P_S`.

**Status:** PPVC and its two-moment sharpness statement are **PROVED** by the displayed factorization.

---

## 4. The central spatial leakage is deterministic at scale `n`

We next establish the two typical quantities entering PPVC.

### 4.1 Exact two-point interpolation

For `l<=k`, let

\[
u_{2,l}=\frac{l(l-1)}{n(n-1)},
\qquad
\alpha_l=\frac{l(l-1)}{k(k-1)},
\qquad
w_{ij}=|P_{ij}|^2.
\]

The principal-minor generating polynomial is

\[
F(x_1,\ldots,x_n)
 =\det(I+[I+(z-1)P]\operatorname{diag}x)
 =\sum_S\det[I+(z-1)P]_S x^S.
\]

At `x_i=t`,

\[
F(t)=(1+t)^k(1+zt)^k.
\]

Differentiating twice at distinct `i,j`, and using

\[
[I+(z-1)P](I+t[I+(z-1)P])^{-1}
 =\frac1{1+t}(I-P)+\frac z{1+zt}P,
\]

shows that the coefficient of `w_ij` in the `l`-slice two-point function is

\[
-\frac{(z-1)^2[t^{l-2}](1+t)^{k-2}(1+zt)^{k-2}}{Z_l(z)}
=-\alpha_l\theta_{n,l}(z).
\]

The constant term is fixed by `sum_{i\ne j}Y_iY_j=l(l-1)`. Consequently

\[
\boxed{
E_{\gamma_l}Y_iY_j
 =u_{2,l}+\theta_{n,l}
 \left[
 \alpha_l\left(\frac14-w_{ij}\right)-u_{2,l}
 \right].}
\tag{4.1}
\]

Thus every quadratic statistic has the exact interpolation between the uniform slice and `q_l^max` with coefficient `theta_{n,l}`. This is where the exact layer-dependent clock coefficient enters the new proof.

### 4.2 Mean of `T`

The projection identities give

\[
\sum_{i\ne j}w_{ij}=\frac n4.
\tag{4.2}
\]

For the cyclic half-Fourier projection, the exact fourth-power sum is

\[
\sum_{i\ne j}w_{ij}^2
 =\frac n{48}+\frac1{6n}.
\tag{4.3}
\]

Using (4.1),

\[
E_{u_l}T=\frac{l(n-l)}{4(n-1)},
\tag{4.4}
\]

\[
E_{q_l^{\max}}T
 =\frac l4-
 \alpha_l\left(\frac n{24}-\frac1{6n}\right),
\tag{4.5}
\]

and exactly

\[
E_{\gamma_l}T
 =(1-\theta_{n,l})E_{u_l}T
 +\theta_{n,l}E_{q_l^{\max}}T.
\tag{4.6}
\]

On every fixed window `|l-k|<=K sqrt(n)`, the reviewed Gibbs saddle estimates give

\[
\theta_{n,l}\longrightarrow c^2
\]

uniformly. Therefore

\[
\boxed{
\frac1nE_{\gamma_l}T
 \longrightarrow
 t_c:=\frac{3+c^2}{48}}
\tag{4.7}
\]

uniformly on each such window.

### 4.3 Concentration of `T`

The law `gamma_l` is a fixed-size determinantal `L`-ensemble and hence is strong Rayleigh. Toggling one coordinate changes `T` by at most

\[
\sum_{j\ne i}|P_{ij}|^2=\frac14.
\]

The strong-Rayleigh Lipschitz concentration theorem therefore yields, for every fixed `epsilon>0`,

\[
\sup_{|l-k|\le K\sqrt n}
\gamma_l\left(
\left|\frac{T}{n}-t_c\right|>\epsilon
\right)\longrightarrow0.
\tag{4.8}
\]

This is not a central-limit discard of other layers; it is a concentration statement used only inside a fixed central window. The actual count-weight complement is paid later by the reviewed tail ledger.

---

## 5. Typical posterior mean and the improved variance floor

Let

\[
\bar r_{n,l}:=E_G R.
\]

The reviewed central Gibbs saddle estimate gives, uniformly for `l=k-r` with `0<=r<=K sqrt(n)`,

\[
\bar r_{n,l}=qk-\frac r2+O_K(1),
\tag{5.1}
\]

so

\[
\frac1n\left(\frac l2-\bar r_{n,l}\right)
\longrightarrow\frac c4.
\tag{5.2}
\]

By total variance under the Gibbs joint law,

\[
E_{\gamma_l}M_S=\bar r_{n,l},
\qquad
\operatorname{Var}_{\gamma_l}(M_S)
 \le\operatorname{Var}_G(R)=nv_G+o_K(n),
\quad v_G=\frac b4=\frac{1-c^2}{16}.
\tag{5.3}
\]

Hence, for every fixed `L`,

\[
\gamma_l\left(
|M_S-\bar r_{n,l}|>L\sqrt{nv_G}
\right)
\le L^{-2}+o_K(1).
\tag{5.4}
\]

On the intersection of the events in (4.8) and (5.4), PPVC gives

\[
\frac{V_S}{n}
\ge
\mathsf A_c\frac c4-\mathsf B_c t_c-o_{K,L,\epsilon}(1)
-\mathsf B_c\epsilon.
\tag{5.5}
\]

The main term simplifies exactly to

\[
\mathsf A_c\frac c4-\mathsf B_c t_c
=rac{(1-c^2)^2(5c^2+3)}
       {16(1+c^2)(c^2+3)}.
\tag{5.6}
\]

After division by `v_G`, this is precisely

\[
\boxed{
\frac{V_S}{nv_G}
\ge \tau_c^{\rm post}-o(1),
\qquad
\tau_c^{\rm post}
=\frac{(1-c^2)(5c^2+3)}
       {(1+c^2)(c^2+3)}.}
\tag{5.7}
\]

The good event has `gamma_l`-probability at least `1-L^{-2}-o(1)`.

For the later Gaussian entropy formula one also needs a subcritical upper bound. Since `R|S` is Poisson-binomial,

\[
V_S\le M_S.
\]

On the same mean-good event,

\[
\frac{V_S}{nv_G}
\le \frac4{1+c}+o(1).
\tag{5.8}
\]

This remains below the Gaussian integrability threshold:

\[
2a_c\frac4{1+c}<1.
\tag{5.9}
\]

Indeed, (5.9) is equivalent to `rho_c<4/(3-c)`, which in turn is equivalent to

\[
-\log c<\frac{(1-c)(1+c)^2}{2c^2(3-c)}.
\]

For

\[
F(c)=\frac{(1-c)(1+c)^2}{2c^2(3-c)}+\log c,
\]

one has `F(1)=0` and

\[
F'(c)=
\frac{(c-1)^2(c^2-6c-3)}{c^3(c-3)^2}<0
\quad(0<c<1),
\]

so `F(c)>0` for `c<1`.

---

## 6. Gaussian entropy payment from the exact radial likelihood

Put

\[
\sigma_n^2=nv_G,
\qquad
x=\frac{r-\bar r_{n,l}}{\sigma_n}.
\]

The reviewed exact-clock radial analysis gives, uniformly for `|l-k|<=K sqrt(n)` and bounded `x`,

\[
q_l^G(r)
 =\frac{1+o(1)}{\sqrt{2\pi nv_G}}e^{-x^2/2},
\tag{6.1}
\]

while the heat overlap is Poisson-binomial with

\[
\frac{\operatorname{Var}_H R}{n}\to v_H,
\qquad
\frac{v_H}{v_G}=\rho_c,
\qquad
E_HR-E_GR=O(1),
\tag{6.2}
\]

and satisfies the corresponding uniform local central limit theorem. Therefore

\[
\boxed{
h_{n,l}(r)
 =\frac{p_l^H(r)}{q_l^G(r)}
 \longrightarrow
 h_c(x):=\rho_c^{-1/2}e^{a_cx^2}}
\tag{6.3}
\]

locally uniformly in `x` and uniformly on every fixed central layer window.

Now consider any sequence of posterior laws `Q_{n,l,S}` on the good event. By (2.2), these are Poisson-binomial. By (5.7), their variance is at least a fixed positive multiple of `n`; hence the uniform Poisson-binomial local CLT applies. After passing to a subsequence,

\[
\frac{M_S-\bar r_{n,l}}{\sigma_n}\to\xi,
\qquad
\frac{V_S}{\sigma_n^2}\to\tau,
\]

with

\[
|\xi|\le L,
\qquad
\tau\ge\tau_c^{\rm post},
\qquad
2a_c\tau<1
\]

by (5.8)–(5.9).

Use the localization inequality (1.3) on a bounded standardized interval and then let the interval grow. Equations (6.3) and the posterior local CLT imply

\[
\liminf
\operatorname{Ent}_{Q_{n,l,S}}(h_{n,l})
\ge
\operatorname{Ent}_{N(\xi,\tau)}(h_c).
\tag{6.4}
\]

For `d=1-2a_c tau`, a direct Gaussian integral gives

\[
\begin{aligned}
\operatorname{Ent}_{N(\xi,\tau)}(h_c)
={}&\rho_c^{-1/2}d^{-1/2}
 e^{a_c\xi^2/d}\\
&\times\left[
\frac{a_c\tau}{d}
+\frac12\log d
+\frac{2a_c^2\tau\xi^2}{d^2}
\right].
\end{aligned}
\tag{6.5}
\]

The expression is increasing in `xi^2`. At `xi=0`, writing `x=a_c tau` and `d=1-2x`, the remaining factor is

\[
G(x)=d^{-1/2}\left(\frac{x}{d}+\frac12\log d\right).
\]

The bracket is positive for `x>0`, since its derivative is `2x/d^2`; moreover

\[
G'(x)=d^{-5/2}
\left[
 d\left(\frac{x}{d}+\frac12\log d\right)+2x
\right]>0.
\tag{6.6}
\]

Thus (6.5) is minimized, under the good-event constraints, at `xi=0` and `tau=tau_c^post`. Its minimum is exactly `Delta_c` in (T1).

The subsequence argument also proves uniformity over all good `S` and all `|l-k|<=K sqrt(n)`. Combining with the good-set probability and then taking `n->infinity`, `L->infinity`, and `epsilon->0` in that order gives

\[
D(p_l^H\Vert q_l^G)-U_{n,l}(c)
\ge\Delta_c-o_K(1)
\tag{6.7}
\]

uniformly on every fixed central window. The reviewed radial convergence to `D_c` now proves (T2)–(T3).

**Consequence:** asymptotic saturation of the radial data-processing bound is impossible for these actual laws. The statement that the central spatial output could have `U_{n,l}->D_c` is **DISPROVED**; there is a uniform positive loss `Delta_c`.

---

## 7. Paying the actual signed count sum and all noncentral layers

The reviewed actual-count ledger supplies

\[
\frac1n\sum_l(\kappa_l)_+\to M_b,
\qquad
\sum_l\kappa_l=0,
\tag{7.1}
\]

so the negative mass has the same limit (here `(\kappa_l)_-=\max\{-\kappa_l,0\}`). It also supplies the genuine all-layer estimate

\[
\frac1n\sum_{|l-k|>K\sqrt n}
|\kappa_l|
\left(1+\frac{(l-k)^2}{n}\right)
\le\frac{C_c}{K^2},
\tag{7.2}
\]

and the output envelope

\[
U_{n,l}(c)
\le C_c\left(1+\frac{(l-k)^2}{n}\right)
\tag{7.3}
\]

on every layer, with the four endpoint entries equal to zero.

For fixed `K`, use `U>=0` on positive coefficients and (T3) on negative central coefficients. The complementary contribution is paid by (7.2)–(7.3):

\[
\begin{aligned}
\Psi_n(c)
&=\frac1n\sum_l\kappa_lU_{n,l}(c)\\
&\ge
-\bigl(D_c-\Delta_c+o_K(1)\bigr)
  \frac1n\sum_{|l-k|\le K\sqrt n}(\kappa_l)_-
-\frac{C_c}{K^2}.
\end{aligned}
\tag{7.4}
\]

Take first `n->infinity`, then `K->infinity`. Equations (7.1)–(7.4) give (T4).

This step uses the actual `kappa_l`; in particular, the balanced-amplitude derivative term hidden inside the exact identity

\[
\kappa_l=
\left(\frac{(l-k)^2}{b^2}-\frac nb\right)\pi_l
+\frac{2c}{b}\dot\pi_l
\]

is not dropped, differentiated through, or replaced by Gaussian weights.

---

## 8. Status of the substantive conclusions

1. **PROVED — new reusable mechanism.** The CLP identity (CLP) converts radial-to-output KL loss into an average posterior entropy Jensen gap in the correct direction `D(mu||gamma)`.
2. **PROVED — exact posterior structure.** The Gibbs posterior overlap is Poisson-binomial with parameters determined by the compression spectrum of `P_S`.
3. **PROVED — new sharp spectral certificate.** PPVC gives a factored, two-moment-sharp lower bound on posterior overlap variance using the posterior mean and the spatial leakage `T(S)`.
4. **PROVED — strict central KL loss.** The actual central output KL is at most `D_c-Delta_c+o(1)` uniformly on every fixed `sqrt(n)` layer window.
5. **PROVED — quantitative signed improvement.** At `c=.95`,
   \[
   \liminf\Psi_n\ge-2.790112731640185\ldots,
   \]
   improving the reviewed `-2.799095159908040...` bound by `0.008982428267855...`.
6. **DISPROVED — asymptotic radial saturation.** The actual output channel cannot asymptotically retain all of the radial KL on central layers.
7. **INCOMPLETE — zero cancellation target.** This proof does not establish `Psi_n->0`, `liminf Psi_n>=0`, or a full limiting layer profile `U_c(y)`.
8. **INCOMPLETE — corrected midpoint concavity.** The theorem only improves the output-KL component in the reviewed compensated ledger. It does not prove the needed S52 susceptibility bound and does not justify a boundary equality.
9. **INCOMPLETE / out of scope — ultimate true-law target.** Nothing here alone proves full-configuration Shannon entropy-rate concavity for the true sine Toeplitz family.

---

## 9. Source boundary and references read

All five required repository paths were accessible and read on branch
`research/sa-cycle07-s54-20260918`:

1. `research/CYCLE07_20260918/sources/S43_CYCLE05_RESULT.md`
2. `research/INDEPENDENT_REVIEW_20260918/S43_CYCLE05.md`
3. `research/CYCLE04_20260918/recovered/S43_cycle03/S43_CYCLE03_MISSING_PROOF.md`
4. `research/INDEPENDENT_REVIEW_20260918/S43_CYCLE03.md`
5. `research/CYCLE04_20260918/recovered/S43_cycle03/S43_RESULT.md`

External standard inputs used:

- J. Borcea, P. Brändén, T. Liggett, *Negative dependence and the geometry of polynomials*, JAMS 22 (2009), arXiv:0707.2340: determinantal measures and finite symmetric exclusion are strong Rayleigh.
- R. Pemantle, Y. Peres, *Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures*, Combinatorics, Probability and Computing 23 (2014), arXiv:1108.0687: Gaussian concentration for Lipschitz observables under strong-Rayleigh laws.

The accompanying script is diagnostic. It checks the exact factorization, constants, finite principal-minor normalization, the two-point `T` formula, and PPVC on small slices. It is not independent certification and is not used to infer any asymptotic statement.
