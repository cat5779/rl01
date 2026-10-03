# Canonical quotient law and its six conditional messages

## 1. The specified family of probability laws

Let B be iid Bernoulli(1/2) bond percolation on T3. Its clusters are finite almost surely. For lambda>0, contract those clusters and give an original closed edge uv resistance

\[
r_\lambda(uv)=\lambda^{\deg_B(u)+\deg_B(v)}.
\tag{1}
\]

Because this edge is closed, each endpoint has B-degree at most two. Put a_lambda=min(1,lambda^4) and b_lambda=max(1,lambda^4). All quotient edge resistances belong to [a_lambda,b_lambda]. The quotient is a countable locally finite tree, since its vertices are finite connected clusters.

The network is transient. Indeed, representing open original edges as zero resistance, and increasing every edge resistance to b_lambda, gives the usual binary half-tree with resistance b_lambda to infinity. Rayleigh comparison bounds every forward half-network resistance above by b_lambda. The zero cluster at its root is finite; its finitely many positive-resistance boundary edges form a cutset. If it has d boundary edges, the unit-flow energy on that cutset is at least a_lambda/d. Consequently each forward resistance satisfies 0<R<=b_lambda almost surely. This uses no finite mean cluster size.

Conditional on B, take the canonical oriented wired spanning forest of this transient quotient. Its unoriented marginal is the weighted WUSF. Every quotient vertex has exactly one outgoing edge. This is the oriented WUSF of BLPS Definition 5.2: orient each edge in the direction of the loop-erased walk that inserted it in Wilson's algorithm rooted at infinity. Its law is independent of the vertex enumeration and covariant under network isomorphism, as established in Proposition 5.3. No one-endedness theorem for this random quotient is being assumed, and its orientation is not asserted to be a function of the unoriented forest.

This defines an actual measurable conditional probability kernel. For example, enumerate quotient clusters using the first vertex of each cluster in a fixed countable enumeration of the original vertices; enumerate their incident original edges; use independent uniforms for the resulting network walks in Wilson's algorithm. Cluster membership, positive transition probabilities, transient loop erasure and the resulting forest are measurable. The enumeration defines a law, and its order independence supplies covariance of that law; it does not supply an equivariant sampling map. The exceptional set of infinite critical clusters has zero probability and may be ignored when defining this probability law.

Lift every selected quotient edge back to the original tree, and adjoin B, obtaining T_lambda. Orient the internal B tree of each cluster toward the tail of that cluster's outgoing quotient edge, then orient the selected boundary edges according to the oriented quotient forest. Every original vertex now has exactly one outgoing edge. There are no contradictory opposite orientations on an edge and no unoriented cycles. The marked joint probability law of B, the oriented forest and T_lambda is Gamma-invariant because (1), contraction and lifting are covariant, and the conditional oriented WUSF kernel is covariant.

This is a specified invariant probability law, not an appeal to equivariant disintegration of some unknown endpoint joining. It makes no joint iid factor claim.

## 2. Every parameter has the correct one-edge marginal

Apply the original-tree fair-vertex mass-transport principle to the nonnegative transport sending one unit along each outgoing oriented edge of the lifted forest. The proof from the regular Gamma edge action is given in [MTP.md](MTP.md), and works unchanged for the present joint marked environment. Outgoing mass is identically one, so mean incoming mass at a fair vertex is one. Hence

\[
\mathbb E\deg_{T_\lambda}(o)=2.
\]

Gamma is transitive on unoriented original edges. If their common inclusion probability is p_lambda, every original vertex has mean degree 3p_lambda. Therefore

\[
p_\lambda=\frac23,\qquad
\mathbb P(e\notin T_\lambda)=\frac13
\quad\hbox{for every }\lambda>0.
\tag{2}
\]

This argument needs neither endpoint-exchange symmetry nor a finite expected quotient degree. It uses the oriented conditional forest law and the original tree, whose vertex degrees are three. Every original vertex has an incident selected edge, so the probability that all three incident edges are absent is zero.

## 3. Six actual infinite-network half-tree laws

