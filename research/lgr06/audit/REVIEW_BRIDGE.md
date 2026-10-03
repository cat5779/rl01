# Q7.7 semantics and application-interface audit B

STATUS: CRITICAL_GAPS

This status is for the **whole claimed application chain through the Lyons--Gaboriau target**, not for the prescribed-
\(W\) theorem by itself.  I found no load-bearing mathematical gap in `theorem01.md`/`proof01.md`.  The critical gap is
that Q7.7 factorhood does not supply connectivity or a low-cost connectivity repair.  If that missing input did give
the sharp cost bound for the regular Bernoulli action of a finitely generated infinite group, Abért--Weiss maximality
would in fact upgrade it to fixed price; see Section 4.

## Sources

Primary sources checked:

1. Russell Lyons and Andreas Thom, *Invariant coupling of determinantal measures on sofic groups*, ETDS 36 (2016),
   574--607, author-hosted published PDF: <https://rdlyons.pages.iu.edu/pdf/couple-pub.pdf>.
2. Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, ICM 2014, author-hosted published
   PDF: <https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf>.
3. Russell Lyons, Mikael Pichot, and Stéphane Vassout, *Uniform non-amenability, cost, and the first
   \(\ell^2\)-Betti number*, author-hosted PDF: <https://rdlyons.pages.iu.edu/pdf/unabetti.pdf>.
4. Miklós Abért and Benjamin Weiss, *Bernoulli actions are weakly contained in any free action*, ETDS 33 (2013),
   323--333, authors' repository copy: <https://real.mtak.hu/10014/1/abert.pdf>.

## Separate verdicts

| Item | Verdict | Exact boundary |
|---|---|---|
| Main prescribed-\(W\) DPP proof | **CORRECT** | No critical gap found; it proves a total Borel, everywhere equivariant map from iid labels indexed by the same countable \(\Gamma\)-set \(W\). |
| Match to original Question 7.7 | **CORRECT, with terminology pinned to the paper** | Lyons--Thom explicitly call \((A^W,\lambda^W)\) a Bernoulli shift for a countable \(\Gamma\)-set \(W\); Q7.7 therefore does not force the source to be \(A^\Gamma\). |
| Fixed-graph FUSF consequence | **CORRECT only via the law-level sampler criterion and the separate vertex-to-edge iid lemma** | It is not a literal corollary of `theorem01.md`'s unsigned commuting-kernel hypothesis.  Scope is a fixed countable locally finite simple graph; no varying-random-graph measurability is obtained. |
| Lyons--Gaboriau bridge | **CRITICAL GAPS / OPEN** | Q7.7 gives a factor representation only.  Connectivity of the chosen Theorem 5.10 approximant, or an arbitrarily cheap measurable connectivity repair, remains unproved.  Conditional on that missing step yielding the sharp regular-Bernoulli cost bound, Abért--Weiss would upgrade the result to fixed price for finitely generated infinite \(\Gamma\). |

## 1. Main proof audit

### 1.1 Finite DPP tilt and uniform row bound

The singular-endpoint treatment is sound.  With
\(M=I-K+K^{1/2}DK^{1/2}\), positivity follows from
\(M\ge I-K+dK\ge\min(1,d)I\); neither \(K\) nor \(I-K\) is inverted.  The tilted generating polynomial gives the
Hermitian positive contraction
\(P=D^{1/2}K^{1/2}M^{-1}K^{1/2}D^{1/2}\).  For its root row,
\[
 \sum_y |\operatorname{Cov}(\eta_x,\eta_y)|
 =p(1-p)+(P^2)_{xx}-p^2\le 2p(1-p)\le\tfrac12.
\]
This covers complex Hermitian entries, eigenvalues 0 and 1, and deterministic coordinates.

### 1.2 Exhaustion and component independence

The threshold graph \(|Q_{xy}|\ge1/n\) has degree at most \(n^2\), since
\(\sum_y|Q_{xy}|^2=(Q^2)_{xx}\le Q_{xx}\le1\).  Radius-\(n\) balls are therefore finite; increasing the threshold
index and radius makes them nested, and every finite nonzero-kernel path eventually appears.  Block determinants plus
inclusion--exclusion give independence of the entire component sigma-fields, not merely finite-coordinate independence.

### 1.3 Infinite SDE and posterior

The limsup drift is defined on every real field.  The proof only applies the \(\ell^\infty\) Lipschitz estimate to
bounded **differences** of Picard iterates or solutions; it never assumes a countable Brownian field is spatially
bounded.  The factorial Picard estimate yields an all-input Borel causal solution and pathwise uniqueness.

Finite Gaussian Bayes, upward conditional-expectation convergence on the kernel component, and component independence
identify the endpoint posterior.  Brownian bridges are independent of the entire endpoint/signal field, so the same
posterior is the posterior given the full observation history.  Joint measurability and Fubini correctly avoid an
uncountable intersection of fixed-time full-measure events.

