# S1 round 4 check 2 — actual-output weighted tail for growing half-density Fourier projections

**Status:** `INCOMPLETE`.  The fixed-density sine entropy-rate concavity target is
not proved.  The new result is a uniform, actual-output weighted-tail theorem
for the growing contiguous half-density Fourier family at `c=19/20`, on the
non-microscopic interior chord range

\[
J=\left[\frac1{50},\frac3{100}\right].
\]

It removes every outside word outside an `O(sqrt(n log n))` count band from the
outstanding extensive star budget, with an `O(n^{1-gamma})` error for any fixed
`gamma>1`.  The complete negative Fisher square and the negative weighted
remainder are retained.  The central count band remains unresolved.

All logarithms are natural.

## 1. Imported checkpoint, not counted as new work

The previous cumulative checkpoint proves, at author-unreviewed scope, the
all-odds identity

\[
H_n''(a)=\sum_{i=0}^{n-1}\mathbb E_{Y_{-i}}
\left[\frac{e_i}{16}-\frac{W_i}{2}-\mathsf S_i\right],
\tag{1.1}
\]

where

\[
e_i=s_i d_i^2(\Delta_iG_i)^2,
\qquad
\mathsf S_i=
\left(\frac1{\sqrt{s_i}}-
\frac14d_i\sqrt{s_i}\,\Delta_iG_i\right)^2,
\tag{1.2}
\]

and `W_i>=0` is the actual-output weighted nonlinear remainder.  Its bounded
star variables satisfy

\[
\Delta_iG_i=
\sum_{j\in J_1}g(t_{ij}^{(1)})-
\sum_{j\in J_0}g(t_{ij}^{(0)}),
\tag{1.3}
\]

\[
W_i=(1-r_i)\sum_{j\in J_0}\rho(t_{ij}^{(0)})
+r_i\sum_{j\in J_1}\rho(t_{ij}^{(1)}),
\tag{1.4}
\]

with

\[
g(t)=2[-\log(1-t)-t],
\qquad
\rho(t)=2\left[t+\frac{t}{1-t}+2\log(1-t)\right].
\tag{1.5}
\]

Here `r_i=Pr(Y_i=1|Y_-i)`, `s_i=r_i(1-r_i)`, and `d_i=1-2r_i`.
The proof of (1.1)--(1.5) is preserved verbatim in the check-1 archive.  This
round neither renames nor re-counts that decomposition as progress.  Everything
below is new.

## 2. Fourier family and output L-ensemble

Let `n=2m`, and let `P_n` be the projection onto the contiguous Fourier columns

\[
U_{x,k}=n^{-1/2}e^{2\pi i xk/n},
\qquad 0\le k<m.
\]

Fix

\[
c=\frac{19}{20},\qquad a\in J.
\]

Let

\[
K_{n,a}=aI+cP_n,
\qquad
Y\sim\operatorname{DPP}(K_{n,a}).
\]

Since `0<K_{n,a}<I`, its output `L`-matrix is

\[
L_{n,a}=K_{n,a}(I-K_{n,a})^{-1}
=\lambda_0(a)(I-P_n)+\lambda_1(a)P_n,
\tag{2.1}
\]

where

\[
\lambda_0(a)=\frac{a}{1-a},
\qquad
\lambda_1(a)=\frac{a+c}{1-a-c}.
\tag{2.2}
\]

The complete output law is the genuine `L`-ensemble

\[
\Pr(Y=S)=\frac{\det (L_{n,a})_S}{\det(I+L_{n,a})}.
\tag{2.3}
\]

Put

\[
\kappa(a)=\frac{\lambda_1(a)}{\lambda_0(a)}
=\frac{(a+c)(1-a)}{a(1-a-c)}.
\]

A direct derivative gives

\[
\frac{d}{da}\log\kappa(a)
=
\frac{c(2a+c-1)}{a(a-1)(a+c)(a+c-1)}.
\]

The denominator is positive on the legal interval, so `kappa` decreases up to
`a=(1-c)/2=1/40` and increases afterwards.  Consequently, on `J`,

\[
\boxed{
\kappa(a)\le \kappa_*:=\frac{4753}{3}.
}
\tag{2.4}
\]

Define

\[
D_*:=\kappa_*-1=\frac{4750}{3},
\qquad
\tau_*:=\left(\frac{\kappa_*-1}{\kappa_*+1}\right)^2
=\left(\frac{2375}{2378}\right)^2.
\tag{2.5}
\]

