# Scoped independent review

**Verdict: CORRECT_SCOPED.**

The review checked the one-edge equations, both single-star Bernoulli events, the two-star splitting formula, the extremum over \(\theta\in[5/24,7/24]\), and the general-\(p\) algebra.

- The common one-edge marginal together with the A/B unique-sign support gives \(q(0)=1/3\) and the displayed parameterization.
- Cyclic invariance, not reflection invariance, gives the four conditional star probabilities \(1/24,1/12,1/12,1/24\).
- The all-vacant star constraints correctly sharpen the interval to \([5/24,7/24]\).
- Conditioning on the shared edge gives exactly
  \(S(\theta)=1/[576\theta(1/2-\theta)]\), whence
  \(1/36\le S\le1/35<1/32\).
- For general \(p\), matching \(S_p(\theta)=p^5\) has only the roots \(p/3,2p/3\); the all-vacant condition then gives
  \(p\le(3-\sqrt5)/2\).

The conclusion is deliberately limited to the five-state splitting class in `TASK.md`.  It is not a proof that the invariant endpoint coupling fails, and it supplies no conclusion about an iid factor coupling.

No novelty, external peer review, or formal verification is asserted.
