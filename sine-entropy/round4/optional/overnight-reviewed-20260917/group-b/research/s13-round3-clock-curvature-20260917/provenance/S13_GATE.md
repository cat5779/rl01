# S13 bounded gate: degree-two multiplier and positive potential clock

## Scope and verdict

This is a bounded algebraic triage of Sections 3, 6, and 7 of `S13_AUTHOR_REPLY.md`. It does **not** audit the saddle expansion, Theorem A, the midpoint cusp/local-limit calculation, Theorem B, the entropy comparison bounds, or the full entropy-concavity target.

**Verdict:** the displayed degree-two multiplier, the coefficientwise proof of

\[
0<\theta_{n,l}<1,
\]

and the resulting positive Bernoulli--Laplace clock's exact matching of the single Fourier pair-potential expectation are algebraically sound, with the usual convention that out-of-range binomial coefficients are zero. The boxed two-mode no-go is sound only under its explicit extra requirement of matching the degree-one **operator/channel multiplier**. It is not, as written, a no-go for matching the averaged translation-invariant output law, because the averaged input density has zero Johnson degree-one component.

## 1. Exact degree-two formula

Take `n=2k` and `2 <= l <= k`, and fix a `k`-set `A`. Under the tilted overlap law, let `J=|A cap S|` and

\[
H_1(S)=2J-l,\qquad \lambda=\frac{\mathbb E H_1}{l}.
\]

Writing `x_i=2 1_{i in A}-1`, one has `sum_i x_i=0` and

\[
\sum_{\{i,j\}\subset S}x_ix_j=\frac{H_1(S)^2-l}{2}.
\]

The normalized Johnson degree-two zonal function that equals one on the maximal-overlap state is therefore

\[
\Phi_2(S)
=
\frac{(n-1)(H_1(S)^2-l)+l(l-1)}{n l(l-1)}.
\]

Since `E H_1^2=4 Var(J)+l^2 lambda^2`, its expectation is

\[
\mathbb E\Phi_2
=
\lambda^2+
\frac{4(n-1)\operatorname{Var}(J)-l(n-l)(1-\lambda^2)}{n l(l-1)}.
\]

This is exactly the author's variance formula for `theta_{n,l}`. It also fixes the normalization: the denominator `n l(l-1)` and the factor `4(n-1)` are correct.

For the coefficient form, factorial-moment extraction from

\[
Z_{n,l}(z)=\sum_j {k\choose j}{k\choose l-j}z^j
\]

gives the same degree-two expectation as

\[
\theta_{n,l}
=
\frac{(z-1)^2 B_l(z)}{\alpha_{n,l}Z_{n,l}(z)},
\quad
B_l(z)=\sum_j {k-2\choose j}{k-2\choose l-2-j}z^j,
\quad
\alpha_{n,l}=\frac{l(l-1)}{k(k-1)}.
\]

Thus the two displayed formulas are consistent. Complementation transports the statement to `l>k`; the author should keep saying explicitly that the multiplier there is *defined/identified through complement symmetry*, since the displayed `J` normalization was derived for `l<=k`.

## 2. The strict coefficient bound

Put `y=z-1>0`. Vandermonde expansion gives

\[
Z_{n,l}(1+y)
=\sum_{r=0}^l {k\choose r}{2k-r\choose l-r}y^r,
\]

and

\[
y^2B_l(1+y)
=\sum_{r=2}^l {k-2\choose r-2}{2k-r-2\choose l-r}y^r.
\]

For `2<=r<=l`, the numerator coefficient divided by the corresponding coefficient of `Z` is

\[
R_r=
\frac{r(r-1)(2k-l)(2k-l-1)}
{k(k-1)(2k-r)(2k-r-1)}.
\]

The factor `r(r-1)/((2k-r)(2k-r-1))` is strictly increasing in `r`, and

\[
R_l=\frac{l(l-1)}{k(k-1)}=\alpha_{n,l}.
\]

Hence every common coefficient below degree `l` is strictly smaller than its coefficient in `alpha Z`, while degrees zero and one occur only in `alpha Z`. All coefficients are nonnegative and the numerator is nonzero for `y>0`. Therefore

\[
0<(z-1)^2B_l(z)<\alpha_{n,l}Z_{n,l}(z)
\]

for `2<=l<=k`, proving `0<theta_{n,l}<1`. Complement symmetry supplies `k<l<=n-2`. This argument is exact and has no asymptotic dependency.

Small boundary checks agree: for `(k,l)=(2,2)`,

