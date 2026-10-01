**PROVED.**

Let \(m=|S|\), \(W=\Gamma\times S\), and \(x_a=(e,a)\). All configuration and noise actions below are the coordinate-permutation actions induced by
\[
g(\gamma,a)=(g\gamma,a).
\]

We prove the stronger process assertion: one iid field of unit-rate Poisson random measures \(N_x(ds\,du)\) produces a temporally increasing, product-topology càdlàg process satisfying
\[
X_s\sim\mathbf P^{(1-e^{-s})Q},
\qquad
X_\infty=\bigcup_{n\ge1}X_n\sim\mathbf P^Q.
\]
Every coordinate has at most one birth. The terminal map will be defined on every input, Borel, and exactly equivariant. There is no assertion of finitary coding or monotonicity in the noise.

## 1. Determinantal measures and shorting

### Determinantal measures from their defining probabilities

For a positive contraction \(K<I\) on a finite set \(F\), put \(L=K(I-K)^{-1}\). The nonnegative weights
\[
\mu_K(\eta)=\frac{\det L[\eta]}{\det(I+L)}
\]
sum to one by principal-minor expansion. For a diagonal matrix \(Z=\operatorname{diag}(z_x)\),
\[
\sum_{\eta\subseteq F}\mu_K(\eta)\prod_{x\in\eta}z_x
=\frac{\det(I+LZ)}{\det(I+L)}
=\det(I-K+KZ)
=\det(I+K(Z-I)).
\]
Comparing coefficients of \(\prod_{x\in B}(z_x-1)\) gives
\(\mathbf P[B\subseteq\eta]=\det K[B]\).

For general \(0\le K\le I\), let \(rK\uparrow K\). The exact probabilities converge by
\[
\mu_K(\eta)
=\sum_{B\subseteq F\setminus\eta}(-1)^{|B|}
  \det K[\eta\cup B].
\tag{1}
\]
They remain nonnegative and normalized. Formula (1) also proves uniqueness.

On a countable set, these finite laws are consistent. Existence follows, for example, by enumerating the coordinates and successively sampling each bit according to the conditional probability prescribed by the consistent finite laws, assigning arbitrary transitions on zero-probability prefixes. This auxiliary construction need not be equivariant. Uniqueness follows from the finite distributions.

Consequently \(\mathbf P^Q\) is invariant when \(Q\) is equivariant. Independently retaining each occupied point with probability \(p\) gives \(\mathbf P^{pQ}\), since its inclusion probabilities are
\[
p^{|B|}\det Q[B]=\det(pQ[B]).
\tag{2}
\]

### Shorting

For \(0\le A\le I\), write
\[
M_\eta^A=\overline{A^{1/2}\ell^2(\eta)},\qquad
\Pi_\eta^A=P_{M_\eta^A},
\]
\[
\mathsf S_\eta(A)=A^{1/2}(I-\Pi_\eta^A)A^{1/2},
\qquad
b_A(x,\eta)=\langle\mathsf S_\eta(A)\delta_x,\delta_x\rangle.
\]
The Hilbert-space distance formula gives
\[
\langle\mathsf S_\eta(A)f,f\rangle
=\inf_{g\in\ell^2(\eta)}
   \langle A(f+g),f+g\rangle.
\tag{3}
\]
In particular,
\[
0\le\mathsf S_\eta(A)\le A\le I,
\qquad b_A(x,\eta)=0\quad(x\in\eta).
\]
Enlarging \(\eta\) decreases the shorting, while increasing \(A\) increases its shorting over a fixed \(\eta\). If \(A\) is equivariant, then
\[
b_A(gx,g\eta)=b_A(x,\eta).
\tag{4}
\]

The infimum in (3) can be restricted to finite-support vectors having rational real and imaginary parts, subject to their support lying in \(\eta\). This proves Borel measurability in \(\eta\), and joint Borel measurability in \((s,\eta)\) for a norm-continuous family \(A_s\).

The operator fields needed below are also measurable. With \(D_\eta\) the coordinate projection and \(B_\eta=A^{1/2}D_\eta A^{1/2}\),
\[
\Pi_\eta^A
=\mathrm{s}\!-\!\lim_{n\to\infty}
 B_\eta(B_\eta+n^{-1}I)^{-1}.
\tag{5}
\]
Indeed, \(\overline{\operatorname{ran}B_\eta}=M_\eta^A\); the limit is zero on its kernel and the identity on its range closure. The approximants are strongly Borel, and covariance is preserved.

