# PRO02 RESULT — Posterior cross-energy dissipation for true rank-one reveals

## Status

- **PROVED:** an exact finite two-branch payment inequality for the **retained logarithmic pair remainder**, valid on every genuine noisy-DPP reveal and uniform in the core dimension.
- **PROVED:** a nonnegative posterior cross-energy storage whose one-step dissipation pays the complete core matrix quadratic variation, with no edge-degree or core-pair multiplier.
- **PROVED:** a complete localization inequality for the sine Toeplitz model, including cut-pair tails, observation error, and finite endpoints.
- **PROVED:** at the balanced channel, the observation coefficient improves from the previous `Theta((1-c)^(-7))` scale to `Theta((1-c)^(-3))`.
- **DISPROVED:** the retained exact potential is not convex along all genuine rank-one reveals. A legal three-site Schur family gives a negative two-branch Jensen defect and a quantitative lower bound for the exact-potential/unweighted-Hilbert–Schmidt-budget class.
- **INCOMPLETE:** no finite benchmark window is certified to make the full upper bound negative at `c=19/20, a=1/40`. The benchmark curvature conclusion therefore remains open.

The main theorem is stronger in channel scope than required: the reveal and payment theorem holds for every strict binary channel `0<a<1-c` and every finite positive-contraction DPP kernel. The final spatial localization is then specialized to the sine Toeplitz kernel at `rho=1/2`.

Here **PROVED** means proved from the explicitly imported packet facts listed in Section 15. The far-pair estimate, posterior external-field identity, inverse gap, and sine phase-symbol estimate are dependencies, not newly re-certified results. No concrete defect was found in the subset of those inputs used below.

---

## 1. What is constructed

The constructed tool has three linked components.

1. **Exact curvature potential.** The old quartic potential is replaced by a logarithmic homogeneous pair potential that retains the complete nonnegative remainder from SA02 (3.3)–(3.4), instead of discarding it.
2. **Posterior-normalized reveal coordinates.** In these coordinates a true output reveal has the exact two branches
   \[
   X^1=X+\frac{H}{p},\qquad X^0=X-\frac{H}{1-p},\qquad H=c^2uu^*.
   \]
   The direction is not arbitrary: `u` is the actual Schur column of the current posterior kernel.
3. **Dissipative storage.** For unrevealed external coordinates `O`,
   \[
   \mathscr S(R;I,O)=\|R_{I,O}\|_{\mathrm{HS}}^2
   \]
   is a storage function. Its conditional expected decrease pays the core posterior quadratic variation exactly up to a nonnegative residual.

This is an adaptation of the storage/supply viewpoint of dissipative systems: the state is the current posterior kernel, the supply is the core quadratic variation, and the cross-block Frobenius energy is stored energy. The classical source is J. C. Willems, *Dissipative dynamical systems Part I: General theory*, Archive for Rational Mechanics and Analysis 45 (1972), 321–351, DOI `10.1007/BF00276493`. No theorem from that paper is used as a black box; the required dissipation inequality is proved below from the DPP Schur update.

The transfer would fail for an arbitrary rank-one martingale. It works here because the two branch coefficients, the branch probabilities, the column `u`, and the remaining external column `v` all come from the same posterior Schur complement, while `0<=R<=I` supplies the decisive row-energy inequality.

---

## 2. Setup and imported facts

Let `V` be finite. Let the latent process be a DPP with Hermitian kernel `Q_V`, `0<=Q_V<=I`, and pass each latent bit independently through

\[
\mathbb P(Y_i=1\mid \xi_i)=a+c\xi_i,
\qquad 0<a<1-c.
\tag{2.1}
\]

Put

\[
d=1-a-c,
\qquad \delta=\min(a,d),
\qquad K_V=aI+cQ_V.
\tag{2.2}
\]

For an observed set `B` and its true output word,

\[
G_B=\left[K_B-\operatorname{diag}(1-Y_B)\right]^{-1}.
\tag{2.3}
\]

For a core `I subseteq V`, the exact core contribution to the complete entropy Hessian is

\[
\mathcal C_I^V
=-\sum_{i\in I}\mathbb E(G_V)_{ii}^2
 +2\sum_{i<j\in I}\mathbb E g_{ij}^{V},
\tag{2.4}
\]

where each pair is conditioned on its actual full outside output. The complete Hessian is `H_n''=mathcal C_V^V`.

The following facts are imported from the supplied SA02/S7 packet and are listed again in the dependency ledger:

- the complete Hessian decomposition (2.4);
- the exact pair integral SA02 (3.3);
- the posterior external-field formula S7 (2.5)–(2.6);
- the sine far-pair bound with constant `C_*`;
- the sine phase-energy estimate
  \[
  F(\theta)=\sum_r|q_r|^2|e^{ir\theta}-1|^2\le |\theta|/\pi;
  \tag{2.5}
  \]
- the inverse gap `||G_B||<=delta^(-1)`.

All new payment, Hessian, storage, and localization steps are proved here.

---

## 3. The exact retained-remainder potential

For a Hermitian matrix `G` in an actual output-word domain, set for every pair

\[
v_{ij}=G_{ii}G_{jj},
\qquad h_{ij}=|G_{ij}|^2,
\qquad d_{ij}=v_{ij}-h_{ij}.
\tag{3.1}
\]

For actual words, `d_ij/v_ij>0`. Define, continuously at `h=0`,

\[
L(v,h)=h+(v-h)\log\frac{v-h}{v}.
\tag{3.2}
\]

A direct integration gives

\[
L(v,h)=\int_0^1(1-t)\frac{h^2}{v-th}\,dt.
\tag{3.3}
\]

