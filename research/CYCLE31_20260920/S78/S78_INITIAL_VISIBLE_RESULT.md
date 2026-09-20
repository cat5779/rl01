# S78 result

**Global status: INCOMPLETE.** The full Shannon entropy-rate concavity target remains open. Major progress was obtained in three directions:

1. **DISPROVED:** unconditional nonnegative \(\Chi\)-reveal drift does not survive the first genuinely interacting-center case \(k=2\), even at half density and with a legal true-sine principal compression.
2. **PROVED:** a noncommutative, actual-weight matrix-martingale replacement controls the negative reveal drift by the Frobenius variance of the exact conditional \(2\times2\) pair kernel.
3. **PROVED:** when used to complete the one-center star to the full two-parity halo, the new tool reduces the certified nearby missing-parity payment from \(107488.020226\ldots\) to \(47537.632653\ldots\). The result is still far from proving \(h''<0\).

The complete English proof is here:

- :chatgpt-content-reference{index="5"}
- :chatgpt-content-reference{index="6"}
- :chatgpt-content-reference{index="7"}
- :chatgpt-content-reference{index="8"}
- :chatgpt-content-reference{index="9"}

The starting packet supplies the exact two-output pair functional, the one-center positive reveal theorem, and the warning that for \(k\ge2\) the conditional center updates are noncommuting rank-one matrices. citeturn457179view0

---

# PROVED

## 1. Exact pair-kernel semiconvexity

For a strict \(2\times2\) DPP kernel

\[
C=\begin{pmatrix}\alpha&z\\ \bar z&\beta\end{pmatrix},
\qquad s=|z|^2,
\]

put

\[
\begin{aligned}
p_{11}&=\alpha\beta-s,
&
p_{10}&=\alpha(1-\beta)+s,\\
p_{01}&=(1-\alpha)\beta+s,
&
p_{00}&=(1-\alpha)(1-\beta)-s .
\end{aligned}
\]

The exact actual-weight pair average is

\[
\mathcal F(C)
=
s\sum_{y\in\{0,1\}^2}\frac1{p_y}
+\log\frac{p_{11}p_{00}}{p_{10}p_{01}}.
\]

Thus, after conditioning on every exterior output, averaging the two selected outputs gives \(\mathcal F\) of their exact conditional kernel. No independent surrogate weights are introduced.

Assume

\[
\delta I\preceq C\preceq(1-\delta)I,
\qquad 0<\delta<\frac12.
\]

Define

\[
\kappa_\delta
=\frac{(1-2\delta)^2}{4\delta(1-\delta)},
\qquad
\theta_\delta=(1-2\delta)^2,
\]

\[
A_+(\delta)
=
1+\kappa_\delta+2(\kappa_\delta-1)_+,
\]

and

\[
\boxed{
M_2(\delta)
=
\frac{2}{\delta^2}
\left[
A_+(\delta)+1+3\theta_\delta
\right].
}
\]

Then, for every Hermitian direction \(H\),

\[
\boxed{
D^2\mathcal F(C)[H,H]
\ge
-M_2(\delta)\|H\|_F^2.
}
\tag{1}
\]

### Key estimates in the proof

The four exact cell ratios obey

\[
\frac{s}{p_{11}},\frac{s}{p_{00}}
\le
\kappa_\delta,
\qquad
\frac{s}{p_{10}},\frac{s}{p_{01}}
\le
\theta_\delta.
\tag{2}
\]

For example, if \(\lambda\le\mu\) are the eigenvalues of \(C\), then

\[
s=(\mu-\lambda)^2t(1-t).
\]

For an opposite-sign cell,

\[
\max_t\frac{s}{p_{10}}
=
\left(
\sqrt{\mu(1-\lambda)}
-
\sqrt{\lambda(1-\mu)}
\right)^2
\le (1-2\delta)^2.
\]

For a cell contribution

\[
\phi_y=\frac{s}{p_y}+\epsilon_y\log p_y,
\]

where \(\epsilon_y=1\) for \(11,00\) and \(-1\) for \(10,01\), write

\[
a_y=(\log p_y)',
\qquad
\ell_y=(\log p_y)''.
\]

The signed resolvents satisfy

