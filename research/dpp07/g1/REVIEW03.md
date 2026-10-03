# Independent full mathematical audit of `proof02.md`

**Frozen source SHA-256:** `433075F76CB4602FD2A027DA6576230C6FE9ABBAA2FCC5819045A1EC211906E8`

**STATUS: CORRECT**

## 1. Exact scope of the verdict

The manuscript proves the following fixed-kernel statement.  For every countable group
\(\Gamma\), acting on its single regular orbit by left translation, and every fixed complex
Hermitian positive contraction \(0\le Q\le I\) on \(\ell^2(\Gamma)\) that commutes with
that action, put
\(p=\operatorname{FK}(Q)\).  If \(0<p\le 1\), a single regular iid source admits a total
Borel, everywhere equivariant map to a coupling
\[
 X\sim\operatorname{Ber}(p)^\Gamma,\qquad Y\sim\operatorname{DPP}(Q),
 \qquad X\subseteq Y.
\]
For \(p=0\), the same conclusion follows conditionally from the explicitly stated
hypothesis H that this fixed \(\operatorname{DPP}(Q)\) already has a total Borel,
everywhere equivariant regular-iid sampler.

The proof does not establish a sampler jointly measurable in a varying kernel, a grand
coupling over kernels, a finitary coding, a coding-radius estimate, or a result for
nonregular orbits and arbitrary stabilizers.  None of these stronger conclusions is used
in deriving the stated result.

I reconstructed every section below.  The arguments that look standard have enough
hypotheses in the manuscript for their stated uses.

## 2. Operator path and determinant flow (Sections 2–3)

For \(0<p<1\), the path
\[
 a_t=\frac p{\operatorname{FK}(Q+tI)},\qquad K_t=a_t(Q+tI)
\]
is a path of strictly gapped positive contractions.  The lower gap is immediate from
\(K_t\ge a_ttI\).  If \(M=\|Q\|\), then
\[
 \log\frac{\operatorname{FK}(Q+tI)}p
 =\int\log(1+t/\lambda)\,d\nu_Q(\lambda)
 \ge \log(1+t/M),
\]
so \(\|K_t\|\le M\).  The only possible equality problem when \(M=1\) would force the
spectral distribution to be \(\delta_1\); faithfulness of the group trace would then give
\(Q=I\), contradicting \(p<1\).  Thus the upper gap is also strict, and both gaps are
uniform on compact \(t\)-intervals.

Logarithmic monotone convergence at \(t\downarrow0\), together with the large-\(t\)
expansion, gives the norm endpoints
\[
 K_t\to Q\quad(t\downarrow0),\qquad K_t\to pI\quad(t\to\infty).
\]
Differentiating the scalar Fuglede–Kadison factor and then a finite principal determinant
gives (1) and (3) with the displayed signs.  No commutativity beyond functional calculus
of the single self-adjoint operator \(Q\) is being assumed.

For a gapped kernel \(K\), the manuscript sets \(L=K(I-K)^{-1}\).  The shorted-operator
formula (5) is valid for every exterior configuration because \(L\) is bounded above and
below.  Coordinate projections converge strongly under product convergence of
configurations; the middle operators in (5) have a common positive lower bound, so their
inverses also converge strongly.  This proves the claimed all-input continuity and
Borel covariance.

The passage from finite conditional odds to the full exterior is also valid.  Compress
\(K\) to a finite exhaustion, extend the compression by any scalar in the common gap, and
apply continuous functional calculus.  The extended kernels and their \(L\)-operators
converge strongly with uniform bounds.  Formula (5) therefore converges for every fixed
exterior, while the corresponding finite conditional probabilities form the usual
bounded martingale under \(\mu_K\).  Hence (6) is an almost-sure version of the full
conditional occupation probability while remaining continuously defined on every input.

Minimizing the quadratic form over vectors whose \(x\)-coordinate is one gives (7).
Since enlarging the exterior decreases the shorted diagonal, (7) makes the rate (8)
nonnegative and decreasing in the occupied exterior.  Conditioning at one site then
gives
\[
 \mathbb E[1_{B\setminus\{i\}\subseteq\eta}1_{i\notin\eta}c_t(i,\eta)]
 =r_t\det K_t[B]-a_t\det K_t[B\setminus\{i\}],
\]
which, after reversing time, is exactly the forward identity (10).  Inclusion monomials
span all functions on a finite cylinder, so this proves (10) for every cylinder function.

## 3. Covariant sensitivity and the use of joint invariance (Section 4)

