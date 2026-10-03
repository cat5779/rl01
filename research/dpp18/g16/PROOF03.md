# Completion of G16's dimension-free fixed-projector Hölder selector

Section 2 incorporates the complete-current correction documented in [ERRATUM03.md](ERRATUM03.md). The frozen original continuation is preserved separately. This note addresses fixed P and exponent one-half only; the varying-P exponent-one target in [TASK.md](TASK.md) remains open. The full fiber means nonnegative upward edge flows with divergence b_(K,P), total mass one, and outgoing capacity (2/epsilon)p_K(S). See [REVIEW03.md](REVIEW03.md) for the checked scope.

For a finite ground set E, let p_K(S) be the exact probability of S under the DPP with kernel K, and put b_(K,P)(S) = (d/dt) p_(K+tP)(S) at t=0. An upward edge (S,i) goes from S to S union {i}, where i is not in S. Divergence means total incoming flow minus total outgoing flow. The outgoing capacity at S is the bound on the sum over all its upward outgoing edges. Psi(K,P) is the unique minimizer of (1/2) sum_e f_e^2/w_K(e) over this full fiber; zero-weight edges are forced to carry zero flow. The weights w_K are defined in Section 1.


## 1. Source verdict versus theorem verdict

The candidate at source lines 385--392 does not supply its weighted repair or variational inequality. An l1 repair alone does not control the weighted energy, because the weights can be exponentially small. Thus the original text does not constitute a complete proof of (H). The completion below uses an additional argument: the same positive residual state used in fixed-P repair has a positive flow bounded by twice its own signed current. This gives the missing *weighted* repair.

We prove the exact constant claimed in the candidate. Matrix norm is unnormalized trace norm; flow norm is edge l1. Fix \(0<\varepsilon<1/2\), any finite E, and one rank-one \(P=vv^*\). All kernels in this proof are epsilon-gapped and commute with this same P.

Write
\[
w_K(S,i)=P_{ii}[p_K(S)+p_K(S+i)],\qquad
\|z\|_{w_K}^2=\sum_{e:w_K(e)>0}z_e^2/w_K(e).
\]
Every feasible nonnegative flow has coordinate mass \(P_{ii}\), by testing its divergence against the indicator of coordinate i. Thus directions where \(P_{ii}=0\) vanish in every feasible flow and every current used below. On the remaining edges all weights are positive.

## 2. Weights, current energy, and its derivative

The two exact probabilities in the weight sum are the reduced DPP atom on E minus i. Consequently \(\sum_e w_K(e)=1\), and Cauchy-Schwarz gives
\(\|z\|_1\le\|z\|_{w_K}\).

All one-coordinate conditional exact-pattern probabilities lie in \([\varepsilon,1-\varepsilon]\). Sequential occupation/vacancy Schur complements preserve the same gap: for occupation apply the Schur complement inequality to \(K-\varepsilon'I\) with \(\varepsilon'<\varepsilon\), noting that division by \(K_{ii}\) subtracts less than division by \(K_{ii}-\varepsilon'\); vacancy is the corresponding argument for \(I-K\). Pass \(\varepsilon'\uparrow\varepsilon\). This checks the gap hypothesis even at boundary eigenvalues.

Let \(M_S=K-D_{S^c}\), \(u^S=M_S^{-1}v\), and let \(J_K\) be the signed endpoint current. It has both incident representations
\[
J(S,i)=-p_K(S)\operatorname{Re}(v_i\overline{u_i^S}),\quad i\notin S,
\]
\[
J(S-i,i)=p_K(S)\operatorname{Re}(v_i\overline{u_i^S}),\quad i\in S.
\]
Also \(\|M_S^{-1}\|_{\rm op}\le\varepsilon^{-1}\). At either endpoint of any edge,
\[
J_e^2/w_K(e)
\le(1-\varepsilon)p_K(S)|u_i^S|^2.
\]
Summing over vertices counts each edge twice. Therefore
\[
\|J_K\|_{w_K}^2\le\frac{1-\varepsilon}{2\varepsilon^2}.
\tag{1}
\]
Put \(B_\varepsilon=\sqrt{2(1-\varepsilon)}/\varepsilon\), so \(\|J_K\|_{w_K}\le B_\varepsilon/2\). The audited positive-part endpoint theorem gives a feasible endpoint flow \(h\le2(J_K)_+\), hence
\(\|h\|_{w_K}\le B_\varepsilon\). In particular the full-fiber energy minimizer exists uniquely and satisfies
\[
\|\Psi(K,P)\|_{w_K}\le B_\varepsilon. \tag{2}
\]

