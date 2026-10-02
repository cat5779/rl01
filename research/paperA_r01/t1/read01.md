# Independent general-referee report

## Recommendation

**Major revision.** I found no concrete counterexample to Theorems A--D, and the principal proof chains are mathematically coherent. The most delicate result—the natural, jointly Borel sampler—nevertheless crosses two levels that are compressed into a few paragraphs: from finite posterior formulas to a countable stochastic system, and from a fixed countable index set to the Borel field of arc sets over unlabelled rooted graphs. Those are parts of the theorem, not implementation details. They should become named propositions with explicit measurable spaces and null-set quantifiers.

The paper contains enough material for more than one substantial article. Its present architecture can work if the introduction makes the dependency structure unmistakable and the exposition consistently separates four notions: an iid factor, ordinary stochastic domination, an invariant monotone joining, and invariant coupling distance.

This report separates mathematical correctness from readability. It does not assess novelty; the draft makes no priority claim, and I have not performed an exhaustive forward-citation search.

## The four claims and their source questions

1. Lyons--Thom Question 7.7 asks whether DPPs associated with equivariant positive contractions are factors of Bernoulli shifts. Theorem A supplies a stronger natural sampler on the prescribed countable index set $W$. Its source is $[0,1]^W$; no regular source is silently substituted.
2. Applying this sampler to a jointly Borel transfer-current kernel gives FUSF as an Angel--Ray--Spinka graph factor on every locally finite connected simple random rooted graph.
3. Lyons's Conjecture 5.7 supplies the FK-determinant Bernoulli bounds. Theorem B proves the bounds for every countable group, while Theorem C proves pointwise equality for amenable groups and gives strict $C_3*C_3$ counterexamples outside that class, including an explicit finite-support group-ring kernel.
4. A separate, unnumbered question immediately after Lyons--Thom Lemma 7.8 asks for the sharp noncommutative $\bar d$ trace-norm bound. Theorem D proves it for countable sofic groups by combining their ordered-coupling theorem with a polygonal path inside the positive contractions.

The draft gets this distinction right. Question 7.7 is the factor question; it is not the $\bar d$ question and should never be described as an equation numbered 7.7.

## Mathematical assessment

### 1. The countable DPP sampler

The construction in §§3.1--3.5 is plausible and, in its main algebraic and probabilistic steps, convincing.

- The threshold graphs $D_n$ have finite degree because each row of a positive contraction is square summable. The balls $E_n(x)$ are finite, increase with $n$, and exhaust the component of $x$ in the nonzero-kernel graph.
- Lemma 3.1 gives the needed dimension-free $1/2$-Lipschitz constant. Its tilted-kernel formula covers singular and complex Hermitian kernels.
- The Picard argument is designed correctly for spatially unbounded Brownian input: only successive corrections are estimated in $\ell^\infty$.
- In §3.4, the Brownian-bridge decomposition identifies the endpoint posterior with the history posterior, and the innovations calculation yields a product Brownian field. Pathwise uniqueness turns the auxiliary weak construction into the required deterministic map. The integer-time decoder and countability of $W$ give simultaneous recovery of all coordinates.

I see no evident contradiction in this chain. Several assertions carrying most of the probability theory are simply too condensed for a result of this strength.

**Rewrite request at §3.3, immediately after (3.6).** State a proposition whose conclusion is the precise joint Borel map

\[
(K,w)\longmapsto \mathcal Z_K(w)
\]

on a named standard Borel space of positive contractions and a named product path space. Specify the topology or sigma-field on the operator parameter. “Borel in the matrix entries” is adequate only after the parameter space has been defined.

**Rewrite request at Lemma 3.2.** Break the proof into three labelled claims:

1. $b^n_{t,x}(X_t)$ is the finite-window posterior and converges to the all-coordinate endpoint posterior;
2. the bridge sigma-field is independent of $\sigma(\eta,X_t)$, so the endpoint posterior is a version of the history posterior for $dt\otimes d\mathbb P$-almost every $(t,\omega)$;
3. the innovations are a countable product Brownian field for the common completed, right-continuous filtration.

The prose around (3.8) contains these facts, but the reader has to reconstruct the monotone-class and null-set argument. State where countability of $W$ is used and why no intersection over uncountably many times is taken.

