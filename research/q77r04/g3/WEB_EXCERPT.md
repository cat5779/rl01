PROVED

Write \(o=H\) and
\[
d(g)=[H:H\cap gHg^{-1}].
\]
The hypothesis is precisely that \(d(g)=d(g^{-1})<\infty\) for every \(g\in\Gamma\).

We will construct a total Borel map
\[
\Phi_Q:[0,1]^W\longrightarrow\{0,1\}^W
\]
that is equivariant everywhere and has push-forward law \(\mathbf P^Q\).

The DPP background used is existence for positive contractions and the defining identities
\[
\mathbf P^Q(F\subseteq Z)=\det Q_F
\qquad(F\subset W\text{ finite}),
\]
which determine the law by inclusion–exclusion. Equivariance of \(Q\) makes this law invariant. These facts are recorded in Sections 2–3 of Lyons–Thom. :chatgpt-content-reference{index="0"}

## 1. Orbit counting and the random-operator trace

### Orbit counting

The map
\[
H/(H\cap gHg^{-1})\longrightarrow H\cdot gH,
\qquad
h(H\cap gHg^{-1})\longmapsto hgH
\]
is a bijection: two images agree exactly when the quotient of the representatives lies in \(H\cap gHg^{-1}\). Thus the \(H\)-orbit of \(gH\) has size \(d(g)\). These orbits are indexed by \(H\backslash\Gamma/H\), with the orbit/index convention used in Anantharaman-Delaroche, Section 1.1. :chatgpt-content-reference{index="1"}

Let \(f:W^2\to[0,\infty]\) be diagonally \(\Gamma\)-invariant. Choosing one representative per double coset gives
\[
\sum_{y\in W}f(o,y)
=\sum_{HgH}d(g)f(o,gH).                                      \tag{1}
\]
Also,
\[
f(gH,o)=f(o,g^{-1}H).
\]
Inversion bijects the double cosets, so
\[
\sum_{y\in W}f(y,o)
=\sum_{HgH}d(g^{-1})f(o,gH).                                  \tag{2}
\]
The rearrangements involve nonnegative series. Balance makes (1) and (2) equal.

Consequently, if \(\Gamma\) acts probability-preservingly on \((\Omega,\mathbb P)\) and
\[
F(g\omega,gx,gy)=F(\omega,x,y),\qquad F\geq0,
\]
then applying (1)–(2) to \(\mathbb EF\) and using Tonelli gives
\[
\mathbb E\sum_yF(\omega,o,y)
=\mathbb E\sum_yF(\omega,y,o).                                \tag{3}
\]
For complex transports, the same conclusion holds whenever the outgoing absolute sum is integrable: first apply (3) to \(|F|\).

### The actual random trace

Let \(U_g\delta_x=\delta_{gx}\). Consider essentially uniformly bounded, weakly measurable operator fields satisfying
\[
B_{g\omega}=U_gB_\omega U_g^*.
\]
Products of fields are taken at the **same** \(\omega\). Define
\[
\tau_\Omega(B)=\mathbb E(B_\omega)_{oo}.
\]

For two such fields \(B,C\), use the transport
\[
F(\omega,x,y)=(B_\omega)_{xy}(C_\omega)_{yx}.
\]
It is jointly covariant, and
\[
\sum_y|(B_\omega)_{oy}(C_\omega)_{yo}|
\leq
\|B_\omega^*\delta_o\|\,\|C_\omega\delta_o\|
\leq\|B\|_\infty\|C\|_\infty.
\]
Therefore (3) applies and yields
\[
\begin{aligned}
\tau_\Omega(BC)
&=\sum_y\mathbb E(B_\omega)_{oy}(C_\omega)_{yo}\\
&=\sum_y\mathbb E(B_\omega)_{yo}(C_\omega)_{oy}
=\tau_\Omega(CB).                                             \tag{4}
\end{aligned}
\]

This functional is positive and unital. It is faithful: if
\[
\tau_\Omega(B^*B)=\mathbb E\|B\delta_o\|^2=0,
\]
invariance and transitivity imply \(B\delta_x=0\) almost surely for each \(x\); countability gives \(B=0\) almost surely. On decomposable operators, it is the vector state of the constant section \(\delta_o\), hence is normal.

