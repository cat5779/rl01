# Harvest provenance — S43, cycle 03 response

Status: AUTHOR_CLAIMS_PENDING_INDEPENDENT_REVIEW.
Acquired via read_thread on 2026-09-18. PARTIAL EXPORT: the API returned only the first 20,000 characters. The omitted tail and downloadable attachments have NOT been acquired. Do not treat the author's headline as a verified theorem.
Original citation tokens below are preserved as source text, not independently resolved evidence.

---

# S43 cycle 03 — A signed \(n\)-scale envelope

**CORRECTED_LAW_ONLY**

I obtain a signed envelope, not merely an unsigned \(O(n)\) estimate:

\[
\boxed{\text{At }c=\frac{19}{20},\qquad -W_n=\Theta(n).}
\]

More precisely, the upper-envelope constant for \(W_n/n\) is strictly negative and is approximately \(-2.689614884862\). **I do not prove that \(W_n/n\) converges.**

The derivation below does **not** assume S45’s pending \(O(n)\) theorem. It proves the radial estimates needed for a sharper transport argument, using the established strong-Rayleigh preservation theorem for finite symmetric exclusion as its named external input. The pending-review distinction in the assignment is retained. citeturn764912view0turn725836view4

## Main theorem

For each fixed \(0<c<1\), define
\[
p=\frac{1+c}{2},\qquad q=\frac{1-c}{2},\qquad
b=pq=\frac{1-c^2}{4},
\]
and
\[
\rho_c=1-\frac{c^2\log c}{2b},\qquad
D_c=\frac12\bigl(\rho_c-1-\log\rho_c\bigr),
\]
\[
M_b=\frac{2e^{-1/2}}{\sqrt{2\pi}\,b},\qquad
A_c=\frac{16c^4}{b\pi^4},\qquad
L_c=\frac{c^4}{4b^2}+\frac cb\log\frac pq.
\]

For the prescribed cyclic half-density corrected law, with its **exact coefficient clock and actual count weights**,
\[
\boxed{
-L_c-M_bD_c
\le
\liminf_{\substack{n\to\infty\\ n\ {\rm even}}}\frac{W_n}{n}
\le
\limsup_{\substack{n\to\infty\\ n\ {\rm even}}}\frac{W_n}{n}
\le
-A_c+M_bD_c.
}
\tag{T}
\]

All estimates are for fixed \(c\); no uniformity as \(c\to0\) or \(c\to1\) is asserted.

At \(c=19/20\),
\[
\begin{aligned}
\rho_c&\approx1.949583552508,
&
D_c&\approx0.140983882778,
\\
A_c&\approx5.488710044770,
&
M_bD_c&\approx2.799095159908,
\\
A_c-M_bD_c&\approx2.689614884862,
&
L_c+M_bD_c&\approx488.308585220766.
\end{aligned}
\]

The decimal evaluations are not premises of the proof. Strict positivity of \(A_c-M_bD_c\) is established analytically below.

Equivalently, for every \(\varepsilon>0\), there is \(N(c,\varepsilon)\) such that every even \(n\ge N(c,\varepsilon)\) satisfies
\[
-L_c-M_bD_c-\varepsilon
\le \frac{W_n}{n}
\le -A_c+M_bD_c+\varepsilon.
\]

The proof has two new components:

**A count-Stein curvature certificate** identifies a strictly negative auxiliary Gibbs response.

**An averaged third-difference log-determinant estimate** makes the heat/Gibbs evidence correction flat on the \(\sqrt n\) layer scale. The remaining output KL need not have a derivative or a convergent profile: its entire signed contribution is paid by the explicit budget \(M_bD_c\).

---

# 1. Exact model and conventions

Let \(n=2k\ge4\), and write
\[
U_{jr}=n^{-1/2}e^{2\pi i jr/n},
\qquad 0\le j<n,\quad 0\le r<k,
\qquad P=UU^*.
\]
The latent \(k\)-set has law
\[
\nu(A)=\det P_A.
\]

Conditional on \(A\), at layer \(2\le l\le k\), start from a uniform \(l\)-subset of \(A\), and run
\[
(G_lf)(S)=
\sum_{i\in S,\ j\notin S}
[f(S-i+j)-f(S)].
\]

