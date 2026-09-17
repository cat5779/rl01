# S2 check1: two distinct obstructions to composing projection curvature comparisons

**Result status: PROVED_SCOPED_LEMMA.** These are new author proofs and exact certificates, **not independently audited results**. The high-contrast S-sine entropy-rate concavity theorem and general projection (P2) remain unresolved.

## 0. What is new, and what is not

This round proves two consequential failures of a proposed composable extension.

1. **An all-rank, actual-Fourier compatibility obstruction.** For every odd `n` and `3 <= k <= n-4`, suitable two disjoint reflection transpositions of the genuine consecutive Fourier projection have the following property. The first affine permutation chord consists of projection DPP laws, but a second nontrivial affine chord is not the law of **any** Hermitian-contraction DPP. A rank-four conditional Gram matrix proves impossibility, irrespective of the proposed common frame. This applies along `k ~ rho*n` at every fixed `0<rho<1`.
2. **An actual higher-rank curvature reversal, with its error paid exactly.** On the genuine seven-site, rank-three Fourier projection, apply successive physical quadrature rotations to two reflection pairs. Every intermediate kernel is a projection; the outside frame and all diagonal entries are fixed during each step. At `c=19/20`, `a=1/200`, the second physical step has entropy-curvature difference less than `-4/5`, whereas the intended affine second step has difference greater than `4/5`. Their curvature discrepancy is less than `-17/10`. All complete output atoms and both offset derivatives are retained. Exact cubic-field arithmetic and rational logarithm enclosures certify the signs.

The second obstruction tensorizes to a negative comparison/payment of order `n` at density `3/7`. That family is a **block sum**, not the contiguous growing Fourier projection. The first obstruction, in contrast, applies directly to growing contiguous Fourier projections, but does not by itself provide an extensive approximation-cost lower bound there.

A rational seven-site projection gives a separate exact reversal with margin greater than `13/5`. A rational conditional-Gram fixture has distance greater than `10^-6` in total variation from every rank-three projection law. These strengthen the arithmetic and robustness checks, not the claimed target coverage.

The reviewed rank-one theorem and reviewed S8 four-cycle theorem are supplied baselines. Neither is re-proved or counted as a new result. No bridge is re-proved. No claim of `H''>0` or of a counterexample to S-sine concavity is made.

### 0.1 The original goal and the exact missing sign

On `T=R/Z`, let `E_rho` be an interval of measure `0<rho<1`. The stationary DPP has symbol

\[
 f_a(\theta)=a+c1_{E_\rho}(\theta),\qquad 0\le a\le1-c.
\]

Its true `n`-site kernel is `K_n(a)=aI_n+cQ_n`, where

\[
 (Q_n)_{ij}=\int_{E_\rho}e^{2\pi i(i-j)\theta}\,d\theta.
\]

Let `p_(n,a)(T)` denote each complete atom, and let

\[
 H_n(a)=-\sum_{T\subset[n]}p_{n,a}(T)\log p_{n,a}(T),\qquad
 h_\rho(a,c)=\lim_{n\to\infty}H_n(a)/n.
\]

The goal, still unresolved here for general `37/40<c<1`, is

\[
 h_\rho((1-t)a_0+ta_1,c)\ge(1-t)h_\rho(a_0,c)+t h_\rho(a_1,c)
\]

for all legal shifts and `0<=t<=1`. The true `Q_n` is a contraction, not in general a projection.
For a genuine rank-`k` projection input `X` and the channel below, put `Ppost(a)=H(X|Y)`. The missing projection inequality is

\[
 Ppost''(a)\ge-\frac{k}{(a+c)(1-a-c)}-\frac{n-k}{a(1-a)}
 \qquad(0<a<1-c).\tag{P2}
\]

The elementary entropy decomposition makes this equivalent to `H_P''<=0`. Our new results instead concern differences between two such full entropies and the feasibility of proposed paths between their input laws. They do not settle this missing absolute sign.

## 1. Definitions and the proposed extension being tested

All logarithms are natural. Every finite DPP kernel here is Hermitian with `0<=K<=I`. For an `n x k` isometry `U`, let `P=UU*` and let

\[
 \mu_P(S)=|\det U_S|^2,\qquad |S|=k.
\]

The other input atoms are zero. The full output of the channel is

\[
 \Pr(Y_i=1\mid X_i)=a+cX_i,
 \qquad 0<c<1,\quad 0\le a\le 1-c.
\]

