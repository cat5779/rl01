# RESULT.md — Quadratic-cut acceleration control and an actual-law rate bridge

:chatgpt-content-reference{index="2"} · :chatgpt-content-reference{index="3"} · :chatgpt-content-reference{index="4"}

**The unrestricted all-density high-contrast target remains INCOMPLETE.** The results obtained here are an all-size actual-law acceleration estimate, exact accounting of its accumulation through blocking, a paid but extremely narrow high-contrast entropy-rate theorem, and a certified obstruction to entrywise positivity of mixed diagonal information derivatives.

The principal estimate is
\[
\boxed{|C_{\mathrm{acc}}|\le B_\delta\|K_{AB}\|_{\mathrm{HS}}^2,
\qquad B_\delta\le 6\delta^{-12}.}
\]
Its cost telescopes into the finite-compression leakage
\[
\operatorname{tr}(Q_{\rho,L}-Q_{\rho,L}^2).
\]
This is a proved bound on the unresolved term, not an equivalent reformulation.

The accepted Fisher inequality \(D_F\ge0\) and the audited two-site seed are used as inputs from the supplied packet. Neither S71 nor the affine-mixture obstruction is re-proved; S73 is not used. citeturn351960view0turn374335view0

---

## 1. The mathematical tool

### Input class

Let
\[
K(a)=T+aI,\qquad
\delta I\preceq K(a)\preceq(1-\delta)I
\quad(a\in J),
\]
where \(T\) is Hermitian, \(J\) is a compact interval, and \(0<\delta\le1/2\).

Partition the finite ground set into blocks \(A,B\), and put
\[
X=K_{AB}=T_{AB}.
\]
Thus the cross-block matrix is independent of \(a\). All entropies below are full configuration Shannon entropies in nats.

Define
\[
r=\frac{\delta}{1-\delta},
\]
\[
L_\delta=
\frac{2}{r^2\delta}
+\frac{1}{r^5\delta^2}
+\frac{1}{r^6\delta^3},
\]
and
\[
\boxed{
B_\delta=\frac{4L_\delta}{\delta^3}
+\frac{2}{r^4\delta^4}.
}
\tag{1}
\]

### Output inequality

For the actual DPP law,
\[
\boxed{
|C_{\mathrm{acc}}(a)|
\le B_\delta\|X\|_{\mathrm{HS}}^2.
}
\tag{2}
\]
Consequently, using the accepted \(D_F\ge0\),
\[
\boxed{
M''(a)\ge-B_\delta\|X\|_{\mathrm{HS}}^2.
}
\tag{3}
\]

The constant is independent of the block sizes. It is conservative in the contraction gap.

The proof below retains every mixed coordinate contribution and every configuration.

---

## 2. Cofactor integration by parts

Write \(s_i=2y_i-1\). Differentiation with respect to the single diagonal coordinate \(K_{ii}\) gives
\[
\partial_iP_K(y)
=s_iP_{K_{-i}}(y_{-i}),
\]
and, for \(i\ne j\),
\[
\partial_i\partial_jP_K(y)
=s_is_jP_{K_{-\{i,j\}}}(y_{-\{i,j\}}).
\tag{4}
\]
Also \(\partial_i^2P_K(y)=0\).

These are cofactor identities for the actual atoms. The deleted-coordinate probabilities are the actual DPP marginals.

For a function \(g\), define
\[
\Delta_{ij}g(z)
=g(1,1,z)+g(0,0,z)-g(1,0,z)-g(0,1,z).
\]
Along the common identity shift, (4) implies
\[
\sum_yP_K''(y)g(y)
=
2\sum_{i<j}
\mathbb E_{Y_{-\{i,j\}}}\Delta_{ij}g.
\tag{5}
\]
Here \(g\) is frozen when applying this identity.

Define the conditional log-odds potential
\[
W(K,y)=\sum_{i<j}\Delta_{ij}\log P_K(y).
\tag{6}
\]
Each summand is independent of the displayed pair of bits, so its expectation under the deleted-coordinate marginal equals its expectation under the full law.

Let
\[
K^{(0)}=K_A\oplus K_B.
\]
Apply (5) to
\[
\ell=\log P_K-\log P_{K_A}-\log P_{K_B}
\]
in the accepted acceleration formula. This gives
\[
\boxed{
C_{\mathrm{acc}}
=
2\mathbb E_{P_K}
\big[W(K,Y)-W(K^{(0)},Y)\big].
}
\tag{7}
\]

