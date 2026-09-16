# Delta from the latest local S6 round

## Public reviewed baseline

The Round 4 public packet at commit
`c307fe1bcf46b56e4755655c90f60a681979bf13` independently accepts the earlier
S6 obstruction to unrestricted Berezin/Jensen and the extensive value gap of
the optimized one-site product tangent.  It does **not** list the immediately
preceding local Round 3 package among the reviewed results.

## Latest local result and review status

The latest package in this conversation, labelled `PROVED_SCOPED_LEMMA`, claimed:

1. an exact configuration-dependent pencil
   `A_S(a)=aI+cQ-diag(1_(S^c))` and a dimension-free Chebyshev expansion of the
   normalized measured entropy with coefficient degree at most `2m` and norm at
   most `r^m/m`;
2. a whole-interval Markov response estimate giving `C^2` convergence and
   `O(log^6 R/R)` curvature control for disjoint-block and finite-memory KL
   remainders on fixed interior strips;
3. a strict-concavity corollary only at extremely small fixed density or
   co-density; and
4. exact real-q bookkeeping only at the derivative `q=1`.

That package was self-checked, but no independent audit of it is included in the
Round 4 public handoff.  It is therefore treated here as an **author claim**, not
as an imported reviewed theorem.  The load-bearing full-atom expansion is
re-stated and proved again in `proof.md`, Sections 2--3.  The previous claimed
KL-curvature theorem is not used as a premise.

## Obstruction resolved in the latest local result

The product reference omitted an order-`n` dependence term.  The local Round 3
claim replaced it by references made from true spatial blocks and supplied a
candidate route to derivative control.  Its remaining sign corollary did not
cover fixed positive density at high contrast, and it did not control a genuine
open interval of real `q`.

## Genuinely unpaid estimates selected for this round

Two unpaid estimates were frozen before final proof/certification:

* transport the reviewed `c=37/40` curvature margin into a **strictly
  high-contrast, all-density, dimension-uniform** region by sharpening the
  full-atom response estimate on nested intervals; and
* control the exact positive correlated-reference remainder for **real q on an
  open neighborhood of one**, including a signed finite Jensen defect, rather
  than only its derivative at `q=1`.

## New delta proved in this package

* For every finite Hermitian contraction, not only the sine blocks, the full
  measured entropy has curvature at most `-n/200` for
  `37/40 <= c <= 37/40+10^(-13)` on a fixed centered `a` interval of length
  `1/100`.  This gives a new all-density high-contrast sine-rate theorem on that
  strip.
* For true disjoint `R`-block references and every `1/2<=q<=3/2`, the exact
  real-q Hölder/Renyi remainder per site and its signed Jensen defect are bounded
  by
  `c Tr b(Q_R)/R + 2880 Lambda_delta^2 |q-1|`.

These are not reformulations of the preceding Round 3 claims.
