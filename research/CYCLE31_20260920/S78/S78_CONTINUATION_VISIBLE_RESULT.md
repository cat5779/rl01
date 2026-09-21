# S78 continuation result

I replaced the previous coarse arbitrary-Hessian completion estimate with an **exact log-determinant compensation theorem**. The accepted one-center theorem, exact two-output averaging identity, true-compression model, and original Shannon interface remain unchanged. citeturn753804view0

## PROVED

For a strict conditional pair kernel

\[
C=\begin{pmatrix}\alpha&z\\ \bar z&\beta\end{pmatrix},
\qquad
\ell(C)=\log\det C+\log\det(I-C),
\]

define

\[
\mathcal B(C)=\mathcal F(C)-\ell(C),
\]

where \(\mathcal F\) is the exact actual-weight average of the pair score.

Along every rank-one line \(C(t)=C+t\,vv^*\),

\[
\boxed{
\frac{d^2}{dt^2}\mathcal B(C(t))
=
\sum_{y\in\{0,1\}^2}
\frac{2|h-a_yz(t)|^2}{p_y(t)}
+a_{10}(t)^2+a_{01}(t)^2
\ge0,
}
\]

with \(h=v_1\overline{v_2}\) and

\[
a_y=v^*(C-\operatorname{diag}(1-y))^{-1}v.
\]

This is an exact sum-of-squares identity. It is not the previous \(M_2(\delta)\) semiconvexity envelope.

For an actual reveal with moving conditional probability \(q\),

\[
C_1=C-\frac{bb^*}{q},
\qquad
C_0=C+\frac{bb^*}{1-q},
\qquad
qC_1+(1-q)C_0=C,
\]

rank-one convexity gives

\[
\boxed{
q\mathcal F(C_1)+(1-q)\mathcal F(C_0)-\mathcal F(C)
\ge
q\ell(C_1)+(1-q)\ell(C_0)-\ell(C).
}
\]

The inequality uses all actual configurations and does not replace \(q\) by a marginal probability.

### Arbitrary noncommuting reveal blocks

For nested actual reveal fields \(\mathscr A\subset\mathscr V\),

\[
\boxed{
\mathbb E\mathcal F(C_{P\mid\mathscr V})
-
\mathbb E\mathcal F(C_{P\mid\mathscr A})
\ge
\mathbb E\ell(C_{P\mid\mathscr V})
-
\mathbb E\ell(C_{P\mid\mathscr A}).
}
\]

Successive rank-one updates are used in their actual order; no matrix words are commuted.

The accumulated barrier loss has the exact information-theoretic representation

\[
\boxed{
\begin{aligned}
&\mathbb E\!\left[
\ell(C_{P\mid\mathscr V})-\ell(C_{P\mid\mathscr A})
\right]\\
&\quad=
-\mathbb E\!\left[
D(P_R\Vert P_R^{11})
+
D(P_R\Vert P_R^{00})
\right],
\end{aligned}
}
\]

where \(P_R\) is the actual newly revealed block law and \(P_R^{11},P_R^{00}\) are that law conditioned on the retained pair having outputs \(11\) and \(00\). Thus the defect is an identified reverse-information payment, not an unspecified remainder.

If all conditional kernels retain the spectral gap

\[
\delta I\preceq C\preceq(1-\delta)I,
\]

then, for a fixed retained pair,

\[
\boxed{
\mathbb E\Delta\mathcal F
\ge
-2\log\frac1{4\delta(1-\delta)}.
}
\]

This payment is independent of the number of additional centers or leaves. The gap preservation itself follows from the appropriate Schur complements and is included in the proof.

For a core with \(k\) centers and \(\ell\) opposite-parity leaves, summing the pair theorem costs at worst

\[
2k\ell\log\frac1{4\delta(1-\delta)}.
\]

Thus the tool is \(O(1)\) for the one-pair entropy interface, \(O(k)\) for one retained leaf and \(k\) retained centers, and presently \(O(k\ell)\) for a balanced growing core.

### Half-density star boundary payment

For a selected star pair of weight \(s=|z_i|^2\),

\[
\boxed{
D_\star
\le
\log\frac{(d^2-s)((1-d)^2-s)}
{\delta^2(1-\delta)^2}
-
\frac{\sum_{\ell\ne i}w_\ell^2}
{d(1-d)(1-\delta)^2}.
}
\]

For fixed \(c,s,\delta\), this upper bound is maximized at \(d=1/2\). Consequently it is uniform over every compact legal bias interval \(J\) having the stated gap \(\delta\).

At \(d=1/2\), the exact initial barrier has the convergent expansion

\[
\mathbb E\ell(C_\star)
=
2\log A_0
-
\sum_{n\ge1}
\frac{\mathbb E t^{2n}}{n(4A_0^2)^n},
\qquad
A_0=\frac14-s.
\]

For the infinite sine star,

\[
T=\sum_{\ell\ne i}w_\ell=\frac{c^2}{4}-s,
\qquad
A_0-T=\frac{1-c^2}{4}>0,
\]

so the full actual support lies in the convergence domain for every \(0<c<1\), including the complete target range \(c\in(37/40,1)\).

At

\[
c=\frac{19}{20},
\qquad
\delta=\frac1{50},
\]

the certified 20-moment calculation and 21st-moment tail give