Put
\[
z=(p/q)^2,\qquad \beta=\log z,
\]
\[
Z_l=[t^l](1+t)^k(1+zt)^k,\qquad
a_j=[t^j](1+t)^{k-2}(1+zt)^{k-2},
\]
\[
\alpha_l=\frac{l(l-1)}{k(k-1)},\qquad
\theta_l=\frac{(z-1)^2a_{l-2}}{\alpha_lZ_l},
\qquad
s_l=-\frac{\log\theta_l}{2(n-1)}.
\tag{1}
\]
These are the original-rate clock and frozen corrected-law definitions—not a limiting half-step replacement. citeturn725836view0turn725836view2

Let \(\mu_l\) be the marginal at \(s_l\), and
\[
F_l=D(\mu_l\Vert u_l).
\]
Use the prescribed complementary layers above \(k\), and the uniform-law convention at \(0,1,n-1,n\). Thus
\[
F_{n-l}=F_l,\qquad F_0=F_1=F_{n-1}=F_n=0.
\]

The clock is nonnegative directly from its coefficients. With \(f(t)=(1+t)(1+zt)\),
\[
\alpha_lZ_l=[t^{l-2}]f^{k-2}
\left((f')^2+\frac{ff''}{k-1}\right).
\]
The bracket has nonnegative coefficients and constant coefficient
\[
(z+1)^2+\frac{2z}{k-1}>(z-1)^2.
\]
Hence \(0<\theta_l<1\).

The actual count law is
\[
\sum_l\pi_l(a,c)t^l
=[1-a-c+(a+c)t]^k[1-a+at]^k.
\]
All layer entropies in \(W_n\) are frozen at \(a_*=q\).

Extend \(B_m=0\) outside \(0\le m\le n-2\), and define
\[
w_l=B_{l-1}-B_{l-2},\qquad
\kappa_l=B_l-2B_{l-1}+B_{l-2}.
\]
Then
\[
\kappa_l=\pi_l''(a_*,c),
\]
and
\[
W_n=\sum_{l=0}^n\kappa_lF_l
=\sum_{m=0}^{n-2}B_m(F_{m+2}-2F_{m+1}+F_m)
=-2\sum_{l=2}^k w_l(F_l-F_{l-1}).
\tag{2}
\]
This is the moving-count response, not the full second derivative containing the separate clock-acceleration term \(C_n\). citeturn725836view1

---

# 2. The actual signed count kernel

Set
\[
\phi(t)=b+(1-2b)t+bt^2,
\]
\[
\eta_k=\frac{k-1+2b}{2(2k-1)},\qquad
\psi_k(t)=\eta_k+(1-2\eta_k)t+\eta_kt^2.
\]
Separating the ordered deleted pairs into high–high, low–low, and mixed pairs gives exactly
\[
\sum_m\frac{B_m}{n(n-1)}t^m
=\phi(t)^{k-2}\psi_k(t),
\qquad b\le\eta_k\le\frac14.
\tag{3}
\]

Indeed, if \(A(t)=q+pt\) and \(E(t)=p+qt\), the unnormalized remaining factor is
\[
k(k-1)(A^2+E^2)+2k^2\phi.
\]

The probability distribution in (3) is a sum of \(n-2\) independent Bernoulli variables. Its mean is \(k-1\), its variance is
\[
V_B=(n-4)b+2\eta_k,
\]
and its centered characteristic function is
\[
\chi_n(t)
=(1-4b\sin^2(t/2))^{k-2}
(1-4\eta_k\sin^2(t/2)).
\]
For \(|t|\le\pi\),
\[
|\chi_n(t)|
\le e^{-2V_B\sin^2(t/2)}
\le e^{-2V_Bt^2/\pi^2},
\qquad V_B\ge(n-2)b.
\tag{4}
\]

Define
\[
\varphi_b(x)=\frac{e^{-x^2/(2b)}}{\sqrt{2\pi b}},
\qquad
g_b(x)=-\varphi_b'(x)=\frac{x}{b}\varphi_b(x).
\]
Fourier inversion, \(t=u/\sqrt n\), and (4) give
\[
\frac{\kappa_{k-\lfloor x\sqrt n\rfloor}}{\sqrt n}
\longrightarrow\varphi_b''(x),
\qquad
\frac{w_{k-\lfloor x\sqrt n\rfloor}}n
\longrightarrow g_b(x).
\tag{5}
\]

The convergence is locally uniform. The underlying lattice first- and second-difference errors are actually uniform over all lattice indices: after scaling, their absolute errors are bounded by integrals independent of the Fourier phase, with integrable envelopes
\[
C|u|e^{-a u^2},\qquad Cu^2e^{-a u^2}.
\]

## 2.1 Exact sign pattern and total positive mass

Multiplication of a coefficient sequence by a positive linear polynomial cannot increase its number of sign changes. After a positive geometric rescaling, the new coefficients are adjacent averages of the old ones, hence samples of their piecewise-linear interpolation.

Both \(\phi\) and \(\psi_k\) factor into positive linear factors; for \(\psi_k\), the discriminant is \(1-4\eta_k\ge0\). Therefore the coefficients of
\[
(1-t)^2\phi(t)^{k-2}\psi_k(t)
\]
have at most two sign changes.

These coefficients are positive at both endpoints, symmetric, and sum to zero. Thus, ignoring zeros, the sign pattern of \(\kappa_l\) is exactly
\[
+,\ -,\ +.
\]

Writing \(D_m=B_m-B_{m-1}\), summation of its increasing and decreasing pieces gives
\[
\sum_l(\kappa_l)_+=2\max_mD_m,
\qquad
\sum_l|\kappa_l|=4\max_mD_m.
\]
The uniform first-difference limit yields
\[
\boxed{
\frac1n\sum_l(\kappa_l)_+\longrightarrow
2\max_{x\ge0}g_b(x)
=\frac{2e^{-1/2}}{\sqrt{2\pi}\,b}=M_b,
}
\tag{6}
\]
and
\[
\frac1n\sum_l|\kappa_l|\longrightarrow2M_b.
\]

## 2.2 A complete tail bound from actual coefficients

Choose fixed \(K_0>\sqrt b\). By (5) and the sign pattern, for sufficiently large \(n\), all negative \(\kappa_l\) lie within
\[
|l-k|\le K_0\sqrt n+2.
\]

Exact summation by parts gives
\[
\begin{aligned}
\sum_l\kappa_l(l-k)^4
&=\sum_mB_m\{12(m-k+1)^2+2\}\\
&=n(n-1)(12V_B+2).
\end{aligned}
\tag{7}
\]
The negative part is confined to a fixed scaled window, and the total variation is \(O(n)\). Consequently
\[
\sup_{\substack{n\ge4\\n\ {\rm even}}}
\frac1n\sum_l|\kappa_l|
\left(1+\left|\frac{l-k}{\sqrt n}\right|^4\right)<\infty.
\tag{8}
\]
In particular, for \(K\ge1\),
\[
\boxed{
\frac1n\sum_{|l-k|>K\sqrt n}|\kappa_l|
\left(1+\frac{(l-k)^2}{n}\right)
\le\frac{C_b}{K^2}.
}
\tag{9}
\]

This controls all complementary layers using the actual weights. No Gaussian substitute weights have been inserted.

## 2.3 Signed profile functional and central endpoint

For a symmetric array \(h_l\), put
\[
G_{n,r}=h_k-h_{k-r}.
\]
Since \(\sum_l\kappa_l=0\),
\[
\frac1n\sum_l\kappa_lh_l
=-\frac2n\sum_{r=1}^k\kappa_{k-r}G_{n,r}.
\tag{10}
\]
There is no omitted central atom: \(G_{n,0}=0\) exactly.

If these profiles converge locally uniformly to \(G\), and
\[
|G_{n,r}|\le C(1+r^2/n),
\]
then (5) and (9) imply
\[
\boxed{
\frac1n\sum_l\kappa_lh_l
\longrightarrow
-2\int_0^\infty\varphi_b''(x)G(x)\,dx.
}
\tag{11}
\]
For \(G(x)=\alpha x^2\), this gives \(-2\alpha\), fixing the sign and normalization.

The proof of (T) will not assume that the corrected profile converges.

---

# 3. Exact Bayesian transport

Introduce the auxiliary Gibbs channel
\[
T_l^G(S\mid A)=\frac{z^{|A\cap S|}}{Z_l},
\qquad |S|=l.
\]
The same coefficient formula defines \(Z_l\) on all layers for this comparison; it introduces no new corrected-law clocks.

Let
\[
\Lambda=I+(z-1)P,\qquad
\ell(S)=\log\det\Lambda_S.
\]
Cauchy–Binet gives
\[
\mathbb E_\nu z^{|A\cap S|}
=\det\Lambda_S.
\]
Thus
\[
\gamma_l(S)=\frac{\det\Lambda_S}{Z_l},
\qquad
\nu^G(A\mid S)
=\frac{\nu(A)z^{|A\cap S|}}{\det\Lambda_S}.
\tag{12}
\]

Define
\[
\mathscr F_l=D(\gamma_l\Vert u_l),\qquad
U_l=D(\mu_l\Vert\gamma_l),
\]
\[
v_l=\mathbb E_H\ell(S)-\mathbb E_G\ell(S).
\]
The exact output ledger is
\[
\boxed{F_l=\mathscr F_l+U_l+v_l.}
\tag{13}
\]

Conditional on \(A\), both channels are uniform within overlap orbits. For
\[
R=|S\cap A^c|,
\]
write their radial laws as \(p_l^H,q_l^G\). Then
\[
q_l^G(r)
=\frac{\binom kr\binom k{l-r}z^{l-r}}{Z_l}.
\]
The KL chain rule gives
\[
\begin{aligned}
D(p_l^H\Vert q_l^G)
&=D(\nu T_l^H\Vert\nu T_l^G)\\
&=U_l+
\mathbb E_{\mu_l}
D\!\left(\nu^H(\cdot\mid S)\Vert\nu^G(\cdot\mid S)\right).
\end{aligned}
\tag{14}
\]
In particular,
\[
0\le U_l\le D(p_l^H\Vert q_l^G).
\tag{15}
\]

There is no assertion that \(U_l-U_{l-1}\) has a sign.

The Fourier relations
\[
DPD^*=I-P,\qquad D_{jj}=(-1)^j,\qquad \nu(A^c)=\nu(A)
\]
and Jacobi’s complementary-minor identity imply
\[
\ell(S)=\beta(|S|-k)+\ell(S^c).
\tag{16}
\]
Hence \(\mathscr F_l,U_l,v_l\) extend symmetrically across \(k\). At the four endpoint layers their ledger values are zero.

---

# 4. The radial KL has an explicit central limit

Fix \(c\), and choose a sufficiently small \(\eta>0\), for example smaller than \(q/4\). “Macro band” below means
\[
(1-\eta)k\le l\le k.
\]
Constants may depend on \(c,\eta\), but not on \(n,l\).

I will prove
\[
\boxed{
\sup_{0\le k-l\le K\sqrt n}
\left|D(p_l^H\Vert q_l^G)-D_c\right|\longrightarrow0
\quad\text{for every finite }K,
}
\tag{17}
\]
together with a uniform \(O(1)\) bound throughout the macro band.

## 4.1 Gibbs means, variances, and log masses

Let
\[
X=l-R,\qquad m_l=\mathbb E_GX,\qquad
\sigma_l^2=\operatorname{Var}_GX.
\]
Its adjacent-probability ratio is
\[
\frac{\Pr_G(X=j+1)}{\Pr_G(X=j)}
=\frac{z(k-j)(l-j)}
{(j+1)(k-l+j+1)}.
\tag{18}
\]

A mode is within two of the root \(x_l^*\) of
\[
z(k-u)(l-u)=u(k-l+u).
\]
Indeed, the polynomial on the left minus right has derivative at most \(-2k\), and the two mode inequalities give the claimed distance.

Writing \(\lambda=l/k\) and \(A_z=(z+1)/(z-1)\),
\[
x_l^*=\frac k2
\left\{\lambda+A_z-\sqrt{A_z^2-1+(1-\lambda)^2}\right\}.
\]
Since \(\sqrt{A_z^2-1}=2b/c\),
\[
\left|x_{k-r}^*-\left(pk-\frac r2\right)\right|
\le\frac{cr^2}{8bk}.
\tag{19}
\]

All four selected/unselected population counts near the mode are therefore a positive fraction of \(n\) in the macro band.

Successive log-ratios in (18) decrease by at least a constant times \(1/n\) over the support and change by \(O(1/n)\) in the fixed interior region. Summing from a mode gives
\[
q_l^G(r)\le\frac C{\sqrt n}
\exp\!\left(-a\frac{(r-r_l^*)^2}{n}\right),
\qquad
q_l^G(r_l^*)\asymp n^{-1/2}.
\tag{20}
\]
For the normalization, the global ratio bound makes the sum of ratios to the modal weight at most \(C\sqrt n\); the local lower bound gives the reverse inequality.

Thus centered absolute moments of order \(j\) are \(O(n^{j/2})\). Also, if
\[
B(u)=z(k-u)(l-u)-u(k-l+u),
\]
the ratio identity implies \(\mathbb EB(X)=0\), hence
\[
B(m_l)=-(z-1)\sigma_l^2,\qquad m_l-x_l^*=O(1).
\tag{21}
\]

Taylor expansion of the binomial log weights, with (20) controlling the complement, proves their uniform Gaussian local limit. The exponent, in the variable \(t=X/k\), has second derivative
\[
-\frac1{t(1-t)}
-\frac1{(\lambda-t)(1-\lambda+t)}.
\]
This is bounded away from zero; higher derivatives are uniformly bounded locally.

Consequently, on every fixed central \(\sqrt n\) layer window,
\[
\frac{\sigma_l^2}{n}\longrightarrow\frac b4,
\tag{22}
\]
and, on bounded standardized overlap windows,
\[
-\log q_l^G(r)
=\frac12\log(2\pi n b/4)
+\frac{(r-\mathbb E_GR)^2}{2n(b/4)}
+o(1),
\tag{23}
\]
uniformly.

We also have the global macro-band bound
\[
\left|-\log q_l^G(r)-\frac12\log n\right|
\le C\left(1+\frac{(r-\mathbb E_GR)^2}{n}\right).
\tag{24}
\]
Inside a fixed interior neighborhood, this follows by summing log-ratio bounds. Outside it, \(-\log q_l^G(r)\le Cn\), while the squared-distance term is at least a constant times \(n\).

## 4.2 Exact clock matching

Set
\[
\xi_l=\frac{2m_l-l}{l}.
\]
The prescribed coefficient clock satisfies the exact identity
\[
\boxed{
\theta_l=\xi_l^2+
\frac{4(n-1)\sigma_l^2-l(n-l)(1-\xi_l^2)}
{nl(l-1)}.
}
\tag{25}
\]

To derive it, choose two distinct sites \(i_1,i_2\in A\) and two distinct sites \(j_1,j_2\notin A\). The expectation of
\[
(\mathbf1_{i_1\in S}-\mathbf1_{j_1\in S})
(\mathbf1_{i_2\in S}-\mathbf1_{j_2\in S})
\]
is both
\[
\frac{(z-1)^2a_{l-2}}{Z_l}
\]
and
\[
\frac{\mathbb E[X(X-1)+(l-X)(l-X-1)]}{k(k-1)}
-\frac{2\mathbb E[X(l-X)]}{k^2}.
\]
Divide by \(\alpha_l\) and substitute the mean and variance.

The heat overlap has rates
\[
\lambda_r=(l-r)(k-r),\qquad
\mu_r=r(k-l+r),\qquad R(0)=0.
\]
Its drift is \(kl-nr\). The first two moment equations give exactly
\[
\mathbb E_HR=\frac l2(1-e^{-ns}),
\tag{26}
\]
\[
\operatorname{Var}_HR
=
\frac{l(n-l)}{4(n-1)}(1-e^{-2(n-1)s})
+\frac{l^2}{4}e^{-2(n-1)s}(1-e^{-2s}).
\tag{27}
\]

In the macro band, \(\xi_l\) lies in a compact subset of \((0,1)\). Equations (25)–(27), using
\[
e^{-ns_l}=\theta_l^{\,n/[2(n-1)]},
\]
give
\[
|\mathbb E_HR-\mathbb E_GR|\le C,
\qquad
\operatorname{Var}_HR\asymp n.
\tag{28}
\]

On each fixed central window, the leading numerator terms in (25) cancel by (22):
\[
n(\theta_l-\xi_l^2)\longrightarrow0.
\]
Expanding the **exact** power of \(\theta_l\) therefore gives
\[
\mathbb E_HR-\mathbb E_GR
\longrightarrow
\delta_c=-\frac{c\log c}{4},
\tag{29}
\]
and
\[
\frac{\operatorname{Var}_HR}{n}
\longrightarrow
v_H=\frac b4-\frac{c^2\log c}{8},
\qquad
v_G=\frac b4.
\tag{30}
\]

## 4.3 Poisson-binomial heat overlap and entropy tails

The external theorem used is the finite symmetric exclusion preservation theorem of Borcea–Brändén–Liggett: a strongly Rayleigh initial law remains strongly Rayleigh under a finite symmetric exclusion semigroup. citeturn482119view1

Its hypotheses apply to the **conditional** heat channel. The initial generating polynomial is
\[
\frac{e_l((x_i)_{i\in A})}{\binom kl},
\]
which is real stable. The generator is
\[
G_l=\sum_{i<j}(\tau_{ij}-I),
\]
with nonnegative symmetric rates. Specializing the evolved generating polynomial to \(x_i=1\) on \(A\) and \(x_i=t\) outside \(A\) yields a real-rooted probability polynomial with nonnegative coefficients. Its roots are nonpositive, so it factors into Bernoulli probability polynomials.

Thus \(R\) under the heat law is exactly a sum of at most \(n\) independent Bernoulli variables. No strong-Rayleigh assertion about the latent heat mixture is needed.

For completeness, if \(Y_n\) is any such Bernoulli sum with variance \(V_n\ge an\), then uniformly over these arrays,
\[
H(Y_n)=\frac12\log(2\pi eV_n)+o(1).
\tag{31}
\]

Here is the needed entropy-tail argument. Its characteristic function satisfies
\[
|\chi(t)|\le e^{-2V_n\sin^2(t/2)}.
\]
At \(t=u/\sqrt{V_n}\), the logarithmic expansion has remainder \(O(|u|^3/\sqrt n)\) on bounded intervals. Fourier inversion gives the uniform lattice local CLT and
\[
\max_j\Pr(Y_n=j)\le C/\sqrt{V_n}.
\]

Let \(r_j\) be the normalized discrete Gaussian proportional to
\[
e^{-(j-\mathbb EY_n)^2/(2V_n)}.
\]
For a tail set \(T\), write \(P_T=\sum_Tp_j\), \(R_T=\sum_Tr_j\). Log-sum gives
\[
\sum_Tp_j\log(r_j/p_j)
\le P_T\log(R_T/P_T)\le R_T/e.
\]
The upper tail of \(H(Y_n)-\tfrac12\log V_n\) is therefore bounded by
\[
CP_T+
\frac{\mathbb E[(Y_n-\mathbb EY_n)^2;T]}{2V_n}
+R_T/e.
\]
The lower tail is bounded below by \(-CP_T\), using the maximum-mass bound. Hoeffding concentration controls these quantities uniformly for
\[
T=\{|Y_n-\mathbb EY_n|>K\sqrt{V_n}\}.
\]
Letting \(K\to\infty\) proves uniform integrability and (31).

Applying (31) to the heat overlap, and integrating (23) using (24) and the same concentration, gives
\[
D(p_l^H\Vert q_l^G)
\longrightarrow
\frac12\left(\frac{v_H}{v_G}-1-\log\frac{v_H}{v_G}\right)
=D_c,
\]
uniformly on every fixed central layer window. This proves (17).

Throughout the macro band, the maximum-mass estimate gives
\[
H(p_l^H)\ge\tfrac12\log n-C,
\]
while (24) and (28) give cross-entropy at most \(\tfrac12\log n+C\). Hence
\[
D(p_l^H\Vert q_l^G)\le C.
\tag{32}
\]

---

# 5. The new third-difference transport estimate

An \(O(1)\) KL bound by itself does not control layer differences. The following matrix estimate supplies the missing regularity.

## 5.1 Signed triple-difference bound

Let \(\Lambda\) be any Hermitian matrix satisfying
\[
I\preceq\Lambda\preceq zI,
\qquad
\ell(T)=\log\det\Lambda_T.
\]
Let \(\delta_{ij}\ell(T)\) and \(\delta_{ijk}\ell(T)\) denote second and third inclusion-exclusion differences at distinct sites outside \(T\).

After taking the Schur complement \(M\) over \(T\), normalize by its diagonal:
\[
R_{ij}=\frac{M_{ij}}{\sqrt{M_{ii}M_{jj}}}.
\]
Then
\[
z^{-1}I\preceq R\preceq zI,\qquad R_{ii}=1.
\]
The two-site formula gives
\[
\delta_{ij}\ell(T)=\log(1-|R_{ij}|^2),
\]
and therefore
\[
\sum_{j\ne i}|\delta_{ij}\ell(T)|\le C_z.
\tag{33}
\]

The stronger estimate is: for every remaining \(i\) and any two subsets \(J,K\) of remaining sites,
\[
\boxed{
\left|
\sum_{\substack{j\in J,\ k\in K\\i,j,k\ {\rm distinct}}}
\delta_{ijk}\ell(T)
\right|\le C_z.
}
\tag{34}
\]
This is a signed double-row estimate—not a bound on the absolute sum of every triple term.

To prove it, put
\[
a=R_{ij},\qquad d=R_{ik},\qquad e=R_{jk},
\qquad A=|a|^2,\ B=|d|^2,\ C=|e|^2.
\]
The exact three-site expression is
\[
\delta_{ijk}\ell(T)
=
\log(1-A-B-C+2\Re(ae\bar d))
-\log(1-A)-\log(1-B)-\log(1-C).
\]

All determinants and products here have positive lower bounds depending only on \(z\). Subtracting \((1-A)(1-B)(1-C)\), then applying Taylor’s formula to the logarithm, gives
\[
\delta_{ijk}\ell(T)
=2\Re(R_{ij}R_{jk}R_{ki})+E_{ijk},
\]
where
\[
|E_{ijk}|\le C_z
\left(
|R_{ij}|^2|R_{ik}|^2+
|R_{ij}|^2|R_{jk}|^2+
|R_{ik}|^2|R_{jk}|^2
\right).
\tag{35}
\]

For an explicit remainder check, the determinant minus the product is
\[
2\Re(ae\bar d)-(AB+AC+BC)+ABC.
\]
Its square is bounded by a constant times \(AB+AC+BC\), and
\[
\sqrt{ABC}(A+B+C)\le AB+AC+BC.
\]
These bounds prove (35).

The signed leading sum is a masked matrix product
\[
R_{i,*}\Pi_JR\Pi_KR_{*,i},
\]
bounded by an operator norm and two row Euclidean norms. Removing repeated indices costs only a bounded amount. Each absolute remainder sum is bounded using
\[
\sum_j|R_{ij}|^2\le z^2.
\]
This proves (34).

## 5.2 Population averages inherit a third-order bound

For fixed \(A\), average \(\ell(S)\) over uniform choices of \(h\) sites in \(A\) and \(r\) sites outside it; then average over \(A\sim\nu\). Call the result \(a_n(h,r)\).

Uniform subset extension expresses every pure or mixed finite difference of \(a_n\) as the corresponding averaged inclusion-exclusion difference of \(\ell\).

If the relevant population sizes are at least \(\epsilon n\), (33)–(34) imply
\[
|\Delta a_n|\le\beta,\qquad
|\Delta^2a_n|\le \frac{C_{z,\epsilon}}n,\qquad
|\Delta^3a_n|\le \frac{C_{z,\epsilon}}{n^2}.
\tag{36}
\]
For the third estimate, sum (34) first over the first chosen site. The numerator is \(O(n)\); the number of ordered triples is \(\Theta

