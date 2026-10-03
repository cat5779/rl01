# Invariant superposition for a determinantal birth equation

## Frozen primary target W

Fix a countable discrete group Gamma acting regularly on itself. Let C,H be fixed equivariant complex Hermitian operators with H>=0 and

\[
\epsilon I\le K_t=C+tH\le(1-\epsilon)I\qquad(0\le t\le1).
\]

Write mu_t for the DPP of K_t. Suppose finite-valued nonnegative Borel functions a_i(t,x), i in Gamma, on [0,1] x {0,1}^Gamma satisfy all the following:

1. a_i(t,x)=0 when x_i=1, and a_(gi)(t,gx)=a_i(t,x) for every input and g,i.
2. For each i, the mean activity is integrable in time; one may assume the exact bound integral a_i(t,x) dmu_t(x)=tau(H) for every t.
3. For every bounded cylinder function f,

\[
\mu_t(f)-\mu_0(f)=\int_0^t\int L_s f(x)\,d\mu_s(x)\,ds,
\qquad
L_s f(x)=\sum_i a_i(s,x)[f(x\cup\{i\})-f(x)].
\tag{CE}
\]

Prove or disprove: **for every such rate field**, there exists a Gamma-invariant probability law on coordinatewise cadlag pure-birth paths (X_t)_(0<=t<=1), starting with mu_0, with X_t~mu_t for every t, such that for every bounded cylinder f,

\[
f(X_t)-f(X_0)-\int_0^t L_s f(X_{s-})\,ds
\]

is a martingale in the natural path filtration. This asks for a weak process with its prescribed generator, not yet a factor of a prescribed iid input. Every coordinate jumps at most once; establish the needed simultaneous-jump and integrability assertions instead of assuming them.

The group is not assumed amenable or sofic; the rates are not assumed continuous, finite range, or uniformly bounded in the configuration. Do not insert these assumptions into the conclusion. A restricted theorem is useful only when separately labeled. A disproof of W must retain the linear, uniformly gapped determinantal marginal path and all displayed conditions, not replace it by unrelated marginals.

## Why these hypotheses arise

The following positive-flow construction may be used as an input. Set T=H^(1/2), v_g=T delta_g and H=sum_g v_g v_g* strongly. For v_e nonzero choose h=epsilon/(2||v_e||^2). Rank-one DPP coupling supplies a Borel kernel P_(t,e)(x,dy) from mu_t to mu_(K_t+h v_e v_e*) adding at most one point; all P_(t,g) are translates of this same root disintegration. If q_(t,g)(x,i) is the conditional probability of adding i, then

\[
a_i(t,x)=h^{-1}\sum_g q_{t,g}(x,i)
\]

has mean tau(H) and satisfies (CE). Indeed DPP cylinder probabilities are affine on each rank-one line, and the probability of adding i has mean h|v_g(i)|^2. Infinite values occur only on null sections under mu_t and may be set to zero covariantly without changing (CE). The at-most-one-point coupling is the standard consequence of Lyons 2003 Proposition 10.3 and support-minimal dilation, https://numdam.org/item/10.1007/s10240-003-0016-0.pdf . The zero-increment case is deterministic.

This input establishes a rate field and a continuity equation. Its existence is not a martingale-problem existence theorem. In particular, a compact set of candidate path laws stable under a nonamenable group action need not have an invariant element. Verify hypotheses of any superposition, Markov-selection, Poisson representation or uniqueness theorem you invoke, using primary references.

## Separate extraction interface S

If W can be established, determine what is additionally needed for a strong relative factor. In particular prove or refute this **conditional interface**, without treating its hypotheses as proved for the above selected rates:

Assume there is an invariant compatible weak solution jointly with X_0 and independent sitewise unit-rate Poisson random measures N_i, independent of X_0, satisfying

\[
X_i(t)=X_i(0)+\int_{(0,t]\times[0,\infty)}
\mathbf1_{\{u\le a_i(s,X_{s-})\}}N_i(ds,du).
\]

The joint noise is a product Poisson field, not merely a collection of coordinate processes with the correct compensators. Assume also that some L in L^1[0,1] satisfies, for every jointly Gamma-invariant pair (U,V) with both marginals mu_t,

\[
\mathbb E|a_e(t,U)-a_e(t,V)|
\le L(t)\mathbb P(U_e\ne V_e)
\tag{AL}
\]

for almost every t. Does this yield a total Borel, all-input equivariant relative map of (X_0,independent regular iid labels) to the path, with the correct marginals? A null exceptional input may return the constant initial path.

The intended route is conditional independent copies over the entire driving noise, pathwise uniqueness, and a Dirac conditional law. Prove the temporal compatibility needed for the copies to remain solutions in the enlarged filtration; conditioning on the full future noise must not silently invalidate compensation. Separately prove the all-input equivariant version. If this is an application of an existing theorem, state that accurately. The main research target remains W; a conditional extraction theorem alone is not general ordered-factor existence.

## Known failed shortcuts

Within-approximation oscillation control does not give a cross-approximation rate bound. On one site take independent Bernoulli(1/4) initial state, common Poisson input, and lambda_n(t)=2 times the indicator that fractional_part(2^n t)<1/2. The rates lambda_n(t)(1−x) have uniform sensitivity and uniformly convergent, uniformly gapped DPP marginals; their integrated forward equations converge. Nevertheless the endpoint mismatch between any distinct n,m is (3/2)(exp(−1)−exp(−3/2))>0. Thus no same-input convergent subsequence follows from that information. Different covariant rates may even generate exactly the same finite DPP marginal path. Do not reuse either shortcut.

Return PROVED, DISPROVED or INCOMPLETE separately for W and S, with complete arguments and exact remaining hypotheses. Keep weak existence, invariant weak existence, joint independent-noise representation, pathwise uniqueness, and strong factor realization as distinct conclusions.
