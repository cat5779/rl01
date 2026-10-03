# Support-degeneration continuity of the weighted minimizer

Fix a finite E of size n and epsilon in (0,1/2). Keep every upward cube edge as a variable, including directions forced to zero by P_ii=0. The full feasible fiber is described by
\[
Af\le c(K,P),\qquad Hf=d(K,P), \tag{1}
\]
where the matrices A,H are fixed for this E. Specifically, A encodes nonnegativity and vertex outgoing capacities, H encodes divergence and total mass one. The right sides are continuous: exact atom probabilities are determinant polynomials and their rank-one directional derivatives are polynomial in the real matrix coordinates.

No new constraints with parameter-dependent normal vectors are added when P_ii vanishes. Instead the coordinate-mass identity, which follows from the divergence equalities, forces those variables to zero. This fixed-normal description is essential below.

## 1. Finite-dimensional error bound with all conditions stated

For fixed finite real matrices A,H, every nonempty set
\[
F(c,d)=\{z:Az\le c,\ Hz=d\}
\]
satisfies
\[
\operatorname{dist}_2(x,F(c,d))
\le C_{A,H}
\bigl(\|(Ax-c)_+\|_2+\|Hx-d\|_2\bigr). \tag{2}
\]
The constant depends only on these matrices. This is the classical finite-dimensional polyhedral error bound; the following argument explains why no parameter uniformity is assumed beyond the fixed normals.

Delete redundant rows of H. Let z be the Euclidean projection of x onto the nonempty closed convex polyhedron. Its projection normal x-z belongs to the cone of active inequality normals plus the row space of H. This normal-cone description follows from the finite linear Farkas alternative. Choose a representation using active inequality rows independent modulo row(H): any dependence can be removed by adjusting the nonnegative coefficients until one is zero, while absorbing the row(H) component into the unconstrained equality coefficients.

The combined selected-row matrix B therefore has full row rank. Write x-z=B*lambda, where the selected inequality coefficients are nonnegative. Since there are only finitely many possible full-rank selected-row matrices, their smallest singular values have a positive minimum eta. It follows that
\[
\|\lambda\|_2\le \eta^{-1}\|x-z\|_2.
\]
Dotting the normal representation against x-z uses equality of every selected active constraint at z. Negative inequality residuals may be discarded because their coefficients are nonnegative. Cauchy--Schwarz then gives
\[
\|x-z\|_2^2
\le\|\lambda\|_2
 \bigl(\|(Ax-c)_+\|_2+\|Hx-d\|_2\bigr).
\]
Division proves (2), with C=eta^-1. If the projection normal is zero the assertion is immediate. Consistent deleted equality rows can be restored without affecting the bound. The finite Farkas alternative here applies to ordinary real linear inequalities and equalities; no smoothness, strict feasibility, or boundedness of the polyhedron is assumed.

## 2. Feasible competitors at every nearby input

Let x_m=(K_m,P_m) tend to x=(K,P) in the commuting gapped domain. Every fiber is nonempty, by the inherited positive endpoint coupling, and compact because flows are nonnegative with total mass one.

Take any f in F(x). Its violations of the system at x_m are bounded by the differences of the continuous right sides. Equation (2) supplies f_m in F(x_m) with f_m tending to f. This proves lower hemicontinuity. Closedness of the graph follows directly from (1). Compact graph alone would not have supplied the competitor sequence.

## 3. Continuity of the objective along the feasible graph

Define on feasible pairs
\[
\mathcal E(K,P,f)
=\tfrac12\sum_{e:w_{K,P}(e)>0}f_e^2/w_{K,P}(e).
\]
Every reduced exact atom is at least epsilon^(n-1), by multiplying its n-1 sequential conditional probabilities, all of which have the same epsilon gap. Thus
\[
w_{K,P}(S,i)\ge P_{ii}\varepsilon^{n-1}.
\]
The coordinate-mass identity gives \(0\le f(S,i)\le P_{ii}\). Consequently
\[
0\le f(S,i)^2/w_{K,P}(S,i)
\le P_{ii}\varepsilon^{-(n-1)}. \tag{3}
\]
For a sequence of feasible triples tending to one with P_ii=0, the edge contribution tends to zero by (3), matching its deleted-term definition at the limit. If the limit P_ii is positive, ordinary continuity of the numerator and positive denominator applies. There are only finitely many edges. Therefore E is continuous on the entire feasible graph, including all changes of projector support.

## 4. Continuity and covariance of the rule

Let f_m be the unique weighted minimizer at x_m. Every subsequence has a further convergent subsequence in the unit-flow simplex. Its limit f is feasible at x by graph closedness.

For any g in F(x), choose the nearby feasible g_m from Section2. Optimality and graph-continuity of the objective give
\[
\mathcal E(x,f)
=\lim_m\mathcal E(x_m,f_m)
\le\lim_m\mathcal E(x_m,g_m)
=\mathcal E(x,g).
\]
The minimizer is unique on the nonforced directions and all remaining directions are zero, so f=Psi(x). Every subsequential limit is the same. Thus the whole sequence converges and Psi is continuous for this fixed E. Permutation covariance follows from naturality of the feasible system and weights and uniqueness.

The parameter domain for this fixed E is compact, so the rule is also uniformly continuous there. Neither the polyhedral constant C_A,H nor the atom lower bound epsilon^(n-1) is dimension independent. This statement fills the original topological gap and implies Borel dependence, but cannot be substituted for the dimension-free estimate required by full FC.

## 5. Scope of the supplement

The G16 weighted optimizer is one globally defined continuous rule on every fixed finite-dimensional commuting domain. The PROOF03.md with ERRATUM03.md additionally gives a dimension-free one-half Hölder modulus when P is held fixed. This supplement gives no dimension-free modulus when P changes and no exponent-one theorem. The original source's compactness/uniqueness sentence was missing the lower-hemicontinuity argument supplied in Sections1--2.
