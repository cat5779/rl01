# R18 G16 external result audit

Date: 2026-10-03 (Asia/Singapore)

Source: `randomcat4/dpp-entropy-tools#148`, head
`0aeb7e68c574d9b8f3dcf386d7d912aff2dc26db`.

## Verdict

`OPEN / INCOMPLETE`.

The certified proof ledger in the PR is an accurate consolidation of earlier
audited results.  It does not prove or disprove global finite consistency for
arbitrary commuting inputs with varying delocalized projectors.

The later 1038-line `CONTINUATION_02_UNREVIEWED.md` is explicitly a candidate
packet.  The present audit promotes only its Section 1 fixed-projector repair
lemma; every other new section remains outside the certified ledger.  In
particular:

- the fixed-projector full-fiber repair is correct, but the one-half-Hoelder
  selector remains a candidate and neither is an exponent-one
  varying-projector theorem;
- the bounded-component candidate is now independently supplied by the more
  complete G17 proof, but still has a constant depending on the fixed bound;
- the proposed three-input factor `13/12`, even if its exact arithmetic is
  confirmed, only shows that pairwise optima need not glue exactly.  A fixed
  factor cannot disprove existence of some universal Lipschitz constant;
- the affine-rule and electrical-current examples rule out particular
  construction principles, not every nonlinear selector;
- Section 7 lacks the explicit finite-dimensional formulas and is not
  self-contained enough to certify.

Thus this is the unfinished one in the strongest sense: it preserves the exact
breakpoint and promising subclaims, but returns neither `PROVED` nor
`DISPROVED` for its assigned theorem.

## Certified sublemma from continuation Section 1

For a fixed rank-one projector `P`, if `K` and `L` commute with `P`, then every
flow in the full positive fiber `F(K,P)` can be repaired to a flow in
`F(L,P)` with

`||f-g||_1 <= (4/epsilon)||K-L||_1`.

The background repair is valid: the residual positive fermionic state has
mass `1-c_B`, its upward coupling contributes exactly the residual divergence,
and the atom-mixture identity supplies the outgoing-capacity bound.  For the
marked eigenvalue repair, the two scalar inequalities defining `c_lambda`
are precisely the coefficientwise conditions after writing the atom law as
`(1-lambda) alpha + lambda beta`.  The bound
`1-c_lambda <= 2|lambda-nu|/epsilon` covers both active ratios and all endpoint
cases.  Combining the two stages gives the displayed constant four.  Reversing
the roles of `K,L` gives the corresponding Hausdorff estimate.

This sublemma is pairwise and fixes `P`; by itself it gives neither a coherent
global selector nor control when the projector varies.
