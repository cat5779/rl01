# S72 result

Files:

- :chatgpt-content-reference{index="7"}
- :chatgpt-content-reference{index="8"}

The supplied packet’s exact score identities, logarithmic domains, martingale interface, and finite-to-true theorem were used only within their independently reviewed fixed-gap scope. In particular, the packet proves \(H_n''=-\mathbb E\Phi(G_n)\), \(F_{eo,n}=-\mathbb E\Chi(G_n)\), the actual score martingale, and the common fixed-sign interpolation domain. citeturn558044view1turn558044view2turn558044view3turn235241view0

## Main result

Fix \(0<c<1\), \(0<\rho<1\), and a compact interval \(J\Subset(0,1-c)\). Set

\[
\delta=\min_{a\in J}\min\{a,1-a-c\},
\qquad
\kappa=\frac{c^2}{4\delta(\delta+c)},
\qquad
\theta=\frac{\kappa}{1+\kappa},
\]

\[
\beta_\delta=\frac{1-2\delta}{\delta},
\qquad
\eta_\delta=\frac{\beta_\delta}{2}
=\frac1{2\delta}-1,
\qquad
C_{\log}=\max\{1,\log(1+\kappa)\}.
\]

For \(\lambda>0\), define

\[
A_\lambda=2\kappa+4\theta(1+\lambda),
\qquad
B_\lambda=\theta\beta_\delta(1+\lambda^{-1}),
\]

and

\[
C_\Phi=\inf_{\lambda>0}
\max\{A_\lambda,\,2B_\lambda-2\},
\qquad
\Gamma_\Phi=\frac{C_\Phi}{2},
\]

\[
C_\Chi=\inf_{\lambda>0}
\max\{A_\lambda/2,\,B_\lambda\},
\qquad
\Gamma_\Chi=\frac{C_\Chi}{2}.
\]

Then the old arbitrary-Hessian observation payment can be replaced by the following actual-reveal, one-sided payment:

\[
\boxed{
\mathbb E\Psi((G_V)_{II})
-\mathbb E\Psi((G_A)_{II})
\ge
-\Gamma_\Psi\eta_\delta\,
\mathbb E
\sum_{\substack{i\in I\\r\in V\setminus A}}
|G_V(i,r)|^2,
\qquad
\Psi\in\{\Phi,\Chi\}.
}
\tag{1}
\]

The accompanying expected spatial tail is

\[
\boxed{
\frac1{|V|}
\mathbb E\sum_{i,j\in V}
\min\!\left\{\frac{|i-j|}{R},1\right\}|G_V(i,j)|^2
\le
\widehat\tau(R),
}
\tag{2}
\]

where

\[
\boxed{
\widehat\tau(R)=
\min\left\{
\frac2\delta-4,\,
\frac{4c^2}{\pi^2\delta^3}
\frac{H_{R-1}+2}{R}
\right\}.
}
\tag{3}
\]

Consequently, with

\[
\widehat B=\frac{2C_{\log}}{\delta},
\]

\[
\widehat\epsilon^\Phi_{m,L}
=
C_{\log}\widehat\tau(m)
+\Gamma_\Phi\eta_\delta\widehat\tau(L+1),
\]

\[
\widehat\epsilon^\Chi_{m,L}
=
C_{\log}\widehat\tau(m)
+\Gamma_\Chi\eta_\delta\widehat\tau(L+1),
\]

the original Shannon entropy satisfies

\[
\boxed{
\frac{H_n''(a)}n
\le
W_{m,L}(a)+\widehat\epsilon^\Phi_{m,L}
+4\widehat B\frac{m+L}{n}.
}
\tag{4}
\]

At \(\rho=1/2\),

\[
\boxed{
-\frac{F_{eo,n}(a)}n
\ge
V_{m,L}(a)-\widehat\epsilon^\Chi_{m,L}
-4\widehat B\frac{m+L}{n}.
}
\tag{5}
\]

