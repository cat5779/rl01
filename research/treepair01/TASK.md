# Finite-state splitting laws for the optimal tree coupling

Determine whether the following precisely restricted class contains a coupling. A negative answer only excludes this class; a positive answer must verify all finite cylinders and yields a Gamma-invariant monotone law, not automatically a joint iid factor.

Let Gamma=C3*C3 act on the bipartite 3-regular Bass–Serre tree, with unoriented edges a regular Gamma-set. Orient every ambient edge from its A-type endpoint to its B-type endpoint. Use the five edge states

`0, u+, u-, b+, b-`.

State 0 means vacant in T and B. The states u and b mean present in T; only b means present in B. Signs record an orientation of the T edge toward the unique end of its component, with + meaning A-to-B. At every A-vertex exactly one of its three incident states must have sign +; at every B-vertex exactly one must have sign -. This is a local support constraint, not a claimed global one-endedness theorem.

A splitting law here means the following data and **exact** conditional-independence property:

1. A common one-edge probability vector q on the five states.
2. Two probability tables P_A and P_B on cyclically ordered triples of edge states. Each table is invariant under cyclic rotation, satisfies its local one-outgoing support constraint, and has q as each of its three one-edge marginals. The cyclic orders come from the two C3 factors; reflection symmetry is not imposed.
3. Given the state on any one edge, the colored configurations in the two components after deleting that edge are independent. At a vertex of type X, conditional on its parent-edge state s with q(s)>0, its other two states have the conditional distribution of P_X given that specified coordinate equals s. The ordered positions are inherited from the cyclic order. Rooting at any vertex to generate these conditional branches must give the same cylinder law; the common marginals provide the usual consistency condition. Zero-mass states never occur and their conditional rows may be assigned arbitrarily.

Equivalently, for any finite connected subtree of vertices, the probability of a compatible assignment on all their incident edges is

`product_v P_type(v)(the three states at v) / product_internal_edges q(the edge state)`.

This equation, followed by summing boundary states, specifies every finite edge cylinder. It is the definition of the class; arbitrary hidden infinite state or conditioning on a chosen end is not allowed.

Required projected marginals, for **every finite edge set F** and every A subset of F:

`P(A subset B)=2^(-|A|)` and `P(A subset T)=det Q[A]`,

where Q is the gradient-projection kernel under the edge identification with Gamma:

`Q(x,x)=2/3`,

`Q(x,y)=(-1)^(ell(x^-1 y)+1)/(3*2^ell(x^-1 y))` for x!=y,

and ell is reduced syllable length. Inclusion–exclusion must therefore recover the full Bernoulli and WUSF marginals, rather than just their one-edge or star moments. In particular, for a finite connected edge set of m edges the upper inclusion probability is `2^(-m)(1+m/3)`.

The necessary one-edge vector has the form

`q(0)=1/3`, `q(b+)=theta`, `q(b-)=1/2-theta`,

`q(u+)=1/3-theta`, `q(u-)=theta-1/6`,

for some `theta in [1/6,1/3]`. Do not silently impose theta=1/4: Gamma preserves the bipartition, so endpoint-exchange symmetry is not part of the target.

Either supply explicit nonnegative tables and a proof of the required **all-finite-cylinder** identities, or derive an exact contradiction from a specified finite family of necessary identities valid for every table in this class. Numerical feasibility/infeasibility without an exact certificate is only a probe. If proving finitely many identities suffices, prove that sufficiency through the explicit transfer/branch recursion. If the class contains a law, check one-endedness through the resulting exact WUSF marginal and report factor realization separately.

This task is independent of random-conductance cluster contraction, Wilson stacks, and effective-resistance computations. Do not analyze those methods. No conclusion about all invariant couplings follows from failure of the splitting class.

## Deliverable

Add `research/treepair01/RESULT.md` to this branch, preserving this frozen task. Begin with `PROVED`, `DISPROVED`, or `INCOMPLETE`, with a self-contained derivation and the first unproved assertion if incomplete. No novelty claim is requested.
