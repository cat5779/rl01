# High-contrast uniform route: endpoint asymptotics and the volume obstruction

**Status.** This note is not the source of the package's strongest theorem.
Sections 1--2 rederive the historical \(c\leq12/25\) result; both it and the
later \(312/625\) sharpening are superseded by the exact universal theorem
through \(c=1/2\) in `stationary-half-endpoint-closure.md`.  The new content
here is the fixed-dimensional endpoint expansion and the proof that its
leading negative curvature is not uniform in volume.  These facts explain
why the most direct high-contrast passage fails.  No claim for \(c>1/2\) is
proved here.  Later references to \(312/625\) describe the state of the route
when this note was written.

Throughout, entropy uses natural logarithms.

## 1. Historical strict result

Let \(K\) be any \(n\times n\) Hermitian positive contraction and set

\[
H_K(a)=H\!\left(\operatorname{DPP}(aI+cK)\right),
\qquad 0\leq a\leq1-c.
\]

Define

\[
A(x)=x^{-2}-(1-x)^{-2}\qquad(0<x\leq1/2).
\]

The following theorem is dimension-uniform.

> **Theorem 1 (historical universal \(12/25\) contrast theorem).**
> For every finite positive contraction \(K\) and every
> \(0\leq c\leq12/25\), the map \(a\mapsto H_K(a)\) is strongly concave on
> its full legal interval. One common modulus for this whole range is
> \[
> \kappa_*=
> 4-\frac{81}{8192}
> \frac{8984375+3015625\sqrt{193}}{127008}
> =0.0390381789161\ldots .
> \tag{1}
> \]
> Thus, in the strict channel interior,
> \[
> H_K''(a)\leq-\kappa_*n.
> \tag{2}
> \]

### 1.1 Refined conditional-pair coefficient

Put \(d=1-a-c\). On the middle interval

\[
\frac12-c\leq a\leq\frac12,
\]

we have \(0<a,d\leq1/2\). After conditioning outside an unordered pair
\(D=\{i,j\}\), the conditional output kernel is

\[
Q=aI_2+cR_{D,D}
=\begin{pmatrix}q&z\\\bar z&r\end{pmatrix},
\]

where \(R\) is a positive-contraction posterior input kernel. Hence

\[
q,r\in[a,a+c]=[a,1-d],
\qquad |z|^2=c^2|R_{ij}|^2.                             \tag{3}
\]

For the exact two-site entropy functional,

\[
g(Q)=-\int_0^{|z|^2}v\Lambda''(v)\,dv,
\]

and direct differentiation gives

\[
-\Lambda''(v)\leq-A(q)A(r).                            \tag{4}
\]

The function \(A\) is strictly decreasing and
\(A(1-x)=-A(x)\). If \(q,r\) are on the same side of \(1/2\), the right
side of (4) is nonpositive. If they are on opposite sides, monotonicity and
(3) give

\[
-A(q)A(r)\leq A(a)[-A(a+c)]=A(a)A(d).
\]

Therefore

\[
g(Q)_+\leq\frac{c^4}{2}A(a)A(d)|R_{ij}|^4.             \tag{5}
\]

This is the key improvement: the two opposing endpoints of the same
spectral interval occur as a product. Replacing them by the square of one
worst endpoint loses the high-contrast range.

### 1.2 Hölder posterior energy

Define

\[
h_c(a)=\sqrt{a(a+c)}+\sqrt{(1-a)d}.
\]

The exact reverse-Bayes identity, Hölder's inequality, and the common full
posterior positive contraction give

\[
\sum_{i<j}\mathbb E
|R^{\{i,j\},Y_{-\{i,j\}}}_{ij}|^4
\leq\frac{n}{32h_c(a)^8}.                              \tag{6}
\]

The common-shift entropy Hessian is

\[
H_K''(a)=
-\sum_i\mathbb E\frac1{u_i(1-u_i)}
+2\sum_{i<j}\mathbb E g(Q^{ij}),
\]

