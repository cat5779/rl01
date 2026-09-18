# PRO01, second research round: a positive Ward–Stein chord kernel

**Status: PROVED, with proofs below, for the finite representation, infinite identification, effective approximation, and the interval `0 < c <= sqrt(3)/2`. INCOMPLETE for the sign at `c = 19/20` and for the whole interval `0 < c < 1`. Pending fresh independent review.**

This report supersedes neither the frozen SA03 inputs nor their scoped `SOL_REVIEW.md`. It does not certify the first-round report. The first-round degree/local certificate is an auxiliary approximation lemma, not a completed high-contrast sign tool. The present construction is different: an exact positive reversible Stein operator, an explicit score potential, and a positive single-flip chord budget. No weak-coupling series is extrapolated to large contrast.

## 0. Results and limitations

Put `r=c^2`. Under precisely the infinite unsmoothed sine DPP law in the assignment, let `q` be the full external posterior of the observed central bit, `q^j` its value after flipping external bit `j`, and `v=G b` the usual Schur response. Let

\[
\ell(p)=\log\frac p{1-p},\qquad
[\ell]_{p,t}=\begin{cases}(\ell(t)-\ell(p))/(t-p),&t\ne p,\\
1/[p(1-p)],&t=p.
\end{cases}
\]

### PROVED — the new representation

For every fixed `0<c<1`,

\[
\boxed{\Gamma(c)=\frac4{1-r}
 -\mathbb E_{\infty,c}\sum_{j\ne0}|v_j|^2[\ell]_{q,q^j}.}\tag{0.1}
\]

The notation `E_{infinity,c}` means the **actual** infinite DPP with kernel
`K=(I+cJ)/2`, where `J=2Q-I` and `Q=T(1_{[-1/4,1/4]})`. It is the assignment's law at `u=1`, not a surrogate. The disappearance of the `u` integral is an exact finite entropy-production/ Ward-identity calculation followed by a proved limit; see Section 6. In particular it is not an identification of the local production functional with normalized block entropy by assertion.

Every summand being subtracted is nonnegative. The sum is absolutely convergent. More usefully, define

\[
m=\frac{2q-1}{c},\quad
\kappa_j=\frac{1-r}{r}|v_j|^2,\quad f_c(t)=\operatorname{atanh}(ct),
\]
\[
\boxed{\mathcal B_c(z)=c\sum_{j\ne0}\kappa_j(z)
 [f_c]_{m(z),m(z^j)}.}\tag{0.2}
\]

Then

\[
\boxed{\Gamma(c)=\frac4{1-r}(1-\mathbb E\mathcal B_c),\qquad
\kappa_j\ge0,\quad\sum_j\kappa_j=1-m^2,\quad |m|\le c.}\tag{0.3}
\]

Thus the precise all-contrast obstruction is the **averaged** inequality
`E B_c < 1`, not solvability of an unspecified Poisson equation.

### PROVED — a dimension-free one-sided theorem and a non-perturbative sign interval

Define the elementary scalar envelope

\[
b(r)=\max_{0\le x\le r}
 \frac{(r-x^2)(\operatorname{atanh}r-\operatorname{atanh}x)}{r-x},
\quad B_r(r):=\frac r{1+r}.\tag{0.4}
\]

This is an explicit one-variable function, independent of any DPP expectation or unknown target. For all `0<c<1`,

\[
\boxed{\frac{4(1-b(c^2))}{1-c^2}\le\Gamma(c)\le\frac4{1-c^2}.}\tag{0.5}
\]

The same inequality holds for `-4 H''(0)/n` for **every finite Hermitian projection** `Q` with all diagonal entries `1/2`, with `K_d=(I+c(2Q-I)+dI)/2`. It does not require a Toeplitz kernel or a bipartite matrix.

An executed exact-rational polynomial certificate proves

\[
b(3/4)<997/1000.
\]

The envelope is increasing in `r`. Consequently

\[
\boxed{\Gamma(c)\ge\frac{3}{250(1-c^2)}>0
\quad\text{for }0<c\le\sqrt3/2.}\tag{0.6}
\]

The decimal `sqrt(3)/2 ≈ 0.866025` is only a description of the endpoint; the theorem uses the exact endpoint. This is a weaker-contrast theorem, **not** a proof at `19/20`.

At the requested benchmark the separately executed certificate gives
`b(361/400)<1587/1000`, hence

\[
\boxed{-\frac{4696}{195}\le\Gamma(19/20)\le\frac{1600}{39}.}\tag{0.7}
\]

This interval, approximately `[-24.0821,41.0257]`, does not determine the sign. It is stated to quantify the remaining gap, not to advertise a benchmark solution.

### PROVED — an explicit finite representation with a target-independent error

Section 7 defines `Gamma_M^+` using only true `2M`-bit DPP marginal probabilities and finite matrices obtained from an explicit all-occupied reference resolvent. There is no infinite linear solve in its definition. With the explicit constants and column-tail function `t_c(M)` given there,

\[
\boxed{|\Gamma-\Gamma_M^+|
\le 2aW D_1t_c(M)+(D_1+W^2D_2)t_c(M)^2,}\tag{0.8}
\]

where

\[
a=\frac2{1-c},\quad W=\frac c{\sqrt{1-c^2}},\quad
D_1=\frac4{1-c^4},\quad D_2=\frac{16c^2}{(1-c^4)^2}.
\]

The spatial-index tail alone costs `D_1 t_c(M)^2`. Unlike V14 truncation, the new representation needs no double-flip spatial-tail estimate after the exact transformation. This is not a claimed new rate for the original aligned Fejer sequence `A_R''`.

### DISPROVED — the tempting pointwise closure

`B_c(z)<=1` is false in the general finite projection class, already at `c=19/20`. Section 9 gives a rational `32`-site half-rank projection and an exact-rational logarithm certificate proving `B_c(z)>117/100`. Thus positive Markov rates and projection covariance row sums do **not** automatically finish the sign proof. An averaged argument is genuinely necessary for the general class.

