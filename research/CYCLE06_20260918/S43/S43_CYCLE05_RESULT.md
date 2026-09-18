# S43 cycle05 — Terminal-production transfer and conditional-odds compensation

**CORRECTED_LAW_ONLY. New author derivation; independent validation is separate.**

## 1. New result, with the decisive object defined

All logarithms are natural. Fix `0<c<1`, let `n=2k` tend to infinity through even
integers, and put
\[
p=(1+c)/2,\quad q=(1-c)/2,\quad b=(1-c^2)/4.
\]
Let `P=P_n` be the prescribed cyclic half-density Fourier projection. Define the
auxiliary **full spatial law**, not a radial law,
\[
 Q_{n,u}=\operatorname{DPP}\bigl((1-u)I/2+uP\bigr),\qquad 0<u<1.
\]
For its output bits `Y`, set
\[
 r_{i,u}=Q_{n,u}(Y_i=1\mid Y_{-i}),\quad
 h_{i,u}=\log\frac{r_{i,u}}{1-r_{i,u}},\quad x_{i,u}=2r_{i,u}-1,
\]
\[
 \mathsf I_n(u)=\sum_{i=1}^n E_{Q_{n,u}}[x_{i,u}h_{i,u}].
\]
This is the entropy production of the full spatial law under the generator
`L_flip f=sum_i[f(Y^i)-f(Y)]`, with rate one per bit.

**Terminal-transfer theorem.** At the exact corrected clock, in original `G` time,
\[
 \boxed{\sup_{|l-k|\le n^{2/3}}
 \left|\frac{J_l(s_l)}{n^2}-\frac{\mathsf I_n(c)}{2n}\right|\longrightarrow0,}
 \tag{T1}
\]
and, with all the actual count weights and endpoint conventions,
\[
 \boxed{C_n(c)=\frac{\mathsf I_n(c)}b+o(n).}                 \tag{T2}
\]
No limit of `mathsf I_n(c)/n`, and no limiting differentiability, is assumed.

For `g(x)=x log((1+x)/(1-x))`, the resulting explicit terminal interval is
\[
 \boxed{\frac{g(8c^2/\pi^2)}{2b}
 \le\liminf\frac{C_n}{n}\le\limsup\frac{C_n}{n}
 \le\frac{2g(c^4)+g(c^2)}{3b}.}                            \tag{T3}
\]
At `c=19/20`, this is
\[
 27.971948500903766\ldots\ \le\liminf C_n/n
 \le\limsup C_n/n\ \le87.472582228429019\ldots.
\]
These are asymptotic coefficients, not replacements for every finite-`n` bound.

There is also a joint, compensated estimate. Define
\[
 M_b=\frac{2e^{-1/2}}{\sqrt{2\pi}\,b},\quad
 D_c=\tfrac12(\rho_c-1-\log\rho_c),\quad
 \rho_c=1-\frac{c^2\log c}{2b}.
\]
Using their established cycle03 output-KL budget,
\[
 \boxed{\frac{c^4/3-c^6}{b(1-c^4)}-M_bD_c
 \le\liminf\frac{W_n+C_n}{n}
 \le\limsup\frac{W_n+C_n}{n}
 \le\frac{2c^8+c^4}{3b}+M_bD_c.}                          \tag{T4}
\]
At `c=19/20` its endpoints are
`-105.331223693047389...` and `32.082474477215733...`.
It does not decide the sign of `W_n+C_n`.

## 2. Exact clocks and the reviewed inputs actually used

