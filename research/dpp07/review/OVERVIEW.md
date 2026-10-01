# DPP comparisons: established statements and missing interfaces

Let Γ be a countable discrete group, acting regularly on itself. Write μ_Q for the determinantal law of an equivariant complex Hermitian positive contraction Q, and τ for the normalized group trace. Statements about arbitrary index actions require a separate specification of the noise source.

## Statements under review

1. **FK domination.** For each fixed Q, Bern(FK(Q)) ≤st μ_Q ≤st Bern(1−FK(I−Q)). The complete domination proof passes a full mathematical review. Its scalar examples establish uniform sharpness as a function of FK data, not optimality for every fixed nonscalar kernel.
2. **Ordered invariant coupling.** For each fixed pair A≤B there exists an invariant joint law with marginals μ_A, μ_B and X⊆Y almost surely. The full manuscript, including approximation and removal of the spectral gap, passes a mathematical review.
3. **Sharp invariant distance.** The ordered-coupling statement implies d̄(μ_A,μ_B)≤τ|A−B| for arbitrary A,B. The distance uses invariant joint laws and normalized mismatch at the identity.
4. **Marginal sampling.** The separate sampling manuscript constructs a DPP from iid labels indexed by the prescribed countable index set. Combining that result with law-level coupling existence does not yet prove a joint monotone iid factor.

These are proof-review findings for the stated domains. Pointwise FK optimality on arbitrary infinite groups, joint monotone iid realization, and a common construction proving all the statements remain separate obligations. Independent domain review and novelty assessment remain open.

## An exact equivalence between ordered coupling and the distance bound

Suppose the sharp distance bound holds for every pair of kernels. For A≤B, every invariant coupling has

\[
\mathbb P(X_e\ne Y_e)=\tau(B-A)+2\mathbb P(X_e=1,Y_e=0).
\]

The space of invariant couplings with prescribed marginals is nonempty and compact: the product law is invariant, and both marginal constraints and invariance are weakly closed on the compact configuration-pair space. The mismatch functional is continuous because it is a cylinder function. It therefore attains its minimum. The asserted upper bound, together with the displayed identity, forces a minimizing law to have P(X_e=1,Y_e=0)=0. Invariance and countability give X⊆Y simultaneously at all sites almost surely.

Conversely, ordered invariant couplings yield equality d̄(μ_A,μ_B)=τ(B−A) on ordered pairs. Relative independent gluing over a common marginal preserves invariance and proves the triangle inequality. Put D=B−A=D₊−D₋. For a positive integer N define

\[
R_k=\frac{(N-k)A+kB}{N+1}\quad(0\le k\le N),
\qquad S_k=R_k+\frac{D_+}{N+1}\quad(0\le k<N).
\]

All these operators are positive contractions: R_k≤N I/(N+1) and 0≤D₊≤I. Moreover S_k−R_k=D₊/(N+1) and S_k−R_{k+1}=D₋/(N+1). The ordered steps from A down to R₀, then via S_k and R_{k+1}, and finally from R_N up to B give

\[
\bar d(\mu_A,\mu_B)
\le\frac{\tau(A)+\tau(B)+N\tau|A-B|}{N+1}.
\]

Letting N tend to infinity gives the sharp bound. Thus these two statements are equivalent as universal assertions over the regular-orbit kernel class. Neither direction establishes an iid representation of the coupling.

## FK domination is not a direct Loewner-order application

On Γ=Z/2, take

\[
Q=\begin{pmatrix}1/2&1/4\\1/4&1/2\end{pmatrix}.
\]

Its eigenvalues are 1/4 and 3/4, whereas FK(Q)=√3/4>1/4. Hence FK(Q)I is not ≤Q. The FK stochastic comparison may hold, but applying an ordered-kernel coupling theorem to this pair is invalid.

For a finite group of order n, ordinary domination Bern(p)≤st μ_Q forces pⁿ≤det Q by the full-occupation event. Thus p≤FK(Q); complementation yields the matching upper necessity. This proves fixed-kernel optimality on finite groups once domination is known. An infinite group has no finite full-occupation cylinder, so this argument supplies no infinite-group necessity result.

## Source scope

The fixed-symbol equivalences in Lyons–Steif, [Theorem 5.11](https://rdlyons.pages.iu.edu/pdf/dyn.pdf), support reading optimality as a pointwise threshold. Lyons's [Conjecture 5.7](https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf) includes optimality and appears in a subsection initially fixing a sofic group; an all-countable-group theorem should be identified as such an extension. The invariant-coupling theorem and Bernoulli-factor question in [Lyons–Thom](https://rdlyons.pages.iu.edu/pdf/couple-pub.pdf) concern distinct conclusions.

## Connectivity applications

The two connectivity manuscripts leave the general group-cost equality unresolved. A conditional infinite-contact construction supplies arbitrarily cheap connections if its multiscale geometric hypothesis holds. That hypothesis has not been established for general FUSF. A separate cycle-space/exchange formulation requires its own proof and source audit. The marginal DPP sampler supplies no missing connectivity estimate.
