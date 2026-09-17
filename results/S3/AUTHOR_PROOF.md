# S3 check3 — audited bridge and a growing-family obstruction to an atomwise leaf payment

## 0. Status and notation

The requested high-contrast sine entropy-rate concavity theorem is **not proved**. The remaining unpaid term is displayed in Section 4.

All logarithms are natural. For a Hermitian contraction `0<=Q<=I` on `s` labelled coordinates, let

\[
F_Q(a,c)=H\bigl(\operatorname{DPP}(aI_s+cQ)\bigr),
\qquad 0\le a\le1-c,
\]

where `H` is the Shannon entropy of the complete `2^s`-atom law. Equivalently, if `X~DPP(Q)` and, independently by coordinate conditional on `X`,

\[
\Pr(Y_i=1\mid X_i)=a+cX_i,
\]

then `Y~DPP(aI+cQ)`. Indeed, for every coordinate set `A`,

\[
\Pr(A\subseteq Y)
 =\sum_{B\subseteq A}a^{|A|-|B|}c^{|B|}\det Q_B
 =\det(aI_A+cQ_A),
\]

and inclusion probabilities determine all complete atoms by inclusion-exclusion.

The previous round's archive is preserved under `inherited/`. Sections 1--3 below independently expose and check the response step needed to use that bridge. Sections 5--7 are new in this round.

---

## 1. The exact ordered latent-block decomposition

Let `X~DPP(Q)` on `[n]`, where `Q` may be a projection or any Hermitian contraction. Let

\[
\mathcal B=(B_1,\ldots,B_k)
\]

be a deterministic ordered partition, and put

\[
U_j=B_1\cup\cdots\cup B_{j-1},\qquad
R_j=B_j\cup\cdots\cup B_k.
\]

For a positive-probability latent prefix word `u=X_{U_j}`, let `Q^u` be the exact conditional DPP kernel on `R_j`, and let

\[
Q_j^u=(Q^u)_{B_j,B_j}.
\]

All prefix weights `Pr(X_{U_j}=u)` are independent of `a`. Define

\[
G_{Q,\mathcal B}(a,c)
 =\sum_{j=1}^k\mathbb E_u F_{Q_j^u}(a,c),
\tag{1.1}
\]

and

\[
E_{Q,\mathcal B}(a,c)
 =\sum_{j=1}^k\mathbb E_u
 I(X_{B_j};Y_{R_j\setminus B_j}\mid Y_{B_j},X_{U_j}=u).
\tag{1.2}
\]

### Proposition 1.1 — exact decomposition and legal direction

For every finite contraction `Q`, every ordered partition, and every legal `a,c`,

\[
\boxed{F_Q=G_{Q,\mathcal B}+E_{Q,\mathcal B}.}
\tag{1.3}
\]

Every summand in `G` moves in the legal common-shift direction

\[
aI_{B_j}+cQ_j^u,
\]

and every averaging weight is independent of `a`.

#### Proof

At one node, abbreviate `B=B_j`, `C=R_j\setminus B`, and condition on the fixed latent prefix `u`. Given `X_B`, the channel outputs `Y_B` and `Y_C` are independent. Therefore

\[
\begin{aligned}
H(Y_B,Y_C\mid u)
&=H(Y_B\mid u)+H(Y_C\mid Y_B,u)\\
&=H(Y_B\mid u)+H(Y_C\mid X_B,u)
  +I(X_B;Y_C\mid Y_B,u).
\end{aligned}
\tag{1.4}
\]

The first term is `F_{Q_j^u}`. The second is the actual latent-word average of the child remaining-block entropies after revealing all of `X_B`. Multiplying by `Pr(u)` and summing over all nodes makes every nonroot remaining-block entropy occur once positively at its own node and once negatively in its parent's child average, with the same global latent probability. All such terms cancel; the empty leaf entropy is zero. The uncancelled terms are exactly (1.1) and (1.2). No output conditioning is used to define a local kernel. ∎

For interior `a`, every atom is positive and the exact complete-law Hessian is