Write `H_P(a,c)` for its **complete configuration** Shannon entropy. No count entropy or spectral entropy replaces this object.

For a transposition `A={i,j}`, denote by `S_A` the coordinate permutation and by

\[
 \mathcal T_{A,t}\mu=(1-t)\mu+t(S_A)_*\mu
 \tag{1.1}
\]

the affine operation on input laws. Define a physical unitary, equal to the identity off `A`, by its block

\[
 R_A(t)=
 \begin{pmatrix}\sqrt{1-t}&i\sqrt t\\ i\sqrt t&\sqrt{1-t}\end{pmatrix}.
 \tag{1.2}
\]

Here `i` in (1.2) is the imaginary unit. The two endpoints of (1.1) have coordinate-permuted laws and hence equal full output entropy.

The reviewed S8 comparison only proves its curvature orientation for its stated real rank-two/four-cycle hypotheses. Two stronger possible continuations are investigated here:

* **Affine-closure continuation:** after a first compatible chord, realize further affine permutation chords by projections, possibly by changing the common frame.
* **Physical-rotation continuation:** use (1.2) on the actual complex intermediate projection, retaining a nonnegative curvature gain, or replacing the ideal affine step with at most an `o(n)` curvature payment.

The results below disprove those continuations in the explicit scopes stated. They do not disprove every more restrictive local extension or every possible path.

### Lemma 1.1: the first quadrature chord is compatible in every rank

If `U` is real, then

\[
 \mu_{R_A(t)U}=\mathcal T_{A,t}\mu_U.
 \tag{1.3}
\]

**Proof.** A minor containing neither distinguished row is unchanged. A minor containing both is multiplied by `det R_A(t)=1`. A minor containing exactly one row becomes `sqrt(1-t) d_0+i sqrt(t) d_1`, with both original ordered minors real. Its squared modulus is `(1-t)d_0^2+t d_1^2`. Cauchy--Binet gives normalization, and (1.2) preserves the column Gram matrix. This proves the identity for every complete atom. Zero minors cause no problem. ∎

This algebraic identity is not a new curvature bound. It is used to identify a compatible **first** step before proving the obstruction to a second one.

## 2. A necessary rank-two Gram constraint

Let a probability law on the pairs of a finite set `L` be a rank-two projection DPP. Write its pair probabilities as `p_ij` and its positive one-site probabilities as

\[
 h_i=\sum_{j\ne i}p_{ij}>0.
\]

Define a real symmetric matrix

\[
 \mathcal G_{ii}=1,
 \qquad
 \mathcal G_{ij}=1-\frac{2p_{ij}}{h_i h_j}\quad(i\ne j).
 \tag{2.1}
\]

### Lemma 2.1: complex rank-two representability forces rank at most three

For every complex Hermitian rank-two projection law, `G` in (2.1) is positive semidefinite and

\[
 \operatorname{rank}\mathcal G\le3.
 \tag{2.2}
\]

**Proof.** Let the corresponding frame row be `u_i=(alpha_i,beta_i)`, so `h_i=|alpha_i|^2+|beta_i|^2`. Set

\[
 v_i=\frac1{h_i}
 \left(2\operatorname{Re}(\overline{\alpha_i}\beta_i),
       2\operatorname{Im}(\overline{\alpha_i}\beta_i),
       |\alpha_i|^2-|\beta_i|^2\right)\in\mathbb R^3.
\]

Direct expansion gives `||v_i||=1` and

\[
 |\det(u_i,u_j)|^2=\frac{h_i h_j}{2}(1-v_i\cdot v_j).
\]

Therefore `G_ij=v_i dot v_j`. It is a Gram matrix of vectors in `R^3`, proving (2.2). This necessary condition permits arbitrary complex frames and arbitrary column changes; it is not merely a real-frame constraint. ∎

### Lemma 2.2: conditioning an included set preserves the projection class

If `P=UU*` has rank `k`, `|C|=r`, and `det P_C>0`, then the conditional law on the remaining sites, given `C subset X`, is a rank-`k-r` projection DPP.

**Proof.** The rows `U_C` have rank `r`. A unitary change of column frame gives `U_C=(A,0)` with `A` invertible. The last `k-r` columns vanish on `C` and restrict to an isometry `V` on `C^c`. For every `T subset C^c` of size `k-r`, block expansion gives

\[
 |\det U_{C\cup T}|^2=|\det A|^2|\det V_T|^2.
\]

Summing by Cauchy--Binet proves both the conditioning probability `det P_C=|det A|^2` and the claimed conditional law. The corresponding kernel is the usual exact Schur complement