## 3. Exact L-ensemble meaning of the bounded star variables

Fix a site `i` and an outside occupied set

\[
T\subseteq [n]\setminus\{i\}.
\]

For `j` outside `T union {i}`, condition the output on the occupied outside set
`T` and leave only `i,j` free.  The unnormalized four-cell table is

\[
\det L_T,\quad
\det L_{T\cup\{j\}},\quad
\det L_{T\cup\{i\}},\quad
\det L_{T\cup\{i,j\}}.
\tag{3.1}
\]

Let `C_T=L/L_T` be the Schur complement on `T^c`.  Schur determinant formulas
give

\[
t_{ij}(T)
=1-\frac{\det L_T\det L_{T\cup\{i,j\}}}
{\det L_{T\cup\{i\}}\det L_{T\cup\{j\}}}
=\frac{|(C_T)_{ij}|^2}{(C_T)_{ii}(C_T)_{jj}}.
\tag{3.2}
\]

This is exactly the previous checkpoint's even-parity bounded variable.
Therefore, for the star based at outside word `T`,

\[
t_{ij}^{(0)}(T)=t_{ij}(T),\qquad j\notin T\cup\{i\}.
\tag{3.3}
\]

For `j in T`, let `B=L_{T union {i}}` and `Q=B^{-1}`.  The two-by-two Schur
complement on `{i,j}` after eliminating `T\setminus\{j\}` has inverse equal to
the `{i,j}` principal block of `Q`.  Normalized off-diagonal correlation is
unchanged by inversion of a positive two-by-two matrix.  Hence

\[
t_{ij}^{(1)}(T)
=\frac{|Q_{ij}|^2}{Q_{ii}Q_{jj}},\qquad j\in T.
\tag{3.4}
\]

Finally, with

\[
\ell_i(T)=\frac{\det L_{T\cup\{i\}}}{\det L_T}=(C_T)_{ii},
\]

the complete outside law and the conditional output probability are

\[
\nu_{i,a}(T):=\Pr(Y_{-i}=T)
=\frac{\det L_T(1+\ell_i(T))}{\det(I+L)},
\tag{3.5}
\]

\[
r_i(T)=\frac{\ell_i(T)}{1+\ell_i(T)}.
\tag{3.6}
\]

Thus no reference/product law has replaced the actual outside-word law.

## 4. A conditioned-correlation lemma

### Lemma 4.1

Let `L` be positive definite and

\[
mI\preceq L\preceq MI,
\qquad \kappa=M/m.
\]

For every `i,T` as above, the quantities in (3.2)--(3.4) satisfy

\[
0\le t_{ij}^{(b)}\le
\left(\frac{\kappa-1}{\kappa+1}\right)^2,
\tag{4.1}
\]

and

\[
\sum_{j\notin T\cup\{i\}}t_{ij}^{(0)}\le\kappa-1,
\qquad
\sum_{j\in T}t_{ij}^{(1)}\le\kappa-1.
\tag{4.2}
\]

#### Proof

Every principal submatrix of `L` has spectrum in `[m,M]`.  Also every Schur
complement `C_T` has spectrum in `[m,M]`, because

\[
C_T^{-1}=(L^{-1})_{T^c,T^c}
\]

and the latter principal submatrix has spectrum in `[1/M,1/m]`.

For a positive two-by-two matrix with eigenvalues `mu_- <= mu_+`, write its
diagonal entries as `alpha,delta` and its off-diagonal entry as `beta`.  Since

\[
|\beta|^2\le\frac{(\mu_+-\mu_-)^2}{4}
\]

and `alpha delta=mu_+ mu_-+|beta|^2`,

\[
\frac{|\beta|^2}{\alpha\delta}
\le
\left(\frac{\mu_+-\mu_-}{\mu_++\mu_-}\right)^2
\le
\left(\frac{\kappa-1}{\kappa+1}\right)^2.
\]

This proves (4.1) for Schur complements and, by (3.4), for the inverse principal
matrices as well.

For any positive matrix `A` with spectrum in `[m,M]`, let

\[
R=D^{-1/2}AD^{-1/2},\qquad D=\operatorname{diag}(A).
\]

Then `R_ii=1`, and its largest eigenvalue is at most `kappa`: for `x=D^{1/2}y`,

\[
\frac{x^*Rx}{x^*x}
=
\frac{y^*Ay}{y^*Dy}
\le\frac{M}{m}=\kappa.
\]

