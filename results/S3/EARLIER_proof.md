# S3 continuation: completion obstructions, exact absorption, and a scoped assembly

**Status: PROVED_SCOPED_LEMMA. The S-sine entropy-rate target is not proved.**

All logarithms are natural. This manuscript is independent of any repository or prior conversation. “New” below means newly proved in this continuation, not a claim of priority in the literature.

## 1. Results and scope

The new results are the following.

1. **The sufficient completion estimate (C) is false.** A two-coordinate, rank-one projection with `c = 19/20` gives an exact interior counterexample. The excess in (C) is greater than 15, while the complete output entropy has second derivative less than -552 at that same point. More generally, the completion excess has an explicitly computed positive `1/a` coefficient near an endpoint. For every fixed `0<c<1`, there are constant-diagonal, full-support Fourier projections for which **every possible first coordinate** violates (C) near both endpoints.

2. **The completion failure is absorbed at the endpoints in each fixed dimension.** For every fixed homogeneous binary input law, not just a projection DPP, its complete channel-output entropy is concave in sufficiently small neighborhoods of both endpoints. An explicit coefficient-based error bound is given. The latent conditioning tree gives an exact, signed telescoping of the positive and negative completion coefficients. The neighborhood is not uniform in dimension or in the input law.

3. **A compatible independent-block theorem holds in all dimensions.** Any fixed input law that is a product over disjoint blocks of size at most two has complete output entropy satisfying
   \[
   H_n''(a,c)\le -4n,\qquad 0<a<1-c.
   \]
   Therefore
   \[
   H_n(a_t,c)\ge (1-t)H_n(a_0,c)+tH_n(a_1,c)
      +2n t(1-t)(a_1-a_0)^2.
   \]
   This includes DPP kernels block diagonal with blocks of size at most two. It does **not** include the sine Toeplitz blocks.

The inherited spectral-mixture reduction is re-proved in Section 8. Its error remains a bound on **finite entropy deficits**, not on derivatives. The unresolved signed averaged projection deficit is identified in Section 10.

## 2. Definitions and complete-atom differentiation

Let `0<c<1`, put `d=1-c`, and let `0<=a<=d`. For an input bit `x`, define the binary channel
\[
W_{a,c}(1\mid x)=a+cx,\qquad
W_{a,c}(0\mid x)=1-a-cx.
\]
For a fixed probability law `mu` on `{0,1}^n`, let `Y_a` be obtained by applying this channel independently in all coordinates to `X~mu`. Its complete atom law is
\[
p_a(y)=\sum_x\mu(x)\prod_{i=1}^n
 (a+cx_i)^{y_i}(1-a-cx_i)^{1-y_i}.
\tag{2.1}
\]
Each atom is a polynomial of degree at most `n`. Every atom is strictly positive for `0<a<d`. Define
\[
H_\mu(a,c)=-\sum_y p_a(y)\log p_a(y).
\]

A law is **homogeneous of rank r** if it is supported on configurations with exactly `r` ones. It has **full layer support** if every such configuration has positive probability.

For a Hermitian contraction `0<=Q<=I`, `DPP(Q)` is the law specified by
\[
\Pr(A\subseteq X)=\det Q[A].
\]
Inclusion probabilities determine the complete atom law by inclusion-exclusion. For a projection `P=UU*` of rank `r`, its law is homogeneous and
\[
\Pr(X=T)=|\det U_T|^2,\qquad |T|=r.
\tag{2.2}
\]
The weights in (2.2) sum to one by Cauchy--Binet. The identity for their inclusion probabilities also follows by expanding
`det(U* diag(z_i) U)` in the variables `z_i-1`. Equivalently, the count generating function is `det(I+(z-1)P)=z^r`.

Write `mathsf H(P;a,c)=H_{DPP(P)}(a,c)`. The channel maps `DPP(Q)` to `DPP(aI+cQ)`: indeed, for every coordinate set `A`,
\[
\begin{aligned}
\Pr(A\subseteq Y)
 &=\mathbb E\prod_{i\in A}(a+cX_i)\\
 &=\sum_{B\subseteq A}a^{|A|-|B|}c^{|B|}\det Q[B]
 =\det(aI_A+cQ[A]).
\end{aligned}
\tag{2.3}
\]
Thus (2.3) proves an identity of complete laws, not merely of counts.

### 2.1 Exact jets

