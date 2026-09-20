# S76 RESULT — a signed overlap/Jeffreys payment at the symmetric bias

## Status

**PROVED:** At the symmetric bias, for every size `m >= 1`, every `0 < c < 1`, and every Hamming-layer doubly stochastic channel `W` (hence in particular every actual cyclic exterior channel `W_{U_m}`), the midpoint acceleration splits into two exact sectors. The sector that changes the frequency of equal input pairs is always nonpositive. It is exactly a normalized loss of adjacent-mask Jeffreys divergence through `W`, and it has an explicit posterior-variance lower bound. Only a conditional-Rademacher/Krawtchouk sector remains unpaid.

**DISPROVED:** A natural pointwise attempt to pay the remaining sector by the local expected number of equal pairs fails already for the actual four-site cyclic Fourier channel, throughout the high-contrast range (indeed for `c > 0.59678...`). Thus the remaining estimate must be averaged; a pointwise positive-pair envelope cannot close it.

**INCOMPLETE:** The remaining Krawtchouk-sector upper bound is not proved uniformly in `m`. No cyclic-to-true Toeplitz/Hilbert second-response bridge is proved. Nothing here treats off-midpoint bias or arbitrary density `rho`.

All logarithms are natural.

---

## 1. Input and notation

Assume the exact finite model in `research/CYCLE26_20260920/S76/PACKET.md`. At

\[
a_0=\frac{1-c}{2},\qquad k=c^2,\qquad
r=\frac{1-k}{4},\qquad s=\frac{1+k}{4},\qquad
L=\log\frac{s}{r}=\log\frac{1+k}{1-k}.
\]

The iid pair table is

\[
P(00)=P(11)=r,\qquad P(01)=P(10)=s.
\]

Let

\[
X=A-m=|Y|+|Z|-m=|Y|+|T|-m
\]

and introduce the hidden equal-pair count

\[
D=\#\{i:Y_i=Z_i\}=m-A+2B.
\]

Thus `X` is output-measurable, while `D` is hidden. In spin notation
`\sigma_i=2Y_i-1`, `\tau_i=2Z_i-1`,

\[
X=\sum_i \frac{\sigma_i+\tau_i}{2},
\qquad
D=\sum_i \mathbf 1_{\sigma_i=\tau_i}.
\]

Let `R=log(P(Y,Z)/Q(Y,T))` be the information density of the entropy gain.
At the midpoint the Fisher loss is zero because the score is `S=X/r`, which is output-measurable.

---

## 2. Exact acceleration split

For one pair, the score is `-1/r,0,0,1/r` on `00,01,10,11`, while the atom acceleration `p''/p` is `2/r,-2/s,-2/s,2/r`. Hence for the product law

\[
\mathcal A
=\frac{X^2-D}{r^2}+\frac{D-2mr}{rs}. \tag{2.1}
\]

Indeed, expanding the product acceleration gives

\[
\mathcal A
=\frac{X^2}{r^2}
+D\left(\frac2r-\frac1{r^2}\right)
-(m-D)\frac2s,
\]

and (2.1) follows from `r+s=1/2`.

Since the Fisher loss is zero,

\[
G''=C_X+C_D, \tag{2.2}
\]

where

\[
C_X:=\frac1{r^2}\,\mathbb E[(X^2-D)R], \tag{2.3}
\]

\[
C_D:=\frac1{rs}\,\mathbb E[(D-2mr)R]. \tag{2.4}
\]

The labels have a probabilistic meaning. `D` is binomial with parameter `2r`; conditional on `D`, the signs of the `D` equal pairs are fair Rademachers and their sum is `X`. Thus `X^2-D` is the centered second Krawtchouk statistic of those signs.

---

## 3. Boolean integration by parts and the Jeffreys payment

### 3.1 Fair-spin density

At the midpoint the input density relative to the uniform law on `(Y,Z)` is

\[
F_k(y,z)=\prod_{i=1}^m(1-k\sigma_i\tau_i).
\]

