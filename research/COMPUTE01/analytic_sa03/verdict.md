# Current verdict

- `Gamma(19/20)>0`: **INCOMPLETE, numerically supported**.
- Nonnegative signed transport: **DISPROVED**.
- Nonnegative complete kernel for every physical word: **DISPROVED**.
- Surviving line: prove an expectation-level compensated inequality under the
  true DPP law.  The data say to invest in the parameter-derivative budget and
  its cancellation with transport, not in pointwise positivity.
- The currently sharp candidate must include the Bregman-phi-prime term; the
  simpler `transport + parameter/2 >= 0` statement already has finite
  counterexamples.
- Calibrated true-DPP sampling gives positive integrated curvature
  `7.699,9.504,11.225` at `R=20,40,80`, with naive standard errors below
  `0.051`.  This materially supports `Gamma(19/20)>0`, but does not certify the
  infinite-volume sign.
- A complete 123-minute slow-path rerun agrees with the optimized sampler in
  all 1,057 numeric fields to `8.53e-14` maximum absolute error.  The large-R
  evidence is therefore insensitive to the eigendecomposition caching
  optimization.
