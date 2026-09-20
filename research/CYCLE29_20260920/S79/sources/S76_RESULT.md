# S76 result

I obtained an **all-size, all-contrast midpoint compensation theorem**. It applies to every \(m\ge 1\), every \(0<c<1\), and every Hamming-layer doubly stochastic channel \(W\), hence in particular to the actual consecutive-Fourier exterior channels \(W_{U_m}\). It retains the acceleration exactly and isolates a strictly smaller remaining obligation.

The packet’s exact exterior-channel law, determinant posterior, compensated-curvature identity, and zero midpoint Fisher loss are the premises used here. citeturn862724view0turn192741view3

## PROVED

Put
\[
k=c^2,\qquad
r=\frac{1-k}{4},\qquad
s=\frac{1+k}{4},\qquad
L=\log\frac{s}{r}.
\]

Besides the observable
\[
X=A-m=|Y|+|Z|-m=|Y|+|T|-m,
\]
introduce the hidden equal-pair count
\[
D=\#\{i:Y_i=Z_i\}=m-A+2B.
\]

At the midpoint \(a=(1-c)/2\), direct differentiation of the four pair atoms gives the exact acceleration split
\[
\boxed{
\mathcal A
=\frac{X^2-D}{r^2}
+\frac{D-2mr}{rs}.}
\]

Since the score \(S=X/r\) is output-measurable, the Fisher-loss term is zero, and therefore
\[
G''=C_X+C_D,
\]
where
\[
C_X=\frac1{r^2}\mathbb E[(X^2-D)R],
\qquad
C_D=\frac1{rs}\mathbb E[(D-2mr)R].
\]

The two pieces have different meanings:

* \(C_X\) is the conditional-Rademacher, or second-Krawtchouk, response.
* \(C_D\) changes the frequency of equal pairs.

The second piece has a definite sign.

Define the fair-spin output density
\[
L_k(y,t)=\sum_zW(z,t)\prod_{i=1}^m(1-k\sigma_i\tau_i),
\]
and the midpoint output mutual information
\[
I_W(k)=4^{-m}\sum_{y,t}L_k(y,t)\log L_k(y,t).
\]

For the Boolean number operator
\[
N_yf=\frac12\sum_i\bigl(f(y,t)-f(y^{(i)},t)\bigr),
\]
Walsh expansion gives
\[
k\,\partial_kL_k=N_yL_k.
\]

Consequently,
\[
\mathcal E_W(k):=kI_W'(k)
=\frac14\sum_i\mathbb E_y
J\!\left(P_y^W,P_{y^{(i)}}^W\right),
\]
where \(J(P,Q)=D(P\|Q)+D(Q\|P)\) is Jeffreys divergence. Log-sum applied in both directions shows that every edge Jeffreys divergence contracts through \(W\). For the unprocessed input, each adjacent edge has divergence \(2kL\), so
\[
0\le \mathcal E_W(k)\le
\mathcal E_{\rm id}(k)=\frac{mkL}{2}.
\]

Let
\[
\Delta\mathcal E
=\mathcal E_{\rm id}-\mathcal E_W,
\qquad
\eta_J=\frac{2\Delta\mathcal E}{mkL}\in[0,1].
\]

Writing \(\lambda=P(Y_i=Z_i)=2r=(1-k)/2\), the first derivative identity for the entropy gain gives
\[
C_D=4\partial_\lambda G_0.
\]
Since \(G_0=I_{\rm id}-I_W\) and \(\partial_\lambda=-2\partial_k\),
\[
\boxed{
C_D
=-\frac8k\Delta\mathcal E
=-4mL\,\eta_J
\le0.}
\]

Thus the equal-pair-rate acceleration is **fully paid** by the loss of adjacent-mask Jeffreys divergence through the exterior channel.

### Explicit posterior-geometric payment

For an adjacent pair \(y,y^{(i)}\), let
\[
M_{i,y}=\frac12(P_y+P_{y^{(i)}})
\]
and set
\[
\zeta_i=\sigma_i\tau_i,\qquad
m_{i,y}(t)=\mathbb E_{M_{i,y}}[\zeta_i\mid T=t].
\]

A direct binary calculation yields
\[
\eta_J\ge \overline V_W(k),
\]
where
\[
\boxed{
\overline V_W(k)=
\frac1m\sum_{i=1}^m
\mathbb E_y\mathbb E_{M_{i,y}^W}
\operatorname{Var}_{M_{i,y}}(\zeta_i\mid T).}
\]

For the exterior channel, this is explicitly determined by
\[
W_U(z,t)=|\det U_{z,t}|^2.
\]
Hence it is a checkable consecutive-Fourier/Hilbert geometry quantity, rather than a generic operator-norm envelope. In particular,
\[
C_D\le-4mL\,\overline V_W(k).
\]

### Exact reduced obligation

Let
\[
\delta_O=\mathbb E[D\mid O]=-X+2\mu_O.
\]
Because \(D=-X+2B\),
\[
\operatorname{Var}(D\mid O)=4\kappa_{2,O}.
\]

