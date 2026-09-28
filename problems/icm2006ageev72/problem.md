# Frozen problem

Let \((X,\mathcal B,\mu)\) be a nonatomic standard probability space and let \(T:X\to X\) be an invertible measure-preserving transformation, where transformations equal almost everywhere are identified.

The transformation \(T\) is **rank one** if there are measurable bases \(B_n\in\mathcal B\) and heights \(h_n\ge 1\) such that

1. \(B_n,TB_n,\ldots,T^{h_n-1}B_n\) are pairwise disjoint; and
2. the associated tower partitions generate \(\mathcal B\) modulo null sets: for every \(A\in\mathcal B\),
   \[
   \inf_{J\subseteq\{0,\ldots,h_n-1\}}
   \mu\!\left(A\,\triangle\!\bigcup_{j\in J}T^jB_n\right)\longrightarrow 0.
   \]

Let \(U_T:L^2(X,\mu)\to L^2(X,\mu)\) be the Koopman unitary \(U_Tf=f\circ T\), and let
\[
L^2_0(X,\mu)=\left\{f\in L^2(X,\mu):\int_X f\,d\mu=0\right\}.
\]
The **maximal spectral type** of \(U_T|_{L^2_0}\) is the measure class on the unit circle that dominates the spectral measure of every vector in \(L^2_0\). It is **singular** if that measure class is singular with respect to normalized Lebesgue measure on the unit circle.

> **Problem 7.2 (Ageev, ICM 2006).** Is it true that every rank-one transformation has a singular spectrum?

The task is to prove the universal assertion exactly as stated or to disprove it by constructing a rank-one invertible probability-preserving transformation whose maximal spectral type on \(L^2_0\) has a nonzero absolutely continuous component. Results for flows, nonsingular transformations, infinite-measure systems, random subclasses, or restricted cutting parameters do not settle this frozen problem.