For pairs inside a block, this subtracts the corresponding marginal conditional log odds. For cross-block pairs, the marginal differences vanish. Thus the moving marginal references have not been discarded.

Identity (7) is preparatory. The substantive estimate is the following pointwise cut bound.

---

## 3. A dimension-independent pointwise cut estimate

### 3.1 Masked resolvents and conditional odds

Fix a configuration \(y\), and write
\[
R=\bigl(K-\operatorname{diag}(1-y)\bigr)^{-1},
\qquad
b_i=s_iR_{ii}-1.
\]
The masked matrix equals
\[
\frac12\operatorname{diag}(s_i)
+\left(K-\frac12I\right).
\]
Its smallest singular value is at least \(\delta\), hence
\[
\|R\|_{\mathrm{op}}\le\delta^{-1}.
\tag{8}
\]

If
\[
q_i=P(Y_i=y_i\mid Y_{-i}=y_{-i}),
\]
the first cofactor identity gives
\[
R_{ii}=\frac{s_i}{q_i}.
\]
Applying (8) both before and after flipping bit \(i\) proves
\[
\delta\le q_i\le1-\delta,
\qquad
r\le b_i=\frac{1-q_i}{q_i}\le r^{-1}.
\tag{9}
\]
This holds for every word.

For \(i\ne j\), put
\[
\sigma_{ij}=s_is_j,
\qquad
x_{ij}=\frac{|R_{ij}|^2}{b_ib_j}.
\]
If \(y^i\) and \(y^{ij}\) denote the corresponding flipped words, the determinant lemma gives
\[
\frac{P(y)P(y^{ij})}{P(y^i)P(y^j)}
=1-\sigma_{ij}x_{ij}.
\]
When the two bits agree, this is the conditional odds ratio; otherwise it is its reciprocal. Therefore
\[
\boxed{
W(K,y)=
\sum_{i<j}\sigma_{ij}
\log(1-\sigma_{ij}x_{ij}).
}
\tag{10}
\]

For \(\sigma_{ij}=1\), the ratio is a ratio of two one-site conditional odds. By (9), it is at least \(r^2\). For \(\sigma_{ij}=-1\), the denominator is \(1+x_{ij}\ge1\). Thus
\[
1-\sigma_{ij}x_{ij}\ge r^2.
\tag{11}
\]

### 3.2 An operator-norm bound for the gradient

Treat the right side of (10) as a function of the Hermitian matrix \(R\), with the signs fixed. Its differential is
\[
dW=\operatorname{tr}(G\,dR),
\]
where, for \(i\ne j\),
\[
G_{ij}
=
-\frac{R_{ij}}
{b_ib_j(1-\sigma_{ij}x_{ij})},
\tag{12}
\]
and
\[
G_{ii}
=
\frac{s_i}{b_i}
\sum_{j\ne i}
\frac{x_{ij}}{1-\sigma_{ij}x_{ij}}.
\tag{13}
\]

I claim
\[
\boxed{\|G\|_{\mathrm{op}}\le L_\delta.}
\tag{14}
\]

Let \(D=\operatorname{diag}(b_i^{-1})\). Split the off-diagonal part of \(G\) into
\[
-\operatorname{offdiag}(DRD)
\]
and a remainder. The first part has operator norm at most
\[
2\|D\|_{\mathrm{op}}^2\|R\|_{\mathrm{op}}
\le 2r^{-2}\delta^{-1}.
\]

Using
\[
\frac1{1-\sigma x}-1
=\frac{\sigma x}{1-\sigma x},
\]
the remainder has entries bounded by
\[
r^{-6}|R_{ij}|^3.
\]
For every row,
\[
\sum_j|R_{ij}|^3
\le
\left(\max_j|R_{ij}|\right)\sum_j|R_{ij}|^2
\le\delta^{-3}.
\]
The Hermitian remainder therefore has operator norm at most
\[
r^{-6}\delta^{-3}.
\]

Finally, (13) gives
\[
|G_{ii}|
\le r^{-5}\sum_j|R_{ij}|^2
\le r^{-5}\delta^{-2}.
\]
Adding the three estimates proves (14).

