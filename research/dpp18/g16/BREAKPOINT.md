# Current breakpoint

## Frozen target

The target inherited from \`cat5779/rl01#123\` is the dimension-free finite-consistency property on the full commuting class.

No valid proof or selector-independent disproof is currently available.

## What has already been reduced away

The following are not the remaining difficulty:

- existence of positive feasible flows;
- dimension-free stability of the signed current;
- dimension-free stability of the capacity vector \(2J_+\);
- variation of the background kernel when the projector is fixed;
- diagonal kernels;
- scalar-complement kernels;
- canonical matching-block kernels;
- coordinate or uniformly bounded-support directions;
- failure of one chosen optimizer;
- instability of deliberately selected circulations.

The unresolved variable is the simultaneous variation of the **marked rank-one projector** through high-dimensional, delocalized eigenspaces while retaining globally coherent choices.

## Strongest positive subproblem

The cleanest sufficient subproblem is #122.

For each commuting input \(x=(K,P)\), define
\[
\mathcal H_E(x)
=
\left\{
f:
\begin{array}{l}
f\ge0,\\
f\text{ has exact endpoint marginals }(\mu_{0,x},\mu_{1,x}),\\
f\le2(J_x)_+
\end{array}
\right\}.
\]

We know:

1. \(\mathcal H_E(x)\ne\varnothing\).
2. The source/target marginals vary dimension-freely in \(\ell^1\).
3. The capacity vector \(2(J_x)_+\) varies dimension-freely in \(\ell^1\).
4. For each fixed \(E\), the unique least-Euclidean-norm point is continuous.
5. No dimension-free active-set/Hoffman bound is known.
6. For fixed \(P\), a much stronger directed repair bound is known.

Therefore a dimension-free globally coherent section
\[
\Theta_E(x)\in\mathcal H_E(x)
\]
would immediately solve #123 positively.

## Why generic transport theory is insufficient

Abstract bipartite one-cover coupling graphs can have unbounded condition numbers: thin path examples amplify an \(O(\delta)\) marginal perturbation to \(O(m\delta)\) edge movement.

The DPP problem avoids the exact thin-path example because:

- every atom is strictly positive under the spectral gap;
- adjacent atoms are uniformly comparable;
- the graph contains many additional routes;
- support reduction and coordinate-mass identities impose extra structure.

A successful positive proof must therefore use more than generic max-flow continuity.

## Why existing negative results are insufficient

The full-fiber Hausdorff counterexample (#109) gives:
- nearby parameters;
- a specially chosen source flow;
- macroscopic distance from the target fiber.

It does **not** give:
\[
\inf_{F\in\mathcal F(x),\,G\in\mathcal F(y)}
\frac{\|F-G\|_1}{d(x,y)}
\to\infty,
\]
nor does it give a finite branching/cycle certificate trapping every selector.

The least-norm counterexample (#116) similarly identifies a bad optimizer, not a bad fiber pair.

## Minimal positive theorem still missing

One of the following would be sufficient:

### Route P1: stable section of \(\mathcal H\)

Construct one explicit or variational selector whose \(\ell^1\) modulus depends only on \(\varepsilon\), not on the number of configurations/edges.

### Route P2: finite-family simultaneous repair

Prove directly that for every finite list \(x_1,\ldots,x_m\) one can choose
\[
f_a\in\mathcal H_E(x_a)
\]
with all pairwise bounds simultaneously.

This may bypass the need for a closed-form pointwise selector.

### Route P3: canonical nonlinear coupling of endpoint states

Find a coupling operation natural under coordinate permutations and stable under simultaneous variation of the background state and the marked mode. The operation must remain one-point upward and preserve the endpoint marginals.

## Minimal negative theorem still missing

A valid disproof must produce, for a fixed \(\varepsilon\), a sequence of finite families of commuting inputs such that **every** feasible simultaneous choice violates every fixed Lipschitz constant.

Two acceptable forms are:

1. pair separation of the entire fibers;
2. a finite branching/cycle obstruction where each edge of the parameter graph forces incompatible choices.

The family must use genuinely delocalized projectors or another mechanism not eliminated by the support-reduction results.

## Current resume point

The most economical next attack is the restricted endpoint-capacity fiber \(\mathcal H\), not the full fiber \(\mathcal F\).

If \(\mathcal H\) admits a uniform section, #123 is proved.
If \(\mathcal H\) has a selector-independent finite-family obstruction, that is a strong structural negative result, although by itself it would still not disprove selection in the larger full fibers.