Allow separate offsets `a_i` temporarily, keeping the input law and contrast fixed. With `sigma_i(y)=2y_i-1`,
\[
\partial_{a_i}p(y)=\sigma_i(y)p_{-i}(y_{-i})=:D_ip(y).
\tag{2.4}
\]
The marginal on the right is independent of `a_i`. Hence `D_i^2=0`, the operators commute, and on the common-offset diagonal,
\[
p'=\sum_iD_ip,
\qquad
p''=2\sum_{i<j}D_iD_jp.
\tag{2.5}
\]
For `0<a<d`,
\[
H_\mu''=-\sum_y p_y''\log p_y-\sum_y\frac{(p_y')^2}{p_y}.
\tag{2.6}
\]
The first term in (2.6) is retained throughout. No atom or conditioning weight is frozen.

## 3. Legal latent conditioning and the exact expression for (C)

Let `P` be an `n`-coordinate projection of rank `r`, and isolate the last coordinate:
\[
P=\begin{pmatrix}A&u\\u^*&q\end{pmatrix},\qquad 0<q<1.
\]
From `P^2=P`,
\[
\|u\|^2=q(1-q),\qquad Au=(1-q)u,\qquad A^2+uu^*=A.
\]
The conditional latent kernels are
\[
P^{(1)}=A-\frac{uu^*}{q},\qquad
P^{(0)}=A+\frac{uu^*}{1-q}.
\tag{3.1}
\]
They are projections of ranks `r-1` and `r`. To check idempotence, split into the span of `u` and its orthogonal complement. On the former, their eigenvalues are respectively zero and one; on the latter they both equal the projection induced by `A`. In particular,
\[
P^{(0)}-P^{(1)}=vv^*,\qquad
v=\frac{u}{\sqrt{q(1-q)}}.
\tag{3.2}
\]

The conditional-law assertion follows directly from determinants. Inclusion conditioning uses the Schur complement. For exclusion conditioning, for each set `B` of remaining coordinates,
\[
\det P[B]-\det P[B\cup\{n\}]
=(1-q)\det\left(P[B]+\frac{u_Bu_B^*}{1-q}\right).
\]
This identity also holds when a displayed submatrix is singular, by polynomial continuity.

If `q=0` or `q=1`, then `u=0`; the last latent bit is deterministic and the only nonzero-probability branch is the remaining projection. These cases require no division by zero.

Let `Z=X_n`. Put `gamma_0=1-q`, `gamma_1=q`. Let `r_z(v;a)` be the complete output law of the remaining coordinates in branch `Z=z`, and set
\[
k_z(b;a)=(a+cz)^b(1-a-cz)^{1-b},\qquad
h_z(v,b;a)=r_z(v;a)k_z(b;a).
\]
Then
\[
p(v,b;a)=\sum_{z=0}^1\gamma_zh_z(v,b;a).
\tag{3.3}
\]
Every branch in (3.3) moves along its actual legal common diagonal shift `aI+cP^(z)`. The weights `gamma_z` are independent of `a`.

The exact entropy decomposition is
\[
\begin{aligned}
\mathsf H(P;a,c)={}&
q\{\mathsf H(P^{(1)};a,c)+b(a+c)\}\\
&+(1-q)\{\mathsf H(P^{(0)};a,c)+b(a)\}+I_a(Z;Y),
\end{aligned}
\tag{3.4}
\]
where `b(s)=-s log s-(1-s)log(1-s)`.

### 3.1 All acceleration and moving-posterior terms

With `sigma_b=2b-1`, the conditional atom derivatives are
\[
h_z'=r_z'k_z+\sigma_b r_z,
\qquad
h_z''=r_z''k_z+2\sigma_b r_z'.
\tag{3.5}
\]
In particular the cross term in the second formula is present.

Directly differentiating
`I= sum_{z,y} gamma_z h_z log h_z - sum_y p log p`
gives
\[
\boxed{
I_a''=
\sum_{z,y}\gamma_z h_z''(y)\log\frac{h_z(y)}{p(y)}
+\sum_{z,y}\gamma_z\frac{h_z'(y)^2}{h_z(y)}
-\sum_y\frac{p'(y)^2}{p(y)}.
}
\tag{3.6}
\]
Equivalently, with `s_z=h_z'/h_z` and `s=p'/p`,
\[
I_a''=
\sum_{z,y}\gamma_z h_z''(y)\log\frac{h_z(y)}{p(y)}
+\sum_{z,y}\gamma_z h_z(y)(s_z(y)-s(y))^2.
\tag{3.7}
\]
The second term is the nonnegative Fisher-information loss. Equations (3.5)--(3.7) include the motion of the posterior probabilities `Pr(Z=z|Y=y)`. They are not obtained by differentiating with fixed posterior weights.

Define
\[
B_q(a,c)=\frac{1-q}{a(1-a)}+
          \frac{q}{(a+c)(d-a)}
\]
and the **completion excess**
\[
R_P(a,c):=\mathsf H''(P;a,c)
-q\mathsf H''(P^{(1)};a,c)
-(1-q)\mathsf H''(P^{(0)};a,c).
\tag{3.8}
\]
Differentiating (3.4), using `b''(s)=-1/[s(1-s)]`, gives
\[
\boxed{R_P(a,c)=I_a''(Z;Y)-B_q(a,c).}
\tag{3.9}
\]
Consequently, the proposed sufficient estimate (C) is exactly the assertion `R_P<=0`.

## 4. A rigorously certified interior counterexample to (C)

Take
\[
P=vv^*,\qquad v=\frac1{10}(1,\sqrt{99})^T,
\qquad q=P_{22}=\frac{99}{100},
\]
\[
c=\frac{19}{20}>\frac{37}{40},\qquad a=\frac1{1000}.
\tag{4.1}
\]
This is a rank-one orthogonal projection with full layer support. Its conditional latent projections are `P^(1)=[0]` and `P^(0)=[1]`.

For general `a,c,q` in this two-coordinate rank-one family, let `z=a(d-a)` and order the complete atoms as `00,01,10,11`. Up to interchanging the two middle atoms, they are
\[
\alpha=(1-a)(d-a),\quad
\beta=z+cq,\quad
\gamma=z+c(1-q),\quad
\delta=a(a+c).
\tag{4.2}
\]
At (4.1), the four numerators over the common denominator `10^6` are
\[
\alpha:\ 48951,\qquad
\beta:\ 940549,\qquad
\gamma:\ 9549,\qquad
\delta:\ 951.
\tag{4.3}
\]
They are positive and sum to `10^6`. Their derivatives are
\[
\alpha'=-\frac{131}{125},\qquad
\beta'=\gamma'=\frac6{125},\qquad
\delta'=\frac{119}{125};
\]
the second derivatives are `2,-2,-2,2`.

Put
\[
L=\frac{\beta\gamma}{\alpha\delta}
=\frac{997922489}{5172489},
\qquad
F=\frac{\alpha'^2}{\alpha}+
\frac{\beta'^2}{\beta}+
\frac{\gamma'^2}{\gamma}+
\frac{\delta'^2}{\delta}.
\]
Equation (2.6) becomes
\[
\mathsf H''(P;a,c)=2\log L-F.
\tag{4.4}
\]
Since the two conditional entropies are `b(a)` and `b(a+c)`,
\[
R_P=2\log L+T,
\]
where the following is an exact rational identity:
\[
\begin{aligned}
T&=-F+\frac{q}{a(1-a)}+
             \frac{1-q}{(a+c)(d-a)}\\
 &=\frac{240392711171000000}{15485229291615363}>15.
\end{aligned}
\tag{4.5}
\]
Also `L>1`. It follows without a floating-point logarithm that
\[
\boxed{R_P>15.}
\tag{4.6}
\]
Thus (C) is false.

### 4.1 This is not a counterexample to entropy concavity

Indeed `L<200`, while just the `11`-atom Fisher contribution is
\[
\frac{\delta'^2}{\delta}=\frac{906304}{951}>950.
\]
Using `log x<=x-1`,
\[
\mathsf H''(P;a,c)=2\log L-F
<2(200-1)-950=-552.
\tag{4.7}
\]
The full negative branch curvature therefore absorbs the positive completion excess at this exact point. Section 7 proves concavity on the **entire legal interval** for every two-coordinate input law, including this example.

All rational identities and strict comparisons above are independently checked using Python's exact `Fraction` arithmetic in `scripts/certify_completion.py`. The proof of (4.6)--(4.7) needs only those rational comparisons and the elementary logarithm inequality, not a numerical approximation.

## 5. Endpoint curvature for every fixed homogeneous input

The next theorem both generalizes the completion obstruction and quantifies its absorption.

### Theorem 5.1 — the full-atom endpoint coefficient

Let `mu` be a fixed homogeneous rank-`r` law on `n` coordinates, with `0<c<1` fixed. Define
\[
A_-(\mu,c)=\sum_{y:p_y(0)=0}p_y'(0).
\tag{5.1}
\]
Then
\[
H_\mu''(a,c)=-\frac{A_-(\mu,c)}a+
O_{\mu,c,n}(1+|\log a|),\qquad a\downarrow0,
\tag{5.2}
\]
and
\[
A_-(\mu,c)\ge(n-r)c^r.
\tag{5.3}
\]
If `mu` has full layer support, equality holds in (5.3).

Writing `bar(mu)` for the input law after complementing every bit,
\[
H_\mu''(a,c)=-\frac{A_-(\bar\mu,c)}{d-a}
 +O_{\mu,c,n}(1+|\log(d-a)|),\qquad a\uparrow d,
\tag{5.4}
\]
with
\[
A_-(\bar\mu,c)\ge r c^{n-r},
\]
and equality for full layer support.

#### Proof

For each output atom, factor its polynomial at zero as
\[
p_y(a)=a^{k_y}r_y(a),\qquad k_y\ge0,\quad r_y(0)>0.
\]
Such a factorization exists because every atom is a nonzero polynomial positive on `(0,d)`.

If `k_y=0`, that atom's entropy contribution has bounded second derivative near zero. If `k_y=1`, direct substitution into (2.6) gives
\[
(-p_y\log p_y)''=-\frac{r_y(0)}a+O(1+|\log a|).
\]
If `k_y>=2`, the contribution is `O(1+|log a|)`. There are finitely many atoms. Summing proves (5.2), since the linear-zero coefficients are precisely the nonzero terms in (5.1). This argument differentiates the actual atom polynomials; it does not infer derivative estimates from a small bound on entropy values.

At `a=0`, no false positive is possible. Therefore every output set of size `r+1` has zero probability. Its first derivative is
\[
p_S'(0)=c^r\sum_{\substack{T\subset S\\|T|=r}}\mu(T),
\qquad |S|=r+1.
\tag{5.5}
\]
Each input set `T` has exactly `n-r` supersets of size `r+1`. Summing (5.5) gives `(n-r)c^r`. Other linear-zero atoms can only increase (5.1), proving (5.3).

For full layer support, every output set of size at most `r` has strictly positive probability at zero. A set of size greater than `r` has zero of order exactly `|S|-r`, by (2.1). Thus only the sets of size `r+1` contribute, proving equality.

Finally, complementing input and output converts `W_(a,c)` into `W_(d-a,c)`. Entropy is unchanged by this bijection. Applying (5.2) to the complement law proves (5.4). ∎

### 5.2 Explicit finite error constants

Here is one coefficient-based choice of all constants in (5.2). It is deliberately not advertised as dimension-stable.

For one atom, write
\[
p(a)=a^k r(a),\quad r(a)=r_0+\sum_{j\ge1}r_j a^j,\quad r_0>0,
\]
and define
\[
B=\sum_{j\ge1}|r_j|,\quad
D_1=\sum_{j\ge1}j|r_j|,\quad
D_2=\sum_{j\ge2}j(j-1)|r_j|,\quad R=r_0+B.
\]
Take
\[
\delta=\min\left\{d/2,1,
\min_{y:B_y>0}\frac{r_{y,0}}{2B_y}\right\},
\tag{5.6}
\]
where the minimum over an empty set imposes no restriction. For `0<a<=delta`,
\[
r_0/2\le r(a)\le R,\quad |r'(a)|\le D_1,\quad |r''(a)|\le D_2.
\]
Set
\[
M=\max\{|\log(r_0/2)|,|\log R|\}.
\]
The following per-atom constants work:
\[
C_y=
\begin{cases}
D_2M+2D_1^2/r_0,&k=0,\\[2mm]
(2D_1+D_2)(1+M)+B+2D_1+2D_1^2/r_0,&k=1,\\[2mm]
U(k+M)+k^2R+2kD_1+2D_1^2/r_0,&k\ge2,
\end{cases}
\tag{5.7}
\]
where `U=k(k-1)R+2kD_1+D_2` in the last case. With `C=sum_y C_y`,
\[
\left|H_\mu''(a,c)+\frac{A_-(\mu,c)}a\right|
\le C(1+|\log a|),\qquad 0<a\le\delta.
\tag{5.8}
\]

The constants in (5.7) bound the summands of the **normalized global Hessian** (2.6). An individual second derivative `(-p log p)''` also contains `-p''`; these extra terms cancel exactly in the sum because `sum_y p_y''=0`. No such term is being dropped from the total entropy derivative.

To verify (5.7), use
\[
p''=k(k-1)a^{k-2}r+2ka^{k-1}r'+a^kr'',
\]
\[
\frac{p'^2}{p}
=a^{k-2}\left(k^2r+2ka r'+a^2\frac{r'^2}{r}\right).
\]
For `k=1`, separate `r_0/a` from `r(a)/a` and use
`|r(a)-r_0|/a<=B`. The displayed bounds then give (5.7) term by term.

If `A=A_-(mu,c)>0` and `C>0`, put
\[
\varepsilon_-=
\min\{\delta,(A/(4C))^2\}.
\tag{5.9}
\]
Since `a(1+log(1/a))<=2 sqrt(a)` for `0<a<=1`, (5.8) implies
\[
H_\mu''(a,c)\le -\frac{A}{2a}<0,
\qquad 0<a\le\varepsilon_-.
\tag{5.10}
\]
If `C=0`, use `epsilon_-=delta`. Apply the same construction to the complement law for `epsilon_+`.

For `0<r<n`, both endpoint coefficients are positive by (5.3)--(5.4). Thus the full entropy is concave on `[0,epsilon_-]` and `[d-epsilon_+,d]`. Continuity at the endpoints follows from polynomial atom probabilities and `0 log 0=0`. The cases `r=0` and `r=n` are deterministic inputs and have entropy respectively `n b(a)` and `n b(a+c)`, concave on the whole legal interval.

The constants contain the smallest leading atom coefficients and can deteriorate badly with `n`. Neither (5.9) nor (5.10) supplies a fixed positive neighborhood valid for the sine entropy-rate limit.

## 6. Completion asymptotics, balanced obstructions, and signed assembly

### 6.1 Exact asymptotic excess

Suppose the rank-`r` projection `P` has full layer support, `0<r<n`, and isolate a coordinate with latent probability `q`. Both conditional laws have full layer support on their respective ranks. Theorem 5.1 and (3.8) give
\[
\boxed{
R_P(a,c)=\frac{c^{r-1}}a
\left[q(n-r)(1-c)-(1-q)c\right]
+O_{P,c,n}(1+|\log a|).
}
\tag{6.1}
\]
Indeed, the three left-end coefficients are
\[
A(P)=(n-r)c^r,
\quad A(P^{(1)})=(n-r)c^{r-1},
\quad A(P^{(0)})=(n-r-1)c^r.
\]
Therefore (C) fails for all sufficiently small positive `a` whenever
\[
q>\frac{c}{c+(n-r)(1-c)}.
\tag{6.2}
\]
By complementation it fails near `a=d` whenever
\[
(1-q)r(1-c)>qc.
\tag{6.3}
\]
A positive coefficient in (6.1) gives an unbounded completion excess as `a` tends to zero. This is more than a change in the constant in (C).

### 6.2 No first-coordinate choice repairs (C) for these projections

Fix any `0<c<1`. Choose an integer
\[
r>\frac{c}{1-c},\qquad n=2r.
\]
Let `omega=exp(2 pi i/n)` and
\[
U_{jk}=n^{-1/2}\omega^{jk},\qquad
0\le j<n,\quad 0\le k<r,
\qquad P=UU^*.
\tag{6.4}
\]
The columns of `U` are orthonormal by the finite geometric sum. Hence `P` is a projection of rank `r`, with every diagonal entry `r/n=1/2`.

Every `r`-row minor of `U` is a nonzero Vandermonde determinant, because its row parameters are distinct roots of unity. Thus its projection DPP has full layer support. With `q=1/2`, the coefficient in (6.1) is
\[
\frac{c^{r-1}}2\{r(1-c)-c\}>0.
\tag{6.5}
\]
The same coefficient occurs at the upper endpoint. Since this argument applies to every coordinate, no choice of first latent coordinate makes (C) valid near either endpoint. For a common neighborhood for all choices, take the minimum of their finitely many positive endpoint neighborhood sizes; the dimension is fixed in this assertion.

For an explicit high-contrast instance take `c=19/20`, `r=20`, `n=40`. At every coordinate,
\[
R_P(a,c)=\frac{c^{19}}{40a}+O(1+|\log a|)
\]
at the left endpoint, and the analogous formula holds with `a` replaced by `d-a` at the right endpoint.

These are counterexamples to (C) for **finite Fourier projections**. They are not counterexamples to general projection concavity, and they are not assertions about the particular random spectral projections of `Q_n`.

### 6.3 Absorption by the actual branches

For a full-support projection the weighted branch curvature is
\[
q\mathsf H''(P^{(1)})+(1-q)\mathsf H''(P^{(0)})
=-\frac{c^{r-1}}a
\left[q(n-r)+(1-q)(n-r-1)c\right]
+O(1+|\log a|).
\tag{6.6}
\]
Adding (6.1) to (6.6) gives exactly
\[
-\frac{(n-r)c^r}{a}+O(1+|\log a|).
\tag{6.7}
\]
Thus the positive completion excess is absorbed by the **true** negative branch curvature in a sufficiently small endpoint neighborhood. There is no independent reuse of a coordinate Fisher contribution in (6.6).

### 6.4 The complete latent tree and multiplicities

Fix a coordinate order. A node `v` is a feasible latent prefix. Its weight
\[
\pi_v=\Pr(X_{\mathrm{prefix}}=v)
\]
is independent of `a`. Conditional on the prefix, the remaining input is a projection DPP, obtained successively by (3.1); deterministic branches are handled as stated after (3.2). Write its entropy as `H_v`, its next-bit probability as `q_v`, and let
\[
R_v=H_v''-(1-q_v)H_{v0}''-q_vH_{v1}''.
\]
At a leaf there are no remaining coordinates and `H_leaf=0`. Exact telescoping gives
\[
\boxed{H_{\rm root}''=\sum_{v\text{ nonleaf}}\pi_v R_v.}
\tag{6.8}
\]
Every nonroot node's full entropy Hessian occurs once with positive weight `pi_v` and once with negative weight from its parent. Those occurrences cancel. Equivalently, every intermediate complete-atom Fisher and acceleration sum cancels with exactly the same complete-atom weights. No pairwise overlap charge is used.

Let `A_v=A_-(mu_v,c)` and write
\[
H_v''=-A_v/a+e_v(a).
\]
The leading completion coefficient is
\[
V_v=-A_v+(1-q_v)A_{v0}+q_vA_{v1}.
\]
Consequently,
\[
\boxed{\sum_v\pi_vV_v=-A_{\rm root}.}
\tag{6.9}
\]
For full layer support, a node with `m` remaining coordinates and remaining rank `k` has
\[
A_v=(m-k)c^k,
\]
and for a nondeterministic node
\[
V_v=c^{k-1}\{q_v(m-k)(1-c)-(1-q_v)c\}.
\tag{6.10}
\]
For a deterministic zero next bit, `V_v=-1`; for a deterministic one next bit, `V_v=0`. Formula (6.9) includes these cases.

The remainders telescope as well:
\[
\sum_v\pi_v\{e_v-(1-q_v)e_{v0}-q_ve_{v1}\}=e_{\rm root}.
\tag{6.11}
\]
Therefore the endpoint error can be bounded by the root constant in (5.8), not by an artificially accumulated positive-part sum over the tree.

Equations (6.8)--(6.11), together with (5.8)--(5.10), constitute a compatible signed assembly for the **fixed-dimensional endpoint theorem**. They do not establish a nonpositive or sublinear curvature defect at a fixed interior parameter as `n` grows.

## 7. A new two-coordinate inequality and a compatible independent-block theorem

### Theorem 7.1 — universal two-coordinate common-offset bound

For any fixed input law on two bits and any `0<c<1`, its complete channel-output entropy satisfies
\[
H''(a,c)\le-8,\qquad 0<a<1-c.
\tag{7.1}
\]
No DPP or negative-dependence assumption is needed.

#### Proof

Let the current strictly positive output table be
`alpha,beta,gamma,delta` in order `00,01,10,11`. Put
\[
k=\alpha-\delta,\qquad M=\beta+\gamma=1-\alpha-\delta.
\]
Equations (2.4)--(2.5) give the exact jets
\[
p'=(-(1+k),k,k,1-k),\qquad p''=(2,-2,-2,2).
\]
Thus
\[
H''=2\log\frac{\beta\gamma}{\alpha\delta}
-\frac{(1+k)^2}{\alpha}-\frac{(1-k)^2}{\delta}
-k^2\left(\frac1\beta+\frac1\gamma\right).
\tag{7.2}
\]
For fixed `alpha,delta`, write `x=beta gamma`. The part of (7.2) depending on the two middle atoms is
\[
2\log x-\frac{k^2M}{x}.
\]
Its derivative in `x` is `2/x+k^2M/x^2>0`. Therefore (7.2) is maximized by equalizing the middle atoms: `beta=gamma=M/2`.

Set
\[
S=\alpha+\delta,\quad M=1-S,\quad
V=\sqrt{S^2-k^2}=2\sqrt{\alpha\delta}.
\]
Here `0<V<=S<1`. The Fisher term for the equalized table is
\[
F_{\rm eq}=\frac4S+
\frac{4k^2M^2}{SV^2}+\frac{4k^2}{M}.
\tag{7.3}
\]
It obeys
\[
F_{\rm eq}\ge4\left(1+\frac MV\right).
\tag{7.4}
\]
For an explicit algebraic verification of (7.4), put `x=V/M>0` and `tau=S/M>0`. Substitution in (7.3) gives
\[
F_{\rm eq}-4(1+M/V)
=\frac{4(S-V)}{x^2}
\bigl(1-x+\tau x^2+x^3\bigr).
\tag{7.5}
\]
The bracket is positive: if `x<=1`, use `1-x>=0`; if `x>=1`, use `x^3-x>=0`. All other factors in (7.5) are nonnegative.

For the equalized table the logarithmic term in (7.2) is `4 log(M/V)`. Hence, with `z=M/V>0`,
\[
H''\le4\log z-4(1+z)\le-8,
\]
where the last inequality is `log z<=z-1`. This proves (7.1). All acceleration and Fisher terms in (7.2) have been retained. ∎

The bound is sharp: the equality case is the uniform four-atom output table. It is attainable for every fixed contrast by taking two independent unbiased input bits and `a=(1-c)/2`.

### Theorem 7.2 — disjoint blocks of size at most two

Suppose the fixed input law factors over a partition into independent blocks of size one or two. Then for every dimension `n`, every `0<c<1`, and every interior `a`,
\[
H_n''(a,c)\le-4n.
\tag{7.6}
\]
For every `a_0,a_1 in [0,1-c]` and `t in [0,1]`,
\[
\boxed{
H_n(a_t,c)\ge(1-t)H_n(a_0,c)+tH_n(a_1,c)
+2nt(1-t)(a_1-a_0)^2.
}
\tag{7.7}
\]

#### Proof and exact allocation

Independent coordinate channels preserve the independence of these blocks. Thus the actual complete output law is a product of the actual block laws and its entropy is their sum. A one-bit block has success probability `a+c mu(X=1)` and second derivative at most `-4`. A two-bit block contributes at most `-8` by Theorem 7.1. Summing proves (7.6).

At the level of (2.6), each block Fisher term is used once. The joint score is the sum of independent block scores of mean zero, so its cross products have zero expectation. The cross-block acceleration products also integrate to zero against the sum of block log probabilities, using `sum p_block'=sum p_block''=0`. No moving weight is suppressed.

The function `H_n(a,c)+2na^2` has nonpositive second derivative in the interior. Its concavity gives (7.7) there. Finite-atom continuity extends (7.7) to both endpoints. The boundary and finite-size error is exactly zero. ∎

In particular, (7.7) holds for `DPP(aI+cQ)` whenever `Q` is block diagonal with blocks of size at most two. Its DPP law factors because the generating determinant factors, or equivalently because all inclusion probabilities factor.

This cannot be applied to the sine blocks merely by grouping coordinates into pairs. For example, `|q_1|=sin(pi rho)/pi>0`, and any partition into blocks of size at most two leaves at least `n-1-floor(n/2)` nearest-neighbor edges outside the blocks. Any matrix block diagonal for that partition differs from `Q_n` in squared Hilbert--Schmidt norm by at least
\[
2\{n-1-\lfloor n/2\rfloor\}|q_1|^2.
\]
This is a linear geometric discrepancy for fixed `rho`. It is not itself an entropy lower bound, but no sublinear entropy replacement error has been proved for such a pairing approximation.

## 8. Re-verification of the inherited spectral-mixture reduction

Let `Q` be any Hermitian contraction on `n` coordinates, with eigenvalues `lambda_j` and orthonormal eigenvectors `u_j`. Independently include mode `j` in `J` with probability `lambda_j`, and put
\[
P_J=\sum_{j\in J}u_ju_j^*.
\]
Conditional on `J`, let `X~DPP(P_J)`. For any coordinate set `A`, Cauchy--Binet gives
\[
\begin{aligned}
\mathbb E_J\det P_J[A]
 &=\sum_{|L|=|A|}|\det U_{A,L}|^2
                     \prod_{j\in L}\lambda_j\\
 &=\det Q[A].
\end{aligned}
\]
Thus the marginal input is exactly `DPP(Q)`. Applying (2.3), the complete output is exactly `DPP(aI+cQ)`.

The distribution of `J` is independent of `a`. Consequently,
\[
H_Q(a,c)=\mathbb E_J\mathsf H(P_J;a,c)+I(J;Y_a),
\tag{8.1}
\]
\[
0\le I(J;Y_a)\le H(J)=\sum_j b(\lambda_j).
\tag{8.2}
\]
For `a_t=(1-t)a_0+ta_1` define
\[
\mathcal D_F=(1-t)F(a_0)+tF(a_1)-F(a_t).
\]
Since each information term in (8.1) belongs to `[0,H(J)]`,
\[
\left|\mathcal D_{H_Q}
-\mathbb E_J\mathcal D_{\mathsf H(P_J;\cdot,c)}\right|
\le H(J).
\tag{8.3}
\]
Each spectral realization is counted once with its actual probability. The discrepancy is one mutual information, not a sum of pairwise charges.

### 8.1 The sine Toeplitz error

For an interval `E_rho` in `R/Z`, write
\[
q_k=\widehat{\mathbf1_{E_\rho}}(k),\qquad
Q_n=(q_{i-j})_{1\le i,j\le n}.
\]
The quadratic-form integral over `E_rho` proves `0<=Q_n<=I`. It is a compression of a projection, not assumed to be a finite projection. Moreover,
\[
q_0=\rho,\quad
|q_k|=\frac{|\sin(\pi\rho k)|}{\pi|k|}\le\frac1{\pi|k|}
\quad(k\ne0),\qquad
\sum_{k\in\mathbb Z}|q_k|^2=\rho.
\]
Therefore, for `n>=2`,
\[
\begin{aligned}
\operatorname{Tr}(Q_n-Q_n^2)
 &=\sum_{0<|k|<n}|k||q_k|^2
   +n\sum_{|k|\ge n}|q_k|^2\\
 &\le\frac2{\pi^2}(\log n+3).
\end{aligned}
\tag{8.4}
\]
Here use `sum_{k=1}^{n-1}1/k<=1+log n` and
`sum_{k=n}^infty 1/k^2<=1/(n-1)<=2/n`.

For `0<=x<=1`,
\[
b(x)\le2\sqrt{x(1-x)}.
\tag{8.5}
\]
One proof uses `log(1+u^2)<=u` for `u>=0`, whose difference has derivative `(u-1)^2/(1+u^2)>=0`. Apply it with `u=sqrt((1-x)/x)` and then interchange `x` and `1-x`.

Combining (8.4)--(8.5) with Cauchy--Schwarz gives
\[
H(J_n)\le2\sqrt{n\operatorname{Tr}(Q_n-Q_n^2)}
\le\frac{2\sqrt2}{\pi}\sqrt{n(\log n+3)}=o(n).
\tag{8.6}
\]
The bound is uniform in `rho`, `a`, and `c`. For `n=1`, simply use `H(J_1)<=log 2`.

No assertion about `I(J;Y_a)''` follows from (8.2) or (8.6), and none is made here.

## 9. Continuity and rate-limit audit

### 9.1 A uniform continuity modulus

For any fixed input law on `n` bits, couple offsets `a` and `b` by the same input `X` and independent uniform variables `U_i`, setting
\[
Y_i^{(a)}=\mathbf1\{U_i\le a+cX_i\}.
\]
Each coordinate mismatch probability is exactly `delta=|a-b|`. With the error vector `E=Y^(a) xor Y^(b)`,
\[
H(Y^{(a)}\mid Y^{(b)})\le H(E)\le n b(\delta).
\]
The same holds with `a,b` reversed, so
\[
\boxed{|H_n(a,c)-H_n(b,c)|\le n b(|a-b|).}
\tag{9.1}
\]
Thus any existing entropy-rate limit has the modulus
\[
|h(a,c)-h(b,c)|\le b(|a-b|),
\tag{9.2}
\]
including at both endpoints.

### 9.2 How a legitimate finite inequality would pass to the rate

Stationarity and entropy subadditivity give `H_(n+m)<=H_n+H_m`; dividing into blocks of fixed size proves that `H_n/n` converges to its infimum. This argument uses only the full configuration entropies.

If a finite deficit upper bound `o(n)` were proved for every fixed admissible interior triple `(a_0,a_1,t)`, division by `n` and this limit would yield interior rate concavity. Equation (9.2) would then extend it to the endpoints. Neither step needs twice differentiability of `h`.

The results of Sections 5--7 do not supply that bound for `Q_n`. In particular, a neighborhood shrinking with `n` cannot cover a fixed interior triple.

## 10. Precisely what is still missing

For the random spectral projections in Section 8, no proof is supplied of
\[
\mathbb E_J\mathcal D_{\mathsf H(P_{n,J};\cdot,c)}
\le o(n)
\]
for every fixed admissible triple in the requested high-contrast range. No universal replacement for (C) controlling the entire latent tree at a fixed interior `a` has been established.

The following four assertions are distinct:

- coordinate submodularity is false (verified inherited example below);
- the sufficient completion estimate (C) is false (new Sections 4 and 6);
- general projection common-shift entropy concavity is **not disproved or proved here**;
- S-sine entropy-rate concavity is **not disproved or proved here**.

## Appendix A. Verified inherited obstructions

### A.1 Coordinate submodularity

For a positive two-bit table `(alpha,beta,gamma,delta)`, separate-offset differentiation gives
\[
H_{12}=-\log\frac{\alpha\delta}{\beta\gamma}-C_{12},
\]
where, with `Delta=alpha delta-beta gamma` and
`e_3=alpha beta gamma+alpha beta delta+alpha gamma delta+beta gamma delta`,
\[
C_{12}=-\frac{\Delta e_3}{\alpha\beta\gamma\delta}.
\]
The latter identity follows by expanding the four products `D_1p D_2p/p` and using that the atoms sum to one.

Take
\[
\alpha=\delta=\frac{29}{901},\quad
\beta=\frac2{901},\quad\gamma=\frac{841}{901}.
\]
Then `alpha delta/(beta gamma)=1/2` and `C_12=959/1802`, so
\[
H_{12}=\log2-\frac{959}{1802}>0.
\]
For example, `log 2>2/3>959/1802`. This is the complete atom law of
\[
K=\frac1{901}\begin{pmatrix}870&29\\29&31\end{pmatrix}.
\]
Its eigenvalues are `(1-c)/2,(1+c)/2` with `c=sqrt(785/901)>37/40`; hence `K=aI+cP` for a rank-one projection. This is only a counterexample to the sign of a mixed derivative, not to the common-direction bound in Theorem 7.1.

### A.2 Pairwise overcounting

For an `n`-coordinate entropy Hessian,
\[
\sum_{i<j}(\partial_i+\partial_j)^2H
=(\sum_i\partial_i)^2H+(n-2)\sum_iH_{ii}.
\]
Every favorable diagonal term has been counted `n-1` times on the left. Nonpositivity of all two-coordinate common-direction Hessians therefore does not establish the desired global sign.

### A.3 Observed-output conditioning changes the direction

If `K(a)=aI+cP`, conditioning on output coordinate `Y_i=1` gives
\[
K_R^{(1)}(a)=aI_R+cP_R-
\frac{c^2P_{Ri}P_{iR}}{a+cP_{ii}},
\]
\[
\frac d{da}K_R^{(1)}(a)=I_R+
\frac{c^2P_{Ri}P_{iR}}{(a+cP_{ii})^2}.
\]
Conditioning on `Y_i=0` gives the same positive rank-one speed correction with denominator `(1-a-cP_ii)^2`. Unless the off-diagonal column vanishes, these are not common unit diagonal shifts. The legal tree in Section 6 conditions on latent `X`, not observed `Y`.

### A.4 Counts and unitary conjugation

The kernels
\[
K_1=\begin{pmatrix}3/4&0\\0&1/4\end{pmatrix},\qquad
K_2=\begin{pmatrix}1/2&1/4\\1/4&1/2\end{pmatrix}
\]
are unitarily conjugate. Their complete atom laws are respectively
\[
(3,1,9,3)/16,\qquad (3,5,5,3)/16.
\]
They have identical count distributions and identical spectral traces `Tr b(K)`, but strictly different configuration entropies by strict concavity under equalization of the two middle probabilities. No spectral entropy is substituted for configuration entropy in this manuscript.

## Appendix B. A further exact obstruction: acceleration alone is insufficient

This appendix records a failed strengthening of a separate symmetrization approach. It is not used in any positive theorem above.

Let `mu` be homogeneous of rank `r`, let `nu_r` be the uniform law on that layer, and write `p=T_(a,c)mu`, `u=T_(a,c)nu_r`. Their output count laws are identical: conditional on any input of rank `r`, the output count is the sum of `r` Bernoulli variables with parameter `a+c` and `n-r` with parameter `a`. Moreover, `u(y)` depends only on `|y|`. Consequently `sum_y p_y log u_y = sum_y u_y log u_y`, and the exact full-configuration identity is `D(p||u)=H(u)-H(p)`. This uses count layers only to simplify the cross entropy; it does not replace the configuration entropy by count entropy.

For their full-configuration relative entropy, direct differentiation gives
\[
D(p\Vert u)''=
\sum_y p_y''\log(p_y/u_y)
+\sum_y p_y\left(p_y'/p_y-u_y'/u_y\right)^2.
\tag{B.1}
\]
In the usual general formula there is also `-sum p_y u_y''/u_y`. It vanishes here because `u_y''/u_y` is constant within each count layer and the two laws have identical layer masses. Thus (B.1) retains the complete relative-Fisher term.

It is tempting to require the first term in (B.1) to be nonnegative. That strengthening is false, even for a rank-one projection input.

Take `n=3`, `r=1`, with the one-hot probabilities
\[
(w_1,w_2,w_3)=(1/1000,1/5,799/1000),
\quad c=3/10,\quad a=693/1000.
\tag{B.2}
\]
These are the probabilities of the rank-one projection with unit vector having entries `sqrt(w_i)`. All parameters are legal; this particular obstruction is at contrast `3/10`, not in the high-contrast range.

Let `z=a(1-c-a)=4851/10^6`. For a one-hot input on three coordinates, singleton-output atoms are
\[
p_{\{i\}}=(1-a)(z+cw_i),
\]
and two-element-output atoms, indexed by their missing coordinate, are
\[
p_{[3]\setminus\{i\}}=a(z+c(1-w_i)).
\]
For the uniform input replace `w_i` by `1/3`. The zero- and three-element-output atoms agree for the two inputs. The common second derivatives within the singleton and two-element layers are respectively
\[
6a-2(2-c)=379/500,
\qquad 2(1-c)-6a=-1379/500.
\]
Consequently the acceleration term in (B.1) is
\[
\mathcal A=\frac{379}{500}\log R_1-
            \frac{1379}{500}\log R_2,
\tag{B.3}
\]
where exact rational evaluation gives
\[
R_1=\prod_{i=1}^3\frac{z+cw_i}{z+c/3}
=\frac{81691650417051}{1152703815007051}<\frac1{14},
\]
\[
R_2=\prod_{i=1}^3\frac{z+c(1-w_i)}{z+2c/3}
=\frac{38254213470213}{67687822640213}>\frac9{16}.
\]
The elementary inequalities
\[
\log2>2/3,\qquad
\log x\le\frac{x-1}{\sqrt x}\quad(x\ge1)
\]
imply
\[
\log14>7/3,
\qquad \log(16/9)\le7/12.
\]
For the first, use `14^2>2^7`; the second logarithm inequality follows by setting `v=sqrt(x)` and differentiating `v-v^(-1)-2 log v` from `v=1`. Hence
\[
\boxed{
\mathcal A< -\frac{379}{500}\frac73+
                 \frac{1379}{500}\frac7{12}
=-\frac{959}{6000}<0.
}
\tag{B.4}
\]
The exact rational comparisons are checked in `scripts/certify_symmetry_acceleration.py`. No numerical logarithm is used in that certificate.

Equation (B.4) does not determine the sign of (B.1). In particular, the unproved full symmetrization-convexity statement must not be rejected by discarding its positive relative-Fisher term, just as projection concavity must not be rejected merely because (C) fails.
