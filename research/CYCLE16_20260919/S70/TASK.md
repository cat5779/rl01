# S70 — Contrast robustness at fixed rho=1/3
Use p=a/(1-c) to track a nonvanishing fraction of the legal bias interval. S63's proven seed is c=.95,p in[.42,.48]. Primary target: a rigorously certified parameter rectangle
rho=1/3, c in[.95,.96], p in[.42,.48],
or a clearly specified substantial subrectangle with c_upper>.95. This is an ambitious target, not an assumed true theorem. Do not silently replace it by pointwise existence of a neighborhood. State the certified width and whether it improves the accepted result at contrasts strictly above .95.

Construct a quantitative stability/continuation theorem for the entire PSD-score witness, including posterior Loewner bounds, guard caps, strict PSD slack, complete-data Fisher budget, test-function expectation and moving probabilities. The extension should be controlled analytically or by rigorous interval certificates, not justified by a generic continuity slogan. Since the original test is fixed at (rho,c,a)=(1/3,.95,.025), it may be held fixed as a variational function while the FULL probability law moves in c and p. Prove the multivariate evolution/derivative bounds rather than reusing a-only nilpotence without justification.

Transfers worth exploring include robust optimization with certified margins, implicit certificate continuation, and perturbation theory for conditional expectations. Reuse original finite data where legitimate; identify which margins are small and which can be redistributed. Permit redesigned witnesses if the original loses margin, but keep this lane on contrast extension, not filling the full a benchmark or changing density.

Report a reproducible continuum certificate and resulting uniform H_n''<=-eta n+B, or a sharply proved obstruction to the chosen witness plus a meaningful repaired contrast theorem. Legal endpoints move with c; keep p away from0,1 and a=(1-c)p. A finite-grid c-scan is not an interval theorem; improved behavior at a fixed a outside the legal domain is invalid.
