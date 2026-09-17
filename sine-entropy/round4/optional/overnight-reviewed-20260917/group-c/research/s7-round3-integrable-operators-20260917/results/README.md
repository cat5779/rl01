# S7 / PR111: actual-law spatial curvature control

**Status: PROVED_SCOPED_LEMMA.** These are author proofs and author arithmetic
checks, pending independent review. The ultimate sine entropy-rate concavity
target is **still open**; this is not PROVED_SINE_TARGET or a target counterexample.

The main result is a quantitative approximation of the **complete labelled
configuration Shannon Hessian** by an explicitly finite conditional-table
expression, with paid pair-distance, observation-radius, and finite-volume
errors. It applies to every fixed strict noisy channel, including high contrast,
and every density. A separate growing actual Toeplitz family disproves the
word-uniform `C/|i-j|` inverse estimate that would have been a tempting shortcut.

## Read in this order

1. `PROOF.md`: Theorems A--C, full-word and posterior identities, complete mixed
   Hessian, actual posterior spatial energy, and its matching-order lower bound.
2. `AVERAGED_LOCALIZATION.md`: Theorem F, the principal new observation-radius
   improvement, and the fully finite enclosure of entropy-rate curvature.
3. `OBSTRUCTIONS.md`: a certified positive averaged pair, two other scoped
   interface failures, and the growing alternating-word inverse obstruction.
4. `ONE_SIDED_CURVATURE.md`: an upper enclosure with no single-site
   coarsening cost; the negative conditional Fisher gain is retained.
5. `QUASILOCALITY.md`: a separately proved word-uniform weighted estimate and a
   faster pair-distance curvature tail; not needed for Theorem F's main error.

`DEPENDENCY_DELTA.md`, `SCOUT_LEDGER.md`, `CANDIDATE_FREEZE.md`, and `GAP_AUDIT.md`
delimit imported facts, hypotheses, candidate decisions, and remaining gaps.
`REPRODUCE.md` describes the arithmetic certificates. `WORK_LOG.md` records
observed elapsed time, not an invented computation budget.

## Frozen main statement

Let Q_n be the actual n-site compression of the one-interval Fourier projection
of density 0<rho<1. Let K_n=aI+cQ_n, with 0<c<1 and 0<a<1-c. Set

\[
 d=1-a-c,\quad\delta=\min(a,d),\quad m=\max(a,d),\quad
 \beta_*=\delta(\delta+c),\quad
 M=\max\{1,\log[(a+c)(1-a)/(ad)]\},
\]
\[
 B_* =\min\{3c^2/(8\delta^4),3c^2/(2\beta_*^2)\},\qquad
 C_* =\min\{3c^4/(16\delta^8),3c^2M/(2\beta_*^2)\}.
\]

For a one-site conditional probability u put f(u)=1/[u(1-u)]. For a normalized
two-site conditional table p put

\[
 g(p)=\log\frac{p_{10}p_{01}}{p_{00}p_{11}}
 -(p_{10}p_{01}-p_{00}p_{11})\sum_b p_b^{-1}.
\]

Let u^(L) be the conditional output probability at 0 given all other outputs
in [-L,L], and let p^(r,L) be the conditional table at {0,r} given all other
outputs in [-L,r+L]. All expectations below are their actual noisy-sine laws.
For positive integers R,L define the genuinely finite expression

\[
 \mathcal K_{R,L}=-\mathbb E f(u^{(L)})
       +2\sum_{r=1}^{R-1}\mathbb E g(p^{(r,L)}).
\]

Then, for every positive integer n,

\[
\begin{aligned}
\left|H_n''/n-\mathcal K_{R,L}\right|
\le{}&C_*/R+
 \frac{B_*\delta^{-4}}L\{m^{-1}+156(R-1)m^{-2}\}\\
&+\frac{\delta^{-2}}n
 [4L+M\{8L(R-1)+R(R-1)\}].
\end{aligned}
\]

Consequently, for the stationary entropy rate,

\[
 |h_\rho''-\mathcal K_{R,L}|
 \le C_*/R+
 \frac{B_*\delta^{-4}}L\{m^{-1}+156(R-1)m^{-2}\}.
\]

The observation error is **O_(a,c)(R/L)**, not the much slower
O_(a,c)(R L^(-delta/64)) word-uniform fallback. All constants are independent
of rho and n, but diverge at the channel boundary. The proof is by a coupled
actual-word resolvent identity and an explicit fixed-completion likelihood
payment; it does not invoke a general kernel-mixture assertion.

Taking R=floor(n^(1/4)), L=ceil(n^(1/2)) gives the conservative bound

\[
 |H_n''/n-h_\rho''|\le D_*n^{-1/4}\quad(n\ge16),
\]

with D_* stated in Theorem F. Basic C^2 regularity itself is not claimed new
relative to S6's reviewed response estimates. The new contribution is the
spatial conditional-table approximation and its paid errors.

## The spatial mechanism and its limits

For the complete-input posterior kernel R^Y, the analytical proof gives

\[
 \mathbb E\sum_{|i-j|\ge R}|R^Y_{ij}|^2\le3n/(2R).
\]

A conditional-variance inequality, bounded Fourier phases, and a tent cutoff
pay the finite-compression boundary. At rho=1/2, n>=4R, the same energy is at
least tau^4 n/(8 pi^2 R), where tau=sqrt(a(a+c))+sqrt(d(1-a)). Thus its n/R
order is sharp; the entropy-curvature remainder can decay faster because g
has additional cancellation. No sharpness for curvature is asserted.

For rho=1/2, fixed c, a=(1-c)/2, and the alternating output on 2M+1 sites,
`OBSTRUCTIONS.md` proves a lower bound

\[
 |G_{0,2M}|\ge A_c(M+1)^{-1+\eta_c},\qquad
 \eta_c=c^2/[\pi^2(1+c^2)]>0.
\]

This is a growing, fixed-density, fixed-noise **actual Toeplitz** family.
It rules out a uniform C/r bound and all fixed-polylogarithmic C(log r)^k/r
variants over every word. It does not contradict the actual-law average.

A separate exact six-site sine certificate at rho=1/2, c=19/20, a=1/40 gives

\[
 37/100000<\mathbb E g_{1,6}<39/100000,
 \qquad -50<H_6''<-49.
\]

Thus even actual averaging does not make every pair nonpositive; the TOTAL
curvature in this witness is negative. This is not a target counterexample.

## Precise unresolved step

No upper bound on K_(R,L) has been proved that pays the two positive error
terms uniformly in the requested high-contrast range. In particular, neither
reflection symmetry nor pairwise averaged nonpositivity closes that gap.
There is no new contrast threshold, no endpoint-uniform estimate, and no
full-interval concavity certificate in this submission.

Reviewed baseline: `aaf3e86576a867067701089805c9e5e5a83e44f5`.
Assignment parent: `549a3a532454dd870b63b89d71bbbda1286bda48`.
Only this PR's assigned results directory is used for the new mathematics.
