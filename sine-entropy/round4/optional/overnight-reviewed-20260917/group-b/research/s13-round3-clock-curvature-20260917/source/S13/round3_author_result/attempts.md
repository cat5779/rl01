# Attempts and retained failures

## A. Promoted route: clock-curvature entropy production

The full corrected chain rule was expanded first. At the symmetric shift,
`z'=0` removes all first-clock and cross terms exactly. The surviving clock
piece is `sum pi(-tau'')I`.

A sign from `I>=0` alone was rejected as non-substantive. The route was promoted
only after two quantitative facts were obtained:

1. `-tau''/n -> 2/(1-c^2)` uniformly on central layers;
2. a nonzero averaged adjacent degree-two mode plus slice mLSI gives
   `I>=D_pair(c)-o(1)`.

Their product yields the explicit extensive theorem.

## B. Scope repair of the old two-mode no-go

The averaged maximal-overlap density is translation invariant and has no
Johnson degree-one component. Therefore the old random-clock Jensen obstruction
is retained only for channel/operator multiplier matching when degree one is
separately required, for example before input averaging. It is not used as an
averaged-law no-go.

This round instead exhibits a second nonzero averaged observable: an adjacent
pair degree-two mode. One mode is enough for the KL lower bound, but not for a
new mixture incompatibility theorem.

## C. Unpaid moving-count term and numerical warning

Direct finite enumeration of the corrected law gave

| n | `W_n=sum pi''K_l` at `c=.95` |
|---:|---:|
| 8 | -10.67 |
| 10 | -21.97 |
| 12 | -38.06 |
| 14 | -59.07 |
| 16 | -84.96 |

These data are in `../exploration/` in the cumulative package. They suggest a
middle-layer cusp that could be larger than the favorable `O(n)` clock term.
No asymptotic conclusion is drawn.

An attempted entropy-deletion proof stalled. Uniform deletion from the middle
slice gives an exact KL chain rule, but the corrected clocks satisfy the wrong
monotonicity for the desired comparison: the `k-1` layer is less heated, not
more heated, than the deletion of the `k` layer. Therefore data processing does
not supply the needed lower bound on `K_k-K_(k-1)`.

## D. Rejected shortcuts

- Counting `I>=0` without a quantitative lower bound.
- Reusing the round-two unreviewed saddle or cusp claim as a premise.
- Treating the pair-mode KL lower bound as a full entropy-curvature sign.
- Differentiating any entropy value comparison.
- Declaring the negative finite `W_n` sequence to be an asymptotic theorem.