**Rewrite request at Theorem A.** State first the action-free sampler theorem for arbitrary countable $W$ and arbitrary positive contraction $Q$. Then state equivariance under a group action as a corollary of naturality. That is the proof's logical order and makes clear that regularity of the action plays no role.

### 2. Varying graphs and joint Borel measurability

The passage from a fixed index set to Corollary A1 is the point most likely to draw a descriptive-set-theory objection. Section 4.2 recognizes the issue and uses the right strategy: finite-cycle projections, a canonical numbered representative, and naturality to remove the numbering.

The paragraph around (4.2) nevertheless combines three distinct claims:

1. arc sets of the numbered representatives form a countable Borel field;
2. $(G,a,b)\mapsto K_G(a,b)$ is Borel on that field;
3. the sampler of §3 is Borel on variable countable fibers and descends through a change of representative.

**Rewrite request at §4.2, after (4.2).** Promote these claims to a “Borel bundle lemma.” Give the exact Aldous--Lyons result used: the continuous canonical representative on a network with vertex set $\mathbb N$. Explain that Lusin--Novikov partial enumerations are used only to verify Borel measurability of finite sums and finite balls. Finally, state that two representatives are related by a fiberwise bijection and invoke (3.9) to prove independence from the numbering. This closes the only genuinely nontrivial bridge from Theorem A to a graph factor.

The finite-cycle approximation itself is sound. Its center may depend on the first specified arc because it is used only to compute one matrix entry; the draft correctly warns that these approximants are not being assembled into one global finite-stage kernel.

### 3. The Angel--Ray--Spinka and Timár definitions

The draft uses the Angel--Ray--Spinka definition explicitly and proves a pointwise rerooting-compatible Borel rule. This is enough for Corollary A1 and does not require unimodularity.

Timár §2 gives an automorphism-equivariant factor map on a fixed quasi-transitive graph and then says that the root/incident-edge local-approximation formulation can be applied to arbitrary unimodular random graphs. The direction needed here is safe: a Borel graph factor gives local approximation in probability at the root. Section 4.4 states exactly that direction.

Appendix A.2 is appropriately cautious. The reverse implication is asserted only for a compatible system inside a jointly unimodular marked coupling, and the arbitrary-coupling weakening is labelled artificial rather than attributed to Timár.

**Rewrite request at §4.4.** Quote or paraphrase Timár's two-sentence definition more exactly, and state one implication in theorem form: “ARS graph factor implies Timár root-local approximation; this is the only implication used.” Keep the conditional converse and the two-colouring counterexample in Appendix A.2.

**Rewrite request at Corollary A1 and §4.4.** Retain “simple” in every short restatement. The parallel-edge obstruction shows that it is a mathematical hypothesis under vertex-only randomness. Also retain the sentence that no finitary or finite-bit conclusion is claimed.

### 4. The FK Bernoulli bounds

The proof in §5 is concise and structurally complete. Formula (5.3) is checked on an actual basis of all functions on $2^V$; (5.2) supplies the sign; inverse compression and equality of diagonal entries give the finite-volume hypothesis along the determinant-preserving path. Regularization handles $D(Q)=0$, including injective kernels with nonintegrable $\log Q$, and complementation supplies the upper bound.

I found no quantifier loss here. The conclusion is ordinary stochastic domination, and the draft repeatedly distinguishes it from an invariant monotone joining.

**Rewrite request at §5.1.** Turn the conclusion following (5.4) into a named finite differential lemma. Theorem B depends on it, and a reader should be able to locate its hypotheses without extracting them from prose.

**Rewrite request at (5.5)--(5.8).** Add one displayed line showing

\[
D(K_t)=a_tD(Q+tI)=D(Q)
\]

and one line deriving $K_t'=a_t(I-\tau(K_t^{-1})K_t)$. These calculations explain the path and prevent the central interpolation from looking magical.

### 5. Amenable equality and the tree counterexample

The use of Li--Thom Theorem 1.4 in §6.1 has the correct premises: a positive element in $M_d(\mathcal N\Gamma)$, a countable amenable group, unnormalized matrix trace, and no invertibility or finite-generation hypothesis. Testing all-occupied events then gives the necessary bound, including when the determinant is zero.