Thus it is a finite trace on the algebra of bounded covariant random fields. **The fields need not commute with \(\Gamma\) at a fixed sample.** Their joint covariance and the invariant probability law are what establish (4).

This is a direct proof of the random trace property, not an inference from the deterministic root-state criterion discussed in Anantharaman-Delaroche, Section 1.3. :chatgpt-content-reference{index="2"}

## 2. Shorting and the precise averaged Lipschitz estimate

For \(0\leq A\leq I\), set
\[
K_\eta=\overline{A^{1/2}\ell^2(\eta)},\qquad
\Pi_\eta^A=P_{K_\eta},\qquad
S_\eta(A)=A^{1/2}(I-\Pi_\eta^A)A^{1/2}.
\]
Then
\[
\langle S_\eta(A)f,f\rangle
=\inf_{g\in\ell^2(\eta)}
  \langle A(f+g),f+g\rangle.                                 \tag{5}
\]
In particular,
\[
0\leq S_\eta(A)\leq A\leq I,
\]
\(b_A(x,\eta)=0\) for \(x\in\eta\), and \(b_A(x,\eta)\) decreases as \(\eta\) increases.

The infimum can be taken over finite-support rational complex vectors supported in \(\eta\), proving Borel measurability.

The projections and polar parts also belong to the random algebra just considered. Indeed, with \(P_\eta\) the coordinate projection and
\[
C_\eta=A^{1/2}P_\eta A^{1/2},
\]
we have
\[
\Pi_\eta^A
=\operatorname{s-lim}_{n\to\infty}
 C_\eta(C_\eta+n^{-1}I)^{-1}.                                 \tag{6}
\]
This is the support projection of
\[
C_\eta=(A^{1/2}P_\eta)(A^{1/2}P_\eta)^*.
\]
The formula gives measurable bounded covariant fields without selecting bases of random subspaces. Likewise, the polar part of a measurable covariant field \(T\) is
\[
V=\operatorname{s-lim}_{n\to\infty}
T(T^*T+n^{-1}I)^{-1/2}.                                      \tag{7}
\]

### Nested jointly invariant pairs

Suppose \(A\) is deterministic and equivariant, and \((\eta,\zeta)\) has a jointly invariant law with \(\eta\subseteq\zeta\). Put
\[
D=P_{\zeta\setminus\eta},
\qquad
T=(I-\Pi_\eta^A)A^{1/2}D.
\]
Since
\[
K_\zeta
=\overline{K_\eta+A^{1/2}\ell^2(\zeta\setminus\eta)},
\]
we have
\[
\overline{\operatorname{ran}T}=K_\zeta\ominus K_\eta.
\]
Thus, for \(T=V|T|\),
\[
VV^*=\Pi_\zeta^A-\Pi_\eta^A=:P,\qquad V^*V\leq D.
\]
All these are measurable covariant random fields. Equation (4) gives
\[
\tau_\Omega(P)
=\tau_\Omega(VV^*)
=\tau_\Omega(V^*V)
\leq\tau_\Omega(D)
=\mathbb P(o\in\zeta\setminus\eta).                           \tag{8}
\]
Moreover,
\[
\begin{aligned}
\mathbb E[b_A(o,\eta)-b_A(o,\zeta)]
&=\tau_\Omega(A^{1/2}PA^{1/2})\\
&=\tau_\Omega(PAP)
\leq\tau_\Omega(P)
\leq\mathbb P(o\in\zeta\setminus\eta).                        \tag{9}
\end{aligned}
\]

### Arbitrary jointly invariant pairs

Let \(\theta=\eta\cap\zeta\). Monotonicity gives
\[
|b_A(o,\eta)-b_A(o,\zeta)|
\leq b_A(o,\theta)-b_A(o,\eta)
   +b_A(o,\theta)-b_A(o,\zeta).
\]
Applying (9) twice, with disjoint difference sets, proves
\[
\boxed{
\mathbb E|b_A(o,\eta)-b_A(o,\zeta)|
\leq\mathbb P(\eta(o)\ne\zeta(o)).
}                                                            \tag{10}
\]

