# SOL final review of Pro Tasks 01--02

**Review scope:** mathematical interfaces only.  The task prompts were not edited.  No global concavity claim is assessed here.

## Verdict

- **Task 01:** `ACCEPT_MATH`.  The S4 definitions, posterior normalization, `R_kappa` identity, and midpoint value `kappa=2` are correct.  The prompt already excludes merely naming or numerically evaluating the slack.  A fixed-`n` structural theorem is a legitimate finite-scope result, but it must not be reported as a dimension-uniform or extensive payment.
- **Task 02:** `ACCEPT_MATH`.  Displayed bound (2) is the reviewed one-sided Corollary G, not the absolute-error Theorem F.  Conditional Fisher convexity removes the single-site `B_* delta^(-4)m^(-1)/L` cost.  The added `B_g` definition is correct; the pair filtration must omit both pair sites, as the task now clarifies.

## 1. Task 01 algebra audit

### 1.1 Definitions and normalization

The full channel likelihood, atom law, posterior DPP kernel, covariance signs, and complete-channel Fisher budget agree with reviewed S4.  In particular,

\[
 \mathcal E=\mathbb E e_Y^TC_Ye_Y
 =\Psi-2\mathcal S,
 \qquad
 F=\mathcal D-\mathcal E.
\]

All expectations are under the actual output law.  The pair quantity `Gamma` must be read as

\[
 \Gamma_{ij}(Y_{-ij})=
 (A_{10}A_{01}-A_{00}A_{11})
 \sum_{(u,v)\in\{0,1\}^2}A_{uv}^{-1}.
\tag{1.1}
\]

With that four-cell summation convention, reviewed posterior rebasing gives

\[
 \Gamma_{ij}(Y_{-ij})
 =\mathbb E[e_{Y_i}e_{Y_j}|R^Y_{ij}|^2\mid Y_{-ij}],
\]

and therefore

\[
 \sum_{i<j}\mathbb E\Gamma_{ij}=\mathcal S.
\tag{1.2}
\]

The prompt's `sum_b 1/A_b` is mathematically correct if `b` ranges over all four cells, but writing `(u,v)` would remove a possible mistaken two-value interpretation.

### 1.2 Exact `R_kappa` identity

The acceleration payment is

\[
 A=2\sum_{i<j}\mathbb E\Lambda_{ij}.
\]

Hence the proposed slack is exactly

\[
 \mathcal R_\kappa
 =2\sum_{i<j}\mathbb E(\kappa\Gamma_{ij}-\Lambda_{ij})
 =2\kappa\mathcal S-A\ge0.
\tag{1.3}
\]

Using `Psi=mathcal E+2mathcal S`,

\[
\begin{aligned}
 \kappa\Psi-(\kappa-1)\mathcal E-\mathcal R_\kappa
 &=\kappa(\mathcal E+2\mathcal S)
   -(\kappa-1)\mathcal E-(2\kappa\mathcal S-A)\\
 &=A+\mathcal E=I''.
\end{aligned}
\tag{1.4}
\]

Thus equation (2) in Task 01 is an exact identity, not merely an upper bound, and contains no expectation-normalization error.

### 1.3 Midpoint constant

At `c=19/20`, `a=1/40`,

\[
 \tau_0=\tau_1={39\over1600},\qquad
 \theta=\log 1521.
\]

The three admissible candidates for `kappa` are

\[
 {400\over\sqrt{29679}}>2,
 \qquad {1521\over1520}\log1521>2,
 \qquad 2,
\]

where the last candidate is legal because `(19/20)^2=361/400<23/25`.  Therefore the minimum is exactly

\[
 \boxed{\kappa=2.}
\]

For the cyclic rank-`n/2` projection, fixed `|X|` and `e_0=e_1` imply

\[
 \mathcal E=e^2\mathbb E\operatorname{Var}(|X|\mid Y)=0.
\]

This statement is correctly restricted to the fixed-count cyclic projection.  It does not hold for the finite sine Toeplitz compression, whose input count is not fixed.

### 1.4 Scope and non-circularity

The prohibition against defining `L` through the target Hessian, `R_kappa` itself, or an unspecified nonnegative compensator successfully blocks the most direct circular answers.  The pair counterexample, midpoint tangent gate, and old two-bit theorem exclusion are also appropriate.

