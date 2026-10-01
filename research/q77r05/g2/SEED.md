# Candidate extension of the Brownian observation argument

Status: ROOT-PROPOSED RESEARCH DIRECTION, NOT REVIEWED OR CERTIFIED.
This changes the statement from the concrete BS(2,3) kernel and is not covered
by an audit of that concrete statement. It requires a new complete proof and
fresh-context verification. Provenance: the Brownian posterior mechanism is
from the preserved G4 source; the canonical kernel-support exhaustion below
is a root proposal made after reading that source.

## Frozen proposed statement

Let W be a countable set, and let Gamma be a countable group acting on W by
permutations. Let Q be a bounded Hermitian positive contraction on l2(W)
commuting with this action. Is P^Q the image of product Lebesgue measure on
[0,1]^W under a total Borel Gamma-equivariant map to {0,1}^W?

The input is indexed by W, not necessarily by Gamma. No freeness, transitivity,
commensurated stabilizer, local finiteness of a given action graph, spectral
gap, amenability or soficity is assumed. No finitary or isomorphism assertion.

## Proposed equivariant finite exhaustion of the relevant component

For n>=1, define a simple undirected graph D_n on W by joining distinct x,y
when |Q(x,y)| >= 1/n. Let E_n(x) be the radius-n ball about x in D_n.

Since sum_y |Q(x,y)|^2 = (Q^2)(x,x) <= Q(x,x) <= 1,
the degree in D_n is at most n^2. Thus E_n(x) is finite. These sets are nested,
contain x and satisfy E_n(gx)=gE_n(x). Their union is the component C(x) in
the graph of nonzero off-diagonal entries of Q: any finite nonzero-edge path
appears at some threshold n and within radius n.

Q is block diagonal over those components. DPP restrictions to disjoint
components should therefore be independent: finite inclusion determinants
factor over blocks, then finite-pattern inclusion-exclusion and a monotone
class argument give sigma-field independence. This must be proved explicitly.

## Proposed Brownian proof obligations

For the actual marginal on E_n(x), tilt by
exp(sum_{z in E_n(x)} (y_z-t/2) eta_z), and let b^n_{t,x}(y) be its mean at x.
The finite external-field DPP identity in the G4 source suggests the uniform
bound sum_z |partial_{y_z} b^n_{t,x}| <= 1/2, including singular kernels.
Define b_{t,x}(y)=limsup_n b^n_{t,x}(y) on every real field.

The limsup is Borel, bounded, equivariant, and 1/2-Lipschitz for bounded
differences of fields in the sup norm. Picard iteration should solve
Z_t(x)=w_t(x)+integral_0^t b_{s,x}(Z_s) ds pathwise for every countable field
of continuous paths w, using bounded differences rather than assuming the
noise lies in l-infinity.

For independent eta~P^Q and iid Brownian B, put X_t=t eta+B_t. Finite Bayes,
upward martingale convergence on C(x), and component independence should give
b_{t,x}(X_t)=E[eta_x | X_t(z), z in W]. Independent Brownian bridges then
identify conditioning on the whole observed path through t. The innovations
beta=X-integral b(X) should be an iid Brownian field relative to one usual
filtration, by finite-dimensional martingale/bracket characterization.

Pathwise uniqueness identifies X with the deterministic solution driven by
beta. The total factor is liminf_n 1{Z_n(x)>n/2}. Summable Gaussian error
exp(-n/8) identifies its law with P^Q, with a single input Brownian field.
An identical Borel Uniform-to-Wiener encoding at every site supplies [0,1]^W.

## Attacks required before any promotion

1. Verify tilt closure for every finite positive contraction, especially
   eigenvalues 0 and 1, complex Hermitian entries and deterministic bits.
2. Verify that the root-dependent E_n(x) suffice: posterior limits recover
   only C(x), and using the rest of W requires genuine independence.
3. Verify joint measurability in time/field, limsup Lipschitz preservation,
   pathwise integral existence for all noise fields and causal measurability.
4. Verify the full observation-past posterior and vector Brownian property,
   with usual augmentation, without an infinite-product Girsanov density.
5. Check exact equivariance on all inputs and distinguish W-indexed source
   from the generally impossible regular-Gamma source for infinite stabilizers.
6. Novelty is separate. Nam--Sly--Zhang's observation construction and any
   uniform-covariance/stochastic-localization factor theorem are candidates
   for prior art; lack of a search hit does not certify novelty.
