# Fair-vertex mass transport from the regular edge action

Let Gamma=C3*C3 act on its 3-regular bipartite Bass–Serre tree. Vertices have types A and B. Unoriented edges form a regular Gamma-set. Each vertex stabilizer is C3 and cyclically permutes its three incident edges. Fix an edge e0 with endpoints o_A,o_B. A fair vertex observation means choosing each endpoint with probability 1/2, independently of the configurations.

The identity below uses only invariance of the marked probability law and equivariance of the nonnegative transport. It applies to the lifted oriented quotient law.

For completeness, the fair-vertex mass-transport identity follows from the regular edge action. Let F(v,w) be any nonnegative measurable equivariant transport on vertices, possibly depending on the joint configuration. Define the transport on edges by

\[
f(e,e')=\frac19\sum_{v\in e}\sum_{w\in e'}F(v,w).
\]

Writing e_g=g e0, invariance gives

\[
\sum_g\mathbb E f(e_0,e_g)
=\sum_g\mathbb E f(e_{g^{-1}},e_0)
=\sum_g\mathbb E f(e_g,e_0).
\]

These equalities use Tonelli and the bijection g to g^{-1}. Each vertex belongs to three edges, so the two sides are respectively

\[
\frac13\sum_{v\in\{o_A,o_B\}}\mathbb E\sum_wF(v,w),
\quad
\frac13\sum_{w\in\{o_A,o_B\}}\mathbb E\sum_vF(v,w).
\]

Cancelling the common factor proves

\[
\mathbb E\sum_wF(o,w)=\mathbb E\sum_vF(v,o)
\tag{1}
\]

under the fair vertex observation. Extended infinite values are allowed. Thus no vertex-transitivity hypothesis on Gamma, and no unannounced larger symmetry group for the joint law, is used.
