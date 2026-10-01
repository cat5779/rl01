**PROVED — the sampler criterion below, and consequently the frozen universal prescribed-\(W\)-source DPP statement.** The argument verifies the proposed seed rather than assuming it.

**Novelty is UNKNOWN.** The Brownian mechanism has direct prior art, but no inspected theorem was verified to imply the whole result without the infinite-system argument below. The universal replacement of the \(W\)-source by a regular \(\Gamma\)-source is **DISPROVED**. GitHub publication is **INCOMPLETE**; the files and fallback archive are linked below.

## 1. Exact sampler criterion

For a finite binary law \(\nu\) on \(F\), let \(\nu^h\) be its tilt by \(\exp(\sum_{z\in F}h_z\eta_z)\), normalized to total mass one. Positive multiplicative fields allow **every \(h\in\mathbb R^F\)**, not just \(h\ge0\).

**Theorem.** Let \(\mu\) be a \(\Gamma\)-invariant binary law on countable \(W\). Suppose there is a deterministic \(\Gamma\)-invariant partition into components \(C\) such that the restrictions \(\eta|_C\) are jointly independent. Suppose deterministic finite windows satisfy
\[
x\in E_n(x)\subseteq E_{n+1}(x)\subseteq C(x),\qquad
\bigcup_nE_n(x)=C(x),\qquad E_n(gx)=gE_n(x).
\]
Assume that one \(L<\infty\) satisfies
\[
\boxed{\forall x,n,\ \forall h\in\mathbb R^{E_n(x)},\qquad
\sum_{z\in E_n(x)}
\left|\operatorname{Cov}_{(\mu_{E_n(x)})^h}(\eta_x,\eta_z)\right|\le L.} \tag{1}
\]
Then \(\mu\) is a **total Borel, exactly \(\Gamma\)-equivariant factor of \(\operatorname{Uniform}[0,1]^W\)**.

Here \(\mu_F\) means the **actual unconditional marginal**. Arbitrary boundary-condition Gibbs laws are not substitutes. Only the root row in each specified window is required; all finite-set row bounds suffice. No \(L<1\) assumption or existence of general infinite-field tilts is required.

### Proof: an all-input strong solution

