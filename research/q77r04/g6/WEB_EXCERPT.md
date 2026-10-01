**PROVED — Conditional scope theorem:** The candidate statement would answer Lyons–Thom Question 7.7 affirmatively in the regular and finite-mark operator setting explicitly developed in their paper. It would also imply that the free uniform spanning forest on every locally finite Cayley graph is a factor of the stated **Γ-indexed Uniform[0,1] source**.

**The candidate itself remains UNRESOLVED.** The arguments below establish implications from it, not its validity. A different assertion involving arbitrary nonfree actions and a prescribed regular Γ-indexed source is **DISPROVED** below.

## 1. The exact Q7.7 scope

Write **C** for the candidate in the question.

Lyons–Thom define Bernoulli shifts using product measures on \(A^\Gamma\), and more generally \(A^W\) for countable Γ-sets. Their explicit motivating DPP question concerns \(2^\Gamma\). Section 3 treats \(R(\Gamma)\) and the Cayley-diagram algebra \(R(\Gamma,S)=M_S(R(\Gamma))\). Section 7 introduces the joining metric for quasi-transitive \(W\). Theorem 7.3 gives finitely dependent approximations under soficity; Corollary 7.4 gives Bernoulli isomorphism under amenability. Question 7.6 explicitly invokes quasi-transitive \(W\). Question 7.7 says:

> Are determinantal probability measures associated to equivariant positive contractions factors of Bernoulli shifts?

The subsequent implication from Questions 7.5–7.6 invokes Theorem 7.3 and is stated for sofic groups. These passages do not explicitly prescribe a regular Γ-indexed source for every arbitrary target Γ-set. :chatgpt-content-reference{index="0"}

### Theorem 1: C implies the affirmative answer in the developed setting

**Proof.** For a singleton mark set, the candidate’s operators are exactly the positive contractions commuting with the left regular representation—that is, the positive contractions in \(R(\Gamma)\).

For a finite symmetric generating set \(D\), the directed Cayley-diagram edges have the equivariant identification
\[
\theta_D:\Gamma\times D\longrightarrow E_{\mathrm{dir}},
\qquad
(g,d)\longmapsto(g,gd).
\]
Both directions of each unoriented graph edge occur here.

Transporting the standard basis through \(\theta_D\) gives a unitary \(U\). An operator \(Q\) on diagram edges becomes \(U^*QU\) on \(\ell^2(\Gamma\times D)\). Positivity, contractivity, and equivariance are preserved. Moreover,
\[
\mathbf P^Q(F\subseteq X)
=\det[\langle Q\delta_y,\delta_x\rangle]_{x,y\in F}
\]
is unchanged after the corresponding coordinate relabelling. Applying C and then \(\theta_D\) therefore gives the required factor.

The output can equivalently be grouped as
\[
\{0,1\}^{\Gamma\times D}
\cong
(\{0,1\}^{D})^\Gamma.
\]
That grouping is not an additional assumption.

The source conversion also needs checking. Enumerate \(S=\{s_1,\ldots,s_m\}\). If \(\epsilon_n(u)\) are binary digits, define
\[
V_{g,s_i}
=
\sum_{k\ge1}2^{-k}\epsilon_{m(k-1)+i}(U_g).
\]
For iid uniform \(U_g\), disjoint digit subsequences give independent uniform \(V_{g,s_i}\). The construction is identical at every \(g\), hence Γ-equivariant. Interleaving digits supplies an inverse almost surely. Dyadic exceptions and their countable translates form a null set.

Thus
\[
([0,1]^\Gamma,\operatorname{Leb}^\Gamma)
\cong_\Gamma
([0,1]^{\Gamma\times S},
 \operatorname{Leb}^{\Gamma\times S})
\]
modulo null sets. The candidate’s source is already a Bernoulli source permitted by the paper, and it is equivalent to the uniform source on its free finite-mark coordinates.

This proves the implication. Neither Question 7.5 nor the closure assertion in Question 7.6 must first be established. Nor must one prove the stronger Bernoulli-isomorphism conclusion. ∎

**Consequently, it would be incorrect to reject C as answering the developed Q7.7 merely because it does not settle every arbitrary-action interpretation.** The authors’ maximal intended quantification beyond that setting is not explicit enough to certify here.

Arbitrary nonfree target actions, a prescribed same-\(W\) source, all-\(\operatorname{Aut}(G)\) equivariance, random unimodular graphs, infinitely many marks, joint measurability in \(Q\), finitary coding, and Bernoulli isomorphism are separate specifications. They are not all claimed to be open, and they should not be inserted into the original question to manufacture a remainder.