For a bounded \(T\), its polar partial isometry is obtained by extending the isometry \(|T|f\mapsto Tf\), and setting it zero on \(\ker|T|\). It satisfies
\[
V=\mathrm{s}\!-\!\lim_{n\to\infty}
T(T^*T+n^{-1}I)^{-1/2}.
\tag{6}
\]
Thus the polar parts below are measurable and covariant.

The one-sided continuity needed later is particularly important. If \(A_j\downarrow A\) strongly, with a common bound, then for fixed \(\eta,f\),
\[
\begin{aligned}
\inf_j\langle\mathsf S_\eta(A_j)f,f\rangle
&=\inf_j\inf_{g\in\ell^2(\eta)}
       \langle A_j(f+g),f+g\rangle\\
&=\inf_{g\in\ell^2(\eta)}\inf_j
       \langle A_j(f+g),f+g\rangle\\
&=\langle\mathsf S_\eta(A)f,f\rangle.
\end{aligned}
\tag{7}
\]
Hence \(\mathsf S_\eta(A_j)\downarrow\mathsf S_\eta(A)\) strongly. Strong convergence follows from
\[
\|Df\|^2\le \|D\|\langle Df,f\rangle
\]
for the positive differences \(D\). Equation (7) concerns fixed \(\eta\); it is not used to justify a moving-window limit.

The Hilbert-space foundations here are the orthogonal projection theorem and continuous functional calculus for bounded self-adjoint operators: a closed subspace has an orthogonal projection realizing distance, and continuous functions on the spectrum admit a positive, isometric, unital \(*\)-homomorphism extending polynomial evaluation. Sources are Teschl, Sections 1.3 and 3.1; the polar construction above is supplied directly. :chatgpt-content-reference{index="0"}

## 2. The summed covariant trace estimate

For uniformly bounded covariant random operator fields over an invariant probability law, define
\[
\tau(B)=\sum_{a\in S}
\mathbb E\langle B\delta_{x_a},\delta_{x_a}\rangle.
\]
This is an unnormalized finite trace. To prove cyclicity, use matrix entries
\(B_{u,v}=\langle B\delta_v,\delta_u\rangle\):
\[
\tau(BC)
=\sum_{a,b\in S}\sum_{\gamma\in\Gamma}
\mathbb E\!\left[
 B_{(e,a),(\gamma,b)}C_{(\gamma,b),(e,a)}
\right].
\tag{8}
\]
The series is absolutely integrable: row-column Cauchy–Schwarz bounds the sum before expectation by \(m\|B\|\|C\|\). Thus Fubini applies under its absolute-integrability hypothesis. :chatgpt-content-reference{index="1"}

Joint covariance and invariance under \(\gamma^{-1}\) transform a summand into
\[
\mathbb E\!\left[
 B_{(\gamma^{-1},a),(e,b)}
 C_{(e,b),(\gamma^{-1},a)}
\right].
\]
Commuting these scalar factors and reindexing gives
\[
\tau(BC)=\tau(CB).
\tag{9}
\]

Now let \((\eta,\zeta)\) be a **jointly invariant** pair. First suppose \(\eta\subseteq\zeta\). Set
\[
D=D_{\zeta\setminus\eta},
\qquad
T=(I-\Pi_\eta^A)A^{1/2}D.
\]
Since
\[
M_\zeta^A
=\overline{M_\eta^A+A^{1/2}\ell^2(\zeta\setminus\eta)},
\]
we have
\[
\overline{\operatorname{ran}T}=M_\zeta^A\ominus M_\eta^A.
\]
For the polar part \(V\) of \(T\),
\[
VV^*=P:=\Pi_\zeta^A-\Pi_\eta^A,
\qquad V^*V\le D.
\]
Consequently
\[
\tau(P)=\tau(VV^*)=\tau(V^*V)\le\tau(D),
\]
and, because \(PAP\le P\),
\[
\begin{aligned}
\sum_a\mathbb E[b_A(x_a,\eta)-b_A(x_a,\zeta)]
&=\tau(A^{1/2}PA^{1/2})\\
&=\tau(PAP)\\
&\le\sum_a\mathbb P[x_a\in\zeta\setminus\eta].
\end{aligned}
\tag{10}
\]

