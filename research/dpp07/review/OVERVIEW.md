# DPP comparisons: established statements and missing interfaces

Let Γ be a countable discrete group, acting regularly on itself. Write μ_Q for the determinantal law of an equivariant complex Hermitian positive contraction Q, and τ for the normalized group trace. Statements about arbitrary index actions require a separate specification of the noise source.

## Statements under review

1. **FK domination.** For each fixed Q, Bern(FK(Q)) ≤st μ_Q ≤st Bern(1−FK(I−Q)). The complete domination proof passes a full mathematical review. Its scalar examples establish uniform sharpness as a function of FK data, not optimality for every fixed nonscalar kernel.
2. **Ordered invariant coupling.** For each fixed pair A≤B there exists an invariant joint law with marginals μ_A, μ_B and X⊆Y almost surely. The full manuscript, including approximation and removal of the spectral gap, passes a mathematical review.
3. **Sharp invariant distance.** The ordered-coupling statement implies d̄(μ_A,μ_B)≤τ|A−B| for arbitrary A,B. The distance uses invariant joint laws and normalized mismatch at the identity.
4. **Marginal sampling.** The separate sampling manuscript constructs a DPP from iid labels indexed by the prescribed countable index set. Combining that result with law-level coupling existence does not yet prove a joint monotone iid factor.
5. **Joint iid coupling at the FK parameter.** For each fixed Q on the regular orbit, the revised direct construction produces X~Bern(FK(Q)), Y~μ_Q, and X⊆Y from one regular iid input. The complete revised proof passes two full mathematical reviews. When FK(Q)>0, it constructs the coupling directly; when FK(Q)=0, it uses the stated marginal-sampling hypothesis H. The output map is total Borel and equivariant on all inputs. This is a theorem for one fixed kernel, not a grand coupling or an all-kernel measurable family. See PR #92.

These are proof-review findings for the stated domains. The universal pointwise FK threshold assertion is false: a verified tree-projection counterexample and its extensions are recorded in RL01 PR #93. On amenable groups, known determinant approximation combined with the reviewed domination theorem gives pointwise equality. Joint monotone iid realization for an arbitrary ordered kernel pair, and a common construction covering that case and the FK path, remain separate obligations. Independent domain review and novelty assessment remain open.

Complementing the FK construction gives the upper FK coupling separately. The two separate endpoint constructions do not automatically give one joint triple consisting of lower Bernoulli, DPP, and upper Bernoulli configurations. The exact optimal parameter in the nonamenable tree example is also a separate problem: the task in PR #97 has no result yet.

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

The three connectivity manuscripts leave the general group-cost equality unresolved. A conditional infinite-contact construction supplies arbitrarily cheap connections if its multiscale geometric hypothesis holds. That hypothesis has not been established for general FUSF. The marginal DPP sampler supplies no missing connectivity estimate.

Two scoped reviews now support further restrictions and bookkeeping. An intersection-relation certificate based on arbitrarily small complete sections fails in the indicated product-of-free-groups example; this does not rule out all cheap repairs. Relative-cost compression and extension identities rephrase the missing bound. Separately, the cycle-defect identity and the FUSF exchange formula are valid with closed boundary operators in the unbounded-degree case. The proposed vanishing exchange budget is equivalent to the group-cost target, rather than a proved weaker lemma. These arguments are recorded with their reviews in PRs #89 and #90.

Exact attainment by a connected graph law at the Betti degree would force treeability. The group-cost target only asks for arbitrarily accurate approximation, so exact attainment must not be inserted as an extra requirement. Weak limits also require a separate connectivity argument and control of incident-edge mass escaping through group labels. None of these observations supplies the missing approximate connected construction, and no fixed-price conclusion has been obtained.

## Pointwise optimality: corrected route status

On the regular edge orbit of Γ=C3*C3 there is an equivariant projection Q with FK(Q)=0 and exact lower threshold p₋(Q)=1/2. The contraction (I+63Q)/128 is bounded between I/128 and I/2, has FK value 1/8, and dominates Bernoulli(65/256). Thus imposing a two-sided spectral gap does not restore universal pointwise optimality. A separate free-group example is injective with FK(K)=8/27 and p₋(K)=1/3.

For amenable groups, Li–Thom's existing [Theorem 1.4](https://www.math.buffalo.edu/~hfli/entdettor17.pdf) supplies the finite-compression determinant necessity, including singular endpoints. Combined with FK domination, it yields the exact thresholds in that scope. The general pointwise assertion is retired as false; determining its valid scope replaces the former attempt to prove it universally. This change does not affect the domination, invariant ordered-coupling, distance, or marginal sampling proofs. It also does not by itself settle the author's intended meaning of optimality or certify novelty.
