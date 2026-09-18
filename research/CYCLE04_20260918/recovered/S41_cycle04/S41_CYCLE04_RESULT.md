# S41 cycle 04 — actual-law averaged localization of the complete curvature jet

## Status

**PROVED_SCOPED — new, not yet independently reviewed.**

The result below is a quantitative observation-domain theorem for the frozen
half-filled, balanced-point sine functional.  It is relative to the finite
V14 grouped-curvature identity and the identification

\[
\Gamma(c)=\int_0^1u\,\mathbb E_{cu,\infty}\overline{\mathcal G}_{cu,\infty}\,du
\]

used in the frozen source.  The new part is the actual-law, random-anchor
localization of the **complete** curvature jet.  It controls the moving atom
law, posterior first and second derivatives, and all connected one- and
two-flip terms.  It is not merely a scalar posterior estimate.

It does not prove the ultimate all-parameter entropy-rate concavity theorem.
That target still asks for every `0<rho<1`, every `0<c<1`, and every legal
`a`, and still requires a bridge from this balanced half-density local
curvature to the Hessian of the true full-configuration entropy rate.

No claim of literature novelty is made.

---

## 1. Main result

Let `Q` be the half-filled sine projection on `ell^2(Z)`:

\[
Q_{ii}=\frac12,\qquad
Q_{ij}=\frac{\sin(\pi(i-j)/2)}{\pi(i-j)}\quad(i\ne j).
\]

For `N>=1` and `r=0,...,N-1`, put

\[
I_{N,r}=\{-r,-r+1,\ldots,N-1-r\},
\qquad J_{N,r}=I_{N,r}\setminus\{0\}.
\]

Thus the origin occupies each of the `N` possible positions in a length-`N`
observation interval.

For `x in [0,c]`, use the exact sine principal marginal

\[
K_x(h)=hI+x(Q-I/2).
\]

For `z in {0,1}^{J_{N,r}}`, let

\[
B_{r,z}(h)=K_{x,J_{N,r}}(h)-\operatorname{diag}(1-z),
\quad G_{r,z}(h)=B_{r,z}(h)^{-1},
\]

\[
b_r=xQ_{J_{N,r},0},
\qquad q_{r,z}(h)=h-b_r^*G_{r,z}(h)b_r,
\]

and let `w_{r,z}(h)` be the exact atom probability of `z`.  With

\[
\phi(q)=\left(q-\frac12\right)\log\frac q{1-q},
\]

define

\[
F_{x,N,r}(h)=\sum_z w_{r,z}(h)\phi(q_{r,z}(h)),
\]

\[
\overline F_{x,N}''=\frac1N\sum_{r=0}^{N-1}F_{x,N,r}''(1/2),
\]

and

\[
\boxed{
\Gamma_N^{\rm av}(c)
=\int_0^1u\,\overline F_{cu,N}''\,du .
}
\]

This is a finite object: a finite word sum for each anchor followed by a
one-dimensional integral.  It uses the exact unsmoothed sine marginal; there
is no Fejer, cyclic, or Toeplitz-to-projection replacement.

Put

\[
a_c=\frac2{1-c},\qquad
s_c=\sqrt{\frac{1+c}{1-c}},\qquad
C_{\rm jet}(c)=2^{28}a_c^{28}.
\]

Let

\[
V_Q(N)=\operatorname{Var}_Q\!\left(\sum_{j=0}^{N-1}X_j\right).
\]

Define

\[
\begin{aligned}
E_c^{\rm split}(N)
={}&C_{\rm jet}(c)s_c^7\frac{V_Q(N)}N\\
&+\frac23 C_{\rm jet}(c)s_c^2(s_c^{3/2}-1)
 \sqrt{\frac{V_Q(N)}N},
\end{aligned}
\]

\[
E_c^{\rm simple}(N)
=\frac53C_{\rm jet}(c)s_c^{7/2}
\sqrt{\frac{V_Q(N)}N},
\]

and

\[
E_c^{\rm av}(N)=
\min\{E_c^{\rm split}(N),E_c^{\rm simple}(N)\}.
\]

### Theorem A — effective complete-jet observation localization

For every fixed `0<c<1` and every `N>=1`,

\[
\boxed{
\left|\Gamma(c)-\Gamma_N^{\rm av}(c)\right|
\le E_c^{\rm av}(N).
}
\]

