# Dependency and contribution delta

Baseline: `main@6242dc3206ff196dc15b9dbfb0e41971844cecdc`, incorporated into the
existing S8 branch by merge `f265c68d798f9d7e6ad2f01ef57fa0745b768e2a`.
The updated task blob is `11bef38d37ae2e24815fcbbef88e3454d52b1430`.
Prior S8 artifacts and reviewed S9 repairs are not changed by the new proofs.

| Exact path and section at the baseline | Hypotheses / accepted role | Imported unchanged | New step in this packet |
|---|---|---|---|
| `research/s23-reviewed-20260916/source/s2/proof.md`, Sections 3--4, especially (3.1), (4.1)--(4.6) | Realizable rank-one singleton weights; `c>=1/2`; complete channel law | The successful proof strategy: exact atom pairing, positive integral, common-shift log-convexity; the elementary inequality `(1-e^-u)^2<=u` | Rank-two determinant atoms; explicit affine chord of **projection** laws; four-cycle cancellation; a `C^2` Gaussian inverse-determinant integral and outside operator budget; (15a) sharpens the elementary scalar estimate to `u/2`. The proof and sign are supplied, not assumed |
| Same S2 file, Sections 2 and 5--6; `S2_INDEPENDENT_AUDIT.md` | Arbitrary rank-one/co-rank-one, `n>=2`, `1/2<=c<1`; full curvature bound `-4n(n-1)/(n+2)` | Scope and comparison baseline only | The new theorem does not deduce a rank-two result by falsely applying this rank-one bound. It proves a higher-rank **curvature difference**, not a new absolute entropy bound |
| `research/s23-reviewed-20260916/source/s2/attempts.md`, Section 5 | Exact five-bit homogeneous **non-DPP** obstruction | Unrestricted homogeneous smoothing is unavailable | Every intermediate input in the positive theorem has an explicit common two-column isometry; two new obstructions themselves use genuine projections |
| `research/s23-reviewed-20260916/S3_INDEPENDENT_AUDIT.md`, Sections 1--3 | Completion (C) fails, including every-first-coordinate Fourier endpoint examples; endpoint neighborhoods dimension dependent | Exclusion of that sufficient condition and scope warning | No completion inequality or shrinking endpoint neighborhood is used |
| `research/s8-finite-jensen-20260916/SUPPLEMENT.md`, Sections 5 and 7 | Johnson exchange identity for any homogeneous law; noisy eight-site count-layer obstruction | Existing identity/obstruction are acknowledged, not relabeled as new | The new object is an interpolation Fisher representation with a proved sign under a compatible circuit condition; neither old identity is a proof dependency |
| `research/s789-reviewed-20260916/README.md`, accepted S8/S9 results and repairs | S8 full-law transfer; S9 integrated localization/stability with repaired endpoint-log-Lipschitz/KL proof | Their availability and review status only | No new finite sine Jensen sign has been established, so the transfer is deliberately **not invoked** to claim a sine-rate result |
| `research/n4-transposition-c1-20260914/GATE.md`, (3) and remaining obligation; `STATUS_AND_HANDOFF.md` | Existing general N4 transposition research remains scoped/incomplete | Avoid claiming that a special comparison settles the general C1 gate | This packet supplies an all-ambient-dimension compatible four-cycle comparison and exact limits of two proposed extensions, not a general N4 theorem |
| Root `README.md`, `STATIONARY_STATUS.md`; `research/s23-reviewed-20260916/README.md`; both independent S2/S3 audits | Official universal threshold `37/40` and accepted continuation scopes | Status, not unverified mathematical black boxes | No official threshold or existing theorem statement is changed |

## Why this is more than an equivalent target

Theorem 1 has explicit additional hypotheses (real two-plane, equal pair
leverage, two-support outside minor difference), an explicit isometric path,
and an unconditional nonnegative integral formula. Its proof controls every
remainder and gives `D_t''>=2c^3(4c-beta)eta^2t(1-t)`.
The connected family (20) meets those hypotheses for every ambient dimension,
with `eta=1/8`, `beta=3/8`. These are independently checkable structural facts,
not names for an unknown Jensen deficit.

The two obstructions also decide concrete live sufficient conditions: a
monotone leverage-balancing real rotation with a negative curvature gain,
and an exact negative Gaussian-density second derivative for a connected
projection after summing all outside words. Neither is called a target
counterexample. The general signed formula alone remains a reduction.

## Imported external mathematics and evidence boundary

The Gaussian integral, Cauchy--Binet identity, finite entropy differentiation,
and one-dimensional Green identity are proved or explicitly expanded in the
new proof. No unverified external research theorem is required for its sign.
S2's imported Shepp--Olkin theorem is not needed for Theorem 1 here.
A primary-source search was exploratory only and supports no novelty claim.

The referenced independent audits apply to the frozen baseline, not this new
packet. The new analytic proof and finite certificates are author-level.
Replaying the checker twice is not independent mathematical review.