For arbitrary \(\eta,\zeta\), put \(\theta=\eta\cap\zeta\). Monotonicity gives
\[
|b_A(x,\eta)-b_A(x,\zeta)|
\le b_A(x,\theta)-b_A(x,\eta)
   +b_A(x,\theta)-b_A(x,\zeta).
\]
Apply (10) to the two nested pairs. Their added sets are disjoint, yielding
\[
\boxed{
\sum_{a\in S}\mathbb E
 |b_A(x_a,\eta)-b_A(x_a,\zeta)|
\le
\sum_{a\in S}\mathbb P[\eta(x_a)\ne\zeta(x_a)].
}
\tag{11}
\]

There is no per-label version. For the trivial group, two labels, and
\[
A=\frac12
\begin{pmatrix}1&1\\1&1\end{pmatrix},
\quad
\eta=\varnothing,\quad\zeta=\{2\},
\]
the first rate changes by \(1/2\), although the first label’s membership does not change. The sum of both rate changes is \(1\), agreeing with (11).

## 3. The strong Picard construction and its exact uniqueness class

Set
\[
t_s=1-e^{-s},\qquad
A_s=e^{-s}Q(I-t_sQ)^{-1}=f_s(Q),
\]
\[
f_s(q)=\frac{e^{-s}q}{1-(1-e^{-s})q}.
\tag{12}
\]
For \(q\in[0,1]\), \(0\le f_s(q)\le1\), including \(f_s(1)=1\). Therefore \(0\le A_s\le I\). The Neumann series proves norm-continuity in \(s\) on every bounded interval.

Use marks in \((0,1)\); endpoints have zero intensity. For an adapted càdlàg pure-birth process \(U\), its left-limit field \(U_{s-}\) is predictable. Explicitly, approximate it by the processes equal to \(U_{k2^{-n}}\) on
\((k2^{-n},(k+1)2^{-n}]\). Joint Borel measurability from Section 1 then makes
\[
b_{A_s}(x,U_{s-})
\]
predictable.

Define
\[
\Phi_N(U)_t(x)=
\mathbf1\left\{
\exists(s,u)\in N_x:
s\le t,\quad u\le b_{A_s}(x,U_{s-})
\right\}.
\tag{13}
\]
This is a pure-birth path, measurable and equivariant. Local finiteness is needed only at each site.

We use predictable Poisson compensation in a specified common filtration. For a predictable rectangle, conditional independence of future Poisson increments gives
\[
\mathbb E\int H\,dN=\mathbb E\int H\,d\nu,
\qquad
\nu(dx\,ds\,du)=\#_W(dx)\,ds\,du.
\tag{14}
\]
Nonnegative simple approximation extends this to predictable integrands. Initially, spatial support and the time horizon are finite. The same rectangle argument proves the martingale identity for bounded compensated integrals.

Write
\[
d_T(U,V)=\sum_a
\mathbb P\{U_\cdot(x_a)\ne V_\cdot(x_a)
          \text{ somewhere on }[0,T]\}.
\]
Suppose \(U,V\) are jointly invariant and adapted to a common filtration relative to which \(N\) is a Poisson field. Differing updated paths require some proposal to lie below just one threshold. Thus (14) and (11) give
\[
\begin{aligned}
d_T(\Phi_N(U),\Phi_N(V))
&\le\int_0^T\sum_a
 \mathbb E|b_{A_s}(x_a,U_{s-})-b_{A_s}(x_a,V_{s-})|\,ds\\
&\le\int_0^T d_s(U,V)\,ds.
\end{aligned}
\tag{15}
\]

Let \(X^{(0)}=\varnothing\) and \(X^{(k+1)}=\Phi_N(X^{(k)})\). The iterates are jointly invariant, causal measurable functions of the iid field. For
\[
D_k(T)=d_T(X^{(k+1)},X^{(k)}),
\]
we obtain
\[
D_0(T)\le m,\qquad
D_k(T)\le\int_0^T D_{k-1}(s)\,ds
\le m\frac{T^k}{k!}.
\tag{16}
\]
The first Borel–Cantelli lemma requires only summability of the event probabilities, not independence. :chatgpt-content-reference{index="2"}

Applying it here, then using invariance and countability of \(W\) and of integer horizons, gives one conull event on which every coordinate path eventually agrees exactly between successive iterates on every compact time interval. Denote the limit by \(X\). Its coordinates are càdlàg pure-birth paths. They give a càdlàg path in a product metric by controlling finitely many coordinates and then the summable metric tail.

