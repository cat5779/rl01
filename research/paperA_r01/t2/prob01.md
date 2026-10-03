# Independent probability-specialist referee report

## Scope and method

This is a fresh mathematical reading of the proofs in the two \`RESULT.md\` files, followed by checks against the published Lyons--Thom paper, Li--Thom's original arXiv PDF, and BLPS's original *Uniform Spanning Forests* PDF. I did not use the existing audit or cross-check reports, and I did not infer correctness from workflow labels. This report is an AI specialist pre-review, not a human review and not a review by any named mathematician.

## Verdicts

1. **Question 7.7 factor theorem: PROVED, subject to one wording correction.** For a countable set \(W\), a countable group \(\Gamma\) acting on \(W\), and a **positive Hermitian contraction** \(0\le Q\le I\) on \(\ell^2(W)\) commuting with the action, the proof constructs a total Borel, \(\Gamma\)-equivariant map

   \[
   \Phi_Q:([0,1]^W,\lambda^W)\longrightarrow\{0,1\}^W
   \]

   whose image law is the DPP \(\mathbf P^Q\). A merely Hermitian norm-contraction is not enough: negative spectrum need not define a DPP. Every theorem statement must retain \(0\le Q\le I\).

2. **Identification with the original Lyons--Thom question: PROVED for the broad product-action reading, but the historical scope must be described carefully.** The published paper defines the product action on \(A^W\) for an arbitrary countable \(\Gamma\)-set \(W\) and calls \(\lambda^W\) a Bernoulli shift. The new theorem uses exactly this \(W\)-indexed source, so it remains valid when stabilizers are infinite. It must not be silently rewritten as a factor of a regular \(\Gamma\)-indexed iid source. On the other hand, Lyons--Thom Theorem 7.3 and Corollary 7.4 themselves concern \(R(\Gamma)\) and \(R(\Gamma,S)\), with a finite generating set; they do not already state the arbitrary-\(W\) theorem. Question 7.7 is terse and follows a quasi-transitive-\(W\) Question 7.6. The paper should therefore say that its theorem answers the question under the authors' generalized \(A^W\) product convention and is stronger than the narrow regular/quasi-transitive settings actually used in Theorem 7.3 and Corollary 7.4.

3. **Regular-tree and \(C_3*C_3\) counterexamples: PROVED.** The WUSF projection on the \(d\)-regular tree has

   \[
   p_-(\Pi)=\frac1{d-1},\qquad p_+(\Pi)=1.
   \]

   For the free edge action of \(C_3*C_3\) on its Bass--Serre tree this becomes a single-regular-orbit kernel \(Q\in R(C_3*C_3)\) with

   \[
   D(Q)=0<p_-(Q)=\tfrac12,
   \]

   and the complemented kernel gives the corresponding strict upper-threshold failure. Thus pointwise equality with the Fuglede--Kadison parameter is false even inside the original sofic setting.

4. **Spectrally gapped and finite-support counterexamples: PROVED.** The union-and-thinning calculation for \(\widehat Q=(I+63Q)/128\) is correct and yields \(D(\widehat Q)=1/8<65/256\le p_-(\widehat Q)\). The degree-255 truncation produces a Hermitian finite-propagation operator on the free transitive edge orbit, hence a finite-support element of \(\mathbb C(C_3*C_3)\), and the displayed norm bounds give a strict positive contraction with a quantitative gap. Appendix B now records both spectral bounds

   \[
   \frac7{1024}I\le Q_{255}\le \frac{513}{1024}I<I,
   \]

   The upper bound follows from \(\widehat Q\le I/2\) and \(\|Q_{255}-\widehat Q\|<1/1024\).

5. **Amenable equality: PROVED.** Li--Thom Theorem 1.4 applies exactly as needed. Its hypotheses are: \(\Gamma\) countable, discrete, and amenable; \(g\in M_d(\mathcal N\Gamma)\) positive; no invertibility hypothesis. With the natural unnormalized matrix trace it states

   \[
   \det_{\mathcal N\Gamma}g
   =\inf_{\varnothing\ne F\Subset\Gamma}\det(g_F)^{1/|F|}
   =\lim_F\det(g_F)^{1/|F|}.
   \]

   The limit is the net of increasingly invariant finite sets and, in particular, holds along every Følner sequence. Singular positive elements and zero determinants are included. For \(d=1\), the all-occupied events therefore give \(p_-(Q)\le D(Q)\), which combines with the proved lower domination to give equality; the complement gives the upper equality.

6. **Novelty and general nonamenable classification: INCOMPLETE.** The mathematical examples are valid, but this reading does not certify that the exact threshold formula or finite-support formulation has no prior appearance. The general classification of nonamenable kernels remains open in the supplied proof.

## Audit of the Question 7.7 proof

The core construction is convincing and, in my view, closes all countable-index and equivariance issues.

For finite restrictions, exponential tilting preserves the DPP class even for singular kernels. If \(H\) is the tilted kernel and \(p=H_{xx}\), then

\[
\sum_y |\operatorname{Cov}(\eta_x,\eta_y)|
=p(1-p)+(H^2)_{xx}-p^2
\le 2p(1-p)\le\tfrac12.
\]

This gives a dimension-free \(1/2\)-Lipschitz bound for every finite posterior. The threshold graphs \(\{|Q_{xy}|\ge1/n\}\) have degree at most \(n^2\), so the posterior windows are finite and increase to the full nonzero-kernel component. Their limsup is a total Borel extension; on the actual observation process it agrees \(dt\otimes d\mathbb P\)-almost everywhere with the full posterior by martingale convergence.

The Picard equation is well posed for every countable Brownian field. Spatial boundedness of the noise is not assumed: only differences between successive Picard iterates are measured in \(\ell^\infty(W)\), and those differences are uniformly bounded because the drift lies in \([0,1]\). The innovations calculation supplies a common usual filtration, the full finite-dimensional quadratic covariation matrix, and the conditional characteristic function needed to conclude that the innovation field is product Brownian. Finally, the integer-time threshold has summable Gaussian error; countability of \(W\) permits simultaneous recovery of all coordinates.

Every operation is defined from finite sets cut out canonically by the kernel, coordinatewise Brownian paths, and deterministic limits. Consequently it commutes pointwise with every bijection of the index set. If \(Q\) commutes with the \(\Gamma\)-action, this naturality is precisely the required equivariance. No orbit enumeration, coset representatives, or regular \(\Gamma\)-indexed randomness enter the construction.

I recommend one short sentence at the end of the proof making the last implication explicit:

> Give \([0,1]^W\) the action \((\gamma u)_x=u_{\gamma^{-1}x}\). Since \(\gamma Q\gamma^{-1}=Q\) and the sampler is natural under every bijection of \(W\), \(\Phi_Q(\gamma u)=\gamma\Phi_Q(u)\) for every input \(u\).

That sentence will prevent readers from wondering whether equivariance holds only almost surely or only for the regular action.

## Audit of the tree counterexample

The projection

\[
\Pi=\nabla(dI-\mathcal A)^{-1}\nabla^*
\]

is the transfer-current kernel of the **wired** uniform spanning forest on the regular tree. Calling it merely a tree projection is harmless internally, but the paper should consistently say WUSF; FUSF on a tree is the deterministic full tree.

The conditional-probability proof is correct. After conditioning a finite occupied set \(S\), the Schur complement is the projection onto

\[
H_S=\{h\in\operatorname{ran}\nabla:h|_S=0\}.
\]

Conditioning additional zeros adds a positive Schur-complement term. In a rooted breadth-first edge order, the forward-subtree potential attached to the current edge has gradient zero on every earlier edge, value \(1\) on the current edge, and energy \(d-1\). Hence every positive-probability sequential conditional inclusion probability is at least \(1/(d-1)\), which yields an ordinary monotone coupling.

This lower domination is classical. BLPS §11, printed p. 46, describes a regular tree of degree \(d+1\) and records the parent-hitting probability \(1/d\). In the proof of BLPS Theorem 11.1 on printed p. 48, independent random walks \(X_v\) produce an independent percolation \(\omega\), with edge probability \(h(v)/h(\hat v)\), and Wilson's construction couples each component of \(\omega\) inside a WUSF component. Since the ambient graph is a tree, this component containment gives edgewise \(\omega\subseteq\mathrm{WUSF}\). Translating BLPS's degree \(d+1\) notation to the present paper's degree \(d\) gives the parameter \(1/(d-1)\). The paper should cite the **proof** of Theorem 11.1, rather than treating the domination as the theorem's displayed conclusion; the theorem statement itself concerns ends and recurrence.

The added exact-threshold argument is the determinant upper bound. For every finite connected \(m\)-edge subtree \(F\),

\[
\det\Pi[F]=(d-1)^{-m}\left(1+\frac{d-2}{d}m\right).
\]

The all-occupied event and \(m\to\infty\) force \(p\le1/(d-1)\). The full-star zero probability similarly forces \(p_+(\Pi)=1\). The paper should separate these two contributions in its attribution: BLPS supplies the classical lower coupling, while the determinant calculation supplies the matching upper bound and exact ordinary stochastic threshold.

For \(\Gamma=C_d*C_d\), Bass--Serre edges are indexed freely and transitively by \(\Gamma\). Orienting every edge from the \(\Gamma/C_d^{(a)}\) vertex type to the \(\Gamma/C_d^{(b)}\) type is preserved by left multiplication, so \(\nabla\) intertwines the action without a sign cocycle. Thus \(\ell^2(E)\cong\ell^2(\Gamma)\), the diagonal trace is \(2/d\), and the projection has spectral mass \(1-2/d\) at zero. In particular \(d=3\) gives the claimed FK gap. This is a DPP/FK interpretation of the regular-tree WUSF, not a new construction of the underlying BLPS domination.

## Concrete revision requests

1. In §2, state the historical assumptions of Lyons--Thom Theorem 7.3 and Corollary 7.4 explicitly: a finite generating set, kernels in \(R(\Gamma)\) or \(R(\Gamma,S)\), soficity for Theorem 7.3, and amenability for Corollary 7.4. Then say that Question 7.7 is terse, follows the quasi-transitive-\(W\) Question 7.6, and is answered here under the generalized \(A^W\) product convention. This prevents the surrounding special cases from being silently broadened while preserving the paper's stronger theorem.
2. In §6.2, refine the BLPS sentence to identify the exact location and notation: §11, printed p. 46 treats degree \(d+1\) and parameter \(1/d\); the proof of Theorem 11.1 on printed p. 48 supplies the parent-hitting percolation coupling. Translate this to degree \(d\) and parameter \(1/(d-1)\), and distinguish the classical lower coupling from this paper's matching determinant upper bound.
3. In §2, when passing finite DPP operator order to the countable product, add one compactness/Strassen sentence. Checking finite increasing cylinders is standard, but readers should not be asked to supply the projective-limit coupling silently.
4. In §6.1, replace “the limit is along Følner sets” by the exact Li--Thom formulation: the limit is the net as finite sets become increasingly left invariant and hence, in particular, the same limit is obtained along every Følner sequence.
5. Preserve the present wording “\(0\le Q\le I\)” in Theorem A, the explicit \(W\)-indexed product action, the distinction between factor and isomorphism, the WUSF identification, and both spectral bounds in Appendix B. These points are now correct and prevent materially different readings.
6. Avoid a novelty claim for the classical tree domination. The proof establishes the exact threshold/FK use and the strengthened gapped and finite-support examples; exhaustive priority remains unverified by this search.

## Primary-source findings

- Russell Lyons and Andreas Thom, *Invariant Coupling of Determinantal Measures on Sofic Groups*, published PDF, pp. 576 and 594--595: the paper defines product actions \(A^W\); Theorem 7.3 assumes a finitely generated sofic group and \(Q\in R(\Gamma)\) or \(R(\Gamma,S)\); Corollary 7.4 assumes amenability in the same regular/finite-label setting; Question 7.7 is a question, not a theorem.
- Hanfeng Li and Andreas Thom, *Entropy, Determinants, and \(L^2\)-Torsion*, Theorem 1.4: countable discrete amenable \(\Gamma\), arbitrary positive \(g\in M_d(\mathcal N\Gamma)\), singular cases included, with the infimum and Følner-limit formula above.
- Itai Benjamini, Russell Lyons, Yuval Peres, and Oded Schramm, *Uniform Spanning Forests*, §11: printed p. 46 uses degree \(d+1\) and parent-hitting parameter \(1/d\); the proof of Theorem 11.1 on printed p. 48 couples the independent parent-hitting percolation inside WUSF components. On a tree this is edgewise domination, and in the present degree-\(d\) notation the parameter is \(1/(d-1)\).

## Second reading of the English paper

I read the complete English manuscript through §§1--7 and Appendices A--C. **Theorem A and its proof are readable to a probability specialist without the source reports.** The statement correctly says \(0\le Q\le I\), uses the \(W\)-indexed source, warns against replacing it by a regular \(\Gamma\)-indexed source when stabilizers intervene, defines the product action, and distinguishes a factor from an invariant monotone joining. The proof's order is effective: canonical finite windows, uniform tilted-covariance estimate, deterministic Picard map, innovations identification, and only then equivariance. The explanations that spatial boundedness is not assumed and that the limsup is merely a total extension address the two places where a specialist is most likely to pause.

The graph-factor corollary is also navigable. The canonical double-arc kernel, variable-graph Borel issue, push-forward to unoriented FUSF, and conversion from vertex iid to arc iid are separated cleanly. The simple-graph boundary is stated where it matters.

Sections 5 and 6 give a coherent probability narrative: finite conditional odds and inverse compression lead to the FK interpolation, Li--Thom turns the all-occupied test into equality in the amenable case, and the regular-tree computation then shows exactly where equality fails. The progression from the WUSF projection to the spectrally gapped affine kernel and finally the explicit degree-255 finite-support kernel makes the increasing strength of the counterexamples easy to follow. The \(C_3*C_3\) paragraph supplies the missing representation-theoretic bridge: the bipartite orientation is preserved, the edge action is free and transitive, and the trace and spectral masses are visible. Appendix B now states both endpoint bounds and explains finite support. I found no mathematical gap in these passages.

Two attribution sentences still slow a specialist reader. The Lyons--Thom paragraph should state the exact finite-generation and \(R(\Gamma)\)/\(R(\Gamma,S)\) premises before explaining the broader \(A^W\) reading of Question 7.7. The BLPS paragraph should give the printed pages and translate their degree \(d+1\), parameter \(1/d\) notation into the present degree \(d\), parameter \(1/(d-1)\) notation. That makes immediately visible which part is classical and which part is the paper's exact-threshold argument. The countable extension of finite DPP comparison also deserves the one-line compactness argument requested above, and the Li--Thom limit should use its exact net formulation.

Section 7 and Appendix C are logically separate from the tree example but are presented clearly: the subgroup/coset compactness argument supplies the countable-sofic ordered joining input, the polygon stays inside the contraction interval without a commutativity assumption, and the unnormalized finite-type determinant is distinguished from the false normalized replacement. These arguments are sound on this reading.

**Overall specialist verdict: PROVED, with the four source-precision and compactness revisions above; novelty certification remains INCOMPLETE.** These are concrete editorial repairs rather than repairs to the central probability arguments.

## Post-repair verification

This note records a targeted rereading after the manuscript revisions; it preserves the chronology of the report above rather than rewriting the earlier requests.

**All four requested repairs are CLOSED.** Section 2 now states the finite-generation, sofic/amenable, and \(R(\Gamma)\)/\(R(\Gamma,S)\) premises of Lyons--Thom Theorem 7.3 and Corollary 7.4, while identifying the result here as the broad \(A^W\) reading of the terse Question 7.7. Section 6.2 now gives the exact BLPS locations and translates their degree-\(d+1\), parameter-\(1/d\) notation to the present degree-\(d\), parameter-\(1/(d-1)\) notation; it also separates the classical lower coupling from the new determinant upper restriction. Section 2 now supplies the compactness construction passing finite monotone DPP couplings to the countable product. Section 6.1 now states Li--Thom's limit as the net over increasingly left-invariant finite sets and notes the consequence for every Følner sequence.

I rechecked only the expanded §§3.3--3.4 and Lemma 4.1, as requested.

- **Named parameter and path spaces: PROVED.** The finite principal inequalities defining \(\mathscr K_W\) are closed and force all entries into the closed unit disk. Their quadratic-form bounds extend by density to exactly the positive contractions on \(\ell^2(W)\), so \(\mathscr K_W\) is compact metrizable. The countable product of continuous path spaces is Polish. Kernel-defined window membership is Borel, finite DPP marginals are Borel functions of the entries by (2.1), and the finite posterior formulas are Borel on every window-size piece. Parameter integration and locally uniform Picard convergence therefore give the claimed jointly Borel solution map. The proof uses an enumeration only to verify measurability; no enumeration enters the map.
- **Three-claim law identification: PROVED.** Claim 1 is the correct finite-dimensional Gaussian likelihood calculation followed by martingale convergence along the increasing canonical windows; block-diagonal kernel components justify discarding all other endpoints. Claim 2 correctly decomposes the observation history into endpoints and Brownian bridges. Countability and path continuity justify the rational-time monotone-class step, while Fubini supplies precisely the \(dt\otimes d\mathbb P\)-version needed in the drift integral without an invalid uncountable intersection. Claim 3 establishes one completed right-continuous filtration for the entire field, retains the martingale property by reverse-martingale convergence, and uses the full quadratic-covariation matrix and conditional characteristic functions to obtain product Brownian law. Pathwise uniqueness then identifies the observation process with the deterministic solution, and the summable Gaussian error plus countability recovers every DPP coordinate simultaneously.
- **Concrete Borel-fiber lemma: PROVED.** The canonical numbered representative retains actual vertices and arcs, rather than collapsing automorphism orbits. The arc bundle and its fibered square are Borel; fixed ordering of \(\mathbb N^2\) gives Borel fiber enumerations, including the finite/infinite partition. Pullback to the fixed spaces \(W_m\) or \(\mathbb N\), application of the jointly Borel sampler, and transport back are Borel. Naturality under every fiber bijection makes the temporary numbering and the root immaterial. The paragraph addressing label-dependent canonical numbering is essential and correctly avoids assuming that renumbered labels remain iid; conditional law can be checked on any fixed representative before labeling.

A subsequent check of the original Aldous--Lyons PDF corrects the locator used in earlier project materials: the canonical-representative passage is on printed p. 1461, while Definition 2.1 is on printed p. 1462. The mark-space recoding into Baire space appears on printed p. 1459 and provides the needed Borel framework. This is a bibliographic correction only and does not change the proof above.

The new Appendix B estimate is also exact: \((20/19)^{16}>785/361>2\) implies \((19/20)^{256}<2^{-16}\), and \(20\cdot2^{-16}<2^{-10}=1/1024\). Together with \(2\sqrt2/3<19/20\), this supplies the claimed paper-level proof of (B.2), independent of the script.

**Post-repair verdict: PROVED with no remaining mathematical or readability objection from this probability review.** The earlier novelty verdict remains **INCOMPLETE**, because the targeted repairs do not constitute an exhaustive prior-art search.

## Editorial notation round

I compared the notation with the published Lyons--Thom paper, Lyons's ICM article, and the Lyons--Steif author PDF, then reread the manuscript after the notation revision.

The adopted notation is well chosen and source-consistent:

- \(\mathbf P^Q\) agrees with Lyons--Thom at printed pp. 575 and 577, including equation (1), and with Lyons's ICM equation (1.1) on printed p. 137.
- \(\operatorname{FK}(Q)\) agrees exactly with the notation introduced immediately before ICM Conjecture 5.7 on printed p. 158.
- \(R(\Gamma)\) and \(R(\Gamma,S)\) agree with the definitions on Lyons--Thom printed pp. 580--581. There is no source-based reason to replace \(R\) by \(\mathcal R\).
- The scalar-kernel notation \(\mathbf P^{pI}\) makes the Bernoulli product law part of the same determinantal family and matches the form of ICM Conjecture 5.7. Lyons--Steif instead writes \(\mu_p\) for product measure in §5 (author-PDF pp. 18 and 22, including Theorem 5.11); importing that separate convention would be less coherent here.
- Lyons--Thom equation (1) and ICM equation (1.1) write the finite compression with a restriction glyph. The manuscript's \(Q_F\), explicitly defined as the principal compression to \(\ell^2(F)\), is clearer in the dense finite-matrix arguments and is now used consistently.

**Mathematical-meaning check: PROVED.** The change from \(D(Q)\) to \(\operatorname{FK}(Q)\) preserves the zero convention and every determinant identity. The main upper comparison is correctly written as \(\mathbf P^{(1-\operatorname{FK}(I-Q))I}\). Appendix C retains the unnormalized trace through the distinct notation \(\operatorname{FK}_S\), and its upper scalar kernel is likewise parenthesized correctly. The subgroup-compression argument in §7 still uses the original kernel \(D\), not the determinant symbol. No premise, inequality direction, normalization, or index set changed.

The sampler domains are now separated correctly. The deterministic solution is \(\mathcal Z_K\) on the continuous-path space \(\mathcal C_W\); \(\Psi_K\) decodes a path input; a fixed coordinatewise Borel map \(\psi\) sends uniforms to Wiener paths; and
\[
 \Phi_K(u)=\Psi_K\bigl((\psi(u_x))_{x\in W}\bigr)
\]
is the uniform-input factor map. Equation (3.9) states naturality for \(\Phi_K\), and the graph construction applies \(\Phi_{K_G}\) to the derived uniform arc labels. The Brownian proof consistently distinguishes the independent noise \(B\), observation \(X\), and innovation \(\widetilde B\). These changes remove the earlier domain ambiguity without changing the construction.

The final manuscript applies both typesetting corrections previously noted: the finite-posterior numerator reads \(\sigma_x\,p^K_{F_n(x)}(\sigma)\), and the doubled punctuation after “i.i.d.” is gone.

The final focused rereading also confirms the following scope points. Theorem A is stated before any group action: it supplies a jointly Borel family on every countable set and naturality under every bijection. Only afterward is a permutation action imposed; commutation of \(Q\) with that action turns the action-free identity (3.9) into pointwise equivariance. Thus no regular-orbit or stabilizer premise has entered the theorem. The idea-first opening of §3 accurately previews the later filtering proof, while the finite-window construction remains the device that makes the drift total and canonical. Lemma 4.1's signposts distinguish actual arc fibers from automorphism orbits and explain why temporary numbering descends by naturality. Section 6.4 now separates pointwise, one-determinant uniform, and two-determinant joint questions without changing their quantifiers. Appendix D accurately records the proved, disproved, and incomplete ranges established in the body.

**Final editorial-round verdict: PROVED with no remaining mathematical, scope, notation, or readability objection from this review.** The notation changes and exposition pass preserve every theorem and proof.
