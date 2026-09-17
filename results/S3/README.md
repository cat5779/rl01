# S3 latest reviewed packet — 2026-09-17

**The fixed-density high-contrast sine entropy-rate concavity target remains OPEN.**

This directory records the first independent review of the previously unaudited parts of `S3_check3_cumulative.zip` (SHA-256 `be920a74ba45bf12c733e07bdf62931d9341e05cc404e34d18cb59e4f0b138d6`). Earlier S3 dependencies are treated as already accepted and are not re-certified here.

## Accepted scope

1. **Finite mesoscopic response bridge.** For fixed `0<c<1` and fixed `0<eta<(1-c)/2`, the exact latent-prefix block decomposition has weights independent of `a`, legal local kernels `aI+cQ_j^u`, and a nonnegative information remainder `E=F-G`. If `epsilon=B/n`, where `B=sum_j Tr b(Q_{B_j})`, then on `a in [eta,1-c-eta]`
   
   `sup |F''-G''| <= n C_(c,eta) epsilon[1+log(1/epsilon)]^3`.
   
   Hence `B=o(n)` implies `F''-G''=o(n)` uniformly on every fixed interior interval. Using the already accepted sine-block trace-defect bound with block length `floor(sqrt(n))` gives this `o(n)` response for the finite Toeplitz compressions. It does not sign `G''`.

2. **Two-bit payment lemma.** For every negatively correlated binary pair and every symmetric channel with `0<epsilon<1/2`, the exact output negative log-odds obeys Lemma 5.1 in `AUTHOR_PROOF.md`. This is a local scalar inequality; no compatible global allocation is inferred.

3. **Pooled per-atom obstruction.** The stated rational rank-three projection on six coordinates, at `c=99/100`, `a=1/200`, and atom `111000`, violates the proposed once-only atomwise pooled payment by more than `6/5`. Direct sums of `k` copies have pointwise defect greater than `6k/5`. The exact all-atom Hessian of the base example is below `-1000`.

## Scope boundaries

The obstruction is a finite block-diagonal direct-sum construction. It is not a contiguous Fourier projection, not a genuine continuous Fourier limit, and not a counterexample to complete expected entropy concavity. The repeated bad atom has exponentially small probability. It therefore cannot be upgraded to an expected extensive obstruction or to a counterexample to the sine target.

The remaining obligation is the actual conditioned leaf-volume bound

`sup_a G_(n,m)''(a,c) <= o(n)`

on fixed interior intervals (or an equivalent finite-Jensen estimate) for the true latent-conditioned kernels. These kernels are general finite contractions; they are not assumed to remain Fourier, projection, or constant-diagonal.

## Files and replay

- `INDEPENDENT_AUDIT.md` — independent correctness and scope review.
- `INTEGRATION_SUMMARY.md` — repository-ledger wording.
- `AUTHOR_PROOF.md` — reviewed author proof, with one malformed TeX escape repaired.
- `AUTHOR_RESPONSE_AUDIT.md`, `AUTHOR_GAP_AUDIT.md` — preserved author scope records.
- `scripts/` and `evidence/` — exact rational certificates and the high-precision decomposition cross-check.

From this directory, using Python with `sympy` and `mpmath` installed:

```text
python scripts/certify_growing_pointwise_obstruction.py
python scripts/certify_global_negative_hessian.py
python scripts/validate_center_decomposition.py
```

Expected markers are `PASS`, `PASS_GLOBAL_NEGATIVE`, and an absolute decomposition difference below `1e-55`. The random scalar-odds script is diagnostic only and is not needed for acceptance.
