# S52 cycle06 — A compensated conditional-odds susceptibility inequality

## Verdict: **INCOMPLETE**

A new actual-output inequality is proved below.  It replaces the crude use of
the worst log-odds slope on every edge by an exact observed-Fisher/Bregman
compensator.  It is valid at every finite even `n`, keeps the actual
configuration weights, and does not assume that the signed local compensator
is componentwise nonpositive.

At `c=19/20` it yields the unconditional finite-`n` estimate

\[
 R_n(c)\ge -\frac{-\log(1-c^2)-c^2}{2b}\,n
          =-29.239034\ldots n,
\tag{1}
\]

and, using the cyclic parity block and one explicit contrast-Fisher statistic,

\[
 \liminf_{n\to\infty,\;2\mid n}\frac{R_n(c)}n
 \ge -26.4886\ldots .
\tag{2}
\]

This is a substantial improvement over the direct worst-slope estimate, but it
does **not** reach the corrected-entropy milestone

\[
 M_bD_c-4=-1.20090484\ldots .
\]

The remaining quantified gap is about `25.2877` per site.  The precise
remaining obligation is to improve the payment of the signed Bregman skew in
Theorem 1 below (or to obtain a stronger lower bound on its contrast-Fisher
payment) by at least that amount.  No true Toeplitz entropy-rate conclusion is
claimed.

---

# 1. The new inequality

Put

\[
 H:=2P-I,\qquad K_c=\frac{I+cH}{2},\qquad
 S_y:=\operatorname{diag}(2y_1-1,\ldots,2y_n-1),
\]

so that at the midpoint `a_*=(1-c)/2`,

\[
 K_c=a_*I+cP,\qquad K_c(I-K_c)=bI,
 \qquad b=\frac{1-c^2}{4}.
\]

For a configuration `y`, define

\[
 A_y:=K_c-\operatorname{diag}(1-y)=\frac{S_y+cH}{2},
 \qquad B_y:=A_y^{-1}.
\]

All configurations have positive probability because `0<K_c<I`, hence every
`A_y` is invertible.  Define the finite-output Fisher information in the
**contrast direction** `K_t=(I+tH)/2` by

\[
 \mathcal F_{H,n}(c)
 :=\mathbb E_c\!\left[\left(\frac12\operatorname{Tr}(B_YH)\right)^2\right].
\tag{3}
\]

Finally set

\[
 \Phi(u):=-\log(1-u)-u,
 \qquad
 \alpha_c:=\frac{\Phi(c^2)}{c^2}.
\tag{4}
\]

## Theorem 1 (actual-output Fisher–Bregman susceptibility bound) — **PROVED**

For every even `n` and every `0<c<1`, for the cyclic projection law in the
assignment,

\[
\boxed{
 R_n(c)
 \ge
 4\sum_{i=1}^n\mathbb E\frac{x_i^2}{1-x_i^2}
 -\frac{n\Phi(c^2)}{2b}
 +2\Phi(c^2)\,\mathcal F_{H,n}(c).
 }
\tag{5}
\]

Consequently,

\[
\boxed{
 R_n(c)\ge-\frac{n\Phi(c^2)}{2b}.
 }
\tag{6}
\]

The mechanism is transferable.  The local part only needs: (i) a positive
binary law with nonpositive conditional pair determinants; (ii) a binary
symmetric-channel representation with correlation `c`; and (iii) an
exact-configuration determinant family whose diagonal Hessian is observed
Fisher information.  The projection DPP supplies these hypotheses here.

---

# 2. Exact probability, score, and Fisher identities

We first establish the interfaces used in the proof rather than treating an
author label as an axiom.

## Lemma 2.1 (exact-configuration determinant)

For a DPP with Hermitian contraction kernel `K`,

\[
 \Pr_K(Y=y)=(-1)^{n-|y|}\det\bigl(K-\operatorname{diag}(1-y)\bigr).
\tag{7}
\]

### Proof

Both sides are multilinear in the diagonal selectors.  Expanding the
determinant by the rows selected from `K` and from `-(I-\operatorname{diag}y)`
recovers the usual inclusion–exclusion formula for the event that exactly the
set `{i:y_i=1}` is occupied.  For `0<K<I` every exact event is positive, so the
sign in (7) is fixed and can be ignored when differentiating its logarithm.
\(\square\)

