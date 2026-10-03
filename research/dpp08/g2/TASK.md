# Optimal Bernoulli extraction from the regular-tree determinantal law

Let Gamma=C3*C3, with its Bass–Serre tree T3. Identify unoriented edges with Gamma and orient each edge from its first-factor coset to its second-factor coset. The left Gamma action is free and transitive on edges. Let Q be the gradient projection, with scalar regular kernel

Q(x,x)=2/3; Q(x,y)=(-1)^(ell(x^-1 y)+1)/(3*2^ell(x^-1 y)) for x!=y,

where ell is reduced syllable length. Write mu_Q for the DPP, equivalently the wired uniform spanning forest law on this tree.

Available input: ordinary stochastic domination Bern(1/2)^Gamma <=st mu_Q, with exact lower threshold 1/2, whereas FK(Q)=0. A root-dependent breadth-first construction proves domination. The proof and full endpoint checks are in PR #93, research/dpp07/g2/RESULT.md. Its coupling need not be Gamma-invariant. For a finite connected edge set F of size m, det Q[F]=2^-m(1+m/3). Every finite compression is positive definite, but conditional occupation at a fixed edge tends to zero when more of its complement is conditioned occupied. These facts are consistent with ordinary domination.

Main target: determine whether there is a Gamma-equivariant joint factor of regular iid uniforms producing (B,T) with B~Bern(1/2)^Gamma, T~mu_Q, and B contained in T almost surely. A construction should be total Borel and equivariant on all inputs after an invariant null-set completion. The endpoint 1/2 is the target; distinguish it explicitly from subcritical p<1/2 results.

If a joint iid factor cannot be established, settle the strictly weaker existence of a Gamma-invariant monotone joint law, or produce a rigorous obstruction to either stated target. A counterexample to one rooted algorithm does not refute existence. A constructive result for a nontrivial range of p<1/2 is useful if it isolates the remaining endpoint gap; do not rename such a partial result as the endpoint theorem.

This is a test of the gap between ordinary domination, invariant monotone coupling, and joint iid realization at a genuine optimal threshold beyond FK. The scalar kernel (1/2)I is not <= Q in Loewner order, so an ordered-kernel coupling theorem does not apply directly. Separate marginal iid samplers cannot be combined by assuming an equivariant disintegration. Compactness of joint laws preserves invariance and monotonicity but not a factor representation. A fixed root or end cannot be chosen equivariantly without proof.

Potential methods include Wilson stacks/cycle popping, equivariant thinning of the one-ended forest, matchings or mass transport, and a relative sampler conditional on critical Bernoulli clusters. These are suggestions, not granted lemmas. Bernoulli clusters at 1/2 on T3 are finite almost surely, with unbounded sizes; account for integrability and any limiting dependence. Work with the countable Gamma action specified above, not an unannounced full-automorphism action. No finitary, grand-coupling, or simultaneous-kernel requirement is imposed.

Check relevant prior results before claiming novelty. Primary sources include BLPS Uniform Spanning Forests, Section 11 (https://rdlyons.pages.iu.edu/pdf/usf.pdf), Lyons–Thom Invariant Coupling of Determinantal Measures on Sofic Groups (https://rdlyons.pages.iu.edu/pdf/couple-pub.pdf), and Ray–Spinka Characterizations of amenability through stochastic domination and finitary codings (https://arxiv.org/abs/2304.13784). Check exact hypotheses rather than citing a general invariant-domination principle.

Deliver PROVED, DISPROVED, or INCOMPLETE with the full supporting argument or the precise first unproved step. Separate classical inputs, new deductions, ordinary/invariant/factor conclusions, and the optimal endpoint. No literature novelty claim without primary evidence.