After the channel,

\[
L_k(y,t)=\sum_z W(z,t)F_k(y,z)
\]

is the output density relative to uniform. Because `W` is doubly stochastic, both output marginals are fair, and

\[
I_W(k)=4^{-m}\sum_{y,t}L_k(y,t)\log L_k(y,t)
\]

is exactly `I(Y;T)` at the midpoint. For the identity channel, write `I_id(k)`.
The entropy gain is

\[
G_0(k)=I_{id}(k)-I_W(k). \tag{3.1}
\]

### 3.2 Number-operator identity

Let

\[
N_y f=\frac12\sum_{i=1}^m\bigl(f(y,t)-f(y^{(i)},t)\bigr),
\]

where `y^{(i)}` flips bit `i`. Expanding `F_k` in Walsh characters and then applying `W` gives

\[
k\,\partial_k L_k=N_yL_k. \tag{3.2}
\]

Differentiating entropy and using the discrete integration-by-parts identity yields

\[
\mathcal E_W(k):=kI_W'(k)
=\langle N_yL_k,\log L_k\rangle
\]

\[
=\frac14\sum_{i=1}^m
\mathbb E_{y\sim\mathrm{Unif}}
J\!\left(P_y^W,P_{y^{(i)}}^W\right), \tag{3.3}
\]

where `P_y^W` is the conditional law of `T` given `Y=y` and

\[
J(P,Q)=D(P\|Q)+D(Q\|P)
\]

is Jeffreys divergence.

For completeness, the edge identity behind (3.3) is

\[
\langle Nf,\log f\rangle
=\frac14\sum_i
\left\langle(f-f^{(i)})(\log f-\log f^{(i)})\right\rangle.
\]

### 3.3 Contraction and exact sign

For every adjacent pair `y,y^{(i)}`, the output laws are obtained by sending the corresponding `Z` laws through the same Markov kernel `W`. Applying the log-sum inequality to both directed KL divergences gives

\[
J(P_y^W,P_{y^{(i)}}^W)
\le J(P_y^{id},P_{y^{(i)}}^{id}).
\]

For the input pair, only bit `i` changes, and the adjacent Jeffreys divergence is

\[
J(P_y^{id},P_{y^{(i)}}^{id})=2kL.
\]

Consequently

\[
0\le \mathcal E_W(k)\le \mathcal E_{id}(k)=\frac{mkL}{2}. \tag{3.4}
\]

Put

\[
\Delta\mathcal E(k)=\mathcal E_{id}(k)-\mathcal E_W(k)\ge0,
\qquad
\eta_J(k)=\frac{2\Delta\mathcal E(k)}{mkL}\in[0,1]. \tag{3.5}
\]

Now let `lambda=P(Y_i=Z_i)=2r=(1-k)/2`. The score for varying `lambda` is

\[
S_\lambda=\frac{D-m\lambda}{\lambda(1-\lambda)}.
\]

The first derivative of the entropy gain is

\[
\partial_\lambda G_0=\mathbb E[S_\lambda R].
\]

Since `lambda(1-lambda)=4rs` and `partial_lambda=-2 partial_k`, (2.4) becomes

\[
\boxed{
C_D
=4\partial_\lambda G_0
=-8\partial_kG_0
=-\frac8k\Delta\mathcal E(k)
=-4mL\,\eta_J(k)
\le0.} \tag{3.6}
\]

This is the signed payment. It is an exact identity, not an absolute-value estimate.

---

## 4. A directly checkable posterior-uncertainty lower bound

Fix an edge `(i,y)` and let

\[
M_{i,y}=\frac12(P_y^{id}+P_{y^{(i)}}^{id})
\]

on `Z`. Under `M_{i,y}`, the spin

\[
\zeta_i=\sigma_i\tau_i
\]

is a fair sign. Define

\[
m_{i,y}(t)=\mathbb E_{M_{i,y}}[\zeta_i\mid T=t].
\]

