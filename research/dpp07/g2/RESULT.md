# Failure of pointwise Fuglede–Kadison domination thresholds

The fixed-kernel assertion is false for **ordinary stochastic domination**. An explicit counterexample is a projection on the scalar regular representation of
\[
\Gamma=C_3*C_3=\langle a,b\mid a^3=b^3=1\rangle.
\]
If \(\ell(g)\) denotes reduced syllable length, define
\[
Q(x,y)=
\begin{cases}
2/3,&x=y,\\[2mm]
\displaystyle\frac{(-1)^{\ell(x^{-1}y)+1}}{3\,2^{\ell(x^{-1}y)}},&x\ne y.
\end{cases}                                                    \tag{1}
\]
This is an equivariant orthogonal projection, and
\[
\boxed{p_-(Q)=\frac12>0=\mathrm{FK}(Q).}
\]
Furthermore \(p_+(Q)=1\), so complementation gives
\[
\boxed{p_+(I-Q)=\frac12<1=1-\mathrm{FK}(Q).}
\]
There are also counterexamples bounded away from **both** spectral endpoints, and an injective, noninvertible example on \(\mathbb F_2\) with positive FK determinant. None uses hypothesis (D).

Lyons’s Conjecture 5.7 states the FK domination inequalities and optimality, following the abelian result. The strongest pointwise interpretation is precisely what fails here; the counterexamples do not refute the two inequalities themselves. [Lyons, Conjecture 5.7](https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf)

## 1. A projection on a regular tree

Fix \(d\ge3\). On the infinite \(d\)-regular tree \(T_d=(V,E)\), orient each unoriented edge once and use counting measure on both Hilbert spaces. Define
\[
\nabla f(e)=f(e^+)-f(e^-),\qquad
\Delta=\nabla^*\nabla=dI-\mathcal A,
\]
where \(\mathcal A\) is adjacency.

The bound \(\|\mathcal A\|\le2\sqrt{d-1}<d\) has an elementary proof: orient toward a fixed end for this estimate, giving every vertex one parent and \(d-1\) children, and sum
\[
2|uv|\le(d-1)^{-1/2}|u|^2+(d-1)^{1/2}|v|^2
\]
over parent–child pairs. Thus \(\Delta\) is boundedly invertible and
\[
\Pi=\nabla\Delta^{-1}\nabla^*
\]
is the orthogonal projection onto the closed space \(H=\operatorname{ran}\nabla\).

Put
\[
r=\frac1{d-1},\quad c=\frac{d-1}{d(d-2)},\quad
\alpha=\frac{d-2}{d}.
\]
The Green kernel is
\[
G(u,v)=c\,r^{\operatorname{dist}(u,v)}.                          \tag{2}
\]
Indeed, its columns are square summable; the identities
\(dr=1+(d-1)r^2\) and \(dc(1-r)=1\) verify \(\Delta G(\cdot,v)=\delta_v\). Invertibility identifies the inverse. Consequently
\[
\Pi(e,f)=G(e^+,f^+)-G(e^+,f^-)-G(e^-,f^+)+G(e^-,f^-),           \tag{3}
\]
with \(\Pi(e,e)=2/d\).

Every finite compression \(\Pi[S]\) is positive definite. For a finitely supported edge vector \(v\),
\[
\langle\Pi v,v\rangle
=\langle\Delta^{-1}\nabla^*v,\nabla^*v\rangle.
\]
A finitely supported divergence-free flow on a tree is zero, by successively removing leaf edges of its support forest. Thus the quadratic form vanishes only for \(v=0\). In particular, every finite all-occupied event has positive probability.

## 2. A complete ordinary domination coupling

For finite occupied \(S\), Schur complements of inclusion determinants give conditional kernel
\[
B^S=\Pi-\Pi_{\cdot S}\Pi[S]^{-1}\Pi_{S\cdot}
=P_{H_S},\qquad H_S=\{h\in H:h|_S=0\}.                        \tag{4}
\]
The projection identity holds because \(\Pi[S]\) is the Gram matrix of \(\{\Pi\delta_s:s\in S\}\).