## 2. Finite stabilizers are covered; arbitrary stabilizers create a real source distinction

### Theorem 2: finite-stabilizer extension

Assuming C, let
\[
W=\bigsqcup_{s=1}^m\Gamma/H_s,
\qquad |H_s|<\infty.
\]
Every equivariant positive-contraction DPP on \(W\) is a Γ-factor of regular Γ-indexed iid uniforms.

**Proof.** Define the equivariant isometry
\[
J\delta_{gH_s}
=
|H_s|^{-1/2}\sum_{h\in H_s}\delta_{(gh,s)}
\]
and set \(\widetilde Q=JQJ^*\).

Within each coset fiber, the rows of \(\widetilde Q\) are proportional. Therefore its DPP selects at most one point of each fiber almost surely: every two-point inclusion determinant within a fiber is zero.

For distinct target cosets \(w_1,\ldots,w_k\), one choice of a representative in each fiber has inclusion probability
\[
\det[Q(w_i,w_j)]_{i,j\le k}
\prod_{i=1}^k|H_{s_i}|^{-1}.
\]
There are \(\prod_i|H_{s_i}|\) such choices, with disjoint inclusion events up to null sets. Summing gives exactly the inclusion determinant of \(Q\).

Consequently, mapping occupied fibers to their cosets sends \(\mathbf P^{\widetilde Q}\) to \(\mathbf P^Q\). Compose this map with C. ∎

This argument does **not** identify the nonfree \(W\)-indexed source with the regular Γ-indexed source.

### Proposition 3: the universal arbitrary-action/regular-source extension is false

Take
\[
\Gamma=F_2,\qquad H=\langle a\rangle,\qquad W=\Gamma/H,
\]
and \(Q=pI\), where \(0<p<1\). Its DPP is iid Bernoulli\((p)\) on \(W\).

Suppose it were the image of regular Γ-indexed iid under a Γ-factor \(\Phi\). Then
\[
f(U)=\Phi(U)(H)
\]
would be invariant under \(H\).

But the restriction of the regular Bernoulli action to any infinite subgroup \(H\) is ergodic. For the needed elementary proof, approximate an invariant \(L^2\) function \(f\) by a function \(f_K\) of finitely many coordinates \(K\subset\Gamma\). Choose \(h\in H\) with \(hK\cap K=\varnothing\). Then \(f_K(U)\) and \(f_K(hU)\) are independent. Since \(f(U)=f(hU)\), letting the approximation error tend to zero gives
\[
\operatorname{Var}(f)=0.
\]
This contradicts \(f\sim\operatorname{Bernoulli}(p)\).

Therefore the assertion
\[
\text{“every equivariant DPP on every Γ-set is a factor of regular Γ-iid”}
\]
is **DISPROVED**.

There is no obstruction for the same-\(W\) source in this example:
\[
X(w)=\mathbf1_{\{U_w\le p\}}
\]
already works. This counterexample distinguishes sources; it does not contradict C.

## 3. A demanding forest implication on a nonamenable graph with cycles

Consider
\[
\Gamma=F_2\times C_3
=\langle a,b\rangle\times\langle c:c^3=1\rangle
\]
and
\[
G=\operatorname{Cay}
\bigl(\Gamma,\{a^{\pm1},b^{\pm1},c^{\pm1}\}\bigr)
=T_4\square C_3.
\]

### Exact edge coordinates and projections

Let \(T=\{a,b,c\}\). Since \(T\cap T^{-1}=\varnothing\),
\[
\theta:\Gamma\times T\longrightarrow E(G),
\qquad
(g,t)\longmapsto\{g,gt\}
\]
is a bijection. Orient that edge from \(g\) to \(gt\). Left translations preserve these orientations.

Use \(\ell^2(E^+)\), with one orientation and one unit basis vector per unoriented edge. Put
\[
df(e)=f(e^+)-f(e^-),
\]
\[
\mathcal S=\overline{dC_c(V)},
\qquad
\mathcal C
=
\overline{\operatorname{span}
 \{\text{finite signed cycle vectors}\}}.
\]
All closures are in \(\ell^2(E^+)\). Cycle telescoping gives
\[
\mathcal S\subseteq\mathcal C^\perp.
\]
Define
\[
Q_W=P_{\mathcal S},
\qquad
Q_F=P_{\mathcal C^\perp}.
\]