The two adjacent input laws are `M(1-k\zeta_i)` and `M(1+k\zeta_i)`, so after `W` their Jeffreys divergence is exactly

\[
4k\,\mathbb E_{M^W}
\left[m_{i,y}(T)\operatorname{artanh}(k m_{i,y}(T))\right]. \tag{4.1}
\]

The input value is `4k artanh(k)=2kL`. Since for `0<=x<=1`

\[
\operatorname{artanh}(kx)\le x\operatorname{artanh}(k),
\]

(4.1) gives the edgewise loss bound

\[
J_{in}-J_{out}
\ge 2kL\,
\mathbb E_{M^W}\bigl[1-m_{i,y}(T)^2\bigr].
\]

Therefore

\[
\boxed{
\eta_J(k)\ge
\overline V_W(k):=
\frac1m\sum_{i=1}^m
\mathbb E_{y\sim\mathrm{Unif}}
\mathbb E_{M_{i,y}^W}
\operatorname{Var}_{M_{i,y}}(\zeta_i\mid T).} \tag{4.2}
\]

For an exterior channel this is a finite determinant expression, because every occurrence of `W(z,t)` is `|det U_{z,t}|^2`. Thus (4.2) is a model-valid, all-size quantity that can be bounded using the actual consecutive-Fourier/Hilbert geometry rather than an arbitrary norm envelope.

Combining (3.6) and (4.2),

\[
C_D\le-4mL\,\overline V_W(k). \tag{4.3}
\]

---

## 5. The remaining overlap/Krawtchouk cost

Let

\[
\delta_O=\mathbb E[D\mid O].
\]

Because `D=-X+2B`, the packet's Poisson-binomial posterior gives

\[
\delta_O=-X+2\mu_O,
\qquad
\operatorname{Var}(D\mid O)=4\kappa_{2,O}. \tag{5.1}
\]

Also `gamma=-2L` and `B=(D+X)/2`. Absorbing the output-measurable term `-LX` into the partition function gives

\[
R=-LD-\log \widehat Z_O.
\]

Hence

\[
\operatorname{Cov}(D,R\mid O)=-L\operatorname{Var}(D\mid O),
\]

and therefore

\[
\boxed{
C_X=\frac1{r^2}\,
\mathbb E\left[(X^2-\delta_O)\psi_O+4L\kappa_{2,O}\right].} \tag{5.2}
\]

Combining (2.2), (3.6), and (5.2) gives the main identity

\[
\boxed{
G''
=\frac1{r^2}\,
\mathbb E\left[(X^2-\delta_O)\psi_O+4L\kappa_{2,O}\right]
-4mL\eta_J.} \tag{5.3}
\]

The total observed entropy curvature is thus

\[
\boxed{
H_{out}''
=C_X-\frac{2m}{r}+4mL(1-\eta_J).} \tag{5.4}
\]

Accordingly, midpoint concavity for a given finite channel follows from the strictly narrower obligation

\[
\boxed{
C_X\le \frac{2m}{r}-4mL(1-\eta_J).} \tag{5.5}
\]

A margin `epsilon(c)m` follows if the right side of (5.5) is reduced by `epsilon(c)m`. Using only the posterior-variance lower bound (4.2), it is enough to prove

\[
C_X\le \frac{2m}{r}-4mL(1-\overline V_W)-\epsilon(c)m. \tag{5.6}
\]

The original acceleration has therefore not been renamed: its `D`-rate component has been completely paid, with an explicit determinant-channel payment, and the exact unpaid component is the conditional Rademacher/Krawtchouk response (5.2).

---

## 6. Exact obstruction to a pointwise replacement

A tempting route is a pointwise estimate of

\[
\Xi_O=(X^2-\delta_O)\psi_O+L\operatorname{Var}(D\mid O)
\]

by a constant multiple of `delta_O`. Such an estimate cannot have a small contrast-independent constant.

