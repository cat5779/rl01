# Independent mathematical review

**Verdict: PASS / CORRECT_SCOPED.**

The proof establishes the abstract ordinary weak-realization theorem under exactly the stated hypotheses: weakly continuous one-time laws, finite-valued jointly Borel coordinate birth rates, coordinatewise \(L^1(dt\,\mu_t)\) mean activity, and the exact cylinder continuity equation.

The load-bearing points check as follows.

1. Finite-coordinate conditional rates are measurable and converge to the original rates in \(L^1(dt\,\mu_t)\) by the upward martingale convergence theorem.
2. Each projected continuity equation admits a finite acyclic pure-birth realization even when conditional rates are unbounded. Zero-mass states create no outgoing flux, and the variation-of-constants argument justifies the hazard construction.
3. The finite chains need not be projectively consistent. Their birth-time laws live in a compact metrizable product, so one common weakly convergent subsequence exists before any martingale test is chosen.
4. Positive-time birth atoms are excluded by continuity of the one-coordinate marginals. This makes finite positive-time evaluations almost surely continuous under the limit law. The time-zero marginal is recovered separately from \(X_\delta\to X_0\) and \(\mu_\delta\Rightarrow\mu_0\).
5. For unbounded Borel rates, finite-coordinate conditional expectations are first truncated. Weak convergence handles the bounded truncated terms, while every tail and approximation error is controlled by the same \(L^1(dt\,\mu_t)\) convergence.
6. Positive-time finite-history tests generate the full natural history because \(X_0(i)=\lim_{k\to\infty}X_{r/k}(i)\). A monotone-class argument and then \(r\downarrow0\) give the martingale property from time zero.
7. The weak-limit subsequence is fixed once. No test-dependent diagonal extraction occurs, so one law solves every bounded cylinder martingale problem.
8. Applying the martingale problem to \(x_i\), \(x_j\), and \(x_ix_j\), followed by finite-variation integration by parts, shows that the nonnegative common-jump count has expectation zero. Countability excludes all simultaneous positive-time coordinate jumps.

The proof does not use DPP pattern positivity, a global total-rate bound, invariance, amenability, projective consistency, a Poisson representation, or a strong/factor construction. Accordingly it proves ordinary weak existence only. Invariant existence for arbitrary nonamenable groups remains a separate fixed-point problem.

Minor optional clarifications are to choose one common null set for the countable family of conditional rates and to spell out the standard compensated edge-counting martingale/localization step. Neither changes the theorem or requires an additional hypothesis.
