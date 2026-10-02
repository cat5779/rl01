# Dimension-free positive selector for rank-one directions supported on at most three coordinates

## Frozen theorem

Fix \(0<\varepsilon<1/2\). For every finite coordinate set \(E\), every Hermitian kernel
\[
\varepsilon I\le K\le(1-\varepsilon)I,
\]
and every rank-one projector \(P\) whose coordinate support has size at most three, let \(b_{K,P}\) be the derivative of the exact DPP law in direction \(P\).

Prove or disprove that there is a selector \((K,P)\mapsto F_{K,P}\) and a constant \(C_\varepsilon^{(3)}<\infty\), independent of \(|E|\), such that:

- \(F_{K,P}\ge0\) is an upward Boolean-cube edge flow;
- \(\operatorname{div}F_{K,P}=b_{K,P}\);
- \(\sum_{S,i\notin S}F_{K,P}(S,i)=1\);
- \(F_{K,P,\mathrm{out}}(S)\le(2/\varepsilon)p_K(S)\);
- the selector is Borel and permutation-equivariant; and
- for all allowed pairs on the same \(E\),
  \[
  \|F_{K,P}-F_{L,Q}\|_1
  \le C_\varepsilon^{(3)}
  \bigl(\|K-L\|_1+\|P-Q\|_1\bigr).
  \tag{DF3}
  \]

## Audited input

You may use the proved support-at-most-two theorem with its explicit dimension-free positive clipped selector and constant
\[
C_\varepsilon^{(2)}
=
\max\left\{18,\;2+(6+4/\varepsilon)
\left[1+\left(\frac{1-2\varepsilon}{2\varepsilon}\right)^2\right]\right\}.
\]
You may also use exact conditioning on outside patterns, preservation of the spectral gap, dimension-free trace-norm stability of conditional kernels, the coordinate-direction uniqueness identity, and bounded-active-support Hausdorff stability of the full flow fibers.

## Exact obligation

A fixed active triple is not enough. The construction must remain compatible and Lipschitz when:

- a three-coordinate direction degenerates to support two or one;
- two active triples overlap in two, one, or zero coordinates;
- phases and zero coordinates change;
- \(K\) and \(P\) move simultaneously; and
- the ambient dimension grows while active support stays at most three.

A finite-dimensional Hoffman or Steiner selector on one labeled triple may be used only after proving a uniform \(\varepsilon\)-dependent bound and all cross-triple compatibility/covariance interfaces. Do not divide by the least atom. Do not infer a selector merely from pairwise Hausdorff distance without a globally compatible selection argument.

A negative answer must give an exact obstruction within the support-at-most-three DPP family that defeats every Borel permutation-equivariant dimension-free Lipschitz selector. Failure of one optimizer is insufficient.

## Scope

This is a strict restricted extension of the support-at-most-two theorem. It does not claim the unrestricted arbitrary-support selector theorem.

Return exactly PROVED, DISPROVED, or INCOMPLETE, followed by a complete supporting argument. If incomplete, preserve every complete new local selector or compatibility lemma and state the minimal gap.
