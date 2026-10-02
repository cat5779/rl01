# Compact complete proof of the local endpoint fixed-point reduction

## Frozen theorem

Let a countable group \(\Gamma\) act by coordinate permutations on a countable set, let
\[
K_t=C+tH,\qquad \varepsilon I\preceq K_t\preceq(1-\varepsilon)I,
\]
be an equivariant linear DPP path, and let \(a_i(t,x)\) be finite-valued jointly Borel covariant pure-birth rates satisfying the exact cylinder continuity equation and
\[
\int_0^1\!\int a_i(t,x)\,\mu_t(dx)\,dt<\infty
\]
for every coordinate. Ordinary prescribed-marginal weak solutions exist.

For \(0\le u<v\le1\), let \(\mathcal E_{u,v}\) be the endpoint laws of ordinary prescribed-generator solutions on \([u,v]\). Prove or disprove:
\[
\text{a global \(\Gamma\)-invariant prescribed-generator weak path law exists}
\]
if and only if, along some sequence of finite partitions with mesh tending to zero, every adjacent cell satisfies
\[
\mathcal E_{u,v}^{\Gamma}\ne\varnothing.
\tag{TFP}
\]
The invariant endpoint choices may be independent between cells and refinements.

## Exact closure obligations

A complete proof must explicitly cover, in a compact form:

1. one common conull set for disintegration, integrability, path support, and a countable determining family of natural-filtration martingale identities;
2. segment pasting by the tower property, including deterministic grid boundaries and their absence of positive-time jumps;
3. invariance of the grid skeleton from invariant endpoint laws;
4. an exactly equivariant canonical birth-time interpolation and a mesh-size coupling estimate in a compact birth-time topology;
5. weak-limit closure of the martingale problem for finite-valued but globally unbounded Borel rates via fixed-marginal \(L^1(dt\,\mu_t)\) approximation;
6. the \(r\downarrow0\) argument that closes the natural filtration at time zero;
7. simultaneous recovery of all one-time DPP marginals, all cylinder tests, coordinatewise càdlàg pure-birth support, and a derivation of no simultaneous positive-time jumps from the limiting martingale problem.

Necessity must also be stated. This is only a two-time reduction: do not claim that the local invariant endpoint elements always exist for arbitrary groups. Do not add an endpoint-uniqueness corollary unless it is separately justified.

## Source-completeness constraint

The entire proof must appear in the response itself and must be at most 18,000 Unicode characters, including displayed formulas. Do not rely on an attachment, archive, hidden continuation, or omitted tail. The final equivalence and scope sentence must be present before the response ends.

Return exactly PROVED or DISPROVED, followed by a complete supporting argument.



