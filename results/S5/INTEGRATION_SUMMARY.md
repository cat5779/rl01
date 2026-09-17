# Integration summary

## Accept

- Theorem 6.1, the balanced-midpoint actual-adjacent curvature identity, for every law on the \(m\)-subsets of \([2m]\) and every \(0<c<1\).
- Lemmas 3.1, 3.2, 4.1, 5.1; the exact normalizers (5.5); reference/Fisher formula (6.6); and square-face formula (7.1).
- The explicit statement that the Jeffreys production is nonnegative while the count-covariance term has no established favorable aggregate sign.
- The strict non-DPP exact comparison in `scripts/audit_non_dpp_check.py` and `evidence/strict_non_dpp_exact.json`.

## Correct during merge

- Do not describe the frozen weights \((1,2,3,4,5,5)/20\) as non-DPP.  Call them a general rational homogeneous input.  Use the new \((10,1,1,1,1,10)/24\) case when a certified non-DPP comparison is needed.

## Retain as open

- Central payment inequality (8.1).
- Weaker full-entropy midpoint inequality (8.2).
- Any nonzero interval or fixed-chord theorem.
- Thermodynamic differentiation and Toeplitz Hessian transfer.
- The sine entropy-rate target and its sign.

## Do not promote

- The prior round-4 \(O(\sqrt n)\) residual payment.  It is not used by the accepted theorem and remains unreviewed in this integration.
- Finite Fourier diagnostics as an all-\(n\) sign theorem.
- Nonnegativity of individual raw edge summands.

Source archive: `[LOCAL_USER]/Desktop/20260907/S5_round5_actual_adjacent_core.zip`  
Verified SHA-256: `663067de725355379900731faadb43d99f40e2bf828b7a96366b5bb9021ec4f6`.

This directory is ready to merge as `research/s5-latest-reviewed-20260917/`; it contains no nested `research/group/research` hierarchy and does not alter the repository root README or manifest.