For \(\eta\subseteq\zeta\), the polar-decomposition construction identifies the loss of
the shorted diagonal with the row sum in (11).  The range projection
\(P=\Pi_\zeta^L-\Pi_\eta^L\) lies in \(L^{1/2}\ell^2(\zeta)\).  Therefore, when
\(x\notin\zeta\), it is orthogonal to \(L^{-1/2}\delta_x\), which justifies inserting
\(L-\ell I\) in the transport coefficient.  Parseval gives the row sum exactly, and the
displayed projection estimate gives the column bound (12).  These calculations remain
valid over the complex Hilbert space because squared moduli are used.

Comparing two arbitrary configurations through their intersection yields (13).  A source
occupied in exactly one configuration is covered by the diagonal mass bounded by
\(\overline c_t\); a source vacant in both is covered by the two shorting transports.
Thus both row and column sums have the bound (14), and all target mass is supported on
mismatched sites.

The hypothesis needed in (15) is joint invariance of the pair, not separate invariance
alone.  It is present at every later use.  Every tuple of Picard iterates, the iterate/limit
pair, and the lower/upper envelope pair is obtained covariantly from the same invariant
iid drivers, hence is jointly invariant.  For such a pair, translating the term
\((e,y)\) by \(y^{-1}\) turns expected outgoing mass at the identity into expected
incoming mass there.  The incoming column is bounded by
\(C_s1_{\{U_e\ne V_e\}}\), proving (15) on every countable group without an amenability
assumption.

## 4. Uniform scalar entrance estimate (Section 5)

This entrance calculation has the strength needed by the Picard argument.  Write
\(u=t^{-1}\), \(m=\tau(Q)\), and \(q_2=\tau(Q^2)\).  Analytic functional calculus near
\(u=0\) gives, in particular,
\[
 r_t=u-mu^2+q_2u^3+O(u^4),\qquad
 a_t=pu-pmu^2+\frac p2(m^2+q_2)u^3+O(u^4),
\]
and
\[
 L_t=\ell I+uG+O(u^2),\qquad
 \ell=\frac p{1-p},\qquad
 G=\frac p{(1-p)^2}(Q-mI).
\]
Translation covariance makes every diagonal entry of \(Q\) equal to \(m\), so
\(G_{xx}=0\) at every site.  In the shorting formula, the direct diagonal is therefore
\(\ell+O(u^2)\).  For every exterior \(\eta\) not containing \(x\),
\[
 D_\eta L_t\delta_x=uD_\eta G\delta_x+O(u^2)
\]
in norm, uniformly in \(x,\eta\), and the inverse in (5) is uniformly bounded.  Hence
\(\lambda_{L_t}(x,\eta)=\ell+O(u^2)\) uniformly over all entrances.

Now
\[
 c_t=(r_t-a_t)\lambda_{L_t}-a_t.
\]
The coefficients of \(u\) and \(u^2\) in
\((r_t-a_t)\ell-a_t\) vanish because \((1-p)\ell=p\), while the error
\((r_t-a_t)O(u^2)\) is \(O(u^3)\).  This proves the first estimate in (18) uniformly.
Also \(L_t-\ell I=O(u)\) and \(L_t^{-1}=O(1)\), so
\((r_t-a_t)\kappa(L_t)=O(u^3)\).  Since \(u=s/(1-s)\), multiplication by \(s^{-2}\)
makes both the full birth rate and the sensitivity bound \(O(s)\) at the entrance.
Consequently the definitions \(b_0=C_0=0\) are jointly continuous there and \(C\) is
integrable on every \([0,S]\), \(S<1\).

Finally, on such a compact interval the kernels have common spectral gaps.  Every exact
finite DPP cylinder probability is therefore positive, continuous in \(s\), and bounded
away from zero.  These facts supply, rather than merely assert, the entrance hypotheses
used in Sections 6 and 8.

## 5. Picard fixed point on the common iid noise (Section 6)

On \([0,S]\) the sitewise proposal intensity can be truncated at a common finite rate
bound \(B\).  Each Picard iterate is consequently an adapted, covariant Borel pure-birth
path.  If \(U,V\) are jointly invariant adapted paths, a disagreement between
\(\Phi(U)\) and \(\Phi(V)\) at the root can only be initiated by a root proposal whose
mark lies between the two predictable thresholds.  Poisson compensation, followed by
(15), proves (20).  The use of the whole-path mismatch on the right is legitimate because
it dominates the instantaneous left-limit mismatch.

Iteration gives
\(D_k(t)\le A(t)^k/k!\).  The summability in \(k\) and Borel–Cantelli imply eventual
equality of successive entire coordinate paths, simultaneously over all sites and a
countable family of compact rational horizons.  The coordinatewise stabilized limit is
adapted and jointly invariant with the drivers.  Applying the same compensation estimate
to \((V^k,Z)\), then dominated convergence using the integrable function \(C\), proves
\(Z=\Phi(Z)\) almost surely.  This argument does not require monotonicity of the Picard
iteration itself and does not make an unjustified assertion at threshold ties.

## 6. Finite dependency envelopes and the four-process sandwich (Sections 7–8)

For fixed \(n\), the lower rate uses the upper configuration inside \(xD_n\) and fills the
outside with occupied sites; the upper rate uses the lower configuration truncated to
\(xD_n\).  Antimonotonicity of \(\rho\) gives the correct order of these two thresholds.

Although the ambient graph is infinite, a queried site has a finite backward dependency
tree almost surely.  A length-\(j\) decreasing-time proposal chain has expected count at
most \((BdS)^j/j!\).  This remains true for repeated sites by the Poisson factorial-moment
formula.  The tail tends to zero, so no infinite backward chain starts from any site;
finite branching then makes the dependency tree finite.  Backward recursion constructs
\((L^n,U^n)\) equivariantly, and the same argument proves
\(L^n\le Z\le U^n\) without assuming attractiveness of the original birth rates.

Uniform continuity on the compact time/configuration space gives \(\omega_n\to0\).
At the first root disagreement of the envelopes, both root coordinates are vacant, and
the threshold gap is at most
\[
 2\omega_n+|b_s(e,L^n_{s-})-b_s(e,U^n_{s-})|.
\]
The envelope pair is jointly invariant, so (15), compensation, and Gronwall give (26).

For a finite \(F\), the conditional rate (27) is defined at every finite state because all
those cylinder probabilities are positive.  Joint continuity and the positive compact
denominator make the rate bounded and continuous in time.  Conditioning (10) on the
finite state shows that \(\nu_s|_F\) satisfies exactly the finite pure-birth forward
equation with these rates.  Uniqueness of the finite forward integral equation identifies
the law of \(V^F_s\) with \(\nu_s|_F\).

The four processes \(V^F,L^n,U^n,Z\) use the same initial Bernoulli field and the same
proposal measures.  At an interior site of \(F\), every full completion of the current
finite state lies between the truncated lower exterior and the occupied-padded upper
exterior.  Antimonotonicity survives conditional averaging and proves (29).  An order
violation must therefore propagate backward through strictly earlier proposals until it
reaches \(\partial_nF\); otherwise it would generate a forbidden infinite backward
chain.  The proposal-chain count yields (30).  No invariance of the finite chain is used.

Combining this boundary estimate with the envelope disagreement estimate gives (31).
The limit order is essential and is correctly respected: first fix \(n,S,B_0\) and let
finite \(F\) exhaust \(\Gamma\), which sends the dependency distance to the boundary to
infinity; only then let \(n\to\infty\), which sends \(p_n(S)\) to zero.  Thus every finite
marginal of \(Z_s\) equals that of \(\nu_s\).  If \(\Gamma\) is finite, taking
\(F=\Gamma\) removes the boundary term directly.

## 7. Endpoint, source map, and exceptional inputs (Section 9)

Local boundedness lets the compact-horizon constructions agree as restrictions of one
path on \([0,1)\).  With \(t_s=s^{-1}-1\), the already identified marginals are
\(\mu_{K_{t_s}}\), and the fixed point path is increasing.  For
\[
 X=Z_0,\qquad Y=\bigcup_{s\in\mathbb Q,\,s<1}Z_s,
\]
finite-set inclusion probabilities converge to \(\det Q[B]\) by the norm convergence
\(K_{t_s}\to Q\).  Inclusion–exclusion then identifies the entire endpoint law as
\(\mu_Q\), and \(X\subseteq Y\).

A single label at each site can be split by a fixed Borel digit convention into the
independent Bernoulli and Poisson drivers.  The Poisson decoding is sitewise and covariant.
Every Picard iterate is a total Borel covariant function of those decoded drivers.  The
simultaneous stabilization and graphical fixed-point conditions are countable Borel,
translation-invariant conditions and hold almost surely.  On that invariant conull set
the manuscript takes the stabilized output; on its complement it outputs
\((\varnothing,\varnothing)\).  Hence the final map is total Borel and equivariant on
every input, while inclusion also holds on every input.  The countable tests do not choose
orbit representatives.

At \(p=0\), hypothesis H supplies \(Y\) and \(X=\varnothing\).  At \(p=1\),
\(\int-\log\lambda\,d\nu_Q=0\) forces \(\nu_Q=\delta_1\), and faithfulness forces
\(Q=I\); the constant all-occupied coupling applies.  These endpoint treatments use
exactly the assumptions stated in Section 1.

## 8. Final judgment

The proof closes the fixed-kernel regular-orbit theorem with the declared conditional
assumption at \(p=0\).  In particular, the entrance estimate is uniform, every invocation
of the sensitivity estimate has the required joint invariance, the finite conditional
chain is coupled to both envelopes on the original drivers, the dependency boundary is
removed in the correct order of limits, and the final source map is total and equivariant
on all inputs.  I found no critical gap or incomplete mathematical obligation within the
stated scope.
