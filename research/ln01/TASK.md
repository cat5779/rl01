# Two remaining Lyons factor questions

This task contains two logically independent problems.  A result on one problem
must not be reported as progress on the other.

## A. Full-automorphism DPP factor

Let `G` be a countable, connected, locally finite, vertex-transitive graph,
let `W=V(G)`, and let `Q` be a Hermitian positive contraction on `l2(W)`
commuting with every permutation induced by `Aut(G)`.  Decide whether the
determinantal law `P^Q` is an `Aut(G)`-factor of iid vertex labels: does there
exist a measurable map

`F:[0,1]^W -> {0,1}^W`

with law `P^Q` under product Lebesgue measure and satisfying
`F(alpha u)=alpha F(u)` for every `alpha in Aut(G)` (almost-everywhere
equivariance is sufficient; an everywhere-defined version is stronger)?

The factor may depend on `(G,Q)`.  A single graphwise rule working
simultaneously for all `(G,Q)` is not required.  A construction equivariant
only under a chosen countable transitive subgroup is not enough.

## B. Lyons--Thom Question 7.6

Let a countable group `Gamma` act quasi-transitively on a countable set `W`,
and let `A` be finite.  Decide whether the class of `Gamma`-invariant laws on
`A^W` that are factors of Bernoulli shifts is closed in Ornstein's invariant
`bar-d` metric.  For an orbit section `W0`,

`bar-d(mu,nu) = inf sum_{w in W0} P[X(w) != Y(w)]`,

where the infimum is over `Gamma`-invariant joinings of `mu` and `nu`.

The amenable case is known.  A negative answer must give genuine Bernoulli
factors converging in `bar-d` to a law proved not to be a Bernoulli factor.
Weak-star convergence alone is not responsive.

## Required output

For each problem separately, output exactly one of `PROVED`, `DISPROVED`, or
`INCOMPLETE`, followed by a complete supporting argument or the smallest
precise unresolved obstruction.  Check primary literature and separate
mathematical correctness from novelty.  Do not merge the Draft PR.