No independence is needed, but the **chosen coupling must be jointly invariant**.

Invariant marginals alone do not suffice. For a counterexample, let \(W=\{0,1\}\), let \(C_2\) swap the points, and take
\[
A=\frac12
\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]
With probability \(1/2\) each, set
\[
(\eta,\zeta)=(\varnothing,\{1\})
\quad\text{or}\quad
(\eta,\zeta)=(\{0,1\},\{0\}).
\]
Both marginals are invariant, and \(\eta(0)=\zeta(0)\) always. But shorting \(A\) by any nonempty set gives zero, so the left side of (10) is \(1/4\), whereas the right side is zero.

Every application of (10) below uses a jointly invariant coupling.

### One-sided parameter continuity

For later use, if \(A_j\downarrow A\) strongly, then, for fixed \(\eta,f\),
\[
\begin{aligned}
\inf_j\langle S_\eta(A_j)f,f\rangle
&=\inf_j\inf_{g\in\ell^2(\eta)}
  \langle A_j(f+g),f+g\rangle\\
&=\inf_{g\in\ell^2(\eta)}\inf_j
  \langle A_j(f+g),f+g\rangle\\
&=\langle S_\eta(A)f,f\rangle.
\end{aligned}                                                \tag{11}
\]
Hence \(S_\eta(A_j)\downarrow S_\eta(A)\) strongly. This concerns fixed \(\eta\); the moving-window assertion is proved separately below.

## 3. The \(W\)-indexed Poisson/Picard construction

Define
\[
t_s=1-e^{-s},\qquad
A_s=e^{-s}Q(I-t_sQ)^{-1}.                                    \tag{12}
\]
For \(q\in[0,1]\),
\[
f_s(q)=\frac{e^{-s}q}{1-(1-e^{-s})q}\in[0,1],
\]
including \(q=1\). Thus \(0\leq A_s\leq I\). On bounded time intervals, the denominator is uniformly bounded away from zero, so \(s\mapsto A_s\) is norm-continuous.

The map \((s,\eta)\mapsto b_{A_s}(x,\eta)\) is Borel. For an adapted coordinatewise càdlàg configuration process, its evaluation at the left limit is predictable.

Take independent PRMs
\[
N_x(ds\,du),\qquad x\in W,
\]
on \((0,\infty)\times(0,1)\), each with intensity \(ds\,du\). Use their common natural filtration with its usual augmentation. Starting from \(X^{(0)}=\varnothing\), define
\[
X^{(k+1)}_s(x)
=\mathbf1\!\left\{
\exists(r,u)\in N_x:
r\leq s,\ 
u\leq b_{A_r}(x,X^{(k)}_{r-})
\right\}.                                                    \tag{13}
\]
Each iterate is an adapted Borel equivariant function of the PRM past. Every coordinate has at most one birth. All iterates are jointly invariant.

Let
\[
D_k(T)=
\mathbb P\!\left(
X^{(k+1)}_\cdot(o)\ne X^{(k)}_\cdot(o)
\text{ somewhere on }[0,T]
\right).
\]
If two updated paths disagree, some common proposal lies in the symmetric difference of their acceptance intervals. Predictable compensation and (10) give, for \(k\geq1\),
\[
\begin{aligned}
D_k(T)
&\leq\int_0^T
 \mathbb E\left|
 b_{A_s}(o,X^{(k)}_{s-})
 -b_{A_s}(o,X^{(k-1)}_{s-})
 \right|\,ds\\
&\leq\int_0^T D_{k-1}(s)\,ds.
\end{aligned}
\]
Since \(D_0(T)\leq1\),
\[
D_k(T)\leq \frac{T^k}{k!}.                                   \tag{14}
\]

Summability and Borel–Cantelli imply eventual exact agreement of successive iterates at each coordinate on each compact time interval. Transitivity gives the same bound at every site; countability of \(W\) and of integer horizons gives a single full-measure stabilization event.

Denote the limit by \(X\). The stabilization event is Borel and invariant. Declare the path empty on its null complement; in the usual augmentation this version remains adapted. It is coordinatewise càdlàg and pure-birth.

