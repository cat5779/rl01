# Current-status audit

Checked: **2026-09-28**.

Classification: **VERIFIED_OPEN**.

Scope comparison:

- Lai, Shao, and Wang, “Cramér type moderate deviations for Studentized U-statistics,” *ESAIM: Probability and Statistics* 15 (2011), 168–179, DOI [10.1051/ps/2009014](https://doi.org/10.1051/ps/2009014), proves the two conclusions with the pointwise kernel condition. It is the theorem behind the ICM question, not a resolution after removing the condition.
- Shao and Zhou, “Cramér type moderate deviation theorems for self-normalized processes,” *Bernoulli* 22 (2016), 2029–2079, DOI [10.3150/15-BEJ719](https://doi.org/10.3150/15-BEJ719), retains domination-type control for the Studentized U-statistic application and explicitly remarks that weakening the condition is interesting and complete removal appears impossible. It supplies neither an unrestricted theorem nor a counterexample.
- Chang, Shao, and Zhou, “Cramér-type moderate deviations for Studentized two-sample U-statistics with applications,” *Annals of Statistics* 44 (2016), 1931–1956, DOI [10.1214/15-AOS1375](https://doi.org/10.1214/15-AOS1375), treats a two-sample framework under its own conditions, not the unrestricted one-sample kernel quantified here.
- Leung, Shao, and Zhang, “Another look at Stein's method for Studentized nonlinear statistics with an application to U-statistics,” arXiv:[2301.02098](https://arxiv.org/abs/2301.02098), and the 2023 nonuniform Berry--Esseen work concern different approximation errors. They do not prove either frozen moderate-deviation statement without kernel control.

Fresh searches covered the exact ICM wording, later Studentized U-statistic moderate-deviation and Berry--Esseen literature, author-linked papers, and forward citations. No complete resolution was located.

Processed-work exclusion:

- All visible open, closed, and merged PRs and published artifacts in `randomcat4/icm-conjecture-results` were checked. They include other numbered Shao problems, but no Open Question 5 proof, disproof, partial attempt, continuation, or review draft.
- The prior P1–P6 dispatch list does not contain this problem.
- The current `cat5779/rl01` main branch was searched before packaging; no Open Question 5 material was found.

The remaining obligation is exactly whether both conclusions survive with condition (3.15)/(D) deleted and no replacement assumption inserted.