Therefore the exact pair identity supplied as SA02 (3.3) becomes

\[
g(P_{ij})=-\mathbb E\bigl[L(v_{ij},h_{ij})\mid Y_{V\setminus\{i,j\}}\bigr].
\tag{3.4}
\]

Define the exact block potential

\[
\Phi_I(G)
=\sum_{i\in I}G_{ii}^2
 +2\sum_{i<j\in I}L(v_{ij},h_{ij}).
\tag{3.5}
\]

### Claim 3.1 — exact core representation: **PROVED**

For every finite `V` and every core `I`,

\[
\boxed{\mathcal C_I^V=-\mathbb E\,\Phi_I((G_V)_{II}).}
\tag{3.6}
\]

**Proof.** Sum (3.4) over internal pairs and add the diagonal Fisher terms. Also,

\[
L(v,h)=\frac12\frac{h^2}{v}+r,
\tag{3.7}
\]

where `r>=0` is exactly the SA02 remainder from (3.4). Hence (3.6) is equivalent to the supplied exact identity (4.2), but no remainder has been dropped. ∎

The sign is useful. For same-sign output bits, `v>0`, `d>0`, and `L>=0`. For opposite-sign bits, `v<0`, `d<0`, and `L<=0`.

---

## 4. Posterior normalization and the true two-branch update

Let `R^B` be the latent posterior DPP kernel after observing `Y_B`. Fix a core output word `y_I` and write

\[
\sigma_i=2y_i-1,
\qquad J=\operatorname{diag}(\sigma_i).
\tag{4.1}
\]

Set

\[
\beta_+=a(a+c),
\qquad \beta_-=d(d+c)=d(1-a),
\tag{4.2}
\]

and let `beta_i=beta_+` if `y_i=1`, `beta_i=beta_-` if `y_i=0`. Put `B_y=diag(beta_i)`.

The posterior inverse identity gives the normalized core matrix

\[
X_B:=B_y^{1/2}J(G_B)_{II}JB_y^{1/2}
     =D_y-c(R^B)_{II},
\tag{4.3}
\]

where

\[
(D_y)_{ii}=\begin{cases}
 a+c,&y_i=1,\\
 -d,&y_i=0.
\end{cases}
\tag{4.4}
\]

Thus the normalization is affine in the posterior kernel. No nonlinear ratio is claimed to be a martingale.

Define the weighted normalized potential

\[
\Psi_y(X)
=\sum_{i\in I}\frac{X_{ii}^2}{\beta_i^2}
 +2\sum_{i<j\in I}\frac{L(X_{ii}X_{jj},|X_{ij}|^2)}{\beta_i\beta_j}.
\tag{4.5}
\]

Homogeneity of `L` implies the exact identity

\[
\boxed{\Psi_y(X_B)=\Phi_I((G_B)_{II}).}
\tag{4.6}
\]

There is no normalization drift in a reveal process because the core word, hence every `beta_i`, is already observed and fixed.

### Claim 4.1 — genuine reveal branches: **PROVED**

Suppose the current posterior kernel on the active coordinates `I union O` is partitioned at the next revealed site `k in O` as

\[
R=\begin{pmatrix}
A&u\\ u^*&r
\end{pmatrix}.
\tag{4.7}
\]

Let

\[
p=\mathbb P(Y_k=1\mid\mathcal F)=a+cr.
\tag{4.8}
\]

After revealing `Y_k` and marginalizing the latent coordinate `k`, the posterior kernels on the remaining coordinates are

\[
R^1=A-\frac{c}{p}uu^*,
\qquad
R^0=A+\frac{c}{1-p}uu^*,
\tag{4.9}
\]

with probabilities `p` and `1-p`. Consequently, on the core,

\[
\boxed{
X^1=X+\frac{H}{p},
\qquad
X^0=X-\frac{H}{1-p},
\qquad H=c^2u_Iu_I^*.}
\tag{4.10}
\]

**Proof.** Weighting one coordinate of a DPP by a likelihood ratio `t` changes the remaining kernel to

\[
A-\frac{t-1}{1+(t-1)r}uu^*.
\tag{4.11}
\]

This follows directly from the `L`-ensemble transformation `L -> D^{1/2}LD^{1/2}` and one Sherman–Morrison inversion. For branch one, `t=(a+c)/a`, giving the first formula in (4.9). For branch zero, `t=d/(d+c)`, giving the second. Equation (4.10) follows from (4.3). ∎

The scalar branch variable is

\[
\zeta=\begin{cases}1/p,&Y_k=1,\\-1/(1-p),&Y_k=0,
\end{cases}
\qquad \mathbb E(\zeta\mid\mathcal F)=0,
\qquad \mathbb E(\zeta^2\mid\mathcal F)=\frac1{p(1-p)}.
\tag{4.12}
\]

---

## 5. Full finite-update control of the exact potential

The next calculation is the geometric core of P1. It controls every point on both branch segments, not only the directional Hessian at the initial state.

Let `X(s)=X+sww^*`. For a pair, write

\[
x_i=X_{ii},\quad x_j=X_{jj},\quad z=X_{ij},
\quad \alpha_i=|w_i|^2,\quad \alpha_j=|w_j|^2,
\tag{5.1}
\]

and along the path let `v=x_i x_j`, `h=|z|^2`, `d=v-h`.

Because the direction is rank one,

\[
v''=h''=2\alpha_i\alpha_j,
\qquad d''=0.
\tag{5.2}
\]

### Claim 5.1 — exact rank-one pair Hessian: **PROVED**

Along every nonsingular part of the path,

\[
\boxed{
\frac{d^2}{ds^2}L(v(s),h(s))
=2\alpha_i\alpha_j\frac{h}{v}
+d\left(\frac{v'}v-\frac{d'}d\right)^2.}
\tag{5.3}
\]