Use `U_jr=n^(-1/2) exp(2 pi i jr/n)`, `0<=r<k`, and `P=UU*`.
The latent law is `nu(A)=det P_A`. The initial conditional law is uniform over
`l`-subsets of `A` for `l<=k`, with the prescribed complementary construction above
`k`. Write `F_l(s)=D(mu_l(s)||u_l)` and `J_l(s)=-F_l'(s)` for
\[
 G_l f(S)=\sum_{i\in S,j\notin S}[f(S-i+j)-f(S)].
\]
For a comparison amplitude `u`, define
\[
 z(u)=\left(\frac{1+u}{1-u}\right)^2,\qquad
 Z_m(z)=[t^m](1+t)^k(1+zt)^k,\quad m=\min(l,n-l),
\]
\[
 \theta_{n,l}(z)=
 \frac{(z-1)^2[t^{m-2}](1+t)^{k-2}(1+zt)^{k-2}}
 {[m(m-1)/(k(k-1))]Z_m(z)},\qquad
 \sigma_l(u)=-\frac{\log\theta_{n,l}(z(u))}{2(n-1)}.
 \tag{2.1}
\]
The actual terminal time is `s_l=sigma_l(c)`. Throughout,
\[
 d_l(c)=-\left.\partial_a^2s_l(a,c)\right|_{a=(1-c)/2}
\]
is the derivative in the original parameter `a`, **not** in the comparison
amplitude `u`. The four layers `0,1,n-1,n` have zero contribution and need no clock.

Define the Gibbs comparison on every layer by
\[
 \Lambda_u=I+(z(u)-1)P,\quad
 \gamma_{l,u}(S)=\frac{\det(\Lambda_u)_S}{Z_l(z(u))},\quad
 \mathscr F_l(u)=D(\gamma_{l,u}\Vert u_l).
\]
The previous complete-source result supplies these precise fixed-amplitude
estimates. For each fixed `u in (0,1)`, there are `eta_u,C_u>0` and `N_u` such that
for even `n>=N_u`,
\[
 |F_l(\sigma_l(u))-\mathscr F_l(u)|\le C_u
 \quad\text{if }|l-k|\le\eta_u k,                         \tag{2.2}
\]
\[
 |\mathscr F_l(u)-\mathscr F_k(u)|
 \le C_u[1+(l-k)^2/n]\quad(0\le l\le n).                 \tag{2.3}
\]
For (2.2), the reviewed ledger is `F_l=mathscr F_l+U_l+v_l`, with both the output
KL `U_l` and the evidence correction `v_l` uniformly bounded in this macro band.
These are static estimates only; no derivative of their errors is imported.
Their original radial proof uses the stable polynomial `e_l(z_A)` of the actual
conditional initial law, not a claim that arbitrary mixtures preserve stability.

The reviewed coefficient-clock estimates, uniform on
`B_n={|l-k|<=n^(2/3)}`, are
\[
 n\sigma_l(u)\to-\log u,\qquad nd_l(c)\to2/b.             \tag{2.4}
\]
Indeed `theta->c^2`,
\[
 \partial_z\log\theta\to\frac{(1-c)^3}{2c(1+c)},\qquad
 z''(a_*)=\frac{32c}{(1-c)^4},\qquad
 d_l=\frac{z''\partial_z\log\theta}{2(n-1)}.
\]
The all-layer bounds needed only for tails are
\[
 F_l(0)\le\min(l,n-l)\log2,\qquad
 0\le d_l/\sigma_l(c)\le K_c,
 \quad K_c=\frac{2z''(a_*)}{(z-1)\beta_0(z)},\quad
 \beta_0(z)=2\log\frac{z+1}{z-1}.                         \tag{2.5}
\]
The accepted sources for (2.2)--(2.3) are original cycle03 §§3--6 and its complete
PR15 review; (2.4)--(2.5) are the clock inputs explicitly accepted in PR18.
They are used as established lemmas, not re-proved signed-envelope claims.

## 3. A dimension-free modulus for full spatial production

