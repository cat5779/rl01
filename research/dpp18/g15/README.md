# RL01 PR #122 transfer: endpoint-capacity selector partial results

This directory transfers a consolidated, adversarially re-checked research packet corresponding to **cat5779/rl01#122** into the DPP research repository.

## Exact source correspondence

- Source repository: cat5779/rl01.
- Source PR: #122, DPP R18 G15: stable endpoint-capacity selector.
- Frozen source head: b79ff47a3d490fdb2ed400b3f908d39ec20f580a.
- Frozen task: research/dpp18/g15/TASK.md.
- TASK blob: 9def850d5577181e8147109b1edff1e0b6278b13.
- PROMPT blob: f41f7f91dc1791813d76b6a712aecd7a4d1f5fb0.
- Source status at that head: OPEN.

TASK.md and PROMPT.md here are verbatim copies of the frozen source files.

## Result status

**OPEN / PARTIAL.** This packet does not claim to prove or disprove unrestricted HSEL.

The main established results are:

1. one globally defined minimum-correction selector, with an explicit dimension-free bound for every fixed projector-support size;
2. the sharper global bound
   \[
   \|\Theta(x)-\Theta(y)\|_1\le5\|J_x-J_y\|_1
   \]
   when projector support has size at most three, including changing supports;
3. a general-dimensional positive signed-energy representation, strict nontrivial capacity cuts, positive-current connectivity, and relative-interior feasibility;
4. dimension-free signed-energy stability under both kernel and projector perturbations;
5. genuine DPP obstructions to exact noise-covariant selection and to fixed-degree normalized configuration formulas;
6. a precise remaining bottleneck for the natural entropy-center selector.

## Reading order

- RESULT.md — consolidated mathematical results and the exact remaining gap.
- REVIEW.md — adversarial re-review of the vulnerable steps and explicit rejection of overclaims.
- STATUS.md — short scope/status ledger.
- SOURCE.md — exact provenance.
- TASK.md, PROMPT.md — frozen RL01 #122 materials.

## Verification boundary

The exact standard-library checkers from the research pass were rerun and returned their scoped PASS statuses. The adversarial review re-derived the vulnerable analytic steps, but it was performed in the same research context and is **not independent external review or formal verification**.

This destination PR should remain **draft**. No novelty or priority claim is made, and no repository-wide theorem-status ledger is changed.
