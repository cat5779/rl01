# Independent mathematical audit of the tree projection counterexample

## Verdict

**STATUS: CORRECT.**

This verdict is restricted to §§1–5 and the core conditioning claim in §8.  In
particular, it certifies the counterexample on
\(\Gamma=C_3*C_3\), the exact values
\[
 \mathrm{FK}(Q)=0,\qquad p_-(Q)=\tfrac12,\qquad p_+(Q)=1,
\]
and the spectrally two-sided perturbation
\[
 \widehat Q=\frac{I+63Q}{128},\qquad
 \mathrm{FK}(\widehat Q)=\tfrac18,
 \qquad p_-(\widehat Q)\ge \frac{65}{256}.
\]
No conclusion is made here about the free-group determinant calculation in §6
or the Følner/amenable extension in §7.

## 1. Tree projection and finite compressions

On the \(d\)-regular tree, \(\|\mathcal A\|\le 2\sqrt{d-1}<d\), so
\(\Delta=dI-\mathcal A\) is boundedly invertible.  Consequently
\[
 \Pi=\nabla\Delta^{-1}\nabla^*
\]
is the orthogonal projection onto \(H=\operatorname{ran}\nabla\); the range is
closed because \(\nabla^*\nabla=\Delta\) is bounded below.  The proposed Green
kernel
\[
 G(u,v)=\frac{d-1}{d(d-2)}(d-1)^{-\operatorname{dist}(u,v)}
\]
satisfies the radial harmonic equation off the pole and the correct equation at
the pole, and its columns lie in \(\ell^2\).  Thus the displayed formula for
\(\Pi(e,f)\), including \(\Pi(e,e)=2/d\), follows.

Every finite compression \(\Pi[S]\) is positive definite.  Indeed,
\[
 \langle \Pi v,v\rangle
 =\langle \Delta^{-1}\nabla^*v,\nabla^*v\rangle,
\]
and a finitely supported divergence-free edge flow on a tree vanishes: a leaf
of the finite support forces its incident coefficient to vanish, and induction
removes the support.  Hence every finite all-occupied event used later has
strictly positive probability.

## 2. Ordinary stochastic domination

After conditioning a finite set \(S\) to be occupied, the conditional kernel is
the Schur complement
\[
 B^S=\Pi-\Pi_{\cdot S}\Pi[S]^{-1}\Pi_{S\cdot}=P_{H_S},
 \qquad H_S=\{h\in H:h|_S=0\}.
\]
If a disjoint finite set \(J\) is additionally conditioned vacant and that
mixed history has positive probability, a block determinant gives
\[
 \mathbb P(\eta_e=1\mid S\text{ occupied},J\text{ vacant})
 =B^S_{ee}+B^S_{eJ}(I-B^S[J])^{-1}B^S_{Je}\ge B^S_{ee}.
\]
There is no singular inverse here: positivity of the vacancy probability is
\(\det(I-B^S[J])>0\), and a positive semidefinite matrix with positive
determinant is positive definite.

The breadth-first argument also has the required quantifiers.  Root the tree
and enumerate edges in nondecreasing depth, with a finite ordering within each
level.  For the current parent-child edge \(e=(u,v)\), put \(f=0\) on the
parent component and \(f(w)=r^{\operatorname{dist}(v,w)}\) on the forward
component, where \(r=(d-1)^{-1}\).  Then \(h=\nabla f\) is supported on \(e\)
and edges strictly below \(e\).  Thus it vanishes simultaneously on every
earlier BFS edge, including earlier edges at the same depth.  Moreover
\[
 |h(e)|=1,
 \qquad \|h\|^2
 =1+\sum_{j\ge0}(d-1)^{j+1}(r^j-r^{j+1})^2=d-1.
\]
For every positive-probability predecessor history, its occupied part \(S\)
therefore satisfies \(h\in H_S\), and
\[
 B^S_{ee}=\|P_{H_S}\delta_e\|^2
 \ge \frac{|\langle\delta_e,h\rangle|^2}{\|h\|^2}=r.
\]
Combining this with the preceding vacancy formula bounds the next conditional
occupation probability by \(r\) for every positive-probability full history.
The sequential common-uniform construction then gives the correct law on every
finite prefix and an iid Bernoulli-\(r\) field below it.  Values assigned on
null histories are irrelevant to all finite-prefix distributions.  Hence
\[
 \operatorname{Bern}(r)^E\le_{\mathrm{st}}\mu_\Pi.
\]
This is ordinary stochastic domination; neither an invariant coupling nor a
uniform lower bound after arbitrary boundary conditioning is used.

## 3. Exact determinant obstruction for every connected shape

Let \(F\) be any finite nonempty connected edge set.  Because the ambient graph
is a tree, its incident vertices form a finite tree with \(|F|+1\) vertices;
there is no restriction to paths or balls.  With \(m=|F|\), its incidence
matrix \(D_F\), and \(R(u,v)=r^{\operatorname{dist}(u,v)}\), one has
\(\Pi[F]=D_F(cR)D_F^*\).  For any positive definite \(C\) on the incident
vertices,
\[
 \det(D_FCD_F^*)=\det(C)\,\mathbf1^*C^{-1}\mathbf1.
\]
This follows from Cauchy--Binet and the fact that every maximal incidence minor
of a finite tree has absolute value one, with cofactor vector spanning
\(\ker D_F=\mathbb C\mathbf1\).