Allow a common diagonal perturbation `K(a)=K_c+(a-a_*)I`.  From (7), at
`a=a_*`,

\[
 \partial_a\log p_a(y)=\operatorname{Tr}B_y,
 \qquad
 -\partial_a^2\log p_a(y)=\operatorname{Tr}B_y^2.
\tag{8}
\]

Normalization gives the ordinary information identity

\[
 \mathcal F_{a,n}
 :=\mathbb E(\operatorname{Tr}B_Y)^2
 =\mathbb E\operatorname{Tr}B_Y^2.
\tag{9}
\]

No limiting entropy or limiting differentiability is used here; (8)–(9) are
finite-sample identities inside the open parameter interval.

## Lemma 2.2 (the common-diagonal Fisher information is exactly `n/b`)

\[
 \mathcal F_{a,n}=\frac nb.
\tag{10}
\]

### Proof

Diagonalize `K(a)`.  Its `k=n/2` eigenvalues in `ran P` are `a+c`, and its
other `k` eigenvalues are `a`.  The standard spectral construction of a DPP is
obtained directly from Cauchy–Binet: first select eigenvectors independently
with those Bernoulli probabilities, then sample from the resulting projection
DPP.  The second stage is independent of `a`.  Hence data processing for the
score gives

\[
 \mathcal F_{a,n}
 \le \frac{k}{(a+c)(1-a-c)}+\frac{k}{a(1-a)}.
\]

At `a=a_*`, both denominators are `b`, so the right side is `n/b`.

For the reverse inequality, let `N=\sum_iY_i`.  A DPP count has

\[
 \mathbb EN=\operatorname{Tr}K(a),\qquad
 \operatorname{Var}N=\operatorname{Tr}(K_c(I-K_c))=nb.
\]

The score identity and Cauchy–Schwarz give

\[
 n^2=(\partial_a\mathbb EN)^2
 =\operatorname{Cov}(N,\partial_a\log p_a(Y))^2
 \le nb\,\mathcal F_{a,n}.
\]

Thus `\mathcal F_{a,n}\ge n/b`, proving equality. \(\square\)

## Lemma 2.3 (diagonal observed information)

Let

\[
 \mathcal D_n:=\mathbb E\sum_i(B_Y)_{ii}^2.
\]

Then

\[
 \mathcal D_n
 =\sum_i\mathbb E\frac1{r_i(1-r_i)}
 =4\sum_i\mathbb E\frac1{1-x_i^2}.
\tag{11}
\]

### Proof

Perturb only the `i`th diagonal entry of `K`.  The marginal law of `Y_{-i}` is
unchanged, while, conditional on `Y_{-i}`, the probability of `Y_i=1` has unit
slope in that diagonal coordinate.  Equivalently, the cofactor in (7) is the
exact marginal weight of `Y_{-i}`.  Therefore

\[
 (B_y)_{ii}=
 \begin{cases}
  1/r_i(y_{-i}),&y_i=1,\\[2mm]
  -1/(1-r_i(y_{-i})),&y_i=0.
 \end{cases}
\]

Averaging first over `Y_i` gives `1/[r_i(1-r_i)]`; substituting
`r_i=(1+x_i)/2` gives (11). \(\square\)

Writing

\[
 \mathcal O_n:=\mathbb E\sum_{i\ne j}|(B_Y)_{ij}|^2,
\tag{12}
\]

(9)–(11) give the exact split

\[
 \mathcal D_n+\mathcal O_n=\frac nb.
\tag{13}
\]

This is the first compensation identity: `n/b-4n=nc^2/b` is exactly the
full-output Fisher ceiling minus the universal diagonal contribution `4n`.

---

# 3. The actual conditional square and its signed Bregman compensator

Fix an unordered pair `{i,j}` and an actual remaining output `z`.  Use the
**global**, not freely normalized, cell weights

\[
 p_{11}=\Pr(Y_i=1,Y_j=1,z),\quad
 p_{10}=\Pr(1,0,z),\quad
 p_{01}=\Pr(0,1,z),\quad
 p_{00}=\Pr(0,0,z),
\]

and let

