# Dimension-free positive selector on the canonical matching-block class

## Frozen theorem

Fix \(0<\varepsilon<1/2\). For a finite coordinate set \(E\), let
\(\mathcal M_E^\varepsilon\) consist of Hermitian kernels \(K\) satisfying
\[
\varepsilon I\preceq K\preceq(1-\varepsilon)I
\]
such that every connected component of the coordinate graph
\[
G_K=(E,\{\{i,j\}:i\ne j,\ K_{ij}\ne0\})
\]
has size at most two. Thus every \(K\in\mathcal M_E^\varepsilon\) is a direct sum of one- and two-coordinate blocks, but its canonical component partition is part of \(K\) and may change when \(K\) changes.

For a rank-one projector \(P\), let \(\mathcal F_E(K,P)\) be the full nonnegative upward DPP birth-flow fiber with exact divergence \(b_{K,P}\), total edge mass one, and pointwise outgoing capacity
\[
F_{\rm out}(S)\le (2/\varepsilon)p_K(S).
\]

Prove or disprove that there are Borel, coordinate-permutation-equivariant selectors
\[
\Psi_E(K,P)\in\mathcal F_E(K,P)
\]
and a finite constant \(C_\varepsilon\), independent of \(|E|\), such that
\[
\|\Psi_E(K,P)-\Psi_E(L,Q)\|_1
\le C_\varepsilon\bigl(\|K-L\|_1+\|P-Q\|_1\bigr)
\tag{MATCH}
\]
for all \(K,L\in\mathcal M_E^\varepsilon\) and all rank-one projectors \(P,Q\). No common block partition for \(K\) and \(L\) is supplied or assumed.

## Audited input and exact boundary

1. If one common partition into blocks of size at most \(r\) is supplied and both kernels are block diagonal over it, an explicit selector with a dimension-free constant \(C_{\varepsilon,r}\) is proved. The proof decomposes the derivative by that fixed partition and uses weighted local selectors.
2. For diagonal kernels, an explicit arbitrary-support selector with universal constant two is proved. Hence merely letting an off-diagonal entry tend to zero does not by itself establish discontinuity of every selector.
3. The whole flow fiber is not dimension-free Hausdorff stable, and the global least-Euclidean-norm selector is not support-uniform. Neither fact alone disproves (MATCH).
4. Two canonical matching partitions can be incompatible: the union of their two matchings can have components of unbounded size. Therefore the supplied-common-partition theorem cannot simply be invoked with a bounded common coarsening.

## Exact obligations

A positive proof must give one selector on the entire class \(\mathcal M_E^\varepsilon\), prove exact divergence, positivity, unit mass, the original capacity, Borel dependence and full coordinate-permutation covariance, and control simultaneous changes of \(K,L,P,Q\) even when canonical one/two-block partitions change incompatibly. It may use the fixed-partition block construction locally, but must prove the missing cross-partition estimate without a factor depending on the number of blocks or on \(|E|\).

A negative proof must be selector-independent: construct admissible matching-block pairs whose positive fibers, together with permutation-equivariance if used, rule out every dimension-free Lipschitz section. Discontinuity of the canonical block formula, instability of a circulation, failure of whole-fiber Hausdorff stability, or the known least-norm counterexample is insufficient unless upgraded to an obstruction for all selectors.

Classify the conclusion only for this canonical one/two-block class. Do not claim the unrestricted non-diagonal theorem, exact JO, or a process construction.

Return exactly PROVED or DISPROVED, followed by a complete supporting argument.