The limit is adapted to the completed natural filtration: at every time it agrees almost surely with the coordinatewise \(\liminf\) of the adapted iterates. The total invariant null-set convention is specified below.

Applying (11) and compensation once more,
\[
d_T(\Phi_N(X^{(k)}),\Phi_N(X))
\le\int_0^T\sum_a
\mathbb P[X^{(k)}_{s-}(x_a)\ne X_{s-}(x_a)]\,ds
\longrightarrow0.
\tag{17}
\]
The integrand is bounded by \(m\), and compact-time stabilization gives convergence. Since \(\Phi_N(X^{(k)})=X^{(k+1)}\) also converges to \(X\), we conclude
\[
X=\Phi_N(X)\quad\text{almost surely}.
\tag{18}
\]

The required uniqueness statement is now precise:

> If \(U,V\) are jointly invariant, adapted, càdlàg pure-birth solutions from the empty configuration, driven by the same \(N\), and \(N\) is a Poisson field relative to their common filtration, then \(U,V\) are indistinguishable.

Indeed, (15) gives \(d_T\le\int_0^T d_s\,ds\). Iteration with \(d_s\le m\) yields \(d_T\le mT^n/n!\) for every \(n\), hence \(d_T=0\). Countability finishes the assertion. Neither process is required in advance to be naturally adapted to \(N\).

## 4. Finite-window hazards given the entire observed past

Temporarily assume \(Q\ge cI\) for some \(c>0\). Sample \(Z\sim\mathbf P^Q\), and independently sample iid \(E_x\sim\operatorname{Exp}(1)\). Define
\[
\tau_x=
\begin{cases}
E_x,&x\in Z,\\
\infty,&x\notin Z,
\end{cases}
\qquad
Y_s(x)=\mathbf1_{\{\tau_x\le s\}}.
\]
By (2),
\[
Y_s\sim\mathbf P^{t_sQ}.
\tag{19}
\]
This is an invariant weak process, not yet a factor.

Let
\[
\mathcal H_t^0=\sigma(Y_r(x):r\le t,\ x\in W),
\qquad
R_x(s)=\mathbf1_{\{x\in Z,E_x\ge s\}}.
\]
In the auxiliary latent filtration
\[
\mathcal L_t^0=\sigma(Z,Y_r:r\le t),
\]
the process
\[
Y_t(x)-\int_0^tR_x(s)\,ds
\tag{20}
\]
is a martingale. Conditional on \(\mathcal L_r^0\), an occupied but unborn site has an independent residual exponential clock. Both its expected birth increment over \((r,t]\) and its expected survival integral equal
\[
\mathbf1_{\{x\in Z,\tau_x>r\}}(1-e^{-(t-r)}).
\]
This directly proves (20). The latent filtration will not be used for the final common-noise comparison.

Choose finite \(F_n\uparrow\Gamma\), put \(W_n=F_n\times S\), and compress \(Q\) to \(Q^{[n]}\). Fix \(s>0\). The entire observed finite past consists of
\[
\eta=Y_{s-}\cap W_n
\]
and the labeled birth times \(r_y<s\), \(y\in\eta\). Given terminal set \(T\supseteq\eta\), its likelihood density is
\[
\left(\prod_{y\in\eta}e^{-r_y}\right)
 e^{-s|T\setminus\eta|}.
\tag{21}
\]
The actual birth-time factor is independent of \(T\). Thus the posterior about unborn terminal points given the full past depends only on \(\eta\).

Let \(\mu_s^{[n]}\) denote exact entire-configuration probabilities of
\(\mathbf P^{t_sQ^{[n]}}\), and let
\[
\mathcal H_{s-}^{n,0}
=\sigma(Y_r(x):x\in W_n,r<s).
\]
Using
\[
\mu_s^{[n]}(\eta)
=t_s^{|\eta|}
 \sum_{T\supseteq\eta}
 \mathbf P[Z\cap W_n=T]e^{-s|T\setminus\eta|},
\]
we obtain, for \(x\in W_n\setminus\eta\),
\[
\mathbb E[R_x(s)\mid\mathcal H_{s-}^{n,0}]
=\frac{e^{-s}}{t_s}
 \frac{\mu_s^{[n]}(\eta\cup\{x\})}{\mu_s^{[n]}(\eta)}.
\tag{22}
\]

