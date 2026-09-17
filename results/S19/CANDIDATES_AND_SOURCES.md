# Candidate, failure, and primary-source ledger

The assigned region was never changed: half density, c=19/20, and the full
fixed offset interval [1/50,3/100]. This is fresh research, not a new review
of the inherited S7 proofs.

## A. Conditional square-function / Bregman payment

Primary source: Djalil Chafai, *Entropies, convexity, and functional
inequalities*, J. Math. Kyoto Univ. 44 (2004), 325–363;
https://arxiv.org/abs/math/0211103, especially the Phi-entropy/Jensen-gap
framework and the convexity conditions on the Bregman remainder.
The paper's PDF page 5 and its stated hypotheses were read. No general
Phi-Sobolev or tensorization constant is assumed for the sine output law.

Actual hypothesis match: the local conditional probability is the conditional
expectation of its fully observed counterpart. For
`f(u)=1/u+1/(1-u)` the exact Bregman remainder has the positive expression
in `notes/S7_PAYMENT_INTERFACE.md`. Thus the one-site Fisher gain is a real,
actual-law Jensen gap, not a frozen-law quantity.

Proposed inequality: pay the pair observation cost with this gain alone,
`pair allowance <= Delta_L`. The fastest falsification test is to compare
its size with the already-paid single-site coarsening upper bound. It gives
`Delta_L <= pair allowance/[5200(R-1)]` on the assigned interval.

Outcome: **refund-only payment fails for the unchanged published allowance**.
This does not show that the actual signed pair error is positive. Replacing
the pair allowance by a new one-sided quantity remains possible. This simple
consequence is not presented as the major new result.

Actual table Jensen gaps were also scouted with `martingale_scout.py`.
Some asymmetric observation fields have positive averaged individual gaps,
while the tested total signed gaps remained negative. These floating tests
are not a proof against the exact symmetric S7 local tables and are not
used in the main certificate.

## B. Conditional operators and a periodic-reference Schur estimate

Primary source: Alexander I. Bufetov, Yanqi Qiu, and Alexander Shamov,
*Kernels of conditional determinantal measures and the proof of the
Lyons–Peres conjecture*, https://arxiv.org/abs/1612.06751.
The conditional-kernel and locality statements in Lemmas 1.11–1.14 and the
operator-martingale discussion were inspected. The source preserves the DPP
class under genuine conditioning; it does not give the signed entropy
payment needed here.

Actual hypothesis match: finite conditional kernels are Schur complements
of the **output** Toeplitz pencil, with all outside probabilities retained.
The new step is to compare a finite arbitrary exterior to one explicit
alternating Fourier reference, using its square-summable tail on a fixed
pair. The finite residual identity explicitly pays the compression boundary.
It is not a claim that all inverse entries satisfy a uniform C/r bound.

Proposed aggregate repair: the bad pairs for the existing comparison
`g_+ <= gamma W`, gamma<=2, might have only o(n) total expected positive
excess in the actual sine family. The scalar finite-input counterexample at
an almost-zero shift does not by itself answer that question in the assigned
interior interval or at growing Toeplitz scale.

Fast falsifier found: the alternating half-density reference has
`g-2W > 1/12` at lag 5, robustly on the whole offset interval and a complete
kernel-parameter neighborhood. A reference calculation alone would be
insufficient because the infinite word has no assigned positive probability.

**Promoted and proved:** the deterministic reference stability estimate
`202/L`, followed by a positive actual-channel cylinder probability, gives
an explicit positive linear expected-excess lower bound. This works for
true growing Toeplitz blocks and for every sufficiently large exact S7
local table. `PROOF.md` states the precise aggregate rule disproved and all
limits. A 200-cell rational certificate pays the scalar sign obligation;
the analytic cylinder argument pays the growing-family bridge.

This is not an assertion that the signed aggregate itself is positive.
Negative local pairs can still compensate the positive exceptions.

## C. Parity decimation and effective contrast c^2

Explored but not promoted as a completion route. For an ambient or finite
cyclic half-density projection in parity form

    P = (1/2) [[I,U],[U*,I]],  U unitary,

write p=a+c/2. The first sublattice output is independent Bernoulli(p).
After observing its word y, the other-sublattice conditional kernel is

    A(p) I + C(p) P_y,
    A(p)=p-c^2/(4p), C(p)=c^2/[4p(1-p)],
    P_y=U* diag(1-y) U.

At p=1/2, C(p)=c^2=361/400, below the inherited universal 37/40 contrast.
This is an exact Schur identity, not invariance of configuration entropy
under U. True finite Toeplitz blocks do not have a unitary cross block;
that boundary distinction must also be paid.

The tempting shortcut is to apply the inherited conditional entropy
concavity and freeze y. It misses the actual product weights
`w_y=p^|y|(1-p)^(m-|y|)`. The exact second derivative is

    -m/[p(1-p)] + sum_y [w_y H_y'' + 2 w_y' H_y' + w_y'' H_y].

At the midpoint, `C_y'=(1+c^2)I` and `C_y''=8(C_y-I/2)`.
Binary symmetric refresh makes the radial entropy derivative nonpositive;
the inherited c^2<=23/25 theorem controls the affine second derivative.
Thus the **frozen-weight principal part** has a negative bound, but the two
moving-weight terms displayed above are not paid. A negative bound for that
principal part alone is not a theorem for the complete entropy Hessian.

Outcome: **unpaid actual-law response**. No unitary entropy invariance,
count-only replacement, or positive-density Toeplitz conclusion is claimed.

## Additional failed scalar scout

`payment_scout.py` searched the feasible two-site comparison at the actual
interior shifts, rather than extrapolating the old endpoint failure. At
c=.95, a=.025 it found a ratio near 2.8334, and at a=.02 near 2.8551. These
are floating scouts for arbitrary conditional contractions. They are not
the growing-family counterexample; the explicit alternating-reference proof
provides that separate bridge.

The first direct interval attempt with the more ambitious margin 1/10 was
unresolved (its lower bound was about .0863 with 200 cells and .0911 with
1000). No negative-curvature or theorem failure was inferred. The final
fixed radius 1/10000 and margin 1/12 are certified by all 200 cells.

The archived failed 1000-cell margin-1/10 receipt and source are preserved
in the standalone fallback ZIP from the interrupted first publication
attempt. They are historical evidence, not a premise of this PR-side
margin-1/12 certificate.

The finite full-law exception diagnostic at n=20 gives, for the tested
central lag-5 pair at the midpoint, approximately 0.0002877441 of actual
expected positive excess, with 272 violating outside words among all
2^18 outside words. This is only a floating diagnostic. The theorem uses
the much smaller explicitly proved cylinder lower bound, not an extrapolation
from these finite numbers.

## Evidence classification

The new route lemma has an author analytic proof plus an executed exact
outward certificate. The finite-law entropy and coarsening scouts are
floating diagnostics only. All tests and receipts in this packet are by
the authoring agent, not a second independent reviewer. No novelty or
priority conclusion follows from this limited primary-source scouting.
