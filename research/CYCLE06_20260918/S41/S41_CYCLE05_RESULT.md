# S41 cycle-05 — the complete-jet lemma: exact obstruction and repaired theorem

## Status

**REFUTED_AND_REPAIRED_SCOPED — new author derivation, not independent certification.**

The first half of the cycle-04 complete-jet lemma is valid: the complete V14
kernel has a dimension-free coordinate tail bounded by the original energy
`T_0+W_0`.  The second half is false.  There is an exact finite-dimensional
posterior-projection example with `T_0=W_0=0` but nonzero directional
curvature derivative.  The missing quantity is

\[
 Z_0(P;I)=\sum_{i\in J}T_i(P;I)
           \sum_{j\in J}|P_{ij}|^2|P_{j0}|^2.
\]

With

\[
 \widetilde U_0=T_0+W_0+Z_0,
\]

the directional estimate closes, the energy is stable under both diagonal
flows used in the finite-to-full interpolation, and its actual-law
random-anchor mean is bounded by the same conditional number variance.  The
repaired observation-localization theorem therefore retains the rate

\[
 O_c\!\left(\sqrt{\frac{\log N}{N}}\right)
\]

for the frozen balanced half-filled sine functional.  The constants proved
here are existence constants, not practical sign-certification constants.

This manuscript does **not** prove the ultimate all-`rho`, all-`c`, all-legal-`a`
Shannon entropy-rate concavity theorem.  It concerns only the frozen balanced,
half-filled local curvature representation and uses the exact unsmoothed sine
marginals.  Identification of that local representation with the intended
infinite functional remains a separately labelled dependency.

---

# 1. Finite complete-jet algebra

Work first on a finite coordinate set

\[
 \{0\}\sqcup E,\qquad E=J\sqcup O,
\]

with an orthogonal projection `P`, a sign word `y in {+1,-1}^E`, and
`0<=x<=c<1`.  Put

\[
 A_c=\frac{2}{1-c}\ge2.
\]

For an unobserved anchor `0`, the posterior-projection/Schur dictionary is

\[
 q=\frac12+x\left(P_{00}-\frac12\right),
\]

\[
 v_i=\frac{2x}{\sqrt{1-x^2}}\,y_iP_{i0},
\]

\[
 G=\frac{2}{1-x^2}
 \{S-xS(2P_E-I)S\},\qquad S=\operatorname{diag}(y_i).
\]

Write

\[
 r_i=y_i-G_{ii},\qquad d_i=q^i-q=-\frac{|v_i|^2}{r_i}.
\]

Flipping coordinate `j` gives the exact rank-one identities

\[
 G^j=G+\frac1{r_j}Ge_je_j^*G,
\]

\[
 v^j=v+\frac{v_j}{r_j}Ge_j,
\]

\[
 q^j=q+d_j.
\]

For `i!=j`,

\[
 r_i^j=r_i-\frac{|G_{ij}|^2}{r_j},
\]

\[
 v_i^j=v_i+\frac{G_{ij}v_j}{r_j},
\]

\[
 d_i^j=-\frac{|v_i^j|^2}{r_i^j}.
\]

For `i=j`, `r_i^i=-1/r_i` and `d_i^i=-d_i`.

For a smooth function `f`, define

\[
 B_f(q,d)=f(q+d)-f(q)-f'(q)d.
\]

Let

\[
 R_{i,E}=\sum_{k\in E}|G_{ki}|^2,
\qquad
 A_E=1+\sum_{k\in E}|v_k|^2,
\qquad
 A_E^i=1+\sum_{k\in E}|v_k^i|^2.
\]

For

\[
 \phi(q)=\left(q-\frac12\right)\log\frac q{1-q},
\]

the complete grouped V14 kernel is exactly

