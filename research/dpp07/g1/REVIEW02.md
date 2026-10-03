# Independent adversarial audit of the frozen coupling proof

STATUS: CORRECT

## Scope of the verdict

The proof establishes the following fixed-kernel statement.

Let \(\Gamma\) be a countable group in its left regular action and let \(Q\) be a fixed complex Hermitian positive contraction \(0\le Q\le I\) on \(\ell^2(\Gamma)\) commuting with that action. Put \(p=\operatorname{FK}(Q)\). If \(p>0\), there is a total Borel, everywhere \(\Gamma\)-equivariant map from the regular iid source to a pair \((X,Y)\) with
\[
X\sim\operatorname{Ber}(p)^\Gamma,\qquad Y\sim\operatorname{DPP}(Q),
\qquad X\subseteq Y.
\]
If \(p=0\), the same conclusion follows under the stated hypothesis H for this fixed \(\operatorname{DPP}(Q)\), by taking \(X=\varnothing\). The proof does not assert measurable dependence on a varying kernel, a grand coupling of kernels, a finite coding radius, or a result for a nonregular action.

The only standard background input is existence and finite-dimensional consistency of the determinantal law of a positive contraction, together with its finite \(L\)-ensemble formula. Every new step needed for the coupling is proved in the manuscript. I found no critical gap.

## Reconstruction of the load-bearing argument

### 1. The Fuglede--Kadison path stays inside the gapped contractions

For \(0<p<1\), set
\[
a_t=\frac{p}{\operatorname{FK}(Q+tI)},\qquad K_t=a_t(Q+tI).
\]
Spectral differentiation gives \(a_t'=-r_ta_t\), where
\(r_t=\tau((Q+tI)^{-1})\), hence
\(K_t'=a_tI-r_tK_t\). If \(M=\|Q\|\), then
\[
\int\log(1+t/\lambda)\,d\nu_Q(\lambda)
\geq \log(1+t/M),
\]
so \(\|K_t\|=a_t(M+t)\leq M\). When \(M=1\), equality would force the spectral measure to be \(\delta_1\), hence \(Q=I\), contradicting \(p<1\). Thus every \(K_t\) has two spectral gaps, locally uniformly in \(t\). Moreover
\[
K_t\to Q\quad(t\downarrow0),\qquad K_t\to pI\quad(t\to\infty)
\]
in norm. Multilinearity of finite determinants gives equation (3), including at singular finite minors.

### 2. The infinite-volume conditional odds are a valid version

For a boundedly invertible positive \(L\), the variational quantity
\[
\lambda_L(x,\eta)=\inf_{h\in\ell^2(\eta)}
\langle L(\delta_x+h),\delta_x+h\rangle
\]
is the \(x\)-diagonal of the shorted operator in equation (5). Product convergence of configurations gives strong convergence of their coordinate projections. The operators inverted in (5) have a common positive lower bound, so their inverses converge strongly. This proves the claimed all-configuration continuity and covariance.

For a gapped contraction \(K\), finite-volume exact-pattern probabilities yield the conditional odds
\[
q(x,\eta)=\frac{\lambda_{K(I-K)^{-1}}(x,\eta)}
{1+\lambda_{K(I-K)^{-1}}(x,\eta)}.
\]
To pass to the whole exterior, compress \(K\) to an exhaustion, extend the compression by a scalar lying in the common gap, and apply continuous functional calculus. The extended kernels converge strongly to \(K\), their \(L\)-operators converge strongly to the global \(L\), and the finite shorted diagonals converge pointwise for every exterior configuration. Along a determinantal sample, the corresponding finite conditional probabilities form the usual bounded martingale. Its almost-sure limit is conditioning on the full exterior. Thus equation (6) is simultaneously an everywhere-defined continuous function and an almost-sure version of the required infinite-volume conditional probability.

The full-exterior variational minimum is
\[
\lambda_{L_t}(x,\Gamma\setminus\{x\})
=\frac{1}{\langle L_t^{-1}\delta_x,\delta_x\rangle}
=\frac{a_t}{r_t-a_t}.
\]
This makes the birth rates in (8) nonnegative. Their decrease in the occupied exterior follows directly from monotonicity of shorting.

### 3. The prescribed DPP marginals satisfy the birth forward equation

Conditioning at a site \(i\in B\) and using equation (6) gives
\[
\mathbb E\!\left[
\mathbf1_{\{B\setminus\{i\}\subseteq\eta\}}
\mathbf1_{\{i\notin\eta\}}c_t(i,\eta)
\right]
=r_t\det K_t[B]-a_t\det K_t[B\setminus\{i\}].
\]
After the reverse-time change \(t=s^{-1}-1\), this is exactly the derivative obtained from equation (3). Inclusion monomials span every finite cylinder algebra, so equation (10) holds for all cylinder functions. No unproved pointwise identification of an infinite generator is used.

### 4. Covariant sensitivity and mass transport are valid for every countable group

For \(\eta\subseteq\zeta\), the polar decomposition in Section 4 transports the decrement
\(\lambda_L(x,\eta)-\lambda_L(x,\zeta)\) from the source \(x\) to the newly occupied sites \(\zeta\setminus\eta\). The row identity is equation (11). The column estimate follows from
\[
\sum_{x\notin\zeta}w(x,y)
=\|(I-D_\zeta)(L-\ell I)L^{-1/2}V\delta_y\|^2,
\]
and both row and column sums are bounded by \(\kappa(L)\). Comparing two arbitrary configurations through their intersection, with a diagonal term only when the source occupations differ, gives equations (13)--(14).

All pieces of the polar construction are Borel and covariant. The group acts freely and transitively on the coordinate set, so the outgoing-to-incoming mass-transport identity applies without amenability. It converts the deterministic row/column estimates into equation (15) for every jointly invariant random pair.

### 5. The scalar entrance at \(s=0\) is integrable

Writing \(u=1/t\), the norm expansions in equation (16) imply
\[
L_t=\ell I+uG+O(u^2),\qquad
\ell=\frac{p}{1-p},\qquad G_{xx}=0.
\]
Uniformly over all vacant exteriors, the direct diagonal in the shorted formula is \(\ell+O(u^2)\), while its Schur-complement correction is also \(O(u^2)\). Hence \(\lambda_{L_t}(x,\eta)=\ell+O(u^2)\) uniformly.

In
\[
c_t=(r_t-a_t)\lambda_{L_t}-a_t,
\]
the coefficients of \(u\) and \(u^2\) cancel because \((1-p)\ell=p\). Therefore \(\overline c_t=O(u^3)\). Also \(\|L_t-\ell I\|=O(u)\), so \((r_t-a_t)\kappa(L_t)=O(u^3)\). Since \(u=s/(1-s)\), the reversed rates and the sensitivity coefficient are \(O(s)\) at the entrance. This proves continuity of the rates through \(s=0\) and local integrability of \(C_s\); no spectral gap for the terminal kernel \(Q\) is being inserted here.

### 6. The iid-driven fixed point is a strong construction

On each \([0,S]\), the rates have a finite bound. Starting from the iid Bernoulli field and independent sitewise Poisson random measures, the Picard map (19) is adapted and equivariant. Poisson compensation together with equation (15) gives equation (20). Consequently the successive-path disagreement probabilities satisfy
\[
D_k(t)\leq \frac{A(t)^k}{k!},\qquad A(t)=\int_0^tC_r\,dr.
\]
The series is summable. Borel--Cantelli therefore gives eventual stabilization of every coordinate path, simultaneously over all coordinates and rational compact horizons.

Comparing a Picard iterate with the stabilized limit in the same compensation estimate and applying dominated convergence proves the graphical fixed-point equation. This produces an adapted solution as a measurable function of the original independent drivers. The stated Gronwall argument proves pathwise uniqueness within the jointly invariant adapted class. The marginal argument below uses existence; it does not require a stronger unclaimed uniqueness theorem.

### 7. Finite envelopes identify the marginals without a weak path limit

The cross-dependent lower and upper envelopes in equation (22) are finite-range systems. For a fixed source, the expected number of backward proposal chains of length \(j\) is at most
\((BdS)^j/j!\). Finite branching and absence of infinite backward chains give a well-defined equivariant recursive construction on the infinite coordinate set. Antimonotonicity of the vacant-site rate proves both the envelope order and the bracket
\[
L_t^n\subseteq Z_t\subseteq U_t^n.
\]

Uniform continuity on the compact time-configuration domain gives \(\omega_n\to0\). At the first envelope disagreement, the threshold gap is bounded by two truncation errors plus the full-rate difference. Compensation, equation (15), and Gronwall give equation (26), so the two envelopes agree locally in probability as \(n\to\infty\).

For a finite \(F\), the conditional rates in equation (27) are defined for every finite state because all finite cylinder probabilities are positive. Conditioning equation (10) shows that \(\nu_s|_F\) solves the forward equation of the finite pure-birth chain with those rates. Bounded continuous finite-state rates give uniqueness, so the chain \(V^F\) driven by the same initial bits and proposals has exactly the marginal \(\nu_s|_F\).

At a dependency-interior site, every completion of the finite state lies between the truncated lower exterior and the exterior padded by occupied sites. Antimonotonicity therefore sandwiches the conditional finite-chain rate between the two envelope rates, which is equation (29). Any local order violation must trace backward either to the finite boundary or along an infinite proposal chain. The latter event has probability zero; the former has the factorial tail in equation (30). For fixed \(n\), exhausting the group by finite sets sends the boundary distance to infinity. Equation (31), followed first by this exhaustion and then by \(n\to\infty\), proves
\(Z_s\sim\nu_s\) for every \(s<1\). This also covers finite groups by taking \(F=\Gamma\).

### 8. The ungapped endpoint and the total Borel factor are both covered

The constructions on compact subintervals are restrictions of one construction on \([0,1)\). Define \(X=Z_0\) and let \(Y\) be the union over rational \(s<1\). Monotonicity of the path and norm convergence \(K_{t_s}\to Q\) give, for every finite \(B\),
\[
\mathbb P(B\subseteq Y)=\lim_{s\uparrow1}\det K_{t_s}[B]=\det Q[B].
\]
Inclusion--exclusion recovers all finite cylinder probabilities, so \(Y\) has law \(\operatorname{DPP}(Q)\). This endpoint argument needs no inverse or spectral gap for \(Q\).

A sitewise Borel splitting of one uniform label supplies the initial Bernoulli bit and all independent Poisson randomness. The locally finite point-measure decoder, Picard iterates, stabilization event, fixed-point event, rational endpoint union, and coordinatewise output are Borel. Equality of the binary càdlàg paths can be tested on rational times together with the compact endpoint. Every defining condition is imposed at every coordinate, so the good set is invariant and the construction on it is equivariant. It is conull. Sending its invariant complement to \((\varnothing,\varnothing)\) makes the map total, everywhere equivariant, and pointwise order preserving without changing its law.

### 9. Boundary cases and exact limitations

For \(p=0\), H is used only to sample the fixed \(\operatorname{DPP}(Q)\), and \(X\) is empty. For \(p=1\), faithfulness of the trace and \(\int -\log\lambda\,d\nu_Q=0\) force \(Q=I\), so the constant full configuration works.

Thus the manuscript proves precisely the regular-orbit, fixed-kernel theorem it states. It neither uses nor proves a sampler hypothesis for \(p>0\), kernel-uniform measurability, a grand coupling, finite coding, or an extension to actions with stabilizers.

## Noncritical presentation point

In the displayed conditional-expectation formula immediately before equation (10), `\!left[` is a typesetting typo for `\!\left[`. It does not alter the formula or any inference.
