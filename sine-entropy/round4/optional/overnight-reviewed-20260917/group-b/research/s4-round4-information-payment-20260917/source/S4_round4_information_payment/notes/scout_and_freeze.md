# Candidate scout and frozen proof attempts

UTC checkpoint supplied separately by the logging script.

The round-3 MMSE theorem is an author theorem in this conversation, not a reviewed premise in commit c307fe1bcf46b56e4755655c90f60a681979bf13. It gives J_T'' <= (5/4)delta^-5 integral MMSE and only an extremely dilute interior sine region. No credit will be taken for restating it.

## Three scouts (no additional mechanisms)

A. Gaussian localization + unnormalized second likelihood response. Aim to improve the all-field local bound Q_pi'' <= const delta^-5 E Varpost to order delta^-2 by reorganizing the pair term. Fast tests: four-site midpoint; skew rank-one; contiguous P_6,2 and P_6,3. Obstacle: previously discarded positive covariance-column terms and pair-to-full inverse likelihood powers. NOT promoted yet; no theorem asserted.

B. Gaussian completion + generalized extrinsic-information / GEXIT identity. Keep the complete channel score (Louis missing-information identity, to be derived rather than cited), and bound the nonnegative log-odds acceleration using an averaged compatible posterior covariance. This could pay information curvature directly, without integrating the very costly pointwise Q'' estimate. Adjacent-field source: Measson--Montanari--Richardson--Urbanke, Generalized Area Theorem, plus GSV vector I-MMSE. Fast tests same as A, plus generic non-DPP laws. PROMOTED #1.

Frozen B1 claim to attempt: there exists an explicit channel-only C(a,c) growing at most O(delta^-2 log(1/delta)) on compact high-contrast proportional-offset intervals, such that for every finite Hermitian-contraction DPP,
  I(X;Y_a)'' <= C(a,c) E Tr Cov(X|Y_a),
and for every deterministic Gaussian time T,
  I(Y_a;Z_[0,T])'' <= C(a,c) E Tr Cov(X|Y_a).
The proof must retain A=-sum p'' log p and the actual output Fisher. It must yield a density region beyond the previous delta^5 entropy criterion, with no claim for all homogeneous laws. The intended separately estimable budget is the complete channel Fisher -(n-TrK)b''(a)-TrK b''(a+c), not the desired Hessian in disguise. Constants and improved subclaims must be frozen before proof, and failed versions preserved.

C. Spatial block/reveal localization. Reveal separating sites or use block Gaussian observations to isolate true Fourier interfaces. Variance tails can be bounded by Hilbert-Schmidt cross-boundary correlations, but no signed information-curvature bound with an o(n) error is in hand. NOT promoted. A value-only interface bound does not count as curvature progress.

Main target and all quantifiers remain those in mandatory TARGET.md.
