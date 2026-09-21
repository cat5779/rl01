# S67 continuation — Count-gauge transport with compensated weighted resolvents

## Status and scope

**PROVED:** an improved all-volume asymptotic upper bound for the signed actual-law acceleration on the frozen benchmark chord. The proof preserves actual endpoint and intermediate laws, every configuration, nonprojection leakage, and a quantitatively explicit finite-compression error.

**INCOMPLETE:** a positive true entropy-rate chord. The new bound is still larger than the reviewed available budget. Neither every chord on the benchmark interval nor the all-parameter objective is established.

**DISPROVED:** the stronger shortcut that a count tilt of a finite sine compression is exactly the compression of the count-tilted infinite two-level kernel. Section 11 gives an exact one-site counterexample in the actual model. A derivative-level boundary estimate replaces that false equality.

This is a continuation of the attached `S67_ACCELERATION_RESULT.md`, not a replacement of its source-status ledger and not a claim of independent review. The new contribution is the combination of an odds-*width* binary inequality, a count-gauge reference change, a direct interaction-level boundary estimate, and a compensated noncentered resolvent allocation. The elementary ingredients have classical antecedents. No external novelty claim is made.

### Main numerical conclusion

Put

\[
 U_{\mathrm{cg}}:=\frac{110333}{166400000}
 =0.000663058894230769230769230769\ldots.
\]

For the actual sine DPPs in this manuscript,

\[
 \boxed{\limsup_{n\to\infty}\frac{\mathcal C_n}{n}
 \le U_{\mathrm{cg}}.} \tag{0.1}
\]

Consequently, using the **lower** reviewed endpoint of \(c_{16}=\mathcal C_{16}/16\),

\[
 \boxed{\limsup_{N\to\infty}A_{16\,2^N}
 \le 0.000516378413904885283217037721230769\ldots.} \tag{0.2}
\]

This improves the previously published conservative acceleration cap
\(0.000703319519674116052447806952\) by approximately 26.6%. It does **not** meet

\[
 \gamma_{16}+B_{16}
 \in[0.000245932000395801628841632655,
       0.000245932000395801628841632657]. \tag{0.3}
\]

Equivalently, the new upper bound on \(\mathcal C_n/n\) exceeds the required cap

\[
 C_*:=c_{16}+\gamma_{16}+B_{16}
 \in[0.000392612480721685576393825703,
       0.000392612480721685576393825706] \tag{0.4}
\]

by approximately \(0.000270446413509084\). An upper bound above the cap is a limitation of the proof, **not** a counterexample to the desired entropy chord.

## 1. Frozen model, accepted inputs, and provenance

We use the full configuration law

\[
 P_{a,n}=\operatorname{DPP}(K_{a,n}),\qquad K_{a,n}=aI+cQ_n,
\]

where

\[
 Q_n(i,i)=\tfrac12,\qquad
 Q_n(i,j)=\frac{\sin(\pi(i-j)/2)}{\pi(i-j)},\quad i\ne j.
\]

Throughout,

\[
 c=\frac{19}{20},\quad a_0=\frac1{50},\quad a_1=\frac3{100},
 \quad b=\frac1{40},\quad\lambda=\frac12.
\]

Let \(H_n\) be full Shannon entropy in nats and \(h=\lim_n H_n/n\). Neither count entropy nor \(\operatorname{Tr}\eta(K_n)\) is substituted for \(H_n\).

The acceleration and relative-entropy terms are

\[
 \mathcal D_n=\tfrac12 D(P_{a_0,n}\Vert P_{b,n})
             +\tfrac12 D(P_{a_1,n}\Vert P_{b,n}),
\]

\[
 \mathcal C_n=E_b\log p_b-\tfrac12E_{a_0}\log p_b
                           -\tfrac12E_{a_1}\log p_b.
\]

Exactly, \(\operatorname{Gap}H_n=\mathcal D_n-\mathcal C_n\). We accept the reviewed S64/PR46 length inequality

\[
 \frac{\mathcal D_M}{M}\ge\frac{\mathcal D_{16}}{16}
                  +(1-16/M)B_{16},\qquad M\ge16, \tag{1.1}
\]

and the following frozen intervals, supplied in the assignment and recorded in the preceding manuscript:

\[
\begin{aligned}
 B_{16}&\in[.000104188037840358653653185471,
              .000104188037840358653653185472],\\
 \gamma_{16}&\in[.000141743962555442975188447184,
                  .000141743962555442975188447185],\\
 c_{16}&\in[.000146680480325883947552193048,
              .000146680480325883947552193049].
\end{aligned} \tag{1.2}
\]

We do not reprove KL length convexity or add its budget to a determinant budget. We do not use the author-only S63 claim, perform S68's endpoint two-defect expansion, or differentiate an entropy-value \(o(n)\) error.

The inherited source packet is the one identified in the assignment: repository `cat5779/rl01`, source PR45, branch `research/sa-cycle11-pr128-20260918`; the S64 review/result/checks, CYCLE11/12/13 status files, and `prompts/CYCLE13/S67.md`. The preceding attached manuscript records their actual retrieval and reading. This continuation does **not** claim a fresh audit of live repository status or a fresh execution of the original exhaustive n=15/16 verifier. Its numerical intervals remain accepted inputs. The present derivation is self-contained given those inputs; its acceleration bound itself does not depend on the n=15/16 enumeration.