Because \(Q^{[n]}\ge cI\) and \(0<t_s<1\),
\[
L_s=t_sQ^{[n]}(I-t_sQ^{[n]})^{-1}
\]
is positive definite, so all the denominators in (22) are positive. The finite \(L\)-ensemble formula and the Schur determinant identity identify the ratio with \(b_{L_s}(x,\eta)\). Homogeneity of shorting gives
\[
\mathbb E[R_x(s)\mid\mathcal H_{s-}^{n,0}]
=b_{A_s^{[n]}}(x,Y_{s-}\cap W_n),
\tag{23}
\]
where
\[
A_s^{[n]}=e^{-s}Q^{[n]}(I-t_sQ^{[n]})^{-1}.
\]
For born \(x\), both sides vanish. Time zero has zero compensator measure; its rate is defined through \(A_0=Q\).

## 5. Moving windows and the infinite full-past compensator

Let \(P_n=P_{W_n}\), extend \(Q_n=P_nQP_n\) by zero, and set \(A_{s,n}=f_s(Q_n)\). Since \(f_s(0)=0\), this is \(A_s^{[n]}\) extended by zero.

We have \(Q_n\to Q\) strongly. The uniformly convergent Neumann series on bounded time intervals gives \(A_{s,n}\to A_s\) strongly. Moreover, for \(0\le s\le T\),
\[
A_{s,n}\ge c_TP_n,\qquad A_s\ge c_TI,
\]
\[
c_T=\frac{e^{-T}c}{1-(1-e^{-T})c}>0.
\tag{24}
\]

Fix an arbitrary, possibly infinite, \(\eta\), and write
\[
D_n=D_{\eta\cap W_n},\quad D=D_\eta,
\]
\[
C_n=D_nA_{s,n}D_n+I-D_n,\qquad C=DA_sD+I-D.
\]
Then \(D_n\to D\) and \(C_n\to C\) strongly, while \(C_n,C\ge c_TI\). The identity
\[
C_n^{-1}-C^{-1}=C_n^{-1}(C-C_n)C^{-1}
\]
proves strong convergence of the inverses.

The minimization in (3) is now coercive on the constrained subspace. Its minimizer is \(-C_n^{-1}D_nA_{s,n}f\), and hence
\[
\begin{aligned}
\mathsf S_{\eta\cap W_n}(A_{s,n})
&=A_{s,n}-A_{s,n}D_nC_n^{-1}D_nA_{s,n}\\
&\longrightarrow
A_s-A_sDC^{-1}DA_s
=\mathsf S_\eta(A_s)
\end{aligned}
\tag{25}
\]
strongly. Therefore
\[
b_{A_s^{[n]}}(x,\eta\cap W_n)\longrightarrow b_{A_s}(x,\eta)
\tag{26}
\]
once \(x\in W_n\). This explicitly handles both the moving operator and the moving constraint.

For fixed \(x,s>0\),
\[
\mathcal H_{s-}^{n,0}\uparrow
\mathcal H_{s-}^0
=\sigma(Y_r(x):r<s,\ x\in W).
\]
The upward conditional-expectation theorem applies: for integrable \(R\) and increasing sigma fields \(\mathcal F_n\),
\[
\mathbb E[R\mid\mathcal F_n]
\longrightarrow
\mathbb E[R\mid\sigma(\cup_n\mathcal F_n)]
\quad\text{almost surely and in }L^1.
\]
Here \(R_x(s)\in[0,1]\), so the hypotheses hold. :chatgpt-content-reference{index="3"}

Combining (23) and the samplewise limit (26),
\[
\mathbb E[R_x(s)\mid\mathcal H_{s-}^0]
=\lambda_x(s):=b_{A_s}(x,Y_{s-})
\quad\text{almost surely for every fixed }s>0.
\tag{27}
\]

We do not claim that an arbitrary collection of conditional versions is jointly measurable. The specified right side already is Borel and predictable. For bounded nonnegative \(\mathcal H^0\)-predictable \(U\), the variable \(U_s\) is \(\mathcal H_{s-}^0\)-measurable. Equation (20), then (27) and Fubini, give
\[
\mathbb E\int_0^T U_s\,dY_s(x)
=\mathbb E\int_0^T U_sR_x(s)\,ds
=\mathbb E\int_0^T U_s\lambda_x(s)\,ds.
\tag{28}
\]
Thus \(Y_t(x)-\int_0^t\lambda_x(s)ds\) is a raw \(\mathcal H^0\)-martingale. This is a full infinite-past compensator identity.