If a further finite set \(J\) is vacant, and the joint history has positive probability, then for \(e\notin S\cup J\),
\[
\mathbb P(\eta_e=1\mid\eta|_S=1,\eta|_J=0)
=B^S_{ee}+B^S_{eJ}(I-B^S[J])^{-1}B^S_{Je}
\ge B^S_{ee}.                                                 \tag{5}
\]
To verify this, use vacancy probability \(\det(I-B^S[J])\), subtract the vacancy probability on \(J\cup\{e\}\), and take a block determinant. The denominator is positive on the stipulated history; since \(B^S[J]\) is a positive contraction, \(I-B^S[J]\) is positive definite. Thus no singular conditioning is hidden. The underlying mixed-pattern determinant identity is Lyons’s Theorem 2.4; the formulas above follow by the indicated finite Schur complements. [Lyons, Theorem 2.4](https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf)

Choose a root vertex and enumerate edges breadth first. At the current edge \(e=(u,v)\), with \(v\) the child, put \(f=0\) on the parent-side component and
\[
f(w)=r^{\operatorname{dist}(v,w)}
\]
on the forward component. Then \(f\in\ell^2(V)\), \(h=\nabla f\in H\), and \(h\) vanishes on every predecessor edge. Moreover \(|h(e)|=1\) and
\[
\|h\|^2
=1+\sum_{j\ge0}(d-1)^{j+1}(r^j-r^{j+1})^2=d-1.
\]
For any predecessor history, its occupied set \(S\) satisfies \(h\in H_S\). Therefore
\[
B^S_{ee}=\|P_{H_S}\delta_e\|^2
\ge\frac{|h(e)|^2}{\|h\|^2}=r.
\]
Equation (5) proves that **every positive-probability predecessor history** has next occupation probability at least \(r\).

Use iid Uniform variables \(U_i\). If \(q_i\) is that conditional probability, recursively set
\[
\eta_i=\mathbf1\{U_i\le q_i\},\qquad
\xi_i=\mathbf1\{U_i\le r\}.
\]
Assign any value at least \(r\) on null histories. Induction gives the prescribed DPP distribution on every finite prefix, hence the entire DPP law, while \(\xi\) is iid Bernoulli \(r\) and \(\xi\le\eta\). Thus
\[
\operatorname{Bern}(r)^E\le_{\rm st}\mu_\Pi.                    \tag{6}
\]
The root and enumeration need not be invariant. That is allowed by the stated definition of domination.

## 3. Exact finite determinants

For every finite nonempty **connected** edge set \(F\), with \(m=|F|\),
\[
\boxed{\det\Pi[F]=r^m(1+\alpha m).}                            \tag{7}
\]
Here is a derivation for all shapes. Let \(U\) be its \(m+1\) vertices, \(D_F\) its oriented incidence matrix, and
\(R(u,v)=r^{\operatorname{dist}(u,v)}\). Equation (3) gives
\(\Pi[F]=D_F(cR)D_F^*\).

For any positive definite \(C\) on \(U\),
\[
\det(D_FCD_F^*)=\det C\,\mathbf1^*C^{-1}\mathbf1.               \tag{8}
\]
Indeed, tree-incidence maximal minors have absolute value one, and their signed cofactor vector is constant because \(\ker D_F=\mathbb C\mathbf1\). Expanding twice by Cauchy–Binet gives (8).

Root the finite tree. The invertible transformation with root coordinate \(z(o)\) and other coordinates
\[
\frac{z(v)-rz(\operatorname{parent}(v))}{\sqrt{1-r^2}}
\]
sends covariance \(R\) to the identity, as direct substitution of the tree distances verifies. Therefore
\[
\det R=(1-r^2)^m,\qquad
\mathbf1^*R^{-1}\mathbf1
=1+m\frac{(1-r)^2}{1-r^2}=1+\alpha m.
\]
Since \(c(1-r^2)=r\), equation (8) proves (7).

If Bernoulli \(p\) is dominated by \(\mu_\Pi\), its all-occupied cylinder on \(F\) gives
\(p^m\le r^m(1+\alpha m)\). Taking arbitrarily large connected \(F\) yields \(p\le r\). Together with (6),
\[
p_-(\Pi)=\frac1{d-1}.                                        \tag{9}
\]
In fact, (6) applies to **every** finite set, so
\[
\inf_{\varnothing\ne F\Subset E}\det\Pi[F]^{1/|F|}=r.          \tag{10}
\]
Thus the finite-window obstruction is not just a poorly chosen exhaustion.

For the upper parameter, take the full star \(S\) at a vertex \(v\). The nonzero vector \(\nabla\delta_v\) belongs to \(H\) and is supported on \(S\); hence \(\Pi[S]\) has eigenvalue one. Consequently
\[
\mu_\Pi(\eta|_S=0)=\det(I-\Pi[S])=0.
\]
Bernoulli \(p<1\) gives this decreasing event positive probability, ruling out \(\mu_\Pi\le_{\rm st}\operatorname{Bern}(p)^E\). Therefore \(p_+(\Pi)=1\).

