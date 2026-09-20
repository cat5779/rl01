# S78 RESULT — matrix-martingale pair-kernel variance tool

## Status

### PROVED

1. A two-site semiconvexity theorem for the exact, actual-weight pair functional \(\mathcal F\), with an explicit fixed-gap constant.
2. An actual-law matrix-martingale reveal inequality
   \[
   \mathbb E\Delta f_{ij}\ge -\frac{M_2(\delta)}2\,
   \mathbb E\|C_{ij}^{\rm fine}-C_{ij}^{\rm coarse}\|_F^2,
   \]
   valid for an arbitrary block of revealed sites. No rank-one matrices are assumed to commute.
3. For one revealed site, the variance payment is exactly
   \[
   \frac{\|v\|^4}{q(1-q)}
   \]
   conditional on the old exterior word, with the actual success probability \(q\).
4. For any number of interacting centers, the total pair-kernel variance is at most \(1/2\). Hence the entire same-parity center-completion cost for one fixed cross pair is at most \(M_2(\delta)/4\), independently of the number of added centers.
5. In the two-center sine geometry, the defect has an explicit fourth-moment formula in the true leaf weights. Its pairwise spatial envelope is summable.
6. Substitution into the accepted S72/S75 original-Shannon interface replaces the benchmark missing-parity envelope \(107488.020226\ldots\) by \(47537.632653\ldots\). Including the still-unpaid full-score core/pair term leaves \(48024.561392\ldots\), before subtracting the baseline and star lower bound.

### DISPROVED

Unconditional nonnegative \(\Chi\)-reveal drift already fails for two interacting centers in a legal, true half-density sine principal compression. A certified example is
\[
 \rho=\tfrac12,\qquad c=\tfrac{19}{20},\qquad a=\tfrac1{40},
\]
with centers \(\{0,10\}\), core leaf \(7\), old observed leaf \(-3\), and revealed leaf \(-1\). For
\[
 I=\{0,10,7\},\qquad A=\{0,10,7,-3\},
\]
where \(\Chi=f_{0,7}+f_{10,7}\), interval enumeration gives
\[
\mathbb E\Chi(G_{A\cup\{-1\}})-\mathbb E\Chi(G_A)
\in
[-4.9124340176021933,-4.9124340176021930]\,10^{-7}<0.
\]
Thus the one-center S75 positivity cone does not lift unchanged to \(k=2\).

### INCOMPLETE

The new interaction payment is still much larger than the available star lower bound, and the separate full-score core/pair truncation remains. This does not prove the original Shannon entropy-rate concavity target. For a growing interval core, applying the pair theorem separately to all cross pairs would also overcount; a collective \(\Chi\)-level semiconvexity or a block-cut mechanism is still needed.

---

## 1. Exact pair functional

For a strict \(2\times2\) DPP kernel
\[
 C=\begin{pmatrix}\alpha&z\\ \bar z&\beta\end{pmatrix},
 \qquad s=|z|^2,
\]
write
\[
\begin{aligned}
 p_{11}&=\alpha\beta-s, & p_{10}&=\alpha(1-\beta)+s,\\
 p_{01}&=(1-\alpha)\beta+s, & p_{00}&=(1-\alpha)(1-\beta)-s.
\end{aligned}
\]
The accepted two-output identity is
\[
 \mathbb E f_{12}((C-\operatorname{diag}(1-Y))^{-1})
 =\mathcal F(C),
\]
where
\[
 \mathcal F(C)=s\sum_{y\in\{0,1\}^2}\frac1{p_y}
 +\log\frac{p_{11}p_{00}}{p_{10}p_{01}}.       \tag{1}
\]
All four probabilities are the actual DPP cell probabilities.

---

## 2. A fixed-gap semiconvexity theorem

Let
\[
 \mathcal K_\delta=\{C=C^*: \delta I\preceq C\preceq(1-\delta)I\},
 \qquad 0<\delta<\tfrac12.
\]
Define
\[
 \kappa_\delta=\frac{(1-2\delta)^2}{4\delta(1-\delta)},
 \qquad
 \theta_\delta=(1-2\delta)^2
 =\frac{\kappa_\delta}{1+\kappa_\delta},                  \tag{2}
\]
\[
 A_+(\delta)=1+\kappa_\delta+2(\kappa_\delta-1)_+,       \tag{3}
\]
and
\[
 \boxed{
 M_2(\delta)=\frac{2}{\delta^2}
 \left[A_+(\delta)+1+3\theta_\delta\right].
 }                                                        \tag{4}
\]