\[
\theta=\frac{(z-1)^2}{1+4z+z^2},
\]

and for `(k,l)=(3,2)`,

\[
\theta=\frac{(z-1)^2}{1+3z+z^2};
\]

both exhibit the claimed strict interval directly for `z>1`.

## 3. Exact positive potential matching

The root-of-unity identity

\[
\sum_{j\ne i}\log|\zeta_i-\zeta_j|^2=2\log n
\]

says that the pair kernel defining `U_n` has constant row sums. Consequently, on every fixed slice, `U_n-E_{u_l}U_n` has no Johnson degree-zero or degree-one part and is a pure degree-two observable. The total-rate-one Bernoulli--Laplace generator acts on it with eigenvalue

\[
\gamma_{2,l}=\frac{2(n-1)}{l(n-l)}.
\]

Uniform thinning from a `k`-set to an `l`-set multiplies the centered pair statistic by

\[
\alpha_{n,l}=\frac{{l\choose2}}{{k\choose2}},
\]

and complementation gives the corresponding statement above the middle slice. Thus the maximal-overlap averaged initial law has potential amplitude `alpha_{n,l} V_n`.

Since `0<theta<1`,

\[
\widehat\tau_l=-\frac{\log\theta_{n,l}}{\gamma_{2,l}}>0.
\]

The finite irreducible forward Bernoulli--Laplace semigroup preserves mass and makes the evolved law strictly positive. Self-adjointness with respect to the uniform slice law then gives, exactly,

\[
\mathbb E_{\widehat q_l}\overline U_{n,l}
=e^{-\gamma_{2,l}\widehat\tau_l}\alpha_{n,l}V_n
=\theta_{n,l}\alpha_{n,l}V_n
=\mathbb E_{q_l}\overline U_{n,l}.
\]

Adding back the uniform mean proves `E_{hat q_l} U_n=E_{q_l}U_n` layer by layer. The exceptional layers `l=0,1,n-1,n` have identically zero centered pair potential, so the author's separate definition there is harmless.

This certifies one scalar expectation. It does not certify equality of laws, equality of all Fourier/Johnson modes, a KL response sign, or any differentiated entropy estimate.

## 4. Critical qualification to the two-mode no-go

For a positive forward-time mixture, with `X=e^{-gamma_1 T}` and `r=gamma_2/gamma_1>1`, the operator multipliers are indeed

\[
m_1=\mathbb E X,\qquad m_2=\mathbb E X^r,
\]

and Jensen gives `m_2 >= m_1^r`. Therefore, if one separately requires the mixture kernel to match the actual channel's degree-one multiplier `lambda`, then it cannot also match `theta<lambda^r` on the asserted asymptotic band. That conditional operator statement is correct, assuming the unaudited asymptotic strict inequality.

But the law denoted `r_l^{max}` has already been averaged over the cyclically invariant input `mu_n`. Its one-site marginals are uniform. Every Johnson degree-one function has the form

\[
h(S)=\sum_i b_i1_{\{i\in S\}},\qquad \sum_i b_i=0,
\]

and cyclic invariance gives

\[
\langle r_l^{max},h\rangle_{u_l}=0.
\]

Hence the degree-one component of the averaged initial density is zero. Applying the actual channel or any scalar/random BL clock leaves that component zero, regardless of the numerical degree-one multiplier. Matching `lambda` is therefore not a necessary condition for matching the averaged output law `q_l`.

The boxed no-go should be relabeled as a **channel/operator-multiplier obstruction**, or formulated before averaging, conditional on `A`. It does not rule out a positive random BL mixture that matches the averaged law or all of its nonzero modes. In particular, choosing a deterministic clock with `e^{-gamma_2 t}=theta` already matches the nonzero potential mode, as Section 6 demonstrates.

## 5. Precise next proof obligation

To turn the no-go into an averaged-law obstruction, exhibit a second **nonzero component of the averaged initial density** whose actual multiplier is incompatible, by the Hausdorff moment constraints, with the degree-two multiplier `theta`; then prove that both components remain nonzero on the declared layer and parameter band. Alternatively, state and prove the theorem at the `A`-conditional kernel level, where the degree-one signal is present, and avoid claiming an obstruction for the averaged law.

For the entropy target, the separate unpaid obligation remains a signed estimate for the full corrected Fourier-reference divergence, retaining moving count weights and conditional Fisher/acceleration terms. Nothing in this gate certifies the saddle limit, cusp coefficient, Gaussian boundary layer, or either large-`n` theorem.
