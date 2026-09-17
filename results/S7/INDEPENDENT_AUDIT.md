# Independent audit — S7 certificate delta / PR111

## Verdict

**STATUS: CORRECT for the newly supplied certificate unit.**  The prior audit
accepted the analytic localization theorems and withheld only the absent
six-site and finite-algebra payloads.  This audit covers the new three scripts,
six JSON payloads, updated receipt, and reproduction instructions.  It does
not reopen the analytic proof.

## Reproduction results

- `verify_pair_witness.py`, normal and optimized: certified all 64 atoms and
  16 outside words and reproduced
  `37/100000 < E g_(1,6) < 39/100000` together with
  `-50 < H_6'' < -49`.
- `verify_identities.py`, normal and optimized: `PASS`, 1004 exact rational
  checks.
- `verify_localization.py`, normal and optimized: `PASS`, 8049 exact rational
  checks over 168 finite cases, including 96 all-one and 72 all-zero fixed
  completions.

After removing only `elapsed_seconds_diagnostic` and using the documented
compact JSON serialization, each normal/optimized pair was identical and each
rerun was identical to the corresponding committed payload.  Canonical hashes:

- pair witness: `dd172332e7edd7af8cc4fff1978f2e356af8c40dd3ca8282553595c50a2ba61c`
- identities: `01a7c81b2952f711b7792cf96e024d6e01c3be9b406f6daae7cd6518b6eb9a14`
- localization: `f94a2b9abbaa9603f9121ee9d3aebfa0f848680358791f9559b54a0415759014`

The six-site result is a finite route obstruction to pairwise averaged
nonpositivity.  Its total six-site Hessian is negative, so it is not an entropy
concavity counterexample.  The identity and localization scripts certify their
finite algebra fixtures; they do not numerically prove the sine tail,
thermodynamic passage, or entropy-rate sign.

