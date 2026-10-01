# Relative transition candidates and limits of coupling upgrades

The unrestricted exact joint-iid target remains INCOMPLETE. This is a partial mathematical text. Its displayed auxiliary claims are awaiting a scoped independent audit; no whole-manuscript approval is attached.

**INCOMPLETE for the unrestricted joint-iid target.** The missing step is an exactly order-preserving **pair** construction for arbitrary \(A\le B\), not individual marginal sampling.

Below are a proved relative transition, its quantitative consequences, a restricted positive theorem, and explicit obstructions. None of the obstructions disproves the existential target.

Write
\[
\tau(K)=\langle K\delta_e,\delta_e\rangle,\qquad
\mathcal C=C_r^*(\Gamma)
\]
in the right regular representation. All kernels are complex Hermitian, all actions are regular, and all choices concern fixed kernels.

## 1. A prescribed invariant ordered joining need not be an iid factor

On \(\mathbb Z\), encode ordered pairs by colors
\[
0=(0,0),\qquad1=(0,1),\qquad2=(1,1).
\]
Let \(\pi\) be uniform on these colors and set
\[
Q=\frac1{36}
\begin{pmatrix}
4&5&3\\
5&2&5\\
3&5&4
\end{pmatrix}.
\]
Let \(\lambda_0\) consist of independent \(Q\)-pairs on \((2k,2k+1)\), let \(\lambda_1\) use \((2k+1,2k+2)\), and put
\(\lambda=(\lambda_0+\lambda_1)/2\).

Rows and columns sum to \(1/3\), and \(Q_{00}=Q_{22}=1/9\). Both binary projections are therefore iid, giving, for every finite \(F\),
\[
\mathbb P(F\subseteq X)=3^{-|F|},\qquad
\mathbb P(F\subseteq Y)=(2/3)^{|F|}.
\]
These identify \(\mu_{I/3}\) and \(\mu_{2I/3}\). Containment is automatic, and the shift \(T\) exchanges the components, making \(\lambda\) invariant.

Set
\[
\phi(a,b)=\mathbf1\{\text{exactly one of }a,b\text{ equals }1\}.
\]
Its expectations under \(Q\) and \(\pi\otimes\pi\) are \(5/9\) and \(4/9\). Even-edge averages converge to these respective values under \(\lambda_0,\lambda_1\): for the latter, split the one-dependent sequence into two iid parity subsequences. Odd-edge averages reverse the limits. Thus the configuration determines a mean-zero phase \(H=\pm1\), invariant under \(T^2\) and reversed by \(T\). Each component is \(T^2\)-ergodic, so their exchange makes \(\lambda\) \(T\)-ergodic, but not \(T^2\)-ergodic.

Join \(Z\sim\lambda\) and \(W\sim\nu\) stationarily, where \(\nu\) is \(T^2\)-ergodic. The conditional laws of \(W\) given \(H=\pm1\) are \(T^2\)-invariant and have densities at most two relative to \(\nu\). Ergodicity makes both densities constant. Hence \(W\) is independent of \(H\), and
\[
\frac1{18}
=\left|\mathbb E H\,[\phi(Z_0,Z_1)-\phi(W_0,W_1)]\right|
\le 2\mathbb P(Z_0\ne W_0).
\]
Therefore
\[
\boxed{\bar d(\lambda,\nu)\ge 1/36.}
\]

Every iid factor is \(T^2\)-ergodic, since the iid source, grouped into consecutive pairs, is a Bernoulli shift. Thus \(\lambda\) is not an iid factor. In particular, no equivariant conditional map \(Y=\Psi(X,U)\), with \(X\) iid Bernoulli \(1/3\) and \(U\) independent regular iid, can realize this prescribed joining.