\[
 m_z:=p_{11}+p_{10}+p_{01}+p_{00},
 \qquad
 \Delta_z:=p_{10}p_{01}-p_{11}p_{00}.
\tag{14}
\]

Conditioning a DPP on any fixed inclusion/exclusion pattern again gives a DPP
on the remaining sites, so

\[
 \Delta_z\ge0.
\tag{15}
\]

The Boolean conditional-log-odds difference is the same in both directions:

\[
 \theta_z:=\partial_jh_i(z)=\partial_ih_j(z)
 =\log\frac{p_{11}p_{00}}{p_{10}p_{01}}\le0.
\tag{16}
\]

## Lemma 3.1 (Jacobi square identity)

For every one of the four configurations `y=(a,b,z)`,

\[
 |(B_y)_{ij}|^2=\frac{\Delta_z}{p_{ab}^2}.
\tag{17}
\]

### Proof

Apply the Desnanot–Jacobi identity to the two diagonal coordinates `i,j` in
`A_y`.  The four diagonal choices are precisely the four exact probabilities
in (14), including their fixed determinant signs.  The remaining term is the
product of the two conjugate off-diagonal cofactors.  Dividing by
`|\det A_y|^2=p_{ab}^2` gives (17). \(\square\)

It follows that the directed observed-Fisher payment of this square is

\[
 2\Delta_z\left(\frac1{p_{11}}+\frac1{p_{10}}+
                  \frac1{p_{01}}+\frac1{p_{00}}\right),
\tag{18}
\]

where the factor two is for `i\to j` and `j\to i`.  The directed susceptibility
cost is `2m_z(-\theta_z)`.

Normalize the table by `m_z` and set

\[
 u_{10}:=\frac{\Delta_z}{m_zp_{10}},\qquad
 u_{01}:=\frac{\Delta_z}{m_zp_{01}},
\]

\[
 v_{11}:=\frac{\Delta_z}{m_zp_{11}},\qquad
 v_{00}:=\frac{\Delta_z}{m_zp_{00}}.
\tag{19}
\]

Define

\[
 \Psi(v):=v-\log(1+v)\ge0.
\tag{20}
\]

## Lemma 3.2 (exact skew-minus-trapezoid identity)

For one direction of the square,

\[
\begin{aligned}
 &m_z(-\theta_z)
 -\Delta_z\left(\frac1{p_{11}}+\frac1{p_{10}}+
                  \frac1{p_{01}}+\frac1{p_{00}}\right)\\
 &\quad=m_z\bigl[
   \Phi(u_{10})+\Phi(u_{01})
  -\Psi(v_{11})-\Psi(v_{00})
 \bigr].
\end{aligned}
\tag{21}
\]

### Proof

For the normalized table write `A,B,C,D` for `11,10,01,00` and
`\delta=BC-AD`.  The independent table with the same one-site margins is

\[
 (A+\delta,\;B-\delta,\;C-\delta,\;D+\delta).
\]

Its odds ratio is one.  Consequently

\[
 \log\frac{BC}{AD}
 =-\log(1-\delta/B)-\log(1-\delta/C)
   +\log(1+\delta/A)+\log(1+\delta/D).
\]

Subtracting `\delta(1/A+1/B+1/C+1/D)` gives (21). \(\square\)

The right side of (21) has no fixed pointwise sign.  For example,

\[
 (A,B,C,D)=(0.089,0.811,0.011,0.089)
\]

has `BC-AD=0.001` and makes the left side of (21) strictly positive.  Thus the
ansatz `-\theta\le` endpoint observed Fisher is false.  This is a failure of a
pointwise ansatz, not a counterexample to the cyclic susceptibility conjecture.

---

# 4. The sharp BSC cap on the positive skew

The law `Q_{n,c}` is the binary-symmetric-channel output, with correlation
`c`, of the projection DPP `DPP(P)`.  A short proof avoids importing this as a
black box.  For spins `S_i=2Y_i-1`, a DPP satisfies

\[
 \mathbb E\prod_{i\in A}S_i=\det((2K-I)_A).
\tag{22}
\]

At `K=(I+cH)/2`, this equals `c^{|A|}\det(H_A)`, exactly the Fourier moment
obtained by passing the spin law of `DPP(P)` through independent BSCs of
correlation `c`.  Fourier moments determine a law on the finite cube.

