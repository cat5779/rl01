# Invariant determinantal processes: factors, Bernoulli comparison, and coupling distance

English mathematical draft. This manuscript consolidates the project arguments identified in the accompanying source register. The labels PROVED, DISPROVED, and INCOMPLETE record the scope of the arguments supplied here; they do not assert publication, priority, or formal verification.

## Abstract

We give a Borel sampling construction for determinantal probability measures on a countable set. The construction is natural under every relabelling of the index set. Consequently, an equivariant determinantal measure is a factor of the product process on the same index set. Its dependence on the kernel is measurable, which yields a graph factor representation of the free uniform spanning forest on every locally finite connected simple random rooted graph, without a unimodularity assumption.

For the regular action of any countable group, we prove the two Bernoulli domination bounds expressed by Fuglede–Kadison determinants. These bounds are the exact parameters for every kernel on an amenable group. They need not be exact on a nonamenable group: the wired spanning forest projection of the three-regular tree, viewed on the regular edge action of \(C_3*C_3\), gives a strict counterexample. The failure persists for operators with a spectral gap at both endpoints and for finite-support group-algebra kernels. Finally, for sofic groups we obtain the sharp noncommutative trace-norm bound for invariant coupling distance by a polygonal interpolation using the ordered coupling theorem of Lyons–Thom.

## 1. Statements and their scope

For a countable set \(W\) and a Hermitian positive contraction \(Q\) on \(\ell^2(W)\), write \(\mu_Q\) for the determinantal probability measure characterized by
\[
 \mu_Q\{\eta:F\subseteq\eta\}=\det Q[F],
 \qquad F\subset W\ \text{finite}.
\]
Here \(Q[F]\) is the principal compression to \(\ell^2(F)\). We identify a subset with its indicator field.

### Theorem A: factors with the prescribed index set — PROVED

Let a countable group \(\Gamma\) act by permutations on a countable set \(W\). Suppose that \(0\le Q\le I\) commutes with this action. There is a Borel map
\[
 \Phi_Q:[0,1]^W\longrightarrow\{0,1\}^W
\]
defined on every input, equivariant on every input, and satisfying
\[
 (\Phi_Q)_*\operatorname{Leb}^W=\mu_Q.
\]
The construction can be chosen jointly Borel in the matrix entries of \(Q\), and natural under bijections between countable index sets.

The stronger action-free statement behind Theorem A is that one can choose a sampler for every positive contraction on every countable set, jointly Borel in the kernel and natural under every bijection of the index set. Equivariance for a group action is an immediate consequence of this naturality; it is not a hypothesis used to construct the sampler.

The source in this statement is indexed by **\(W\)**. Lyons–Thom use the term *Bernoulli shift* for product actions \(A^W\), as well as for regular product actions \(A^\Gamma\) [LT, p. 576]. We follow that convention when relating Theorem A to their Question 7.7. If \(W=\Gamma\times S\), the source is the regular Bernoulli shift with base \([0,1]^S\). No such replacement is asserted for an arbitrary action with infinite stabilizers. A concrete obstruction to making this replacement in general appears in Appendix A.

### Corollary A1: free uniform spanning forests as graph factors — PROVED

There is one Borel graph-factor rule which, for every locally finite connected simple random rooted graph \((G,o)\), transforms conditionally iid uniform vertex labels into a sample with conditional law \(\operatorname{FUSF}_G\).

We use the definition of Angel–Ray–Spinka: the rule is defined on marked rooted graph isomorphism classes, preserves the underlying graph, and is invariant under rerooting [ARS, §2.1]. It does not use the root to choose the output. No unimodularity, degree bound, recurrence, amenability, or equality of FUSF and WUSF is required. The word *simple* matters if the input consists only of vertex labels; see §4.4.

For a regular group action, let \(R(\Gamma)\) be the commutant of left translations on \(\ell^2(\Gamma)\), let
\[
 \tau(T)=\langle T\delta_e,\delta_e\rangle,\qquad
 D(Q)=\exp\!\left(\int_{[0,1]}\log\lambda\,d\nu_Q(\lambda)\right),
\]
where \(\nu_Q\) is the spectral distribution for \(\tau\), and set \(\exp(-\infty)=0\). This is the analytic Fuglede–Kadison determinant, including the spectral mass at zero.

Write \(\operatorname{Ber}(p)^W\) for the product law with occupation probability \(p\), and \(\preceq\) for ordinary stochastic domination. Define
\[
 p_-(Q)=\sup\{p:\operatorname{Ber}(p)^\Gamma\preceq\mu_Q\},\qquad
 p_+(Q)=\inf\{p:\mu_Q\preceq\operatorname{Ber}(p)^\Gamma\}.
\]

### Theorem B: Fuglede–Kadison domination — PROVED

For every countable group \(\Gamma\) and every positive contraction \(Q\in R(\Gamma)\),
\[
 \operatorname{Ber}(D(Q))^\Gamma
 \preceq\mu_Q
 \preceq\operatorname{Ber}(1-D(I-Q))^\Gamma.
 \tag{B}
\]
The operators may be complex Hermitian, singular, or injective without a bounded inverse. Soficity is not assumed. The conclusion is ordinary stochastic domination; an invariant monotone joining is a separate requirement.

### Theorem C: pointwise optimality and its failure

**PROVED, amenable case.** For every countable amenable group and every such \(Q\),
\[
 p_-(Q)=D(Q),\qquad p_+(Q)=1-D(I-Q).
 \tag{C1}
\]

**DISPROVED, general pointwise assertion.** On \(\Gamma=C_3*C_3\), there is an equivariant projection \(\Pi\) for which
\[
 D(\Pi)=0,\qquad p_-(\Pi)=\frac12,\qquad p_+(\Pi)=1.
 \tag{C2}
\]
Its complement disproves pointwise optimality of the upper bound. There are also strictly positive contractions, bounded away from both \(0\) and \(I\), with a strict lower-bound gap. Such counterexamples can be chosen in the finite-support group algebra \(\mathbb C\Gamma\).

Lyons's Conjecture 5.7 couples the inequalities (B) with an optimality assertion [ICM, p. 158]. If optimality means the exact parameters for each fixed kernel, Theorems B and C settle the truth of that assertion: the inequalities hold, but the proposed universal equalities do not. They do not classify which nonamenable groups or which individual kernels satisfy (C1). If optimality only means that a bound using the displayed single determinant value cannot be improved uniformly over all kernels, \(Q=pI\) already proves that weaker sharpness statement.

For invariant laws on \(\{0,1\}^\Gamma\), define
\[
 \bar d_\Gamma(\mu,\nu)
 =\inf_{\lambda\in J_\Gamma(\mu,\nu)}
       \lambda\{(X,Y):X_e\ne Y_e\},
\]
where \(J_\Gamma\) is the set of **invariant** joinings with the prescribed marginals.

### Theorem D: sharp noncommutative coupling bound — PROVED

If \(\Gamma\) is a countable sofic group and \(A,B\in R(\Gamma)\) are positive contractions, then
\[
 \bar d_\Gamma(\mu_A,\mu_B)\le\tau|A-B|.
 \tag{D}
\]
No commutativity assumption is needed, and the constant \(1\) is optimal. The proof uses the sofic ordered coupling theorem of Lyons–Thom. The extension of that input from finitely generated to countable sofic groups is supplied in §7.1.

Theorem A, Theorem B, and Theorem D answer different questions. Sampling two laws from iid labels does not by itself supply an invariant *monotone* joining. The proof of Theorem B establishes ordinary stochastic order. The proof of Theorem D explicitly uses an invariant joining theorem.

### Reading guide

Section 3 proves the sampling theorem. Section 4 supplies the additional measurability needed for random graphs. Sections 5 and 6 prove the FK comparison and analyze optimality. Section 7 is an independent, short argument for the coupling-distance bound. It addresses the unnumbered question after Lyons–Thom Lemma 7.8; their Question 7.7 is the factor question. The finite-support counterexample and the finite-matrix trace convention are isolated in Appendices B and C.

The dependencies are separate: the natural sampler gives Question 7.7 and, after a Borel graph-kernel construction, FUSF; a finite differential comparison gives the FK bounds; and the published invariant ordered-coupling theorem plus a polygon gives the trace-norm bound. None of the latter two arguments uses the sampling theorem.

## 2. Preliminaries and the original questions

The action on a product space is
\[
 (\gamma u)(x)=u(\gamma^{-1}x).
\]
A factor is a measurable map intertwining the actions. Theorem A provides an everywhere-defined Borel version with pointwise equivariance, rather than leaving exceptional inputs unspecified.

The finite cylinder probabilities of a DPP are recovered from its inclusion probabilities by
\[
 \mu_Q(\eta\cap F=S)
 =\sum_{S\subseteq T\subseteq F}(-1)^{|T\setminus S|}\det Q[T].
 \tag{2.1}
\]
We will repeatedly use two immediate consequences. Restricting the process to \(F\) compresses the kernel to \(Q[F]\); taking the complement replaces \(Q\) by \(I-Q\). Kernels with zero cross-block entries give independent processes on the blocks.