### 1.4 Innovations and same-noise decoding

All innovation coordinates are martingales in one completed right-continuous filtration.  Finite-vector quadratic
variation \(tI\) and the vector Lévy characterization give product Wiener law, which is stronger than pairwise zero
covariance.  Pathwise uniqueness identifies the observation process as the deterministic solution driven by those
innovations.  The decoder uses that same noise for all integer times; the summable Gaussian error bound and
Borel--Cantelli recover all countably many bits.  Thus there is no weak-limit/factor-limit substitution.

## 2. What Lyons--Thom Question 7.7 actually asks

The paper's introduction defines a \(\Gamma\)-factor at journal p.576 and then says that for a countable
\(\Gamma\)-set \(W\), if \(\mu=\lambda^W\), the action on \(A^W\) is called a **Bernoulli shift** (journal p.576,
PDF pp.3--4).  It explicitly says the spaces considered are \(A^\Gamma\), "or, more generally, \(A^W\)".  Hence the
paper itself licenses the prescribed-\(W\) source.

Question 7.7 reads: "Are determinantal probability measures associated to equivariant positive contractions factors
of Bernoulli shifts?" (journal p.595, PDF p.22).  It follows Question 7.6, which explicitly concerns a quasi-transitive
countable \(W\), and the proof discussion immediately says statements for \(R(\Gamma)\) extend to
\(R(\Gamma,S)=M_S(R(\Gamma))\).  The original setting is therefore not restricted to a regular \(\Gamma\)-indexed
source in the modern narrower use of "Bernoulli shift".

The frozen theorem is in fact more general in group assumptions: it allows every countable group and every countable
\(\Gamma\)-set, whereas the paper's principal theorems are developed for finitely generated sofic groups and finite
generating sets.  This extra generality does not weaken or alter Q7.7.

### Regular source conversion and its limits

For \(W=\Gamma\times S\) with finite \(S\), digit splitting at each \(g\) converts iid \([0,1]^\Gamma\) into iid
\([0,1]^{\Gamma\times S}\) equivariantly.  This covers the finite-matrix/Cayley-**diagram arc** coordinate space.
It must not be called a bijection with the unoriented edge set of a Cayley graph: for symmetric \(S\), opposite arcs
represent the same edge, and an involutive generator can prevent an equivariant choice of one orientation.  The
candidate's regular-source sentence is correct only when "arc" remains explicit.

For a general nonfree \(\Gamma\)-set, prescribed-\(W\) iid cannot be replaced universally by regular
\(\Gamma\)-iid.  The coset example correctly detects the stabilizer obstruction when the stabilizer
acts ergodically on the regular Bernoulli source.  This is a boundary of regularization, not a defect in the answer to
the paper's own terminology.

## 3. FUSF interface

Lyons--Thom describe FUSF on a fixed graph as the projection DPP onto the orthogonal complement of the finite-cycle
space (journal pp.578--579, especially their spanning-forest discussion in Section 2).  After choosing reference
orientations, a graph automorphism generally acts on \(\ell^2(E)\) by a **signed permutation**.  Thus the projection
usually satisfies
\[
 U_\phi Q U_\phi^*=Q
\]
for signed \(U_\phi\), not \(P_\phi QP_\phi^*=Q\) for the unsigned coordinate permutation.

Consequently, one may not invoke `theorem01.md` verbatim.  The FUSF conclusion is nevertheless supported by the more
general sampler criterion proved in `g6/source.md`:

* signed conjugation leaves every principal determinant unchanged, hence the unoriented DPP law is invariant;
* it leaves \(|Q_{ef}|\) unchanged, hence the threshold windows are invariant;
* the drift in that criterion is defined from finite marginal laws and those windows, so it is exactly equivariant at
  the law level.

This distinction must remain visible in any theorem statement or abstract.  "The kernel commutes with automorphisms"
is false if it means the unsigned permutation representation.

The edge-iid to vertex-iid interface in `g6/source.md` is valid for a **fixed countable locally finite simple graph**.
Independent vertex keys choose an owner for every edge; the owner's independent stack coordinate is selected by the
neighbor's key rank.  Conditional on the keys, distinct edges use distinct iid stack coordinates, so the edge labels
are iid.  The construction is pointwise equivariant under the full (possibly uncountable) \(\operatorname{Aut}(G)\).
Countability makes the global no-tie event conull.  Local finiteness is used to give a finite rank/slot at each vertex.

Therefore the fixed-graph claim is acceptable:

> On every fixed connected countable locally finite simple graph, FUSF is a total Borel vertex-iid factor equivariant
> under the full automorphism group.

It does **not** establish one jointly Borel rule over a random rooted graph space.  It also does not follow by treating
full \(\operatorname{Aut}(G)\) as the countable group in `theorem01.md`; it follows because the canonical formulas
commute pointwise with every automorphism.

## 4. Lyons--Gaboriau cost bridge

