# Dimension-free positive selector for all gapped diagonal kernels

## Frozen theorem

Fix \(0<\varepsilon<1/2\). For every finite coordinate set \(E\), every diagonal kernel
\[
K=\operatorname{diag}(k_i)_{i\in E},
\qquad
\varepsilon\le k_i\le1-\varepsilon,
\]
and every rank-one projector \(P\), let \(\mathcal F_E(K,P)\) be the full nonnegative capacitated DPP birth-flow fiber.

Prove or disprove that the explicit rule
\[
\boxed{
F_{K,P}(S,i)
=
P_{ii}\,p_{K_{E\setminus\{i\}}}(S),
\qquad S\subseteq E\setminus\{i\},
}
\tag{DSEL}
\]
is a Borel, coordinate-permutation-equivariant selector in \(\mathcal F_E(K,P)\) and obeys a dimension-free estimate
\[
\|F_{K,P}-F_{L,Q}\|_1
\le
C_\varepsilon
\bigl(\|K-L\|_1+\|P-Q\|_1\bigr)
\tag{DLIP}
\]
for all gapped diagonal \(K,L\) and all rank-one \(P,Q\) on the same \(E\).

Here \(p_{K_{E\setminus\{i\}}}\) is the exact DPP law on the coordinates other than \(i\), identified with subsets \(S\subseteq E\setminus\{i\}\).

## Audited input

At \(K=I/2\), this formula reduces to
\[
F_{I/2,P}(S,i)=2^{-(|E|-1)}P_{ii}
\]
and is an independently audited selector with Lipschitz constant \(1\). Full-fiber Hausdorff stability nevertheless fails there because other flows may carry unstable circulations; that fact does not obstruct this selector.

You may use total-variation/edge-\(\ell^1\) stability of finite DPP laws,
\[
\|p_A-p_B\|_1\le2\|A-B\|_1,
\]
but must exploit the weights \(P_{ii}\) rather than sum a dimension-dependent bound over \(i\).

## Exact obligations

Verify directly:

1. the exact derivative \(b_{K,P}\) at a diagonal kernel, including why off-diagonal entries and phases of \(P\) do not enter;
2. nonnegativity, total mass one, exact divergence, and the original pointwise capacity
   \[
   F_{\rm out}(S)\le(2/\varepsilon)p_K(S);
   \]
3. a dimension-free comparison for simultaneous changes of all diagonal entries of \(K\) and the arbitrary-support projector \(P\);
4. zero-coordinate degenerations, Borel dependence, and coordinate-permutation covariance.

A proof must write the weighted product-law estimate in full and give an explicit finite \(C_\varepsilon\) (a universal constant is allowed). A disproof must identify an exact failed obligation for (DSEL), not merely the instability of other points in the fiber.

This theorem concerns diagonal kernels only. Do not claim the unrestricted non-diagonal selector theorem.

Return exactly PROVED or DISPROVED, followed by a complete supporting argument.