Nevertheless, \(\lambda\) is a weak limit of ordered iid factors with these **same exact marginals**. Use iid Bernoulli \(p\) markers. Between consecutive markers, pair vertices from left to right, leaving a final singleton when necessary. Sample independent \(Q\)-pairs and \(\pi\)-singletons. Conditional on this equivariant partition, both binary marginals remain iid. The invariant null event lacking markers in either direction receives constant color zero.

No markers in \([-r-1,r+1]\) leaves \([-r,r]\) in one uninterrupted pairing. The preceding-marker distance is geometric, with parity bias \(p/[2(2-p)]\). Consequently,
\[
\|\lambda_p|_{[-r,r]}-\lambda|_{[-r,r]}\|_{\rm TV}
\le (2r+3)p+\frac{p}{2(2-p)}
\longrightarrow0.
\]
Every \(\lambda_p\) is still at \(\bar d\)-distance at least \(1/36\) from \(\lambda\). Common-input realizations cannot be Cauchy in root probability: a summably Cauchy subsequence would stabilize by Borel–Cantelli to an iid factor with law \(\lambda\).

This does **not** refute the target: common uniform thresholds monotonically couple the same scalar kernels. Cyclic-coset copies extend the obstruction to groups containing an infinite-order element, including free groups. The general failure of weak closure is already known; the additional features here are the fixed scalar DPP marginals and explicit quantitative separation. 

## 2. The finite-support relative transition is proved

**Theorem R.** Suppose
\[
K_t=C+tTT^*,\qquad
\epsilon I\le K_t\le(1-\epsilon)I\quad(0\le t\le1),
\]
where \(C,T\) commute with left translation and \(v=T\delta_e\) has finite support \(S\). Given \(X\sim\mu_C\) and independent regular iid clocks, a total Borel equivariant pure-birth map produces \(X_t\sim\mu_{K_t}\). Exceptional inputs receive the constant initial path. Neither H nor L is assumed.

The external determinantal input is finite Hermitian DPP stochastic domination under operator order, supplied by Lyons’ Theorem 2.9. 

### Conditional kernels and invariant mean sensitivity

For every configuration \(x\), define
\[
G_x=(K-P_{x^c})^{-1}.
\]
With \(J_x=2P_x-I\),
\[
K-P_{x^c}
=\tfrac12J_x[I+J_x(2K-I)],
\qquad \|G_x\|\le\epsilon^{-1}.
\]
The uniformly geometric Neumann series makes \(G_xw\) continuous in \((t,x)\) for each fixed \(w\).

For finite \(F\), the all-boundary conditional kernel is
\[
N_F(x)=K_F-
K_{F,F^c}(K_{F^c}-P_{x^c\cap F^c})^{-1}K_{F^c,F}.
\]
It lies between \(\epsilon I\) and \((1-\epsilon)I\), and decreases in operator order when exterior occupied coordinates are added. Finite conditioning proves this by Schur complements: conditioning on occupation subtracts \(kk^*/p\); conditioning on vacancy adds \(kk^*/(1-p)\). The bounds on \(K\) and \(I-K\) preserve the gap.

The finite-conditioning formulas converge uniformly on fixed vectors: finite Neumann products have compact vector images as \((t,x)\) varies, finite-coordinate projections converge uniformly on those images, and the remaining tails are uniformly geometric. Martingale convergence then identifies the full conditional law as \(\mu_{N_F(x)}\).

For an exterior flip \(j\), block inversion and Sherman–Morrison give
\[
\left|\operatorname{tr}\bigl(N_F(x^j)-N_F(x)\bigr)\right|
\le \epsilon^{-1}\sum_{s\in F}|G_x(s,j)|^2. \tag{1}
\]
Indeed, the Schur vector is
\[
-(N_F-P_{x^c\cap F})G_{F,j},
\]
whose first factor has norm at most one. The scalar denominator has inverse absolute value at most \(\epsilon^{-1}\): its conditional probability belongs to \([\epsilon,1-\epsilon]\).

Summing (1) over blocks \(gS\), indexed with multiplicity by \(g\), gives a column bound \(|S|\epsilon^{-3}\). For fixed \(F\), the row tails vanish uniformly, because
\(\{G_{t,x}\delta_s\}_{t,x}\) is compact in \(\ell^2\).

Now let \(L\le U\) have any invariant joint law and write
\(d=\mathbb P(L_e\ne U_e)\). Change their disagreements at independent rate-one exponential times. Uniform row tails justify the integrated flip-generator identity by finite-set approximation. Mass transport transfers the sum over flipped coordinates to the column sum at the root. Its expected contribution at interpolation time \(r\) is at most
\(|S|\epsilon^{-3}de^{-r}\). Integrating yields
\[
\mathbb E\operatorname{tr}\bigl(N_S(L)-N_S(U)\bigr)
\le |S|\epsilon^{-3}d. \tag{2}
\]
Crucially, the column bound is evaluated at one common configuration, not by summing separate worst-case influences.

### Positive finite flows

For a gapped finite matrix \(N\), let \(p_N\) be its DPP point probabilities and
\[
b_N=\left.\partial_h p_{N+hvv^*}\right|_{h=0}.
\]
Finite stochastic domination puts \(b_N\) in the cone generated by upward Boolean-cube edge incidences.

This cone admits a Lipschitz positive-flow selection. Intersect it with
\[
m(b)=\sum_\eta|\eta|b(\eta)=1.
\]
The section is the finite convex hull of the edge columns. Triangulate it, choose feasible flows at its vertices, extend affinely on each simplex and homogeneously along rays, and assign zero at the origin. The resulting flow \(q_N\) has divergence \(b_N\) and total mass \(\|v\|^2\). Since successive conditioning gives
\(p_N(\eta)\ge\epsilon^{|S|}\), rates
\[
q_N(\eta,i)/p_N(\eta)
\]
are bounded and Lipschitz in \(N\).

Apply these conditional flows on every \(gS\) and sum the finitely many contributions at each site. The intrinsic rates \(a_i(t,x)\), defined with \(x_i=0\), are bounded, continuous, and equivariant. Write \(a_i^-,a_i^+\) for their infimum and supremum over \([L,U]\).

Local-pattern disagreements and (2) imply, for a finite constant \(c\),
\[
\mathbb E(a_e^+-a_e^-)
\le c\,\mathbb P(L_e\ne U_e). \tag{3}
\]
For the conditional-kernel term, all kernels lie between the endpoint kernels. The needed matrix estimate is
\(-D\le E\le D\Rightarrow\|E\|_1\le\operatorname{tr}D\), obtained by applying the two inequalities on the positive and negative spectral subspaces of \(E\).

### Common-clock construction and identification

Use sitewise Poisson marks \((t,z)\) of intensity \(dt\,dz\), with \(0\le z\le M\), where \(M\) bounds the rates. Start with the constant lower path and the upper path accepting its first clock. Iteratively let the lower path accept the first mark below the infimum over the preceding interval, and the upper accept the first mark at most its supremum.

The intervals are nested. Finite clock lists make each site’s entire envelope paths stabilize. Compactness passes extrema to the limiting box; predictable thresholds almost surely do not equal a clock mark. The limits satisfy their clock equations.

A discrepancy can first arise only at a mark between the thresholds. The Poisson compensator and (3) give
\[
d(t)\le c\int_0^t d(s)\,ds.
\]
Gronwall gives coalescence. Every **relaxed solution** on the same clocks is trapped between all envelope iterates, even without invariance or adaptation: it starts at the given configuration, changes only by births at its own clocks, accepts strictly sub-threshold marks, rejects strictly super-threshold marks, and may choose either action at equality.

For marginal identification, adding \(h v_gv_g^*\) fixes its exterior law and changes its conditional kernel by that rank-one matrix. The flow-divergence identity therefore applies. Summing the finitely many blocks meeting a cylinder gives
\[
\partial_t\mu_{K_t}(f)=\mu_{K_t}(\mathcal L_t f). \tag{4}
\]
A formal forward equation alone is not enough. For finite \(\Lambda\), define
\[
\widehat a_i^\Lambda(t,\eta)
=\mathbb E_{\mu_{K_t}}
 [a_i(t,X)\mid X_\Lambda=\eta],
\qquad \eta_i=0.
\]
All conditioning events have positive probability. Equation (4) is the exact finite forward equation, so its finite chain has marginal \(\mu_{K_t}|_\Lambda\).

Run these chains on the **same** initial configuration and site clocks, freezing exterior sites. Uniform continuity gives
\(\widehat a_i^\Lambda\to a_i\) uniformly on matching inputs. Finite clock lists give every subsequence a coordinatewise, whole-path convergent subsubsequence. Its limit is a relaxed solution, hence the envelope path. Thus the full sequence converges on the common input, and
\[
\mathbb P(F\subseteq X_t)
=\lim_\Lambda\mathbb P(F\subseteq X_t^\Lambda)
=\det((K_t)_F).
\]
Inclusion–exclusion identifies every marginal.

The good-input set is Borel and invariant. Outside it, return the initial constant path. Exhaustions only verify the map; they do not order its updates.

## 3. Quantitative interfaces and actual common-input limits

### Finite-range approximation

Let \(\omega_m\) be the uniform rate oscillation for configurations agreeing on finite relative neighborhoods \(W_m\uparrow\Gamma\). Then \(\omega_m\downarrow0\). Local interval extrema give nested finite-range envelopes on the same clocks.

Their backward ancestry is finite: the expected number of length-\(n\) clock chains is bounded by a constant times
\((M|W_m|)^n/n!\). The local interval width exceeds the full interval width by at most \(2\omega_m\), so
\[
d_m(t)\le2\omega_m t+c\int_0^t d_m(s)\,ds.
\]
Counting discrepancy-creating marks yields
\[
\mathbb P(L_e^m\ne U_e^m\text{ as entire paths})
\le C_c\omega_m,\qquad
C_c=\frac{2(e^c-1)}c,
\]
with value two at \(c=0\). Choosing \(\omega_{m_k}\le2^{-k}\) gives actual summable common-input errors. No finitary initial iid sampler is assumed.

### Monotone reduced-algebra increments

If \(D\in\mathcal C\) and \(D\ge\delta I>0\), write
\[
D=\sum_n T_nT_n^*
\]
increasingly in norm, with each \(T_n\) finitely supported. Given residual \(R_n\), approximate \((R_n/2)^{1/2}\) so that
\[
\|T_nT_n^*-R_n/2\|\le\min\sigma(R_n)/4.
\]
Then
\[
R_n/4\le R_{n+1}\le3R_n/4.
\]
Composing R on fresh channels gives a relative monotone transition from \(\mu_C\) to \(\mu_{C+D}\) whenever the interval is gapped. Its root-change probability is exactly \(\tau D\).

For gapped \(K,L\) with \(D=L-K\in\mathcal C\), this gives an actual relative transition of cost at most \(\tau|D|+\eta\). Write \(D=D_+-D_-\), use a fine polygon \(C_j=K+jD/n\), and move through
\[
C_j\le E_j=C_j+D_+/n+\beta I\ge C_{j+1}.
\]
Choose
\[
\|D_+\|/n+\beta<\epsilon/2,\qquad 2n\beta<\eta.
\]
Both increments are strictly positive in \(\mathcal C\); downward transitions use complements. Their summed root cost is
\(\tau|D|+2n\beta\). This construction need not be monotone even when \(K\le L\).

### Arbitrary-kernel near-optimal relative interface

**Theorem.** For every fixed pair of positive contractions \(K,L\) and every \(\eta>0\), a total Borel equivariant map from a given \(X\sim\mu_K\) and independent regular iid noise produces \(Y\sim\mu_L\) with
\[
\boxed{\mathbb P(X_e\ne Y_e)\le\tau|K-L|+\eta.} \tag{5}
\]
No endpoint monotonicity or prescribed joining is claimed.

For gapped endpoints, put \(D=L-K\), choose \(n\) with \(\|D\|/n<\epsilon/2\), and set \(C_j=K+jD/n\).

There exist self-adjoint \(D_m\in\mathcal C\), bounded by \(\|D\|\), converging strongly to \(D\). Explicitly, truncate convolution coefficients on finite inverse-closed sets to obtain self-adjoint \(S_m\). For finitely supported \(u\), \(S_mu\to Du\), and
\[
(S_m-i)^{-1}(D-i)u-u
=(S_m-i)^{-1}(D-S_m)u\to0.
\]
The uniform resolvent bound and density give strong resolvent convergence, also at \(-i\). Apply continuous compactly supported functional calculus with a real function equal to the identity on \([-\|D\|,\|D\|]\) and bounded by \(\|D\|\). This gives the \(D_m\). Uniform boundedness also gives
\(\tau|D_m|\to\tau|D|\).

For one step \(C_j\to C_j+D/n\), all
\(H_m=C_j+D_m/n\) are gapped. Use the preceding interface first from \(C_j\) to \(H_1\), then from \(H_m\) to \(H_{m+1}\), on fresh channels. Choose a subsequence with
\[
\|(D_m-D)\delta_e\|\le e_m,
\qquad \sum_m e_m
\]
arbitrarily small. Since \(\tau|E|\le\|E\delta_e\|\), successive root disagreements are at most
\[
(e_m+e_{m+1})/n+\zeta_m,
\]
with arbitrarily small summable allowances \(\zeta_m\).

Borel–Cantelli gives actual coordinate stabilization. Finite determinants identify the limit as \(\mu_{C_j+D/n}\). Its root cost from the given input is at most
\[
\frac{\tau|D_1|}{n}
+\frac1n\sum_m(e_m+e_{m+1})
+\sum_m\zeta_m,
\]
including the initial allowance in the last sum. This approaches \(\tau|D|/n\). Composing the \(n\) steps proves (5) for gapped endpoints.

For singular endpoints, independently flip each initial bit with probability \(s<1/2\). The resulting kernel is
\[
K_s=sI+(1-2s)K,
\]
because
\[
\begin{aligned}
\mathbb E\prod_{i\in F}[s+(1-2s)X_i]
&=\sum_{J\subseteq F}s^{|F|-|J|}(1-2s)^{|J|}\det K_J\\
&=\det((K_s)_F).
\end{aligned}
\]
The root cost is exactly \(s\). Use the gapped interface to reach \(L_s\), then successively \(L_{s_m}\), where \(s_m\downarrow0\). The latter costs sum to at most
\[
s\,\tau|I-2L|+\sum_m\zeta_m
\le s+\sum_m\zeta_m.
\]
Actual stabilization identifies \(\mu_L\). Total cost is at most
\[
\tau|K-L|+2s+\sum_m\zeta_m.
\]
Choose the last terms below \(\eta\). On the invariant Borel stabilization-failure set return the initial configuration.

### Consequences and a restricted exact theorem

Taking the initial configuration empty proves **H**, without assuming it.

For ordered \(A\le B\), (5) gives joint iid realizations with exact marginals and root order violation at most \(\eta/2\), since
\[
2\mathbb P(X_e=1,Y_e=0)
=\mathbb P(X_e\ne Y_e)-\tau(B-A).
\]
Letting \(\eta\downarrow0\) and taking a weak limit of these **laws** proves **L**. It does not produce a joint iid limit.

