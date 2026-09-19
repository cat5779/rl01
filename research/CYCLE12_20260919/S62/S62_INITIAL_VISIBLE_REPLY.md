# Intake provenance

Visible assistant reply recovered from its original chat on 2026-09-19. This is AUTHOR_ONLY discussion, not an independent mathematical review. Truncated: false. S62 is actively being revised by its author at the user's request; do not treat the initial output as final. Numeric claims in S52 were not accompanied by original scripts/data and are unverified.

---

# S62 result

**New reusable tool: PROVED.**  
**Fixed benchmark negative curvature at \(c=19/20\): INCOMPLETE.**  
**Ultimate whole-interval entropy-rate concavity: INCOMPLETE.**  
**New claims disproved: none.**

Complete deliverable:

:chatgpt-content-reference{index="7"}

The proof below gives the central theorem and the exact remaining gap.

---

## 1. Audited inherited inputs

The status memo records S59 and S60 as incomplete and author-only for their new sign claims. It also restricts S61 to the frozen corrected cyclic \(W_{\rm rel}\) problem and explicitly states that S61 does not pay the true-block curvature ledger. citeturn362557view0turn362557view4

The independently reviewed SA02 inputs used here are:

\[
\mathcal C_B^V
=-\frac12\sum_{i\in B}\mathbb E Z_i^2
-\frac12\mathbb E\mathfrak T((G_V)_{BB})
-2\sum_{i<j\in B}\mathbb E r_{ij},
\]

where

\[
r_{ij}
=\int_0^1(1-t)
\left[
\frac{h_{ij}^2}{v_{ij}-th_{ij}}
-\frac{h_{ij}^2}{v_{ij}}
\right]dt\ge0,
\]

together with

\[
\mathbb E[(G_V)_{BB}\mid Y_A]=(G_A)_{BB},
\qquad B\subset A\subset V,
\]

and the genuine one-site reveal increment

\[
\Delta G=\zeta ww^*,
\qquad
\zeta=
\begin{cases}
1/u,&\text{probability }u,\\
-1/(1-u),&\text{probability }1-u.
\end{cases}
\]

These identities and their coefficients were independently checked in the SA02 review. citeturn290162view1turn392383view0turn727171view0

The QWE01 review independently verifies the exact full-Hessian block ledger, while leaving the proposed general common-shift Fisher-convexity payment open. citeturn362557view3

No external theorem is imported as a new load-bearing step below. Posterior score identities, the normalization estimates, and all rank-one calculus are derived directly.

---

# 2. Exact retained-remainder potential

Let \(Q_U\) be any finite Hermitian positive contraction and

\[
K_U=a\,\mathrm{Id}_U+cQ_U,
\qquad 0<a<1-c,\quad 0<c<1.
\]

For an actual output \(Y_U\), write

\[
G_U(Y_U)
=\bigl(K_U-\operatorname{diag}(1-Y_U)\bigr)^{-1}.
\]

Fix \(B\subset U\), and for a Hermitian matrix \(X=(X_{ij})_{i,j\in B}\) set

\[
x_i=X_{ii},\qquad
h_{ij}=|X_{ij}|^2,\qquad
v_{ij}=x_ix_j,\qquad
d_{ij}=v_{ij}-h_{ij}.
\]

For an actual inverse-score matrix, the SA02 two-point identity gives

\[
\operatorname{sgn}(v_{ij})
=\operatorname{sgn}(d_{ij})
=(2Y_i-1)(2Y_j-1).
\]

Hence \(d_{ij}/v_{ij}>0\). Define

\[
\Psi(v,h)
:=\int_0^1(1-t)\frac{h^2}{v-th}\,dt.
\]

Direct integration gives

\[
\boxed{
\Psi(v,h)
=h+(v-h)\log\frac{v-h}{v}.
}
\tag{2.1}
\]

Now define

\[
\boxed{
\mathfrak P_B(X)
=
2\sum_{i\in B}x_i^2
+
4\sum_{\substack{i<j\\i,j\in B}}
\Psi(v_{ij},h_{ij}).
}
\tag{2.2}
\]

Because

\[
\Psi(v_{ij},h_{ij})
=\frac{h_{ij}^2}{2v_{ij}}+r_{ij},
\]

and

\[
\mathfrak T(X)
=\sum_{i\in B}x_i^2
+2\sum_{i<j}\frac{h_{ij}^2}{v_{ij}},
\]

we have the pointwise identity

\[
\mathfrak P_B(X)
=
\sum_{i\in B}x_i^2
+\mathfrak T(X)
+4\sum_{i<j}r_{ij}.
\]

Therefore the full internal curvature is exactly

