# S78 — exact log-barrier compensation for interacting reveals

## Status

### PROVED

1. For the exact two-output pair functional \(\mathcal F\), the compensated function
   \[
   \mathcal B(C):=\mathcal F(C)-\log\det C-\log\det(I-C)
   \]
   is convex on every rank-one positive line that stays inside the strict-contraction cone.
   The proof is an exact sum-of-squares Hessian identity, not an arbitrary-Hessian envelope.

2. Consequently, every actual one-site DPP reveal, with its moving actual probability, satisfies
   \[
   \mathbb E\Delta\mathcal F\ge \mathbb E\Delta\ell,
   \qquad
   \ell(C):=\log\det C+\log\det(I-C).
   \]
   This telescopes through any finite or increasing countable sequence of noncommuting rank-one
   updates.  It handles both opposite-parity leaf addition and same-parity center addition.

3. The accumulated barrier loss is exactly the sum of two reverse Kullback--Leibler
   divergences: the actual newly revealed block law versus the same law conditioned on the retained
   pair being respectively `11` and `00`.  Thus the defect is an identified information cost, not
   an unnamed remainder.

4. For a fixed cross pair, adding arbitrarily many interacting centers has a completion payment
   independent of their number:
   \[
   \mathbb E\mathcal F(C_{\rm fine})
   \ge \mathbb E\mathcal F(C_{\rm coarse})
      -\bigl\{\mathbb E\ell(C_{\rm coarse})-2\log[\delta(1-\delta)]\bigr\}.
   \]
   The completely uniform payment is
   \[
   2\log\frac1{4\delta(1-\delta)}.
   \]

5. In the half-density one-center sine star, the initial barrier is explicitly controlled by the
   actual independent leaf marginal.  For selected pair weight \(s=|z_i|^2\),
   \[
   D_{\star}\le
   \log\frac{(d^2-s)((1-d)^2-s)}{\delta^2(1-\delta)^2}
   -\frac{\sum_{\ell\ne i}w_\ell^2}
          {d(1-d)(1-\delta)^2}.
   \]
   At the midpoint there is a convergent all-moment refinement with a certified tail.

6. The one-step compensated defect has an exact resolvent formula and a true-sine \(k=2\)
   fourth-moment envelope decaying as \(O(|p-q|^{-4})\).  Thus the first-interaction defects are
   spatially summable.  The arbitrary-block theorem, rather than illegal pairwise additivity, is
   the valid route after several centers have already been observed.

7. In the accepted original-Shannon interface at \(c=19/20\), \(\delta=1/50\), the asymptotic
   missing-parity envelope is reduced from \(107488.020226\ldots\) to less than
   \(3.745696\).  Including the unchanged full-score core/pair payment leaves
   \(490.674434\ldots\), an improvement factor exceeding \(220.05\).

### DISPROVED

Unconditional zero-payment monotonicity also fails for **center addition**, even at half density,
at the midpoint, and starting from a genuine one-center star.  A certified true-sine example has
raw drift
\[
[-0.001933130713983041,-0.001933130713983040]<0.
\]
Together with the earlier certified two-center leaf-addition obstruction, neither operation has a
universal raw sign.

### INCOMPLETE

The original Shannon entropy-rate concavity target remains open.  The separate full-score
core/pair payment is still \(486.928738\ldots\), and even the new barrier floor-envelope is larger
than the available \(0.26275\) star lower bound.  For a growing core containing \(k\) centers and
\(\ell\) leaves, the presently proved pair-barrier sum has worst-case accumulation \(O(k\ell)\);
a collective barrier or the separate block-cut mechanism is still required.

---

## 1. Pair functional and barrier

Let
\[
C=\begin{pmatrix}\alpha&z\\ \bar z&\beta\end{pmatrix},
\qquad 0\prec C\prec I,
\qquad s=|z|^2.
\]
The four actual DPP cell probabilities are
\[
\begin{aligned}
p_{11}&=\alpha\beta-s,
& p_{10}&=\alpha(1-\beta)+s,\\
p_{01}&=(1-\alpha)\beta+s,
& p_{00}&=(1-\alpha)(1-\beta)-s.
\end{aligned}
\]
The accepted exact pair-output average is
\[
\mathcal F(C)
=s\sum_{y\in\{0,1\}^2}\frac1{p_y}
 +\log\frac{p_{11}p_{00}}{p_{10}p_{01}}.                 \tag{1}
\]
Define
\[
\ell(C)=\log\det C+\log\det(I-C)
       =\log p_{11}+\log p_{00},                         \tag{2}
\]
and
\[
\mathcal B(C)=\mathcal F(C)-\ell(C).                    \tag{3}
\]