The infinite transfer-current theorem gives exactly
\[
\operatorname{WUSF}_G=\mathbf P^{Q_W},
\qquad
\operatorname{FUSF}_G=\mathbf P^{Q_F}.
\]
These are the wired and free projections, respectively—not interchangeable conventions. :chatgpt-content-reference{index="1"}

The exhaustion argument explains the distinction. For a free finite exhaustion \(G_n\), its UST projection, extended by zero outside its edges, is
\[
I_{E(G_n)}-P_{\mathcal C_n}.
\]
The cycle spaces increase densely to \(\mathcal C\), so these operators converge strongly to \(I-P_{\mathcal C}\). For wired exhaustion with interior vertices \(V_n\), the star spaces
\[
\operatorname{span}\{d\delta_v:v\in V_n\}
\]
increase densely to \(\mathcal S\), so their projections converge strongly to \(P_{\mathcal S}\). Finite inclusion determinants converge in each case.

Translation preserves finite signed cycles. Thus \(Q_F\), transported through \(\theta\), satisfies precisely the operator hypotheses of C. Applying C and forgetting the coordinate names proves:

> **Conditional forest theorem.** The FUSF on \(T_4\square C_3\) is a measurable Γ-factor of iid Uniform\([0,1]\) labels indexed by its vertex set Γ.

### Why this is not a deterministic-tree or wired-forest substitution

**Nonamenability.** For a finite vertex set \(A\), let \(A_j\) be its slice in the \(j\)-th copy of \(T_4\). Since a finite induced subgraph of \(T_4\) is a forest, its horizontal edge boundary has at least \(2|A_j|\) edges. Summing over the three slices gives
\[
|\partial_E A|\ge2|A|.
\]

**Every edge is genuinely random.** Every vertical edge belongs to a triangle, and every horizontal edge belongs to a four-cycle. If \(e\) belongs to a cycle of length \(L\), then
\[
\|P_{\mathcal C}\delta_e\|^2\ge \frac1L,
\qquad
Q_F(e,e)\le1-\frac1L<1.
\]
An endpoint star belongs to \(\mathcal S\subset\mathcal C^\perp\) and has nonzero pairing with \(\delta_e\). Since the degree is six,
\[
Q_F(e,e)\ge\frac16>0.
\]
Thus the free forest is nondeterministic.

**Free and wired are different.** Root \(T_4\) at \(o\) and distinguish one branch. Define \(h(o)=1/4\), and at depth \(n\ge1\),
\[
h(v)=
\begin{cases}
1-\frac34\,3^{-n},&\text{in the distinguished branch},\\[2mm]
\frac14\,3^{-n},&\text{in the other three branches}.
\end{cases}
\]
The root equation and
\[
4h_n=h_{n-1}+3h_{n+1}
\]
show that \(h\) is harmonic.

At level \(n\), the increments are \((3/2)3^{-n}\) on \(3^{n-1}\) edges and \(-(1/2)3^{-n}\) on \(3^n\) edges. Hence
\[
\sum_{\{v,w\}\in E(T_4)}|h(v)-h(w)|^2
=\sum_{n\ge1}3^{-n}
=\frac12.
\]
Lift \(H(v,j)=h(v)\) to \(G\). It is harmonic and has energy \(3/2\). Therefore
\[
0\ne dH\in\mathcal C^\perp\cap\mathcal S^\perp:
\]
membership in \(\mathcal C^\perp\) follows by telescoping, and orthogonality to \(\mathcal S\) follows by summation by parts and harmonicity.

Consequently,
\[
Q_F-Q_W
=
P_{\mathcal C^\perp\cap\mathcal S^\perp}\ne0.
\]
A nonzero positive operator has some positive diagonal entry, so at least one edge marginal differs:
\[
\operatorname{FUSF}_G\ne\operatorname{WUSF}_G.
\]

The graph is also nonplanar: contract the triangle fibers over three neighbors of a tree vertex, retain the three central-fiber vertices, and delete the central triangle edges. This produces a \(K_{3,3}\) minor.

### All Cayley graphs, including involutive generators

A globally invariant orientation is unnecessary.

For a finite symmetric generating set \(D\), use all arcs \(\Gamma\times D\). Choose reference orientations only for Hilbert-space coordinates and define
\[
J\delta_e
=
\frac{\delta_{\vec e}-\delta_{\overleftarrow e}}{\sqrt2},
\qquad
\widehat Q=JQ_FJ^*.
\]
The edge-coordinate action has signs when an orientation is reversed. \(J\) intertwines that action with the permutation action on arcs. Thus \(\widehat Q\) is an equivariant positive contraction on the candidate’s free finite-mark space.

