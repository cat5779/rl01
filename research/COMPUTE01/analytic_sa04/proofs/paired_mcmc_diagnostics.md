# Paired central diagnostics beyond exact enumeration

**Status: EXPLORATORY MCMC / NOT AN ASYMPTOTIC PROOF**

The same-clock deletion loss is estimated directly under the pair law
`J(T,x)`: sample the central `k`-set at time `s_k`, delete a uniform occupied
point, and evaluate

\[
\log f_k(S;s_k)-\log f_{k-1}(T;s_k).
\]

The binomial constants cancel exactly at `n=2k`, so this paired observable has
expectation `A_k=D(J||R)`.  It avoids subtracting two noisy entropy estimates.
The reverse-clock loss `E_k` is estimated in both bridge directions with
importance reweighting; `d_k=A_k-E_k` is then reported directly.

| n | A_k | batch SE | E_k | batch SE | d_k | naive SE | sqrt(n) d_k |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 40 | 0.929301 | 0.010942 | 0.170458 | 0.002158 | 0.758843 | 0.011153 | 4.7994 |
| 60 | 1.040865 | 0.013033 | 0.362924 | 0.005391 | 0.677941 | 0.014104 | 5.2519 |
| 80 | 1.089113 | 0.014014 | 0.517745 | 0.008006 | 0.571368 | 0.016139 | 5.1105 |
| 100 | 1.107150 | 0.014591 | 0.675069 | 0.010027 | 0.432081 | 0.017704 | 4.3208 |
| 120 | 1.149216 | 0.014597 | 0.767230 | 0.013610 | 0.381986 | 0.019958 | 4.1844 |

Six chains, 2,000 burn-in exchanges, 6,000 retained draws per chain, and
thinning four were used.  Split-Rhat values for the paired deletion statistic
and both bridge directions lie between about `0.97` and `1.06`.  At `n=80`,
the three relevant split-Rhat values lie between `0.980` and `1.037`.  These
batch errors do not certify mixing, but the positive margins are far larger
than the observed uncertainty.

At `n=100,120`, the paired deletion and two bridge split-Rhat values lie in
`[0.986,1.038]`.  The corresponding rescaled increments are
`4.321+/-0.177` and `4.184+/-0.219`.  They reject treating the near-exact
`5.1105` match at `n=80` as a stabilized leading constant, while continuing
to support an inverse-root scale.

The conclusion is route-level: the old sufficient condition
`E_k<2c^4/9` fails by `n=60`, but the main central increment remains strongly
positive because the actual deletion loss is much larger than its conservative
analytic lower bound.  However, the scaled values `sqrt(n)d_k` are approximately
constant across `n=40,60,80`.  The new evidence therefore favors
`d_k=Theta(n^-1/2)` over a dimension-free positive lower bound.  Work should
target this joint local limit, not the discarded initial-dissipation bound or
the over-strong `d_k>=epsilon` closure.

For larger dimensions the birth--death heat kernel is evaluated by Poisson
uniformization.  This preserves nonnegativity and replaces an eigendecomposition
whose tiny tails became negative at `n=80` in binary64.

## First window profile at n=100

The paired estimator was also run away from the single central layer.  Here
`offset=k-l` and `x=offset/sqrt(n)`.

| offset | x | A_l | E_l | d_l | sqrt(n)d_l | naive SE after scaling |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.0 | 1.1072 | 0.6751 | 0.4321 | 4.3208 | 0.1770 |
| 2 | 0.2 | 0.8798 | 0.1816 | 0.6982 | 6.9824 | 0.1423 |
| 4 | 0.4 | 0.6913 | 0.0718 | 0.6194 | 6.1943 | 0.1113 |
| 6 | 0.6 | 0.5515 | 0.0330 | 0.5185 | 5.1848 | 0.0919 |
| 8 | 0.8 | 0.4505 | 0.0183 | 0.4322 | 4.3216 | 0.0930 |
| 12 | 1.2 | 0.3184 | 0.0060 | 0.3124 | 3.1243 | 0.0635 |
| 15 | 1.5 | 0.2427 | 0.0031 | 0.2396 | 2.3959 | 0.0571 |

The rescaled profile has a finite off-center peak and then decreases; no growth
with the raw dimension is visible in this window.  Most split-Rhat values are
near one; the largest is `1.105` for the offset-four deletion chain, so this
remains route-selection evidence rather than a uniform bound.  The outer
offsets have split-Rhat values in `[0.974,1.048]`.

