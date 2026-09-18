# Large-radius true-DPP scout

**Status: EXPLORATORY IID MONTE CARLO / NOT A SIGN CERTIFICATE FOR GAMMA**

At each Gauss--Legendre node, the exterior physical word is sampled from its
genuine marginal-kernel DPP by the exact eigenvector/projection-DPP algorithm.
The four compensated residual blocks are then evaluated with conditional
resolvent rank-one updates.  Spectral Bernoulli selections occur only inside
the exact sampler and are not substituted for the physical word.

Twenty-four quadrature nodes and 3,000 independent DPP words per node give:

| R | baseline | curvature | Bregman phi-prime | parameter derivative | signed transport | A_R'' estimate | naive SE |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 20 | 3.9909 | 1.3136 | 0.5137 | 3.3870 | -1.5066 | 7.6987 | 0.0259 |
| 40 | 3.9976 | 1.7298 | 0.8147 | 5.3071 | -2.3456 | 9.5037 | 0.0390 |
| 80 | 3.9994 | 2.0653 | 1.0935 | 7.2776 | -3.2109 | 11.2248 | 0.0508 |

Every sampled-node expectation is positive.  At `R=80`, the largest node
standard error is about `2.69` at `u=0.9976`, where the mean normalized kernel
is about `151.33`; the high-u positive margin is therefore not close to zero.

The focused compensated candidate

\[
E[\bar{\mathcal B}_{\phi'}]
+\tfrac12E[\partial_h\bar{\mathcal B}_\phi]
+E[\Theta\bar{\mathcal B}_\phi]\ge0
\]

has integrated margins `0.701,1.123,1.521` at `R=20,40,80`.  This supports
retaining the Bregman-phi-prime term in the analytic closure.  The simpler
pointwise-in-u half-parameter inequality already has finite counterexamples
and is not revived by these positive integrals.

## Calibration

The same sampler and 24-node integration were run at `R=7` with 10,000 words
per node.  It gives `5.407205 +/- 0.005405`, while exhaustive full-word
enumeration gives `5.409329`; the discrepancy is `-0.39` reported standard
errors.  This checks the complete sampling, local-kernel, and quadrature path
against the finite exact implementation.

The original slow path, which recomputes the DPP eigendecomposition for every
sample, was also allowed to complete all `R=20,40,80` nodes (about 123 minutes)
with the same seed.  A recursive comparison against the optimized path, which
precomputes one eigendecomposition per quadrature node, found 1,057 numeric
fields, no structural or nonnumeric mismatch, and maximum absolute numerical
difference `8.53e-14`.  Thus the optimization changes floating-point evaluation
order only; it does not change any reported sign, component budget, or error.

The values increasing through `R=80` do not prove divergence or a limit;
the volume theorem already supplies a finite limiting object.  This scout only
selects the sign mechanism and the high-contrast region needing proof.