After conditioning on the actual remaining output `z`, the two unobserved
output bits are still independent BSC outputs of their two latent bits under
the posterior given `z`.

## Lemma 4.1 (gain-cell cap)

For every actual conditional square,

\[
 0\le u_{10},u_{01}\le c^2.
\tag{23}
\]

### Proof

Let the posterior latent two-bit table be `(A,B,C,D)`, with `B,C` the two
opposite cells, and put `\Delta_X=BC-AD`.  If `\epsilon=(1-c)/2` and
`q=(1+c)/2`, the corresponding output opposite cell is

\[
 B'=q^2B+\epsilon^2C+q\epsilon(A+D),
\]

and determinants transform by

\[
 \Delta_Y=c^2\Delta_X.
\]

The output conditional table is a DPP table, so `\Delta_Y\ge0`, and hence
`\Delta_X\ge0`.  With `s=A+D` and `C=1-s-B`, direct algebra gives

\[
 B'-\Delta_X=(B-\epsilon)^2+s(B+\epsilon c)+AD\ge0.
\tag{24}
\]

Thus `\Delta_Y/B'\le c^2`.  This quotient is exactly `u_{10}`.  Interchanging
`B,C` proves the other inequality. \(\square\)

Since

\[
 \frac{\Phi(u)}u=\sum_{m\ge2}\frac{u^{m-1}}m
\]

is increasing on `[0,1)`, (23) implies

\[
 \Phi(u)\le\alpha_c u\qquad(0\le u\le c^2).
\tag{25}
\]

Let

\[
 \mathcal G_n
 :=\mathbb E\sum_{i\ne j}\mathbf1_{\{Y_i\ne Y_j\}}
                    |(B_Y)_{ij}|^2.
\tag{26}
\]

Using (17), summing (21) with the **actual** weights `m_z`, keeping the negative
`-\Psi` terms, and applying (25) only to the two gain cells gives

\[
 \Xi_n\le\alpha_c\mathcal G_n,
\tag{27}
\]

where `\Xi_n` is the exact global difference

\[
 \sum_{i\ne j}\mathbb E[-\partial_jh_i]-\mathcal O_n.
\tag{28}
\]

Equation (27), not a worst-slope bound on every Stein edge, is the new local
tool.

---

# 5. Paying the gain Fisher information once

A second exact identity prevents multiple use of the same Fisher budget.
From `A_Y=(S_Y+cH)/2`,

\[
 S_YB_Y=2I-cHB_Y.
\tag{29}
\]

The finite parametric family `K_t=(I+tH)/2` is normalized, so

\[
 \mathbb E\operatorname{Tr}(HB_Y)=0,
 \qquad
 \mathbb E\operatorname{Tr}(HB_YHB_Y)=4\mathcal F_{H,n}(c).
\tag{30}
\]

On the other hand,

\[
 \operatorname{Tr}(S_YB_YS_YB_Y)
 =\sum_{i,j}(2Y_i-1)(2Y_j-1)|(B_Y)_{ij}|^2.
\]

The diagonal and same-output off-diagonal entries enter with `+`, while the
opposite-output entries enter with `-`.  Therefore, using (13),

\[
 \mathbb E\operatorname{Tr}(S_YB_YS_YB_Y)
 =\frac nb-2\mathcal G_n.
\tag{31}
\]

Taking expectations in the square of (29) and using (30) gives

\[
 \frac nb-2\mathcal G_n=4n+4c^2\mathcal F_{H,n}(c),
\]

or

\[
\boxed{
 \mathcal G_n
 =\frac12\left(\frac nb-4n-4c^2\mathcal F_{H,n}(c)\right).
 }
\tag{32}
\]

In particular `\mathcal G_n\le nc^2/(2b)`.

Now combine (13), (27), (28), and the definition of `R_n`:

\[
\begin{aligned}
 R_n
 &=\frac{nc^2}{b}-\mathcal O_n-\Xi_n\\
 &=\mathcal D_n-4n-\Xi_n\\
 &\ge \mathcal D_n-4n-\alpha_c\mathcal G_n.
\end{aligned}
\]

