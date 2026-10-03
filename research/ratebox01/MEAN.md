# Bounded all-coupling Osgood mean criterion

This is the bounded-rate specialization of the complete Osgood/compatible-strong argument used by DYNAMIC.md. It imports ordinary weak existence and the bounded compatible product-Poisson completion from [RESULT.md Section 1 and Appendix A](RESULT.md), without assuming that the input weak law is invariant. It provides no finite certificate by itself.

For attribution, conditional compatible weak/strong extraction is classical: Thomas G. Kurtz, [Weak and strong solutions of general stochastic models](https://arxiv.org/abs/1305.6747), Theorem 1.5, Lemmas 2.11--2.12, and Proposition 2.13. The required conditional-copy argument is supplied below. No priority claim is made.

## 1. Exact sufficient condition

Let I be a countable Gamma-set. Assume covariant Borel pure-birth rates bounded by a finite constant M, an ordinary prescribed-marginal weak law, and no simultaneous positive-time births. Let mu_t be the given invariant DPP marginals. Suppose there are:

- a continuous nondecreasing omega:[0,1]->[0,infinity), with omega(0)=0, omega(r)>0 for r>0, and integral_(0,1/2) dr/omega(r)=infinity;
- a nonnegative L in L1[0,1];
- one Lebesgue-null time set outside which EVERY coupling (U,V) with both laws mu_t satisfies

    sup_i E|a_i(t,U)-a_i(t,V)|
      <= L(t) omega(sup_j P(U_j != V_j)).                       (UC)

No invariance of the coupling is assumed. This is a property of the given rates and known marginal laws, not a condition on an unknown invariant process.

Then the prescribed-marginal martingale law is unique. It is consequently invariant for every countable Gamma. It admits a causal strong relative realization from X_0 and independent product Poisson noise, with a total Borel exactly equivariant version after a null-set convention. Uniqueness is asserted within the prescribed mu_t class, not for all other initial laws or other marginal curves.

All Poisson extensions below use the bounded-rate completion proved in RESULT.md Appendix A, which supplies genuine joint product noise relative to the full X-past. No simultaneous births is part of the weak-existence input; it is not inferred from single-site compensators.

## 2. Pathwise uniqueness for compatible prescribed-marginal solutions

Suppose X^1,X^2 share X_0 and the same product PRM field N in a common filtration in which future N is independent of the past. Each solves

    X_i^k(t)-X_i(0)=integral_(0,t] 1_{u<=a_i(s,X^k_(s-))}N_i(ds,du),

and each has marginals mu_t. For each coordinate, a discrepancy at time t can occur only after at least one proposal with different acceptance indicators. Thus Poisson compensation gives

    P(X_i^1(t)!=X_i^2(t))
       <= integral_0^t E|a_i(s,X^1_(s-))-a_i(s,X^2_(s-))|ds.     (1)

The integrand is dominated for a fixed i by the two coordinate rates with finite integrated mean. For this bounded specialization, coordinate integrability follows immediately from M.

For each deterministic s>0, X^k(s-)=X^k(s) almost surely as an E-valued variable. To see this, each coordinate has absolutely continuous expected birth count, from its compensator; hence no jump at a deterministic time. Countability handles all coordinates at this fixed s. Therefore the pair of left states in (1) has both marginals mu_s.

Let delta(t)=sup_i P(X_i^1(t)!=X_i^2(t)). This is measurable by countability. Taking the supremum in (1), using (UC), and moving the supremum inside the nonnegative integral yields

    delta(t)<=integral_0^t L(s)omega(delta(s))ds.                (2)

Extend omega constantly beyond 1 if needed. Set D(t) equal to the right side. Then D is nonnegative and absolutely continuous, D(0)=0, delta<=D, and

    D'(t)<=L(t)omega(D(t))

almost everywhere. For eta>0, monotonicity gives

    integral_eta^{D(t)+eta} dr/omega(r)
      = integral_0^t D'(s)/omega(D(s)+eta)ds
      <= integral_0^t L(s)ds.

If D(t)>0, the left side tends to infinity as eta decreases to zero by the Osgood assumption, a contradiction. Thus D=delta=0. The paths agree at all rational times and at the endpoint almost surely, simultaneously at every coordinate; cadlag paths then give X^1=X^2 as whole paths.

This argument applies to arbitrary compatible couplings with the specified marginals. It does not invoke a jointly invariant pair.

## 3. Conditional copies retain genuine common-noise compatibility

Take any ordinary prescribed-marginal law P and extend it by RESULT.md Appendix A. Write Z=(X_0,N), with input law nu=mu_0 tensor product(PRM). These spaces and the coordinatewise path space are standard Borel. Let k(z,dX) be a regular conditional distribution of X given the whole Z.

Fix a deterministic s and let Z_s=(X_0,N restricted through s). The future part N_(s,1] is independent of the enlarged X/noise past by that completion. Consequently for every bounded Borel function f of X through s,

    E[f(X through s)|Z] = E[f(X through s)|Z_s].                (3)

For completeness, test this identity against a product of a bounded function of Z_s and a bounded function of future noise. Independence of future noise from the joint past factors its latter expectation. Such products generate sigma(Z); a monotone class proves (3). A countable generating family for each prefix path sigma field supplies the corresponding conditional-kernel identity. It is an identity at each s, not an assertion of a universal choice of uncountably many conditional versions.

Now, conditional on Z=z, draw two independent whole paths with distribution k(z,.) and k(z,.). Their conditional joint past distribution through s is the product of the two prefix kernels. By (3) each factor depends only on Z_s. Since future N is independent of Z_s, it is independent of the joint past of the two copies, X_0, and N through s. This proves the full product-Poisson conditional law in their common raw past filtration. The finite-window count martingales preserve this property after completion/right-continuous augmentation, by the integrably dominated count argument in RESULT.md Appendix A.

Both copies satisfy the original pathwise integral equation: it is a probability-one relation between X and Z, hence holds under k(z,.) for nu-almost every z and under its product kernel. Each copy's unconditional marginal law is the original P, so it has every prescribed mu_t and the required coordinate integrability. They share X_0 by construction. Section 2 therefore applies and makes them identical.

For a probability kernel on a standard Borel space, two conditionally independent draws being equal almost surely implies the kernel is Dirac almost everywhere. One elementary proof tests a countable separating family C: k(z,C)(1-k(z,C))=0 almost everywhere. All probabilities are zero or one on one common conull set, and a probability on a standard Borel space with that property is a point mass. Thus k(z,.)=delta_{F(z)} for a Borel map F, nu-almost surely. Define F arbitrarily by the constant initial path outside this set to make it total.

Equation (3) then implies that every prefix F(Z) through s is measurable in the completed sigma field of Z_s. Thus F is a causal strong realization under nu, although its all-input null-set convention need not be pointwise causal on exceptional inputs.

## 4. Law uniqueness, invariance, and the all-input equivariant version

Apply Section 3 to any two ordinary prescribed-marginal laws P_1,P_2, obtaining F_1,F_2 with the same input law nu. Couple them using the same Z. Their prefixes are measurable in its completed past filtration, so N is a product PRM in this common filtration; both output paths have their prescribed marginals and solve the equation. Section 2 gives F_1(Z)=F_2(Z). Hence P_1=P_2.

The translate of any such law by any gamma in Gamma is again a prescribed-generator law with the same mu_t, because rates are covariant and the DPP marginals invariant. Uniqueness therefore proves P itself invariant, without amenable averaging. the coordinatewise Poisson-completion construction from this now-invariant P is jointly invariant in (X,X_0,N).

The Dirac conditional map F consequently satisfies

    F(gamma z)=gamma F(z)

for nu-almost every z, for each gamma. This follows by translating the joint invariant distribution and comparing its two Dirac conditional kernels. Take the intersection over all gamma of these Borel equality sets. It is conull and invariant: if the equality holds for every gamma at z, it also holds for every gamma at eta z, using the equality at eta and gamma eta. Within this equality set also impose the Borel property that F(z) has initial state z_0; this property is conull and invariant there, by the equalities just imposed. On the resulting invariant set use F, and off it use the constant path equal to the supplied initial state z_0. The fallback is exactly equivariant. This gives a total Borel exactly equivariant relative map with the correct path law under nu.

If an independent equivariant iid sampler of mu_0 is separately supplied, composing it with this relative map yields an iid realization. That extra sampler is not manufactured by (UC). None of this implies an all-initial-law martingale uniqueness theorem.