\[
\boxed{
\mathcal C_B^U
=
-\frac12\,
\mathbb E\,
\mathfrak P_B((G_U)_{BB}).
}
\tag{2.3}
\]

This retains the entire logarithmic remainder, rather than a truncated quadrature layer.

**Claim 2.1: PROVED.**

---

# 3. Posterior-normalized opposite-sign row cone

Let

\[
\sigma_i=2Y_i-1,
\]

and define

\[
\lambda_+
=\frac{c}{a(a+c)},
\qquad
\lambda_-
=\frac{c}{(1-a)(1-a-c)}.
\]

Use the latent-channel representation

\[
X^{\mathrm{lat}}\sim\operatorname{DPP}(Q_U),
\qquad
Y_i\mid X_i^{\mathrm{lat}}
\sim\operatorname{Bernoulli}(a+cX_i^{\mathrm{lat}}).
\]

Let \(R\) be the posterior DPP kernel of \(X^{\mathrm{lat}}\) given \(Y_U\), and put \(r_i=R_{ii}\).

The complete single-site local-offset score is

\[
s_i=
\begin{cases}
\dfrac1a-\lambda_+X_i^{\mathrm{lat}},&Y_i=1,\\[1.2ex]
-\dfrac1{1-a}-\lambda_-X_i^{\mathrm{lat}},&Y_i=0.
\end{cases}
\]

Taking posterior expectation gives

\[
(G_U)_{ii}
=
\begin{cases}
\dfrac1a-\lambda_+r_i,&\sigma_i=+1,\\[1.2ex]
-\dfrac1{1-a}-\lambda_-r_i,&\sigma_i=-1.
\end{cases}
\tag{3.1}
\]

For \(i\ne j\), the mixed local-offset derivative of the observed log likelihood is simultaneously

\[
-|G_{ij}|^2
\]

and

\[
\operatorname{Cov}(s_i,s_j\mid Y).
\]

The posterior DPP covariance is

\[
\operatorname{Cov}(X_i^{\mathrm{lat}},X_j^{\mathrm{lat}}\mid Y)
=-|R_{ij}|^2.
\]

Consequently,

\[
\boxed{
|G_{ij}|^2
=\lambda_{\sigma_i}\lambda_{\sigma_j}|R_{ij}|^2.
}
\tag{3.2}
\]

Since \(0\preceq R\preceq\mathrm{Id}\),

\[
\sum_{j\ne i}|R_{ij}|^2
=(R^2)_{ii}-r_i^2
\le r_i(1-r_i).
\tag{3.3}
\]

Define

\[
\boxed{
\mu_+
=\frac{c^2}{4(1-a)(1-a-c)},
\qquad
\mu_-
=\frac{c^2}{4a(a+c)}.
}
\tag{3.4}
\]

For \(\sigma_i=+1\), equations (3.1)–(3.3) give

\[
\frac{\sum_{\sigma_j=-1}|G_{ij}|^2}{G_{ii}^2}
\le
\frac{\lambda_+\lambda_-r_i(1-r_i)}
{(a^{-1}-\lambda_+r_i)^2}.
\]

The function \(r(1-r)/(A-Br)^2\) is maximized at

\[
r=\frac{A}{2A-B}.
\]

Substituting \(A=1/a\) and \(B=\lambda_+\) gives the maximum \(\mu_+\).

For \(\sigma_i=-1\), the relevant function is

\[
\frac{\lambda_+\lambda_-r(1-r)}
{((1-a)^{-1}+\lambda_-r)^2},
\]

whose maximum occurs at \(r=A/(2A+B)\), giving \(\mu_-\).

Thus

\[
\boxed{
\sum_{\substack{j\in B\\\sigma_j=-\sigma_i}}
|G_{ij}|^2
\le
\mu_{\sigma_i}G_{ii}^2.
}
\tag{3.5}
\]

This is a second-order-cone constraint:

\[
\left\|
(G_{ij})_{\{j:\sigma_j=-\sigma_i\}}
\right\|_2
\le
\sqrt{\mu_{\sigma_i}}\,\sigma_iG_{ii}.
\tag{3.6}
\]

For a fixed core output word \(\sigma\), its feasible set is convex. Both endpoints of an actual one-site reveal satisfy it, so the whole reveal chord satisfies it even though interior chord points need not themselves correspond to actual conditional DPP laws.

**Posterior-normalized row-cone claim: PROVED.**

---

# 4. Exact second variation only along the actual direction

Let

\[
X(s)=X+sww^*,
\qquad p_i=|w_i|^2.
\]

For a pair \(i<j\), write