Thus `R^2 <= kappa R`, and the `i`th diagonal entry gives

\[
1+\sum_{j\ne i}|R_{ij}|^2=(R^2)_{ii}\le\kappa.
\]

Apply this first to `C_T`, and then to `Q=(L_{T union {i}})^{-1}`, whose
condition number is also at most `kappa`.  Equations (3.2) and (3.4) give
(4.2).  ∎

## 5. Dimension-free size of every star

Set

\[
C_g:=\frac{g(\tau_*)}{\tau_*},
\qquad
C_\rho:=\frac{\rho(\tau_*)}{\tau_*}.
\tag{5.1}
\]

The positive-coefficient series

\[
\frac{g(t)}t=2\sum_{q\ge2}\frac{t^{q-1}}q,
\qquad
\frac{\rho(t)}t
=2\sum_{q\ge3}\frac{q-2}{q}t^{q-1}
\]

show that both ratios are increasing on `[0,1)`.  Lemma 4.1 therefore gives,
uniformly in `n,a,i,T`,

\[
|\Delta_iG_i(T)|\le 2C_gD_*,
\tag{5.2}
\]

\[
0\le W_i(T)\le C_W:=C_\rho D_*,
\tag{5.3}
\]

and, for the previous checkpoint's

\[
A_i=r_i\sum_{j\notin T\cup\{i\}}t_{ij}^{(0)}
+(1-r_i)\sum_{j\in T}t_{ij}^{(1)},
\]

\[
A_i(T)\le D_*,
\qquad
\Theta_i(T)=3d_i(T)^2A_i(T)\le3D_*.
\tag{5.4}
\]

Since the channel itself gives

\[
r_i=a+c\Pr(X_i=1\mid Y_{-i})\in[a,a+c]
\subseteq\left[\frac1{50},\frac{49}{50}\right],
\tag{5.5}
\]

we have

\[
s_i\ge\frac{49}{2500}.
\tag{5.6}
\]

Also, with `x=d_i=1-2r_i`,

\[
s_i d_i^2=\frac{x^2(1-x^2)}4\le\frac1{16}.
\tag{5.7}
\]

Consequently

\[
0\le\frac{e_i}{16}\le
C_E:=\frac{C_g^2D_*^2}{64},
\tag{5.8}
\]

and

\[
0\le\mathsf S_i\le
C_S:=\left(\frac{50}{7}+\frac{C_gD_*}{4}\right)^2.
\tag{5.9}
\]

Thus the complete signed star integrand has the dimension-free absolute bound

\[
\left|\frac{e_i}{16}-\frac{W_i}{2}-\mathsf S_i\right|
\le C_{\rm abs}:=C_E+\frac{C_W}{2}+C_S.
\tag{5.10}
\]

For reference, deterministic high-precision evaluation gives

\[
\begin{aligned}
C_g&<9.997,\\
C_\rho&<771.175,\\
C_W&<1.222\times10^6,\\
C_E&<3.914\times10^6,\\
C_S&<1.572\times10^7,\\
C_{\rm abs}&<2.024\times10^7.
\end{aligned}
\tag{5.11}
\]

The constants are large but independent of `n` and of the outside word.  No
unconditional Fourier-kernel decay was asserted to survive conditioning.

The candidate positive large-star excess is also bounded:

\[
\frac{W_i}{32}(\Theta_i-16)_+
\le C_\Theta:=\frac{3C_\rho D_*^2}{32}.
\tag{5.12}
\]

## 6. Exact outside-count law and a uniform Bernstein tail

Let

\[
N_i=|Y_{-i}|,
\qquad
\mu_{n,a}=(n-1)\left(a+\frac c2\right).
\tag{6.1}
\]

A projection DPP with kernel `P_n` has exactly `m=n/2` occupied input sites,
and `(P_n)_{ii}=1/2`.  Hence the *actual* law of `N_i` is

\[
\begin{aligned}
N_i\ \stackrel{d}=\ \frac12&\left[
\operatorname{Bin}\left(m,a+c\right)
+\operatorname{Bin}\left(m-1,a\right)
\right]\\
+\frac12&\left[
\operatorname{Bin}\left(m-1,a+c\right)
+\operatorname{Bin}\left(m,a\right)
\right],
\end{aligned}
\tag{6.2}
\]

where the displayed sums use independent binomials and the outer `1/2` denotes
a mixture, not arithmetic addition of random variables.

