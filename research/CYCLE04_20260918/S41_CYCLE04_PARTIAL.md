# Acquisition status

PARTIAL EXPORT: first 20,000 characters only. Author claims a complete-jet O_c(sqrt(log N/N)) observation theorem. Truncated during section10; file bodies not acquired. New result pending separate review; prior cycle03 certificate is scoped reviewed in PR17.

---

# S41 cycle-04 result

## Status: **PROVED_SCOPED — NEW, NOT YET INDEPENDENTLY REVIEWED**

I obtained an actual-law averaged finite-observation theorem for the **complete curvature jet**. It replaces the cycle-03 worst-word stretched-log observation rate by

\[
O_c\!\left(\sqrt{\frac{\log N}{N}}\right).
\]

The result controls the exact moving-law second derivative, including

\[
w''\phi+2w'\phi'q'
+w\bigl(\phi''(q')^2+\phi'q''\bigr),
\]

rather than controlling only the scalar posterior \(q\).

The theorem is scoped to the frozen half-filled sine projection, the balanced point, and the frozen infinite curvature functional

\[
\Gamma(c)=\int_0^1u\,
\mathbb E_{cu,\infty}\overline{\mathcal G}_{cu,\infty}\,du .
\]

The finite grouped-kernel identity and this identification of \(\Gamma\) are dependency-labelled because their frozen source remains pending independent review. citeturn872045view0turn605628view3

This does **not** complete the ultimate target, which remains concavity of the true full-configuration sine Toeplitz entropy rate for every \(0<\rho<1\), every \(0<c<1\), and every legal \(a\). citeturn605628view1

---

# 1. The finite actual-sine object

Let \(Q\) be the half-filled sine projection on \(\ell^2(\mathbb Z)\):

\[
Q_{ii}=\frac12,\qquad
Q_{ij}=
\frac{\sin(\pi(i-j)/2)}{\pi(i-j)}
\quad (i\neq j).
\]

For an integer \(N\ge 1\) and \(r=0,\ldots,N-1\), define the length-\(N\) interval

\[
I_{N,r}=\{-r,-r+1,\ldots,N-1-r\},
\]

so that the origin occupies each possible position in the interval, and put

\[
J_{N,r}=I_{N,r}\setminus\{0\}.
\]

For \(0\le x<1\), use the exact unsmoothed sine marginal

\[
K_x(h)=hI+x\left(Q-\frac12I\right).
\]

For a word \(z\in\{0,1\}^{J_{N,r}}\), define

\[
B_{r,z}(h)
=
K_{x,J_{N,r}}(h)-\operatorname{diag}(1-z),
\]

\[
G_{r,z}(h)=B_{r,z}(h)^{-1},
\qquad
b_r=xQ_{J_{N,r},0},
\]

and

\[
q_{r,z}(h)
=
h-b_r^*G_{r,z}(h)b_r.
\]

Let \(w_{r,z}(h)\) be the exact marginal probability of the observed word. With

\[
\phi(q)=
\left(q-\frac12\right)\log\frac q{1-q},
\]

define

\[
F_{x,N,r}(h)
=
\sum_z w_{r,z}(h)\phi(q_{r,z}(h)),
\]

and average over all anchor placements:

\[
\overline F_{x,N}''
=
\frac1N\sum_{r=0}^{N-1}
F_{x,N,r}''(1/2).
\]

The finite actual-law curvature object is

\[
\boxed{
\Gamma_N^{\mathrm{av}}(c)
=
\int_0^1u\,\overline F_{cu,N}''\,du.
}
\]

This uses the exact sine principal marginal throughout:

- no Fejér kernel;
- no cyclic projection;
- no fictitious exterior word;
- no Toeplitz block treated as a projection.

The random-anchor average is essential. It converts posterior boundary energy into a conditional count variance and hence into the sine number variance.

---

# 2. Main theorem

Put

\[
a_c=\frac{2}{1-c},
\qquad
s_c=\sqrt{\frac{1+c}{1-c}},
\]

and use the deliberately conservative complete-jet constant

\[
\boxed{
C_{\mathrm{jet}}(c)=2^{28}a_c^{28}.
}
\]

Let

\[
V_Q(N)
=
\operatorname{Var}_Q
\left(\sum_{j=0}^{N-1}X_j\right).
\]

Define

\[
\begin{aligned}
E_c^{\mathrm{split}}(N)
={}&
C_{\mathrm{jet}}(c)s_c^7\frac{V_Q(N)}N\\
&+
\frac23C_{\mathrm{jet}}(c)s_c^2
\bigl(s_c^{3/2}-1\bigr)
\sqrt{\frac{V_Q(N)}N},
\end{aligned}
\]

and

\[
E_c^{\mathrm{simple}}(N)
=
\frac53C_{\mathrm{jet}}(c)s_c^{7/2}
\sqrt{\frac{V_Q(N)}N}.
\]

Finally set

\[
E_c^{\mathrm{av}}(N)
=
\min\left\{
E_c^{\mathrm{split}}(N),
E_c^{\mathrm{simple}}(N)
\right\}.
\]

## Theorem A — effective complete-jet observation localization

For every fixed \(0<c<1\) and every \(N\ge1\),

\[
\boxed{
\left|
\Gamma(c)-\Gamma_N^{\mathrm{av}}(c)
\right|
\le
E_c^{\mathrm{av}}(N).
}
\]

For the half-filled sine projection,

\[
V_Q(N)
=
\frac2{\pi^2}
\left(
\sum_{\substack{1\le k\le N\\k\ {\rm odd}}}\frac1k
+
N\sum_{\substack{k>N\\k\ {\rm odd}}}\frac1{k^2}
\right)
\le
\frac{\log N+4}{\pi^2}.
\]

The exact formula and the displayed upper bound were also used in the previously verified coordinate-tail result. That earlier theorem did not pay observation truncation; the present theorem does. citeturn605628view2

Consequently,

\[
\boxed{
E_c^{\mathrm{av}}(N)
\le
\frac{5C_{\mathrm{jet}}(c)s_c^{7/2}}{3\pi}
\sqrt{\frac{\log N+4}{N}}
\longrightarrow0.
}
\]

Thus the observation-domain rate improves from the cycle-03 worst-word stretched-log behavior to the power rate

\[
\boxed{
O_c\!\left(\sqrt{\frac{\log N}{N}}\right).
}
\]

---

# 3. The complete moving-law derivative

Fix one finite observed set and abbreviate, at \(h=1/2\),

\[
B=B_z(1/2),\qquad
G=B^{-1},\qquad
v=Gb,
\]

\[
q=\frac12-b^*Gb,
\qquad
w=w_z(1/2).
\]

Because \(B'(h)=I\),

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
1+b^*G^2b
=
1+\|v\|^2,
\]

and

\[
q''
=
-2b^*G^3b.
\]

Therefore the exact finite derivative is

\[
\boxed{
\begin{aligned}
F_{x,N,r}''(1/2)
=
\sum_z\Big\{&
w_z''\phi(q_z)
+
2w_z'\phi'(q_z)q_z'\\
&+
w_z\big[
\phi''(q_z)(q_z')^2
+
\phi'(q_z)q_z''
\big]
\Big\}.
\end{aligned}
}
\tag{3.1}
\]

No probability acceleration or cross term has been dropped.

## 3.1 The grouped curvature kernel

Write

\[
\sigma_j=2z_j-1,
\qquad
o_j=\sigma_jG_{jj}-1,
\]

and

\[
\bar r_j=\sigma_j-G_{jj}=-\sigma_jo_j.
\]

For the word \(z^j\) obtained by flipping coordinate \(j\), Sherman–Morrison gives

\[
G^j
=
G-\frac{\sigma_j}{o_j}
Ge_je_j^*G,
\]

\[
v^j
=
v-\frac{\sigma_jv_j}{o_j}Ge_j,
\]

and

\[
d_j
:=
q(z^j)-q(z)
=
\frac{\sigma_j|v_j|^2}{o_j}.
\]

For a smooth \(\psi\), define

\[
\operatorname{Breg}_{\psi}(p,q)
=
\psi(p)-\psi(q)-\psi'(q)(p-q),
\]

\[
\overline{\mathcal B}_{\psi}(z)
=
\sum_j
\bar r_j
\operatorname{Breg}_{\psi}(q(z^j),q(z)),
\]

and

\[
A_z=1+\|v_z\|^2.
\]

The complete grouped kernel is

\[
\boxed{
\begin{aligned}
\overline{\mathcal G}(z)
={}&
\phi''(q)
+
\overline{\mathcal B}_{\phi'}\\
&+
\sum_j
(G^2)_{jj}
\operatorname{Breg}_{\phi}(q(z^j),q)\\
&+
\sum_j
\bar r_j
\left[
\{\phi'(q(z^j))-\phi'(q)\}A_{z^j}
-\phi''(q)d_jA_z
\right]\\
&+
\sum_j
\bar r_j
\left[
\overline{\mathcal B}_{\phi}(z^j)
-\overline{\mathcal B}_{\phi}(z)
\right].
\end{aligned}
}
\tag{3.2}
\]

This is the frozen V14 form. citeturn872045view0

## 3.2 Why (3.2) includes every derivative term

Define the flip operator

\[
(Tf)(z)
=
\sum_j
\bar r_j(z)
\bigl[f(z^j)-f(z)\bigr],
\]

and

\[
D=\partial_h+T.
\]

The determinant flip identity gives

\[
\frac{d}{dh}\mathbb E_hf_h
=
\mathbb E_hDf_h.
\]

The rank-one formulas imply

\[
Dq=1,
\qquad
DG=0,
\qquad
Dv=0.
\]

For example,

\[
\sum_j\bar r_jd_j
=
-\sum_j|v_j|^2,
\]

which cancels the \(\|v\|^2\) part of \(\partial_hq\). Similarly, the flip correction for \(G\) sums to \(G^2\), cancelling \(\partial_hG=-G^2\).

Because \(T\) is a jump operator, the ordinary chain rule acquires a Bregman term:

\[
D\psi(q)
=
\psi'(q)
+
\overline{\mathcal B}_{\psi}.
\]

Applying this first to \(\phi\), then to

\[
\phi'(q)+\overline{\mathcal B}_{\phi},
\]

produces exactly (3.2). Hence

\[
F_{x,N,r}''(1/2)
=
\mathbb E_{x,N,r}
\overline{\mathcal G}_{x,N,r}.
\]

The accompanying code checks this equality word-by-word in expectation for small finite sine systems; the agreement is at floating-point roundoff.

---

# 4. Latent posterior projection and the Schur-data dictionary

Generate the output from a latent sine projection DPP through the balanced channel

\[
\Pr(Y_j=1\mid X_j)
=
\frac12+x\left(X_j-\frac12\right).
\]

Write

\[
y_j=2Y_j-1,
\qquad
s_x=\sqrt{\frac{1+x}{1-x}}.
\]

If outputs are observed on a set \(J\), let \(D_J(y)\) be diagonal with

\[
D_J(y)e_j
=
\begin{cases}
s_x^{y_j}e_j,&j\in J,\\
e_j,&j\notin J.
\end{cases}
\]

If \(Q=UU^*\), the posterior latent law is again a projection DPP, with projection

\[
\boxed{
\Pi_J
=
D_JU
\left(U^*D_J^2U\right)^{-1}
U^*D_J.
}
\tag{4.1}
\]

Equivalently, \(\Pi_J\) is the orthogonal projection onto

\[
D_J\operatorname{Ran}(Q).
\]

This posterior-projection representation was independently verified in the preceding review for the finite and infinite noisy projection setting. citeturn605628view2

For an unobserved anchor \(0\), the output Schur data satisfy the exact identities

\[
\boxed{
q
=
\frac12+x\left(\Pi_{00}-\frac12\right),
}
\tag{4.2}
\]

\[
\boxed{
v_j
=
\frac{2x}{\sqrt{1-x^2}}\,
y_j\Pi_{j0},
}
\tag{4.3}
\]

and, on the observed block,

\[
\boxed{
G
=
\frac2{1-x^2}
\left[
S-xS(2\Pi_J-I)S
\right],
\qquad
S=\operatorname{diag}(y_j).
}
\tag{4.4}
\]

These identities follow by substituting (4.1) into the block Schur complement and checking \(BG=I\) and \(Bv=b\).

In particular,

\[
|v_j|^2
=
\frac{4x^2}{1-x^2}
|\Pi_{j0}|^2,
\]

recovering the previously verified influence identity.

For \(x\le c<1\), all legal posterior data obey

\[
q\in\left[\frac1{a_c},1-\frac1{a_c}\right],
\]

\[
\|G\|\le a_c,
\qquad
\|v\|\le a_c,
\qquad
|o_j|^{-1}\le a_c.
\tag{4.5}
\]

---

# 5. Boundary covariance energy

Let \(I\) be a finite interval containing the anchor, put

\[
J=I\setminus\{0\},
\qquad
O=\mathbb Z\setminus I,
\]

and let \(P\) be any posterior projection.

Define

\[
T_0(P;I)
=
\sum_{k\in O}|P_{k0}|^2,
\]

and, for \(j\in I\),

\[
T_j(P;I)
=
\sum_{k\in O}|P_{kj}|^2.
\]

The second-order energy needed by the resolvent and connected double-flip terms is

\[
W_0(P;I)
=
\sum_{j\in J}|P_{j0}|^2T_j(P;I).
\]

Put

\[
\boxed{
U_0(P;I)=T_0(P;I)+W_0(P;I).
}
\tag{5.1}
\]

The scalar term \(T_0\) controls the anchor posterior column. The \(W_0\) term is what upgrades the argument from scalar-posterior localization to localization of the complete curvature jet.

Projection identities imply

\[
T_0\le P_{00}(1-P_{00})\le\frac14,
\]

and

\[
W_0
\le
\frac14
\sum_{j\ne0}|P_{j0}|^2
\le\frac1{16}.
\]

Thus

\[
U_0\le\frac5{16}<1.
\tag{5.2}
\]

---

# 6. Diagonal projection flow

Let

\[
D_t=e^{tH},
\]

where \(H\) is real diagonal, and let \(P_t\) be the orthogonal projection onto

\[
D_t\operatorname{Ran}(P_0).
\]

Differentiation of the projection formula gives

\[
\boxed{
\dot P_t
=
(I-P_t)HP_t
+
P_tH(I-P_t).
}
\tag{6.1}
\]

## Lemma 6.1 — outside-observation flow

Assume \(H\) is supported on \(O\) and

\[
\|H\|\le h.
\]

For every \(i\in I\),

\[
\boxed{
\|\dot P_te_i\|
\le
h\sqrt{T_i(P_t;I)}.
}
\tag{6.2}
\]

Moreover,

\[
|T_0'|\le2hT_0,
\]

\[
|W_0'|
\le
hT_0+3hW_0,
\]

and hence

\[
\boxed{
U_0(P_t;I)
\le
e^{3ht}U_0(P_0;I).
}
\tag{6.3}
\]

Also,

\[
\boxed{
\|P_1e_0-P_0e_0\|
\le
(e^h-1)\sqrt{T_0(P_0;I)}.
}
\tag{6.4}
\]

### Proof

Since \(He_i=0\) for \(i\in I\), (6.1) gives

\[
\dot P_te_i
=
(I-2P_t)HP_te_i.
\]

Because \(I-2P_t\) is a unitary involution,

\[
\|\dot P_te_i\|
=
\|HP_te_i\|
\le
h\|E_OP_te_i\|,
\]

which is (6.2).

Differentiating \(T_0\) gives

\[
|T_0'|
\le
2hT_0.
\]

For \(W_0\), the row norm bound

\[
\sum_{j\in J}|\dot P_{0j}|^2
\le h^2T_0
\]

and \(|T_j'|\le2hT_j\) yield

\[
\begin{aligned}
|W_0'|
&\le
2\sum_{j\in J}
|P_{0j}||\dot P_{0j}|T_j
+
2hW_0\\
&\le
2h\sqrt{T_0W_0}+2hW_0\\
&\le
hT_0+3hW_0.
\end{aligned}
\]

Adding the two inequalities proves (6.3). Integrating (6.2), using

\[
T_0(t)\le e^{2ht}T_0(0),
\]

proves (6.4).

---

# 7. Observing the anchor

Let \(P^-\) be the posterior projection after observing \(Y_J\), and let \(P^+\) be the posterior after additionally observing \(Y_0\).

## Lemma 7.1

Pointwise in the observed word,

\[
\boxed{
U_0(P^-;I)
\le
s_x^4U_0(P^+;I).
}
\tag{7.1}
\]

### Proof

Interpolate by scaling only coordinate \(0\). Let the logarithmic scale be \(\eta\), so

\[
|\eta|\le\log s_x.
\]

For \(k\in O\) and \(j\in J\), (6.1) gives

\[
\dot P_{k0}
=
\eta(1-2P_{00})P_{k0},
\]

\[
\dot P_{0j}
=
\eta(1-2P_{00})P_{0j},
\]

and

\[
E_O\dot Pe_j
=
-2\eta P_{0j}E_OPe_0.
\]

It follows that

\[
|T_0'|\le2|\eta|T_0
\]

and

\[
|W_0'|
\le
2|\eta|T_0+4|\eta|W_0.
\]

Therefore

\[
|U_0'|\le4|\eta|U_0.
\]

Integrating in either direction gives (7.1).

---

# 8. Complete curvature-jet localization

For a finite coordinate set \(J\), let

\[
\mathscr K_{x,J}(P,y_J)
\]

denote the complete grouped kernel (3.2), with \(q,v,G\) supplied by the dictionary (4.2)–(4.4), and with every one- and two-flip sum restricted to \(J\).

## Lemma 8.1 — complete-jet tail

Let \(I=J\cup\{0\}\). Then

\[
\boxed{
\left|
\mathscr K_{x,\mathbb Z\setminus\{0\}}(P,y)
-
\mathscr K_{x,J}(P,y_J)
\right|
\le
C_{\mathrm{jet}}(c)U_0(P;I).
}
\tag{8.1}
\]

## Lemma 8.2 — complete-jet directional bound

If \(P_t\) is an outside diagonal-tilt flow as in Lemma 6.1, then

\[
\boxed{
\left|
\frac d{dt}\mathscr K_{x,J}(P_t,y_J)
\right|
\le
C_{\mathrm{jet}}(c)\|H\|
\left(
\sqrt{T_0(P_t;I)}
+
\sqrt{W_0(P_t;I)}
\right).
}
\tag{8.2}
\]

These two statements are the central cycle-04 gain.

## 8.1 Primitive estimates

Write

\[
p_j=|P_{j0}|,
\qquad
g_{ij}=|P_{ij}|.
\]

Projection identities give

\[
\sum_{j\ne0}p_j^2
=
P_{00}-P_{00}^2
\le\frac14,
\]

and

\[
\sum_k g_{jk}^2=P_{jj}\le1.
\tag{8.3}
\]

The posterior dictionary and (4.5) imply

\[
|v_j|\le a_cp_j,
\]

\[
|G_{ij}|\le2a_cg_{ij}
\quad(i\ne j),
\]

and

\[
|d_j|
\le
a_c^3p_j^2.
\tag{8.4}
\]

On the posterior interval for \(q\),

\[
|\phi''|\le a_c^4,
\qquad
|\phi'''|\le a_c^6,
\qquad
|\phi''''|\le5a_c^8.
\tag{8.5}
\]

For a projection direction \(\dot P\), define

\[
\delta_0=\|\dot Pe_0\|,
\]

\[
\delta_1
=
\left(
\sum_{j\in J}
p_j^2\|\dot Pe_j\|^2
\right)^{1/2}.
\tag{8.6}
\]

Differentiating the dictionary and flip identities gives

\[
|\dot q|\le\delta_0,
\]

\[
\|\dot v\|\le a_c\delta_0,
\]

\[
\|\dot Ge_j\|
\le
2a_c\|\dot Pe_j\|,
\tag{8.7}
\]

and

\[
|\dot d_j|
\le
2a_c^3p_j|\dot P_{j0}|
+
2a_c^5p_j^2\|\dot Pe_j\|.
\tag{8.8}
\]

Consequently,

\[
\sum_j|\dot d_j|
+
\sum_j|d_j\dot d_j|
\le
4a_c^8(\delta_0+\delta_1).
\tag{8.9}
\]

The derivatives of the one-flip quantities \(G^j,v^j,q^j,A_{z^j}\) obey the same weighted norm, with an additional factor bounded by \(2^8a_c^{12}\).

## 8.2 Tail monomials

The connected two-flip expansion is controlled by the prototype families

\[
K_1=g_{ij}p_i^3p_j,
\]

\[
K_2=g_{ij}^2p_i^4,
\]

\[
K_3=g_{ij}^2p_i^2p_j^2,
\]

\[
K_4=g_{ij}^4p_i^4,
\]

plus the connected term

\[
|d_j|D_{ij}^2,
\qquad
D_{ij}
=
\max\{|d_i(z)|,|d_i(z^j)|\}.
\]

The corresponding resolvent-form prototypes are exactly the families used in the frozen connected-tail estimate. citeturn872045view2

On the union where \(i\in O\) or \(j\in O\),

\[
\sum K_1
\le
2(T_0+W_0),
\tag{8.10}
\]

\[
\sum K_2
\le
T_0+W_0,
\tag{8.11}
\]

\[
\sum K_3
\le
2T_0,
\tag{8.12}
\]

and

\[
\sum(K_4+K_4^{\rm swapped})
\le
2(T_0+W_0).
\tag{8.13}
\]

The only superficially linear tail is part of \(K_1\). It is actually quadratic in boundary energy:

\[
\begin{aligned}
\sum_{\substack{i\in J\\j\in O}}
g_{ij}p_i^3p_j
&\le
\sqrt{T_0}
\sum_{i\in J}p_i^3\sqrt{T_i}\\
&\le
\sqrt{T_0W_0}\\
&\le
\frac12(T_0+W_0).
\end{aligned}
\]

For the connected remainder, the flip formula gives

\[
|v_i(z^j)|
\le
a_cp_i+2a_c^3p_jg_{ij}.
\]

Hence

\[
D_{ij}
\le
2a_c^3p_i^2
+
8a_c^7p_j^2g_{ij}^2,
\]

and therefore

\[
\boxed{
\sum_{\substack{i\in O\ {\rm or}\\j\in O}}
|d_j|D_{ij}^2
\le
144a_c^{17}(T_0+W_0).
}
\tag{8.14}
\]

Substitution into the complete connected expansion, together with the single-flip terms, gives a bound below

\[
2^{13}a_c^{22}(T_0+W_0).
\]

The rounded constant

\[
2^{28}a_c^{28}
\]

therefore proves (8.1).

## 8.3 Marked monomials

Differentiate the connected expansion before taking absolute values. Each term is one of the preceding prototype monomials with one marked derivative factor.

The key row bounds are

\[
\sum_jp_j|\dot P_{ij}|
\le
\|\dot Pe_i\|
\left(\sum_jp_j^2\right)^{1/2},
\tag{8.15}
\]

and

\[
\sum_jg_{ij}|\dot P_{ij}|
\le
\|\dot Pe_i\|.
\tag{8.16}
\]

These prevent a factor proportional to \(|J|\). For example,

\[
\sum_{i,j}
p_i^3p_j|\dot P_{ij}|
\le
\sum_i p_i^3\|\dot Pe_i\|
\le
\delta_1.
\]

Differentiating either \(p\)-factor costs a constant times \(\delta_0\).

The four marked prototype families are bounded respectively by

\[
8a_c^5(\delta_0+\delta_1),
\]

\[
16a_c^6(\delta_0+\delta_1),
\]

\[
24a_c^6(\delta_0+\delta_1),
\]

and

\[
64a_c^8(\delta_0+\delta_1).
\]

The differentiated connected family—including derivatives of \(o_j^{-1}\), all one- and two-flip posterior quantities, the \(A\)-terms, and the Bregman remainders—is bounded by

\[
2^{22}a_c^{27}(\delta_0+\delta_1).
\]

The base and three single-sum groups cost less than

\[
2^{14}a_c^{20}(\delta_0+\delta_1).
\]

Thus

\[
\left|
D\mathscr K_{x,J}(P)[\dot P]
\right|
\le
C_{\mathrm{jet}}(c)
(\delta_0+\delta_1).
\tag{8.17}
\]

Along an outside-observation flow, Lemma 6.1 gives

\[
\delta_0
\le
\|H\|\sqrt{T_0},
\]

and

\[
\delta_1
\le
\|H\|\sqrt{W_0}.
\]

This proves (8.2).

The important point is not the large numerical constant. It is that no factor \(N\), \(|J|\), or number of double-flip pairs survives.

---

# 9. Actual-law averaging

Fix one interval \(I=I_{N,r}\).

Use one coupled latent sine process \(X\) and output field \(Y\). Let

- \(\Pi_r^-\) be the posterior projection given \(Y_{I\setminus\{0\}}\);
- \(\Pi_r^+\) be the posterior given \(Y_I\);
- \(\widehat\Pi^-\) be the full posterior given every output except \(Y_0\).

## 9.1 Averaged finite boundary energy

By Lemma 7.1,

\[
U_0(\Pi_r^-;I)
\le
s_x^4U_0(\Pi_r^+;I).
\tag{9.1}
\]

For a projection DPP,

\[
\sum_{i\in I}
T_i(\Pi_r^+;I)
=
\operatorname{Var}(N_I\mid Y_I).
\tag{9.2}
\]

Also,

\[
\begin{aligned}
\sum_{i\in I}W_i(\Pi_r^+;I)
&=
\sum_{j\in I}
T_j
\sum_{\substack{i\in I\\i\ne j}}
|\Pi_{ji}^+|^2\\
&\le
\sum_{j\in I}T_j.
\end{aligned}
\tag{9.3}
\]

The law of total variance gives

\[
\mathbb E
\operatorname{Var}(N_I\mid Y_I)
\le
\operatorname{Var}_Q(N_I)
=
V_Q(N).
\tag{9.4}
\]

Averaging over all \(N\) anchor positions therefore yields

\[
\boxed{
\frac1N
\sum_{r=0}^{N-1}
\mathbb E
U_0(\Pi_r^-;I_{N,r})
\le
2s_x^4\frac{V_Q(N)}N.
}
\tag{9.5}
\]

This is exactly where the actual law replaces the cycle-03 worst-word bound.

## 9.2 Transport to the full posterior

Starting at \(\Pi_r^-\), reveal every output in

\[
O=\mathbb Z\setminus I.
\]

This is the projection flow of Section 6 with

\[
\|H\|=\log s_x.
\]

If

\[
U(t)=U_0(P_t;I),
\qquad
U(0)=U_r^-,
\]

then

\[
U(t)\le s_x^{3t}U_r^-.
\]

Applying the directional jet bound,

\[
\begin{aligned}
&
\left|
\mathscr K_{x,J}
(\widehat\Pi^-,Y_J)
-
\mathscr K_{x,J}
(\Pi_r^-,Y_J)
\right|\\
&\le
C_{\mathrm{jet}}
\int_0^1
(\log s_x)
\bigl(\sqrt{T(t)}+\sqrt{W(t)}\bigr)\,dt\\
&\le
\frac{2\sqrt2}{3}
C_{\mathrm{jet}}
\bigl(s_x^{3/2}-1\bigr)
\sqrt{U_r^-}.
\end{aligned}
\tag{9.6}
\]

At the full posterior, the omitted-coordinate tail satisfies

\[
\left|
\mathscr K_{x,\infty}(\widehat\Pi^-,Y)
-
\mathscr K_{x,J}(\widehat\Pi^-,Y_J)
\right|
\le
C_{\mathrm{jet}}U(1).
\tag{9.7}
\]

Keeping (9.7) linear and using (9.5) gives

\[
\begin{aligned}
&
\left|
F_{x,\infty}''(1/2)
-
\frac1N\sum_rF_{x,N,r}''(1/2)
\right|\\
&\le
2C_{\mathrm{jet}}s_x^7\frac{V_Q(N)}N\\
&\qquad+
\frac43C_{\mathrm{jet}}s_x^2
\bigl(s_x^{3/2}-1\bigr)
\sqrt{\frac{V_Q(N)}N}.
\end{aligned}
\tag{9.8}
\]

Alternatively, because \(U<1\), replace \(U(1)\) by \(\sqrt{U(1)}\). This yields the simpler bound

\[
\boxed{
\left|
F_{x,\infty}''(1/2)
-
\frac1N\sum_rF_{x,N,r}''(1/2)
\right|
\le
\frac{10}{3}
C_{\mathrm{jet}}s_x^{7/2}
\sqrt{\frac{V_Q(N)}N}.
}
\tag{9.9}
\]

Finally take \(x=cu\), dominate the monotone constants by their values at \(c\), and use

\[
\int_0^1u\,du=\frac12.
\]

This proves Theorem A.

---

# 10. Response-coordinate truncation remains separate

For a finite anchor model, let \(\tau_{r,L}(z)\) be the squared response energy in finite observed coordinates omitted from a chosen retained set \(L\).

The exact finite response-coordinate loss is

\[
\boxed{
\Delta_{N,L}^{\mathrm{resp}}(c)
=
\frac1N
\sum_{r=0}^{N-1}
\int_0^1
8u\,
\mathbb E_{cu,N,r}
\frac{\tau_{r,L}(z)^2}
{(1-4r_{r,z}^2)^2}
\,du.
}
\]

It is nonnegative. The coefficient \(8\) and the denominator were independently checked in the earlier review. citeturn605628view2

Define

\[
\underline\Gamma_{N,L}^{\mathrm{av}}(c)
=
\Gamma_N^{\mathrm{av}}(c)
-
\Delta_{N,L}^{\mathrm{resp}}(c).
\]

Then

\[
\box