For the half-filled sine projection,

\[
V_Q(N)
=\frac2{\pi^2}
\left(
\sum_{\substack{1\le k\le N\\ k\ \rm odd}}\frac1k
+N\sum_{\substack{k>N\\k\ \rm odd}}\frac1{k^2}
\right)
\le\frac{\log N+4}{\pi^2}.
\]

Consequently,

\[
\boxed{
E_c^{\rm av}(N)
\le
\frac{5C_{\rm jet}(c)s_c^{7/2}}{3\pi}
\sqrt{\frac{\log N+4}{N}}
\longrightarrow0 .
}
\]

This replaces the cycle-03 worst-word stretched-log observation rate by a
power rate under the actual law.  The constants are intentionally
conservative; the gain is the mechanism and the `N`-dependence.

---

## 2. The complete finite derivative is retained

For a fixed finite observed set, abbreviate `B=B_z(1/2)`, `G=B^{-1}`,
`v=Gb`, `q=1/2-b^*Gb`, and `w=w_z(1/2)`.  Since `B'(h)=I`,

\[
w'=w\operatorname{tr}G,
\]

\[
w''=w\{(\operatorname{tr}G)^2-\operatorname{tr}(G^2)\},
\]

\[
q'=1+b^*G^2b=1+\|v\|^2,
\qquad
q''=-2b^*G^3b.
\]

Therefore