The identity extends continuously through `h=0`.

**Proof.** Differentiate `L=h+d log(d/v)`, use `h=v-d`, and then use `d''=0`. Every derivative of the moving diagonal denominators and the off-diagonal cross term is retained. ∎

For same-sign core bits, `v,d>0`, so (5.3) is nonnegative.

For opposite signs write

\[
x_i=A>0,
\qquad x_j=-B<0,
\qquad r_0=\frac{h}{AB},
\qquad P=\frac{\alpha_i}{A},
\qquad Q=\frac{\alpha_j}{B}.
\tag{5.4}
\]

Choose `theta` so that

\[
\operatorname{Re}(\bar z w_i\bar w_j)=AB\sqrt{r_0PQ}\cos\theta.
\tag{5.5}
\]

Then (5.3) becomes

\[
-\frac{L''}{h}
=2PQ+
\frac{[\sqrt{r_0}(P-Q)-2\sqrt{PQ}\cos\theta]^2}{1+r_0}
\le 3(P^2+Q^2).
\tag{5.6}
\]

Indeed,

\[
[\sqrt{r_0}|P-Q|+2\sqrt{PQ}]^2
\le(1+r_0)[(P-Q)^2+4PQ]
=(1+r_0)(P+Q)^2,
\tag{5.7}
\]

and `2PQ+(P+Q)^2<=3(P^2+Q^2)`.

Now define

\[
\kappa=\frac{c^2}{4\delta(\delta+c)}.
\tag{5.8}
\]

For a positive-contraction posterior `R`,

\[
\sum_{j\ne i}|R_{ij}|^2\le R_{ii}(1-R_{ii}).
\tag{5.9}
\]

For a positive core output, `|X_ii|=a+c(1-R_ii)`; for a negative output, `|X_ii|=d+cR_ii`. The elementary maximization

\[
\max_{0\le e\le1}\frac{c^2e(1-e)}{(t+ce)^2}
=\frac{c^2}{4t(t+c)}
\le\kappa,
\qquad t\in\{a,d\},
\tag{5.10}
\]

therefore gives

\[
\frac{\sum_{j:\sigma_j=-\sigma_i}|X_{ij}|^2}{|X_{ii}|^2}\le\kappa.
\tag{5.11}
\]

Put

\[
\beta_{\max}=\max(\beta_+,\beta_-),
\qquad
\boxed{
\Gamma_{\mathrm{ro}}(a,c)
=\left[
\frac{3\kappa}{\beta_+\beta_-}
-\frac1{\beta_{\max}^2}
\right]_+.}
\tag{5.12}
\]

### Claim 5.2 — rank-one semiconvexity on the full genuine segment: **PROVED**

For every positive-contraction posterior state and every rank-one direction `H=ww*` arising from a true reveal,

\[
\boxed{
D^2\Psi_y(X)[H,H]
\ge -2\Gamma_{\mathrm{ro}}(a,c)\|H\|_{\mathrm{HS}}^2.}
\tag{5.13}
\]

The same bound holds at every point of both segments joining `X` to `X^1` and `X^0`.

**Proof.** The diagonal part of (4.5) contributes

\[
2\sum_i\frac{\alpha_i^2}{\beta_i^2}.
\tag{5.14}
\]

Same-sign pairs contribute nonnegatively. By (5.6), opposite-sign pairs contribute at least

\[
-\frac{6}{\beta_+\beta_-}
 \sum_i\frac{\alpha_i^2}{|X_{ii}|^2}
 \sum_{j:\sigma_j=-\sigma_i}|X_{ij}|^2.
\tag{5.15}
\]

Use (5.11). This yields

\[
D^2\Psi_y(X)[H,H]
\ge2\sum_i
\left(\frac1{\beta_i^2}-\frac{3\kappa}{\beta_+\beta_-}\right)
\alpha_i^2.
\tag{5.16}
\]

By (5.12), this is at least `-2 Gamma_ro sum_i alpha_i^2`, and

\[
\sum_i\alpha_i^2\le\left(\sum_i\alpha_i\right)^2
=\|ww^*\|_{\mathrm{HS}}^2.
\tag{5.17}
\]

For the segment assertion, `X+sH` corresponds to the core block of a convex combination of the current posterior kernel and the appropriate branch posterior. Positive contractions form a convex set. Equations (5.9)–(5.11) and the sign domain therefore remain valid all along the segment. ∎

### Theorem 5.3 — exact two-branch Jensen payment: **PROVED**

For every true reveal,

\[
\boxed{
 p\Psi_y(X^1)+(1-p)\Psi_y(X^0)-\Psi_y(X)
 \ge
 -\Gamma_{\mathrm{ro}}(a,c)
 \frac{\|H\|_{\mathrm{HS}}^2}{p(1-p)}.}
\tag{5.18}
\]

Equivalently,

\[
\mathbb E[\Psi_y(X_{t+1})-\Psi_y(X_t)\mid\mathcal F_t]
\ge
-\Gamma_{\mathrm{ro}}(a,c)
 \mathbb E[\|\Delta X_t\|_{\mathrm{HS}}^2\mid\mathcal F_t].
\tag{5.19}
\]

**Proof.** By Claim 5.2,

\[
s\longmapsto \Psi_y(X+sH)+
\Gamma_{\mathrm{ro}}\|H\|_{\mathrm{HS}}^2s^2
\tag{5.20}
\]

is convex on the entire interval containing both true branch points. Apply Jensen to the mean-zero random variable `zeta` from (4.12). This is a finite-update argument, not a Taylor approximation. ∎