For every \(t\ge0\) and \(y\in\mathbb R^W\), define
\[
b^n_{t,x}(y)=\mathbb E_{(\mu_{E_n(x)})^{y|_{E_n(x)}-t\mathbf1/2}}\eta_x,
\qquad b_{t,x}(y)=\limsup_n b^n_{t,x}(y).
\]
The finite functions are continuous and their field derivatives are covariances. Integrating derivatives along a segment and using (1), then taking limsup, gives
\[
\sup_x|b_{t,x}(y)-b_{t,x}(y')|
\le L\|y-y'\|_\infty
\quad\text{if }y-y'\in\ell^\infty(W). \tag{2}
\]
The drift \(b\) is jointly Borel, \([0,1]\)-valued, and exactly equivariant. No pointwise convergence at all deterministic fields has been asserted.

For **every** \(w\in C_0([0,\infty),\mathbb R)^W\), define
\[
Z^0=w,\qquad Z^{k+1}_t(x)=w_t(x)+\int_0^t b_{s,x}(Z^k_s)\,ds.
\]
Bounded Borel integrands make these Lebesgue integrals exist on all inputs. The iterates have continuous coordinate paths, Borel dependence on \(w\), and are causal. Moreover,
\[
\sup_x\sup_{s\le t}|Z^{k+1}_s(x)-Z^k_s(x)|
\le\frac{L^kt^{k+1}}{(k+1)!}.
\]
Thus they converge uniformly in their differences on bounded times to a solution \(\Psi(w)\) of
\[
Z_t(x)=w_t(x)+\int_0^t b_{s,x}(Z_s)\,ds. \tag{3}
\]
**The noise need not belong to \(\ell^\infty\):** only differences of iterates do. Any two solutions have differences bounded by \(2t\), so Grönwall gives uniqueness. Borel parameter integration, limits, and rational-time evaluations prove that \(\Psi\) is a total Borel causal map into the product path space. Its construction is exactly equivariant.

### Proof: full-past identification and innovations

On an auxiliary space sample \(\eta\sim\mu\) independently of iid Brownian \(B\), and put \(X_t=t\eta+B_t\). Finite Gaussian Bayes gives, for each fixed \(t>0\),
\[
b^n_{t,x}(X_t)=\mathbb E[\eta_x\mid X_t(z):z\in E_n(x)].
\]
Upward martingale convergence gives the posterior on \(C(x)\). Independence of the pairs \((\eta|_C,B|_C)\) lets us add all other components without changing it. Hence
\[
b_{t,x}(X_t)=\mathbb E[\eta_x\mid X_t(z):z\in W]
\quad\text{a.s. for each fixed }t>0. \tag{4}
\]
Joint measurability and Fubini handle the time-dependent exceptional sets.

For fixed \(t\), the countable Brownian bridge field
\[
R_s(z)=B_s(z)-(s/t)B_t(z),\qquad s\le t,
\]
is independent of \((\eta,B_t)\), by Gaussian independence and a monotone-class argument. Since \(X_s=(s/t)X_t+R_s\), (4) also equals the posterior given the **entire raw observation past**
\[
\mathcal F_t^0=\sigma(X_s(z):s\le t,z\in W).
\]
No infinite-product Girsanov density is used.

Define
\[
\beta_t(x)=X_t(x)-\int_0^t b_{s,x}(X_s)\,ds.
\]
The drift is progressive. Brownian increment independence, the posterior identity, tower property, and Fubini show that each \(\beta(x)\) is a continuous square-integrable raw-filtration martingale. Since the correction is finite variation,
\[
[\beta(x),\beta(y)]_t=\mathbf1_{x=y}t.
\]
Use **one common usual augmentation**
\[
\mathcal F_t=\bigcap_{u>t}(\mathcal F_u^0\vee\mathcal N).
\]
The martingale property survives by letting \(r\downarrow s\) in
\[
\mathbb E[\beta_t\mid\mathcal F_r^0\vee\mathcal N]=\beta_r,
\]
using reverse conditional-expectation convergence and \(L^1\) continuity. Every finite vector of \(\beta\) is standard vector Brownian motion by the martingale/bracket characterization. Therefore \(\beta\) has product Wiener law on the countable product path space.

This supplies the countable-field version of the classical innovation ingredient. Crucially, Brownian innovations alone are not a strong inverse: here (3) and pathwise uniqueness give **\(X=\Psi(\beta)\)**. :chatgpt-content-reference{index="0"}

Finally, on every path input define
\[
F(w)(x)=\liminf_n\mathbf1\{\Psi(w)_n(x)>n/2\}.
\]
Under \(X\), each indicator errs about \(\eta_x\) with probability at most \(e^{-n/8}\). Borel–Cantelli and countability give \(F(\beta)=\eta\) almost surely. \(F\) remains total Borel and exactly equivariant.

For the uniform source, split one uniform’s binary digits into independent streams, transform them into normals, and construct Brownian motion by dyadic Gaussian bridges on successive unit intervals. This is a Borel map \(\kappa:[0,1]\to C_0\) with Wiener pushforward; on its Borel null set of nonconvergence, assign the zero path. Apply **the identical \(\kappa\) at every site**. Then
\[
\Phi(u)=F((\kappa(u_x))_{x\in W})
\]
proves the criterion. The file includes the series-convergence estimate. ∎

## 2. Every DPP hypothesis is verified, including eigenvalues 0 and 1

Let \(K\) be a finite Hermitian positive contraction and \(D=\operatorname{diag}(e^{h_i})>0\). Put
\[
M=I-K+K^{1/2}DK^{1/2},\quad R=D^{1/2}K^{1/2},\quad K_D=RM^{-1}R^*.
\]
Then
\[
M\ge\min(1,\min_iD_{ii})I>0,\qquad M\ge R^*R,
\]
so \(0\le K_D\le I\). For \(Z=\operatorname{diag}(z_i)\), the generating polynomial is
\[
g_K(z)=\det(I+(Z-I)K).
\]
Sylvester’s identity gives
\[
\frac{g_K(DZ)}{g_K(D)}
=\frac{\det(M+R^*(Z-I)R)}{\det M}
=\det(I+(Z-I)K_D).
\]
Thus the tilted law is exactly \(\mathbf P^{K_D}\). Neither \(K^{-1}\) nor \((I-K)^{-1}\) appears: **complex entries, singular kernels, projections, and deterministic bits are included**.

For \(H=K_D\) and \(p=H_{xx}\), diagonal covariance is \(p(1-p)\), and off-diagonal covariance is \(-|H_{xz}|^2\). Therefore
\[
\boxed{
\sum_z|\operatorname{Cov}(\eta_x,\eta_z)|
=p(1-p)+(H^2)_{xx}-p^2
\le2p(1-p)\le\tfrac12.} \tag{5}
\]
Equality is attained by the equal-weight two-point rank-one projection. Every actual finite marginal of \(\mathbf P^Q\) has the positive-contraction kernel \(Q_F\), so (5) holds for **every finite marginal and every positive field**.

For the remaining hypotheses, join \(x\ne y\) in \(D_n\) when \(|Q(x,y)|\ge1/n\), and take radius-\(n\) balls \(E_n(x)\). The estimate
\[
\sum_y|Q(x,y)|^2=(Q^2)_{xx}\le Q_{xx}\le1
\]
gives degree at most \(n^2\). The windows are finite, nested, equivariant, and exhaust precisely the nonzero-kernel components.

\(Q\) is block diagonal over those components. For disjoint finite \(A,B\),
\[
\mathbb P(A\subseteq\eta,\ B\cap\eta=\varnothing)
=\sum_{T\subseteq B}(-1)^{|T|}\det Q_{A\cup T}.
\]
Block determinants factor this expression over components. Finite-pattern probabilities therefore factor; the monotone-class theorem gives **joint independence of the entire component restrictions**.

All criterion hypotheses now hold with \(L=1/2\). Consequently:

> **PROVED.** Every bounded Hermitian positive contraction on \(\ell^2(W)\) commuting with a countable \(\Gamma\)-action defines a DPP that is a total Borel \(\Gamma\)-factor of iid Uniform\([0,1]\) labels indexed by **\(W\)**.

The limsup drift genuinely removes the need for pointwise infinite-volume tilt convergence. The remaining necessary convergence is along the true observation law, and that was proved by upward martingale convergence.

## 3. Exact prior-art comparison

The files contain sixteen sources, with URLs, versions, and theorem-level comparisons. Here are the decisive statements; “stronger” means stronger within the source’s narrower domain.

| Primary source and version | Exact statement inspected | Relationship |
|---|---|---|
| **Nam–Sly–Zhang**, [arXiv:2012.09484v2](https://arxiv.org/pdf/2012.09484v2), 22 Jan 2022 | §2.2/Lemma 2.1, p.5; Propositions 2.2–2.3; Theorem 1, p.2. Free Ising on sufficiently high-degree regular trees, \(\tanh\beta\le c/\sqrt{d-1}\). | **Same observation/strong-SDE method.** Their infinite-radius and root-change estimates are model-specific. A finite coordinatewise derivative bound is not our uniform row bound. :chatgpt-content-reference{index="1"} |
| **Fujisaki–Kallianpur–Kunita**, 1972 | §2, Lemmas 2.1–2.2, pp.21–22: finite-vector observations, square-integrable signals, and future-noise independence. | **Same innovation ingredient**; Brownianity alone does not establish the strong inverse. :chatgpt-content-reference{index="2"} |
| **El Alaoui–Montanari**, v2, 9 Sep 2021; **Chen–Eldan**, v2, 6 Jun 2022 | Respectively §3/Theorem 2, pp.6–7; §2.4.2/Facts 13–14, pp.15–16, Proposition 16, p.17. Finite-dimensional Gaussian localization. | **Same finite posterior machinery**, not a countable-site equivariant factor theorem. :chatgpt-content-reference{index="3"} |
| **Montanari**, v2, 2 Sep 2025; **Shi–Tian–Zhang**, v2, 17 Jan 2026 | Respectively §1.3/Proposition 1.1 and §4.1; §3/Theorem 2, p.6. Finite-dimensional observation/localization representations. | Further **same-method** accounts; no universal infinite DPP assertion. :chatgpt-content-reference{index="4"} |
| **Borcea–Brändén–Liggett**, v2, 27 Jul 2008 | Proposition 3.5, p.18; Theorems 4.2, p.21, and 4.9, p.24: DPPs are strongly Rayleigh, homogenization, negative dependence under fields. | **Same finite ingredients.** They yield the row bound for finite strongly Rayleigh laws, but not an infinite factor theorem. :chatgpt-content-reference{index="5"} |
| **Anari–Liu–Oveis Gharan**, v3, 17 Sep 2020; **Anari–Oveis Gharan–Rezaei**, COLT 2016 | Definition 1.2/Theorem 1.3, pp.1–2: finite spectral independence/Glauber gap. Separately Theorem 2, PDF p.3: homogeneous strongly Rayleigh swap-chain mixing. | **Nearby finite samplers.** Different influence hypotheses; no automatic infinite equivariant passage. :chatgpt-content-reference{index="6"} |
| **Lyons–Steif**, v5, 23 Jan 2003; **Broman**, 2005 | Theorem 3.1, p.15: stationary \(\mathbb Z^d\) DPPs are Bernoulli-isomorphic. Theorem 1.3, PDF p.3: degree-one trigonometric DPPs are two-block factors. | **Stronger restricted DPP conclusions**, including projection symbols in the former. :chatgpt-content-reference{index="7"} |
| **Lyons–Thom**, v2, 19 May 2014; **Spinka**, v2, 19 Jan 2020 | Theorem 7.3/Corollary 7.4, p.24: sofic approximation/amenable isomorphism. Theorem 1.1, p.2: finitely dependent processes on transitive amenable graphs are finitary. | Approximation is **not itself** a factor construction; isomorphism/finitary results are stronger in narrower domains. :chatgpt-content-reference{index="8"} |
| **Angel–Ray–Spinka**, 2021/2024; **Timár**, v2, 16 Dec 2025 | Theorems 1.4/4.1, §4: WUSF on connected transient random rooted graphs; no unimodularity assumption in that theorem. Theorems 4/9 and Corollary 5, pp.5–6: invariantly amenable USF, including finitary coding. | Genuine forest-factor results, but **wired or amenable**, not general nonamenable FUSF. :chatgpt-content-reference{index="9"} |

The strongly Rayleigh row bound follows explicitly: homogenize to \(2n\) coordinates with deterministic total \(n\). After tilting original coordinates, off-diagonal covariances remain nonpositive and each full covariance row sums to zero. Restricting to original coordinates bounds its absolute row sum by \(2\operatorname{Var}(\eta_i)\le1/2\). The infinite component/exhaustion requirements remain separate. :chatgpt-content-reference{index="10"}

This does not imply single-bit Glauber mixing: the two-point projection is supported on \(\{(1,0),(0,1)\}\), so every one-bit heat-bath update is frozen despite (5). Swap chains and the Brownian construction are different mechanisms.

**No inspected theorem was verified to imply the whole prescribed-\(W\) result without the countable-field argument above. Novelty is UNKNOWN—not certified new, and not certified open.**

## 4. Q7.7 and the exact sources

Lyons–Thom allow Bernoulli sources \(A^W\) for countable \(\Gamma\)-sets (p.3). Their developed operators include \(R(\Gamma)\) and \(R(\Gamma,S)=M_S(R(\Gamma))\); Q7.7 is on p.25. The theorem supplies an allowed source, answers the explicitly developed Q7.7 setting, and proves the precise prescribed-\(W\) formulation. No stronger regular-source quantifier is inferred from uncertain author intent. :chatgpt-content-reference{index="11"}

For \(W=\Gamma\times S\), Cayley-diagram arcs identify by \((g,s)\mapsto(g,gs)\); this basis bijection preserves actions, operators, and inclusion determinants. Output grouping gives \((\{0,1\}^S)^\Gamma\). To obtain the regular \(\Gamma\)-source, enumerate \(S=\{s_1,\ldots,s_m\}\) and split binary digits:
\[
V_{g,s_i}=\sum_{k\ge1}2^{-k}\epsilon_{m(k-1)+i}(U_g).
\]
The \(V\)’s are iid uniforms on \(\Gamma\times S\), and the formula commutes with left translations. No source identification is being assumed silently.

**DISPROVED: universal replacement by regular \(\Gamma\)-iid for nonfree actions.** Take \(\Gamma=F_2\), \(H=\langle a\rangle\), \(W=\Gamma/H\), and \(Q=pI\), \(0<p<1\). The target is iid Bernoulli\((p)\), trivially a \(W\)-factor. A regular-source factor would make its bit at \(H\) a nonconstant \(H\)-invariant function. But the restricted regular Bernoulli action is ergodic: approximate an invariant event by a cylinder on finite \(K\), choose \(h\in H\) with \(hK\cap K=\varnothing\), use independence, and let the approximation error vanish to obtain \(\mathbb P(A)=\mathbb P(A)^2\). This contradicts \(p\in(0,1)\).

## 5. Free forests: derive the edge action and vertex source

On a fixed countable locally finite simple graph, choose reference orientations and define
\[
\mathcal C=\overline{\operatorname{span}\{\text{finite signed cycles}\}},
\qquad \mathcal S=\overline{dC_c(V)}.
\]
The respective kernels are
\[
\mathrm{FUSF}=\mathbf P^{P_{\mathcal C^\perp}},\qquad
\mathrm{WUSF}=\mathbf P^{P_{\mathcal S}}.
\]
These are stated in Lyons–Thom §2, p.6, and follow from strong limits of free projections \(I_{E_n}-P_{\mathcal C_n}\) and wired star projections. :chatgpt-content-reference{index="12"}

Automorphisms act on reference-oriented coordinates by **signed permutations**. The free projection need not commute with the unsigned action. Nevertheless, sign conjugation preserves principal determinants and absolute kernel entries. Thus its unoriented law and threshold windows satisfy the **criterion directly**. The proof is exactly equivariant under every preserving permutation, including the full, possibly uncountable \(\operatorname{Aut}(G)\).

Vertex iid supplies edge iid as follows. Split each vertex label into an independent continuous key and an iid uniform stack. Assign each edge to its smaller-key endpoint and use the stack slot given by the other endpoint’s rank among its neighbors’ keys. Conditional on the keys, different edges use distinct independent slots. On the invariant null event of any key tie, assign all edge labels zero. This is total Borel and \(\operatorname{Aut}(G)\)-equivariant.

Consequently, the proof gives **vertex-iid, full-\(\operatorname{Aut}(G)\)-equivariant FUSF on every fixed connected countable locally finite simple graph**. It does not assert joint Borel dependence on a varying random graph. The file also checks the nonamenable cyclic example \(T_4\square C_3\) and proves its free and wired laws differ.

## Remaining obligation and files

For the frozen fixed-\(Q\) statement, **no analytic or source hypothesis is left open in this proof**. Exact literature priority remains unresolved. Finitary coding, Bernoulli isomorphism, computational rates, and joint random-graph measurability are separate, unasserted conclusions.

GitHub discovery found the connector uninstalled; `gh` was unavailable; `git ls-remote` failed with `Could not resolve host: github.com`. No push, PR creation, merge, or modification of another worker’s files occurred. The archive contains only the two requested repository-relative files.

:chatgpt-content-reference{index="14"}[RESULT.md](sandbox:/mnt/data/q77r05g6/research/q77r05/g6/RESULT.md) · :chatgpt-content-reference{index="15"}[REFERENCES.md](sandbox:/mnt/data/q77r05g6/research/q77r05/g6/REFERENCES.md) · :chatgpt-content-reference{index="16"}[q77r05g6-001.zip](sandbox:/mnt/data/q77r05g6-001.zip)