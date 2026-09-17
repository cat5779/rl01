# Reproduction and certificate guide

The principal deliverable is the analytical proof in the Markdown files.
The scripts are exact-arithmetic supporting certificates, not a code task or
an independent mathematical review. They need only Python's standard library.

From this results directory run:

```sh
python verify_pair_witness.py --output checks/pair_witness.json
python -O verify_pair_witness.py --output checks/pair_witness_optimized.json
python verify_identities.py --output checks/identities.json
python -O verify_identities.py --output checks/identities_optimized.json
python verify_localization.py --output checks/localization.json
python -O verify_localization.py --output checks/localization_optimized.json
```

The expected statuses are CERTIFIED_FINITE_ROUTE_OBSTRUCTION for the first
pair and PASS for the other four runs. These scripts use explicit failures,
not Python assert statements whose removal could invalidate the optimized
checks. The last script imports the exact fixture utilities from
verify_identities.py; keep the files together.

`pair_witness.json` contains every atom polynomial, all outside-word
contributions, rational interval endpoints, and strict rational inequalities.
`identities.json` reports 1004 exact algebra checks, including a nonprojection
fixture, actual posterior normalizers, inverse/pair identities, full jets,
and the canonical posterior mean. `localization.json` reports 8049 checks
across 168 set/observation/channel cases, including both common-completion
choices and the actual-weight likelihood payment.

The normal and optimized JSON files have identical mathematical payloads;
the key `elapsed_seconds_diagnostic` naturally differs. `checks/RECEIPT.json`
records the comparison. Printed decimal interval values are convenience
only; the exact rational endpoints are the certificate.

These finite checks do not validate an infinite parameter domain by sampling.
Theorems A--F and all boundary constants must be checked from their proofs.
In particular, the six-site total entropy curvature is negative: this is a
counterexample to pairwise averaged nonpositivity, not to entropy concavity.

SHA256SUMS within this directory, when supplied, lists delivered files except
itself. Diagnostic wall-clock durations will change on reruns, and that will
change the hashes of the regenerated receipts; this is expected.
