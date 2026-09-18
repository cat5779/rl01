# S43 cycle 03 — A signed linear-scale envelope for the corrected-law response

**CORRECTED_LAW_ONLY.** Repository `cat5779/rl01`, branch
`research/sa-cycle03-20260918`, assignment `prompts/CYCLE03/S43.md`.

## 0. Result and status

**PROVED, in the scope of the derivation below:** the prescribed corrected-law
response at `c=19/20` is eventually strictly negative and has order `n`.
The result is a signed envelope, not a claim that `W_n/n` converges.

The proof does not assume S45's pending `O(n)` theorem. It uses the established
strong-Rayleigh preservation theorem for finite symmetric exclusion, stated
explicitly below, and proves the additional local-limit and transport estimates
needed here. The prior S43 review is context, not a substitute for any identity
used in this proof. This is a mathematical derivation, not an independent-review
verdict on another submission.

For a fixed `0<c<1`, put
\[
p=\frac{1+c}{2},\qquad q=\frac{1-c}{2},\qquad
b=pq=\frac{1-c^2}{4},\qquad z=(p/q)^2,\qquad\beta=\log z,
\]
\[
\rho_c=1-\frac{c^2\log c}{2b},\qquad
D_c=\frac12(\rho_c-1-\log\rho_c),\qquad
M_b=\frac{2e^{-1/2}}{\sqrt{2\pi}\,b},
\]
\[
A_c=\frac{16c^4}{b\pi^4},\qquad
L_c=\frac{c^4}{4b^2}+\frac cb\log\frac pq.
\]
All limits below are through even integers `n=2k`. Estimates are for fixed `c`;
no uniformity as `c` approaches zero or one is asserted.

### Main theorem

For the cyclic half-density Fourier-DPP corrected law with the exact coefficient
clock and actual count weights specified in Section 1,
\[
\boxed{
 -L_c-M_bD_c
 \ \le\ \liminf_{n\to\infty}\frac{W_n}{n}
 \ \le\ \limsup_{n\to\infty}\frac{W_n}{n}
 \ \le\ -A_c+M_bD_c.
}
\tag{0.1}
\]
The proof is valid for each fixed `0<c<1`; positivity of the upper-envelope
margin is asserted here specifically at `c=19/20`.

At that value,
\[
\begin{aligned}
\rho_c&\simeq1.949583552508, &D_c&\simeq0.140983882778,\\
A_c&\simeq5.488710044770, &M_bD_c&\simeq2.799095159908,\\
A_c-M_bD_c&\simeq2.689614884862,
&L_c+M_bD_c&\simeq488.308585220766.
\end{aligned}
\tag{0.2}
\]
The decimal evaluations are not inputs to the proof. Section 9 proves
`A_c-M_bD_c>0` using elementary inequalities. In particular, there are constants
`0<a<C<infinity` and an even `N`, depending only on `c=19/20`, such that
\[
-Cn\le W_n\le-an\qquad(n\ge N,\ n\text{ even}).
\tag{0.3}
\]

**INCOMPLETE:** an exact limit of `W_n/n`; the sign of `W_n+C_n`; any transfer to
true output; and the ultimate concavity of the true sine-Toeplitz
full-configuration Shannon entropy rate for every fixed `0<rho<1`, `0<c<1`, and
all `0<=a<=1-c`. No assertion here closes any of those targets.

The two new mechanisms are an exact **count-Stein curvature certificate** for
the auxiliary Gibbs law and an **averaged third-difference log-determinant
transport lemma**. The latter makes the evidence correction flat on the
`sqrt(n)` scale without differentiating an entropy approximation. The remaining
nonnegative output KL is paid by an explicit signed count-weight budget.

## 1. Exact model and conventions

Let `n=2k>=4` and
\[
U_{jr}=n^{-1/2}e^{2\pi i jr/n},\quad 0\le j<n,\quad0\le r<k,
\qquad P=UU^*.
\]
The latent `k`-set has law `nu(A)=det P_A`. Given `A`, for `2<=l<=k`, start at a
uniform `l`-subset of `A` and run the original-rate exclusion generator
\[
(G_lf)(S)=\sum_{i\in S,j\notin S}[f(S-i+j)-f(S)].
\]
Write its conditional channel as `T_l^H` when evaluated at the following time:
\[
Z_l=[t^l](1+t)^k(1+zt)^k,\quad
 a_j=[t^j](1+t)^{k-2}(1+zt)^{k-2},\quad
 \alpha_l=\frac{l(l-1)}{k(k-1)},
\]
\[
\theta_l=\frac{(z-1)^2a_{l-2}}{\alpha_lZ_l},\qquad
s_l=-\frac{\log\theta_l}{2(n-1)}.
\tag{1.1}
\]
Let `mu_l` be its marginal and `F_l=D(mu_l||u_l)`, with `u_l` uniform on the
`l`-slice. Higher layers are the prescribed complementary layers; at
`l=0,1,n-1,n`, use the frozen uniform-law convention. Thus `F_{n-l}=F_l` and the
four endpoint values are zero. No endpoint clock is invented.

