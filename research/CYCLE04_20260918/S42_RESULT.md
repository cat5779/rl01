# Harvest provenance — S42, cycle 03 response

Status: AUTHOR_CLAIMS_PENDING_INDEPENDENT_REVIEW.
Acquired via read_thread on 2026-09-18. Complete visible assistant response acquired; attachment cards do not mean attachment file bodies were acquired.
Original citation tokens below are preserved as source text, not independently resolved evidence.

---

# S42 cycle-03 result — an all-scale finite-chord correlation bridge

The cycle-03 prompt asks for a bridge to the **true infinite sine entropy rate**, without assuming that every correlation correction is positive and without exchanging an entropy-rate limit with differentiation. It also says that the reconstructed \(6\)- and \(12\)-site margins are inputs, not an entropy-rate conclusion. citeturn366449view0turn366449view1

The independently reconstructed finite inputs used below are

\[
H_6''(a_0)<-49.5655,\qquad
H_{12}''(a_0)<-126.1801,
\]

\[
(2H_6-H_{12})''(a_0)>27.0490,
\]

and the interval result

\[
H_6''(a)<-44.9,
\qquad
\frac3{200}\le a\le\frac7{200}.
\]

These are finite-block statements; the reconstruction itself does not claim an entropy-rate sign. citeturn366449view2turn366449view3

## Result status

**Proved here**

1. An exact dyadic identity expressing every finite entropy-rate chord as a finite block chord minus a summable sequence of adjacent-block mutual-information chords.
2. A finite signed-ladder version in which the retained scales may have either sign.
3. An explicit bound on every omitted scale under the **actual infinite sine law**, obtained from the sine projection’s number variance.
4. Bounds uniform in every \(0<\rho<1\), every \(0<c<1\), and every legal \(0\le a\le1-c\), including the channel endpoints.
5. At the benchmark \(c=19/20\), an exact quantitative reduction to a finite signed aggregate with a remaining margin of only
   \[
   1.99717043204465\times10^{-6}
   \]
   at dyadic depth \(J=12\).

**Not proved here**

A rigorous lower bound for that remaining finite signed aggregate is not supplied. Therefore the benchmark entropy-rate chord, and hence the full entropy-rate target, remain open.

All entropies below use natural logarithms.

---

# 1. True sine process

Let \(Q_\rho\) be the sine projection on \(\ell^2(\mathbb Z)\),

\[
(Q_\rho)_{ij}=q_{i-j},
\qquad
q_0=\rho,
\qquad
q_r=\frac{\sin(\pi\rho r)}{\pi r}\quad(r\ne0).
\]

For \(0<c<1\) and \(0\le a\le1-c\), define the stationary DPP \(Y^{(a)}\) with kernel

\[
K(a)=aI+cQ_\rho .
\]

Equivalently, if \(X\) has the sine projection law, then conditionally independently over the sites,

\[
\Pr(Y_i=1\mid X)=a+cX_i .
\]

Write

\[
H_L(a)=H(Y_1,\ldots,Y_L),
\qquad
h(a)=\lim_{L\to\infty}\frac{H_L(a)}L.
\]

The limit exists by stationarity and subadditivity. No differentiability of \(h\) is assumed.

For a legal chord radius \(\eta\), let

\[
\Delta_\eta f(a)
=f(a+\eta)+f(a-\eta)-2f(a).
\]

For two adjacent \(L\)-blocks define

\[
J_L(a)
=I_a(Y_1^L;Y_{L+1}^{2L})
=2H_L(a)-H_{2L}(a)\ge0.
\]

---

# 2. Exact dyadic finite-chord bridge

## Theorem 2.1

For every stationary finite-alphabet process, every integer \(m\ge1\), and every legal three-point chord,

\[
\boxed{
\Delta_\eta h(a)
=
\frac{\Delta_\eta H_m(a)}m
-
\sum_{k=0}^{\infty}
\frac{\Delta_\eta J_{m2^k}(a)}{2m2^k}.
}
\tag{2.1}
\]

The series in (2.1) is absolutely convergent.

For \(J\ge0\), put

\[
L_k=m2^k
\]

and define the retained signed aggregate

\[
M_J(a,\eta)
=
\sum_{k=0}^{J-1}
\frac{\Delta_\eta J_{L_k}(a)}{2L_k}.
\tag{2.2}
\]