This proves P1, including moving denominators, off-diagonal cross terms, and the complete retained pair remainder.

---

## 6. A posterior cross-energy storage that pays all reveals once

Let the currently active latent coordinates be `I union O`. Reveal `k in O` and write `O'=O\{k}`. Partition the current posterior kernel as

\[
R=
\begin{pmatrix}
A&B&u\\
B^*&C&v\\
u^*&v^*&r
\end{pmatrix},
\tag{6.1}
\]

with blocks indexed by `I`, `O'`, and `k`.

Define the storage

\[
\mathscr S_t=\|R_{I,O}\|_{\mathrm{HS}}^2.
\tag{6.2}
\]

Under the two branches, the new cross block is

\[
B'=B+\eta uv^*,
\qquad
\eta=\begin{cases}-c/p,&Y_k=1,\\ c/(1-p),&Y_k=0.
\end{cases}
\tag{6.3}
\]

Thus

\[
\mathbb E(\eta\mid\mathcal F)=0,
\qquad
\mathbb E(\eta^2\mid\mathcal F)=\frac{c^2}{p(1-p)}.
\tag{6.4}
\]

### Theorem 6.1 — one-step dissipation inequality: **PROVED**

For every true reveal,

\[
\boxed{
\mathbb E[\mathscr S_{t+1}
 +\|\Delta R_{II,t}\|_{\mathrm{HS}}^2\mid\mathcal F_t]
\le \mathscr S_t.}
\tag{6.5}
\]

More precisely, the nonnegative residual is

\[
\begin{aligned}
&\mathscr S_t-
 \mathbb E[\mathscr S_{t+1}
 +\|\Delta R_{II,t}\|_{\mathrm{HS}}^2\mid\mathcal F_t]\\
&\quad=
\|u\|^2
\left[
1-\frac{c^2(\|u\|^2+\|v\|^2)}{p(1-p)}
\right]\\
&\quad\ge
\|u\|^2
\frac{(1-r)a(1-a)+r\,d(a+c)}{p(1-p)}
\ge0.
\end{aligned}
\tag{6.6}
\]

**Proof.** Since the cross term vanishes after averaging `eta`,

\[
\mathbb E\|B'\|_{\mathrm{HS}}^2
=\|B\|_{\mathrm{HS}}^2
 +\frac{c^2}{p(1-p)}\|u\|^2\|v\|^2.
\tag{6.7}
\]

The core update is `Delta R_II=eta uu*`, hence

\[
\mathbb E\|\Delta R_{II}\|_{\mathrm{HS}}^2
=\frac{c^2}{p(1-p)}\|u\|^4.
\tag{6.8}
\]

Subtract (6.7) and (6.8) from the old storage `||B||^2+||u||^2`. Because `0<=R<=I`,

\[
\|u\|^2+\|v\|^2\le r(1-r).
\tag{6.9}
\]

Finally,

\[
\begin{aligned}
p(1-p)-c^2r(1-r)
&=(1-r)a(1-a)+r\,d(a+c)>0.
\end{aligned}
\tag{6.10}
\]

This proves (6.5)–(6.6). ∎

### Corollary 6.2 — summable dimension-uniform budget: **PROVED**

Reveal any set of external outputs in any order, always using one common filtration. If `O_0=V\A`, then

\[
\boxed{
\sum_t\mathbb E\|\Delta R_{II,t}\|_{\mathrm{HS}}^2
\le
\mathbb E\|R^A_{I,V\setminus A}\|_{\mathrm{HS}}^2.}
\tag{6.11}
\]

Since `Delta X=-c Delta R_II`,

\[
\boxed{
\sum_t\mathbb E\|\Delta X_t\|_{\mathrm{HS}}^2
\le
c^2\mathbb E\|R^A_{I,V\setminus A}\|_{\mathrm{HS}}^2.}
\tag{6.12}
\]

There is no factor `|I|`, number of internal pairs, or graph degree. Every reveal spends from one cross-block storage account.

---

## 7. Joint exact block payment

Combine the finite two-branch inequality (5.19), the storage telescope (6.12), the exact potential relation (4.6), and the exact core identity (3.6).

### Theorem 7.1 — dimension-uniform genuine-reveal payment: **PROVED**

For every finite positive-contraction DPP kernel, every strict channel `0<a<1-c`, and every `I subseteq A subseteq V`,

\[
\boxed{
\mathcal C_I^V
\le
-\mathbb E\,\Phi_I((G_A)_{II})
+\Gamma_{\mathrm{ro}}(a,c)c^2
 \mathbb E\|R^A_{I,V\setminus A}\|_{\mathrm{HS}}^2.}
\tag{7.1}
\]

**Proof.** Conditional on `Y_A`, reveal all outputs in `V\A`. By (5.19) and (6.12),

\[
\mathbb E\Psi_y(X_V)
\ge
\mathbb E\Psi_y(X_A)
-\Gamma_{\mathrm{ro}}c^2
 \mathbb E\|R^A_{I,V\setminus A}\|_{\mathrm{HS}}^2.
\tag{7.2}
\]

Use (4.6), multiply by `-1`, and use (3.6). ∎

This is the requested reusable payment theorem. It keeps every pair in the block, every pair is computed from the same actual posterior and the same reveal filtration, and the complete exact pair remainder is retained.

---

## 8. Spatial payment for the sine posterior storage

Now specialize to the sine Toeplitz compression, with the final target `rho=1/2`. Let `I` be an interval of length `q`, and let

\[
A=(I+[-L,L])\cap V,
\qquad L\ge1.
\tag{8.1}
\]

### Lemma 8.1 — conditional posterior Dirichlet contraction: **PROVED**