\[
F_Q''(a,c)
=-\sum_y p_y''\log p_y-\sum_y\frac{(p_y')^2}{p_y}.
\tag{1.5}
\]

Both acceleration and Fisher terms are therefore retained in every leaf summand and in the aggregate debt.

---

## 2. Independent value payment for the outside-block debt

The following is the value estimate to which the response lemma is applied.

### Proposition 2.1 — boundary-information budget

Let `b(x)=-x\log x-(1-x)\log(1-x)`. Then

\[
0\le E_{Q,\mathcal B}(a,c)
\le \mathfrak B(Q,\mathcal B)
:=\sum_j\operatorname{Tr}b(Q_{B_j}),
\tag{2.1}
\]

uniformly in `a,c`.

#### Proof

At a conditional node, data processing gives

\[
I(X_B;Y_C\mid Y_B)
=I(X_B;Y_C)-I(Y_B;Y_C)
\le I(X_B;X_C).
\tag{2.2}
\]

For a projection DPP, the exterior-power pure state has the complete DPP configuration law as its coordinate-basis measurement. Across the split `B|C`, its Schmidt eigenvalues are products of the eigenvalues of `P_B`; hence its reduced-state entropy is `Tr b(P_B)`. Measurement cannot increase relative entropy, so

\[
I(X_B;X_C)\le\operatorname{Tr}b(P_B).
\tag{2.3}
\]

For a contraction, use the canonical projection dilation

\[
\widetilde P=
\begin{pmatrix}
Q&\sqrt{Q(I-Q)}\\
\sqrt{Q(I-Q)}&I-Q
\end{pmatrix}.
\]

Its marginal on the original coordinates is exactly `DPP(Q)` because all inclusion probabilities agree. Adding the auxiliary measured coordinates can only increase mutual information, and `(\widetilde P)_B=Q_B`; therefore (2.3) remains valid with `Q`.

The exact one-coordinate conditional kernels satisfy

\[
(1-q)Q^{(0)}+qQ^{(1)}=A,
\tag{2.4}
\]

where `A` is the unconditioned remaining principal block. Iteration yields the matrix martingale

\[
\mathbb E_u Q_j^u=Q_{B_j}.
\tag{2.5}
\]

Since `A\mapsto Tr b(A)` is concave on Hermitian contractions,

\[
\mathbb E_u\operatorname{Tr}b(Q_j^u)
\le\operatorname{Tr}b(Q_{B_j}).
\tag{2.6}
\]

Average (2.2)--(2.3) at each node and sum. ∎

This is a full-law information bound. No particle-count entropy or trace surrogate is substituted for a configuration entropy.

---

## 3. Audited degree-cancellation response lemma

This section records the exact hypotheses and constants needed to convert the aggregate value budget (2.1) into an interior curvature budget. It is included because this bridge was provisional in the preceding response.

Fix `0<c<1` and `0<eta<(1-c)/2`. Put

\[
d=1-c,\quad \delta=\eta/2,\quad
I=[\delta,d-\delta],\quad I'=[\eta,d-\eta],
\]

\[
\ell=d-\eta,
\quad
\sigma={2\sqrt{(\eta/2)(d-3\eta/2)}\over d-\eta},
\quad
r={1-\delta\over1+\delta}.
\tag{3.1}
\]

### Lemma 3.1 — full-moving-law polynomial response

Let `Q` range over any collection of finite Hermitian contractions. Let

\[
g(a)={1\over n}\left(F_{Q_*}(a,c)-
 \sum_\alpha w_\alpha F_{Q_\alpha}(a,c)\right),
\tag{3.2}
\]

where `w_alpha>=0` are independent of `a`, and the weighted dimensions satisfy

\[
\sum_\alpha w_\alpha\dim Q_\alpha=n=\dim Q_*.
\tag{3.3}
\]

Assume

\[
\|g\|_{C(I)}\le\epsilon\le\log2.
\tag{3.4}
\]

For every integer `M>=1`,

\[
\sup_{a\in I'}|g''(a)|
\le B_M(\epsilon+2V_M)+2A_1S_{2,M}+2A_2S_{1,M},
\tag{3.5}
\]

where

\[
A_1={64\over\ell^2\sigma^2},\qquad
A_2={32\over\ell^2\sigma^3},\qquad
B_M=A_1M^3+A_2M^2,
\]

\[
V_M={r^{M+1}\over(M+1)(1-r)},
\]

\[
S_{1,M}=r^{M+1}\left({M+1\over1-r}+{r\over(1-r)^2}\right),
\]

\[
S_{2,M}=r^{M+1}\left({(M+1)^2\over1-r}
+{2(M+1)r\over(1-r)^2}
+{r(1+r)\over(1-r)^3}\right).
\tag{3.6}
\]

Choosing

\[
M=\max\left\{1,\left\lceil{2\log(1/\epsilon)\over-\log r}\right\rceil\right\}
\tag{3.7}
\]

gives

\[
\sup_{I'}|g''|
\le C_{c,\eta}\epsilon[1+\log(1/\epsilon)]^3,
\tag{3.8}
\]

with a constant independent of all dimensions, numbers of latent words, and conditioning probabilities.

#### Proof

For an occupied set `S` on `s` coordinates, put

\[
A_S(a)=aI+cQ-D_{S^c}.
\]

On `I`, the eigenvalues of `aI+cQ` lie in `[delta,1-delta]`. Since

\[
A_S=(aI+cQ-\tfrac12I)+(\tfrac12I-D_{S^c}),
\]

and the second summand has every singular value `1/2` while the first has norm at most `1/2-delta`,

\[
\delta\le s_{\min}(A_S)\le s_{\max}(A_S)\le1-\delta.
\tag{3.9}
\]

The full atom is `p_a(S)=|det A_S(a)|`, and hence

\[
{F_Q(a,c)\over s}
=-{1\over2s}\mathbb E_{p_a}\operatorname{Tr}\log A_S(a)^2.
\tag{3.10}
\]

For `delta^2<=u<=1`, the uniformly absolutely convergent Chebyshev expansion is

\[
-\tfrac12\log u=C_\delta+
\sum_{h\ge1}{(-1)^hr^h\over h}
T_h\left({2u-(1+\delta^2)\over1-\delta^2}\right),
\quad C_\delta=\log{2\over1+\delta}.
\tag{3.11}
\]

At order `h`, the normalized trace in (3.11) is a polynomial of total degree at most `2h` in `(a,1_S)`. After reducing Boolean powers, a monomial is `a^r prod_{i in V}1_{i in S}` with `r+|V|<=2h`. Under the **moving complete DPP law**,

\[
\mathbb E\prod_{i\in V}1_{i\in S}=\det(aI+cQ)_V,
\]

which has degree at most `|V|` in `a`. Thus the expected order-`h` coefficient is a polynomial of degree at most `2h`; the movement of every atom weight is included. Spectral boundedness in (3.9)--(3.11) gives its sup norm at most `r^h/h`.

By the dimension identity (3.3), the constant `C_delta` cancels exactly in (3.2). Therefore

\[
g=\sum_{h\ge1}v_h,
\qquad \deg v_h\le2h,
\qquad \|v_h\|_{C(I)}\le{2r^h\over h}.
\tag{3.12}
\]

There is no factor equal to the number of nodes: all latent weights have already been summed, and their weighted local dimensions total `n`.

For a polynomial `P` of degree `D` on `I`, use

\[
a=a_{mid}+{\ell\over2}\cos\theta.
\]

On `I'`, `|sin theta|>=sigma`. Cosine orthogonality bounds every positive Chebyshev coefficient by `2||P||`. Differentiating `T_h(cos theta)=cos(h theta)` twice and summing the coefficient bounds gives

\[
\|P''\|_{C(I')}
\le {8\over\ell^2}
\left({D^3\over\sigma^2}+{D^2\over\sigma^3}\right)
\|P\|_{C(I)}.
\tag{3.13}
\]

The truncation through `M` has degree `2M` and norm at most `epsilon+2V_M`. Apply (3.13) to it. Apply (3.13) separately to each tail term in (3.12), and sum the exact geometric tails `sum_{h>M}h r^h=S_{1,M}` and `sum_{h>M}h^2r^h=S_{2,M}`. This proves (3.5). The same summable majorants justify termwise differentiation. Formula (3.8) follows from (3.7) and the displayed geometric sums. ∎

### Audit conclusion

Propositions 1.1, 2.1, and Lemma 3.1 verify the inherited bridge on its stated fixed-interior domain. In particular, if

\[
\epsilon_{n,m}={\mathfrak B(Q_n,\mathcal B_m)\over n}=o(1),
\]

then

\[
\sup_{a\in I'}|F_{Q_n}''-G_{Q_n,\mathcal B_m}''|
\le nC_{c,\eta}\epsilon_{n,m}
 [1+\log(1/\epsilon_{n,m})]^3.
\tag{3.14}
\]

For the sine Toeplitz compression and `m=floor(sqrt n)`, the inherited trace-defect calculation gives the stated `o(n)` bound. This audit does **not** give a sign for `G''`.

---

## 4. The precise unpaid conditioned leaf-volume inequality

For the true sine block

\[
Q_n=T_n(1_{E_\rho}),
\]

use consecutive blocks of size `m=floor(sqrt n)` and the exact latent conditional kernels from Section 1. The unresolved quantity is

\[
\boxed{
G_{n,m}''(a,c)
=\sum_j\mathbb E_{u}
F_{(Q_n^u)_{B_j}}''(a,c).
}
\tag{4.1}
\]

The necessary new volume estimate is, for fixed positive density, fixed high contrast, and a fixed nonshrinking interior interval,

\[
\boxed{
\sup_{a\in I'}G_{n,m}''(a,c)\le o(n)
}
\tag{4.2}
\]

or an integrated finite-Jensen version with the same scale. The weights in (4.1) are the actual latent prefix probabilities and are independent of `a`; the kernels are not assumed Fourier, constant-diagonal, or projection kernels.

This round did not prove (4.2). Direct enumeration found no positive example for small genuine Fourier roots, but that is diagnostic only; see `attempts.md`.

---

## 5. New exact scalar paid-odds lemma

The following local inequality is useful because it retains the complete two-bit odds acceleration and pays it by a covariance-weighted, one-site expression. It is not by itself a compatible global allocation.

### Lemma 5.1 — negative-covariance output odds payment

Let `(X_1,X_2)` be any binary pair with

\[
\Pr(X_1=1)=x,\qquad \Pr(X_2=1)=y,
\qquad \operatorname{Cov}(X_1,X_2)=-d\le0.
\]

Pass both bits independently through the symmetric binary channel

\[
\Pr(Y_i=1\mid X_i=0)=\varepsilon,
\qquad
\Pr(Y_i=1\mid X_i=1)=1-\varepsilon,
\]

where `0<epsilon<1/2`, `c=1-2epsilon`, and `tau=epsilon(1-epsilon)`. Put

\[
q=\varepsilon+cx,\qquad r=\varepsilon+cy,
\qquad z=c^2d.
\]

If the output table in the order `00,01,10,11` is `(A,B,C,D)`, then

\[
A=(1-q)(1-r)-z,\quad B=(1-q)r+z,
\]

\[
C=q(1-r)+z,\quad D=qr-z.
\]

Its negative log-odds satisfies

\[
\boxed{
\log{BC\over AD}
\le {z\over2\tau}
\left({1\over q(1-q)}+{1\over r(1-r)}\right).
}
\tag{5.1}
\]

Since

\[
q(1-q)=\tau+c^2x(1-x),\qquad
r(1-r)=\tau+c^2y(1-y),
\]

(5.1) also implies the weaker latent-margin bound obtained by replacing `q(1-q),r(1-r)` by `x(1-x),y(1-y)` whenever those margins are nondegenerate.

#### Proof

Keep `q,r` fixed and interpolate the covariance magnitude from `0` to `z`:

\[
A_t=(1-q)(1-r)-t,\quad B_t=(1-q)r+t,
\]

\[
C_t=q(1-r)+t,\quad D_t=qr-t.
\]

Every `0<=t<=z` is feasible because it corresponds to the convex interpolation between the independent input table with margins `x,y` and the given input table. Define

\[
h(t)=\log{B_tC_t\over A_tD_t}.
\]

Then

\[
h'(t)=A_t^{-1}+B_t^{-1}+C_t^{-1}+D_t^{-1}.
\tag{5.2}
\]

Now `A_t+B_t=1-q`. Conditional on `Y_1=0`, the bit `Y_2` is still obtained by passing some posterior Bernoulli input through the same symmetric channel, so

\[
{B_t\over A_t+B_t}\in[\varepsilon,1-\varepsilon].
\]

Therefore

\[
A_tB_t\ge\tau(1-q)^2,
\qquad
A_t^{-1}+B_t^{-1}
={1-q\over A_tB_t}\le{1\over\tau(1-q)}.
\]

The same argument conditional on `Y_1=1` gives

\[
C_t^{-1}+D_t^{-1}\le{1\over\tau q}.
\]

Thus

\[
h'(t)\le{1\over\tau q(1-q)}.
\tag{5.3}
\]

Interchanging the two coordinates also gives

\[
h'(t)\le{1\over\tau r(1-r)}.
\tag{5.4}
\]

Average (5.3)--(5.4), integrate from `0` to `z`, and use `h(0)=0`. ∎

The obstruction in Section 6 shows why a pointwise sum of such pair payments cannot simply be identified with one total diagonal Fisher budget.

---

## 6. New exact growing-family obstruction to an atomwise total payment

This section tests a concrete center allocation that is stronger than the required averaged leaf sign. Its failure is therefore an exclusion, not a counterexample to the target.

At the channel center put

\[
a={1-c\over2},\qquad \tau=a(1-a).
\]

Let `P` be a projection, `K=aI+cP`, and fix an output atom `y`. Put

\[
M_y=K-D_{1-y},\qquad R=M_y^{-1},\qquad s_i=2y_i-1,
\]

\[
r_i=s_iR_{ii},\qquad g_i=r_i-1,
\qquad f_i={r_i^2\over g_i}.
\tag{6.1}
\]

For `i!=j`, put

\[
w_{ij}=R_{ij}^2,
\quad \epsilon_{ij}=s_is_j,
\quad x_{ij}={w_{ij}\over g_ig_j},
\quad N_{ij}=r_ir_j-\epsilon_{ij}w_{ij}.
\]

Define

\[
o_{ij}=\begin{cases}
1-x_{ij},&\epsilon_{ij}=1,\\
(1+x_{ij})^{-1},&\epsilon_{ij}=-1,
\end{cases}
\]

\[
m_{ij}=\begin{cases}
(1+g_ig_j-w_{ij})/N_{ij},&\epsilon_{ij}=1,\\
(g_i+g_j)/N_{ij},&\epsilon_{ij}=-1,
\end{cases}
\]

and the complete pair debt at this atom

\[
h_{ij}=-\log o_{ij}-(1-o_{ij})
-m_{ij}{(1-o_{ij})^2\over o_{ij}}.
\tag{6.2}
\]

These quantities come from the exact center Hessian, not from a covariance-only surrogate. For a projection,

\[
K^2-K+\tau I=0.
\]

Writing `S=diag(s_i)` and `M=K-D_{1-y}`, inversion gives

\[
{g_i\over\tau}-r_i^2=\sum_{j\ne i}R_{ij}^2\ge0.
\tag{6.3}
\]

Conditioning the complete law on all coordinates except `i,j`, direct differentiation of its four atoms gives the acceleration `-log o_{ij}` and the cross-Fisher correction represented by the other two terms in (6.2). Rao--Blackwellizing each one-coordinate squared score gives the diagonal term `f_i`. Consequently the full common-direction curvature is exactly

\[
F_P''(a,c)
=-\mathbb E\sum_i f_i
 +2\sum_{i<j}\mathbb E h_{ij}.
\tag{6.4}
\]

The proposed once-only atomwise total rule was

\[
2\sum_{i<j}h_{ij}\le\sum_i f_i.
\tag{6.5}
\]

Unlike a pair-by-pair allocation, (6.5) already allows arbitrary transfers among pairs while using the total diagonal payment only once.

### Proposition 6.1 — exact rational counterexample and linear direct-sum growth

Let

\[
T=\begin{pmatrix}
7/27&-1/14&10/49\\
13/48&-3/22&13/50\\
5/36&-3/32&3/41
\end{pmatrix},
\]

\[
V=\binom{T}{I_3},\qquad
P=V(I_3+T^TT)^{-1}V^T.
\tag{6.6}
\]

Then `P` is an exact rational rank-three projection on six coordinates. At

\[
c={99\over100},\qquad a={1\over200},
\qquad y=111000,
\]

the defect in (6.5) satisfies

\[
\boxed{
2\sum_{i<j}h_{ij}-\sum_i f_i>{6\over5}.
}
\tag{6.7}
\]

For every integer `k>=1`, the block diagonal projection

\[
P^{(k)}=\operatorname{diag}(P,\ldots,P)
\]

on `6k` coordinates, at the repeated atom `y^{(k)}=(111000)^k`, has defect greater than `6k/5`.

#### Proof

Equation (6.6) gives

\[
P^2=V(I+T^TT)^{-1}(I+T^TT)(I+T^TT)^{-1}V^T=P,
\]

and `rank P=3`. All entries are rational. The exact certificate constructs `M_y`, its rational inverse, and every quantity in (6.1)--(6.2). Multiplying all odds together reduces the defect to

\[
\Delta=-2\log R_0+Q_0,
\tag{6.8}
\]

where `R_0` and `Q_0` are the exact rationals stored in
`evidence/exact_growing_pointwise_obstruction.json`. No floating matrix operation enters this reduction.

To enclose the only logarithm, apply exact power-of-two range reduction to `R_0^{-1}`:

\[
R_0^{-1}=2^k m,\qquad 1\le m<2.
\]

For a rational `z=(m-1)/(m+1)`, use

\[
\log m=2\sum_{j=0}^{N}{z^{2j+1}\over2j+1}+\mathcal R_N,
\]

\[
0<\mathcal R_N
<{2z^{2N+3}\over(2N+3)(1-z^2)}.
\tag{6.9}
\]

The identical series with `z=1/3` encloses `log 2`. With `N=30`, exact rational comparison yields

\[
1.2248629717184887
<\Delta<
1.2248629717184890,
\]

and in particular `Delta>6/5`. The atom probability is also exactly positive; its decimal value is approximately `1.19088736e-6`.

A second exact rational-log enclosure, now summing all 64 complete atoms with their actual probabilities and retaining both `p'' log p` and Fisher terms, gives

\[
F_P''(1/200,99/100)<-1000.
\tag{6.10}
\]

Thus the example is rigorously not a counterexample to projection concavity at this parameter.

For the direct sum, `M_{y^{(k)}}` and its inverse are block diagonal. Cross-copy inverse entries vanish. Every within-copy `r_i,g_i,f_i,o_{ij},m_{ij},h_{ij}` is unchanged. Therefore the defect is exactly `k Delta`, proving the final claim. ∎

### Scope of Proposition 6.1

The proposition is a rigorous growing-family obstruction to the **pointwise** total allocation (6.5). It is not:

- a counterexample to the expected version after weighting all atoms;
- a counterexample to projection entropy concavity;
- a counterexample to the sign of (4.1);
- a counterexample to S-sine entropy-rate concavity.

The bad repeated atom has exponentially small probability in the direct sum, so no expected extensive obstruction is inferred from the pointwise estimate (6.7).

---

## 7. Consequences and nonconsequences for the leaf problem

The audited bridge proves that the outside-block debt costs only `o(n)` curvature on fixed interior intervals for the true sine blocks. Proposition 6.1 shows that one natural attempt to sign the remaining leaf volume cannot work atom by atom, even after pooling all pairs before spending the diagonal Fisher budget.

A successful proof of (4.2) must therefore exploit at least one of the following structures that (6.5) discards:

1. averaging over the complete output law;
2. signed cancellation between output atoms or count layers;
3. the distribution of the actual latent-conditioned kernels;
4. a multiscale transfer rather than a pointwise pair payment.

No such averaged negative volume budget is proved here.

---

## 8. Boundary and quantifier audit

1. **Interior response.** Lemma 3.1 is uniform on every fixed `I'=[eta,1-c-eta]`; its constant depends on `c,eta` but not on dimension, density, latent-word probabilities, or number of nodes.
2. **Complete laws.** Every entropy and derivative uses the complete atom law. Spectral entropy is used only to bound a proved mutual-information debt.
3. **Weights.** All weights in `G` are latent-input probabilities independent of `a`; no moving weight is frozen.
4. **Acceleration.** Formula (1.5) and all local pair formulas retain the `p'' log p` term.
5. **Endpoints.** Finite block entropies are continuous on `[0,1-c]` with `0 log 0=0`. The inherited coupling bound
   \[
   |F_Q(a,c)-F_Q(b,c)|\le s\,b(|a-b|)
   \]
   handles endpoint passage once a finite interior Jensen estimate is available. No differentiability of the entropy-rate limit is assumed.
6. **Target quantifier.** The desired statement is for fixed `rho`, fixed `c>37/40`, and all legal `a_0,a_1,t`. This archive does not reach that quantifier.