This step replaces the apparent number of mixed terms by operator and row-square bounds. No factor of the number of sites remains.

### 3.3 Quadratic dependence on the cut

At a fixed \(a\), consider
\[
K_t=K_A\oplus K_B+tE,
\qquad
E=
\begin{pmatrix}
0&X\\
X^*&0
\end{pmatrix},
\qquad 0\le t\le1.
\]
For \(U=I_A\oplus(-I_B)\),
\[
K_t=\frac{1+t}{2}K+\frac{1-t}{2}UKU^*.
\]
Every \(K_t\) therefore has the same contraction margin \(\delta\).

This is an interpolation of kernels. It is **not** an affine mixture of endpoint probability laws.

Write
\[
R_t=\bigl(K_t-\operatorname{diag}(1-y)\bigr)^{-1},
\qquad x=\|X\|_{\mathrm{HS}}.
\]
The block resolvent equation gives
\[
(R_t)_{AB}
=-t(R_0)_{AA}X(R_t)_{BB},
\]
so
\[
\|(R_t)_{AB}\|_{\mathrm{HS}}
\le t\delta^{-2}x.
\tag{15}
\]

Because \(R_t'=-R_tER_t\),
\[
\|(R_t')_{AA}\|_1+\|(R_t')_{BB}\|_1
\le4t\delta^{-3}x^2.
\tag{16}
\]
For example,
\[
(R_t')_{AA}
=-(R_t)_{AA}X(R_t)_{BA}
 -(R_t)_{AB}X^*(R_t)_{AA},
\]
and each term is bounded using (8), (15), and
\[
\|UV\|_1\le\|U\|_{\mathrm{HS}}\|V\|_{\mathrm{HS}}.
\]

Also
\[
\|R_t'\|_{\mathrm{HS}}
\le\delta^{-2}\|E\|_{\mathrm{HS}}
=\sqrt2\,\delta^{-2}x.
\]
Since the two off-diagonal blocks of a Hermitian matrix have equal Hilbert–Schmidt norm,
\[
\|(R_t')_{AB}\|_{\mathrm{HS}}
\le\delta^{-2}x.
\tag{17}
\]

Equations (11), (12), and (15) imply
\[
\|(G_t)_{AB}\|_{\mathrm{HS}}
\le r^{-4}\|(R_t)_{AB}\|_{\mathrm{HS}}
\le tr^{-4}\delta^{-2}x.
\tag{18}
\]

Pair the diagonal blocks of \(\operatorname{tr}(G_tR_t')\) using operator/trace norms, and the off-diagonal blocks using Hilbert–Schmidt norms. Equations (14), (16)–(18) yield
\[
\left|\frac{d}{dt}W(K_t,y)\right|
\le
\left(
4tL_\delta\delta^{-3}
+2tr^{-4}\delta^{-4}
\right)x^2.
\]
Integration gives the pointwise bound
\[
\boxed{
|W(K,y)-W(K^{(0)},y)|
\le
\left(
2L_\delta\delta^{-3}
+r^{-4}\delta^{-4}
\right)\|X\|_{\mathrm{HS}}^2.
}
\tag{19}
\]

Taking the expectation in (7) proves (2). The accepted Fisher inequality proves (3).

Finally, \(r\ge\delta\) implies
\[
\begin{aligned}
B_\delta
&\le
8\delta^{-6}+4\delta^{-10}
+4\delta^{-12}+2\delta^{-8}\\
&=
\delta^{-12}
\left(4+4\delta^2+2\delta^4+8\delta^6\right)
\le6\delta^{-12},
\end{aligned}
\tag{20}
\]
because \(\delta\le1/2\).

This completes the all-size acceleration estimate.

---

## 4. Exact accumulation through blocking

Fix a leaf size \(L\), and merge \(q\) adjacent leaves into an interval of length \(qL\).

Every unordered pair of sites in different leaves lies across exactly one cut in a binary merge tree: the cut at its lowest common ancestor. Therefore
\[
\boxed{
\sum_{\text{merges}}\|K_{AB}\|_{\mathrm{HS}}^2
=
\frac{c^2}{2}
\left[
\operatorname{tr}Q_{\rho,qL}^2
-q\operatorname{tr}Q_{\rho,L}^2
\right].
}
\tag{21}
\]
Thus every mixed cross-leaf contribution is charged once, not once per scale.

Applying (3) at every merge, with the same \(B_\delta\), gives
\[
F_{qL}(a)\ge qF_L(a)
-\frac{B_\delta c^2}{2}
\left[
\operatorname{tr}Q_{\rho,qL}^2
-q\operatorname{tr}Q_{\rho,L}^2
\right].
\tag{22}
\]

The finite sine compression is a contraction, not generally a projection. Writing
\[
q_r=\frac{\sin(\pi\rho r)}{\pi r},
\qquad q_0=\rho,
\]
we have
\[
\frac1N\operatorname{tr}Q_{\rho,N}^2
=
\sum_{|r|<N}
\left(1-\frac{|r|}{N}\right)|q_r|^2
\longrightarrow
\sum_{r\in\mathbb Z}|q_r|^2=\rho.
\tag{23}
\]
The last equality is Parseval for the indicator of a Fourier interval of length \(\rho\); square summability justifies dominated convergence.

Define
\[
D_{\rho,L}
=\operatorname{tr}(Q_{\rho,L}-Q_{\rho,L}^2),
\]
and, with \(c,\rho\) fixed,
\[
\operatorname{Gap}_\lambda f
=f((1-\lambda)a_0+\lambda a_1)
-(1-\lambda)f(a_0)-\lambda f(a_1),
\qquad \Delta=a_1-a_0.
\]

Integrate (22) while the volume is finite:
\[
\begin{aligned}
\operatorname{Gap}_\lambda H_{qL}
\ge{}&
q\operatorname{Gap}_\lambda H_L\\
&-\frac{B_\delta c^2}{4}
\left[
\operatorname{tr}Q_{\rho,qL}^2
-q\operatorname{tr}Q_{\rho,L}^2
\right]
\lambda(1-\lambda)\Delta^2.
\end{aligned}
\]
Divide by \(qL\), then use the entropy-value limits and (23). This proves the actual-law bridge
\[
\boxed{
\operatorname{Gap}_\lambda h
\ge
\frac{\operatorname{Gap}_\lambda H_L}{L}
-\frac{B_\delta c^2D_{\rho,L}}{4L}
\lambda(1-\lambda)\Delta^2.
}
\tag{24}
\]

In particular, a certified seed \(F_L(a)\ge f_L\) on the entire compact interval gives
\[
\boxed{
\operatorname{Gap}_\lambda h
\ge\frac{\kappa_L}{2}\lambda(1-\lambda)\Delta^2,
\qquad
\kappa_L=
\frac{f_L}{L}
-\frac{B_\delta c^2D_{\rho,L}}{2L}.
}
\tag{25}
\]

**The payment condition is \(\kappa_L>0\), not merely \(f_L>0\).**

No limit of \(H_N''/N\) was taken. No monotonicity of \(F_N/N\) for every \(N\), and no Dini argument, is used. The conclusion is a rate chord inequality; it does not require twice differentiability of \(h\).

For completeness, the leakage is explicitly
\[
D_{\rho,L}
=\frac2{\pi^2}
\left[
\sum_{r=1}^{L-1}\frac{\sin^2(\pi\rho r)}r
+
L\sum_{r\ge L}\frac{\sin^2(\pi\rho r)}{r^2}
\right],
\]
and
\[
D_{\rho,L}\le
\min\left\{
L\rho(1-\rho),
\frac2{\pi^2}(\log L+3)
\right\}.
\tag{26}
\]
The final accumulated penalty is exactly the one in (25), rather than an unspecified logarithmic error per merge.

---

## 5. A paid high-contrast region

### One-site seed

The observed marginal is
\[
t=a+c\rho,
\]
not the noise bias \(p_{\mathrm{noise}}=a/(1-c)\). Hence
\[
F_1(a)=\frac1{t(1-t)}\ge4,
\qquad
D_{\rho,1}=\rho(1-\rho).
\]
Equations (20) and (25) give
\[
\boxed{
\kappa_1\ge
4-3c^2\delta^{-12}\rho(1-\rho).
}
\tag{27}
\]

Therefore, for every fixed \(c\in(37/40,1)\) and every fixed compact legal interval \(J\), the tool proves strict rate concavity on the explicit density region
\[
\boxed{
\rho(1-\rho)<\frac{4\delta^{12}}{3c^2}.
}
\tag{28}
\]
For example,
\[
\min\{\rho,1-\rho\}
\le\frac{2\delta^{12}}{3c^2}
\]
implies \(\kappa_1\ge2\).

### An exact product-domain budget

Consider
\[
\frac{37}{40}\le c\le\frac{19}{20},
\qquad
\frac1{50}\le a\le\frac3{100},
\qquad
0<\min\{\rho,1-\rho\}\le10^{-21}.
\tag{29}
\]
The common contraction margin is \(\delta=1/50\). Exact rational arithmetic gives
\[
4-3\left(\frac{19}{20}\right)^2 50^{12}10^{-21}
=\frac{27353}{8192}
=3.3389892578125.
\]
Thus, for each fixed \(c,\rho\) in this region and every chord in the displayed \(a\)-interval,
\[
\boxed{
\operatorname{Gap}_\lambda h
\ge
\frac{27353}{16384}
\lambda(1-\lambda)(a_1-a_0)^2.
}
\tag{30}
\]

This is a genuine full-configuration entropy-rate certificate. The product region follows from a uniform analytic bound, not from multiplying independently audited numerical rectangles.

**Its density width is extremely small.** Equation (28) supplies corresponding regions for every fixed high contrast and compact interior parameter interval, but does not cover every density or all legal biases at a fixed positive density.

### The half-density two-site seed is not paid

At half density,
\[
D_{1/2,2}=\frac12-\frac2{\pi^2}>0.
\]
Using the accepted seed gives the candidate
\[
\kappa_2=
\frac{8+C(c^2/\pi^2)}2
-\frac{B_\delta c^2}{4}
\left(\frac12-\frac2{\pi^2}\right).
\tag{31}
\]

For \(c=19/20\), \(J=[1/50,3/100]\),
\[
B_\delta\approx8.654336163038125\times10^{20},
\]
and (31) is approximately
\[
-5.806308012581715\times10^{19}.
\]
The budget fails decisively.

Indeed, the audited bias-uniform two-site lower bound does not pay this conservative constant anywhere in the high-contrast range. There,
\[
\delta<3/80<1/4,\qquad r<1,
\]
so \(B_\delta>16384\). Also
\[
\frac{c^2}{4}\left(\frac12-\frac2{\pi^2}\right)>\frac1{20},
\]
whereas
\[
\frac{8+C(c^2/\pi^2)}2<\frac{36}{5}.
\]
Thus this particular seed budget is negative throughout that range.

Failure of this sufficient budget is not failure of rate concavity.

---

## 6. Certified actual-sine obstruction to entrywise mixed positivity

Take
\[
N=6,\quad \rho=\frac12,\quad c=\frac{19}{20},
\quad a=\frac1{40},
\]
with
\[
A=\{1,2,3\},\qquad B=\{4,5,6\}.
\]
This is the actual midpoint sine kernel
\[
K=\frac12I+\beta T,\qquad \beta=\frac{19}{20\pi},
\]
where \(T_{ii}=0\), \(T_{ij}=0\) at nonzero even distances, and
\[
T_{ij}=\frac{(-1)^{(|i-j|-1)/2}}{|i-j|}
\]
at odd distances.

Let \(\mathcal M(u,v)\) be actual DPP block information at
\[
K(u,v)=K+ue_1e_1^*+ve_6e_6^*.
\]
The base point is exactly the frozen sine law. Away from the base point, these are diagonal-coordinate perturbations, not common-identity sine shifts.

Since the directions are in different blocks,
\[
\mathcal M_{uv}(0,0)
=
\sum_y\frac{(\partial_1P_y)(\partial_6P_y)}{P_y}
+\sum_y(\partial_1\partial_6P_y)\log P_y.
\tag{32}
\]

The executed directed-integer interval certificate proves
\[
\boxed{
-0.0003790922420416860133
<
\mathcal M_{uv}(0,0)
<
-0.0003790922420416860132.
}
\tag{33}
\]

It also proves, uniformly for \(0\le u,v\le\varepsilon=10^{-10}\),
\[
-0.0003791099694534979385
<
\mathcal M_{uv}(u,v)
<
-0.0003790745146298547933
<-\frac3{10000}.
\]
Therefore
\[
\boxed{
\begin{aligned}
&\mathcal M(\varepsilon,\varepsilon)
-\mathcal M(\varepsilon,0)
-\mathcal M(0,\varepsilon)
+\mathcal M(0,0)\\
&\hspace{35mm}<-3\times10^{-24}.
\end{aligned}}
\tag{34}
\]

This falsifies the shortcut that every mixed diagonal rectangle defect can be taken nonnegative. It does **not** falsify positive semidefiniteness of the full diagonal Hessian or convexity in the common identity direction.

At precisely the same sine base point, the certificate gives
\[
32.5907519603242448559425
<D_F<
32.5907519603242448559426,
\]
\[
-18.8409844899709791046131
<C_{\mathrm{acc}}<
-18.8409844899709791046130,
\]
and hence
\[
\boxed{
13.7497674703532657513294
<M_{3,3}''
<
13.7497674703532657513295.
}
\tag{35}
\]
Thus this is **not** a finite sine counterexample to \(M''\ge0\).

### Certification method and actual execution

:chatgpt-content-reference{index="5"} was executed successfully. It uses Python integers and directed fixed-point intervals at 65 decimal places—not floating-point signs.

Its \(\pi\) enclosure uses Machin’s identity
\[
\pi=16\arctan(1/5)-4\arctan(1/239),
\]
with 90 alternating-series terms and a signed next-term remainder. Determinants use a division-free subset recurrence. Every one of the 64 six-site atoms is included and certified positive. Derivatives use (4) and actual marginal sums.

Logarithms are rescaled to \(1\le x\le2\), then evaluated through
\[
\log x=2\sum_{k\ge0}\frac{z^{2k+1}}{2k+1},
\qquad z=\frac{x-1}{x+1}.
\]
After 85 terms, the positive remainder is bounded by
\[
\frac{2z^{171}}{171(1-z^2)}.
\]
All arithmetic is rounded outward. Interval diagonals give the uniform rectangle certificate. The strictness of the printed decimal bounds was separately checked.

A separate executed diagnostic tested the odds representation, acceleration identity, and resolvent gradient on 34 finite kernels. Its maximum absolute acceleration-identity residual was about \(1.42\times10^{-14}\); its maximum normalized gradient residual was about \(3.26\times10^{-10}\). These are floating-point diagnostics, not proofs. The all-size theorem rests on the analytic argument above.

---

## 7. Hypothesis map and final ledger

| Ingredient | Exact role and scope |
|---|---|
| Accepted S71 input | Supplies \(D_F\ge0\) for the actual common identity direction. |
| Cofactor/odds argument | Finite strict Hermitian contractions; every configuration retained. |
| Cut interpolation | Preserves the same gap by pinching and sign conjugation; no probability-mixture substitution. |
| Rate transfer | Fixed \(c,\rho\), a compact legal \(a\)-interval, a uniform \(B_\delta\), and entropy-value limits after integration. |
| Paid high-contrast theorem | Requires the explicit density/gap condition (28); no unrestricted coverage is asserted. |
| Mixed-direction obstruction | An actual six-site sine base point; independent diagonal directions test the stronger polarized claim. |

| Result | Status |
|---|---|
| Dimension-independent quadratic cut-energy control of actual acceleration | **PROVED** |
| Exact accumulated cost over adjacent merge trees | **PROVED** |
| Finite-seed-to-rate chord bridge (24)–(25) | **PROVED** |
| Sparse/dense high-contrast rate region (28)–(30) | **PROVED, NARROW SCOPE** |
| Entrywise nonnegative mixed diagonal rectangles at sine base points | **DISPROVED by executed interval certificate** |
| All-size \(M_{m,n}''\ge0\) on the frozen common identity path | **INCOMPLETE; not disproved** |
| High-contrast half-density propagation from the accepted two-site seed | **INCOMPLETE; this budget does not pay it** |
| Every density and every legal interior bias for every \(37/40<c<1\) | **INCOMPLETE** |

The substantive structural result is the pointwise estimate (19), followed by the exact total charge (21). The remaining high-contrast difficulty is obtaining enough **Fisher–acceleration cancellation** to replace the conservative worst-word constant, or producing an affordable seed that pays the leakage penalty in (25).
