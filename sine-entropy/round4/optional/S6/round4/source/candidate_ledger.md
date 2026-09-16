# Candidate ledger

The initial frozen ledger is in
`evidence/frozen/candidate_ledger_initial.md`.  Exactly three structurally
separate mechanisms were scouted and two were promoted.

## C1 — correlated true-block reference plus strong-Rayleigh concentration

**Status:** promoted and proved.

**Frozen test.**  The full information content `-log p(S)` had to be Hamming
Lipschitz with a constant independent of dimension on a fixed spectral strip;
the DPP law then had to meet every hypothesis of a primary-source concentration
theorem.  Failure of either point would have rejected the candidate quickly.

**Outcome.**  The L-ensemble Schur-complement ratio gives the exact Lipschitz
constant `Lambda_delta`.  The L-ensemble generating polynomial is proved stable
directly.  Pemantle--Peres Theorem 3.2 then yields a dimension-linear MGF bound.
Applied separately to `log p` and the true block-reference `log w`, it controls
the exact positive real-q Hölder remainder and a signed Jensen defect.

**Scope.**  Fixed interior spectral strip, real `q` in `[1/2,3/2]`, disjoint true
blocks, and all multiples `n` of `R`.  The theorem does not sign the block
entropy curvature.

## C2 — full-atom Chebyshev series plus interior Bernstein response

**Status:** promoted and proved.

**Frozen test.**  Recheck the prior author-claimed full-atom expansion and its
moving-law degree cancellation.  Then replace the whole-interval Markov cost by
an interior Bernstein cost and test whether the reviewed `1/50` curvature margin
survives at any fixed `c>37/40` uniformly in dimension.

**Outcome.**  The expansion was re-established.  The nested-interval response
bound is `O(M^2 epsilon + tail)` rather than `O(M^4 epsilon + tail)`.  Combined
with an exact contrast coupling and particle-hole complementation, rational
constants certify a fixed band of width `10^(-13)` and curvature `-n/200` for
every finite contraction on a centered strip.

**Scope.**  The contrast band is nonempty but extremely narrow, and the proof is
not uniform at the legal `a` endpoints.

## C3 — abstract polymer/connected-cluster expansion

**Status:** scouted and rejected before proof attempt.

**Primary source checked.**  Bissacot--Fernandez--Procacci,
arXiv:1002.3261, on convergence criteria for abstract/subset polymer gases.

**Fastest falsification test.**  Identify a polymer activity for the real-q
principal-minor pressure and verify a dimension-uniform summability criterion at
fixed high contrast.  No such verified activity estimate emerged.  The
algebraic decay of sine-kernel pair correlations is not a bound on all connected
configuration interactions.

**Conclusion.**  No cluster theorem is imported, and no impossibility claim is
made.  A different polymerization with cancellation or a resolvent small
parameter remains live.
