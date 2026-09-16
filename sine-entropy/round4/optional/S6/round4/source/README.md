# S6 round 4 deliverable

Status: `PROVED_SCOPED_LEMMA`.

The package contains two new complete scoped theorems:

1. a dimension-uniform full-configuration curvature sign for every Hermitian
   contraction on the fixed high-contrast band
   `37/40 <= c <= 37/40+10^(-13)` and centered `a` strip of length `1/100`;
2. a positive real-q estimate for disjoint true-block correlated references,
   including a vanishing signed finite Jensen defect.

The general sine target remains open.

## Main files

* `proof.md` — definitions, exact statements, and proofs.
* `DELTA_FROM_LAST_ROUND.md` — reviewed baseline versus latest local author claim.
* `gap_audit.md` — proved/certified/diagnostic/unresolved separation.
* `attempts.md` — preserved failed drafts and repairs.
* `candidate_ledger.md` — three scouted mechanisms and two promoted attempts.
* `work_log.md` — genuine UTC timing and checkpoints.
* `sources/reading_notes.md` — public commit and primary-source theorem audit.
* `scripts/` — exact certificates, finite checks, replay, and manifest tools.
* `evidence/frozen/` — read-only candidate and theorem freezes.
* `evidence/certificates/` — frozen exact outputs.
* `output/` — mutable replay destination only.

## Reproduction

From the extracted directory, run:

```bash
python3 scripts/replay.py --output-dir output/replay
```

The replay writes only below the chosen output directory, compares parsed JSON
rather than line endings, and verifies the frozen certificate hashes recorded in
`manifest.json`.

All proof scripts use only the Python standard library.  UTF-8 and LF are used
for generated text.

## Evidence labels

* Universal mathematics in `proof.md`: analytical proof.
* Rational inequalities and finite atom algebra: exact certificate.
* Noninteger-q example grid: floating Decimal diagnostic only.
* This package's replay: self-review, not independent certification.