The universal accepted reference \(c\le37/40\) is unchanged. Proving an acceleration bound at \(c=19/20\) is not a new full-interval entropy concavity theorem.

## 2. The exact interaction representation

For \(x\in\{0,1\}^n\), set

\[
 D_x=\operatorname{diag}(1-x_i),\quad S_x=I-2D_x,\quad
 B_K(x)=(K-D_x)^{-1}.
\]

For every strictly interior Hermitian positive contraction,

\[
 p_K(x)=\det(S_x)\det(K-D_x)>0. \tag{2.1}
\]

Separate local diagonal parameters give

\[
 \partial_i\log p=B_{ii},\qquad
 \partial_i\partial_j\log p=-|B_{ij}|^2\quad(i\ne j).
\]

For a conditional two-site DPP table, ordered as 11,10,01,00, write

\[
 A=uv-t,\quad B=u(1-v)+t,\quad
 C=(1-u)v+t,\quad D=(1-u)(1-v)-t,
 \qquad t\ge0.
\]

Here \(t=BC-AD\), and define

\[
 J=\log\frac{BC}{AD},\qquad
 W=t\left(\frac1A+\frac1B+\frac1C+\frac1D\right). \tag{2.2}
\]

Let \(J^K_{ij}(x_{-ij})\) be the conditional interaction, and let

\[
 F_K(x)=\sum_{i<j}J^K_{ij}(x_{-ij}).
\]

For the **fixed original reference** \(b\), multiaffinity of the configuration determinant gives

\[
 \frac{d^2}{da^2}E_a\log p_b
 =-2\sum_{i<j}E_{a,-ij}J^b_{ij}. \tag{2.3}
\]

Indeed the exterior marginal is independent of the two local diagonal parameters, and the mixed derivative of the four conditional cells is \((1,-1,-1,1)\). Their contribution is \(\log(AD/BC)\); pure local second derivatives vanish. The exterior law in (2.3) is the actual law at \(a\).

With \(d=a-b\), \(D_0=1/200\), and

\[
 G(a)=\frac{D_0-|a-b|}{2},\qquad a\in[a_0,a_1],
\]

finite-chord integration by parts gives

\[
 \mathcal C_n=2\int_{a_0}^{a_1}G(a)E_a F_{K_b}(X)\,da. \tag{2.4}
\]

In particular,

\[
 \int G=\frac1{80000},\qquad
 \int G(a)(a-b)^2\,da=\frac1{19200000000}. \tag{2.5}
\]

No endpoint/volume interchange is used here.

## 3. A reusable odds-width inequality, invariant under a common field

### Lemma 3.1 — common-center odds-width comparison

Let \((A,B,C,D)\) be a strictly positive negative-covariance binary table. Suppose that for some \(z>0\) all four one-bit conditional odds lie in

\[
 [z/M,zM],\qquad M\le20.
\]

Then

\[
 J\le\frac32W. \tag{3.1}
\]

The center \(z\) is arbitrary. In particular, the conclusion is preserved when a binary law satisfying the centered odds condition is tilted by a common fugacity, even if its absolute conditional odds then exceed 20.

**Proof.** Write \(r=BC/(AD)\ge1\) and

\[
 A=\sqrt{AD}e^u,\quad D=\sqrt{AD}e^{-u},\quad
 B=\sqrt{rAD}e^v,\quad C=\sqrt{rAD}e^{-v}.
\]

The four adjacent log odds are \(u\pm v\pm\tfrac12\log r\). The common interval centered at \(\log z\) therefore implies

\[
 |u-\log z|+|v|+\tfrac12\log r\le\log M.
\]

Thus \(1\le r\le M^2\) and \(|v|\le\log M-\frac12\log r\). If \(q=A+D\), then

\[
 q=\frac{\cosh u}{\cosh u+\sqrt r\cosh v}
 \ge\frac1{1+\sqrt r\cosh(\log M-\frac12\log r)}
 =\frac{2M}{M^2+2M+r}. \tag{3.2}
\]

This argument uses \(\cosh u\ge1\), not a bound on the absolute location of \(u\). That is why the common field costs nothing in this comparison.

Direct algebra gives

\[
 W=(r-1)\{q+(1-q)/r\}.
\]

Using the weaker interval with \(M=20\), it remains to prove

\[
 \phi(r):=\frac32\frac{(r-1)(41r+400)}{r(r+440)}-\log r\ge0,
 \qquad1\le r\le400. \tag{3.3}
\]

Its derivative has the sign of

\[
 P(r)=-2r^3+51283r^2-384800r+528000.
\]

