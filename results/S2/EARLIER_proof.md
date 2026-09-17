# A rank-one projection curvature theorem for route S2

**Status: PROVED_SCOPED_LEMMA.** All logarithms are natural. The main S-sine entropy-rate concavity problem is **not proved** here.

This document proves P2, with a positive quantitative margin, for every rank-one and co-rank-one projection in every finite dimension when `1/2 <= c < 1`. Thus it includes the entire requested high-contrast range `37/40 < c < 1` for these families. Coordinate direct sums of these projections are also covered. The new sign estimate is convexity, in the channel-shift parameter, of the entropy increase under balancing two singleton weights. It is proved by a positive Laplace representation; it is not an equivalent reformulation of P2.

Two companion documents contain additional results: `high_fidelity.md` proves a finite-dimensional high-fidelity theorem for every fixed-cardinality input law, and `bridge.md` proves an audited, endpoint-uniform complete-configuration entropy bridge to the S-sine process. Neither extends the rank-one result to cyclic projections of rank proportional to dimension.

## 1. Setup and the curvature inequality that is actually needed

Let `P = P* = P^2` be a projection on `C^n`, of rank `k`. The projection DPP has law

\[
 \mu(S)=\det P_S,\qquad |S|=k.
\]

Zero minors are allowed and have probability zero. With `P=VV*`, `V*V=I_k`, Cauchy--Binet gives `sum_{|S|=k} det P_S=1`.

Fix `0<c<1`, put `delta=1-c`, and use the independent-coordinate channel

\[
 \Pr(Y_i=1\mid X_i=0)=a,\qquad
 \Pr(Y_i=1\mid X_i=1)=a+c,\qquad 0\le a\le\delta.
\]

Write `q_a(T)=Pr(Y=T)`, `H_P(a)=H(Y)`, and `Pcal_P(a)=H(X|Y)`. All of these are entropies of full finite random vectors, not just of their cardinalities. For `0<a<delta`, all output atoms are strictly positive and are polynomials in `a`. Therefore all the entropies in this paragraph are smooth in the interior, even if the input has zero minors.

The exact identity

\[
 H_P(a)=H(X)+(n-k)b(a)+kb(a+c)-\mathcal P_P(a),
 \qquad b(u)=-u\log u-(1-u)\log(1-u)
 \tag{1.1}
\]

implies

\[
 H_P''(a)=-J_{n,k}(a,c)-\mathcal P_P''(a),\qquad
 J_{n,k}(a,c)=\frac{n-k}{a(1-a)}+
 \frac{k}{(a+c)(1-a-c)}.
 \tag{1.2}
\]

Thus P2 is precisely `H_P''<=0`, not the stronger and generally false assertion `Pcal_P''>=0`.

For orientation, the exact complete-atom identity is