Rooting this arbitrary finite tree and applying the triangular innovation map
\(z(v)\mapsto(z(v)-rz(\operatorname{parent}(v)))/\sqrt{1-r^2}\) gives
\[
 \det R=(1-r^2)^m,
 \qquad \mathbf1^*R^{-1}\mathbf1
 =1+m\frac{(1-r)^2}{1-r^2}=1+\frac{d-2}{d}m.
\]
Since \(c(1-r^2)=r\), this proves for every connected shape
\[
 \det\Pi[F]=r^m\left(1+\frac{d-2}{d}m\right).
\]
The all-occupied event therefore forces any dominated Bernoulli parameter
\(p\) to satisfy \(p\le r\) after taking connected sets of arbitrarily large
size.  Together with the coupling, \(p_-(\Pi)=r\).

For the full star at a vertex, \(\nabla\delta_v\) is a nonzero vector in
\(H\) supported on that star.  Hence the star compression has eigenvalue one,
so its all-vacant probability is zero.  Since Bernoulli \(p<1\) assigns that
decreasing event positive probability, \(p_+(\Pi)=1\).

## 4. The regular representation and the explicit kernel

For \(\Gamma=C_d*C_d\), with factors \(A,B\), the Bass--Serre vertices are
\(\Gamma/A\sqcup\Gamma/B\), and the edge indexed by \(g\) joins \(gA\) to
\(gB\).  The edge stabilizer is \(A\cap B=\{1\}\) by reduced normal form, and
there is one edge orbit.  Thus the edge action is free and transitive and
\(\ell^2(E)\) is exactly one scalar regular representation, with no hidden
stabilizer or orbit multiplicity.

Orienting every edge from its \(A\)-vertex to its \(B\)-vertex is preserved by
left translation, so \(Q=\Pi\) is equivariant.  Two edge indices \(x,y\) have
line-graph distance equal to the reduced syllable length
\(\ell(x^{-1}y)\).  Substitution of the four endpoint distances in the Green
second difference gives, for \(x\ne y\),
\[
 Q(x,y)=\frac{d-2}{d}
 \frac{(-1)^{\ell(x^{-1}y)+1}}{(d-1)^{\ell(x^{-1}y)}}.
\]
Thus at \(d=3\) the sign and coefficient in the claimed explicit kernel are
correct, while \(Q(x,x)=2/3\).  This formula is derived from a bounded
projection and does not require norm convergence of a formal convolution
series.

The canonical trace is \(\tau(Q)=2/d\).  Since \(Q\) is a projection, its
tracial spectral measure has masses \(1-2/d\) at zero and \(2/d\) at one.
For \(d=3\), therefore,
\[
 \mathrm{FK}(Q)=0,
 \qquad p_-(Q)=\tfrac12,
 \qquad p_+(Q)=1.
\]
Complementing configurations changes the DPP kernel from \(Q\) to \(I-Q\)
and reverses stochastic order, so also
\(p_+(I-Q)=1-p_-(Q)=1/2\).

## 5. Spectral-gap perturbation

Union with an independent Bernoulli-\(1/64\) field transforms the kernel by
\[
 Q\longmapsto I-(1-1/64)(I-Q)=\frac{I+63Q}{64}.
\]
Under the established coupling with Bernoulli \(1/2\), the lower field becomes
Bernoulli
\[
 1-(1-1/2)(1-1/64)=65/128.
\]
Common independent thinning by \(1/2\) preserves the pointwise order and
transforms the upper kernel into
\(\widehat Q=(I+63Q)/128\), while the lower field becomes iid Bernoulli
\(65/256\).  Therefore
\[
 p_-(\widehat Q)\ge65/256.
\]
The two spectral values are \(1/128\) and \(1/2\), with tracial masses \(1/3\)
and \(2/3\).  Hence
\[
 \mathrm{FK}(\widehat Q)
 =(1/128)^{1/3}(1/2)^{2/3}=1/8<65/256.
\]

## 6. Boundary-conditioning check

For finite \(S_n\uparrow E\setminus\{e\}\), all events that every edge of
\(S_n\) is occupied have positive probability by positive definiteness of the
finite compressions.  Their conditional occupation probabilities are
\[
 \|P_{H_{S_n}}\delta_e\|^2.
\]
The subspaces decrease to \(H\cap\mathbb C\delta_e\).  A gradient supported on
one edge comes from a potential constant on each of the two infinite
components.  Square summability of the potential forces both constants to be
zero, so the intersection is \(\{0\}\).  Strong convergence of projections
onto decreasing closed subspaces therefore makes these conditional
probabilities tend to zero.  This correctly separates ordinary stochastic
domination from domination uniformly under arbitrary boundary conditioning.

## Scope of certification

The audited core is self-contained and does not use hypothesis (D).  The
conclusion is a valid counterexample to identifying the ordinary domination
parameters pointwise with the Fuglede--Kadison expressions.  This report does
not certify any statement in §§6–7.