\[
 P_{C^c,C^c}-P_{C^c,C}(P_C)^{-1}P_{C,C^c}.
\]

Only the column frame changes in this proof. No physical-coordinate entropy invariance is asserted. ∎

## 3. Rank inflation under two independent reflection averages

Suppose a real rank-two frame has rows indexed by reflection pairs, possibly with some fixed sites. Its normalized vectors from Lemma 2.1 can be written

\[
 v_i=(b_i,0,d_i),\qquad b_{-i}=-b_i,
 \quad d_{-i}=d_i,
 \quad h_{-i}=h_i>0.
 \tag{3.1}
\]

Thus the original Gram matrix is

\[
 \mathcal G=bb^T+dd^T.
\]

Choose disjoint reflection pairs `A={p,-p}` and `B={q,-q}`. Let `b_A,b_B` be the restrictions of `b` to those pairs, and put `b_0=b-b_A-b_B`.

### Theorem 3.1: exact conditional rank-four obstruction

Assume

\[
 d\ne0,\qquad b_A\ne0,\qquad b_B\ne0,\qquad b_0\ne0.
 \tag{3.2}
\]

For every `0<t<1` and `0<u<1`, the pair law

\[
 \nu=\mathcal T_{B,u}\mathcal T_{A,t}\mu
\]

is not a complex rank-two projection DPP.

**Proof.** The one-site probabilities stay `h_i`, since each averaged transposition interchanges equal marginals. Formula (2.1) is therefore affine in the pair probabilities during both operations. Swapping a reflection pair preserves `d` and reverses the sign of the corresponding part of `b`.

Let independent signs `epsilon_A,epsilon_B` equal `-1` with probabilities `t,u`, respectively. The new Gram matrix is

\[
 \begin{aligned}
 \mathcal G_\nu
 &=dd^T+\mathbb E\big[(b_0+\epsilon_A b_A+\epsilon_B b_B)
                (b_0+\epsilon_A b_A+\epsilon_B b_B)^T\big]\\
 &=dd^T+\bar b\bar b^T
    +4t(1-t)b_A b_A^T+4u(1-u)b_B b_B^T,\\
 \bar b&=b_0+(1-2t)b_A+(1-2u)b_B.
 \end{aligned}
 \tag{3.3}
\]

The three odd vectors `b_0,b_A,b_B` are nonzero with disjoint supports, hence linearly independent. The even nonzero vector `d` is orthogonal to their span. Since both variance coefficients in (3.3) are positive, its rank is exactly four. Lemma 2.1 gives a contradiction. ∎

There is also an explicit certificate. If `d_p != 0` and `r` is a third positive index with `b_r != 0`, then on the four sites `(p,-p,q,r)`,

\[
 \boxed{
 \det(\mathcal G_\nu)_{\{p,-p,q,r\}}
 =64t(1-t)u(1-u)d_p^2 b_p^2 b_q^2 b_r^2>0.
 }
 \tag{3.4}
\]

To verify (3.4), factor (3.3) into the four columns `d,bar b,2 sqrt(t(1-t)) b_A,2 sqrt(u(1-u)) b_B`. Subtract the `b_A,b_B` components from `bar b` inside the determinant. The resulting four-column determinant has absolute value `2|d_p b_p b_q b_r|` before the two variance factors. Squaring gives (3.4).

At `t` or `u` equal to `0` or `1`, this rank-four argument no longer applies. A single real-frame chord followed by a permutation is indeed compatible. The strict interior conditions are essential.

## 4. Application to genuine growing-rank contiguous Fourier projections

Use signed site labels

\[
 I_n=\{-(n-1)/2,\ldots,(n-1)/2\},\qquad n\text{ odd}.
\]

Let `P_{n,k}` be the projection onto the consecutive Fourier modes `0,...,k-1`. A diagonal site phase moves the modes to the centered frequencies `ell-(k-1)/2`. Its kernel is real. An explicit real isometry uses the constant mode and paired sine/cosine modes when `k` is odd, and the paired half-integer sine/cosine modes when `k` is even. The columns are orthonormal by the finite geometric sum. Diagonal site phases preserve all principal minors and therefore all complete configuration atoms.

For distinct sites the Vandermonde formula gives

\[
 \mu_{n,k}(S)=\frac1{n^k}
   \prod_{i<j\in S}|e^{2\pi i i/n}-e^{2\pi i j/n}|^2>0,
 \qquad |S|=k.
 \tag{4.1}
\]

