# Independent audit — S7 / PR111

## Verdict

**ACCEPTED_SCOPED / PARTIAL_OVERALL.** The analytic spatial-control unit is
accepted at frozen head `5950f93b927bad324f48dff7f17896e6554d645e` against
baseline `aaf3e86576a867067701089805c9e5e5a83e44f5`. The sine entropy-rate
concavity target remains open.

## Accepted statements and exact scope

1. For every finite interval `B={1,...,n}`, every one-interval sine Toeplitz
   compression of density `0<rho<1`, every strict channel
   `0<c<1`, `0<a<1-c`, and every positive integer `R`, Theorem A's complete
   labelled-Shannon Hessian identity and absolute far-pair bound are accepted:
   `2 sum_{i<j, j-i>=R} E|g_ij| <= n C(a,c)/R`, with `C(a,c)` exactly as
   displayed in `results/PROOF.md`. This accepts the acceleration and mixed
   Fisher terms together; it does not assign a sign to the near-pair sum.
2. Under the same finite actual law, Theorem B is accepted:
   `E sum_{|i-j|>=R}|R^Y_ij|^2 <= 3n/(2R)`. The proof correctly uses
   conditional-variance contraction and the ambient Fourier projection only
   after a finite-support cutoff; it does not treat the finite compression as
   a projection. The word-uniform inverse estimate of Theorem C and the
   actual-law averaged inverse estimate are also accepted with their stated
   `delta` and `beta_*` constants.
3. Theorem F is accepted for all positive integers `n,R,L` and all
   `0<rho<1`, at fixed strict channel parameters. Its finite conditional-table
   formula has paid errors `C_*/R`, `O_(a,c)(R/L)`, and the displayed finite
   boundary term. The fixed-completion likelihood payment, table tower rule,
   pair multiplicity, and passage to the stationary `C^2` limit are accounted
   for. The resulting `n^(-1/4)` finite-volume rate is accepted with the
   conservative constant stated there.
4. The one-sided Corollary G and the word-uniform weighted inverse/locality
   estimate in `QUASILOCALITY.md` are accepted in their stated strict-channel
   scope. Proposition D's posterior-mean identity and Corollary E's matching
   `n/R` lower order at `rho=1/2`, `n>=4R`, are also accepted.
5. The alternating-word analytic obstruction in `OBSTRUCTIONS.md` §4 is
   accepted: at `rho=1/2`, `a=(1-c)/2`, the growing actual Toeplitz family
   rules out a word-uniform `C/r` inverse bound and every fixed-polylogarithmic
   multiple of it. This is not an averaged-law or entropy-sign counterexample.

## Partial and rejected units

- **PARTIAL:** no upper sign bound on `K_(R,L)` pays the positive localization
  errors in the requested high-contrast range. There is no endpoint-uniform
  estimate, improved contrast threshold, full-interval concavity certificate,
  or resolution of the near-field sign.
- **CRITICAL GAP (certificate packaging only):** `results/REPRODUCE.md` and
  `results/checks/RECEIPT.json` refer to `verify_pair_witness.py`,
  `verify_identities.py`, `verify_localization.py` and generated JSON payloads,
  but none of those scripts or payloads is present in the PR111 results tree.
  Therefore the six-site rational witness `37/100000<E g_(1,6)<39/100000`,
  `-50<H_6''<-49`, and the receipt's 1004/8049 check counts are **not accepted
  as independently reproduced certificate units** in this integration. The
  receipt is retained only as author provenance. This does not undermine the
  accepted analytic Theorems A--F, whose proofs do not depend on those scripts.

## Verification performed

The proof was checked from the complete-word determinant through the posterior
kernel, conditional variance, bounded-phase tail, completion averaging,
scalar `g` bound, actual-law coupling, table Lipschitz bounds, boundary counts,
and limit passage. No unreviewed earlier proof was re-audited; explicitly named
baseline identities were used only at their already-reviewed scope.

