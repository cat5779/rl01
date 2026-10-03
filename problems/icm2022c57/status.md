# Current-status audit

Checked: **2026-09-28**.

Classification: **VERIFIED_OPEN**.

Direct evidence and adjacent results:

- Schwartz's ICM article, published by EMS Press in 2023 for ICM 2022, explicitly presents the assertion as Conjecture 5.7 and attributes it to numerical experiments with McBilliards.
- Schwartz, “Obtuse Triangular Billiards II: One Hundred Degrees Worth of Periodic Trajectories,” *Experimental Mathematics* 18 (2009), 137–171, DOI [10.1080/10586458.2009.10128891](https://doi.org/10.1080/10586458.2009.10128891), gives finite analytic descriptions and rigorous analysis of many particular tiles, while explicitly saying that general connectedness and simple connectedness were unproved.
- Alex Becker, “Periodic Billiards in Isosceles Triangles,” arXiv:[1306.6702](https://arxiv.org/abs/1306.6702), and “On the Local Theory of Billiards in Polygons,” arXiv:[1405.1150](https://arxiv.org/abs/1405.1150), establish openness/affine-line alternatives, symmetry, stability, and piecewise-analytic boundary information in special settings. They do not determine the topology of every stable orbit tile.

The fresh audit checked the exact conjecture phrase and number, Schwartz's maintained publication page, later triangular-billiards searches, forward citations of DOI 10.4171/ICM2022/66, and errata/update paths. No post-ICM source claiming a proof or counterexample was found, and no later result located subsumes both topological conclusions for every stable word.

Processed-work exclusion:

- All visible open, closed, and merged PRs and published artifacts in `randomcat4/icm-conjecture-results` were checked. PR material on Schwartz Conjecture 5.10 concerns finite covers of acute-triangle parameter space, not orbit-tile connectedness or simple connectedness.
- The prior P1–P6 dispatch included another Schwartz item, not Conjecture 5.7.
- The current `cat5779/rl01` main branch was searched before packaging; no Conjecture 5.7 attempt or package was found.

The exact remaining obligation is global in the word: special families, finite searches, and plots of bounded word length do not decide it.
