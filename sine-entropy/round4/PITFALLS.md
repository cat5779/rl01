# Failed methods and distinctions to preserve
 that this round must respect

For a projection P, split on an input site i with `q=P_ii in (0,1)`. On the
remaining sites,
`P^(1)=P_-i,-i-P_-i,i P_i,-i/q`,
`P^(0)=P_-i,-i+P_-i,i P_i,-i/(1-q)`.
With `H_P(a)=H(DPP(aI+cP))`, define
`R_P=H_P''-(1-q)H_{P^(0)}''-q H_{P^(1)}''`.
The proposed universal completion inequality (C), `R_P<=0`, is FALSE.
For `P=vv*`, `v=(1,sqrt(99))/10`, splitting on the second site, at
`c=19/20,a=1/1000`, an exact certificate gives `R_P>15` while `H_P''<-552`.
Thus it is the sufficient recursion step, not full entropy concavity, that fails.

More strongly, for any fixed `0<c<1`, choose an integer `r>c/(1-c)` and the
first r Fourier columns on n=2r sites. Every site has q=1/2 and the input has
full support on the r-subsets. At every possible first coordinate,
`R_P(a,c)=[c^(r-1)/2]*(r*(1-c)-c)/a+O(1+|log a|)` as a decreases to 0,
with the same positive right-end obstruction by complementation. Dimension
is fixed BEFORE taking the endpoint limit. Coordinate ordering alone cannot
make (C) universal. Signed cancellation across a whole latent tree remains
possible; requiring each node's excess to be nonpositive is forbidden.

Further, unrestricted pair-smoothing curvature for all homogeneous input laws
is false (a five-bit non-DPP example exists). Atomwise log-concavity, count
entropy concavity, and a positive Fisher term alone do not settle complete
entropy curvature. A new obstruction to an auxiliary claim is valuable, but
must not be advertised as a counterexample to the sine target.




## Additional pitfalls from the reviewed second round

- A globally averaged localization correction can have positive curvature even
  when every normalized-posterior first derivative vanishes. Keep second
  response and output-law derivatives. See S4 in KNOWN_RESULTS.md.
- No exact common Bernoulli-Laplace clock exists on the supplied growing Fourier
  family, but its exhibited harmonic moments shrink with size. Nonzero mismatch
  is not yet an extensive entropy obstruction. See S5.
- A low-contrast counterexample does not settle a high-contrast-only estimate.
- A Berezin integral is not a positive probability measure. Unrestricted Jensen
  has been disproved. Integer replicas do not grant real-q continuation.
- Replacing the full law by a product loses extensive spatial dependence. A
  value error bound does not control the a-curvature of its error. See S6.
- S7's two stalled runs supplied no accepted new theorem. A masked-resolvent
  representation and uniform far-tail bound are not inherited results.
- This packet's exact finite checks verify their stated finite identities and
  signs; they do not prove the fixed-density entropy-rate target.

## S8's new boundaries

Entropy increase under a real leverage-balancing rotation does not imply convex
curvature gain. Pointwise positivity/convexity inside a Gaussian representation
can fail while the integral has the desired sign. Do not discard signed terms
individually. The reviewed rank-two comparison is a curvature DIFFERENCE; an
iterable path to a solved reference and a fixed-density sign remain unpaid.
