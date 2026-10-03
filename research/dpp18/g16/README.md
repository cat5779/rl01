# DPP selector finite-consistency breakpoint archive

Date: 2026-10-03

Primary source task: `cat5779/rl01#123`, **DPP R18 G16: finite-consistency attack**.

This directory is a handoff archive of the current mathematical breakpoint, the certified inputs inherited from earlier DPP selector work, and the exploratory routes checked during the 2026-10-03 continuation.

## Status

**OPEN / INCOMPLETE.**

No proof or selector-independent disproof of the full commuting finite-consistency theorem is claimed here.

The exact remaining target is:

For every finite coordinate set (E), every (0<\varepsilon<1/2), and every finite list of commuting inputs
\[
x_a=(K_a,P_a),\qquad
\varepsilon I\preceq K_a\preceq(1-\varepsilon)I,\quad
P_a\text{ rank one},\quad K_aP_a=P_aK_a,
\]
choose
\[
f_a\in\mathcal F_E(K_a,P_a)
\]
simultaneously so that
\[
\|f_a-f_b\|_1
\le C_\varepsilon
\bigl(\|K_a-K_b\|_1+\|P_a-P_b\|_1\bigr)
\]
for all (a,b), with (C_\varepsilon) independent of (|E|), the list length, and support size.

By the certified compactness argument in `cat5779/rl01#119`, this finite-consistency property is equivalent, for each fixed (E), to a global Lipschitz selector; averaging over the finite permutation group then gives permutation equivariance without enlarging the constant.

## What is preserved here

- `PROOF_LEDGER.md`: certified theorem inventory and exact quantitative bounds.
- `PROOF_EXTRACTS.md`: self-contained proof skeletons for the main reusable inputs.
- `BREAKPOINT.md`: the current obstruction after all certified reductions.
- `FAILED_ROUTES.md`: routes that are known insufficient or were analytically rejected in this continuation.
- `NEXT_ATTACKS.md`: concrete next proof/disproof programs.
- `SOURCE_MAP.md`: source PRs and files in `cat5779/rl01`.
- `CONTINUATION_02_UNREVIEWED.md`: later candidate derivations, deliberately kept out of the certified proof ledger.
- `REVIEW_REQUEST_CONTINUATION_02.md`: independent-audit checklist for those candidate derivations.

## Continuation 02 boundary

The second continuation contains candidate advances on:

- full-fiber fixed-projector repair;
- a globally coherent fixed-(P) weighted selector with a candidate (1/2)-Hölder modulus;
- fixed bounded coordinate components;
- an explicit three-input finite-family incompatibility;
- structural obstructions to affine-in-(P) rules and unconstrained weighted currents.

These are **not independently reviewed**. The main verdict remains `OPEN / INCOMPLETE` until a separate audit promotes any individual statement.

## Important scope rule

Several prior negative results concern a particular optimizer or the geometry of the full fiber. They are **not** selector-independent obstructions. In particular:

- failure of dimension-free Hausdorff stability of the entire positive fiber does not disprove a well-chosen selector;
- failure of the global least-Euclidean-norm selector does not disprove a different selector;
- negative entries of the explicit signed current do not imply failure of positive selection.

Conversely, pairwise repairs are not enough: the frozen target requires one set of choices satisfying all pairwise bounds on every finite list.

## Repository placement note

The source task and its proof history live in `cat5779/rl01`. The active GitHub integration available in this session did not have branch-write access there (GitHub returned HTTP 403 on branch creation). This archive is therefore stored in `randomcat4/dpp-entropy-tools` as a preservation/handoff PR, with all original source locations explicitly recorded.