Then

\[
\boxed{
\Delta_\eta h(a)
\le
\frac{\Delta_\eta H_m(a)}m
-M_J(a,\eta)
+
\sum_{k=J}^{\infty}
\frac{J_{L_k}(a)}{L_k}.
}
\tag{2.3}
\]

No sign is imposed on any retained correction.

### Proof

Let

\[
e_L(a)=\frac{H_L(a)}L.
\]

Stationarity gives

\[
e_L-e_{2L}
=
\frac{2H_L-H_{2L}}{2L}
=
\frac{J_L}{2L}.
\]

Telescoping over \(L=m,2m,4m,\ldots\) and using \(e_{m2^N}\downarrow h\),

\[
e_m(a)-h(a)
=
\sum_{k=0}^{\infty}
\frac{J_{m2^k}(a)}{2m2^k}.
\tag{2.4}
\]

Apply (2.4) at \(a-\eta,a,a+\eta\) and subtract. This proves (2.1), provided the subtraction is legitimate.

It is, because

\[
\left|\Delta_\eta J_L(a)\right|
\le
J_L(a+\eta)+J_L(a-\eta)+2J_L(a),
\]

and each of the three corresponding nonnegative series converges by (2.4). Hence the chord series converges absolutely.

For an omitted scale,

\[
-\Delta_\eta J_L(a)
=
2J_L(a)-J_L(a+\eta)-J_L(a-\eta)
\le2J_L(a),
\]

because mutual information at the two endpoints is nonnegative. Dividing by \(2L\) and summing over \(k\ge J\) proves (2.3). ∎

## Significance

This is not a rewriting with an unnamed total-correlation remainder.

Every retained quantity in \(M_J\) is a finite, signed, actual-law chord. Every unretained scale is charged to the explicit center mutual information \(J_L(a)\). Negative retained scales are allowed.

A future finite computation may therefore provide either separate lower bounds

\[
\Delta_\eta J_{L_k}(a)\ge\mu_k
\]

or one direct aggregate bound

\[
M_J(a,\eta)\ge\underline M_J.
\]

No all-scale positivity hypothesis appears.

---

# 3. Quasi-free majorant for the true sine law

Let

\[
b(x)=-x\log x-(1-x)\log(1-x)
\]

be binary entropy.

For \(A=\{1,\ldots,L\}\), define the number variance of the underlying sine projection,

\[
V_\rho(L)
=
\operatorname{Tr}Q_A(I-Q_A)
=
\sum_{\substack{i\in A\\j\notin A}}
|(Q_\rho)_{ij}|^2.
\tag{3.1}
\]

## Theorem 3.1 — projection-pair bound

Let \(\lambda_1,\ldots,\lambda_L\) be the eigenvalues of the finite compression \(Q_A\). Then

\[
\boxed{
J_L(a)
\le
\sum_{r=1}^{L}g_{a,c}(\lambda_r),
}
\tag{3.2}
\]

where

\[
g_{a,c}(\lambda)
=
b(a+c\lambda)
+b(a+c(1-\lambda))
-b(a)-b(a+c),
\tag{3.3}
\]

and

\[
\boxed{
\sum_{r=1}^{L}\lambda_r(1-\lambda_r)
=
V_\rho(L).
}
\tag{3.4}
\]

### Proof

For a positive contraction \(K\), consider the gauge-invariant quasi-free fermionic state \(\varrho_K\) with one-particle correlation matrix \(K\).

Occupation-number measurement in the site basis has generating function

\[
\operatorname{Tr}\varrho_K\prod_i z_i^{N_i}
=
\det(I-K+KZ),
\]

so its classical outcome distribution is exactly the DPP with kernel \(K\).

Diagonalizing the one-particle matrix gives

\[
S(\varrho_K)=\operatorname{Tr}b(K).
\]

Quantum mutual information is relative entropy. Applying local occupation measurements on \(A\) and a disjoint block \(B\), followed by data processing, yields

\[
I_{\rm classical}(A:B)
\le
I_{\rm quantum}(A:B)
\le
I_{\rm quantum}(A:A^c).
\tag{3.5}
\]

Now use that \(Q_\rho\) is an orthogonal projection on the full infinite one-particle space.