## 1. Domain, conventions, and external transfer mechanism

### 1.1 Fixed target

The target remains the assignment's `Gamma(c)`, obtained from the actual Fejer DPP, actual posterior, and full differentiation of its probability weights. Write

\[
Q=T(1_{[-1/4,1/4]}),\quad J=2Q-I,\quad
J_{ij}=\frac{2\sin(\pi(i-j)/2)}{\pi(i-j)}\ (i\ne j),\quad J_{ii}=0.
\]

Then `J=J*`, `J^2=I`. In the finite auxiliary theorem, `J=2Q-I` for an arbitrary finite projection of constant diagonal `1/2`. The spin bias `d` used below is **twice** the kernel-diagonal bias. At the original noise layer, `d=2u delta`. This factor is retained in Section 6.

Latent spins are `X_i in {-1,1}` with projection-DPP law. Observed spins are `S_i=2Y_i-1`. The channel is

\[
\Pr(S_i=s_i\mid X)=\frac{1+s_i(d_i+cX_i)}2.\tag{1.1}
\]

Conditional independence in (1.1) does not make the observed physical word independent. The resulting observed DPP kernel for common `d_i=d` is `K_d=(I+cJ+dI)/2`. To check this identification directly, write `Z_i=(1+X_i)/2` and `alpha=(1-c+d)/2`. For any subset `A`, conditional independence followed by the principal-minor determinant expansion gives

\[
E\prod_{i\in A}Y_i
=E\prod_{i\in A}(\alpha+cZ_i)
=\det(\alpha I_A+cQ_A).
\]

These inclusion probabilities identify the finite binary law. Separate biases give the same argument with the diagonal entries `alpha_i=(1-c+d_i)/2`. The common-bias model is strictly admissible for `|d|<1-c`.

### 1.2 Transfer: exchangeable-pair Stein identities, not signed dissipation

The source mechanism is reversible exchangeable-pair integration by parts: an explicit function whose generator drift equals a score converts a moving-law derivative into an edge expectation. Chatterjee's exchangeable-pair treatment gives this mechanism in an abstract form [C, Lemma 3.1]. We prove the exact finite identity needed here directly.

The correspondence is:

* the state is the actual external physical word;
* the positive reversible edge rates are posterior-predictive rates, not the old signed transport rates;
* total observed magnetization is an explicit Poisson potential;
* the score source includes the unobserved central posterior;
* a Bayes edge-reversal identity converts the conductance into nonnegative posterior covariance weights;
* the nonlinear test function is the actual central log odds.

What does not transfer automatically is positivity of the resulting curvature. The Stein identity gives a **positive budget subtracted from** an explicit positive term. Its budget can exceed one pointwise. The new ingredients are the fixed-count Ward identity, the covariance/chord conversion, and the projection energy identity. No spectral-gap estimate, mixing theorem, concentration theorem, or unproved Poisson solution is imported.

No priority claim is made. The construction and its proofs below are self-contained apart from the explicitly identified frozen V14 interface used to recognize the original infinite target.

## 2. PROVED — fixed-count Ward identities, including all moving weights

Let `n` be even and let the latent law be any law supported on
`sum_i X_i=0`. In this section it need not be determinantal. Set `r=c^2` and `M=sum_i s_i`.

For a fixed balanced latent word, at `d=0`,

\[
\partial_d\log\Pr(S=s\mid X)
=\sum_i\frac{s_i}{1+cs_iX_i}
=\frac{M-c\sum_iX_i}{1-r}=\frac M{1-r}.\tag{2.1}
\]

Averaging over the latent law preserves this identity. Thus the **actual** word mass `p_d(s)` satisfies