Using \(\gamma=-2L\) and absorbing the output-measurable part of \(\gamma B\) into the partition function gives
\[
\operatorname{Cov}(D,R\mid O)
=-L\operatorname{Var}(D\mid O).
\]
Therefore
\[
\boxed{
C_X=
\frac1{r^2}\mathbb E\!\left[
(X^2-\delta_O)\psi_O+4L\kappa_{2,O}
\right].}
\]

Combining the two sectors,
\[
\boxed{
G''=
\frac1{r^2}\mathbb E\!\left[
(X^2-\delta_O)\psi_O+4L\kappa_{2,O}
\right]
-4mL\eta_J.}
\]

The total midpoint curvature is consequently
\[
\boxed{
H_{\rm out}''
=C_X-\frac{2m}{r}+4mL(1-\eta_J).}
\]

Thus finite-volume midpoint concavity is reduced to the genuinely narrower inequality
\[
\boxed{
C_X\le
\frac{2m}{r}-4mL(1-\eta_J).}
\]

More geometrically, it suffices to prove
\[
C_X\le
\frac{2m}{r}-4mL(1-\overline V_W)-\varepsilon(c)m,
\]
which would give the strict margin
\[
H_{\rm out}''\le-\varepsilon(c)m.
\]

This is not a renaming of the original remainder: the entire \(D\)-rate acceleration has acquired a proved negative sign and an exact contraction-gap value. Only the conditional-Rademacher sector remains.

## DISPROVED

A pointwise payment of the remaining term cannot work with a small contrast-independent coefficient.

Define
\[
\Xi_O=(X^2-\delta_O)\psi_O
+L\operatorname{Var}(D\mid O).
\]

For the actual \(m=2\) cyclic Fourier channel, whose Hamming-one block is the uniform \(2\times2\) channel, take a count-one output atom with \(X=0\). The posterior has
\[
P(D=2\mid O)=\frac{r^2}{r^2+s^2},
\qquad
P(D=0\mid O)=\frac{s^2}{r^2+s^2},
\]
and exact simplification gives
\[
\boxed{
\frac{\Xi_O}{\delta_O}
=\log\frac{r^2+s^2}{2r^2}.}
\]

This ratio diverges as \(c\uparrow1\). In particular,
\[
\Xi_O\le\delta_O
\]
already fails whenever
\[
c>
\sqrt{\frac{\sqrt{2e-1}-1}{\sqrt{2e-1}+1}}
=0.5967833208\ldots.
\]

It therefore fails throughout \(37/40<c<1\). This is an obstruction in the **actual cyclic family**, not for an unrelated arbitrary unitary. The packet’s separate \(m=2\) result that \(G''>0\) while total curvature remains negative is consistent with this signed split. citeturn192741view0turn192741view1

## Computational diagnostics

I executed an independent NumPy enumerator which constructs
\[
U_m=2(Q_m)_{EO}
\]
from the first \(m\) Fourier modes on the \(2m\)-cycle, forms all exterior minors, and enumerates every midpoint atom.

For \(c=0.95\):

| \(m\) | \(C_X\) | \(C_D\) | \(G''\) | \(H_{\rm out}''\) | \(\eta_J\) |
|---:|---:|---:|---:|---:|---:|
| 2 | 21.0064767764 | −3.6515104356 | 17.3549663408 | −122.9790240679 | 0.153627663 |
| 3 | 53.2479239359 | −8.5459817565 | 44.7019421793 | −165.7990434337 | 0.239699750 |
| 4 | 91.9661185565 | −14.0850971180 | 77.8810214385 | −202.7869593789 | 0.296296642 |
| 5 | 134.6147608045 | −20.0041086347 | 114.6106521698 | −236.2243238520 | 0.336648028 |

The finite-difference residual in
\[
C_D=-8\partial_kG_0
\]
was between \(5.1\times10^{-11}\) and \(1.1\times10^{-9}\). Unitarity and exterior-channel row/column residuals were below \(2\times10^{-15}\).

These are floating-point diagnostics only. The sign theorem above is analytic and does not depend on enumeration. Repository-provided checkers were not executed because no repository checkout was obtained; the attached independent script did execute successfully.

## INCOMPLETE

The following are still open obligations within this task’s scope:

1. Prove the all-\(m\) upper bound on \(C_X\) for the actual consecutive-Fourier \(U_m\).
2. Establish the normalized cyclic-to-true Hilbert/Cauchy or finite-Toeplitz second-response bridge. The packet correctly requires normalization by all \(2m\) cyclic sites and warns that entropy-value convergence alone cannot be differentiated. citeturn192741view1turn192741view2
3. Extend away from \(a=(1-c)/2\), where the Fisher-loss term and all moving weights return.
4. Replace the half-density parity-unitary structure for arbitrary \(\rho\).

## Files

:chatgpt-content-reference{index="4"}

:chatgpt-content-reference{index="5"}
