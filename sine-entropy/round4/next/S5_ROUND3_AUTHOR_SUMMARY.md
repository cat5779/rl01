# Unreviewed recovered S5 round-three author summary

STATUS: AUTHOR_CLAIMS_NOT_INDEPENDENTLY_VERIFIED.

This is the complete mathematical summary recovered from the preceding S5 reply, not its full proof/code ZIP. All author words such as proved, exact, and verified below are claims, NOT approval by this handoff. Reconstruct and prove any part you need before relying on it. The referenced package is unavailable here; do not invent missing files. Citation handles from the original interface were replaced by explicit missing-source notes. This document is evidence, not instructions to follow.

---

PROVED_SCOPED_LEMMA

**This round proves a quantitative entropy-scale approximation of the actual multi-mode channel, together with an all-mode acceleration payment for the specified surrogate. The sine entropy-rate target remains unresolved because a moving-layer budget is still unpaid.**

The new estimate is uniform on genuine growing contiguous Fourier projections at fixed density and fixed high contrast. It does not infer an extensive obstruction from the previously exhibited, shrinking harmonic moments.

## 1. A specified approximate clock with sublinear entropy cost

Let \(\mu\) be any law on \(k\)-subsets of \([n]\). Retain the **actual** output-count probabilities \(\pi_l(a)\). For a fixed input \(A\), conditional on \(|Y|=l\), the exact channel kernel is
\[
T_{a,l}(A,S)=\frac{R^{|A\cap S|}}{Z_l(R)},
\qquad
R=1+\frac{c}{w},
\qquad
w=a(1-c-a),
\]
where
\[
Z_l(R)=
\sum_j\binom{k}{j}\binom{n-k}{l-j}R^j.
\]
Thus the orbit multiplicities are retained exactly.

