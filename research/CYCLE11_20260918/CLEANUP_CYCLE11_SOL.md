# Cycle11 PR cleanup record

Date: 2026-09-19 (Asia/Singapore)

This cleanup separates archival value from mathematical completeness. A negative audit, a repaired partial result, or a precise gap is retained as research evidence; it is not promoted to a proof of the sine entropy-rate conjecture. Every merge used a merge commit with a fresh state/head check. No branch was deleted.

## `cat5779/rl01`

### Merged source archives

- #22 — Cycle06 source archive.
- #28 — Cycle07 S51/S53 sources and S54 task archive.
- #32 — Cycle08 complete source/review archive and S55 task archive.

These PRs were merged as provenance archives. Their author manuscripts were not promoted beyond the separate independent-review verdicts.

### Merged independent reviews

- #24 — S41 Cycle05 complete-jet repair review.
- #25 — S44 Cycle04 projection-completed jet review.
- #29 — S53 Cycle06 curvature-bridge review.
- #30 — S51 Cycle06 entropy-rate bridge review.
- #31 — S51 high-contrast continuation review.
- #33 — QWE02 boundary-response review.
- #34 — S54 Cycle07 signed output-KL review.
- #35 — S51 C1 renormalized V14 review.
- #36 — QWE01 incomplete-continuation review.
- #37 — S52 Cycle06 susceptibility review.
- #38 — S55 Cycle08 curvature-transfer review.
- #40 — Ward–Stein PR2 review.
- #41 — QWE06 Cycle09 partial-result review.
- #42 — QWE05 Cycle09 review, retaining the corrected **one-sided** payment statement.

All fourteen formal review Markdown files were checked directly in the final `origin/main` tree. In particular, the incomplete QWE01/QWE05/QWE06 lines remain explicitly incomplete; merging their reviews does not certify the main conjecture.

### Deliberately left open and untouched

- #5 — pre-existing diagnostics Draft.
- #39 — protected Cycle09 S59/S60 intake/archive.
- #43 — protected Cycle10 S61 task.
- #44 — protected new S61 review.
- #45 — protected Cycle11 archive/task PR.

No `STATE.json`, `LOG.md`, `math/rl01-cycle09`, or `math/rl01-cycle10` content was edited.

## `randomcat4/dpp-stationary-entropy`

### Merged

- #121 — S-line bearing map and repository homepage.
- #122 — QWE01 archive, whose PR title/body explicitly say **INCOMPLETE**.
- #123 — QWE02 source/result archive; its accepted mathematical scope remains the independent review recorded in RL01 #33.

### Closed as stale task-only PRs

- #124 — QWE03.
- #125 — QWE04.

Each received a public cleanup comment stating that no research result had been delivered and that closure was operational, not a mathematical disproof. Both head branches and commits were verified to remain present after closure.

### Kept open with exact blockers

- #126 — QWE05. RL01 #42 verifies only the one-sided weighted `J_m` payment. The full `W_rel >= -o(n)` target remains incomplete because the actual deletion conditional-KL term `C_m` is unpaid. A public cleanup comment records this boundary.
- #127 — QWE06. RL01 #41 preserves the partial result with reviewer repairs; the reflection ordering, claimed `O(n^3)` tail step, and differentiated local-CLT interface are not certified as written. The fixed-window main target remains incomplete. A public cleanup comment records this boundary.

### Protected / unrelated

- #118 and #128 were not changed.
- Older unrelated open PRs were not changed.

## `randomcat4/dpp-entropy-concavity`

- #1 — merged the simplified five-page S-line load-bearing map.
- #2 — added the RL01 #40 review boundary in a public comment, marked the Draft ready, and merged it as a scoped Ward–Stein research archive. The merge does **not** assert the sign at `c=19/20`, a threshold improvement, or the full entropy-rate theorem.
- #3 — the five-point homepage counterexample PR was already merged before this cleanup and was not modified here.

The repository has no remaining open PR after #1 and #2 were merged.

## Final verification

- RL01 open set is exactly protected #39/#43/#44/#45 plus Draft #5.
- DPP stationary #126/#127 remain open with precise blockers; protected #118/#128 remain open and unchanged.
- DPP concavity has no open PR.
- The QWE03/QWE04 closed branches still resolve to their original head commits.
- `dpp-entropy-tools` was not changed.
- Transient GitHub TLS/mergeability delays were handled by re-reading remote state and exact head SHA before every mutation; no action was repeated on an already-merged or already-closed PR.
