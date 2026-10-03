# Relative monotone transition beyond finite-support increments

## Fixed target

Let Gamma be any countable discrete group, acting on itself by left translation. Fix complex Hermitian equivariant kernels C and D on l2(Gamma) and epsilon>0 such that

\[
\epsilon I\le C\le D\le(1-\epsilon)I.
\]

Prove or disprove the existence of a total Borel, all-input equivariant map Phi(x,u) such that, whenever X has determinantal law mu_C and U is an independent regular iid family of atomless labels, Y=Phi(X,U) has law mu_D and X is contained in Y. Require all-input containment; a null exceptional set may return x itself. The kernels and group are fixed before constructing the map. Do not require a prescribed joining, measurable dependence on all kernels, a finitary code, or a simultaneous grand coupling. A pure-birth path with marginals mu_{C+t(D-C)} is a useful stronger output but is not required for the endpoint target.

No finite-support or reduced-group-C*-algebra assumption is imposed on D-C. The increment may have nontrivial kernel. Write T=(D-C)^(1/2), which is a bounded equivariant operator with T delta_e in l2(Gamma), generally of infinite support.

## Mathematical input and obstruction

The supplied finite-support theorem gives a relative pure-birth transition along C+tTT* when T delta_e has finite support and the whole path is uniformly gapped. Its mechanism is a positive flow on a finite Boolean cube, summed over translates, with invariant mean sensitivity and a common-noise envelope construction.

That theorem may be used as a stated input. Its role here is to isolate the passage from finite support to a general square-summable column. Prove every additional limit or selection step needed for the present target.

An auxiliary near-optimal relative interface, even if accepted for arbitrary kernels, supplies only root mismatch <=tau|C-D|+eta for eta>0. For C<=D this permits order violations up to eta/2. Neither a weak limit of joint factor laws nor summable order-violation probabilities supplies the required common-input, order-preserving limit.

Dominated positive-square approximation also fails in general. On Gamma=Z take a positive-measure closed nowhere-dense set E of the Fourier circle. For C=I/8, D=I/4+P_E/4, the increment is I/8+P_E/4. Any continuous multiplier dominated by it is <=1/8 on the dense open complement and therefore everywhere, so such dominated approximants cannot converge in trace to the increment. This is an obstruction to one approximation method, not a counterexample to the target.

## Suggested point of attack

Seek a representation of the finite-support flow and its sensitivity that survives l2 truncation without constants diverging with support size, or construct a different ordered relative sampler. Carefully distinguish a bounded sum evaluated at one configuration from a sum of separate worst-case influences. If using truncated generators or ordered pair approximations, prove actual common-input convergence and correct marginals; do not infer a factor from weak compactness. Any independence, pathwise uniqueness, all-boundary conditioning or exceptional-set assertion must be justified at its use.

If the target cannot be completed, report the smallest precise missing lemma and its relation to the target: strictly weaker, equivalent, stronger, or unknown. A failure of a chosen flow selection or approximation is not a disproof. A partial theorem must state exactly what additional assumptions it uses, and it must not silently replace this target.

## Deliverable

Give a complete mathematical argument or an explicit counterexample satisfying all assumptions. Identify each external input precisely and distinguish correctness from novelty. Include all load-bearing steps in the main text. Keep the unrestricted target marked INCOMPLETE unless it is actually proved or disproved.