The role of \(\ell\) is forced by the exact Hessian calculation below.  It is not a renamed
remainder and is quantitatively paid at the entropy interface.

---

## 2. PROVED: exact rank-one square identity

Let
\[
C(t)=C+tH,
\qquad H=vv^*,
\qquad h=v_1\overline{v_2},
\]
on any interval for which \(0\prec C(t)\prec I\).  For a pair word \(y\), set
\[
D_y=\operatorname{diag}(1-y),
\qquad G_y(t)=(C(t)-D_y)^{-1},
\qquad a_y(t)=v^*G_y(t)v.
\]
Let \(\epsilon_y=+1\) for \(y=11,00\) and \(\epsilon_y=-1\) for
\(y=10,01\).

### Lemma 2.1 — PROVED

For every such \(C(t)\),
\[
\boxed{
\frac{d^2}{dt^2}\mathcal F(C(t))
=
\sum_y\frac{2|h-a_yz(t)|^2}{p_y(t)}
-a_{11}^2-a_{00}^2+a_{10}^2+a_{01}^2.
}                                                         \tag{4}
\]
Consequently,
\[
\boxed{
\frac{d^2}{dt^2}\mathcal B(C(t))
=
\sum_y\frac{2|h-a_yz(t)|^2}{p_y(t)}
+a_{10}^2+a_{01}^2\ge0.
}                                                         \tag{5}
\]

### Proof

