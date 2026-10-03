# Finite-output relative kernels: the precise continuity criterion

This explanatory single-output lemma received a complete scoped different-author review. It is not a process theorem or a priority claim; see REVIEWD.md.

Let X={0,1}^I for a countable set I, with product topology and a Borel probability mu. Let p(x)=(p_1(x),...,p_k(x)) be a Borel probability kernel to the finite output alphabet {1,...,k}, understood up to mu-almost-sure equality.

The following are equivalent.

(i) There is a Borel relative sampler F(x,z), using fresh noise z with a fixed law independent of x, whose conditional output probabilities agree with p for mu-almost every x, and a measurable conull set of input pairs at each of which its output has a finite certificate valid under every outside completion of the initial/noise labels. The certificate's initial component reads finitely many coordinates of x. An arbitrary standard site-label noise space is permitted, as in RESULT.md Appendix B.

(ii) The kernel has an everywhere-defined Borel version with each p_j continuous at mu-almost every x.

For necessity, let h_j(x)=integral 1{F(x,z)=j} dnu(z). Fubini supplies a full-measure set of x with a conull certificate section. Fix any such x and any sequence x_n->x, keeping the entire noise z fixed. For each good z, eventually x_n agrees with x on its finite queried initial coordinates, so the all-completion certificate gives F(x_n,z)=F(x,z). Dominated convergence yields h_j(x_n)->h_j(x). The good section is independent of the chosen sequence. Metrizability gives genuine continuity at x, simultaneously for the finitely many j. The h_j are the required Borel version and sum to one everywhere.

For sufficiency, choose that version and a fresh uniform U in [0,1]. Let c_0=0 and c_j=sum_(a<=j)p_a, so c_k=1. Output j when c_(j-1)(x)<U<=c_j(x), with a fixed convention at U=0. At a common continuity point x, almost every U avoids the finite set {c_0(x),...,c_k(x)}. The unique output's two strict inequalities then continue to hold throughout some finite cylinder around x, by continuity of the two cumulative probabilities at x. Reading that finite set of initial bits and the one complete uniform label fixes the output under every outside completion. The sampler is Borel and has the desired kernel.

No full-support assumption on mu is needed for the equivalence. The version in (ii) must be continuous at typical x against ALL nearby inputs, not merely on a conull subspace. This distinction is exactly what the positive-measure cylinders in RESULT.md Appendix B exploit.

This criterion concerns ONE finite-valued output. Sampling several coordinates independently by their one-coordinate kernels generally loses their required joint conditional law. It gives no simultaneous equivariant process construction, no arbitrary-path-space converse, and no query-moment or effective-comparison bound. The input noise labels are complete real labels, not a finite number of random bits.