\[
v(s)=X_{ii}(s)X_{jj}(s),\quad
h(s)=|X_{ij}(s)|^2,\quad
d(s)=v(s)-h(s).
\]

Because the direction is rank one,

\[
v''=2p_ip_j,
\qquad
h''=2p_ip_j,
\qquad
d''=0.
\tag{4.1}
\]

Writing

\[
\Psi(v,h)=v-d+d\log(d/v),
\]

and differentiating twice yields the exact formula

\[
\boxed{
\Psi''
=
\frac{\left(d'-\frac dvv'\right)^2}{d}
+\frac{2h}{v}p_ip_j.
}
\tag{4.2}
\]

The determinant \(d(s)\) is affine. At both reveal endpoints,

\[
\operatorname{sgn}d
=\operatorname{sgn}v
=\sigma_i\sigma_j,
\]

so these signs persist over the chord.

Hence:

\[
\sigma_i=\sigma_j
\quad\Longrightarrow\quad
\Psi''\ge0,
\tag{4.3}
\]

whereas

\[
\sigma_i=-\sigma_j
\quad\Longrightarrow\quad
\Psi''\le0.
\tag{4.4}
\]

This is the exact sign split. It does not demand positivity pair by pair; it identifies precisely which pairs can generate reveal concavity.

For an opposite-sign pair, suppose \(X_{ii}>0>X_{jj}\), and set

\[
D=|X_{ii}X_{jj}|,\qquad
r=\frac hD,\qquad
\alpha=\frac{p_i}{|X_{ii}|},\qquad
\beta=\frac{p_j}{|X_{jj}|}.
\]

For some \(\theta\in[-1,1]\), substitution into (4.2) gives

\[
-\Psi''
=
D\left[
\frac{
\left(
r(\beta-\alpha)
+2\sqrt{r\alpha\beta}\,\theta
\right)^2
}{1+r}
+2r\alpha\beta
\right].
\tag{4.5}
\]

Cauchy–Schwarz gives

\[
\left[
\sqrt r(\beta-\alpha)
+2\sqrt{\alpha\beta}\,\theta
\right]^2
\le
(1+r)(\alpha+\beta)^2.
\]

Therefore

\[
\boxed{
-\Psi''
\le
h(\alpha^2+4\alpha\beta+\beta^2).
}
\tag{4.6}
\]

**Exact rank-one second-variation claim: PROVED.**

---

# 5. True-path full-block theorem

Fix a tuning parameter \(\vartheta>0\), and define

\[
\chi_+(\vartheta)
=(1+2\vartheta)\mu_+,
\qquad
\chi_-(\vartheta)
=(1+2\vartheta^{-1})\mu_-,
\]

and

\[
\eta_\pm(\vartheta)
=(\chi_\pm(\vartheta)-1)_+.
\]

Using

\[
4\alpha\beta
\le
2\vartheta\alpha^2
+2\vartheta^{-1}\beta^2
\]

in (4.6), summing over opposite-sign pairs, and applying the row cone (3.5), gives

\[
\sum_{\sigma_i\ne\sigma_j}(-\Psi_{ij}'')
\le
\sum_{\sigma_i=+1}\chi_+p_i^2
+
\sum_{\sigma_i=-1}\chi_-p_i^2.
\tag{5.1}
\]

The diagonal part \(2\sum_iX_{ii}(s)^2\) of \(\mathfrak P_B\) has second derivative \(4\sum_i p_i^2\), while all same-sign pair terms are convex. Therefore

\[
\boxed{
\frac{d^2}{ds^2}\mathfrak P_B(X+sww^*)
\ge
4\sum_{i\in B}
(1-\chi_{\sigma_i})p_i^2.
}
\tag{5.2}
\]

It follows that

\[
s\longmapsto
\mathfrak P_B(X+sww^*)
+
2s^2\sum_i\eta_{\sigma_i}p_i^2
\]

is convex on the actual reveal chord.

For one reveal,

\[
M_{\rm new}=X+\zeta ww^*,
\qquad
\mathbb E\zeta=0,
\qquad
\mathbb E\zeta^2=\frac1{u(1-u)}.
\]

Conditional Jensen therefore gives

\[
\mathbb E[
\mathfrak P_B(M_{\rm new})\mid\mathcal F]
\ge
\mathfrak P_B(X)
-\frac{2}{u(1-u)}
\sum_i\eta_{\sigma_i}p_i^2.
\tag{5.3}
\]

But

\[
\Delta M_{ii}=\zeta p_i,
\qquad
\mathbb E[(\Delta M_{ii})^2\mid\mathcal F]
=\frac{p_i^2}{u(1-u)}.
\]