Indeed, conditional on the complete input `X`, the outside outputs are
independent and

\[
\mathbb E[N_i\mid X]
=a(n-1)+c(m-X_i).
\]

Its difference from `mu_{n,a}` is exactly

\[
\mathbb E[N_i\mid X]-\mu_{n,a}=c\left(\frac12-X_i\right),
\tag{6.3}
\]

whose absolute value is `c/2`.

For `a in J`, both possible Bernoulli variances obey

\[
a(1-a)\le v_*:=\frac{291}{10000},
\qquad
(a+c)(1-a-c)\le v_*.
\tag{6.4}
\]

For completeness, if `S` is a sum of independent Bernoulli variables with
total variance `V`, then

\[
\Pr(|S-\mathbb ES|\ge u)
\le2\exp\left[-\frac{u^2}{2(V+u/3)}\right].
\tag{6.5}
\]

To verify (6.5), for a centered Bernoulli variable `Z`, `|Z|<=1` and
`E|Z|^q<=EZ^2`.  Since `q!>=2*3^{q-2}` for `q>=2`,

\[
\mathbb Ee^{tZ}
\le\exp\left(\frac{t^2\mathbb EZ^2}{2(1-t/3)}\right),
\qquad0<t<3.
\]

Multiply the moment generating functions and optimize at
`t=u/(V+u/3)`; apply the same argument to `-Z`.

Combining (6.3)--(6.5), for every `u>0`,

\[
\boxed{
\Pr\left(
|N_i-\mu_{n,a}|\ge\frac c2+u
\right)
\le
2\exp\left[-\beta_n(u)\right],
}
\tag{6.6}
\]

where

\[
\beta_n(u)=
\frac{u^2}{2((n-1)v_*+u/3)}.
\tag{6.7}
\]

This is an actual-output statement.  No product approximation of the spatial
output law is being made; only the count conditional on the fixed-size input is
a sum of independent channel bits.

## 7. Main new theorem: weighted rare-word sector with both negative budgets retained

Define the rare outside-word event

\[
\mathcal T_{i,n}(u)=
\left\{
|N_i-\mu_{n,a}|\ge\frac c2+u
\right\}.
\tag{7.1}
\]

Define the *real paid bad-star surplus*

\[
\mathsf B_i=
\left(\frac{e_i}{16}-\frac{W_i}{2}\right)_+.
\tag{7.2}
\]

This is the positive part of the actual signed term before the Fisher square;
it is not the looser pointwise test `Theta_i>16`.

### Theorem 7.1

For every even `n>=2`, every `a in J`, every `u>0`, and the growing contiguous
half-density Fourier projection `P_n`,

\[
\boxed{
\sum_i\mathbb E\left[W_i\mathbf1_{\mathcal T_{i,n}(u)}\right]
\le
2nC_W e^{-\beta_n(u)}.
}
\tag{7.3}
\]

The actual bad-star contribution obeys

\[
\boxed{
\sum_i\mathbb E\left[\mathsf B_i\mathbf1_{\mathcal T_{i,n}(u)}\right]
\le
2nC_E e^{-\beta_n(u)}.
}
\tag{7.4}
\]

The candidate `Theta`-bad excess obeys

\[
\boxed{
\sum_i\mathbb E\left[
\frac{W_i}{32}(\Theta_i-16)_+
\mathbf1_{\mathcal T_{i,n}(u)}
\right]
\le
2nC_\Theta e^{-\beta_n(u)}.
}
\tag{7.5}
\]

Most importantly, the complete signed tail contribution satisfies

\[
\boxed{
\begin{aligned}
&\sum_i\mathbb E\left[
\left(\frac{e_i}{16}-\frac{W_i}{2}-\mathsf S_i\right)
\mathbf1_{\mathcal T_{i,n}(u)}
\right]\\
&\qquad\le
2nC_Ee^{-\beta_n(u)}
-\frac12\sum_i\mathbb E[W_i\mathbf1_{\mathcal T_{i,n}(u)}]
-\sum_i\mathbb E[\mathsf S_i\mathbf1_{\mathcal T_{i,n}(u)}].
\end{aligned}
}
\tag{7.6}
\]

Thus neither the nonlinear negative remainder nor the complete Fisher square is
discarded.  Each appears once, with its original actual-output weight.

Finally,

