# Extension to any fixed density and any strictly interior base shift

This is an author extension of `MESOSCOPIC_COMPENSATION.md`, not a claim of
sine entropy concavity. The central count band is **noise-adapted** unless
the base output density is `1/2`. That distinction is essential: this result
does not silently relabel a moving band as one fixed set of count layers.

## 1. Frozen statement

Fix `0<rho<1`, `0<c<1`, and `0<a_0<1-c`. Let

\[
 \gamma=\min\{a_0,1-a_0-c\}>0,\qquad
 m_0=a_0+c\rho,\qquad \mu=m_0-1/2.
\]

Take one interval `E_rho` of circle measure `rho`, set `p_R=F_R*1_E_rho`,
and use the genuine stationary symbol

\[
 f_{R,u,\delta}=\tfrac12+u(a_0+c p_R-\tfrac12+\delta),
 \qquad u\in[1/(R+1),1].
\]

The Fejer cutoff and the center's conditioning radius are both `R`. The
polynomial degree is at most `R`, and equals `R` whenever `sin(pi rho R)!=0`.
There is an unbounded such subsequence for every `0<rho<1`; along it the
literal degree is exactly aligned with the radius. The estimates hold for
all integer `R` tending to infinity, so they also hold on that subsequence.
Put
`C_R=[-R,R]\\{0}`, `M_R=sum_{C_R}Y_i`, and define the fixed-base standardized
count

\[
 X_R(u)=\frac{M_R-2R(1/2+u\mu)}{\sqrt R}.
 \tag{1.1}
\]

The centering is independent of the perturbation `delta`. Let `q_R` be the
complete conditional predictor at the center and let `phi` have the same
definition as in the companion note. For a bounded test `F`, set

\[
 A_{R,F}(\delta)=\int_{1/(R+1)}^1
   \mathbb E_\delta[\phi(q_R)F(X_R(u))]\,\frac{du}{u},
 \qquad \mu_R^\theta(F)=A_{R,F}(\theta/\sqrt R).
\]

Let `I_0(u)` now be the full production of the true, unregularized symbol
`1/2+u(a_0+c 1_Erho-1/2)`. Define

\[
 v_\rho(u)=\frac12-2u^2[\mu^2+c^2\rho(1-\rho)],
 \qquad v_{\rho,\min}=v_\rho(1)>0.
 \tag{1.2}
\]

The strict positivity follows alternatively by writing `v_rho(u)` as twice
the average Bernoulli variance of the two spectral values, both lying in
`[gamma,1-gamma]` at `u=1` and closer to `1/2` for smaller `u`.

### Theorem

Uniformly on every compact real `theta` set,

\[
 \mu_R^\theta(dx)\Rightarrow
 \int_0^1 I_0(u)\gamma_{v_\rho(u)}(x-2u\theta)\,\frac{du}{u}\,dx.
 \tag{1.3}
\]

The symmetrized endpoint measure minus the center has zero limiting total
mass, strictly negative limiting mass on `[-b,b]` for `b>0,theta!=0`, and
exactly opposite positive mass on its complement. The same explicit
martingale translation coupling as in the half-density theorem proves this
compensation.

For every bounded continuous `F`, and for indicators of finite intervals,

\[
 \frac{A_{R,F}''(0)}R\longrightarrow
 4\int_0^1u I_0(u)\int F(x)\gamma_{v_\rho(u)}''(x)dx\,du.
 \tag{1.4}
\]

Thus the **noise-adapted** band `|M_R-2R(1/2+u mu)|<=b sqrt R` and its
complement have curvatures `-R C_b+o(R)` and `+R C_b+o(R)`, where

\[
 C_b=8b\int_0^1u I_0(u)\gamma_{v_\rho(u)}(b)/v_\rho(u)\,du>0.
\]

In particular, for every strictly interior base shift as quantified above,

\[
 C_{1/2}>\frac{665}{768}
          \left(\frac{c\sin(\pi\rho)}{\pi}\right)^4.
 \tag{1.5}
\]

This inequality is a lower bound on the limiting constant. Convergence rates
and sufficiently-large-radius thresholds are not asserted to be uniform as
`a_0` approaches an endpoint or as `rho` or `c` approaches its boundary.

## 2. Exact modifications to the quantitative proof

The proof is not an appeal to continuity in density. All changes from the
half-density argument are specified here.

Set `epsilon=gamma/2`, `D=1-gamma`, `D_0=1-2gamma`. For
`R>=(2T/gamma)^2`, every real perturbation `|delta|<=T/sqrt R` has the same
strict strip `[epsilon,1-epsilon]`, and every conditional predictor satisfies
`|2q-1|<=uD`. Consequently the all-word production and Lipschitz constants
are `M_D=D atanh D` and `L_D=2(atanh D+D/(1-D^2))` as before. At the
unperturbed true symbol the bound is `I_0(u)<=M_{D_0}u^2`.

