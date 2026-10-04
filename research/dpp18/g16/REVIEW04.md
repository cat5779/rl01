PASS_CORRECT_SCOPED

# Independent audit of the fixed-projector weighted selector

## Audited statement and boundary

I audited `PROOF03.md` together with its incorporated correction
`ERRATUM03.md`, and independently checked the support-degeneration argument in
`TOPOLOGY03.md` and the method boundary in `METHOD03.md`.  I treated
`REVIEW03.md` only as a list of locations to attack, not as evidence.

The result that passes is exactly the following.  Let (E) be finite,
(0<\varepsilon<1/2), and let the **same** rank-one projector (P=vv^*)
commute with two kernels

\[
 \varepsilon I\preceq K,L\preceq(1-\varepsilon)I.
\]

On the full positive upward-flow fiber with divergence (b_{K,P}), total mass
one, and outgoing capacity ((2/\varepsilon)p_K(S)), define

\[
 w_K(S,i)=P_{ii}\bigl(p_K(S)+p_K(S\cup\{i\})\bigr)
\]

and let (\Psi_E(K,P)) be the unique minimizer of
(\frac12\sum_e f_e^2/w_K(e)), with zero-weight directions forced to zero.
Then

\[
 \|\Psi_E(K,P)-\Psi_E(L,P)\|_1
 \le 10\varepsilon^{-3/2}\|K-L\|_{\rm tr}^{1/2}.
\]

The constant is independent of (|E|) and of the coordinate support of (P).
This audit does **not** pass a varying-(P) estimate, exponent one, unrestricted
non-diagonal selection, finite consistency for arbitrary lists with varying
projectors, exact JO, or a general strong-factor construction.

## 1. Exact atoms, Schur gap, weights, and current energy

The atom/resolvent normalization in `PROOF03.md` lines 23--43 is consistent.
For (M_S=K-D_{S^c}),

\[
 M_S=(K-\tfrac12I)+(\tfrac12I-D_{S^c})
\]

has

\[
 s_{\min}(M_S)\ge \tfrac12-\|K-\tfrac12I\|_{\rm op}
 \ge\varepsilon,
\]

so (\|M_S^{-1}\|_{\rm op}\le\varepsilon^{-1}).  Successive occupation and
vacancy conditioning preserves the same gap: occupation is the Schur
complement of (K), while vacancy is the corresponding Schur complement of
(I-K).  Hence every exact one-coordinate conditional probability is in
([\varepsilon,1-\varepsilon]), including the boundary eigenvalue cases.

For an edge (e=(S,i)), (p_K(S)+p_K(S+i)) is the exact reduced atom on
(E\setminus\{i\}).  Therefore

\[
 \sum_e w_K(e)=\sum_iP_{ii}=1.
\]

Testing the divergence equation against (1_{\{i\in S\}}) gives total flow in
direction (i) equal to (P_{ii}).  Thus (P_{ii}=0) really forces every
such edge to carry zero flow; no positive-weight term is silently deleted.

The two incident formulas in `PROOF03.md` lines 28--34 describe the same
signed edge current.  At either endpoint,

\[
 \frac{J_e^2}{w_K(e)}
 \le (1-\varepsilon)p_K(S)|u_i^S|^2,
 \qquad u^S=M_S^{-1}v.
\]

Summing over all vertices counts every edge exactly twice and gives

\[
 2\|J_K\|_{w_K}^2
 \le (1-\varepsilon)\sum_Sp_K(S)\|u^S\|_2^2
 \le\frac{1-\varepsilon}{\varepsilon^2}.
\]

Thus equation (1) and (\|J_K\|_{w_K}\le B_\varepsilon/2), with
(B_\varepsilon^2=2(1-\varepsilon)/\varepsilon^2), have the correct factor
of two.  A positive endpoint flow bounded by (2(J_K)_+) consequently has
weighted norm at most (B_\varepsilon), which supplies the uniform energy
competitor used for the minimizer.

## 2. Weight derivative and complete-current endpoint count

For a gapped segment with derivative (D) and
(d=\|D\|_{\rm tr}), the reduced-atom determinant derivative gives

\[
 |\partial_t\log w_t(e)|
 =|\operatorname{tr}(M_{e,t}^{-1}D_{E\setminus\{i\}})|
 \le d/\varepsilon.
\]

Compression contracts trace norm, so `PROOF03.md` equation (3) and the metric
comparison (e^{-q}w_K\le w_L\le e^qw_K), (q=d/\varepsilon), are valid.

The correction in `ERRATUM03.md` is essential and correct.  Writing

\[
 \dot p(S)=p(S)\alpha_S,
 \quad \alpha_S=\operatorname{tr}(M_S^{-1}D),
 \quad \dot u^S=-M_S^{-1}Du^S,
\]

one must first differentiate the complete current.  The same edge derivative
then has, from either incident endpoint (S), the representation

\[
 \dot J_e=\pm p(S)\operatorname{Re}
 \left[v_i\overline{\alpha_Su_i^S+\dot u_i^S}\right].
\]

Only at this stage is the two-endpoint count legitimate.  It yields