We also use the finite DPP comparison theorem: if \(0\le C\le C'\le I\) on a finite set, then \(\mu_C\preceq\mu_{C'}\) [LT, Theorem 2.1]. The same conclusion on a countable set follows by applying the finite theorem to every compression. More explicitly, extend each finite monotone coupling to the full prescribed marginals by conditional sampling; compactness along an exhaustion gives a coupling ordered on every coordinate. These applications do not assert invariance of a resulting coupling.

Lyons–Thom's Question 7.7 asks whether equivariant determinantal measures are factors of Bernoulli shifts. Their definitions explicitly allow \(W\)-indexed product actions. The preceding Theorem 7.3 assumes a finite generating set, a sofic group, and \(Q\in R(\Gamma)\) or \(R(\Gamma,S)\); it gives approximation by finitely dependent processes in \(\bar d\). Corollary 7.4 assumes amenability in the same regular or finite-type setting and concludes isomorphism to a Bernoulli shift. These are not stated there for arbitrary actions with stabilizers. Theorem A answers the broad \(A^W\) reading of Question 7.7, and in particular its regular and quasi-transitive special cases.

The optimality in Conjecture 5.7 is naturally read pointwise: the adjacent abelian result is a necessary-and-sufficient statement for each symbol, as made explicit in Lyons–Steif, Theorem 5.11 [LS]. This is an interpretation of the mathematical context, not an attribution of an unstated intention to the author. We retain the distinction between pointwise equality and uniform one-datum sharpness throughout.

## 3. A natural sampler for a countable DPP

The sampling mechanism has two parts. First we define a deterministic integral equation driven by one continuous path at each index. Then, by revealing an independent DPP through Gaussian observations, we identify the law of its solution under product Brownian input. This order separates the everywhere-defined map from the almost-sure argument identifying its distribution.

### 3.1 Finite windows selected by the kernel

Fix a countable set \(W\) and \(0\le K\le I\). For each integer \(n\ge1\), connect distinct \(x,y\) when \(|K(x,y)|\ge1/n\). Call this graph \(D_n\), and let \(E_n(x)\) be its radius-\(n\) ball about \(x\).

These are finite sets. Indeed,
\[
 \sum_y|K(x,y)|^2=(K^2)(x,x)\le K(x,x)\le1,
\]
so \(D_n\) has degree at most \(n^2\). The sets \(E_n(x)\) increase and exhaust the component of \(x\) in the graph of nonzero off-diagonal entries. Different components have zero cross-kernel entries, and their DPP configurations are independent by (2.1).

This choice of windows is important: it uses no enumeration of \(W\), no metric on the group, and no choice of a root.

### 3.2 A uniform bound on tilted covariances

**Lemma 3.1 — PROVED.** Let a finite DPP with positive contraction \(K_F\) be tilted by the density proportional to \(\exp(\sum_z h_z\eta_z)\), where \(h_z\) are arbitrary real numbers. If \(p_x\) is the tilted occupation probability, then
\[
 \sum_y|\operatorname{Cov}(\eta_x,\eta_y)|
 \le 2p_x(1-p_x)\le\frac12.
 \tag{3.1}
\]

**Proof.** Put \(D=\operatorname{diag}(e^{h_z})\) and
\[
 M=I-K_F+K_F^{1/2}DK_F^{1/2},\qquad
 H=D^{1/2}K_F^{1/2}M^{-1}K_F^{1/2}D^{1/2}.
\]
The bound \(M\ge\min(1,\min_zD_{zz})I\) makes the inverse well defined. Since \(M\ge K_F^{1/2}DK_F^{1/2}\), one has \(0\le H\le I\). The determinant generating function, together with \(\det(I+AB)=\det(I+BA)\), shows that the tilted law is \(\mu_H\). This formula does not require \(K_F\) or \(I-K_F\) to be invertible.

The one- and two-point determinants give
\[
 \operatorname{Var}(\eta_x)=p_x(1-p_x),\qquad
 \operatorname{Cov}(\eta_x,\eta_y)=-|H(x,y)|^2\quad(y\ne x).
\]
Consequently the absolute covariance row sum equals
\[
 p_x(1-p_x)+(H^2)(x,x)-p_x^2
 \le 2p_x(1-p_x).
\]
This proves (3.1), including singular and complex Hermitian kernels. \(\square\)

### 3.3 The deterministic equation

For a fixed countable \(W\), let \(\mathscr K_W\) be the subset of \(\mathbb C^{W\times W}\) whose finite principal matrices satisfy \(0\le K[F]\le I_F\). With the product topology on entries this is a closed subset of the product of closed unit discs, and hence compact metrizable. Its elements are exactly the matrices of positive contractions: the finite quadratic-form inequalities extend by density to a bounded positive operator on \(\ell^2(W)\). Thus \(\mathscr K_W\) is the standard Borel parameter space meant by “Borel in the kernel.” Let \(\mathscr P_W=C_0([0,\infty),\mathbb R)^W\), where \(C_0\) here means continuous paths with value zero at time zero, and each path coordinate has the topology of uniform convergence on compact intervals. This is also a Polish space.

