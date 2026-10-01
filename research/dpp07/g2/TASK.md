# Pointwise optimality of Fuglede–Kadison Bernoulli bounds

For a countable discrete group Gamma, let Q be a complex Hermitian positive contraction on l2(Gamma) commuting with left translations, tau(T)=<T delta_e,delta_e>, FK(Q)=exp(tau(log Q)) with exp(-infinity)=0, and mu_Q the DPP with inclusion probabilities det Q_F.

Define p_-(Q)=sup{p in [0,1]: Bernoulli(p)^Gamma is stochastically dominated by mu_Q}, where stochastic domination means comparison of all bounded increasing cylinder functions, with no invariance requirement on a witnessing coupling. Define p_+(Q)=inf{p: mu_Q is stochastically dominated by Bernoulli(p)^Gamma}.

The substantive target is the fixed-kernel statement:
for EVERY countable Gamma and EVERY such Q,
p_-(Q)=FK(Q) and p_+(Q)=1-FK(I-Q).
Do not replace this with uniform sharpness witnessed only by scalar Q. Read Lyons's Conjecture 5.7 in its strongest reasonable substantive sense, compare its abelian precursor, and be especially skeptical of our claimed generalization.

Main task: prove this exact fixed-kernel assertion, or give an explicit equivariant kernel/group and a rigorous strict inequality refuting it. A theorem settling all amenable groups with an exact explanation of the remaining nonamenable interface is a meaningful intermediate result, but must be labeled partial. Search for counterexamples as seriously as a proof.

You may take the ordinary inequalities Bern(FK(Q)) <=st mu_Q <=st Bern(1-FK(I-Q)) as an explicit hypothesis D if needed; distinguish a proof conditional on D from an unconditional proof. The main missing necessity is p_-(Q)<=FK(Q). On a finite group the full-occupation event gives p^|Gamma|<=det Q. In infinite groups, whole-space occupation is not a finite cylinder event. Test whether finite-window determinants recover the FK determinant with the exact quantifiers needed. In amenable groups, a Følner argument must justify the logarithmic/singular endpoint, not only polynomial trace convergence. On nonamenable groups, no Følner sequence may be assumed.

Potential approaches include finite-volume determinant variational formulas, strong versus ordinary stochastic domination, entropy/determinant approximations, tree or free-group kernels and projection/zero-FK endpoints. A projection with FK=0 is particularly informative if it rigorously dominates a nondegenerate product measure. Numerical tests are probes only. State whether a proposed obstruction applies to ordinary domination, invariant monotone coupling, or a stronger conditional domination criterion.

For each claimed theorem, give all hypotheses and exact dependence on group, representation, trace, and kernel. Test finite groups, Z, free groups, scalar kernels, kernels with zero spectrum or eigenvalue1, and non-invertible kernels with positive FK. Separate false target, failed proof, and absence of a known argument. Do not infer novelty from failure to locate a paper.

Primary sources: Lyons, Determinantal probability, ICM2014, Conjecture5.7, https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf ; Lyons–Steif, Stationary determinantal processes, especially the exact necessary-and-sufficient Bernoulli domination statements, https://rdlyons.pages.iu.edu/pdf/dyn.pdf . Verify source hypotheses from the papers. Output a complete argument or the precise smallest unresolved necessity statement.