For every finitely supported complex sequence `f`,

\[
\mathbb E_{Y_A}
\sum_{u,v}|R^A_{uv}|^2|f_u-f_v|^2
\le
\mathcal E_P(f)
:=\sum_{u,v\in\mathbb Z}|q_{u-v}|^2|f_u-f_v|^2.
\tag{8.2}
\]

**Proof.** A positive-contraction DPP kernel `R` satisfies

\[
\operatorname{Var}_R\left(\sum_i f_i\xi_i\right)
\ge\frac12\sum_{u,v}|R_{uv}|^2|f_u-f_v|^2.
\tag{8.3}
\]

Take conditional expectation given `Y_A` and use the law of total variance. Embed the finite model in a larger sine compression containing the support of `f`. For a compression of the ambient sine projection, twice the prior variance equals `mathcal E_P(f)` after extending `f` by zero. This gives (8.2). ∎

Choose a tent `g` that is one on `I`, has linear ramps of length `q` on both sides, and is zero beyond those ramps. Then

\[
\|g\|_2^2\le\frac{5q}{3},
\qquad
\|\nabla g\|_2^2=\frac2q.
\tag{8.4}
\]

Using the imported phase symbol estimate (2.5),

\[
\mathcal E_P(g)\le\frac12\|g\|_2\|\nabla g\|_2<1.
\tag{8.5}
\]

For `f_theta(j)=g_j e^{i theta j}`,

\[
\mathcal E_P(f_\theta)
\le1+\frac{2q|\theta|}{\pi}.
\tag{8.6}
\]

Average `theta` uniformly on `[-pi/L,pi/L]`. If `i in I` and `j notin A`, then `|i-j|>=L`, and

\[
\operatorname{Av}_\theta|f_\theta(i)-f_\theta(j)|^2
\ge1-\frac1{\pi^2}>\frac89.
\tag{8.7}
\]

The ordered Dirichlet sum contains both orientations of each cross pair.

### Theorem 8.2 — spatial storage bound: **PROVED**

\[
\boxed{
\mathbb E\|R^A_{I,V\setminus A}\|_{\mathrm{HS}}^2
\le\frac9{16}\left(1+\frac qL\right).}
\tag{8.8}
\]

**Proof.** Apply (8.2) to `f_theta`, average over `theta`, use (8.6), and lower-bound the two oriented copies of every desired cross term by `2*(8/9)`. ∎

The constant is independent of the number of internal pairs and of the ambient volume.

Combining (7.1) and (8.8) gives

\[
\boxed{
\mathcal C_I^V
\le
-\mathbb E\Phi_I((G_A)_{II})
+A_{\mathrm{ro}}(a,c)\left(1+\frac{|I|}{L}\right),}
\tag{8.9}
\]

where

\[
\boxed{A_{\mathrm{ro}}(a,c)=\frac9{16}c^2\Gamma_{\mathrm{ro}}(a,c).}
\tag{8.10}
\]

---

## 9. Reconnection to the complete entropy Hessian

Let `V=[n]`. For each shift `theta=0,...,m-1`, cut the integer line into blocks of length `m` and intersect with `V`; call the resulting partition `pi_theta`. For each core block `I`, put

\[
A_I=(I+[-L,L])\cap V
\tag{9.1}
\]

and define the exact local quantity

\[
\mathcal L(I,A_I)
=-\mathbb E\Phi_I((G_{A_I})_{II}).
\tag{9.2}
\]

Let

\[
\mathsf h_m=\sum_{k=1}^m\frac1k
\tag{9.3}
\]

be the harmonic number. The supplied S7 tail constant is

\[
C_*=
\min\left\{
\frac{3c^4}{16\delta^8},
\frac{3c^2M}{2\beta_*^2}
\right\},
\quad
\beta_*=\delta(\delta+c),
\quad
M=\max\left(1,\log\frac{(a+c)(1-a)}{ad}\right).
\tag{9.4}
\]

A pair at distance `r` is cut in the proportion `min(r/m,1)` of shifts. Since

\[
\min(r/m,1)=\frac1m\sum_{k=1}^m\mathbf 1_{\{r\ge k\}},
\tag{9.5}
\]

the absolute cut-pair contribution is at most `n C_* mathsf h_m/m`.

For a fixed shift, the number of nonempty grid blocks is at most `n/m+2`. Summing (8.8) over blocks gives

\[
\sum_{I\in\pi_\theta}
\mathbb E\|R^{A_I}_{I,V\setminus A_I}\|_{\mathrm{HS}}^2
\le\frac9{16}\left(\frac nm+2+\frac nL\right).
\tag{9.6}
\]

### Theorem 9.1 — finite complete-Hessian localization: **PROVED**

For every `n,m,L>=1`,

\[
\boxed{
\begin{aligned}
\frac{H_n''(a)}n
\le{}&
\frac1{mn}\sum_{\theta=0}^{m-1}
\sum_{I\in\pi_\theta}\mathcal L(I,A_I)
+\frac{C_*\mathsf h_m}{m}\\
&+A_{\mathrm{ro}}(a,c)
\left(\frac1m+\frac1L+\frac2n\right).
\end{aligned}}
\tag{9.7}
\]

**Proof.** For each shift, the sum of exact core curvatures over its blocks contains every diagonal term and every uncut pair. Bound cut pairs by absolute value and average over shifts using (9.5). Apply Theorem 7.1 to every block and then use (9.6). ∎

This is a bound for the complete `H_n''`, not for a favorable subexpression.

### Stationary one-window form and finite endpoints

For the infinite stationary sine process let

\[
I=[1,m],
\qquad A=[1-L,m+L],
\tag{9.8}
\]

and define

