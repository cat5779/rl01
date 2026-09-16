# S6 gap audit

## 1. Frozen target and delivered status

The target is concavity in a of the measured full-configuration entropy rate h_rho(a,c), for the true sine Toeplitz blocks, at fixed 0<rho<1 and fixed 37/40<c<1 as n grows. It has not been proved or disproved in this bundle.

The status `DISPROVED_ROUTE_LEMMA` refers only to an unrestricted Berezin trial-action Jensen connection, as formulated in [NRR24, Eqs. (134)-(136)]. It is not a claim that the integer field representation is wrong, that all mean-field lower bounds are false, or that the sine target is false.

## 2. Exact versus approximate statements

| Statement | Status | Scope / remaining issue |
|---|---|---|
| p(S)=det(I-K)det L_S; Z(q)=sum p(S)^q | Supplied baseline, retained exactly | No novelty claimed |
| Integer-replica Grassmann integral | Exact; proved independently | Integer replicas only |
| Two-replica sign integral | Exact; proved independently | q=2 only |
| Positive Gibbs variational formula | Exact finite classical identity | Full 2^n-configuration optimization remains |
| a- and q-derivatives at fixed finite n | Justified on compact legal a-intervals | No dimension-uniform derivative bounds asserted |
| Unrestricted Gaussian-trial Jensen lower bound | **Disproved** | Strict reverse inequality for every Hermitian L>0 |
| Fourier error >180 n at a=1/40,c=19/20,k=n/2 | Complete all-even-n proof | Error of the auxiliary bound, not H curvature |
| Density-only uncorrected mean-field lower bound | Valid by Cauchy-Schwarz | This subfamily is not disproved; no Shannon error bound |
| Real-q product-Hölder bound | Valid finite-q inequality | Product trial family only |
| Optimized product tangent equals sum b(K_ii) | Exact finite derivative identity | Does not replace measured entropy |
| True Toeplitz product-tangent error >=8 floor(n/2)c^4[sin(pi rho)/pi]^4 | Complete growing-family estimate | Controls the omitted Shannon derivative, not its a-curvature |
| H_4'' point enclosure | Exact finite certificate | One coupled four-site kernel and one interior a,c |
| Stationary-trial 101-point grid | Exact grid diagnostic only | No interval sign or universal conclusion |

## 3. Every step still missing for a target proof by this route

1. The complete curvature identity still contains the acceleration term `sum p_a''(S) log p_a(S)`. No estimate establishes that it is bounded below by minus the Fisher term, up to a sublinear error, for the Fourier projections of proportional rank or for Q_n.
2. The false unrestricted Berezin Jensen argument cannot be used to supply that estimate. The failure is quantitative and extensive even in a fixed interior strip.
3. The valid density-only q=2 bound does not determine the real-q derivative at 1. No analytic-continuation uniqueness statement based only on integer replicas is used or proved.
4. The specified real-q product repair loses an extensive derivative at 1. Its missing term is the spatial total correlation. Neither the positivity nor the lower bound for this error controls its a-curvature or its Jensen difference.
5. An exact correlated trial family is possible in the Gibbs variational formula, but no tractable correlated optimization with the needed error control has been established. Replacing it by the exact escort law merely restates the original problem and is not offered as progress.
6. There is no uniform bound justifying a- or q-differentiation after n goes to infinity. The rate consequence in Theorem 7.1 uses only entropy values and the supplied existence of their limit.
7. No finite cyclic entropy-concavity theorem or sublinear cyclic Jensen error is proved. The supplied cyclic-to-Toeplitz bridge therefore has no new concavity input to transfer here.

## 4. Known hazards explicitly excluded

- **Full spatial atoms:** Adjacent and opposite pairs in the four-site example are kept distinct. No entropy of particle count is substituted.
- **Projection versus true Toeplitz:** Only P_(n,k) is used in the projection identities. The Toeplitz error estimate uses its exact nearest-neighbor entries separately. In the code, the cyclic pair deficit is c^2/8, not the true rho=1/2 Toeplitz value c^2/pi^2.
- **Spatial basis:** No arbitrary unitary transformation is applied to the measured law. Constant diagonal in the Fourier theorem is calculated directly from its specified U entries.
- **Quantum measurement:** No spectral/von Neumann entropy or quasi-free relative entropy is used. No o(n) measurement loss is assumed.
- **Moving expectations:** The escort-law covariance derivatives and all normalization derivatives are retained in recovering H''.
- **Saddles:** There is no saddle-point error estimate. The unrestricted variational counterexample is not extrapolated to every stationary saddle.
- **Recursion:** No coordinatewise completion inequality, latent-tree sign, or pair-smoothing assumption is invoked.
- **Endpoints:** The obstruction has fixed a=1/40,c=19/20 for every n. The product-gap endpoint extension uses continuity, not a nonuniform endpoint expansion.

## 5. Important distinction about the paper's mean-field claims

The counterexample uses S_trial=Q_L. This is a legitimate trial in the unrestricted statement and corresponds to zero density fields. It does not satisfy the nonzero density self-consistency equations. Therefore it directly refutes the unrestricted Jensen-corrected functional, not necessarily the specialized interpolation starting at a self-consistent solution.

For the density-only uncorrected functional, a direct Cauchy-Schwarz bound proves a lower bound, as shown in proof.md Section 6.1. The exploratory self-consistent example found no negative curvature on its grid and is preserved rather than omitted. No claim that Appendix I's specialized self-consistent interpolation is always nonconvex is made.

## 6. Certificate limitations and independent checking

The certificate is exact over rational/Gaussian-rational arithmetic. Transcendental signs use a proved positive-series remainder bound and rational interval endpoints. This avoids rounding-based sign claims. Nonetheless, software can contain mistakes: the proof gives closed-form quantities and all sixteen atom derivatives so an independent implementation need not trust the supplied code.

Seven regression tests and a fresh-extraction reproduction are self-checks only. They do not constitute independent certification. The original conjecture and every missing thermodynamic curvature step remain open within this deliverable.
