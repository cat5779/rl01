# Bounded message laws and a one-step certificate

This auxiliary lemma supplies the infinite message bridge for [THEOREM.md](THEOREM.md). The finite probability signs require the separate exact certificates.
Only the almost-sure critical Bernoulli environment is considered.

Fix lambda >= 1 and C >= lambda^4. Every Bernoulli open cluster in the
binary rooted half-tree is finite almost surely. Contract these clusters.
At every vertex of the resulting rooted quotient tree there are at least
two forward edges. Indeed a cluster with n original vertices has n+1
forward boundary edges, since the root half-tree has one missing parent
edge. A non-root cluster has one parent boundary edge removed from its
n+2 boundary edges, with the same result. Every quotient-edge resistance
lies in [1,lambda^4]. This observation uses no one-endedness claim.

Consider a finite quotient tree cut at forward depth n. Give each cut
vertex an arbitrary additional resistance in [0,C] to the wired sink.
Every effective forward resistance is at most C, by induction: each
forward arm has resistance at most lambda^4+C <= 2C, and there are at
least two such arms. In a unit current flow, the current assigned to any
one arm is at most

    c = 2C/(1+2C) < 1

times the current entering its vertex. To see this, the chosen arm has
resistance at least 1 while at least one competing arm has resistance at
most 2C. Extra arms only decrease this bound. Thus every current reaching
a cut vertex is at most c^n. These cut currents are nonnegative and sum
to one. In particular their squared sum is at most c^n.

Let R_n(0) and R_n(z) be the root resistances with zero cut resistance
and arbitrary z in [0,C]. Rayleigh gives R_n(0) <= R_n(z). Extend the
minimizing flow for R_n(0) through the added cut resistances. Thomson's
principle gives

    0 <= R_n(z)-R_n(0) <= C sum_cut I_v^2 <= C c^n.

Consequently all bounded boundary assignments converge uniformly in the
boundary assignment to the wired root resistance. The quotient graph
can have arbitrarily large but finite degrees; the argument requires
only its two forward arms and finite truncations. If the half-tree root
cluster is conditioned by the parent-open bit and child-open count, its
finite conditional cluster still has at least two forward boundary
edges, so the same proof applies in each of the six conditional states.

This also identifies the limit of the original-depth message recursion
with the quotient wired resistance. For any fixed quotient depth n,
its finite set of contracted clusters is contained in an original
finite-depth truncation once that depth is sufficiently large. Finite
clusters and local finiteness ensure this containment. The remaining
boundary messages lie in [0,C], so the preceding sandwich proves the
identification, first for fixed n and then as n tends to infinity.

Let T be the six-state distributional message map, retaining the exact
parent bit, child count, independent descendant environments, and the
child-count law (1,2,1)/4. On distributions supported in [0,C], T is
monotone in stochastic order and has a unique bounded fixed law. For
clarity, uniqueness does not follow from stochastic monotonicity alone:
after expanding a depth-N recursive tree, any candidate bounded law is
realized by independent boundary messages with the prescribed conditional
state. Contracting the realized finite open clusters and applying the
uniform boundary estimate shows that every such expansion converges to
the same wired resistance law. Therefore any bounded fixed law is this
law. The same argument applies to iterations of any bounded initial
message law, without needing a fixed-point assumption.

In particular, a componentwise stochastic subsolution L <= T(L) and a
supersolution T(U) <= U, both supported in [0,C], satisfy

    L <= law(R_wired) <= U.

Iterating T from either of them preserves the respective order, and the
preceding boundary comparison identifies each limit with the same law.
Existence of a law-valued limit can also be obtained from compact support
and monotonicity. T is continuous under these limits: its series and
parallel maps are continuous on nonnegative finite arguments, including
parallel(0,0)=0.

For a directed grid, let Tlo use downward-rounded closed resistances,
floor the parallel result, and round the probability CDF upward; let
Tup use the opposite directions. Then

    Tlo(X) <= T(X) <= Tup(X).

A final integer PMF certificate therefore needs only

    L <= Tlo(L),       Tup(U) <= U,

checked by integer CDF comparisons in all six states. It need not replay
the author's search iterations. Grid values are in [0,P/M] with
P=ceil(M lambda^4), so C=P/M is admissible. This one-step test certifies
an infinite wired resistance enclosure, rather than a finite-depth or
population approximation.

The Bernoulli conditioning and independent descendant messages must
remain as in the six-state recursion of CONSTRUCTION. An arbitrary proposed
joint coupling cannot be substituted for this product message map.
