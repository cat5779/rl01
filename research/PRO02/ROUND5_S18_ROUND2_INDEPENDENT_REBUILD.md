# S18 Round 2 finite certificate: independent rebuild

Date: 2026-09-18

Status: **finite claims independently reproduced; entropy-rate claim still open**.

## Scope and evidence boundary

The visible S18 Round 2 message was available, but its new attachment bodies were
not.  I therefore used the message only to identify claims to test.  I did not
treat its stated intervals, proof script, or status label as certified input.

A repository search found no `compute01` copy of the new 12-site or neighborhood
certificate.  It did find the older same-author six-site pair witness at
`results/S7/certificates/pair_witness.json`; that file was excluded as an
independent source.  The checks below instead rebuild the atoms and derivatives
directly from the finite sine kernel.

The specifically suggested directory `C:\Users\UIO\Desktop\20260907` contains
`RESULTS18` and `PRO02_checks S18`, but SHA-256 comparison shows that they are
byte-for-byte identical to the already archived `S18_RESULT.md` and
`checks/S18_PRO02_checks.py` respectively (`0B7F4860...C355B` and
`EE2F53C5...BD2DF`).  They are the recovered Round 1 artifacts, not the missing
Round 2 attachments.

## Independent method

At half density, with `c=19/20`, put

\[
 K_n(a)=aI+cQ_n,\qquad
 (Q_n)_{ij}=\begin{cases}
 1/2,&i=j,\\
 \sin(\pi(i-j)/2)/(\pi(i-j)),&i\ne j.
 \end{cases}
\]

For every word `y`, the checker evaluates the actual DPP atom

\[
 p_y(a)=(-1)^{\#\{i:y_i=0\}}
 \det\bigl(K_n(a)-I_{\{i:y_i=0\}}\bigr)
\]

in 256-bit Arb ball arithmetic.  If `G_y` is the inverse of the matrix inside
the determinant, direct determinant differentiation gives

\[
 p_y'=p_y\operatorname{tr}G_y,
 \qquad
 p_y''=p_y\bigl((\operatorname{tr}G_y)^2-
 \operatorname{tr}(G_y^2)\bigr),
\]

and hence

\[
 H_n''=-\sum_y\left(p_y''\log p_y+\frac{(p_y')^2}{p_y}\right).
\]

This is a different implementation route from the missing author's stated
minor-marginal/Janossy program.  Every atom must be strictly positive as an Arb
ball or the program aborts.

For independent diagonal shifts, the same inverse yields the complete Hessian.
The checker also verifies that its all-ones quadratic direction equals the
separately accumulated common-shift curvature.  Negative definiteness is not
inferred from floating-point eigenvalues: an interval `LDL^T` factorization of
`-Hessian-4.85 I` must have six strictly positive pivots.

## Certified results

The direct enumeration gives

\[
 H_6''(1/40)=
 [-49.5655212392509631975961954433188966659964420194298033311591578608393900
 \;\pm 5.57\times10^{-71}],
\]

with normalization diagnostics

\[
 \sum_y p_y=1\pm1.85\times10^{-75},\quad
 \sum_y p_y'=0\pm3.17\times10^{-74},\quad
 \sum_y p_y''=0\pm1.71\times10^{-72}.
\]

The six-coordinate Hessian satisfies the stronger independently certified
bound

\[
 \lambda_{\max}(\nabla^2 H_6)<-4.85,
\]

so it in particular implies the submitted `-4.289916...` bound.  The last
`LDL^T` pivot is still strictly positive:

\[
 0.0079320134876695262\ldots\pm7.16\times10^{-71}.
\]

The claimed sign failure of entrywise negativity is also reproduced:

\[
 \partial_{t_1}\partial_{t_6}H_6=
 0.0003790922420416860132632736413167970\ldots
 \pm4.05\times10^{-73}>0.
\]

For the neighborhood, 1024 exact rational subintervals cover
`[3/200,7/200]`.  Direct interval evaluation on every cell proves the uniform
bound

\[
 H_6''(a)<-44.9<0
 \qquad(3/200\le a\le7/200).
\]

This is substantially stronger than the visible submission's looser
`-2.921874...` upper bound.  The largest upper endpoint encountered in the
1024-cell run was `-47.34058659490649...`; `-44.9` is retained as the simple
reproducible theorem margin.

Using all 4096 twelve-site words gives

\[
 H_{12}''(1/40)=
 [-126.18012856070795600233729690376512423856024222506376183770570420617582
 \;\pm2.25\times10^{-69}],
\]

with `sum p = 1 +/- 4.67e-74`, `sum p' = 0 +/- 1.33e-72`, and
`sum p'' = 0 +/- 1.57e-70`.  Therefore the exact stationarity identity

\[
 \operatorname{TC}_{6,6}''=2H_6''-H_{12}''
\]

gives

\[
 \operatorname{TC}_{6,6}''(1/40)=
 [27.04908608220602960714490601712733090656735818620415517538738848449704
 \;\pm2.36\times10^{-69}]>27.0490.
\]

All displayed central values agree with the visible S18 intervals.

## Independent numerical cross-check

The pre-existing high-precision `mpmath` enumerator uses direct determinants
and separately accumulates the inverse-potential identity.  A fresh 12-site run
gave

```text
sum_p = 1.000000000000000000000000000000000000000000000000000000000001400178438
direct H12pp = -126.1801285607079560023372969037651242385602422250637618377056102312323
potential H12pp = -126.1801285607079560023372969037651242385602422250637618377059089359656
difference = 2.9870473333733480194e-58
```

This second computation is not used for rigor, but it checks the Arb route
against a separately expressed entropy-curvature identity.

## Verdict and remaining obstruction

The visible S18 conclusion is supported **at its stated finite scope**:

1. six-site benchmark curvature is negative;
2. the six-site result persists on the claimed neighborhood;
3. the full six-coordinate Hessian is negative definite despite a positive
   remote mixed entry;
4. twelve-site benchmark curvature is negative; and
5. the first `6 -> 12` total-correlation correction is strictly favorable.

The missing attachments remain unaudited as artifacts, but their central
finite claims no longer depend on trusting them: they have been independently
rebuilt here.

This does **not** prove entropy-rate concavity.  Positivity of
`TC_{6,6}''` is one scale and one point only.  It does not imply the required
uniform finite-chord condition for `TC_N` at all `N`, nor justify a
thermodynamic derivative-limit exchange.  Thus the correct final status is:

- finite `n=6`, `n=12`, and the first scale-doubling interface: **verified**;
- all-scale/entropy-rate curvature: **open**.

## Reproduction

From the repository root:

```powershell
uv run --with python-flint python research/PRO02/checks/verify_s18_round2_finite.py --parts 1024
```

The rigorous checker is `checks/verify_s18_round2_finite.py`.
