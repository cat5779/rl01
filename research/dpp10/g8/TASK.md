# Dimension-free selection of rank-one determinantal birth flows

## Frozen primary problem

For each fixed 0 < epsilon < 1/2, is there a finite constant C_epsilon, independent of the positive integer n, with the following property?

For every complex Hermitian matrix epsilon I <= K <= (1−epsilon)I on E={1,...,n} and every unit vector v in C^n, choose nonnegative numbers F_(K,v)(S,i), indexed by S subset E and i notin S. Let p_K(S) be the exact DPP configuration probability, and set

\[
b_{K,v}(S)=\left.\frac{d}{dh}p_{K+hvv^*}(S)\right|_{h=0}.
\]

Require the upward-edge flow equations

\[
b_{K,v}(S)=\sum_{i\in S}F_{K,v}(S\setminus\{i\},i)
              -\sum_{i\notin S}F_{K,v}(S,i),
\qquad
\sum_{S,i\notin S}F_{K,v}(S,i)=1,
\]

and the pointwise outgoing-capacity bound

\[
\sum_{i\notin S}F_{K,v}(S,i)\le(2/\epsilon)p_K(S).
\]

The selection must be Borel in (K,v), depend only on vv*, and commute with every permutation of E. For two admissible pairs (K,v),(L,w) on the same E, require

\[
\sum_{S,i\notin S}|F_{K,v}(S,i)-F_{L,w}(S,i)|
\le C_\epsilon\bigl(\|K-L\|_1+\|vv^*-ww^*\|_1\bigr),
\tag{DF}
\]

where ||.||_1 is the unnormalized matrix trace norm. Prove this selection theorem or disprove it by an explicit family showing that every admissible choice has unbounded required constants. A counterexample to one arbitrary tie-breaking rule or to one optimizer is not a disproof of this existential selection problem.

## Inputs and motivation

Feasibility for each individual (K,v) is known. For h=epsilon/2, a monotone coupling between the DPPs of K and K+hvv* can add at most one point. Its off-diagonal edge masses divided by h give the displayed flow and capacity, because finite DPP probabilities are affine along a rank-one line. This follows from nested projection coupling and a support-minimal dilation; see Lyons, *Determinantal probability measures* (2003), Proposition 10.3, https://numdam.org/item/10.1007/s10240-003-0016-0.pdf . Do not present this feasibility observation as new.

For each fixed n, polyhedral positive-flow selection gives continuity estimates, but current estimates depend badly on n, especially after dividing by configuration probabilities. The new problem is uniform stability while retaining a uniform outgoing capacity. The invariant infinite-volume construction needs more than individual measurable selections: it must compare two approximations on a common random input. Different positive flows can have exactly the same DPP forward equation.

A possible approach is a uniquely specified convex minimizer on the feasible flow polytope, with a carefully weighted objective; another is an explicit rank-one coupling preserving quantitative stability. Treat these as suggestions, not added hypotheses. If an entropic or quadratic optimizer fails, determine whether this is a method obstruction or an obstruction to all selections.

## Required scope analysis

Explain what (DF), if true, yields for the weighted mean difference of intrinsic rates F_(K,v)(S,i)/p_K(S). Identify any additional dimension dependence or DPP total-variation input. Do not claim that (DF) alone solves general infinite-volume ordered iid coupling: translating a finite support estimate into an invariant per-site estimate and identifying limiting marginals remain separate obligations.

If the frozen theorem cannot be settled, report INCOMPLETE and isolate a proved restricted statement or a mathematically exact obstruction. Keep a restriction such as fixed v, diagonal K, bounded n, or commuting kernels explicitly separate. Numerical optimization is a probe, not a dimension-free proof. Cite primary sources for related selection or coupling results and distinguish rediscovery from novelty.
