# Frozen theorem v2: inverse-root adjacent-layer regularity

**Status: CANDIDATE / NOT PROVED.**  Version 1 remains unchanged as the record
of the dimension-free attempt; current larger-size evidence disfavors it.

Use the corrected SA04 objects and original clocks.  Let `n=2k`, and for
`3<=l<=k` put `d_l=A_l-E_l` exactly as in the reviewed report.

## Intended central-window claim

There are constants `K<infinity` and `n_0` such that, for every even
`n>=n_0` and every layer in the expanded window

\[
k-\left\lceil\sqrt{(n-2)\log n/2}\right\rceil\le l\le k,
\]

one has

\[
|d_l|\le {K\over\sqrt n}.
\]

Together with the already proved weight tail bound, this implies `W_n=O(n)`.
It does not determine the sign of `W_n`.

## Optional sharper central claim

At the single central layer, seek a nonzero limit or two-sided bounds for
`sqrt(n)d_k`.  The finite data currently support positivity but do not yet
stabilize a leading constant, so no numerical value is frozen here.

## Success standard

A proof must preserve the original layer clocks and separately expose the
cancellation between same-clock deletion and the finite-exchange bridge.  A
single-layer estimate is insufficient for the `W_n=O(n)` conclusion; the
expanded window and its uniform constants are part of the theorem.

Finite MCMC diagnostics may select the local profile but cannot discharge the
uniform quantifiers.