The two opposite-arc rows are negatives, so its DPP cannot select both. For \(k\) distinct unoriented edges, each of the \(2^k\) orientation choices has determinant
\[
2^{-k}\det(Q_F|_F).
\]
Summing the disjoint choices recovers the FUSF inclusion determinant. Applying C and forgetting orientations proves the all-Cayley-graph implication, without claiming all-\(\operatorname{Aut}(G)\) equivariance.

## 4. Which forest consequences are already known?

### Wired forests: a verified theorem, but the wrong projection for the main test

Angel–Ray–Spinka, Theorems 1.4 and 4.1 and §4, prove that WUSF on a connected transient random rooted graph is a graph factor of iid. **Their WUSF theorem does not require unimodularity.** It implements infinite cycle-popping rather than merely invoking order-independence of Wilson’s output distribution. :chatgpt-content-reference{index="2"}

On \(T_4\square C_3\), the horizontal projection of simple random walk is a lazy transient walk on \(T_4\), so the theorem applies. Its vertex source is exactly Γ-indexed. But it produces \(Q_W\), not the distinct \(Q_F\) above.

### A nonamenable cyclic FUSF consequence whose exact status is known

Take the genus-two surface group
\[
\Lambda
=
\langle a,b,c,d\mid[a,b][c,d]=1\rangle
\]
and the Cayley graph obtained from the one-vertex, four-edge, one-octagon cellulation of the surface. Its universal cover is the degree-eight hyperbolic octagonal tiling. It has a proper plane embedding and finite cycles. The group is nonamenable: it surjects onto \(F_2\) by killing \(b,d\).

The dual is locally finite and transient. Its vertices—the lifted faces—form one free Λ-orbit. Fix one lifted face \(f_0\). The map
\[
g\longmapsto gf_0
\]
is an equivariant bijection from Λ to dual vertices. Assign the face \(gf_0\) the label \(U_g\). This explicitly converts the required regular source into the dual-vertex iid source.

Apply the Angel–Ray–Spinka WUSF factor on the dual, then declare
\[
e\in F
\quad\Longleftrightarrow\quad
e^\dagger\notin W^\dagger.
\]
BLPS Theorem 12.2 identifies this law as the **primal FUSF**. The map is Λ-equivariant. Thus this nonamenable, cyclic projection-DPP consequence of C is **already known independently of C**. Its kernel is \(P_{\mathcal C^\perp}\), just as above. :chatgpt-content-reference{index="3"}

### What remains unverified in the literature audit

For the exact Γ-equivariant FUSF assertion on \(T_4\square C_3\), I located neither a matching theorem nor a counterexample. Its individual prior-art status is therefore **UNRESOLVED in this audit**, not certified open or novel.

Timár’s December 16, 2025 revision expressly records the FUSF factor question **in full generality** as open. His Theorem 4, Corollary 5, and Theorem 9 use invariant amenability; free and wired coincide there. That dated statement about the broader graph-factor problem does not certify that every individual nonamenable Cayley example is unresolved. :chatgpt-content-reference{index="4"}

Likewise, iid-weight **minimal** spanning forests are not **uniform** spanning forests, and disconnectedness of a FUSF is not a factor obstruction. The relevant primary works distinguish those issues. :chatgpt-content-reference{index="5"}

## 5. Primary-source comparison

“Stronger” below means a stronger conclusion **within the stated restricted hypotheses**, not a theorem globally stronger than C. The links supply the requested URLs; complete bibliographic information and version checks are in `REFERENCES.md`.

