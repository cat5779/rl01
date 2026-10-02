# Relative sparse completion of the product-group spanning forest

## Frozen benchmark target

Let Gamma=F(a,b) x F(c,d), and let G be its standard undirected Cayley graph with the eight symmetric generators a,b,c,d and their inverses. Let F have the free uniform spanning forest law on G. For this group beta_1^(2)(Gamma)=0 and FUSF=WUSF; the group and its free pmp actions have the known cost value 1. These facts are calibration, not new conclusions.

For every eta>0, prove or disprove the existence of a total Borel Gamma-equivariant map

\[
A_\eta:\{0,1\}^{E(G)}\times[0,1]^\Gamma
\longrightarrow\{0,1\}^{\binom\Gamma2}
\]

such that, given this prescribed sample F and independent regular iid labels U, the undirected graph F union A_eta(F,U) is connected almost surely and

\[
\frac12\mathbb E\deg_{A_\eta(F,U)\setminus F}(e)\le\eta.
\tag{RC}
\]

All vertices are retained and no edge of F may be deleted. Added edges may join arbitrary distinct group elements, not only neighbors in G; the budget counts edges, not their word length. Prove measurability and exact equivariance on every input, and finite expected added degree. Connectivity and the budget are required under the stated input law. An exceptional input may return no added edges. Do not replace this prescribed-forest relative problem by constructing an unrelated low-cost graphing or by showing cost(Gamma)=1.

The universal existence assertion in (RC) is the target. A failure of independent sprinkling, a fixed choice of short edges, a particular small-section criterion, or an imposed finite coding radius is not a disproof. A negative result must obstruct all allowed maps or establish a positive lower bound for the displayed infimum.

## Granted random-source interface

You may assume H77: each fixed invariant determinantal law on a finite collection of regular Gamma label orbits is a total Borel equivariant factor of regular iid. On this Cayley graph this supplies a regular iid realization of the FUSF. The current problem is stronger in a different direction: it takes a prescribed FUSF sample as input and uses only fresh independent iid in addition to it. Do not re-audit H77. Mark uses of it; the relative target itself is stated directly on the forest law.

## Known obstructions to account for

1. **Independent edge sprinkling fails.** BLPS, *Uniform spanning forests*, Theorem 13.7, proves that on a bounded-degree network with bounded conductances and spectral radius below one, WUSF union independent Bernoulli(p) nearest-neighbor edges has infinitely many components for sufficiently small p. Primary source: https://rdlyons.pages.iu.edu/pdf/usf.pdf . Apply its hypotheses carefully to G. Correlation with F and/or a genuinely different use of long edges is therefore essential to any proposed improvement over that construction. Do not spend the task reproving this known obstruction as if it were the new target.

2. **A previous small-section route is incomplete.** For a measured forest subrelation S of the Bernoulli orbit relation and an ambient generator phi, the intersection relation x E_phi y iff x S y and phi(x) S phi(y) can have finite classes. Thus one cannot simply assume that it has complete sections of arbitrarily small measure. In the product-group WUSF setting the finite-overlap estimate follows from the square-summable two-walk intersection kernel when the random-walk spectral radius is below one. Avoid taking a failed intersection criterion as a necessary condition for all sparse repair.

3. **Small degree perturbation does not preserve connectivity in weak limits.** Any approximation must prove final connectivity and keep control of incident edge mass over group labels. Local convergence alone is not enough.

4. **The exact and approximate targets differ.** An exact connected treeing at the Betti lower bound would impose much more than the eta>0 approximation here. Do not strengthen (RC) to zero added cost or exact attainment and then call the resulting obstruction a refutation of (RC).

## Suggested new direction

Try a correlated multiscale completion based on the commuting product directions, or a sharp variational/relative-cost argument that quantifies the obstruction for a prescribed forest. Long jumps and correlated marking are permitted. If using a complete section, prove the existence and measure of the needed section for the actual relation, and show the resulting partial maps generate all missing orbit connections. If using clusters or random representatives, ensure the selection is equivariant and no uniform representative of an infinite class is silently invoked.

The precise measured counterpart is the infimum cost of graphings Phi for which the join of the given forest subrelation S_F and R_Phi equals the full Bernoulli orbit relation, using the original unnormalized probability measure. Cost of the ambient relation, cost of S_F, and this relative infimum need not be interchangeable. Establish the exact implication used and consult primary sources before declaring the relative statement new or open.

## Connection to the larger question

The wider Lyons–Gaboriau goal is cost(Gamma)=1+beta_1^(2)(Gamma) for arbitrary infinite finitely generated groups. That general problem is not solved by treating this known-cost example. The purpose of (RC) is to test whether preserving a given FUSF while adding arbitrarily little cost can survive a concrete nonamenable product case where independent sprinkling fails. A positive construction should identify which product-specific property carries the proof and state a precise possible generalization without claiming it. A genuine negative theorem would retire this additive relative strategy on the benchmark while leaving other low-cost graphings available.

Return PROVED, DISPROVED or INCOMPLETE for (RC), with the complete mathematical argument and exact limitations. A new restricted theorem or method obstruction must be labeled separately and must not replace the frozen target. Keep group cost, Bernoulli-action cost, fixed price, invariant joint laws and relative iid constructions distinct.
