# Route registry

## ROUTE-1: componentwise nonnegative dissipation

- Status: **DISPROVED**.
- Counterexample: already at `R=1`, the signed transport component is strictly
  negative for every nontrivial coupling.

## ROUTE-2: wordwise positivity of the complete local kernel

- Status: **DISPROVED**.
- Counterexample: at `R=9,u=1`, the physical word
  `001010011001101011` (site order `-9,...,-1,1,...,9`) has normalized local
  kernel `-1.9552822249`.
- Its residual components are `0`, `-4.1063612421`, `+5.5419951053`, and
  `-11.3909160881`; after adding the independent baseline `8`, the total is
  negative.

## ROUTE-3: expected compensated budget

- Status: **ACTIVE**.
- Evidence: the physical-word expectation remains positive at every tested
  quadrature node through `R=9`; the integrated total grows from `3.0720` at
  `R=1` to `5.8581` at `R=9`.
- Target: compare the expected parameter-derivative block plus
  `phi''-8` against the expected negative transport block, using the true DPP
  integration-by-parts structure.
- A tempting sharper subclaim,
  `E[transport]+(1/2)E[parameter derivative]>=0`, is **DISPROVED** by the
  exhaustive finite scan from `R=3` onward.
- The compensated candidate
  `E[Bregman phi-prime]+(1/2)E[parameter derivative]+E[transport]>=0`
  survives the `R<=9` grid.  Its smallest margins occur at the weak-coupling
  endpoint and approach zero, so a proof must retain the Bregman term rather
  than round the observed ratio to one half.

## ROUTE-4: large-R true-DPP sampling

- Status: **COMPLETED SCOUT THROUGH R=80**.
- The sampler is calibrated against exact full-word enumeration.  It is used
  to decide whether ROUTE-3 remains plausible, not to certify `Gamma`.
- Results: `A_R''=7.699+/-0.026,9.504+/-0.039,11.225+/-0.051` at
  `R=20,40,80`.  The Bregman-compensated half-parameter margins are
  `0.701,1.123,1.521`, all positive.
- Calibration: at `R=7`, the sampler differs from exhaustive enumeration by
  `-0.39` reported standard errors.
- Optimization audit: the 123-minute recomputing-eigendecomposition path and
  the precomputed-eigendecomposition path agree in all 1,057 numeric fields to
  maximum absolute error `8.53e-14`, with no structural mismatch.

## ROUTE-5: weak-coupling series at `c=19/20`

- Status: **REJECTED AS A HIGH-CONTRAST CLOSURE**.
- The positive fourth- and sixth-order coefficients are rigorous near
  `cu=0`, but the existing uniform constants do not cover `u` near one.
