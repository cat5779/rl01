# Directed-double-cover interface audit

STATUS: CORRECT

The directed-double-cover construction is correct.  For a countable group acting on a fixed countable locally finite
simple graph, it turns a signed-equivariant FUSF projection into a genuinely commuting positive contraction on the
unsigned arc permutation representation.  Applying the frozen prescribed-\(W\) theorem H77 on the arc set and then
forgetting orientation gives exactly FUSF.  On a Cayley simple graph with a finite symmetric generating set, this also
gives the regular-\(\Gamma\)-iid source by finite digit splitting, including involutive generators.

This does not make H77 applicable to an uncountable full automorphism group, and it does not produce a jointly Borel
factor over a varying random graph.

## 1. Setup and the intertwiner

Let \(G=(V,E)\) be a fixed countable locally finite simple graph.  Choose one reference orientation \(e^+\) for every
unoriented edge \(e\), and write \(e^-\) for its reverse.  Let
\[
 A=\{e^+,e^-:e\in E\}
\]
be the directed-arc double cover.

Suppose a countable group \(\Gamma\) acts on \(G\).  Relative to the chosen reference orientations, its action on
\(\ell^2(E)\) is the signed permutation representation \(U_\gamma\): if \(\gamma e^+\) agrees with the reference
orientation of \(\gamma e\), the sign is \(+1\), and if it is the reverse reference orientation, the sign is \(-1\).
On \(\ell^2(A)\), let \(V_\gamma\) be the ordinary unsigned permutation of directed arcs.

Define the isometry \(T:\ell^2(E)\to\ell^2(A)\) by
\[
 (Tf)(e^+)=\frac{f(e)}{\sqrt2},\qquad
 (Tf)(e^-)=-\frac{f(e)}{\sqrt2}.
\]
The normalization gives \(T^*T=I\).  A direct check on each oriented basis vector gives
\[
 V_\gamma T=T U_\gamma. \tag{1}
\]
Indeed, when \(\gamma\) preserves the reference orientation, both sides move the antisymmetric pair
\((1,-1)/\sqrt2\) to the corresponding pair; when it reverses reference orientation, the unsigned arc permutation
swaps the two coordinates, multiplying that antisymmetric pair by \(-1\), exactly the sign in \(U_\gamma\).

Let \(Q\) be the reference-oriented FUSF kernel, so \(0\le Q\le I\) and
\(U_\gamma Q U_\gamma^*=Q\).  Put
\[
 \widetilde Q=TQT^*.
\]
Then \(\widetilde Q\) is Hermitian and
\[
 0\le \widetilde Q\le TT^*\le I.
\]
Using (1),
\[
 V_\gamma\widetilde QV_\gamma^*
 =V_\gamma TQT^*V_\gamma^*
 =TU_\gamma Q U_\gamma^*T^*
 =\widetilde Q. \tag{2}
\]
Thus \(\widetilde Q\) genuinely commutes with the **unsigned** permutation action on arcs.  No signed-action extension
of H77 is used.

## 2. At most one orientation of each edge

For a fixed edge \(e\), the \(\{e^+,e^-\}\)-principal block of \(\widetilde Q\) is
\[
 \frac{Q_{ee}}2
 \begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]
Its determinant is zero.  Therefore, for \(Y\sim\mathbf P^{\widetilde Q}\),
\[
 \mathbf P\{e^+,e^-\in Y\}=0. \tag{3}
\]
Since \(E\) is countable, a countable union shows that almost surely no edge has both arcs selected.

This conull statement is used only to identify the pushforward law.  It is not needed to define the factor map on
exceptional inputs.

## 3. Forgetting orientation gives exactly \(\mathbf P^Q\)

Define the total map
\[
 \pi:\{0,1\}^A\to\{0,1\}^E,
 \qquad
 \pi(y)_e=y_{e^+}\lor y_{e^-}. \tag{4}
\]
It is Borel and commutes with every graph automorphism on every input, including configurations that contain both arcs
of some edge.

Let \(B=\{e_1,\ldots,e_k\}\subset E\) be finite.  For a sign choice
\(\sigma=(\sigma_1,\ldots,\sigma_k)\in\{+,-\}^k\), let
\(B^\sigma=\{e_i^{\sigma_i}:1\le i\le k\}\).  Equation (3) makes the \(2^k\) events
\(\{B^\sigma\subseteq Y\}\) pairwise disjoint modulo null sets when they are used to specify which orientation covers
each edge.  More directly, their finite union differs from \(\{B\subseteq\pi(Y)\}\) only by the finite union of the
zero-probability double-arc events.