On this interval \(P''(r)=102566-12r>0\). The exact signs
\(P(1)>0\), \(P(2)<0\), \(P(5.69)<0<P(5.70)\), and \(P(400)>0\), together with the signs of \(P'\) at the endpoints, give precisely one local maximum and one subsequent local minimum of \(\phi\). The latter is in \((5.69,5.70)\). The rational function

\[
 w(r)=\frac{(r-1)(41r+400)}{r(r+440)}
\]

is increasing: its derivative numerator is \(17681r^2+800r+176000>0\). At that minimum,

\[
 \phi(r)\ge\tfrac32w(5.69)-\log(5.70)
 >\tfrac32w(5.69)-\tfrac74>0.
\]

The last comparison is rational, and \(e^{7/4}>\sum_{k=0}^6(7/4)^k/k!>5.70\). Finally \(\phi(1)=0\). This proves the lemma. ∎

The factor-one comparison remains false in the actual sine model, as recorded by the preceding S67 counterexamples. This lemma does not resurrect it. Without the common odds-width hypothesis even the factor-three-halves inequality fails, for example for the positive table \((10,1,1000,10)/1021\), which has \(J=\log10>2\) while \((3/2)W<2\).

## 4. Count gauges and the endpoint-matched auxiliary kernel

For any positive L-ensemble, \(L=K(I-K)^{-1}\), count tilting by \(z^{|x|}\) gives another DPP with

\[
 K^{(z)}=f_z(K),\qquad
 f_z(t)=\frac{zt}{1+(z-1)t},
\]

and exactly

\[
 \log p_{K^{(z)}}(x)=\log p_K(x)+|x|\log z-\log Z_K(z). \tag{4.1}
\]

A mixed two-bit difference annihilates both added terms. Hence

\[
 F_{K^{(z)}}(x)=F_K(x) \tag{4.2}
\]

for every configuration, in every finite volume.

For each actual intermediate \(a=b+d\), choose

\[
 z(a)=\sqrt{\frac{a(a+c)}{(1-a)(1-a-c)}}
     =\sqrt{\frac{s+d+d^2}{s-d+d^2}},\qquad s=\frac{39}{1600}.
 \tag{4.3}
\]

Define

\[
 u=f_z(b)=\frac{z}{39+z},\qquad
 v=f_z(1-b)=\frac{39z}{1+39z},\qquad
 \widehat K_{a,n}=uI+(v-u)Q_n. \tag{4.4}
\]

This is an auxiliary **reference** kernel. It is not substituted for the actual law \(P_{a,n}\).

At the two spectral endpoints the actual/reference odds ratios are reciprocal. Their common envelope is

\[
 R(a)^2=
 \frac{1-d^2/(1-b)^2}{1-d^2/b^2}. \tag{4.5}
\]

In particular,

\[
 \frac45<z<\frac54,\qquad
 R^2\le\frac{4753}{4563}<\frac{25}{24},\quad
 R^2-1\le1666d^2,\quad R-1\le833d^2. \tag{4.6}
\]

Unlike the old transport factor, whose deviation from one was first order in \(|d|\), this residual odds factor is **second order** in \(d\).

To extend the endpoint comparison to every spectral value of \(Q_n\), note that \(f_R\) is concave and \(f_{1/R}\) is convex for \(R\ge1\). Bounds at both endpoints of two affine probability interpolations imply the same bounds at their interpolated values by these two scalar Jensen inequalities. Functional calculus therefore gives

\[
 R^{-1}L(\widehat K_{a,n})\le L(K_{a,n})
                         \le R L(\widehat K_{a,n}). \tag{4.7}
\]

The proof pays the finite-compression mismatch between \(f_z(K_{b,n})\) and \(\widehat K_{a,n}\) separately in Section 5. They are not equal.

### Conditional odds of the auxiliary reference

For a compression of an infinite two-level kernel with values \(u,v\) and diagonal projection density \(1/2\), compression of inverse operators and the Schur-complement variational formula give

\[
 \frac1{\ell_-}\le\omega\le\ell_+,
\quad
 \ell_+=\tfrac12\left(\frac u{1-u}+\frac v{1-v}\right),\quad
 \ell_-=\tfrac12\left(\frac{1-u}{u}+\frac{1-v}{v}\right).
\]

For (4.4),

\[
 \ell_+=z\frac{761}{39},\qquad
 \ell_-=z^{-1}\frac{761}{39}. \tag{4.8}
\]

Thus every conditional pair of \(\widehat K\), including exceptional configurations, has all adjacent odds in
\([z/M_b,zM_b]\), \(M_b=761/39<20\). Lemma 3.1 applies with the unchanged coefficient \(3/2\).

For completeness, the compression inequality is \((PAP)^{-1}\le PA^{-1}P\) on the compressed subspace for positive \(A\). Apply it to \(K_\infty\) and \(I-K_\infty\). The conditional occupied-site odds is a Schur complement of \(L\), between \(1/(L^{-1})_{ii}\) and \(L_{ii}\). This proves the displayed odds bounds without treating \(Q_n\) as a projection.

## 5. Direct interaction-level control of the compression error

This section is a derivative-level estimate for the actual interaction functional. It is **not** differentiation of an entropy-value error.

### Lemma 5.1 — a trace-norm boundary estimate for the sum of interactions

Suppose \(K_0,K_1\) and their line segment have spectra in \([\varepsilon,1-\varepsilon]\), \(0<\varepsilon<1/2\). Put \(t_0=\varepsilon/(1-\varepsilon)\). Then uniformly in every configuration,

\[
 |F_{K_1}(x)-F_{K_0}(x)|
 \le L_n(\varepsilon)\,\|K_1-K_0\|_1,
\]

\[
 L_n(\varepsilon)
 =t_0^{-2}\varepsilon^{-3}\sqrt n
  +t_0^{-3}\varepsilon^{-4}. \tag{5.1}
\]

**Proof.** Along the line segment write \(B=(K-D_x)^{-1}\),
\(T_i=|B_{ii}|-1\), and \(\sigma_i=2x_i-1\). A conditional-probability calculation gives

\[
 T_i=\frac{p_K(x^i)}{p_K(x)},\qquad
 T_iT_j-\sigma_i\sigma_j|B_{ij}|^2
       =\frac{p_K(x^{ij})}{p_K(x)}. \tag{5.2}
\]

All one-bit conditional probabilities lie in \([\varepsilon,1-\varepsilon]\), so \(T_i\ge t_0\), and the second ratio in (5.2), obtained by two successive flips, is at least \(t_0^2\).

Also \(\|B\|\le\varepsilon^{-1}\). One direct proof is to observe that the Hermitian part of \(S_x(K-D_x)\), after grouping occupied and absent coordinates, is the block diagonal matrix with blocks \(K_{11}\) and \(I-K_{00}\), each at least \(\varepsilon I\). Thus its smallest singular value, and hence that of \(K-D_x\), is at least \(\varepsilon\).

The exact common-configuration formula is

\[
 J_{ij}=-\sigma_i\sigma_j
 \log\left(1-\sigma_i\sigma_j\frac{|B_{ij}|^2}{T_iT_j}\right).
\]

Differentiating it, with \(\dot B=-B\dot K B\), gives

\[
 |\dot J_{ij}|\le
 2t_0^{-2}|B_{ij}||\dot B_{ij}|
 +t_0^{-3}|B_{ij}|^2
       (|\dot B_{ii}|+|\dot B_{jj}|). \tag{5.3}
\]

Summing the first term over \(i<j\) and using Frobenius Cauchy–Schwarz bounds it by
\(t_0^{-2}\sqrt n\,\varepsilon^{-3}\|\dot K\|_1\). The second term is at most
\(t_0^{-3}\varepsilon^{-2}\sum_i|\dot B_{ii}|\), hence at most
\(t_0^{-3}\varepsilon^{-4}\|\dot K\|_1\). Integrating proves (5.1). ∎

### Application to the count gauge

Let \(E_n=Q_n-Q_n^2\ge0\). Scalar linear interpolation of \(f_z\), with its explicit second derivative, gives

\[
 \|f_z(K_{b,n})-\widehat K_{a,n}\|_1
 \le\frac{5c^2}{16}\operatorname{Tr}E_n. \tag{5.4}
\]

Indeed \(|f_z''(t)|\le2z|z-1|/\min(1,z)^3\), and for \(4/5\le z\le5/4\),
\(z|z-1|/\min(1,z)^3\le5/16\). The scalar chord-error bound supplies the factor \(q(1-q)c^2\), and both matrices are functions of \(Q_n\), so their trace norm is the sum of the absolute scalar errors.

All relevant auxiliary and tilted kernels lie in \([1/50,49/50]\). Consequently we may take

\[
 L_n=49^2 50^3\sqrt n+49^3 50^4. \tag{5.5}
\]

Equations (4.2), (5.1), and (5.4) give, under the **unchanged actual law**,

\[
 E_aF_{K_b}\le E_aF_{\widehat K_a}
              +\frac{5c^2}{16}L_n\operatorname{Tr}E_n. \tag{5.6}
\]

The contribution to \(\mathcal C_n/n\) is at most

\[
 \mathcal E_n:=\frac{c^2}{128000}
 \left(\frac{49^2 50^3}{\sqrt n}+\frac{49^3 50^4}{n}\right)
 \operatorname{Tr}E_n. \tag{5.7}
\]

For the sine compression,

\[
 \operatorname{Tr}E_n
 \le\frac2{\pi^2}\left(H_{n-1}+n\sum_{d\ge n}\frac1{d^2}\right)
 \le\frac2{\pi^2}\left(H_{n-1}+\frac n{n-1}\right),\quad n\ge2. \tag{5.8}
\]

Thus \(\mathcal E_n\to0\). Its constants are very large. We make **no** practical-volume smallness claim. This is sufficient for an all-volume limsup theorem, not for a small stopping-volume certificate.

## 6. Noncentered weighted resolvents with actual-law compensation

### Lemma 6.1 — weighted square allocation

Let \(K=uI+(v-u)Q_n\), with \(0<u<v<1\). Set

\[
 m=u+v,\quad s_+=uv,\quad s_-=(1-u)(1-v),\qquad
 s_i=\begin{cases}s_+&x_i=1,\\s_-&x_i=0.\end{cases}
\]

Then, for \(B=(K-D_x)^{-1}\),

\[
 B\operatorname{diag}(s_i)B+(v-u)^2BE_nB
 =\tfrac12(S_xB+BS_x)+(m-1)B-I. \tag{6.1}
\]

Consequently,

\[
 \sum_{i\ne j}|B_{ij}|^2
 \le\sum_i\left\{\frac{(m-2D_{ii})B_{ii}-1}{s_i}-B_{ii}^2\right\}
 -(v-u)^2\operatorname{Tr}(\operatorname{diag}(s_i)^{-1}BE_nB).
 \tag{6.2}
\]

**Proof.** Since \(K^2-mK+uvI=-(v-u)^2E_n\), substitute \(K=B^{-1}+D_x\) and multiply on both sides by \(B\), obtaining (6.1). Multiply its diagonal equations by \(1/s_i\) and sum. The square coefficient on an unordered off-diagonal pair is \(s_j/s_i+s_i/s_j\ge2\). The discarded excess and the displayed leakage are both nonnegative. ∎

This avoids the much more expensive replacement of both \(s_+\) and \(s_-\) by their minimum.

### Lemma 6.2 — retain the favorable and unfavorable one-bit terms together

Let \(r\) be the reference one-site conditional probability and \(q\) the actual one, for the same exterior configuration. Define

\[
 A_0=\frac m{s_+},\quad B_0=\frac{2-m}{s_-},\quad
 C_0(p)=\frac{m-p}{s_+}+\frac{1-m+p}{s_-},\quad p=E_aX_i.
\]

Then the actual expectation of the first, undiagonalized expression in (6.2), per site, is exactly

\[
 C_0(p)+E_{a,-i}(q-r)
       \left(\frac{A_0}{r}-\frac{B_0}{1-r}\right). \tag{6.3}
\]

If actual/reference conditional odds ratios lie in \([1/R,R]\), then

\[
 (q-r)\left(\frac{A_0}{r}-\frac{B_0}{1-r}\right)
 \le(R-1)\max(A_0,B_0). \tag{6.4}
\]

**Proof.** Before averaging, the expression equals

\[
 q\frac{m/r-1}{s_+}+(1-q)\frac{(2-m)/(1-r)-1}{s_-}.
\]

Expand \(q=r+(q-r)\), collect the remaining term affine in \(q\), and use \(E q=p\). This gives (6.3); in particular, \(r\) has not been incorrectly averaged under the reference law.

For (6.4), if \(q\ge r\), then
\(q-r\le(R-1)r(1-r)/(1+(R-1)r)\). If the multiplying bracket is negative there is nothing to prove; otherwise the product is at most \((R-1)A_0\). If \(q\le r\), use
\(r-q\le(R-1)r(1-r)/(R-(R-1)r)\); the positive case of the product is at most \((R-1)B_0\). ∎

### Local transport and Fisher subtraction

Schur complements preserve the order (4.7). For a conditional law on \(k\) remaining sites, its probability ratios are therefore in \([R^{-k},R^k]\). One proof connects the two positive conditional L matrices by a matrix-logarithmic path: the derivative of a configuration log probability is the trace pairing of a projection minus a positive contraction with a whitened derivative of norm at most \(\log R\). Its absolute value is at most \(k\log R\). Integration proves the claim.

For \(k=1\), pointwise in the full configuration,

\[
 |B_{\widehat K_a,ii}|^2\ge R^{-2}|B_{K_a,ii}|^2. \tag{6.5}
\]

For \(k=2\), Lemma 3.1 and the conditional inverse identity yield

\[
 \sum_{i<j}E_{a,-ij}J^{\widehat K_a}_{ij}
 \le\frac32R^2\sum_{i<j}E_a|B_{\widehat K_a,ij}|^2. \tag{6.6}
\]

Here the exact inverse identity is \(|B_{ij}(x)|^2=t/q_{\rm ref}(x_i,x_j)^2\); averaging with reference pair probabilities gives \(W\), and the actual conditional weights are bounded below by \(R^{-2}\) times those probabilities. The exterior weights are still actual weights.

Combining (6.2)–(6.6), and dropping only favorable terms, gives

\[
 \frac2n E_aF_{\widehat K_a}
 \le\frac32\left[
 R^2 C_0(p)+R^2(R-1)\max(A_0,B_0)-d_n^{\rm loc}(a)\right], \tag{6.7}
\]

where any proved lower bound on \(n^{-1}\sum_i E_a|B_{K_a,ii}|^2\) may be used for \(d_n^{\rm loc}(a)\). The actual marginal here is exactly \(p=a+c/2\).

## 7. A finite three-site input, with its proof and boundary cost

For a separate local diagonal parameter at site \(i\), marginal score projection gives

\[
 E_a[B_{K_a,ii}(X)\mid X_W]
 =B_{K_{a,W},ii}(X_W),\qquad
 E_a|B_{K_a,ii}|^2\ge E_a|B_{K_{a,W},ii}|^2. \tag{7.1}
\]

This follows by differentiating the finite marginal sum and applying conditional Jensen. It is the classical Fisher score-projection identity, applied to a **local** parameter, not the scalar that changes all diagonals.

For a center site and its two neighbors, the neighbors have independent Bernoulli marginals with parameter \(p=a+c/2\in[.495,.505]\), because their mutual sine-kernel entry is zero. Set \(\tau=(c/\pi)^2\). If \(k\) neighbors are occupied, the central conditional probability is

\[
 r_k=p-\tau\left(\frac{k}{p}-\frac{2-k}{1-p}\right).
\]

All four exterior configurations give the exact Fisher input

\[
 d_3(a)=\sum_{k=0}^2\binom2k
 \frac{p^k(1-p)^{2-k}}{r_k(1-r_k)}. \tag{7.2}
\]

We restate the analytic lower bound from the preceding S67 manuscript rather than treating it as an unexamined numerical input:

\[
 d_3(a)\ge d_*:=2+\frac2{1-64\tau^2}>\frac{63}{10}. \tag{7.3}
\]

To verify it, put \(x=(2p-1)^2\le10^{-4}\), \(v_0=(1-x)/4\), and

\[
 E(x)=(1-8\tau)^2-(2+16\tau)x+x^2.
\]

Direct algebra splits (7.2) into

\[
 D_{02}(x)=\frac{2(1+x+8\tau)}{1-x+8\tau}
 +\frac{128\tau^2(1+x-8\tau)}{(1-x+8\tau)E(x)},
\]

\[
 D_1(x)=\frac{2v_0^3}{v_0^3-x\tau(v_0+\tau)}.
\]

The elementary enclosure \(.09<\tau<.092\) makes all displayed denominators positive on \([0,10^{-4}]\). The numerators of the two positive ratios in \(D_{02}\) increase and their denominators decrease there; \(E'(x)<0\). Thus
\(D_{02}(x)\ge D_{02}(0)=2/(1-64\tau^2)\), while \(D_1(x)\ge2\). Finally the rational enclosure \(3.14<\pi<3.1416\), obtainable from Machin's formula and alternating arctangent remainders, proves \(d_*>63/10\). The exact verifier reproduces that enclosure.

Use the three-site window at each of the \(n-2\) interior sites and the one-site marginal bound \(1/[p(1-p)]\ge4\) at the two boundary sites. Then, for \(n\ge3\),

\[
 d_n^{\rm loc}(a)\ge\frac{63}{10}-\frac{23}{5n}. \tag{7.4}
\]

The finite boundary is explicit; it has not been absorbed into an asymptotic assertion.

## 8. Exact scalar envelope and proof of the new acceleration bound

Let \(k=1/s-2<40\), \(p=1/2+d\), and \(t=\log z\). Direct substitution in (6.3) gives

\[
 C_0(p)=3+k\{pz+(1-p)/z\}-(1-p)z^2-p/z^2
\]

\[
 =3+k\cosh t-\cosh(2t)
      +2d\{k\sinh t+\sinh(2t)\}. \tag{8.1}
\]

Moreover,

\[
 A_0=2+k/z,\qquad B_0=2+kz,
 \qquad\max(A_0,B_0)<51. \tag{8.2}
\]

Since

\[
 t=\operatorname{atanh}\frac{d}{s+d^2},
\]

and \(|d|\le1/200\), the positive series for atanh gives \(|t|\le42|d|\le.21\). More explicitly,

\[
 \operatorname{atanh}x\le x+\frac{x^3}{3(1-x^2)},\qquad
 0\le x\le8/39,
\]

and \(s^{-1}[1+64/(3(1521-64))]<42\).

On \(|t|\le.21\), elementary positive-series estimates give

\[
 \cosh t-1\le\tfrac{103}{200}t^2,\quad
 \cosh(2t)-1\ge2t^2,\quad
 |\sinh t|\le\tfrac{101}{100}|t|,\quad
 |\sinh(2t)|\le\tfrac{103}{100}\,2|t|.
\]

For example, \(\cosh(.21)\le1/(1-.21^2/2)<1.03\), and
\(\sinh(.42)/.42\le1+.42^2/6+.42^4/[120(1-.42^2/42)]<1.03\). These are rational comparisons. Thus (8.1) gives

\[
 C_0(p)\le\frac1s+37000d^2. \tag{8.3}
\]

Indeed the coefficient obtained directly from those estimates is \(36377.04<37000\).

Combining (4.6), (8.2), and (8.3), with \(1/s<42\), yields

\[
 R^2 C_0(p)+R^2(R-1)\max(A_0,B_0)
 \le\frac1s+153000d^2. \tag{8.4}
\]

The coefficient on the right is an outward rational bound because

\[
 1666\cdot42+\frac{25}{24}(37000+833\cdot51)
 =152766.79166\ldots<153000.
\]

Insert (7.4), (8.4), and (5.6) into (2.4) and (6.7). For every \(n\ge3\),

\[
 \boxed{
 \frac{\mathcal C_n}{n}
 \le\frac32\left[
 \frac{1600/39-63/10}{80000}
 +\frac{153000}{19200000000}\right]
 +\frac{69}{800000n}+\mathcal E_n
 =\frac{110333}{166400000}
  +\frac{69}{800000n}+\mathcal E_n.} \tag{8.5}
\]

Every term is explicit. More precisely, the right-hand side of (8.5) may be decreased by the sum of the following two nonnegative quantities, with $B=B_{\widehat K_a}(X)$ and the configuration-dependent $s_i$ of Section 6:

\[
 \mathcal L_n=\frac{3}{2n}\int G(a)R(a)^2(v-u)^2
 E_a\operatorname{Tr}(\operatorname{diag}(s_i)^{-1}BE_nB)\,da,
\]

\[
 \mathcal W_n=\frac{3}{2n}\int G(a)R(a)^2
 E_a\sum_{i<j}\left(\frac{s_i}{s_j}+\frac{s_j}{s_i}-2\right)|B_{ij}|^2\,da.
\]

They are displayed to keep the favorable finite-compression and unequal-row-weight contributions explicit; no numerical credit from them is claimed. Favorable contraction leakage and favorable unequal-row-weight square terms were discarded only after their signs were proved. Equation (5.8) shows \(\mathcal E_n\to0\), proving (0.1) and (0.2).

One may take the minimum with the original S67 finite-volume bound when it is better at a practical volume. In particular, the very large boundary constant in (5.7) means that (8.5) is primarily an asymptotic improvement, not a uniformly better small-volume bound.

## 9. The remaining budget, and a genuinely finite sufficient input

The proved bound is not enough. Combining (8.5) with the accepted KL length inequality gives only

\[
 \operatorname{Gap}h\ge C_* - U_{\rm cg},
\]

with a negative right-hand side. No positive \(\delta\) is asserted.

The new mechanism nevertheless gives a concrete sufficient input different from, and independently checkable without, the unknown acceleration limit.

Suppose an odd finite window of length \(m\) has a certified lower bound \(d_m(a)\ge D\ge4\) for its central **actual local diagonal Fisher information**, for every \(a\in[.02,.03]\). Score projection, with at most \(m-1\) boundary sites treated by the one-site bound, gives

\[
 \limsup_n\frac{\mathcal C_n}{n}
 \le\frac32\left[
 \frac{1600/39-D}{80000}
 +\frac{153000}{19200000000}\right]. \tag{9.1}
\]

The analogous weighted integral criterion, replacing \(D\int G\) by a certified \(\int G(a)d_m(a)\,da\), is weaker and also sufficient.

In particular, the finite input

\[
 \boxed{d_m(a)\ge\frac{83}{4}=20.75\quad
 \hbox{throughout the actual chord}} \tag{9.2}
\]

would give

\[
 \limsup_n\frac{\mathcal C_n}{n}
 \le\frac{65249}{166400000}
 =0.000392121394230769230769\ldots,
\]

and therefore, using the reviewed lower endpoint of \(C_*\),

\[
 \operatorname{Gap}h>\frac{49}{100000000}=4.9\times10^{-7}. \tag{9.3}
\]

**The input (9.2) has not been proved or certified.** The conditional corollary (9.1)–(9.3) is not a completion of the benchmark. It is included to make the remaining finite obligation explicit, not to disguise the target as a renamed remainder.

The old diagonal-only obstruction concerned the old transport and square-allocation constants. It does not automatically apply to (9.1). Conversely, removal of that particular obstruction is not evidence that (9.2) actually holds. At the reference point, the simple conditional-odds Fisher ceiling is

\[
 d_m(b)\le\frac1{(39/800)(761/800)}
 =\frac{640000}{29679}>20.75.
\]

Thus this elementary ceiling alone does not falsify (9.2), but the required information is close to that ceiling. A further attempt should check actual attainable Fisher information or improve the pair/compensation step before committing to expensive window enumeration. No large-window success is claimed here.

### Finite stopping still requires the full entropy tail

For a finite \(M\ge16\), the admissible interface remains

\[
 \operatorname{Gap}h\ge\gamma_{16}+(1-16/M)B_{16}
 -\left[U_{\rm cg}+\frac{69}{800000M}+\mathcal E_M-c_{16}\right]
 -T_{\rm QWE}(M). \tag{9.4}
\]

The full entropy-chord \(T_{\rm QWE}\) has not been replaced by a determinant tail, set to zero, or assumed numerically small. The direct limsup proof of (0.1) uses a proved vanishing interaction-level boundary estimate, not a practical-volume tail assumption.

## 10. Dependency ledger and verification scope

| Item | Status and dependency |
|---|---|
| Full-law model, \(\operatorname{Gap}H_n=\mathcal D_n-\mathcal C_n\), existence/interface for the entropy rate | Frozen assignment inputs; objects are not interchanged |
| PR46 KL length convexity and n=15/16 numerical intervals | ACCEPTED, not reproved or independently rerun here |
| Local score projection and three-site Fisher input | Prior S67 ingredient, with complete derivation restated in Section 7 |
| Count tilt of an L-ensemble | Classical identity, proved explicitly in Section 4 |
| Common-center odds-*width* extension | PROVED, Section 3; the arbitrary center is essential to this continuation |
| Interaction-level trace-norm boundary estimate | PROVED, Section 5; explicit finite error, not an entropy-value derivative |
| Noncentered weighted resolvent identity and compensated actual conditional expectation | PROVED, Section 6 |
| Endpoint-matched residual transport and rational envelope | PROVED, Sections 4 and 8 |
| Improved acceleration bound (8.5), (0.1), (0.2) | PROVED; benchmark-specific |
| Finite-window sufficient input (9.2) | UNVERIFIED; not asserted for the actual model |
| Positive benchmark entropy-rate chord | INCOMPLETE |

`code/verify_exact.py` uses only exact rational arithmetic for acceptance comparisons. It encloses \(\pi\) by Machin's identity, checks the pair-lemma polynomial signs, the scalar envelope, the final budget, and exact rational matrix/configuration identities with nonzero contraction leakage. Those rational matrix examples are algebra checks, **not** substitutes for actual sine probabilities. The proof is analytic; the rational scalar checks make its numerical constants reproducible.

`code/check_small_actual_sine.py` separately performs high-precision diagnostics on every configuration at n=2,4,6 of the actual sine model. Its output, when executed successfully, is labeled a diagnostic rather than an interval certificate. It checks gauge invariance, the noncentered matrix identity, conditional transport, odds-width pair comparisons, and finite actual-law quantities. No entropy-rate theorem follows from those finite observations.

Execution records are produced by the programs themselves. A supplied program is not silently equated with a successful run. Read the accompanying exit-status and JSON files for the actual execution result. The verifier's wall time is not research-session duration, and the original exhaustive S64 verifier is not represented as rerun.

## 11. Adversarial checks and failure boundaries

### 11.1 An exact actual-model counterexample to zero compression cost

Already for \(n=1\), \(Q_1=1/2\) and \(K_{b,1}=1/2\). With \(z=6/5\), the true finite count tilt has marginal

\[
 f_z(1/2)=\frac6{11}.
\]

The compression of the tilted infinite two-level kernel instead has marginal

\[
 \tfrac12\left(f_z(1/40)+f_z(39/40)\right)
 =\tfrac12\left(\frac2{67}+\frac{234}{239}\right)
 =\frac{8078}{16013}.
\]

Their difference is exactly

\[
 \frac6{11}-\frac{8078}{16013}=\frac{7220}{176143}>0.
\]

This is the actual sine-compression model, not an unrelated kernel. It disproves the tempting finite-volume equality. The n=1 interaction sum happens to vanish, but the kernel replacement itself is false; Section 5 is needed to control the interaction-level replacement in arbitrary volumes.

### 11.2 What is not implied

The factor-one conditional-pair inequality is still false. The common-center odds-width lemma does not permit unrelated centers for different conditional odds. This restriction is genuine: start with the unnormalized table $(10,\sqrt{1000},\sqrt{1000},10)$, whose adjacent odds lie between $1/\sqrt{10}$ and $\sqrt{10}$. Opposite site fields $z_1=1/\sqrt{1000}$ and $z_2=\sqrt{1000}$ turn it into $(10,1,1000,10)$, which violates $J\le(3/2)W$. A common field cannot perform this transformation. This auxiliary binary-table counterexample is separate from the actual-sine compression counterexample in Section 11.1. No unweighted raw-window monotonicity is inferred. The moving auxiliary reference is allowed only because (4.1) has exactly zero mixed two-bit response; one cannot omit reference-response terms for a general moving reference.

The auxiliary law \(\operatorname{DPP}(\widehat K_a)\) is never substituted for the actual law \(P_a\). Its conditional probabilities enter a local likelihood comparison; the outer expectation remains actual. All states are included in the uniform boundary estimate and in the analytic odds bounds.

The bound uses \(\varepsilon=1/50\); constants diverge as a legal spectral edge approaches zero or one. The scalar constants use \(\rho=1/2\), \(b=(1-c)/2\), and the stated symmetric chord. They do not prove the same estimate for every reference point in \([.02,.03]\), other \(\rho\), other contrasts, or legal boundary endpoints.

The favorable leakage \(Q_n-Q_n^2\) appears in both the algebra and the boundary estimate. Treating it as zero at finite n is not an admissible simplification. Nor may an entropy-value boundary estimate be differentiated to replace Section 5.

### 11.3 Size of the remaining difficulty

The present theorem is an improved upper bound, not an estimate of the true limiting acceleration. Its approximately \(2.70\times10^{-4}\) excess over the required \(\mathcal C\)-cap remains unpaid. The large interaction-localization constant precludes presenting a small-volume stopping result. The finite Fisher criterion is close to a simple information ceiling and must be tested rather than assumed.

## 12. Handoff and session-accounting statement

The **benchmark chord** remains INCOMPLETE. The assertion for **every chord on the benchmark interval** remains INCOMPLETE. The **all-\(\rho\), all-\(c\), all-legal-\(a\)** objective remains INCOMPLETE.

What has changed is the proved acceleration baseline: a count gauge removes the first-order part of the local odds mismatch, the odds-width lemma prevents paying again for the common field, and a weighted resolvent allocation retains the relevant cancellation. Their combination gives (8.5), not merely an identity or a renamed unknown. A precise finite-window sufficient input is recorded in (9.2), with its status explicitly unverified.

No global repository status was edited, no PR was merged, and no other researcher was contacted in producing this artifact.

**Duration accounting:** the resumed context does not supply a complete, independently inspectable continuous research-session timer. This manuscript does not assert that 120 minutes of active research have been certified. Program-generated start/end times and verification wall seconds refer only to those executions. No elapsed duration is invented, and no waiting or idle loop is counted as research. The substantive mathematical result above is preserved independently of that accounting limitation.