### Theorem 4.1: a first compatible chord and an impossible second chord

Let `n` be odd and `3 <= k <= n-4`. Put `r=floor(k/2)`, `A={r,-r}`, and `B={r+1,-r-1}`. For every `0<t,u<1`,

\[
 \mathcal T_{A,t}\mu_{n,k}
 \quad\text{is a projection DPP law, but}\quad
 \boxed{\mathcal T_{B,u}\mathcal T_{A,t}\mu_{n,k}
        \text{ is not a Hermitian-contraction DPP law}.}
 \tag{4.2}
\]

Consequently no alternative common frame, Schur-complement realization, or complex projection can realize that second affine endpoint law.

**Proof.** Choose the reflection-invariant included set of size `k-2` as follows:

* if `k=2r+1`, take `C={-(r-1),...,r-1}`;
* if `k=2r`, take `C={±1,...,±(r-1)}`.

At least three nonzero reflection pairs remain outside `C`. By (4.1), the event `C subset X` has positive probability. Put `theta_j=pi*j/n` and

\[
 w_j=\prod_{v\in C}\sin^2\!\frac{\pi(j-v)}n>0
 \qquad(j\notin C).
\]

The conditional pair law is proportional to

\[
 w_iw_j\sin^2(\theta_i-\theta_j).
 \tag{4.3}
\]

This follows by separating the Vandermonde factors involving two free sites, those involving `C`, and the constant factors internal to `C`.

Because `w_{-j}=w_j`, put

\[
 A_0^2=\sum_{j\notin C}w_j\cos^2\theta_j,
 \qquad B_0^2=\sum_{j\notin C}w_j\sin^2\theta_j.
\]

Both numbers are positive and the weighted sine/cosine cross sum is zero. The explicit **common conditional frame** is therefore

\[
 v_j=\sqrt{w_j}
       \left(\frac{\cos\theta_j}{A_0},
             \frac{\sin\theta_j}{B_0}\right).
 \tag{4.4}
\]

It is an isometry and its squared pair minors have exactly the probabilities (4.3), after normalization. Write `v_j=(x_j,y_j)` and set

\[
 h_j=x_j^2+y_j^2,
 \quad b_j=\frac{2x_jy_j}{h_j},
 \quad d_j=\frac{x_j^2-y_j^2}{h_j}.
 \tag{4.5}
\]

They have the reflection properties (3.1). Every remaining nonzero pair has `b_j != 0`, because `|theta_j|<pi/2` and `theta_j != 0`.

The vector `d` is not zero. If site zero remains, `d_0=1`. Otherwise, on positive indices `d_j=0` is equivalent to `tan^2 theta_j=B_0^2/A_0^2`, which holds for at most one of the at least three distinct positive indices. The positive indices `r,r+1,r+2` all remain. Thus the stated pairs `A={r,-r}`, `B={r+1,-r-1}` have nonzero odd parts, and the odd part on the remaining pair `±(r+2)` is nonzero as well. This verifies (3.2) for these explicitly specified pairs. If a displayed four-by-four minor is wanted, at most one of `d_r,d_{r+1}` is zero, so interchange the names of the two averaged pairs if necessary and apply (3.4).

The first global chord is realized by Lemma 1.1 applied to the real centered Fourier frame. Both transpositions fix `C`. Therefore averaging commutes exactly with conditioning on `C subset X`; the conditioning probability is unchanged. The conditional law of the twice-averaged full law is precisely the twice-averaged pair law in Theorem 3.1. Its Gram matrix has rank four, or explicitly has the positive minor (3.4).

If the twice-averaged full law were a rank-`k` projection DPP, Lemma 2.2 would make that conditional law a rank-two projection DPP. This contradicts Lemma 2.1.

Finally, the twice-averaged law has exactly `k` particles. If it were `DPP(K)` for a Hermitian contraction, then

\[
 0=\operatorname{Var}|X|=\operatorname{Tr}(K-K^2).
\]

Every eigenvalue lies in `[0,1]`, so all are zero or one. Thus `K` would be a rank-`k` projection, already excluded. ∎

### Fixed-density quantifiers

For any fixed `0<rho<1`, choose odd `n -> infinity` and, for example, `k_n=floor(n*rho+1/2)`. For all sufficiently large `n`, `3<=k_n<=n-4`, so Theorem 4.1 applies at the actual fixed density. The theorem does **not** assert that every pair of transpositions fails, or that no more carefully chosen path can work.

