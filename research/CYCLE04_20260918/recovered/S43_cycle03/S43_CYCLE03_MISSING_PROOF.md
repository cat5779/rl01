## Count-Stein/Gibbs curvature and the actual count weights

Fix \(0<c<1\) and even \(n=2k\ge4\). All constants and limits below are for fixed \(c\). Set
\[
p=\frac{1+c}{2},\quad q=\frac{1-c}{2},\quad
b=pq=\frac{1-c^2}{4},\quad z=(p/q)^2,\quad\beta=\log z.
\]
Let \(P=UU^*\), where \(U_{jr}=n^{-1/2}e^{2\pi ijr/n}\), \(0\le j<n\), \(0\le r<k\), and let \(\nu(A)=\det P_A\) on \(k\)-sets. Define
\[
\Lambda=I+(z-1)P,\quad \ell(S)=\log\det\Lambda_S,\quad
Z_l=[t^l](1+t)^k(1+zt)^k,
\]
\[
\gamma_l(S)=\frac{\det\Lambda_S}{Z_l},\qquad
\mathscr F_l=D(\gamma_l\Vert u_l).
\]
These are comparison laws, not an identification with the corrected heat laws.

The **actual** count probabilities and coefficients are
\[
\sum_l\pi_l(a,c)t^l
=[1-a-c+(a+c)t]^k[1-a+at]^k,\qquad
\pi_l=\pi_l(q,c),
\]
\[
B_m=\sum_{i\ne j}\Pr\left(\sum_{a\notin\{i,j\}}Z_a=m\right),
\quad w_l=B_{l-1}-B_{l-2},\quad
\kappa_l=B_l-2B_{l-1}+B_{l-2},
\tag{1}
\]
where the independent count bits \(Z_a\) have parameters \(p\) on the first \(k\) sites and \(q\) on the others, and \(B_m=0\) outside \([0,n-2]\). Differentiating the count polynomial twice gives
\[
\kappa_l=\partial_a^2\pi_l(q,c),\quad
\sum_l\kappa_l=0,\quad \sum_mB_m=n(n-1).
\]
For the frozen corrected entropies \(F_l\),
\[
W_n=\sum_{l=0}^n\kappa_lF_l
=\sum_{m=0}^{n-2}B_m\Delta^2F_m
=-2\sum_{l=2}^kw_l(F_l-F_{l-1}).
\tag{2}
\]
The last equality uses \(F_{n-l}=F_l\) and the prescribed zero entropies at \(0,1,n-1,n\). No layer law is differentiated in (2).

### Finite count-Stein certificate

Since \(\pi_l=b^kz^{-l/2}Z_l\), form
\[
Q(S)=\pi_{|S|}\gamma_{|S|}(S)
=b^kz^{-|S|/2}\det\Lambda_S.
\]
Conditional on \(A\sim\nu\), take independent bits \(Y_i\) with probabilities \(p\) on \(A\) and \(q\) outside. For \(|S|=l\), their conditional atom probability is
\[
b^kz^{|A\cap S|-l/2}.
\]
Cauchy–Binet gives \(\mathbb E_\nu z^{|A\cap S|}=\det\Lambda_S\), proving this representation of \(Q\).

Write \(N=\sum_iY_i\), \(X=N-k\), and
\[
\partial_if=f(Y_{-i},1)-f(Y_{-i},0).
\]
For every real function on the finite cube, conditional Bernoulli integration by parts gives
\[
\boxed{\mathbb E_Q[Xf]=b\sum_i\mathbb E_Q\partial_if.}
\tag{3}
\]
Indeed, all conditional Bernoulli variances equal \(b\), and their conditional means sum to \(k\).

Let \(Y^i\) denote the configuration with bit \(i\) flipped and
\(\mathcal Lf=\sum_i[f(Y^i)-f(Y)]\). The pointwise identity
\[
\partial_i(Xf)=X\partial_if+f(Y^i)
\]
and two applications of (3), with \(\partial_{ii}f=0\), give
\[
\boxed{
\operatorname{Cov}(X^2,f)
=b^2\sum_{i\ne j}\mathbb E\partial_{ij}f+b\mathbb E\mathcal Lf.
}
\tag{4}
\]
Here \(\mathbb EX^2=nb\), also obtained from (3).

