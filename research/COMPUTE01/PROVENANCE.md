# Provenance and non-overlap

- Task source: `results/SA03/COMPUTATION_HANDOFF.md`,
  `results/SA04/COMPUTATION_HANDOFF.md`, and
  `results/SA05/SA05_HANDOFF.md` on RL01 `main` at `11d385b`.
- Selection reason: these handoffs explicitly require local enumeration,
  parameter search, high-precision or interval error propagation, and repeated
  runtime validation. They are poor fits for a browser-only derivation session.
- PR #2 studies a new analytic sign tool for SA03; C03 is only its computational
  companion and will not claim the same theorem without a certificate.
- PR #4 studies a new analytic cancellation tool for SA04; C02 builds the
  reduced numerical experiment requested by the old handoff.
- PR #3 studies SA02 and is outside this branch.
- The SA01 and SA02 proof-construction tasks were not claimed because they are
  primarily analytic and already have suitable browser-PRO assignments.

The original SA author status remains historical metadata. A successful run is
not an independent proof audit, and a finite certificate is not a growing-volume
theorem.