\[
\boxed{
\mathcal W_{m,L}
=-\frac1m\mathbb E\Phi_I((G_A)_{II}).}
\tag{9.9}
\]

Define

\[
\ell(x)=\frac{(1+x)\log(1+x)-x}{x},
\qquad \ell(0)=0,
\tag{9.10}
\]

and

\[
\Lambda_{\delta,c}=\max(1,\ell(\kappa)),
\qquad
\Xi_{\delta,c}=\Lambda_{\delta,c}\delta^{-2}.
\tag{9.11}
\]

For same-sign pairs, `0<=L(v,h)<=h`. For an opposite-sign pair, applying (5.11) at both endpoints gives `h/|v|<=kappa`; hence

\[
|L(v,h)|=h\,\ell(h/|v|)\le h\ell(\kappa).
\tag{9.12}
\]

Consequently,

\[
|\Phi_I(G)|
\le\Lambda_{\delta,c}\|G_{II}\|_{\mathrm{HS}}^2
\le\Xi_{\delta,c}|I|.
\tag{9.13}
\]

For each shift, at most `2(m+L)` core sites lie in a short or endpoint-truncated block. Replacing those blocks by the stationary reference costs at most `4 Xi_(delta,c)(m+L)`.

### Corollary 9.2 — stationary finite-endpoint bound: **PROVED**

\[
\boxed{
\begin{aligned}
\frac{H_n''(a)}n
\le{}&
\mathcal W_{m,L}
+\frac{C_*\mathsf h_m}{m}
+A_{\mathrm{ro}}(a,c)
 \left(\frac1m+\frac1L+\frac2n\right)\\
&+\frac{4\Xi_{\delta,c}(m+L)}n.
\end{aligned}}
\tag{9.14}
\]

In particular,

\[
\boxed{
\limsup_{n\to\infty}\frac{H_n''(a)}n
\le
\mathcal W_{m,L}
+\frac{C_*\mathsf h_m}{m}
+A_{\mathrm{ro}}(a,c)
 \left(\frac1m+\frac1L\right).}
\tag{9.15}
\]

Hence the explicit finite-window condition

\[
\boxed{
\mathcal W_{m,L}
+\frac{C_*\mathsf h_m}{m}
+A_{\mathrm{ro}}(a,c)
 \left(\frac1m+\frac1L\right)<0}
\tag{9.16}
\]

is sufficient for negative asymptotic curvature. Including the two `1/n` terms from (9.14) gives a sufficient condition for a specified finite `n`.

This proves P3.

---

## 10. Exact improvement at the benchmark

Now set

\[
a=d=\delta=\frac1{40},
\qquad c=\frac{19}{20},
\qquad \beta_+=\beta_-=\beta=\frac{39}{1600}.
\tag{10.1}
\]

Then

\[
\kappa=\frac{361}{39},
\qquad
3\kappa-1=\frac{348}{13},
\tag{10.2}
\]

and

\[
\boxed{
\Gamma_{\mathrm{ro}}
=\frac{3\kappa-1}{\beta^2}
=\frac{296960000}{6591}
\approx 45055.3785465.}
\tag{10.3}
\]

Therefore

\[
\boxed{
A_{\mathrm{ro}}
=\frac9{16}c^2\Gamma_{\mathrm{ro}}
=\frac{50251200}{2197}
\approx 22872.6445152.}
\tag{10.4}
\]

The old SA02 observation coefficient was

\[
\boxed{
A_{\mathrm{old}}
=\frac{271401301760000}{6591}
\approx4.11775605765\times10^{10},}
\tag{10.5}
\]

multiplying `1/L`.

The new observation term is

\[
A_{\mathrm{ro}}\left(\frac1m+\frac1L\right).
\tag{10.6}
\]

If `m>=L`, it is at most `2 A_ro/L`, so the benchmark coefficient is smaller than the old one by the factor

\[
\frac{A_{\mathrm{old}}}{2A_{\mathrm{ro}}}
\approx 900148.659.
\tag{10.7}
\]

If `m` is taken much larger than `L`, the comparison of the `1/L` coefficients alone is approximately `1.8002973*10^6`.

The other explicit benchmark constants are

\[
C_*=\frac{1155200}{507}\log(1521)
\approx16694.8576474,
\tag{10.8}
\]

and

\[
\Xi_{\delta,c}
=1600\,\ell(361/39)
\approx2527.03007376.
\tag{10.9}
\]

### Endpoint scaling: **PROVED**

On the balanced channel `delta=(1-c)/2`, as `delta downarrow 0`,

\[
A_{\mathrm{old}}=\Theta(\delta^{-7}),
\tag{10.10}
\]

whereas

\[
\boxed{
A_{\mathrm{ro}}
\sim\frac{27}{64}\delta^{-3}
=\frac{27}{8}(1-c)^{-3}.}
\tag{10.11}
\]

Thus four endpoint powers are removed. The improvement is structural: the exact normalized reveal is paid by posterior cross-energy dissipation. It is not a small optimization of the old all-direction Hessian constants.

---

## 11. A legal obstruction for raw convexity and for this budget class

The exact potential is not convex along every genuine reveal.

Fix a balanced channel `a=d=delta`, `c=1-2delta`, with `0<delta<1/4`, and put `e=delta/c`. For `epsilon>0` small, let

\[
\lambda_\epsilon=\frac12-2\epsilon^2
\tag{11.1}
\]

and define the strict posterior kernel

\[
R_\epsilon=
\begin{pmatrix}
1-e&\sqrt{\lambda_\epsilon e}&\epsilon\sqrt e\\
\sqrt{\lambda_\epsilon e}&1/2&0\\
\epsilon\sqrt e&0&1/2
\end{pmatrix}.
\tag{11.2}
\]