\[
|a_y|^2\le2\delta^{-2}\|H\|_F^2,
\qquad
|\ell_y|\le\delta^{-2}\|H\|_F^2.
\]

A direct differentiation gives

\[
\phi_y''
=
\frac{s''}{p_y}
-2\frac{s'}{p_y}a_y
+\frac{s}{p_y}a_y^2
+\left(\epsilon_y-\frac{s}{p_y}\right)\ell_y.
\]

Using

\[
(s')^2\le2ss'',
\]

the first three terms are bounded below by

\[
-\frac{s}{p_y}a_y^2.
\]

Combining this with (2) yields (1).

### No hidden gap assumption

Actual DPP conditioning preserves the same gap. If

\[
\begin{pmatrix}C&v\\v^*&q\end{pmatrix}
\]

lies between \(\delta I\) and \((1-\delta)I\), then its conditional kernels

\[
C_1=C-\frac{vv^*}{q},
\qquad
C_0=C+\frac{vv^*}{1-q}
\]

also satisfy

\[
\delta I\preceq C_0,C_1\preceq(1-\delta)I.
\]

This follows from Schur complements of \(K-\delta I\) and \(I-K-\delta I\). Consequently all successive actual conditional pair kernels remain in the domain of (1).

---

## 2. Matrix-valued actual-weight reveal tool

Let \(P=\{i,j\}\) be a selected cross pair. Let \(\mathscr A\subset\mathscr V\) be nested exterior reveal sigma-fields, and write

\[
C_{\mathscr A}=K_{P\mid\mathscr A},
\qquad
C_{\mathscr V}=K_{P\mid\mathscr V}
\]

for the exact conditional pair kernels.

A one-site reveal has the two updates

\[
C_1=C-\frac{vv^*}{q},
\qquad
C_0=C+\frac{vv^*}{1-q},
\]

with the moving actual conditional probability \(q\). Therefore

\[
qC_1+(1-q)C_0=C.
\tag{3}
\]

Hence the conditional pair kernel is a Hermitian matrix martingale:

\[
\mathbb E[C_{\mathscr V}\mid\mathscr A]
=
C_{\mathscr A}.
\tag{4}
\]

Since

\[
C\longmapsto
\mathcal F(C)+\frac{M_2(\delta)}2\|C\|_F^2
\]

is convex by (1), conditional Jensen gives the main tool:

\[
\boxed{
\mathbb E f_{ij}(G_{\mathrm{fine}})
-
\mathbb E f_{ij}(G_{\mathrm{coarse}})
\ge
-\frac{M_2(\delta)}2
\mathbb E
\|C_{\mathscr V}-C_{\mathscr A}\|_F^2.
}
\tag{5}
\]

This uses the entire actual word distribution and makes no commutativity assumption.

### Exact one-site interface

For one revealed site,

\[
\boxed{
\mathbb E\!\left[
\|C_Y-C\|_F^2
\mid\mathscr A
\right]
=
\frac{\|v\|^4}{q(1-q)}.
}
\tag{6}
\]

Consequently,

\[
\boxed{
\mathbb E\Delta f_{ij}
\ge
-\frac{M_2(\delta)}2
\mathbb E\frac{\|v\|^4}{q(1-q)}.
}
\tag{7}
\]

In particular, replacing \(q\) by the marginal \(d\) would be invalid.

### Arbitrary-block cap

For an arbitrary finite block, or an increasing countable block,

\[
\begin{aligned}
\mathbb E\|C_{\mathscr V}-C_{\mathscr A}\|_F^2
&=
\mathbb E\operatorname{tr}(C_{\mathscr V}^2)
-
\mathbb E\operatorname{tr}(C_{\mathscr A}^2)\\
&\le
\mathbb E\operatorname{tr}
\left[
C_{\mathscr A}(I-C_{\mathscr A})
\right]\\
&\le\frac12.
\end{aligned}
\]

Thus

\[
\boxed{
\mathbb E\Delta f_{ij}
\ge
-\frac{M_2(\delta)}4
}
\tag{8}
\]

for any number of newly interacting centers or leaves. For a fixed pair, the payment does not grow with the number \(k\) of added sites.

For a fixed core \(I\),

\[
\boxed{
\mathbb E\Delta\Chi
\ge
-\frac{M_2(\delta)}2
\sum_{(i,j)\in\mathcal P(I)}
Q_{ij},
\qquad
Q_{ij}
=
\mathbb E
\|C_{ij}^{\rm fine}-C_{ij}^{\rm coarse}\|_F^2.
}
\tag{9}
\]

Since \(Q_{ij}\le1/2\),

\[
\mathbb E\Delta\Chi
\ge
-\frac{M_2(\delta)}4|\mathcal P(I)|.
\tag{10}
\]

Thus the absolute accumulation is linear in the number of cross pairs \(k\ell\). This is sufficient for the \(m=2\) star-completion interface, where there is only one core pair, but not for a growing interval core where \(k\ell\) can be quadratic in \(m\).

---

## 3. Coupling-sensitive center-block payment

After conditioning on the old exterior word, write the kernel on the selected pair and an unrevealed block \(R\) as

\[
\begin{pmatrix}
C&W\\
W^*&A_R
\end{pmatrix}.
\]

For the final block word \(y_R\),

\[
C_{y_R}-C
=
-W
\bigl(A_R-\operatorname{diag}(1-y_R)\bigr)^{-1}
W^*.
\]

Writing the block resolvent as \(R_y\) and \(P=W^*W\),

\[
\|C_{y_R}-C\|_F^2
=
\operatorname{tr}(R_yPR_yP)
\le
\|P\|\operatorname{tr}(PR_y^2).
\]

The accepted S72 Ward estimate is

\[
\mathbb E R_y^2\preceq\frac2\delta I,
\]

so

\[
\boxed{
\mathbb E\|C_{y_R}-C\|_F^2
\le
\frac2\delta
\|W\|_{\mathrm{op}}^2\|W\|_F^2.
}
\tag{11}
\]

The packet proves the corresponding actual-law Ward inequality and uses it in the original Shannon comparison. citeturn724413view1turn724413view2

For the half-density sine geometry, after conditioning on the old leaves except the selected leaf \(i\), let \(p\) be the distinguished center and \(R\) the set of additional same-parity centers. Then

\[
\|W\|_F^2=s_i+Z,
\]

where

\[
s_i=\sum_{q\in R}|b_{qi}|^2,
\]

\[
Z=
\sum_{q\in R}
\left|
\sum_{\ell\ne i}
\xi_\ell b_{p\ell}\overline{b_{q\ell}}
\right|^2,
\qquad
\xi_\ell=
\frac{1-Y_\ell}{1-d}-\frac{Y_\ell}{d}.
\]

The actual leaf variables satisfy

\[
\mathbb E\xi_\ell=0,
\qquad
\mathbb E\xi_\ell^2=\frac1{d(1-d)}.
\]

With \(e=\min(d,1-d)\),

\[
\mathbb E Z\le\frac{c^4}{24d(1-d)},
\qquad
Z\le\frac{c^4}{16e^2}.
\]

It follows that

\[
\mathbb E\|W\|_F^4\le J(d,c),
\]

where

\[
\boxed{
J(d,c)
=
\frac{c^4}{16}
+
\frac{c^6}{48d(1-d)}
+
\frac{c^8}{384e^2d(1-d)}.
}
\tag{12}
\]

Therefore the fixed-pair completion variance obeys

\[
\boxed{
Q_{p,i;R}
\le
\min\left\{
\frac12,\,
\frac{2J(d,c)}{\delta}
\right\}.
}
\tag{13}
\]

This is explicit and independent of the number of centers in \(R\).

---

## 4. Exact first interacting-center defect

Take two same-parity centers \(p,q\) and selected opposite-parity leaf \(i\). Condition on old leaves \(B\setminus\{i\}\), and define

\[
\alpha
=
d+\sum_{\ell\ne i}\xi_\ell|b_{p\ell}|^2,
\]

\[
\beta
=
d+\sum_{\ell\ne i}\xi_\ell|b_{q\ell}|^2,
\]

\[
\tau
=
\sum_{\ell\ne i}
\xi_\ell b_{p\ell}\overline{b_{q\ell}}.
\]

The exact kernel on the selected pair and the new center has

\[
C=
\begin{pmatrix}
\alpha&b_{pi}\\
\overline{b_{pi}}&d
\end{pmatrix},
\qquad
v=
\binom{\tau}{\overline{b_{qi}}}.
\]

Thus adding center \(q\) satisfies

\[
\boxed{
\begin{aligned}
&\mathbb E f_{pi}(G_{\{p,q\}\cup B})
-
\mathbb E f_{pi}(G_{\{p\}\cup B})\\
&\qquad\ge
-\frac{M_2(\delta)}2
\mathbb E
\frac{
\left(|\tau|^2+|b_{qi}|^2\right)^2
}{
\beta(1-\beta)
}.
\end{aligned}
}
\tag{14}
\]

This is a genuinely matrix-valued defect: \(\tau\) is the off-diagonal center-center correlation created by the old leaves.

For the real sine kernel, let

\[
S_2=\sum_{\ell\ne i}(b_{p\ell}b_{q\ell})^2,
\qquad
S_4=\sum_{\ell\ne i}(b_{p\ell}b_{q\ell})^4,
\]

\[
m_2=\frac1{d(1-d)},
\qquad
m_4=d^{-3}+(1-d)^{-3}.
\]

Then the actual independent leaf marginal gives

\[
\mathbb E\tau^2=m_2S_2,
\]

\[
\boxed{
\mathbb E\tau^4
=
3m_2^2S_2^2
+
\left(m_4-3m_2^2\right)S_4.
}
\tag{15}
\]

For same-parity centers separated by the nonzero even integer \(R=p-q\),

\[
\boxed{
\sum_{\ell\ {\rm opposite\ parity}}
|b_{p\ell}|^2|b_{q\ell}|^2
=
\frac{c^4}{2\pi^2R^2}.
}
\tag{16}
\]

Hence the fourth-moment interaction defect decays as \(O(R^{-4})\). In particular,

\[
\sum_{q\ne p}
\left(
\frac{c^4}{2\pi^2(p-q)^2}
\right)^2
=
\frac{c^8}{2880}.
\tag{17}
\]

This summability is a valid two-center spatial envelope. It is not used to pretend that simultaneous noncommuting center additions are pairwise additive; those additions are controlled by the block variance in (5), (11), or (13).

---

# DISPROVED

## Unconditional nonnegative \(k=2\) leaf-reveal drift

Use

\[
\rho=\frac12,
\qquad
c=\frac{19}{20},
\qquad
a=\frac1{40},
\qquad
d=\frac12.
\]

Take two centers

\[
C=\{0,10\},
\]

one core leaf \(7\), an old observed leaf \(-3\), and reveal the new leaf \(-1\):

\[
I=\{0,10,7\},
\]

\[
A_{\rm old}=\{0,10,7,-3\},
\qquad
A_{\rm new}=A_{\rm old}\cup\{-1\}.
\]

The core potential is

\[
\Chi=f_{0,7}+f_{10,7}.
\]

These are true finite principal compressions of the half-density sine kernel. The two leaf coupling vectors are nonparallel, and their rank-one center updates do not commute.

Every actual DPP word was enumerated using 80-digit interval arithmetic. The resulting reveal drift is

\[
\boxed{
\mathbb E\Chi(G_{A_{\rm new}})
-
\mathbb E\Chi(G_{A_{\rm old}})
\in
[-4.9124340176021932629,\,
 -4.9124340176021930]
\times10^{-7}<0.
}
\tag{18}
\]

The separately accumulated probability-mass intervals for both observed sets contain \(1\). The executed program returned

```text
PASS_INTERVAL_K2_NEGATIVE_REVEAL
```

Therefore:

\[
\boxed{
\text{The unconditional nonnegative one-center S75 reveal sign does not lift to }k=2.
}
\]

This is specifically an **opposite-parity leaf addition** in the presence of two centers. It is not a counterexample to Shannon entropy concavity.

---

# Quantitative interface to original Shannon entropy

The accepted S72 half-density benchmark is

\[
h''(a)
\le
-\frac1{50}
-2V_{m,L}(a)
+2\widehat\epsilon^\Chi_{m,L}.
\]

The packet also keeps the full-score core/pair and far-observation terms separate. citeturn724413view1

Take

\[
I=\{1,2\},
\qquad
A_L=[1-L,2+L],
\]

and the one-center star

\[
A_L^\star
=
\{2\}\cup
\bigl(A_L\cap\{\text{odd sites}\}\bigr).
\]

Let \(L_L(a)\) denote the accepted S75 star lower bound for the core pair. Reveal every missing even site as one interacting center block. The new theorem gives

\[
\mathbb E f_{12}(G_{A_L})
\ge
L_L(a)
-\frac{M_2(\delta)}2Q_L,
\]

where

\[
Q_L
=
\mathbb E
\left\|
C_{12\mid A_L}
-
C_{12\mid A_L^\star}
\right\|_F^2
\le\frac12.
\]

Since

\[
V_{2,L}
=
\frac12\mathbb E f_{12}(G_{A_L}),
\]

the original Shannon interface becomes

\[
\boxed{
\begin{aligned}
h''(a)\le{}&
-\frac1{50}
-L_L(a)
+\frac{M_2(\delta)}2Q_L\\
&+
2C_{\log}\widehat\tau(2)
+
2\Gamma_\Chi\eta_\delta\widehat\tau(L+1).
\end{aligned}
}
\tag{19}
\]

No star score has been identified with the full inverse score, and no omitted full-score pair has been assigned a favorable sign.

For

\[
c=\frac{19}{20},
\qquad
J=[0.02,0.03],
\qquad
\delta=0.02,
\]

the new constants are

\[
\kappa_\delta
=
11.7551020408163265\ldots,
\]

\[
\theta_\delta=0.9216,
\]

\[
M_2(\delta)
=
190150.5306122448979\ldots.
\]

Therefore

\[
\frac{M_2(\delta)}2Q_L
\le
\frac{M_2(\delta)}4
=
47537.6326530612245\ldots.
\]

The still-separate accepted full-score core/pair payment is

\[
2C_{\log}\widehat\tau(2)
=
486.9287385765045\ldots.
\]

As \(L\to\infty\), the new residual before subtracting the baseline and star lower bound is

\[
\boxed{
48024.5613916377290\ldots.
}
\tag{20}
\]

The earlier S75/S72 interface had the payments

\[
107488.020226\ldots
\quad\text{and}\quad
486.928738\ldots,
\]

for a total of

\[
107974.9489647355\ldots.
\]

Those earlier terms and their distinct origins are recorded explicitly in the packet. citeturn724413view0

Thus the new center-completion mechanism improves the certified total residual by the factor

\[
\frac{107974.9489647355\ldots}
     {48024.5613916377290\ldots}
=
2.24832764\ldots.
\]

This is a structural improvement: the missing-center payment now saturates at a fixed pair-kernel variance and no longer grows through the previous inverse-score energy envelope.

---

# Falsification tests

Any proposed stronger matrix cone or sign theorem must pass all of the following:

1. **Actual-sine \(k=2\) test:** it must permit the strict negative drift in (18).
2. **Actual-probability test:** every one-site step must preserve
   \[
   qC_1+(1-q)C_0=C
   \]
   with the moving conditional \(q\).
3. **Variance test:** its one-site defect must reduce exactly to
   \[
   \frac{\|v\|^4}{q(1-q)}.
   \]
4. **Noncommutative test:** it must work for nonparallel sine coupling vectors without commuting their rank-one matrices.

---

# INCOMPLETE

The exact remaining payment is:

1. The universal semiconvexity constant \(M_2(\delta)\) and the cap \(Q_L\le1/2\) are still much too large. At the benchmark they leave \(48024.56\ldots\), versus a star lower bound of order \(0.26275\).
2. The full-score core/pair term
   \[
   2C_{\log}\widehat\tau(2)
   =
   486.928738\ldots
   \]
   is unchanged.
3. For a growing interval core, summing the pair tool can cost \(O(k\ell)\), hence \(O(m^2)\). A collective-\(\Chi\) semiconvexity theorem or a block-cut cancellation is still required.
4. Both leaf addition and center addition are now tracked by the same compensated matrix-martingale tool, but neither operation has a universal nonnegative sign.
5. No conclusion is claimed for arbitrary density, the entire \(c\in(37/40,1)\) range, or global Shannon entropy-rate concavity.

No repository checkout, shared-state edit, PR action, or merge was performed.
