# Candidate ledger

The contract allowed at most three structurally different candidates and at
most two promotions.  The precise promoted statements were frozen in
`evidence/checkpoints/CP01_frozen_theorem.md` before proof.

## Candidate A — spectral defect plus lattice saddle point

- **Field/tool:** harmonic analysis on Johnson slices plus one-dimensional
  lattice Laplace asymptotics for a Fisher noncentral hypergeometric overlap.
- **Question:** is the finite potential mismatch extensive, and what is the
  sign/scale of its actual second response after the moving count weights are
  included?
- **Fast falsification test:** derive the exact all-`n` degree-two multiplier;
  if the layer gap were order one on central layers, the aggregate obstruction
  would be extensive.  It is instead order `1/n`.
- **Decision:** promoted.
- **Result:** exact `Delta_n=C log n+o(log n)` and a negative
  `sqrt(n)log n` midpoint curvature boundary layer with explicit Gaussian
  profile.
- **External theorem dependency:** none.  Uniform Stirling/Laplace expansion,
  the concentration bound, and the local limit estimate are proved in
  `proof.md` rather than cited as black boxes.

## Candidate B — positive heat-semigroup potential clock

- **Field/tool:** positive Markov semigroups and the Hausdorff-moment/Jensen
  constraint on Laplace-transform multipliers.
- **Question:** can one repair the potential-relevant mode by a valid positive
  law, and how large is the repair?
- **Fast falsification test:** prove `0<theta_l<1`; failure would make the
  proposed clock nonpositive or backward.
- **Decision:** promoted.
- **Result:** `tauhat_l=-log(theta_l)/gamma_(2,l)` defines a strictly positive
  normalized BL heat law that matches the potential exactly.  The clock change
  has bounded average duration and `O(log n)` entropy-value cost.
- **Precise negative result:** no positive random forward-time mixture from the
  same initial law can match both degree one and degree two on central growing
  layers, because `E X^r >= (E X)^r` while the actual `theta_l` lies below the
  mean-clock multiplier.
- **Boundary:** this does not rule out multi-generator, state-dependent, signed,
  non-Markov, or direct actual-path transports.

## Candidate C — direct actual-path Fourier-reference KL renormalization

- **Field/tool:** entropy/Fisher/acceleration decomposition after exposing the
  `n log n` cancellation.
- **Question:** can the actual or corrected `D_F''` be bounded with an explicit
  subextensive signed remainder?
- **Fast falsification test:** expand every derivative before estimating.  The
  terms `2 pi_l'D_l'`, `pi_l''D_l`, and conditional acceleration remain of
  uncontrolled sign; an `O(log n)` KL value estimate cannot be differentiated.
- **Decision:** not promoted in this round.
- **Reason retained:** after Candidate B, this is the live target-level
  obligation.  It was not converted into a conditional theorem or a
  tautological restatement.

## Rejected micro-candidates

- Inferring `Delta_n''` from `Delta_n>0`: rejected; Theorem 1 proves the opposite
  midpoint sign at leading order.
- A degree-two additive density correction without a positivity proof:
  rejected before promotion.
- Another finite `n=6,8` scan: rejected as non-substantive and unnecessary.
- Differentiating the `O(log n)` or `O(sqrt n log n)` entropy-value couplings:
  rejected as invalid.
