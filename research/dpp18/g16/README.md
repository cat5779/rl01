# Commuting DPP positive selectors: current breakpoint

The general varying-projector, dimension-free Lipschitz finite-consistency problem remains **OPEN / INCOMPLETE**. Its exact statement is [TASK.md](TASK.md).

The current fixed-projector conclusion is stronger than the original archive: one weighted-energy rule satisfies

\[
\|\Psi_E(K,P)-\Psi_E(L,P)\|_1
\le 10\varepsilon^{-3/2}\|K-L\|_{\rm tr}^{1/2}
\]

for all finite E and epsilon-gapped kernels commuting with the same rank-one P. The constant does not depend on E or the support of P. This is an exponent-one-half result with P fixed, not the exponent-one target with P varying.

## Read the current derivations

1. [PROOF03.md](PROOF03.md): the complete weighted repair and two variational inequalities. It incorporates the complete-current derivative correction documented in [ERRATUM03.md](ERRATUM03.md).
2. [TOPOLOGY03.md](TOPOLOGY03.md): continuity of the same rule across projector-support changes when E is fixed. Its constants depend on E.
3. [METHOD03.md](METHOD03.md): a quantum positive-overlap obstruction, general quantum endpoint trace comparison, and a scalar example showing why the obstruction does not refute positive selection.
4. [REVIEW03.md](REVIEW03.md): the checked scope and the remaining gaps in the original derivation.
5. [Exact three-input gap, RL01 PR126](https://github.com/cat5779/rl01/pull/126): the returned full-fiber proof and two independent exact checks establish the bounded ratio 13/12. Read this as a separate finite obstruction to pairwise optimum gluing.

The earlier [REVIEW02.md](REVIEW02.md) separately checks the fixed-P full-fiber l1 repair with constant 4/epsilon. The new weighted repair is needed because l1 control alone does not control energy under small edge weights.

## What remains unresolved

Changing P can destroy a common positive quantum substate even when the full quantum states are close. That defeats this particular residual method; it does not prove that the weighted optimizer, or every selector, is unstable. The scalar example has an explicit stable optimizer.

The main task remains simultaneous exponent-one control for arbitrary finite lists of commuting inputs with varying, potentially delocalized projectors. Neither a fixed finite incompatibility ratio nor an unstable arbitrary point in a fiber resolves it.

## Historical sources

[CONTINUATION_02_UNREVIEWED.md](CONTINUATION_02_UNREVIEWED.md) is preserved unchanged. Its fixed-P weighted proof omitted the central weighted-repair and variational steps; the new note supplies them. Other claims in that packet retain their individual review status in [STATUS.md](STATUS.md). The earlier [PROOF_LEDGER.md](PROOF_LEDGER.md), [PROOF_EXTRACTS.md](PROOF_EXTRACTS.md), and [SOURCE_MAP.md](SOURCE_MAP.md) record inherited results and provenance. Older attack plans are historical context rather than the current reading order.

The duplicate archive at `randomcat4/dpp-entropy-tools#148` has been closed after preservation. This RL01 directory is the current entry. These are scoped research derivations with local review, not external peer review, full formalization, or a novelty certification. The general problem is not marked solved.