whose diagonal part is at most \(-4n\). The factor \(2\) over unordered
pairs cancels the factor \(1/2\) in (5). Thus

\[
\frac1nH_K''(a)
\leq-4+
\frac{c^4A(a)A(d)}{32h_c(a)^8}.                        \tag{7}
\]

The concavity and symmetry of \(h_c\) on the middle interval imply

\[
h_c(a)^8\geq
C_c:=\left(\frac{1+\sqrt{1-4c^2}}2\right)^4.           \tag{8}
\]

### 1.3 Uniform scalar optimization

Set

\[
\mathcal A(c)=
\max_{\substack{a+d=1-c\\0<a,d\leq1/2}}A(a)A(d),
\qquad
\mathcal B(c)=\frac{c^4\mathcal A(c)}{32C_c}.           \tag{9}
\]

The function \(\mathcal B\) is nondecreasing on \((0,1/2)\). To see this,
write

\[
a=\frac{1-c}{2}+u,\qquad d=\frac{1-c}{2}-u,
\qquad |u|\leq\frac c2.
\]

If \(c'\geq c\), keeping \(u\) gives a feasible pair for \(c'\), with both
new coordinates no larger. Since \(A\) is positive and decreasing on
\((0,1/2]\), \(\mathcal A(c')\geq\mathcal A(c)\). Also \(c^4\) increases
and \(C_c\) decreases.

It remains to optimize exactly at \(c=12/25\). Put \(p=ad\). Then

\[
A(a)A(d)=
R_c(p):=\frac{4p+2c-1}{p^2(c+p)^2},
\qquad
\frac1{100}\leq p\leq\frac{169}{2500}.                 \tag{10}
\]

The sign of \(R_c'(p)\) is the opposite of the sign of

\[
6p^2+(6c-2)p+2c^2-c.
\]

At \(c=12/25\), the unique positive critical point is

\[
p_*=\frac{\sqrt{193}-11}{150},
\]

and it lies in the interval in (10). The derivative changes from positive
to negative there, so

\[
\mathcal A(12/25)
=R_{12/25}(p_*)
=\frac{8984375+3015625\sqrt{193}}{127008}.             \tag{11}
\]

At the same contrast,

\[
C_{12/25}=\left(\frac{16}{25}\right)^4,
\qquad
\frac{c^4}{32C_c}=\frac{81}{8192}.
\]

The rational inequality \(\sqrt{193}<139/10\) gives

\[
\frac{81}{8192}\mathcal A(12/25)<4.                   \tag{12}
\]

Equations (7)--(12) prove (2) on the middle interval. On
\(0<a<1/2-c\), every conditional pair kernel lies below \(I_2/2\), so
all pair terms are nonpositive and \(H_K''\leq-4n\). Bit complementation
gives the same result on \(1/2<a<1-c\). These intervals cover the legal
interior. Continuity of finite-word entropy extends the integrated strong
Jensen inequality to \(a=0\) and \(a=1-c\). This proves Theorem 1.

## 2. Historical stationary consequence, including sine projections

Let \(\mathbf X\) be any stationary DPP on \(\mathbb Z\), with stationary
kernel operator \(0\leq K\leq I\). Its restriction to a block of length
\(m\) has the principal-compression kernel \(K_m\), which is a positive
contraction. After the channel, the actual block law is

\[
\operatorname{DPP}(aI_m+cK_m).
\]

Theorem 1 therefore supplies the same normalized strong Jensen inequality
for every block length. Divide by \(m\) and pass to the ordinary
block-entropy limits at the three parameters in that inequality.

> **Corollary 2.**
> For every stationary DPP and every \(0\leq c\leq12/25\), the output
> entropy rate is strongly concave in \(a\) on \([0,1-c]\), with modulus
> \(\kappa_*\). This includes every measurable projection symbol
> \(\mathbf1_E\), at every density, and in particular every fixed-positive-
> density discrete sine projection.

This is a stationary result, not merely a statement about cyclic projection
approximants. No entropy-rate derivative is taken.

## 3. Fixed-dimensional endpoint expansion

The endpoint expansion gives additional negative curvature for each fixed
projection, but it does not enlarge the current \(312/625\) stationary
theorem.

Let \(P\) be a rank-\(k\) projection and \(0<c<1\). Suppose first that its
projection DPP has full support on the \(k\)-slice. At \(a=0\), the output
is a \(c\)-thinning of a \(k\)-point input, so all configurations of size
greater than \(k\) have zero mass. For a \((k+1)\)-set \(T\),

\[
\mathbb P_a(Y=T)
=a c^k\sum_{j\in T}\det P_{T\setminus\{j\}}+O(a^2).
\]

Summing over \(T\), using
\(\sum_{|S|=k}\det P_S=1\), gives

\[
\sum_{|T|=k+1}
\left.\frac{d}{da}\mathbb P_a(Y=T)\right|_{a=0}
=(n-k)c^k.                                             \tag{13}
\]

All size-\(\leq k\) atoms are positive at \(a=0\) under the full-support
assumption. Atoms vanishing to order at least two contribute only
\(O(|\log a|)\) to the second derivative. Applying
\(-x\log x\) atom by atom therefore yields

\[
H_{P,c}''(a)
=-\frac{(n-k)c^k}{a}+O_{n,P,c}(|\log a|)
\qquad(a\downarrow0).                                  \tag{14}
\]

If the projection law has support zeros, additional first-order atoms can
only add further negative \(1/a\) terms; (13) remains a universal
cardinality-sector contribution.

By complementation, with
\(\varepsilon=1-c-a\downarrow0\),

\[
H_{P,c}''(a)
=-\frac{k c^{\,n-k}}{\varepsilon}
+O_{n,P,c}(|\log\varepsilon|)                          \tag{15}
\]

under the analogous full-support assumption for the complement.

Equations (14)--(15) prove a one-sided strictly concave neighborhood of
each channel endpoint for every fixed \(n\). They do not provide a
neighborhood uniform in \(n\).

## 4. Why the endpoint main term is not volume-uniform

For a half-density projection, the normalized coefficient in (14) is

\[
\frac{n-k}{n}c^k=\frac12c^{n/2},
\]

which tends to zero exponentially for every fixed \(c<1\). Contiguous
finite Fourier projections are full spark: their maximal minors are
Vandermonde determinants at distinct roots of unity. Hence the half-density
sine approximants realize this decay; projection structure does not restore
a dimension-uniform \(1/a\) coefficient.

There is a second, complementary obstruction in the high-contrast scaling

\[
c=1-d,\qquad a=db,\qquad 0<b<1,\qquad d\downarrow0.
\]

For any fixed law \(p\) on the \(k\)-slice and any compact
\(J\Subset(0,1)\), the exact chain rule and the one-flip posterior
classification give, in \(C^2(J)\),

\[
\begin{aligned}
H(Y_{d,b})
={}&H(p)+(n-k)\eta(db)+k\eta(d(1-b))\\
&-d[bC_+(p)+(1-b)C_-(p)]
+O_{n,k,p,J}^{C^2}(d^2|\log d|),
\end{aligned}                                          \tag{16}
\]

where \(C_+\) and \(C_-\) are the finite addition and deletion ambiguity
entropies. Their coefficient is affine in \(b\), so

\[
\frac{\partial^2}{\partial b^2}H(Y_{d,b})
=-d\left(\frac{n-k}{b}+\frac{k}{1-b}\right)
+O_{n,k,p,J}(d^2|\log d|).                             \tag{17}
\]

For fixed \(n,k,p\), (17) proves strict concavity for sufficiently small
\(d\). For a full-support slice law, however, a same-cardinality output has
\(k(n-k)\) one-exchange alternative inputs. Their posterior entropy contains

\[
2k(n-k)d^2b(1-b)|\log d|+O_{n,k,J}(d^2).               \tag{18}
\]

Since \(H(X\mid Y)\) is subtracted in the chain rule, (18) contributes the
adverse positive curvature

\[
4k(n-k)d^2|\log d|+O_{n,k,J}(d^2).                    \tag{19}
\]

At fixed density, the negative term in (17) is \(O(nd)\), while (19) is
\(O(n^2d^2|\log d|)\). Thus this expansion closes only in a regime such as
\(nd|\log d|\ll1\). The \(n^2\) coefficient is real for full-spark Fourier
projections, including half-density sine approximants.

Actual stationary blocks behave differently from finite cyclic
projections. If \(0<|E|<1\), every finite Toeplitz compression of
\(\mathbf1_E\) satisfies \(0<K_m<I\): for a nonzero trigonometric
polynomial \(v\), both
\(\int_E|v|^2\) and \(\int_{E^c}|v|^2\) are positive. Hence its endpoint
word law has no finite-block support zeros. The singular expansion
(14) belongs to the cyclic projection approximation and cannot simply be
identified with a stationary block expansion.

## 5. Historical numerical probe and the remaining gap

The proof of Theorem 1 separates the maximum of \(A(a)A(d)\) from the
minimum of \(h_c(a)^8\). Retaining their common \(a\)-dependence gives the
smaller scalar budget

\[
B_{\rm exact}(a,c)=
\frac{c^4A(a)A(d)}{32h_c(a)^8}.                         \tag{20}
\]

A direct numerical scan of this older separated budget gives

\[
\max_a B_{\rm exact}(a,12/25)
\approx3.232119095<4,
\]

and suggests that this particular exact budget reaches \(4\) near
\(c\approx0.482498\). This numerical threshold is already subsumed by the
current \(312/625\) theorem.  It is retained only to diagnose the loss in
the older separated estimate; no global symbolic optimization or monotonicity
theorem for (20) is asserted.

For \(c>312/625\), neither ordinary entropy concavity nor its failure is
proved by the package. The minimal obstruction exposed by the endpoint route
is now precise:

1. the universal posterior fourth-energy estimate loses the diagonal
   information of the full posterior and its sufficient budget exceeds the
   diagonal Fisher reserve shortly above \(0.48\);
2. the fixed-\(n\) endpoint \(1/a\) term has exponentially vanishing
   normalized coefficient on positive-density sine approximants;
3. the small-\(d\) fixed-slice expansion has a genuine
   \(k(n-k)d^2|\log d|\) exchange sector and cannot be passed termwise to
   fixed-density stationary limits.

To advance beyond this point one needs a volume-uniform resummation of all
exchange orders, or a stronger posterior estimate that uses the stationary
projection/Fourier structure jointly with the pair diagonals. A fixed-\(n\)
endpoint sign, number rigidity, or a finite fourth-order Taylor coefficient
does not supply that missing estimate.

## 6. Result ledger

- **HISTORICAL, SUPERSEDED:** the independent finite positive-contraction
  proof through \(c\leq12/25\), with the explicit modulus (1), and its direct
  stationary block transfer.  The current audited theorem reaches
  \(c\leq312/625\).
- **PROVED:** the fixed-dimensional endpoint expansions (14)--(15) under
  full support, with additional negative singular terms possible when
  support zeros occur.
- **PROVED:** fixed-\(n\) high-contrast strict concavity on compact
  \(b\)-subintervals, and the nonuniform exchange coefficient (18).
- **HISTORICAL NUMERICAL DIAGNOSTIC:** the separated scalar budget (20)
  appears usable until approximately \(c=0.482498\), below the current
  theorem.
- **OPEN PACKAGE-WIDE:** every assertion for \(c>312/625\), including the
  full high-contrast stationary sine conjecture.
