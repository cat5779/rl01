# Failed or insufficient routes

This file separates established dead ends from exploratory ideas that were checked and rejected during the continuation. Nothing here is a new theorem unless explicitly tied to an audited source.

## 1. Full-fiber Hausdorff stability

**Status:** rigorously disproved upstream (#109), but insufficient for #123.

The obstruction exploits a deliberately chosen macroscopic circulation. A selector may avoid that region of the fiber.

Do not reuse this as an every-selector argument without an additional infimum-distance or cycle certificate.

## 2. Global least-Euclidean-norm selector

**Status:** rigorously disproved as a dimension-free selector upstream (#116).

The output/input ratio grows at least on the order of \(\sqrt n\) in a scalar-kernel family.

This route cannot be repaired merely by controlling active-set changes: the upstream example has strict inequality slack.

However the same family has a different stable selector, so least norm is a method failure, not a theorem disproof.

## 3. Generic fixed-normal/Hoffman continuity

**Status:** insufficient.

For each fixed dimension, standard polyhedral error bounds give continuity/Lipschitz selection constants. Those constants can depend badly on the number and geometry of cuts.

The target specifically forbids a dimension-dependent Hoffman or active-set factor.

## 4. Pairwise repair only

**Status:** logically insufficient.

Even a symmetric Hausdorff estimate between every pair of fibers would not automatically supply one compatible choice over every finite family.

The frozen theorem requires simultaneous consistency. Any repair algorithm that depends on an ordering or a chosen root needs a proof that accumulated error does not grow with list length or path length.

## 5. Sequential shared-uniform monotone coupling

**Status:** analytically rejected as a direct construction.

Natural idea:
1. reveal coordinates in a fixed order;
2. couple conditional Bernoulli decisions with the same uniform variable;
3. hope that after the unique \(0/1\) split, the remaining conditional kernels coincide.

The last step is false in general. Schur-complement conditioning of a rank-one ordered pair preserves structured low-rank relations, but a first split does not generally collapse the two remaining conditional kernels to equality.

Therefore this does not directly produce a one-point upward endpoint coupling.

## 6. Add a point with weights proportional only to \(P_{ii}\)

**Status:** analytically rejected outside diagonal/scalar-complement cases.

Natural candidate:
- sample \(S\) from the lower endpoint law;
- among \(i\notin S\), choose the new point using a normalization of the diagonal masses \(P_{ii}\).

This matches the diagonal formula heuristically but ignores the non-diagonal dependence of the upper endpoint DPP. In a general commuting non-diagonal pair, the target inclusion/exact-pattern probabilities depend on off-diagonal interference, so diagonal weights alone cannot recover the required upper marginal.

The successful diagonal and scalar-complement selectors should not be extrapolated this way.

## 7. Force linearity in the projector

**Status:** not established and structurally too restrictive as a default route.

It is tempting to seek
\[
P\mapsto f_{K,P}
\]
linear on the spectral eigenspace, equivalently an operator/POVM-valued flow whose rank-one evaluation gives the desired scalar flow.

Nothing in the positive-part max-flow proof supplies such a linear section. The feasibility theorem is nonlinear because it takes positive parts and invokes max-flow cuts.

A positive proof may be nonlinear in \(P\); requiring linearity risks imposing a stronger false problem.

## 8. Use the signed current itself

**Status:** impossible as a positive selector in general.

The explicit \(J_{K,P}\) is stable and has exactly the right endpoint marginals, but can have negative edges.

The theorem that a positive flow exists below \(2J_+\) repairs feasibility but does not identify a canonical stable repair.

Negative entries of \(J\) are therefore not a disproof.

## 9. Support-bounded obstruction

**Status:** ruled out as a standalone dimension-free counterexample mechanism.

Upstream support reduction shows that bounded common coordinate support reduces to finitely many fixed-dimensional cube problems, with ambient-dimension-independent constants.

A genuine negative family must let the effective coordinate support grow.

## 10. Coordinate projector endpoint

**Status:** ruled out as a strong pairwise obstruction.

Coordinate directions have singleton fibers and every nearby fiber collapses linearly toward them.

Hence a construction with one endpoint equal to a coordinate projector cannot generate an unbounded pairwise separation ratio.

## Preservation note

Some exploratory computations were discussed during the live continuation, but no independently reproducible script/output was committed in the source repository during that session. This archive therefore does **not** promote those numerical observations to evidence. Only analytical deductions and upstream audited results are preserved as such.
