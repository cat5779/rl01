# Candidate freeze — S7 / PR111

This is a prospective statement, not yet an accepted theorem.

Observed runtime UTC: 2026-09-16T17:16:54Z (the assignment is labelled 2026-09-17).
Baseline: aaf3e86576a867067701089805c9e5e5a83e44f5.

## Main candidate

For the actual sine Toeplitz compression Q_n, 0<c<1, a>0, d=1-a-c>0,
put delta=min(a,d). For the exact two-site conditional Hessian functional
`g_ij`, averaged under the actual outside-output law, prove

`2 sum_{i<j, j-i>=R} E |g_ij| <= 3 n c^4/(16 delta^8 R)`

for every n and every positive integer R. The absolute value is inside the
sum and expectation; hence this bounds the actual signed curvature remainder.

Mechanism: exact full-word pencil A_y=aI+cQ_n-diag(1-y), its word-uniform
inverse gap, bounded phase commutators, and two-site Schur complements.
The pencil/gap are already present in reviewed S6 and are not new results.
The proposed new step is the spatially uniform commutator-to-curvature tail.

Quick falsification checks: (i) reproduce the complete four-atom mixed Hessian,
(ii) check the Schur identity for each of all completions of an outside word,
(iii) check the Fourier translation/Parseval constant and ordered/unordered
pair factors, and (iv) confirm that no changing-law derivative is discarded.

## Secondary candidate

A word-uniform polynomially weighted inverse estimate may control changes of
local conditional kernels when distant output coordinates are discarded. This
would be a genuinely spatial result, not an entropy value-to-Hessian shortcut.
All constants and dependence on delta must be proved explicitly.

## Explicit nonclaims

Neither candidate establishes the sign of the near-pair sum. No endpoint-
uniform estimate, full sine concavity, independent review, or novelty priority
is claimed. Mere C^2 convergence of normalized entropy may already follow from
the reviewed S6 response theorem plus value tails; it must not be claimed as
an independent new discovery here.

## Enhanced candidate — observed UTC 2026-09-16T17:26:19.605240+00:00

For the actual posterior of the latent input on B=[1,n], propose

`E sum_{i,j in B, |i-j|>=R} |R^Y_ij|^2 <= 7 n/(4 R)`.

The proof uses conditional-variance contraction with a phase-modulated
plateau/tent test function on a larger finite sine compression. It never
assumes Q_n itself is a projection. The tent has squared norm <=2n and
prior commutator energy <=12/pi^2. Its boundary cost is absorbed by n/R
for R<=n; R>n is vacuous.

With beta_*=min(a(a+c),d(1-a))=delta(delta+c), the exact signed-pencil/
posterior relation gives an averaged inverse tail
`<=7 n c^2/(4 beta_*^2 R)`.

For a conditional pair, put xi=s/(p00 p11), u=p00+p11. The exact
ratio of |g| to the conditional mean of |G_ij|^2 is bounded by
`max(1,log theta)`, theta=(a+c)(1-a)/(a d)=1+c/(a d).
This could improve the curvature tail to
`7 n c^2 max(1,log theta)/(4 beta_*^2 R)`.
All constants and the completion averaging still require proof audit.

## Boundary obstruction candidate — observed UTC 2026-09-16T18:28:34.233221+00:00

At rho=1/2, a=(1-c)/2, n=2M+1, with even sites empty and odd sites occupied on {0,...,2M}, conjecture/prove

`(2M) |G_{0,2M}| >= 16 c^2/[pi^2(1+c^2)^2] sum_{l=0}^{M-1} 1/(2l+1)`.

Mechanism: parity block-square identity and the missing exterior Hilbert-kernel columns. After a fixed alternating phase gauge, their Gram matrix is entrywise nonnegative, so a Neumann series gives a lower bound. Quick falsification tests: sign of the exterior-column Gram entries, exact ambient H H*=I/4, midpoint diagonal +/-1/2, and the telescoping endpoint sum. If established this rules out a uniform 1/r bound for all finite words, not the averaged tail or the sine entropy target. It is a refinement/obstruction within the already frozen weighted-inverse attempt, not a new unrelated promoted method.

## Averaged coarsening refinement — 2026-09-16T18:38:00.942375+00:00

Refinement of promoted attempt A, not a third independent program. Couple two full outside words independently given the retained local observations, use one common forced pair completion, then the resolvent identity and Cauchy–Schwarz. The two marginals are the actual outside law. Candidate: averaged local-curvature replacement error is bounded by a noise-dependent constant times R/L, using the already proved actual-law squared-inverse tail. The common-completion change of measure and pair multiplicity constants require the next audit. No new sign is asserted.

## Author resolution — 2026-09-16T18:45:11.824396+00:00

The main and secondary candidates now have complete author proofs. The
posterior energy constant was improved from the prospective 7/4 to 3/2.
The averaged coarsening refinement is Theorem F, with observation error
`B_* delta^(-4) [m^(-1)+156(R-1)m^(-2)]/L` and the explicit finite-volume
boundary term. The alternating-word obstruction was strengthened to a
positive-power lower bound, excluding fixed-polylog/r as well as 1/r.
All statements remain pending independent review; near-field sign and the
full target remain open. The prospective entries above are preserved.
