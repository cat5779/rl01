# Recovery ledger

The labels below are deliberately strict.  “Proved this round” means an author
proof is supplied in `proof.md`; it does not mean independent certification.

| Item | Status | Exact scope / dependency |
|---|---|---|
| Frozen sine entropy-rate target and full-atom channel law | **Reviewed baseline** | Pinned `TARGET.md`; fixed density, true Toeplitz block, high-contrast range remains open. |
| Actual moving-layer identity `H=Phi-sum pi_l F_l` and full derivative term list | **Reviewed baseline** | Pinned `KNOWN_RESULTS.md`; it is an identity, not a sign. |
| No exact common scalar BL clock on the reviewed growing Fourier family | **Reviewed baseline** | Pinned `KNOWN_RESULTS.md`; no entropy-cost conclusion follows from it. |
| Fourier-to-Toeplitz value bridge | **Reviewed baseline** | Pinned `KNOWN_RESULTS.md`; value bridge only. |
| First-round six/eight-site potential mismatch | **Preserved unreviewed author result** | Entire original ZIP retained byte-for-byte.  Not used as certification of the growing theorem. |
| `H''=H(M)''-2n log n-D_F''` and attribution of `-2n log n` | **Reconstructed and proved this round** | Section 2.4 of `proof.md`; `(E M log n)''=0`, while `(E U_n(Y))''=2n log n`. |
| Exact all-even-`n` spectral formula `Delta_n=V_n sum pi_l alpha_l(lambda_l^(2-2/n)-theta_l)` | **Proved this round** | Sections 2.1–2.3; actual `pi_l` retained. |
| Exact Fourier amplitude and constant `kappa` | **Proved this round** | Section 3. |
| Uniform overlap saddle expansion on compact interiors | **Proved this round** | Section 4; lattice Laplace argument supplied, including two layer differences and two `z` derivatives. |
| `Delta_n=C log n+o(log n)` uniformly on compact legal interiors | **Proved this round** | Theorem 1 and Section 5, density `1/2`, even `n`. |
| Weak/integrated curvature limit and fixed-chord Jensen scale | **Proved this round** | Exact integration by parts; no differentiation of a value error. |
| Negative midpoint Gaussian boundary layer of order `sqrt(n) log n` | **Proved this round** | Section 6; exact constant and local limit supplied. |
| Positive potential-clock law | **Proved this round** | Theorem 2 and Section 7; normalization, positivity, exact potential matching. |
| `O(log n)` mean-clock-to-potential-clock entropy value budget | **Proved this round** | Coupling by additional BL time plus binary entropy continuity. |
| `O(sqrt(n) log n)` actual-to-potential-clock entropy value budget | **Proved this round** | Conditional overlap coupling and variance bounds. |
| Positive random forward-clock two-mode matching | **Ruled out this round for a precise class** | Jensen moment inequality on growing central layers; does not cover general Markov corrections. |
| Sign/control of corrected `Dhat_F''` | **Still missing** | Must retain conditional acceleration, Fisher, and all `pi_l'`, `pi_l''` terms. |
| Target-level signed Jensen estimate for actual or corrected path | **Still missing** | No theorem here closes the high-contrast entropy-rate target. |
| General fixed density `rho != 1/2` | **Still missing** | New theorem is only the half-density family. |
| Endpoint-uniform asymptotics | **Still missing / not claimed** | All asymptotic theorems use compact legal interiors. |