The conditioning event may become rare, and (3.4) is not claimed to be bounded below uniformly in this sequence. Thus exact incompatibility alone does not rule out a paid `o(n)` approximation on the true Fourier family.

### The incompatibility also persists for the full noisy law

For a contraction `Q`, channeling `DPP(Q)` gives `DPP(aI+cQ)`: for every inclusion set `A`, expand

\[
 \mathbb E\prod_{i\in A}(a+cX_i)
 =\sum_{B\subset A}a^{|A|-|B|}c^{|B|}\det Q_B
 =\det(aI_A+cQ_A).
\]

The one-bit channel matrix has determinant `c`, so its `n`-fold tensor product is invertible whenever `c>0`, including at `a=0` and `a=1-c`. Hence the output law of the impossible second affine input law cannot equal `DPP(aI+cQ)` for any contraction `Q`. Otherwise inverting the channel would contradict (4.2).

## 5. Genuine Fourier curvature reversal for an actual physical continuation

The preceding theorem rules out an ideal affine continuation. The following result checks what happens if one instead continues with the actual physical unitary.

Label seven sites by `(0,1,-1,2,-2,3,-3)` and set

\[
 (P_0)_{ij}=\frac{1+2\cos(2\pi(i-j)/7)}7.
 \tag{5.1}
\]

This is the rank-three projection onto centered Fourier modes `-1,0,1`, diagonally phase-gauge equivalent to consecutive modes `0,1,2`. Let

\[
 P_1=R_{\{1,-1\}}(1/2)P_0R_{\{1,-1\}}(1/2)^*,
\]
\[
 P_2=R_{\{2,-2\}}(1/2)P_1R_{\{2,-2\}}(1/2)^*.
 \tag{5.2}
\]

Write `H_j(a,c)=H(DPP(aI+cP_j))`. Let `tilde H_2` be the full output entropy for the input law `(mu_{P_1}+(S_{2,-2})_*mu_{P_1})/2`.

### Theorem 5.1: certified reversal and the exact unpaid correction

At

\[
 c_*={19\over20},\qquad a_*={1\over200},
 \tag{5.3}
\]

the following outward rational decimal enclosures hold:

\[
 H_1''-H_0''\in
 [2.234011527651,\ 2.234011527652],
 \tag{5.4}
\]
\[
 \boxed{H_2''-H_1''\in
 [-0.888244305490,\ -0.888244305489]<-4/5,}
 \tag{5.5}
\]
\[
 \widetilde H_2''-H_1''\in
 [0.860920037700,\ 0.860920037701]>4/5,
 \tag{5.6}
\]
\[
 \boxed{H_2''-\widetilde H_2''\in
 [-1.749164343190,\ -1.749164343189]<-17/10.}
 \tag{5.7}
\]

Primes mean derivatives with respect to `a`, with the projection and `c` fixed. Both steps have genuine projection kernels throughout. Every diagonal entry remains `3/7`; during the second step all frame rows outside `{2,-2}` are fixed. The covariance graph also remains connected: every nonzero site has a nonzero correlation with site zero, and rotating its reflection pair multiplies that correlation by a unit-modulus scalar. Nevertheless its outside frame is generally complex, and the full law is not the affine surrogate.

The individual Hessians are all negative:

\[
\begin{array}{c|c}
 P_0&[-666.924885557585,-666.924885557584]\\
 P_1&[-664.690874029934,-664.690874029933]\\
 P_2&[-665.579118335423,-665.579118335422].
\end{array}
\tag{5.8}
\]

Thus this is a comparison/composition obstruction, **not** a counterexample to (P2) or to sine entropy-rate concavity.

**Proof and arithmetic certificate.** Projection preservation follows from the unitaries (1.2). The diagonal invariance follows because the two initial entries are equal and the within-pair off-diagonal entry is real. The first rotation does not change the entries of the second principal two-site block, so the same reasoning applies there. For connectedness, `1+2 cos(2*pi*j/7)` never vanishes for nonzero sites `j`: its vanishing would require a nontrivial cube root of unity to be a seventh root. Each reflection pair has equal initial correlation with site zero; its quadrature rotation multiplies that correlation by `sqrt(1-t)+i sqrt(t)`, which never vanishes. Formula (1.3) proves the first law is its affine chord. Theorem 4.1 applies here with `n=7,k=3,r=1,C={0}`, exactly the two pairs in (5.2), and excludes the ideal second law from the projection class.

