# Close the local endpoint fixed-point reduction for invariant weak DPP birth laws

## Frozen theorem

Let a countable group \(\Gamma\) act by coordinate permutations on a countable set, let
\[
K_t=C+tH,\qquad \varepsilon I\le K_t\le(1-\varepsilon)I,
\]
be an equivariant linear DPP path, and let \(a_i(t,x)\) be finite-valued jointly Borel covariant pure-birth rates satisfying the exact cylinder continuity equation and
\[
\int_0^1\int a_i(t,x)\,\mu_t(dx)\,dt<\infty
\]
for every coordinate. Ordinary prescribed-marginal weak solutions are known to exist.

For \(0\le u<v\le1\), let \(\mathcal E_{u,v}\) be the set of endpoint laws \(\operatorname{Law}(X_u,X_v)\) of ordinary prescribed-generator solutions on \([u,v]\).

Prove or disprove:

> A \(\Gamma\)-invariant global prescribed-generator weak path law exists if and only if, along some sequence of finite partitions with mesh tending to zero, every adjacent cell \([u,v]\) has
> \[
> \mathcal E_{u,v}^{\Gamma}\ne\varnothing.
> \tag{TFP}
> \]
> The invariant endpoint elements may be chosen independently on different cells and independently for every refinement; no projective consistency is required.

This theorem is an equivalence/reduction. It does not assert that the local invariant endpoint elements always exist for arbitrary groups.

## Closure obligations

A complete positive proof must explicitly close all of the following.

1. Disintegrate each segment solution using a single common conull set supporting integrability, initial state, pure-birth/single-jump support, and a countable determining family of natural-filtration martingale identities.
2. Paste the segment kernels by a tower-property calculation, including deterministic grid boundaries and the fact that no positive deterministic time is a jump time.
3. Show that invariant endpoint kernels give an invariant grid skeleton, construct an exactly equivariant canonical interpolation, and prove its distance from the true pasted solution tends to zero in a compact birth-time topology.
4. Pass the martingale problem through weak limits for finite-valued but globally unbounded Borel rates using fixed-marginal \(L^1(dt\,\mu_t)\) approximation.
5. Extend positive-time history tests to time zero by an explicit \(r\downarrow0\) \(L^1\) argument for the natural filtration, not merely by recovering the initial marginal.
6. Re-derive absence of simultaneous positive-time jumps in the weak limit from the limiting martingale problem, for example using the cylinder functions \(x_i,x_j,x_ix_j\); do not call this property topologically closed.
7. Recover all prescribed one-time DPP marginals, coordinatewise càdlàg pure-birth paths, and all cylinder tests simultaneously.

If (TFP) is false, give explicit admissible data satisfying the frozen DPP/rate hypotheses and identify the failed implication. General invariant-coupling counterexamples outside this DPP/rate class do not suffice.

## Scope

A proof closes only the two-time reduction and any correctly stated endpoint-law-uniqueness corollary. It does not prove arbitrary-group invariant existence until the local fixed points are constructed. Do not claim endpoint-only uniqueness is strictly weaker than weak uniqueness unless an actual separation or the necessary extension lemma is proved.

Return exactly PROVED, DISPROVED, or INCOMPLETE, followed by a complete supporting argument.
