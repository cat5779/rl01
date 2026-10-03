# Dimension-free selector for canonical uniformly bounded components

## Frozen theorem

Fix \(0<\varepsilon<1/2\) and an integer \(r\ge1\). For every finite coordinate set \(E\), let \(\mathcal B_{E,r}^\varepsilon\) consist of Hermitian kernels \(K\) satisfying
\[
\varepsilon I\preceq K\preceq(1-\varepsilon)I
\]
such that every connected component of the coordinate graph
\[
G_K=(E,\{\{i,j\}:i\ne j,\ K_{ij}\ne0\})
\]
has size at most \(r\). The canonical component partition is determined by \(K\) and may change when \(K\) changes.

For a rank-one projector \(P\), let \(\mathcal F_E(K,P)\) be the full nonnegative upward DPP birth-flow fiber with exact divergence \(b_{K,P}\), total mass one, and pointwise outgoing capacity
\[
F_{\rm out}(S)\le(2/\varepsilon)p_K(S).
\]

Prove or disprove that, for every fixed \((\varepsilon,r)\), there are Borel, coordinate-permutation-equivariant selectors
\[
\Psi_{E,r}(K,P)\in\mathcal F_E(K,P)
\]
and a finite constant \(C_{\varepsilon,r}\), independent of \(|E|\), such that
\[
\|\Psi_{E,r}(K,P)-\Psi_{E,r}(L,Q)\|_1
\le C_{\varepsilon,r}
\bigl(\|K-L\|_1+\|P-Q\|_1\bigr)
\tag{BCOMP}
\]
for all \(K,L\in\mathcal B_{E,r}^\varepsilon\) and all rank-one projectors \(P,Q\). No common block partition for \(K\) and \(L\) is supplied or assumed.

## Audited input and exact boundary

1. If one common partition into blocks of size at most \(r\) is supplied and both kernels are block diagonal over it, a dimension-free selector with constant depending only on \((\varepsilon,r)\) is known.
2. The theorem is known for \(r=1\) by the diagonal selector and for \(r=2\) by a refinement-compatible two-coordinate selector. In the \(r=2\) proof, incompatible matchings are compared by deleting noncommon matching edges and using trace-norm duality.
3. For \(r\ge3\), two canonical partitions can be incompatible and their union can have large components. A common coarsening cannot simply be inserted into the supplied-partition theorem.
4. A positive proof may let its constant grow with the fixed parameter \(r\), but never with \(|E|\) or the number of components.

## Exact obligations

A positive proof must give one selector on the whole class and prove exact divergence, positivity, unit mass, the original capacity, Borel dependence and full permutation covariance. It must establish exact compatibility whenever a canonical component splits after some off-diagonal entries vanish, and it must compare incompatible partitions without accumulating a factor proportional to the number of blocks. Any local finite-dimensional selector used must be quantitatively compatible across all refinements, not just continuous inside one fixed block.

A negative proof must be selector-independent for some fixed finite \(r\): construct admissible bounded-component kernels whose full positive fibers rule out every dimension-free Lipschitz section. Failure of a particular local optimizer or canonical formula is insufficient.

Classify the result for each fixed \(r\). A constant depending on \(r\) does not prove the unrestricted non-diagonal theorem as \(r\to\infty\).

Return exactly PROVED or DISPROVED, followed by a complete supporting argument.
