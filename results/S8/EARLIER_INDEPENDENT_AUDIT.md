# Independent S8 round-two audit

## Verdict

**STATUS: CORRECT for the scoped mathematical claims.**

The frozen PR 101 head `ed2d4e4ad78f92395ac1651602dfa530617b16f3`
contains a correct proof of the stated rank-two four-cycle curvature comparison,
correct connected examples in every ambient dimension, a correct finite
`Pi_{5,2}` specialization, and correct exact obstructions to two proposed proof
extensions. It does **not** prove the main fixed-density sine Toeplitz entropy-rate
concavity target, and the packet says this accurately.

The main goal therefore remains **OPEN**.

## Load-bearing proof audit

1. The two-row block
   `sqrt(1-s) I + i sqrt(s) [[0,1],[1,0]]` is unitary. Acting on a real
   two-column frame makes each affected squared minor the affine interpolation
   of its two endpoint squared minors. Thus the whole chord consists of genuine
   complex Hermitian rank-two projection DPPs; projection compatibility is not
   assumed from convexity.

2. The complete output atom formula
   `q_s(T)=a^(|T|-2)(1-a)^(n-|T|-2) det(xI+cM_T^s)` follows from the channel
   likelihood and Cauchy--Binet. Under the two-opposite-difference hypothesis,
   `partial_s q_s(T)` is supported exactly on outputs choosing one coordinate
   from each distinguished pair. Squaring it and dividing by `q_s(T)` cancels
   the problematic powers of `a(1-a)` exactly, giving equation (11).

3. The complex two-dimensional Gaussian identity for `1/det(A)` is used only
   for the positive matrix `A=xI+cM` in the legal interior. Summing the outside
   subsets gives equations (13)--(14) with no omitted output words.

4. With `r_v=1-exp(-cE_v)`, direct differentiation gives
   `(log G)''=2R-sum r_v^2/(1-ar_v)^2`. The elementary bound
   `(1-exp(-u))^2 <= u/2`, the legal-domain inequality `1-ar_v>=c`, and the
   outside frame operator bound give
   `(log G)'' >= (2-beta/(2c))R`. This is nonnegative exactly when
   `c>=beta/4`.

5. The quantitative lower bound is also correct. Each of the four terms in
   `C_s` is at least `exp(-cR)`, the outside product is at least
   `exp(-ac sum_O E_v)`, and `c+x+ac=c+a-a^2<=1`. Hence
   `C_sG_s>=4exp(-R)`. Since the complex Gaussian moment is
   `integral R exp(-R) d^4z/pi^2=2`, equation (18) follows. Integrating against
   the Dirichlet Green kernel, whose mass is `t(1-t)/2`, gives exactly
   `D_t'' >= 2c^3(4c-beta)eta^2t(1-t)`.

6. The Green identity uses the exact affine-in-`s` full law, so it retains both
   the `a`-acceleration and `a`-Fisher terms. Endpoint convexity follows from
   finite-law continuity; no endpoint second derivative is claimed.

## Specializations and contribution

- The growing family is a real rank-two isometry: its column Gram matrix is
  `I_2`, `eta=1/8`, and the outside operator is `diag(0,3/8)`, so `beta=3/8`.
  Its covariance support graph is connected. Its rank stays two while ambient
  dimension grows, so its density tends to zero.
- For the genuine consecutive Fourier projection `Pi_{5,2}`, the real gauge is
  valid, `eta^2=1/125`, and the one spectator row gives `beta=2/5`. The stated
  threshold `c>=1/10` and lower bound in equation (22) follow from Theorem 1.
- The four-site fixed-diagonal extension is also correct. Only size-two output
  atoms vary; the projection endpoint bounds put the two auxiliary roots in
  `[0,1]`, yielding `(1/q_s)''>=4` and equation (24).
- This is a genuine advance over the prior rank-one result: it controls a
  coupled rank-two projection chord through a two-complex-dimensional
  inverse-determinant representation and a shared row-energy budget. It is
  still a comparison theorem, not an absolute concavity theorem.

## Obstructions

- The four-site rotation certificate correctly refutes the proposal that a
  monotone real leverage-balancing rotation with positive endpoint entropy gain
  must have a convex gain in `a`. Both endpoint entropy Hessians remain negative,
  so it is a route obstruction rather than a target counterexample.
- Equations (B2)--(B5) correctly identify the signed multi-edge extension. Same
  sign pairs have negative coefficients, so the four-cycle proof does not
  extend by termwise convexity.
- The 34-site connected projection correctly gives a negative second derivative
  for the full outside-word-summed Gaussian density at the displayed point.
  Its integrated Fisher second derivative and actual curvature gain are
  positive, so this refutes only pointwise density convexity.

## Exact replay and provenance

- The snapshot records PR 101 head
  `ed2d4e4ad78f92395ac1651602dfa530617b16f3`. Every listed source byte length,
  SHA-256, and Git blob SHA matches `snapshot.json`.
- The checker passed normally and with `-O` under Python 3.12.14. Both runs
  emitted all seven expected PASS lines.
- The generated receipts are semantically identical to the frozen receipts.
  After converting Windows CRLF to canonical LF, every generated receipt has
  the exact SHA-256 recorded in `RUN_RECORD.json`. Raw Windows hashes differ
  only because `Path.write_text` translates newlines on this platform.
- Concatenating, decoding, and decompressing the five 34-site transport parts
  produced gzip SHA-256
  `47562250ab85e1d160419100f1fd95a665be2628ecc8e487bcc5193abd2c3cc5`
  and JSON SHA-256
  `ea2d502f3592e1af4402aa3f9b8eda9f3d7fb82f4cb39ca5b1047b326d17e322`,
  exactly as documented.
- The recorded research span is internally consistent: 7316.11882 seconds
  (121 minutes 56.11882 seconds), with the run record declaring no sleep/idle
  padding and no early-stop exception. This audit can check arithmetic and
  record consistency, not independently reconstruct historical activity.
- The branch packet explicitly says the root `MANIFEST.sha256` was not safely
  rewritten and must not be reported as passing. That is a disclosed,
  repairable packaging limitation and does not affect the frozen S8 file/blob
  verification above.

Logs are in `audit/replay/*.log`, `audit/hash_audit.log`,
`audit/normalized_hash_audit.log`, `audit/environment.log`, and
`audit/timing_audit.log`.

## Exact remaining gap to the main target

The theorem gives `H_t''-H_0'' >= 0`; it gives no upper bound on `H_t''`.
Closing the actual sine Toeplitz entropy-rate target still requires all of:

1. a finite fixed-positive-density Jensen/curvature sign for the genuine sine
   approximants;
2. control of the signed same-sign terms in the multi-edge formula, or a
   different representation that retains their cancellation;
3. an iterable projection-compatible path to a reference law with known
   absolute sign; and
4. the already-reviewed finite-to-Toeplitz transfer only after that missing
   finite sign is proved.

Neither the direct-sum density-`2/5` corollary nor the isolated `Pi_{5,2}`
comparison supplies these steps.
