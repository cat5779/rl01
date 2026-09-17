# Source ledger

## Mandatory pinned sources

New assignment:

- commit `e78392fc440d81abaad0f3728c5b23505d038ee6`
- path `sine-entropy/round4/overnight-20260917/check1/S13.md`

Reviewed baseline and strengthened contract:

- commit `9032d04fbde2ae97ba9de2702ddcd07aa3923e89`
- `sine-entropy/round4/TARGET.md`
- `sine-entropy/round4/KNOWN_RESULTS.md`
- `sine-entropy/round4/PITFALLS.md`
- `sine-entropy/round4/READING_MAP.md`
- `sine-entropy/round4/REVIEW_SCOPE.md`
- `sine-entropy/round4/overnight-20260917/CONTRACT.md`

These sources establish the problem definition, open status, reviewed inputs,
and mandatory derivative bookkeeping. No unreviewed round-two asymptotic claim
is imported as a premise for the new theorem.

## Modified log-Sobolev provenance

The slice inequality reconstructed in Section 6 agrees with Proposition 4.7 of:

S. G. Bobkov and P. Tetali, *Modified Logarithmic Sobolev Inequalities in
Discrete Settings*, Journal of Theoretical Probability 19 (2006), 289–336.

The package includes a self-contained induction with the generator normalization
used in this project, so the theorem does not rest on an uncopied black-box
constant.

## Reviewer status supplied by the user

The fresh reviewer checked only:

- the exact theta variance/coefficient formulas;
- the coefficientwise proof `0<theta<1`;
- positivity/normalization of the BL potential clock;
- layerwise matching of the one Fourier pair-potential expectation.

It did not certify the new saddle estimate, the extensive entropy-production
bound, earlier cusp/local-limit claims, entropy comparison bounds, the package,
or the target.