For completeness, `0<theta_l<1`. With `f(t)=(1+t)(1+zt)`,
\[
\alpha_l Z_l=[t^{l-2}]f^{k-2}
 \left((f')^2+\frac{ff''}{k-1}\right).
\]
The bracket has nonnegative coefficients and constant coefficient
`(z+1)^2+2z/(k-1)>(z-1)^2`. This proves the strict upper bound.

The actual count generating function is
\[
\sum_l\pi_l(a,c)t^l
 =[1-a-c+(a+c)t]^k[1-a+at]^k.
\]
All layer laws are frozen at `a_*=q`. Let `B_m` be the actual sum of ordered
pair-deleted count probabilities, extend `B_m=0` outside `[0,n-2]`, and put
\[
w_l=B_{l-1}-B_{l-2},\qquad
\kappa_l=B_l-2B_{l-1}+B_{l-2}=\pi_l''(a_*,c).
\tag{1.2}
\]
Then
\[
W_n=\sum_{l=0}^n \kappa_lF_l
 =\sum_{m=0}^{n-2}B_m(F_{m+2}-2F_{m+1}+F_m)
 =-2\sum_{l=2}^k w_l(F_l-F_{l-1}).
\tag{1.3}
\]
The symbols `\kappa_l` are count-derivative coefficients. The separate
clock-acceleration quantity `C_n` in the assignment is not estimated here.

## 2. The actual signed count kernel, endpoints, and tails

Set
\[
\phi(t)=b+(1-2b)t+bt^2,
\qquad
\eta_k=\frac{k-1+2b}{2(2k-1)},
\qquad
\psi_k(t)=\eta_k+(1-2\eta_k)t+\eta_kt^2.
\]
Separating the ordered deleted pairs into the two same-type classes and the
mixed class gives exactly
\[
\sum_m\frac{B_m}{n(n-1)}t^m=\phi(t)^{k-2}\psi_k(t),
\qquad b\le\eta_k\le\frac14.
\tag{2.1}
\]
Indeed, if `A(t)=q+pt` and `E(t)=p+qt`, the unnormalized factor remaining after
`phi^(k-2)` is `k(k-1)(A^2+E^2)+2k^2 phi`.

Let `V_B=(n-4)b+2eta_k`. The distribution in (2.1) is a sum of `n-2` independent
Bernoulli variables, has mean `k-1`, and has variance `V_B`. Its centered
characteristic function is
\[
\chi_n(t)=(1-4b\sin^2(t/2))^{k-2}
          (1-4\eta_k\sin^2(t/2)).
\tag{2.2}
\]
For `|t|<=pi`,
\[
|\chi_n(t)|\le e^{-2V_B\sin^2(t/2)}
             \le e^{-2V_Bt^2/\pi^2},
\qquad V_B\ge(n-2)b.
\tag{2.3}
\]

Define
\[
\varphi_b(x)=\frac{e^{-x^2/(2b)}}{\sqrt{2\pi b}},
\qquad g_b(x)=-\varphi_b'(x)=\frac{x}{b}\varphi_b(x).
\]
Fourier inversion, the substitution `t=u/sqrt(n)`, and dominated convergence in
(2.3) give
\[
\frac{C_{k-\lfloor x\sqrt n\rfloor}}{\sqrt n}
 \longrightarrow\varphi_b''(x),\qquad
\frac{w_{k-\lfloor x\sqrt n\rfloor}}{n}
 \longrightarrow g_b(x).
\tag{2.4}
\]
These convergences are uniform on compact `x`-intervals. In fact the corresponding
lattice first- and second-difference Fourier errors are uniform over all lattice
indices: their absolute errors are bounded by an integral independent of the
Fourier phase. The multipliers become `iu` and `-u^2`, respectively; the
integrable envelopes are constant multiples of `|u| exp(-a u^2)` and
`u^2 exp(-a u^2)` for a fixed `a>0`.

### 2.1 Exact sign pattern and positive mass

Multiplying a finite real coefficient sequence by a positive linear polynomial
cannot increase its number of sign changes. To see this, make a positive
geometric rescaling so that the new coefficients are proportional to adjacent
averages of the old ones. They are samples of the piecewise-linear interpolation
between the old coefficients, which cannot acquire extra sign changes.

Both `phi` and `psi_k` are products of positive linear factors: for the latter,
the discriminant is `1-4eta_k>=0`. Therefore the coefficients of
`(1-t)^2 phi^(k-2) psi_k`, namely `\kappa_l/[n(n-1)]`, have at most two sign changes.
They are positive at both endpoints, sum to zero, and are symmetric about `k`.
Thus their sign pattern, ignoring zero coefficients, is exactly `+,-,+`.

With `D_m=B_m-B_{m-1}`, summing its positive and negative increments gives
\[
\sum_l(\kappa_l)_+=2\max_mD_m,
\qquad
\sum_l|\kappa_l|=4\max_mD_m.
\tag{2.5}
\]
The uniform first-difference limit in (2.4) yields
\[
\frac1n\sum_l(\kappa_l)_+
 \longrightarrow 2\max_{x\ge0}g_b(x)
 =\frac{2e^{-1/2}}{\sqrt{2\pi}\,b}=M_b,
\qquad
\frac1n\sum_l|\kappa_l|\longrightarrow2M_b.
\tag{2.6}
\]

### 2.2 A moment tail bound using the actual coefficients

Choose any fixed `K_0>sqrt(b)`. The local limit and the sign pattern imply that,
for all sufficiently large `n`, every negative `\kappa_l` lies within
`|l-k|<=K_0 sqrt(n)+2`.

On the other hand, exact summation by parts gives
\[
\sum_l \kappa_l(l-k)^4
 =\sum_m B_m\{12(m-k+1)^2+2\}
 =n(n-1)(12V_B+2).
\tag{2.7}
\]
Combining (2.5)--(2.7), and enlarging a constant to cover the finite exceptional
values of `n`, proves
\[
\sup_{n\ge4,\ n\ \mathrm{even}}
 \frac1n\sum_l|\kappa_l|
 \left(1+\left|\frac{l-k}{\sqrt n}\right|^4\right)<\infty.
\tag{2.8}
\]
In particular, for `K>=1`,
\[
\frac1n\sum_{|l-k|>K\sqrt n}|\kappa_l|
 \left(1+\frac{(l-k)^2}{n}\right)\le\frac{C_b}{K^2}.
\tag{2.9}
\]
This pays complementary layers, not just a fixed central layer. An additional
exponential bound is available directly from (2.1):
`B_{k-R-1}<=n(n-1) exp(-2R^2/(n-2))`.

### 2.3 The signed profile functional, including its endpoint

For any symmetric array `h_l`, set `G_{n,r}=h_k-h_{k-r}`. Since `sum \kappa_l=0`,
\[
\frac1n\sum_l\kappa_lh_l
 =-\frac2n\sum_{r=1}^k C_{k-r}G_{n,r}.
\tag{2.10}
\]
There is no missing central atom: `G_{n,0}=0` exactly. If these profiles converge
locally uniformly to `G(x)` and satisfy a uniform bound
`|G_{n,r}|<=C(1+r^2/n)`, (2.4) and (2.9) imply
\[
\boxed{
\frac1n\sum_l\kappa_lh_l\longrightarrow
 -2\int_0^\infty\varphi_b''(x)G(x)\,dx.
}
\tag{2.11}
\]
For example, `G(x)=alpha x^2` gives `-2alpha`, fixing the sign and normalization.
The theorem below does not assume that the corrected profile converges. It
identifies the Gibbs contribution differently and bounds the nonconvergent KL
contribution by (2.6).

## 3. Exact Bayesian transport to a determinantal comparison law

Use the same coefficient formula for `Z_l` on all `0<=l<=n` in the
auxiliary comparison; this introduces no additional corrected-law clocks.
Introduce only as a comparison channel
\[
T_l^G(S\mid A)=\frac{z^{|A\cap S|}}{Z_l},\qquad |S|=l.
\]
Let
\[
\Lambda=I+(z-1)P,\qquad\ell(S)=\log\det\Lambda_S.
\]
Cauchy--Binet gives
\[
\mathbb E_\nu z^{|A\cap S|}=\det\Lambda_S,
\quad
\gamma_l(S)=\frac{\det\Lambda_S}{Z_l},
\quad
\nu^G(A\mid S)=\frac{\nu(A)z^{|A\cap S|}}{\det\Lambda_S}.
\tag{3.1}
\]
Write `mathscr F_l=D(gamma_l||u_l)` and
\[
U_l=D(\mu_l\Vert\gamma_l),\qquad
v_l=\mathbb E_H\ell(S)-\mathbb E_G\ell(S).
\]
The exact output ledger is
\[
\boxed{F_l=\mathscr F_l+U_l+v_l.}
\tag{3.2}
\]
Conditional on `A`, both channels are uniform within overlap orbits. If
`R=|S intersect A^c|`, denote the heat and Gibbs overlap laws by `p_l^H,q_l^G`.
Then
\[
q_l^G(r)=\frac{\binom kr\binom k{l-r}z^{l-r}}{Z_l},
\]
\[
D(p_l^H\Vert q_l^G)
 =D(\nu T_l^H\Vert\nu T_l^G)
 =U_l+\mathbb E_{\mu_l}
 D(\nu^H(\cdot\mid S)\Vert\nu^G(\cdot\mid S)).
\tag{3.3}
\]
In particular,
\[
0\le U_l\le D(p_l^H\Vert q_l^G).
\tag{3.4}
\]
No sign is asserted for a difference `U_l-U_{l-1}`. The layer-clock mismatch is
paid below, not removed by a data-processing assertion.

The Fourier identities
\[
DPD^*=I-P,\quad D_{jj}=(-1)^j,\quad \nu(A^c)=\nu(A),
\]
and Jacobi's complementary-minor formula imply
\[
\ell(S)=\beta(|S|-k)+\ell(S^c).
\tag{3.5}
\]
Thus `mathscr F_l,U_l,v_l` extend symmetrically across `k`. At the four endpoint
layers their output ledgers are zero, because both marginals are uniform and
`ell` is constant on each of these layers.

## 4. A sharp radial KL budget at the exact clock

Fix `c` and choose a sufficiently small `eta>0`, for example a smaller positive
constant than `q/4`. Throughout this section all uniform macro-layer assertions
refer to `(1-eta)k<=l<=k`. Constants may depend on `c,eta`, never on `n,l`.

### 4.1 Gibbs overlap estimates

Let `X=l-R`, `m_l=E_G X`, and `sigma_l^2=Var_G X`. A mode is within two of the
root `x_l^*` of
\[
z(k-u)(l-u)=u(k-l+u).
\tag{4.1}
\]
Indeed, the adjacent-probability ratio is
\[
\frac{\Pr_G(X=j+1)}{\Pr_G(X=j)}
 =\frac{z(k-j)(l-j)}{(j+1)(k-l+j+1)}.
\tag{4.2}
\]
The polynomial on the left minus right of (4.1) has derivative at most `-2k`
on `[0,l]`; the two mode inequalities prove the stated distance bound.

Writing `lambda=l/k` and `A_z=(z+1)/(z-1)`, the root is
\[
x_l^*=\frac k2\left\{\lambda+A_z-
 \sqrt{A_z^2-1+(1-\lambda)^2}\right\}.
\tag{4.3}
\]
At `l=k`, the bracket's contrast is `c`, and
`sqrt(A_z^2-1)=2b/c`. Consequently
\[
\left|x_{k-r}^*-\left(pk-\frac r2\right)\right|
 \le\frac{c r^2}{8bk}.
\tag{4.4}
\]
All four selected/unselected population counts at the mode are a positive
fraction of `n` in the specified macro band.

Here are details sufficient for the uniform local limits used below. Successive
log-ratios in (4.2) decrease by at least a constant times `1/n` over the whole
support, and their changes are `O(1/n)` in the fixed interior region. Summing
these inequalities from a mode gives
\[
q_l^G(r)\le\frac C{\sqrt n}
 \exp\left(-a\frac{(r-r_l^*)^2}{n}\right),
\qquad q_l^G(r_l^*)\asymp n^{-1/2}.
\tag{4.5}
\]
For the normalization statements, the upper bound on the ratios gives
`sum q(r)/q(r*)<=C sqrt(n)`; their local lower bound gives the reverse inequality.
Thus (4.5) follows without assuming a local limit theorem.

In particular all fixed centered absolute moments of order `j` are
`O(n^(j/2))`. Also, with
`B(u)=z(k-u)(l-u)-u(k-l+u)`, the ratio identity gives `E B(X)=0`, whence
\[
B(m_l)=-(z-1)\sigma_l^2,
\qquad m_l-x_l^*=O(1).
\tag{4.6}
\]
Taylor expansion of the logarithm of the binomial weights, with (4.5) controlling
the complement, now proves a uniform Gaussian local limit. More explicitly, for
`l/k` in a compact subinterval of the macro band, the exponent is
`k[H(t)+H(l/k-t)+beta t]`, with the sign of `beta` changed when using `R`.
At its stationary point its second derivative is
\[
-\frac1{t(1-t)}-\frac1{(l/k-t)(1-l/k+t)}.
\]
It is bounded away from zero, and all higher derivatives are bounded locally.
Taylor expansion on `|r-r_l^*|<=K sqrt(n)` gives the Gaussian ratio uniformly;
(4.5) supplies normalization and moment convergence. Therefore the variance is
uniformly comparable to `n`, and for every fixed finite `K`, uniformly for
`0<=k-l<=K sqrt(n)`,
\[
\frac{\sigma_l^2}{n}\longrightarrow\frac b4,
\tag{4.7}
\]
\[
-\log q_l^G(r)=\frac12\log(2\pi n b/4)
 +\frac{(r-\mathbb E_GR)^2}{2n(b/4)}+o_K(1)
\tag{4.8}
\]
on every fixed standardized overlap window. We will also use the global bound
\[
\left|-\log q_l^G(r)-\frac12\log n\right|
 \le C\left(1+\frac{(r-\mathbb E_GR)^2}{n}\right).
\tag{4.9}
\]
For (4.9), sum the local log-ratio bounds within a fixed interior neighborhood.
Outside it, every Gibbs weight is at least `exp(-C n)`, and the squared-distance
term is at least a constant times `n`. The lower bound follows from (4.5).

### 4.2 Exact coefficient matching and heat moments

Set `xi_l=(2m_l-l)/l`. The coefficient clock satisfies the exact identity
\[
\boxed{
\theta_l=\xi_l^2+
\frac{4(n-1)\sigma_l^2-l(n-l)(1-\xi_l^2)}{nl(l-1)}.
}
\tag{4.10}
\]
One direct derivation tests
`(1_{i_1 in S}-1_{j_1 in S})(1_{i_2 in S}-1_{j_2 in S})`, with two distinct
`i`'s in `A` and two distinct `j`'s outside it. Its Gibbs expectation is both
`(z-1)^2 a_{l-2}/Z_l` and
\[
\frac{\mathbb E[X(X-1)+(l-X)(l-X-1)]}{k(k-1)}
 -\frac{2\mathbb E[X(l-X)]}{k^2}.
\]
Divide by `alpha_l` and substitute the mean and variance to obtain (4.10).

The heat overlap has birth and death rates
\[
\lambda_r=(l-r)(k-r),\qquad\mu_r=r(k-l+r),\qquad R(0)=0.
\]
Its drift is `kl-nr`. The first two moment equations give, exactly,
\[
\mathbb E_HR=\frac l2(1-e^{-ns}),
\tag{4.11}
\]
\[
\operatorname{Var}_H R=
\frac{l(n-l)}{4(n-1)}(1-e^{-2(n-1)s})
+\frac{l^2}{4}e^{-2(n-1)s}(1-e^{-2s}).
\tag{4.12}
\]
For example, the variance satisfies
`V'=-2(n-1)V+l(n-l)/2+(l^2/2)e^{-2ns}`, which integrates to (4.12).

In the macro band, `xi_l` stays in a compact subset of `(0,1)`. Equations
(4.10)--(4.12), with `e^{-ns_l}=theta_l^(n/[2(n-1)])`, imply
\[
|\mathbb E_HR-\mathbb E_GR|\le C,
\qquad \operatorname{Var}_H R\asymp n.
\tag{4.13}
\]
On each fixed central `sqrt(n)` window, the leading terms in the numerator of
(4.10) cancel by (4.7), so `n(theta_l-xi_l^2)->0`, uniformly. Expanding the exact
power of `theta_l`, not an assumed half-step clock, gives
\[
\mathbb E_HR-\mathbb E_GR\longrightarrow
\delta_c=-\frac{c\log c}{4},
\tag{4.14}
\]
\[
\frac{\operatorname{Var}_H R}{n}\longrightarrow
v_H=\frac b4-\frac{c^2\log c}{8},
\qquad v_G=\frac b4.
\tag{4.15}
\]

### 4.3 Why the heat overlap is Poisson-binomial

The external theorem used here is Borcea--Branden--Liggett's finite symmetric
exclusion preservation theorem: a law with real-stable multiaffine generating
polynomial retains that property under a finite symmetric exclusion semigroup
(Proposition 5.1 and Theorem 5.2 of *Negative dependence and the geometry of
polynomials*, arXiv:0707.2340).

Its hypotheses apply exactly. The conditional initial generating polynomial is
`e_l((x_i)_{i in A})/binom(k,l)`, which is real stable. The generator is
`sum_{i<j}(tau_ij-I)` with nonnegative symmetric rates. Each two-site semigroup
is a partial symmetrization; the finite Trotter product is the stated
semigroup. Specialize the evolved polynomial to `x_i=1` on `A` and `x_i=t`
outside `A`. Stability under real specialization and diagonalization gives a
univariate real-rooted probability polynomial with nonnegative coefficients.
Its roots are nonpositive, so it factors into Bernoulli probability polynomials.
Thus `R` is exactly a sum of at most `n` independent Bernoulli variables.

For clarity, stability of `e_l` follows by taking a coefficient in the stable
polynomial `prod_i(t+x_i)`: differentiate in `t`, then specialize `t=0`.
These operations preserve real stability by the elementary differentiation and
real-specialization closure properties. Degenerate Bernoulli factors are
allowed. This argument applies to the conditional heat law, not to an asserted
strong-Rayleigh property of the latent heat mixture.

### 4.4 Entropy local limit and the explicit KL constant

We record the entropy estimate with its tail justification. If `Y_n` is a sum
of at most `n` independent Bernoulli variables and its variance `V_n>=a n` for
a fixed `a>0`, then, uniformly over such arrays,
\[
H(Y_n)=\frac12\log(2\pi e V_n)+o(1).
\tag{4.16}
\]
To prove this, its centered characteristic function satisfies
`|chi(t)|<=exp(-2V_n sin^2(t/2))`. At `t=u/sqrt(V_n)`, expansion of the logarithm
has remainder `O(|u|^3/sqrt(n))` on bounded `u`-intervals. Fourier inversion and
the same Gaussian domination as in (2.3) give the uniform lattice local CLT
and `max_j Pr(Y_n=j)<=C/sqrt(V_n)`.

Here is the entropy-tail step, which is necessary in addition to that local
CLT. Let `r_j` be the normalized discrete Gaussian proportional to
`exp(-(j-EY_n)^2/(2V_n))`. For a tail set `T`, write `P_T=sum_T p_j` and
`R_T=sum_T r_j`. Log-sum gives
\[
\sum_Tp_j\log(r_j/p_j)\le P_T\log(R_T/P_T)\le R_T/e.
\]
It follows that the upper tail of `H(Y_n)-(1/2)log V_n` is bounded by
\[
CP_T+\frac{\mathbb E[(Y_n-\mathbb EY_n)^2;T]}{2V_n}+R_T/e.
\]
The lower tail is bounded below by `-C P_T` using the maximum-mass estimate.
Hoeffding's bound and integration of its tail control the second moment
uniformly when `T={|Y_n-EY_n|>K sqrt(V_n)}`. Letting `K` tend to infinity proves
uniform integrability and hence (4.16).

Apply (4.16) to the heat overlap. Equations (4.8)--(4.9), (4.13), and its
Poisson-binomial concentration similarly justify integrating the Gibbs
log-mass expansion. Therefore, for every finite `K`,
\[
\boxed{
\sup_{0\le k-l\le K\sqrt n}
\left|D(p_l^H\Vert q_l^G)-D_c\right|\longrightarrow0,
\qquad
D_c=\tfrac12(v_H/v_G-1-\log(v_H/v_G)).
}
\tag{4.17}
\]
The squared mean difference is `O(1)` and so vanishes after division by `n`.
This explains why it does not appear in `D_c`.

In the whole macro band the same argument, without taking a limit, gives
\[
D(p_l^H\Vert q_l^G)\le C.
\tag{4.18}
\]
Indeed, the maximum-mass estimate gives `H(p_l^H)>=(1/2)log n-C`, and (4.9),
(4.13) give cross-entropy at most `(1/2)log n+C`. No pending S45 conclusion is
required for (4.17) or (4.18).

## 5. A third-difference determinant transport lemma

This is the additional regularity that an `O(1)` KL bound alone does not give.

### 5.1 Matrix statement

Let `Lambda` be any Hermitian matrix with `I<=Lambda<=zI`, and set
`ell(T)=log det Lambda_T`. For distinct sites outside `T`, let `delta_ij ell(T)`
and `delta_ijk ell(T)` denote their second and third inclusion-exclusion
differences.

If `M` is the Schur complement after `T`, then `I<=M<=zI`. Normalize it by its
diagonal to obtain `R_ij=M_ij/sqrt(M_ii M_jj)`. Then
`z^(-1)I<=R<=zI`, `R_ii=1`, and
\[
\delta_{ij}\ell(T)=\log(1-|R_{ij}|^2),
\qquad
\sum_{j\ne i}|\delta_{ij}\ell(T)|\le C_z.
\tag{5.1}
\]
The latter follows from the lower bound on two-site determinants and
`sum_j |R_ij|^2<=z^2`.

The stronger statement needed here is: for any two subsets `J,K` of remaining
sites and every remaining `i`,
\[
\boxed{
\left|\sum_{\substack{j\in J,k\in K\\i,j,k\ \mathrm{distinct}}}
\delta_{ijk}\ell(T)\right|\le C_z.
}
\tag{5.2}
\]
This is a **signed** double-row bound, not a bound on the sum of the absolute
values of all triple differences.

Proof: put `a=R_ij`, `d=R_ik`, `e=R_jk` and
`A=|a|^2`, `B=|d|^2`, `C=|e|^2`. The exact three-site formula is
\[
\delta_{ijk}\ell(T)=
\log(1-A-B-C+2\Re(ae\bar d))
-\log(1-A)-\log(1-B)-\log(1-C).
\]
The determinants and products appearing here are bounded below by positive
constants depending only on `z`. Subtracting
`(1-A)(1-B)(1-C)` inside the logarithm and applying Taylor's formula gives
\[
\delta_{ijk}\ell(T)=2\Re(R_{ij}R_{jk}R_{ki})+E_{ijk},
\]
\[
|E_{ijk}|\le C_z
\bigl(|R_{ij}|^2|R_{ik}|^2+
      |R_{ij}|^2|R_{jk}|^2+
      |R_{ik}|^2|R_{jk}|^2\bigr).
\tag{5.3}
\]
Here is an explicit control of the Taylor remainder. The determinant minus the
product equals `2 Re(ae conj(d))-(AB+AC+BC)+ABC`. Its square is bounded by a
constant times `AB+AC+BC`; also
`sqrt(ABC)(A+B+C)<=AB+AC+BC`. These bounds, and the positive lower bounds on the
logarithm's arguments, prove (5.3).

The signed sum of the leading triangles is a masked matrix product
`R_{i,*} Pi_J R Pi_K R_{*,i}`, bounded by the operator norm of `R` and two row
Euclidean norms. Removing repeated indices costs only a bounded amount. Each
of the three absolute remainder sums in (5.3) is bounded by two row-square
bounds. This proves (5.2).

### 5.2 Population-averaged finite differences

For fixed `A`, average `ell(S)` over a uniform choice of `h` sites in `A` and
`r` sites outside it, then average over `A~nu`; call the result `a_n(h,r)`.
Uniform subset extension gives exact identities expressing each mixed finite
difference of `a_n` as the corresponding averaged `delta ell`.

If the relevant selected and unselected population sizes are at least
`epsilon n`, (5.1)--(5.2) imply
\[
|\Delta a_n|\le\beta,
\qquad |\Delta^2 a_n|\le C_{z,\epsilon}/n,
\qquad |\Delta^3 a_n|\le C_{z,\epsilon}/n^2,
\tag{5.4}
\]
for every pure or mixed coordinate finite difference of the indicated order.
For the third bound, sum (5.2) first over the first chosen site. The numerator
is `O(n)` and the number of ordered triples is `Theta(n^3)`. This remains true
when two or all three sites come from the same population; the distinctness
restriction is already included in (5.2).

Let `f_{n,l}(r)=a_n(l-r,r)`. Its first differences are globally bounded by
`beta`; in a fixed interior region its second and third differences satisfy
`O(1/n)` and `O(1/n^2)`. These assertions follow by expanding the directional
finite differences in the two coordinate shifts. The same mixed-third bound
shows that its second difference changes by `O(d/n^2)` if its population base
point moves by lattice distance `d`.

### 5.3 The evidence correction is flat on the central scale

Choose an integer `j_l` nearest `E_G R`. Discrete Taylor summation gives
\[
f_{n,l}(j_l+t)=f_{n,l}(j_l)
+t\Delta f_{n,l}(j_l)
+\tfrac12t(t-1)\Delta^2f_{n,l}(j_l)
+O\left(\frac{|t|^3+|t|+1}{n^2}\right)
\tag{5.5}
\]
while the points remain in the fixed interior region. Outside it, the global
Lipschitz bound and exponential overlap tails make the expected error
negligible. All centered third absolute moments are `O(n^(3/2))`, by (4.5) and
Poisson-binomial concentration.

Subtracting heat and Gibbs expectations in (5.5) yields, uniformly on each
fixed central `sqrt(n)` layer window,
\[
v_l=(\mathbb E_HR-\mathbb E_GR)\Delta f_{n,l}(j_l)
+\frac12(\operatorname{Var}_H R-\operatorname{Var}_G R)
            \Delta^2f_{n,l}(j_l)+o(1).
\tag{5.6}
\]
Terms from the bounded displacement of either mean from `j_l` contribute only
`O(1/n)`.

Let
\[
A_n=\Delta f_{n,k}(j_k),\qquad
B_n=n\Delta^2f_{n,k}(j_k).
\]
Both sequences are bounded; neither is assumed to converge. Equations (4.4),
(4.6), and (5.4) show that when `0<=k-l<=K sqrt(n)`, the first derivative in
(5.6) differs from `A_n` by `O_K(n^(-1/2))`, and `n` times the second derivative
differs from `B_n` by `O_K(n^(-1/2))`. Combining with (4.14)--(4.15),
\[
v_l=\delta_c A_n+
\frac12\left(-\frac{c^2\log c}{8}\right)B_n+o_K(1).
\]
Consequently,
\[
\boxed{
\sup_{0\le k-l\le K\sqrt n}|v_l-v_k|\longrightarrow0
\quad\text{for every finite }K.
}
\tag{5.7}
\]
A second-order version of the same argument, using (4.13), gives `|v_l|<=C`
throughout the macro band.

Globally `|v_l|<=n beta`; combined with the macro bound this gives
`|v_l-v_k|<=C(1+(l-k)^2/n)` for all layers. Therefore the actual-coefficient
tail estimate (2.9) and (5.7) prove
\[
\boxed{\frac1n\sum_l\kappa_lv_l\longrightarrow0.}
\tag{5.8}
\]
This is the paid evidence commutator. It is not inferred from a static entropy
approximation or from the size of the KL divergence.

## 6. Gibbs layer regularity and an exact count/field conversion

### 6.1 The modest profile bound needed for the conversion

The count distribution at the midpoint is `pi_l=[t^l]phi(t)^k`, and
\[
\pi_l=b^kz^{-l/2}Z_l.
\tag{6.1}
\]
For a sum of the corresponding `n` Bernoulli variables, exponential tilting to
an integer mean `l` in the macro band keeps all Bernoulli parameters in a fixed
compact subset of `(0,1)`. The Fourier local limit proved in Section 4, now
applied to the tilted array at its mean, puts its point mass between
`c/sqrt(n)` and `C/sqrt(n)`, uniformly. The tilt's rate function has second
derivative `1/Var_t N=O(1/n)`. Hence
\[
|\log\pi_{k-r}-\log\pi_k|\le C(1+r^2/n).
\tag{6.2}
\]
Also `|log binom(n,k-r)-log binom(n,k)|<=C r^2/n` in the same band, by summing
adjacent binomial ratios.

For the population average define
`a_n^circ(h,r)=a_n(h,r)-beta(h+r)/2`. Complementation and interchange of the
latent populations give
\[
a_n^\circ(h,r)=a_n^\circ(k-r,k-h).
\tag{6.3}
\]
Choose integers `h_0+r_0=k` with `h_0` nearest `pk`. The sequence
`a_n^circ(h_0+t,r_0+t)` is even in `t` and has second difference `O(1/n)`.
Its displacement from its value at zero is therefore `O(t^2/n)`: evenness
bounds the first increment, and summation bounds all the others.

Replacing the Gibbs overlap by its mean costs `O(1)`, by the second-difference
bound and variance `O(n)`. Equations (4.4), (4.6) displace that mean from
`(pk-r/2,qk-r/2)` by `O(1+r^2/n)`. The globally bounded first differences pay
this displacement, and one coordinate step pays odd `r`. Finally,
\[
\mathscr F_l=\mathbb E_Ga_n^\circ(X,l-X)
 +k\log b+\log\binom nl-\log\pi_l.
\]
Together with (6.2), this proves
\[
|\mathscr F_{k-r}-\mathscr F_k|\le C(1+r^2/n)
\tag{6.4}
\]
in the macro band. Outside it, `0<=mathscr F_l<=n log 2` extends the same
quadratic envelope after enlarging `C`.

### 6.2 An exact derivative identity for the counts

Let `dot pi_l` denote differentiation of the balanced count law with respect
to `c`, so the high and low Bernoulli parameters change with velocities
`1/2` and `-1/2`. This derivative acts on counts only. Direct differentiation
of their product law gives
\[
\boxed{
\pi_l''(a_*,c)=
\left(\frac{(l-k)^2}{b^2}-\frac nb\right)\pi_l
+\frac{2c}{b}\dot\pi_l.
}
\tag{6.5}
\]
For example, the first `a`-score is `(N-k)/b`; the remaining term in its second
derivative is `(2c/b)` times the balanced `c`-score.

The latter full Bernoulli score has variance `n/(4b)`. Conditioning on `N`
cannot increase its variance, so by (6.4) and the count's fourth-moment bound,
\[
\left|\sum_l\dot\pi_l\mathscr F_l\right|
=\left|\sum_l\dot\pi_l(\mathscr F_l-\mathscr F_k)\right|
\le \sqrt{n/(4b)}
 \left[\mathbb E_\pi(\mathscr F_N-\mathscr F_k)^2\right]^{1/2}
=O(\sqrt n)=o(n).
\tag{6.6}
\]

### 6.3 The count-only field correction is `o(n)`

Form the auxiliary full Gibbs law and its natural count tilt:
\[
Q(S)=\pi_{|S|}\gamma_{|S|}(S)
 =b^kz^{-|S|/2}\det\Lambda_S,
\qquad
Q_t(S)=\frac{e^{t(|S|-k)}Q(S)}{\mathbb E_Qe^{t(N-k)}}.
\tag{6.7}
\]
Set `m_t=E_{Q_t}N/n` and
\[
\mathcal D_n(t)=D(Q_t\Vert\operatorname{Ber}(m_t)^{\otimes n}).
\]
The conditional law given `N=l` is `gamma_l` for every `t`. Consequently
\[
\mathcal D_n(t)=\mathbb E_{\pi_t}\mathscr F_N
+D(\pi_t\Vert\operatorname{Bin}(n,m_t)).
\tag{6.8}
\]
Put `X=N-k`. At zero, `E X=0`, `E X^2=nb`, and `E X^3=0`. Differentiating the
finite count expressions exactly gives
\[
\left.\frac{d^2}{dt^2}D(\pi_t\Vert\operatorname{Bin}(n,m_t))\right|_{t=0}
=\operatorname{Cov}\left(X^2,
 \log\frac{\pi_N}{\operatorname{Bin}(n,1/2)(N)}\right)+nbc^2.
\tag{6.9}
\]
We now estimate this already-exact expression, not a derivative of a static
asymptotic entropy formula.

The ordinary and tilted count local limits give, uniformly on bounded
`y=(l-k)/sqrt(n)` intervals,
\[
\log\frac{\pi_l}{\operatorname{Bin}(n,1/2)(l)}
=-\frac12\log(4b)+\left(2-\frac1{2b}\right)y^2+o(1).
\tag{6.10}
\]
In a macro band the absolute difference from its central value is bounded by
`C(1+y^2)`, using the same tilting proof as (6.2). Outside the band it is `O(n)`,
while the count probability is exponentially small. Hoeffding's bound therefore
justifies uniform integrability after multiplication by `y^2`. Since
`X/sqrt(n)` converges to `Normal(0,b)` with its moments, (6.9) divided by `n`
converges to
\[
\left(2-\frac1{2b}\right)2b^2+bc^2=0.
\tag{6.11}
\]
Combining (6.5)--(6.11),
\[
\boxed{
W_n^G:=\sum_l \kappa_l\mathscr F_l
=\frac{\mathcal D_n''(0)}{b^2}+o(n).
}
\tag{6.12}
\]
This conversion pays the difference between the actual `a`-count derivative and
the convenient natural-field derivative.

## 7. A count-Stein signed curvature certificate

This mechanism is not restricted to DPPs. Suppose a latent configuration has
exactly `k=n/2` occupied sites and, conditionally on it, independent output bits
have success probabilities `p` on occupied and `q` on unoccupied sites. Write
`Q` for the output. Then for every real function `f` on the Boolean cube,
\[
\boxed{\mathbb E_Q[(N-k)f]=b\sum_i\mathbb E_Q\partial_i f,}
\qquad
\partial_i f=f(Y_{-i},1)-f(Y_{-i},0).
\tag{7.1}
\]
This is conditional Bernoulli integration by parts: all conditional variances
are `b`, and the conditional sum of the means is exactly `k`.

The law (6.7) has this representation by (3.1). It is also log-submodular,
since it is an `L`-ensemble and (5.1) is nonpositive. Let
\[
r_i=Q(Y_i=1\mid Y_{-i}),\quad
h_i=\log\frac{r_i}{1-r_i},\quad x_i=2r_i-1.
\]
Then `q<=r_i<=p`, and `partial_j r_i<=0` for `j!=i`.

Apply (7.1) twice, using the exact Boolean product identity
`partial_i[(N-k)f]=(N-k)partial_i f+f(Y^i)`. If
`mathcal L f=sum_i[f(Y^i)-f(Y)]`, this gives
\[
\operatorname{Cov}((N-k)^2,f)
=b^2\sum_{i\ne j}\mathbb E\partial_{ij}f+b\mathbb E\mathcal Lf.
\tag{7.2}
\]
For `f=log Q`,
\[
\mathbb E\mathcal L\log Q=-\sum_i\mathbb E[x_i h_i].
\]
Differentiating `mathcal D_n(t)=n H_Ber(m_t)-H(Q_t)` exactly at zero yields
\[
\boxed{
\mathcal D_n''(0)=
b^2\sum_{i\ne j}\mathbb E\partial_jh_i
-b\sum_i\mathbb E[x_i h_i]+nbc^2.
}
\tag{7.3}
\]
Let `v_i=E[r_i(1-r_i)]`. Another application of (7.1) gives
\[
b\sum_{j\ne i}\mathbb E\partial_jr_i
=\operatorname{Cov}(N,r_i)=b-v_i.
\tag{7.4}
\]
For the last equality, `Cov(N,Y_i)=b`, and replacing `Y_i` by its conditional
mean removes exactly `v_i` from that covariance.

On `[q,p]`, the derivative of the logit is between `4` and `1/b`. Since the
increments of `r_i` are nonpositive,
\[
\frac1b\partial_jr_i\le\partial_jh_i\le4\partial_jr_i.
\tag{7.5}
\]
Using the upper inequality, (7.3)--(7.4), and `4b+c^2=1`,
\[
\mathcal D_n''(0)
\le b\sum_i\mathbb E[x_i^2-x_i h_i]
\le-b\sum_i\mathbb E x_i^2.
\tag{7.6}
\]
The last inequality is the elementary identity/inequality
`x log((1+x)/(1-x))>=2x^2`, for `|x|<1`.

For the lower bound, use the other side of (7.5), `v_i<=1/4`, and
`x_i h_i<=c log(p/q)`. This gives
\[
\mathcal D_n''(0)\ge
-n\left(\frac{c^4}{4}+bc\log\frac pq\right).
\tag{7.7}
\]

### 7.1 Strictness from the actual Fourier correlation

The kernel of `Q` is `K=qI+cP`, so `E Y_i=1/2` and, for `i!=j`,
\[
\operatorname{Cov}(Y_i,Y_j)=-c^2|P_{ij}|^2.
\]
This also follows directly by expanding the two-site determinant; no entropy
approximation is involved. For neighboring cyclic sites,
\[
|P_{i,i+1}|=\frac1{n\sin(\pi/n)}.
\]
Since `Y_j` is measurable with respect to `Y_{-i}`,
\[
\mathbb E x_i^2=4\operatorname{Var}(r_i)
\ge16\operatorname{Cov}(Y_i,Y_j)^2
=\frac{16c^4}{n^4\sin^4(\pi/n)}.
\tag{7.8}
\]
Equations (7.6)--(7.8) and (6.12) prove
\[
\boxed{
-L_c\le\liminf\frac{W_n^G}{n}
\le\limsup\frac{W_n^G}{n}\le-A_c.
}
\tag{7.9}
\]
This is a genuine signed susceptibility estimate for the auxiliary law, not a
renaming of an unknown layer difference.

## 8. Paying the output-KL correction against every actual weight

By (3.4), (4.17)--(4.18),
\[
0\le U_l\le D_c+o_K(1)
\quad\text{uniformly for }|l-k|\le K\sqrt n,
\qquad U_l\le C\quad\text{in the macro band}.
\]
Globally, `gamma_l(S)>=exp(-C n)` follows from
`det Lambda_S>=1` and `Z_l<=2^n z^n`, so `U_l<=C n`.
Consequently `U_l<=C(1+(l-k)^2/n)` for all layers, after enlarging `C`.

On a fixed central window, use nonnegativity of `U_l` to bound the positive
coefficient contribution by `(D_c+o_K(1)) sum(\kappa_l)_+`; similarly bound its
negative contribution. The complement is uniformly `O(K^(-2))` by (2.9).
First let `n` tend to infinity and then let `K` tend to infinity. Equation (2.6)
proves
\[
\boxed{
-M_bD_c\le\liminf\frac1n\sum_l\kappa_lU_l
\le\limsup\frac1n\sum_l\kappa_lU_l\le M_bD_c.
}
\tag{8.1}
\]
This is the exact signed budget appropriate to a bounded nonnegative KL
profile. It does not claim that this profile converges or that its derivative
has a sign.

Finally, (3.2), (5.8), (7.9), and (8.1) prove (0.1). In particular all count
layers, including the endpoints and the complement of every fixed central
window, have been accounted for with the actual coefficients.

## 9. Positivity of the margin and what remains

For `x=c^2 in (0,1)`,
\[
\rho_c=1-\frac{x\log x}{1-x}\in(1,2),
\]
because `-x log x<1-x`. Thus
\[
0<D_c<\frac{1-\log2}{2}<\frac16.
\]
Also `b M_b=sqrt(2/(pi e))<1/2`. At `c=19/20`, `c^4>4/5` and `pi^4<100`, so
\[
b(A_c-M_bD_c)
>\frac{16}{125}-\frac1{12}=\frac{67}{1500}>0.
\tag{9.1}
\]
This proves strict negativity without relying on the decimal computations.
The exact expression gives the sharper displayed margin of approximately
`2.689614884862`.

The remaining gap for an **exact** signed coefficient is now smaller and
specific: one needs the limiting conditional-odds susceptibility in (7.3),
and the actual signed output-KL profile contribution, rather than its interval
budget (8.1). No convergence of either has been asserted. The evidence term no
longer contributes at scale `n`.

The separate clock-acceleration term `C_n` has not been compared at scale `n`.
Accordingly, (0.1) makes no claim about `W_n+C_n`. The ultimate all-amplitude,
all-density true Toeplitz entropy-rate concavity target remains outside this
corrected-law theorem.

## 10. Reproducible diagnostics and references

`S43_checks.py` checks the finite Stein identity, the exact count/field
conversion, coefficient clocks and radial moments, the third determinant
identity, and the count-kernel sign normalization. Its larger radial examples
are diagnostics only, not fits or proof certificates. `S43_checks_output.json`
records the executed binary64 results. No numerical statement supplies an
asymptotic premise of the proof.

Repository inputs read for this assignment, all at the specified cycle-03
branch:

- `prompts/CYCLE03/S43.md`.
- `results/SA04/TASK.md`.
- `results/SA04/SA04_REPORT.md`.
- `results/SA04/sources/S13_PROOF.md` (frozen definitions, not new S13 claims).
- `research/CYCLE03_20260918/reviews/S43.md`.
- `research/CYCLE03_20260918/S45_RESULT.md` (pending review; not assumed).
- `TARGET.md` for the ultimate target's scope.

External theorem used: J. Borcea, P. Branden, T. M. Liggett, *Negative dependence
and the geometry of polynomials*, Journal of the American Mathematical Society
22 (2009), 521--567; arXiv:0707.2340, Proposition 5.1 / Theorem 5.2, and the stated
real-stability closure operations. Applicability to the conditional heat
channel is proved in Section 4.3.