The nonlocality of the rates requires checking the fixed point, rather than merely taking pointwise limits. Let \(\Psi_N\) denote the update in (13). Compensation and (10) applied to \((X^{(k)},X)\) give
\[
\begin{aligned}
&\mathbb P\!\left(
\Psi_N(X^{(k)})_\cdot(o)\ne
\Psi_N(X)_\cdot(o)\text{ on }[0,T]
\right)\\
&\hspace{2cm}\leq
\int_0^T
\mathbb P(X^{(k)}_{s-}(o)\ne X_{s-}(o))\,ds
\longrightarrow0.
\end{aligned}
\]
But \(\Psi_N(X^{(k)})=X^{(k+1)}\) also converges to \(X\) in this compact-path sense. Therefore
\[
X=\Psi_N(X)
\]
almost surely, simultaneously at all sites and times.

### Exact uniqueness class

Suppose \(U,V\) are adapted pure-birth solutions from the empty configuration, driven by the same \(N\), in a common filtration \(\mathcal G\). Assume \(N\) is a PRM field relative to \(\mathcal G\), and \((N,U,V)\) has a jointly invariant law.

For the root compact-path disagreement probability \(D(T)\), the same calculation gives
\[
D(T)\leq\int_0^T D(s)\,ds.
\]
Since \(D\leq1\), iteration gives \(D(T)\leq T^n/n!\) for every \(n\), hence \(D(T)=0\). Countability gives indistinguishability.

A solution need not initially be adapted to the natural filtration of \(N\). Adaptation to this common filtration suffices. No uniqueness claim outside this class is needed.

## 4. Terminal thinning and finite-window full-past hazards

Temporarily suppose
\[
Q\geq cI,\qquad c>0.                                        \tag{15}
\]

Take \(Z\sim\mathbf P^Q\) and independent mean-one exponential variables \(E_x\), also independent of \(Z\). Define
\[
Y_s(x)=\mathbf1_{\{x\in Z,\ E_x\leq s\}}.                    \tag{16}
\]
This process is invariant and pure-birth, with no simultaneous births at distinct sites almost surely. Its inclusion probabilities show that
\[
Y_s\sim\mathbf P^{t_sQ}.                                    \tag{17}
\]

We must identify its intensities in the **observed full-past filtration**.

Fix a finite \(F\ni x\), and let \(\mathcal F_s^F\) be generated by the observed paths in \(F\) through time \(s\). For \(s>0\), put
\[
K=t_sQ_F,\qquad
L=K(I-K)^{-1},\qquad
A_{s,F}=e^{-s}Q_F(I-t_sQ_F)^{-1}.                            \tag{18}
\]
Notice that \(A_{s,F}\) is formed from \(Q_F\); it is not being identified with the compression of \(A_s\).

The exact-set probabilities are
\[
p_s^F(\eta):=\mathbb P(Y_s\cap F=\eta)
=\det(I-K)\det L_\eta.                                      \tag{19}
\]
Indeed, the inclusion identities give
\[
\mathbb E\prod_{x\in F}z_x^{Y_s(x)}
=\det(I-K+K\operatorname{diag}(z)).
\]
Factoring \(I-K\) and expanding principal minors gives
\[
\det(I-K)
\sum_{\eta\subseteq F}\det L_\eta\prod_{x\in\eta}z_x,
\]
proving (19). Under (15), \(L\) is positive definite, so all these probabilities are positive.

The exact observed birth times carry no additional information about \(Z\cap F\) once the current observed set \(\eta\) is known. For a possible terminal set \(T\supseteq\eta\), their likelihood is proportional to
\[
\mathbf P(Z\cap F=T)
\left(\prod_{y\in\eta}e^{-r_y}\right)
e^{-s|T\setminus\eta|}.
\]
The factor involving the observed times is independent of \(T\).

Exponential memorylessness therefore gives, at a vacant \(x\in F\),
\[
\begin{aligned}
\lambda_F(s,x)
&=\mathbb P(x\in Z\mid\mathcal F_{s-}^F)\\
&=\frac{1-t_s}{t_s}
  \frac{p_s^F(\eta\cup\{x\})}{p_s^F(\eta)},
\qquad \eta=Y_{s-}\cap F.                                   \tag{20}
\end{aligned}
\]
The ratio also follows directly by comparing thinning weights for the same terminal sets containing \(\eta\cup\{x\}\). At occupied sites the intensity is zero.