\[
\begin{aligned}
 \mathscr K_{x,E}(P,y_E)
 ={}&\phi''(q)
 +\sum_{i\in E}r_iB_{\phi'}(q,d_i)\\
 &+\sum_{i\in E}R_{i,E}B_\phi(q,d_i)\\
 &+\sum_{i\in E}r_i
 \{[\phi'(q+d_i)-\phi'(q)]A_E^i
       -\phi''(q)d_iA_E\}\\
 &+\sum_{i,j\in E}C_{ij},
\end{aligned}
\tag{1.1}
\]

where the connected ordered-pair term is

\[
 \boxed{
 C_{ij}=r_j\{r_i^jB_\phi(q+d_j,d_i^j)
                 -r_iB_\phi(q,d_i)\}.
 }
\tag{1.2}
\]

Equation (1.2) is obtained by expanding, without omission, the last V14 group

\[
 \sum_j r_j\{\overline{\mathcal B}_\phi(y^j)
                    -\overline{\mathcal B}_\phi(y)\}.
\]

Thus (1.1) is an exhaustive finite expression: one base term, three
single-index groups, and one ordered double-index group.

All one- and two-flip posteriors lie in

\[
 \left[\frac1{A_c},1-\frac1{A_c}\right].
\]

The diagonal formula for `G` also gives

\[
 A_c^{-1}\le |r_i|\le A_c.
\]

Further,

\[
 \|G\|,\|G^i\|\le A_c,
 \qquad \|v\|,\|v^i\|\le A_c.
\tag{1.3}
\]

Put

\[
 p_i=|P_{i0}|,\qquad g_{ij}=|P_{ij}|.
\]

Then

\[
 |v_i|\le A_cp_i,
 \qquad |G_{ij}|\le2A_cg_{ij}\quad(i\ne j),
\tag{1.4}
\]

and the projection identities give

\[
 \sum_i p_i^2\le\frac14,
 \qquad \sum_k g_{ik}^2=P_{ii}\le1.
\tag{1.5}
\]

On the legal posterior interval we use the safe bounds

\[
 M_2:=\|\phi''\|_\infty\le A_c^4,
\quad
 M_3:=\|\phi'''\|_\infty\le A_c^6,
\quad
 M_4:=\|\phi''''\|_\infty\le5A_c^8.
\tag{1.6}
\]

---

# 2. Exact refutation of the old directional estimate

The cycle-04 claim

\[
 \left|\frac d{dt}\mathscr K_{x,J}(P_t,y_J)\right|
 \le C(c)\|H\|\{\sqrt{T_0}+\sqrt{W_0}\}
\tag{2.1}
\]

is false for every finite choice of `C(c)`.

## 2.1 Exact projection

Let

\[
 U=
 \begin{pmatrix}
 1/2&0\\
 \sqrt{3/8}&\sqrt{3/8}\\
 0&1/(2\sqrt2)\\
 0&-1/(2\sqrt2)\\
 \sqrt{3/8}&-\sqrt{3/8}
 \end{pmatrix},
 \qquad
 w=\begin{pmatrix}0\\0\\1/\sqrt2\\1/\sqrt2\\0\end{pmatrix}.
\]

Then

\[
 U^*U=I_2,\qquad U^*w=0.
\]

Put

\[
 B=UU^*,\qquad A(\lambda)=B+\lambda ww^*.
\]

At `lambda=1/2`,

\[
 A-A^2=\frac14ww^*.
\]

Hence

\[
 P=
 \begin{pmatrix}
 A(1/2)&\frac12ww^*\\
 \frac12ww^*&I-A(1/2)
 \end{pmatrix}
\tag{2.2}
\]

is an exact rank-three orthogonal projection on two copies of `R^5`.

Take the first copy as

\[
 I=\{0,1,2,3,4\},\qquad J=\{1,2,3,4\},
\]

and the second copy as `O`.  Direct exact calculation gives

\[
 T_0=0,
\qquad
 W_0=0.
\tag{2.3}
\]

The nonzero anchor couplings are only at coordinates `1` and `4`, and those
two columns have no component in `O`.  In contrast, the repaired energy below
is

\[
 Z_0=\frac9{4096}>0.
\tag{2.4}
\]

## 2.2 Exact V14 derivative

Choose

\[
 x=\frac12,
 \qquad y_1=y_2=y_3=y_4=+1.
\]

Construct `q,v,G` from the upper-left compression `A(lambda)` by the exact
dictionary in Section 1.  Substitution into the full kernel (1.1), including
all ordered connected pairs, simplifies to

\[
 \boxed{
 \mathscr K_{1/2,J}(\lambda,+)
 =\frac13\log\frac{16\lambda-29}{16\lambda-27}
  -\frac92\log5+\frac92\log3+\frac{544}{45}.
 }
\tag{2.5}
\]

Therefore

\[
 \left.\frac{d\mathscr K}{d\lambda}\right|_{\lambda=1/2}
 =\frac{32}{1197}.
\tag{2.6}
\]

Let `H` be the identity on the two outside coordinates spanning `w` and zero
elsewhere.  The projection onto `exp(tH) Ran(P)` has upper-left compression

\[
 B+\lambda(t)ww^*,
 \qquad
 \lambda(t)=\frac1{1+e^{2t}}.
\]

Thus

\[
 \boxed{
 \left.\frac d{dt}\mathscr K_{1/2,J}(P_t,+)\right|_{t=0}
 =-\frac{16}{1197}\ne0.
 }
\tag{2.7}
\]

For an actual binary-channel reveal at `x=1/2`, replace the unit generator by

\[
 H=(\log s_{1/2})E_O,
 \qquad s_{1/2}=\sqrt3.
\]

Then the derivative is the equally nonzero legal value

\[
 -\frac{8\log3}{1197}.
\tag{2.8}
\]

This projection is in the legal posterior-projection class.  Given the signs
`y_J=+`, let `D_J` multiply the four observed coordinates by `s_{1/2}` and
choose the prior projection to be the projection onto

\[
 D_J^{-1}\operatorname{Ran}(P).
\]

After observing that positive-probability word, the posterior projection is
exactly `P`.  The intermediate `P_t` need not itself be a posterior for a
binary word; it is precisely the bounded diagonal-likelihood interpolation
used in the finite-to-full proof.  Every `P_t` remains an orthogonal
projection.

All four non-connected groups in (1.1) have zero `lambda` derivative at
`lambda=1/2`; the entire value `32/1197` comes from eight active-inactive
ordered connected pairs.

## 2.3 The missed monomial

In this example an anchor-inactive coordinate `i` has

\[
 p_i=0,\qquad T_i>0,
\]

while an anchor-active coordinate `j` has `p_j>0` and `g_{ij}>0`.  Before
flipping `j`, `d_i=0`; after flipping `j`,

\[
 v_i^j=\frac{G_{ij}v_j}{r_j}\ne0,
 \qquad
 d_i^j\asymp g_{ij}^2p_j^2.
\]

Differentiating the coefficient `r_i^j` in the connected Bregman term creates
an unavoidable marked family

\[
 \|\dot Pe_i\|\,g_{ij}^4p_j^4.
\tag{2.9}
\]

Neither `T_0` nor `W_0=sum p_i^2T_i` sees it when `p_i=0`.  This is the exact
coverage failure in the cycle-04 marked-monomial argument.

---

# 3. The original tail estimate is valid

For the finite partition `E=J sqcup O`, define

\[
 T_0=\sum_{o\in O}p_o^2,
 \qquad
 T_i=\sum_{o\in O}g_{oi}^2\quad(i\in J),
\]

\[
 W_0=\sum_{i\in J}p_i^2T_i,
 \qquad
 U_0=T_0+W_0.
\tag{3.1}
\]

## Theorem 3.1 — complete-kernel tail

For every finite projection, every sign word, every `0<=x<=c<1`, and every
partition `E=J sqcup O`,

\[
 \boxed{
 |\mathscr K_{x,E}(P,y_E)-\mathscr K_{x,J}(P,y_J)|
 \le C_{\rm tail}(c)U_0,
 }
\tag{3.2}
\]

with the explicit valid constant

\[
 \boxed{
 C_{\rm tail}(c)=2^{12}A_c^{25}.
 }
\tag{3.3}
\]

### 3.1 Bregman calculus

For `B(q,d)=B_phi(q,d)`, the integral remainder formula gives

\[
 |B(q,d)|\le\frac{M_2}{2}d^2.
\tag{3.4}
\]

If both endpoint pairs are legal, put

\[
 D=\max\{|d|,|d+\eta|\}.
\]

Since

\[
 \partial_dB=\phi'(q+d)-\phi'(q),
 \qquad
 \partial_qB=B_{\phi'}(q,d),
\]

integration along the segment from `(q,d)` to `(q+e,d+eta)` gives

\[
 \boxed{
 |B(q+e,d+\eta)-B(q,d)|
 \le M_2D|\eta|+\frac{M_3}{2}D^2|e|.
 }
\tag{3.5}
\]

For `i!=j`, set

\[
 D_{ij}=\max\{|d_i|,|d_i^j|\},
 \qquad \eta_{ij}=d_i^j-d_i.
\]

The exact flip formulas imply

\[
 D_{ij}
 \le8A_c^7\{p_i^2+g_{ij}^2p_j^2\},
\tag{3.6}
\]

\[
 |\eta_{ij}|
 \le4A_c^7
 \{g_{ij}p_ip_j+g_{ij}^2(p_i^2+p_j^2)\}.
\tag{3.7}
\]

Indeed, write

\[
 u=\frac{G_{ij}v_j}{r_j},
 \qquad
 \rho=\frac{|G_{ij}|^2}{r_j}.
\]

Then `v_i^j=v_i+u`, `r_i^j=r_i-rho`,

\[
 |u|\le2A_c^3g_{ij}p_j,
\]

and subtracting `-|v_i|^2/r_i` from
`-|v_i+u|^2/(r_i-rho)` proves (3.6)--(3.7).

### 3.2 Exact connected-pair bound

For `i!=j`, (1.2) becomes

\[
 \boxed{
 C_{ij}
 =-|G_{ij}|^2B_\phi(q+d_j,d_i^j)
  +r_ir_j\{B_\phi(q+d_j,d_i^j)-B_\phi(q,d_i)\}.
 }
\tag{3.8}
\]

Define

\[
\begin{aligned}
 \Omega_{ij}={}&
 g_{ij}p_ip_j(p_i^2+p_j^2)\\
 &+g_{ij}^2(p_i^2+p_j^2)^2\\
 &+p_i^2p_j^2(p_i^2+p_j^2).
\end{aligned}
\tag{3.9}
\]

Substituting (3.4)--(3.7) into (3.8) gives, term by term,

\[
\begin{aligned}
 |C_{ij}|
 \le{}&128A_c^{20}g_{ij}^2X_{ij}^2
       +32A_c^{20}X_{ij}Y_{ij}
       +32A_c^{25}X_{ij}^2p_j^2,
\end{aligned}
\]

where

\[
 X_{ij}=p_i^2+g_{ij}^2p_j^2,
 \quad
 Y_{ij}=g_{ij}p_ip_j+g_{ij}^2(p_i^2+p_j^2).
\]

Because `p_i,g_ij<=1`, expansion of the three products yields

\[
 \boxed{
 |C_{ij}|\le2^8A_c^{25}\Omega_{ij}.
 }
\tag{3.10}
\]

For `i=j`, the exact identities `r_i^i=-1/r_i`, `d_i^i=-d_i` give

\[
 C_{ii}=-B_\phi(q+d_i,-d_i)-r_i^2B_\phi(q,d_i),
\]

hence

\[
 |C_{ii}|\le A_c^{12}p_i^4.
\tag{3.11}
\]

### 3.3 Exhaustive tail summation

Let `R` be the ordered pairs with `i in O` or `j in O`.  The three rows of
(3.9) have the following complete bounds:

| tail family | bound over `R` |
|---|---:|
| `g_ij p_i p_j(p_i^2+p_j^2)` | `<=2(T_0+W_0)` |
| `g_ij^2(p_i^2+p_j^2)^2` | `<=4(T_0+W_0)` |
| `p_i^2p_j^2(p_i^2+p_j^2)` | `<=T_0` |

For example, the only apparently linear part is

\[
 \sum_{i\in J,j\in O}g_{ij}p_i^3p_j
 \le\frac12\sqrt{T_0W_0}
 \le\frac14(T_0+W_0).
\]

All remaining entries follow directly from (1.5), after splitting `R` into
`i in O` and `i in J,j in O`.  Thus

\[
 \sum_{(i,j)\in R}\Omega_{ij}\le7U_0.
\tag{3.12}
\]

The other three groups in (1.1) have no hidden pair terms.  Their complete
ledger is:

| group omitted when passing from `E` to `J` | bound |
|---|---:|
| `sum r_i B_{phi'}` | `(1/2)A_c^13 T_0` |
| `sum R_i B_phi` | `(1/2)A_c^12T_0+2A_c^12W_0` |
| `A^i,A` group | `5A_c^10T_0+8A_c^14W_0` |
| diagonal connected terms | `A_c^12T_0` |
| off-diagonal connected terms | `7*2^8 A_c^25 U_0` |

For the `A` group one uses

\[
 A_E-A_J\le A_c^2T_0,
\]

and, for `i in J`,

\[
 A_E^i-A_J^i
 \le2A_c^2T_0+8A_c^6p_i^2T_i.
\]

The displayed ledger sums to less than `2^12 A_c^25 U_0`, proving
Theorem 3.1.

### 3.4 Infinite kernel

For an infinite orthogonal projection on `ell^2(Z)`, define
`K_{x,J}` for finite `J` by (1.1).  Every group is absolutely summable:

* the single-index groups are dominated by constants times `sum p_i^2`;
* the diagonal connected group is dominated by `sum p_i^4`;
* the off-diagonal group is dominated by `sum Omega_ij`, which is finite by
  (3.12) with `J` empty.

If `J_n` increases to `Z\{0}`, then

\[
 T_0(J_n)\to0
\]

by square summability of the anchor column, and

\[
 W_0(J_n)
 =\sum_{i\in J_n}p_i^2
   \sum_{o\notin J_n}|P_{oi}|^2\to0
\]

by dominated convergence.  Theorem 3.1 therefore makes `K_{x,J_n}` Cauchy,
independently of the exhaustion.  This defines the complete infinite kernel
and proves (3.2) with `O` equal to the full complement.

---

# 4. Repaired directional calculus

The new energy is

\[
 S_i=\sum_{j\in J}g_{ij}^2p_j^2,
\]

\[
 \boxed{
 Z_0=\sum_{i\in J}T_iS_i,
 \qquad
 \widetilde U_0=T_0+W_0+Z_0.
 }
\tag{4.1}
\]

## Theorem 4.1 — finite complete-jet derivative

Let `P_t` be any differentiable path of orthogonal projections.  Put

\[
 h_i=|\dot P_{i0}|,
 \quad e_i=\|\dot Pe_i\|,
 \quad \gamma_{ij}=|\dot P_{ij}|,
\]

\[
 \delta_0=\|\dot Pe_0\|,
\]

\[
 \delta_1=
 \left(\sum_{i\in J}p_i^2e_i^2\right)^{1/2},
\]

\[
 \delta_2=\sum_{i\in J}e_iS_i.
\tag{4.2}
\]

Then, uniformly in finite `J`,

\[
 \boxed{
 \left|\frac d{dt}\mathscr K_{x,J}(P_t,y_J)\right|
 \le C_{\rm dir}(c)(\delta_0+\delta_1+\delta_2),
 }
\tag{4.3}
\]

with

\[
 \boxed{
 C_{\rm dir}(c)=2^{26}A_c^{36}.
 }
\tag{4.4}
\]

### 4.1 Primitive derivative bounds

Differentiating the dictionary gives

\[
 |\dot q|\le\delta_0,
 \qquad
 |\dot v_i|\le A_ch_i,
 \qquad
 \|\dot Ge_i\|\le2A_ce_i,
 \qquad
 |\dot r_i|\le2A_ce_i.
\tag{4.5}
\]

Also

\[
 |\dot d_i|
 \le2A_c^3p_ih_i+2A_c^5p_i^2e_i.
\tag{4.6}
\]

For `i!=j`, use

\[
 u=\frac{G_{ij}v_j}{r_j},
 \qquad
 \rho=\frac{|G_{ij}|^2}{r_j},
\]

and the connected identity

\[
 \eta_{ij}
 =-\frac{2\Re(\overline v_i u)+|u|^2}{r_i-\rho}
  -\frac{|v_i|^2\rho}{r_i(r_i-\rho)}.
\tag{4.7}
\]

Differentiating (4.7), rather than separately differentiating two large
fractions, yields

\[
 |\dot\eta_{ij}|\le64A_c^{13}\Lambda_{ij},
\tag{4.8}
\]

where the following table is exhaustive.  An entry `(a,b,d;mark)` denotes
`p_i^a p_j^b g_ij^d` times the displayed marked derivative.

| source in (4.7) | exponent triples and marks |
|---|---|
| coefficient of `dot v_i` | `(0,1,1;h_i)`, `(1,0,2;h_i)` |
| `dot u` | `(1,1,0;gamma)`, `(1,0,1;h_j)`, `(1,1,1;e_j)`, `(0,2,1;gamma)`, `(0,1,2;h_j)`, `(0,2,2;e_j)` |
| coefficient of `dot r_i` | `(1,1,1;e_i)`, `(0,2,2;e_i)`, `(2,0,2;e_i)` |
| `dot rho` and denominator response | `(2,0,1;gamma)`, `(2,0,2;e_j)`, `(0,2,3;gamma)`, `(0,2,4;e_j)` |

This accounts for every derivative of `v_i`, `v_j`, `G_ij`, `r_i`, and
`r_j` in the exact two-flip formula.

### 4.2 Exact connected derivative operations

For `B=B_phi`, put

\[
 D=p_i^2+g_{ij}^2p_j^2,
\]

\[
 X=g_{ij}p_ip_j+g_{ij}^2(p_i^2+p_j^2),
\]

\[
 P_j=p_j^2.
\]

After constants and powers of `A_c` are separated, every exact derivative
term from (3.8) is bounded by one of the following eight exhaustive majorant
operations.  The list deliberately overcovers a few lower-order monomials; it
does not omit any derivative source:

| operation | normalized polynomial |
|---:|---|
| 1 | `g gamma D^2` |
| 2 | `g^2 D (dot d_i + dot eta)` |
| 3 | `g^2 D^2 (dot q + dot d_j + dot d_i + dot eta)` |
| 4 | `(e_i+e_j){D X + D^2(P_j+X)}` |
| 5 | `{D X + D^2(P_j+X)} dot q` |
| 6 | `{X+D(P_j+X)} dot d_i` |
| 7 | `D^2 dot d_j` |
| 8 | `D dot eta` |

To verify exhaustiveness, write

\[
 \Delta B=B(q+d_j,d_i+\eta)-B(q,d_i).
\]

The four exact gradient differences are

\[
\begin{aligned}
 |\dot{\Delta B}|\le{}&
 \{M_3DX+\tfrac12M_4D^2|d_j|\}|\dot q|\\
 &+\tfrac12M_3D^2|\dot d_j|\\
 &+\{M_2X+M_3D|d_j|\}|\dot d_i|\\
 &+M_2D|\dot\eta|.
\end{aligned}
\tag{4.9}
\]

Together with the derivative of `-|G_ij|^2 B(q+d_j,d_i+eta)` and the
derivative of `r_ir_j`, these are precisely rows 1--8.  There is no
unlisted derivative source.

Expanding rows 1--8 with (4.6), (4.8), `D`, `X`, and `P_j` gives the
following full coefficient ledger.

| operation | occurrence count | coefficient cap for each occurrence |
|---:|---:|---:|
| 1 | 4 | `2^8 A_c^20` |
| 2 | 34 | `2^11 A_c^26` |
| 3 | 80 | `2^13 A_c^35` |
| 4 | 44 | `2^8 A_c^29` |
| 5 | 22 | `2^11 A_c^31` |
| 6 | 22 | `2^8 A_c^27` |
| 7 | 8 | `2^6 A_c^27` |
| 8 | 30 | `2^9 A_c^26` |

Thus there are 244 marked-monomial occurrences and 147 distinct
exponent-mark quadruples.  Since `p_i,g_ij<=1`, all are dominated by the following 33
minimal families.

| mark | complete minimal exponent list `(a,b,d)` |
|---|---|
| `dot q` | `(0,4,4)`, `(1,3,3)`, `(2,2,2)`, `(3,1,1)`, `(4,0,2)`, `(4,2,0)` |
| `e_i` | `(0,4,4)`, `(1,3,3)`, `(2,2,2)`, `(3,1,1)`, `(4,0,2)`, `(4,2,0)` |
| `e_j` | `(0,4,4)`, `(1,3,3)`, `(2,2,2)`, `(3,1,1)`, `(4,0,2)`, `(4,2,0)` |
| `gamma_ij` | `(0,4,3)`, `(1,3,2)`, `(2,2,1)`, `(3,1,0)`, `(4,0,1)` |
| `h_i` | `(0,3,3)`, `(1,2,2)`, `(2,1,1)`, `(3,0,2)`, `(3,2,0)` |
| `h_j` | `(0,3,4)`, `(1,2,3)`, `(2,1,2)`, `(3,0,1)`, `(4,1,0)` |

This table is the promised complete coverage certificate for the connected
derivative.

### 4.3 Summing every marked family

The row and column inequalities are

\[
 \sum_jg_{ij}^2\le1,
 \qquad
 \sum_j\gamma_{ij}^2\le e_i^2,
 \qquad
 \sum_i h_i^2\le\delta_0^2,
\tag{4.10}
\]

\[
 \sum_iS_i
 =\sum_jp_j^2\sum_i g_{ij}^2
 \le\frac14.
\tag{4.11}
\]

The 33 rows sum as follows.

| marked family class | uniform sum bound |
|---|---:|
| six `dot q` families | `<=delta_0` |
| five `h_i` families | `<=delta_0` |
| five `h_j` families | `<=delta_0` |
| five `gamma_ij` families | `<=delta_1` |
| six `e_i` families | `<=delta_1+delta_2` |
| six `e_j` families | `<=delta_1+delta_2` |

For a fully checkable exponent-to-norm map, read each bound list in the same
order as the exponent list in the 33-family table:

| mark | individual bounds in table order |
|---|---|
| `dot q` | `(1/4, 5/32, 1/16, 1/8, 1/4, 1/16) delta_0` |
| `e_i` | `(delta_2, delta_1/4, delta_1/8, delta_1/4, delta_1/2, delta_1/8)` |
| `e_j` | `(delta_1/2, delta_1/4, delta_1/8, delta_1/4, delta_2, delta_1/8)` |
| `gamma_ij` | `(delta_1/2, delta_1/2, delta_1/4, delta_1/4, delta_1/2)` |
| `h_i` | `(1/4, 1/8, 1/4, 1/2, 1/8) delta_0` |
| `h_j` | `(1/2, 1/4, 1/8, 1/4, 1/8) delta_0` |

These follow only from (4.10)--(4.11), `sum p_i^2<=1/4`, and Cauchy--Schwarz.
For example, the potentially dangerous `e_j(3,1,1)` family is summed in the
`i` direction:

\[
 \sum_i p_i^3\sum_j g_{ij}p_je_j
 \le\delta_1\sum_i p_i^3
 \le\frac14\delta_1,
\]

so no unweighted `sum_j p_je_j` occurs.

There are no dimension factors.  The two families not
paid by `delta_1` alone are bounded by

\[
 \sum_{i,j}e_i g_{ij}^4p_j^4
 \le\sum_i e_iS_i=\delta_2,
\]

and its transposed counterpart.  Every other `e` row contains an explicit
`p_i` next to `e_i` after a row/column Cauchy--Schwarz step and is therefore
paid by `delta_1`.  The `gamma` rows use

\[
 \sum_j\gamma_{ij}p_j\le\frac12e_i,
 \qquad
 \sum_j\gamma_{ij}g_{ij}\le e_i,
\]

and the `h` rows use `||h||_2<=delta_0`.  Substitution of each exponent in
the displayed 33-family table gives exactly the six aggregate bounds above.

The row-by-row ledger in the preceding table is in particular bounded by
`2^16 A_c^35` per occurrence.  The worst power `A_c^35` occurs in row 3,
from

\[
 |G_{ij}|^2 M_3D^2|\dot\eta_{ij}|.
\]

Hence all off-diagonal connected derivatives are below

\[
 244\,2^{16}A_c^{35}
 (\delta_0+\delta_1+\delta_2)
 <2^{24}A_c^{35}
 (\delta_0+\delta_1+\delta_2).
\tag{4.12}
\]

The remaining groups are differentiated directly.  Their complete ledger is

| differentiated group | bound |
|---|---:|
| `phi''(q)` | `A_c^6 delta_0` |
| `sum r_i B_{phi'}` | `4A_c^15(delta_0+delta_1)` |
| `sum R_i B_phi` | `4A_c^14(delta_0+delta_1)` |
| `A^i,A` group | `20A_c^14(delta_0+delta_1)` |
| diagonal `C_ii` | `32A_c^16(delta_0+delta_1)` |

For the fourth row one uses

\[
 |\dot A|\le2A_c^2\delta_0,
\]

\[
 |\dot A^i|
 \le2A_c^2\delta_0+2A_c^4h_i+8A_c^6p_ie_i.
\]

Combining this table with (4.12) is strictly below the rounded constant in
(4.4), proving Theorem 4.1.

---

# 5. Outside diagonal tilts and closure of the repaired energy

Let

\[
 P_t=\operatorname{proj}(e^{tH}\operatorname{Ran}P_0),
\]

where `H` is real diagonal, supported on `O`, and `||H||<=h`.  The exact
projection derivative is

\[
 \dot P=(I-P)HP+PH(I-P).
\tag{5.1}
\]

For every `i in I`,

\[
 e_i=\|\dot Pe_i\|\le h\sqrt{T_i}.
\tag{5.2}
\]

Consequently

\[
 \delta_0\le h\sqrt{T_0},
 \qquad
 \delta_1\le h\sqrt{W_0}.
\]

By (4.11),

\[
 \delta_2
 \le h\sum_i\sqrt{T_i}S_i
 \le\frac h2\sqrt{Z_0}.
\]

The repaired directional estimate is therefore

\[
 \boxed{
 \left|\frac d{dt}\mathscr K_{x,J}(P_t,y_J)\right|
 \le C_{\rm dir}(c)h
 \{\sqrt{T_0}+\sqrt{W_0}+\tfrac12\sqrt{Z_0}\}.
 }
\tag{5.3}
\]

This holds for every intermediate orthogonal projection, whether or not that
intermediate projection is itself the posterior of a binary word.

## 5.1 Gronwall bound for `Z_0`

Let

\[
 C=P_{O,J},\quad M=P_{J,J},\quad z=P_{J,0},
\]

and let

\[
 D_T=\operatorname{diag}(T_i),
 \qquad D_p=\operatorname{diag}(p_i).
\]

Then

\[
 Z_0=\operatorname{Tr}(D_TM D_p^2M^*).
\tag{5.4}
\]

Under (5.1),

\[
 \dot M=-2C^*HC,
 \qquad
 \dot z=-2C^*Hc_0,
 \quad c_0=P_{O,0}.
\tag{5.5}
\]

The derivative of `D_T` contributes at most `2hZ_0`.  The two `M`
derivatives contribute at most

\[
 2h\sqrt{W_0Z_0}.
\]

Indeed, `||CD_p||_{HS}^2=W_0`, while

\[
 \|CD_TM D_p\|_{HS}^2\le\frac14Z_0.
\]

The `D_p^2` derivative contributes at most

\[
 2h\sqrt{T_0Z_0};
\]

here `||dot z||<=2h sqrt(T_0)` and each diagonal entry of
`M^*D_TM` is at most `1/4`.  Therefore

\[
 |Z_0'|
 \le2hZ_0+2h\sqrt{W_0Z_0}+2h\sqrt{T_0Z_0}
 \le h(T_0+W_0+4Z_0).
\tag{5.6}
\]

Together with

\[
 |T_0'|\le2hT_0,
 \qquad
 |W_0'|\le hT_0+3hW_0,
\]

this gives

\[
 \boxed{
 \widetilde U_0(P_t;I)
 \le e^{4ht}\widetilde U_0(P_0;I).
 }
\tag{5.7}
\]

---

# 6. Adding or removing the anchor observation

Scale only coordinate `0`, with logarithmic speed `eta`.  For `i,j in J` and
`k in O`,

\[
 \dot P_{k0}=\eta(1-2P_{00})P_{k0},
\]

\[
 \dot P_{ki}=-2\eta P_{k0}P_{0i},
\]

\[
 \dot P_{ij}=-2\eta P_{i0}P_{0j}.
\]

These identities give

\[
 |T_0'|\le2|\eta|T_0,
\]

\[
 |W_0'|\le|\eta|(T_0+3W_0).
\tag{6.1}
\]

For `Z_0`, differentiating `T_i` and `S_i` yields

\[
 |T_i'|\le4|\eta|p_i\sqrt{T_iT_0},
\]

\[
 |S_i'|\le2|\eta|p_i\sqrt{S_i}+2|\eta|S_i.
\]

Using

\[
 \sum_i p_i^2S_i\le\frac1{16}
\]

and Cauchy--Schwarz gives

\[
 |Z_0'|
 \le |\eta|\left(\frac12T_0+W_0+\frac72Z_0\right).
\tag{6.2}
\]

Equations (6.1)--(6.2) imply

\[
 |\widetilde U_0'|\le4|\eta|\widetilde U_0.
\]

If `P^-` is the posterior before observing the anchor and `P^+` is the
posterior after observing it, the scale length is at most `log s_x`, where

\[
 s_x=\sqrt{\frac{1+x}{1-x}}.
\]

Hence

\[
 \boxed{
 \widetilde U_0(P^-;I)
 \le s_x^4\widetilde U_0(P^+;I).
 }
\tag{6.3}
\]

---

# 7. Actual-law random-anchor averaging

Let `I` be a length-`N` interval.  Condition on all actual channel outputs in
`I`, and let `P^+` be the resulting latent posterior projection.  For each
choice of anchor `a in I`, define `T_a,W_a,Z_a` relative to the same exterior
`O=Z\I`.

Projection algebra gives

\[
 \sum_{a\in I}T_a
 \le\sum_{i\in I}T_i,
\]

\[
 \sum_{a\in I}W_a
 \le\sum_{i\in I}T_i.
\]

For the new term,

\[
\begin{aligned}
 \sum_{a\in I}Z_a
 &\le\sum_{a,i,j\in I}
 T_i|P_{ij}|^2|P_{ja}|^2\\
 &\le\sum_{i,j\in I}T_i|P_{ij}|^2P_{jj}\\
 &\le\sum_{i\in I}T_i.
\end{aligned}
\tag{7.1}
\]

For a projection DPP,

\[
 \sum_{i\in I}T_i
 =\operatorname{Var}(N_I\mid Y_I).
\tag{7.2}
\]

Taking the actual conditional law and then using total variance,

\[
 \mathbb E\sum_{i\in I}T_i
 \le\operatorname{Var}_Q(N_I)=V_Q(N).
\tag{7.3}
\]

After removing the anchor observation and using (6.3),

\[
 \boxed{
 \frac1N\sum_{a\in I}
 \mathbb E\widetilde U_a(P_a^-;I)
 \le3s_x^4\frac{V_Q(N)}N.
 }
\tag{7.4}
\]

Thus the repair has an actual-law cost of exactly one additional copy of the
same conditional count-variance budget.  It is not an unknown residual.

---

# 8. Repaired finite-observation theorem

Let `Gamma_N^av(c)` be the exact random-anchor, actual-sine finite-observation
curvature defined in cycle 04, and let `Gamma(c)` denote the frozen infinite
half-filled balanced local curvature functional.  Set

\[
 s_c=\sqrt{\frac{1+c}{1-c}}.
\]

## Theorem 8.1 — repaired observation localization

Subject to the frozen V14 identification of the finite and infinite curvature
functionals,

\[
 \boxed{
 |\Gamma(c)-\Gamma_N^{\rm av}(c)|
 \le E_{\rm C05}(c,N),
 }
\tag{8.1}
\]

where

\[
\boxed{
\begin{aligned}
 E_{\rm C05}(c,N)={}&
 \frac32C_{\rm tail}(c)s_c^8\frac{V_Q(N)}N\\
 &+\frac34C_{\rm dir}(c)
   (s_c^2-1)s_c^2
   \sqrt{\frac{V_Q(N)}N}.
\end{aligned}
}
\tag{8.2}
\]

### Proof

For each anchor, start at the posterior `P^-` based on the finite observed
word and reveal every output in `O` through the diagonal path.  Its generator
has norm

\[
 h=\log s_x.
\]

By (5.7),

\[
 \widetilde U(t)\le s_x^{4t}\widetilde U(0).
\]

Integrating (5.3) gives

\[
 |\mathscr K_{x,J}(P_1)-\mathscr K_{x,J}(P_0)|
 \le\frac{\sqrt3}{2}C_{\rm dir}(c)
 (s_x^2-1)\sqrt{\widetilde U(0)}.
\tag{8.3}
\]

At the full posterior, Theorem 3.1 and (5.7) give

\[
 |\mathscr K_{x,\infty}(P_1)-\mathscr K_{x,J}(P_1)|
 \le C_{\rm tail}(c)s_x^4\widetilde U(0).
\tag{8.4}
\]

Average (8.3)--(8.4) with the actual word probabilities, average the anchor,
apply (7.4), and use Jensen for the square root.  This yields

\[
\begin{aligned}
 \left|F_{x,\infty}''
 -\frac1N\sum_aF_{x,N,a}''\right|
 \le{}&3C_{\rm tail}(c)s_x^8\frac{V_Q(N)}N\\
 &+\frac32C_{\rm dir}(c)(s_x^2-1)s_x^2
 \sqrt{\frac{V_Q(N)}N}.
\end{aligned}
\tag{8.5}
\]

Set `x=cu`, dominate the constants by their values at `c`, and integrate with
`int_0^1 u du=1/2`.  This proves (8.1)--(8.2).

For the half-filled sine projection,

\[
 V_Q(N)\le\frac{\log N+4}{\pi^2}.
\]

Therefore

\[
 E_{\rm C05}(c,N)
 =O_c\!\left(\sqrt{\frac{\log N}{N}}\right).
\tag{8.6}
\]

The rate is the same as claimed in cycle 04, but it now rests on a valid
complete-jet lemma.  The cycle-04 theorem with only `T_0+W_0` is not valid as
written.

The constants

\[
 C_{\rm tail}(c)=2^{12}\left(\frac2{1-c}\right)^{25},
\]

\[
 C_{\rm dir}(c)=2^{26}\left(\frac2{1-c}\right)^{36}
\]

are fully accounted existence constants.  They are much too large near
`c=19/20` to supply a realistic sign test.  No positivity certificate for
`Gamma(19/20)` is claimed.

---

# 9. Exact scope and dependency ledger

## Proved in this manuscript

1. The old `T_0+W_0` complete-kernel tail estimate, uniformly in finite
   volume, with absolute convergence and an exhaustion-independent infinite
   kernel.
2. An exact legal posterior-projection counterexample to the old directional
   estimate.
3. Identification of the missing marked connected monomial.
4. A closed weighted term algebra covering every connected derivative source:
   244 occurrences, 147 distinct marked monomials, 33 minimal summability
   families.
5. The repaired finite derivative theorem with the explicit energy `Z_0`.
6. Closed Gronwall bounds for `T_0+W_0+Z_0` under outside and anchor diagonal
   tilts.
7. Actual-law random-anchor averaging of `Z_0` by conditional count variance.
8. The repaired `O_c(sqrt(log N/N))` finite-observation theorem, conditional
   only on the frozen V14/local-functional identification.

## Not proved here

1. No practical finite radius or interval-certified sign at `c=19/20`.
2. No extension from half filling to every `0<rho<1`.
3. No extension from the balanced point to every legal `a`.
4. No proof of limiting differentiability of the true Shannon entropy rate.
5. No identification of `Tr b(K)` with the classical configuration entropy.
6. No proof of the ultimate full-configuration all-parameter entropy-rate
   concavity target.

The finite Toeplitz compression is not treated as a projection anywhere in
this proof.  Projection structure is used only for the latent posterior of an
underlying projection DPP and its diagonal-likelihood orbit.

---

# 10. Computational companion

`S41_CYCLE05_checks.py` performs exact symbolic checks, not random
certification:

1. verifies `U^*U=I`, constructs the exact Halmos projection, and checks
   `P^2=P`;
2. computes `T_0=W_0=0`, `Z_0=9/4096`;
3. constructs the complete V14 kernel and proves symbolically the formula
   (2.5);
4. proves `dK/dlambda=32/1197`, the unit-generator derivative
   `-16/1197`, and the legal reveal derivative `-8 log(3)/1197`;
5. generates the eight connected derivative operations, all 244 monomial
   occurrences, all 147 distinct terms, and exactly the 33 minimal families
   displayed in Section 4.

The script is a bookkeeping and exact-algebra companion to the analytic
proof; the infinite and actual-law estimates are proved above rather than
inferred from tests.