The success gate is adequate because it asks for a new explicit lower bound or posterior-average inequality, excludes renaming `R_kappa`, and requires a structural/geometric lemma if a growing-scale result is unavailable.  A fixed-`n` theorem may count at its stated finite scope; it must not be presented as `L_n>=eta n`, a nonshrinking parameter theorem, or a dimension-uniform payment without those additional proofs.  A single numerical positive slack remains only a diagnostic.  If the cyclic projection is chosen, the initial finite fixtures must use even `n`; `n=3` is available only for the Toeplitz option.

## 2. Task 02 interface audit

### 2.1 Exact S7 formulas and the stronger one-sided enclosure

The complete Hessian identity (1), the conditional two-site table, and the far-pair estimate agree with reviewed S7.  The local quantity `mathcal K_(R,L)` also matches the reviewed averaged-localization definition.

Theorem F gives an absolute comparison and contains the additional single-site term `B_* delta^(-4)m^(-1)/L`.  Task 02 deliberately uses the stronger one-sided Corollary G:

\[
\begin{aligned}
 {H_n''\over n}\le{}&\mathcal K_{R,L}+{C_*\over R}
 +{156(R-1)B_*\delta^{-4}m^{-2}\over L}\\
 &+{\delta^{-2}\over n}
 [4L+M\{8L(R-1)+R(R-1)\}].
\end{aligned}
\tag{2.1}
\]

This omission is valid.  For an interior site, if `u_i^B` conditions on the full outside word and `u_i^L` on the local window, then

\[
 \mathbb E[u_i^B\mid\mathcal F_L]=u_i^L.
\]

Since `f(u)=1/[u(1-u)]` is convex,

\[
 \mathbb E f(u_i^B)\ge\mathbb E f(u_i^L).
\]

The Hessian contains the negative term `-E f`, so replacing the full conditional Fisher payment by the local one creates no positive error in an upper bound.  Boundary sites and pair coarsening retain exactly the terms shown in (2.1).  Independent-audit item 4 accepts Corollary G in this strict-channel scope.  My earlier demand to restore `B_* delta^(-4)m^(-1)/L` was therefore incorrect and is withdrawn.

### 2.2 Reveal martingales

For nested sigma-fields `F_(t-1) subset F_t` that never reveal target site `i`,

\[
 u_t=\mathbb P(Y_i=1\mid F_t)
\]

is a bounded martingale.  With `f(u)=1/[u(1-u)]`, its Bregman remainder is exactly

\[
 B_f(x,y)=f(x)-f(y)-f'(y)(x-y)
 =(x-y)^2\left[{1\over xy^2}+{1\over(1-x)(1-y)^2}\right].
\tag{2.3}
\]

Consequently the stated telescoping expectation and `B_f>=16(x-y)^2` are correct.

For a pair `(i,j)`, the filtration must reveal neither `i` nor `j`.  Then the four-vector

\[
 P_t=(\mathbb P(Y_i=u,Y_j=v\mid F_t))_{u,v}
\]

is a simplex-valued martingale.  The exact pair telescoping requires the definition

\[
 B_g(P,Q)=g(P)-g(Q)-\nabla g(Q)\cdot(P-Q),
\tag{2.4}
\]

after which

\[
 \mathbb E g(P_T)-\mathbb E g(P_0)
 =\sum_t\mathbb E B_g(P_t,P_{t-1}).
\]

The task now defines `B_g` by (2.4) and clarifies that pair reveals skip both sites.  With that convention the reveal interface is exact.  Revealing one member would degenerate the four-cell table, so this convention should remain explicit in the dispatched text.

### 2.3 Task boundary

The task is well bounded.  It asks for one local compatibility or reveal-compensation result, accepts a precise counterexample, and explicitly excludes the already reviewed two-bit concavity theorem.  It also correctly warns that conditional DPP kernels do not average linearly under coarsening.

The prompt should continue to require a non-overcounting rule.  Without it, summing valid two-site payments can reuse the same one-site Fisher budget `O(R)` times and does not enter the near-field sum in (1).

## 3. Final recommendation

Task 01 is mathematically ready.  Its central identity (1.4) is exact and is a sound starting point for the ordinary-density posterior-slack search.  Finite-scope and scalable conclusions must remain distinctly labelled.

Task 02 is mathematically ready with Corollary G's one-sided upper enclosure.  The removed single-site error is an accepted Fisher-convexity gain, not an omission.  The explicit pair-filtration and Bregman conventions make the reveal interface auditable.
