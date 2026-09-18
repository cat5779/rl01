# QWE05 / DPP PR126 — full proof received, separate audit queued

Updated intake: 2026-09-18T20:32:41.034483+08:00
Source repository: randomcat4/dpp-stationary-entropy, PR126.
Source result directory: research_tasks/external_20260918/QWE05/results/
Latest harvested PR update UTC: 2026-09-18T12:31:21Z

The earlier 18:18 Asia/Singapore comment-only intake is superseded. The
full 893-line mathematical report QWE05_RESULT.md and both verification
scripts are now in the PR and harvested here. The author is adding data
companions. No ZIP or manual download is needed to begin the proof audit.

Current archived files: QWE05_RESULT.md, README.md, analytic_check_summary.json, analytic_run.log, anchor_checks.csv, deletion_ledger.csv, environment.json, full_model.csv, interpolation_checks.csv, qwe05_analytic_checks.py, qwe05_verify.py, radial_checks.csv, run.log, verification_summary.json.
Report-listed reproduction companions not yet present at this snapshot:
analytic_source_checks.csv.
These numerical companions are tracked separately from mathematical source
completeness; they are not a checksum or proof-acceptance gate.

Author's overall target W_rel >= -o(n) remains INCOMPLETE. New claims pending
independent review: a uniform J_m <= K(1+log n)/n upper bound, its exact
count-flux o(n) payment, an all-mode density-source O(n^-2) bound, and a
polynomial pointwise likelihood comparison allowing Poisson score transfer.
The resulting sufficient unpaid target is sum omega_m C_m = o(n), where
C_m is the actual reverse conditional deleted-site KL given the complete
retained configuration. This is neither a necessary condition nor a proof
of entropy-rate concavity. The numerical tests are diagnostics only.

One separate QWE05 audit assignment was queued to existing Sol high task
01a0b04a-afe9-7393-ba97-58270365d292, after its current QWE06 review. It must
produce QWE05_REVIEW.md and its own RL01 PR. QWE06 and Ward-Stein keep their
independent reports. S59/S60 are untouched; no web resend was performed.

## Completed separate independent audit — RL01 PR42

The corrected independent report is copied to ../reviews/QWE05_REVIEW.md.
Verdict: NEW ONE-SIDED J_m PAYMENT VERIFIED; FULL TARGET INCOMPLETE.
The reviewer verified Poisson uniformization, actual-law polynomial
pointwise likelihood comparison, score transfer and the complete moving-
reference interpolation estimate. In particular sum omega_m J_m is bounded
ABOVE by K sqrt(n)(1+log n); no two-sided or absolute bound is asserted.
The original review wording was clarified by its author in the same PR42.
The remaining sufficient condition sum omega_m C_m=o(n) is still OPEN.
Deleting a point can hide conditional distinctions even when deleted
marginals coincide; the generic linear-algebra example is not an actual
Fourier-DPP counterexample. See RENEWAL_DECISION.md for the proposed next
tool. No new web research assignment was sent.

The reviewer reproduced both author scripts, including n<=18 complete
configuration tests and 270+30+24 analytic stress checks. The omitted
analytic_source_checks.csv is regenerable; it is not a proof acceptance gate.
