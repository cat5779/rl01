# PRO02 round 2 takeover: a strict posterior reserve and a sine-specific pair-cut budget

## Status

**PROVED, scoped and pending fresh independent review:**

1. the logarithmic block potential in the visible S18 summary exactly retains the entire pair remainder;
2. the posterior cross-storage identity has a strictly positive reserve which, at the balanced channel, improves the total internal quadratic-variation budget by the factor `c^2`;
3. the initial cross-storage admits an exact variational-capacity upper bound;
4. at half density, every pair cut of a contiguous block partition can be paid by the sine number variance, replacing the old `C_* H_m/m` tail by `C_pair V_m/m`.

**INCOMPLETE:** no complete benchmark window has been proved negative. The first-round S18 attachment bodies, including the claimed finite two-branch Jensen proof, are not present in the public branch or the local packet. I therefore do not certify that missing proof. The new results below are self-contained and show precisely how the claimed localization inequality would improve once that load-bearing lemma is independently recovered.

All expectations below use the actual output law. No uniform word average or averaged conditional kernel is used.

## 1. Setting and recovery boundary

Let `V` be a finite integer interval and let `Q_V` be the half-density sine Toeplitz compression,

\[
(Q_V)_{ii}=\frac12,\qquad
(Q_V)_{ij}=\frac{\sin(\pi(i-j)/2)}{\pi(i-j)}\quad(i\ne j).
\]

Put `K=aI+cQ`, with `0<a<1-c`. The benchmark is

\[
a=\frac1{40},\qquad c=\frac{19}{20},
\qquad a=\frac{1-c}{2}.
\]

For a complete output word `Y`, write

\[
G=[K-\operatorname{diag}(1-Y)]^{-1},\qquad
v_{ij}=G_{ii}G_{jj},\qquad h_{ij}=|G_{ij}|^2.
\]

The visible S18 harvest reports a first-round theorem, but the actual `RESULT.md`, its proof, and its scripts are unavailable. Direct enumeration in `checks/enumerate_phi.py` nevertheless reproduces its two quoted diagnostics:

\[
H_6''=-49.5655212392509\ldots,
\qquad \mathcal W_{4,2}=-10.1330043150628\ldots.
\]

This confirms the interpretation of the displayed potential and weights; it is not independent certification of the missing theorem.

## 2. Exact recovery of the logarithmic potential

Define

\[
\Psi(v,h)=h+(v-h)\log\frac{v-h}{v}.
\]

For every true word, `v` and `v-h` have the same sign. Direct integration gives

\[
\int_0^1(1-t)\frac{h^2}{v-th}\,dt
=h+(v-h)\log\frac{v-h}{v}=\Psi(v,h). \tag{2.1}
\]

The audited old SA02 pair identity is

\[
g(P_{ij})=-\mathbb E\left[
\int_0^1(1-t)\frac{h_{ij}^2}{v_{ij}-t h_{ij}}dt
\,\middle|\,Y_{V\setminus\{i,j\}}\right].
\]

Thus for a core `I`,

\[
\Phi_I(G)=\sum_{i\in I}G_{ii}^2
+2\sum_{i<j\in I}\Psi(v_{ij},h_{ij}) \tag{2.2}
\]

satisfies the exact identity

\[
\boxed{\mathcal C_I^V=-\mathbb E\Phi_I((G_V)_{II}).} \tag{2.3}
\]

In particular, the old nonnegative pair remainder has not been discarded; it is exactly the difference between `Psi` and its zeroth rational layer.

## 3. Strict dissipation of posterior cross-storage

This section proves more than the non-strict storage inequality quoted in the S18 summary.

Let the current unrevealed external set be `O={j} union O'`, with fixed core `I`. Conditional on the current output history, the latent variables on `I union O` form a DPP with positive-contraction kernel `R`. Write

\[
q=R_{jj},\quad p=a+cq,\quad b=R_{I,j},\quad
d=R_{O',j},\quad C=R_{I,O'}.
\]

After observing `Y_j` and deleting coordinate `j`, the two actual branches are

\[
R^1=R-\frac c p R_{\cdot j}R_{j\cdot},\qquad
R^0=R+\frac c{1-p}R_{\cdot j}R_{j\cdot}, \tag{3.1}
\]

with probabilities `p` and `1-p`. If `gamma=-c/p` in the first branch and `gamma=c/(1-p)` in the second, then

\[
\mathbb E\gamma=0,qquad
\lambda:=\mathbb E\gamma^2=\frac{c^2}{p(1-p)}. \tag{3.2}
\]

Set

\[
S=\|R_{I,O}\|_{HS}^2=\|b\|^2+\|C\|_{HS}^2.
\]

