# Independent review request — continuation 02

Review target: \`CONTINUATION_02_UNREVIEWED.md\`.

The main theorem remains open. This review should classify each section independently; do not issue one blanket PASS if only some sections survive.

## Section 1 — full-fiber fixed-projector repair

Check:

- the decomposition \(K=\lambda P+B\), \(L=\nu P+B'\);
- the residual-state identity used to repair an arbitrary full-fiber flow;
- exact divergence after adding the residual endpoint flow;
- outgoing capacity under background change;
- outgoing capacity under marked-eigenvalue change;
- the final constant \(4/\varepsilon\).

Desired verdict: \`PASS\`, \`GAP\`, or \`FAIL\`.

## Section 2 — weighted selector

Check in this order:

1. identity
   \[
   w(S,i)=P_{ii}p_{K_{-i}}(S);
   \]
2. total weight one;
3. the energy estimate
   \[
   \|J\|_w^2\le(1-\varepsilon)/(2\varepsilon^2);
   \]
4. existence of a feasible point of uniformly bounded energy;
5. continuity through \(P_{ii}=0\);
6. differential estimates for \(w_t\) and \(J_t\);
7. weighted repair bound;
8. variational inequality producing the \(1/2\)-Hölder modulus.

In particular, determine whether the claimed constant
\[
10\varepsilon^{-3/2}
\]
is actually justified or only schematic.

## Section 3 — bounded components

Check:

- trace-norm pinching identities;
- exact well-definedness of the boundary rule on multiply reducible kernels;
- fixed-dimensional projection Lipschitz lemma;
- homogeneous zero-weight estimate;
- global product divergence and capacity;
- independence of the number of blocks.

## Section 4 — three-input finite-family certificate

This is the highest-priority finite exact calculation.

Recompute from scratch:

- spectrum and commutation;
- all DPP exact atoms;
- divergence \(b_{K_a,P}\);
- feasibility of \(F_a\);
- pairwise optimum \(48\eta/21\);
- cyclic-symmetrization reduction;
- the orbit-range identity;
- potential gradient values;
- pairing \(26\eta/21\);
- simultaneous optimum \(52\eta/21\).

If possible, produce a small exact-rational verification script.

## Section 5 — affine-in-\(P\) obstruction

Check:

- reduction of an affine rule to operators \(A_e\);
- positivity implication \(A_e\succeq0\);
- coordinate-mass identity at operator level;
- rank-one support implication;
- derivative values for the two explicit projectors.

## Section 6 — unconstrained weighted current

Recompute the matrix spectrum and the grounded Laplacian exactly.

Check:

- residual of \(\widehat\phi\);
- \(Lq\ge310\mathbf1\);
- maximum-principle comparison;
- strict negative sign on edge \(1\to12\);
- claimed capacity-side bound.

A reproducible rational checker is preferred.

## Section 7 — low-energy arbitrary-repair obstruction

Do not certify from the current text alone. Require reconstruction of the explicit finite-dimensional family and a reproducible dual/linear-functional certificate.

## Scope discipline

Even if Sections 1–6 all pass:

- do not mark PR #123 PROVED;
- do not claim a varying-projector Lipschitz selector;
- do not claim selector-independent nonexistence;
- do not claim unrestricted noncommuting results;
- do not promote fixed-\(r\) bounds to a uniform \(r\to\infty\) theorem.

Record each accepted result with its exact quantifiers.
