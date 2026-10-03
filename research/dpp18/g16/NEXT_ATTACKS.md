# Next attacks

This is a concrete continuation plan for the finite-consistency problem. The order reflects mathematical leverage, not certainty.

## Attack A — stable section of the positive-part endpoint fiber

### Goal

For
\[
\mathcal H(x)
=
\{f:\text{endpoint marginals correct},\ 0\le f\le2J_x^+\},
\]
construct a selector
\[
\Theta(x)\in\mathcal H(x)
\]
with
\[
\|\Theta(x)-\Theta(y)\|_1
\le C_\varepsilon d(x,y).
\]

### Why this is first

- feasibility is already certified;
- all right-hand-side data are already dimension-free Lipschitz;
- success immediately proves the original finite-consistency theorem;
- failure may expose the first genuine selector-independent branching obstruction.

### Avoid

Do not invoke a generic Hoffman constant without proving it is uniform for this DPP-generated family.

### Candidate structures worth testing

1. entropy/KL projection relative to a strictly positive reference built from \(J_+\);
2. lexicographic or randomized max-flow rules only if one can prove dimension-free sensitivity;
3. Sinkhorn-like balancing only if exact zero/nonedge constraints and hard capacities are retained;
4. a monotone residual decomposition driven by the Fock-space positive state, rather than by arbitrary network pivots;
5. finite-family simultaneous convex programs whose objective is symmetric over the list, followed by a list-length-independent estimate.

## Attack B — construct a canonical nonlinear one-point coupling

### Goal

Given the two endpoint density matrices
\[
\rho_0,\qquad \rho_1=U\rho_0U^*,
\]
extract an actual probability coupling on upward coordinate edges with a formula stable in both \(\rho_0\) and the marked mode \(v\).

### Key difficulty

The signed quasi-coupling
\[
q(S,T)=\operatorname{Re}[U_{T,S}(\rho_0U^*)_{S,T}]
\]
is explicit and stable but signed.

The max-flow theorem proves existence of a positive correction but loses canonicality.

### Desired output

A nonlinear map
\[
(\rho_0,U)\mapsto \pi
\]
such that:

- \(\pi\ge0\);
- \(\pi\) has the correct marginals;
- \(\pi\) is supported on upward one-point edges;
- \(\pi\le2q_+\) or satisfies the original DPP capacity;
- the map is permutation natural;
- its \(\ell^1\) modulus is dimension-free.

## Attack C — finite-family symmetric optimization

Instead of first building a single-fiber selector, attack the equivalent finite-consistency statement directly.

For a finite list \(x_1,\ldots,x_m\), solve a single symmetric convex feasibility/optimization problem over
\[
(f_1,\ldots,f_m)
\]
with each \(f_a\in\mathcal H(x_a)\).

Possible objective:
\[
\min\ \max_{a,b}
\frac{\|f_a-f_b\|_1}{d(x_a,x_b)+\eta}
\]
or a convex surrogate.

The proof obligation is not existence in fixed dimension; it is a dimension- and list-length-independent a priori bound.

A successful estimate may exploit the fact that all fibers are generated from stable signed currents \(J_a\) with uniformly bounded total variation.

## Attack D — search for a branching/cycle obstruction inside a degenerate eigenspace

### Why this is the minimal negative arena

Fixed \(K\) with a spectral eigenspace of multiplicity \(r\ge2\) allows \(P\) to vary continuously while keeping \(KP=PK\).

This isolates the projector-variation difficulty without introducing kernel variation.

### Requirements for a valid negative result

Need a finite family
\[
P_1,\ldots,P_m
\]
inside one common eigenspace and commuting with the same gapped \(K\), such that every simultaneous choice of positive flows incurs an unbounded Lipschitz ratio.

A bad least-norm selection is irrelevant.

### Recommended progression

1. start with a 3- or 4-cycle of projectors;
2. impose permutation/symmetry reductions on flows;
3. formulate exact LP dual certificates for incompatibility;
4. only then scale dimension/support.

A useful certificate would be a bounded family of linear functionals \(\ell_{ab}\) on edge-flow space such that:
- feasibility forces incompatible signs/offsets around the cycle;
- the sum of parameter distances around the cycle tends to zero or stays bounded;
- every simultaneous assignment accumulates a fixed defect.

## Attack E — bounded component size \(r\ge3\)

PR #124 isolates a related structural problem.

For \(r=1,2\), exact refinement compatibility is known.
For fixed \(r\ge3\), canonical component partitions can change incompatibly and their union can form large components.

A solution here may reveal the right refinement-compatible local selector technology needed for the general commuting problem.

Conversely, a counterexample for one fixed \(r\) would provide a highly structured selector-independent obstruction.

## Attack F — exploit trace identities to eliminate apparent dimension factors

The scalar-complement proof contains an important pattern:
\[
2(n-1)|a-c|
\]
looks dimension-dependent, but
\[
(n-1)a=\operatorname{tr}K-\operatorname{tr}(KP)
\]
converts it to a trace-norm bound.

When a candidate construction produces sums over many coordinates/eigenmodes, search for identities expressing the full sum as:
- \(\operatorname{tr}(K-L)\);
- \(\operatorname{tr}(KP-LQ)\);
- a trace norm of a compressed difference;
- or total mass already normalized to one.

This is the main known mechanism by which a local product estimate becomes dimension-free.

## Acceptance checklist for a positive solution

Before labeling PROVED, verify all of:

- arbitrary finite coordinate set;
- arbitrary spectral multiplicity;
- varying projectors;
- support degenerations;
- eigenvalue degenerations within the gap;
- exact divergence;
- positivity;
- total edge mass one;
- pointwise capacity;
- Borel dependence;
- coordinate-permutation covariance;
- constant independent of \(|E|\);
- constant independent of list length;
- finite-list simultaneous consistency, not only pairwise repair.

## Acceptance checklist for a negative solution

Before labeling DISPROVED, verify:

- every flow/selector is trapped, not a chosen optimizer;
- all kernels satisfy the fixed spectral gap;
- all projectors commute with their kernels;
- the ratio diverges with an explicit family;
- bounded-support reductions do not invalidate the example;
- the obstruction survives the availability of alternate circulations/routes;
- the conclusion is stated only for the commuting class unless more is separately proved.