Since \(B\subset A\), every \(\sigma_i\) is known at the start of the reveal process. Summing (5.3) over the martingale and using scalar martingale orthogonality gives

\[
\mathbb E\mathfrak P_B((G_V)_{BB})
\ge
\mathbb E\mathfrak P_B((G_A)_{BB})
-
2\eta_+\Delta F_{B,+}
-
2\eta_-\Delta F_{B,-},
\]

where

\[
\Delta F_{B,\pm}
=
\sum_{i\in B}
\mathbb E\left[
\mathbf1_{\{\sigma_i=\pm1\}}
\bigl((G_V)_{ii}^2-(G_A)_{ii}^2\bigr)
\right].
\]

Using \(\mathcal C=-\frac12\mathbb E\mathfrak P\) proves:

\[
\boxed{
\mathcal C_B^V
\le
\mathcal C_B^A
+\eta_+(\vartheta)\Delta F_{B,+}
+\eta_-(\vartheta)\Delta F_{B,-}.
}
\tag{5.4}
\]

This is the sign-resolved actual-path theorem.

Choose \(\vartheta\) so that \(\chi_+=\chi_-\). Their common value is

\[
\boxed{
\chi_*(a,c)
=
\frac{
\mu_++\mu_-
+\sqrt{\mu_+^2+14\mu_+\mu_-+\mu_-^2}
}{2}.
}
\tag{5.5}
\]

Putting

\[
\eta_*(a,c)=(\chi_*(a,c)-1)_+
\]

and

\[
\Delta F_B
=\sum_{i\in B}
\left(
\mathbb E(G_V)_{ii}^2
-\mathbb E(G_A)_{ii}^2
\right)
\]

gives the reusable scalar interface

\[
\boxed{
\mathcal C_B^V
\le
\mathcal C_B^A
+\eta_*(a,c)\Delta F_B(A,V).
}
\tag{5.6}
\]

This uses one diagonal Fisher quadratic-variation budget for the whole block. It does not allocate one budget per overlapping pair.

**True-path retained-remainder Bellman theorem: PROVED.**

---

# 6. Explicit endpoint scaling

Let

\[
\delta=\min\{a,1-a-c\},
\qquad
\kappa=\frac{c^2}{4\delta(\delta+c)}.
\]

Since

\[
\mu_+\le\kappa,\qquad \mu_-\le\kappa,
\]

equation (5.5) gives

\[
\chi_*\le3\kappa.
\]

Thus the simpler bound

\[
\boxed{
\mathcal C_B^V
\le
\mathcal C_B^A
+(3\kappa-1)_+\Delta F_B
}
\tag{6.1}
\]

holds.

The diagonal quadratic variation satisfies

\[
\Delta F_B
\le
\mathbb E
\left\|
(G_V)_{BB}-(G_A)_{BB}
\right\|_{\mathrm{HS}}^2.
\]

The reviewed SA02 observation comparison is

\[
\mathbb E
\left\|
(G_V)_{BB}-(G_A)_{BB}
\right\|_{\mathrm{HS}}^2
\le
\frac1{2\delta^2}
\mathbb E
\sum_{\substack{i\in B\\j\notin A}}
|(G_V)_{ij}|^2.
\]

Its proof and its single-budget interpretation were independently checked. citeturn392383view1turn727171view1

Consequently,

\[
\boxed{
\mathcal C_B^V
\le
\mathcal C_B^A
+
\frac{\eta_*(a,c)}{2\delta^2}
\mathbb E
\sum_{\substack{i\in B\\j\notin A}}
|(G_V)_{ij}|^2.
}
\tag{6.2}
\]

For fixed \(c\),

\[
\eta_*(a,c)=O(\delta^{-1}),
\]

so the complete observation coefficient is

\[
O(\delta^{-3}).
\]

By contrast, the inherited all-Hermitian Bellman constant behaves as \(O(\delta^{-3})\) before localization and \(O(\delta^{-5})\) after the same observation-domain conversion. citeturn392383view0turn392383view1

**Strictly improved endpoint-scaling claim: PROVED.**

---

# 7. Actual sine-Toeplitz ledger

For the sine Toeplitz law on \(V=[n]\), let \(\pi_\theta\) be the random-shift partition into core blocks \(B\) of length at most \(m\), and put

\[
A_B=(B+[-L,L])\cap V.
\]

The reviewed sine tail estimates give

\[
\sum_{B\in\pi_\theta}
\mathbb E
\sum_{\substack{i\in B\\j\notin A_B}}
|G_{ij}|^2
\le
\frac{nB_*}{L},
\]

and the averaged cut-edge cost is at most

