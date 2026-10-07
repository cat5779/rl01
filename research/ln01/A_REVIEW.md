# Independent review of Problem A

## Verdict

`CORRECT / PROVED`.

Let `W` be countable and let `Q` be a Hermitian positive contraction on
`l2(W)`.  Write

`S_Q = {pi in Sym(W) : Q(pi x,pi y)=Q(x,y) for all x,y}`.

The construction in `research/q77r05/g4/PROOF.md`, and in the stronger
parameterized form in `research/paperA_r01/t1/paperA.md`, gives a total Borel
map from `[0,1]^W` to `{0,1}^W` with law `P^Q` that commutes, on every input,
with every member of `S_Q`.  No countability assumption on `S_Q` is used.

Consequently, when `W=V(G)` and `Q` is invariant under the full automorphism
group of a countable graph `G`, the DPP is a full `Aut(G)`-factor of iid vertex
labels.  Choosing a countable transitive subgroup is unnecessary.

## Load-bearing checks

1. The threshold graph joining `x` and `y` when `|Q_xy| >= 1/n` has degree at
   most `n^2`.  Its radius-`n` balls are finite, nested, and transported
   exactly by every kernel-preserving permutation.  Their union is the
   nonzero-kernel support component.
2. Distinct support components are independent as complete configuration
   sigma-fields.  This follows from inclusion--exclusion and factorization of
   every finite block determinant, followed by a monotone-class argument.
3. Every finite exponential tilt remains determinantal, including complex
   Hermitian and singular kernels.  Its covariance row has absolute sum at
   most `1/2`, giving a dimension-free posterior Lipschitz estimate.
4. The limsup drift is total Borel on all real fields.  Picard iteration only
   estimates bounded differences of solutions, so a spatial Brownian field
   is never assumed to be `l-infinity`-valued.
5. Finite endpoint Bayes formulas, upward conditional-expectation convergence,
   component independence, and Brownian-bridge independence identify the
   posterior for the full observation history.  Fixed-time exceptional sets
   enter time integrals through measurability and Fubini; there is no
   intersection over all real times.
6. The innovations are continuous martingales in one usual filtration, with
   joint bracket `tI` on every finite coordinate set.  The vector Levy
   characterization therefore gives a product Brownian path field, rather
   than only pairwise zero covariance.
7. Pathwise uniqueness gives a same-noise identity.  The total sitewise
   Brownian encoding and binary liminf decoder are Borel on every input;
   Borel--Cantelli is used only to identify the push-forward law.
8. Equivariance of the threshold sets, drift, Picard iterates, decoder, and
   readout is algebraic on their complete domains.  Hence no conull-set
   intersection over the possibly uncountable group `S_Q` occurs.

## Relation to the existing public manuscript

This is a scope confirmation, not a new sampling mechanism.  The public
manuscript `research/paperA_r01/t1/paperA.md`, merged through PR 106, already
states the stronger jointly Borel natural sampler: it is Borel in the kernel
and natural under arbitrary bijections of countable index sets.  Problem A is
an immediate fixed-kernel consequence of that theorem.  Its mathematical
status had been understated when only the narrower theorem statement in PR 85
was consulted.

This review makes no claim about Problem B, novelty, priority, finitary coding,
or a regular group-indexed source for arbitrary actions with infinite
stabilizers.