\[
\boxed{
\sum_i\mathbb E\left[
\left|\frac{e_i}{16}-\frac{W_i}{2}-\mathsf S_i\right|
\mathbf1_{\mathcal T_{i,n}(u)}
\right]
\le2nC_{\rm abs}e^{-\beta_n(u)}.
}
\tag{7.7}
\]

#### Proof

The pointwise bounds (5.3), (5.8), (5.9), (5.10), and (5.12), multiplied by
the probability bound (6.6), prove (7.3)--(7.5) and (7.7).
For (7.6), retain the negative terms and bound only the positive energy:

\[
\begin{aligned}
&\mathbb E\left[
\left(\frac{e_i}{16}-\frac{W_i}{2}-\mathsf S_i\right)
\mathbf1_{\mathcal T_i}
\right]\\
&\quad\le
C_E\Pr(\mathcal T_i)
-\frac12\mathbb E[W_i\mathbf1_{\mathcal T_i}]
-\mathbb E[\mathsf S_i\mathbf1_{\mathcal T_i}].
\end{aligned}
\]

Sum over `i` and use (6.6).

Only after this full actual-law estimate do we use cyclic symmetry.  Since
`P_n` is circulant and the channel is homogeneous, the joint law and every star
functional are shift-covariant.  Therefore every sum in (7.3)--(7.7) is exactly
`n` times the representative `i=0` expectation.  ∎

## 8. Explicit growing-n consequence

For `gamma>0`, put

\[
u_{n,\gamma}
=
\sqrt{2v_*(n-1)\gamma\log n}
+\frac{2\gamma}{3}\log n.
\tag{8.1}
\]

Let `x=gamma log n`, `V=(n-1)v_*`, and write
`u=sqrt(2Vx)+2x/3`.  Then

\[
u^2\ge2x(V+u/3),
\]

so `beta_n(u_{n,gamma})>=gamma log n`.  Hence Theorem 7.1 gives

\[
\sum_i\mathbb E[W_i\mathbf1_{\mathcal T_{i,n}}]
\le2C_W n^{1-\gamma},
\tag{8.2}
\]

\[
\sum_i\mathbb E[\mathsf B_i\mathbf1_{\mathcal T_{i,n}}]
\le2C_E n^{1-\gamma},
\tag{8.3}
\]

and

\[
\begin{aligned}
&\sum_i\mathbb E\left[
\left(\frac{e_i}{16}-\frac{W_i}{2}-\mathsf S_i\right)
\mathbf1_{\mathcal T_{i,n}}
\right]\\
&\quad\le
2C_En^{1-\gamma}
-\frac12\sum_i\mathbb E[W_i\mathbf1_{\mathcal T_{i,n}}]
-\sum_i\mathbb E[\mathsf S_i\mathbf1_{\mathcal T_{i,n}}],
\end{aligned}
\tag{8.4}
\]

and

\[
\sum_i\mathbb E\left[
\left|\frac{e_i}{16}-\frac{W_i}{2}-\mathsf S_i\right|
\mathbf1_{\mathcal T_{i,n}}
\right]
\le 2C_{\rm abs}n^{1-\gamma}.
\tag{8.4a}
\]

where now

\[
\mathcal T_{i,n}=
\left\{
|N_i-\mu_{n,a}|\ge
\frac{19}{40}
+\sqrt{\frac{291\gamma}{5000}(n-1)\log n}
+\frac{2\gamma}{3}\log n
\right\}.
\tag{8.5}
\]

For every fixed `gamma>1`, all stars outside the band (8.5) have total signed
size `o(1)`, not merely `o(n)`.  For example `gamma=3` gives an
`O(n^{-2})` total error outside an `O(sqrt(n log n))` count band.

Splitting (1.1) into the central and tail events, cyclic symmetry yields the
exactly scoped reduction

\[
\begin{aligned}
H_n''(a)
\le{}&n\,\mathbb E\left[
\left(\frac{e_0}{16}-\frac{W_0}{2}-\mathsf S_0\right)
\mathbf1_{\mathcal T_{0,n}^c}
\right]\\
&+2C_En^{1-\gamma}
-\frac n2\mathbb E[W_0\mathbf1_{\mathcal T_{0,n}}]
-n\mathbb E[\mathsf S_0\mathbf1_{\mathcal T_{0,n}}].
\end{aligned}
\tag{8.6}
\]

The estimate is uniform for every `a` on every chord contained in `J`.  If a
future argument proves that the central signed expectation in (8.6) is
nonpositive along such a chord, integrating the actual curvature estimate
costs at most