In the actual `m=2` cyclic Fourier channel, the Hamming-one block is the uniform `2 x 2` matrix. Take a count-one output atom with `X=0`. Its hidden `D` equals `2` with probability

\[
\alpha=\frac{r^2}{r^2+s^2}
\]

and equals `0` otherwise. Direct substitution gives

\[
\delta_O=2\alpha,
\qquad
\boxed{
\frac{\Xi_O}{\delta_O}
=\log\frac{r^2+s^2}{2r^2}.} \tag{6.1}
\]

The ratio tends to infinity as `c -> 1`. In particular `Xi_O <= delta_O` fails whenever

\[
c>
\sqrt{\frac{\sqrt{2e-1}-1}{\sqrt{2e-1}+1}}
=0.5967833208\ldots,
\]

so it fails throughout the requested high-contrast range. This is an actual cyclic obstruction, not an arbitrary-unitary example. It explains why the Jeffreys payment must be extracted after averaging rather than atom by atom.

---

## 7. Computational diagnostics and execution status

I wrote and executed an independent NumPy enumerator, `s76_checks.py`. It constructs
`U=2Q_EO` from the first `m` Fourier modes on the `2m`-cycle, forms every exterior minor, enumerates all midpoint atoms, and checks

\[
C_D=-8\,\partial_k G_0
\]

by a centered finite difference. This is floating-point evidence only; none of the proofs above uses it.

For `c=0.95` the executed output was:

| m | C_X | C_D | G'' | H_out'' | eta_J | `C_D+8 dG/dk` |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 21.0064767764 | -3.6515104356 | 17.3549663408 | -122.9790240679 | 0.153627663 | 2.1e-10 |
| 3 | 53.2479239359 | -8.5459817565 | 44.7019421793 | -165.7990434337 | 0.239699750 | 8.2e-10 |
| 4 | 91.9661185565 | -14.0850971180 | 77.8810214385 | -202.7869593789 | 0.296296642 | -5.1e-11 |
| 5 | 134.6147608045 | -20.0041086347 | 114.6106521698 | -236.2243238520 | 0.336648028 | -1.1e-9 |

The largest unitarity and row/column-sum residuals in these runs were below `2e-15`.
For the pointwise atom in Section 6 at `c=0.95`, the run produced

\[
\delta_O=0.00523902852360,
\quad
\operatorname{Var}(D\mid O)=0.01045060962733,
\]

\[
\Xi_O=0.02751338275296,
\quad
\Xi_O/\delta_O=5.25161919409679,
\]

matching (6.1).

Repository-provided checkers were not executed: the local runtime did not obtain a repository checkout. The raw packet was available and the attached enumerator was executed locally.

---

## 8. Exact remaining obligations

1. **Finite cyclic midpoint:** Prove (5.5), or the stronger determinant-geometric form (5.6), for the actual consecutive-Fourier `U_m`, uniformly in `m`. The only unpaid term is (5.2).
2. **True sine process:** Establish a separately justified cyclic-to-Hilbert/Toeplitz bridge for the normalized second response. No derivative of an `o(m)` entropy-value error is used here.
3. **Bias and density:** Extend away from `a=(1-c)/2`; then the Fisher-loss term and all moving weights return. Extend from `rho=1/2` to general `rho`, where the parity unitary representation is unavailable.
4. **S73 mixed-response interface:** This result does not by itself prove the true-law bound `v_lim >= -1/100`; the required normalization is still by the total `2m` cyclic sites, and the response bridge remains an independent obligation.

---

## Reproducible source map

- Task: `research/CYCLE26_20260920/S76/TASK.md`
- Complete packet: `research/CYCLE26_20260920/S76/PACKET.md`
- Raw packet supplied by the user: `https://raw.githubusercontent.com/cat5779/rl01/research/sa-cycle19-harvest-20260919/research/CYCLE26_20260920/S76/PACKET.md`
- Independent diagnostic script produced with this result: `s76_checks.py`