For `n=100`, the tail-splice radius prescribed by the reviewed report is
`sqrt((n-2)log(n)/2)`, approximately `15.02`.  Thus the scan reaches the actual
finite-n splice point.  Its largest observed rescaled increment is `6.98`, at
offset two, and the profile decreases to `2.40` by the splice.  This is direct
finite evidence for the full window shape required by the version-2 theorem;
it is not a proof uniform in `n`.

## Cross-dimensional window check at n=120

A second scan tests whether the `n=100` shape persists when the dimension is
increased.  Offset 17 is the nearest integer to the new tail-splice radius
`sqrt((n-2)log(n)/2)=16.81`.

| offset | x | A_l | E_l | d_l | sqrt(n)d_l | naive SE after scaling |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 0.1826 | 0.9369 | 0.2530 | 0.6838 | 7.4912 | 0.1835 |
| 6 | 0.5477 | 0.6130 | 0.0508 | 0.5622 | 6.1588 | 0.0982 |
| 12 | 1.0954 | 0.3816 | 0.0115 | 0.3701 | 4.0545 | 0.0858 |
| 17 | 1.5519 | 0.2602 | 0.0043 | 0.2559 | 2.8030 | 0.0578 |

All twelve split-Rhat values for the deletion statistic and the two bridge
directions lie in `[0.965,1.040]`.  The rescaled profile again stays of order
one and decreases toward the splice.  Its values are not identical to the
`n=100` scan, so the data do not identify a limiting curve or a sharp constant.
They do, however, strengthen the route-level case for a dimension-uniform
`K/sqrt(n)` window bound and against a constant-size central cusp.  This remains
finite MCMC evidence, not a proof of the uniform bound or of the sign of `W_n`.

### Higher-statistics independent-seed dense window

An independent run with six chains, 2,500 burn-in exchanges, and 12,000
retained draws per chain gives the following first completed block:

| offset | sqrt(n)d_l | naive SE after scaling | deletion/forward/reverse split-Rhat |
|---:|---:|---:|:---|
| 0 | 4.1074 | 0.1749 | 0.974 / 1.039 / 0.986 |
| 1 | 6.4247 | 0.1222 | 0.988 / 0.996 / 1.001 |
| 2 | 7.3939 | 0.0869 | 1.026 / 0.998 / 0.971 |
| 3 | 7.5413 | 0.0668 | 0.985 / 1.002 / 0.975 |
| 4 | 7.1596 | 0.0669 | 0.993 / 0.990 / 1.019 |
| 5 | 6.8415 | 0.0535 | 0.993 / 0.975 / 1.027 |
| 6 | 6.3405 | 0.0528 | 0.970 / 1.032 / 1.017 |
| 8 | 5.5030 | 0.0455 | 0.988 / 1.005 / 0.972 |
| 10 | 4.7512 | 0.0409 | 0.991 / 1.003 / 1.010 |
| 12 | 4.0954 | 0.0337 | 1.016 / 1.012 / 0.987 |
| 14 | 3.5148 | 0.0330 | 0.981 / 0.980 / 1.034 |
| 15 | 3.3224 | 0.0332 | 1.015 / 0.989 / 1.029 |
| 16 | 3.0337 | 0.0293 | 1.090 / 0.999 / 1.025 |
| 17 | 2.9075 | 0.0289 | 0.974 / 0.994 / 0.993 |

The new central value agrees with the earlier `4.184+/-0.219`, and the new
offset-two value agrees with `7.491+/-0.183`.  The off-center peak is therefore
reproducible.  Offsets two and three differ by only about `1.35` combined naive
standard errors, so the data do not yet distinguish the exact discrete peak.
Offset four is lower than offset three by about four combined naive standard
errors, and offsets five and six continue the decline.  The peak is therefore
localized to offsets two or three.  Offsets eight, ten, and twelve extend the
resolved descending segment; the new offset-twelve value agrees with the first
scan's `4.055+/-0.086`.  The consecutive tail values at offsets
`14,15,16,17` are `3.515,3.322,3.034,2.908`, so no upturn appears before the
splice.  The deletion chain at offset sixteen has split-Rhat `1.090`, above the
rest of the dense run (`0.970`--`1.039`); that point therefore carries a mixing
caution and is being independently rerun.  All other displayed diagnostics
are complete.