The tree calculation in §6.2 is internally consistent. The projection is the WUSF projection, every finite edge compression is nonsingular, the forward-subtree gradient gives conditional occupation at least $1/(d-1)$, and the finite-subtree determinant has the matching exponential rate. The complete-star event proves $p_+=1$.

The representation step in §6.3 is essential and is present: the Bass--Serre edge action of $C_3*C_3$ is free and transitive, and the bipartite orientation is preserved. This puts the edge projection in one regular copy of $R(\Gamma)$. The spectral-gap affine kernel and the explicit finite-support approximation answer the two obvious objections to the projection example.

**Rewrite request at §6.2, before (6.4).** Say explicitly that the breadth-first enumeration constructs an ordinary sequential coupling. No invariance of that coupling is claimed or needed for $p_-$.

**Rewrite request in Appendix B at (B.2).** Do not leave the strict numerical inequality to an accompanying script. Include a short exact bound in the text or an exact integer inequality in a footnote. The script is corroboration, not a proof premise.

**Rewrite request in Appendix B before (B.2).** Add the geometric-series identity showing directly why $P_N\to\Pi$. The phrase “The Neumann series ... imply” currently suppresses the calculation explaining the degree-$255$ choice.

### 6. The $\bar d$ theorem

Section 7 correctly separates the source theorem from the polygon. Lyons--Thom Theorem 5.1 is stated with its original finite-generation premise. The extension in §7.1 is valid: compression to an increasing finitely generated subgroup preserves positivity, order, and subgroup equivariance; independent copies on left cosets have block-diagonal kernels $C_n,D_n$; finite principal matrices eventually agree with the target kernels; compactness preserves invariance and monotonicity.

The polygon in §7.2 stays in the positive-contraction interval. Consecutive points are comparable in alternating directions, and summing their ordered coupling distances gives (7.3). Letting $N\to\infty$ is purely numerical and requires no continuity of $\bar d$. The scalar example proves sharpness.

**Rewrite request at §7.1.** Insert one sentence explaining why each finitely generated subgroup of a sofic group is sofic, and specify that the compression is the principal compression to $\ell^2(H_n)$. Also state that the block-diagonal kernel on cosets is the kernel of the independently copied marginal.

**Rewrite request at §7.3.** Preserve the distinction already made there: Question 7.7 is the factor question, while the trace-norm problem is unnumbered and follows Lemma 7.8. Put this correction once in the introduction as well.

## Architecture and reader burden

The current order is the right one:

1. natural sampling on arbitrary $W$;
2. the FUSF graph-factor application;
3. the FK comparison;
4. amenable sharpness and nonamenable counterexamples;
5. the independent $\bar d$ polygon.

The introduction should make the dependency graph explicit:

\[
\text{natural sampler}
\longrightarrow
\begin{cases}
\text{Lyons--Thom Q7.7},\\
\text{FUSF graph factor},
\end{cases}
\qquad
\text{finite differential lemma}\longrightarrow\text{FK bounds},
\qquad
\text{ordered invariant coupling}+\text{polygon}\longrightarrow\bar d.
\]

This would prevent the article from looking like three unrelated notes bound together.

The following changes would materially reduce reader burden.

- Consolidate status labels into theorem headings and the three-item list in §6.4. Repeating **PROVED**, **DISPROVED**, and **INCOMPLETE** inside ordinary paragraphs reads like an audit log. The labels can be retained while reducing repetition.
- Add a conventional bibliography. A source register is valuable for auditability, but it is not a substitute for complete bibliographic entries in a mathematical article.
- Define once the three operator settings: arbitrary $\ell^2(W)$, single-orbit $R(\Gamma)$, and finite-type $M_S(R(\Gamma))$. Appendix C will then read as a controlled extension rather than a late change of trace convention.
- Keep the finite-type theorem in Appendix C unless it is advertised in the abstract. It is correct and useful, but it is not one of the four headline claims.
- Remove project-process prose and links to internal review files from the public mathematical article. A reproducibility statement may point to public supplementary scripts. AI pre-review status and internal source-register workflow belong in release metadata.

## Strongest possible rejection reasons

If submitted in its current form, the strongest objections would be:

