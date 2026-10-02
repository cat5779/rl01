# Dimension-free positive selector on the commuting kernel-direction class

## Frozen theorem

Fix \(0<\varepsilon<1/2\). For every finite coordinate set \(E\), let
\[
\mathcal C_E^\varepsilon
=
\left\{(K,P):
\varepsilon I\preceq K\preceq(1-\varepsilon)I,
\ P\text{ rank-one projector},
\ KP=PK
\right\}.
\]
For \((K,P)\in\mathcal C_E^\varepsilon\), let \(\mathcal F_E(K,P)\) be the full nonnegative upward DPP birth-flow fiber with exact divergence \(b_{K,P}\), total mass one, and outgoing capacity
\[
F_{\rm out}(S)\le (2/\varepsilon)p_K(S).
\]

Prove or disprove that there are Borel, coordinate-permutation-equivariant selectors
\[
\Psi_E(K,P)\in\mathcal F_E(K,P)
\]
and a finite constant \(C_\varepsilon\), independent of \(|E|\) and of \(|\operatorname{supp}P|\), such that
\[
\|\Psi_E(K,P)-\Psi_E(L,Q)\|_1
\le
C_\varepsilon\bigl(\|K-L\|_1+\|P-Q\|_1\bigr)
\tag{COM}
\]
whenever both pairs lie in \(\mathcal C_E^\varepsilon\).

The selector need not be the least-Euclidean-norm point.

## Audited input and exact boundary

1. The global least-Euclidean-norm selector fails every support-uniform bound, already at a scalar kernel \(K=pI\): an explicit full-support family has output/input ratio at least \(c_\varepsilon\sqrt{|E|}\). This rules out that method, not the existence of another selector.
2. At every scalar kernel \(pI\), the explicit rule
   \[
   F_{pI,P}(S,i)=P_{ii}p_{(pI)_{E\setminus\{i\}}}(S)
   \]
   is a positive stable selector with constant one in \(P\). Hence the least-norm counterexample cannot be reused as a selector-independent disproof.
3. A dimension-free selector is proved for every fixed finite support bound, for all diagonal kernels with arbitrary support, and for kernels block diagonal over a supplied uniformly bounded partition. None of these covers the full commuting class: a rank-one eigendirection of a non-diagonal \(K\) may have full coordinate support.

## Exact obligations

A positive proof must construct one selector on the whole commuting class and check exact divergence, positivity, unit mass, the original pointwise capacity, Borel dependence, coordinate-permutation covariance, all spectral/eigenspace degenerations, and simultaneous changes of both commuting pairs. It may exploit that \(P\) is a spectral rank-one direction of \(K\), but it must not choose an eigenvector phase or basis discontinuously. Any monotone DPP coupling invoked must be turned into a single measurable flow and must be quantitatively stable in edge \(\ell^1\).

A negative proof must be selector-independent: give admissible commuting pairs whose full fibers themselves have no possible Lipschitz section with dimension-free constant, or establish an equivalent obstruction applying to every Borel permutation-equivariant selector. A bad least-norm flow, an unstable circulation, or failure of whole-fiber Hausdorff stability alone is insufficient.

Classify the result only for the commuting class. Do not claim general unrestricted non-diagonal kernels, exact JO, or a strong process.

Return exactly PROVED or DISPROVED, followed by a complete supporting argument.
