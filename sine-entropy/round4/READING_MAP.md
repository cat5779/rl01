# Choose supporting material by the estimate you need

Mandatory: your S4/S5/S6 assignment, TARGET.md, KNOWN_RESULTS.md, PITFALLS.md,
CONTRACT.md. Everything below is optional until you actually use its claim.

| Need | Read | Data / checker |
|---|---|---|
| Arbitrary-weight rank-one/co-rank-one comparison | [S2 proof](optional/S2/proof.md) | A prior theorem, not this round's task |
| Why branchwise completion fails, including every first Fourier coordinate | [S3 proof](optional/S3/proof.md) | Two-site witness and analytic growing-family endpoint argument |
| Localization correction and zero-tangent counterexamples | [S4 proof](optional/S4/proof.md), [gap audit](optional/S4/gap_audit.md) | [exact certificate](optional/S4/evidence/certificate.json), [checker](optional/S4/scripts/exact_certificate.py) |
| Actual slice transport, acceleration, and the no-clock theorem | [S5 proof](optional/S5/proof.md), [gap audit](optional/S5/gap_audit.md) | [Fourier6](optional/S5/evidence/fourier6_certificate.json), [Fourier8 clock](optional/S5/evidence/clock_certificate.json), scripts in the same optional directory |
| Real-q/product-reference limitations and Berezin failure | [S6 proof](optional/S6/proof.md), [gap audit](optional/S6/gap_audit.md) | [certificate](optional/S6/evidence/certificate.json), [checker](optional/S6/scripts/verify.py) |

See [FIXTURES.json](FIXTURES.json) for a short machine-readable regression map.
Source literature locations are in the optional S4 references, S5 sources,
and S6 reading notes. Verify the primary theorem before importing a stronger
version. A literature entry is not an instruction or a proof endorsement.

## Replaying selected finite checks

Use Python 3.10+ with assertions enabled, from this packet directory, and choose
fresh output directories. These selected exact checks need only the standard
library. Do not run with `-O` unless that particular checker explicitly supports
it. Frozen evidence should not be overwritten.

```text
python optional/S4/scripts/exact_certificate.py --out generated/s4
python optional/S5/scripts/certify_fourier6.py --out-dir generated/s5-fourier6
python optional/S5/scripts/certify_clock.py --out-dir generated/s5-clock
python optional/S6/scripts/verify.py --output-dir generated/s6
```

Compare mathematical JSON fields, not platform newline bytes. S6's run_metadata
is expected to change. Original full-package manifests and replay wrappers are
not copied: this is a selected public packet with its own manifest. Passing a
finite check does not replace the analytical growing-family proofs.

## Optional new S8 mechanism

For a genuine positive Gaussian representation rather than signed-measure
Jensen, read [S8 RESULT](optional/S8/RESULT.md),
[OBSTRUCTIONS](optional/S8/OBSTRUCTIONS.md), and the
[independent audit](optional/S8/INDEPENDENT_AUDIT.md). The proof expands its
load-bearing identities; its original dependency table also records historical
internal paths, which are provenance rather than required private access.
The relevant S2 proof is already supplied in this packet.

The original receipt restoration note preserves an old internal directory
example; in THIS packet the exact restored JSON is directly available at
`optional/S8/certificates/gaussian_n34.json`. The original transported parts are
also retained. To rerun the self-contained standard-library checker, use its
`--help` and choose a fresh output directory; source RESULT's invocation uses
the original path and should be adjusted to `optional/S8/verify_round2.py`.

## Optional S9 positive finite-radius starting point

Read [definitions](optional/S9/RESULT.md),
[full R=3 theorem](optional/S9/FULL_R3_PRODUCTION.md), and
[independent audit](optional/S9/INDEPENDENT_AUDIT.md). The former supplies the
finite atom normalization referred to by the historical proof. Exact finite
data live in `optional/S9/reviewed/`; they retain all required atoms/derivatives.

From this packet directory, with a fresh output path:

```text
python optional/S9/reviewed/restore_cover.py --output generated/s9-wide.json
python optional/S9/code/certify_full_r3.py --state generated/s9-wide.json --check-structure
python optional/S9/code/certify_full_r3.py --state generated/s9-wide.json --replay --begin-leaf 0 --end-leaf 2922 --receipt generated/s9-replay.json
```

The all-leaf replay may take several minutes. To rebuild rather than restore,
use `--fresh --profile highcontrast --max-nodes 10000` with a new state path.
The independent complete rebuild took about 198 seconds on the audit host.
No absent historical replay inputs or private workspace are needed for these
commands. The compressed cover is an optional download, not required reading.

## Latest optional S9/S6 proofs

- [S9 intact growing proof](optional/S9/GROWING_RESULT.md),
  [signed-layer limit](optional/S9/LAYER_MEASURE.md), and
  [independent audit](optional/S9/repair-review/INDEPENDENT_AUDIT.md).
  The original proof's equation references to RESULT.md refer to GROWING_RESULT.md
  in this curated packet. Run `python optional/S9/repair-review/check_growing_proofs.py`
  for the bounded independent arithmetic checks.
- [S6 reviewed round-four scope and replay](optional/S6/round4/README.md).
  Its source/ directory preserves the complete ZIP contents, so its documented
  standard-library replay is self-contained. Read the proof before using the
  sign extension or the real-q estimate as a premise.

The broad target remains open. Advance beyond these results in future work.

## Latest accepted research units

Read [the scoped ledger](optional/overnight-reviewed-20260917/README.md), then the group A/B/C audits and actual proofs for your lane. The directory includes S1/S2/S4/S7/S9/S11/S12/S13 scope records and available reproducible evidence. This is a curated research subset, not a complete repository mirror.