## 4. Exactly the required regular representation

For \(\Gamma=C_d*C_d\), with factors \(A,B\), form vertices
\(\Gamma/A\sqcup\Gamma/B\) and let edge \(g\) join \(gA\) to \(gB\). Reduced-word normal form proves this is the \(d\)-regular tree. The edge action is **free and transitive**, so \(\ell^2(E)=\ell^2(\Gamma)\), not a multiple or coset representation.

Orient edges from their \(A\)-vertices to their \(B\)-vertices. Left translations preserve orientation, intertwine the gradients, and commute with the inverse Laplacian. Thus \(Q=\Pi\) is equivariant for the required action. Its specified trace is
\[
\tau(Q)=2/d.
\]
Since it is a projection, its tracial spectral measure has mass \(1-2/d\) at zero and mass \(2/d\) at one. Both masses are positive, giving
\[
\mathrm{FK}(Q)=\mathrm{FK}(I-Q)=0.                             \tag{11}
\]
For distinct edges, line-graph distance is reduced syllable length. Substitution in (3), with the bipartite orientation, gives
\[
Q(x,y)=\frac{d-2}{d}\,
\frac{(-1)^{\ell(x^{-1}y)+1}}{(d-1)^{\ell(x^{-1}y)}}.
\]
At \(d=3\) this is exactly (1). In particular, the asserted infinite matrix is a bounded projection by construction; no formal convolution series is presumed norm-convergent.

Equations (9)–(11) prove the strict lower counterexample. Inclusion-exclusion identifies the complement DPP with kernel \(I-Q\), and complementation reverses stochastic order. Thus
\[
p_+(I-Q)=1-p_-(Q)=1/2,
\]
which proves the strict upper counterexample.

## 5. The failure persists away from both spectral endpoints

For (1), set
\[
\widehat Q=\frac{I+63Q}{128}.
\]
First union \(\eta\sim\mu_Q\) with independent Bernoulli \(1/64\). The resulting DPP has kernel \((I+63Q)/64\): its complement is an independent thinning of the original complement, so the assertion follows from inclusion determinants. Under the coupling (6), this union dominates iid Bernoulli \(65/128\).

Now thin both coupled configurations using the same independent Bernoulli \(1/2\) field. The upper kernel becomes \(\widehat Q\), and the lower law is Bernoulli \(65/256\). Therefore
\[
\frac1{128}I\le\widehat Q\le\frac12I,\qquad
p_-(\widehat Q)\ge\frac{65}{256}.
\]
Its spectral masses are \(1/3\) at \(1/128\) and \(2/3\) at \(1/2\). Hence
\[
\boxed{\mathrm{FK}(\widehat Q)=\frac18<\frac{65}{256}
\le p_-(\widehat Q).}
\]
Complementation gives the equally strict upper counterexample
\[
p_+(I-\widehat Q)\le191/256<7/8=1-\mathrm{FK}(\widehat Q).
\]

## 6. A free-group counterexample with positive FK and no kernel

On \(\Gamma=\mathbb F_2=\langle a,b\rangle\), write
\[
(R_gf)(x)=f(xg),\quad T_a=R_a-I,
\]
\[
\Delta=4I-R_a-R_a^*-R_b-R_b^*,\qquad
K=T_a\Delta^{-1}T_a^*.
\]
These are operators in the right group von Neumann algebra with the normalized canonical trace. The Cayley graph is \(T_4\); its edges have two invariant classes \((g,ga)\) and \((g,gb)\). Thus \(K\) is the compression of the preceding projection onto the first class, identified with the single regular representation. It is an equivariant positive contraction.

Restriction of (6) gives \(p_-(K)\ge1/3\). The \(a\)-edge path of length \(n\) has determinant \(3^{-n}(1+n/2)\) by (7), giving the reverse bound:
\[
p_-(K)=1/3.                                                   \tag{12}
\]
It is injective because \(T_a^*f=0\) forces \(f\) to be constant on infinite right \(a\)-orbits and therefore zero in \(\ell^2\). It is not bounded below: the unit vectors
\(f_N=N^{-1/2}\sum_{j=1}^N\delta_{a^j}\) satisfy
\[
\|T_a^*f_N\|^2=2/N,\qquad
\langle Kf_N,f_N\rangle\le2\|\Delta^{-1}\|/N\longrightarrow0.
\]

