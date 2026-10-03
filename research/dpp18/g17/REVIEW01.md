# Adversarial review of the bounded-component selector proof

## Review status

This file records an adversarial re-review of `RESULT.md`. It is **not an
independent external referee report**: the proof and this review were produced
within the same ChatGPT research session. The review intentionally re-derived
the vulnerable steps and attempted to falsify the argument, but it cannot rule
out correlated model error. No formal verification or novelty certification is
claimed.

Subjective confidence after this review: **about 0.90** that the stated proof is
mathematically correct as written. This number is not a statistical confidence
level and is not inferred from the supplementary numerical checks.

The conclusion of the review is that the proof addresses the frozen theorem in
`TASK.md` without adding a common-partition hypothesis, changing the norm,
relaxing the original capacity, restricting to real kernels, or bounding the
environment dimension. No unresolved mathematical gap was found in the review.
The remaining verification gap is independent third-party/domain review.

## 1. Scope audit: no substitution of the theorem

The proof is checked against the frozen task from PR #124 at commit
`8f7f8d0460f7e6c59f2ae47d3ca631629601922b`.

The claimed selector is defined for every finite coordinate set `E`, every
gapped complex Hermitian kernel whose canonical connected components have size
at most the fixed `r`, and every rank-one projector. The matrix norm is the
unnormalized Schatten trace norm. The flow is required to lie in the original
fiber with exact divergence, nonnegativity, total mass one, and pointwise
outgoing capacity `(2/epsilon) p_K(S)`.

The constant is allowed to depend on `(epsilon,r)` but not on `|E|` or on the
number of components. The proof explicitly does **not** claim a bound uniform
as `r -> infinity`, and therefore does not settle the unrestricted non-diagonal
selector problem.

## 2. Fixed-normal projection is the first critical point

A dangerous but invalid shortcut would be: “the quadratic objective is strongly
convex, therefore the minimizer is Lipschitz when the feasible set moves.” That
statement is false in that level of generality.

`RESULT.md` instead proves the special lemma needed here. The feasible set has
the form

\[
C(u)=\{z:Az\le u\}
\]

with a **fixed** matrix `A`; only the target `y` and right-hand side `u` move.
At a Euclidean projection, the normal vector can be represented by a linearly
independent subset of active normals. For each such subset `I`, the projection
has the affine formula

\[
q_I(y,u)=(I-A_I^\dagger A_I)y+A_I^\dagger u_I.
\]

The domain on which this formula is valid is a closed convex polyhedron. A
finite collection of these regions covers the feasible parameter domain, and
on overlaps the formulas agree by uniqueness of the Euclidean projection.
Subdividing a parameter line segment by these regions yields a global
Lipschitz bound.

This argument does not use strict feasibility, strict complementarity, a
locally fixed active set, or a locally constant fiber dimension. Degenerate
faces, forced zero edges, and lower-dimensional fibers are therefore included.
No gap was found here.

## 3. The explicit constraint matrix and its quantitative bound

The total-mass equation is first shown to follow exactly from the divergence by
testing divergence against set cardinality. Therefore it is legitimate to use
only

\[
A_n=[-I;D;-D;O]
\]

as the fixed inequality matrix.

The proof that `A_n` is totally unimodular was checked separately. After
expanding identity rows and removing opposite duplicate incidence rows, one
reduces to minors of `[D;O]`. If an incidence row and outgoing row at the same
vertex both occur, adding the outgoing row to the incidence row turns that
incidence row into an incoming row. After changing signs of the outgoing rows,
each edge column has at most one `+1` and at most one `-1`. Such square matrices
have determinant `0,+1,-1` by elementary expansion/zero-column-sum arguments.

Hence nonsingular square minors have determinant `+/-1`, and the active-system
pseudoinverses admit a finite bound depending only on the local dimension.
The qualitative theorem needs only finiteness for each fixed `n`; the explicit
constant in `RESULT.md` uses the displayed coarse bound.

No dependence on the ambient `|E|` is introduced: this local `n` is always at
most the fixed component bound `r`.

## 4. No circularity in the refinement induction

The main logical risk is circularity: to extend a selector over an `n`-block,
one must already have a jointly Lipschitz prescription on **all** splitting
strata, including intersections of incompatible splittings.

The induction in `RESULT.md` avoids that circle. At stage `n`, the prescribed
boundary is the whole disconnected-kernel locus `Z_n`. Every connected
component of a kernel in `Z_n` has size at most `n-1`, so the boundary value is
the already-constructed global selector with component bound `n-1`. The
cross-stratum Lipschitz comparison for that smaller bound has already been
proved by the common-refinement argument before the stage-`n` extension is
invoked.

