# Handoff prompt: finite consistency for commuting positive flows

Prove or disprove the following frozen theorem. The conclusion concerns simultaneous choices on arbitrary finite lists; pairwise repairs or instability of one optimizer do not settle it.

Fix \(0<\varepsilon<1/2\). For a finite coordinate set \(E\), let
\[
\mathcal C_E^\varepsilon
=\{(K,P):\varepsilon I\preceq K\preceq(1-\varepsilon)I,
\ P\text{ rank-one projector},\ KP=PK\}.
\]
Let \(\mathcal F_E(K,P)\) be the full nonnegative upward DPP birth-flow fiber with exact divergence \(b_{K,P}\), total mass one, and pointwise outgoing capacity
\[
F_{\rm out}(S)\le(2/\varepsilon)p_K(S).
\]

Determine whether there is a finite constant \(C_\varepsilon\), independent of \(E\), such that for every integer \(m\ge1\) and every finite list
\[
x_a=(K_a,P_a)\in\mathcal C_E^\varepsilon,
\qquad 1\le a\le m,
\]
there are flows \(f_a\in\mathcal F_E(K_a,P_a)\) satisfying, simultaneously for all \(a,b\),
\[
\|f_a-f_b\|_1
\le C_\varepsilon
\bigl(\|K_a-K_b\|_1+\|P_a-P_b\|_1\bigr).
\tag{FC}
\]

The following facts may be used:

1. For fixed \(E\), (FC) is equivalent by compactness on a countable dense set to a global dimension-free Lipschitz selector on the commuting class; averaging over the finite permutation group enforces equivariance without changing the constant.
2. A stable signed endpoint current and nonempty positive endpoint fibers dominated by twice its positive part are known. They do not imply simultaneous consistency.
3. A dimension-free directed repair is known when all inputs have the same projector. A full positive selector is known on the scalar-complement subclass and on canonical matching-block kernels. These results do not cover arbitrary varying projectors in the commuting class.
4. The global least-norm selector is not support-uniform. This is not a selector-independent obstruction to (FC).

A positive proof must establish simultaneous choices for arbitrary finite lists, not merely pairwise Hausdorff estimates or ordering-dependent repairs. It must work for varying projectors and every spectral multiplicity, with a constant independent of \(|E|\), \(m\), and support size. Explain explicitly how the finite-list choices yield a Borel permutation-equivariant selector.

A negative proof must give a selector-independent obstruction: an explicit sequence of finite lists of commuting inputs such that every feasible simultaneous choice has a Lipschitz ratio tending to infinity. A bad optimizer, unstable circulation, or failure of whole-fiber Hausdorff stability is insufficient.

Classify the result only for the commuting class. Do not claim unrestricted noncommuting kernels, exact JO, or a process construction.

Return `PROVED` or `DISPROVED`, followed by a complete supporting argument.