| Primary source and date | Exact relevant result and hypotheses | Relationship to C and the proposed method |
|---|---|---|
| [Lyons–Steif](https://arxiv.org/abs/math/0204324), 2002 preprint; 2003 publication | **Theorem 3.1:** stationary DPPs on \(\mathbb Z^d\), measurable symbols \(0\le f\le1\). | Bernoulli **isomorphism**: stronger conclusion on the abelian special case, including projection symbols. Not the proposed birth construction. :chatgpt-content-reference{index="6"} |
| [Lyons–Thom](https://arxiv.org/abs/1402.0969), 2014; 2016 publication | **Theorem 7.3:** sofic approximation in \(\bar d\). **Corollary 7.4:** amenable Bernoulli isomorphism. | Nearby approximation; stronger amenable conclusion. Approximation alone is not C. :chatgpt-content-reference{index="7"} |
| [Georgii–Yoo](https://arxiv.org/abs/math/0401402), 2004; 2005 publication | **(H), Theorems 3.1, 3.6–3.7:** locally trace-class Hermitian \(K\), \(\|K\|<1\); additional condition for equality with the global shorting limit. | Papangelou determinant ratios, antimonotonicity, global conditional intensities: same ingredients, not a universal iid-factor theorem. :chatgpt-content-reference{index="8"} |
| [Yoo](https://arxiv.org/abs/math/0506189), 2005; 2007 publication | **Preprint Theorem 2.4, (2.22)–(2.27), (H):** bounded positive injective interaction \(A\), functionally completed energy space. | Direct prior art for the residual-distance/shorted Papangelou expression. Arbitrary singular projections are not covered. :chatgpt-content-reference{index="9"} |
| [Chae–Yoo](https://arxiv.org/abs/1001.1589), 2009 publication; 2010 arXiv | **Theorem 2.2; Proposition 3.8; Assumption (A), Theorem 4.2:** strict diagonal dominance; additional small off-diagonal mass for ergodicity. | Shorting increment identities and invariant Feller dynamics. Same ingredients; invariant measure or ergodicity alone does not establish a factor. :chatgpt-content-reference{index="10"} |
| [Lytvynov–Ohlerich](https://arxiv.org/abs/math/0702338), 2007; 2008 publication | **§2, Theorem 3.1:** spectral value \(1\) excluded; stated rate-integrability assumptions. | DPP-symmetric conservative Hunt dynamics via Dirichlet forms. Nearby equilibrium result, not prescribed-noise strong realization. :chatgpt-content-reference{index="11"} |
| [Garcia–Kurtz](https://arxiv.org/abs/math/0605620), 2006 | **Theorem 2.13; Theorems 3.3, 3.10; Lemma 3.16:** weighted worst-case influence \(M<\infty\), with \(M<1\) for contraction. | Poisson equations, Picard construction, common-noise stationary factors are prior art. Their worst-case/unit-death hypotheses are not the candidate’s averaged estimate. :chatgpt-content-reference{index="12"} |
| [Hough–Krishnapur–Peres–Virág](https://arxiv.org/abs/math/0503110), 2005; 2006 publication | **Theorem 7; Algorithm 18, Proposition 19:** trace-class spectral mixture and finite-dimensional projection sampling. | Exact sampling in that domain. Global normalized selection does not directly treat a nonzero invariant infinite-trace Γ-kernel. :chatgpt-content-reference{index="13"} |
| [Decreusefond–Flint–Low](https://arxiv.org/abs/1311.1027), 2013 | **(H1), §3.2 Theorem 3.1, Algorithms 1–2:** \(\|K\|<1\), dominating birth–death process and global empty-state coalescence. | Close Papangelou/CFTP ingredients. The global count/visit-empty justification does not establish the infinite-total-intensity Γ application. :chatgpt-content-reference{index="14"} |
| [Spinka](https://arxiv.org/abs/1901.00123), 2019; 2020 publication | **Theorem 1.1:** finitely dependent invariant processes on transitive amenable locally finite graphs. | Finitary factor: stronger regularity in a special case. Does not cover arbitrary nonamenable or long-range DPPs. :chatgpt-content-reference{index="15"} |
| [BLPS](https://rdlyons.pages.iu.edu/pdf/usf.pdf), 2001 | **Theorems 5.1, 7.8, 12.2:** transient Wilson law, forest projections, proper-plane duality with locally finite dual. | Identifies the precise laws and enables the planar consequence; not a universal nonamenable-FUSF factor theorem. :chatgpt-content-reference{index="16"} |
| [Angel–Ray–Spinka](https://arxiv.org/abs/2112.03228), 2021; 2024 publication | **Theorems 1.4/4.1, §4:** connected transient random rooted graph; no unimodularity assumption for this theorem. | Actual graph-FIID theorem for **WUSF**, with stronger graph equivariance than a chosen Γ action. Different projection and method. :chatgpt-content-reference{index="17"} |
| [Timár](https://arxiv.org/abs/2306.15120), 2023; v2 December 2025 | **Theorem 4, Corollary 5, Theorem 9:** invariant amenability and compatible monotone limits; finitary USF. | Stronger coding regularity in the amenable case, not the distinct nonamenable free law. :chatgpt-content-reference{index="18"} |
| [Nam–Sly–Zhang](https://arxiv.org/abs/2012.09484), 2020 | **Theorem 1, §2: