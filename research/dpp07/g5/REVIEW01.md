# Independent adversarial audit of the visible relative-transition response

STATUS: **VISIBLE_SCOPE_CORRECT; UNRESTRICTED EXACT JOINT-IID TARGET STILL INCOMPLETE**

## Scope boundary

The reviewed source contains complete visible Sections 1--3 and only the visible beginning of Section 4. No mathematical claim about an unavailable continuation or attachment is certified here.

Within that boundary, no critical mathematical gap was found after independently reconstructing the compressed load-bearing steps. In particular, the visible argument does establish all of the following:

1. the scalar-marginal ordered joining in Section 1 is invariant but not an iid factor, is separated by at least \(1/36\) in \(\bar d\) from every \(T^2\)-ergodic law, and is a weak limit of ordered iid factors having the same exact marginals;
2. Theorem R gives a relative pure-birth transition for a spectrally gapped finite-support positive square;
3. the relative transition yields actual common-input convergence, not merely weak convergence of output laws;
4. for arbitrary fixed positive contractions \(K,L\) and every \(\eta>0\), there is a relative iid transition of root cost at most \(\tau|K-L|+\eta\);
5. this independently implies H, implies L only at the level of invariant laws, and proves the exact ordered joint-iid target for the strict subclass
   \[
   B-A\in C_r^*(\Gamma),\qquad B-A\geq\delta I>0;
   \]
6. the unrestricted exact ordered pair construction remains unproved.

Thus the response's **INCOMPLETE** label is accurate. The positive auxiliary theorems do not solve the general exactJO target, while that incompleteness does not invalidate the auxiliary theorems.

## 1. The fixed-marginal obstruction on \(\mathbb Z\)

The matrix \(Q\) has uniform one-site marginals. Under the color maps \(0,1\mapsto X=0\), \(2\mapsto X=1\) and \(0\mapsto Y=0\), \(1,2\mapsto Y=1\), the identities

\[
Q_{22}=Q_{00}=1/9
\]

show that the two binary coordinates inside each \(Q\)-block are independent. Different blocks are independent. Hence both pairing phases have exact marginals

\[
X\sim\operatorname{Bern}(1/3)^{\mathbb Z}=\mu_{I/3},\qquad
Y\sim\operatorname{Bern}(2/3)^{\mathbb Z}=\mu_{2I/3}.
\]

The statistic \(\phi\) has means \(5/9\) on a \(Q\)-edge and \(4/9\) across two independent uniform colors. Even- and odd-edge ergodic averages therefore recover the pairing phase \(H\). It is \(T^2\)-invariant, is reversed by \(T\), and has mean zero. Each phase is \(T^2\)-ergodic; their exchange under \(T\) makes the mixture \(T\)-ergodic but not \(T^2\)-ergodic.

For any stationary joining with a \(T^2\)-ergodic law \(\nu\), the conditional law of \(W\) given \(H=h\) is \(T^2\)-invariant and is dominated by \(2\nu\). Its Radon--Nikodym derivative is therefore \(T^2\)-invariant and hence constant, so \(W\) is independent of \(H\). Consequently

\[
\frac1{18}
=\left|\mathbb E H\bigl(\phi(Z_0,Z_1)-\phi(W_0,W_1)\bigr)\right|
\leq 2\mathbb P(Z_0\neq W_0),
\]

because changing a two-coordinate word changes \(\phi\) only if one of its two coordinates changes. Taking the infimum over stationary joinings proves the stated \(1/36\) lower bound.

A factor of a regular iid \(\mathbb Z\)-shift is \(T^2\)-ergodic, since the iid source under \(T^2\) is the product of its even and odd Bernoulli shifts. Thus the prescribed joining is not an iid factor. This also excludes a relative conditional factor realizing this particular joining, because \((X,\Psi(X,U))\) would itself be an iid factor.

The marker construction has the claimed exact marginals. Conditional on the marker partition, every \(Q\)-pair and every singleton supplies independent Bernoulli coordinates for each binary projection, with parameters independent of the partition. The finite-window boundary probability is \(O(rp)\), while the parity bias of the preceding marker tends to zero, giving the displayed total-variation convergence. Every approximant is an iid factor and hence \(T^2\)-ergodic, so the same \(1/36\) lower bound applies. If common-input maps were Cauchy in root probability, a subsequence could be chosen with summable successive root discrepancies. Equivariance and Borel--Cantelli would then give coordinatewise stabilization to an iid factor with law \(\lambda\), a contradiction. This correctly distinguishes weak convergence of laws from common-input convergence of maps.

## 2. Theorem R

### 2.1 Conditional kernels and the sensitivity estimate

For \(J_x=2P_x-I\), direct multiplication gives

\[
K-P_{x^c}=\frac12J_x\bigl[I+J_x(2K-I)\bigr].
\]

The spectral gap gives \(\|2K-I\|\leq1-2\epsilon\), so the inverse exists for every boundary configuration and has norm at most \(\epsilon^{-1}\). The Neumann series converges uniformly. Each finite partial sum is norm-continuous on fixed vectors in the product topology, which proves the asserted fixed-vector continuity and compactness of the family \(G_{t,x}\delta_s\).

Finite occupation and vacancy conditioning are Schur complements. Occupation subtracts \(kk^*/p\), vacancy adds \(kk^*/(1-p)\), and applying the same statement to \(I-K\) preserves both sides of the gap. Exhausting the exterior, the uniformly convergent resolvent formulas and martingale convergence identify the all-boundary conditional law with the displayed kernel \(N_F(x)\), with

\[
\epsilon I\leq N_F(x)\leq(1-\epsilon)I.
\]

An exterior flip changes \(N_F\) by a rank-one matrix. Block inversion expresses its vector through \(G_x(\cdot,j)\); the relevant scalar inverse is a conditional one-site probability or its complement and is at most \(\epsilon^{-1}\). This gives (1). Uniform row tails follow from compactness in \(\ell^2\), while the column sum is bounded by the resolvent norm. Interpolating \(L\leq U\) by independently switching each disagreement at an exponential time, finite-set truncation justifies differentiation. Mass transport changes the expected row sum into the column sum at the root, and integration of the surviving disagreement density \(de^{-r}\) proves (2).

### 2.2 Positive finite flows

For finite \(S\), stochastic domination of
\(\mu_N\) by \(\mu_{N+hvv^*}\) implies that
\(p_{N+hvv^*}-p_N\) is the divergence of a nonnegative flow on upward comparable pairs. Splitting each comparable jump into Boolean-cube edges, dividing by \(h\), and taking a limit puts \(b_N\) in the closed cone generated by upward edge columns. The expected-cardinality functional

\[
m(b)=\sum_\eta |\eta|b(\eta)
\]

equals the total edge-flow mass and equals \(\|v\|^2\) for this derivative. The slice \(m=1\) is a finite polytope. A fixed triangulation with feasible vertex flows gives a continuous piecewise-affine selection on the slice and hence a homogeneous Lipschitz selection on the cone. This fills the compressed selection argument without adding an assumption.

Successive one-site conditioning and the spectral gap give
\(p_N(\eta)\geq\epsilon^{|S|}\). Therefore the selected edge flow divided by \(p_N(\eta)\) gives bounded rates Lipschitz in \(N\). Summing translated block contributions is finite at each site because \(S\) is finite.

For configurations in an interval \([L,U]\), their conditional kernels lie between the endpoint conditional kernels. If \(E\) is their difference and \(D=N_S(L)-N_S(U)\geq0\), then \(-D\leq E\leq D\). On the positive and negative spectral subspaces of \(E\), these two inequalities give

\[
\|E\|_1\leq\operatorname{tr}D.
\]

The rate oscillation is bounded by a constant times the number of local-pattern disagreements plus a constant times this trace norm. Invariance bounds the first expectation by a finite multiple of \(\mathbb P(L_e\neq U_e)\), and (2) bounds the second. This proves (3); no pointwise summation of separate worst-case influences is used.

### 2.3 Common clocks and marginal identification

The lower and upper envelope iteration is well-defined because the rates are bounded and continuous, and the order interval of configurations is compact. Each site has finitely many clock marks on the bounded time interval. The lower birth time moves monotonically through this finite list and the upper birth time moves oppositely, so both envelope paths stabilize at each site. The limiting extrema are attained on the compact interval. Equality between a predictable threshold and a Poisson height has probability zero.

The limiting envelopes form an invariant ordered pair. A first discrepancy can occur only at a mark between their two thresholds. The compensator formula and (3) yield

\[
d(t)\leq c\int_0^t d(s)\,ds,\qquad d(0)=0.
\]

Gronwall gives equality of the envelopes. The deterministic trapping induction applies to every relaxed solution on the same clocks, so the solution is unique on the full-measure invariant good set.

It remains necessary to identify its law; the formal infinite forward equation alone would not do so. A rank-one increment supported on \(gS\) leaves the exterior marginal unchanged and adds exactly that rank-one matrix to the conditional kernel. The finite-flow divergence identity therefore gives (4) for every cylinder.

For finite \(\Lambda\), conditioning the rates under the proposed law gives an ordinary finite pure-birth chain. Equation (4), grouped by the states of \(\Lambda\), is exactly its finite Kolmogorov forward equation, whose solution is unique. Thus its time-\(t\) law is \(\mu_{K_t}|_\Lambda\). Uniform continuity supplies the required stronger convergence statement: once \(\Lambda\) contains a sufficiently large relative neighborhood, every extension of a fixed \(\Lambda\)-pattern has nearly the same intrinsic rate, so the conditional average \(\widehat a_i^\Lambda\) is uniformly close to \(a_i\) on matching inputs.

Run all finite chains from the same initial configuration and clocks. From every subsequence, diagonal compactness of the finite sitewise clock lists produces a whole-path convergent subsubsequence. Uniform rate convergence makes its limit a relaxed solution; uniqueness identifies it with the envelope path. Hence the full finite-chain sequence converges on the common input. Passing the exact finite marginals to the limit and using inclusion--exclusion proves \(X_t\sim\mu_{K_t}\). The invariant bad set can receive the constant initial path, which makes the map total and preserves pure-birth order.

This establishes Theorem R for complex Hermitian kernels and does not assume H or L.

## 3. Quantitative interfaces

### 3.1 Actual finite-range convergence

For the finite-range envelopes, backward dependence is almost surely finite: the expected number of length-\(n\) chronological dependency chains is bounded by a constant times \((M|W_m|)^n/n!\). Uniform rate oscillation contributes at most \(2\omega_m\), and the same sensitivity estimate gives the displayed Gronwall inequality. Integrating the discrepancy-creating intensity yields the whole-path root bound \(C_c\omega_m\). A subsequence with \(\omega_{m_k}\leq2^{-k}\) therefore has summable common-input errors. This is stronger than convergence of factor laws and is the property needed for pointwise stabilization.

### 3.2 Positive increments in \(C_r^*(\Gamma)\)

If \(D\in C_r^*(\Gamma)\) and \(D\geq\delta I\), functional calculus puts \((R_n/2)^{1/2}\) in the same algebra. Approximation by a finite-support convolution \(T_n\) can be chosen so that

\[
\left\|T_nT_n^*-\frac12R_n\right\|\leq\frac14\min\sigma(R_n).
\]

Thus \(R_{n+1}=R_n-T_nT_n^*\) remains positive and lies between \(R_n/4\) and \(3R_n/4\). The partial sums increase in operator order and converge in norm to \(D\). Applying Theorem R successively on fresh iid channels gives a monotone relative transition. Monotonicity makes its root-change probability the difference of the one-site intensities, exactly \(\tau D\), and coordinatewise limits identify the terminal DPP.

For self-adjoint \(D=L-K\in C_r^*(\Gamma)\), the two legs through

\[
E_j=C_j+D_+/n+\beta I
\]

have strictly positive increments \(D_+/n+\beta I\) and \(D_-/n+\beta I\). The gap conditions in the source keep every intermediate operator a positive contraction. Summing the two monotone costs over the polygon gives
\(\tau|D|+2n\beta\). The construction is a relative transition, but the two-leg path need not be monotone from its original input to its final output.

### 3.3 Strong approximation and arbitrary kernels

For general self-adjoint \(D\) in the group von Neumann algebra, symmetric finite Fourier truncations \(S_m\) converge to \(D\) on finitely supported vectors. The displayed resolvent identity proves strong resolvent convergence. Choosing a bounded real \(f\in C_c(\mathbb R)\) equal to the identity on \([-\|D\|,\|D\|]\) gives

\[
D_m=f(S_m)\in C_r^*(\Gamma),\qquad
\|D_m\|\leq\|D\|,\qquad D_m\to D\ \text{strongly}.
\]

Uniform boundedness and polynomial approximation to the absolute-value function also give \(|D_m|\to|D|\) strongly, hence \(\tau|D_m|\to\tau|D|\).

Choose a subsequence with summable
\(e_m=\|(D_m-D)\delta_e\|\). Since

\[
\tau|E|\leq\|E\delta_e\|
\]

for self-adjoint equivariant \(E\), the successive relative-transition costs from \(H_m\) to \(H_{m+1}\) are bounded by the displayed summable errors. Borel--Cantelli gives coordinatewise stabilization on the actual common input. Strong kernel convergence gives entrywise convergence on every finite principal matrix, so finite determinants identify the limit law. This proves the gapped arbitrary-kernel interface with cost arbitrarily close to \(\tau|K-L|\).

Independent bit flips with probability \(s\) transform \(\mu_K\) into the DPP with kernel \(K_s=sI+(1-2s)K\); the determinant expansion in the source proves this for every finite inclusion event. Applying the gapped interface and then a summable sequence \(L_{s_m}\to L\) costs at most

\[
s+(1-2s)\tau|K-L|+s\,\tau|I-2L|+\text{allowances}
\leq\tau|K-L|+2s+\text{allowances}.
\]

This closes the singular endpoints and proves (5).

### 3.4 Exact implications

- **H is proved independently.** Set the initial kernel to \(0\). The input is the deterministic empty configuration, so (5) gives an equivariant iid sampler for every fixed positive contraction.
- **L is proved only at law level.** For \(A\leq B\), the identity
  \[
  2\mathbb P(X_e=1,Y_e=0)
  =\mathbb P(X_e\neq Y_e)-\tau(B-A)
  \]
  makes the root order violation at most \(\eta/2\). Compactness gives a weak limit of the pair laws; the root violation event is clopen, and invariance plus countability gives containment at every coordinate. This does not produce a limit factor map.
- **A strict exactJO subclass is proved.** If \(D=B-A\in C_r^*(\Gamma)\) and \(D\geq\delta I\), choose \(\epsilon_0<\delta/2\), sample \(\mu_{A+\epsilon_0I}\) using H, and apply the monotone \(C_r^*\) transition to \(B-\epsilon_0I\). Decreasing scalar corrections of the lower process and increasing scalar corrections of the upper process can be run on fresh channels so that
  \[
  X_{n+1}\subseteq X_n\subseteq Y_n\subseteq Y_{n+1}
  \]
  on every good input. Binary monotonicity itself gives coordinatewise limits; finite determinants give marginals \(\mu_A,\mu_B\). Returning the empty pair on the invariant union of null exceptional sets provides the all-input convention.

The last result genuinely gives one iid input after the countably many independent channels are encoded coordinatewise into a single regular iid source.

## 4. Visible part of the remaining-gap section

Only the visible claims are assessed.

- The summable-disagreement criterion (6) is sufficient by equivariance, Borel--Cantelli and countability. Requiring every approximant to use the ordered three-letter alphabet is essential.
- The Fourier example correctly blocks dominated positive-square approximation. A continuous multiplier dominated by \(D=I/8+P_E/4\) is at most \(1/8\) on the dense open complement of \(E\), hence everywhere, so its trace cannot converge to \(\tau D>1/8\).
- The one-hot finite-label obstruction is correct. Zero same-fiber two-point determinants force rank-one diagonal fiber blocks; positivity kills their orthogonal complements. The resulting DPP is independent marking of a base DPP. Nested retention is therefore independent thinning. The \(C_2\) matrices satisfy \(0<A<B<I\), but their two-point determinants violate the necessary thinning identity.
- For a finite group, a finite monotone coupling can be averaged to an invariant one and sampled equivariantly from the unique minimum-priority iid vertex using an independent random channel. The tie convention has probability zero and is equivariant.
- The scalar lower and scalar upper constructions are correct; avoidance probabilities in the first and inclusion probabilities in the second identify the desired DPPs, including the deterministic endpoints.

These tests exclude particular mechanisms only. They do not disprove the unrestricted target.

## External inputs and prior-art boundary

The only external determinantal input needed by Theorem R is finite Hermitian DPP stochastic domination under operator order, stated as Theorem 2.9 in Lyons' ICM survey. The named Lyons--Thom Theorem 5.1 supplies invariant monotone couplings only in its sofic scope. Its Question 7.7 asks whether equivariant DPPs are Bernoulli factors. Neither named source contains the relative pure-birth theorem, the arbitrary-countable-group conclusion H, the near-sharp arbitrary-kernel relative interface, or the strict positive-\(C_r^*\)-increment exactJO construction.

Accordingly, the visible positive results are not merely restatements of the two named sources. This is not a comprehensive novelty certification: priority against all later or unpublished work remains unverified.

Primary sources checked:

- R. Lyons, *Determinantal probability: basic properties and conjectures*, especially Theorem 2.9 and Section 5.2: <https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf>.
- R. Lyons and A. Thom, *Invariant coupling of determinantal measures on sofic groups*, especially Theorem 5.1 and Question 7.7: <https://rdlyons.pages.iu.edu/pdf/couple-pub.pdf>.

## Final verdict

The visible Sections 1--3 withstand adversarial reconstruction. They prove H, law-level L, the near-optimal relative iid interface, and the strict positive-\(C_r^*\)-increment exactJO subclass. They do not prove the unrestricted exact ordered joint-iid theorem. Since the source is truncated after the visible part of Section 4 and its referenced attachment was unavailable, no whole-response or whole-manuscript certification is given.
