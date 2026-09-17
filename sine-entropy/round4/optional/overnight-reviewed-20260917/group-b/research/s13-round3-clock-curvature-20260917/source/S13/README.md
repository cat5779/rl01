INCOMPLETE_TARGET__CUMULATIVE_S13_ROUNDS_1_TO_3

# Cumulative S13 research package

This archive preserves all prior S13 artifacts and adds the new round-three
author theorem. No result in this package closes the complete-configuration
sine entropy-rate target.

## Directory status

- `round1_unreviewed/` — the original first-round ZIP, preserved byte-for-byte.
- `round2_unreviewed/` — the prior growing-defect, cusp, potential-clock, and
  entropy-value report, preserved as author-unreviewed material.
- `round3_author_result/` — the new extensive signed clock-curvature component,
  proof, ledgers, replay scripts, and frozen receipts.
- `exploration_unproved/` — finite corrected-law experiments concerning the
  unpaid moving-count term. These are candidates, not theorems.

## Important superseding scope note

The round-two random-forward-clock degree-one/degree-two no-go must not be read
as an averaged-law obstruction. The averaged maximal-overlap density has zero
Johnson degree-one component. It remains informative only as a conditional or
operator-multiplier obstruction when degree-one matching is separately imposed.
Round three makes this correction explicit and proves its KL lower bound using
a nonzero averaged degree-two adjacent-pair mode.

## New round-three theorem

At `a_*=(1-c)/2`, the corrected clock contributes

`C_n=sum_l pi_l[-tauhat_l''] I_l`

to the uniform-slice divergence curvature. For every fixed `0<c<1`, even `n`,

`liminf C_n/n >= 2 D_pair(c)/(1-c^2)>0`.

At `c=19/20`, the lower coefficient is
`1.4045396549292533...`.

This is only one signed component. The moving-count term
`W_n=sum_l pi_l''K_l` remains unpaid and may offset it.

## Verification

Run:

```bash
python round3_author_result/scripts/replay.py
python verify_manifest.py
```

`MANIFEST.sha256` covers every package file except itself. Deterministic JSON
receipts are author self-checks, not external certification.
