# Unrestricted invariant Bernoulli endpoint below the \(C_3*C_3\) WUSF

Let \(\Gamma=C_3*C_3\) act on its bipartite 3-regular Bass--Serre tree, with its unoriented edge set identified with the regular \(\Gamma\)-set.  Let \(T\) have the WUSF law, equivalently the DPP with gradient-projection kernel \(Q\), and let \(B\) have the iid Bernoulli\((1/2)\) edge law.

Prove or disprove:

> There exists a diagonally \(\Gamma\)-invariant joint law of \((B,T)\) supported on \(B\subseteq T\).

A construction must verify all finite cylinders, projective consistency, both exact marginals, invariance, and monotonicity.  A disproof must be a universal exact obstruction for all invariant couplings, not merely the failure of a finite-state, splitting, Markov, end-oriented, or reflection-symmetric ansatz.

Known inputs:

- Ordinary stochastic domination holds at \(p=1/2\) without an invariance requirement.
- The five-state conditional-independence splitting class is impossible: its adjacent-star five-edge probability is at most \(1/35\), while iid Bernoulli\((1/2)\) requires \(1/32\).
- That contradiction has no force against arbitrary invariant couplings.
- The invariant coupling set is weakly closed, so endpoint failure would force the invariant threshold strictly below \(1/2\).

This task concerns \(p_{\mathrm{inv}}\) only.  Do not substitute the iid-factor question, and do not infer a common-input factor from weak convergence.

## Deliverable

Return `PROVED` with a complete invariant construction, or `DISPROVED` with a complete universal obstruction.  Finite numerical evidence is not a conclusion without an exact extension theorem or exact dual certificate.
