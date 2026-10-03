# Current-status audit

Checked: **2026-09-28**.

Classification: **VERIFIED_OPEN**.

Scope comparison:

- Jing, Shao, and Zhou, “Saddlepoint approximation for Student's t-statistic with no moment conditions,” *Annals of Statistics* 32 (2004), 2679–2711, DOI [10.1214/009053604000000742](https://doi.org/10.1214/009053604000000742), proves the fixed-\(x\) expansion under the Fourier-integrability condition used in ICM equation (3.3). It does not answer the question after that condition is removed.
- Zhou and Jing, “Tail probability approximations for Student's t-statistics,” *Probability Theory and Related Fields* 136 (2006), 541–559, DOI [10.1007/s00440-005-0494-8](https://doi.org/10.1007/s00440-005-0494-8), removes that condition for a strongly nonlattice vector \((X,X^2)\). Its Section 4 leaves the lattice extension open, and it does not prove the shrinking-\(x\) uniform assertion.
- Konstantin Borovkov, “On large deviation probabilities for self-normalized sums of random variables,” arXiv:[2501.12480](https://arxiv.org/abs/2501.12480) (2025), proves exact leading large-deviation equivalents in specified nondegenerate settings. It does not contain the displayed \(1/w-1/v\) correction with the required remainder and does not establish the requested uniform range for all admissible laws.

Fresh searches covered the exact ICM label and formula, later saddlepoint and self-normalized large-deviation papers, author/survey records, and forward citations. No paper located proves both frozen assertions or gives a valid counterexample satisfying the frozen hypotheses.

Processed-work exclusion:

- Every open, closed, and merged PR visible in `randomcat4/icm-conjecture-results` was checked. Shao Conjectures 1 and 2 and Open Question 4 have material there; Open Question 3 does not.
- The previously dispatched P1–P6 identifiers were checked; this problem was not among them.
- The current `cat5779/rl01` main branch was searched before opening this package; no prior Open Question 3 package or attempt was found.

The exact remaining obligation is the two-part statement in `problem.md`, including lattice and weakly nonlattice laws and the uniform shrinking-endpoint range.
