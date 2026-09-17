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
