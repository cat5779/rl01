# Every-selector obstruction at the fixed kernel \(K=I/2\)

## Frozen claim

Fix \(0<\varepsilon<1/2\). For each finite coordinate set \(E\), let
\[
K_E=\tfrac12 I_E,
\]
and for every rank-one projector \(P\) let \(\mathcal F_E(P)=\mathcal F_E(K_E,P)\) be the full nonnegative capacitated DPP birth-flow fiber:
\[
\operatorname{div}F=b_{K_E,P},\qquad
\sum_eF(e)=1,\qquad
F_{\rm out}(S)\le(2/\varepsilon)p_{K_E}(S).
\]

Prove or disprove the following nonexistence statement:

> There is no finite \(C_\varepsilon\), independent of \(|E|\), and no family of Borel coordinate-permutation-equivariant selections
> \[
> P\longmapsto \Phi_E(P)\in\mathcal F_E(P)
> \]
> such that
> \[
> \|\Phi_E(P)-\Phi_E(Q)\|_1
> \le C_\varepsilon\|P-Q\|_1
> \tag{NS0}
> \]
> for all rank-one projectors \(P,Q\) on the same \(E\).

Thus PROVED means an exact every-selector obstruction, while DISPROVED means an explicit selector satisfying (NS0), with a dimension-free bound.

## Audited input and logical warning

At \(K=I/2\), dimension-free Hausdorff stability of the entire fibers is false. There are \(P_m,Q_m\) with
\[
\|P_m-Q_m\|_1=2\sqrt6\,m^{-1/4}
\]
and a deliberately chosen \(F_m\in\mathcal F(P_m)\) whose distance from the entire target fiber is at least \(3/32\).

This does **not** prove (NS0): it is a directed bad-flow witness, and a selector may avoid \(F_m\). Any proof of nonexistence must force every Borel permutation-equivariant choice, for example through symmetry, branching, cycles, or a quantitative incompatibility among several nearby projectors. Failure of one optimizer or one chosen flow is insufficient.

Support-at-most-\(s\) selectors exist with constants depending on \(s\), so any obstruction must use genuinely unbounded support. Coordinate directions have singleton fibers.

## Exact obligation

For PROVED, produce an explicit or exactly parameterized finite family or asymptotic family of projectors and show that every permitted equivariant selection violates a dimension-free Lipschitz bound. All lower bounds must apply to the selected points forced by the hypotheses, not to a freely chosen bad point.

For DISPROVED, construct one globally compatible Borel permutation-equivariant selector on all rank-one projectors at \(K=I/2\), prove fiber membership and a constant independent of dimension, and treat phases and zero-coordinate degenerations.

Return exactly PROVED or DISPROVED, followed by a complete supporting argument.