Take core outputs `(1,0)` and reveal site three.

### Claim 11.1 — legality and realizability: **PROVED**

For every sufficiently small `epsilon>0`,

\[
0<R_\epsilon<I.
\tag{11.3}
\]

Moreover it is the actual posterior of a strict DPP prior after observing the stated core word.

**Proof.** Using the lower `2x2` diagonal block, the Schur complement for `I-R_epsilon` is

\[
e-2\lambda_\epsilon e-2\epsilon^2e=2\epsilon^2e>0.
\tag{11.4}
\]

The Schur complement for `R_epsilon` is

\[
1-e-2\lambda_\epsilon e-2\epsilon^2e
=1-2e+2\epsilon^2e>0,
\tag{11.5}
\]

because `e<1/2` when `delta<1/4`.

For realizability, let `D` be the positive diagonal external field corresponding to the observed word `(1,0)` and an unobserved third coordinate. Given `L_R=R(I-R)^(-1)`, define

\[
L_Q=D^{-1/2}L_RD^{-1/2},
\qquad Q=L_Q(I+L_Q)^{-1}.
\tag{11.6}
\]

Then `0<Q<I`, and applying the field `D` returns exactly `R`. Hence the reveal is a genuine noisy-DPP reveal, not an arbitrary rank-one construction. ∎

For the normalized core matrix, as `epsilon->0`,

\[
X_{11}=2\delta,
\qquad X_{22}=-\frac12,
\qquad |X_{12}|^2\longrightarrow\frac{c\delta}{2}.
\tag{11.7}
\]

The reveal direction is a positive multiple of `e_1e_1^*`. From (5.3),

\[
\lim_{\epsilon\downarrow0}
\frac{D^2\Phi(X)[H,H]}{\|H\|_{\mathrm{HS}}^2}
=2-\frac{c^2}{8\delta(1+c/2)}.
\tag{11.8}
\]

### Claim 11.2 — raw exact-potential reveal convexity: **DISPROVED**

At the benchmark `delta=1/40, c=19/20`, the right side of (11.8) is negative. Therefore the exact potential is not convex along all genuine reveal directions.

More quantitatively, suppose a scalar `gamma` satisfies, for every strict DPP posterior state and every genuine balanced reveal,

\[
p\Phi(X+H/p)+(1-p)\Phi(X-H/(1-p))-\Phi(X)
\ge-\gamma\frac{\|H\|_{\mathrm{HS}}^2}{p(1-p)}.
\tag{11.9}
\]

Then necessarily

\[
\boxed{
\gamma\ge
\left[
\frac{c^2}{16\delta(1+c/2)}-1
\right]_+.}
\tag{11.10}
\]

At the benchmark this lower bound is

\[
\gamma\ge\frac{125}{236}\approx0.529661017.
\tag{11.11}
\]

As `delta downarrow0`, it is `Omega(delta^(-1))`. After the unavoidable balanced scaling by `beta^(-2)`, this is `Omega(delta^(-3))` for the exact-potential plus unweighted Hilbert–Schmidt quadratic-variation class.

This obstruction is deliberately narrow. It does **not** rule out a different potential, a weighted/self-normalized supply, or a sine-specific improvement. It also does not show that every Bellman approach has cubic endpoint cost. It proves only the stated lower bound for (11.9) over all strict DPP posterior states.

The upper constant from this report has normalized leading behavior `3/(4 delta)`; the lower family gives `1/(24 delta)`. Thus the endpoint exponent is sharp for this class, while the leading constant is not.

---

## 12. Benchmark conclusion and smallest remaining obstruction

### Benchmark negative curvature: **INCOMPLETE**

No pair `(m,L)` has been certified to satisfy (9.16) at

\[
\rho=1/2,
\qquad c=19/20,
\qquad a=1/40.
\tag{12.1}
\]

The new theorem reduces the remaining task to a finite, explicit statement:

> certify one true stationary window value `mathcal W_(m,L)` strongly enough that
> \[
> \mathcal W_{m,L}
> +\frac{C_*\mathsf h_m}{m}
> +\frac{50251200}{2197}
> \left(\frac1m+\frac1L\right)<0.
> \tag{12.2}
> \]

For a specified finite `n`, add the explicit endpoint terms from (9.14).

This is the smallest obstruction left by the present mechanism. The observation-domain change of the exact remainder is no longer an unnamed error; it is fully paid by Theorems 6.1 and 7.1. The unresolved issue is the magnitude of one finite true-window expectation relative to known tail and localization costs.

Exploratory small-window values are negative, but they are far too small to overcome the explicit costs at those window sizes and are not a benchmark certificate.

---

## 13. Boundary and failure checks

1. **Strict branch probabilities — PROVED.** Since `r in [0,1]`, `p=a+cr in [a,a+c] subset (0,1)`. Both branch denominators are finite.
2. **Moving denominators — PROVED.** Equation (5.3) differentiates `v`, `d`, and their logarithms exactly. The square in (5.3) contains every denominator and cross-term drift.
3. **No nonlinear martingale assumption — PROVED.** Only the affine matrix `X=D_y-cR_II` has mean-zero rank-one increments. Ratios such as `h/(|x_i x_j|)` are used only pointwise in Hessian estimates.
4. **Entire finite branch segments — PROVED.** The proof uses convex combinations of actual posterior kernels, so the semiconvexity bound holds between the initial point and both branch endpoints.
5. **Zero off-diagonal entries — PROVED by continuity.** The function `L` has an analytic extension at `h=0`, with `L=O(h^2/v)` on same-sign blocks.
6. **Semidefinite prior kernels — PROVED by approximation.** The channel is strict; formulas first proved for strict `Q` extend to positive contractions by continuity.
7. **No edge multiplier — PROVED.** The only block-count term is `1/m`, arising from one bounded spatial storage cost per block. There is no number-of-pairs or maximum-degree factor.
8. **No incompatible pair posteriors — PROVED.** Every internal pair is evaluated from the same `G_t`, equivalently the same posterior `R_t`, along one filtration.
9. **Raw exact potential convexity — DISPROVED.** Section 11 supplies a legal actual-reveal counterexample.
10. **Sine-only optimality — UNREVIEWED/INCOMPLETE.** The lower-bound family is a general strict DPP posterior, not a sine Toeplitz posterior. No sine-specific lower bound is claimed.