\[
\frac{nC_*\mathsf H_m}{m},
\qquad
\mathsf H_m=\sum_{k=1}^m\frac1k.
\]

The random-shift combinatorics and all finite boundary terms were independently verified in SA02. citeturn290162view3turn727171view1

Substituting (6.2) into the exact block ledger gives

\[
\boxed{
\frac{H_n''(a,c)}{n}
\le
\frac1{mn}
\sum_{\theta=0}^{m-1}
\sum_{B\in\pi_\theta}
\mathcal C_B^{A_B}
+
\frac{C_*\mathsf H_m}{m}
+
\frac{\eta_*(a,c)B_*}{2\delta^2L}.
}
\tag{7.1}
\]

Crucially,

\[
\boxed{
\mathcal C_B^{A_B}
=
-\frac12\mathbb E
\left[
2\sum_{i\in B}(G_{A_B})_{ii}^2
+
4\sum_{i<j\in B}
\left(
h_{ij}
+(v_{ij}-h_{ij})
\log\frac{v_{ij}-h_{ij}}{v_{ij}}
\right)
\right].
}
\tag{7.2}
\]

Thus the coarse-window term is:

- the actual Toeplitz-output law;
- finite and explicitly evaluable;
- inclusive of all moving probabilities;
- inclusive of the full exact signed remainder;
- not a cyclic correction or averaged kernel.

**Exact-remainder global ledger: PROVED from reviewed inputs.**

---

# 8. Benchmark constants

Take

\[
\rho=\frac12,\qquad
c=\frac{19}{20},\qquad
a\in I=\left[\frac1{50},\frac3{100}\right].
\]

Here

\[
\delta(a)
=\min\left\{a,\frac1{20}-a\right\}
\ge\frac1{50}.
\]

Therefore

\[
\kappa
\le
\frac{(19/20)^2}
{4(1/50)(1/50+19/20)}
=
\frac{9025}{776}.
\]

Equation (6.1) gives the uniform true-path inequality

\[
\boxed{
\mathcal C_B^V
\le
\mathcal C_B^A
+
\frac{26299}{776}\Delta F_B.
}
\tag{8.1}
\]

After localization,

\[
\boxed{
\mathcal C_B^V
\le
\mathcal C_B^A
+
\frac{16436875}{388}
\mathbb E
\sum_{\substack{i\in B\\j\notin A}}
|G_{ij}|^2.
}
\tag{8.2}
\]

The coefficient is

\[
\frac{16436875}{388}
\approx 4.23630799\times10^4.
\]

At the same worst-case \(\delta=1/50\), the inherited all-Hermitian coefficient is

\[
\frac{\Gamma_{\delta,c}}{4\delta^2}
=
\frac{42874390625}{776}
\approx5.52505034\times10^7.
\]

Thus the elementary rational uniform form improves this observation coefficient by a factor of approximately

\[
1304.21.
\]

It also retains \(\mathcal C_B^A\) itself, whereas the inherited envelope replaced it by a remainder-free block potential.

**Benchmark dimension-consistent signed saving: PROVED.**

---

# 9. Precise remaining gap

The theorem does **not** establish

\[
H_n''(a,19/20)\le-\varepsilon n+o(n)
\]

uniformly on

\[
a\in\left[\frac1{50},\frac3{100}\right].
\]

What remains is exactly a finite-window sign certificate strong enough to show

\[
\frac1{mn}
\sum_{\theta,B}\mathcal C_B^{A_B}
\le
-\varepsilon
-\frac{C_*\mathsf H_m}{m}
-\frac{\eta_*(a,c)B_*}{2\delta^2L}
\]

for some fixed \(m,L,\varepsilon>0\), uniformly over the benchmark interval.

This is not a renamed abstract remainder: \(\mathcal C_B^{A_B}\) is explicitly given by (7.2). It includes all probability weights, all pair signs, and the complete logarithmic remainder.

Accordingly:

- **Posterior-normalized row cone:** PROVED.
- **Exact actual-rank-one second variation:** PROVED.
- **Sign-resolved full-block Bellman payment:** PROVED.
- **\(O(\delta^{-3})\) localized observation payment:** PROVED.
- **Insertion into the complete sine block ledger:** PROVED.
- **Uniform benchmark negative curvature:** INCOMPLETE.
- **Whole legal-interval entropy-rate concavity:** INCOMPLETE.
- **General common-shift Fisher convexity:** not used and remains incomplete in the inherited record.
- **Overall S62 ultimate objective:** INCOMPLETE.

The artifact contains the full dependency ledger, complete proofs, exact constants, and claim-by-claim disposition:

:chatgpt-content-reference{index="8"}