\[
 H_P''=-\sum_yq_a''(y)\log q_a(y)
             -\sum_y\frac{q_a'(y)^2}{q_a(y)}.
 \tag{1.3}
\]

No output weights will be held fixed in this proof. We prove an actual bound on (1.3), by comparing full entropies.

The channel output is the DPP with kernel `aI+cP`: for every coordinate set `B`,

\[
 \Pr(B\subseteq Y)
 =\mathbb E\prod_{i\in B}(a+cX_i)
 =\sum_{A\subseteq B}a^{|B|-|A|}c^{|A|}\det P_A
 =\det(aI_B+cP_B).
 \tag{1.4}
\]

Inclusion probabilities determine a finite binary law by inclusion--exclusion.

## 2. Main theorem

**Theorem 2.1 (rank one and co-rank one).** Let `n>=2`, `1/2<=c<1`, and let `P` be a rank-one or co-rank-one projection on `C^n`. Define

\[
 \kappa_n=\frac{4n(n-1)}{n+2}.
\]

Then, for every `0<a<1-c`,

\[
 \boxed{H_P''(a)\le-\kappa_n,}
 \tag{2.1}
\]

and consequently

\[
 \boxed{\mathcal P_P''(a)\ge-J_{n,k}(a,c)+\kappa_n.}
 \tag{2.2}
\]

For `a_0,a_1` in the closed interval `[0,1-c]` and `0<=t<=1`, set `a_t=(1-t)a_0+ta_1`. Then

\[
 H_P(a_t)\ge(1-t)H_P(a_0)+tH_P(a_1)
 +\frac{\kappa_n}{2}t(1-t)(a_1-a_0)^2.
 \tag{2.3}
\]

There is no positivity assumption on individual singleton weights or minors. The theorem also holds for every `0<c<1` when `n=2`. For `n=1` the input is deterministic; the appropriate one-coordinate bound is `H_P''<=-4`.

The proof occupies Sections 3--6. Its only non-elementary input is the established Shepp--Olkin theorem stated precisely in Section 5. That theorem is used only for an exactly identified count-entropy term; the other term in the complete configuration entropy is retained and bounded explicitly.

## 3. Rank-one minors and pair smoothing

Let `P=vv*`, `||v||=1`, and put

\[
 w_i=|v_i|^2,\qquad w_i\ge0,\qquad\sum_iw_i=1.
\]

The input is a random singleton of weight vector `w`. Conversely, every such vector occurs as the singleton weights of a rank-one projection. Denote the full output entropy by `H_w(a)` and put

\[
 d=\delta-a,\qquad x=a(\delta-a),\qquad
 w_T=\sum_{i\in T}w_i.
\]

For every complete output atom `T`, direct summation over the location of the input singleton gives

\[
 q_w(T)
 =a^{|T|}(1-a)^{n-|T|}
   \frac{x+cw_T}{a(1-a)}.
 \tag{3.1}
\]

Indeed, relative to the all-`Bernoulli(a)` product law, a singleton in `T` has likelihood ratio `(a+c)/a`, whereas one outside `T` has ratio `d/(1-a)`. Their weighted sum is `(ad+cw_T)/(a(1-a))`.

Fix different coordinates `i,j`. Keep all other weights fixed, and keep

\[
 s=w_i+w_j
\]

fixed. A **pair smoothing** replaces `(w_i,w_j)` by another nonnegative pair with the same sum and a no larger absolute difference. Put

\[
 v_0=\frac c2|w_i-w_j|,\qquad
 v_1=\frac c2|\widetilde w_i-\widetilde w_j|,
 \qquad 0\le v_1\le v_0.
\]

For `R` contained in the remaining `n-2` coordinates, let

\[
 B_R(a)=a^{|R|}(1-a)^{n-2-|R|},\qquad
 u_R(a)=x+c(w_R+s/2).
\]

The only atom pairs that change are

\[
 q_w(R\cup\{i\})=B_R(u_R+v),\qquad
 q_w(R\cup\{j\})=B_R(u_R-v),
 \tag{3.2}
\]

where the sign of `v` only interchanges the two atoms. Atoms containing both or neither coordinate are unchanged. On the open parameter interval,

\[
 u_R-v_0=x+c(w_R+\min(w_i,w_j))>0.
\]

Define

\[
 \psi_v(u)=(u+v)\log(u+v)+(u-v)\log(u-v)-2u\log u.
\]

The terms involving `log B_R` cancel in the difference of the two full entropies, giving the exact formula

\[
 H_{\widetilde w}(a)-H_w(a)
 =\sum_R B_R(a)
       \big[\psi_{v_0}(u_R(a))-\psi_{v_1}(u_R(a))\big].
 \tag{3.3}
\]

This identity is a sum over the entire output law, not a conditional entropy with frozen output weights.

## 4. A new sign estimate: the smoothing loss is convex

**Lemma 4.1 (positive Laplace representation).** If `u>|v|`, then

\[
 \psi_v(u)=\int_0^\infty
       \frac{2(\cosh(vt)-1)}{t^2}e^{-ut}\,dt.
 \tag{4.1}
\]

**Proof.** The integrand is bounded at zero and integrable at infinity. Twice differentiating the right side in `v`, locally within `|v|<u`, gives

\[
 \int_0^\infty2\cosh(vt)e^{-ut}\,dt
 =\frac1{u-v}+\frac1{u+v},
\]

which is also `partial_v^2 psi_v(u)`. Both sides and their first `v` derivatives vanish at `v=0`. This proves (4.1). The indicated differentiations are dominated on any compact subinterval of `|v|<u` by an exponential with a strictly positive decay rate. ∎

Summing (4.1) in (3.3), and using nonnegativity to interchange sum and integral, gives

\[
 H_{\widetilde w}(a)-H_w(a)
 =\int_0^\infty
  \frac{2[\cosh(v_0t)-\cosh(v_1t)]}{t^2}\,G_t(a)\,dt,
 \tag{4.2}
\]

where

\[
 G_t(a)=
 e^{-t[a(\delta-a)+cs/2]}
 \prod_{\ell\ne i,j}(1-a+ae^{-tcw_\ell}).
 \tag{4.3}
\]

Every factor outside `G_t` in (4.2) is nonnegative and independent of `a`. The integral is finite: near infinity it is bounded by a constant times `e^{-a(delta-a)t}/t^2`, and near zero it is bounded.

**Lemma 4.2 (log-convex integrand).** For `c>=1/2`, every function `G_t`, `t>0`, is log-convex on `(0,delta)`.

**Proof.** Put `r_ell=1-e^{-tcw_ell}`. Differentiation of the logarithm of (4.3) gives exactly

\[
 (\log G_t)''
 =2t-\sum_{\ell\ne i,j}\frac{r_\ell^2}{(1-ar_\ell)^2}.
 \tag{4.4}
\]

For `u>=0`, `(1-e^{-u})^2<=u`: when `u<=1`, use `1-e^{-u}<=u`, and when `u>=1`, use `1-e^{-u}<=1`. Moreover `1-ar_ell>=1-a>=c`. Therefore

\[
 \sum_{\ell\ne i,j}\frac{r_\ell^2}{(1-ar_\ell)^2}
 \le\frac{tc\sum_{\ell\ne i,j}w_\ell}{c^2}
 =\frac{t(1-s)}c\le\frac tc.
\]

Thus `(log G_t)''>=t(2-1/c)>=0`. When `n=2`, the sum in (4.4) is empty, so the conclusion holds for all `0<c<1`. ∎

A positive log-convex function is convex, since

\[
 G_t''=G_t\big((\log G_t)''+((\log G_t)')^2\big)\ge0.
\]

Apply the defining convexity inequality pointwise under the nonnegative integral (4.2). No interchange of two `a` derivatives with the improper integral is needed. This proves:

**Proposition 4.3 (convex smoothing deficit).** For `c>=1/2`, each pair smoothing satisfies

\[
 a\longmapsto H_{\widetilde w}(a)-H_w(a)
 \quad\hbox{is convex on }(0,\delta).
 \tag{4.5}
\]

Since the entropies are smooth there,

\[
 H_w''(a)\le H_{\widetilde w}''(a).
 \tag{4.6}
\]

This is the bound supplied by the rank-one projection-minor structure. The affine dependence on `w_R`, and the fact that the imbalance `v` is independent of `a` and of `R`, produce the nonnegative product integral (4.2). Neither fact holds for a general fixed-cardinality input law.

### Reaching uniform weights in finitely many steps

Let `r=1/n`. Unless `w` is uniform, select one weight `w_i>r` and one `w_j<r`, and transfer

\[
 \varepsilon=\min(w_i-r,r-w_j)
\]

from `i` to `j`. This is a pair smoothing, because `2 epsilon<=w_i-w_j`; at least one of the two new weights equals `r`. Never change coordinates already fixed at `r`. At most `n-1` operations reach

\[
 w_*=(1/n,\ldots,1/n).
\]

Adding the convex losses gives

\[
 H_{w_*}-H_w\text{ is convex},\qquad
 H_w''\le H_{w_*}''.
 \tag{4.7}
\]

This argument includes vectors with zero weights without approximation.

## 5. The uniform singleton law: keeping all configuration entropy

Under `w_*`, the complete output law is invariant under every coordinate permutation. Given `M=|Y|`, it is uniform on the `binom(n,M)` configurations of that size. Consequently the **exact full-entropy decomposition** is

\[
 H_{w_*}(a)=H(M(a))+
      \mathbb E\log\binom n{M(a)}.
 \tag{5.1}
\]

Conditional on any location of the input singleton, the count has the same law. It is therefore the sum of independent Bernoulli variables with probabilities

\[
 (a+c,a,\ldots,a).
 \tag{5.2}
\]

We use the following established theorem, with its hypotheses stated here.

**Shepp--Olkin theorem [HJ17, Theorem 1.2].** If `Z_1,...,Z_n` are independent Bernoulli variables of parameters `p_1,...,p_n`, then the Shannon entropy of `sum_i Z_i` is a jointly concave function of `(p_1,...,p_n)` on `[0,1]^n`.

This is a proved external theorem, not an assumption about DPP configuration entropy. Applying it along the affine path (5.2) yields

\[
 \frac{d^2}{da^2}H(M(a))\le0.
 \tag{5.3}
\]

We must still control the second term in (5.1). Let

\[
 g(m)=\log\binom nm,\qquad 0\le m\le n.
\]

For independent Bernoulli variables whose probabilities all have derivative one, multilinearity in their individual probabilities gives

\[
 \frac{d^2}{da^2}\mathbb E g(M)
 =2\sum_{i<j}\mathbb E\,\Delta^2g(M_{-ij}),
 \tag{5.4}
\]

where `M_{-ij}` is the sum omitting `i,j`, and `Delta^2g(m)=g(m+2)-2g(m+1)+g(m)`. To verify (5.4), first condition on all variables except `Z_i`; the derivative in `p_i` is `E Delta g(M_{-i})`. Differentiate in `p_j`. There is no second derivative in a repeated coordinate because the expectation is affine in each `p_i`.

For `0<=m<=n-2`,

\[
 \begin{aligned}
 \Delta^2g(m)
 &=\log\frac{(n-m-1)(m+1)}{(n-m)(m+2)}\\
 &=\log\left(1-\frac1{n-m}\right)
   +\log\left(1-\frac1{m+2}\right)\\
 &\le-\frac1{n-m}-\frac1{m+2}
 \le-\frac4{n+2}.
 \end{aligned}
 \tag{5.5}
\]

The last inequality follows from `(n-m)+(m+2)=n+2`. Combining (5.4)--(5.5),

\[
 \frac{d^2}{da^2}\mathbb E\log\binom nM
 \le-\frac{4n(n-1)}{n+2}=-\kappa_n.
 \tag{5.6}
\]

Equations (5.1), (5.3), and (5.6) prove `H_{w_*}''<=-kappa_n`. This is a bound on the full entropy, not an identification of it with `H(M)`.

Together with (4.7), this proves Theorem 2.1 for rank-one projections in the interior.

## 6. Complements, direct sums, and endpoints

### 6.1 Co-rank one

The complement of a projection DPP with kernel `P` is the projection DPP with kernel `I-P`. This follows from inclusion--exclusion:

\[
 \Pr(B\subseteq X^c)=\mathbb E\prod_{i\in B}(1-X_i)=\det(I-P)_B.
\]

Set `Z=1-X` and `W=1-Y`. Given `Z_i=0`, `Pr(W_i=1)=delta-a`; given `Z_i=1`, this probability is `delta-a+c`. Thus complementation replaces `a` by `delta-a`, preserves `c`, and preserves full configuration entropy. In particular,

\[
 H_P(a)=H_{I-P}(\delta-a),\qquad
 H_P''(a)=H_{I-P}''(\delta-a).
\]

The rank-one result proves the co-rank-one result, with the same constant.

### 6.2 Coordinate direct sums

If `P` is block diagonal in the coordinate basis, its DPP factors into independent block DPPs: their inclusion probabilities factor, hence so do the complete laws. The channel also acts independently on the blocks. Therefore full entropies, their second derivatives, and the constants `J_{n,k}` add.

It follows that P2 holds for a coordinate direct sum of rank-one, co-rank-one, zero, and identity projection blocks when `c>=1/2`. Each block of size `m>=2` and rank one or co-rank one contributes the margin `kappa_m`. Each deterministic coordinate contributes at least `4`, since `b''(u)=-1/[u(1-u)]<=-4`. A one-dimensional projection is deterministic and is handled this way.

This is a coordinate-block statement, not a claim of invariance under arbitrary unitary conjugation.

### 6.3 Boundary continuity and strong concavity

For fixed finite input law, each complete output atom is a polynomial in `a`. The function `-x log x`, with value zero at zero, is continuous. Therefore `H_P` extends continuously to `a=0,delta`, even when some atoms vanish there.

For the rank-one and co-rank-one cases with `n>=2`, (2.1) says that

\[
 a\longmapsto H_P(a)+\frac{\kappa_n}{2}a^2
\]

is concave in the interior. Take limits of its concavity inequality to extend it to the closed interval. Rearranging gives (2.3). Equation (1.2) gives (2.2) only in the interior, where its displayed denominators are defined; endpoint P2 is not asserted as a finite derivative formula.

This completes the proof of Theorem 2.1. ∎

## 7. Exact relation to the stationary S-sine target

For a fixed interval `E_rho` of measure `0<rho<1`, the target is concavity of the entropy rate of the stationary DPP with symbol

\[
 f_a(\theta)=a+c1_{E_\rho}(\theta).
\]

Its finite Toeplitz compression `Q_N=T_N(1_{E_rho})` is not a projection. The bridge in `bridge.md` uses genuine cyclic Fourier projections of rank `k_N=rho N+O(1)` and proves an endpoint-uniform `o(N)` comparison of their full output entropies with the true block entropies.

Theorem 2.1 covers cyclic ranks one and `N-1`, but not ranks `rho N+O(1)` for fixed `0<rho<1`. Nor is a dense cyclic Fourier projection a coordinate direct sum of the covered blocks. The quantitative finite-dimensional theorem in `high_fidelity.md` also loses its useful sign when `N` tends to infinity at a fixed `c<1`.

Accordingly, the general projection P2 inequality, the fixed-density cyclic curvature bound, and the original S-sine concavity theorem remain unresolved in this deliverable. The new rank-one/co-rank-one theorem is a proved, unbounded-dimensional subfamily within the previously requested high-contrast regime; it is not advertised as the main theorem.

## 8. Hypothesis and dependency audit

- Projection: exact, finite, Hermitian; no Toeplitz compression is silently treated as idempotent.
- Rank-one parameters: every probability vector `w`, including zero entries; complex phases in `v` do not change its singleton minors.
- Channel range: `1/2<=c<1` and the entire closed interval `0<=a<=1-c`; derivatives only in the open interval.
- Constants: `kappa_n=4n(n-1)/(n+2)`, no hidden dependence on the smallest nonzero minor or on an `a`-compact set.
- Dimension: arbitrary finite `n`; not fixed before choosing a weight vector.
- Output weights: retained in (3.3), including the factors `B_R(a)` and the `a`-dependent `u_R(a)`.
- Counts: used only in the exact exchangeable decomposition (5.1); the conditional-configuration entropy term is explicitly differentiated.
- Imported established result: [HJ17, Theorem 1.2], with its exact scope stated above. The new Laplace/balancing estimate and all constants are proved here.
- No numerical experiment is used in the proof.

## References

[HJ17] Erwan Hillion and Oliver Johnson, **A proof of the Shepp--Olkin entropy concavity conjecture**, *Bernoulli* **23**(4B), 3638--3649 (2017), Theorem 1.2. DOI: `10.3150/16-BEJ860`. Author manuscript: <https://arxiv.org/abs/1503.01570>; theorem checked against PDF page 2. The imported theorem is stated above; no external manuscript is redistributed.
