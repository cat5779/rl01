# Exact three-input DPP flow consistency gap

STATUS: OPEN_DERIVATION_TASK. No proof has been accepted for the formulas below.

## Frozen question

Work on `E={1,2,3}`, fix `epsilon=2/5`, and let `0<eta<=1/10`. Put

\[
P=\frac13\mathbf1\mathbf1^{\mathsf T},\qquad
K_0=\frac12I+\frac{\eta}{21}
\begin{pmatrix}-11&13&-2\\13&-2&-11\\-2&-11&13\end{pmatrix}.
\]

For the cycle `sigma=(123)`, put `K_a=sigma^a K_0 sigma^{-a}`, `a=0,1,2`.

For each `a`, define the *full* positive birth-flow fiber `F_a` on the twelve upward Boolean-cube edges by

\[
f\ge0,\quad \operatorname{div}f=b_{K_a,P},\quad
\sum_e f_e=1,\quad
\sum_{i\notin S}f(S,i)\le5p_{K_a}(S).
\]

Here `p_K(S)=(-1)^{|S^c|} det(K-D_{S^c})`, `b_(K,P)=d/dh p_(K+hP)|_(h=0)`, and divergence is incoming minus outgoing.

Derive, or refute with an exact countercertificate, the following two formulas uniformly for every `0<eta<=1/10`:

\[
\inf_{f\in F_a,g\in F_b}\|f-g\|_1=\frac{48\eta}{21}
\quad(a\ne b),
\]

\[
\inf_{f_a\in F_a}\max_{a<b}\|f_a-f_b\|_1
=\frac{52\eta}{21}.
\]

The infima include arbitrary full-fiber flows, not only endpoint couplings, the explicit signed current, or a chosen optimizer.

## Required self-contained output

1. Prove the spectrum is `{1/2-eta,1/2,1/2+eta}`, and check commutation and the stated common gap.
2. Derive all exact atom probabilities and divergences.
3. Give explicit feasible attaining flows for both optima and verify all capacities throughout the eta interval.
4. Give exact lower-bound certificates: all-flow divergence duality for pairwise optimization, and a valid simultaneous/cyclic dual certificate for the triple.
5. Explain any use of symmetrization without presupposing equivariance of arbitrary choices.
6. Report `PROVED`, `DISPROVED`, or `INCOMPLETE`; no novelty or general-selector claim.

Exact-rational code may accompany the derivation, but numerical LP output or one eta value does not settle the interval.

## Why useful / boundary

If true, the factor `13/12` is an exact, selector-independent obstruction to gluing *pairwise optimal* choices into one optimal triple. It tests the finite-list geometry that the main FC question genuinely needs. It does not refute any universal FC constant; in particular this is a fixed-dimensional, fixed-projector family and the ratio does not diverge.

## Frozen source and handoff

The candidate formulas occur in [the unreviewed continuation, Section 4](https://github.com/cat5779/rl01/blob/b279b112c9bc4b25c7827dd7fb4ae9dc445ae214/research/dpp18/g16/CONTINUATION_02_UNREVIEWED.md). [The matching scope review](https://github.com/cat5779/rl01/blob/b279b112c9bc4b25c7827dd7fb4ae9dc445ae214/research/dpp18/g16/REVIEW02.md) does not certify these formulas. Reconstruct the derivation from the displayed matrices; do not inherit the candidate verdict.

Return the complete derivation as RESULT.md beside this task, with any exact computation and explicit certificate. Preserve this frozen task. A result requires a separate mathematical review before changing its status. The parent unrestricted problem remains [PR123](https://github.com/cat5779/rl01/pull/123).
