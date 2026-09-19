# S63 verified scoped theorem — independent PR47

Independent full recomputation accepts the actual sine Toeplitz complete-configuration theorem at rho=1/3,c=19/20,a in [.021,.024]: H_n_second <= -n/25+399 for every n>=22, yielding true entropy-rate Jensen gap >=lambda(1-lambda)(a1-a0)^2/50. This is a fixed-density strict subinterval theorem beyond the accepted universal c<=37/40 baseline. It is not all[.02,.03], all legal a, all rho or all c.

Evidence:138828 arithmetic checks;60 global cells;1536 guard cells; all4194304 true-law atoms; regenerated moving-weight coefficients; exact rational alpha/PSD/Bernstein/tail closure. The coordinator inspected actual recomputation logs. All source and review copies remain distinct from reviewer-generated outputs. No hash gates.

Correction to the reviewer's initial repair claim: original eps=ua(max(e0,e1),ew) already adds diagonal and off-diagonal error upward. It bounds the maximum absolute row sum of the symmetric2x2 error, hence its operator norm. Original C +/- eps I is safe. Doubling eps is optional conservative stress testing, not a required repair. Original1536 cells passed66610050 boxes; doubled bound passed66614920 boxes. Main coordinator caught the erroneous repair diagnosis and requested its withdrawal in the same independent PR47. No original author file has been modified.

The finite upper bound only forces strict negative finite-volume curvature for n>=9976; the entropy-rate strict concavity follows without assuming differentiability of the limiting entropy rate. External novelty remains unaudited.

Next priority may now be extending this SAME verified PSD-score-martingale witness mechanism to more of the c=.95 benchmark, after a distinct task definition and global cap check. No new web task is sent by this receipt. S68 remains under separate full-package review.
