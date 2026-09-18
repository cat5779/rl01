S51 c -> 1: actual-law V14 renormalization and averaged cancellation

Main result: S51_C1_RENORMALIZED_V14.md
Checks: S51_C1_checks.py
Actual run output: S51_C1_check_results.json
Existing author interface: DEPENDENCY_S51_CYCLE06_RESULT.md

The new proof uses the existing S51 bridge only on compact subsets of x<1.
No endpoint-uniform theorem is borrowed from that interface. No independent
certification is claimed. The complete readable core is also returned in chat.

PROVED: exact projection Ward identities with finite Toeplitz leakage;
actual-law logit entropy derivative bridge; conditional cross-ratio measure
and exact mass; complete V14 averaged renormalization; logarithmic endpoint
bound and compensated distributional compactness; sine spectral prediction
bound; noncommutation of finite-window and noiseless limits.

INCOMPLETE: a finite natural kappa^2-scaled endpoint limit, and nonnegative
curvature near c=1. No full-configuration entropy concavity claim is made.

The finite cyclic-projection checks test algebra ONLY. The true finite sine
checks retain Q_A-Q_A^2 and never regard a Toeplitz compression as a projection.

Run: OPENBLAS_NUM_THREADS=1 python S51_C1_checks.py
Python dependency: numpy.
