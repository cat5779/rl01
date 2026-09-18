# Harvest provenance — S41, cycle 03 response

Status: AUTHOR_CLAIMS_PENDING_INDEPENDENT_REVIEW.
Acquired via read_thread on 2026-09-18. PARTIAL EXPORT: the API returned only the first 20,000 characters. The omitted tail and downloadable attachments have NOT been acquired. Do not treat the author's headline as a verified theorem.
Original citation tokens below are preserved as source text, not independently resolved evidence.

---

# S41 cycle-03 result

## Status: **PROVED_SCOPED**

I obtained an explicit, genuinely finite-observation posterior certificate for the frozen half-filled sine curvature functional

\[
\Gamma(c)
=
\int_0^1
u\,\mathbb E_{cu,\infty}
\overline{\mathcal G}_{cu,\infty}\,du,
\qquad 0<c<1.
\]

The construction uses the **exact finite marginal of the unsmoothed sine process**. It does not replace the sine kernel by a Fejér or cyclic kernel and does not fill the unobserved exterior with an artificial word.

The main result is

\[
\boxed{
\left|
\Gamma(c)-\Gamma_R^{\mathrm{obs}}(c)
\right|
\le
\varepsilon_{\mathrm{obs}}(c;R,m,d),
}
\]

where:

- \(\Gamma_R^{\mathrm{obs}}(c)\) is exactly computable from the \(2^{2R}\) words on
  \[
  C_R=\{-R,\ldots,-1,1,\ldots,R\};
  \]
- \(\varepsilon_{\mathrm{obs}}\) is an explicit deterministic expression depending only on \(c,R,m,d\);
- for every fixed \(0<c<1\), suitable \(m=m(R)\) and \(d=d(R)\) make
  \[
  \varepsilon_{\mathrm{obs}}(c;R,m,d)\longrightarrow0;
  \]
- the response-coordinate loss, observation-domain loss, and kernel-replacement loss remain separate.

This directly pays the observation-truncation obligation identified in the prompt and in the S42 review. That review verified the full-posterior coordinate-energy tail but emphasized that it did not control replacing the full exterior posterior by a finite observed-window posterior. citeturn475757view0turn475757view3turn475757view5

The ultimate target remains the concavity of the true full-configuration sine Toeplitz entropy rate for every fixed \(0<\rho<1\), \(0<c<1\), and every legal \(a\). The result below is only half-filled, balanced-point, and local-functional scoped; it does not establish that ultimate theorem. citeturn186003view0

---

# 1. The finite object

Let \(Q\) be the half-filled sine projection on \(\ell^2(\mathbb Z)\):

\[
Q_{ii}=\frac12,
\qquad
Q_{ij}=
\frac{\sin(\pi(i-j)/2)}{\pi(i-j)}
\quad(i\ne j).
\]

For \(x\in[0,c]\) and a finite set \(V\subset\mathbb Z\), define

\[
K_{x,V}(h)
=
hI_V+x\left(Q_V-\frac12I_V\right).
\]

At \(h=1/2\),

\[
K_{x,V}(1/2)
=
\frac{1-x}{2}I_V+xQ_V,
\]

which is exactly the principal marginal of the infinite noisy sine process. No kernel approximation has occurred.

For \(R\ge1\), put

\[
C_R=\{-R,\ldots,-1,1,\ldots,R\},
\qquad
V_R=C_R\cup\{0\}.
\]

For \(z\in\{0,1\}^{C_R}\), set

\[
B_{R,z}(h)
=
K_{x,C_R}(h)-\operatorname{diag}(1-z),
\]

\[
G_{R,z}(h)=B_{R,z}(h)^{-1},
\qquad
b_R=xQ_{C_R,0},
\]

and

\[
q_{R,z}(h)
=
h-b_R^*G_{R,z}(h)b_R.
\]

The exact external-word probability is

\[
w_{R,z}(h)
=
(-1)^{2R-|z|}\det B_{R,z}(h).
\]