The update gives

\[
R'_{I,O'}=C+\gamma bd^*,\qquad
\Delta R_{II}=\gamma bb^*.
\]

The first-order terms vanish by (3.2), so conditionally and exactly,

\[
\begin{aligned}
\mathbb E[S'+\|\Delta R_{II}\|_{HS}^2]&=S-D_j,\\
D_j&=\|b\|^2\left[1-\lambda(\|b\|^2+\|d\|^2)\right]. \tag{3.3}
\end{aligned}
\]

Because `R` is a contraction,

\[
\|b\|^2+\|d\|^2\le q(1-q).
\]

Moreover,

\[
p(1-p)-c^2q(1-q)
=(1-q)a(1-a)+q(a+c)(1-a-c)>0. \tag{3.4}
\]

Hence `D_j>=0`. Equation (3.3) recovers the reported dissipation inequality and identifies the strict reserve that the summary discarded.

### Balanced-channel improvement

Now let `a=(1-c)/2` and

\[
\beta=a(1-a)=\frac{1-c^2}{4},\qquad
\kappa=\frac{c^2}{1-c^2}.
\]

Then

\[
p(1-p)=\beta+c^2q(1-q).
\]

Writing `Q_j=E||Delta R_II||_HS^2=lambda||b||^4`, (3.3) gives

\[
\frac{Q_j}{D_j}
\le\frac{c^2q(1-q)}\beta\le\kappa. \tag{3.5}
\]

Telescoping (3.3) over all external reveals, and retaining the nonnegative terminal storage, yields

\[
\sum_t\mathbb E(Q_t+D_t)\le\mathbb ES_0.
\]

Since `Q_t<=kappa D_t`,

\[
\boxed{
\sum_t\mathbb E\|\Delta R_{II,t}\|_{HS}^2
\le\frac\kappa{1+\kappa}\mathbb ES_0
=c^2\mathbb ES_0.} \tag{3.6}
\]

This is a strict, dimension-free strengthening of the coefficient-one storage budget. At the benchmark the improvement factor is `361/400=0.9025`.

## 4. A variational capacity bound for the initial storage

Let `A` be the already observed window, `I subset A`, and `O=V\setminus A`. Let `R^A` be the latent posterior kernel given `Y_A`. For any real vector `f`, the elementary DPP variance formula implies

\[
\operatorname{Var}_{R^A}\left(\sum_i f_iX_i\right)
\ge\frac12\sum_{i,j}|R^A_{ij}|^2(f_i-f_j)^2. \tag{4.1}
\]

Averaging and applying conditional-variance contraction bounds the left side by its prior variance. If `f=1` on `I` and `f=0` on `O`, the two orientations of `I times O` in (4.1) combine exactly into `||R^A_{I,O}||_HS^2`. Therefore

\[
\boxed{
\mathbb E\|R^A_{I,O}\|_{HS}^2
\le \operatorname{Var}_{Q}\left(\sum_i f_iX_i\right).} \tag{4.2}
\]

Taking the infimum over all admissible `f` gives a discrete capacity `Cap_Q(I,A)`. This is an exact state-dependent interface, not a norm relaxation.

At half density, the trial `f=1_I` gives

\[
\mathbb E\|R^A_{I,O}\|_{HS}^2\le V_m,
\]

where, for `m=|I|` consecutive sites,

\[
\boxed{
V_m=\frac m4-\frac2{\pi^2}
\sum_{\substack{1\le r<m\\r\ {
m odd}}}\frac{m-r}{r^2}.} \tag{4.3}
\]

Consequently, once the S18 bound `9/16(1+m/L)` is independently recovered, it can be replaced by the minimum of that bound, `V_m`, and the variational capacity.

## 5. A sine-specific payment for every cut pair

At the balanced point, the posterior normalization gives, for `i ne j`,

\[
|G_{ij}|^2=\frac{c^2}{\beta^2}|R^Y_{ij}|^2. \tag{5.1}
\]

If `Y_i=Y_j`, then `v>h` and `Psi(v,h)>=0`; omitting that cross-block pair only enlarges an upper bound on the Hessian. If `Y_i ne Y_j`, then `v<0` and

\[
-\Psi(v,h)=h\ell(h/|v|)\le h\ell(\kappa),
\qquad
\ell(x)=\frac{(1+x)\log(1+x)-x}{x}. \tag{5.2}
\]

Thus the complete bad contribution of all cross-block pairs is at most

\[
C_{\rm pair}
\sum_{i,j:B(i)\ne B(j)}\mathbb E|R^Y_{ij}|^2,
\qquad
C_{\rm pair}=\frac{c^2}{\beta^2}\ell(\kappa), \tag{5.3}
\]

where the sum is ordered and therefore already contains the factor two from the Hessian's unordered pairs.

For a contiguous partition `pi`, apply (4.1) with `f=1_B` for every block and sum. Each ordered cross-block pair occurs in two block indicators, which gives

\[
\mathbb E\sum_{i,j:B(i)\ne B(j)}|R^Y_{ij}|^2
\le\sum_{B\in\pi}\operatorname{Var}_Q(N_B). \tag{5.4}
\]

The quantity `V_r` in (4.3) is increasing because

\[
V_{r+1}-V_r
=\frac14-\frac2{\pi^2}
\sum_{\substack{1\le k\le r\\k\ {
m odd}}}\frac1{k^2}>0.
\]

A length-at-most-`m` partition of `[n]` has at most `n/m+2` blocks. Hence

\[
\boxed{
\frac{\text{complete pair-cut cost}}n
\le C_{\rm pair}V_m\left(\frac1m+\frac2n\right).} \tag{5.5}
\]

This pays every cut distance at once. No harmonic layer sum and no `C_*` are needed.

At the benchmark,

\[
C_{\rm pair}
=\frac{6400}{1521}\left(400\log\frac{400}{39}-361\right)
=2399.100214664\ldots. \tag{5.6}
\]

The old coefficient is

\[
C_*=\frac{3c^2\log 1521}{2\beta^2}
=16694.857647373\ldots.
\]

Representative per-site comparisons are:

| `m` | `V_m` | new pair-cut term | old `C_* H_m/m` |
|---:|---:|---:|---:|
| 1,000 | 0.929938 | 2.231 | 124.969 |
| 5,000 | 1.093008 | 0.524 | 30.366 |
| 100,000 | 1.396539 | 0.0335 | 2.018 |

## 6. Consequence for the reported S18 localization interface

The S18 summary reports a finite two-branch Jensen payment with

\[
\Gamma_{\rm ro}=\frac{296960000}{6591}
\]

and the observation coefficient

\[
A_{\rm ro}=\frac9{16}c^2\Gamma_{\rm ro}
=\frac{50251200}{2197}.
\]

I have not recovered the missing proof of that Jensen statement. Conditional on it, the proved reserve (3.6) changes the payment from `Gamma_ro c^2 E S_0` to `Gamma_ro c^4 E S_0`; hence

\[
\boxed{
A_{\rm ro}\longmapsto c^2A_{\rm ro}
=\frac{45351708}{2197}
=20642.561675011\ldots.} \tag{6.1}
\]

At the same time, (5.5) replaces the full old pair-cut term. Ignoring only the already displayed finite endpoint terms, the reported sufficient inequality would become

\[
\boxed{
\mathcal W_{m,L}
+C_{\rm pair}\frac{V_m}{m}
+\frac{45351708}{2197}\left(\frac1m+\frac1L\right)<0,} \tag{6.2}
\]

with the observation term further reducible through `Cap_Q(I,A)`. For finite `n`, retain the `2/n` terms in the reported observation bound, use (5.5), and retain the reported `4 Xi_delta(m+L)/n` endpoint term.

Equation (6.2) is a rigorously quantified reduction of the remaining obstacle, not a completed sign certificate.

## 7. Verification and reproducibility

The following commands use only NumPy and the standard library:

```text
python checks/enumerate_phi.py 6,0 4,2
python checks/benchmark_reduction.py
python checks/verify_reductions.py
```

The checks performed were:

- all scripts compile;
- actual-law enumeration reproduces the two visible S18 diagnostics;
- actual-law half-density windows `(n,m)=(6,2),(8,3),(10,4)` satisfy both stages of the pair-cut bound;
- ten seeded random strict contractions, with every external output branch enumerated, satisfy `sum Q_t <= c^2 S_0`.

These computations test the formulas and factors. The general results are proved algebraically above and do not rely on floating-point signs.

## 8. Exact remaining obstruction

No proved analytic upper bound on the large-window term `W_{m,L}` is currently strong enough to combine with (6.2). Direct enumeration grows exponentially and is not a route to the required scale. The next load-bearing step is one of:

1. prove a sine-realizable average Jensen sign or a substantially smaller state-dependent payment for the exact potential;
2. prove an extensive analytic lower bound on `E Phi_I` that survives the large core and observation window;
3. obtain a rigorously certified multiscale comparison that transfers a finite negative block to large `m` without paying the uniform worst-case observation constant per small block.

The benchmark curvature sign therefore remains **INCOMPLETE**.
