# Scope and independent checks

Accepted scope: both exact optima in the frozen task, uniformly for `0 < eta <= 1/10`. Two different authors read the full returned proof against the original task. The second reviewer did not read the first review before completing its reconstruction. Both reviewers reused existing research contexts, so these are not fresh-context certifications.

The checks reconstruct the eight determinant atoms and their projector-direction derivatives; the twelve-edge incidence matrix; the attaining pair and triple; the pair potential and triple edgewise potentials; and the rank-four saturated incidence submatrix. The two checkers use independent symbolic and rational-polynomial implementations. Their exact results are recorded in CHECK.json and CHECK2.json.

Two terse arguments in the returned proof can be made explicit. First, every nonnegative divergence solution has bottom and top total mass q. Each doubleton outgoing edge is at most q; a singleton outgoing mass is at most q+h+13t <= 83/210. Empty and full states satisfy the same bound. Every atom is at least 79/840, so every capacity has slack at least 5(79/840)-83/210 = 3/40. Pairing divergence with cardinality gives total mass one. Thus the capacity reduction applies to the entire positive divergence fiber.

Second, equality in the pair dual forces zero difference on all eight nonsaturated edges. The four remaining incidence columns have rank four: they form two disjoint three-vertex trees. Hence the optimal ordered pair difference is uniquely determined. Its three cyclic rotations sum to -6t times the nonzero six-cycle circulation, whereas actual differences must telescope to zero.

The simultaneous lower bound applies directly to arbitrary triples. Each edge's three dual gradients have sum zero and positive-part sum at most one. The weighted sum of three edge masses is therefore at most their range, which equals half the sum of their three pair distances. Summing yields a total distance at least 156t, hence a maximum at least 52t. The displayed cyclic triple attains this bound. No equivariance or symmetrization restriction is imposed on competitors.

No mathematical edit to the returned proof was needed. Its bounded ratio 13/12 does not imply divergence in growing dimension and does not settle general FC. No formal proof or novelty certification is supplied.