\[
\boxed{
D_{\star,\infty}^{\mathrm{floor}}
\in
[3.7456951075302371,\,
 3.7456952529240384].
}
\]

### First interacting-center spatial defect

For same-parity centers \(p,q\), retained leaf \(i\), and center separation \(R=p-q\),

\[
\mathbb E\Delta\mathcal F
\ge
-\frac{2}{\delta^3}
\mathbb E\bigl(|\tau|^2+|b_{qi}|^2\bigr)^2,
\]

where \(\tau\) is the actual off-diagonal center-center correlation created by the old leaves.

The exact leaf moments give

\[
\mathbb E\tau^2=m_2S_2,
\]

\[
\mathbb E\tau^4
=
3m_2^2S_2^2+
(m_4-3m_2^2)S_4,
\]

and the true sine overlap satisfies

\[
S_2\le\frac{c^4}{2\pi^2R^2}.
\]

Therefore the first-interaction fourth-moment defect is \(O(R^{-4})\) and spatially summable. This summability is not used to make an invalid pairwise-additivity claim after other noncommuting centers have already been conditioned; the arbitrary-block barrier theorem is the valid many-center mechanism.

## DISPROVED

Raw zero-payment monotonicity fails for both operations.

### Same-parity center addition

At

\[
\rho=\frac12,\qquad
c=\frac{19}{20},\qquad
a=\frac1{40},\qquad d=\frac12,
\]

take retained pair \(P=\{0,-3\}\), old one-center star

\[
A_{\rm old}=\{0,-3,1,3\},
\]

and add center \(r=-4\). Full 80-digit interval enumeration of all actual words gives

\[
\boxed{
\mathbb E\Delta f_{0,-3}
\in
[-0.00193313071398304015931,\,
 -0.00193313071398304015930]
<0.
}
\]

For the same example,

\[
\mathbb E\Delta\ell
\approx-0.158200253002973652106,
\]

and hence

\[
\boxed{
\mathbb E\Delta(\mathcal F-\ell)
\in
[0.1562671222889906119470,\,
 0.1562671222889906119471]
>0.
}
\]

The raw sign fails, while the compensated theorem succeeds strictly.

### Opposite-parity leaf addition with two centers

For centers \(\{0,10\}\), core leaf \(7\), old observed leaf \(-3\), and revealed leaf \(-1\),

\[
\Chi=f_{0,7}+f_{10,7},
\]

and the certified actual-word drift is

\[
\boxed{
\mathbb E\Delta\Chi
\in
[-4.912434017602194,\,
 -4.912434017602193]\times10^{-7}
<0.
}
\]

Neither obstruction is a counterexample to Shannon entropy concavity.

## Quantitative Shannon interface

For the accepted one-pair core \(I=\{1,2\}\), the new completion theorem gives

\[
\mathbb E f_{12}(G_{A_L})
\ge
L_L(a)-D_{\star,L}.
\]

Substitution into the original Shannon comparison yields

\[
\boxed{
\begin{aligned}
h''(a)\le{}&
-\frac1{50}-L_L(a)+D_{\star,L}\\
&+2C_{\log}\widehat\tau(2)
+2\Gamma_\Chi\eta_\delta\widehat\tau(L+1).
\end{aligned}
}
\]

This leaves the full-score core/pair and far-observation terms separate, as required.

At \(c=19/20,\delta=1/50\),

\[
D_{\star,\infty}<3.745695253,
\]

while the unchanged full-score core/pair payment is

\[
486.9287385765045\ldots.
\]

The resulting asymptotic residual is

\[
\boxed{
490.674433829429\ldots
}
\]

instead of

\[
107974.9489647355\ldots.
\]

The certified improvement factor exceeds

\[
\boxed{220.0541571}.
\]

The packet identifies the original nearby missing-parity and core-truncation costs as the principal obstruction to the star-to-full-halo interface; the new theorem structurally removes almost all of the former but does not affect the latter. citeturn753804view0

## INCOMPLETE

The full entropy-rate concavity theorem is still open.

The precise remaining payments are:

- \(486.9287385765\ldots\) from the full-score core/pair truncation;
- approximately \(3.7457\) from the present spectral-floor barrier envelope;
- \(O(k\ell)\) worst-case accumulation when the retained core itself grows with both parities.

Even after the far tail vanishes and the certified star lower bound \(0.26275\) is subtracted, the present upper bound remains approximately

\[
490.391684>0.
\]

A collective \(\Chi\)-barrier with \(O(k+\ell)\) rather than \(O(k\ell)\) range, a substantially sharper estimate of the terminal reverse-KL payment, or the separate block-cut cancellation is still required.

## Files and execution status

- :chatgpt-content-reference{index="3"}
- :chatgpt-content-reference{index="4"}
- :chatgpt-content-reference{index="5"}
- :chatgpt-content-reference{index="6"}
- :chatgpt-content-reference{index="7"}
- :chatgpt-content-reference{index="8"}
- :chatgpt-content-reference{index="9"}
- :chatgpt-content-reference{index="10"}
- :chatgpt-content-reference{index="11"}
- :chatgpt-content-reference{index="12"}

All four certificate programs were rerun successfully, matched their saved outputs, and ended in their stated `PASS_...` conditions. No repository edit, shared-state mutation, PR action, or merge was performed.
