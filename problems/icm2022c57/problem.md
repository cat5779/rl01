# Frozen problem

Let
\[
\mathcal T=\{(\alpha,\beta,\gamma)\in(0,\pi)^3:\alpha+\beta+\gamma=\pi\}
\]
be the two-dimensional parameter space of similarity classes of labeled, nondegenerate Euclidean triangles. Side \(i\) is opposite the correspondingly labeled angle. The topology is the relative Euclidean topology on this open simplex.

A billiard path is a straight polygonal path in the triangle that avoids all vertices and, at every side hit, obeys specular reflection: angle of incidence equals angle of reflection. It is periodic when it returns to its initial point with its initial direction. Its **bounce word** is the finite cyclic sequence in \(\{1,2,3\}\) recording the side labels met during one period. Choosing a different starting hit cyclically rotates the word; reversing direction reverses it. These changes do not change the supporting parameter set.

A periodic path, or its bounce word \(w\), is **stable** if the same finite side sequence is realized by a periodic billiard path for every sufficiently small perturbation of the labeled triangle. Equivalently in the source's unfolding language, the first and last copies of the starting side are parallel for every triangle and the word is realized for at least one triangle.

For every stable word \(w\), define its orbit tile by
\[
O(w)=\{T\in\mathcal T:T\text{ supports a nonsingular periodic billiard path with bounce word }w\}.
\]
Thus \(O(w)\) is the entire supporting set for the word, not a chosen connected component. It is a nonempty open subset of \(\mathcal T\).

Prove or disprove:
\[
\boxed{\text{For every stable word }w,\;O(w)\text{ is connected and simply connected.}}
\]

“Simply connected” means path connected with trivial fundamental group in the ordinary topology of \(\mathcal T\); since connectedness is also asserted, an empty-set convention is irrelevant. Degenerate triangles on the boundary \(\alpha\beta\gamma=0\) are not members of \(\mathcal T\). A counterexample must give an actual stable word and an independently checkable exact description or certificate showing disconnection or a nontrivial hole. A finite-resolution plot alone is not a proof.