---

## 14. Calculations actually performed

The accompanying `PRO02_checks.py` was executed.

### Exact or symbolic checks

- SymPy simplified the difference between the two sides of (5.3) to exactly zero.
- Python rational arithmetic produced
  \[
  \beta=39/1600,
  \quad \kappa=361/39,
  \quad A_{\mathrm{ro}}=50251200/2197,
  \quad A_{\mathrm{old}}=271401301760000/6591,
  \tag{14.1}
  \]
  and the lower bound `125/236` in (11.11).

### High-precision finite enumeration

A 60-digit enumeration of all `2^6` benchmark words gave

\[
H_6''=-49.5655212392509631975961954433\ldots
\tag{14.2}
\]

and

\[
-\mathbb E\Phi_V(G_V)
=-49.5655212392509631975961954433\ldots,
\tag{14.3}
\]

with numerical discrepancy below `10^(-59)`. This checks the exact-potential identity in one nontrivial sine instance; it is not used as proof.

The same code gave the exploratory local value

\[
\mathcal W_{4,2}
=-10.13300431506280689245412\ldots.
\tag{14.4}
\]

This value does not close (12.2).

### Floating-point stress tests

- Five hundred random positive-contraction posterior states at the benchmark produced no violation of (5.18); the smallest computed slack was about `4.73*10^(-5)`.
- For the legal obstruction with `epsilon=0.02`, the minimum eigenvalues of `R` and `I-R` were positive, and the finite two-branch defect divided by quadratic variation was approximately `-0.52556`, approaching the exact limit `-125/236`.

These random and floating-point checks are diagnostics only. No interval certificate or large-window benchmark computation was performed.

---

## 15. Dependency ledger

| Item | Status in this report | Source or proof |
|---|---|---|
| Complete entropy Hessian decomposition | Imported | `inputs/TASK.md`, equation (1); S7 Section 5 |
| Exact pair integral and nonnegative remainder | Imported, then repackaged exactly | `inputs/SA02_MATRIX_BELLMAN_FULL_BLOCK.md`, (3.3)–(3.4) |
| Posterior external-field identity | Imported | `inputs/sources/S7_PROOF.md`, (2.5)–(2.6) |
| True one-site posterior branch formulas | Re-proved | Claim 4.1 |
| Exact logarithmic block potential | New construction here; algebra proved | Section 3 |
| Rank-one Hessian identity and semiconvexity | Proved here | Claims 5.1–5.2 |
| Finite two-branch Jensen inequality | Proved here | Theorem 5.3 |
| Posterior cross-energy storage | New construction here; proved | Theorem 6.1 |
| Dimension-uniform total payment | Proved here | Corollary 6.2 and Theorem 7.1 |
| Sine phase symbol estimate | Imported | S7 (3.2) |
| Posterior Dirichlet contraction and tent localization | Re-proved/adapted | Lemma 8.1 and Theorem 8.2 |
| Absolute far-pair tail | Imported | S7 Theorem A / SA02 Section 8 |
| Full finite and stationary Hessian bounds | Proved here | Theorem 9.1 and Corollary 9.2 |
| Old coefficient used for comparison | Imported and recomputed | SA02 (8.3), rational arithmetic |
| Raw-convexity counterexample and budget lower bound | Constructed and proved here | Section 11 |
| Benchmark sign | Not proved | Section 12 |

`SOL_REVIEW.md` and `SA02_SOL_ASSESSMENT_AND_NEXT_ROUTE.md` were not used as theorem inputs. The latter supplied a research direction only. The earlier audit in the conversation remains an audit of the old SA02 package and is not validation of the present result.

No result from another PRO assignment was read or used.

---

## 16. Short statement for a later independent reviewer

Please independently verify four load-bearing points:

1. the exact pair Hessian identity (5.3) and the opposite-sign bound (5.6);
2. the weighting and constant in (5.12)–(5.18);
3. the storage residual identity (6.6), especially the use of `p(1-p)-c^2r(1-r)`;
4. the normalization and endpoint counts in (9.7) and (9.14).

If those four points pass, the dimension-uniform payment theorem (7.1), the full localization theorem (9.14), and the benchmark coefficient (10.4) follow. The benchmark negative-curvature conclusion itself should remain marked **INCOMPLETE** until a finite window satisfies (12.2) by proof or certified computation.

---

## References

1. J. C. Willems, “Dissipative dynamical systems Part I: General theory,” *Archive for Rational Mechanics and Analysis* 45 (1972), 321–351. DOI: `10.1007/BF00276493`.
2. R. Lyons, “Determinantal probability measures,” *Publications Mathématiques de l'IHÉS* 98 (2003), 167–212.
3. J. B. Hough, M. Krishnapur, Y. Peres, and B. Virág, “Determinantal processes and independence,” *Probability Surveys* 3 (2006), 206–229.
4. Supplied repository packet: `research/PRO02/inputs/`, especially the files listed in the dependency ledger.