\[
C_E\,t(1-t)(a_1-a_0)^2 n^{1-\gamma}
\]

in the finite-block Jensen inequality after discarding the two retained
negative tail terms.  This sentence is only an interpretation of the proved
uniform error; the central sign is **not** asserted here.

## 9. What this changes, and what it does not

Before this round, the unpaid term ranged over the complete outside-word law
with no rigorous control on highly weighted rare words.  Theorem 7.1 proves
that, for the growing positive-density Fourier family and uniformly on the
fixed interior interval `J`, every outside count tail beyond an
`O(sqrt(n log n))` band is negligible even after multiplication by `W_i`, by
the true positive star surplus, or by the full signed integrand.  The Fisher
square and nonlinear negative remainder survive with their exact signs.

This is not a finite-rank statement: `rank(P_n)=n/2` grows linearly with `n`.
It is not a value bound differentiated into a Hessian bound: it is proved
directly inside the finite-block curvature identity.

The result does **not** control the central band.  Finite diagnostics show why
that distinction matters: at `n=16`, `a=1/40`, the first words with
`Theta_i>16` occur at the central outside counts `7` and `8`, not in a large
count deviation.  This numerical observation is not used in the proof, but it
prevents an overclaim that the tail theorem has closed all bad stars.

## 10. Dependency table

### Proved in this check-2 file

- The output `L`-ensemble representation specialized to the Fourier projection.
- The exact Schur-complement and precision-matrix formulas (3.2)--(3.4).
- Lemma 4.1, including uniform pair and row bounds under arbitrary conditioning.
- The dimension-free bounds (5.2)--(5.12), uniform in `n`, `a in J`, and every
  outside word.
- The exact outside-count mixture (6.2).
- The self-contained Bernstein estimate and the actual-law tail (6.6).
- The weighted bad-star, weighted-remainder, signed-tail, and absolute-tail
  estimates (7.3)--(7.7).
- The `O(n^{1-gamma})` growing-family consequence and central-band reduction.

### Proved in the preserved check-1 author checkpoint

- The all-odds potential identity and the exact star decomposition (1.1).
- The definitions of `Delta_i G_i`, `W_i`, `e_i`, and `S_i` used here.

These remain author-unreviewed; their full proof is included in the cumulative
archive rather than treated as an external black box.

### Reviewed public inputs used only for scope

- The target, known-range theorem, Fourier/Toeplitz value bridge, and warnings
  against differentiating value errors are as identified in the immutable
  source receipts.  No reviewed result supplies the new tail theorem.

## Gap audit

1. The full sine entropy-rate theorem remains open.
2. The central outside-count band (8.5), which contains probability tending to
   one, is not controlled in sign.
3. No estimate here proves
   `H_n''(a)<=o(n)` on `J`; equation (8.6) isolates the sole remaining extensive
   sector but does not sign it.
4. The theorem does not use or claim posterior decay inherited from the
   unconditional Fourier kernel.
5. The pointwise tests `Theta_i<=16` and individual-star nonpositivity are not
   revived.
6. The constants in (5.11) are explicit but crude.  Improving them alone would
   not settle the central-band sign.
7. No Toeplitz/cyclic value comparison has been differentiated.

## 11. Next exact obligation

Control the representative central-band expectation

\[
\mathbb E\left[
\left(\frac{e_0}{16}-\frac{W_0}{2}-\mathsf S_0\right)
\mathbf1_{\mathcal T_{0,n}^c}
\right]
\]

by `o(1)` from above, or prove a negative constant bound, uniformly for
`a in J`.  The next proof must exploit cancellation inside the central
actual-output law; count concentration alone cannot do it.  Any use of cyclic
Fourier structure must be applied after the full outside-word weights are
present.

## 12. Deterministic replay scope

- `scripts/verify_constants.py` evaluates the exact rational constants and the
  logarithmic constants at 80-digit precision.
- `scripts/verify_fourier_tail.py` exhausts every outside word for
  `n=4,6,8,10` and `a=1/50,1/40,3/100`.  It checks the exact two-binomial count
  mixture numerically, the Schur/precision formulas, every deterministic size
  bound, and finite Bernstein inequalities.
- `exploration/` preserves the seeded diagnostics used while searching.  They
  are explicitly not proofs.  One attempted `n=18` exhaustive diagnostic timed
  out and is not represented as evidence.

The analytical theorem does not depend on any floating-point output.
