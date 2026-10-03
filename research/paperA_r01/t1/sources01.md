# Source register for the English mathematical draft

This register accompanies [paperA.md](paperA.md). It records originals actually opened, the premise checks used in the proofs, and the relation to existing project material. It is not a priority certificate. Searches and source checks were completed on 2 October 2026.

## Primary literature and exact uses

### [LT] Lyons–Thom

Russell Lyons and Andreas Thom, *Invariant coupling of determinantal measures on sofic groups*, Ergodic Theory and Dynamical Systems **36** (2016), 574–607, [published author PDF](https://rdlyons.pages.iu.edu/pdf/couple-pub.pdf), [DOI](https://doi.org/10.1017/etds.2014.70).

The published PDF was opened and compared with the [arXiv version](https://arxiv.org/pdf/1402.0969). References below use printed journal pages, not the additional PDF cover page.

- **p. 576:** measurable equivariant maps and product actions on both \(A^\Gamma\) and \(A^W\). This is the source convention for Theorem A. Arbitrary actions are allowed in the definition; theorems later in the paper have narrower hypotheses.
- **Theorem 2.1, p. 577:** ordered positive contractions on a finite index set give stochastic domination of their DPPs. This supplies the finite comparisons in §§2, 6 and 7 and Appendix B. Every use has Hermitian positivity, contraction bounds, and the required operator order. Countable extension is supplied separately by compactness; invariant coupling is not inferred from this theorem.
- **Lemma 3.4 and the following trace definition:** the finite-type commutant is the matrix algebra over the group commutant, with the sum trace over types. This checks the convention \(\tau_S(I)=|S|\) in Appendix C.
- **Theorem 5.1, p. 588:** a sofic group with a finite generating set, and ordered positive contractions in \(R(\Gamma)\) or \(R(\Gamma,S)\), admit an invariant monotone coupling. Section 7.1 checks these premises on each finitely generated subgroup and proves the extension to a countable sofic group. No non-sofic application is made.
- **pp. 593–594 and Lemma 7.2:** invariant joining distance, its triangle inequality via relatively independent joinings, and equality with the density difference in the ordered case.
- **Theorem 7.3 and Corollary 7.4, pp. 594–595:** finite generating set; regular or finite-type kernels; soficity for finitely dependent approximation, amenability for Bernoulli isomorphism. The draft preserves those historical premises.
- **Question 7.7, p. 595:** the Bernoulli-factor question. Theorem A answers it under the paper's broad product-action convention, including the narrower regular settings. It does not claim a regular-source representation for every stabilizer action.
- **After Lemma 7.8, p. 595:** the noncommutative trace-norm question is unnumbered. **Lemma 7.9** gives the weaker exponent-\(1/3\) estimate. The manuscript's Theorem D addresses this separate question on sofic groups. The finite-matrix discussion on p. 597 is also relevant precedent for the Hamming-cost formulation.

### [ICM] Lyons

Russell Lyons, *Determinantal probability: basic properties and conjectures*, Proceedings of the ICM 2014, Vol. IV, 137–161, [published author PDF](https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf).

Theorem 5.2 and the opening of §5.2, printed p. 157, give the abelian comparison background and the sofic context. Conjecture 5.7, printed p. 158, gives the FK sandwich and the optimality phrase. The phrase is not a formal definition of pointwise versus classwise optimality. The draft therefore distinguishes those readings instead of attributing a uniquely determined intention. The trace-distance paragraph near it is a different question.

The [author's errata](https://rdlyons.pages.iu.edu/errata/icm.pdf), dated 30 December 2025 in the opened document, were checked; no change to Conjecture 5.7 was listed there.

### [LS] Lyons–Steif

Russell Lyons and Jeffrey E. Steif, *Stationary determinantal processes: phase multiplicity, Bernoullicity, entropy, and domination*, Duke Mathematical Journal **120** (2003), 515–575, [author PDF](https://rdlyons.pages.iu.edu/pdf/dyn.pdf).

**Theorem 5.3** treats the one-dimensional ordinary stochastic parameters. **Theorem 5.11** gives the exact geometric-mean parameters for each measurable symbol on \(\mathbb Z^d\); this is a direct pointwise-optimality precedent. **Proposition 3.4** gives the commutative lattice \(\bar d\) bound by the integral of the absolute difference of the symbols. The stronger full-conditioning notions in Definition 5.15 and Theorem 5.16 are not substituted for ordinary stochastic order in the draft.

The [author's errata](https://rdlyons.pages.iu.edu/errata/dyn.pdf) were also opened. The correction concerning Remark 5.12 does not alter the stated use of Theorem 5.11.

### [LiT] Li–Thom

Hanfeng Li and Andreas Thom, *Entropy, Determinants, and \(L^2\)-Torsion*, Journal of the American Mathematical Society **27** (2014), 239–292, [original arXiv PDF](https://arxiv.org/pdf/1202.1213).

**Theorem 1.4**, p. 6 of the opened 60-page preprint, assumes a countable discrete amenable group and a positive element of \(M_d(\mathcal N\Gamma)\). It identifies its analytic FK determinant with the infimum of finite compression determinants to the power \(1/|F|\), and with the limit over increasingly left-invariant finite sets. The matrix trace has total mass \(d\). Neither injectivity nor integral coefficients are required. Singular elements and determinant zero are covered.

In §6.1, \(d=1\), \(g=Q\), and the group is explicitly amenable. In Appendix C, \(d=|S|\), and the trace is explicitly unnormalized. No entropy theorem, determinant conjecture, or invertibility assertion from this paper is used. Switching left and right regular conventions only relabels the finite sets in the infimum.

### [BLPS] Benjamini–Lyons–Peres–Schramm

Itai Benjamini, Russell Lyons, Yuval Peres and Oded Schramm, *Uniform Spanning Forests*, Annals of Probability **29** (2001), 1–65, [author PDF](https://rdlyons.pages.iu.edu/pdf/usf.pdf), opened version dated 1 June 2005. Page numbers in this register refer to that author version.

**Theorem 7.8** is the infinite-graph transfer-current formula. The following projection interpretation identifies FUSF with the orthogonal complement of finite cycle flows and WUSF with the closed star/gradient space. The graphs used in §4 are locally finite connected unit-conductance graphs; the regular trees in §6 are transient unit-conductance networks. Thus the stated network and Hilbert-space prerequisites are satisfied.

**§11, p. 48, proof of Theorem 11.1**, constructs independent parent-hitting percolation and couples its components inside WUSF components on a transient tree. On a tree, containment of connected components implies containment of its edges. The edge probabilities are \(h(v)/h(\hat v)\); on a regular tree of degree \(d\) they equal \(1/(d-1)\). The regular-tree paragraph on p. 46 uses degree \(d+1\) and parameter \(1/d\). This is a direct antecedent of the lower coupling in (6.4).

Theorem 11.1's displayed statement concerns ends and recurrence; the domination is in its proof. The English draft gives its own projection argument, then a determinant calculation for the matching upper restriction. It does not present the classical lower coupling as a new result, or claim that the exact-threshold formula has no older appearance.

### [Tim] Timár

Ádám Timár, *Factor of iid's through stochastic domination*, [arXiv:2306.15120v2](https://arxiv.org/abs/2306.15120v2), version of 16 December 2025, [original full text](https://arxiv.org/html/2306.15120v2), [PDF](https://arxiv.org/pdf/2306.15120v2).

The Introduction states the full-generality FUSF factor question. **§2** uses iid vertex labels and measurable automorphism-equivariant rules on fixed quasi-transitive graphs, followed by a local-prediction formulation for unimodular random graphs. The draft adopts [ARS]'s explicit Borel, rerooting-compatible graph-factor formulation, proves its implication to that operational formulation, and identifies the compatibility needed for a converse in Appendix A. It does not equate the definition with predictability at a single root in an arbitrary coupling.

**Theorem 1** treats recurrent unimodular random graphs. **Theorem 2(1)** treats invariantly amenable unimodular random graphs and gives the stronger finite-valued finitary conclusion. **Corollary 5** is part of the recurrent argument. These are prior special cases, with stronger coding conclusions in their stated range. Corollary A1 covers the simple-graph unimodular range and additionally arbitrary rooted laws, but claims neither finitary coding nor finitely many input bits. No extension to unmarked parallel-edge objects is asserted.

### [ARS] Angel–Ray–Spinka

Omer Angel, Gourab Ray and Yinon Spinka, *Uniform even subgraphs and graphical representations of Ising as factors of i.i.d.*, Electronic Journal of Probability **29** (2024), paper 39, [published PDF](https://dspace.library.uvic.ca/server/api/core/bitstreams/ec346c4f-76f7-4bb3-b54e-b95505de66de/content), [DOI](https://doi.org/10.1214/24-EJP1082).

**§2.1, printed pp. 6–7**, defines graph factors by Borel maps on marked rooted graphs with rerooting compatibility, and discusses vertex and edge marks. Unimodularity is not part of the graph-factor definition. Footnote 2 on p. 7 addresses representatives. **Theorem 1.4**, restated as **Theorem 4.1**, treats WUSF on transient connected random rooted graphs without imposing unimodularity. **Question 6.1** asks about recurrent unimodular graphs. These results do not by themselves provide the variable-graph Borel rule for FUSF used in this draft.

### [AL] Aldous–Lyons

David Aldous and Russell Lyons, *Processes on Unimodular Random Networks*, Electronic Journal of Probability **12** (2007), paper 54, 1454–1508, [published PDF mirror](https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/463/463-1495-1-PB.pdf), [DOI](https://doi.org/10.1214/EJP.v12-463).

**§2, printed p. 1461**, gives canonical numbered representatives for rooted networks; **Definition 2.1, p. 1462**, is the mass-transport definition of unimodularity. Numbered representatives are used only to check variable-graph measurability, not to choose the forest. The manuscript's naturality proof removes the numbering from the result. Appendix A uses mass transport only for its comparison of compatible local definitions, not to construct the graph factor.

### [ES] Elek–Szabó

Gábor Elek and Endre Szabó, *Sofic representations of amenable groups*, Proceedings of the American Mathematical Society **139** (2011), 4285–4291, [published PDF](https://www.ams.org/proc/2011-139-12/S0002-9939-2011-11222-X/S0002-9939-2011-11222-X.pdf), [arXiv record](https://arxiv.org/abs/1010.3424).

**Theorem 1** preserves soficity under amalgamated free products of sofic groups over amenable subgroups. Finite groups are sofic, and the trivial amalgamated subgroup is amenable, so the theorem applies to \(C_3*C_3\). It is used only to check that the counterexample lies within the ICM sofic context.

## Existing candidate arguments and what was rechecked

The recent project main PDF and updated candidate documents were inspected before choosing the manuscript statements. The table identifies the arguments used and the steps rechecked directly from their proofs.

| Candidate antecedent | Relation to the draft | Rechecked steps |
|---|---|---|
| [Public PR 85](https://github.com/cat5779/rl01/pull/85), prescribed-index DPP factor theorem | Theorem A and §3 | Finite tilted kernels, covariance row bound, canonical windows, total drift, Picard uniqueness, full observation posterior, common-filtration innovations, coordinate recovery and pointwise naturality |
| [Public PR 91](https://github.com/cat5779/rl01/pull/91), directed-double-cover interface | §4 | Arc isometry, two-directions exclusion, determinant pushforward; variable-graph Borel dependence and vertex-to-arc iid conversion supplied explicitly |
| *Bernoulli domination for invariant determinantal measures*, unpublished manuscript dated 27 September 2026 | Theorem B and §5 | Schur-complement conditional odds, inclusion-basis derivative identity, constant-FK interpolation, inverse compression, singular limits and complementation |
| [Public PR 93](https://github.com/cat5779/rl01/pull/93), pointwise thresholds and amenable boundary | Theorem C, §6 and Appendix B | Tree projection and regular edge action, conditional lower probabilities, determinant upper restriction, FK spectral masses, affine perturbation, explicit finite-support error margin |
| *Invariant Couplings and the Optimal Trace-Norm Bound for Determinantal Processes* (source title: 行列式过程的不变耦合与最优迹范数界), unpublished manuscript dated 27 September 2026 | Theorem D and §7 | Original mathematical PDF and TeX compared; polygon contraction bounds, trace cost, invariant gluing, exact scope of the published ordered-coupling input; countable-group extension written out |

[Public PR 92](https://github.com/cat5779/rl01/pull/92) contains an additional common-iid FK coupling route. It was inspected, but the ordinary domination proof in this manuscript does not depend on its stronger coupling conclusion. Similarly, no arbitrary-group birth-process coupling claim from the trace-norm source is imported into Theorem D.

## Searches and their limits

The literature check used the original PDFs above, their available errata, arXiv and journal/author pages, and web searches including:

- `free uniform spanning forest graph factor iid`, `FUSF factor iid Timar`;
- `Lyons Conjecture 5.7 Fuglede Kadison`, `Bernoulli domination Fuglede Kadison determinantal`;
- `stationary determinantal geometric mean domination`, `amenable finite compression determinant`;
- `wired spanning forest Bernoulli domination regular tree`;
- `determinantal trace norm coupling`, `determinantal bar d trace bound`, `determinantal Wasserstein trace norm`.

Search snippets were used to locate originals, not to establish claims. The direct tree-domination antecedent found and checked is BLPS §11. The commutative sharp comparisons and trace bound were checked in Lyons–Steif, and the amenable determinant theorem in Li–Thom. The broader fiid, FK and polygonal arguments were already present in the supplied project candidates and are presented as a consolidation and verification of those materials.

No exhaustive forward-citation search, MathSciNet/Zentralblatt audit, or human specialist literature certification was completed. The absence of another matching result from this search is not evidence of its absence from the literature. Novelty and priority remain **INCOMPLETE / NOT CLAIMED**.

## Review provenance

Three separate GPT-5.6 Sol instances, each at xhigh reasoning effort, read the mathematical material independently of the earlier review verdicts. They covered [probability-specialist scrutiny](../t2/prob01.md) of Question 7.7 and the counterexamples, the [sofic polygon proof](../t2/dbar01.md), and [general probability/ergodic-theory readability](read01.md). The root instance synthesized the English proof; the completed synthesis received a second reading from the independent instances. The readability review prompted expanded proofs of measurable dependence, innovations, and variable graph fibers, and a script-independent error estimate; those revisions were reviewed again. These are AI pre-reviews, not external referee reports.