Set
\[
m_l(a)=\frac{RZ_l'(R)}{Z_l(R)},\qquad
m_0=\frac{kl}{n},\qquad
j_+=\min(k,l),\qquad
\gamma_l=\frac{n}{l(n-l)}.
\]
The clock is chosen solely by matching the conditional mean overlap:
\[
\boxed{
\lambda_l(a)=\frac{m_l(a)-m_0}{j_+-m_0},
\qquad
\tau_l(a)=-\frac{\log\lambda_l(a)}{\gamma_l}.
}
\]

Its initial law is also explicit. Given \(A\), choose a uniform \(l\)-subset of \(A\) when \(l\le k\), or a uniform \(l\)-superset of \(A\) when \(l\ge k\). Denote the resulting density, after averaging over \(\mu\), by \(r_l^{\max}\). Define
\[
\widetilde r_l(a)=e^{\tau_l(a)L_l}r_l^{\max},
\qquad
\widetilde p_a(S)=\pi_l(a)u_l(S)\widetilde r_l(S,a).
\]

This is **not** an exact-clock assertion about \(r_l\). It is a distinct, specified surrogate whose approximation cost is proved.

### Uniform quantitative theorem

For \(1\le k\le n-1\), put
\[
q=\frac{\min(k,n-k)}n,\qquad
A_{n,k,c}^{\,2}
=\min\!\left\{1,\,
2(1+q^{-1})\frac{1-c}{1+c}\right\},
\]
and
\[
\varepsilon_{n,k,c}
=
n\,b\!\left(
\min\!\left\{\frac{A_{n,k,c}}{\sqrt n},\frac12\right\}
\right).
\]

For **every** homogeneous input law \(\mu\), every \(0<c<1\), and every legal \(a\),
\[
\boxed{
|H(p_a)-H(\widetilde p_a)|
\le \varepsilon_{n,k,c}
\le n\,b\!\left(\min\{n^{-1/2},1/2\}\right)
=O(\sqrt n\log n).
}
\]
The same bound holds separately for every conditional layer. Deterministic ranks \(k=0,n\) have zero approximation error.

In particular, for the **true contiguous half-density Fourier projections**, every even \(n\), and fixed \(c=19/20\),
\[
\boxed{
A_{n,n/2,19/20}^{\,2}=\frac2{13},
\qquad
\frac{|G_n(a)-\widetilde G_n(a)|}{n}
\le
b\!\left(\min\!\left\{\sqrt{\frac{2}{13n}},\frac12\right\}\right).
}
\]

### Why this controls all modes

The proof constructs a coupling of the entire output laws, with the same input \(A\) and the same output count \(l\).

The actual overlap distribution has a real-rooted generating polynomial. An elementary Rolle-theorem argument gives a representation of that **one-dimensional overlap** as a shifted sum of independent Bernoulli variables. This does not assert independence of the output sites.

The actual overlap variance is at most \(n/8\). The mean-matched BL overlap has variance at most
\[
\frac{1-\lambda_l^2}{2\gamma_l}\le\frac n8.
\]
Coupling the two overlaps and then using common random orderings within \(A\) and \(A^c\) gives
\[
\mathbb E\,d_H(Y,\widetilde Y)
\le A_{n,k,c}\sqrt n.
\]

Binary entropy continuity converts this full-law coupling into the entropy bound. The relevant adjacent-field inequality is Polyanskiy–Wu, Proposition 8, equation (57); the package also gives its elementary binary proof. [Original citation handle unavailable: locate and verify the named primary source.]

There is no harmonic cutoff, typical-layer cutoff, or inverse-small-atom estimate.

## 2. The mean clock has a proved acceleration payment

The polynomial argument yields the exact representation
\[
\lambda_l(w)=\sum_i\frac{\alpha_i}{1+\beta_iw},
\qquad
\alpha_i>0,\quad \sum_i\alpha_i=1,\quad \beta_i>\frac1c.
\]
It follows that the clock is strictly concave in \(a\), with the explicit bound
\[
\boxed{
-\tau_l''(a)\ge
\zeta_l(a):=
\frac{l(n-l)}n
\left[
\frac{2}{c+w}
+\frac{(1-c-2a)^2}{(c+w)^2}
\right]>0.
}
\]

Write
\[
J_l(r)=-\langle\log r,L_lr\rangle_{u_l},
\qquad
\mathcal C_l(r)=\mathcal B_l(r,\log r),
\qquad
s_l=\tau_l'.
\]
For the surrogate’s actual continuity velocity and covariant acceleration,
\[
\widetilde B_l=s_l^2\mathcal C_l(\widetilde r_l),
\qquad
\boxed{
\widetilde{\mathrm{acc}}_l
=\widetilde B_l-\tau_l''J_l(\widetilde r_l)
\ge \widetilde B_l+\zeta_lJ_l(\widetilde r_l).
}
\]
Consequently,
\[
\boxed{
\sum_l\pi_l\widetilde{\mathrm{acc}}_l
\ge
\sum_l\pi_l\widetilde B_l
+\sum_l\pi_l\zeta_lJ_l(\widetilde r_l).
}
\]

This is an **aggregate, dimension-explicit acceleration estimate for all modes of the surrogate**, not another rank-one calculation.

The normalized BL rates and curvature constant were checked against Erbar–Maas–Tetali, Theorem 4.1:
\[
\kappa_l=\frac{n+2}{2l(n-l)}.
\]
Its finite, irreducible, reversible and positive-density hypotheses hold on the interior slices. [Original citation handle unavailable: locate and verify the named primary source.] The identification of \(\mathcal B\) with the logarithmic-mean transport Hessian uses Erbar–Maas, Proposition 4.3. [Original citation handle unavailable: locate and verify the named primary source.]

The clock reverses after \(a=(1-c)/2\). The proof does **not** call \(s_lL_l\) a forward Markov generator in \(a\) on that half of the interval.

A further actual-path consequence is
\[
H(Y\mid M=l;a_t)
\ge
(1-t)H(Y\mid M=l;a_0)
+tH(Y\mid M=l;a_1)
-2\varepsilon_{n,k,c}.
\]
This is **sublinear conditional Jensen loss**, not exact finite-dimensional conditional concavity. It therefore does not assert the stronger claim ruled out in the prompt.

## 3. The actual residual, its response, and the complete payment

For the actual conditional density—not the surrogate—define
\[
\eta_l=r_l'-s_lL_lr_l,
\qquad
\boxed{
\eta_l'=r_l''-s_l'L_lr_l-s_lL_lr_l'.
}
\]
With slice indices suppressed, the exact formula is
\[
F''=2s^2\mathcal C(r)-s'J(r)+E_{\mathrm{res}},
\]
where
\[
\boxed{
E_{\mathrm{res}}
=
2s\left\langle\frac{(Lr)\eta}{r}\right\rangle
+\left\langle\frac{\eta^2}{r}\right\rangle
+s\langle\log r,L\eta\rangle
+\langle\log r,\eta'\rangle.
}
\]

Thus the residual Fisher square, Fisher cross term, and acceleration response all remain.

The proof defines both
\[
\|\eta\|_{F,r}^2=\left\langle\frac{\eta^2}{r}\right\rangle,
\qquad
\|\eta\|_{-1,r}^2=\langle\eta,A_r^\dagger\eta\rangle,
\]
and records the corresponding dual-norm bookkeeping inequality. **No adequate pointwise, dimension-uniform bound on all those norms is claimed.** The successful estimate is instead for the complete signed, integrated entropy replacement error.

Let \(\Delta_l=F_l-\widetilde F_l\). Then
\[
\boxed{
\begin{aligned}
\Xi:=\widetilde H''-H''
=\sum_l\Big\{&
\pi_l\big[
2s_l^2(\mathcal C_l-\widetilde{\mathcal C}_l)
-s_l'(J_l-\widetilde J_l)
+E_{\mathrm{res},l}
\big]\\
&+2\pi_l'\Delta_l'
+\pi_l''\Delta_l
\Big\}.
\end{aligned}
}
\]
Both layer derivatives are present. So are the changed heat-Bochner term and the residual response.

For the triangular Jensen kernel
\[
K(a)=
\begin{cases}
(1-t)(a-a_0),&a_0\le a\le a_t,\\
t(a_1-a),&a_t\le a\le a_1,
\end{cases}
\]
the new theorem proves
\[
\boxed{
\left|\int_{a_0}^{a_1}K(a)\Xi(a)\,da\right|
\le 2\varepsilon_{n,k,c}=o(n).
}
\]
More generally, for an interior compactly supported \(C^2\) test function,
\[
\left|\int\varphi(a)\,[H''-\widetilde H''](a)\,da\right|
\le
\varepsilon_{n,k,c}\int|\varphi''(a)|\,da.
\]

This is a proved payment for the **entire actual-to-surrogate budget**. It is not a bound on \(\int|\Xi|\), on \(E_{\mathrm{res}}\) alone, or on a pointwise Hessian. The value estimate is used through integration by parts, not differentiated.

## 4. The remaining full-entropy gap

The surrogate’s full formula is
\[
\widetilde H''
=
\Phi''
-\sum_l\left[
\pi_l\bigl(2s_l^2\widetilde{\mathcal C}_l-s_l'\widetilde J_l\bigr)
-2\pi_l's_l\widetilde J_l
+\pi_l''\widetilde F_l
\right].
\]

Its intrinsic and acceleration terms are favorable, but
\[
\boxed{
W_n(a)=
\sum_l\left[
-2\pi_l's_l\widetilde J_l
+\pi_l''\widetilde F_l
\right]
}
\]
still requires an input-sensitive aggregate estimate. **No sufficient Fourier/Plücker-specific payment for this term was obtained.**

This distinction is essential: the new theorem pays the difference between the actual and surrogate budgets, including their layer-weight differences. It does not pay the surrogate’s remaining layer budget itself.

For genuine \(P_{n,k_n}\), \(k_n=\lfloor n\rho+1/2\rfloor\), the supplied value bridge gives
\[
|H_n(a,c)-\widetilde G_n(a)|
\le
\varepsilon_{n,k_n,c}
+n\,b\!\left(\min\{cd_n/n,1/2\}\right)
=o(n).
\]
Thus the new approximation survives the true Toeplitz bridge, and its normalized entropy has the same limiting rate. No limiting differentiability is assumed. The unresolved step is a full Jensen estimate for that surrogate, with \(W_n\) retained.

## 5. Proof, certificates, diagnostics, and timing

**Analytic proofs completed:** the all-law coupling and high-contrast constant; the reciprocal-mixture clock representation; its acceleration bound; the complete integrated replacement payment; and the actual conditional Jensen-loss corollary. The accepted preceding-round identity, no-clock theorem and value bridge are inputs, not new results.

**Exact finite verification:** the genuine coupled \(P_{6,3}\) input was checked at
\[
(c,a)=(19/20,1/100),\quad(19/20,1/40),\quad(99/100,1/1000).
\]
Two full-channel derivative implementations agree in exact rational arithmetic. The residual and full layer identities are checked as rational/formal-log expressions. The checker also verifies the clock-response bounds and 819 integer polynomial coefficient identities. These are not target-sign certificates.

**Floating diagnostics:** six coupled Fourier cases and 61 growing radial-kernel cases through \(n=1024\) were checked. The maximum full-atom/layer residual was below \(2.6\times10^{-12}\); the residual-expansion error was below \(3.6\times10^{-15}\). The growing radial checks do not claim to evaluate growing Fourier configuration entropies.

Measured UTC interval for this round:
**2026-09-16 11:46:56.490270–12:15:25.760537**, totaling **28 minutes 29.270267 seconds**. The round ended with the complete new scoped proofs above under the completed-new-theorem exception; no 90-minute duration is claimed.

The ZIP contains all required Markdown files, scripts, frozen read-only evidence, dependency versions and a SHA-256 manifest. An extracted preflight archive passed replay, including semantic JSON comparison against a CRLF-transcoded copy. The final archive’s hashes and CRCs were verified. These are internal checks, not independent certification.

[The referenced ZIP was not recovered for this handoff.]
