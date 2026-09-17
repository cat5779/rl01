# S9 round 3: critical-scale signed compensation

**Status: PROVED_SCOPED_LEMMA**

This is an author proof packet for PR #113, based on reviewed main
`aaf3e86576a867067701089805c9e5e5a83e44f5`. It has not yet received independent
review. The full high-contrast sine entropy-rate concavity target is **not
proved or disproved** by this packet.

## Main result

For a fixed half-density sine family, any fixed `0<c<1`, Fejer degree and
conditioning radius both equal to odd R, and original shifts
`a=(1-c)/2+theta/sqrt(R)`, the complete production-weighted exterior count
has an explicit translated Gaussian-mixture limit. Its symmetrized endpoint
measure minus its center has exactly zero total limiting mass, strictly
negative mass on each central interval, and an exactly compensating positive
mass outside that interval. Actual probability weights are retained.

At the exact midpoint, for the band `|M_R-R|<=sqrt(R)/2`, the two curvature
contributions are

`A_band''(0)=-R C(c)+o(R)` and `A_complement''(0)=+R C(c)+o(R)`.

Here `A=log(2)-J_R` is integrated complete center production, not normalized
block entropy. At `c=19/20`, the proof gives **C(c)>1/140**. Hence the displayed
strict inequalities with `-R/140` and `+R/140` hold for all sufficiently large
odd R. No explicit radius threshold is claimed. Derivatives are justified by
complete-event complex bounds, not by differentiating an entropy value error.

This is stronger and different from the accepted fixed-chord negative-layer
obstruction: it gives the fluctuation-scale signed profile, exact-midpoint
order-R curvature, and the positive contribution that pays its leading term.
It does not sign the smaller complete remainder.

## Reading order

1. [Frozen statement and full proof](MESOSCOPIC_COMPENSATION.md), including
   the quantitative weighted CLT, martingale compensation, explicit constant,
   and complete-event justification for differentiation.
2. [Finite score and acceleration bounds](SCORE_COMPENSATION.md), with a
   parallel author proof and a full-configuration likelihood KL bound of
   order `log(R)/R` to a count tilt on the critical scale.
3. [Any fixed density and interior base shift](GENERAL_DENSITY_EXTENSION.md).
   Away from half output density the center of the count band depends on
   noise; that dependence is expressly retained.
4. [Growing spectral-channel obstruction](SPECTRAL_CHANNEL_OBSTRUCTION.md)
   and [exact Fourier external-field obstruction](EXTERNAL_FIELD_OBSTRUCTION.md).
   These reject specified surrogate proof steps, not the sine target.
5. [Scope/gap audit](AUTHOR_SCOPE_GAP_AUDIT.md),
   [dependency delta](DEPENDENCY_DELTA.md), [candidate ledger](CANDIDATE_LEDGER.md),
   [primary references](REFERENCES.md), [checks](REPRODUCE.md), and
   [truthful work log](WORK_LOG.md).

## Precisely unpaid

The complete production curvature is shown only to be `o(R)`, not nonnegative.
The fixed-chord total signed Jensen integral still has no proved favorable
sign. On chords of length `R^(-1/2)`, an order-`1/R` concavity margin cannot be
paid by the reviewed `O(log(R)/R)` interior value-transfer error, much less by
our larger weighted-CLT error. Neither a count CLT, likelihood closeness, nor
leading cancellation controls that missing signed remainder.

All code is an author algebra check or a floating falsification probe. It is
not the mathematical proof, an independent review, or a domain-cover sign
certificate. In fact the new small-radius band probes have the opposite sign
from the eventual asymptotic assertion; this is explicitly recorded rather
than presented as numerical certification of the theorem.