Put
\[
 \mathscr E_n(u)=D(Q_{n,u}\Vert 2^{-n})=n\log2-H(Q_{n,u}).
\]
Conditional on the projection-DPP latent set, `Q_{n,u}` is obtained by independent
binary-symmetric noise of amplitude `u`. If `u=e^(-2t)`, this is the rate-one
bit-flip semigroup. Exact finite differentiation gives
\[
 \boxed{\mathscr E_n'(u)=\frac{\mathsf I_n(u)}{2u}.}        \tag{3.1}
\]
To check the production expression, condition on `Y_-i` in
`-E L_flip log Q`: the `i`-term is
`(2r_i-1) log(r_i/(1-r_i))`.

We need more than (3.1): `mathsf I_n(u)/n` is uniformly locally Lipschitz in `u`.
Here is an explicit dimension-free proof.
Set `r=(1+u)/(1-u)`. The `L`-matrix of `Q_{n,u}` is
\[
 L_u=rP+r^{-1}(I-P),\qquad r^{-1}I\preceq L_u\preceq rI.
\]
For a configuration `S` outside `i`, `h_i(S)` is the logarithm of the Schur
complement at `i`. Thus
\[
 |h_i|\le\log r,\qquad |\partial_u h_i|\le2/(1-u^2).
 \tag{3.2}
\]
For the derivative, `-R L_u<=L_u'<=R L_u`, with `R=2/(1-u^2)`; differentiate
`h_i=-log[(L_u)_{S+i}^{-1}]_ii` and apply these Loewner inequalities.

There is also the pointwise flip-row estimate
\[
 \boxed{\sum_{j\ne i}|h_i(S\mathbin\triangle\{j\})-h_i(S)|\le2r^2.}
 \tag{3.3}
\]
For additions, take the Schur complement `M` over `S`. Its spectrum is in
`[r^(-1),r]`, and the absolute change from adding `j` is
\[
 -\log\left(1-\frac{|M_{ij}|^2}{M_{ii}M_{jj}}\right)
 \le\frac{|M_{ij}|^2}{M_{ii}M_{jj}-|M_{ij}|^2}
 \le\frac{|M_{ij}|^2}{r^{-1}M_{ii}}.
\]
Summing and using `M^2<=rM` gives at most `r^2`. For deletions, Jacobi's identity
says
\[
 h_i^{L}(S)=-h_i^{L^{-1}}(([n]\setminus\{i\})\setminus S).
\]
The inverse has the same spectral bounds; its additions cost another `r^2`.
This proves (3.3), including both occupied and unoccupied coordinates.

For `f(h)=h tanh(h/2)`, `|f'(h)|<=1+(log r)/2` on the relevant interval.
Since `partial_u Q=-(2u)^(-1)L_flip^*Q`, (3.2)--(3.3) imply
\[
 \boxed{\frac{|\mathsf I_n'(u)|}{n}
 \le\left(1+\frac{\log r}{2}\right)
 \left(\frac2{1-u^2}+\frac{r^2}{u}\right).}               \tag{3.4}
\]
The right side is bounded on each compact subinterval of `(0,1)` and is independent
of `n`. It is a proved modulus, not a claimed small contribution to the final
coefficient. This step is what allows short time secants to return to the actual
terminal time without assuming convergence of a derivative.

## 4. Secant transport to the terminal heat production

The count law of `Q_{n,u}` is exactly
\[
 \pi_l(u)=[t^l]\{b_u+(1-2b_u)t+b_ut^2\}^{k},\qquad
 b_u=(1-u^2)/4,
\]
with mean `k` and variance `nb_u`; conditional on the count its law is
`gamma_l,u`. The entropy chain rule gives
\[
 \mathscr E_n(u)=\sum_l\pi_l(u)\mathscr F_l(u)
 +D(\pi(u)\Vert\operatorname{Bin}(n,1/2)).
\]
There is an explicit sufficient count bound
\[
 0\le D(\pi(u)\Vert\operatorname{Bin}(n,1/2))
 \le\log(n+1)+4b_u.                                     \tag{4.1}
\]
For an integer `l`, its probability under `Bin(n,l/n)` is at least `1/(n+1)`,
because it is a mode. Hence
\[
 \operatorname{Bin}(n,1/2)(l)\ge(n+1)^{-1}
 e^{-nD(\operatorname{Ber}(l/n)\Vert\operatorname{Ber}(1/2))}.
\]
Use `D(Ber(t)||Ber(1/2))<=chi^2=4(t-1/2)^2`, and the actual count variance, to get
(4.1). Equation (2.3) now gives
\[
 \boxed{F_l(\sigma_l(u))=\mathscr E_n(u)
 +O_u\bigl(\log(n+1)+(l-k)^2/n\bigr)}                     \tag{4.2}
\]
inside the macro band. In particular the error is `o(n)` uniformly on `B_n`.

For the original-rate slice flow, `J_l(s)` is nonincreasing. To see this directly,
write, for its density `f`,
\[
 J(f)=\tfrac12\sum_{i<j}E_{u_l}
 (f-T_{ij}f)(\log f-\log T_{ij}f).
\]
The integrand is jointly convex, the heat semigroup commutes with every
transposition, and preserves `u_l`. Jensen's inequality therefore gives
`J(P_tf)<=J(f)`. Positivity at positive times handles initially zero densities.

Fix `0<u_-<c<u_+<1`. For large `n`, uniformly on `B_n`, (2.4) orders the three
**exact** clocks. Monotonicity of production gives
\[
 \frac{F_l(\sigma_l(c))-F_l(\sigma_l(u_-))}
 {\sigma_l(u_-)-\sigma_l(c)}
 \le J_l(\sigma_l(c))\le
 \frac{F_l(\sigma_l(u_+))-F_l(\sigma_l(c))}
 {\sigma_l(c)-\sigma_l(u_+)}.                             \tag{4.3}
\]
Insert (4.2), divide by `n^2`, and use (2.4). For these three fixed amplitudes the
lower and upper expressions become, uniformly in the layer,
\[
 \frac1{2\log(c/u_-)}\int_{u_-}^c\frac{\mathsf I_n(u)}n\frac{du}{u}+o(1),
 \qquad
 \frac1{2\log(u_+/c)}\int_c^{u_+}\frac{\mathsf I_n(u)}n\frac{du}{u}+o(1).
\]
The modulus (3.4) bounds their difference from `mathsf I_n(c)/(2n)` by
`C_c max(c-u_-,u_+-c)+o(1)`. First let `n` tend to infinity, then let the fixed
brackets approach `c`. This proves (T1). Only the static errors at three fixed
amplitudes were used; none was differentiated.

For aggregation, `C_n=sum_l pi_l(c)d_l(c)J_l(s_l)` uses the actual probabilities.
Hoeffding gives
\[
 \sum_{l\notin B_n}\pi_l(c)\le2e^{-2n^{1/3}}.
\]
On every nonendpoint layer, monotonicity also gives `sJ(s)<=F(0)`. Therefore (2.5)
implies the finite bound
\[
 0\le d_lJ_l(s_l)\le K_c\,n\log2/2.
\]
The omitted contribution to `C_n/n` tends to zero. On `B_n`, combine (T1) with
`nd_l->2/b` and the fact that its actual mass tends to one. This proves (T2).
The endpoint contributions are exactly zero. In normalized `L_l` time,
`tau_l=l(n-l)s_l` and `I_l^L=J_l/[l(n-l)]`, so
`(-tau_l'')I_l^L=(-s_l'')J_l`; no rate factor is omitted.

## 5. Checkerboard conditional-odds envelopes

The Fourier projection has diagonal half-blocks:
\[
 P=\frac12\begin{pmatrix}I&V\\ V^*&I\end{pmatrix},\qquad VV^*=V^*V=I,
 \tag{5.1}
\]
when sites are ordered by parity. Thus either parity under `Q_n,c` consists of
independent fair bits. For a fixed site `i`, let the opposite-parity bits be
`Y_j`, and put
\[
 a=c^2,\quad w_j=|V_{ij}|^2=4|P_{ij}|^2,\quad
 y=\sum_jw_j(1-2Y_j),\quad\sum_jw_j=1.
\]
Exact one-site DPP conditioning on these mutually uncorrelated coordinates gives
\[
 E[x_i\mid Y_{\rm opp}]=a y.                             \tag{5.2}
\]
Equivalently, the remaining conditional kernel is
`I/2+(c^2/2)V diag(1-2Y_opp)V*`.

The full conditional odds, including all other sites, satisfy the sharper bounds
\[
 \boxed{\frac{a(y-a)}{1-ay}\le x_i\le\frac{a(y+a)}{1+ay}.} \tag{5.3}
\]
To prove them, write the `L`-matrix as
\[
 L=dI+e\begin{pmatrix}0&V\\V^*&0\end{pmatrix},\quad
 d=\frac{1+c^2}{1-c^2},\quad e=\frac{2c}{1-c^2},\quad d^2-e^2=1.
\]
Conditional probabilities are nonincreasing in each other bit: the second log
atom difference is `log(1-|M_ij|^2/(M_ii M_jj))<=0`. With the opposite pattern
fixed, the maximum occurs when all remaining same-parity bits are zero.
If `t=sum_j w_jY_j=(1-y)/2`, its Schur complement is `d-e^2t/d`. Converting these
odds to `x` gives the upper endpoint in (5.3). The full law is invariant under
complementation, since `I-K=DKD*` for the parity sign matrix `D`. Complementation
gives the lower endpoint. In particular `|x_i|<=c^2`.

The function `g(x)=x log((1+x)/(1-x))` is even and convex, with
`g''(x)=4/(1-x^2)^2`. Given the opposite pattern, a random variable with mean `ay`
and the endpoints (5.3) is bounded in convex order by the two-endpoint variable
with respective weights `(1-ay)/2` and `(1+ay)/2`. Consequently
\[
 E[g(x_i)\mid Y_{\rm opp}]\le\Phi_a(y),
\]
\[
 \Phi_a(y)=\frac a2\left[
 (a+y)\log\frac{1+a^2+2ay}{1-a^2}
 +(a-y)\log\frac{1+a^2-2ay}{1-a^2}\right].                \tag{5.4}
\]
These formulas extend continuously to `y=+/-1`.
With `t_a=2a/(1+a^2)<1`, its uniformly convergent power series on `[-1,1]` is
\[
 \Phi_a(y)=g(a^2)+\sum_{m\ge1}
 \left[\frac{a t_a^{2m-1}}{2m-1}
       -\frac{a^2t_a^{2m}}{2m}\right]y^{2m}.
\]
Every coefficient is positive because `a t_a<1`. Since `Phi_a(1)=g(a)`,
\[
 \Phi_a(y)\le g(a^2)+[g(a)-g(a^2)]y^2.                   \tag{5.5}
\]
The actual independent opposite-parity bits give
\[
 E y^2=\sum_jw_j^2=v_n=\frac13+\frac8{3n^2}.              \tag{5.6}
\]
For a direct finite calculation, `w_j=4/[n^2 sin^2(pi d/n)]` at odd distances.
Differentiate twice `sum_{j=0}^{k-1}csc^2(x+j pi/k)=k^2 csc^2(kx)` and set
`x=pi/(2k)`. This gives `sum csc^4=(k^4+2k^2)/3`, proving (5.6).
Cyclic translation symmetry, (5.4)--(5.6), prove the finite upper bound
\[
 \frac{\mathsf I_n(c)}n\le(1-v_n)g(c^4)+v_ng(c^2).         \tag{5.7}
\]

For a lower bound observe only the two nearest opposite-parity neighbors. They
are independent fair bits, and the conditional mean in (5.2), after averaging
unobserved bits, takes values
\[
 +t_n,\ 0,\ -t_n\quad\text{with probabilities }1/4,1/2,1/4,
 \qquad t_n=\frac{8c^2}{n^2\sin^2(\pi/n)}.
\]
Conditional Jensen gives the finite inequality
\[
 \frac{\mathsf I_n(c)}n\ge\tfrac12g(t_n).                 \tag{5.8}
\]
Combining (5.7)--(5.8) with (T2) proves (T3).

There is an analytic obstruction to the small-clock strategy based on the old
negative-envelope margin. Since `g(t)>2t^2` for `0<t<1`,
\[
 \frac{g(8c^2/\pi^2)}{2b}>
 \frac{64c^4}{b\pi^4}=4A_c.                              \tag{5.9}
\]
Here `A_c=16c^4/(b pi^4)` is the established count-envelope constant.
At `.95`, `A_c-M_bD_c` is positive and smaller than `A_c`. Thus the proposed
sufficient condition `limsup C_n/n < 2.689614884862...` is false in the actual
corrected model. This does **not** prove `C_n>-W_n`: the available envelope does
not identify `-W_n/n`.

## 6. A compensated signed response, not unrelated interval addition

Use the actual second-count coefficients
\[
 \kappa_l=\partial_a^2\pi_l(a_*,c)
 =B_l-2B_{l-1}+B_{l-2},\quad
 B_m=\sum_{i\ne j}\Pr\!\left(\sum_{v\notin\{i,j\}}Z_v=m\right),
\]
where the `Z_v` are the actual independent count bits with parameters `p,q`.
Extend `B` by zero outside its support, so `W_n=sum_l kappa_l F_l(s_l)`.
For Boolean functions use `partial_j f=f(Y_-j,1)-f(Y_-j,0)`. Let
`U_l=D(mu_l(s_l)||gamma_l,c)`. The established cycle03 ledger and count-Stein
identity say
\[
 W_n=\frac{\mathcal D_n''(0)}{b^2}+\sum_l\kappa_lU_l+o(n),
\]
\[
 \mathcal D_n''(0)=
 b^2\sum_{i\ne j}E\partial_jh_i-b\mathsf I_n(c)+nbc^2.
 \tag{6.1}
\]
Here \(Q_{n,c,t}\propto e^{t(N-k)}Q_{n,c}\), \(m_t=E_tN/n\), and
\(\mathcal D_n(t)=D(Q_{n,c,t}\Vert\operatorname{Ber}(m_t)^{\otimes n})\).
It is the natural count-field deficit, not the amplitude function `mathscr E_n`.
Also, the established actual-weight tail ledger gives
\[
 -M_bD_c\le\liminf n^{-1}\sum_l\kappa_lU_l
 \le\limsup n^{-1}\sum_l\kappa_lU_l\le M_bD_c.             \tag{6.2}
\]
In detail, `U_l>=0`, the central radial comparison gives `U_l<=D_c+o(1)`,
`sum(kappa_l)_+/n->M_b`, and the actual fourth-moment bound is
\[
 n^{-1}\sum_{|l-k|>K\sqrt n}|\kappa_l|
 [1+(l-k)^2/n]\le C_c/K^2.
\]
The uniform output-KL bound has the same quadratic envelope; this pays all
complementary layers. No derivative or sign of a layer difference of `U_l` is
needed. The four endpoint ledger entries vanish.

Insert the new (T2) into (6.1). The production terms cancel:
\[
 \boxed{W_n+C_n=
 \underbrace{\sum_{i\ne j}E\partial_jh_i+nc^2/b}_{\mathsf R_n(c)}
 +\sum_l\kappa_lU_l+o(n).}                               \tag{6.3}
\]
This is the compensated object. It has the following proved finite bounds.
Let `V_n=sum_i E x_i^2`. The exact Stein response is
\[
 b\sum_{j\ne i}E\partial_jr_i=b-E[r_i(1-r_i)].
\]
Since `partial_j r_i<=0`, the improved range `|x_i|<=c^2` gives
\[
 \frac4{1-c^4}\partial_jr_i\le\partial_jh_i\le4\partial_jr_i.
\]
Summing, using `E r_i(1-r_i)=(1-E x_i^2)/4`, yields
\[
 \frac{V_n-nc^6}{b(1-c^4)}\le\mathsf R_n(c)\le V_n/b.
 \tag{6.4}
\]
Conditional Jensen in (5.2) gives `V_n/n>=c^4 v_n`. Applying the same two-endpoint
convex-order bound to `x^2` gives
\[
 E[x_i^2\mid Y_{\rm opp}]
 \le a^4+\frac{a^2(1-a^2)^2y^2}{1-a^2y^2}
 \le a^4+(a^2-a^4)y^2.
\]
The last inequality follows either by its positive-coefficient series or by
`1-a^2y^2>=1-a^2`. Consequently
\[
 c^4v_n\le V_n/n\le(1-v_n)c^8+v_nc^4.                    \tag{6.5}
\]
Equations (6.2)--(6.5) prove (T4). This cancels the same conditional-odds production
inside the signed count response and the terminal clock response; it is not the
addition of unrelated upper and lower bounds.

## 7. Scope, quantifiers, and remaining gap

Every limit is along even `n`, with `c` fixed in `(0,1)`. In particular (T2) means:
for every `epsilon>0`, there is `N(c,epsilon)` such that all even `n>=N` satisfy
`|C_n-mathsf I_n(c)/b|<=epsilon n`. The corresponding epsilon-slack interpretation
applies to (T3)--(T4). Constants used for comparison neighborhoods need not be
uniform as `c` approaches zero or one.

The new tools are (3.3)--(3.4), the two-sided terminal secant transfer, and the
checkerboard conditional-odds convex-order envelope. They use binary-noise
integration by parts and elementary convex-analysis secants, but establish their
matrix and probability hypotheses explicitly here. No novelty-priority claim is
made. No derivative of the heat/Gibbs KL, nor replacement of spatial production
by latent production, occurs in the proof.

The sign of `W_n+C_n` remains open under these estimates. The remaining signed
quantity is the explicit susceptibility `mathsf R_n(c)` plus the actual weighted
output KL in (6.3), not a derivative of an unquantified transport remainder.
Neither `W_n/n` nor `C_n/n` has been shown to converge here.

This is a cyclic projection, balanced half-density theorem. The ultimate target
remains classical full-configuration Shannon entropy-rate concavity for actual
finite Toeplitz compressions `aI+cQ_{rho,n}`, every fixed `0<rho<1`, `0<c<1`, and
all legal `0<=a<=1-c`. Those finite compressions are not projections. No trace
spectral entropy substitution or limiting differentiability is used. Even a sign
for the corrected response would not settle that target.

## Appendix A. Explicit finite-sum refinements of the clock interval

The elementary upper coefficient in (T3) is not the strongest consequence of the
new posterior envelope. For any fixed integer `m>=1`, define independent fair
signs `epsilon_j^+,epsilon_j^-`,
\[
 w_j=\frac4{\pi^2(2j+1)^2},\quad
 Y_m=\sum_{j=0}^{m-1}w_j(\epsilon_j^++\epsilon_j^-),\quad
 d_m=1-2\sum_{j=0}^{m-1}w_j.
\]
These are finite sums with their exact `2^(-2m)` probability weights. Then
\[
 \frac1b E g(c^2Y_m)\le\liminf C_n/n,
\]
\[
 \limsup C_n/n\le
 \frac1{2b}E\{\Phi_{c^2}(Y_m+d_m)+\Phi_{c^2}(Y_m-d_m)\}.
 \tag{A.1}
\]
For the lower bound apply conditional Jensen after revealing only these opposite
neighbors. For the upper bound, the omitted independent signs have mean zero and
absolute weighted sum at most `d_m`; conditional on the revealed signs, convexity
of `Phi` bounds their contribution by the chord at `+/-d_m`. At finite `n`, use
`4/[n^2 sin^2((2j+1)pi/n)]` instead of `w_j` and their exact remaining weight.
For sufficiently large `n` the selected neighbors are distinct. Termwise limits
in this fixed finite sum prove (A.1). The remaining spatial tail is thus paid,
not ignored. Convexity of `Phi` follows from the positive series in §5.

For example, the `m=4` formulas evaluate to
\[
 28.8993300857207\ldots\le\liminf C_n/n
 \le\limsup C_n/n\le84.6090352585386\ldots.
\]
The exact finite-sum formulas, not decimal rounding, define these constants.
The diagnostic script evaluates further fixed choices. None is an asymptotic fit.

## Appendix B. The complete count/reference contribution

No corrected Shannon-entropy sign is claimed, but the reference term can be kept
explicit. For the corrected full law `qhat_a(S)=pi_|S|(a) mu_|S|,a(S)`,
\[
 \widehat H_n(a)=\mathcal A_n(a)-\widehat K_n(a),\qquad
 \mathcal A_n(a)=H(\pi(a))+\sum_l\pi_l(a)\log\binom nl.
\]
At the midpoint let `X=l-k`, and
`f_l=log[pi_l/Bin(n,1/2)(l)]`. Its exact derivatives are
\[
 \mathcal A_n''(a_*)=-\sum_l\kappa_l f_l-\frac nb,
 \tag{B.1}
\]
since `pi_l'(a_*)/pi_l=X/b` and `E X^2=nb`.
Use the exact count identity
\[
 \kappa_l=(X^2/b^2-n/b)\pi_l+(2c/b)\dot\pi_l,
\]
where the dot denotes balanced amplitude differentiation of counts only. The
reviewed count local limit and its tilted tail bounds give
\[
 f_{k+x\sqrt n}=-\tfrac12\log(4b)
 +(2-1/(2b))x^2+o(1)
\]
on bounded windows. The difference from the central value is bounded by
`C(1+x^2)` in a macro band; outside it `|f_l|<=Cn` and the count mass is exponentially
small. Hoeffding therefore justifies uniform integrability with an extra `x^2`.
Thus
\[
 \operatorname{Cov}_\pi(X^2,f_N)=-nbc^2+o(n).
\]
The full balanced count score has variance `n/(4b)`; after conditioning on the
count and using the same quadratic envelope,
`sum_l dot pi_l f_l=O(sqrt(n))=o(n)` by Cauchy--Schwarz. Substitution in (B.1) gives
\[
 \mathcal A_n''(a_*)=-4n+o(n),\qquad
 \widehat H_n''(a_*)=-4n-W_n-C_n+o(n).                    \tag{B.2}
\]
Both count acceleration and score terms have been retained. The interval (T4)
straddles the values needed for a Shannon-entropy sign; (B.2) is not a concavity
claim and supplies no passage to the ultimate Toeplitz family.

## Sources and dependency ledger

Repository: `cat5779/rl01`. Frozen definitions and original proofs are not treated
as changes of model when PRs are cleaned up.

* `research/sa-cycle04-20260918/TARGET.md`.
* Same branch: `results/SA04/TASK.md`, `results/SA04/SA04_REPORT.md`.
* Same branch: `research/CYCLE04_20260918/recovered/S43_cycle03/S43_RESULT.md`,
  especially original §§3--6 and §§7--8.
* Same branch: the recovered `S43_CYCLE03_MISSING_PROOF.md` in that directory.
* `research/sa-s43-cycle03-independent-review-20260918`:
  `research/INDEPENDENT_REVIEW_20260918/S43_CYCLE03.md` (PR15).
* `research/sa-cycle04-20260918`: `research/CYCLE04_20260918/S45_EARLY_RESULT.md`.
* `research/sa-s45-cycle04-independent-review-20260918`:
  `research/INDEPENDENT_REVIEW_20260918/S45_CYCLE04.md` (PR18), especially clock
  estimates and all-layer quotient/tail bounds.

Old inputs are explicitly distinguished in §§2 and 6. The new transfer, finite
matrix modulus, parity production bounds, and compensation estimates are proved
in this manuscript. No unavailable report or attachment is invoked.

## Reproducible computation

`S43_CYCLE05_checks.py` evaluates the explicit coefficients and checks the finite
conditional-odds ranges, bit-flip identity, Stein cancellation, original-rate
slice entropies, actual count weights, and exact coefficient clocks. Its output
is `S43_CYCLE05_checks_output.json`. These are implementation diagnostics, not
independent review or proof by finite-size fitting. In particular the small-`n`
clocks are far from their limiting time; the script does not apply asymptotic
coefficient bounds to those finite cases.