Substitution of (11) and (32), with `\alpha_cc^2=\Phi(c^2)`, proves (5).
Dropping the two nonnegative terms in (5) proves (6).  \(\square\)

---

# 6. Cyclic quantitative refinements

These refinements use only the supplied parity interface and an explicitly
proved finite-output Fisher lower bound.

## 6.1 Diagonal Fisher slack from the parity block

Order the two parities so that

\[
 H=\begin{pmatrix}0&V\\V^*&0\end{pmatrix},
\]

with `V` unitary.  For a fixed site `i`, put

\[
 y_i=\sum_j |V_{ij}|^2(1-2Y_j)
\]

on the opposite parity.  The supplied exact interface is

\[
 \mathbb E[x_i\mid\text{opposite parity}]=c^2y_i.
\tag{33}
\]

Because `x\mapsto(1-x^2)^{-1}` is convex on `(-1,1)`,

\[
 \mathbb E\frac1{1-x_i^2}
 \ge \mathbb E\frac1{1-c^4y_i^2}.
\tag{34}
\]

The opposite parity consists of independent fair spins.  In the cyclic block,

\[
 |V_{ab}|^2=rac1{k^2\sin^2(\pi(a-b-1/2)/k)}.
\tag{35}
\]

As `k\to\infty`, `y_i` converges in every fixed moment to

\[
 Y_\infty=\sum_{m\in\mathbb Z}
 \frac{\varepsilon_m}{\pi^2(m+1/2)^2},
\tag{36}
\]

where the `\varepsilon_m` are independent fair signs.  The needed moments are

\[
 \mathbb EY_\infty^2=\frac13,
\quad
 \mathbb EY_\infty^4=\frac{71}{315},
\quad
 \mathbb EY_\infty^6=\frac{24587}{155925}.
\tag{37}
\]

For completeness, if `A_r=\sum_m a_m^r` with
`a_m=[\pi^2(m+1/2)^2]^{-1}`, then

\[
 A_2=\frac13,
 \qquad A_4=\frac{17}{315},
 \qquad A_6=\frac{1382}{155925},
\]

and the Rademacher moment identities give

\[
 \mathbb EY^4=3A_2^2-2A_4,
 \qquad
 \mathbb EY^6=15A_2^3-30A_2A_4+16A_6.
\]

Keeping the first three nonnegative terms of
`(1-c^4Y^2)^{-1}` gives

\[
 \liminf\frac{\mathcal D_n-4n}{n}\ge d_3(c),
\tag{38}
\]

where

\[
 d_3(c):=4\left(
 \frac{c^4}{3}
 +\frac{71c^8}{315}
 +\frac{24587c^{12}}{155925}
 \right).
\tag{39}
\]

## 6.2 A concrete lower bound on the contrast Fisher information

Let `v_d=V_{a,a-d}` and pair each even site with the odd site having the same
block index.  Define

\[
 T_k:=\sum_{a=0}^{k-1}S_{E,a}S_{O,a}.
\]

Along `K_t=(I+tH)/2`, the spin moment identity (22) gives

\[
 \mathbb E_tT_k=-t^2k|v_0|^2.
\tag{40}
\]

For `a\ne b`, the four-spin determinant is

\[
 \mathbb E_t(S_{E,a}S_{O,a}S_{E,b}S_{O,b})
 =t^4|v_0^2-v_{a-b}v_{b-a}|^2.
\]

Since the circulant eigenvalues of `V` are `e^{-\pi ir/k}`, `V^2` is a
nontrivial cyclic shift and

\[
 \sum_dv_dv_{-d}=0.
\]

A direct expansion therefore yields the exact variance

\[
 \operatorname{Var}_t(T_k)
 =k\left(1+t^4\sum_d|v_d|^2|v_{-d}|^2\right).
\tag{41}
\]

The score covariance identity and Cauchy–Schwarz imply

\[
 \mathcal F_{H,n}(c)
 \ge\frac{(\partial_t\mathbb E_tT_k|_{t=c})^2}
          {\operatorname{Var}_c(T_k)}.
\tag{42}
\]

Now

\[
 |v_0|^2\longrightarrow\frac4{\pi^2},
 \qquad
 \sum_d|v_d|^2|v_{-d}|^2
 \longrightarrow
 \sum_{m\in\mathbb Z}\frac1{\pi^4(m^2-1/4)^2}
 =\frac2{\pi^2}.
\]