\[
 2\|\dot J_t\|_{w_t}^2
 \le(1-\varepsilon)\sum_Sp(S)
       \|\alpha_Su^S+\dot u^S\|_2^2
 \le(1-\varepsilon)(2d/\varepsilon^2)^2,
\]

because (|\alpha_S|\le d/\varepsilon),
(\|u^S\|\le\varepsilon^{-1}), and
(\|\dot u^S\|\le d\varepsilon^{-2}).  Hence

\[
 \|\dot J_t\|_{w_t}\le(B_\varepsilon/\varepsilon)d.
\]

This verifies the corrected equation (4).  The invalid older maneuver of
double-counting the split inverse-factor term is not used by the current
proof.

## 3. Positive residual state and all max-flow cuts

The residual-state argument in `PROOF03.md` lines 101--128 is sufficient, not
merely a signed-flow construction.  With (U=C+C^*), define

\[
 q_\tau(S,T)=\operatorname{Re}
 \bigl[U_{T,S}(\rho_\tau U)_{S,T}\bigr].
\]

The row and column sums are respectively the diagonals of (\rho_\tau) and
(U\rho_\tau U).  Number preservation and support on the marked-empty
subspace imply that (q_\tau) is supported only on upward one-point edges.

For source and target families (A,B), let (R=R_A) and
(Q=U^*(I-R_B)U).  Since

\[
 RQ+QR-(R+Q-I)=(R+Q-I)^2\succeq0,
\]

positivity of (\rho_\tau) gives

\[
 \alpha_\tau(A)-\beta_\tau(B)
 \le2\operatorname{Re}\operatorname{tr}(\rho_\tau QR)
 =2\sum_{S\in A,T\notin B}q_\tau(S,T)
 \le2\sum_{S\in A,T\notin B}(q_\tau(S,T))_+.
\]

These are exactly the necessary and sufficient bipartite transportation cuts
(\alpha(A)-\beta(B)\le c(A,B^c)).  Finite max-flow therefore gives an
honest positive endpoint flow (0\le h_\tau\le2(q_\tau)_+) with both required
marginals and total mass (\operatorname{tr}\rho_\tau).  No signed flow has
been substituted for a positive selector.

## 4. Loewner residual, capacity, and two directed weighted repairs

I separately checked the inherited fixed-background comparison used at
`PROOF03.md` lines 150--155.  For the normalized Gaussian density
(\sigma_{B_t}) on the common marked-empty Fock space, put

\[
 M_t=[B_t(I-B_t)]^{-1/2}\dot B_t[B_t(I-B_t)]^{-1/2}.
\]

The sandwiched derivative is

\[
 \sigma_t^{-1/2}\dot\sigma_t\sigma_t^{-1/2}
 =d\Gamma(M_t)-\operatorname{tr}(B_tM_t)I.
\]

The spectrum of (d\Gamma(M_t)) consists of subset sums of the eigenvalues of
(M_t), while (\operatorname{tr}(B_tM_t)) lies between the sum of the
negative eigenvalues and the sum of the positive eigenvalues.  Consequently

\[
 \|\sigma_t^{-1/2}\dot\sigma_t\sigma_t^{-1/2}\|_{\rm op}
 \le\|M_t\|_{\rm tr}
 \le\frac{d_B}{\varepsilon(1-\varepsilon)}.
\]

Integrating the two Loewner differential inequalities gives

