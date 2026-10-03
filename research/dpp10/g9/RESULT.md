# Scoped result: weak superposition and invariant extraction

The complete proof is preserved in `RESULT.pdf`.  This note records its exact
logical output.

## Assumptions

Let a countable group act regularly on itself.  Let
`K_t=C+tH` stay in the spectral gap `[epsilon,1-epsilon]`, and let `mu_t` be
the associated determinantal law.  The nonnegative Borel birth rates vanish
on occupied sites, have integrable mean activity, and satisfy the cylinder
continuity equation in `TASK.md`.

## Proved conclusions

### 1. Ordinary weak superposition

There is a probability law on coordinatewise cadlag pure-birth paths such
that every one-time marginal is `mu_t` and the prescribed cylinder-generator
martingale problem holds.  Every coordinate jumps at most once, the required
integrability holds, and distinct coordinates do not jump simultaneously.

The construction uses exact finite-coordinate conditional rates, finite
pure-birth chains, compactness of the monotone path space, and an `L1`
martingale-convergence passage in the drift.  No same-input convergence of
finite approximations is assumed.

### 2. Invariant weak superposition for amenable groups

The set of weak solutions with the prescribed marginals is nonempty, compact,
convex, and stable under the group action.  For a countable amenable group,
Folner averaging therefore produces an invariant weak solution.

### 3. Conditional strong extraction

Assume additionally that there is an invariant compatible weak solution
jointly driven by an independent product field of sitewise Poisson random
measures, with the causal compatibility stated in `TASK.md`.  Also assume the
displayed invariant-coupling rate estimate (AL) with an integrable coefficient
`L(t)`.  Then conditional independent copies over the whole driving noise
remain solutions in the enlarged filtration; (AL) and Gronwall give pathwise
uniqueness; the conditional law is Dirac.  Consequently there is a total
Borel, all-input equivariant relative map from the initial configuration and
regular iid labels to the path, with the prescribed marginals.

## Not proved

For an arbitrary countable nonamenable group, the compact convex solution set
need not have a fixed point by the amenable averaging argument.  The proof
reduces the remaining invariant weak-existence question to exactly this
fixed-point problem but does not solve it.

The additional causal product-Poisson representation and (AL) used in the
strong extraction statement are hypotheses, not consequences established for
the selected DPP rates.