For every nontrivial eigenvalue \(\lambda_r\in(0,1)\) of \(Q_A\), projection algebra supplies an orthonormal complement mode such that on the corresponding two-dimensional subspace,

\[
Q_\rho
=
\begin{pmatrix}
\lambda_r & \sqrt{\lambda_r(1-\lambda_r)}\\
\sqrt{\lambda_r(1-\lambda_r)}&1-\lambda_r
\end{pmatrix}.
\tag{3.6}
\]

The remaining complement modes are uncoupled from \(A\).

On this pair,

\[
K(a)=aI+cQ_\rho
\]

has global one-particle eigenvalues \(a\) and \(a+c\). Its restrictions to the two individual modes have occupancies

\[
a+c\lambda_r,
\qquad
a+c(1-\lambda_r).
\]

Hence that pair contributes

\[
b(a+c\lambda_r)
+b(a+c(1-\lambda_r))
-b(a)-b(a+c)
\]

to quantum mutual information. Summing the paired modes and using (3.5) proves (3.2).

Finally, from \(Q^2=Q\),

\[
Q_{A,A^c}Q_{A^c,A}=Q_A-Q_A^2.
\]

Taking the trace proves (3.4). ∎

This argument uses the true infinite projection. It does **not** assert that the finite Toeplitz compression \(Q_A\) is itself a projection.

---

# 4. Three usable scalar bounds

## 4.1 Strict-interior bound

Suppose

\[
0<a<a+c<1
\]

and define

\[
\beta(a,c)=\min_{x\in[a,a+c]}x(1-x).
\]

Since

\[
g_{a,c}(0)=g_{a,c}(1)=0
\]

and

\[
g_{a,c}''(\lambda)
=
c^2\!\left[
b''(a+c\lambda)
+b''(a+c(1-\lambda))
\right]
\ge
-\frac{2c^2}{\beta(a,c)},
\]

comparison with \(\lambda(1-\lambda)\) gives

\[
\boxed{
J_L(a)
\le
C_{\rm int}(a,c)V_\rho(L),
\qquad
C_{\rm int}(a,c)=\frac{c^2}{\beta(a,c)}.
}
\tag{4.1}
\]

Indeed, if \(C=c^2/\beta\), then

\[
\left[C\lambda(1-\lambda)-g_{a,c}(\lambda)\right]''\le0
\]

and the bracket vanishes at both endpoints, so it is nonnegative.

---

## 4.2 Sharp balanced bound

At

\[
a_0=\frac{1-c}{2},
\qquad
\Lambda_c=\log\frac{1+c}{1-c},
\]

one has the sharper estimate

\[
\boxed{
J_L(a_0)
\le
C_{\rm bal}(c)V_\rho(L),
\qquad
C_{\rm bal}(c)=2c\Lambda_c.
}
\tag{4.2}
\]

### Proof

Binary-entropy symmetry gives

\[
g_{a_0,c}(\lambda)
=
2\left[
b\!\left(\frac{1-c}{2}+c\lambda\right)
-
b\!\left(\frac{1-c}{2}\right)
\right].
\]

For \(0\le\lambda\le1/2\), define

\[
F(\lambda)
=
c\Lambda_c\lambda(1-\lambda)
-
\left[
b\!\left(\frac{1-c}{2}+c\lambda\right)
-
b\!\left(\frac{1-c}{2}\right)
\right].
\]

Put \(x=1-2\lambda\). Then

\[
b'\!\left(\frac{1-cx}{2}\right)
=
2\operatorname{arctanh}(cx).
\]

Because \(\operatorname{arctanh}\) is convex and vanishes at zero,

\[
\operatorname{arctanh}(cx)
\le
x\operatorname{arctanh}(c).
\]

