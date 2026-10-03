# Frozen problem

A **three-dimensional singular Ricci flow** is understood exactly in the sense used by Kleiner's ICM article and Kleiner–Lott: it is a Ricci-flow spacetime
\[
\mathcal M=(\mathcal M,\mathfrak t,\partial_{\mathfrak t},g)
\]
whose spacetime \(\mathcal M\) is a smooth four-manifold with boundary at the initial time, whose time function \(\mathfrak t:\mathcal M\to[0,\infty)\) has slices \(\mathcal M_t=\mathfrak t^{-1}(t)\), whose time vector field satisfies \(\partial_{\mathfrak t}\mathfrak t=1\), and whose smooth metric on \(\ker(d\mathfrak t)\) evolves by
\[
\mathcal L_{\partial_{\mathfrak t}}g=-2\operatorname{Ric}(g).
\]
In addition it has compact normalized initial slice and satisfies the scalar-curvature properness, completeness, Hamilton–Ivey pinching, and canonical-neighborhood axioms in the standard singular-Ricci-flow definition. These axioms are part of the object, not conclusions to be proved; `source.md` fixes the exact reference.

For a time \(t>0\), interpret \(\bar t\nearrow t\) as approach from below. A component of \(\mathcal M_{\bar t}\) **goes extinct** if its spacetime continuation becomes empty at a time not exceeding \(t\). A **(possibly degenerate) neckpinch singularity** is meant in the canonical-neighborhood/singular-Ricci-flow sense of the cited source; no narrower Type-I or nondegenerate-only interpretation is allowed.

> **Conjecture 3.14 (Kleiner, ICM 2022).** If \(\mathcal M\) is a singular Ricci flow, then the set of times \(t\) for which \(\mathcal M_t\) is noncompact is finite. Moreover, if \(\mathcal M_t\) is noncompact, then as \(\bar t\nearrow t\), each connected component of \(\mathcal M_{\bar t}\) either goes extinct or experiences finitely many (possibly degenerate) neckpinch singularities.

Both clauses are part of the frozen target. The component in the second clause belongs to the earlier slice \(\mathcal M_{\bar t}\), not to \(\mathcal M_t\). A proof only for a special initial topology or only for Type-I/nondegenerate singularities does not settle the conjecture. A counterexample must be a genuine singular Ricci flow satisfying every defining axiom and must violate at least one of the two clauses.