The accepted fixed-gap result already identifies the limit of \(H_n''/n\) with \(h''\); alternatively, a strict continuous-parameter inequality in (4) can be integrated at finite volume and passed to the entropy-value limit, avoiding differentiation of an \(o(n)\) value error. citeturn235241view2turn235241view3turn488637view1

Thus

\[
\boxed{
h''(a)\le
W_{m,L}(a)+\widehat\epsilon^\Phi_{m,L}.
}
\tag{6}
\]

At the separately justified half-density benchmark \(c=19/20\),

\[
\boxed{
h''(a)
\le
-\frac1{50}-2V_{m,L}(a)
+2\widehat\epsilon^\Chi_{m,L}.
}
\tag{7}
\]

The baseline and its original two-sided interface are exactly those recorded in the reviewed packet. citeturn235241view4turn235241view5turn558044view9

---

## Why the new bound holds

### 1. Signed Ward coercivity

For an actual word, let

\[
A_Y=K-\operatorname{diag}(1-Y),
\qquad
G=A_Y^{-1},
\qquad
S=\operatorname{diag}(2Y-1).
\]

Define

\[
R_Y=\frac{SG+GS}{2}.
\]

Since

\[
A_Y=\frac12S+E,
\qquad
\|E\|\le\frac12-\delta,
\]

for \(x=Gz\),

\[
z^*R_Yz
=
x^*\frac{A_YS+SA_Y}{2}x
=
x^*\left(\frac12I+\frac{ES+SE}{2}\right)x
\ge
\delta\|x\|^2.
\]

Therefore

\[
\boxed{R_Y\succeq\delta G^2.}
\tag{8}
\]

There is also an exact actual-law identity

\[
\boxed{\mathbb E R_Y=2I.}
\tag{9}
\]

For the diagonal, conditioning on \(Y_{-i}\) with conditional success probability \(p\) gives

\[
(2Y_i-1)G_{ii}
=
\begin{cases}
1/p,&Y_i=1,\\[2mm]
1/(1-p),&Y_i=0,
\end{cases}
\]

whose conditional expectation is \(2\).

For \(i\neq j\), condition on every output except \(Y_i,Y_j\), and write the conditional two-site kernel as

\[
C=\begin{pmatrix}\alpha&z\\\bar z&\beta\end{pmatrix}.
\]

For word \(11\),

\[
\pi_{11}G_{ij}^{11}=-z,
\]

and for word \(00\),

\[
\pi_{00}G_{ij}^{00}=-z.
\]

The coefficient \((\sigma_i+\sigma_j)/2\) is \(+1\) for \(11\), \(-1\) for \(00\), and zero for the two opposite-sign words, so the off-diagonal expectation cancels.

Taking expectations in (8) yields

\[
\boxed{\mathbb E G^2\preceq\frac2\delta I.}
\tag{10}
\]

Pointwise, taking a diagonal entry in (8) gives

\[
\delta\sum_j|G_{ij}|^2
\le
u_i,
\qquad
u_i=(2Y_i-1)G_{ii}.
\tag{11}
\]

This is the coercivity that is missing from the old arbitrary-direction estimate.

### 2. Exact reachable rank-one sign geometry

Along an actual reveal, the core increment direction is \(D=ww^*\). Put

\[
t_i=|w_i|^2,\qquad
u_i=\sigma_iX_{ii},\qquad
s=u_iu_j,
\qquad
r=\frac{|X_{ij}|^2}{u_iu_j},
\qquad
\alpha_i=\frac{t_i}{u_i}.
\]

The packet’s exact pair Hessian identity is