### Lemma 2.0 — PROVED: gap preservation and signed resolvents

Suppose a conditional kernel on a retained block and one further site is
\[
 \begin{pmatrix}C&v\\v^*&q\end{pmatrix}
\]
and lies between \(\delta I\) and \((1-\delta)I\). Its two one-site
conditional kernels are
\[
 C_1=C-\frac{vv^*}{q},\qquad
 C_0=C+\frac{vv^*}{1-q}.
\]
Then
\[
 \delta I\preceq C_1,C_0\preceq(1-\delta)I.             \tag{4a}
\]
For \(C_1\), the lower bound follows from the Schur complement of
\(K-\delta I\):
\[
 C-\delta I-\frac{vv^*}{q-\delta}\succeq0,
\]
and \(q^{-1}\le(q-\delta)^{-1}\); its upper bound follows from
\(C_1\preceq C\). For \(C_0\), the lower bound follows from
\(C_0\succeq C\), while the upper bound is the same argument applied to
\(I-K\). Endpoint cases follow by continuity (and force the relevant
coupling vector to vanish). Iterating proves that arbitrary actual
conditioning preserves the same spectral gap.

Moreover, for any \(C\in\mathcal K_\delta\) and any two-output word
\(y\), put \(S=\operatorname{diag}(2y-1)\) and
\(E=C-\tfrac12I\). Then
\[
 C-\operatorname{diag}(1-y)=\frac12S+E,
 \qquad
 S\bigl(C-\operatorname{diag}(1-y)\bigr)=\frac12I+SE.
\]
Because \(\|E\|\le\tfrac12-\delta\), every signed resolvent satisfies
\[
 \left\|\bigl(C-\operatorname{diag}(1-y)\bigr)^{-1}\right\|
 \le\delta^{-1}.                                        \tag{4b}
\]
These two facts justify every fixed-gap use below; no favorable-word
restriction is present. ∎

### Lemma 2.1 — PROVED: cell-ratio bounds

For every \(C\in\mathcal K_\delta\),
\[
 \frac{s}{p_{11}},\frac{s}{p_{00}}\le\kappa_\delta,
 \qquad
 \frac{s}{p_{10}},\frac{s}{p_{01}}\le\theta_\delta.     \tag{5}
\]

#### Proof

Let \(\lambda\le\mu\) be the eigenvalues of \(C\). After removing the phase of \(z\), write a basis rotation with parameter \(t\in[0,1]\). Then
\[
 s=(\mu-\lambda)^2t(1-t).
\]
For the same-sign cells,
\[
 p_{11}=\lambda\mu,
 \qquad p_{00}=(1-\lambda)(1-\mu),
\]
and \(t(1-t)\le1/4\). Maximizing over
\(\delta\le\lambda\le\mu\le1-\delta\) gives the first bound in (5).

For \(p_{10}\), put
\[
 A=\lambda(1-\mu),\qquad B=\mu(1-\lambda),
 \qquad B-A=\mu-\lambda.
\]
Then
\[
 \frac{s}{p_{10}}
 =\frac{(B-A)^2t(1-t)}{A+(B-A)t}.
\]
The maximum over \(t\) is
\[
 (\sqrt B-\sqrt A)^2,
\]
which is increasing in \(\mu\) and decreasing in \(\lambda\). Its largest value is therefore
\((1-2\delta)^2\). The \(p_{01}\) case is symmetric. ∎

### Lemma 2.2 — PROVED: semiconvexity of \(\mathcal F\)

For every \(C\in\mathcal K_\delta\) and every Hermitian direction \(H\),
\[
 \boxed{
 D^2\mathcal F(C)[H,H]\ge-M_2(\delta)\|H\|_F^2.
 }                                                        \tag{6}
\]

#### Proof

