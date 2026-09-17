# Problem

For the corrected SA04 law at `c=19/20`, decide whether the central increment

\[
d_k=h(k)-h(k-1)=A_k-E_k,\qquad n=2k,
\]

has a positive dimension-free lower bound for all sufficiently large `k`.
If so, determine whether the positive `w_l` weights force an eventually
negative `n^(3/2)` contribution to `W_n`.

The same-clock deletion loss has now been proved not to vanish.  Larger-size
diagnostics disfavor the original dimension-free claim for `d_k` and instead
support cancellation to inverse-root order.  The active problem is therefore
the version-2 window theorem in `frozen_theorem_v2.md`, which would improve the
existing global response bound from `O(n^(3/2))` to `O(n)`.
