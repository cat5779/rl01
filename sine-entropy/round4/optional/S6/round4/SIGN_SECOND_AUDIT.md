STATUS: CORRECT

# Independent second audit of the S6 sign theorem

## Scope and verdict

I independently audited Sections 1--4 of the frozen source
`S6_round4_correlated_reference_realq/proof.md`. I did not use other reviewers'
conclusions and did not audit the standalone real-\(q\) claims in Sections 5--8.
I treated the three premises explicitly granted for this audit as inputs:

1. the arbitrary-contraction bound \(H''\le -n/50\) at
   \(c_0=37/40\) throughout the legal interior;
2. the exact DPP/channel identity; and
3. value convergence of the finite sine entropy to its entropy rate.

Within that scope, the proof establishes, for every finite Hermitian positive
contraction \(Q\), every \(n\ge1\),
\(c\in[37/40,37/40+10^{-13}]\), and
\(|a-(1-c)/2|\le1/200\),

\[
\frac{d^2}{da^2}H(\mathrm{DPP}(aI+cQ))\le-\frac n{200}.
\]

The finite-dimensional inequality also passes to the sine entropy rate by
ordinary value convergence, with Jensen bonus
\(t(1-t)(a_1-a_0)^2/400\). No differentiation of the limiting rate is
used.

## Verification details

### 1. Exact full-configuration pencil (lines 141--181)

For \(T=S^c\), diagonal multilinearity gives

\[
(-1)^{|T|}\det(K-D_T)
=\sum_{B\subseteq T}(-1)^{|B|}\det K_{S\cup B}=p_K(S).
\]

The comparison matrices \(\delta I-D_T\) and
\((1-\delta)I-D_T\), together with ordered-eigenvalue monotonicity,
put exactly \(|T|\) eigenvalues of \(A_S=K-D_T\) in
\([-(1-\delta),-\delta]\) and all remaining eigenvalues in
\([\delta,1-\delta]\). Thus every atom is strictly positive,
\(p_K(S)=|\det A_S|\), and
\(\delta^2I\le A_S^2\le(1-\delta)^2I\). This proves the
full-atom entropy formula (2.6); it is not a spectral-entropy substitution.

### 2. Degree cancellation under the moving DPP law (lines 183--244)

Writing \(D_S=\mathrm{diag}(y_1,\ldots,y_n)\), the pencil is affine
in \(x,y\), so \(A_S^2\) has total degree at most two and
\(\mathrm{Tr}\,T_m(X_S)\) has total degree at most \(2m\).
Boolean reduction only lowers degree. Each reduced monomial
\(x^j\prod_{i\in V}y_i\) averages to
\(x^j\det(xI+dQ)_V\), whose degree is at most
\(j+|V|\). Consequently the expectation polynomial still has degree at
most \(2m\), even though individual atom probabilities have degree up to
\(n\). No independence of sites is introduced.

The scalar Chebyshev identity in (2.10) is correct for
\(r=(1-\delta)/(1+\delta)\). Functional calculus gives
\(|\mathrm{Tr}\,T_m(X_S)|\le n\), hence the uniform,
dimension-free coefficient bound \(\|u_m\|_\infty\le r^m/m\).

### 3. Nested Bernstein estimate and differentiated convergence (lines 252--326)

For \(x=x_0+(\ell/2)\cos\theta\), direct differentiation gives

\[
P''(x)=\frac{T''(\theta)}{(\ell/2)^2\sin^2\theta}
-\frac{\cos\theta\,T'(\theta)}
{(\ell/2)^2\sin^3\theta}.
\]

On the concentric inner interval,
\(|\sin\theta|\ge\sigma\). Applying the trigonometric
Bernstein inequality first to \(T\) and then to \(T'\) yields
(3.2) with the stated constants. The primary source, Queffélec--Zarouf,
*On Bernstein's inequality for polynomials*, arXiv:1903.10801, states exactly
\(\|T'\|_\infty\le D\|T\|_\infty\) for a
degree-\(D\) trigonometric polynomial.

For a tail term with degree \(2m\) and size
\(Ar^m/m\), (3.2) bounds its second derivative by a constant times
\(A(mr^m+r^m)\). The resulting series is summable uniformly on the inner
interval. This justifies termwise twice differentiation and the passage from
the value bound to (3.6). The displayed formulas for \(V_M,S_{0,M},S_{1,M}\)
are the correct geometric tail sums.

### 4. Complement reduction and contrast coupling (lines 337--411)

If \(\mathrm{Tr}(Q)/n>1/2\), complementing the DPP changes
\(aI+cQ\) to
\((1-a-c)I+c(I-Q)\). Configuration complementation is a bijection, so
entropy is preserved, and the affine change has unit absolute slope, so the
second derivative is preserved. In either case the selected contraction
\(Q_*\) has normalized trace at most \(1/2\). The centered strip is
invariant under this transformation.

The common-uniform channel coupling is monotone. A mismatch at site \(i\)
has exact probability \((c-c_0)(Q_*)_{ii}\), and either output is determined
by the other output plus the mismatch vector. Therefore both conditional
entropies are at most the mismatch-vector entropy, which is at most the sum of
its binary marginal entropies. Concavity, monotonicity near zero, and
\(\mathrm{Tr}(Q_*)/n\le1/2\) give
\(\|F_c-F_{c_0}\|_\infty\le
b((c-c_0)/2)\le2\times10^{-12}\), including both contrast endpoints.

### 5. Domain, constants, and curvature transport (lines 366--460)

The outer interval
\(I_c=[9/500,1-c-9/500]\) is common to amplitudes \(c\) and
\(c_0\); both kernels have spectrum in
\([9/500,1-9/500]\). The target strip lies strictly inside this interval.
At the worst endpoint \(c=c_1\), the outer length is
\(0.0389999999999>0.0389\), while

\[
\sigma^2>1-(100/389)^2=141321/151321>(24/25)^2.
\]

I independently recomputed (3.6) from the displayed rational parameters
\(r=491/509\), \(M=768\), \(A=2\), and
\(\epsilon=1/(5\times10^{11})\). The result is

\[
\mathcal R=0.014503101814653298398674197427\ldots<3/200.
\]

Thus the granted \(c_0\) curvature bound transports as
\(F_c''\le-1/50+\mathcal R<-1/200\). The proof states the slightly
weaker non-strict bound required by the theorem.

### 6. Rate-level Jensen passage (lines 462--479)

Twice integrating \(f''\le-1/200\) gives the finite-dimensional strong
concavity bonus \((1/400)t(1-t)(a_1-a_0)^2\). The supplied value convergence
can then be applied separately at \(a_0,a_1,a_t\), so (4.14) follows without
any derivative-limit interchange.

## Limits of this certification

This report certifies only the stated Sections 1--4 theorem and its rate Jensen
consequence, conditional on the three granted premises above. It makes no
claim about novelty, Sections 5--8, the wider contrast range
\(37/40<c<1\), or the full legal \(a\)-interval. The rational computation
was used to verify the displayed arithmetic; the general proof remains the
analytic argument described above.