1. **The variable-fiber Borel step is underproved.** A fixed-$W$ natural sampler does not automatically give a Borel graph factor over unlabelled random graphs. Section 4.2 has the right ingredients, but the bundle/descent statement should be formalized.
2. **The innovations proof is too compressed for the strength of Theorem A.** The history posterior, common filtration, and simultaneous countable Brownian conclusion need explicit lemmas and quantifiers.
3. **The explicit group-ring counterexample delegates an elementary but necessary numerical inequality to code.** The text should close that finite estimate itself.
4. **The article is not self-contained bibliographically.** The exact premises of Aldous--Lyons, BLPS, Li--Thom, Lyons--Steif, Lyons--Thom, Timár, Angel--Ray--Spinka, and Elek--Szabó should be visible in a conventional reference list.
5. **The contribution hierarchy is unusually broad.** Without a clear two-question spine and dependency diagram, a referee could regard the manuscript as a compilation rather than one paper.

The first two are repairable proof-exposition issues. I do not currently see a fatal mathematical error behind them. The last three are presentation and submission-readiness issues.

## Final disposition after repairs

Subject to a full specialist check of the stochastic filtering argument and the Borel bundle construction, I expect the manuscript to be mathematically viable after major revision. The FK interpolation, amenable optimality argument, tree counterexample, countable-sofic extension, and polygonal $\bar d$ proof are presented with the right quantifiers and theorem-source premises.

The paper should not claim novelty until a separate literature audit is complete, but absence of a novelty claim does not weaken its internal mathematics. My disposition is **major revision, then re-review**, rather than rejection for a detected false theorem.

## Post-repair review (2 October 2026)

I re-read the revised §§3.3–3.4 and 4.2 and Appendix B, together with the new dependency prose and bibliography. This addendum records the result without erasing the concerns that motivated the revision.

### Mathematical correctness

The three main proof-exposition objections in the initial report are now closed.

1. **The fixed-index sampler is now a genuinely parameterized Borel construction.** Section 3.3 specifies the compact standard Borel space of positive-contraction matrices and a Polish path space, and Proposition 3.2 states the jointly Borel solution map. The proof identifies the finite-window events used by the drift, checks parameter-dependent integration, and obtains the solution as a locally uniform Picard limit. This supplies the measurability that §4 needs rather than leaving it implicit in a pathwise ODE argument.

2. **The innovation argument now has the required filtration and null-set bookkeeping.** The three claims in §3.4 distinguish endpoint posteriors, full observation histories, and the common innovation filtration. In particular, the draft takes a \(dt\otimes d\mathbb P\)-null set for the time-integrated identity, uses only a countable intersection over sites, passes to one completed right-continuous filtration, and identifies every finite coordinate vector by its conditional characteristic function. I no longer see the quantifier gap raised in the initial report.

3. **The varying graph fiber is now constructed rather than asserted.** Lemma 4.1 works on a numbered marked representative, realizes the actual directed-arc fiber as a Borel subset of \(\mathscr B\times\mathbb N^2\), splits finite and infinite fibers, invokes the fixed-index sampler on the corresponding standard set, and then descends by naturality. The explicit warning that canonical renumbering need not preserve iid labels is valuable: the law is computed intrinsically on a fixed representative, while numbering is used only to prove measurability. This resolves the strongest graph-factor objection in the first report. The canonical-representative citation should point to Aldous–Lyons §2, printed p. 1461.

4. **Appendix B now contains its own exact estimate.** The geometric remainder identity explains the degree choice, and the binomial inequality proving \(20(19/20)^{256}<1/1024\) is elementary and exact. The accompanying calculation is now corroboration rather than a premise of the proof.

I also checked the promoted finite differential statement in Lemma 5.1. Its hypothesis is visible, the inverse-compression argument supplies that hypothesis along the constant-determinant path, and the draft explicitly covers complex Hermitian kernels. The conventional bibliography and the source-premise sentences remove the self-containment objection at the level expected of a research manuscript.

### Remaining minor corrections

- In §3.3, define the notation \(C_0([0,\infty),\mathbb R)\) explicitly as continuous paths *starting at zero*. In functional analysis the same symbol commonly means continuous functions vanishing at infinity, which Brownian paths do not satisfy. A notation such as \(C_{\mathrm{start}=0}\), or one defining sentence, removes the ambiguity.
- In formula (3.2), write the finite sum as \(\sum_{z\in E_n(x)}\). The present \(\sum_z\) is recoverable from context but needlessly makes the central drift formula harder to parse.
- For a public version, replace links to internal audit files with a stable public supplementary-data citation. This is an editorial publication issue and does not affect any theorem.
- The required status labels can remain. They would read more smoothly if concentrated in theorem headings and the summary table, but their presence is not a correctness or submission blocker.

