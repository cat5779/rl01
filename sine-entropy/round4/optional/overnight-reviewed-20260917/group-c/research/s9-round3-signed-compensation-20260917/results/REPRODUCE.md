# Reproduce

These are author checks, not an independent review and not a finite certificate of the asymptotic theorem.

From `research/s9-round3-signed-compensation-20260917/results/` run:

```text
python verify_exact_identities.py
```

The script checks all 16 complete atoms in each finite score case, exact first/second complete-law jets, the spectral observation-channel identities, the four-site external-field obstruction, the rational lower bound `C_(1/2)(19/20)>1/140`, and the identity for `phi''`. A passing run regenerates `EXACT_CHECK_RECEIPT.json`.

The asymptotic Gaussian-mixture limit, signed compensation, and derivative passage are analytic arguments in the Markdown proofs; the script explicitly does not certify those limits by finite sampling.