For each word, write its contribution to (1) as
\[
\phi_y(t)=\frac{s(t)}{p_y(t)}+\epsilon_y\log p_y(t).
\]
Because the perturbation is rank one, the matrix determinant lemma makes every
\(p_y(t)\) affine in \(t\).  Hence
\[
\frac{p_y'}{p_y}=a_y,
\qquad a_y'=-a_y^2.
\]
Also
\[
s'=2\operatorname{Re}(\bar zh),
\qquad s''=2|h|^2.
\]
Direct differentiation gives
\[
\phi_y''
=\frac{s''-2s'a_y+2sa_y^2}{p_y}-\epsilon_ya_y^2
=\frac{2|h-a_yz|^2}{p_y}-\epsilon_ya_y^2.
\]
Summing the four words proves (4).  Along the same line,
\[
\ell''=-a_{11}^2-a_{00}^2.
\]
Subtracting this from (4) proves (5).  No commutativity assumption appears.  ∎

### Falsification implication

Any stronger claim that \(\mathcal F\) itself is rank-one convex must fail whenever the two
same-sign terms in (4) dominate.  Section 7 gives a legal actual-sine realization of this failure.
The compensator in (2) cancels exactly those two potentially negative squares.

---

## 3. PROVED: actual-weight compensated reveal theorem

Suppose that, after conditioning on an arbitrary old exterior word, the kernel on a retained pair
and one newly revealed site is
\[
\widehat C=
\begin{pmatrix}
C&b\\ b^*&q
\end{pmatrix},
\qquad 0\prec\widehat C\prec I.
\]
The new output is one with its actual probability \(q\), and zero with probability \(1-q\).  The
exact pair kernels after the reveal are
\[
C_1=C-\frac{bb^*}{q},
\qquad
C_0=C+\frac{bb^*}{1-q},                                  \tag{6}
\]
so
\[
qC_1+(1-q)C_0=C.                                          \tag{7}
\]

### Theorem 3.1 — PROVED

For every actual one-site reveal,
\[
\boxed{
q\mathcal F(C_1)+(1-q)\mathcal F(C_0)-\mathcal F(C)
\ge
q\ell(C_1)+(1-q)\ell(C_0)-\ell(C).
}                                                         \tag{8}
\]
Equivalently,
\[
q\mathcal B(C_1)+(1-q)\mathcal B(C_0)\ge\mathcal B(C).  \tag{9}
\]

### Proof

The three kernels in (6) lie on one rank-one line and are strict contractions.  Equation (5)
makes \(\mathcal B\) convex on the whole segment.  Jensen with the actual barycentric weights in
(7) gives (9), hence (8).  ∎

This theorem is applied after the two retained outputs have been exactly averaged using (1).
Therefore \(q\) is the actual probability conditional on the old exterior word, not an
independent substitute and not the probability conditional on a deleted set of configurations.

---

## 4. Exact one-step interaction defect

Put
\[
A=b^*C^{-1}b,
\qquad
B=b^*(I-C)^{-1}b.                                        \tag{10}
\]
The determinant lemma gives
\[
\begin{array}{ll}
\det C_1=\det C\,(1-A/q),
&\det C_0=\det C\,(1+A/(1-q)),\\[1mm]
\det(I-C_1)=\det(I-C)\,(1+B/q),
&\det(I-C_0)=\det(I-C)\,(1-B/(1-q)).
\end{array}                                               \tag{11}
\]
Define the exact barrier loss
\[
\mathfrak D(C,b,q)
:=\ell(C)-q\ell(C_1)-(1-q)\ell(C_0).                    \tag{12}
\]
Then
\[
\boxed{
\begin{aligned}
\mathfrak D={}&-q\log(1-A/q)
 -(1-q)\log(1+A/(1-q))\\
&-q\log(1+B/q)
 -(1-q)\log(1-B/(1-q)).
\end{aligned}
}                                                         \tag{13}
\]
Since \(\ell\) is concave, \(\mathfrak D\ge0\), and (8) becomes
\[
\boxed{
q\mathcal F(C_1)+(1-q)\mathcal F(C_0)-\mathcal F(C)
\ge-\mathfrak D(C,b,q).
}                                                         \tag{14}
\]

Assume now the fixed gap
\[
\delta I\preceq\widehat C\preceq(1-\delta)I.
\]
Schur complements of \(\widehat C-\delta I\) and
\((1-\delta)I-\widehat C\) give
\[
0\le A\le q-\delta,
\qquad
0\le B\le1-q-\delta.                                    \tag{15}
\]
For \(0\le x\le Q-\delta\),
\[
-Q\log(1-x/Q)-x\le\frac{x^2}{2(Q-x)}\le\frac{x^2}{2\delta},
\]
while
\[
x-Q\log(1+x/Q)\le\frac{x^2}{2Q}\le\frac{x^2}{2\delta}.
\]
Applying these four inequalities to (13) yields
\[
\boxed{
0\le\mathfrak D(C,b,q)
\le\frac{A^2+B^2}{\delta}
\le\frac{2\|b\|^4}{\delta^3}.
}                                                         \tag{16}
\]
This is a local, coupling-sensitive defect.  The block theorem below is usually better when many
centers are revealed.

---

## 5. PROVED: arbitrary noncommuting reveal block

Let \(\mathscr A\subset\mathscr V\) be exterior reveal sigma-fields and let
\(C_{P\mid\mathscr A}\), \(C_{P\mid\mathscr V}\) be the exact conditional kernels on a fixed
cross pair \(P\).  Iterate (8), retaining every actual conditional probability.

The fixed spectral gap is genuinely preserved.  If
\(\delta I\preceq\widehat C\preceq(1-\delta)I\), then the Schur complement of
\(\widehat C-\delta I\) gives
\[
C_1-\delta I
\succeq C-\delta I-\frac{bb^*}{q-\delta}\succeq0,
\]
while \(C_1\preceq C\preceq(1-\delta)I\).  Likewise, the Schur complement of
\((1-\delta)I-\widehat C\) gives
\[
(1-\delta)I-C_0
\succeq (1-\delta)I-C-\frac{bb^*}{1-\delta-q}\succeq0,
\]
and \(C_0\succeq C\succeq\delta I\).  Thus every successive actual conditional pair kernel
remains in the same compact gap domain.

### Theorem 5.1 — PROVED

\[
\boxed{
\mathbb E\mathcal F(C_{P\mid\mathscr V})
-
\mathbb E\mathcal F(C_{P\mid\mathscr A})
\ge
\mathbb E\ell(C_{P\mid\mathscr V})
-
\mathbb E\ell(C_{P\mid\mathscr A}).
}                                                         \tag{17}
\]
Equivalently, the process \(\mathcal B(C_{P\mid\mathscr F})\) is a submartingale under actual
reveals.

If every conditional kernel has gap \(\delta\), then
\[
2\log[\delta(1-\delta)]
\le\ell(C)\le2\log(1/4),                                 \tag{18}
\]
so
\[
\boxed{
\mathbb E\mathcal F(C_{P\mid\mathscr V})
\ge
\mathbb E\mathcal F(C_{P\mid\mathscr A})
-\bigl\{\mathbb E\ell(C_{P\mid\mathscr A})
        -2\log[\delta(1-\delta)]\bigr\}.
}                                                         \tag{19}
\]
In particular,
\[
\boxed{
\mathbb E\Delta\mathcal F
\ge-2\log\frac1{4\delta(1-\delta)}.
}                                                         \tag{20}
\]
The right side does not depend on the number of revealed centers or leaves.  For an increasing
countable reveal, the pair-kernel martingale converges and both \(\mathcal F\) and
\(\mathcal B\) are bounded and continuous on the compact gap domain; dominated convergence
therefore passes the finite theorem to the limit.

### Exact reverse-KL interpretation — PROVED

Let \(R\) denote the newly revealed block, and let
\(E_{11}=\{Y_i=Y_j=1\}\), \(E_{00}=\{Y_i=Y_j=0\}\) for the retained pair.  Conditional on
the old sigma-field \(\mathscr A\), write \(P_R\) for the actual law of \(R\), and
\(P_R^{11},P_R^{00}\) for its laws additionally conditioned on the indicated pair event.  The
strict gap makes all these finite-word laws mutually absolutely continuous.  Bayes' formula gives
\[
\log\frac{p_e(\mathscr A,R)}{p_e(\mathscr A)}
=\log\frac{dP_R^e}{dP_R}(R),
\qquad e\in\{11,00\}.
\]
Averaging with respect to the **unconditioned actual** law \(P_R\) yields
\[
\boxed{
\mathbb E[\ell(C_{P\mid\mathscr V})-\ell(C_{P\mid\mathscr A})]
=-\mathbb E\left[
D(P_R\|P_R^{11})+D(P_R\|P_R^{00})
\right].
}                                                         \tag{21}
\]
Consequently the exact compensated block theorem can also be written
\[
\boxed{
\mathbb E\Delta\mathcal F
\ge-\mathbb E\left[
D(P_R\|P_R^{11})+D(P_R\|P_R^{00})
\right].
}                                                         \tag{22}
\]
For one revealed Bernoulli site, the two divergences in (21) are exactly
\(D_{\rm KL}(\operatorname{Bern}(q)\|\operatorname{Bern}(q-A))\) and
\(D_{\rm KL}(\operatorname{Bern}(q)\|\operatorname{Bern}(q+B))\), reproducing (13).
This identity exposes the remaining payment as a pair-event reverse-information cost, rather than
an unnamed error term.

### Tool interface

**Input.** A retained cross pair \(P\); nested actual reveal sigma-fields
\(\mathscr A\subset\mathscr V\); the true conditional DPP kernels; and a proved common gap
\(\delta I\preceq K_{\mid\mathscr F}\preceq(1-\delta)I\).

**Hypotheses.** Unobserved sites are marginalized, all configurations remain in the actual DPP law,
and each reveal uses its moving conditional probability.  No commutation or independence of
conditioned centers is assumed.

**Output.** Use (17) when the endpoint barriers can be estimated, (22) when reverse-information
bounds are available, (19)--(20) for a uniform fixed-pair cap, and (24)--(25) for a finite core.
The tool applies without change to leaf additions, center additions, mixed reveal orders, and
increasing countable blocks.

**Quantitative return to Shannon entropy.** For the accepted one-pair core, substitute (47) into
the S72 inequality to obtain (48); the paid numerical residual is recorded in (49).

### Why noncommutativity is paid

Successive full center-block updates may be noncommuting rank-one matrices.  The proof never
reorders them.  At each step, the current full conditional kernel is used, its principal pair
kernel receives the corresponding restricted rank-one update, and (8) is applied with the current
actual \(q\).  The scalar endpoint in (17) is the telescoped log-determinant barrier.  Thus no
matrix word is silently commuted or discarded.

### Multi-pair form

For a fixed core with center set \(C\) and leaf set \(E\), define
\[
\Lambda_I(\mathbf C)
=
\sum_{p\in C}\sum_{i\in E}
\left\{
\log\det \mathbf C_{\{p,i\}}
+
\log\det(I_2-\mathbf C_{\{p,i\}})
\right\}.                                                \tag{23}
\]
Summing (17) over all cross pairs gives
\[
\boxed{
\mathbb E\Delta\Chi\ge\mathbb E\Delta\Lambda_I.
}                                                         \tag{24}
\]
The worst uniform payment is
\[
2|C||E|\log\frac1{4\delta(1-\delta)}.                   \tag{25}
\]
Hence the cost is linear in the number of pairs.  For one retained leaf and \(k\) retained
centers it is \(O(k)\).  For the entropy interface used below there is one retained pair and all
additional centers are exterior reveals, so the payment is \(O(1)\), independent of their number.
For a balanced growing interval core, (25) is \(O(m^2)\); that collective gap remains open.

---

## 6. Half-density star payment

For a selected one-center star pair, after conditioning on the other old leaves,
\[
C_\star(\beta)=
\begin{pmatrix}
d&z\\ \bar z&\beta
\end{pmatrix},
\qquad
s=|z|^2,
\qquad
\mathbb E\beta=d.                                        \tag{26}
\]
Write \(u=1-d\).  Concavity of \(\ell\) gives
\[
\mathbb E\ell(C_\star)
\le
\ell\!\begin{pmatrix}d&z\\\bar z&d\end{pmatrix}
=
\log(d^2-s)+\log(u^2-s).                                 \tag{27}
\]
Combining (19) and (27), adding any number of missing centers costs at most
\[
\boxed{
D_{\star,0}(d,s,\delta)
=
\log\frac{(d^2-s)(u^2-s)}{\delta^2(1-\delta)^2}.
}                                                         \tag{28}
\]

There is a general variance improvement.  If the old leaves have weights \(w_\ell\), then
\[
\operatorname{Var}\beta
=\frac{\sum_{\ell\ne i}w_\ell^2}{du}.                    \tag{29}
\]
For
\[
g(\beta)=\ell(C_\star(\beta)),
\]
\[
g''(\beta)
=-\frac{d^2}{(d\beta-s)^2}
 -\frac{u^2}{(u(1-\beta)-s)^2}
\le-\frac{2}{(1-\delta)^2}.                              \tag{30}
\]
Therefore
\[
\boxed{
D_\star
\le
\log\frac{(d^2-s)(u^2-s)}{\delta^2(1-\delta)^2}
-
\frac{\sum_{\ell\ne i}w_\ell^2}
     {du(1-\delta)^2}.
}                                                         \tag{31}
\]
For fixed \(s,\delta\), the right side is maximized at \(d=1/2\).  Indeed, with
\(x=du\),
\[
(d^2-s)(u^2-s)=(x+s)^2-s,
\]
and both terms on the right of (31) increase with \(x\le1/4\).  Therefore, for every compact
legal bias interval \(J\), with
\[
\delta=\min_{a\in J}\min\{a,1-a-c\}>0,
\]
the midpoint value is a uniform upper bound for this missing-center payment throughout \(J\)
(the selected sine weight and all old-leaf weights depend on \(c\), not on \(a\)).

### Midpoint all-moment tool

At \(d=u=1/2\), put
\[
A_0=\frac14-s,
\qquad
\beta=\frac12+t.
\]
The old leaf marginal is an independent Rademacher family and
\[
t=2\sum_{\ell\ne i}\varepsilon_\ell w_\ell,
\qquad
\varepsilon_\ell\in\{-1,1\}.
\]
Then
\[
\ell(C_\star)=2\log A_0+
\log\left(1-\frac{t^2}{4A_0^2}\right).                 \tag{32}
\]
If \(T=\sum_{\ell\ne i}w_\ell<A_0\), the entire support satisfies
\(|t|/(2A_0)\le T/A_0<1\), and
\[
\boxed{
\mathbb E\ell(C_\star)
=2\log A_0-
\sum_{n\ge1}\frac{\mathbb E t^{2n}}
 {n(4A_0^2)^n}.
}                                                         \tag{33}
\]
For the infinite sine star,
\[
T=\frac{c^2}{4}-s,
\qquad
A_0-T=\frac{1-c^2}{4}>0,
\]
so the series-domain hypothesis is automatic for every \(0<c<1\), including the entire target
range \(c\in(37/40,1)\).  Every correction in (33) is nonnegative.  Truncating after \(N\)
terms gives a rigorous upper bound on the completion payment.  If
\[
R=(T/A_0)^2,
\]
the omitted correction satisfies
\[
0\le
\sum_{n>N}\frac{\mathbb E t^{2n}}{n(4A_0^2)^n}
\le
\frac{\mathbb E t^{2N+2}}
 {(N+1)(4A_0^2)^{N+1}(1-R)}.                             \tag{34}
\]
The moments can be generated without word enumeration from
\[
\mathbb E e^{zt}=\prod_{\ell\ne i}\cosh(2w_\ell z).
\]
Equivalently, if
\[
\log\mathbb E e^{zt}=\sum_{n\ge1}q_nz^{2n},
\qquad
\mathbb E e^{zt}=\sum_{n\ge0}c_nz^{2n},
\]
then
\[
nc_n=\sum_{r=1}^n r q_r c_{n-r},
\qquad
\mathbb E t^{2n}=(2n)!c_n.                              \tag{35}
\]
For the infinite half-density sine star, every required power sum is explicit:
\[
\sum_{\ell\ \mathrm{odd}}w_\ell^{2n}
=
-\frac{B_{4n}(2^{4n}-1)}{(4n)!}\,c^{4n},               \tag{36}
\]
with the selected weight removed.

For the nearest pair at \(c=19/20\), \(\delta=1/50\), a 20-moment interval computation plus
the 21st-moment tail gives the certified floor-envelope
\[
\boxed{
D_{\star,\infty}^{\rm floor}
\in
[3.7456951075302371,\ 3.7456952529240384].
}                                                         \tag{37}
\]
This is an upper envelope obtained by replacing the final barrier by its spectral-gap floor; it
is not claimed to equal the actual full-line barrier loss.  The reproducible source is
`s78_barrier_moments_interval.py`; its saved actual output is
`S78_BARRIER_MOMENT_INTERVAL.txt`, ending in `PASS_BARRIER_MOMENT_INTERVAL`.

---

## 7. DISPROVED: zero-payment center addition

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
Take the retained pair
\[
P=\{0,-3\},
\]
the old observed one-center star
\[
A_{\rm old}=\{0,-3,1,3\},
\]
and add the same-parity center
\[
r=-4.
\]
All matrices are true finite principal compressions of the half-density sine kernel; sites not
listed are marginalized.

Eighty-digit outward-rounded interval enumeration of every actual word gives
\[
\mathbb E f_{0,-3}(G_{A_{\rm old}})
\in
[0.00039676155509470168359,
 0.00039676155509470168360],
\]
\[
\mathbb E f_{0,-3}(G_{A_{\rm old}\cup\{r\}})
\in
[-0.00153636915888833847572,
 -0.00153636915888833847571],
\]
and hence
\[
\boxed{
\mathbb E\Delta f_{0,-3}
\in
[-0.00193313071398304015931,
 -0.00193313071398304015930]<0.
}                                                         \tag{38}
\]
Thus center addition cannot be assigned a favorable sign, even unconditionally and even at the
midpoint.

For the same example, the exact conditional-pair barrier drift is
\[
\mathbb E\Delta\ell
\in
[-0.158200253002973652107,
 -0.158200253002973652106],
\]
so the compensated drift satisfies
\[
\boxed{
\mathbb E\Delta(\mathcal F-\ell)
\in
[0.1562671222889906119470,
 0.1562671222889906119471]>0.
}                                                         \tag{39}
\]
This simultaneously falsifies the raw sign and checks the direction of the compensator.  The
reproducible source is `s78_center_add_barrier_certificate.py`; its saved 80-digit interval output
is `S78_CENTER_BARRIER_CERTIFICATE.txt`, ending in
`PASS_CENTER_ADD_NEGATIVE_AND_BARRIER_COMPENSATED`.

A distinct certified leaf-addition obstruction uses the same midpoint parameters, centers
\(\{0,10\}\), core leaf \(7\), old observed leaf \(-3\), and newly revealed leaf \(-1\):
\[
I=\{0,10,7\},\qquad
\Chi=f_{0,7}+f_{10,7}.
\]
Full actual-word interval enumeration gives
\[
\boxed{
\mathbb E\Delta\Chi
\in[-4.912434017602194,-4.912434017602193]\times10^{-7}<0.
}
\tag{40}
\]
The corresponding executable returned `PASS_INTERVAL_K2_NEGATIVE_REVEAL`.  Thus both
opposite-parity leaf addition and same-parity center addition require compensation; neither local
failure is a counterexample to Shannon entropy concavity.

---

## 8. First interacting-center sine defect and summability

Let \(p,q\) be same-parity centers, \(i\) a retained opposite-parity leaf, and condition on old
leaves \(B\setminus\{i\}\).  Put
\[
\begin{aligned}
\alpha&=d+\sum_\ell\xi_\ell|b_{p\ell}|^2,\\
\beta&=d+\sum_\ell\xi_\ell|b_{q\ell}|^2,\\
\tau&=\sum_\ell\xi_\ell b_{p\ell}\overline{b_{q\ell}},
\end{aligned}
\qquad
\xi_\ell=\frac{1-Y_\ell}{1-d}-\frac{Y_\ell}{d}.
\]
Then
\[
C=\begin{pmatrix}\alpha&b_{pi}\\\overline{b_{pi}}&d\end{pmatrix},
\qquad
b=\binom{\tau}{\overline{b_{qi}}},
\qquad
q_{\rm reveal}=\beta.                                   \tag{41}
\]
The exact \(k=2\) lower bound is (14) with the two resolvent scalars in (10).  A simpler explicit
envelope follows from (16):
\[
\mathbb E\Delta\mathcal F
\ge
-\frac{2}{\delta^3}\,
\mathbb E(|\tau|^2+|b_{qi}|^2)^2.                       \tag{42}
\]
Let
\[
S_2=\sum_\ell(b_{p\ell}b_{q\ell})^2,
\qquad
S_4=\sum_\ell(b_{p\ell}b_{q\ell})^4,
\]
\[
m_2=\frac1{d(1-d)},
\qquad
m_4=d^{-3}+(1-d)^{-3}.
\]
The actual independent leaf marginal gives
\[
\mathbb E\tau^2=m_2S_2,
\]
\[
\mathbb E\tau^4
=3m_2^2S_2^2+(m_4-3m_2^2)S_4.                           \tag{43}
\]
Hence, with \(M_4=\max\{m_4,3m_2^2\}\),
\[
\boxed{
\mathbb E\mathfrak D
\le
\frac{2}{\delta^3}
\left[
|b_{qi}|^4+2|b_{qi}|^2m_2S_2+M_4S_2^2
\right].
}                                                         \tag{44}
\]
For center separation \(R=p-q\ne0\), the true half-density sine overlap is
\[
S_2\le\frac{c^4}{2\pi^2R^2}.                            \tag{45}
\]
Also \(|b_{qi}|^2=O(|q-i|^{-2})\), so (44) is \(O(R^{-4})\) away from the retained pair and is
summable.

For example, with \(p=0\), \(i=1\), summing the first-interaction envelope over all even
\(q\ne0\) uses
\[
\sum_{q\in2\mathbb Z\setminus\{0\}}\frac1{q^2(q-1)^2}
=\frac{\pi^2}{3}-3,
\]
and gives the finite bracket
\[
\boxed{
\begin{aligned}
\sum_q\mathbb E\|b^{(q)}\|^4
\le{}&c^4\left(\frac1{48}-\frac1{\pi^4}\right)\\
&+\frac{m_2c^6}{\pi^4}\left(\frac{\pi^2}{3}-3\right)
+\frac{M_4c^8}{2880}.
\end{aligned}
}                                                         \tag{46}
\]
Equation (46) is a summable **first-interaction** diagnostic.  It is not used to add defects after
previous centers have changed the kernel.  The valid all-center statement is the block barrier
(17)--(22).

---

## 9. Quantitative interface to original Shannon entropy

Use the accepted half-density benchmark core and halos
\[
I=\{1,2\},
\qquad
A_L=[1-L,2+L],
\qquad
A_L^\star=\{2\}\cup(A_L\cap\{\text{odd sites}\}).
\]
Let \(L_L(a)\) be the accepted one-center star lower bound for the retained pair.  Apply (17) to
reveal every missing even center.  With \(D_{\star,L}\) denoting the barrier payment from
(19),
\[
\mathbb E f_{12}(G_{A_L})\ge L_L(a)-D_{\star,L}.         \tag{47}
\]
Since \(V_{2,L}=\frac12\mathbb E f_{12}(G_{A_L})\), the accepted original-Shannon interface
becomes
\[
\boxed{
\begin{aligned}
h''(a)\le{}&-\frac1{50}-L_L(a)+D_{\star,L}\\
&+2C_{\log}\widehat\tau(2)
 +2\Gamma_\Chi\eta_\delta\widehat\tau(L+1).
\end{aligned}
}                                                         \tag{48}
\]
This replaces only the genuine missing-parity completion cost.  The full-score core/pair term and
the far-observation term remain separate.

At
\[
c=\frac{19}{20},
\qquad
\delta=\frac1{50},
\qquad
 d=\frac12,
\]
the certified 20-moment upper envelope in (37) is
\[
D_{\star,\infty}<3.745695253.
\]
The unchanged core/pair term is
\[
2C_{\log}\widehat\tau(2)
=486.9287385765045\ldots.
\]
Therefore the new asymptotic residual payment is
\[
\boxed{
D_{\star,\infty}
+2C_{\log}\widehat\tau(2)
<490.674433829429.
}                                                         \tag{49}
\]
The previous certified payment was
\[
107974.9489647355\ldots,
\]
so the improvement factor is greater than
\[
\boxed{220.0541571.}                                     \tag{50}
\]
Using only the certified star lower bound \(0.26275\), the right side of (48), after the far tail
vanishes, is still bounded above only by approximately
\[
490.391684>0.
\]
Thus (48) is a major structural reduction but not a concavity certificate.  The interval
arithmetic is reproduced by `s78_updated_interface_interval.py`; the saved output
`S78_UPDATED_INTERFACE_INTERVAL.txt` ends in `PASS_UPDATED_INTERFACE_INTERVAL`.

---

## 10. Falsification tests for future strengthenings

Any proposed replacement must pass all of the following.

1. **Leaf-addition obstruction:** it must permit the earlier certified negative \(k=2\) leaf
   reveal drift.
2. **Center-addition obstruction:** it must permit (38).
3. **Actual-weight barycenter:** every step must use
   \(qC_1+(1-q)C_0=C\) with the moving actual \(q\).
4. **Rank-one Hessian identity:** differentiating the proposed compensated potential along
   \(C+tbb^*\) must agree with (4)--(5).
5. **Reverse-KL check:** the accumulated barrier loss must equal the two reverse divergences in
   (21); a proposed smaller payment must identify which information inequality supplies it.
6. **Degenerate coupling:** if \(b=0\), then \(\mathfrak D=0\) and the reveal drift is exactly
   zero.
7. **Noncommuting order:** the proof must remain valid when successive full center updates do not
   commute.  A product or moment expansion that reorders them is invalid unless the resulting
   commutators are explicitly paid.

---

## 11. Exact remaining payment

1. The full-score core/pair truncation term remains
   \(486.9287385765\ldots\) at the benchmark.
2. The spectral-floor barrier envelope is still about \(3.7457\), larger than the available
   \(0.26275\) one-pair star lower bound.
3. The pair-barrier sum is \(O(k\ell)\) for a balanced growing core.  A collective
   \(\Chi\)-barrier with \(O(k+\ell)\) range, or an external block-cut cancellation, remains open.
4. No theorem here establishes the entire \(c\in(37/40,1)\) Shannon concavity target, arbitrary
   density, or all legal \(a\).
5. The center-addition and leaf-addition obstructions concern local reveal potentials only; they
   are not counterexamples to Shannon entropy concavity.

No repository edit, shared-state mutation, PR action, or merge was performed.