For a word \(y\), let \(\epsilon_y=+1\) for \(11,00\) and
\(\epsilon_y=-1\) for \(10,01\). Its contribution to (1) is
\[
 \phi_y=\frac{s}{p_y}+\epsilon_y\log p_y.
\]
Along \(C+tH\), set
\[
 a_y=(\log p_y)',\qquad \ell_y=(\log p_y)''.
\]
Since
\[
 p_y=\pm\det(C-\operatorname{diag}(1-y)),
\]
with the sign chosen so that \(p_y>0\),
\[
 a_y=\operatorname{tr}(G_yH),
 \qquad
 \ell_y=-\operatorname{tr}(G_yHG_yH),                    \tag{7}
\]
where \(G_y=(C-\operatorname{diag}(1-y))^{-1}\). The fixed-gap signed-resolvent bound gives
\[
 |a_y|^2\le2\delta^{-2}\|H\|_F^2,
 \qquad
 |\ell_y|\le\delta^{-2}\|H\|_F^2.                      \tag{8}
\]

Let \(r_y=s/p_y\). If \(h=H_{12}\), then
\[
 s'=2\Re(\bar z h),\qquad s''=2|h|^2,
 \qquad (s')^2\le2ss''.
\]
A direct differentiation gives
\[
 \phi_y''
 =\frac{s''}{p_y}-2\frac{s'}{p_y}a_y+r_ya_y^2
 +(\epsilon_y-r_y)\ell_y.                                \tag{9}
\]
The first three terms in (9) are bounded below by \(-r_ya_y^2\): after division by \(s\), minimize the quadratic subject to
\(s''/s\ge(s'/s)^2/2\). Hence
\[
 \phi_y''\ge-r_ya_y^2-(|\epsilon_y-r_y|)|\ell_y|.        \tag{10}
\]
For a same-sign cell, (5) makes the coefficient in (10) at most
\[
 2r+|1-r|\le A_+(\delta).
\]
For an opposite-sign cell it is at most
\[
 2r+|-1-r|=1+3r\le1+3\theta_\delta.
\]
Using (8), then summing two cells of each type, proves (6). ∎

---

## 3. The matrix-valued actual-weight reveal tool

Let \(P=\{i,j\}\) be a selected pair. Let \(\mathcal A\subset\mathcal V\)
be two sigma-fields generated by revealed outputs outside \(P\). Write
\[
 C_{\mathcal A}=K_{P\mid\mathcal A},
 \qquad
 C_{\mathcal V}=K_{P\mid\mathcal V}                       \tag{11}
\]
for the exact conditional DPP kernels on the pair. Assume the ambient kernel has fixed gap \(\delta\), so all conditional pair kernels lie in \(\mathcal K_\delta\).

### Theorem 3.1 — PROVED: pair-kernel variance inequality

\[
 \boxed{
 \mathbb E f_{ij}(G_{P\cup\mathcal V})
 -\mathbb E f_{ij}(G_{P\cup\mathcal A})
 \ge
 -\frac{M_2(\delta)}2\,
 \mathbb E\|C_{\mathcal V}-C_{\mathcal A}\|_F^2.
 }                                                        \tag{12}
\]

#### Proof

A one-site DPP conditioning step has the form
\[
 C_1=C-\frac{vv^*}{q},
 \qquad
 C_0=C+\frac{vv^*}{1-q},                                  \tag{13}
\]
with the actual probability \(q\). Therefore
\[
 qC_1+(1-q)C_0=C.                                         \tag{14}
\]
Iterating (14), the conditional pair kernel is a Hermitian-matrix martingale:
\[
 \mathbb E[C_{\mathcal V}\mid\mathcal A]=C_{\mathcal A}. \tag{15}
\]

By Lemma 2.2, the function
\[
 C\longmapsto\mathcal F(C)+\frac{M_2(\delta)}2\|C\|_F^2
\]
is convex. Conditional Jensen, (15), and the exact two-output identity (1) give
\[
\begin{aligned}
 \mathbb E[\mathcal F(C_{\mathcal V})\mid\mathcal A]
 -\mathcal F(C_{\mathcal A})
 &\ge-\frac{M_2(\delta)}2
 \left(\mathbb E[\|C_{\mathcal V}\|_F^2\mid\mathcal A]
       -\|C_{\mathcal A}\|_F^2\right)\\
 &=-\frac{M_2(\delta)}2
 \mathbb E[\|C_{\mathcal V}-C_{\mathcal A}\|_F^2
            \mid\mathcal A].
\end{aligned}
\]
Averaging proves (12). No commutation was used. ∎

### Corollary 3.2 — PROVED: exact one-site payment

For the conditional kernel
\[
 \begin{pmatrix}C&v\\v^*&q\end{pmatrix}
\]
on the pair plus one newly revealed site,
\[
 \boxed{
 \mathbb E\bigl[\|C_Y-C\|_F^2\mid\mathcal A\bigr]
 =\frac{\|v\|^4}{q(1-q)}.
 }                                                        \tag{16}
\]
Thus
\[
 \boxed{
 \mathbb E\Delta f_{ij}
 \ge-\frac{M_2(\delta)}2
 \mathbb E\frac{\|v\|^4}{q(1-q)}.
 }                                                        \tag{17}
\]
This keeps every old word and the moving actual probability \(q\).

### Corollary 3.3 — PROVED: arbitrary-block cap

For any finite or increasing countable reveal block,
\[
 \boxed{
 \mathbb E\|C_{\mathcal V}-C_{\mathcal A}\|_F^2\le\frac12.
 }                                                        \tag{18}
\]
Indeed, using the martingale identity,
\[
 \mathbb E\|C_{\mathcal V}-C_{\mathcal A}\|_F^2
 =\mathbb E\operatorname{tr}(C_{\mathcal V}^2)
  -\mathbb E\operatorname{tr}(C_{\mathcal A}^2).
\]
Since \(0\preceq C_{\mathcal V}\preceq I\),
\(C_{\mathcal V}^2\preceq C_{\mathcal V}\). Hence the last display is at most
\[
 \mathbb E\operatorname{tr}\{C_{\mathcal A}(I-C_{\mathcal A})\}
 \le2\cdot\frac14=\frac12.
\]
Combining (12) and (18),
\[
 \boxed{
 \mathbb E\Delta f_{ij}\ge-\frac{M_2(\delta)}4
 }                                                        \tag{19}
\]
for revealing any number of interacting external sites. This cap is independent of \(k\).

### Corollary 3.4 — PROVED: accumulation for the full cross-pair sum

Let \(\mathcal P(I)\) be the set of opposite-parity pairs in a fixed core
\(I\). Revealing any exterior block gives the exact bookkeeping bound
\[
 \boxed{
 \mathbb E\Delta\Chi
 \ge-\frac{M_2(\delta)}2
       \sum_{(i,j)\in\mathcal P(I)}
       Q_{ij},
 \qquad
 Q_{ij}:=\mathbb E\|C_{ij}^{\rm fine}-C_{ij}^{\rm coarse}\|_F^2.
 }                                                        \tag{19a}
\]
In particular,
\[
 \mathbb E\Delta\Chi\ge
 -\frac{M_2(\delta)}4\,|\mathcal P(I)|.                 \tag{19b}
\]
Thus, for \(k\) centers and \(\ell\) core leaves, the absolute cap is
linear in the \(k\ell\) cross pairs and is independent of how many
exterior sites are revealed. For the entropy interface below,
\(|\mathcal P(I)|=1\), so adding arbitrarily many missing centers costs
only one block variance. For an interval core with both \(k\) and
\(\ell\) growing, (19b) may be quadratic in core size; this is the
collective-\(\Chi\) gap recorded as OPEN below.

### Operation tracking

* **Opposite-parity leaf addition:** apply (12) or (19a) with the new
  leaf in the exterior reveal block. Section 6 gives a true-sine
  \(k=2\) example where the resulting total \(\Chi\) drift is negative.
* **Same-parity center addition:** apply exactly the same matrix
  martingale inequality with the new center in the reveal block.
  Section 5 writes its first two-center defect explicitly, and Section 7
  uses a whole block of center additions to complete the one-center star
  halo.

No sign from one operation is transferred to the other.

---

## 4. Coupling-sensitive block form

Condition on the old exterior word and write the kernel on the pair and an unrevealed block \(R\) as
\[
 \begin{pmatrix}C&W\\W^*&A_R\end{pmatrix}.               \tag{20}
\]
For a final word \(y_R\),
\[
 C_{y_R}-C=-W(A_R-\operatorname{diag}(1-y_R))^{-1}W^*.    \tag{21}
\]
Let \(P=W^*W\). Using
\[
 \operatorname{tr}(RPRP)\le\|P\|\operatorname{tr}(PR^2)
\]
and the accepted actual-law Ward bound
\(\mathbb E R^2\preceq(2/\delta)I\), one obtains
\[
 \boxed{
 \mathbb E\|C_{y_R}-C\|_F^2
 \le\frac2\delta\|W\|_{\rm op}^2\|W\|_F^2.
 }                                                        \tag{22}
\]
Thus the useful payment is the minimum of (18) and (22), not merely the absolute cap.

For the half-density sine bipartite geometry, condition on all old opposite-parity leaves except the selected leaf \(i\). Let \(p\) be the distinguished center and let \(R\) be any set of additional same-parity centers. Put
\[
 e=\min(d,1-d).
\]
The cross block in (20) has
\[
 \|W\|_F^2=s_i+Z,
\]
where
\[
 s_i=\sum_{q\in R}|b_{qi}|^2,
 \qquad
 Z=\sum_{q\in R}\left|\sum_{\ell\ne i}\xi_\ell
 b_{p\ell}\overline{b_{q\ell}}\right|^2.                \tag{23}
\]
The actual leaf increments satisfy
\[
 \mathbb E\xi_\ell=0,
 \qquad
 \mathbb E\xi_\ell^2=\frac1{d(1-d)}.                    \tag{24}
\]
Using the half-density identities
\[
 \sum_{q\ \mathrm{same\ parity}}|b_{qi}|^2=\frac{c^2}{4},
 \qquad
 \sum_{\ell\ \mathrm{opposite\ parity}}|b_{p\ell}|^4
 =\frac{c^4}{48},                                        \tag{25}
\]
one gets
\[
 \mathbb EZ\le\frac{c^4}{24d(1-d)}.                     \tag{26}
\]
Moreover, the original half-density center--leaf coupling operator has norm \(c/2\), so
\[
 Z\le\frac{c^4}{16e^2}.                                  \tag{27}
\]
Consequently
\[
 \mathbb E\|W\|_F^4\le J(d,c),                          \tag{28}
\]
where
\[
 \boxed{
 J(d,c)=\frac{c^4}{16}
 +\frac{c^6}{48d(1-d)}
 +\frac{c^8}{384e^2d(1-d)}.
 }                                                        \tag{29}
\]
Combining (18), (22), and (29),
\[
 \boxed{
 Q_{p,i;R}:=\mathbb E\|C_{\rm full}-C_{\rm star}\|_F^2
 \le\min\left\{\frac12,\frac{2J(d,c)}\delta\right\}.
 }                                                        \tag{30}
\]
This is a finite, explicit, \(k\)-independent center-interaction payment.

---

## 5. Exact two-center specialization

Let the centers be \(p,q\), and let \(i\) be the selected opposite-parity core leaf. Condition on old leaves \(B_i=B\setminus\{i\}\). Define
\[
 \xi_\ell=\frac{1-Y_\ell}{1-d}-\frac{Y_\ell}{d},         \tag{31}
\]
\[
 \alpha=d+\sum_{\ell\in B_i}\xi_\ell|b_{p\ell}|^2,
 \quad
 \beta=d+\sum_{\ell\in B_i}\xi_\ell|b_{q\ell}|^2,
 \quad
 \tau=\sum_{\ell\in B_i}\xi_\ell
 b_{p\ell}\overline{b_{q\ell}},                         \tag{32}
\]
and
\[
 C=\begin{pmatrix}\alpha&b_{pi}\\\overline{b_{pi}}&d\end{pmatrix},
 \qquad
 v=\binom{\tau}{\overline{b_{qi}}}.                      \tag{33}
\]
Then observing center \(q\) changes the selected pair contribution by at least
\[
 \boxed{
 \mathbb E f_{pi}(G_{\{p,q\}\cup B})
 -\mathbb E f_{pi}(G_{\{p\}\cup B})
 \ge
 -\frac{M_2(\delta)}2
 \mathbb E\frac{(|\tau|^2+|b_{qi}|^2)^2}{\beta(1-\beta)}.
 }                                                        \tag{34}
\]
This is the requested first interacting-center defect. It is not obtained by scalarizing the two centers: \(\tau\) is the off-diagonal entry of the genuinely matrix-valued conditional center kernel.

For the real sine kernel, put
\[
 S_2=\sum_{\ell\in B_i}(b_{p\ell}b_{q\ell})^2,
 \qquad
 S_4=\sum_{\ell\in B_i}(b_{p\ell}b_{q\ell})^4,           \tag{35}
\]
\[
 m_2=\frac1{d(1-d)},
 \qquad
 m_4=d^{-3}+(1-d)^{-3}.                                   \tag{36}
\]
Independence of the actual leaf outputs gives the exact moments
\[
 \mathbb E\tau^2=m_2S_2,                                 \tag{37}
\]
\[
 \mathbb E\tau^4
 =3m_2^2S_2^2+(m_4-3m_2^2)S_4.                           \tag{38}
\]
Since \(\beta\in[\delta,1-\delta]\), (34) has the explicit envelope
\[
\begin{aligned}
 \mathbb E f_{pi}(G_{\{p,q\}\cup B})
 -\mathbb E f_{pi}(G_{\{p\}\cup B})
 \ge-\frac{M_2(\delta)}{2\delta(1-\delta)}
 \bigl[&|b_{qi}|^4+2|b_{qi}|^2m_2S_2\\
 &+3m_2^2S_2^2+(m_4-3m_2^2)S_4\bigr].                   \tag{39}
\end{aligned}
\]
If a monotone upper expression is preferred, replace the last two terms by
\[
 \max\{m_4,3m_2^2\}S_2^2.                               \tag{40}
\]

### Sine overlap and summability

For same-parity centers at even separation \(R=p-q\ne0\),
\[
 \boxed{
 \sum_{\ell\ \mathrm{opposite\ parity}}
 |b_{p\ell}|^2|b_{q\ell}|^2
 =\frac{c^4}{2\pi^2R^2}.
 }                                                        \tag{41}
\]
To prove (41), write \(R=2m\) and use
\[
 \frac1{x^2(x-R)^2}
 =\frac1{R^2}\left(\frac1{x^2}+\frac1{(x-R)^2}\right)
 +\frac2{R^3}\left(\frac1x-\frac1{x-R}\right),
\]
then sum over odd \(x\). The last difference sums to zero and
\(\sum_{x\ \mathrm{odd}}x^{-2}=\pi^2/4\).

Therefore the two-center defect in (39) decays as \(O(R^{-4})\) after the fourth moment is taken. In particular,
\[
 \sum_{q\ne p}
 \left(\frac{c^4}{2\pi^2(p-q)^2}\right)^2
 =\frac{c^8}{2880}.                                      \tag{42}
\]
The pairwise defects are summable. Equation (42) is not used to assert illegal pairwise additivity for simultaneous many-center conditioning; the valid many-center statement is Theorem 3.1 with the block variance (18) or (30).

---

## 6. Certified \(k=2\) obstruction

Use
\[
 \rho=\frac12,\quad c=\frac{19}{20},\quad a=\frac1{40},
 \quad d=\frac12.
\]
Take
\[
 C_{\rm centers}=\{0,10\},\qquad
 I=\{0,10,7\},
\]
\[
 A_{\rm old}=\{0,10,7,-3\},
 \qquad r=-1.
\]
The core potential is
\[
 \Chi=f_{0,7}+f_{10,7}.
\]
All matrices are true finite principal compressions of the half-density sine kernel. The two old/revealed leaf rank-one matrices are nonparallel and do not commute.

Eighty-digit interval enumeration of every actual DPP word gives
\[
\begin{aligned}
 \mathbb E\Chi(G_{A_{\rm old}})
 &\in[0.0001805501795704524011007462795153081402583516344768847242633015149645946827777057,\\
 &\hspace{8mm}0.0001805501795704524011007462795153081402583516344768847242633015149645946827777356],\\
 \mathbb E\Chi(G_{A_{\rm old}\cup\{r\}})
 &\in[0.0001800589361686921817744554939710159692463910322614653192024760504160805765456126,\\
 &\hspace{8mm}0.0001800589361686921817744554939710159692463910322614653192024760504160805765456449].
\end{aligned}
\]
Hence
\[
 \boxed{
 \mathbb E\Delta\Chi
 \in[-4.9124340176021932629078554429217101196060221541940506082546454851410623212293,\\
       -4.9124340176021932629078554429217101196060221541940506082546454851410623206093]
       \times10^{-7}<0.
 }                                                        \tag{43}
\]
The probability-mass intervals for both enumerations contain \(1\). The executable source is `s78_k2_counterexample.py`; the actual run returned
`PASS_INTERVAL_K2_NEGATIVE_REVEAL`.

This falsifies only the proposed two-center reveal sign. It is not a counterexample to Shannon entropy concavity.

---

## 7. Quantitative interface to the original Shannon entropy

At \(\rho=1/2\), use the accepted S75 geometry
\[
 I=\{1,2\},
 \qquad
 A_L^\star=\{2\}\cup(A_L\cap\{\text{odd sites}\}),
 \qquad
 A_L=[1-L,2+L].
\]
Let \(L_L(a)\) be the accepted one-center star lower bound for the pair \((1,2)\). Reveal the entire missing even block
\[
 R_L=A_L\setminus A_L^\star.
\]
Theorem 3.1 gives
\[
 \mathbb E f_{12}(G_{A_L})
 \ge L_L(a)-\frac{M_2(\delta)}2Q_L,                       \tag{44}
\]
where
\[
 Q_L=\mathbb E\|C_{12\mid A_L}-C_{12\mid A_L^\star}\|_F^2
 \le\frac12.                                             \tag{45}
\]
Since \(V_{2,L}=\mathbb E f_{12}(G_{A_L})/2\), the accepted S72 rate interface becomes
\[
 \boxed{
\begin{aligned}
 h''(a)\le{}&-\frac1{50}-L_L(a)
 +\frac{M_2(\delta)}2Q_L\\
 &+2C_{\log}\widehat\tau(2)
 +2\Gamma_\Chi\eta_\delta\widehat\tau(L+1).
\end{aligned}
 }                                                        \tag{46}
\]
No star score is identified with the full inverse score. The last two terms are the still-separate full-score core/pair and far-observation payments.

For
\[
 c=\frac{19}{20},
 \qquad J=[0.02,0.03],
 \qquad\delta=0.02,
\]
(2)--(4) give
\[
 \kappa_\delta=11.7551020408163265\ldots,
 \qquad
 \theta_\delta=0.9216,
\]
\[
 M_2(\delta)=190150.5306122448979\ldots,                  \tag{47}
\]
and therefore
\[
 \frac{M_2(\delta)}2Q_L\le\frac{M_2(\delta)}4
 =47537.6326530612245\ldots.                              \tag{48}
\]
The accepted full-score core/pair payment is
\[
 2C_{\log}\widehat\tau(2)=486.9287385765045\ldots.       \tag{49}
\]
As \(L\to\infty\), the proved residual in (46), before subtracting
\(1/50+L_\infty(a)\), is therefore at most
\[
 \boxed{48024.5613916377290\ldots.}                       \tag{50}
\]
The earlier S75/S72 route gave \(107974.9489647355\ldots\). Thus the matrix-martingale tool genuinely controls the missing-parity completion cost and improves that certified envelope by a factor greater than \(2.24\), but it remains far too large to prove negative entropy curvature.

---

## 8. Falsification tests for future improvements

Any proposed stronger cone or sign theorem should pass all four tests.

1. **Actual-sine \(k=2\) test.** It must permit the strict negative drift (43); otherwise it has silently imposed commutation, fixed reveal weights, or a star-only hypothesis.
2. **Martingale identity.** For every one-site step it must preserve
   \(qC_1+(1-q)C_0=C\) with the actual moving \(q\).
3. **Variance identity.** Its one-site defect must reduce to
   \(\|v\|^4/[q(1-q)]\). Replacing \(q\) by \(d\) is invalid.
4. **Block/noncommutative test.** For nonparallel sine coupling vectors, the proof must work without commuting the rank-one matrices. Theorem 3.1 does so because it acts on the conditional pair-kernel martingale, not on entrywise moments of the center block.

---

## 9. Exact remaining payment

The following remain open.

1. A much sharper lower curvature constant than (4), or a direct bound on the actual variance \(Q_L\), is needed before the star lower bound can compete numerically.
2. The full-score core/pair term \(2C_{\log}\widehat\tau(2)\) is untouched.
3. For a growing interval core, a collective \(\Chi\)-level version is needed; summing (12) over all cross pairs can scale quadratically.
4. Center addition and leaf addition are both covered by (12), but neither has a universal nonnegative sign. The certified example (43) shows why compensation is necessary.
5. No conclusion is claimed for the full interval \(c\in(37/40,1)\), arbitrary density, or the global Shannon entropy-rate concavity target.

## 10. Actual execution status

The following commands were run successfully in this session:

```text
python /mnt/data/S78/s78_k2_counterexample.py
python /mnt/data/S78/s78_interface_numbers.py
```

They returned, respectively,

```text
PASS_INTERVAL_K2_NEGATIVE_REVEAL
PASS_INTERFACE_ARITHMETIC
```

No repository checkout, shared-state edit, delegation, PR action, or merge was performed.
