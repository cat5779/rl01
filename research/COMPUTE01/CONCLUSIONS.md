# COMPUTE01 conclusions

This file states what the computations actually decide.  Certificates and
regression details live in the companion notes; they are evidence for these
conclusions, not the conclusions themselves.

## 1. SA05: the finite n=8 gap is neither concave nor convex

For `c=19/20`, let `E_8(a)` be the corrected-minus-true entropy gap defined in
the SA05 handoff on the legal interval `0<a<1/20`.

The certified signs

\[
E_8''(1/200)<0,\qquad E_8''(1/50)>0
\]

have an immediate finite-dimensional consequence:

> **Conclusion SA05.** `E_8(a)` is neither concave nor convex on `(0,1/20)`.

Moreover `E_8''(1/40)>0`, so the symmetric midpoint is locally convex, not
locally concave.  Thus any proposed proof based on a fixed curvature sign,
including a midpoint-concavity heuristic, is false already at `n=8`.

This conclusion is rigorous for `n=8`.  It does not decide the sign of an
entropy-rate limit or the behavior at growing `n`.

## 2. SA04: the finite data favor a non-vanishing central difference

For every tested even `n=6,8,...,20`, the corrected law has

\[
d_k=A_k-E_k=h(k)-h(k-1)>0,
\]

and the observed `d_k` rises from `0.15635` to `0.60852`.  Consequently
`sqrt(n)d_k` rises from `0.38299` to `2.72140`; it does not stabilize or decay
on this range.  At `n=20`,

\[
A_k=0.63965609,\qquad E_k=0.03113159,
\]

so the clock-bridge cost is only about `4.9%` of the deletion loss.  The
strong-cancellation candidate is therefore not the mechanism visible in the
data.

The complete weighted response is negative at every tested size and reaches

\[
W_{20}=-150.68278144.
\]

The ratio `W_n/n^(3/2)` moves from `-0.2591` at `n=6` to `-1.6847` at `n=20`.
Together with the report's proved `O(n^(3/2))` upper bound, the most useful
working conjecture is:

> **Conjecture selected by C02.** The central difference has a nonzero positive
> limit (or at least a positive central-subsequence lower bound), and `W_n` is
> eventually negative of order `n^(3/2)`.

This replaces the previous undirected three-way choice with one concrete
analytic target.  The next useful theorem is a positive lower bound for
`d_k` or a limiting central profile, followed by a local limit calculation for
the positive `w_l` weights.

The SA04 statements in this section are a finite binary64 conclusion and an
asymptotic conjecture, respectively.  They do not yet disprove a hypothetical
eventual `O(n^(-1/2))` bound, because finitely many sizes cannot do that.

## 3. What c=19/20 is doing

The value is not arithmetically mysterious.  It gives

\[
p=(1+c)/2=39/40,\qquad q=(1-c)/2=1/40,
\qquad z=(p/q)^2=1521.
\]

It is a high-correlation interior stress point: close enough to the degenerate
boundary to expose curvature and cancellation failures, but with all relevant
probabilities still positive and all entropy derivatives well-defined.  That
is why several tasks focus on `19/20`.