A coordinatewise McShane extension is then symmetrized over the finite
permutation group and projected onto the current original fiber. On `Z_n`, the
prescribed value is already feasible, so the Euclidean projection fixes it
**exactly**. Thus the new local selector agrees at every proper splitting and
at every intersection of splitting strata, not merely in a limiting sense.

No circular dependency was found in this order of construction.

## 5. Zero block weights and off-block projector entries

For a rank-one global projector `P=vv*`, a principal compression
`P_B=v_B v_B*` has rank at most one. The construction uses the homogeneous
local flow in the unnormalized matrix `P_B`; it does not replace the global
input by the generally higher-rank pinched matrix.

The normalization `P_B / tr(P_B)` is only used internally when the weight is
positive. The estimate

\[
\min(w,v)\|R-T\|_1\le2\|wR-vT\|_1
\]

removes the apparent reciprocal-weight singularity, and zero-weight blocks are
handled directly.

When `K` is block diagonal, the inverse atom matrix
`(K-I_{S^c})^{-1}` is block diagonal. Therefore all off-block entries of the
global rank-one projector disappear from the trace in the exact derivative
formula for `b_{K,P}`. This is an exact identity, not an approximation or an
extra block-diagonal-direction assumption.

## 6. Tensorization keeps the original fiber

Each homogeneous block flow has the correct local divergence, nonnegativity,
mass equal to its block weight, and outgoing capacity

\[
(2/\varepsilon) w_B p_{K_B}.
\]

Multiplying by the outside product DPP law and summing over blocks gives exact
global divergence and total mass `sum_B w_B = 1`. The capacity is

\[
F_{\rm out}(S)
\le (2/\varepsilon)p_K(S)\sum_Bw_B
=(2/\varepsilon)p_K(S).
\]

Thus the proof does not first enlarge the capacity and then absorb the
relaxation into a Lipschitz constant.

When a supplied block is refined, its parent weight cancels the normalization
of the child direction and the probability factors multiply exactly. Hence
coarse and refined tensorizations coincide, including zero-weight blocks.

## 7. Incompatible canonical partitions

The proof never forms the potentially huge common **coarsening** of two
canonical partitions. It takes their common **refinement** and uses coordinate
pinchings.

If `alpha,beta` are the two canonical partitions and `gamma=alpha meet beta`,
then with `delta=||K-L||_1` the three kernel moves satisfy

\[
\|K-K_0\|_1\le2\delta,\qquad
\|K_0-L_0\|_1\le\delta,\qquad
\|L_0-L\|_1\le2\delta.
\]

The three comparisons have supplied partitions `alpha,gamma,beta`, all with
blocks of size at most `r`. Exact refinement compatibility identifies each
intermediate supplied-partition representation with the single canonical
selector.

At a fixed supplied partition, the kernel estimate is weighted by the block
projector masses whose sum is one; the direction estimate uses trace-norm
contractivity of pinching. Hence no factor proportional to the number of
blocks appears.

This directly addresses the obstruction highlighted in the frozen task.

## 8. Attempted counterexample to a nearby, incorrect construction

A useful method check is that the ordinary local least-Euclidean-norm selector
is **not** refinement-compatible. For

\[
\varepsilon=1/5,\quad
K=\operatorname{diag}(3/10,3/5),\quad
P=\begin{pmatrix}1/5&2/5\\2/5&4/5\end{pmatrix},
\]

the least-norm point of the two-coordinate fiber and the tensorization of the
two singleton selectors are both feasible but have `l1` distance exactly
`9/25`.

This falsifies a tempting shortcut. It does not falsify `RESULT.md`, because
`RESULT.md` projects a target extension that is constructed to equal the
already prescribed refinement value on the entire disconnected locus.

## 9. Supplementary computational checks and their limits

Supplementary exact/numerical checks were used only as adversarial diagnostics.
They covered active capacities, zero-weight blocks, forced zero edges, complex
Hermitian block tensorization with nonzero cross-block direction entries, and
changed component partitions. They also reproduced one of the earlier random
verification runs.

These experiments do **not** implement the full compact-domain McShane
extension, do not verify all `r`, and are not formal verification. The proof of
the theorem is the mathematical induction in `RESULT.md`; the computation only
failed to find contradictions in selected finite tests.

## 10. Remaining risk and recommendation

No specific mathematical defect remains identified after this review. The most
sensitive parts are still:

1. the global Lipschitz lemma for Euclidean projection with fixed normals and
   moving right-hand side;
2. the total-unimodularity/pseudoinverse estimate used for the explicit
   constant;
3. the induction order that makes the whole disconnected locus jointly
   Lipschitz before extending to connected local kernels.

Those points were re-derived rather than accepted by assertion, and no gap was
found. Nevertheless, because authoring and adversarial review were done in the
same model session, the PR should remain draft until an independent human or
separate formal/domain review checks the proof line by line.

**Review outcome:** retain the mathematical classification `PROVED`; retain
`draft` repository status pending independent review.