\[
\boxed{\frac{p'_0(s)}{p_0(s)}=\frac M{1-r},\qquad
\sum_s\frac{p'_0(s)^2}{p_0(s)}=\frac n{1-r}.}\tag{2.2}
\]

For the second assertion, conditional on `X`, the observed spins have mean `cX_i`, variance `1-r`, and are independent. The conditional mean of their sum is zero. Hence `E M^2=n(1-r)`.

For clarity about second derivatives, define on mass arrays

\[
(\mathsf A p)(s)=\frac12\sum_i s_i[p(s)+p(s^i)].\tag{2.3}
\]

Differentiating the channel coordinate by coordinate gives `p'=A p`. Its coordinate actions have square zero and commute at distinct coordinates. Therefore

\[
 p''=\mathsf A^2p=\sum_{i\ne j}\mathsf A_i\mathsf A_jp.\tag{2.4}
\]

This is an **ordered double-flip** identity, not a Fisher-only differentiation. Direct differentiation of the likelihood also gives

\[
\boxed{p''_0(s)=\frac{M^2}{(1-r)^2}p_0(s)
 -\frac1{1-r}\sum_i p_0(s^i).}\tag{2.5}
\]

To verify (2.5), the complete log-likelihood second derivative is

\[
-\sum_i\frac1{(1+cs_iX_i)^2}
=-\frac{n(1+r)-2c\sum_i s_iX_i}{(1-r)^2}.
\]

The conditional flip likelihood ratio is
`(1+r-2cs_iX_i)/(1-r)`. Averaging it proves (2.5). In particular the exact entropy derivative is

\[
-H''(0)=\sum_s\frac{p'_0(s)^2}{p_0(s)}+\sum_s p''_0(s)\log p_0(s).\tag{2.6}
\]

The second term has not been removed.

### 2.1 An external word with one latent spin unobserved

Fix a center `i`. Write `C=[n]\\{i}`, `w_d(s_C)=Pr(S_C=s_C)`,
`m_d(s_C)=E[X_i|S_C=s_C]`, and `M_C=sum_{j in C}s_j`.
The latent count in `C`, conditional on `X_i=t`, is `-t`. Applying the preceding likelihood calculation conditionally gives

\[
\boxed{\frac{w'_0}{w_0}=\frac{M_C+cm}{1-r},\qquad
m'_0=\frac{c(1-m^2)}{1-r}.}\tag{2.7}
\]

Here and below a prime is the common external spin-bias derivative at zero. The second formula is the posterior covariance of `X_i` with the conditional likelihood score. It includes differentiation of the posterior denominator.

## 3. PROVED — a positive reversible generator with an explicit potential

Continue with the external word. Put

\[
a_j(s)=E[X_j\mid S_C=s],\qquad
 o_j(s)=\frac{w(s^j)}{w(s)},\qquad
\lambda_j(s)=1-cs_j a_j(s)=\frac{1-r}{2}(1+o_j(s)).\tag{3.1}
\]

The last identity follows by averaging the single-coordinate channel likelihood ratio. In particular `1-c <= lambda_j <= 1+c` and

\[
w(s)\lambda_j(s)=\frac{1-r}{2}[w(s)+w(s^j)]
=w(s^j)\lambda_j(s^j).
\]

Thus

\[
(\mathcal A_C f)(s)=\sum_{j\in C}\lambda_j(s)[f(s^j)-f(s)]\tag{3.2}
\]

is a strictly positive, reversible finite-state generator for the **actual external law**. Since `sum_{j in C}a_j=-m`,

\[
\boxed{\mathcal A_C M_C=-2(M_C+cm).}\tag{3.3}
\]

Consequently

\[
-\mathcal A_C\frac{M_C}{2(1-r)}=\frac{w'_0}{w_0}.\tag{3.4}
\]

A constant can be subtracted from the potential without changing (3.4). Its existence and its size are not unknown inputs. On the full word the same construction gives `A M=-2M` and the full score potential `M/[2(1-r)]`.

### 3.1 Covariance-weighted chord conversion

Assume now that the posterior latent covariances with the center are nonpositive, and define

\[
\kappa_j(s)=-\operatorname{Cov}(X_i,X_j\mid S_C=s)\ge0.
\]

The fixed latent count implies

\[
\sum_{j\in C}\kappa_j=1-m^2.\tag{3.5}
\]

Bayes updating at one observed coordinate gives, with `D_j=(1-r)o_j`,

\[
m(s^j)-m(s)=\frac{2cs_j\kappa_j(s)}{D_j(s)},\qquad
\kappa_j(s^j)=\frac{\kappa_j(s)}{o_j(s)^2}.\tag{3.6}
\]

For the covariance transformation, tilt the posterior by the flip likelihood ratio. Its two values, as a function of `X_j`, have product one. A two-by-two determinant, divided by the square of its normalizing mass, is therefore multiplied by `o_j^{-2}`. This proves the second identity even when the covariance is zero.

For any continuously differentiable scalar `f`, reversibility and (3.3) give

\[
- E[(M_C+cm)f(m)]
=\frac12E\sum_j\lambda_j s_j\,[f(m(s^j))-f(m)].\tag{3.7}
\]

Substitute (3.6). The right side becomes

\[
\frac c2 E\sum_j\kappa_j(1+o_j^{-1})[f]_{m,m^j}.
\]

Edge reversal is crucial: because `w(s^j)=w(s)o_j(s)` and the second identity in (3.6) holds,

\[
\sum_s w(s)\frac{\kappa_j(s)}{o_j(s)}[f]_{m,m^j}
=\sum_s w(s)\kappa_j(s)[f]_{m,m^j}.
\]

We obtain the exact positive-chord Stein identity

\[
\boxed{- E[(M_C+cm)f(m)]
=c E\sum_{j\in C}\kappa_j[f]_{m,m^j}.}\tag{3.8}
\]

This step is where changing weights are used to improve the expression. Replacing the weights by independent or frozen ones would invalidate it.

## 4. PROVED — projection posterior geometry and the entropy-curvature formula

### 4.1 Posterior covariances really have the required sign

Let `Q=VV*` with `V*V=I_{n/2}`. The latent occupation law is supported on sets of size `n/2`. Observing any noisy external word multiplies its atom weights by a strictly positive diagonal external field `D`. Cauchy–Binet gives the posterior projection

\[
P_D=D^{1/2}V(V^*DV)^{-1}V^*D^{1/2}.\tag{4.1}
\]

It is an orthogonal projection. Its two-site determinantal marginal gives

\[
\kappa_j=4|(P_D)_{ij}|^2\ge0,\qquad
\sum_{j\ne i}\kappa_j=4(P_D)_{ii}(1-(P_D)_{ii})=1-m^2.
\]

Thus no general negative-dependence theorem is needed for this use.

### 4.2 A sharper posterior interval from projection energy

For the observed kernel `K=(I+cJ)/2`, partition at the center and set

\[
B=K_C-\operatorname{diag}(1-Y_C),\quad G=B^{-1},\quad
b=K_{Ci},\quad v=Gb,\quad q=\tfrac12-b^*v.
\]

The usual gap bound ensures `B` is invertible. Let `x=(1,-v)` and let `D_0=diag(1-Y_C)`. Then `Kx=(q,-D_0v)` and

\[
x^*K(I-K)x=q(1-q).
\]

Since `Q` is a projection and `Q_{ii}=1/2`,

\[
K(I-K)=\frac{1-r}{4}I,\qquad \|b\|^2=r/4.
\]

Therefore

\[
\boxed{q(1-q)=\frac{1-r}{4}(1+\|v\|^2),\qquad
\|v\|^2=\frac{r(1-m^2)}{1-r}.}\tag{4.2}
\]

Cauchy–Schwarz applied to `q-1/2=-b*v` gives
`(2q-1)^2 <= r||v||^2`. Combining this with (4.2) proves

\[
\boxed{|2q-1|\le r,\qquad |m|\le c.}\tag{4.3}
\]

This is stronger than the noise-gap interval `|2q-1|<=c`.

The rank-one determinant/inverse update gives

\[
q(s^j)-q(s)=\frac{s_j|v_j|^2}{o_j}.
\]

Comparing with (3.6), and using `q=(1+cm)/2`, identifies

\[
\boxed{\kappa_j=\frac{1-r}{r}|v_j|^2.}\tag{4.4}
\]

### 4.3 Full entropy differentiation, not a Hessian analogy

Allow separate biases `d_1,...,d_n` temporarily, and let `H` denote the actual observed-word Shannon entropy. Holding the external biases fixed, the central conditional probability is `(1+d_i+cm)/2`; the external mass does not depend on `d_i`. Hence

\[
\partial_{d_i}H=-E_C\operatorname{atanh}(d_i+cm).\tag{4.5}
\]

Now differentiate (4.5) along the common bias at zero. Both the external mass and the posterior move. Formula (2.7) shows that the derivative of the integrand is exactly

\[
\frac{1+cm'_0}{1-rm^2}=\frac1{1-r}.
\]

Thus the negative Hessian row sum is

\[
R_i:=-\sum_j\partial_{d_i}\partial_{d_j}H\big|_0
=\frac{1+E_C[(M_C+cm)\operatorname{atanh}(cm)]}{1-r}.
\]

Apply (3.8) with `f=f_c`. This proves

\[
\boxed{R_i=\frac{1-E_C\mathcal B_{i,c}}{1-r},\qquad
-\frac4nH''(0)=\frac4{1-r}\left(1-\frac1n\sum_iE_C\mathcal B_{i,c}\right).}\tag{4.6}
\]

Because

\[
[f_c]_{m,m^j}=\frac c4[\ell]_{q,q^j},
\]

(4.4) converts (4.6) to the finite version of (0.1). Every equality is at fixed finite volume. The ordered double derivatives in (2.4), the cross derivatives in (4.5), and the external weight derivative in (2.7) are retained and then algebraically combined.

## 5. PROVED — the scalar budget and its exact certification

For `f_c(t)=atanh(ct)`, its derivative is even and increases with `|t|`. If `0<=m<=c`, the largest secant from `m` to a point of `[-c,c]` is the secant to `c`.

Here is a direct proof covering a chord crossing zero. On the nonnegative half-interval the statement follows from convexity. If the other endpoint is `-a`, its secant is `(f_c(m)+f_c(a))/(m+a)`, a weighted average of `f_c(m)/m` and `f_c(a)/a`. Both are at most `f_c(c)/c`, which is at most the secant from `m` to `c`. Negative `m` follows by oddness; zero endpoints follow by continuity.

Using the positive covariance weights and their exact sum gives

\[
\mathcal B_c(s)\le
c(1-m^2)\frac{\operatorname{atanh}(c^2)-\operatorname{atanh}(c|m|)}{c-|m|}
=B_r(c|m|)\le b(r).\tag{5.1}
\]

All quantities are finite for each `c<1`. This proves (0.5) in finite volume.

### 5.1 Monotonicity of the envelope

Put `x=rt`, `0<=t<=1`, and `z=t+(1-t)v`. The exact integral formula is

\[
B_r(rt)=\int_0^1\frac{r(1-rt^2)}{1-r^2z^2}\,dv.
\]

The numerator of the derivative of the integrand with respect to `r` is
`1-2rt^2+r^2z^2`, which is at least
`1-r(2-r)t^2 >= (1-r)^2 >0`. Thus `b(r)` is increasing. As a purely analytic, though weaker, bound one also has `b(r)<=r/sqrt(1-r^2)`: the inequality

\[
\frac{\operatorname{atanh}r-\operatorname{atanh}x}{r-x}
\le\frac1{\sqrt{(1-r^2)(1-x^2)}}
\]

follows from `atanh z <= z/sqrt(1-z^2)`, and
`(r-x^2)/sqrt(1-x^2)` decreases for `0<=x<=r`.

Consequently the entirely analytic inequality

\[
\Gamma(c)\ge\frac4{1-c^2}\left(1-\frac{c^2}{\sqrt{1-c^4}}\right)
\]

already proves positivity for `0<c<2^(-1/4)`. The certificate below enlarges this interval; it is not the sole justification for the non-perturbative mechanism.

### 5.2 A finite exact polynomial proof at `r=3/4`

The sharper endpoint uses no fitted values. For an integer `L>=1`, define

\[
P_{r,L}(t)=(1-rt^2)\sum_{k=0}^{L-1}\frac{r^{2k+1}}{2k+1}
 \sum_{j=0}^{2k}t^j+\frac{r^{2L+1}}{1-r^2}.\tag{5.2}
\]

The power series for `atanh`, with positive terms, gives
`B_r(rt)<=P_{r,L}(t)` on `[0,1]`: the omitted divided-difference tail is at most `r^(2L+1)/(1-r^2)`.

For a polynomial `p(t)=sum_{k=0}^N p_k t^k`, its power coefficients on a rational interval `[a,b]`, after `t=a+(b-a)v`, are

\[
q_j=\sum_{k=j}^N p_k\binom kj a^{k-j}(b-a)^j.
\]

Its degree-`N` Bernstein coefficients on that interval are

\[
\beta_i=\sum_{j=0}^i q_j\frac{\binom ij}{\binom Nj}.
\tag{5.3}
\]

Nonnegative Bernstein basis functions sum to one. Therefore positivity of every `beta_i` proves positivity of the polynomial everywhere on that interval.

The supplied `certify_chord_envelope.py` executes these formulas with `Fraction` arithmetic only. For

* `r=3/4`, `L=24`, `16` equal intervals, and `p=997/1000-P_{r,L}`, every Bernstein coefficient is strictly positive;
* `r=361/400`, `L=80`, `32` equal intervals, and `p=1587/1000-P_{r,L}`, the same is true.

The exact interval minima and smallest coefficient are in `chord_envelope_certificate.json`; the script recomputes them from (5.2)–(5.3). Their decimal sizes, about `0.0005166` and `0.0010050`, are descriptive only. No floating-point result participates in acceptance. This is a finite rational certificate of a one-variable inequality, not a computation of `Gamma`.

It proves (0.6) and (0.7) once the infinite identification below is made.

**PROVED corollary for the original Fejer sequence.** For each fixed `0<c<=sqrt(3)/2`, the frozen convergence `A_R''(0)->Gamma(c)` and (0.6) imply `A_R''(0)>0` for all sufficiently large positive odd `R`. This is an eventual-positivity statement at each fixed contrast; no practical starting radius is claimed.

## 6. PROVED — identification with the prescribed infinite V14 target

This section is necessary. The finite entropy calculation alone would not identify the assignment's local Fejer curvature.

### 6.1 The exact frozen interface used

For a finite Hermitian kernel of the form
`K(u,delta)=I/2+uH+u delta I`, with `||H||<=c/2`, the frozen signed-transport calculation gives

\[
\partial_\delta^2 E\phi(q)\big|_0=u^2E\bar{\mathcal G}.\tag{6.1}
\]

Here `G=(S/2+uH_C)^{-1}`, `v=Gub^0`, `q=1/2-u(b^0)^*v`,
`d_j=q(z^j)-q(z)`, `A_z=1+||v_z||^2`, and `bar r_j=s_j-G_jj`.
For `Breg_psi(p,q)=psi(p)-psi(q)-psi'(q)(p-q)`, put
`bar B_psi=sum_j bar r_j Breg_psi(q^j,q)`. The kernel being used is exactly

\[
\begin{aligned}
\bar{\mathcal G}={}&\phi''(q)+\bar B_{\phi'}
 +\sum_j(G^2)_{jj}\operatorname{Breg}_\phi(q^j,q)\\
&+\sum_j\bar r_j\{[\phi'(q^j)-\phi'(q)]A_{z^j}
                         -\phi''(q)d_jA_z\}\\
&+\sum_k\bar r_k[\bar B_\phi(z^k)-\bar B_\phi(z)].
\end{aligned}\tag{6.2}
\]

The frozen proof establishes absolute convergence, dimension-free bounds, and the weighted double-flip estimates for this grouped expression. In particular
`|bar G-8| <= C_c u^4`, with the explicit, possibly very large,
`C_c=21 c^4 (2/(1-c))^18/16`. We use that constant only for domination in this identification, not for the sign estimate.

### 6.2 Transitive finite projections approximating the sine projection

For `n=4L+2`, use the cyclic group `Z/nZ` and the Fourier projection onto frequencies `-L,...,L`. Its kernel is

\[
Q_n(j)=\frac{\sin(\pi j/2)}{n\sin(\pi j/n)},\quad j\not\equiv0\pmod n,
\qquad Q_n(0)=\frac12.\tag{6.3}
\]

This is a genuine rank-`n/2` projection of constant diagonal `1/2`. Set `J_n=2Q_n-I`. The model is transitive, and all center posterior production terms have equal expectations.

Represent the cyclic sites by a centered integer interval and embed its matrix by zero outside that interval. The embedded `J_n` are self-adjoint contractions and converge strongly to `J`. To check this, first fix a column index. On bounded displacements its entries converge to the sine coefficients. If `d` is cyclic distance, then `|Q_n(j)|<=1/(2d)` because `sin(pi d/n)>=2d/n` for `d<=n/2`. Hence the squared column tails are uniformly bounded by a constant times `sum_{d>M}d^{-2}`. Entrywise convergence plus this tail proves norm convergence of each fixed column. Density of finitely supported vectors and the common operator norm prove strong convergence. Center columns also converge in `ell^2`.

### 6.3 Why the local kernels converge, including double flips

For completeness, the part of the frozen convergence argument needed for this new approximation sequence is as follows. For a common gap `c<1`,

\[
(S/2+uH_n)^{-1}=2\sum_{k\ge0}(-2uSH_n)^kS.\tag{6.4}
\]

The geometric tail is uniform in `n,u,z`. For each finite term, the image of the compact word space under multiplication by `S_z` is a compact vector family. Uniformly bounded strongly convergent operators converge uniformly on compact vector families. Induction in `k` therefore gives uniform convergence of `v_n`, and of every fixed resolvent column, for all `u` and words. These families consequently have uniformly vanishing squared spatial tails.

The grouped double-flip estimates in the frozen transport proof are bounded by finite linear combinations of

\[
|G_{ij}||v_i|^3|v_j|,\quad |G_{ij}|^2|v_i|^4,\quad
|G_{ij}|^2|v_i|^2|v_j|^2,\quad |G_{ij}|^4|v_i|^4,
\]

their transposes, and `|d_j| max(|d_i(z)|,|d_i(z^j)|)^2`.
Cauchy–Schwarz pays a tail in a `v` index. For a tail solely in the resolvent index, first restrict the other index to a fixed smaller window, use its finitely many column tails, and then pay the remaining `v` tail. The diagonal double flip is a single-index term. This proves uniform tail convergence of (6.2), not just convergence of its finite entries. None of these arguments requires the approximating matrices to be Fejer matrices; the checked hypotheses are the common contraction bound, strong convergence, and center-column convergence.

True finite marginal word probabilities converge on every fixed window by their determinant formulas. Uniform cylinder approximation of the bounded local kernels then implies convergence of their actual expectations. This proves that the torus V14 expectation converges to the same infinite expectation specified in the assignment.

### 6.4 The `u` integral and the factor four

For any fixed finite system, run the channel along
`K(u,delta)=I/2+u[c(Q-I/2)+delta I]`, from `u=0` to `u=1`.
The probability mass satisfies

\[
u\partial_u p_u(s)=\frac12\sum_i[p_u(s)-p_u(s^i)].
\]

Multiplying by `-log p_u` and summing, then grouping each pair of central states with the same external word, gives the **exact** entropy-production identity

\[
u\partial_u H_n(u,\delta)=-\sum_i E\phi(q_i).\tag{6.5}
\]

There is no independence assumption on external words. Since `H_n(0,delta)=n log 2`, integration gives

\[
\frac{H_n(c,2\delta)}n=\log2-
 \int_0^1\frac1n\sum_i E_{u,\delta}\phi(q_i)\,\frac{du}{u}.\tag{6.6}
\]

All weights on the right are the actual moving channel weights. The finite-system differentiation at the lower endpoint can be justified before taking any volume limit: on a fixed small complex neighborhood of `delta=0`, finite word masses and posteriors are analytic for small `u`, uniformly over that finite word set, with `q=1/2+u delta+O_n(u^2)`. Thus `E phi(q)=O_n(u^2)` there, and Cauchy estimates give the same order for its first two delta derivatives on a smaller neighborhood. Away from `u=0` a fixed finite system has a uniform positive gap. This supplies integrable domination for the two finite-system differentiations of (6.6). The subsequent volume limit uses the dimension-free V14 bound at `delta=0`, not this `n`-dependent analytic estimate.

Differentiate twice at zero, use (6.1), and note `d=2delta` at `u=1`. On the transitive torus,

\[
\boxed{-\frac4nH_n''(c,0)
=\int_0^1u E_{n,u}\bar{\mathcal G}_{n,u}\,du.}\tag{6.7}
\]

The common V14 bound just stated justifies both endpoint domination and passage to the limit. The limit of (6.7) is precisely the assignment's `Gamma(c)`.

Independently, the new one-flip kernel converges uniformly along these tori: its summands are bounded by `D_1|v_j|^2`, its finite entries converge uniformly by (6.4), and its squared response tails vanish uniformly. Its expectation therefore converges under the true laws. Passing to the limit in (4.6) proves (0.1)–(0.3). Passing to the limit in the finite scalar bound proves (0.5)–(0.7).

This argument establishes the needed Hessian bridge; it does not assume it. It also explains exactly where the originally signed single- and double-flip terms, the `u` factors, and changing weights have gone.

## 7. PROVED — a finite reference-word certificate and effective spatial control

This is an auxiliary approximation to `Gamma`, not a replacement of the original Fejer model.

### 7.1 An explicit reference resolvent

Work now with the infinite sine `J`, center `0`, and `C=Z\\{0}`. Let

\[
a_j=J_{j0},\quad \|a\|^2=1,\quad J_Ca=0,\quad J_C^2=I-aa^*.
\]

For the reference external word consisting entirely of occupied sites, `S=I`,

\[
\boxed{G_+=\frac2{1-r}(I-cJ_C-r aa^*),\qquad v_+=ca,
\qquad q_+=\frac{1-r}{2}.}\tag{7.1}
\]

These formulas follow by multiplying `I+cJ_C` by `I-cJ_C-r aa*`.

Let `C_M=[-M,M]\\{0}`. For an observed word on `C_M`, extend it by occupied sites outside `C_M`; let `D` be its finite set of holes. Define the finite matrix

\[
W_D=I-(G_+)_{DD}.
\]

It is invertible: `G_+ >= 2/(1+c) I`, so `W_D <= -(1-c)/(1+c) I`. Empty-set formulas have their usual zero-dimensional meaning. Woodbury gives the explicit finite quantities

\[
\boxed{
q_D=\frac{1-r}{2}-r a_D^*W_D^{-1}a_D,\qquad
v_{D,j}=ca_j+c(G_+)_{jD}W_D^{-1}a_D.}\tag{7.2}
\]

A single flip at `j in C_M` replaces `D` by its symmetric difference with `{j}`. Only sine coefficients and finite matrices occur in (7.2).

Let `w_M(s)` be the true marginal word probability on `C_M` for the unsmoothed observed DPP `K=(I+cJ)/2`; explicitly,

\[
w_M(s)=\left(\prod_{j\in C_M}s_j\right)
\det\left(K_{C_M}-\operatorname{diag}\frac{1-s}{2}\right).
\]

Define

\[
\boxed{\Gamma_M^+(c)=\frac4{1-r}-
\sum_{s\in\{-1,1\}^{C_M}}w_M(s)
 \sum_{j\in C_M}|v_{D(s),j}|^2[\ell]_{q_{D(s)},q_{D(s)\triangle\{j\}}}.}\tag{7.3}
\]

The reference extension is only a device for evaluating a cylinder function; the probability `w_M` is **not** the law conditioned on that reference extension. This distinction matters because the reference infinite event has no positive probability. The continuous posterior/resolvent version makes its pointwise evaluation legitimate.

### 7.2 An explicit uniform center-column tail

Write

\[
a_0=\frac2{1-c},\quad L_0=\frac c{1-c},\quad
\eta_c=\min\{1/2,-\log c\},
\]
\[
V_0=\frac{2\sqrt2c}{\pi(1-c)}+\frac{4c^2}{(1-c)^2},\qquad
F_0=\sqrt2V_0+\frac1{1-c},\qquad W=\frac c{\sqrt{1-r}}.
\]

Define, for `s>=1`,

\[
f_0(s)=\begin{cases}
L_0,&s<e^4,\\
\min\{L_0,F_0e^{-\eta_c\sqrt{\log s}}\},&s\ge e^4,
\end{cases}
\qquad t_c(s)=\min\{W,f_0(s)\}.\tag{7.4}
\]

Then, uniformly in **all** external words,

\[
\boxed{\|(I-P_{C_M})v\|\le t_c(M).}\tag{7.5}
\]

Here is a derivation of the explicit tail, to make its role auditable. In the Neumann series put `T=-cSJ_C`, `x_0=S b`, `b=ca/2`. Then `||T||<=c`, `||x_0||=c/2`. The `1/|i-j|` sine-entry bound and a Hilbert–Schmidt sum give, for `t>=2s>=2`,

\[
\|(I-P_t)TP_s\|\le4c\sqrt{s/t},\quad
\|(I-P_t)Tx\|\le c\|(I-P_s)x\|+4c\sqrt{s/t}\|x\|.
\]

Also `||(I-P_B)x_0||<=sqrt(2)c/(pi sqrt(B))`. Iterating at radii `B,B^2,...,B^(k+1)` gives

\[
\|(I-P_{B^{k+1}})T^kx_0\|
\le \frac{c^k\sqrt2c}{\pi\sqrt B}+\frac{2kc^{k+1}}{\sqrt B}.
\]

Since `v=2 sum_{k>=0}T^k x_0`, summing the first `K+1` terms and the geometric tail yields, if `B^(K+1)<=s`,

\[
\|(I-P_s)v\|\le V_0/\sqrt B+c^{K+2}/(1-c).
\]

For `s>=e^4`, take `B=floor(exp(sqrt(log s)))` and
`K=floor(sqrt(log s))-1`. The elementary estimates
`B^(-1/2)<=sqrt(2)exp(-sqrt(log s)/2)` and the corresponding geometric-tail bound prove `f_0`. Finally (4.2) gives the additional global bound `W`. The Hilbert–Schmidt estimate above follows, for example, by summing `4c^2/(pi^2|i-j|^2)` over `|j|<=s`, `|i|>t`; deletion of the center can only decrease that sum.

This tail is deliberately explicit rather than optimized. Its slow decay remains a limitation. The improvement here is in the representation and its error factors, not a claimed sharp spatial-decay theorem.

### 7.3 Error proof under the actual probability law

On the sharper posterior interval from (4.3),

\[
0<[\ell]_{p,q}\le D_1=\frac4{1-r^2},\qquad
|\ell''|\le D_2=\frac{16r}{(1-r^2)^2}.\tag{7.6}
\]

If two words agree on `C_M`, write their Schur matrices as `B` and `B+E`, where `E` is diagonal, supported outside `C_M`, with `||E||<=1`. The resolvent identity and (7.5) imply

\[
\|v-\tilde v\|\le a_0 t_c(M),\qquad
|q-\tilde q|=|v^*E\tilde v|\le t_c(M)^2.\tag{7.7}
\]

The same posterior difference bound holds after any common flip inside `C_M`, since the two flipped words still agree there. The divided-difference integral formula implies

\[
|[\ell]_{q,q^j}-[\ell]_{\tilde q,\tilde q^j}|
\le D_2t_c(M)^2.
\]

The direct spatial tail of the nonnegative sum in (0.1) is at most
`D_1 t_c(M)^2`. For the retained weights,

\[
\sum_{j\in C_M}\big||v_j|^2-|\tilde v_j|^2\big|
\le(\|v\|+\|\tilde v\|)\|v-\tilde v\|
\le2Wa_0t_c(M).
\]

The retained divided-difference error costs at most `W^2D_2t_c(M)^2`. Combining these bounds pointwise and then taking the true expectation proves

\[
\boxed{|\Gamma-\Gamma_M^+|
\le2a_0WD_1t_c(M)+(D_1+W^2D_2)t_c(M)^2.}\tag{7.8}
\]

There is no total-variation replacement of the physical law: the cylinder expectation is exactly the finite sum with `w_M`. There is no dependence on the unknown `Gamma`. The principal error multipliers have at most inverse-gap order three as `c` approaches one; the explicit tail envelope itself also has gap-dependent constants and slow decay. No practical cutoff at `19/20` is claimed, and no value of `Gamma_M^+` large enough to determine that sign was evaluated.

## 8. PROVED — checks, scope boundaries, and a small all-contrast example

### 8.1 Two-site exact check

For `Q=(1/2)[[1,1],[1,1]]`, the latent spins are exactly opposite. The external posterior is `m=-c s`, so

\[
\mathcal B_c=(1-r)\operatorname{atanh}r,
\qquad -\frac4nH''(0)=\frac4{1-r}-4\operatorname{atanh}r.
\]

This is positive for every `0<c<1` and is at least `4`, since
`atanh r <= r/(1-r)`. It checks the factors of two, the weight derivative, and the sign of the chord correction. It is not evidence sufficient for the infinite theorem.

### 8.2 Degenerate and boundary cases

At `c=0`, the observed law is independent and the target is `Gamma(0)=4`; formulas with division by `c` or `r` are interpreted by this limit, not used literally. Zero covariance edges have zero contribution, and coincident posterior endpoints use the derivative definition of the secant. Complex Hermitian projections are allowed: all response and posterior covariance weights use modulus squares. Zero latent atom probabilities cause no difficulty because the noisy observed words have strictly positive mass for `c<1`.

No assertion is made at `c=1`. The noise gap, the explicit inverse bounds, and several endpoint derivatives are then singular. The interval theorem is uniform in volume at each stated contrast; it is not a gapless theorem. The auxiliary torus and reference-word approximations do not alter the original odd-`R`, Fejer, and `delta` conventions.

## 9. DISPROVED / INCOMPLETE — failure mechanisms and the remaining obstruction

### 9.1 DISPROVED: a pointwise positive-curvature certificate in the full projection class

Let `U=Hadamard(16)/4`, using the Sylvester Hadamard matrix, and

\[
J=\begin{pmatrix}0&U\\U^T&0\end{pmatrix},\qquad Q=(I+J)/2.
\]

This is a rational, genuine `32`-site projection of rank `16` and constant diagonal `1/2`. Take `c=19/20`, center `0`, and external signs from the following vector (its first, central entry is ignored):

```
-1, 1,-1,-1,-1, 1,-1,-1,-1, 1, 1,-1,-1, 1, 1,-1,
 1,-1, 1,-1, 1, 1, 1,-1,-1,-1, 1, 1, 1, 1, 1, 1
```

The supplied exact-rational script forms the `31`-site Schur inverse, computes `q`, every `v_j`, and every flipped `q^j` rationally, and encloses each logarithm by the positive `atanh` series with a geometric tail. Every arithmetic rounding in that enclosure is directed rational rounding. It proves

\[
\boxed{\mathcal B_{19/20}(z)>117/100>1.}\tag{9.1}
\]

The numerical location, approximately `1.1776728191`, is not used for the inequality. The exact enclosure is supplied. This disproves the proposed **pointwise** closure in the finite projection class. It does not disprove positive expected curvature, and it is not a counterexample to the infinite sine target.

Exploratory searches also found values above one for finite periodic sine projections. Those searches used ordinary floating point and are explicitly not certified counterexamples for the infinite model. Their only role was to discourage replacing the necessary averaged argument by a guessed pointwise theorem.

### 9.2 INCOMPLETE: averaging beyond the scalar envelope

For `r=361/400`, the scalar envelope is larger than one. It cannot certify the benchmark sign. The exact remaining inequality is

\[
\mathbb E_{\infty,c}\left[
 c\sum_j\kappa_j[\operatorname{atanh}(c\,\cdot)]_{m,m^j}\right]<1.
\tag{9.2}
\]

For the stronger assertion `Gamma(c)>=4`, the sufficient and equivalent budget is `E B_c<=c^2`. Neither assertion is proved here at high contrast. The expectation in (9.2) cannot be replaced by its worst-word supremum in the general projection class, by (9.1).

The useful content is not merely the renaming of this obstruction: the generator and its potential are explicit; the budget is nonnegative; its covariance weights have exact total `1-m^2`; it has a proved non-perturbative scalar bound, a certified positive interval, and a finite target-independent approximation with only single-flip spatial control. Nevertheless the missing averaged inequality is still a substantive research problem, and this report does not call the all-`c` task complete.

Another attempted route was convexity, as a function of a balanced latent prior, of the common-bias negative entropy Hessian. Numerical experiments were suggestive, but no proof was obtained; that convexity is **not** a lemma used anywhere above. Likewise, no positive-dissipation theorem was applied to the old signed transport.

## 10. Dependency and execution ledger

| Claim | Status | Dependencies and validation scope |
|---|---|---|
| Actual finite mass derivatives, Ward score, full Fisher term | PROVED | Direct differentiation of the finite channel; Sections 2–3. |
| Positive reversible generator and explicit score potential | PROVED | Bayes flip likelihood and the fixed latent count; no Poisson solvability assumption. |
| Positive covariance/chord identity | PROVED | Finite edge reversal, posterior covariance transform, actual word weights. |
| Projection posterior covariance signs and sharper posterior interval | PROVED | Cauchy–Binet, a finite Gram projection, Schur energy; Section 4. |
| Finite projection entropy-curvature formula | PROVED | Full two-parameter entropy derivative; no use of the old audit as validation. |
| Infinite identity with the fixed `Gamma` | PROVED relative to frozen V14 interface | Sections 6.1–6.4 check the torus approximation and the exact entropy-production bridge. Uses the frozen general finite V14 identity and its weighted double-flip bounds. |
| Scalar envelope and monotonicity | PROVED | Elementary secant and integral inequalities, Section 5. |
| `Gamma(c)>0` for `0<c<=sqrt(3)/2` | PROVED with executed rational certificate | Scalar theorem, finite rational Bernstein proof, and the proved infinite identification. Pending independent checking. |
| Reference-word finite approximation and error | PROVED | Explicit Woodbury formula, Neumann column-tail proof, response energy, true marginal probabilities. |
| Pointwise budget `B<=1` in the general projection class | DISPROVED | Explicit rational Hadamard projection and executed rational logarithm enclosure. |
| `Gamma(19/20)>0`; all-contrast sign | INCOMPLETE | No evaluated sign certificate and no proved averaged high-contrast budget. |
| Literature novelty | INCOMPLETE / not claimed | Source mechanisms checked for attribution only. |

### Executed computations

`ward_chord/code/` contains executable scripts, and `ward_chord/checks/` contains their outputs. The two decisive certificates are rational computations: the one-variable Bernstein certificate and the pointwise-counterexample logarithm enclosure. Finite rational Ward/Stein regressions separately test the algebra. A further exact-rational regression checks the reference inverse, the Woodbury posterior and response formulas, projection energy, and every single-flip endpoint for `n=2,4,6` finite projection examples. An additional exact-algebraic regression uses a four-site complex Hermitian conference projection at `c=sqrt(3)/2`; it checks modulus-square conventions, full and external scores, covariance reversal, projection energy, and the chord Stein identity for degrees 1 through 7. This example has nonzero triangle edges and is not a bipartite real test. Ordinary floating-point searches and small entropy comparisons are labelled exploratory and are not inputs to any proved sign statement.

No `Gamma_M^+` at a cutoff capable of deciding `19/20` was computed. No fitted power law, guessed analytic continuation, or empirical high-contrast sign was used. No independent validation of the new theorem has yet occurred.

### Frozen-input scope

The only pre-existing mathematical interface used to identify the target is the PRO01 packet: `inputs/TASK.md` for definitions, `inputs/SA03_S9_SIGNED_TRANSPORT.md` for the finite V14 precursor and weighted flip identities, and `inputs/SA03_VOLUME_LIMIT.md` for the explicit infinite kernel and its convergence mechanism. The center-column tail in Section 7 is reproved in the form used here; its constants agree with the conservative column-tail mechanism in `inputs/SA03_EFFECTIVE_REMAINDER.md`. The old scoped audit remains unchanged and does not audit this report. No new results from the other PRO assignments were used.

### External source

[C] Sourav Chatterjee, *Concentration inequalities with exchangeable pairs*, doctoral dissertation, Stanford University, 2005, arXiv:math/0507526, Chapter 3, Lemma 3.1. This is the source mechanism for exchangeable-pair integration by parts. Its hypotheses are not silently assumed for the old signed transport: the positive reversible chain needed here is constructed in Section 3, and the identity is proved directly. No external theorem from [C] carries the sign or the spatial estimates.

## 11. Exact improvement and honest stopping point

The first-round result supplied an effective but unevaluated degree/block truncation. This report instead supplies an exact positive-covariance single-flip budget and a finite reversible score potential, proves a volume-uniform sign theorem through `sqrt(3)/2`, and reduces the spatial error to one center-column tail with low-order explicit prefactors. These are genuine additional conclusions, not a rebranding of the previous truncation lemma.

They still fall short of the user's full high-contrast goal. At `19/20` the proved scalar bracket straddles zero, and a general pointwise closure is rigorously false. The smallest missing ingredient is a law-averaged projection estimate for (9.2), or a certified finite evaluation using (7.3)–(7.8) whose error is smaller than its sign margin. Neither is asserted to have been completed.