### Revised disposition

From the perspective of a general probability and ergodic-theory referee, the repaired manuscript is **mathematically acceptable subject to minor revision**. I found no concrete false theorem in the revised interfaces. The earlier recommendation of major revision was driven by omitted measurable-selection, filtration, and exact-estimate bridges; those bridges are now present.

This judgment concerns internal correctness and readability, not priority. The manuscript appropriately makes no novelty claim, and any eventual priority statement should still rest on a separate literature review. The breadth of the paper remains unusual, but the dependency prose now gives the four results a navigable structure and no longer supplies a mathematical reason for rejection.

### Closure after the final minor edits

The final targeted edits close every remaining request in this addendum. Section 3.3 now defines \(C_0\) as continuous paths starting at zero, and both exponent sums in (3.2) explicitly range over \(E_n(x)\). Section 4.2 gives the corrected Aldous–Lyons page, records the preliminary Baire-space recoding, and explains the finite-graph numbering. The manuscript now uses its conventional bibliography and public source register in place of links to internal audit reports; the separately listed computations are clearly described as supplementary, non-certifying checks. The retained status labels implement an explicit editorial requirement and remain harmless.

No mathematical or readability correction from this review remains open. My final general-referee disposition is **accept**. This remains a judgment of internal correctness and exposition, not a novelty or priority certification.

## Editorial review of the normalized manuscript (2 October 2026)

I compared the revised manuscript with the preceding version and re-read the affected proofs. The revision materially improves the paper. The introduction now moves from the three probabilistic questions to the results and their proof mechanisms; the notation \(\mathbf P^Q\), \(Q_F\), \(\operatorname{FK}(Q)\), and \(\bar d\) is conventional and consistent; and §3 explains the observation–innovation construction before introducing the finite-window machinery. The separation of the Brownian-path solution \(\mathcal Z_K\), the path decoder \(\Psi_K\), and the uniform-label sampler \(\Phi_K\) is especially helpful.

The change in exposition has not weakened the main quantifiers. Theorem A remains a jointly Borel, everywhere-defined sampler on the prescribed countable set \(W\), natural under all bijections. Corollary A1 still gives one vertex-i.i.d. graph-factor rule for every locally finite connected simple rooted graph law, without unimodularity or a degree bound. Theorem B remains an ordinary stochastic-domination statement for every countable group. Theorem C still separates fixed-kernel equality on amenable groups from the \(C_3*C_3\) counterexamples, including the finite-support kernel with a gap at both endpoints. Theorem D still concerns invariant joinings on every countable sofic group. The revised proof roadmaps do not import the sampler into either comparison theorem, and the distinction between ordinary domination and invariant monotone coupling remains explicit.

Appendix D is an effective place for the required status labels. It makes the scope auditable without interrupting theorem statements and proofs. The introduction, §§3–4, and §6 now read as a mathematical article rather than a running verification record.

I found no remaining substantive readability obstacle. Three copyedits would remove the only residual points of friction:

1. In Appendix D, replace “Theorem C(1)” by “Theorem C, (C1)” or “the first assertion of Theorem C”; the theorem has no numbered part (1).
2. In §4.4, write “[ARS, Theorem 1.4, restated there as Theorem 4.1]” if both numbers refer to the Angel–Ray–Spinka paper. As written, “restated as Theorem 4.1” can be mistaken for a cross-reference to this manuscript's Lemma 4.1.
3. Rename §4 “Random rooted graphs and the free uniform spanning forest.” The current “free forest” is understandable but less precise than the terminology used everywhere else.

Subject to these copyedits, my editorial disposition is **accept**. This round assesses clarity, notation, tone, and preservation of the proved statements; it does not certify novelty or priority.

### Editorial closure

All three copyedits have been made, and the punctuation adjustment in the reverse-martingale paragraph preserves the sentence and estimate. No item from this editorial round remains open. The final editorial disposition is **accept**.
