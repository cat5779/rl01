DISPROVED_ROUTE_LEMMA

# S11 resumed quantitative-continuation obstruction

This package answers the strengthened S11 continuation assignment at the pinned
repository revision

`191297f3073e60f5954a93ae5e6e94c32447b590`.

It does **not** prove or disprove the sine entropy-rate target and it does not
claim entropy concavity at `c=0.926`.  It proves two quantitative obstructions
to precisely defined, live continuation-certificate families and identifies
the exact missing estimate.

## New results

Let `c0=37/40=0.925` and `c*=463/500=0.926`.

1. **Adaptive split-tail family.**  Even after optimizing the spectral gap,
   cutoff, outer interval, inner strip, and every continuation step separately,
   the differentiated split-tail certificate used in the rejected checkpoint
   pays more than

   ```text
   (366368000000/1323) * (c-d)
   ~= 2.769221466e8 * (c-d)
   ```

   in curvature response.  This is an exact 100-bin cover of every legal gap
   and every threshold-admissible cutoff, with the best-case zero-width target
   strip and all other positive tail charges deleted.  Its strong-margin total
   contrast ceiling is below `5.417e-11`; subdivision cannot make the payment
   smaller because the lower bound is additive in total contrast.

2. **Uniform mode-separable family.**  Exact coefficient-specific local bounds
   still fail if distinct Chebyshev modes are charged independently and no
   signed cross-mode cancellation is credited.  For the exact witness
   `n=2, Q=diag(1,0)`, mode one has zero contrast response and mode two alone
   costs at least

   ```text
   (4177920000/47458321) * (c-d)
   ~= 88.0334557 * (c-d)
   ```

   at every legal shift.  This witness saturates the exact mode-two maximum
   over the complement-reduced class `Tr(Q)/n<=1/2`.  Across
   `0.925 -> 0.926` this exceeds the entire
   reviewed `1/50` margin.  Nevertheless the complete entropy response of the
   same witness at the target center is exactly
   `-3125000/8800857 < 0`.  Hence cancellation from modes `m>=3` is real and is
   precisely what noncancelling continuation bookkeeping discards.

A successful jump of width `10^-3` retaining final margin `1/200` must average
at most `15` response units per contrast unit.  Against the exact mode-two
floor, it must therefore certify more than
`3466045185/47458321 ~= 73.0334557` units of signed cancellation per contrast
unit, or couple the response to stronger `Q`-dependent base curvature.

## Reproduce

From the package root:

```bash
python3 scripts/build_obstruction_certificate.py \
  --output evidence/replay/obstruction_rebuilt.json
python3 scripts/recheck_obstruction.py \
  evidence/replay/obstruction_rebuilt.json
python3 scripts/derive_low_modes.py
python3 scripts/exact_two_site_witness.py
python3 scripts/audit_document_constants.py
python3 scripts/cover_resolution_check.py
python3 scripts/diagnostic_bruteforce_low_modes.py
python3 scripts/diagnose_split_tail_optimizer.py
python3 scripts/validate_package.py
```

Expected proof markers include:

```text
ALL_EXACT_CHECKS_PASS
INDEPENDENT_EXACT_REPLAY_PASS
SYMBOLIC_LOW_MODE_DERIVATION_PASS
LOW_MODE_NUMERICAL_IDENTITY_CHECK_PASS
PACKAGE_VALIDATION_PASS
```

The first three theorem checks use exact rational/integer algebra.  The
finite-difference regression and floating optimizer are explicitly diagnostic
and are not used to decide a claim.

## File map

- `proof.md` — complete analytic proof and exact outstanding estimate.
- `PARAMETER_REGION.md` — benchmark, certified ceilings, and strip accounting.
- `CONTINUATION_RULE.md` — legal margin and strip inclusion rules.
- `gap_audit.md` — claim-by-claim scope and unresolved target gap.
- `attempts.md` — frozen promoted attempts, failures, and diagnostics.
- `candidate_ledger.md` — three candidates scouted, at most two promoted.
- `work_log.md` — measured UTC checkpoints and elapsed-time accounting.
- `IMPORTED_INPUTS.md` — self-contained restatement of every imported result.
- `source_notes/PINNED_INPUT_LEDGER.md` — exact commit paths and provenance.
- `scripts/` — exact builder, independent checker, symbolic derivation,
  diagnostics, and package validator.
- `evidence/certificates/` — frozen exact certificate and transcript.
- `evidence/replay/` — independently rebuilt outputs.
- `checkpoints/` — concise mathematical checkpoints.
- `prior_checkpoint/` — byte-for-byte rejected prior ZIP, explicitly marked
  unreviewed and not counted as completion.
- `SHA256SUMS` — package manifest, excluding itself.

## Old/new separation

The previous ZIP is preserved only as
`prior_checkpoint/S11_quantitative_continuation_REJECTED_UNREVIEWED.zip` with
SHA-256
`7021ca3527428f1cb0f9f085ef61e5daed7f1292abead8567caa65054fb885af`.
Its microscopic rectangles are not promoted here.  The two obstruction
lemmas, low-mode identities, exact cover, witness calculation, and all new
scripts are from the resumed attempt.

## Scope

The output status is `DISPROVED_ROUTE_LEMMA`, not a target verdict.  The live
mathematical problem at `c=0.926` remains open.  The package proves that neither
adaptive reuse of the current split-tail payment nor exact mode-by-mode
nonnegative budgeting can reach it.  It does not rule out signed blocks of
modes, direct entropy-response estimates, or a continuation argument using
`Q`-specific excess base curvature.