Lyons's ICM survey states (printed p.158, PDF p.21):

* Theorem 5.8: \(\mathbb E_{\rm FSF}\deg(o)=2\beta_1^{(2)}(\Gamma)+2\).
* Theorem 5.10: for every Cayley graph of a finitely generated group and every \(\varepsilon>0\), there is a
  \(\Gamma\)-invariant finitely dependent determinantal edge process dominating FSF with expected degree at most the
  FSF expected degree plus \(\varepsilon\); for sofic \(\Gamma\), it can also be \(\bar d\)-close.
* The following paragraph says that if this process, or every invariant finitely dependent process dominating FSF,
  were connected a.s., then \(\beta_1^{(2)}(\Gamma)+1=\operatorname{cost}(\Gamma)\).

Q7.7 supplies none of the italicized connectivity premise.  A factor image can be disconnected.  Finite dependence,
stochastic domination, small expected-degree excess, and \(\bar d\)-closeness do not become connectivity merely because
the process is represented as a Bernoulli factor.  No "cheap repair" may be appended without a separate measurable
construction and an expected-degree estimate tending to zero.

The cost objects must also remain separate.  Lyons--Pichot--Vassout define (Section 4.3, printed p.8):

1. for an equivalence relation \(R\), \(C(R)\) is the infimum of costs over graphings of that fixed relation;
2. for a free pmp action \(\alpha\), its action cost is \(C(R_\alpha)\);
3. group cost is \(C(\Gamma)=\inf_\alpha C(R_\alpha)\) over ergodic essentially free pmp actions.

A connected invariant edge process realized over the regular Bernoulli action would give a graphing of that
**particular Bernoulli orbit relation**, with cost half its expected degree.  Letting \(\varepsilon\downarrow0\) would
therefore prove
\[
 C(R_{\mathrm{Bern}})\le 1+\beta_1^{(2)}(\Gamma).
\]

There is an important further implication.  Abért--Weiss Theorem 1 says that, for every countably infinite group,
every free pmp action weakly contains every Bernoulli action.  For finitely generated groups, their Theorem 9 gives
the relevant monotonicity direction: if \(f\) weakly contains \(g\), then
\(\operatorname{gcost}(f)\le\operatorname{gcost}(g)\).  Their Corollary 2 consequently states that cost is
**maximal** on free Bernoulli actions (indeed, on free factors of iid).  Thus, for every free pmp action \(\alpha\),
\[
 C(R_\alpha)\le C(R_{\mathrm{Bern}}).
\]
Combining the hypothetical sharp Bernoulli upper bound with Gaboriau's universal lower bound
\(C(R_\alpha)\ge1+\beta_1^{(2)}(\Gamma)\) gives
\[
 C(R_\alpha)=C(R_{\mathrm{Bern}})=1+\beta_1^{(2)}(\Gamma)
 \qquad\text{for every free pmp }\alpha.
\]
For finitely generated infinite \(\Gamma\), the missing connectivity/repair step would therefore prove not only the
group-cost infimum equality but also **fixed price**. This implication uses the stated maximality and lower-bound directions.

Thus the exact present implications are
\[
 \text{prescribed-}W\text{ DPP factor theorem}
 \Longrightarrow \text{Q7.7 factor representation},
\]
and, separately,
\[
 \text{Theorem 5.10 approximant + connectedness (or proved }o(1)\text{-cost repair)}
 \Longrightarrow C(R_{\mathrm{Bern}})=C(\Gamma)=\beta_1^{(2)}(\Gamma)+1
 \Longrightarrow \text{fixed price}
\]
for finitely generated infinite \(\Gamma\), where the last arrow uses Abért--Weiss plus Gaboriau's lower bound.
There is still no proved arrow from the first line to the missing connectivity premise in the second.

## 5. Required wording repairs before downstream use

1. Say "answers Q7.7 in Lyons--Thom's explicit generalized Bernoulli-shift sense \(A^W\)"; do not silently replace
   it by regular \(A^\Gamma\), and do not claim the latter for arbitrary stabilizers.
2. For \(R(\Gamma,S)\), say "directed Cayley-diagram arcs \(\Gamma\times S\)".  Do not identify them with unoriented
   Cayley-graph edges when reversals or involutions are present.
3. State the FUSF application through the invariant-law sampler criterion.  Do not say its reference-oriented kernel
   commutes with the unsigned edge permutation.
4. Keep "fixed graph/full automorphism equivariance" separate from "joint rule on random graphs".
5. Describe the LG consequence as conditional on connectedness or a separately proved arbitrarily cheap repair.
6. Keep group cost, Bernoulli-action cost, and fixed price definitionally distinct, but record the valid implication:
   for finitely generated infinite groups, a sharp upper bound on Bernoulli-action cost plus Abért--Weiss maximality
   and Gaboriau's universal lower bound does upgrade to fixed price.

No connectedness theorem or repair theorem was added in this audit.