\[
f''=(g-rg')s''+g'h''
+\frac{g''}{s}(h'-rs')^2.
\]

Specializing this identity to \(D=ww^*\) gives an exact sign dichotomy.

For equal output signs,

\[
D^2f_{ij}(X)[D,D]
=
2r\,t_it_j+
\frac{s}{1-r}
\left(
2\sqrt{r\alpha_i\alpha_j}\cos\omega
-\sigma_i r(\alpha_i+\alpha_j)
\right)^2
\ge0.
\tag{12}
\]

For opposite output signs,

\[
D^2f_{ij}(X)[D,D]
=
-2r\,t_it_j-
\frac{s}{1+r}
\left(
2\sqrt{r\alpha_i\alpha_j}\cos\omega
-r(\alpha_i-\alpha_j)
\right)^2
\le0.
\tag{13}
\]

Thus all negative reachable curvature comes from opposite actual output signs. This is strictly stronger structural information than a bound on arbitrary Hermitian directions.

The row coercivity survives the reveal interpolation by convexity:

\[
\sum_{j\in I}|X_{ij}|^2\le\frac{u_i}{\delta}.
\]

Subtracting the diagonal term gives the actual row weight

\[
\sum_{j\ne i}\frac{|X_{ij}|^2}{u_i^2}
\le
\frac1{\delta u_i}-1
\le
\beta_\delta.
\tag{14}
\]

Using (13), \((x-y)^2\le(1+\lambda)x^2+(1+\lambda^{-1})y^2\), and the ratio bounds \(r\le\kappa\), \(r/(1+r)\le\theta\), one obtains before uniformization

\[
D^2\Phi(X)[D,D]
\ge
-A_\lambda T^2
+(A_\lambda+2)\sum_i t_i^2
-2\theta(1+\lambda^{-1})
\sum_i\left(\frac1{\delta u_i}-1\right)t_i^2,
\tag{15}
\]

and

\[
D^2\Chi(X)[D,D]
\ge
-\frac{A_\lambda}{2}T^2
+\frac{A_\lambda}{2}\sum_i t_i^2
-\theta(1+\lambda^{-1})
\sum_i\left(\frac1{\delta u_i}-1\right)t_i^2.
\tag{16}
\]

Replacing the actual weights in (15)–(16) by \(\beta_\delta\) and optimizing \(\lambda\) produces \(C_\Phi,C_\Chi\).

### 3. Complete one-reveal remainder

For one reveal,

\[
M_1=M+\frac{vv^*}{q},
\qquad
M_0=M-\frac{vv^*}{1-q}.
\]

The exact complete remainder is

\[
\begin{aligned}
\Delta_\Psi
={}&q\int_0^{1/q}(1/q-t)
D^2\Psi(M+t vv^*)[vv^*,vv^*]\,dt\\
&+(1-q)\int_0^{1/(1-q)}(1/(1-q)-t)
D^2\Psi(M-t vv^*)[vv^*,vv^*]\,dt .
\end{aligned}
\]

The first-order terms cancel with the actual weights \(q\) and \(1-q\). Therefore

\[
\Delta_\Phi
\ge
-\Gamma_\Phi
\frac{\|v\|^4}{q(1-q)},
\qquad
\Delta_\Chi
\ge
-\Gamma_\Chi
\frac{\|v\|^4}{q(1-q)}.
\tag{17}
\]

This permits negative conditional gaps, including the supplied six-site word.

### 4. Actual-\(q\) self-normalization

Let \(v_A\) be the full Schur vector over all previously revealed sites. In the two fine words, the revealed row is

\[
G^{(1)}_{rr}=\frac1q,\qquad
G^{(1)}_{rA}=-\frac{v_A^*}{q},
\]

and

\[
G^{(0)}_{rr}=-\frac1{1-q},\qquad
G^{(0)}_{rA}=\frac{v_A^*}{1-q}.
\]

Applying (11) to these two fine rows, including the diagonal entry, gives

\[
\|v_A\|^2\le\frac q\delta-1,
\qquad
\|v_A\|^2\le\frac{1-q}{\delta}-1.
\]

Hence the core restriction satisfies

\[
\boxed{
\|v\|^2
\le
\omega_\delta(q)
:=
\frac{\min(q,1-q)}{\delta}-1
\le
\eta_\delta.
}
\tag{18}
\]

Furthermore,

\[
q\sum_{i\in I}|G^{(1)}_{ir}|^2
+
(1-q)\sum_{i\in I}|G^{(0)}_{ir}|^2
=
\frac{\|v\|^2}{q(1-q)}.
\]

Thus

\[
\frac{\|v\|^4}{q(1-q)}
\le
\omega_\delta(q)
\left[
q\sum_i|G^{(1)}_{ir}|^2+
(1-q)\sum_i|G^{(0)}_{ir}|^2
\right].
\tag{19}
\]

This retains the actual \(q\) until the final uniform estimate. Revealing the halo successively and applying \(L^2\)-contraction to the score martingale gives (1).

### 5. Expected spatial tail

For an auxiliary diagonal grid-sign matrix \(D\),

\[
[G,D]=-G[K,D]G.
\]

Using (10) after averaging over the actual word,

\[
\mathbb E\|G[K,D]G\|_{HS}^2
\le
2\delta^{-3}\|[K,D]\|_{HS}^2.
\]

Averaging the shifted grid gives the harmonic part of (3). The cap improves because the weight vanishes on the diagonal:

\[
\mathbb E\sum_{j\ne i}|G_{ij}|^2
\le
\frac2\delta-\mathbb E|G_{ii}|^2.
\]

Conditionally,

\[
\mathbb E[|G_{ii}|^2\mid Y_{-i}]
=
\frac1p+\frac1{1-p}\ge4,
\]

so the cap is \(2/\delta-4\), rather than the old \(\delta^{-2}\). The accepted proof’s former deterministic commutator bound and its block-transfer usage are recorded in the packet. citeturn558044view5turn235241view2

---

## Quantitative benchmark

For

\[
c=\frac{19}{20},
\qquad
J=\left[\frac1{50},\frac3{100}\right],
\qquad
\delta=\frac1{50},
\]

one obtains

\[
\kappa=\frac{9025}{776}\approx11.6301546392,
\qquad
\theta=\frac{9025}{9801}\approx0.9208244057,
\]

\[
\beta_\delta=48,
\qquad
\eta_\delta=24,
\qquad
C_{\log}\approx2.5360871801.
\]

The optimized constants are

\[
\lambda_\Phi\approx17.5123893301,
\qquad
\Gamma_\Phi\approx45.7234744440,
\]

\[
\lambda_\Chi\approx18.0169980843,
\qquad
\Gamma_\Chi\approx23.3263932782.
\]

The harmonic tail prefactor is

\[
\frac{4c^2}{\pi^2\delta^3}
=
\frac{451250}{\pi^2}
\approx45721.1841186,
\]

and the cap is \(96\). Therefore the new observation-harmonic products are

\[
\Gamma_\Phi\eta_\delta
\frac{4c^2}{\pi^2\delta^3}
\approx5.0172753\times10^7,
\]

\[
\Gamma_\Chi\eta_\delta
\frac{4c^2}{\pi^2\delta^3}
\approx2.5596248\times10^7.
\]

The packet’s old product is approximately \(1.763690\times10^{15}\), before the harmonic scale factor. citeturn558044view9turn488637view8

This is an improvement by approximately

\[
3.51\times10^7\quad(\Phi),
\qquad
6.89\times10^7\quad(\Chi).
\]

Analytically, as \(\delta\downarrow0\) with \(c\) fixed, the old observation-tail product is \(O_c(\delta^{-10})\), whereas the new one is \(O_c(\delta^{-5})\).

### Remaining certified deficit

At \(m=L=2\),

\[
\widehat\tau(2)=\widehat\tau(3)=96,
\]

so

\[
\widehat\epsilon^\Phi_{2,2}
\approx105590.349488,
\qquad
\widehat\epsilon^\Chi_{2,2}
\approx53987.4744824.
\]

But

\[
|W_{2,2}|,\ |V_{2,2}|
\le
\widehat B
\approx253.608718009.
\]

Therefore, without relying on the floating witness values,

\[
W_{2,2}+\widehat\epsilon^\Phi_{2,2}
\ge105336.740770>0,
\]

and

\[
V_{2,2}-\widehat\epsilon^\Chi_{2,2}
\le-53733.865764<-1/100.
\]

Thus no \(m=L=2\) witness can pay the new bound.

For explicit scale dependence,

\[
\widehat\epsilon^\Phi_{m,L}
\le
115952.908902\frac{3+\log m}{m}
+
50172753.4464
\frac{3+\log(L+1)}{L+1},
\]

\[
\widehat\epsilon^\Chi_{m,L}
\le
115952.908902\frac{3+\log m}{m}
+
25596247.7255
\frac{3+\log(L+1)}{L+1}.
\]

For example,

\[
\widehat\epsilon^\Chi_{20{,}000{,}000,\,
2{,}000{,}000{,}000}<0.428,
\]

and

\[
\widehat\epsilon^\Phi_{20{,}000{,}000,\,
4{,}000{,}000{,}000}<0.430.
\]

The theorem is therefore asymptotically affordable, but the required finite witnesses are currently at scales far beyond the supplied certified enumeration.

---

## Local information identity

For a local parameter \(t\) that shifts only the core diagonals,

\[
\boxed{
\mathbb E\!\left[
q\Phi(M_1)+(1-q)\Phi(M_0)-\Phi(M)
\right]
=
\frac{d^2}{dt^2}
I_t(Y_I;Y_r\mid Y_{A\setminus I}).
}
\tag{20}
\]

This identifies the natural Bellman quantity. It does not give a zero-cost proof:

- the identity is actual-law averaged, not wordwise;
- the global \(a\)-path also moves halo and exterior diagonals;
- the corresponding mixed/background derivatives have not been signed.

The certified six-site example disproves only universal wordwise zero-payment Jensen. Its interval enclosures are

\[
\Delta\Phi\in
[-0.106585307859143407,-0.106585307859143406],
\]

\[
Q\in
[0.170309619791317635,0.170309619791317636],
\]

requiring a conditional coefficient greater than \(0.625832574752639508\). citeturn886696view0turn488637view4

## Status

### PROVED

- Signed coercivity \( (SG+GS)/2\succeq\delta G^2\).
- Exact actual-law Ward identity \(\mathbb E(SG+GS)/2=2I\).
- Improved expected spatial tail (3).
- Exact reachable rank-one sign decomposition.
- Weighted one-sided curvature with the actual factors \(1/(\delta u_i)-1\).
- Complete one-reveal remainder with actual \(q(1-q)\).
- \(q\)-adaptive self-normalization.
- Telescoped halo theorem (1).
- Original-entropy finite-volume, rate, and chord interfaces.
- Reduction of the endpoint-loss exponent from \(\delta^{-10}\) to \(\delta^{-5}\).

### DISPROVED

- Universal zero-payment conditional Jensen.
- Usability of the supplied two-site/two-halo witness under even the improved rigorous bound.

### INCOMPLETE

- Concavity for the whole \(c\in(37/40,1)\), all legal \(a\), and all densities.
- The fixed \(c=.95,\rho=.5\) benchmark itself, because no continuous-parameter large-scale witness has been certified.
- A sign theorem for the actual-law averaged conditional-mutual-information curvature.
- External novelty certification.

The diagnostic script was run successfully with Python 3.13.5 and NumPy 2.3.5. It reproduced the six-site numbers, exhaustively checked all one-reveal coarse words for 200 random contractions of sizes \(3\)–\(6\), and checked the Ward identity and coercivity by full word enumeration on 20 additional kernels. Its terminal status was `PASS_DIAGNOSTIC_NOT_CERTIFICATE`.