\[
\boxed{
\begin{aligned}
F_{x,N,r}''(1/2)
=\sum_z\{&w_z''\phi(q_z)
+2w_z'\phi'(q_z)q_z'\\
&+w_z[\phi''(q_z)(q_z')^2+\phi'(q_z)q_z'']\}.
\end{aligned}
}
\]

The probability acceleration, both cross terms, and the posterior first and
second derivatives are all present.

For localization it is useful to regroup the same expression.  Put

\[
\sigma_j=2z_j-1,
\quad o_j=\sigma_jG_{jj}-1,
\quad \bar r_j=\sigma_j-G_{jj}=-\sigma_jo_j.
\]

Sherman--Morrison gives

\[
G^{j}=G-\frac{\sigma_j}{o_j}Ge_je_j^*G,
\]

\[
v^{j}=v-\frac{\sigma_jv_j}{o_j}Ge_j,
\]

\[
d_j:=q(z^j)-q(z)=\frac{\sigma_j|v_j|^2}{o_j}.
\]

For a smooth `psi`, let

\[
\operatorname{Breg}_\psi(p,q)
=\psi(p)-\psi(q)-\psi'(q)(p-q),
\]

\[
\overline{\mathcal B}_\psi(z)
=\sum_j\bar r_j
\operatorname{Breg}_\psi(q(z^j),q(z)),
\]

and `A_z=1+||v_z||^2`.  The complete grouped kernel is

\[
\boxed{
\begin{aligned}
\overline{\mathcal G}(z)={}&
\phi''(q)+\overline{\mathcal B}_{\phi'}
+\sum_j(G^2)_{jj}\operatorname{Breg}_\phi(q(z^j),q)\\
&+\sum_j\bar r_j
 [\{\phi'(q(z^j))-\phi'(q)\}A_{z^j}
  -\phi''(q)d_jA_z]\\
&+\sum_j\bar r_j
 [\overline{\mathcal B}_\phi(z^j)
  -\overline{\mathcal B}_\phi(z)].
\end{aligned}
}
\tag{2.1}
\]

Here every sum is over the actually observed coordinates.

A short moving-law derivation shows that (2.1) is exactly the displayed full
second derivative.  Let

\[
(Tf)(z)=\sum_j\bar r_j(z)[f(z^j)-f(z)],
\qquad D=\partial_h+T.
\]

The determinant flip identity gives

\[
\frac d{dh}\mathbb E_h f_h=\mathbb E_h Df_h.
\]

Moreover,

\[
Dq=1,
\qquad DG=0,
\qquad Dv=0.
\]

For example,

\[
\sum_j\bar r_jd_j=-\sum_j|v_j|^2,
\]

which cancels the `||v||^2` part of `partial_h q`; and the flip correction to
`G` sums to `G^2`, cancelling `partial_hG=-G^2`.  Because a jump operator does
not obey the ordinary chain rule,

\[
D\psi(q)=\psi'(q)+\overline{\mathcal B}_\psi.
\]

Applying this first to `phi` and then to `phi' + B_phi` gives (2.1).  Thus the
localization theorem concerns the complete curvature jet, not `q` alone.

---

## 3. Posterior projection dictionary

Generate the output from a latent projection DPP `X~DPP(Q)` through the
balanced binary channel

\[
\Pr(Y_j=1\mid X_j)
=\frac12+x\left(X_j-\frac12\right).
\]

Write `y_j=2Y_j-1` and

\[
s_x=\sqrt{\frac{1+x}{1-x}}.
\]

If outputs are observed on a set `J`, define the diagonal multiplier

\[
D_J(y)e_j=
\begin{cases}
s_x^{y_j}e_j,&j\in J,\\e_j,&j\notin J.
\end{cases}
\]

If `Q=UU*`, the latent posterior is again a projection DPP, with projection

\[
\boxed{
\Pi_J
=D_JU(U^*D_J^2U)^{-1}U^*D_J,
}
\tag{3.1}
\]

that is, the orthogonal projection onto `D_J Ran(Q)`.

For an unobserved anchor `0`, the Schur data in Section 2 and the posterior
projection satisfy the exact identities

\[
\boxed{
q=\frac12+x\left(\Pi_{00}-\frac12\right),
}
\tag{3.2}
\]

\[
\boxed{
v_j=\frac{2x}{\sqrt{1-x^2}}\,y_j\Pi_{j0},
}
\tag{3.3}
\]

and, on the observed block,

\[
\boxed{
G=\frac2{1-x^2}
\{S-xS(2\Pi_J-I)S\},
\qquad S=\operatorname{diag}(y_j).
}
\tag{3.4}
\]

These follow by inserting (3.1) into the block Schur complement and checking
`BG=I`, `Bv=b`; (3.2) is also immediate from one-site Bayes conditioning.
In particular,

\[
|v_j|^2=\frac{4x^2}{1-x^2}|\Pi_{j0}|^2.
\]

For `x<=c`, all legal posterior data obey

\[
q\in[1/a_c,1-1/a_c],
\quad \|G\|\le a_c,
\quad \|v\|\le a_c,
\quad |o_j|^{-1}\le a_c.
\tag{3.5}
\]

---

## 4. Projection flow and boundary energy

Let `I` be a finite interval containing the anchor, `J=I\{0}`, and
`O=Z\I`.  For an orthogonal projection `P`, define

\[
T_0(P;I)=\sum_{k\in O}|P_{k0}|^2,
\]

\[
T_j(P;I)=\sum_{k\in O}|P_{kj}|^2,
\]

\[
W_0(P;I)=\sum_{j\in J}|P_{j0}|^2T_j(P;I),
\]

\[
U_0(P;I)=T_0(P;I)+W_0(P;I).
\tag{4.1}
\]

`T_0` measures how much of the anchor posterior-covariance column crosses the
observation boundary.  `W_0` is the second-order boundary energy required by
the `G_ij` and double-flip pieces of the curvature jet.

### Lemma 4.1 — diagonal tilt flow

Let `D_t=e^{tH}` with `H` real diagonal, and let `P_t` be the projection onto
`D_t Ran(P_0)`.  Then

\[
\boxed{
\dot P_t=(I-P_t)HP_t+P_tH(I-P_t).
}
\tag{4.2}
\]

Assume `H` is supported on `O` and `||H||<=h`.  For every `i in I`,

\[
\|\dot P_te_i\|
\le h\sqrt{T_i(P_t;I)}.
\tag{4.3}
\]

For the anchor boundary energy,

\[
|T_0'|\le2hT_0,
\]

\[
|W_0'|\le hT_0+3hW_0,
\]

and hence

\[
\boxed{
U_0(P_t;I)\le e^{3ht}U_0(P_0;I).
}
\tag{4.4}
\]

Also

\[
\boxed{
\|P_1e_0-P_0e_0\|
\le(e^h-1)\sqrt{T_0(P_0;I)}.
}
\tag{4.5}
\]

#### Proof

Differentiate the explicit projection formula to obtain (4.2).  Since
`He_i=0` for `i in I`,

\[
\dot P_te_i=(I-2P_t)HP_te_i.
\]

The involution `I-2P_t` is unitary, which proves (4.3).  Differentiating
`T_0` gives the first bound.  For `W_0`, use the row bound

\[
\sum_j|\dot P_{0j}|^2\le h^2T_0
\]

and `|T_j'|<=2hT_j`:

\[
\begin{aligned}
|W_0'|
&\le2\sum_{j\in J}|P_{0j}||\dot P_{0j}|T_j
 +2hW_0\\
&\le2h\sqrt{T_0W_0}+2hW_0\\
&\le hT_0+3hW_0.
\end{aligned}
\]

This proves (4.4).  Integrating (4.3) together with
`T_0(t)<=e^{2ht}T_0(0)` gives (4.5).

### Lemma 4.2 — adding the anchor output

Let `P^-` be the posterior projection after observing `Y_J`, and let `P^+`
be the posterior after additionally observing `Y_0`.  Then, pointwise in the
observed word,

\[
\boxed{
U_0(P^-;I)\le s_x^4U_0(P^+;I).
}
\tag{4.6}
\]

#### Proof

Interpolate by scaling only coordinate `0`.  If the logarithmic scale is
`eta`, `|eta|<=log s_x`, then for `k in O` and `j in J`,

\[
\dot P_{k0}=\eta(1-2P_{00})P_{k0},
\]

\[
\dot P_{0j}=\eta(1-2P_{00})P_{0j},
\]

\[
E_O\dot P e_j=-2\eta P_{0j}E_OPe_0.
\]

Consequently

\[
|T_0'|\le2|\eta|T_0,
\]

\[
|W_0'|\le2|\eta|T_0+4|\eta|W_0,
\]

so `|U_0'|<=4|eta|U_0`.  Integrating in either direction proves (4.6).

---

## 5. Complete-jet algebraic localization

For a projection `P`, word signs `y`, and a finite coordinate set `J`, let
`K_{x,J}(P,y_J)` denote the complete kernel (2.1), with `q,v,G` supplied by
(3.2)--(3.4) and every one- and two-flip sum restricted to `J`.

The following lemma is the part that upgrades a scalar posterior estimate to
a complete curvature-jet estimate.

### Lemma 5.1 — tail and directional jet bounds

Fix `x<=c`.  Let `I=J union {0}` and use (4.1).  Then

\[
\boxed{
|\mathscr K_{x,Z\setminus\{0\}}(P,y)
 -\mathscr K_{x,J}(P,y_J)|
\le C_{\rm jet}(c)U_0(P;I).
}
\tag{5.1}
\]

If `P_t` is a diagonal-tilt path whose generator `H` is supported on `O`,
then

\[
\boxed{
\left|\frac d{dt}\mathscr K_{x,J}(P_t,y_J)\right|
\le C_{\rm jet}(c)\|H\|
 [\sqrt{T_0(P_t;I)}+\sqrt{W_0(P_t;I)}].
}
\tag{5.2}
\]

#### Proof: primitive bounds

Write

\[
p_j=|P_{j0}|,\qquad g_{ij}=|P_{ij}|.
\]

Projection identities give

\[
\sum_jp_j^2\le\frac14,
\qquad
\sum_kg_{jk}^2=P_{jj}\le1.
\tag{5.3}
\]

From (3.2)--(3.5),

\[
|v_j|\le a_cp_j,
\qquad
|G_{ij}|\le2a_cg_{ij}\quad(i\ne j),
\qquad
|d_j|\le a_c^3p_j^2.
\tag{5.4}
\]

The derivatives of `phi` on `[1/a_c,1-1/a_c]` satisfy

\[
|\phi''|\le a_c^4,
\quad |\phi'''|\le a_c^6,
\quad |\phi''''|\le5a_c^8.
\tag{5.5}
\]

For a projection direction `dot P`, define

\[
\delta_0=\|\dot Pe_0\|,
\qquad
\delta_1=
\left(\sum_{j\in J}p_j^2\|\dot Pe_j\|^2\right)^{1/2}.
\tag{5.6}
\]

Differentiating (3.2)--(3.4) and the rank-one flip formulas gives

\[
|\dot q|\le\delta_0,
\quad \|\dot v\|\le a_c\delta_0,
\quad \|\dot Ge_j\|\le2a_c\|\dot Pe_j\|,
\tag{5.7}
\]

\[
|\dot d_j|
\le2a_c^3p_j|\dot P_{j0}|
 +2a_c^5p_j^2\|\dot Pe_j\|.
\tag{5.8}
\]

Hence

\[
\sum_j|\dot d_j|
+\sum_j|d_j\dot d_j|
\le4a_c^8(\delta_0+\delta_1).
\tag{5.9}
\]

One-flip derivatives, including `dot A_{z^j}`, obey the same weighted norm
with a factor at most `2^8 a_c^12`.  This follows by differentiating

\[
v^j=v-\frac{\sigma_jv_j}{o_j}Ge_j,
\qquad |o_j|^{-1}\le a_c.
\tag{5.10}
\]

#### Proof: tail monomials

The connected double-flip expansion of (2.1) is controlled by the five
nonnegative prototypes

\[
K_1=g_{ij}p_i^3p_j,
\quad K_2=g_{ij}^2p_i^4,
\quad K_3=g_{ij}^2p_i^2p_j^2,
\quad K_4=g_{ij}^4p_i^4,
\]

and the corresponding connected `|d_j|D_{ij}^2` term.  On the union where
`i in O` or `j in O`, Cauchy--Schwarz and (5.3) give

\[
\sum K_1\le2(T_0+W_0),
\]

\[
\sum K_2\le T_0+W_0,
\]

\[
\sum K_3\le2T_0,
\]

\[
\sum(K_4+K_4^{\rm swapped})\le2(T_0+W_0).
\tag{5.11}
\]

For example, the only superficially linear tail is the part of `K_1` with
`j in O`:

\[
\begin{aligned}
\sum_{i\in J,j\in O}g_{ij}p_i^3p_j
&\le\sqrt{T_0}\sum_{i\in J}p_i^3\sqrt{T_i}\\
&\le\sqrt{T_0W_0}
\le\frac12(T_0+W_0).
\end{aligned}
\]

For the connected remainder, (5.10) gives

\[
D_{ij}\le2a_c^3p_i^2+8a_c^7p_j^2g_{ij}^2,
\]

and therefore

\[
\sum_{i\in O\ {m or}\ j\in O}|d_j|D_{ij}^2
\le144a_c^{17}(T_0+W_0).
\tag{5.12}
\]

Substitution into the connected expansion, together with the one-flip terms,
gives a total below `2^13 a_c^22 (T_0+W_0)`, which is bounded by the stated
`C_jet U_0`.  This proves (5.1).

#### Proof: marked monomials

Differentiate the same connected expansion before taking absolute values.
Every term is one of the prototypes in (5.11), with exactly one factor marked
by a derivative, together with the differentiated connected term (5.12).
The useful row estimates are

\[
\sum_jp_j|\dot P_{ij}|
\le\|\dot Pe_i\|\left(\sum_jp_j^2\right)^{1/2},
\]

\[
\sum_jg_{ij}|\dot P_{ij}|
\le\|\dot Pe_i\|,
\tag{5.13}
\]

and their column analogues.  They prevent any factor proportional to `|J|`.
For instance,

\[
\sum_{i,j}p_i^3p_j|\dot P_{ij}|
\le\sum_ip_i^3\|\dot Pe_i\|
\le\delta_1,
\]

while differentiating either `p` factor costs at most a constant times
`delta_0`.  The four prototype families contribute respectively at most

\[
8a_c^5,
\quad16a_c^6,
\quad24a_c^6,
\quad64a_c^8
\]

times `delta_0+delta_1`.  The differentiated connected family, including
all derivatives of `o_j^{-1}`, one- and two-flip `A` factors, and Bregman
remainders, contributes at most

\[
2^{22}a_c^{27}(\delta_0+\delta_1).
\]

The base and three single-sum groups together contribute less than
`2^14 a_c^20(delta_0+delta_1)`.  Thus the deliberately rounded constant
`2^28 a_c^28` gives

\[
|D\mathscr K_{x,J}(P)[\dot P]|
\le C_{\rm jet}(c)(\delta_0+\delta_1).
\tag{5.14}
\]

Along the outside tilt flow, Lemma 4.1 gives

\[
\delta_0\le\|H\|\sqrt{T_0},
\qquad
\delta_1\le\|H\|\sqrt{W_0},
\]

which proves (5.2).

The role of the very large constant is only to make every finite algebraic
branch explicit.  The dimension-free weighting in (5.13), not the constant,
is the essential new feature.

---

## 6. Actual-law averaging pays the observation boundary

Fix an interval `I=I_{N,r}`.  Couple all posteriors using one latent sine DPP
`X` and one channel output field `Y`.

Let

* `Pi_r^-` be the latent posterior projection given `Y_{I\setminus{0}}`;
* `Pi_r^+` be the posterior given `Y_I`;
* `widehat Pi^-` be the posterior given every output except `Y_0`.

### 6.1 Boundary energy before observing the center

By Lemma 4.2,

\[
U_0(\Pi_r^-;I)
\le s_x^4U_0(\Pi_r^+;I).
\tag{6.1}
\]

For a projection DPP, conditional count variance equals cross-boundary
Hilbert--Schmidt mass:

\[
\sum_{i\in I}T_i(\Pi_r^+;I)
=\operatorname{Var}(N_I\mid Y_I).
\tag{6.2}
\]

Moreover,

\[
\sum_{i\in I}W_i(\Pi_r^+;I)
\le\sum_{i\in I}T_i(\Pi_r^+;I).
\tag{6.3}
\]

The law of total variance gives

\[
\mathbb E\operatorname{Var}(N_I\mid Y_I)
\le\operatorname{Var}_Q(N_I)=V_Q(N).
\tag{6.4}
\]

Averaging over the `N` possible anchor locations and translating each interval
to `[0,N-1]` therefore yields

\[
\boxed{
\frac1N\sum_{r=0}^{N-1}
\mathbb E U_0(\Pi_r^-;I_{N,r})
\le2s_x^4\frac{V_Q(N)}N.
}
\tag{6.5}
\]

This is the actual-law step.  No worst-word resolvent tail appears.

### 6.2 Transport from finite to full observation

Starting from `Pi_r^-`, reveal the outputs in `O=Z\I`.  This is the diagonal
flow of Lemma 4.1 with

\[
\|H\|=\log s_x.
\]

Let `U(t)=U_0(P_t;I)` and `U(0)=U_r^-`.  By (4.4),

\[
U(t)\le s_x^{3t}U_r^-.
\]

Using (5.2),

\[
\begin{aligned}
|\mathscr K_{x,J}(\widehat\Pi^-,Y_J)
-\mathscr K_{x,J}(\Pi_r^-,Y_J)|
&\le C_{\rm jet}\int_0^1
 (\log s_x)(\sqrt{T(t)}+\sqrt{W(t)})\,dt\\
&\le\frac{2\sqrt2}{3}C_{\rm jet}
 (s_x^{3/2}-1)\sqrt{U_r^-}.
\end{aligned}
\tag{6.6}
\]

At the full posterior, (5.1) gives the omitted-coordinate tail

\[
|\mathscr K_{x,\infty}(\widehat\Pi^-,Y)
-\mathscr K_{x,J}(\widehat\Pi^-,Y_J)|
\le C_{\rm jet}U(1).
\tag{6.7}
\]

Since every projection satisfies `T_0<=1/4`, `W_0<=1/16`, one also has
`U<=5/16<1`.  Thus (6.7) can either be kept linear, or changed to a square-root
bound.  Combining (6.5)--(6.7) gives two valid averaged estimates:

\[
\begin{aligned}
&\left|
F_{x,\infty}''(1/2)-\frac1N\sum_rF_{x,N,r}''(1/2)
\right|\\
&\le
2C_{\rm jet}(c)s_x^7\frac{V_Q(N)}N
+\frac43C_{\rm jet}(c)s_x^2(s_x^{3/2}-1)
 \sqrt{\frac{V_Q(N)}N},
\end{aligned}
\tag{6.8}
\]

and the simpler

\[
\boxed{
\left|
F_{x,\infty}''(1/2)-\frac1N\sum_rF_{x,N,r}''(1/2)
\right|
\le\frac{10}{3}C_{\rm jet}(c)s_x^{7/2}
\sqrt{\frac{V_Q(N)}N}.
}
\tag{6.9}
\]

Finally set `x=cu`, use monotonicity of the displayed constants in `x`, and
integrate with `int_0^1 u du=1/2`.  Equations (6.8)--(6.9) give Theorem A.

---

## 7. Response-coordinate loss remains separate

For each finite anchor model, let `tau_{r,L}(z)` be the squared response
energy in finite observed coordinates not retained in a selected set `L`.
The exact finite response-coordinate loss is

\[
\Delta_{N,L}^{\rm resp}(c)
=\frac1N\sum_{r=0}^{N-1}
\int_0^1 8u\,
\mathbb E_{cu,N,r}
\frac{\tau_{r,L}(z)^2}{(1-4r_{r,z}^2)^2}\,du
\ge0.
\]

Define

\[
\underline\Gamma_{N,L}^{\rm av}(c)
=\Gamma_N^{\rm av}(c)-\Delta_{N,L}^{\rm resp}(c).
\]

Then

\[
\boxed{
\underline\Gamma_{N,L}^{\rm av}(c)-E_c^{\rm av}(N)
\le\Gamma(c)
\le
\underline\Gamma_{N,L}^{\rm av}(c)
+\Delta_{N,L}^{\rm resp}(c)+E_c^{\rm av}(N).
}
\]

If every finite response coordinate is retained, `Delta_resp=0`.

The error ledger is therefore:

1. response-coordinate truncation: the explicit nonnegative `Delta_resp`;
2. observation-domain truncation: `E_c^av(N)` from Theorem A;
3. kernel/volume replacement: exactly zero;
4. numerical quadrature and rounding: must be paid separately by interval
   arithmetic in any sign certificate.

---

## 8. What happens at `c=19/20`

The accompanying floating-point diagnostic gives

\[
\begin{array}{c|c}
N&\Gamma_N^{\rm av}(19/20)\\ \hline
4&6.8559375\ldots\\
6&8.2609199\ldots\\
8&9.2421388\ldots
\end{array}
\]

These values are exploratory only.  With the deliberately conservative jet
constant, at `N=8` the analytic observation remainder is about

\[
4.60\times10^{55},
\]

so it overwhelms the finite value.  Therefore:

\[
\boxed{
\text{No finite radius is certified here to prove }
\Gamma(19/20)>0.
}
\]

This does not show that no such radius exists.  It shows that the present
explicit constants, although giving a power-rate theorem, are not yet a
practical sign mechanism near `c=1`.

The obstruction in the constants is transparent:

\[
a_c\asymp(1-c)^{-1},
\qquad s_c\asymp(1-c)^{-1/2},
\]

and the raw algebraic tally uses `a_c^28`.  A practical `c=0.95` certificate
needs either a much sharper expectation-level jet inequality, or a
score-orthogonal cancellation that replaces first-order transport by a
quadratic boundary-energy term.

---

## 9. Scope relative to the ultimate target

### Paid by this result

* finite observation uses exact unsmoothed sine principal marginals;
* the complete moving-law derivative is retained;
* scalar posterior, response vector, resolvent columns, one-flip terms, and
  connected two-flip terms are localized together;
* observation error is actual-law averaged and dimension-free;
* the rate is `O_c(sqrt(log N/N))`;
* response-coordinate and observation-domain losses are distinct;
* no Fejer/cyclic replacement is used.

### Not paid

* no interval-certified sign of `Gamma(19/20)`;
* no practical near-`c=1` radius;
* no extension in this manuscript from `rho=1/2` to arbitrary `rho`;
* no extension from the balanced point to every legal `a`;
* no proof that the limiting local curvature equals the second derivative of
  the true entropy rate at all parameters;
* no proof of the ultimate all-parameter sine entropy-rate concavity target.

The projection-flow mechanism itself is transferable: diagonal likelihood
tilts of any projection DPP obey (4.2), and conditional number variance still
pays boundary Hilbert--Schmidt mass.  What is not yet transferred is the exact
balanced half-filled curvature algebra and its uniform endpoint control.

---

## 10. Computational checks

`S41_CYCLE04_checks.py` performs the following non-rigorous diagnostics:

1. exact atom enumeration of every term in the complete finite derivative;
2. equality of that derivative with the V14 grouped kernel for small systems;
3. the posterior-projection dictionary (3.2)--(3.4);
4. the outside-flow bounds `U(1)<=s^3U(0)` and
   `||P_1e_0-P_0e_0||<=(s-1)sqrt(T_0)`;
5. the one-site update bound `U^-<=s^4U^+`;
6. exact sine number variance and the displayed analytic remainder;
7. floating-point values of `Gamma_N^av(c)` for small `N`.

The code deliberately does not label floating-point positivity as a proof.
