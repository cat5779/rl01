# Attempts, repairs, and preserved failed versions

## Attempt A: direct contrast comparison without complementation

The first version compared `H(aI+cQ)` directly with `H(aI+c0 Q)`.  Its entropy
coupling error is controlled by `b((c-c0) Tr(Q)/n)`, which can be as large as
`b(c-c0)`.  This version is valid but gives a weaker explicit contrast band.

**Repair.**  For mean density above one half, complement the output and compare
`DPP(xI+c(I-Q))` with `DPP(xI+c0(I-Q))` at the same transformed variable
`x=1-a-c`.  This reduces the coupled mismatch density to at most one half while
preserving the second derivative because `x` is affine with slope `-1`.

## Attempt B: an incorrect same-a complement shortcut

A discarded draft tried to use
`H_rho(a,c)-H_rho(a,c0)` and then complement both terms to density `1-rho`.
This is not a same-parameter comparison: the transformed intercepts are
`1-a-c` and `1-a-c0`.  Using it would silently introduce an additional moving
`a`/contrast term.

**Repair.**  The proved argument compares the high- and low-contrast laws at the
same transformed intercept `x=1-a-c`; the low-contrast reference is therefore
`H(DPP(xI+c0(I-Q)))`, not the complement of `H(DPP(aI+c0Q))`.

## Attempt C: direct pressure difference between p and the block product

Renyi divergence `D_q(p||w)` does not by itself equal
`log sum p^q - log sum w^q`.  Treating it as that pressure difference would be
incorrect because the escort measure changes.

**Repair.**  Use the exact positive Holder functional

`B(q;w)=q log sum p w^((q-1)/q)`.

Its exact remainder divided by `q-1` is
`D_(1/q)(pi_q||w)`, where `pi_q=p^q/Z(q)`.  Expanding both positive sums under
the original law `p` lets the strong-Rayleigh MGF estimate control the actual
remainder without replacing the escort.

## Attempt D: finite-memory reference

A genuine overlapping finite-memory reference was considered.  A one-site flip
can alter `O(R)` conditional factors, so a direct Lipschitz argument gives a
real-q error growing at least quadratically in `R` before any cancellation.
The disjoint true-block reference already retains correlations through radius
`R-1` and has a dimension-free one-flip constant, so it was selected for the
proved theorem.  No claim is made that finite-memory references cannot be
improved by martingale cancellation.

## Attempt E: polymer expansion

The abstract convergence criteria require a proved activity/summability bound.
No honest high-contrast activity parameter was found for powers of all
principal minors near `q=1`.  Pair-correlation decay alone failed the admission
test, so this candidate was not promoted.

## Numerical exploration versus proof

A high-precision search was used only to choose simple rational constants
`delta=9/500` and `M=768`.  The final comparison is independently redone with
`fractions.Fraction`; the theorem does not rest on the search or on a floating
scan.  The noninteger-q finite example is explicitly labelled diagnostic.