Along any gapped segment \(K_t\) with derivative D and \(d=\|D\|_1\), the reduced determinant derivative gives
\[
|\partial_t\log w_t(e)|\le d/\varepsilon. \tag{3}
\]
There is no derivative of \(P_{ii}\), since P is fixed. Compression contracts the trace norm, and the reduced exact-pattern inverse has the same norm bound, verifying every hypothesis in (3).

For the current derivative, both factors must be differentiated:
\[
\dot p(S)=p(S)\alpha_S,\quad
|\alpha_S|=|\operatorname{tr}(M_S^{-1}D)|\le d/\varepsilon,\qquad
\dot u^S=-M_S^{-1}D u^S.
\]
Differentiate the two *complete* incident representations of the same edge current. At either endpoint S, the complete derivative is
\[
\dot J_e=\pm p(S)\operatorname{Re}
 [v_i\overline{\alpha_Su_i^S+\dot u_i^S}].
\]
Therefore
\[
\dot J_e^2/w_t(e)
\le(1-\varepsilon)p(S)
 |\alpha_Su_i^S+\dot u_i^S|^2.
\]
This is the same complete derivative at both endpoints, so summing over all vertices legitimately counts each edge twice:
\[
\begin{aligned}
2\|\dot J_t\|_{w_t}^2
&\le(1-\varepsilon)\sum_Sp(S)
 \|\alpha_Su^S+\dot u^S\|_2^2\\
&\le(1-\varepsilon)(2d/\varepsilon^2)^2.
\end{aligned}
\]
The last inequality uses ||u^S||<=epsilon^-1, ||D||op<=d,
||dot u^S||<=d epsilon^-2, and sum_S p(S)=1. Since
\(B_\varepsilon^2=2(1-\varepsilon)/\varepsilon^2\),
\[
\|\dot J_t\|_{w_t}
\le(B_\varepsilon/\varepsilon)d. \tag{4}
\]

This proves (4) for the complete derivative. No separate double-counted estimate for the split inverse-factor term is used.

From (3), if \(q=\|K-L\|_1/\varepsilon\),
\[
e^{-q}w_K\le w_L\le e^qw_K,\qquad
\|z\|_{w_K}\le e^{q/2}\|z\|_{w_L}. \tag{5}
\]

## 3. Positive-part flows for an arbitrary positive residual state

This is the missing repair ingredient. Work on fermionic Fock space, with creation C by v and \(U=C+C^*\), a self-adjoint unitary. Let \(\rho_\tau\ge0\) be a number-preserving operator supported on the marked-mode-empty subspace. It may have any nonnegative trace m. Put
\[
\alpha_\tau(S)=\langle S|\rho_\tau|S\rangle,\qquad
\beta_\tau(T)=\langle T|U\rho_\tau U|T\rangle,
\]
\[
q_\tau(S,T)=\operatorname{Re}
[U_{T,S}(\rho_\tau U)_{S,T}].
\]
Its marginals are \(\alpha_\tau,\beta_\tau\); number preservation and \(\rho_\tau C=0\) support it on upward one-point edges.

For source and target families A,B, let R project onto A and
\(Q=U^*(I-R_B)U\). The projection identity
\[
RQ+QR-(R+Q-I)=(R+Q-I)^2\succeq0
\]
and positivity of \(\rho_\tau\) imply
\[
\alpha_\tau(A)-\beta_\tau(B)
\le2\sum_{S\in A,T\notin B}q_\tau(S,T)
\le2\sum_{S\in A,T\notin B}(q_\tau(S,T))_+.
\]
These are precisely all finite bipartite capacity cuts. The finite max-flow theorem therefore supplies an endpoint flow
\[
h_\tau\ge0,\qquad h_\tau\le2(q_\tau)_+,
\tag{6}
\]
of total mass m and these marginals. No Gaussian assumption on the residual state is used.

