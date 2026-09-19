# Rejected, limited, and stalled proof routes

Each entry states what fails and what remains usable.  A failed intermediate
criterion is not described as a counterexample to the original conjecture.

## Arbitrary binary inputs

**Attempt.** Prove entropy concavity for every binary input distribution under
the copy-or-refresh channel, then specialize to DPPs.

**Failure.** An exact three-bit non-DPP distribution violates the proposed
general statement.

**What survives.** DPP posterior closure and Schur geometry provide additional
structure absent from arbitrary binary laws.

## Separate pointwise bounds on pair terms

**Attempt.** Force every conditioned pair contribution to be nonpositive, or
bound the numerator and posterior energy ratio by separate suprema.

**Failure.** Positive pair contributions occur, and separate suprema destroy
the compatibility between atom probabilities, odds ratio, and completion
weights.  The older unrestricted weighted local-row constant diverges near a
channel endpoint for every \(c>1/2\).

**What survives.** Summed positive parts can be paid for by a common global
Fisher–Schur budget.  Completion weights and diagonal rows must remain coupled.

## Pointwise two-budget domination beyond the present threshold

**Attempt.** Continue improving a uniform local inequality
\(g_+\le\gamma(\mathcal K+\mathcal D)\) with \(\gamma<2\).

**Failure.** At \(c=463/500\), an explicit rational feasible table violates
even \(\gamma=2\).

**What it does not refute.** The full entropy Hessian may still be negative
after averaging across pairs and complete outputs.

**What survives.** The local comparison remains rigorous through \(37/40\)
and identifies exactly which spatial information a stronger proof must retain.

## Renewal description of the sine process

**Attempt.** Use renewal entropy formulas after conditioning on a point.

**Failure.** The sine-process Palm law is not a renewal process.

**What survives.** Renewal calculations remain correct for genuine renewal
kernels and are retained as a comparison model.

## Translation-invariant cycle neutrality

**Attempt.** Approximate a nontrivial sine projection by translation-invariant
cycle-neutral finite graphs.

**Failure.** Cycle neutrality under translation invariance permits at most one
positive Fourier lag, too small a class to approximate a contiguous projection
without restoring the obstructing cycles.

**What survives.** The one-harmonic class is an exact all-contrast theorem.

## Finite-dimensional endpoint expansion

**Attempt.** Prove negative curvature near a channel endpoint at every finite
dimension and pass the expansion to the stationary limit.

**Failure.** The leading normalized coefficient can decay exponentially with
volume, while same-cardinality exchanges create nonuniform higher-order terms.
Termwise passage is unjustified.

**What survives.** Hypergeometric resummation correctly handles uniform
fixed-cardinality input.  The remaining term is spatial nonuniformity inside
each output-cardinality layer.

## Perturbative fourth-order sign

**Attempt.** Use the favorable fourth-order coefficient as a stationary
neighborhood theorem.

**Failure.** A coefficient at each fixed dimension supplies no uniform
remainder as the volume grows.

**What survives.** A different dimension-independent argument proves the
small-shape theorem and gives an explicit norm threshold.

## Circulant and finite Fourier substitutions

**Attempt.** Replace Toeplitz principal blocks by cyclic projections, or infer
a positive-density stationary theorem from a fixed list of finite Fourier
sizes.

**Failure.** The two finite laws differ, and fixed-size concavity has no
uniform limiting content without a quantitative comparison.

**What survives.** Cyclic Fourier combs form a genuine all-contrast natural
class.  Trace-norm comparison is useful when its error is controlled.

## Value tails and midpoint Fisher information

**Attempt.** Differentiate a finite-block value approximation to obtain a
Hessian bound, or use the midpoint Fisher limit alone to sign entropy
curvature.

**Failure.** Value error bounds need not survive differentiation.  Entropy
curvature also contains a probability-acceleration term not controlled by the
Fisher limit.

**What survives.** Both results are rigorous and useful for certified Jensen
chords, asymptotics, and isolating the remaining term.

## Channel composition and complementation

**Attempt.** Factor a high-contrast channel through a proved lower-contrast
channel, or convert contrast \(c\) to \(1-c\) by complementation.

**Failure.** Binary-channel determinants multiply under composition, so the
contrast magnitude cannot increase.  Simultaneous complementation preserves
the magnitude of the contrast.

**What survives.** The same algebra yields the useful spectral-width
reduction for already-noised kernels.