All numerical enclosures in (5.4)--(5.8) are certified by the finite exact procedure proved in `certificates.md`, implemented in `scripts/exact_fourier7.py`. The data are not floating-point diagnostics. In brief, `x=cos(2*pi/7)` is the unique root in `(1/2,1)` of

\[
 8x^3+4x^2-4x-1=0.
\]

All input atoms and their complete output jets are calculated exactly in the three-dimensional rational algebra with basis `1,x,x^2`. The root is bracketed by 140 exact rational bisections. The full curvature is evaluated as

\[
 H''=-\sum_{T\subset[7]}q_T''\log q_T
       -\sum_{T\subset[7]}\frac{(q_T')^2}{q_T}.
 \tag{5.9}
\]

Every one of the 128 complete output atoms is included. Rational atanh-series logarithm enclosures with 24 terms, a proved tail, and outward dyadic rounding certify (5.4)--(5.8). Projection identities, normalization, both derivative normalizations, first-chord equality and cycle closure are exact algebraic checks. The source, all atom coefficients, execution receipts, and an optimized-mode higher-precision replay are included. `certificates.md` gives the full derivation and error rules, making this an exhaustively reproducible finite proof. ∎

### A closed physical cycle clarifies the endpoint law

Apply the third rotation to `{3,-3}` to obtain `P_3`. Reflection `S:i -> -i` commutes with `P_0`. The unitary `cos(theta)I+i sin(theta)S` therefore also commutes with `P_0`. At `theta=pi/4`, its non-fixed-site blocks are exactly the three rotations. At site zero it is the scalar `exp(i*pi/4)`. Consequently the product of the three pair rotations differs from this commuting unitary only by a diagonal phase at zero. Therefore `P_3` has exactly the same complete atom law as `P_0`, for every legal channel parameter. This is also checked coefficient-by-coefficient in the certificate.

The comparison orientation cannot be nonnegative along the whole nonconstant cycle. No assertion of invariance under general physical unitary conjugation is used: only a commuting unitary and a diagonal phase establish the endpoint identity.

### Corollary 5.2: an extensive signed payment at fixed density

Take `m` independent coordinate blocks, each containing the seven-site construction. The resulting projection has `n=7m`, rank `3m`, and fixed density `3/7`. Apply each block's first rotation, then each block's second rotation. Let the ideal second law be the **product of the blockwise affine laws**, not a mixture of two whole-system laws.

Independence and additivity of full configuration entropy give, at (5.3),

\[
 H_{2,m}''-H_{1,m}''<-\frac45m=-\frac4{35}n,
 \tag{5.10}
\]
\[
 H_{2,m}''-\widetilde H_{2,m}''
 <-\frac{17}{10}m=-\frac{17}{70}n.
 \tag{5.11}
\]

Thus a universal `o(n)` lower error budget for replacing the ideal affine continuation by the actual quadrature continuation is false, even at fixed high contrast and fixed positive density. For any compact legal `J` containing `1/200`, these pointwise violations also rule out such a uniform-in-`a` budget on `J`.

These block sums are **not** the contiguous projections `P_{7m,3m}`. Nor does the corollary prohibit cancellation with other steps of a specially chosen path. It proves that the negative payment cannot universally be discarded or declared sublinear.

## 6. Rational projection cross-check and robust compatibility obstruction

### 6.1 A purely rational rank-three curvature reversal

Let

\[
 W=\begin{pmatrix}
 1&85&0\\1&51&68\\1&51&-68\\
 1&0&85\\1&0&-85\\1&-75&40\\1&-75&-40
 \end{pmatrix},\qquad P=W(W^TW)^{-1}W^T.
 \tag{6.1}
\]

Its Gram matrix is

\[
 W^TW=\begin{pmatrix}7&37&0\\37&23677&0\\0&0&26898\end{pmatrix},
 \qquad\det(W^TW)=4421224260>0.
\]

Use the reflection pairs of rows `(1,2),(3,4),(5,6)` in **zero-based indexing**. Apply the same quadrature operations as above. At (5.3), exact rational arithmetic gives

\[
 H_1''-H_0''\in[3.773157139144,3.773157139145],
\]
\[
 H_2''-H_1''\in[-2.632780651606,-2.632780651605]<-13/5.
 \tag{6.2}
\]

The corresponding actual-minus-affine second-step curvature is in

\[
 [-3.175610614255,-3.175610614254].
 \tag{6.3}
\]

All individual Hessians remain negative. The full physical second-law/input-affine-law TV discrepancy is exactly

\[
 {25189240\over221061213}>0.
\]

These claims are established by `scripts/exact_certificate.py`, which independently reconstructs all 128 complete output jets for each of four physical states by both channel products and inclusion determinants followed by Möbius inversion. See `certificates.md` for the proof algorithm. This rational fixture removes the cubic-field arithmetic from an independent check of the phenomenon. It is not an additional claimed Fourier family.

### 6.2 A rank-four Gram certificate readable without numerical computation

Take sites labelled `0,±1,±2,±3` and the rational moment-curve frame

\[
 W_j=(1,j,j^2),\qquad P=W(W^TW)^{-1}W^T.
 \tag{6.4}
\]

The columns are independent and `P` is a rank-three projection. Its Gram matrix is

\[
 \begin{pmatrix}7&0&28\\0&28&0\\28&0&196\end{pmatrix}.
\]

Conditioning on occupancy of site zero has probability `1/3`. The conditional rank-two frame on the six remaining sites can be taken as

\[
 v_j=\left(j/\sqrt{28},\ j^2/14\right).
\]

For positive `r=1,2,3`, it gives

\[
 h_r={r^2(7+r^2)\over196},\qquad
 d_r={7-r^2\over7+r^2},\qquad
 b_r={2\sqrt7\,r\over7+r^2}.
 \tag{6.5}
\]

Average the pairs `±1` and `±2` independently at `t=u=1/2`. On conditional sites `(1,-1,2,3)`, (3.4) becomes

\[
 \det\mathcal G
 =4(3/4)^2(7/16)(112/121)(63/64)
 =\boxed{27783/30976}>0.
 \tag{6.6}
\]

Thus the twice-averaged full law is not a projection law, with a simple exact witness.

### Proposition 6.3: explicit robust TV separation

The twice-averaged law in (6.4)--(6.6) is at TV distance **greater than `10^-6`** from every rank-three projection law on these seven sites.

**Proof.** Suppose a projection law is within `epsilon<=10^-6`. Conditioning on the event of mass `1/3` above changes the TV distance by at most a factor six: for every subevent, the quotient formula gives conditional probability difference at most `2 epsilon/(1/3)`. Put `delta<=6 epsilon` for the conditional TV distance.

The target conditional marginal minimum is `m=2/49`. Each pair probability and each marginal changes by at most `delta`; since `delta<m/2`, both Gram matrices are defined. For a projection pair law, `p'_ij<=h'_i h'_j`. Hence

\[
 |\mathcal G_{ij}-\mathcal G'_{ij}|
 \le {2\delta\over m^2}+{4\delta\over m}
       +{2\delta^2\over m^2}
 \le \left({2\over m^2}+{5\over m}\right)\delta
 =1323\delta.
\]

Both matrices are Gram matrices with entries of absolute value at most one. By telescoping the four columns and Hadamard's determinant inequality, the change of a four-by-four determinant is at most 64 times the maximum entry change. Thus it is at most

\[
 64\cdot1323\cdot6\cdot10^{-6}=0.508032
 <27783/30976.
\]

But the candidate projection's conditional Gram determinant is zero by Lemma 2.1, whereas (6.6) is the target determinant. Contradiction. ∎

This finite robust separation does not assert a uniform separation for the growing Fourier conditioning event. For the noisy laws it implies a positive, explicitly smaller separation: the induced `l^1` norm of the inverse one-bit channel is at most `(2-c)/c`, so any candidate of the form `DPP(aI+cQ)` with `Q` a rank-three projection is at output TV distance greater than

\[
 10^{-6}\left({c\over2-c}\right)^7.
\]

This is only a finite-law TV statement, not an entropy-curvature inference.

## 7. The initially frozen common-outside-frame extension: precise surviving question

Before the exploratory search, the following narrower extension was fixed. For real angles `alpha,gamma`, let `f,g` be the orthonormal real four-site vectors

\[
 f={1\over\sqrt2}(\cos\alpha,\cos\alpha,\sin\alpha,\sin\alpha),
\quad
 g={1\over\sqrt2}(\cos\gamma,-\cos\gamma,\sin\gamma,-\sin\gamma).
\]

Let `B` be any real `N x r` isometry with `1<=r<N`, and let `v` be a unit vector orthogonal to its columns. For `0<beta<1`, use the explicit common frame with columns

\[
 U=\big((f,0),\ (\sqrt{1-\beta}\,g,\sqrt\beta\,v),\ (0,B)\big).
 \tag{7.1}
\]

It has rank `r+2`, and can be connected across the active sites and the outside sites. Apply (1.2) to the first active pair.

The proposed inequality `D_t''>=0` for this entire family remains **unproved and undisproved** here. The obstructions in Sections 4--6 do not silently refute this more restrictive family.

There is an exact decomposition explaining the missing payment. Expanding the wedge of the displayed columns gives the input law

\[
 (1-\beta)\,\mu_{f,g}\otimes\mu_B
 +\beta\,\mu_f\otimes\mu_{[B,v]}.
 \tag{7.2}
\]

The two terms have respectively two and one active occupied sites, so their amplitudes have disjoint supports and no interference term is missing. The first active rank-one law `mu_f` stays constant under the quadrature operation, because its first two entries have equal magnitude. Let `L_s,L_f` be the corresponding four-site channel laws, and `Q_B,Q_+` the outside laws for `B` and `[B,v]`. The full output is exactly

\[
 q_s(A,R)=(1-\beta)L_s(A)Q_B(R)
                 +\beta L_f(A)Q_+(R).
 \tag{7.3}
\]

If `d(A)=partial_s L_s(A)`, the interpolation Fisher information is

\[
 I_s(a)=(1-\beta)^2\sum_{A,R}
 \frac{d(A)^2Q_B(R)^2}
 {(1-\beta)L_s(A)Q_B(R)+\beta L_f(A)Q_+(R)}.
 \tag{7.4}
\]

All four displayed laws move with `a`. Freezing `Q_B`, `Q_+`, or their likelihood ratio would not prove the proposed sign. The rank-two S8 product-Gaussian calculation does not supply that missing bound for arbitrary `r`.

The finite exact test in `scripts/exact_common_frame.py` uses a connected rank-three six-site instance of (7.1), with `beta=9/25`, and proves positive differences at three specified offsets. The bounded floating search tested 6000 instances and found no negative example. **Neither observation is a theorem for (7.1), nor is either counted as completion of this round.** The analytical Fourier incompatibility theorem and the exact comparison obstructions above are the substantive completed results.

## 8. Boundary, quantifier, and entropy-object audit

* All projection claims arise from one normalized frame or an explicit unitary transform. No unconstrained pair weights are substituted for projection minors.
* The rank-four obstruction allows arbitrary complex alternative projections. It is not fixed by rephasing rows or changing the column frame.
* The all-rank Fourier theorem requires odd `n`, `3<=k<=n-4`, and the specified reflection-pair construction. It is an existence obstruction to general composability, not a classification of every possible pair or path.
* Strict mixing parameters `0<t,u<1` are needed for rank four. The boundary mixing parameters reduce to one chord/permutations and are not excluded.
* The Fourier obstruction is independent of `a,c`; injectivity transfers it to the complete noisy law for every `c>0` and every legal closed-interval `a`.
* Curvature certificates are at the fixed strict interior point (5.3). They do not assert endpoint second derivatives. At this point every output atom is strictly positive even if some input minors vanish.
* Finite entropy and the cycle identity extend to the closed legal interval by continuity of each atom and of `-p log p` at zero. No derivative of an entropy rate is used.
* All computations preserve each complete output word. All probability accelerations and Fisher terms in (5.9) are present. No output or posterior weights are frozen.
* The tensorized comparison defect is extensive with explicit constants at fixed density, but its kernels are block sums. The growing contiguous-Fourier rank obstruction supplies no unproved uniform entropy/Hessian estimate.
* No value error is differentiated. The comparison error in (5.7) is computed directly from exact complete atom jets.
* The original high-contrast S-sine target, general projection (P2), and the asymptotic upper-curvature bound for growing contiguous Fourier projections remain open in this packet.

## 9. Precise next obligation

A successful continuation must first choose a local class that survives its own operations. It must either avoid the rank-four conditional-Gram obstruction or abandon the exact affine law and retain the actual physical continuation's non-affine response. In the latter case it must prove a **signed curvature/Jensen payment for the particular growing contiguous Fourier path**, not a universal nonnegative or sublinear correction contradicted by (5.10)--(5.11).

For the initially frozen family (7.1), the concrete unresolved analytic subproblem is a bound on the second `a` derivative of (7.4) with the two nested outside DPP laws and their moving likelihood ratio included. Even a proof there must still demonstrate entry from the Fourier family, preservation under later steps, orientation toward a solved reference, and a paid fixed-density cumulative error. None of those obligations is replaced by the reviewed bridge.