\[
 \rho_{0,B'}-c_B\rho_{0,B}\succeq0,
 \qquad c_B=e^{-d_B/[\varepsilon(1-\varepsilon)]}.
\]

For this residual, linearity of the quasi-current gives
(q_\tau=J_M-c_BJ_K).  Using the current derivative estimate and metric
comparison,

\[
 \|J_M-J_K\|_{w_K}\le e^{q_B/2}B_\varepsilon q_B,
 \qquad q_B=d_B/\varepsilon,
\]

and therefore

\[
 \|h_\tau\|_{w_K}
 \le2e^{q_B/2}B_\varepsilon q_B+(1-c_B)B_\varepsilon.
\]

For (g_M=c_Bf+h_\tau), the capacity check is coefficientwise and has the
correct direction:

\[
 p_M-c_Bp_K=(1-\lambda)\alpha_\tau+\lambda\beta_\tau,
 \qquad (h_\tau)_{\rm out}=\alpha_\tau,
\]

and (2(1-\lambda)/\varepsilon\ge2).  Thus
(g_M\in\mathcal F(M,P)), not only in an uncapped divergence fiber, and

\[
 \|g_M-f\|_{w_K}\le8B_\varepsilon q_B.
\]

For the marked eigenvalue step, the coefficient

\[
 c_\lambda=\min\left\{1,\frac\nu\lambda,
 \frac{1-\nu-\varepsilon/2}{1-\lambda-\varepsilon/2}\right\}
\]

is well-defined because the two denominators are positive.  It gives

\[
 \nu-c_\lambda\lambda\ge0,
 \qquad
 1-\nu-c_\lambda(1-\lambda)
 \ge(\varepsilon/2)(1-c_\lambda),
\]

and

\[
 1-c_\lambda\le2|\lambda-\nu|/\varepsilon.
\]

Adding ((1-c_\lambda)) times a positive endpoint flow therefore preserves
the full outgoing capacity of (L).  The resulting repair satisfies

\[
 \|g_L-f\|_{w_K}
 \le8B_\varepsilon(q_B+q_\lambda),
 \qquad q_\lambda=|\lambda-\nu|/\varepsilon.
\]

Repeating the same construction with (K,L) interchanged supplies the reverse
repair in the (w_L) metric.  The proof thus has both directed competitors
needed later; it does not infer them from a one-sided Hausdorff statement.

## 5. Variational inequalities and the metric-change constant

Let (f=\Psi(K,P)), (g=\Psi(L,P)), and choose the two repaired competitors
as in `PROOF03.md` lines 205--211:

\[
 f+u\in\mathcal F(L,P),\quad\|u\|_{w_K}\le8B_\varepsilon q,
\]
\[
 g+z\in\mathcal F(K,P),\quad\|z\|_{w_L}\le8B_\varepsilon q.
\]

The first-order inequalities for the two convex minimizations are

\[
 \langle f,f-g\rangle_{w_K}\le\langle f,z\rangle_{w_K},
 \qquad
 \langle g,g-f\rangle_{w_L}\le\langle g,u\rangle_{w_L}.
\]

For (X=\|f-g\|_{w_K}), their left sides add to

\[
 X^2+
 \langle g,f-g\rangle_{w_K}
 -\langle g,f-g\rangle_{w_L}.
\]

Metric conversion bounds the two repair terms by
(16e^{q/2}B_\varepsilon^2q\le32B_\varepsilon^2q).  Moreover

\[
 |w_K(e)^{-1}-w_L(e)^{-1}|
 \le(e^q-1)w_K(e)^{-1},
\]

so the remaining metric-change term is at most

\[
 (e^q-1)\|g\|_{w_K}X
 \le 2q\,(2B_\varepsilon)(3B_\varepsilon)
 =12B_\varepsilon^2q.
\]

Hence

\[
 X^2\le44B_\varepsilon^2q\le50B_\varepsilon^2q.
\]

Because (\sum_e w_K(e)=1), Cauchy--Schwarz gives
(\|f-g\|_1\le X), and therefore

\[
 \|f-g\|_1
 \le10\sqrt{1-\varepsilon}\,\varepsilon^{-3/2}\sqrt d
 \le10\varepsilon^{-3/2}\sqrt d.
\]

For (d\ge\varepsilon), the unit-mass bound (\|f-g\|_1\le2) is more than
sufficient.  Thus neither the exponent nor the displayed constant is obtained
by hiding a dimension- or support-dependent term.

## 6. Borel rule and support degeneration

`PROOF03.md` lines 245--251 correctly obtain one rule, not a separately chosen
pairwise repair.  On each of the finitely many strata determined by
(P_{ii}>0) or (P_{ii}=0), the feasible constraints have polynomial right
sides and fixed normals, the positive weights are rational functions with
positive denominators, and the objective is strictly convex on all unforced
coordinates.  Its unique minimizer is a semialgebraic, hence Borel, function
on that stratum.  A finite union of the strata is Borel, and uniqueness plus
naturality gives exact coordinate-permutation covariance.

The stronger fixed-(E) continuity claim in `TOPOLOGY03.md` also survives
support loss.  The fixed-normal Hoffman bound supplies nearby feasible
competitors, which is the lower-hemicontinuity step absent from a bare compact
graph argument.  If (P_{ii}\to0), every feasible edge obeys

\[
 0\le f(S,i)\le P_{ii},\qquad
 w_{K,P}(S,i)\ge P_{ii}\varepsilon^{|E|-1},
\]

and hence

\[
 0\le f(S,i)^2/w_{K,P}(S,i)
 \le P_{ii}\varepsilon^{-(|E|-1)}\longrightarrow0.
\]

Thus the deleted energy term agrees with the limiting value.  The Hoffman and
atom constants may depend on fixed (E), exactly as the supplement states;
they are not used in the dimension-free fixed-(P) Hölder estimate.

## 7. Method boundary and final scope ruling

The auxiliary obstruction in `METHOD03.md` is scoped correctly.  At
(K=I/2), distinct marked-empty Fock supports have intersection dimension
(2^{|E|-2}), so the maximal common positive mass is (1/2), even when the
two quantum states approach one another in trace norm.  But for (K=aI) the
weighted minimizer is explicitly

\[
 \Psi(aI,P)(S,i)=P_{ii}a^{|S|}(1-a)^{|E|-1-|S|},
\]

and it is identical for distinct projectors with the same coordinate
diagonal.  Therefore the quantum common-substate failure is only an
obstruction to that repair mechanism, not a counterexample to positive
selection or finite consistency.  The two-plane rotation used for the general
endpoint trace comparison has dimension-free second-quantized operator
displacement, but does not preserve coordinate one-birth edges; it supplies no
missing varying-(P) repair.

No critical mathematical gap remains in the frozen fixed-(P), exponent-one-
half theorem.  External peer review, full formalization, and novelty/priority
are not certified by this audit.