Define the natural count tilt and its entropy deficit by
\[
Q_t=\frac{e^{tX}Q}{\mathbb E_Qe^{tX}},\quad
m_t=\mathbb E_{Q_t}N/n,\quad
\mathcal D_n(t)=D(Q_t\Vert\operatorname{Ber}(m_t)^{\otimes n}).
\]
At zero, \(m_0=1/2\), \(m'_0=b\). Exact finite differentiation of
\(\mathcal D_n(t)=nH_{\rm Ber}(m_t)-H(Q_t)\) gives
\[
\mathcal D_n''(0)=\operatorname{Cov}(X^2,\log Q)+nbc^2.
\tag{5}
\]
For example, \(H(Q_t)=-\mathbb E_t\log Q-t\mathbb E_tX+
\log\mathbb E_Qe^{tX}\), whose second derivative at zero is
\(-\operatorname{Cov}(X^2,\log Q)-nb\). The Bernoulli-entropy term contributes \(-4nb^2\).

Set
\[
r_i=Q(Y_i=1\mid Y_{-i}),\quad
h_i=\log\frac{r_i}{1-r_i},\quad x_i=2r_i-1,\quad
v_i=\mathbb E[r_i(1-r_i)].
\]
The conditional mixture gives \(q\le r_i\le p\). Moreover, \(Q\) is log-submodular. In fact, for a Schur complement \(M\) of \(\Lambda\),
\[
\partial_{ij}\log Q
=\log\left(1-\frac{|M_{ij}|^2}{M_{ii}M_{jj}}\right)\le0.
\]
Thus \(\partial_jr_i\le0\) for \(j\ne i\), and \(h_i=\partial_i\log Q\).
Conditioning on \(Y_{-i}\) gives
\(\mathbb E\mathcal L\log Q=-\sum_i\mathbb E[x_ih_i]\). Consequently (4)–(5) imply
\[
\boxed{
\mathcal D_n''(0)
=b^2\sum_{i\ne j}\mathbb E\partial_jh_i
-b\sum_i\mathbb E[x_ih_i]+nbc^2.
}
\tag{6}
\]

Applying (3) to \(r_i\), which is independent of its own coordinate, yields
\[
b\sum_{j\ne i}\mathbb E\partial_jr_i
=\operatorname{Cov}(N,r_i)=b-v_i.
\tag{7}
\]
For the last equality, (3) with \(f=Y_i\) gives \(\operatorname{Cov}(N,Y_i)=b\), while conditional expectation shows
\(\operatorname{Cov}(N,Y_i-r_i)=v_i\).

On \([q,p]\), the derivative of the logit lies between \(4\) and \(1/b\). Because the increments of \(r_i\) are nonpositive,
\[
\frac1b\partial_jr_i\le\partial_jh_i\le4\partial_jr_i.
\tag{8}
\]
Using the upper inequality, (6)–(7), and \(4b+c^2=1\),
\[
\mathcal D_n''(0)
\le b\sum_i\mathbb E[x_i^2-x_ih_i]
\le-b\sum_i\mathbb Ex_i^2,
\tag{9}
\]
since \(x\log((1+x)/(1-x))\ge2x^2\) for \(|x|<1\).
Using the lower inequality, \(v_i\le1/4\), and
\(x_ih_i\le c\log(p/q)\), gives
\[
\begin{aligned}
\mathcal D_n''(0)
&\ge\sum_i(b-v_i)-b\sum_i\mathbb E[x_ih_i]+nbc^2\\
&\ge-n\left(\frac{c^4}{4}+bc\log\frac pq\right).
\end{aligned}
\tag{10}
\]

The law \(Q\) has \(L\)-matrix \(z^{-1/2}\Lambda\), hence kernel
\(K=qI+cP\). Thus
\[
\mathbb EY_i=\tfrac12,\quad
\operatorname{Cov}(Y_i,Y_j)=-c^2|P_{ij}|^2\quad(i\ne j).
\]
For neighboring cyclic sites,
\[
|P_{i,i+1}|=\frac1{n\sin(\pi/n)}.
\]
Since \(Y_j\) is measurable with respect to \(Y_{-i}\), Cauchy–Schwarz gives
\[
\mathbb Ex_i^2=4\operatorname{Var}(r_i)
\ge16\operatorname{Cov}(Y_i,Y_j)^2
=\frac{16c^4}{n^4\sin^4(\pi/n)}.
\tag{11}
\]
Therefore, for every even \(n\ge4\),
\[
\boxed{
-\left(\frac{c^4}{4b^2}+\frac cb\log\frac pq\right)
\le\frac{\mathcal D_n''(0)}{nb^2}
\le-\frac{16c^4}{bn^4\sin^4(\pi/n)}.
}
\tag{12}
\]
This is the finite signed certificate producing \(L_c\) and, in the limit, \(A_c\).

## Converting field curvature to the actual Gibbs count response

### Layer regularity needed for the conversion

Here are the precise inputs from the recovered argument's overlap and second-difference estimates. For a sufficiently small fixed \(\eta>0\), say \(\eta<q/4\), in \((1-\eta)k\le l\le k\), the Gibbs overlap \(H=|A\cap S|\) has variance \(O(n)\), Gaussian tails, and
\[
\mathbb E_GH=pk-\frac r2+O(1+r^2/n),\qquad r=k-l.
\tag{13}
\]
If \(a_n(h,j)\) averages \(\ell(S)\) over uniform selections of \(h\) points of \(A\) and \(j\) of \(A^c\), and then over \(A\sim\nu\), its first differences are globally bounded and its pure and mixed second differences are \(O(n^{-1})\) in fixed interior population rectangles. These are inputs from the omitted earlier estimates, not an assumption of S45's pending conclusion.

Define \(a_n^\circ(h,j)=a_n(h,j)-\beta(h+j)/2\). The Fourier complement identities give
\[
a_n^\circ(h,j)=a_n^\circ(k-j,k-h).
\tag{14}
\]
Choose integers \(h_0+j_0=k\) with \(h_0\) nearest \(pk\). Then
\(a_n^\circ(h_0+t,j_0+t)\) is even in \(t\) and has second difference \(O(n^{-1})\). Evenness bounds its first increment, and summation gives displacement \(O(t^2/n)\).

Replacing the Gibbs overlap by its mean costs \(O(1)\), by the second-difference bound, variance bound, and tails. Equation (13) costs another \(O(1+r^2/n)\); one coordinate step pays odd \(r\).

For the count law \(\pi_l=[t^l]\{b+(1-2b)t+bt^2\}^k\), exponential tilting to mean \(l\) in this band keeps all Bernoulli parameters in a fixed compact subset of \((0,1)\). Its mass at the tilted mean is between \(c_1/\sqrt n\) and \(c_2/\sqrt n\), uniformly, by Fourier inversion. The rate function has second derivative \(1/\operatorname{Var}_tN=O(n^{-1})\). Thus
\[
|\log\pi_{k-r}-\log\pi_k|\le C(1+r^2/n).
\]
Adjacent binomial ratios likewise give
\(|\log\binom n{k-r}-\log\binom nk|\le Cr^2/n\).
Since
\[
\mathscr F_l=\mathbb E_Ga_n^\circ(H,l-H)
+k\log b+\log\binom nl-\log\pi_l,
\]
we obtain
\[
\boxed{|\mathscr F_l-\mathscr F_k|
\le C\left(1+\frac{(l-k)^2}{n}\right)\quad(0\le l\le n).}
\tag{15}
\]
Symmetry gives the upper band; outside the bands, \(0\le\mathscr F_l\le n\log2\) gives the same envelope. No entropy approximation has been differentiated.

### Exact count differentiation and the count-only correction

Let \(\dot\pi_l=d\pi_l(q(c),c)/dc\): the high and low Bernoulli parameters have velocities \(1/2\) and \(-1/2\). Only counts vary. Direct product differentiation yields
\[
\boxed{
\kappa_l=\left(\frac{(l-k)^2}{b^2}-\frac nb\right)\pi_l
+\frac{2c}{b}\dot\pi_l.
}
\tag{16}
\]
Explicitly, the first \(a\)-score is \(X/b\). If \(T\) is the balanced \(c\)-score, the derivative of the first \(a\)-score with respect to \(a\) at the midpoint is \(-n/b+(2c/b)T\), proving (16).
The full score \(T\) has variance \(n/(4b)\). Conditioning on \(N\), Cauchy–Schwarz, (15), and the fourth count moment give
\[
\left|\sum_l\dot\pi_l\mathscr F_l\right|
\le\sqrt{\frac n{4b}}\,
\bigl[\mathbb E_\pi(\mathscr F_N-\mathscr F_k)^2\bigr]^{1/2}
=O(\sqrt n)=o(n).
\tag{17}
\]

Under \(Q_t\), the law conditional on \(N=l\) stays \(\gamma_l\). Therefore
\[
\mathcal D_n(t)=\mathbb E_{\pi_t}\mathscr F_N
+R_n(t),\qquad
R_n(t)=D(\pi_t\Vert\operatorname{Bin}(n,m_t)).
\tag{18}
\]
At zero, \(\mathbb EX=0\), \(\mathbb EX^2=nb\), \(\mathbb EX^3=0\). Exact finite differentiation gives
\[
R_n''(0)=\operatorname{Cov}\left(X^2,
\log\frac{\pi_N}{\operatorname{Bin}(n,1/2)(N)}\right)+nbc^2.
\tag{19}
\]
This also follows by writing
\(R_n=-H(\pi_t)-\mathbb E_t\log\binom nN+nH_{\rm Ber}(m_t)\)
and differentiating each finite sum.

Uniformly for bounded \(y=(l-k)/\sqrt n\), the count local limits give
\[
\log\frac{\pi_l}{\operatorname{Bin}(n,1/2)(l)}
=-\tfrac12\log(4b)+\left(2-\frac1{2b}\right)y^2+o(1).
\tag{20}
\]
In a fixed macro band its difference from the central value is bounded by \(C(1+y^2)\), by the tilting argument above. Outside that band it is \(O(n)\), while count probability is exponentially small. Hoeffding concentration therefore gives uniform integrability after multiplication by \(y^2\). Since \(X/\sqrt n\) converges to \(N(0,b)\) with its moments, (19) implies
\[
\frac{R_n''(0)}n\longrightarrow
\left(2-\frac1{2b}\right)2b^2+bc^2=0.
\]
Using (16)–(18),
\[
\boxed{W_n^G:=\sum_l\kappa_l\mathscr F_l
=\frac{\mathcal D_n''(0)}{b^2}+o(n).}
\tag{21}
\]
In particular, (12) proves
\[
\boxed{
-L_c\le\liminf\frac{W_n^G}{n}
\le\limsup\frac{W_n^G}{n}\le-A_c,
\quad
L_c=\frac{c^4}{4b^2}+\frac cb\log\frac pq,
\quad A_c=\frac{16c^4}{b\pi^4}.
}
\tag{22}
\]
All limits are along even \(n\). Equation (21), rather than an unproved interchange of derivatives, pays the actual-count/field discrepancy.

## Corrected-law transport, every tail, and signed assembly

For \(2\le l\le k\), \(\mu_l\) is the original-rate slice heat law from a uniform \(l\)-subset of the latent \(A\), at the **exact** time
\[
s_l=-\frac{\log\theta_l}{2(n-1)},\qquad
\theta_l=\frac{(z-1)^2[t^{l-2}](1+t)^{k-2}(1+zt)^{k-2}}
{[l(l-1)/(k(k-1))]Z_l}.
\]
Use complementary layers above \(k\), and the prescribed uniform endpoint layers. Put
\[
F_l=D(\mu_l\Vert u_l),\quad U_l=D(\mu_l\Vert\gamma_l),\quad
v_l=\mathbb E_{\mu_l}\ell-\mathbb E_{\gamma_l}\ell.
\]
The exact logarithmic identity is
\[
\boxed{F_l=\mathscr F_l+U_l+v_l.}
\tag{23}
\]
If \(p_l^H,q_l^G\) denote the heat and Gibbs laws of \(|S\cap A^c|\), uniformity within overlap orbits and the KL chain rule give
\[
0\le U_l\le D(p_l^H\Vert q_l^G).
\tag{24}
\]

The earlier radial and evidence estimates enter here in precisely this form: for some fixed \(\eta,C>0\), throughout \(|l-k|\le\eta k\),
\[
D(p_l^H\Vert q_l^G)\le C,\qquad |v_l|\le C,
\]
and, for every finite \(K\), uniformly on \(|l-k|\le K\sqrt n\),
\[
D(p_l^H\Vert q_l^G)=D_c+o_K(1),\qquad v_l-v_k=o_K(1),
\tag{25}
\]
where
\[
\rho_c=1-\frac{c^2\log c}{2b},\qquad
D_c=\tfrac12(\rho_c-1-\log\rho_c).
\]
These are the exact-clock radial KL and third-difference evidence-flatness inputs. The radial proof's external input was strong-Rayleigh preservation under finite symmetric exclusion; no S45 conclusion is assumed. Statement (25) is not an assertion that \(U_l\) converges or has a signed derivative.

For completeness, the actual-weight input needed to pay the complement is
\[
\frac1n\sum_l(\kappa_l)_+\to M_b,
\quad \frac1n\sum_l|\kappa_l|\to2M_b,
\quad M_b=\frac{2e^{-1/2}}{\sqrt{2\pi}\,b},
\tag{26}
\]
\[
\frac1n\sum_{|l-k|>K\sqrt n}|\kappa_l|
\left(1+\frac{(l-k)^2}{n}\right)\le\frac{C_b}{K^2}
\qquad(K\ge1).
\tag{27}
\]
Here is the exact normalization behind those inputs. With
\[
\phi(t)=b+(1-2b)t+bt^2,\quad
\eta_k=\frac{k-1+2b}{2(2k-1)},\quad
\psi_k(t)=\eta_k+(1-2\eta_k)t+\eta_kt^2,
\]
\[
\sum_m\frac{B_m}{n(n-1)}t^m=\phi(t)^{k-2}\psi_k(t).
\]
The positive-linear-factor sign-variation argument gives the coefficient sign pattern \(+,-,+\) for \(\kappa\). Thus
\(\sum(\kappa_l)_+=2\max_m(B_m-B_{m-1})\).
Fourier inversion gives
\((B_{k-r-1}-B_{k-r-2})/n\to
x\varphi_b(x)/b\) for \(r/\sqrt n\to x\), uniformly over the lattice, where \(\varphi_b\) is the \(N(0,b)\) density. Its maximum is \(e^{-1/2}/(\sqrt{2\pi}b)\), proving (26).

The negative coefficients lie within \(|l-k|\le K_0\sqrt n+2\) for any fixed \(K_0>\sqrt b\) and sufficiently large \(n\). Exact summation gives
\[
\sum_l\kappa_l(l-k)^4=n(n-1)(12V_B+2),\qquad
V_B=(n-4)b+2\eta_k.
\]
Together with (26) and that localization, this bounds
\(n^{-1}\sum_l|\kappa_l|[1+((l-k)/\sqrt n)^4]\)
uniformly, and implies (27). Thus the complement payment is for the actual coefficients, not substituted Gaussian weights.

Globally, \(\det\Lambda_S\ge1\), \(Z_l\le2^nz^n\), and \(0\le\ell(S)\le n\beta\). Hence \(U_l\le Cn\), \(|v_l|\le n\beta\). Combining this with the macro-band bounds,
\[
U_l+|v_l-v_k|\le C\left(1+\frac{(l-k)^2}{n}\right)
\quad\text{on every layer}.
\tag{28}
\]
Since \(\sum_l\kappa_l=0\), (25)–(28) give
\[
\frac1n\sum_l\kappa_lv_l
=\frac1n\sum_l\kappa_l(v_l-v_k)\longrightarrow0:
\]
for fixed \(K\), the central contribution is \(o_K(1)\), and the remaining absolute contribution is at most \(C/K^2\).

On the central window, \(0\le U_l\le D_c+o_K(1)\). Nonnegativity therefore bounds the positive and negative coefficient contributions separately by
\((D_c+o_K(1))\sum_l(\kappa_l)_+\).
The complementary contribution is again at most \(Cn/K^2\). Taking first \(n\to\infty\), then \(K\to\infty\), proves
\[
\boxed{
-M_bD_c\le\liminf\frac1n\sum_l\kappa_lU_l
\le\limsup\frac1n\sum_l\kappa_lU_l\le M_bD_c.
}
\tag{29}
\]

There is no missing boundary term. All sums run over \(0\le l\le n\); at \(0,1,n-1,n\), both \(\mu_l\) and \(\gamma_l\) are uniform, so \(F_l,\mathscr F_l,U_l,v_l\) vanish. The one-point Gibbs law is uniform because \(P_{ii}=1/2\), and the \((n-1)\)-point law follows by complement symmetry. If the sum is paired around \(k\), the central term is removed by subtracting the central value using \(\sum\kappa_l=0\), not by discarding it. All other layers are covered by (27)–(28).

Combining (21)–(23) and (29),
\[
\boxed{
-L_c-M_bD_c
\le\liminf_{n\to\infty,\ n\ {
m even}}\frac{W_n}{n}
\le\limsup_{n\to\infty,\ n\ {
m even}}\frac{W_n}{n}
\le-A_c+M_bD_c.
}
\tag{30}
\]
Equivalently, for every fixed \(c\in(0,1)\) and \(\varepsilon>0\), these lower and upper bounds with an additional \(\varepsilon\) slack hold for every even \(n\ge N(c,\varepsilon)\).

## Analytic positivity at \(c=19/20\) and scope

For \(x=c^2\in(0,1)\),
\[
\rho_c=1-\frac{x\log x}{1-x}\in(1,2),
\]
because \(-x\log x<1-x\). Therefore
\[
0<D_c<\frac{1-\log2}{2}<\frac16,
\qquad bM_b=\sqrt{\frac2{\pi e}}<\frac12.
\]
At \(c=19/20\), \(c^4>4/5\) and \(\pi^4<100\), so
\[
\boxed{
b(A_c-M_bD_c)>
\frac{16}{125}-\frac1{12}=\frac{67}{1500}>0.
}
\tag{31}
\]
Thus (30) yields the recovered author conclusion \(-W_n=\Theta(n)\) at \(c=19/20\). In explicit quantifiers, writing \(\delta=A_c-M_bD_c>0\), for all sufficiently large even \(n\),
\[
\frac\delta2\,n\le -W_n\le(L_c+M_bD_c+1)n.
\]
No limit of \(W_n/n\) is asserted. Its exact coefficient still requires the limiting conditional-odds susceptibility in (6) and the signed output-KL contribution, rather than the interval (29).

**CORRECTED_LAW_ONLY.** This supplies no comparison with the separate clock-acceleration term \(C_n\), no conclusion about \(W_n+C_n\), and no resolution of the ultimate true full-configuration entropy-rate target for all \(0<c<1\) and densities \(0<\rho<1\).

Source: the existing cycle-03 `S43_RESULT.md`, principally its original sections 6–9, with the Stein part placed first and intermediate algebra expanded. No newly repaired mathematical argument is being substituted. The earlier inputs are stated explicitly in (13)–(14) and (25)–(27); this source delivery is not independent certification of them or of the assembled theorem.
