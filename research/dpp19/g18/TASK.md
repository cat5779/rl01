# Invariant critical Bernoulli subcoupling of the WUSF on the \(C_3*C_3\) tree

Let \(\Gamma=C_3*C_3\) act on its bipartite Bass--Serre tree \(T_3\).  Identify the unoriented edge set with the regular \(\Gamma\)-set.  Let \(T\) have the wired uniform spanning forest law, equivalently the determinantal law with the gradient-projection kernel \(Q\).  Let \(B\) have the iid Bernoulli\((1/2)\) edge law.

Determine the following endpoint statement:

> There exists a diagonally \(\Gamma\)-invariant joint law of \((B,T)\) such that \(B\subseteq T\) almost surely.

A positive solution must construct a genuine invariant coupling and verify every finite cylinder: nonnegativity, normalization, projective consistency, both marginals, invariance, and the support condition.  A negative solution must give an exact obstruction valid for every invariant coupling, for example a finite-event linear inequality or a finite LP dual certificate whose validity is proved symbolically.

The endpoint is decisive for the invariant threshold.  The set of invariant monotone couplings is weakly closed on the compact product configuration space; hence an invariant coupling for parameters approaching \(1/2\) would have an endpoint subsequential limit.

## Known inputs and prohibited shortcuts

- Without requiring invariance, Bernoulli\((1/2)\) is stochastically dominated by this WUSF law.
- The Fuglede--Kadison determinant bound is zero here and gives no positive lower parameter.
- The natural five-state conditional-independence splitting class has already been ruled out: its adjacent-star five-edge probability is at most \(1/35\), whereas iid Bernoulli\((1/2)\) requires \(1/32\).  This excludes only that splitting class and is not an obstruction to arbitrary invariant couplings.
- Do not assume reflection symmetry, a distinguished end, or conditional independence across a shared edge unless it is derived from the target law.
- A weak limit of joint laws is not an iid factor construction.  This task concerns only the invariant law endpoint \(p_{\mathrm{inv}}\), not \(p_{\mathrm{iid}}\).
- Finite numerical feasibility or infeasibility is only exploratory unless accompanied by an exact extension theorem or exact dual obstruction.

## Deliverable

Return exactly one of:

- `PROVED`: an explicit invariant endpoint construction with a complete finite-cylinder argument; or
- `DISPROVED`: a universal exact obstruction for invariant endpoint couplings.

If a finite-state or finite-radius ansatz fails, that is not a disproof unless the argument is shown to cover every invariant coupling.
