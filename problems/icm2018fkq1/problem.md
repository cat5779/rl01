# Frozen problem

Fix an integer \(d\ge 1\) and write \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\). For \(\alpha\in\mathbb R^d\), let
\[
T_\alpha(x)=x+\alpha\pmod{\mathbb Z^d}.
\]
The translation vector \(\alpha\) is **Diophantine** in the convention of the ICM article if \((1,\alpha_1,\ldots,\alpha_d)\) is nonresonant and there exist constants \(\gamma>0\) and \(\sigma>0\) such that
\[
\left|k_0+k_1\alpha_1+\cdots+k_d\alpha_d\right|
\ge
\frac{\gamma}{\bigl(|k_0|+\cdots+|k_d|\bigr)^\sigma}
\]
for every nonzero \((k_0,\ldots,k_d)\in\mathbb Z^{d+1}\).

Let \(f:\mathbb T^d\to\mathbb T^d\) be a \(C^\infty\) diffeomorphism in the identity component (the article's \(\mathrm{Diff}_0^\infty(\mathbb T^d)\)). Suppose there is a homeomorphism \(h:\mathbb T^d\to\mathbb T^d\) such that
\[
h\circ f=T_\alpha\circ h.
\]

> **Question 1 (Fayad–Krikorian, ICM 2018).** Must the topological conjugacy be smooth? Equivalently in the intended source sense, must \(f\) be \(C^\infty\)-conjugate to \(T_\alpha\)?

The question is already known to have a positive answer for \(d=1\). The unresolved obligation is the unrestricted higher-dimensional case \(d\ge 2\). A disproof must give a smooth torus diffeomorphism, a Diophantine translation vector, and a topological conjugacy satisfying the displayed equation, while proving that no smooth conjugacy to that translation exists. A local KAM result, an almost-reducibility statement, a result for hyperbolic toral automorphisms, or a conjugacy to a non-Diophantine translation does not settle the question.