For the determinant, use the **analytic** FK extension \(\Delta_\tau(T)=\exp\tau\log|T|\), whose multiplicativity includes bounded noninvertible factors in a finite von Neumann algebra. These hypotheses hold here; the singular factor \(T_a\) is not being treated as invertible. [Fuglede–Kadison, Section 5](https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-kadison/1950s/1952_DeterminantTheoryInFiniteFactors.pdf)

The trace distribution of \(R_a\) is Haar measure, since its nonzero integer moments vanish. Hence
\[
\log\Delta_\tau(T_a)
=\frac1{2\pi}\int_0^{2\pi}\log|e^{it}-1|\,dt=0,
\quad
\mathrm{FK}(K)=\mathrm{FK}(\Delta)^{-1}.                        \tag{13}
\]
The logarithmic singularity is integrable; the mean follows from the double-angle identity for \(\log\sin t\).

For the radial calculation on \(T_d\), let
\(\varphi(T)=\langle T\delta_o,\delta_o\rangle\). At \(d=4\), this is precisely the required group trace on functions of adjacency. For \(z>2\sqrt{d-1}\), set
\[
u(z)=\frac{z-\sqrt{z^2-4(d-1)}}{2(d-1)}.
\]
The radial Green calculation gives
\[
\varphi((zI-\mathcal A)^{-1})=\frac1{z-du}=\frac{u}{1-u^2}.
\]
Thus \(L(z)=\varphi(\log(zI-\mathcal A))\) has that derivative. Substitute
\(z=u^{-1}+(d-1)u\) and use \(L(z)-\log z\to0\) at infinity to obtain
\[
L(z)=-\log u-\frac{d-2}{2}\log(1-u^2).
\]
At \(z=d\), this gives
\[
\exp L(d)
=\frac{(d-1)^{d-1}}{[d(d-2)]^{(d-2)/2}}.
\]
In particular \(\mathrm{FK}(\Delta)=27/8\), so
\[
\boxed{0<\mathrm{FK}(K)=8/27<1/3=p_-(K).}
\]
No finite-quotient determinant approximation or trace on a two-copy edge representation has entered this calculation.

## 7. What is true for amenable groups, including singular endpoints