Let \(\mu_F\) denote the actual marginal of \(\mu_K\) on \(F\). For \(t\ge0\) and an arbitrary real field \(y\in\mathbb R^W\), define
\[
 b^n_{t,x}(y)=
 \frac{\displaystyle\sum_{\sigma\in\{0,1\}^{E_n(x)}}
       \sigma_x\mu_{E_n(x)}(\sigma)
       \exp\!\left(\sum_{z\in E_n(x)}(y_z-t/2)\sigma_z\right)}
      {\displaystyle\sum_{\sigma\in\{0,1\}^{E_n(x)}}
       \mu_{E_n(x)}(\sigma)
       \exp\!\left(\sum_{z\in E_n(x)}(y_z-t/2)\sigma_z\right)},
 \qquad
 b_{t,x}(y)=\limsup_n b^n_{t,x}(y).
 \tag{3.2}
\]
Every denominator is positive. Thus \(b\) is defined for every \(t,y,x\), with values in \([0,1]\). Differentiating a finite tilted expectation gives its covariance row. Lemma 3.1 therefore implies
\[
 \sup_x|b_{t,x}(y)-b_{t,x}(y')|
 \le\frac12\|y-y'\|_\infty
 \quad\text{whenever }y-y'\in\ell^\infty(W).
 \tag{3.3}
\]
The limsup retains this bound; it is used to define the drift even where posterior limits have no probabilistic interpretation.

For any field \(w=(w_x)_{x\in W}\) of continuous paths starting at zero, set
\[
 Z^0_t=w_t,\qquad
 Z^{k+1}_t(x)=w_t(x)+\int_0^t b_{s,x}(Z^k_s)\,ds.
 \tag{3.4}
\]
Although the input field need not be spatially bounded, successive corrections are. Induction using (3.3) gives, for each finite \(T\),
\[
 \sup_{x,\,t\le T}|Z^{k+1}_t(x)-Z^k_t(x)|
 \le\frac{(1/2)^kT^{k+1}}{(k+1)!}.
 \tag{3.5}
\]
Hence the iterates converge uniformly in \(x\) and locally uniformly in time to a solution
\[
 Z_t(x)=w_t(x)+\int_0^t b_{s,x}(Z_s)\,ds.
 \tag{3.6}
\]
Any two solutions with this input differ by a bounded correction on \([0,T]\); (3.3) and Gronwall give uniqueness. Denote the solution by \(\mathcal Z_K(w)\).

**Proposition 3.2 (measurable solution map) — PROVED.** Equation (3.6) defines a jointly Borel map
\[
 \mathcal Z:\mathscr K_W\times\mathscr P_W\longrightarrow\mathscr P_W,
 \qquad (K,w)\longmapsto\mathcal Z_K(w),
\]
with a unique solution for every input pair.

Existence and uniqueness were proved in (3.4)–(3.6). To check measurability, fix an enumeration of \(W\) solely for this check. Membership in \(E_n(x)\) is a countable union of finite path conditions on entries of \(K\), hence Borel. The event \(E_n(x)=F\) is Borel for every finite \(F\), and there are only countably many such \(F\). On each event the finite sums in (3.2) have Borel coefficients by (2.1). Consequently \((K,t,y)\mapsto b_{t,x}(y)\) is Borel. Composition with path evaluation and integration of a bounded Borel function show inductively that \((K,w,t)\mapsto Z_t^k(x)\) is Borel. Parameter integration follows first for simple functions and then by bounded measurable approximation. Each iterate is continuous in time. Its values at nonnegative rational times therefore give a Borel map into the continuous-path space. The locally uniform Picard limit retains this property. The enumeration is absent from the defining formulas, so this measurability check makes no choice in the resulting map. \(\square\)

### 3.4 Identifying the law

**Lemma 3.3 (law identification) — PROVED.** If \(w\) is a field of independent standard Brownian motions, the map
\[
 \mathcal S_K(w)_x
   =\liminf_{m\to\infty}
       \mathbf1\{\mathcal Z_K(w)_m(x)>m/2\}
 \tag{3.7}
\]
has law \(\mu_K\).

**Proof.** On an auxiliary probability space, take \(\eta\sim\mu_K\), independent of an iid Brownian field \(B\), and observe
\[
 X_t(x)=t\eta_x+B_t(x).
\]
**Claim 1: endpoint posteriors.** For fixed \(t>0\), finite-dimensional Gaussian Bayes gives
\[
 b^n_{t,x}(X_t)
   =\mathbb E[\eta_x\mid X_t(z),\,z\in E_n(x)].
\]
Indeed, the likelihood ratio of the observation at site \(z\), relative to a centered normal variable of variance \(t\), is \(\exp(X_t(z)\sigma_z-t\sigma_z/2)\), since \(\sigma_z^2=\sigma_z\). Multiplication over the finite window gives exactly (3.2). The windows increase to the kernel component of \(x\), so bounded martingale convergence identifies their limit with the conditional expectation on all endpoints in that component. The pairs of DPP coordinates and Brownian paths in different components are independent. Adding the other components' endpoints does not change that conditional expectation. Thus the limsup in (3.2), on this observation field, equals the full endpoint posterior for each fixed \(t\), almost surely.

**Claim 2: observation histories and null sets.** For \(0\le r\le t\), write
\[
 X_r(z)=\frac rt X_t(z)
          +\left(B_r(z)-\frac rt B_t(z)\right).
\]
For any finite list of coordinates and times, the bridge terms are centered jointly Gaussian, have zero covariance with all the endpoints \(B_t(z)\), and are independent of \(\eta\). They are therefore independent of \((\eta,X_t)\). By the monotone-class theorem the sigma-field generated by all bridge terms at rational times and all sites is independent of \(\sigma(\eta,X_t)\). Countability of \(W\) and continuity of each path show that these rational-time terms generate the whole bridge history. Moreover, the displayed decomposition shows that the observation-history sigma-field is generated by the endpoints and these bridges. Independence therefore proves
\[
 b_{t,x}(X_t)=
 \mathbb E[\eta_x\mid\mathcal F_t^0],\qquad
 \mathcal F_t^0=\sigma(X_r(z):r\le t,\ z\in W).
 \tag{3.8}
\]
The finite posterior sequence is jointly measurable in \((t,\omega)\), and converges almost surely at each fixed \(t>0\). Fubini makes its convergence simultaneous outside a \(dt\otimes d\mathbb P\)-null set, and a countable intersection handles all sites. Equivalently, the conditional-expectation identity (3.8) holds at each fixed time, with this jointly measurable representative for time integration. No intersection of exceptional sets over uncountably many times is taken. The value at \(t=0\) is immaterial to the integrals.

**Claim 3: a common Brownian innovation field.** Define
\[
 \beta_t(x)=X_t(x)-\int_0^t b_{s,x}(X_s)\,ds.
\]
The process \(b_{s,x}(X_s)\) is bounded and progressively measurable: it is a Borel function of time and the countable continuous adapted vector \(X_s\). For \(s<t\) and \(A\in\mathcal F_s^0\), this event lies in \(\sigma(\eta,B_r(z):r\le s,z\in W)\), so the future Brownian increment has mean zero on it. Also \(A\in\mathcal F_r^0\) for \(r\ge s\). Equation (3.8) and bounded Fubini consequently yield
\[
 \mathbb E[\mathbf1_A(\beta_t(x)-\beta_s(x))]
 =\mathbb E[\mathbf1_A(B_t(x)-B_s(x))]
  +\int_s^t\mathbb E[\mathbf1_A(\eta_x-b_{r,x}(X_r))]\,dr
 =0.
\]
Thus each coordinate is a continuous integrable martingale for the same raw filtration. Let \(\mathcal N\) denote the null sets of the ambient probability space and set \(\mathcal F_s=\bigcap_{u>s}(\mathcal F_u^0\vee\mathcal N)\). Completion does not change conditional expectations. For \(s_j\downarrow s\), \(s_j<t\), the raw martingale property gives \(\mathbb E[\beta_t(x)\mid\mathcal F_{s_j}^0\vee\mathcal N]=\beta_{s_j}(x)\). Reverse martingale convergence and the estimate
\[
 \mathbb E|\beta_{s_j}(x)-\beta_s(x)|
 \le \sqrt{s_j-s}+(s_j-s).
\]
show that \(\mathbb E[\beta_t(x)\mid\mathcal F_s]=\beta_s(x)\). Hence all coordinates remain martingales for this one completed, right-continuous filtration. The bounded finite-variation correction to \(B\) does not change quadratic covariations, so
\[
 [\beta(x),\beta(y)]_t=\mathbf1_{\{x=y\}}t.
\]
For a finite list of distinct coordinates and \(\lambda\in\mathbb R^k\), Itô's formula makes \(\exp(i\lambda\cdot\beta_t+|\lambda|^2t/2)\) a local martingale. Its modulus is bounded on every finite time interval, so it is a true martingale there. Thus
\[
 \mathbb E\!\left[
  e^{\,i\lambda\cdot(\beta_t-\beta_s)}
  \mid\mathcal F_s\right]
 =e^{-|\lambda|^2(t-s)/2}.
\]
The conditional characteristic function identifies the increment as a centered normal vector with covariance \((t-s)I\), independent of \(\mathcal F_s\). Iterating in time proves that each finite coordinate vector is standard Brownian motion. Cylinder sets generate the Borel sigma-field of \(\mathscr P_W\); therefore the whole countable field has product Wiener law.

Equation (3.6) and its pathwise uniqueness identify
\[
 X=\mathcal Z_K(\beta).
\]
At an integer time \(m\), testing \(X_m(x)>m/2\) makes an error about \(\eta_x\) with probability at most \(e^{-m/8}\). Borel–Cantelli and the countability of \(W\) show that (3.7) recovers every coordinate of \(\eta\) simultaneously almost surely. Since \(\beta\) has the required input law, this proves the lemma. \(\square\)

### 3.5 Equivariance, kernel parameters, and uniform labels

Use the same fixed total Borel map from \([0,1]\) to continuous Brownian paths at each site. One construction splits binary digits into independent normal variables and uses the dyadic bridge construction on successive unit intervals; on the Borel null set where the construction fails, assign the zero path. It pushes Lebesgue measure to Wiener measure.

The preceding formulas involve only the kernel, its threshold graphs, finite sums, integrals, and pointwise limits. For every bijection \(\theta:W\to W'\), every kernel \(K\), and every input \(u\), they consequently satisfy
\[
 \mathcal S_{\theta K\theta^{-1}}(\theta u)
     =\theta\mathcal S_K(u).
 \tag{3.9}
\]
This is pointwise naturality, not a statement obtained by intersecting almost-sure events over a symmetry group. Joint Borel dependence on \(K,u\) was verified in §3.3 and is retained by (3.7) and the coordinatewise path decoder. In particular, \(\gamma Q\gamma^{-1}=Q\) gives \(\Phi_Q(\gamma u)=\gamma\Phi_Q(u)\) for every input \(u\), proving Theorem A. For the empty index set use the unique empty map. \(\square\)

## 4. Random rooted graphs and the free forest

### 4.1 The definition used here

Let \(\mathcal G_*\) be the standard Borel space of isomorphism classes of locally finite connected simple rooted graphs. Mark spaces are Polish, and the marked spaces carry the Borel structure generated by finite rooted marked balls.

A graph factor is a Borel rule on marked rooted graphs which preserves the graph and gives the same unrooted output when the root is moved. Equivalently, a vertex mark is a Borel function of the graph viewed from that vertex, and an edge mark is a Borel function of the graph viewed from its two endpoints, symmetric in those endpoints [ARS, §2.1]. This is stronger than merely selecting an output for each rooted isomorphism class without requiring compatibility under rerooting.

The iid input consists of one uniform label at each **vertex**, independently conditional on the graph. Unimodularity is not part of this definition. It is a property a random rooted input law may additionally have.

### 4.2 A canonical arc kernel

Let \(\mathcal A(G)\) be the set of directed arcs. Reversal \(R\) interchanges \((v,w)\) and \((w,v)\). In \(\ell^2(\mathcal A(G))\), let
\[
 P^-=\frac{I-R}{2},
\]
and let \(\mathcal C_G\) be the closed span of the antisymmetric flows around all finite cycles. Define
\[
 K_G=P^--P_{\mathcal C_G}.
 \tag{4.1}
\]
Since \(\mathcal C_G\) lies in the antisymmetric subspace, (4.1) is an orthogonal projection. It is defined without orienting the undirected edges.

The matrix entries are jointly Borel in the graph. For a specified arc \(a\), take the span of the cycles contained in the radius-\(n\) ball about its tail. This is finite dimensional; if its cycle vectors form the columns of \(M\), its projection is
\[
 M(M^*M)^+M^*.
\]
Each specified matrix entry is a Borel function of a finite marked ball. The projections increase strongly to \(P_{\mathcal C_G}\), because every finite cycle eventually lies in the ball. Their entrywise limits give \(K_G(a,b)\). The approximation is used separately to compute each entry; the final operator (4.1), not the collection of finite approximations with different centers, is the kernel.

Every graph isomorphism \(\theta\) preserves reversal and cycle flow, and therefore
\[
 K_H(\theta a,\theta b)=K_G(a,b).
 \tag{4.2}
\]
**Lemma 4.1 (Borel implementation on graph fibers) — PROVED.** A jointly Borel natural sampler on fixed countable index sets, applied to the kernels (4.1), defines a Borel output on marked rooted graph isomorphism classes and commutes with rerooting.

Here is an explicit implementation. Use the Borel canonical numbered representative of each *marked rooted* graph from [AL, §2, p. 1461; ARS, §2.1, footnote 2]. AL first recodes marks in Baire space on p. 1459; only Borel measurability of that recoding is needed here. For finite graphs the same choice is obtained by minimizing over finitely many root-preserving numberings. The vertex set is an initial finite subset of \(\mathbb N\), or all of \(\mathbb N\). Adjacency and all retained marks are Borel coordinate functions of the input class. If \(\mathscr B\) denotes this standard Borel space of input classes, its actual arc bundle is the Borel subset
\[
 \mathscr E=\{(b,i,j)\in\mathscr B\times\mathbb N^2:
                      i\sim j\text{ in the representative of }b\}.
 \tag{4.3a}
\]
These fibers contain distinct arc elements, not automorphism orbits of arcs. The finite-cycle formulas above prove that \((b,a,a')\mapsto K_b(a,a')\) is Borel on the fibered square \(\mathscr E\times_{\mathscr B}\mathscr E\).

Fix an ordering of \(\mathbb N^2\) of order type \(\mathbb N\) only for this implementation. The statement “\(a\) is the \(k\)-th arc in the fiber” is Borel: it tests membership and counts members preceding \(a\) in a finite set of codes. Fiber size, finite or infinite, is likewise Borel. On the Borel piece with \(m\) arcs, pull the kernel and its labels back to \(W_m=\{1,\ldots,m\}\); on the infinite piece use \(W_\infty=\mathbb N\). Proposition 3.2 and the Borel decoder give a Borel output in these coordinates. Transport it back and take the rooted marked-graph isomorphism class. This last map is Borel because the preimages of finite marked-ball events are Borel coordinate conditions. The countable partition by fiber size proves measurability of the entire rule.

Any other numbered representative is related by a graph isomorphism, which induces a bijection of the actual arc fibers and transports the labels. Equations (3.9) and (4.2) give identical transported output, for every input. Thus the rule is independent of the temporary enumeration. The same argument applies when the root is changed. In particular, although the canonical representative of a labelled graph may depend on its labels, its output is the intrinsic output computed on any fixed representative before labelling; no independence assumption about labels after canonical renumbering is used. This proves the lemma. \(\square\)

Double-rooted isomorphism classes alone would not supply this bundle: they can identify distinct vertices or arcs in the same automorphism orbit. The implementation above deliberately retains actual elements in a numbered representative until naturality permits descent.

### 4.3 The law and the labels

Choose reference directions for the following calculation only. Let \(Q_G\) be the projection onto the orthogonal complement of the finite-cycle space in the usual undirected-edge Hilbert space. The transfer-current theorem identifies \(\mu_{Q_G}\) with FUSF [BLPS, Theorem 7.8]. Define the isometry
\[
 T\delta_e=\frac{\delta_{e^+}-\delta_{e^-}}{\sqrt2}.
\]
Then \(K_G=TQ_GT^*\). Its two-arc block above one edge has determinant zero. Consequently an arc DPP with kernel \(K_G\) almost surely chooses at most one direction of each edge.

For \(k\) specified undirected edges, each choice of directions has inclusion probability \(2^{-k}\det Q_G[F]\). Summing over the \(2^k\) mutually exclusive choices gives \(\det Q_G[F]\). Thus forgetting directions by
\[
 \pi(\eta)_e=\eta_{e^+}\vee\eta_{e^-}
\]
pushes \(\mu_{K_G}\) to FUSF.

It remains to obtain arc iid labels from vertex iid labels. Split each vertex label into an independent continuous key \(A_v\) and independent slots \(B_{v,0},B_{v,1},\ldots\). Set
\[
 r_v(w)=\#\{z\sim v:A_z<A_w\},\qquad
 Y_{(v,w)}=B_{v,r_v(w)}.
 \tag{4.3}
\]
This is a total Borel natural rule even when keys tie. Almost surely all keys are distinct. Conditional on them, different arcs use different tail-slot pairs, so the arc labels are iid. Local finiteness guarantees finite ranks, and simplicity makes different arcs with one tail have different heads.

The required graph factor is now
\[
 \Phi(G,U)=\pi\bigl(\mathcal S_{K_G}(Y(G,U))\bigr).
 \tag{4.4}
\]
Its three stages are jointly Borel and natural under every graph isomorphism. None uses the root. Conditional on each fixed graph, its law is FUSF. This proves Corollary A1 for every Borel law on \(\mathcal G_*\). The singleton graph has the deterministic empty forest and causes no exception. The same determinant formulas also prove that \(G\mapsto\operatorname{FUSF}_G\) is a Borel probability kernel. \(\square\)

### 4.4 Relation to the question and to other label conventions

Timár's arXiv:2306.15120v2 first defines a factor on a fixed unimodular quasi-transitive graph as a measurable automorphism-equivariant map from iid vertex uniforms to subgraphs. Its next paragraph gives an operational formulation: for every error tolerance, a finite-radius rooted labelled ball predicts the root and its incident-edge statuses with smaller error probability, using only the ball's rooted isomorphism type. It applies this formulation to general unimodular random graphs [Tim, §2].

**Definition comparison — PROVED.** An ARS Borel graph factor implies Timár's root-local approximation. This is the only direction used for Corollary A1. Indeed, finite marked balls generate the input sigma-field, so conditional-expectation approximation recovers the finite root-star output with error tending to zero. Local finiteness suffices even when the root degree is unbounded: first restrict to a degree cutoff of arbitrarily high probability, then approximate its finitely many status coordinates. The conditional converse and the role of compatible marked couplings are stated in Appendix A.2.

Timár's Introduction states the FUSF factor question in full generality. Within the simple-graph convention, the unimodular quantifier range of that question is contained in Corollary A1; our theorem additionally permits arbitrary rooted laws. It is not a claim about an undefined multigraph label convention.

Thus (4.4) covers the unimodular simple-graph range in that question and also arbitrary rooted laws. It establishes a measurable graph factor; it does not assert a finitary coding or a finite number of random bits per vertex. Timár's Theorems 1 and 2(1), and Corollary 5, provide recurrent and invariantly amenable special cases, including stronger finitary conclusions. Angel–Ray–Spinka's Theorem 1.4, restated as Theorem 4.1, concerns WUSF on transient random rooted graphs. None of these distinctions is suppressed by calling (4.4) an FUSF factor.

The vertex-label convention cannot be extended without qualification to multigraphs whose parallel edges are distinct edge elements but carry no identifying marks. Two vertices joined by two such edges give a counterexample: exchanging the edges fixes every vertex input, whereas a uniform spanning tree must choose exactly one edge. This is a **DISPROVED** extension of the statement, not a gap in (4.4).

Similarly, vertex iid and unoriented-edge iid are not equivalent on every finite graph: the sole edge label of \(K_2\) cannot produce two independent nondegenerate vertex labels equivariantly. Our proof needs only the explicit vertex-to-arc conversion (4.3). These small-graph issues do not affect the definition adopted here.

## 5. Fuglede–Kadison comparison on every countable group

The mechanism is a path from the given kernel to a scalar kernel. The determinant remains constant along the path, while every increasing-event probability decreases. The following finite-dimensional calculation supplies that monotonicity.

### 5.1 A finite differential comparison

Let \(0<C<I\) on a finite set \(V\). For \(i\in V\), set
\[
 q_i(A)=\Pr_{\mu_C}(i\in X\mid X\setminus\{i\}=A),\qquad
 \Delta_i f(A)=f(A\cup\{i\})-f(A).
\]
All configurations have positive probability. Writing \(L=C(I-C)^{-1}\), the exact-configuration formula gives
\[
 \frac{q_i(A)}{1-q_i(A)}
 =L_{ii}-L_{iA}L_A^{-1}L_{Ai}
 =\min_{\substack{v_i=1\\\operatorname{supp}v\subseteq A\cup\{i\}}}v^*Lv.
 \tag{5.1}
\]
Increasing \(A\) enlarges the minimization domain. At \(A=V\setminus\{i\}\) the value is \(1/(L^{-1})_{ii}\). Since \(L^{-1}=C^{-1}-I\), it follows that
\[
 q_i(A)\ge\frac1{(C^{-1})_{ii}}.
 \tag{5.2}
\]

For every real function \(f\) on \(2^V\), an exact derivative identity is
\[
 \left.\frac{d}{ds}\mathbb E_{\mu_{C+s(I-rC)}}f\right|_{s=0}
 =\sum_{i\in V}\mathbb E_{\mu_C}
 \left[(1-rq_i(X\setminus\{i\}))\Delta_i f(X\setminus\{i\})\right].
 \tag{5.3}
\]
To verify it, use the basis \(f_B(X)=\mathbf1_{\{B\subseteq X\}}\). The contribution of \(I\) is
\(\sum_{i\in B}\det C[B\setminus\{i\}]\), the derivative of \(\det(C[B]+sI_B)\). The contribution of \(C\) is \(|B|\det C[B]\), the derivative of \(\det((1+s)C[B])\). Conditional expectation replaces \(\mathbf1_{\{i\in X\}}\) by \(q_i(X\setminus\{i\})\), proving (5.3) on the basis and hence for every \(f\).

**Lemma 5.1 (finite differential comparison) — PROVED.** If \(0<C<I\) on a finite set, \(f\) is increasing, and
\[
 r\ge\max_i(C^{-1})_{ii},
 \tag{5.4}
\]
then (5.2) makes every coefficient in (5.3) nonpositive. For increasing \(f\), the derivative is therefore nonpositive. This argument uses complex Hermitian matrices throughout; no real-entry assumption is present.

### 5.2 A constant-determinant path

First suppose \(\varepsilon I\le Q\le(1-\varepsilon)I\), and put \(p=D(Q)\). Define, for \(t\ge0\),
\[
 a_t=\frac{p}{D(Q+tI)},\qquad K_t=a_t(Q+tI).
 \tag{5.5}
\]
Since \(\tau(I)=1\), the normalization is exactly
\[
 D(K_t)=a_tD(Q+tI)=D(Q).
\]
Moreover,
\[
 K_0=Q,\qquad D(K_t)=p,\qquad K_t\longrightarrow pI
 \quad\text{in operator norm as }t\to\infty.
\]
For \(0<\lambda\le1\), the inequality \(\lambda+t\ge(1+t)\lambda\) gives \(a_t\le(1+t)^{-1}\). Thus \(0<K_t<I\). Differentiating the spectral integral gives \(a_t'/a_t=-\tau((Q+tI)^{-1})\). Since \(K_t^{-1}=a_t^{-1}(Q+tI)^{-1}\), differentiating \(a_t(Q+tI)\) yields
\[
 K_t'=a_t(I-r_tK_t),\qquad r_t=\tau(K_t^{-1}).
 \tag{5.6}
\]

For a finite \(V\subset\Gamma\), put \(C_t=K_t[V]\). The inverse-compression inequality is
\[
 C_t^{-1}\le P_VK_t^{-1}P_V.
 \tag{5.7}
\]
Indeed, for \(v\in\ell^2(V)\), the quadratic form of the left side is the supremum of \(2\operatorname{Re}\langle v,z\rangle-\langle K_tz,z\rangle\) over \(z\in\ell^2(V)\); allowing all \(z\in\ell^2(\Gamma)\) gives the right side. Equivariance makes every diagonal entry of \(K_t^{-1}\) equal to \(r_t\). Thus (5.4) holds for \(C_t\).

Applying (5.3) along (5.5), the expectation of every increasing cylinder function decreases with \(t\). Taking \(t\to\infty\) gives
\[
 \operatorname{Ber}(p)^\Gamma\preceq\mu_Q.
 \tag{5.8}
\]
The only group property used here is equality of the inverse-kernel diagonal entries on the regular orbit.

### 5.3 Singular kernels and the upper bound

For arbitrary \(0\le Q\le I\), set \(Q_\epsilon=(Q+\epsilon I)/(1+2\epsilon)\). These kernels have a gap at both endpoints and converge to \(Q\) in norm. Moreover,
\[
 \log D(Q_\epsilon)
 =\int\log(\lambda+\epsilon)\,d\nu_Q(\lambda)-\log(1+2\epsilon)
 \longrightarrow\log D(Q),
\]
also when the limit is \(-\infty\). This follows by monotone convergence for the logarithmic integral after subtracting a common upper bound. Finite cylinder probabilities converge by (2.1), so (5.8) passes to the limit.

The complement of \(\mu_Q\) is \(\mu_{I-Q}\), and complementation reverses stochastic order. Applying (5.8) to \(I-Q\) proves Theorem B and the useful identity
\[
 p_+(Q)=1-p_-(I-Q).
 \tag{5.9}
\]

If \(\ker Q\ne\{0\}\), the spectral projection at zero is nonzero. Faithfulness of the group trace then gives positive spectral mass at zero and \(D(Q)=0\). The converse need not hold: an injective kernel can have divergent negative logarithmic integral. Theorem B gives the trivial lower parameter zero in either case; it does not say that the *best* lower parameter is zero. Section 6 distinguishes those assertions. This completes the proof of Theorem B. \(\square\)

## 6. What optimality means

### 6.1 Finite and amenable groups

If \(|\Gamma|=n<\infty\), equivariance gives \(D(Q)=(\det Q)^{1/n}\). Any domination \(\operatorname{Ber}(p)^\Gamma\preceq\mu_Q\), tested on occupation of the whole group, implies \(p^n\le\det Q\). Together with Theorem B and (5.9), this proves (C1), including singular kernels.

For a countable amenable group, the required determinant approximation is precisely [LiT, Theorem 1.4]: for a positive operator \(g\in M_d(\mathcal N\Gamma)\),
\[
 \det_{\mathcal N\Gamma}(g)
 =\inf_{\varnothing\ne F\subset\Gamma\text{ finite}}
       (\det g[F])^{1/|F|}
 =\lim_F(\det g[F])^{1/|F|},
 \tag{6.1}
\]
where the limit is the net of increasingly left-invariant finite sets, hence holds along every Følner sequence, and the matrix trace in the determinant is unnormalized. Positivity is assumed; invertibility, integral coefficients, and finite generation are not. In particular, the determinant may vanish. We apply (6.1) with \(d=1\) and \(g=Q\). The left/right regular convention is immaterial: the unitary induced by \(x\mapsto x^{-1}\) switches the two representations, preserves the canonical trace, and relabels finite compressions. We use the infimum identity, so this relabelling causes no choice-of-Følner-side issue.

Every finite all-occupied event gives
\[
 p^{|F|}\le\det Q[F]
 \quad\text{if }\operatorname{Ber}(p)^\Gamma\preceq\mu_Q.
\]
Taking the infimum in (6.1) yields \(p\le D(Q)\); Theorem B gives the reverse inequality for the optimal parameter. Equation (5.9) gives the upper parameter. This proves (C1) for all countable amenable groups. In particular, \(D(Q)=0\) forces \(p_-(Q)=0\) in this class.

The lattice predecessor is [LS, Theorem 5.11], which identifies the parameters on \(\mathbb Z^d\) with geometric means of the Fourier multiplier and its complement. Formula (6.1) supplies the corresponding determinant step for arbitrary amenable groups. No entropy or algebraic-action theorem from Li–Thom is needed.

### 6.2 A tree calculation

Let \(T_d\) be the \(d\)-regular tree, \(d\ge3\), with each edge oriented from one bipartition class to the other. On vertices let \(\mathcal A\) be adjacency and \(\Delta=dI-\mathcal A\). Let \(\nabla f(e)=f(\operatorname{head}e)-f(\operatorname{tail}e)\). Then
\[
 \Pi=\nabla\Delta^{-1}\nabla^*
 \tag{6.2}
\]
is the orthogonal projection onto the closed gradient space. Its DPP is WUSF [BLPS, Theorem 7.8]. Here \(\Delta\) is invertible: a weighted Schur estimate with weights \((d-1)^{-\operatorname{dist}(o,v)/2}\) gives \(\|\mathcal A\|\le2\sqrt{d-1}<d\).

Put
\[
 r=\frac1{d-1},\qquad c=\frac{d-1}{d(d-2)}.
\]
The Green kernel is
\[
 \Delta^{-1}(x,y)=c r^{\operatorname{dist}(x,y)}.
 \tag{6.3}
\]
To check this, its columns are square summable, \(dr=1+(d-1)r^2\) verifies the harmonic equation away from \(y\), and \(dc(1-r)=1\) gives the unit mass at \(y\). Consequently \(\Pi(e,e)=2c(1-r)=2/d\).

We first prove
\[
 \operatorname{Ber}(r)^{E(T_d)}\preceq\mu_\Pi.
 \tag{6.4}
\]
This lower domination already appears in [BLPS, §11, p. 48, proof of Theorem 11.1], through Wilson's algorithm. Their regular-tree discussion on p. 46 uses degree \(d+1\) and parameter \(1/d\), which becomes \(1/(d-1)\) with our degree convention. BLPS supplies the lower coupling; the determinant calculation (6.6) below supplies the matching upper restriction and exact threshold. The following projection proof independently verifies the parameter and conditioning needed here.

Enumerate edges in breadth-first order from a root. This order will construct an ordinary sequential coupling; its invariance is neither asserted nor needed for \(p_-\). For a finite set \(S\) of edges, \(\Pi[S]\) is positive definite: a finitely supported flow in the kernel of \(\nabla^*\) on a tree is zero, by successively deleting leaves. Conditioning all edges in \(S\) to be present leaves the projection
\[
 B^S=\Pi-\Pi_{\cdot S}\Pi[S]^{-1}\Pi_{S\cdot}
\]
onto
\(H_S=\{h\in\operatorname{ran}\nabla:h|_S=0\}\), considered on the remaining coordinates. Further conditioning a finite set \(J\) to be absent, whenever the history has positive probability, adds the positive semidefinite term
\[
 B^S_{\cdot J}(I-B^S[J])^{-1}B^S_{J\cdot}.
 \tag{6.5}
\]
Both formulas follow by taking Schur complements in the inclusion/exclusion determinant identities. Positive probability of the absence event makes the displayed inverse well defined.

For the next edge \(e=(u,v)\), with \(v\) farther from the root, take a potential which is zero on the component toward \(u\), and equals \(r^{\operatorname{dist}(v,w)}\) in the forward subtree of \(v\). It is square summable. Its gradient \(h\) vanishes on every preceding edge, has \(|h(e)|=1\), and satisfies
\[
 \|h\|^2
 =1+\sum_{k\ge1}(d-1)^k(1-r)^2r^{2k-2}
 =d-1.
\]
Thus \(h\in H_S\), and the variational formula for a projection diagonal gives \(B^S(e,e)\ge r\). Equation (6.5) shows that every positive-probability history of the preceding edges has next-edge occupation probability at least \(r\). Sampling these conditional probabilities with independent uniforms and using the same uniforms for Bernoulli \(r\) proves (6.4). Zero-probability histories can be assigned arbitrary transitions and do not change either marginal law.

The matching upper restriction on a lower Bernoulli parameter comes from connected edge sets. If \(F\) is a finite connected subtree with \(m\) edges, then
\[
 \det\Pi[F]
 =r^m\left(1+\frac{d-2}{d}m\right).
 \tag{6.6}
\]
Here are the finite algebra details. On its \(m+1\) vertices let \(R_{xy}=r^{\operatorname{dist}(x,y)}\) and let \(D_F\) be the oriented incidence matrix. Then \(\Pi[F]=D_F(cR)D_F^*\). The incidence cofactors of a tree give, for every positive definite vertex matrix \(C\),
\[
 \det(D_FCD_F^*)=\det C\,\mathbf1^*C^{-1}\mathbf1.
\]
Rooting the finite tree, the innovation representation \(Z_v=rZ_{\operatorname{parent}v}+\sqrt{1-r^2}\,\xi_v\), with \(Z_o=\xi_o\), gives
\[
 \det R=(1-r^2)^m,\qquad
 \mathbf1^*R^{-1}\mathbf1=1+\frac{m(1-r)^2}{1-r^2}.
\]
Substituting \(c(1-r^2)=r\) and \((1-r)/(1+r)=(d-2)/d\) proves (6.6). Applying an all-occupied event and letting \(m\to\infty\) in (6.6) shows that a dominated Bernoulli parameter cannot exceed \(r\). Hence
\[
 p_-(\Pi)=\frac1{d-1}.
 \tag{6.7}
\]

The complete star at a vertex contains the gradient of its point mass. This is a nonzero eigenvector with eigenvalue one for the compressed projection. The probability that the star is empty is therefore zero. A product law of parameter \(p<1\) gives that event positive probability, so it cannot dominate \(\mu_\Pi\). Thus
\[
 p_+(\Pi)=1.
 \tag{6.8}
\]

### 6.3 A regular group action meeting the conjecture's premises

Take \(\Gamma=\langle a,b:a^3=b^3=e\rangle=C_3*C_3\). Its Bass–Serre tree has vertex classes \(\Gamma/\langle a\rangle\) and \(\Gamma/\langle b\rangle\), and an edge indexed by \(g\) joins \(g\langle a\rangle\) to \(g\langle b\rangle\). Reduced normal forms for a free product show that this is a connected three-regular tree. Left translation is free and transitive on edges and preserves the orientation between the two classes. Therefore (6.2), on edges, belongs to \(R(\Gamma)\) for a single regular orbit.

The group is sofic: finite groups are sofic, and the free-product case of [ES, Theorem 1] preserves soficity. Thus this example also satisfies the sofic context of the ICM conjecture; it is not exploiting the subsequent removal of that hypothesis.

The trace of \(\Pi\) is \(2/3\). Since \(\Pi\) is a projection, its spectral distribution is \(\frac13\delta_0+\frac23\delta_1\). Consequently
\[
 D(\Pi)=0<\frac12=p_-(\Pi),\qquad
 p_+(I-\Pi)=\frac12<1=1-D(\Pi).
 \tag{6.9}
\]
The lower and upper pointwise assertions are disproved by \(\Pi\) and its complement, respectively.

This failure survives removal of both spectral endpoints. Set
\[
 \widehat Q=\frac{I+63\Pi}{128}.
\]
For any DPP kernel \(K\), union with an independent Bernoulli field of parameter \(q\) changes the kernel to \(qI+(1-q)K\): this follows by applying independent thinning to the complement. Independent thinning with retention \(s\) then multiplies the kernel by \(s\). Both operations preserve an existing coordinatewise inclusion coupling. Starting with (6.4), taking \(q=1/64\) and \(s=1/2\), gives
\[
 p_-(\widehat Q)\ge\frac{65}{256},\qquad
 D(\widehat Q)=\left(\frac1{128}\right)^{1/3}
               \left(\frac12\right)^{2/3}=\frac18.
 \tag{6.10}
\]
The complement yields a strict upper-bound counterexample as well. Appendix B replaces \(\widehat Q\) by one explicit finite-support group-algebra kernel while preserving the gap. This proves all the counterexample assertions in Theorem C. \(\square\)

### 6.4 Quantifiers and the remaining classification problem

There are three distinct readings of “these bounds are optimal.”

1. **For each fixed kernel:** the two displayed parameters equal \(p_-(Q)\) and \(p_+(Q)\). This is **PROVED** for finite and amenable groups and **DISPROVED** for general groups, even within the sofic finite-support class.
2. **Uniform sharpness using one determinant datum:** no larger universal lower function of \(D(Q)\) alone, or smaller universal upper function of \(D(I-Q)\) alone, works throughout the operator class. This is **PROVED** for every group by \(Q=pI\), which realizes every determinant value and is itself a product kernel.
3. **Best possible joint use of both determinant data:** determine the sharp region of possible thresholds when both \(D(Q)\) and \(D(I-Q)\) are prescribed. This stronger uniform optimization problem is **INCOMPLETE** here. The scalar examples only cover the line \((p,1-p)\) and do not solve it.

The fixed-kernel reading is the more informative reading in context: [ICM, Conjecture 5.7] follows the exact geometric-mean statements of [LS, Theorem 5.11]. This is an interpretation of the mathematical context, not a claim to know the author's intention. The conjecture's wording by itself does not formally choose between the first two readings.

Some further group classes are covered by inheritance. If \(H\le\Gamma\), place an \(H\)-kernel on each left coset and set cross-coset entries to zero. This defines a kernel in \(R(\Gamma)\), with the same spectral distribution at the identity. Its DPP is a product of coset processes. Restriction to one coset and independent products of couplings show that \(D\), \(p_-\), and \(p_+\) are unchanged. Finite support is also preserved. Hence every countable group containing \(C_3*C_3\) admits the counterexamples above, regardless of whether that larger group is known to be sofic.

For orientation, define
\[
 \delta(Q)=\inf_{\varnothing\ne F\subset\Gamma\text{ finite}}
                 (\det Q[F])^{1/|F|}.
\]
All-occupied events and Theorem B give \(D(Q)\le p_-(Q)\le\delta(Q)\). Amenability identifies the two outer quantities through (6.1). Without amenability that identification can fail, and testing all-occupied events alone need not determine stochastic order on all increasing events. A classification of groups for which every kernel has pointwise sharp FK bounds, and a classification of individual kernels outside the amenable case, remain **INCOMPLETE** in this manuscript.

## 7. The sharp trace-norm bound on sofic groups

The argument has two inputs: invariant monotone couplings for ordered kernels, and a polygon lying inside the positive-contraction interval. The interpolation itself is elementary and does not assume that its endpoints commute.

### 7.1 The precise ordered-coupling input

[LT, Theorem 5.1] assumes a sofic group with a **finite generating set**, and gives an invariant monotone coupling whenever \(0\le C\le D\le I\) in \(R(\Gamma)\), or in the corresponding finite-type algebra. We use its regular-action conclusion. Its extension to countable sofic groups requires the following argument.

Write \(\Gamma=\bigcup_n H_n\) with increasing finitely generated subgroups. Each \(H_n\) is sofic: the finite-set approximate multiplicativity and separation conditions defining soficity restrict from \(\Gamma\) to any finite subset of \(H_n\). Take the principal compressions of \(C,D\) to \(\ell^2(H_n)\). They remain \(H_n\)-equivariant ordered positive contractions, so [LT, Theorem 5.1] gives an \(H_n\)-invariant monotone joining \(\lambda_n\). Independently copy this joining on every left coset of \(H_n\). Its law is independent of the choice of coset representatives because \(\lambda_n\) is \(H_n\)-invariant. Left translation permutes the blocks and acts inside each by an element of \(H_n\), so the resulting joining \(\widehat\lambda_n\) is \(\Gamma\)-invariant and monotone.

Its marginals have kernels
\[
 C_n(x,y)=C(x,y)\mathbf1_{\{x^{-1}y\in H_n\}},\qquad
 D_n(x,y)=D(x,y)\mathbf1_{\{x^{-1}y\in H_n\}}.
\]
For any finite \(F\subset\Gamma\), these agree with \(C,D\) on \(F\times F\) once \(F^{-1}F\subset H_n\). Hence their DPPs converge weakly to the desired marginals. Compactness of probability measures on the countable binary product gives a subsequential limit of \(\widehat\lambda_n\). Invariance and coordinatewise order are closed conditions, so the limit is the required invariant monotone joining.

For such an ordered pair, every monotone joining has mismatch probability \(\tau(D-C)\) at the identity. Every joining has mismatch probability at least the difference of the one-site means. Therefore
\[
 \bar d_\Gamma(\mu_C,\mu_D)=\tau(D-C)
 \quad\text{when }0\le C\le D\le I.
 \tag{7.1}
\]
This is the ordered equality recorded in [LT, Lemma 7.2], with the countable-group extension now justified.

We also use the triangle inequality for \(\bar d_\Gamma\). Given two invariant joinings sharing a middle marginal, condition on the middle coordinate and join the two outer coordinates independently. Uniqueness of conditional laws makes this joining invariant; since \(\Gamma\) is countable the necessary null sets can be removed simultaneously. The pointwise triangle inequality for the mismatch indicator proves the desired bound. Alternatively, this is the relatively independent joining argument on [LT, pp. 593–594]. The infimum defining \(\bar d\) is attained, since invariant joinings form a nonempty compact set and the one-site mismatch is continuous.

### 7.2 A polygon inside the contraction interval

Put \(T=B-A=T_+-T_-\), where \(T_+,T_-\ge0\) and \(T_++T_-=|T|\). As \(-I\le T\le I\), both positive parts are contractions. For an integer \(N\ge1\), define
\[
 R_k=\frac{(N-k)A+kB}{N+1},\quad 0\le k\le N,
 \qquad
 S_k=R_k+\frac{T_+}{N+1},\quad 0\le k<N.
 \tag{7.2}
\]
We have \(0\le R_k\le NI/(N+1)\) and \(0\le S_k\le I\). Moreover,
\[
 S_k-R_k=\frac{T_+}{N+1},\qquad
 S_k-R_{k+1}=\frac{T_-}{N+1}.
\]
Thus the route
\[
 A,\ R_0,\ S_0,\ R_1,\ S_1,\ldots,\ S_{N-1},\ R_N,\ B
\]
has ordered consecutive pairs and stays entirely within the allowed operator interval. Equation (7.1) and the triangle inequality give
\[
 \bar d_\Gamma(\mu_A,\mu_B)
 \le\frac{\tau(A)+\tau(B)+N\tau|A-B|}{N+1}.
 \tag{7.3}
\]
Letting \(N\to\infty\) proves (D). No continuity assertion for \(\bar d\) is needed: (7.3) is a numerical upper bound for the same two marginals for every \(N\). Taking \(A=0\) and \(B=pI\), \(0<p\le1\), proves that the coefficient one cannot be decreased. \(\square\)

The scaling in (7.2) is essential to this proof. The tempting common upper bound \(A+(B-A)_+\) need not be a contraction. For example, with
\[
 A=\frac1{25}\begin{pmatrix}16&12\\12&9\end{pmatrix},\qquad
 B=\frac1{25}\begin{pmatrix}9&12\\12&16\end{pmatrix},
\]
both matrices are projections, while \(A+(B-A)_+\) has eigenvalue \(28/25\).

### 7.3 Relation to the existing bounds

The trace-norm question occurs in [LT, p. 595, immediately after Lemma 7.8], not as Question 7.7. Question 7.7 is the factor question answered by Theorem A. [LT, Lemma 7.9] supplies the weaker noncommutative bound \(6\,3^{2/3}\|A-B\|_1^{1/3}\); the surrounding text records the linear bound for commuting kernels. The commutative lattice predecessor is [LS, Proposition 3.4]. These precedents and the unpublished polygonal source are recorded separately in the source register.

For finite index sets, the same polygon and ordinary finite DPP order [LT, Theorem 2.1] prove
\[
 W_H(\mu_A,\mu_B)\le\operatorname{Tr}|A-B|,
 \tag{7.4}
\]
where \(W_H\) minimizes expected total Hamming distance over all couplings. For an ordered pair its value is \(\operatorname{Tr}(B-A)\), so the proof is identical with the unnormalized trace. On a finite group, averaging a coupling over the group preserves its cost and gives an invariant coupling; consequently \(\bar d=W_H/|\Gamma|\).

No arbitrary-group version of (D) is asserted here. The proof still needs invariant monotone couplings for ordered kernels. The sampling and ordinary-domination arguments in §§3 and 5 do not supply that input. Its availability for every countable group is **INCOMPLETE** in this manuscript.

## Appendix A. Two definition boundaries

### A.1 Why the source index set cannot be silently changed

Let \(\Gamma\) be infinite, let \(W\) be a singleton with the trivial action, and take \(Q=[p]\), \(0<p<1\). The target is a nondegenerate Bernoulli random variable with trivial action. The \(W\)-indexed product source supplies it directly, as Theorem A requires. It cannot be a factor of a regular iid shift \(A^\Gamma\): the latter is ergodic, while an equivariant map to this target would give an invariant event of probability \(p\).

For completeness, ergodicity follows by approximating an invariant event by events depending on finitely many coordinates and translating those coordinates off themselves. Such a translation exists for every finite set in an infinite group. Independence of the separated cylinder events and passage to the approximation limit give \(p=p^2\). This example has stabilizer \(\Gamma\) and **DISPROVES** the unrestricted replacement of \(W\) by \(\Gamma\). It does not challenge the original \(A^W\) convention in [LT].

### A.2 Borel factors and local approximation

Under the graph-factor definition used in §4, a Borel output at the root is approximable in probability by functions of finite labelled balls. Conversely, a single compatible system of local approximants whose errors tend to zero determines a Borel root output after an almost-sure subsequence. To obtain a graph factor, the outputs at different roots must agree as one marked graph. In a jointly unimodular coupling of the input and output, root-null discrepancies propagate to a null set at every vertex by the mass-transport principle: for each radius, send mass from every vertex to all bad vertices within that radius. The reverse implication is therefore valid for the compatible, jointly unimodular formulation. Taking the union over radii and using connectedness makes the agreement simultaneous. Our construction already has this stronger compatibility pointwise and does not need unimodularity for it.

One must not weaken that formulation to “the root output is locally predictable in an arbitrary coupling.” On \((\mathbb Z,0)\), with iid labels \(U\), define
\[
 M_v=\mathbf1_{\{U_0<1/2\}}\mathbin{\mathrm{xor}}(v\bmod2).
\]
The marginal law of \(M\) is the uniform proper two-colouring and the root colour is determined by its label. Nevertheless this colouring is not an iid factor: translation by two acts trivially on the two-colouring space, whereas the iid shift restricted to even translations is ergodic. The joint coupling \((U,M)\) above is not rerooting invariant. This is a **DISPROVED** equivalence for an artificially weakened definition, not an attribution of that definition to Timár. The forward implication needed to answer the FUSF question is unconditional and was proved in §4.4.

## Appendix B. A specified finite-support counterexample

Keep the three-regular tree and \(\Gamma=C_3*C_3\). Let \(\rho=2\sqrt2/3<19/20\), set \(N=255\), and define
\[
 p_N(\Delta)=\frac13\sum_{k=0}^{N}(\mathcal A/3)^k,\qquad
 P_N=\nabla p_N(\Delta)\nabla^*,\qquad
 Q_N=\frac{I+63P_N}{128}.
 \tag{B.1}
\]
These are real self-adjoint finite-propagation operators. The fixed bipartite orientation intertwines the group action, so their edge kernels commute with the regular action. Finite propagation on this locally finite tree makes their support in the regular edge orbit finite. Thus \(Q_N\in\mathbb C\Gamma\).

Writing \(U=\mathcal A/3\), the geometric-series remainder is
\[
 \Delta^{-1}-p_N(\Delta)
 =\frac13\,U^{N+1}(I-U)^{-1},\qquad
 \|\Delta^{-1}-p_N(\Delta)\|
 \le\frac{\rho^{N+1}}{3(1-\rho)}.
\]
Together with \(\|\nabla\|^2=\|\Delta\|<6\), this gives
\[
 \epsilon:=\|Q_N-\widehat Q\|
 <\frac{63}{128}\,6\,\frac{\rho^{256}}{3(1-\rho)}
 <20(19/20)^{256}<\frac1{1024}.
 \tag{B.2}
\]
The last estimate has the following short exact verification. The binomial theorem gives
\[
 (20/19)^{16}=(1+1/19)^{16}
 >1+16/19+120/19^2=785/361>2.
\]
Hence \((19/20)^{256}<2^{-16}\), and \(20\cdot2^{-16}<2^{-10}=1/1024\), since \(20<64\). Also \(2\sqrt2/3<19/20\) follows by squaring: \(3200<3249\). Thus (B.2) is a paper proof, with the script providing an independent arithmetic check. It follows that
\[
 \frac7{1024}I<Q_N<\left(\frac12+\frac1{1024}\right)I<I.
\]
In particular this specified finite-support operator satisfies every positivity and contraction premise.

Let \(L=(1/128-\epsilon)I+(63/128)\Pi\). Then \(L\le Q_N\). More generally, for \(a,b\ge0\) and \(a+b\le1\), union with Bernoulli \(a/(a+b)\), followed by thinning with retention \(a+b\), transforms \(\mu_\Pi\) to \(\mu_{aI+b\Pi}\). Applied to its dominated Bernoulli \(1/2\), it proves \(p_-(aI+b\Pi)\ge a+b/2\). Finite DPP order and countable compression therefore give
\[
 p_-(Q_N)\ge p_-(L)\ge\frac{65}{256}-\epsilon
 >\frac{259}{1024}.
 \tag{B.3}
\]

Both \(Q_N\) and \(\widehat Q\) are bounded below by \(mI\), with \(m=7/1024\). The integral representation of the logarithm and the resolvent identity give
\[
 \|\log Q_N-\log\widehat Q\|
 \le\epsilon\int_0^\infty(m+t)^{-2}\,dt
 =\epsilon/m<1/7.
\]
Consequently
\[
 D(Q_N)<\frac{e^{1/7}}8<\frac7{48}<\frac{259}{1024}<p_-(Q_N).
 \tag{B.4}
\]
For the middle estimate, \(\log(7/6)=\int_1^{7/6}x^{-1}\,dx>1/7\). This proves a strict gap with exact constants, rather than only an unspecified sufficiently large polynomial approximation. The complement \(I-Q_N\) supplies a finite-support strict upper-bound counterexample.

## Appendix C. Finite-type kernels and the determinant normalization

Let \(W=\Gamma\times S\), with \(m=|S|\ge1\). The commutant is \(M_m(R(\Gamma))\); the finite-support group-algebra matrices \(M_m(\mathbb C\Gamma)\) form a subclass, not the whole algebra. Use the unnormalized matrix trace
\[
 \tau_S(T)=\sum_{s\in S}\langle T\delta_{(e,s)},\delta_{(e,s)}\rangle,
 \qquad \tau_S(I)=m,
 \qquad \Delta_S(Q)=\exp\tau_S(\log Q).
\]

**PROVED.** For every countable group and every such positive contraction,
\[
 \operatorname{Ber}(\Delta_S(Q))^W\preceq\mu_Q
 \preceq\operatorname{Ber}(1-\Delta_S(I-Q))^W.
 \tag{C.1}
\]
To prove this, first assume a gap at both endpoints and write \(p=\Delta_S(Q)\). Replace (5.5) by
\[
 a_t=\frac{(1+t)^{m-1}p}{\Delta_S(Q+tI)},\qquad K_t=a_t(Q+tI).
\]
Then \(K_0=Q\), \(K_t\to pI\), and \(a_t\le(1+t)^{-1}\) by the same spectral inequality, now traced with mass \(m\). Let
\[
 h_s(t)=\langle(Q+tI)^{-1}\delta_{(e,s)},\delta_{(e,s)}\rangle.
\]
Each \(h_s(t)\ge(1+t)^{-1}\), and differentiation gives
\[
 K_t'=a_t(I-r_tK_t),\qquad
 r_t=\frac{\sum_s h_s(t)-(m-1)/(1+t)}{a_t}
 \ge\max_s\frac{h_s(t)}{a_t}.
 \tag{C.2}
\]
These are exactly the bounds on every orbit's inverse-kernel diagonal needed in (5.4) after inverse compression. The proof of §5 now applies. Regularization handles singular kernels, and complementation gives the upper bound.

The corresponding **normalized** determinant \(\Delta_S(Q)^{1/m}\) cannot replace \(\Delta_S(Q)\) in (C.1). This extension is **DISPROVED** even for the trivial group and \(Q=\operatorname{diag}(1/4,3/4)\). The process has independent unequal coordinates, whose best homogeneous parameters are \(1/4\) and \(3/4\), whereas the proposed normalized parameters are \(\sqrt3/4\) and \(1-\sqrt3/4\).

Nor is (C.1) generally pointwise sharp on amenable groups when \(m>1\). Applying [LiT, Theorem 1.4] to \(F\times S\) gives only
\[
 \Delta_S(Q)\le p_-(Q)\le\Delta_S(Q)^{1/m},\qquad
 1-\Delta_S(I-Q)^{1/m}\le p_+(Q)\le1-\Delta_S(I-Q).
 \tag{C.3}
\]
Here \(p_\pm\) refer to a single common parameter on all types. For example, \(Q=pI_W\) has \(p_-(Q)=p\), while \(\Delta_S(Q)=p^m\). Nevertheless the one-datum uniform bounds in (C.1) are sharp: \(\operatorname{diag}(p,1,\ldots,1)\) realizes lower threshold \(p=\Delta_S(Q)\), and \(\operatorname{diag}(p,0,\ldots,0)\) realizes upper threshold \(p=1-\Delta_S(I-Q)\). These examples work on every group.

Finally, Theorem A applies on this very index set \(\Gamma\times S\), which is a regular Bernoulli source with base \([0,1]^S\). Thus neither the factor assertion nor the trace convention requires identifying the type coordinates or assuming real matrix entries.

## References

[AL] David Aldous and Russell Lyons. *Processes on Unimodular Random Networks*. Electronic Journal of Probability **12** (2007), 1454–1508. [Published PDF](https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/463/463-1495-1-PB.pdf).

[ARS] Omer Angel, Gourab Ray and Yinon Spinka. *Uniform even subgraphs and graphical representations of Ising as factors of i.i.d.* Electronic Journal of Probability **29** (2024), paper 39. [Published PDF](https://dspace.library.uvic.ca/server/api/core/bitstreams/ec346c4f-76f7-4bb3-b54e-b95505de66de/content).

[BLPS] Itai Benjamini, Russell Lyons, Yuval Peres and Oded Schramm. *Uniform Spanning Forests*. Annals of Probability **29** (2001), 1–65. [Author PDF](https://rdlyons.pages.iu.edu/pdf/usf.pdf).

[ES] Gábor Elek and Endre Szabó. *Sofic representations of amenable groups*. Proceedings of the American Mathematical Society **139** (2011), 4285–4291. [Published PDF](https://www.ams.org/proc/2011-139-12/S0002-9939-2011-11222-X/S0002-9939-2011-11222-X.pdf).

[ICM] Russell Lyons. *Determinantal probability: basic properties and conjectures*. Proceedings of the ICM 2014, Vol. IV, 137–161. [Published author PDF](https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf).

[LiT] Hanfeng Li and Andreas Thom. *Entropy, Determinants, and \(L^2\)-Torsion*. Journal of the American Mathematical Society **27** (2014), 239–292. [Original preprint](https://arxiv.org/pdf/1202.1213).

[LS] Russell Lyons and Jeffrey E. Steif. *Stationary determinantal processes: phase multiplicity, Bernoullicity, entropy, and domination*. Duke Mathematical Journal **120** (2003), 515–575. [Author PDF](https://rdlyons.pages.iu.edu/pdf/dyn.pdf).

[LT] Russell Lyons and Andreas Thom. *Invariant coupling of determinantal measures on sofic groups*. Ergodic Theory and Dynamical Systems **36** (2016), 574–607. [Published author PDF](https://rdlyons.pages.iu.edu/pdf/couple-pub.pdf).

[Tim] Ádám Timár. *Factor of iid's through stochastic domination*. arXiv:2306.15120v2, 2025. [Versioned PDF](https://arxiv.org/pdf/2306.15120v2).

## Supplementary verification

Exact source premises, candidate antecedents, and search limits are recorded in [sources01.md](sources01.md).

The exact calculations in [check01.py](../t2/check01.py) check finite tree minors, conditional probabilities, and the explicit rational tail estimate in Appendix B. [mcheck.py](../t2/mcheck.py) checks the finite differential comparison on a complex Hermitian two-type example. These finite computations supplement the proofs; they do not certify the infinite-dimensional arguments. No formal proof-assistant verification or novelty claim is made.