The exact target does hold, including singular endpoints, whenever
\[
\boxed{B-A\in\mathcal C,\qquad B-A\ge\delta I>0.}
\]
Choose \(0<\epsilon_0<\delta/2\). Sample \(\mu_{A+\epsilon_0I}\) using H as just proved, then apply the monotone interface to \(B-\epsilon_0I\). For \(\epsilon_n\downarrow0\), shrink the lower configuration by relative scalar transitions on its complement and grow the upper by relative scalar transitions. On every input,
\[
X_{n+1}\subseteq X_n\subseteq Y_n\subseteq Y_{n+1}.
\]
The limits have marginals \(\mu_A,\mu_B\) by finite determinants. Each transition has a gap; no uniform endpoint gap is assumed.

## 4. The exact remaining gap and representation tests

For ordered pair maps \(F_n\) on one iid input,
\[
\sum_n\mathbb P(F_{n+1}(e)\ne F_n(e))<\infty \tag{6}
\]
suffices: every coordinate stabilizes almost surely, the ordered alphabet
\(\{(0,0),(0,1),(1,1)\}\) is preserved, and the invariant exceptional set receives \((\varnothing,\varnothing)\). Entrywise convergence of marginal kernels identifies both limit DPPs.

**Constructing these ordered pair maps for arbitrary \(A\le B\) is unproved.** Independent marginal corrections can create \((1,0)\). Summable order violations do not imply stabilization of successive pair maps. In particular, (5) cannot be used with \(\eta=0\) without another proof. Section 1 shows why weak convergence cannot replace (6).

Order-preserving positive-square approximation can fail. On \(\mathbb Z\), take a positive-measure closed nowhere-dense set \(E\) on the Fourier circle and
\[
A=I/8,\qquad B=I/4+P_E/4,\qquad D=I/8+P_E/4.
\]
Every continuous multiplier below \(D\) is at most \(1/8\) on the dense open complement, hence everywhere. Dominated finite-support positive-square partial sums therefore have trace at most
\(1/8<\tau D\), precluding even weak convergence despite the gaps.

A one-hot Hermitian DPP on \(\Gamma\times S\) is also not universal. Vanishing same-fiber two-point determinants force each diagonal fiber block to have rank at most one. Positivity annihilates its orthogonal fiber complement, so
\[
K=JCJ^*,\qquad J\delta_g=\delta_g\otimes v.
\]
Inclusion determinants identify independent marking of \(\mu_C\). Nested color retention therefore forces independent thinning:
\[
\det A_F=\theta^{|F|}\det B_F.
\]
On \(C_2\),
\[
A=\begin{pmatrix}1/4&1/8\\1/8&1/4\end{pmatrix},\qquad B=I/2
\]
satisfy \(0<A<B<I\). Intensities force \(\theta=1/2\), but
\[
\det A=3/64\ne1/16=\theta^2\det B.
\]
This excludes only that representation.

Finite groups satisfy the full target: average a finite monotone coupling over the group and sample it in coordinates transported from the unique minimum-priority iid vertex, using an independent uniform there. Invariance identifies the law and equivariance follows because the leader translates. On priority ties return the empty pair. The finite domination input permits complex and singular kernels. 

Scalar lower kernels are covered: for \(aI\le B\), independently sample
\(Z\sim\mu_{(B-aI)/(1-a)}\) and \(X\sim\mathrm{Bern}(a)^\Gamma\), then take \(Y=X\cup Z\). For finite \(F\),
\[
\mathbb P(F\subseteq Y^c)
=(1-a)^{|F|}\det\!\left(\left[I-\frac{B-aI}{1-a}\right]_F\right)
=\det((I-B)_F).
\]
Scalar upper kernels use \(Z\sim\mu_{A/b}\), independent iid Bernoulli \(b\) configuration \(Y\), and \(X=Y\cap Z\); then
\[
\mathbb P(F\subseteq X)=b^{|F|}\det((A/b)_F)=\det A_F.
\]
The endpoint cases are deterministic. Equal kernels, \(A=0\), and \(B=I\) include singular projection cases. 

The remaining material is not included here. The scope of any mathematical review must be stated by section and claim.
