# Invariant weak superposition for a prescribed DPP birth equation

## Frozen target W

Let \(\Gamma\) be any countable discrete group acting regularly on itself. Fix equivariant complex Hermitian operators \(C,H\) with \(H\ge0\) and

\[
\varepsilon I\le K_t=C+tH\le(1-\varepsilon)I,
\qquad 0\le t\le1.
\]

Write \(\mu_t\) for the DPP of \(K_t\). Suppose finite-valued nonnegative Borel functions

\[
a_i:[0,1]\times\{0,1\}^{\Gamma}\longrightarrow[0,\infty),
\qquad i\in\Gamma,
\]

satisfy:

1. \(a_i(t,x)=0\) when \(x_i=1\), and

   \[
   a_{gi}(t,gx)=a_i(t,x)
   \]

   for every \(g,i,t,x\).
2. The mean local activity is integrable in time. In the intended DPP construction one has the exact identity

   \[
   \int a_i(t,x)\,d\mu_t(x)=\tau(H)
   \tag{A}
   \]

   for every \(i,t\).
3. For every bounded cylinder function \(f\),

   \[
   \mu_t(f)-\mu_0(f)
   =\int_0^t\int L_sf(x)\,d\mu_s(x)\,ds,
   \tag{CE}
   \]

   where

   \[
   L_sf(x)=\sum_{i\in\Gamma}a_i(s,x)
   \bigl[f(x\cup\{i\})-f(x)\bigr].
   \]

Prove or disprove the following statement:

> For every rate field satisfying the conditions above, there exists a \(\Gamma\)-invariant probability law on coordinatewise càdlàg pure-birth paths \((X_t)_{0\le t\le1}\), with \(X_0\sim\mu_0\) and \(X_t\sim\mu_t\) for every \(t\), such that for every bounded cylinder \(f\),
> \[
> f(X_t)-f(X_0)-\int_0^tL_sf(X_{s-})\,ds
> \]
> is a martingale in the natural path filtration.

Every coordinate jumps at most once. Establish local integrability, coordinatewise càdlàg paths, and the absence or harmlessness of simultaneous jumps at the level actually needed for the martingale problem.

## Exact scope

This task is only weak existence with the prescribed generator and invariant path law. Do **not** attempt to prove a representation by independent sitewise Poisson random measures, pathwise uniqueness, a strong solution, a factor of iid, all-input equivariance, or convergence of finite-range approximations on a common noise. None of those properties may be inserted as a hidden hypothesis or used as though it followed from W.

The group is not assumed amenable or sofic. The rates are not assumed finite range, continuous in the configuration, uniformly bounded, or quasilocal. A compact convex set of weak solutions need not have an invariant point for a nonamenable action; therefore an averaging argument is invalid unless an actual fixed-point hypothesis is proved.

## Available DPP input

The rate fields motivating W can be constructed exactly. Writing \(T=H^{1/2}\), \(v_g=T\delta_g\), and \(H=\sum_gv_gv_g^*\) strongly, a Borel one-point monotone coupling on each rank-one line yields covariant rates

\[
a_i(t,x)=h^{-1}\sum_gq_{t,g}(x,i)
\]

with (A) and (CE). This supplies a rate field but not a martingale solution. The one-point coupling is the standard consequence of Lyons, *Determinantal Probability Measures* (2003), Proposition 10.3, together with support-minimal dilation. Do not present this rate construction as a proof of W.

## Suggested proof route and obligations

A potentially useful state-space metric is

\[
d(x,y)=\sum_{m\ge1}w_m|x_{i_m}-y_{i_m}|,
\qquad w_m>0,\quad\sum_mw_m=1,
\]

for an enumeration of \(\Gamma\). Invariance and (A) make the expected weighted jump action finite. If invoking a superposition principle for nonlocal continuity equations or a martingale-problem existence theorem on a Polish space, quote a primary theorem and verify every hypothesis: the precise test-function class, Borel jump kernel, local versus total activity, tightness, time measurability, correct marginals, and càdlàg realization.

Most importantly, prove why the resulting path law is \(\Gamma\)-invariant without assuming amenability. A construction is acceptable if it is functorial/canonical enough that covariance of \(a\) and invariance of \(\mu_t\) force invariance; this property must be proved, not asserted. If using finite-dimensional conditional rates, prove projective consistency or another mechanism that survives the non-invariant choice of finite sets.

A disproof must retain all frozen conditions: a uniformly gapped linear DPP path \(C+tH\), a finite-valued covariant Borel rate field, the exact cylinder continuity equation, and integrable mean local activity. General examples of group actions on compact convex sets without fixed points do not suffice unless encoded into such a DPP rate field and shown to forbid every invariant martingale solution.

## Output standard

Return exactly one of `PROVED`, `DISPROVED`, or `INCOMPLETE`, followed by a complete argument. A restricted theorem must be clearly separated and its added hypotheses listed. Distinguish ordinary weak existence from invariant weak existence, and distinguish both from independent-noise or factor representations. Cite all external theorems at theorem level and check their hypotheses explicitly.
