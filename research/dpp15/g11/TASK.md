# Dimension-free positive DPP birth-flow selectors for every fixed support bound

## Frozen theorem

Fix \(0<\varepsilon<1/2\) and an integer \(s\ge1\). For every finite coordinate set \(E\), every Hermitian kernel
\[
\varepsilon I\preceq K\preceq(1-\varepsilon)I,
\]
and every rank-one projector \(P\) with \(|\operatorname{supp}P|\le s\), let \(\mathcal F_E(K,P)\) be the full polytope of nonnegative upward Boolean-cube edge flows with divergence \(b_{K,P}\), total mass one, and outgoing capacity
\[
F_{\rm out}(S)\le (2/\varepsilon)p_K(S).
\]

Prove or disprove that there is a Borel, coordinate-permutation-equivariant selector
\[
(K,P)\longmapsto F_{K,P}\in\mathcal F_E(K,P)
\]
and a finite constant \(C_{\varepsilon,s}\), independent of \(|E|\), such that
\[
\|F_{K,P}-F_{L,Q}\|_1
\le C_{\varepsilon,s}
\bigl(\|K-L\|_1+\|P-Q\|_1\bigr)
\tag{DFS}
\]
whenever both directions have support at most \(s\).

## Audited input

For support at most three this is proved by choosing the unique least-Euclidean-norm point of the entire original fiber. The proof establishes:

1. exact conditioning/product decomposition over every coordinate set \(J\supseteq\operatorname{supp}P\);
2. compatibility of the same global least-norm selector across all support strata;
3. a fixed-normal-matrix least-norm Lipschitz lemma for feasible polyhedra;
4. dimension-free conditional-kernel stability;
5. comparison of two directions on \(J=\operatorname{supp}P\cup\operatorname{supp}Q\), whose size is at most six.

## Exact new obligation

Close the quantifier “for every fixed \(s\)”. A positive proof must give a finite explicit or exactly defined \(C_{\varepsilon,s}\), prove the cube inequality matrix on at most \(2s\) coordinates has a finite uniform active-set constant, and then re-check exact product compatibility, Borel dependence, permutation covariance, zero-coordinate degeneration, and simultaneous variation of \(K,P\). The selector must be one global choice; \(J\) may be pair-dependent only inside the estimate.

No constant uniform in \(s\) is requested. Do not claim the unrestricted arbitrary-support theorem. Do not divide by the least DPP atom, and do not infer a selector merely from pairwise Hausdorff stability.

A negative answer must give a genuine fixed finite \(s\) for which every such selector fails.

Return exactly PROVED or DISPROVED, followed by a complete supporting argument.