For the fixed-P background states in the audited repair construction,
\(\rho_\tau=\rho_{0,B'}-c_B\rho_{0,B}\). Linearity of the Fock quasi-current and its audited identification with the resolvent current give the exact identity
\[
q_\tau=J_M-c_BJ_K. \tag{7}
\]
Thus this residual can be chosen with controlled weighted energy, not merely controlled total mass.

## 4. Weighted repair of an energy-bounded full-fiber flow

Let
\[
K=\lambda P+B,\quad L=\nu P+B',\quad M=\lambda P+B'
\]
on the common decomposition \(\mathbb Cv\oplus v^\perp\). All backgrounds are epsilon-gapped on \(v^\perp\), and
\[
d:=\|K-L\|_1=d_B+d_\lambda,\quad
d_B=\|B-B'\|_1,\quad d_\lambda=|\lambda-\nu|.
\]
Assume \(d\le\varepsilon\), put \(q_B=d_B/\varepsilon\), \(q_\lambda=d_\lambda/\varepsilon\), and \(q=q_B+q_\lambda\le1\). Let \(f\in\mathcal F(K,P)\) satisfy \(\|f\|_{w_K}\le B_\varepsilon\).

The fixed-P fermionic Loewner comparison, under exactly these background/gap hypotheses, gives
\[
D_B=d_B/[\varepsilon(1-\varepsilon)],\quad c_B=e^{-D_B},\quad
\rho_\tau=\rho_{0,B'}-c_B\rho_{0,B}\ge0.
\]
Its mass \(m_B=1-c_B\le q_B/(1-\varepsilon)\le2q_B\).
Integrating (4) along K to M and using (5) gives
\[
\|J_M-J_K\|_{w_K}\le e^{q_B/2}B_\varepsilon q_B.
\]
From (6)--(7) and (1),
\[
\|h_\tau\|_{w_K}
\le2e^{q_B/2}B_\varepsilon q_B+m_BB_\varepsilon.
\]
Set \(g_M=c_Bf+h_\tau\). It has the correct divergence and unit mass. The original full-fiber capacity is preserved because
\[
p_M-c_Bp_K=(1-\lambda)\alpha_\tau+\lambda\beta_\tau,\quad
(h_\tau)_{\rm out}=\alpha_\tau,\quad
2(1-\lambda)/\varepsilon\ge2.
\]
Thus \(g_M\in\mathcal F(M,P)\), and
\[
\|g_M-f\|_{w_K}
\le2m_BB_\varepsilon+2e^{q_B/2}B_\varepsilon q_B
\le8B_\varepsilon q_B, \tag{8}
\]
using \(e^{1/2}<2\).

For the marked eigenvalue change use exactly the audited scalar coefficient
\[
c_\lambda=\min\left\{1,\nu/\lambda,
(1-\nu-\varepsilon/2)/(1-\lambda-\varepsilon/2)\right\}.
\]
All denominators are positive, and \(m_\lambda=1-c_\lambda\le2q_\lambda\).
Choose a positive endpoint flow \(h\le2(J_M)_+\). Its outgoing law is the common lower endpoint law, and
\(\|h\|_{w_K}\le e^{q_B/2}B_\varepsilon\).
Set \(g_L=c_\lambda g_M+m_\lambda h\). The inequalities
\[
\nu-c_\lambda\lambda\ge0,\quad
1-\nu-c_\lambda(1-\lambda)\ge(\varepsilon/2)m_\lambda
\]
verify its full-fiber capacity coefficientwise. Hence \(g_L\in\mathcal F(L,P)\), with
\[
\begin{aligned}
\|g_L-f\|_{w_K}
&\le\|g_M-f\|_{w_K}+m_\lambda\|h-f\|_{w_K}\\
&\le8B_\varepsilon q_B+2(1+e^{1/2})B_\varepsilon q_\lambda\\
&\le8B_\varepsilon q .
\end{aligned} \tag{9}
\]
This is only asserted for old flows with bounded weighted energy. It is the new bound needed for the minimizers. Interchanging K,L gives the corresponding reverse weighted repair.

## 5. Variational inequalities, with an explicit uniform constant

Write \(f=\Psi(K,P)\), \(g=\Psi(L,P)\). By (2), both have energy norm at most \(B_\varepsilon\) in their own weights. From (9), choose competitors
\[
f+u\in\mathcal F(L,P),\quad\|u\|_{w_K}\le8B_\varepsilon q,
\]
\[
g+z\in\mathcal F(K,P),\quad\|z\|_{w_L}\le8B_\varepsilon q.
\]
The two minimizer variational inequalities imply
\[
\langle f,f-g\rangle_{w_K}\le\langle f,z\rangle_{w_K},
\quad
\langle g,g-f\rangle_{w_L}\le\langle g,u\rangle_{w_L}.
\]
Let \(X=\|f-g\|_{w_K}\). Adding and comparing weight metrics gives
\[
X^2\le|\langle f,z\rangle_{w_K}|+
|\langle g,u\rangle_{w_L}|+
|\langle g,g-f\rangle_{w_K}-\langle g,g-f\rangle_{w_L}|.
\]
The first two terms sum to at most
\(16e^{q/2}B_\varepsilon^2q\le32B_\varepsilon^2q\).
For the last term, (5) gives
\[
|w_K(e)^{-1}-w_L(e)^{-1}|
\le(e^q-1)w_K(e)^{-1}.
\]
Also
\(\|g\|_{w_K}\le e^{q/2}B_\varepsilon\) and
\(X\le(1+e^{q/2})B_\varepsilon\). Since \(e^q-1\le(e-1)q<2q\) for \(0\le q\le1\) and \(e^{q/2}<2\), this term is at most \(12B_\varepsilon^2q\). Therefore
\[
X^2\le44B_\varepsilon^2q\le50B_\varepsilon^2q. \tag{10}
\]
Using \(\|f-g\|_1\le X\) and the definition of \(B_\varepsilon\),
\[
\|f-g\|_1
\le10\sqrt{1-\varepsilon}\,\varepsilon^{-3/2}\sqrt d
\le10\varepsilon^{-3/2}\sqrt d. \tag{11}
\]
For \(d\ge\varepsilon\), positivity and unit mass give \(\|f-g\|_1\le2\), which is smaller than the right side of (11). Thus the original dimension-free constant is established for all distances.

## 6. One rule, measurability, and symmetry

Strict convexity on the nonforced coordinates gives a unique minimizer at every input. The resulting rule is Borel for each fixed finite E. For example, partition parameter space into the finitely many projector-support strata. On each stratum the weights are positive, the constraints are polynomial/affine in the real coordinates of K,P, and the objective is a rational positive-definite quadratic form. Clearing the positive denominators, its minimizer graph is semialgebraic by finite-dimensional real quantifier elimination; uniqueness makes the coordinate functions Borel. This argument requires no support-uniform continuity constant.

Alternatively, the fixed-normal finite-dimensional polytope error bound supplies the missing lower hemicontinuity needed for the original support-degeneration continuity suggestion; its constants may depend on E, and are used only for that topological statement. Compact graph and uniqueness alone, as written in the original source, do not supply this step.

Permutation covariance follows directly from uniqueness and naturality of weights/constraints. Fixed-P arbitrary finite families all use this same rule, so (11) gives simultaneous Hölder consistency with no list-length factor.

## 7. Exact result and remaining boundary

The original Continuation 02 Section 2 contains valid weight, energy and differential claims but leaves its principal weighted repair/variational argument schematic. The source proof is therefore incomplete; the theorem (H) is supplied with a repaired argument via (6)--(10).

All uniform constants are independent of E, support, and the finite family length. The exponent is one-half in the unnormalized trace distance, not one. P is the same at both inputs. Nothing in the residual argument compares different marked-mode subspaces, so this does not solve varying-P FC. No bad optimizer or whole-fiber Hausdorff witness is being used to infer a selector-independent conclusion.