Since
\[
L=\frac{t_s}{1-t_s}A_{s,F},
\]
the determinant ratio and the Schur-complement formula yield
\[
\lambda_F(s,x)
=b_{A_{s,F}}(x,Y_{s-}\cap F).                               \tag{21}
\]
The Schur-complement formula is exactly the minimization in (5) for a positive definite finite matrix.

For completeness, the compensator assertion can be checked directly. Before projection to the observed filtration, the exponential waiting time has intensity
\[
\mathbf1_{\{x\in Z\}}\mathbf1_{\{E_x\geq s\}}.
\]
Integrating its density \(e^{-s}\) verifies compensation for predictable tests: their past is the same whether the unobserved clock equals \(s\) or exceeds \(s\). Conditional expectation onto the observed past, followed by the calculation above, proves that
\[
Y_t(x)-\int_0^t\lambda_F(s,x)\,ds
\]
is an \(\mathcal F^F\)-martingale. Thus (21) is a full-past hazard identity, not merely a consequence asserted from the one-time laws.

## 5. Moving-window shorting and the infinite full-past hazard

We need a separate continuity lemma.

**Moving-window lemma.** Let finite sets \(F_n\uparrow W\) have coordinate projections \(P_n\). Suppose
\[
B_n=P_nB_nP_n,\qquad
aP_n\leq B_n\leq P_n,\qquad
B_n\longrightarrow B\text{ strongly},\qquad a>0.
\]
Then, for every fixed \(\eta\subseteq W\) and \(x\in W\),
\[
b_{B_n}(x,\eta\cap F_n)\longrightarrow b_B(x,\eta),           \tag{22}
\]
where \(B_n\) is extended by zero outside \(F_n\).

**Proof.** If \(x\in\eta\), both sides eventually vanish. Otherwise, every finite-support competitor in \(\ell^2(\eta)\) is available for all sufficiently large \(n\). Strong convergence in (5) gives the required upper bound on the limsup.

For the lower bound, pass to a subsequence realizing the liminf and choose
\[
h_n=\delta_x+g_n,\qquad
g_n\in\ell^2(\eta\cap F_n),
\]
whose energies are within \(1/n\) of the infima. Their energies are at most \(1+1/n\); coercivity on \(F_n\) makes \((h_n)\) bounded. Along a subsequence,
\[
h_n\rightharpoonup h=\delta_x+g,\qquad g\in\ell^2(\eta).
\]
Continuous functional calculus on uniformly bounded positive operators gives
\[
B_n^{1/2}\longrightarrow B^{1/2}\quad\text{strongly}.
\]
Consequently,
\[
B_n^{1/2}h_n\rightharpoonup B^{1/2}h.
\]
Weak lower semicontinuity yields
\[
\liminf_n\langle B_nh_n,h_n\rangle
\geq\langle Bh,h\rangle
\geq b_B(x,\eta).
\]
This proves (22). \(\square\)

Apply the lemma with
\[
Q_n=P_nQP_n,\qquad B_n=f_s(Q_n),\qquad B=A_s.
\]
Because \(f_s(0)=0\), \(B_n\) is exactly the zero extension of \(A_{s,F_n}\). Strong convergence \(Q_n\to Q\) gives \(B_n\to A_s\) strongly. On \(0\leq s\leq T\),
\[
ce^{-T}P_n\leq B_n\leq P_n.
\]
Thus, for every \(s\) and every configuration \(\eta\),
\[
b_{A_{s,F_n}}(x,\eta\cap F_n)
\longrightarrow b_{A_s}(x,\eta).                            \tag{23}
\]
No invariance of the finite windows is assumed.

Let \(\mathcal F_s^Y\) be the full observed-past filtration and define
\[
\lambda_x(s)=b_{A_s}(x,Y_{s-}).                              \tag{24}
\]
This is predictable and bounded by one.