Thus

\[
q_{R,z}(h)
=
\Pr_h(Y_0=1\mid Y_{C_R}=z),
\]

and \(w_{R,z}(h)\) is the actual marginal probability of \(z\).

Define

\[
\phi(q)
=
\left(q-\frac12\right)\log\frac q{1-q},
\]

\[
F_{x,R}(h)
=
\sum_{z\in\{0,1\}^{C_R}}
w_{R,z}(h)\phi(q_{R,z}(h)).
\]

The finite-observation sine curvature is

\[
\boxed{
\Gamma_R^{\mathrm{obs}}(c)
=
\int_0^1u\,F_{cu,R}''(1/2)\,du.
}
\]

This is a finite sum followed by a one-dimensional integral.

---

# 2. Exact finite differentiation

At \(h=1/2\), abbreviate

\[
B=B_{R,z}(1/2),
\quad
G=B^{-1},
\quad
v=Gb_R,
\quad
r=b_R^*Gb_R,
\quad
q=\frac12-r.
\]

Since \(B'(h)=I\),

\[
G'=-G^2.
\]

Jacobi differentiation gives

\[
w'=w\,\operatorname{tr}G,
\]

\[
w''
=
w\left[
(\operatorname{tr}G)^2-\operatorname{tr}(G^2)
\right].
\]

For the posterior,

\[
q'
=
1+b_R^*G^2b_R
=
1+\|v\|^2,
\]

\[
q''
=
-2b_R^*G^3b_R.
\]

Also

\[
\phi'(q)
=
\log\frac q{1-q}
+
\frac{q-1/2}{q(1-q)},
\]

\[
\phi''(q)
=
\frac1{2q^2(1-q)^2}.
\]

Therefore

\[
\boxed{
\begin{aligned}
F_{x,R}''(1/2)
={}&
\sum_z
\Big\{
w_z''\phi(q_z)
+
2w_z'\phi'(q_z)q_z'
\\
&\qquad\qquad
+
w_z\big[
\phi''(q_z)(q_z')^2
+
\phi'(q_z)q_z''
\big]
\Big\}.
\end{aligned}
}
\]

This retains:

- probability acceleration \(w''\);
- the two moving-law cross terms;
- the posterior first and second derivatives;
- the true finite sine word weights.

No fixed-law differentiation shortcut is being used.

---

# 3. Exact finite response-coordinate account

For \(0\le\ell\le R\), let

\[
\tau_{R,\ell}(z)
=
\sum_{\substack{j\in C_R\\|j|>\ell}}
|v_{R,z,j}|^2.
\]

At \(\theta=2-4\alpha\), define

\[
k_{R,\ell,\alpha}(z)
=
\frac{
4\left(
\sum_{0<|j|\le\ell}|v_{R,z,j}|^2+4r_{R,z}^2
\right)
}{
(1+\theta r_{R,z})^2
}.
\]

The independently reviewed finite Fisher-dual identity gives

\[
F_{x,R}''(1/2)
-
\underline F_{x,R,\ell}''
=
8\,
\mathbb E_{w_{x,R}}
\frac{\tau_{R,\ell}^2}{(1-4r_R^2)^2}.
\]

The coefficient \(8\), moving mixture weights, and denominator were checked in the S42 review. citeturn475757view3turn475757view4

After integration, define

\[
\Delta_{R,\ell}^{\mathrm{resp}}(c)
=
8\int_0^1
u\,
\mathbb E_{w_{cu,R}}
\frac{\tau_{R,\ell}^2}{(1-4r_R^2)^2}
\,du
\ge0
\]

and

\[
\underline\Gamma_{R,\ell}^{\mathrm{obs}}(c)
=
\Gamma_R^{\mathrm{obs}}(c)
-
\Delta_{R,\ell}^{\mathrm{resp}}(c).
\]

When \(\ell=R\),

\[
\tau_{R,R}=0,
\qquad
\Delta_{R,R}^{\mathrm{resp}}=0,
\]

so the response-coordinate account is exactly zero:

\[
\underline\Gamma_{R,R}^{\mathrm{obs}}
=
\Gamma_R^{\mathrm{obs}}.
\]

Thus response truncation need not be mixed with observation truncation.

---

# 4. Explicit observation-error constants

Fix \(0<c<1\), and put

\[
a=\frac2{1-c},
\qquad
L=\frac{c}{1-c}=\frac{ac}{2},
\]

\[
\kappa
=
\min\left\{\frac12,-\log c\right\}.
\]

Define

\[
V_c
=
\frac{2\sqrt2c}{\pi(1-c)}
+
\frac{4c^2}{(1-c)^2},
\]

\[
F_c
=
\sqrt2V_c+\frac1{1-c},
\]

\[
G_c
=
\frac{8\sqrt2c}{(1-c)^2}
+
\frac2{1-c}.
\]

For \(s\ge1\), define

\[
f_c(s)
=
\begin{cases}
L,&s<e^4,\\[2mm]
\min\left\{
L,\,
F_ce^{-\kappa\sqrt{\log s}}
\right\},
&s\ge e^4,
\end{cases}
\]

and

\[
g_c(s)
=
\begin{cases}
a,&s<e^4,\\[2mm]
\min\left\{
a,\,
G_ce^{-\kappa\sqrt{\log s}}
\right\},
&s\ge e^4.
\end{cases}
\]

These are uniform \(\ell^2\)-tail envelopes for the posterior response vector and resolvent columns. Their form is motivated by the frozen effective-remainder file, but the needed estimates are rederived below rather than accepted from its status label. The source itself labels those estimates pending independent review. citeturn478838view5turn478838view6

For \(m\ge2\), set

\[
T_c(m)
=
16a^{16}
\left[
f_c(m)
+
f_c(m/2)^2
+
g_c(m/2)^2
\right].
\]

Choose integers satisfying

\[
\boxed{
m\ge2,
\qquad
2m\le d,
\qquad
2d\le R.
}
\]

Define

\[
\beta_R
=
\frac{\sqrt2c}{\pi\sqrt R},
\]

\[
\delta_v
=
a\left[
\beta_R
+
cL\sqrt{\frac dR}
+
\frac c2f_c(d)
\right],
\]

\[
\delta_q
=
L\beta_R+\frac c2\delta_v,
\]

\[
\delta_G
=
a\left[
ca\sqrt{\frac dR}
+
\frac c2g_c(d-m)
\right].
\]

Put

\[
D_{\mathrm{obs}}(c;R,m,d)
=
\max\{\delta_v,\delta_q,\delta_G\}.
\]

The pointwise observation error is

\[
E_{\mathrm{obs}}(c;R,m,d)
=
2T_c(m)
+
128a^{12}m^2D_{\mathrm{obs}}(c;R,m,d),
\]

and the integrated error is

\[
\boxed{
\varepsilon_{\mathrm{obs}}(c;R,m,d)
=
\frac12E_{\mathrm{obs}}(c;R,m,d).
}
\]

Every quantity on the right is elementary and computable. There is no hidden posterior expectation or unknown convergence modulus.

---

# 5. Main certificate theorem

## Theorem

For every \(0<c<1\) and every \(R,m,d\) satisfying

\[
m\ge2,\qquad2m\le d,\qquad2d\le R,
\]

one has

\[
\boxed{
\left|
\Gamma(c)-\Gamma_R^{\mathrm{obs}}(c)
\right|
\le
\varepsilon_{\mathrm{obs}}(c;R,m,d).
}
\]

Consequently, for every \(0\le\ell\le R\),

\[
\boxed{
\Gamma(c)
\ge
\underline\Gamma_{R,\ell}^{\mathrm{obs}}(c)
-
\varepsilon_{\mathrm{obs}}(c;R,m,d).
}
\]

There is also the computable two-sided enclosure

\[
\boxed{
\begin{aligned}
\underline\Gamma_{R,\ell}^{\mathrm{obs}}(c)
-\varepsilon_{\mathrm{obs}}
\le{}&
\Gamma(c)
\\
\le{}&
\underline\Gamma_{R,\ell}^{\mathrm{obs}}(c)
+
\Delta_{R,\ell}^{\mathrm{resp}}(c)
+
\varepsilon_{\mathrm{obs}}.
\end{aligned}
}
\]

For the full finite response vector, \(\ell=R\),

\[
\boxed{
\left|
\Gamma(c)
-
\underline\Gamma_{R,R}^{\mathrm{obs}}(c)
\right|
\le
\varepsilon_{\mathrm{obs}}(c;R,m,d).
}
\]

The kernel/volume-replacement error for this theorem is exactly zero.

---

# 6. Proof

## 6.1 Uniform coercivity

Let

\[
C=\mathbb Z\setminus\{0\},
\]

\[
A_x=x\left(Q_C-\frac12I\right),
\qquad
b_x=xQ_{C0}.
\]

For a full exterior word \(z\), write

\[
S_z=\operatorname{diag}(2z_i-1),
\]

\[
B_z=\frac12S_z+A_x,
\qquad
G_z=B_z^{-1},
\qquad
v_z=G_zb_x.
\]

Since \(Q-I/2\) has norm \(1/2\),

\[
\|2S_zA_x\|\le x\le c<1.
\]

Thus

\[
G_z
=
2\sum_{k\ge0}
(-2S_zA_x)^kS_z
\]

and

\[
\|G_z\|
\le
\frac2{1-c}=a.
\]

The same estimate holds for every principal compression.

The projection identity gives

\[
\|Q_{C0}\|^2
=
Q_{00}-Q_{00}^2
=
\frac14,
\]

so

\[
\|b_x\|\le\frac x2\le\frac c2
\]

and

\[
\|v_z\|\le\frac{ac}{2}=L.
\]

The channel noise also puts every conditional center posterior in

\[
\left[
\frac{1-c}{2},\frac{1+c}{2}
\right]
=
\left[
\frac1a,1-\frac1a
\right].
\]

This controls all derivatives of \(\phi\), including on very unlikely words.

---

## 6.2 Effective response and resolvent tails

Let \(P_s^{j_0}\) denote projection onto coordinates at distance at most \(s\) from \(j_0\). Put

\[
T=-2S_zA_x.
\]

For \(t\ge2s\ge2\),

\[
\boxed{
\left\|
(I-P_t^{j_0})TP_s^{j_0}
\right\|
\le
4c\sqrt{\frac st}.
}
\]

To see this, use

\[
|(A_x)_{ij}|
\le
\frac c{\pi|i-j|}.
\]

For each near column, the squared mass outside radius \(t\) is at most \(8/t\) before multiplication by \(4c^2/\pi^2\); there are at most \(3s\) near columns. Hence the Hilbert–Schmidt norm is below \(4c\sqrt{s/t}\).

Consequently,

\[
\|(I-P_t^{j_0})Ty\|
\le
c\|(I-P_s^{j_0})y\|
+
4c\sqrt{\frac st}\,\|y\|.
\]

Iterating on radii

\[
B,B^2,\ldots,B^{K+1}
\]

gives, whenever \(B^{K+1}\le s\),

\[
\|(I-P_s^0)v_z\|
\le
\frac{V_c}{\sqrt B}
+
\frac{c^{K+2}}{1-c}.
\]

Similarly, for a resolvent column, whenever \(B^K\le s\),

\[
\|(I-P_s^i)G_ze_i\|
\le
\frac{8c}{(1-c)^2\sqrt B}
+
\frac{2c^{K+1}}{1-c}.
\]

For \(s\ge e^4\), take

\[
r=\sqrt{\log s},
\qquad
B=\lfloor e^r\rfloor.
\]

Using

\[
B^{-1/2}\le\sqrt2e^{-r/2}
\]

and

\[
c^{\lfloor r\rfloor+1}
\le
e^{-(-\log c)r},
\]

one obtains uniformly over full and finite compressed sine systems

\[
\boxed{
\|(I-P_s^0)v_z\|
\le
f_c(s),
}
\]

\[
\boxed{
\sup_i
\|(I-P_s^i)G_ze_i\|
\le
g_c(s).
}
\]

---

## 6.3 The exact signed curvature kernel

For a flip at \(i\), let \(z^i\) be the flipped word and define

\[
\sigma_i=2z_i-1,
\]

\[
o_i=\sigma_iG_{ii}-1,
\]

\[
\bar r_i
=
\sigma_i-G_{ii}
=
-\sigma_io_i.
\]

The determinant lemma and Sherman–Morrison formula give

\[
G_{z^i}
=
G_z
-
\frac{\sigma_i}{o_i}
G_ze_ie_i^*G_z,
\]

\[
v_{z^i}
=
v_z
-
\frac{\sigma_i}{o_i}
v_iG_ze_i,
\]

and

\[
d_i
:=
q(z^i)-q(z)
=
\frac{\sigma_i|v_i|^2}{o_i}.
\]

For a smooth \(\psi\), define

\[
\operatorname{Breg}_\psi(p,q)
=
\psi(p)-\psi(q)-\psi'(q)(p-q),
\]

\[
\overline{\mathcal B}_\psi(z)
=
\sum_i
\bar r_i
\operatorname{Breg}_\psi(q(z^i),q(z)),
\]

and

\[
A_z=1+\|v_z\|^2.
\]

The normalized curvature kernel is

\[
\boxed{
\begin{aligned}
\overline{\mathcal G}(z)
={}&
\phi''(q)
+
\overline{\mathcal B}_{\phi'}
\\
&+
\sum_i
(G^2)_{ii}
\operatorname{Breg}_\phi(q(z^i),q)
\\
&+
\sum_i
\bar r_i
\left[
\big(\phi'(q(z^i))-\phi'(q)\big)A_{z^i}
-
\phi''(q)d_iA_z
\right]
\\
&+
\sum_j
\bar r_j
\left[
\overline{\mathcal B}_\phi(z^j)
-
\overline{\mathcal B}_\phi(z)
\right].
\end{aligned}
}
\tag{1}
\]

This is the same grouped kernel appearing in the frozen definition of \(\Gamma\). citeturn478838view7turn475757view2

For completeness, it follows directly from the moving word law. Define

\[
(Tf)(z)
=
\sum_i
\bar r_i(z)\,[f(z^i)-f(z)]
\]

and

\[
D=\partial_h+T.
\]

Multilinearity of the atom determinant gives

\[
\partial_hw=T^*w.
\]

The flip identities give

\[
Dq=1
\]

because

\[
\partial_hq
=
1+\|v\|^2
\]

and

\[
Tq
=
\sum_i\bar r_id_i
=
-\sum_i|v_i|^2.
\]

Likewise,

\[
DG=0.
\]

Therefore

\[
D\phi(q)
=
\phi'(q)+\overline{\mathcal B}_\phi.
\]

Differentiating the moving expectation once more gives

\[
F''(1/2)
=
\mathbb E
\left[
\phi''(q)
+
\overline{\mathcal B}_{\phi'}
+
D\overline{\mathcal B}_\phi
\right].
\]

Expanding \(D\overline{\mathcal B}_\phi\) by the rank-one flip identities yields exactly (1). Thus all moving-law derivatives are retained, and no positive-Markov-semigroup assumption is involved.

---

## 6.4 Curvature-coordinate tail

Let

\[
C_m=\{i:0<|i|\le m\}.
\]

Define \(\overline{\mathcal G}^{[m]}\) by:

- retaining the base term \(\phi''(q)\);
- restricting each single sum in (1) to \(C_m\);
- restricting both indices in the last double-flip term to \(C_m\).

Then

\[
\boxed{
\left|
\overline{\mathcal G}
-
\overline{\mathcal G}^{[m]}
\right|
\le
T_c(m).
}
\tag{2}
\]

Here is the quantitative accounting.

Write

\[
f=f_c(m),
\qquad
f_*=f_c(m/2),
\qquad
g_*=g_c(m/2),
\]

and

\[
g_{ij}=|G_{ij}|.
\]

The single-flip tails cost at most

\[
2a^{10}f^2.
\]

Every off-diagonal connected double-flip summand is bounded by a fixed linear combination of

\[
K_1
=
g_{ij}|v_i|^3|v_j|,
\]

\[
K_2
=
g_{ij}^2|v_i|^4,
\]

\[
K_3
=
g_{ij}^2|v_i|^2|v_j|^2,
\]

\[
K_4
=
g_{ij}^4|v_i|^4,
\]

its \(i,j\)-swapped version, and the weighted connected term

\[
|d_j|D_{ij}^2,
\qquad
D_{ij}
=
\max\{|d_i(z)|,|d_i(z^j)|\}.
\]

On the set where at least one index lies outside \(C_m\),

\[
\sum K_1
\le
2aL^3f,
\]

\[
\sum K_2
\le
2a^2L^2f_*^2+L^4g_*^2,
\]

\[
\sum K_3
\le
2a^2L^2f^2,
\]

\[
\sum
(K_4+K_4^{\mathrm{swapped}})
\le
2a^2\sum K_2,
\]

and

\[
\sum |d_j|D_{ij}^2
\le
4a^3L^4f^2.
\]

The differentiated rank-one formulas dominate the non-diagonal kernel by

\[
4a^7K_1
+
3a^8K_2
+
26a^8K_3
+
6a^{10}(K_4+K_4^{\mathrm{swapped}})
+
4a^5|d_j|D_{ij}^2.
\]

The diagonal part costs at most

\[
2a^6L^2f^2.
\]

Since \(L\le a/2\) and \(a\ge2\), the total is bounded by

\[
16a^{16}
\left(
f+f_*^2+g_*^2
\right)
=
T_c(m).
\]

This proves (2). Importantly, the proof does not split off a non-summable bare double difference.

---

## 6.5 Stability of the retained kernel

Consider two legal posterior data sets

\[
(q,v,G,S)
\quad\text{and}\quad
(\widetilde q,\widetilde v,\widetilde G,S)
\]

having the same signs on \(C_m\). Define

\[
\Delta
=
\max
\left\{
|q-\widetilde q|,
\,
\|v-\widetilde v\|,
\,
\max_{i\in C_m}
\|(G-\widetilde G)e_i\|
\right\}.
\]

Then

\[
\boxed{
\left|
\overline{\mathcal G}^{[m]}
-
\widetilde{\overline{\mathcal G}}^{[m]}
\right|
\le
128a^{12}m^2\Delta.
}
\tag{3}
\]

The uniform posterior interval bounds control all odds, inverse odds, and derivatives of \(\phi\). Rank-one updates give, for \(i,j\in C_m\),

\[
|d_i-\widetilde d_i|
\le
\frac12a^4\Delta,
\]

\[
|q(z^i)-\widetilde q(z^i)|
\le
a^4\Delta,
\]

\[
\|v(z^i)-\widetilde v(z^i)\|
\le
a^4\Delta,
\]

\[
\|(G(z^j)-\widetilde G(z^j))e_i\|
\le
2a^4\Delta,
\]

and

\[
|q(z^{ij})-\widetilde q(z^{ij})|
\le
a^8\Delta.
\]

Term-by-term in (1):

\[
|\Delta\phi''|
\le
8a^3\Delta;
\]

the three single-index groups cost at most

\[
20a^{12}\Delta,
\qquad
5a^{12}\Delta,
\qquad
6a^{12}\Delta
\]

per index; and every ordered double-index term costs at most

\[
10a^{12}\Delta.
\]

Since \(|C_m|=2m\),

\[
8a^3
+
\bigl[31(2m)+10(2m)^2\bigr]a^{12}
\le
128a^{12}m^2
\]

for \(m\ge2\) and \(a\ge2\). This proves (3).

---

## 6.6 Full exterior versus finite observed window

Let \(P_R\) be projection onto \(C_R\). Given a full exterior word \(z\), let

\[
B=\frac12S_z+A_x,
\qquad
B_R=P_RBP_R,
\]

\[
G=B^{-1},
\qquad
G_R=B_R^{-1},
\]

\[
b=b_x,
\qquad
b_R=P_Rb,
\]

\[
v=Gb,
\qquad
v_R=G_Rb_R,
\]

and

\[
q=\frac12-b^*v,
\qquad
q_R=\frac12-b_R^*v_R.
\]

The finite data are the exact conditional data from observing \(z_R\). They are not obtained by setting the unseen coordinates to zero.

First, the sine center-column tail gives

\[
\|(I-P_R)b\|^2
\le
\frac{2c^2}{\pi^2R},
\]

hence

\[
\|(I-P_R)b\|
\le
\beta_R.
\tag{4}
\]

Next, for \(d\le R/2\),

\[
\boxed{
\|(I-P_R)A_xP_d\|
\le
c\sqrt{\frac dR}.
}
\tag{5}
\]

Indeed,

\[
\begin{aligned}
\|(I-P_R)A_xP_d\|_{\mathrm{HS}}^2
&\le
\sum_{0<|j|\le d}
\sum_{|i|>R}
\frac{c^2}{\pi^2(i-j)^2}
\\
&\le
\frac{8c^2d}{\pi^2R}
<
c^2\frac dR.
\end{aligned}
\]

The full and finite equations imply

\[
B(v-v_R)
=
(I-P_R)b
-
(I-P_R)A_xP_Rv_R.
\]

Split \(v_R\) into \(P_dv_R+(I-P_d)v_R\). Using (5),

\[
\|v_R\|\le L,
\qquad
\|A_x\|\le\frac c2,
\qquad
\|(I-P_d)v_R\|\le f_c(d),
\]

one obtains

\[
\boxed{
\|v-v_R\|
\le
\delta_v.
}
\tag{6}
\]

For the posterior,

\[
\begin{aligned}
|q-q_R|
&\le
\|(I-P_R)b\|\,\|v\|
+
\|b_R\|\,\|v-v_R\|
\\
&\le
L\beta_R+\frac c2\delta_v
=
\delta_q.
\end{aligned}
\tag{7}
\]

For \(i\in C_m\),

\[
B(G-G_R)e_i
=
-(I-P_R)A_xP_RG_Re_i.
\]

After splitting at \(P_d\), the portion of \(G_Re_i\) outside \(C_d\) lies at distance at least \(d-m\) from \(i\). Thus

\[
\boxed{
\|(G-G_R)e_i\|
\le
\delta_G.
}
\tag{8}
\]

Equations (6)–(8) give

\[
\Delta
\le
D_{\mathrm{obs}}(c;R,m,d).
\]

---

## 6.7 Pointwise curvature comparison

Apply (2) to both systems and (3) to the two retained kernels:

\[
\begin{aligned}
&
\left|
\overline{\mathcal G}_{x,\infty}(z)
-
\overline{\mathcal G}_{x,R}(z_R)
\right|
\\
&\le
\left|
\overline{\mathcal G}_{x,\infty}
-
\overline{\mathcal G}_{x,\infty}^{[m]}
\right|
\\
&\quad+
\left|
\overline{\mathcal G}_{x,\infty}^{[m]}
-
\overline{\mathcal G}_{x,R}^{[m]}
\right|
\\
&\quad+
\left|
\overline{\mathcal G}_{x,R}^{[m]}
-
\overline{\mathcal G}_{x,R}
\right|
\\
&\le
2T_c(m)
+
128a^{12}m^2D_{\mathrm{obs}}
\\
&=
E_{\mathrm{obs}}(c;R,m,d).
\end{aligned}
\tag{9}
\]

This is uniform over

\[
0\le x\le c
\]

and every full exterior word.

---

## 6.8 Why no probability-law or kernel term appears

The restriction of a DPP to a subset is exactly the DPP whose kernel is the corresponding principal submatrix. Hence the distribution of \(z_R\) under the infinite noisy sine process is exactly the law used to define \(F_{x,R}\).

Therefore

\[
\mathbb E_{x,R}
\overline{\mathcal G}_{x,R}
=
\mathbb E_{x,\infty}
\left[
\overline{\mathcal G}_{x,R}(z_R)
\right].
\]

Taking expectations in (9),

\[
\left|
\mathbb E_{x,\infty}
\overline{\mathcal G}_{x,\infty}
-
F_{x,R}''(1/2)
\right|
\le
E_{\mathrm{obs}}(c;R,m,d).
\]

There is:

- no total-variation comparison;
- no finite Fejér word law;
- no cyclic projection;
- no kernel interpolation;
- no fabricated outside word.

Finally,

\[
\begin{aligned}
\left|
\Gamma(c)-\Gamma_R^{\mathrm{obs}}(c)
\right|
&\le
\int_0^1
uE_{\mathrm{obs}}\,du
\\
&=
\frac12E_{\mathrm{obs}}
\\
&=
\varepsilon_{\mathrm{obs}}.
\end{aligned}
\]

This proves the main theorem.

Since

\[
\Gamma_R^{\mathrm{obs}}
=
\underline\Gamma_{R,\ell}^{\mathrm{obs}}
+
\Delta_{R,\ell}^{\mathrm{resp}}
\]

with

\[
\Delta_{R,\ell}^{\mathrm{resp}}\ge0,
\]

the one-sided and two-sided certificates follow immediately.

---

# 7. Explicit vanishing

Let

\[
t=\log R,
\]

and, for sufficiently large \(R\), choose

\[
d=\lfloor R^{1/2}\rfloor,
\]

\[
m=
\left\lfloor
\exp\left(
\frac{\kappa\sqrt t}{64}
\right)
\right\rfloor,
\]

with an integer adjustment if needed to enforce

\[
2m\le d,\qquad2d\le R.
\]

Then:

\[
T_c(m)\longrightarrow0,
\]

because \(f_c(m)\), \(f_c(m/2)\), and \(g_c(m/2)\) vanish.

Furthermore,

\[
m^2R^{-1/2}\to0,
\qquad
m^2\sqrt{d/R}
=
m^2R^{-1/4}\to0,
\]

and

\[
m^2f_c(d)\to0,
\qquad
m^2g_c(d-m)\to0.
\]

Thus

\[
\boxed{
\varepsilon_{\mathrm{obs}}(c;R,m(R),d(R))
\longrightarrow0
}
\]

for every fixed \(0<c<1\).

A conservative rate summary is

\[
\varepsilon_{\mathrm{obs}}
=
O_c\left(
\exp\left[
-\frac{\kappa^{3/2}}{16}
(\log R)^{1/4}
\right]
\right).
\]

The finite displayed formula for \(\varepsilon_{\mathrm{obs}}\), rather than the \(O_c\) notation, is the effective certificate.

---

# 8. A sharper auxiliary scalar observation theorem

The preceding pointwise certificate is robust but has very large constants near \(c=1\). There is a separate actual-law localization mechanism that gives an \(O(\log L/L)\) observation rate for the scalar posterior.

This does not yet replace the full resolvent-data error, but it is useful new structure.

## Randomized-window posterior theorem

Let \(X\) be any stationary projection DPP on \(\mathbb Z\

