# Exact dependency delta

Frozen accepted baseline: `aaf3e86576a867067701089805c9e5e5a83e44f5`.
Task branch starts at `9f20b96daaa9ba4cbf89ef6f04abc5cd167d0225`.
All paths below are relative to the repository root. No unreviewed contrast
extension is an input. The ultimate sine concavity target remains unresolved.

## Imported baseline results, and where they are actually used

| Path and section | Imported claim | Use here / new step not imported |
|---|---|---|
| `research/s9-noise-flow-finite-band-20260916/RESULT.md`, Section 2, full noise identity and localization theorem | Full entropy production integrates to `log 2-h`; the integrated error between full production and radius-r production is at most `H_(r+1)/(r+1)-h`. | Main Sections 1,4,5. The block length is r+1. The new step multiplies a conditional count CLT by the actual local production weight and bounds replacing that weight by the full predictor. |
| Same file, Section 3.3, equations (3.7)-(3.9), and Section 3.4 | Strict-strip block error at most `sum min(k,n)|fhat(k)|^2/[epsilon(1-epsilon)n]`; Fejer multipliers do not increase this Fourier energy. | Produces the explicit uniform `E_(r+1)`. This is an entropy VALUE/localization bound, not an imported derivative estimate. |
| Same file, Section 4.2, equation (4.3) | Interval Fejer L1 error `eta_R=min(1/2,(log(R+1)+1/2)/(R+1))`. | Used in defect and kernel comparisons; the short interval proof is also included in Main Section 2. |
| Same file, Section 4.3 and Section 5.3.1-5.3.4, especially (5.5)-(5.8) | Stationary coupling and common-flip proof give the FULL-production absolute-integral modulus `2b(||f-g||_1)`. | Main (5.1) pays the changing Fejer kernel and changing original shift after local-to-full comparison. It is not applied directly to one finite center. |
| Same file, Section 6.3, equations (6.2)-(6.3) | Explicit finite-Jensen to entropy-rate VALUE transfer. | Main Section 9 compares the order of this error with the critical chord's order-1/R margin. It explains why the present theorem does not pay the remaining sign. |
| `research/s9-round2-sign-certificates-20260916/FULL_R3_PRODUCTION.md`, full-production theorem | At half density, degree/context 3 has `I_3,aa>=6u^2` in the stated contrast/shift domain. | Baseline and candidate A only. Not rerun, not extended by induction, not used to prove the Gaussian compensation. |
| `research/s9-round2-sign-certificates-20260916/GROWING_RESULT.md`, growing central-band and weak-limit theorems; `repair-review/INDEPENDENT_AUDIT.md` | Fixed-chord negative mass persists; some nearby shifts have large negative band curvature; no full signed-sum sign follows. | The new theorem instead treats delta=theta/sqrt(R), proves actual midpoint band curvature `-R C+o(R)` and its complementary `+R C+o(R)`, with an explicit positive C. The previous radius 160001 is not reused. |
| `research/s9-round2-sign-certificates-20260916/LAYER_MEASURE.md` | Macroscopic signed-layer weak limit, not total-variation-distance convergence. | Comparison point only. The new fluctuation-scale law is Gaussian, not a macroscopic moving Dirac law. |
| `STATIONARY_STATUS.md`; `research/s23-reviewed-20260916/METHODS_AND_NEXT_ROUND.md` | Reviewed universal 37/40 region; failed latent-completion, tangent-only and fixed-layer routes. | Scope and overlap checks. No tiny contrast extension, spectral entropy substitution, or inherited unproved posterior-tail lemma is used. |

## New finite and asymptotic steps proved in this packet

1. All-word conditional rank/trace comparison and an elementary Lindeberg
   bound, combined with local predictor replacement, give a quantitative
   **production-weighted** Gaussian limit for aligned growing Fejer kernels.
   This is Main Sections 2-5, not just a citation to a count CLT.
2. A concrete martingale translation coupling gives exact leading signed
   compensation and a positive transport cost. Main Sections 6-7 compute the
   midpoint central-band/complement constants, including `C>1/140` at c=19/20.
3. Complex complete-event determinant domination at imaginary shifts of
   size R^(-1/2) gives a locally bounded holomorphic family. Cauchy's formula
   justifies actual derivatives of the mesoscopic limit (Main Section 8).
4. The fixed spectral observation channel gives finite full-law score and
   acceleration bounds in terms of the retained defect `Tr Q(I-Q)`, plus an
   explicit likelihood KL bound to a count tilt. Score Sections 1-2 prove this
   directly, without claiming that configuration entropy is count entropy.
5. Score Section 3 separately accounts for `a g+2s g'+g''`, yielding a parallel
   author proof of the second derivative theorem. It is not an independent
   referee report.
6. The general-density note explicitly changes the count center, variance,
   strip, error terms, and analytic constants. Exact degree alignment is stated
   on the unbounded subsequence with nonzero top Fourier coefficient.
7. The growing layer-bistochastic-channel obstruction retains full spatial
   entropy and proves a positive n^(3/2) curvature asymptotic. Such a channel
   cannot be the exterior powers of one unitary; it is NOT a DPP counterexample.
8. The four-site Fourier external-field obstruction has exact rational atoms
   and analytic logarithm bounds. It rejects a surrogate path, not the actual
   common affine shift.

## External references

Primary sources and their precise scope are recorded in `REFERENCES.md`.
Soshnikov's scalar CLT, Shepp-Olkin count entropy, likelihood approximations,
and quantum entropy results do not supply the weighted theorem or its sign.
No claim of literature-wide priority follows from this search.