Hence

\[
 \liminf\frac{\mathcal F_{H,n}(c)}n\ge f_*(c),
\tag{43}
\]

with

\[
 f_*(c):=
 \frac{32c^2/\pi^4}{1+2c^4/\pi^2}.
\tag{44}
\]

Combining (5), (38), and (43) proves

\[
\boxed{
 \liminf_{n\to\infty,\;2\mid n}\frac{R_n(c)}n
 \ge d_3(c)-\frac{\Phi(c^2)}{2b}+2\Phi(c^2)f_*(c).
 }
\tag{45}
\]

At `c=19/20`,

\[
 \Phi(c^2)=\log\frac{400}{39}-\frac{361}{400}
 =1.4254029\ldots,
\]

\[
 d_3(c)=2.0249660\ldots,
 \qquad f_*(c)=0.25448\ldots,
\]

and (45) is the stated bound `-26.4886...`.

---

# 7. Interface with the corrected-law milestone

The susceptibility theorem above uses only the true finite DPP law and the
parity interface (33).  It does **not** use a corrected law, a layerwise KL
bound, or a limiting entropy derivative.

For scope comparison only, take the following source interfaces exactly in
their stated directions:

1. the author-submission identity
   \[
   W_n+C_n=R_n+\sum_\ell\kappa_\ell
   D(\mu_\ell^{\rm corrected}\Vert\gamma_{\ell,c})+o(n);
   \]
2. the independently reviewed reverse-KL envelope
   \[
   \liminf\frac1n\sum_\ell\kappa_\ell
   D(\mu_\ell^{\rm corrected}\Vert\gamma_{\ell,c})
   \ge-M_bD_c;
   \]
3. the author-submission count/reference formula
   \[
   \widehat H_n''(a_*)=-4n-W_n-C_n+o(n).
   \]

These formulas imply, with the signs shown,

\[
 \liminf R_n/n\ge M_bD_c-4+\varepsilon
 \quad\Longrightarrow\quad
 \liminf(W_n+C_n)/n\ge-4+\varepsilon,
\]

and hence `\widehat H_n''(a_*)\le-\varepsilon n+o(n)`.  The KL direction is the
reverse direction displayed above; no forward-KL quantity is substituted, no
unknown signed term is set to zero, and no derivative of an `O(1)` layerwise
bound is taken.

The present bound (45) falls short, so it does not certify corrected cyclic
concavity.  Even such a certification would still not prove full true-Toeplitz
entropy-rate concavity.

---

# 8. Source interfaces actually used

Files read on branch `research/sa-cycle06-s51-s56-20260918`:

- `research/CYCLE06_20260918/S43/S43_CYCLE05_RESULT.md`, especially its
  susceptibility decomposition and Appendix-B sign conventions;
- `research/INDEPENDENT_REVIEW_20260918/S43_CYCLE03.md`, only for the stated
  reverse-KL envelope when checking the scoped implication;
- `research/INDEPENDENT_REVIEW_20260918/S45_CYCLE04.md`, as scope control for
  the terminal/count route, not as an input to Theorem 1;
- `results/SA04/TASK.md`, only to check the corrected-law naming and
  normalization.

Theorem 1 itself does not promote any pending author claim into an axiom.  Its
new determinant, Fisher, BSC-cap, and cyclic-statistic interfaces are proved
above.

---

# 9. Precise remaining obligation

Equation (21) identifies the only loss in the new mechanism.  One must prove a
stronger actual-law estimate for

\[
 \sum_{\{i,j\},z}2m_z
 \bigl[\Phi(u_{10})+\Phi(u_{01})
       -\Psi(v_{11})-\Psi(v_{00})\bigr],
\]

rather than discarding both negative `\Psi` terms and replacing
`\Phi(u)/u` by its endpoint value `\alpha_c`.  At the benchmark, (45) must be
raised by at least

\[
 25.2877\ldots
\]

per site to reach `M_bD_c-4`.  This is an actual conditional-square
obligation.  It is not a terminal-clock bound, not a forward/reverse KL
conversion, and not a true-versus-corrected layer comparison.
