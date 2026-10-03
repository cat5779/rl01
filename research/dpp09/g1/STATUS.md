# Scope of the general-increment results

The unrestricted target is **INCOMPLETE**: for a fixed countable group and fixed equivariant kernels epsilon I <= C <= D <= (1−epsilon)I, a relative iid map taking a prescribed sample with law mu_C to an ordered sample with law mu_D has not been constructed in full generality, nor disproved.

## Accepted auxiliary arguments

A scoped mathematical audit accepts the following statements in the submitted manuscript:

- **Conditional exhaustion:** a monotone strong exhaustion of D−C by sums of finite-propagation positive squares suffices, using the supplied finite-support transition theorem at each step.
- **Rank-one coupling:** an increment ww* admits a monotone coupling adding at most one point. This is a standard consequence of Lyons's projection coupling and a support-minimal dilation, not a new theorem.
- **Positive continuity equation:** for arbitrary D−C, a Borel covariant single-birth rate field can be selected with mean activity tau(D−C) at each site and the exact forward equation for every cylinder function. This is a statement about the prescribed laws and the rate field. It does not establish a process on independent clocks.
- **Fourier obstruction:** the displayed fat-Cantor example prevents the stated contraction-preserving finite-propagation positive-square approximation, including monotone exhaustion. It does not refute the factor target.

For the covariance assertion, choose one root disintegration and define every translated conditional kernel by translating that same version. For the rank-one dilation, restrict its middle summand to the range of (ww*)^(1/2); this summand has dimension at most one. These details are spelled out in REVIEW01.md.

## Two unresolved interfaces

**1. Marginal identification in the closure theorem.** Theorem 4 uses, but does not explicitly assume, X_t^(n) ~ mu_(K_t^(n)) for every n,t. Under a literal reading, zero-rate constant processes refute its stated conclusion for nonconstant prescribed kernel paths. Under the intended stronger reading, the common-clock estimate and the proof work once this marginal condition, predictable clock solutions, and the other standard measurability conditions in the review are stated. No new process-existence conclusion follows from adding an assumption.

**2. Cross-approximation stability.** Section 6 controls how a single approximating rate changes with the configuration. Theorem 4 instead needs comparison of rates belonging to two different approximations. Convergence of forward equations does not supply that comparison. The review gives two different covariant positive flows with exactly the same finite DPP forward equations. OBSTRUCTION.md gives a separately reviewed one-point example with bounded rates, a common spectral gap, uniform marginal convergence, and weak or integrated convergence of forward equations, but no subsequence converging in probability on the fixed Poisson input.

A usable sufficient condition must state a vanishing cross-index mean rate error, or provide a different explicit proof of common-input convergence, together with marginal identification for the approximating processes. If “approximated” is intended to mean a stronger topology, that topology and its verification are part of the missing hypothesis. Neither counterexample disproves existence of the endpoint factor or the positive-flow identity.

## Review boundary

The submitted auxiliary package has the overall verdict **CRITICAL_GAPS**, with the separate accepted components listed above. The oscillating-rate obstruction has an independent **CORRECT** review. These are different scopes, not two full acceptances of the submitted manuscript. The raw mathematical manuscript is preserved as MANUSCRIPT.md; neither the general relative target nor novelty has been certified. Independent domain review and formal verification remain open.