Let R_{s,k}(lambda) be the wired resistance of a forward binary half-tree, conditional on the excluded parent edge's B status being s in {0,1} and on exactly k in {0,1,2} forward edges being open. The excluded parent status affects the root's B-degree and therefore its incident positive resistances; the parent edge itself is not part of this half-network. The root degree is k+s.

Write pi=(1,2,1)/4 for a child's forward B-count. Independently for each child, draw J with this distribution and use the appropriate conditional child resistance. An open arm has law

\[
O=R_{1,J}(\lambda),
\]

and a closed arm, when the root degree is d, has law

\[
C_d=\lambda^{d+J}+R_{0,J}(\lambda).
\]

All child half-trees and the root's edge bits are independent before conditioning on the count k. Conditioning on k only fixes which arm types occur; it does not couple their child trees. The parallel map Phi(x,y)=xy/(x+y), with Phi(0,0)=0, is increasing in both coordinates. Thus the actual laws satisfy

\[
R_{s,0}=\Phi(C_s,C'_s),\quad
R_{s,1}=\Phi(O,C_{s+1}),\quad
R_{s,2}=\Phi(O,O'),
\tag{3}
\]

with independent arm draws on each right side. These equations follow first on wired finite-depth half-networks and then by the increasing resistance limit. Only the indicated conditional marginal of a child is used in each branch; no independence of R_{0,J} and R_{1,J} on the same child tree is asserted or needed.

## 4. An exact adjacent-pair cylinder

Fix edges e1,e2 meeting at v, and put P_lambda=P(e1,e2 absent from T_lambda). They must both be closed in B, an event of probability 1/4. Let their outer endpoint forward counts be J1,J2, with independent pi laws, and let their exterior resistances be R1=R_{0,J1}, R2=R_{0,J2}. The third edge at v is open with probability 1/2, independently of the three exterior half-trees.

If it is closed, v's B-degree is zero, r1=lambda^{J1}, r2=lambda^{J2}, and the third arm has law C_0=lambda^{J3}+R_{0,J3}. If it is open, v's B-degree is one, r1=lambda^{1+J1}, r2=lambda^{1+J2}, and the third arm has law O=R_{1,J3}.

For positive first-edge resistances r1,r2 and exterior resistances R1,R2,t, the transfer-current complement determinant gives

\[
F(r_1,r_2,R_1,R_2,t)=
\frac{r_1r_2}{(r_1+R_1)(r_2+R_2)+(r_1+r_2+R_1+R_2)t}.
\tag{4}
\]

To derive it, set c_i=1/(r_i+R_i) for the first two arms, c3=1/t and C=c1+c2+c3. The symmetric transfer-current complement has diagonals r_i(c_i-c_i^2/C) and off-diagonals of absolute value sqrt(r1*r2)*c1*c2/C. Its determinant is r1*r2*c1*c2*c3/C, which simplifies to (4). The finite wired calculation extends to the infinite wired matrix by the transfer-current theorem. Formula (4) also has its continuous interpretation when a finite wired exterior resistance is zero.

Therefore

\[
P_\lambda=\frac18\mathbb E\left[
F(\lambda^{J_1},\lambda^{J_2},R_1,R_2,C_0)
+F(\lambda^{1+J_1},\lambda^{1+J_2},R_1,R_2,O)
\right],
\tag{5}
\]

where the first two count/resistance pairs and each third arm are independent. For fixed counts and hence fixed r1,r2, F is decreasing in each of its three exterior resistances.


## 5. Continuity of the wired pair probability

Under a common Bernoulli configuration, if lambda' tends to lambda, every closed edge has resistance ratio between min(1,(lambda'/lambda)^4) and max(1,(lambda'/lambda)^4). Rayleigh comparison yields the same multiplicative bounds for every wired half-tree resistance, first at finite depth and then in the limit. Thus each actual resistance converges pointwise. All finite B-clusters and transience are valid simultaneously for every positive parameter on the same full-probability Bernoulli event. In (5), the powers of lambda and all resistances therefore vary continuously. Its summands lie in [0,1], so dominated convergence proves that P_lambda is continuous.