## 6. Right-continuous augmentation, proved explicitly

We need the following lemma.

**Augmentation lemma.** Let \((\mathcal F_t^0)\) be a filtration, and let \(\mathcal N\) be the family of all subsets of ambient measurable null sets, completing the ambient probability space. Put
\[
\mathcal F_t=\bigcap_{u>t}(\mathcal F_u^0\vee\mathcal N).
\tag{29}
\]
If \(M\) is a càdlàg \(\mathcal F^0\)-martingale, right-continuous in \(L^1\) at deterministic times, then \(M\) is an \(\mathcal F\)-martingale. Compact-time domination by an integrable random variable suffices for the \(L^1\) hypothesis.

**Proof.** For \(A\in\mathcal F_s\) and \(s<t\), choose \(s_n\downarrow s\) with \(s<s_n<t\). Since \(A\in\mathcal F_{s_n}^0\vee\mathcal N\), completion and the raw martingale identity give
\[
\mathbb E[\mathbf1_A M_t]
=\mathbb E[\mathbf1_A M_{s_n}]
\longrightarrow \mathbb E[\mathbf1_A M_s].
\]
Adaptedness is immediate. This proves the assertion. Compact integrable domination gives the required \(L^1\) convergence. The filtration in (29) is complete and right-continuous by its definition.

Raw predictable processes remain predictable for the enlarged filtration. A preserved compensated-count martingale gives compensation for augmented predictable rectangles, and then for all nonnegative predictable tests by a monotone-class extension. \(\square\)

For (28), the compensated martingale is bounded on \([0,T]\) by \(1+T\). Hence \(\lambda_x(s)ds\) remains its compensator in the usual augmentation of \(\mathcal H^0\).

The lemma does not assert equality of raw and augmented sigma fields. It will be applied again below to integrably dominated **finite-spatial-window** counts, never to an infinite total count.

## 7. Progressive marking and Poisson completion

Enlarge the weak-process space by iid \(V_x\sim\operatorname{Uniform}(0,1)\) and an independent unit-rate Poisson field \(M_x\), both independent of the whole \(Y\) path. Reveal \(V_x\) only at the true birth of \(x\), and give that birth mark
\[
u_x=\lambda_x(\tau_x)V_x.
\tag{30}
\]
There is almost surely no birth with \(\lambda_x=0\), because (28) gives
\[
\mathbb E\int_0^T
\mathbf1_{\{\lambda_x(s)=0\}}\,dY_s(x)=0.
\tag{31}
\]
Countability handles all sites and integer horizons simultaneously.

Let \(J\) be the marked real-birth point measure. Retain from \(M_x\) the points with \(u>\lambda_x(s)\), calling the retained measure \(K\), and set
\[
N=J+K.
\tag{32}
\]

First use the raw progressive filtration
\[
\mathcal G_t^0
=\mathcal H_t^0
 \vee\sigma(V_xY_t(x):x\in W)
 \vee\mathcal M_t^0.
\tag{33}
\]
The latent terminal field and unrevealed marks are not adjoined as generators. Both \(Y\) and \(N\) are adapted to this filtration.

For an auxiliary unmarked calculation, define
\[
\mathcal K_t^0
=\mathcal H_t^0\vee\sigma(V_x:x\in W)\vee\mathcal M_t^0.
\]
The unmarked martingale \(Y_x-\int\lambda_xds\) remains a martingale in \(\mathcal K^0\): test against products of a bounded \(\mathcal H_r^0\)-variable, a bounded function of \(V\), and a bounded \(\mathcal M_r^0\)-variable. Independence from the whole \(Y\) path factors the latter two from the expectation. Such products generate the sigma field. Also \(M\) remains Poisson relative to \(\mathcal K^0\), since its future is independent of its past and of \((Y,V)\).

The marked real compensator requires the progressive filtration, not this enlarged auxiliary filtration. Fix a site \(x\), a bounded \(\mathcal G_r^0\)-measurable variable \(H\), and a bounded Borel function \(\varphi\). On \(\{\tau_x>r\}\), \(H\) cannot use \(V_x\): the revealing generator \(V_xY_r(x)\) equals zero. For cylinder functions this follows by replacing \(V_x\) by a fixed dummy value, and the property extends by a monotone class.

Therefore, in an expectation involving a birth of \(x\) in \((r,t]\),