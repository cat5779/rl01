# SA05 n=8 finite sign certificate

**Status: FINITE_CERTIFIED**

This certificate addresses only the complete 70-state formula in section A of
`results/SA05/SA05_HANDOFF.md`, at `c=19/20,n=8`.  It does not imply a sign for
other dimensions or for the entropy-rate limit.

## Certified points

The standard-library script `sa05_n8_interval.py` uses exact integer/Fraction
arithmetic.  It encloses `sqrt(2)` and positive seventh roots by rational
bisection.  Logarithms are enclosed by

\[
\log x=2\sum_{r=0}^{M}\frac{t^{2r+1}}{2r+1}+R_M,
\qquad t=\frac{x-1}{x+1},
\]

after power-of-two range reduction, with the explicit positive tail bound from
the task handoff.  Second derivatives are propagated by interval forward-mode
automatic differentiation; no finite difference or binary floating-point sign
decision enters the certificate.

At 96 rational bisection/tail bits the output is:

| parameter | certified interval for `E_8''(a)` | sign |
|---|---:|---|
| `a=1/200` | `[-0.00037268948828,-0.00037268948827]` | negative |
| `a=1/50` | `[0.00034554219606,0.00034554219607]` | positive |
| `a=1/40` | `[0.00044081523988,0.00044081523989]` | positive midpoint |

The 70 states collapse to seven exact orbit-data types with multiplicities
`2,4,8,8,16,16,16`.  Before differentiating, the script verifies that the
interval enclosures of the uniform means satisfy

\[
\mathbb E r_0=1,\qquad \mathbb E v_2=0,\qquad \mathbb E v_4=0.
\]

The independent binary64 jet implementation `sa05_n8_explore.py` lands inside
all three certified intervals and also locates the two symmetric sign-change
brackets recorded in its JSON receipt.  That floating run is a regression
check, not part of the proof.

## Independent 256-atom regression

`sa05_n8_full_atoms.py` independently forms every rank-four Fourier projection
minor, mixes the resulting 70 latent DPP atoms through the coordinatewise
channel, and reconstructs all 256 output atoms.  It checks total and layerwise
zeroth/first/second mass, positivity, the exact count-law coefficients, and the
complete corrected-minus-true entropy Hessian.  At all three points the largest
component discrepancy from the reduced 70-state formula is below
`3.5e-14`; details are in `sa05_n8_full_atoms_result.json`.

That independent cross-check is deliberately labelled
`BINARY64_INDEPENDENT_REGRESSION`.  It validates the derivation and
implementation but does not supply the sign proof.  The sign claim remains the
output of the exact-rational outward interval calculation described above.

Thus C01 is complete as a finite certificate plus independent implementation
regression.  No all-`n` or asymptotic conclusion is claimed.
