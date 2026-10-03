# Finite-circuit separate convexity and independent-bin bounds

Fix positive selected path-edge resistances and consider the vacancy event A for e1,e3 in the wired circuit in THEOREM.md. As a function of any one exterior arm resistance s_i, keeping the other variables fixed, its probability is decreasing and convex on (0,infinity), with its continuous extension at zero. This holds both with the positive middle edge and after its contraction.

To see monotonicity without assuming it from the displayed rational formula, replace the exterior arm by its single conductance g=1/s_i to the common wire. This is an unselected edge of a finite weighted connected graph. Its spanning-tree law is determinantal with Hermitian projection kernel K in the usual conductance-normalized edge basis. Conditional on this edge being included, the kernel on the selected edges F={e1,e3} is

\[
K_F^{\rm inc}=K_F-K_{F,g}K_{g,F}/K_{gg}.
\]

This identity follows directly by taking the Schur complement in the inclusion determinants. Here K_gg>0; if the wire edge is a bridge its cross entries vanish and the same conclusion is immediate. Therefore I-K_F^{inc} is at least I-K_F in positive-semidefinite order, and its determinant is at least det(I-K_F). The determinant monotonicity includes singular matrices by adding epsilon*I and taking a limit. Thus P(A|g included)>=P(A), so Cov(1_A,1_g)>=0.

Differentiating the finite tree weight sum with respect to g gives

\[
\frac{d\mathbb P(A)}{dg}=\frac{\operatorname{Cov}(\mathbf1_A,\mathbf1_g)}g\ge0.
\]

Each tree weight uses g at most once. Hence the probability as a function of resistance s=1/g has the form

\[
p(s)=\frac{a s+b}{c s+d}
\]

with nonnegative coefficients and d>0. It is decreasing by the preceding derivative, and

\[
p''(s)=-\frac{2c}{cs+d}p'(s)\ge0.
\]

This proves separate convexity in every exterior resistance. After contraction the two internal exterior arms are simply two parallel wire edges, so the same argument applies to each one separately. Fixed additive closed-edge series resistances preserve the property.

Consequently, for independent exterior variables X1,...,X4, sequential Jensen gives

\[
\mathbb E p(X_1,\ldots,X_4)\ge p(\mathbb E X_1,\ldots,\mathbb E X_4).
\]

More usefully, partition each variable's law into finitely many bins. Conditional on the independent bin labels, apply Jensen using each bin's conditional mean, then average the exact bin probabilities. This is a lower bound on the original vacancy probability. Rounding a bin mean upward preserves a lower bound because p is decreasing.

In the lower arithmetic certificate, one can first replace each actual conditional resistance law by an exact stochastically larger finite-grid law. Decreasingness makes its expectation a lower bound on the true probability. Binning that finite law and replacing each bin by an upward-rounded conditional mean retains a lower bound by the preceding argument. This compresses the four-variable sum while keeping a rigorous infinite bridge and preserving the discrete B-count conditioning.