For a bounded predictable test depending on histories in a fixed finite window, apply (21) in any larger \(F_n\). Equation (23) and dominated convergence pass its compensation identity to (24).

These tests generate the full predictable sigma-field. More explicitly, first take tests \(\mathbf1_{(a,b]}h\), where \(h\) is measurable with respect to a finite-window past at \(a\), and then apply a monotone-class argument over the increasing finite-window past sigma-fields. It follows that
\[
Y_t(x)-\int_0^t b_{A_s}(x,Y_{s-})\,ds                       \tag{25}
\]
is a martingale in the full observed-past filtration.

One may first work in the raw filtration and then take its usual augmentation. On bounded time intervals these martingales are bounded and càdlàg; for \(s<t\), conditioning along \(r\downarrow s\) gives
\[
\mathbb E[M_t\mid\mathcal F_{s+}]
=\lim_{r\downarrow s}M_r=M_s.
\]
Thus the martingale identities persist without revealing terminal information.

## 6. Progressive common-filtration Poisson completion

Independently of \(Y\), take iid uniforms \(V_x\in(0,1)\) and independent PRMs \(R_x(ds\,du)\) of intensity \(ds\,du\), the two auxiliary families also independent.

Let \(T_x\) be the birth time of \(Y(x)\), possibly infinite. At a birth, place a marked point at
\[
(T_x,\lambda_x(T_x)V_x),
\]
and call this marked birth measure \(M_x\).

A birth with \(\lambda_x(T_x)=0\) has probability zero, since for every finite \(T\),
\[
\mathbb E\int_0^T
\mathbf1_{\{\lambda_x(s)=0\}}\,dY_s(x)
=
\mathbb E\int_0^T
\mathbf1_{\{\lambda_x(s)=0\}}\lambda_x(s)\,ds
=0.
\]

Use the raw progressive filtration generated, for \(r\leq s\), by all \(Y_r(x)\), the restrictions of all \(R_x\) through time \(r\), and
\[
V_x\mathbf1_{\{T_x\leq r\}}.
\]
Thus a mark is revealed **only when its birth occurs**. We do not initially reveal \(Z\), the complete exponential-clock values, or unused uniforms.

The martingales (25) remain martingales in this enlargement. Indeed, averaging an event in the enlarged past conditional on the entire path of \(Y\) produces a variable measurable with respect to the past of \(Y\): the auxiliary variables are independent, and the set of revealed marks is determined by that past. The original martingale identity then applies. Independence likewise keeps \(R\) a PRM field in this filtration.

For a nonnegative predictable test \(h(s,u)\), extended by zero at \(u=0\), the mark \(V_x\) is still unrevealed just before the unique birth at \(x\). Integrating over that uniform and then using (25) gives
\[
\begin{aligned}
\mathbb E\int h(s,u)M_x(ds\,du)
&=\mathbb E\int
 \left[\int_0^1h(s,\lambda_x(s)v)\,dv\right]dY_s(x)\\
&=\mathbb E\int_0^\infty
 \int_0^{\lambda_x(s)}h(s,u)\,du\,ds.                         \tag{26}
\end{aligned}
\]
This is verified first for elementary predictable tests and then by monotone approximation.

Now define
\[
N_x(ds\,du)
=
M_x(ds\,du)
+\mathbf1_{\{u>\lambda_x(s)\}}R_x(ds\,du).                    \tag{27}
\]
Its joint compensator is deterministic: counting measure on \(W\), times \(ds\,du\).

We must also establish **jointly independent PRMs relative to the common filtration**, not merely individual compensators.

Distinct births of \(Y\) never occur simultaneously, because the underlying exponential clocks are independent and continuous. The independent padding PRMs have no simultaneous points on finite site sets and avoid all birth times almost surely. Thus, on every finite set of sites, the completed process has at most one marked point at any time.

Let \(F\) be finite and let \(\mu\) be its deterministic intensity measure. For bounded deterministic \(f\geq0\), supported in \((a,b]\times F\times(0,1)\), the single-jump change formula and the compensator identity show that
\[
L_t=
\exp\left\{
-\int_{(a,t]}f\,dN
+\int_{(a,t]}(1-e^{-f})\,d\mu
\right\},
\