Therefore \(F'(\lambda)\ge0\), while \(F(0)=0\). Reflection around \(1/2\) proves

\[
g_{a_0,c}(\lambda)
\le
2c\Lambda_c\lambda(1-\lambda).
\]

Sum over the eigenvalues and use (3.4). ∎

The coefficient \(2c\Lambda_c\) is tangent-sharp as \(\lambda\to0\) or \(1\).

---

## 4.3 Endpoint-safe bound

The strict-interior coefficient diverges at \(a=0\) and \(a=1-c\). The following different estimate preserves the complete legal range.

For binary entropy,

\[
|b(x)-b(y)|\le b(|x-y|).
\tag{4.3}
\]

A self-contained proof is obtained by coupling Bernoulli variables of means \(x,y\) with mismatch probability \(|x-y|\), then using

\[
H(U)\le H(V)+H(U\mid V).
\]

Let

\[
s=\lambda(1-\lambda),
\qquad
d=\min(\lambda,1-\lambda).
\]

The two entropy differences in \(g_{a,c}\) each involve arguments separated by \(cd\), hence

\[
g_{a,c}(\lambda)
\le2b(cd).
\]

Since \(d\le2s\) and \(2cs\le c/2<1/2\),

\[
g_{a,c}(\lambda)\le2b(2cs).
\]

Jensen’s inequality now gives, uniformly for every \(0\le a\le1-c\),

\[
\boxed{
J_L(a)
\le
2L\,b\!\left(\frac{2cV_\rho(L)}L\right).
}
\tag{4.4}
\]

Using

\[
b(x)\le x(1-\log x)
\]

gives

\[
\boxed{
J_L(a)
\le
4cV_\rho(L)
\left[
1+\log\frac{L}{2cV_\rho(L)}
\right].
}
\tag{4.5}
\]

Because \(V_\rho(L)\le L/4\), the logarithm is positive.

This is the endpoint-safe component needed to retain the full \(0<c<1\), \(0\le a\le1-c\) target.

---

# 5. Actual sine number variance

For the density-\(\rho\) sine projection,

\[
\boxed{
V_\rho(L)
=
\frac{2}{\pi^2}
\sum_{r=1}^{\infty}
\frac{\min(r,L)\sin^2(\pi\rho r)}{r^2}.
}
\tag{5.1}
\]

Indeed, for each distance \(r\), exactly \(2\min(r,L)\) ordered pairs cross the two boundaries of the interval.

Uniformly in \(0<\rho<1\),

\[
\boxed{
V_\rho(L)\le
\frac{2}{\pi^2}(\log L+2).
}
\tag{5.2}
\]

At half density,

\[
\boxed{
V_{1/2}(L)
=
\frac{2}{\pi^2}
\left[
\sum_{\substack{1\le r\le L\\r\ {\rm odd}}}\frac1r
+
L\sum_{\substack{r>L\\r\ {\rm odd}}}\frac1{r^2}
\right].
}
\tag{5.3}
\]

An elementary bound is

\[
V_{1/2}(L)\le\frac{\log L+4}{\pi^2}.
\tag{5.4}
\]

For even \(L\), a sharper estimate is

\[
\boxed{
V_{1/2}(L)
\le
\frac{\log L+\gamma+\log2+1+1/(3L^2)}{\pi^2}.
}
\tag{5.5}
\]

To see this, write \(L=2M\). Then

\[
\sum_{\substack{r\le L\\r\ {\rm odd}}}\frac1r
=
H_{2M}-\frac12H_M
\le
\frac12\log L
+\frac12(\gamma+\log2)
+\frac1{6L^2},
\]

while midpoint comparison for the convex function \(x^{-2}\) gives

\[
L\sum_{\substack{r>L\\r\ {\rm odd}}}\frac1{r^2}
\le\frac12.
\]

---

# 6. Summable all-scale tails

Suppose

\[
J_L(a)\le C V_{1/2}(L).
\]

For even \(L\),

\[
\sum_{j=0}^{\infty}
\frac{J_{2^jL}(a)}{2^jL}
\le
R_{\rm sharp}(C,L),
\]

where

\[
\boxed{
R_{\rm sharp}(C,L)
=
\frac{2C}{\pi^2L}
\left(\log L+\gamma+1+2\log2\right)
+
\frac{8C}{21\pi^2L^3}.
}
\tag{6.1}
\]

This follows by inserting (5.5) and using

\[
\sum_{j\ge0}2^{-j}=2,\qquad
\sum_{j\ge0}j2^{-j}=2,\qquad
\sum_{j\ge0}8^{-j}=\frac87.
\]

A simpler bound is

\[
\boxed{
R_{\rm elem}(C,L)
=
\frac{2C}{\pi^2L}
\left(\log L+4+\log2\right).
}
\tag{6.2}
\]

Uniformly in density,

\[
\boxed{
R_{\rho,{\rm univ}}(C,L)
=
\frac{4C}{\pi^2L}
\left(\log L+2+\log2\right).
}
\tag{6.3}
\]

Thus the true omitted-scale tail is

\[
O\!\left(\frac{\log L}{L}\right).
\]

## Endpoint-safe tail

At half density, combining (4.5) and (5.4) gives

\[
\boxed{
R_{{\rm all},1/2}(c,L)
=
\frac{4c}{\pi^2L}
\left[
2AB+2r(A+B)+6r^2
\right],
}
\tag{6.4}
\]

where

\[
A=\log L+4,
\quad
B=1+\log L+\log\frac{\pi^2}{2c},
\quad
r=\log2.
\]

Uniformly in density one may use

\[
\boxed{
R_{{\rm all},{\rm univ}}(c,L)
=
\frac{4c}{\pi^2L}
\left[
2AB+2r(A+2B)+12r^2
\right],
}
\tag{6.5}
\]

with

\[
A=2\log L+4,
\qquad
B=1+\log L+\log\frac{\pi^2}{2c}.
\]

These are \(O((\log L)^2/L)\), but unlike the strict-interior coefficient they remain valid at \(a=0\) and \(a=1-c\).

---

# 7. Master finite certificate

## Theorem 7.1

Let \(L_k=m2^k\). Suppose a finite computation or finite-scale theorem supplies rigorous lower bounds

\[
\Delta_\eta J_{L_k}(a)\ge\mu_k,
\qquad 0\le k<J.
\]

Set

\[
\underline M_J
=
\sum_{k=0}^{J-1}\frac{\mu_k}{2L_k}.
\]

Then, at a strict-interior center,

\[
\boxed{
\Delta_\eta h(a)
\le
\frac{\Delta_\eta H_m(a)}m
-\underline M_J
+R(C,L_J),
}
\tag{7.1}
\]

where

\[
C=C_{\rm int}(a,c)
\]

or, at \(a=(1-c)/2\),

\[
C=C_{\rm bal}(c),
\]

and \(R\) may be chosen from (6.1)–(6.3).

At arbitrary legal \(a\), including either endpoint, use (6.4) or (6.5).

Consequently,

\[
\frac{\Delta_\eta H_m(a)}m-\underline M_J+R(C,L_J)<0
\]

is a complete finite certificate for the true entropy-rate chord.

The \(\mu_k\) may be negative. There is no individual positivity obligation.

## Shrinking chords

If the seed has the form

\[
\frac{\Delta_\eta H_m(a)}m\le-M\eta^2,
\]

the interior tail becomes \(o(\eta^2)\) by taking

\[
L_J\asymp \eta^{-2}\log(1/\eta).
\]

The endpoint-safe estimate requires only

\[
L_J\asymp \eta^{-2}\log^2(1/\eta).
\]

This gives an explicit scale rate compatible with the full local-concavity target.

---

# 8. Benchmark \(c=19/20\)

Take

\[
\rho=\frac12,
\qquad
c=\frac{19}{20},
\qquad
a_0=\frac1{40},
\qquad
\eta=\frac1{100},
\qquad
m=6.
\]

The reconstructed interval bound

\[
H_6''(a)<-44.9
\quad\text{on}\quad
[a_0-\eta,a_0+\eta]
\]

implies, using the triangular second-difference kernel,

\[
\Delta_\eta H_6(a_0)
=
\int_{-\eta}^{\eta}
(\eta-|s|)H_6''(a_0+s)\,ds
\le-44.9\eta^2.
\]

Hence

\[
\boxed{
\frac{\Delta_\eta H_6(a_0)}6
\le
-\frac{44.9\eta^2}{6}
=
-0.000748333333333333\ldots .
}
\tag{8.1}
\]

At the balanced center,

\[
C_{\rm bal}
=
2c\log\frac{1+c}{1-c}
=
\frac{19}{10}\log39
=
6.960767127646328\ldots .
\tag{8.2}
\]

The sharp actual-law tails are:

| Retained depth \(J\) | Tail starts at \(L_J=6\cdot2^J\) | \(R_{\rm sharp}\) | \(R_{\rm sharp}-44.9\eta^2/6\) |
|---:|---:|---:|---:|
| 11 | 12,288 | 0.00142109425870536 | \(+0.000672760925372027\) |
| 12 | 24,576 | 0.000750330503765378 | **\(+0.000001997170432045\)** |
| 13 | 49,152 | 0.000395056939109401 | **\(-0.000353276394223932\)** |

Therefore:

### Depth \(J=12\)

A rigorous bound

\[
\boxed{
M_{12}(a_0,\eta)
>
1.99717043204465\times10^{-6}
}
\tag{8.3}
\]

would prove

\[
\Delta_\eta h(a_0)<0.
\]

This is the weighted aggregate of the twelve finite corrections at scales

\[
6,12,\ldots,12288.
\]

They do not need to be individually positive.

### Depth \(J=13\)

It is enough to prove

\[
\boxed{
M_{13}(a_0,\eta)
>
-3.53276394223932\times10^{-4}.
}
\tag{8.4}
\]

Thus the first thirteen corrections may have a moderately negative total and the true all-scale chord still follows.

## Relation to the reconstructed first doubling

The reconstructed point margin is

\[
J_6''(a_0)
=
(2H_6-H_{12})''(a_0)
>27.0490.
\]

Were this upgraded to a rigorous finite-chord lower bound over the benchmark interval, its first weighted contribution would be approximately

\[
\frac{27.0490\eta^2}{12}
=
2.2540833333\times10^{-4}.
\]

That is over one hundred times the deficit in (8.3). But this comparison is explicitly **conditional**: a point curvature lower bound alone is not a finite-chord certificate.

---

# 9. Computational evidence

The attached optional finite enumeration uses the true Toeplitz DPP kernels at \(n=6\) and \(n=12\), enumerating every word in ordinary IEEE double precision.

On the grid

\[
a=0.015,0.016,\ldots,0.035,
\]

it found

\[
\min_{\rm grid}
(2H_6''-H_{12}'')
=
27.0490860822059\ldots
\]

at \(a=0.025\), with larger values toward both endpoints.

Direct endpoint evaluation of the finite chord gave

\[
\Delta_\eta J_6(a_0)
=
0.00278611912298032\ldots,
\]

and therefore

\[
\frac{\Delta_\eta J_6(a_0)}{12}
=
0.000232176593581694\ldots .
\]

This is strong evidence that the first correction is favorable across the benchmark chord. It is not an interval enclosure and is not used as a proved input.

The analytic tail formulas themselves are rigorous; their displayed decimal evaluations are high-precision numerical evaluations rather than outward-rounded interval balls.

---

# 10. Legal obstruction to a fixed unsigned remainder

The bridge identifies a useful obstruction.

Suppose one fixes a scale \(L_J\), has a seed

\[
\frac{\Delta_\eta H_m(a)}m\le-M\eta^2,
\]

and controls all omitted corrections only by mutual-information nonnegativity. Then the conclusion has the form

\[
\Delta_\eta h(a)
\le
-M\eta^2+R_J,
\]

where \(R_J>0\) does not shrink with \(\eta\).

It therefore fails whenever

\[
0<\eta<\sqrt{R_J/M}.
\]

Thus no fixed-scale unsigned center-value remainder can establish a genuine neighborhood of local concavity.

At least one of the following is necessary:

1. an adaptive scale \(J(\eta)\to\infty\);
2. signed finite-chord control on the retained scales;
3. a new chord-sensitive tail carrying its own \(\eta^2\) factor.

This explains precisely why neither the finite block margin alone nor the favorable first doubling alone completes the rate argument.

---

# Conclusion

The completed mathematical result is

\[
\boxed{
\text{true-sine all-scale finite-chord bridge proved,}
}
\]

with

\[
\boxed{
\text{no all-scale positivity assumption and no rate differentiation.}
}
\]

At the benchmark, the infinite-volume obstruction has been reduced to the finite signed condition

\[
M_{12}>1.99717043204465\times10^{-6},
\]

or the more tolerant depth-\(13\) condition

\[
M_{13}>-3.53276394223932\times10^{-4}.
\]

The remaining finite signed aggregate has not been certified here, so the benchmark entropy-rate sign and the ultimate all-\(0<c<1\) target remain open.

## Files

- :chatgpt-content-reference{index="3"}
- :chatgpt-content-reference{index="4"}
- :chatgpt-content-reference{index="5"}
- :chatgpt-content-reference{index="6"}
- :chatgpt-content-reference{index="7"}
- :chatgpt-content-reference{index="8"}