If \(D_\sigma\) is the diagonal \(k\times k\) sign matrix, then the corresponding principal matrix is
\[
 \widetilde Q_{B^\sigma}
 =\frac12D_\sigma Q_BD_\sigma.
\]
Hence
\[
 \det\widetilde Q_{B^\sigma}
 =2^{-k}\det(D_\sigma Q_BD_\sigma)
 =2^{-k}\det Q_B. \tag{5}
\]
Summing the \(2^k\) orientation choices gives
\[
 \mathbf P\{B\subseteq\pi(Y)\}
 =\sum_{\sigma\in\{+,-\}^k}\det\widetilde Q_{B^\sigma}
 =\det Q_B. \tag{6}
\]
These finite inclusion probabilities characterize the discrete DPP, so
\[
 \pi_*\mathbf P^{\widetilde Q}=\mathbf P^Q. \tag{7}
\]
The diagonal case \(k=1\) is included: each arc has marginal \(Q_{ee}/2\), their simultaneous probability is zero,
and their OR has marginal \(Q_{ee}\).

## 4. Consequence of H77

Apply H77 to the countable \(\Gamma\)-set \(A\) and the truly commuting positive contraction \(\widetilde Q\).  It
gives a total Borel exactly \(\Gamma\)-equivariant factor
\[
 F_A:[0,1]^A\longrightarrow\{0,1\}^A,
 \qquad (F_A)_*\lambda^A=\mathbf P^{\widetilde Q}.
\]
Then \(\pi\circ F_A\) is a total Borel exactly equivariant factor with law \(\mathbf P^Q\).  Thus, for countable
\(\Gamma\), the Cayley/FUSF consequence is a direct corollary of H77 itself; the law-level signed sampler extension in
`g6/source.md` is unnecessary for this countable-group conclusion.

## 5. Cayley graphs, reverse arcs, and involutions

Let \(G=\operatorname{Cay}(\Gamma,S)\) be a simple Cayley graph for a finite symmetric generating set \(S\), with the
usual exclusion of the identity generator.  The directed arc set is canonically
\[
 A\cong\Gamma\times S,\qquad (g,s)\longmapsto(g,gs). \tag{8}
\]
The reverse of \((g,s)\) is \((gs,s^{-1})\).  If \(s=s^{-1}\), these are still two distinct arcs because their initial
vertices are \(g\) and \(gs\).  Thus involutions cause no collapse in the double cover.  The left \(\Gamma\)-action on
\(\Gamma\times S\) is free and has \(|S|\) orbits.

Split the binary digits of each regular label \(U_g\) into \(|S|\) fixed streams, using a fixed total convention at
dyadic points.  This defines a total Borel left-equivariant map
\[
 [0,1]^\Gamma\longrightarrow[0,1]^{\Gamma\times S}
\]
whose pushforward is iid uniform on all arcs.  Composing with \(F_A\) and \(\pi\) proves that Cayley FUSF is a
regular-\(\Gamma\)-iid factor.  This argument keeps the directed arcs until the final OR map, so it never identifies
\(\Gamma\times S\) with the unoriented edge set and does not require an equivariant orientation choice.

## 6. Boundaries that remain

1. **Full automorphism group.**  If \(\operatorname{Aut}(G)\) is uncountable, one cannot simply set
   \(\Gamma=\operatorname{Aut}(G)\) in H77, whose group hypothesis is countability.  The double cover repairs the signed
   representation issue but does not repair this cardinality mismatch.  A full-automorphism conclusion still needs a
   pointwise-canonical construction argument or another extension.
2. **Random graphs.**  The construction is made after fixing \(G\) and reference orientations.  It supplies no common
   jointly Borel choice over a space of varying random rooted graphs.
3. **Graph conventions.**  Formula (8) uses a simple Cayley graph with a genuine set \(S\), no identity generator and
   one directed arc for each ordered generator step.  Multigraph conventions require retaining generator-labelled
   arcs as distinct coordinates; the same proof then applies to that labelled multigraph, but it is a different edge
   space.
4. **Local finiteness.**  The double-cover argument itself only needs countability.  Local finiteness is part of the
   stated graph/FUSF interface and is needed for the separate elementary vertex-iid-to-edge-iid stack construction,
   but that construction is no longer needed for the Cayley regular-source route above.

No claim about connectivity, low-cost repair, the Lyons--Gaboriau bridge, or varying-graph measurability is added.
