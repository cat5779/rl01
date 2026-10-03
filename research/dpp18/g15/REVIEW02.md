# R18 G15 external result audit

Date: 2026-10-03 (Asia/Singapore)

Source: `randomcat4/dpp-entropy-concavity#10`, head
`d2ade711f44c6eca1bcb8a7535e10146f3b807d1`.

## Verdict

`PARTIAL / UNRESTRICTED TARGET OPEN`.

The packet itself correctly does not claim the unrestricted endpoint-capacity
selector theorem.  It contains useful constructions and structural identities,
but its review was produced in the same research session and the new
all-dimensional energy/Hessian claims have not received an independent
whole-proof audit here.  They are therefore preserved as candidates rather
than promoted to the certified ledger.

## What can safely be used now

- The exact remaining obstruction is correctly identified: the proved signed
  energy form does not give a dimension-free inverse estimate for the different
  Hessian governing the entropy-center selector.
- A failure of bit-flip covariance, a fixed-degree formula, or one electrical
  repair rule is only a method obstruction, not a disproof of all selectors.
- The support-at-most-three and fixed-support conclusions are consistent with
  already certified restricted-selector results.  They do not extend to
  unbounded delocalized support.
- No selector-independent finite family with divergent required Lipschitz
  ratio is supplied.

Consequently this PR changes the attack map, not the truth status of the full
theorem.

