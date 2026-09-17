# Reproduction and certificate guide

The analytical proof is the primary deliverable. These Python files are
same-author exact-arithmetic supporting certificates, not an independent
mathematical review. They require only the Python standard library.

From this staged directory run:

```sh
python code/verify_pair_witness.py --output rerun/pair_witness.raw.json
python -O code/verify_pair_witness.py --output rerun/pair_witness_optimized.raw.json
python code/verify_identities.py --output rerun/identities.raw.json
python -O code/verify_identities.py --output rerun/identities_optimized.raw.json
python code/verify_localization.py --output rerun/localization.raw.json
python -O code/verify_localization.py --output rerun/localization_optimized.raw.json
```

Expected statuses are `CERTIFIED_FINITE_ROUTE_OBSTRUCTION` for the pair
witness and `PASS` for the identity/localization runs. The validators use
explicit exceptions rather than `assert`, so `python -O` does not remove the
checks.

To compare a rerun with the committed certificate JSON, remove only
`elapsed_seconds_diagnostic`, then serialize with
`json.dumps(obj, separators=(',', ':')) + "\n"`. Each normal/optimized pair
is byte-identical after this canonicalization. Exact committed hashes and raw
run hashes are in `checks/RECEIPT.json`.

The pair witness enumerates all 64 atoms and all 16 outside words with rational
outward intervals. At `n=6`, `rho=1/2`, `c=19/20`, `a=1/40` it certifies

`37/100000 < E g_{1,6} < 39/100000` and `-50 < H_6'' < -49`.

This is a counterexample to pairwise averaged nonpositivity, not to entropy
concavity. Its logical payload also reproduces the historical pretty-printed
canonical SHA256 `2ca70c96b9f5991f6fc2b13adfc295b94abd9d6cf5809051e153445f3989cc3a`.

`verify_identities.py` reports 1004 exact rational checks of the finite
complete-word, channel/posterior, inverse, pair-completion, commutator, jet,
posterior-mean, and variance identities. `verify_localization.py` reports 8049
exact checks over 168 finite D/F/channel cases, including both all-one and
all-zero fixed-completion choices and the actual-weight likelihood payment.

The scripts do not replace the analytical proof of Theorems A--F, the sine
`n/R` tail, boundary constants, or the thermodynamic passage. Independent
review remains pending.