The determinant approximation below is a self-contained specialization of the existing theorem of Li–Thom, [Theorem 1.4](https://www.math.buffalo.edu/~hfli/entdettor17.pdf); it is not a new determinant-approximation theorem.

For arbitrary \(\Gamma,Q\), put
\[
\delta(Q)=\inf_{\varnothing\ne F\Subset\Gamma}
\det Q[F]^{1/|F|}.
\]
The all-occupied cylinders prove \(p_-(Q)\le\delta(Q)\). Logarithmic compression gives
\[
\tau\log(Q+\varepsilon I)
\le\frac1{|F|}\log\det(Q[F]+\varepsilon I).
\]
Indeed, the variational formula for inverses gives
\[
(PTP+sI_P)^{-1}\le P(T+sI)^{-1}P.
\]
Integrating the resolvent formula for \(\log\) reverses that inequality, and equivariance makes the diagonal of \(\log(Q+\varepsilon I)\) constant. Letting \(\varepsilon\downarrow0\) proves
\[
\mathrm{FK}(Q)\le\delta(Q).                                   \tag{14}
\]

Suppose now that \(\Gamma\) admits a right Følner sequence \(F_n\). Write \(P_n=P_{F_n}\) and \(q(g)=Q(g,1)\). Then
\[
\frac{\|(I-P_n)QP_n\|_{\rm HS}^2}{|F_n|}
=\sum_g|q(g)|^2\frac{|\{x\in F_n:xg\notin F_n\}|}{|F_n|}
\longrightarrow0.                                            \tag{15}
\]
Here \(Q(x,y)=q(y^{-1}x)\); dominated convergence uses \(q\in\ell^2(\Gamma)\).

For fixed \(k\), this implies
\[
|F_n|^{-1}\operatorname{Tr}(Q[F_n]^k)\longrightarrow\tau(Q^k).
\]
Explicitly, with \(P=P_n\), \(R=PQP\), and \(M_k=PQ^kP-R^k\),
\[
M_{k+1}=RM_k+PQ(I-P)Q^kP.
\]
The trace norm of the last term is at most
\(k\sqrt2\|(I-P)QP\|_{\rm HS}^2\), by the commutator expansion of \([Q^k,P]\) and \(\|Q\|\le1\). Induction proves the assertion.

Polynomial approximation now gives, for each \(\varepsilon>0\),
\[
\frac1{|F_n|}\log\det(Q[F_n]+\varepsilon I)
\longrightarrow\tau\log(Q+\varepsilon I).
\]
The **unregularized** normalized log determinants are bounded below by \(\tau\log Q\), by compression, and their limsup is at most the displayed limit for every \(\varepsilon>0\). Since
\(\tau\log(Q+\varepsilon I)\downarrow\tau\log Q\),
\[
\boxed{\frac1{|F_n|}\log\det Q[F_n]\longrightarrow\tau\log Q,}   \tag{16}
\]
including value \(-\infty\). No unproved uniform integrability of logarithms is used.

Consequently, for every countable amenable group,
\[
\delta(Q)=\mathrm{FK}(Q),\qquad
p_-(Q)\le\mathrm{FK}(Q),\qquad
p_+(Q)\ge1-\mathrm{FK}(I-Q).
\]
These necessity statements are unconditional; **equalities here follow conditional on (D)**. This is not a proof of (D).

The nonamenable obstruction is exact: for (1), equation (10) gives
\[
\inf_{\varnothing\ne F\Subset\Gamma}\det Q[F]^{1/|F|}
=1/2>0=\mathrm{FK}(Q).
\]
Even the infimum over every finite window cannot recover FK.

## 8. Conditional domination and boundary checks

The coupling in §2 does not imply a positive lower bound under arbitrary boundary conditioning. For a fixed edge \(e\), let finite \(S_n\uparrow E\setminus\{e\}\). Equation (4) gives
\[
\mathbb P(\eta_e=1\mid\eta|_{S_n}=1)
=\|P_{H_{S_n}}\delta_e\|^2\longrightarrow0.
\]
Indeed, the decreasing subspaces intersect in \(H\cap\mathbb C\delta_e=\{0\}\): an \(\ell^2\) vertex potential with gradient supported on one edge is constant on each of two infinite components and must vanish. Projections onto decreasing closed subspaces converge strongly to the intersection projection. All the conditioning events have positive probability.

This distinguishes ordinary domination from the full-conditioning notion separated in Lyons–Steif, Definition 5.15 and Theorem 5.16. No invariant coupling is asserted. [Lyons–Steif, Definition 5.15 and Theorem 5.16](https://rdlyons.pages.iu.edu/pdf/dyn.pdf)

For a finite group, \(\tau\) is normalized matrix trace and the whole-space occupation event proves the necessity \(p_-\le(\det Q)^{1/|\Gamma|}\); together with (D), both equalities follow. Proper nonzero finite-group projections give \(p_-=0,p_+=1\) directly, with zero and identity handled separately.

For \(\mathbb Z^k\), Lyons–Steif Theorems 5.3 and 5.11 give unconditional, pointwise necessary-and-sufficient statements for every measurable symbol \(f:\mathbb T^k\to[0,1]\), including singular endpoints. For example \(f(t)=|1-e^{it}|^2/4\) on \(\mathbb Z\) is injective but noninvertible, with parameters \(p_-=1/4,p_+=3/4\). [Lyons–Steif](https://rdlyons.pages.iu.edu/pdf/dyn.pdf)

Finally \(Q=pI\) gives exactly Bernoulli \(p\) for every group, including \(p=0,1\). Those scalar equalities do not establish pointwise optimality for other kernels.

**The frozen universal assertion is therefore false, not merely unproved.**

## 9. Prior work and interpretation

The tree construction uses classical wired-spanning-forest structure. In Benjamini–Lyons–Peres–Schramm, [Section 11 and the proof of Theorem 11.1](https://rdlyons.pages.iu.edu/pdf/usf.pdf), Wilson's construction couples independent parent-hitting percolation below the wired forest. On a regular tree the hitting parameter is the reciprocal of the forward degree. The Hilbert-space argument above supplies a separate derivation of this domination; the domination mechanism itself is not claimed as new.

The free product C3*C3 is sofic, as follows from closure under free products of sofic groups; see Elek–Szabó, [Theorem 1](https://www.ams.org/proc/2011-139-12/S0002-9939-2011-11222-X/S0002-9939-2011-11222-X.pdf), with trivial amalgamation. Thus restricting the pointwise assertion to sofic groups does not remove the counterexample.

The mathematical conclusion is a refutation of the explicit pointwise-threshold assertion. It preserves the two FK domination inequalities and their scalar class-level sharpness. The word “optimal” in the source question must be discussed with these distinctions visible; the counterexample alone does not establish the author's intended interpretation. No priority or exhaustive novelty claim is made.