The exterior restriction `Q_R` of `T(p_R)` has trace `2R rho`. Its defect
still satisfies

\[
 V_R=\operatorname{Tr}Q_R(I-Q_R)
 \le\mathcal V_R=(2R+1)\eta_R+2\mathsf H_R/\pi^2+1/4,
\]

where `eta_R=min(1/2,(log(R+1)+1/2)/(R+1))`. The proof only uses the interval
Fejer `L^1` bound and `|p_hat_R(k)|<=1/(pi |k|)`, not half-density parity.
Removal of the center costs at most `rho(1-rho)<=1/4`.

A direct trace calculation at `delta=theta/sqrt R` gives

\[
 \mathbb E X_R(u)=2u\theta,
\]
\[
 \operatorname{Var}M_R
 =R v_\rho(u)+u^2c^2V_R
            -4u^2\mu\theta\sqrt R-2u^2\theta^2.
 \tag{2.1}
\]

Conditioning on `C_r` still changes the mean by at most `4r` and the variance
by at most `5r/2`; these finite-rank comparisons did not use the diagonal
value `1/2`. Hence the conditional Gaussian bound in the companion note is
replaced by

\[
 \mathcal B_{R,r}^{\rho,a_0}
 =\frac73R^{-1/6}+\frac{4r}{\sqrt R}
 +\frac{c^2\mathcal V_R+4|\mu|T\sqrt R+2T^2+(5/2)r}
        {R\sqrt{v_{\rho,\min}}}.
 \tag{2.2}
\]

All other steps use the same process at local radius `r`, followed by the
full-production stability estimate to the fixed true base symbol. With

\[
 E_n=\frac{c^2(\mathsf H_n+1)}{\pi^2\epsilon(1-\epsilon)n},
\]

the bounded-Lipschitz error is at most

\[
 \frac{L_D}{2\sqrt2}\sqrt{E_{r+1}}
 +\frac{M_D}{2}\mathcal B_{R,r}^{\rho,a_0}
 +E_{r+1}+2b(c\eta_R+T/\sqrt R)
 +\frac{M_{D_0}}{2(R+1)^2},
 \tag{2.3}
\]

provided the argument of `b` is at most `1/2`. Taking `r=floor(R^(1/3))`
gives `O_{rho,c,a_0,T}(R^(-1/6)sqrt(log R))`. This proves (1.3), including
the changed kernel, changed shift, local predictor, and noise tail. The
joint-test version of the companion theorem permits the noise-dependent
centering in (1.1).

## 3. Derivatives and the strict compensation constant

For complex `theta`, the complete-event eigenvalue separation and the
`2R`-word determinant domination are unchanged, with
`epsilon=gamma/2`. Set

\[
 L=1+c^2/(4\epsilon^2),\qquad D_1=1-\gamma/2.
\]

For `R>=(4LT/gamma)^2`, the Schur-resolvent comparison gives
`|2q(theta/sqrt R)-1|<=uD_1` on the whole `theta` disk. Thus

\[
 |\mu_R^\theta(F)|\le\tfrac12M_{D_1}\|F\|_\infty
                              e^{T^2/\epsilon^2}.
\]

The centering and the Borel test in (1.1) do not depend on complex `theta`.
The same normal-family uniqueness and Cauchy integral argument therefore
proves derivative convergence, including (1.4). This is a separate analytic
estimate, not differentiation of (2.3).

For completeness, the lower production bound is valid at any base output
mean. At noise `u`, let `p=1/2+u mu` and let the nearest-neighbor kernel
entry have squared magnitude
`t=u^2(c sin(pi rho)/pi)^2`. Conditioning only on that neighbor gives center
probabilities `p-t/p` and `p+t/(1-p)`, with weights `p` and `1-p`.
Their conditional-predictor variance is `t^2/[p(1-p)]`. Since `phi''>=8`
and `phi(p)>=0`, conditional Jensen with its quadratic remainder gives

\[
 I_0(u)\ge4t^2/[p(1-p)]
 \ge16u^4(c\sin(\pi\rho)/\pi)^4.
 \tag{3.1}
\]

For `1/2<=u<=3/4`, the quantity in brackets in (1.2) is at most `1/4`,
because it is the spectral average of `(a_0+c 1_Erho-1/2)^2`. Therefore
`7/32<=v_rho(u)<=1/2`. The same elementary Gaussian lower bound and integral
used in Section 7 of the companion note give (1.5).

At `rho=1/2,a_0=(1-c)/2`, `mu=0`, the band ceases to depend on noise and all
formulas reduce to the original theorem. Away from this centered situation,
the adaptation in (1.1) must be retained. Neither case signs the complete
subleading curvature or closes a fixed-chord entropy-rate Jensen inequality.
