# Quantum positive-overlap obstruction: scope and proof

Let E have size n>=2. On fermionic Fock space over C^E, let C_v be creation by a unit vector v, P=vv*, and N_P=C_v C_v* the projection onto states whose v mode is occupied.

## V1. Exact scalar-background obstruction

At K=I/2 the normalized marked-empty endpoint state is
\[
\rho_{0,P}=2^{-(n-1)}(I-N_P).
\]
For every two distinct rank-one projectors P,Q:
\[
\sup\{\operatorname{tr}\tau:0\preceq\tau\preceq\rho_{0,P},
\ \tau\preceq\rho_{0,Q}\}=1/2. \tag{V1}
\]
No positive scalar c>0 satisfies \(c\rho_{0,P}\preceq\rho_{0,Q}\).
Nevertheless
\[
\|\rho_{0,P}-\rho_{0,Q}\|_{\rm tr}
=\tfrac12\|P-Q\|_{\rm tr}. \tag{V2}
\]
Thus neither a retained scalar multiple nor even an arbitrary common positive substate can provide a lost-mass O(||P-Q||) residual protocol as P approaches Q.

## V3. Explicit coexistence with a successful selector

For K=aI with 0<a<1, the G16 weighted-energy minimizer is exactly
\[
\Psi(aI,P)(S,i)=P_{ii}a^{|S|}(1-a)^{n-1-|S|}. \tag{V3}
\]
There are arbitrarily close distinct P,Q of equal coordinate diagonal; then the two minimizers agree exactly. Therefore V1 is an obstruction to the quantum-positive-residual construction, not to the weighted selector and not to full FC.

## V4. Optional quantitative interface for general backgrounds

For epsilon-gapped K,L commuting respectively with P,Q, let rho_{a,K,P} (a=0,1) be the normalized marked-empty/marked-occupied endpoint Gaussian states. The dimension-free comparison proved below is
\[
\|\rho_{a,K,P}-\rho_{a,L,Q}\|_{\rm tr}
\le \sqrt2\,\|P-Q\|_{\rm tr}
+\frac2{\varepsilon(1-\varepsilon)}
 \bigl(\|K-L\|_{\rm tr}
 +2\sqrt2(1-\varepsilon)\|P-Q\|_{\rm tr}\bigr). \tag{V4}
\]
It is based on a two-mode rotation and the audited fixed-background Loewner comparison. Classical endpoint marginal continuity is already inherited from G16's signed-current stability; V4 must not be sold as a new endpoint theorem. Its purpose is to locate the remaining obstruction despite close full quantum states.


# Close marked directions and discontinuous positive overlap

## 1. Definitions and scalar state

Use the canonical anticommutation relations
\[
C_v^*C_v+C_vC_v^*=I,\qquad C_v^2=0.
\]
For ||v||=1, \(N_P=C_vC_v^*\) is the orthogonal projection onto states with the v mode occupied. Its complement is the subspace annihilated by C_v^*. The empty-mode endpoint state for K=I/2 has independent Bernoulli(1/2) occupation in every other orthonormal mode and certain vacancy in the v mode. Thus
\[
\rho_{0,P}=a_n(I-N_P),\qquad a_n=2^{-(n-1)}.
\]
It is positive, number preserving, and has trace one because the empty-mode subspace has dimension \(2^{n-1}\). This is a normalized full quantum density, not just its diagonal classical atom law.

## 2. Exact maximal common positive mass

Let \(0\preceq\tau\preceq a_n\Pi_P\), where \(\Pi_P=I-N_P\). If x is in ker(Pi_P), then
\[
0\le\langle x,\tau x\rangle\le0.
\]
Positivity implies \(\tau^{1/2}x=0\), hence \(\tau x=0\). Therefore the support of tau is contained in range(Pi_P). Applying the same argument for Q shows that any common positive lower state is supported on
\[
\operatorname{ran}\Pi_P\cap\operatorname{ran}\Pi_Q.
\]

Since P and Q are distinct rank-one projectors, their ranges span a two-dimensional plane W. The intersection is exactly the Fock space over W-perp. Indeed, its vectors are annihilated by C_v^* and C_w^*. By linearity they are annihilated by both annihilation operators of any orthonormal basis of W; in the occupation decomposition
\(\mathcal F(W)\otimes\mathcal F(W^\perp)\), only the W-vacuum component remains. Its dimension is \(2^{n-2}\).

On this intersection both rho_0,P and rho_0,Q equal a_n times the identity. Every common tau therefore has all eigenvalues at most a_n and trace at most
\[
a_n 2^{n-2}=1/2.
\]
Equality is attained by a_n times the projection onto that intersection. This proves V1, including that arbitrary off-diagonal choices of tau cannot improve the mass.

If \(c\rho_{0,P}\preceq\rho_{0,Q}\) with c>0, the same support argument would force the entire \(2^{n-1}\)-dimensional P-empty space into the Q-empty space. Equal dimensions would then imply equality, contradicting the intersection dimension just calculated. Therefore c=0 is the only possible retained scalar coefficient.

The case P=Q is different: maximal common mass is one and scalar coefficient one is valid. Thus the overlap obstruction is discontinuous exactly on the equality locus.

## 3. Quantum trace distance tends to zero

Let theta in (0,pi/2] be the principal angle between the two marked lines:
\[
|\langle v,w\rangle|=\cos\theta.
\]
On the two-mode Fock factor F(W), N_P-N_Q vanishes on the vacuum and on the two-particle state. On the one-particle sector it is exactly P-Q, whose eigenvalues are +sin(theta), -sin(theta). Hence
\[
\|P-Q\|_{\rm tr}=2\sin\theta.
\]
Tensoring with the identity on the remaining Fock factor multiplies the trace norm by \(2^{n-2}\). Consequently
\[
\|\rho_{0,P}-\rho_{0,Q}\|_{\rm tr}
=a_n\,2^{n-2}\,2\sin\theta
=\sin\theta=\tfrac12\|P-Q\|_{\rm tr}.
\]
This proves V2.

In particular, along any distinct P_j tending to P, both full quantum states and their classical measurement distributions converge, while at most half of either state can be retained as a common positive substate. A purported residual protocol retaining mass at least \(1-C\|P-P_j\|_{\rm tr}\) for a universal C fails once the distance is less than 1/(2C).

## 4. The weighted minimizer succeeds on this example

Let K=aI, with epsilon<=a<=1-epsilon. Put
\[
w(S,i)=P_{ii}a^{|S|}(1-a)^{n-1-|S|}.
\]
All coordinates of P with P_ii=0 force the corresponding flow edges to zero, so only positive-weight edges need be considered.

This w has total edge mass one. At an atom S of size k,
\[
\begin{aligned}
w_{\rm in}(S)-w_{\rm out}(S)
={}&a^{k-1}(1-a)^{n-k}\sum_{i\in S}P_{ii}\\
&-a^k(1-a)^{n-k-1}\sum_{i\notin S}P_{ii}.
\end{aligned}
\]
This is exactly the rank-one determinant derivative of p_K(S). The terms with an empty sum are zero, so the formula also covers k=0 and k=n. Also
\[
w_{\rm out}(S)
=\frac{p_K(S)}{1-a}\sum_{i\notin S}P_{ii}
\le\varepsilon^{-1}p_K(S).
\]
Therefore w belongs to the full original positive fiber, with stronger capacity than required.

For every feasible f, its total mass is one and the weights sum to one. Cauchy--Schwarz yields
\[
\sum_{e:w_e>0}f_e^2/w_e\ge1.
\]
Equality holds precisely when f is proportional to w, hence exactly when f=w. Thus the G16 weighted-energy rule is
\[
\Psi(aI,P)=w.
\]

For an explicit arbitrarily close pair take n=2,
\[
v=2^{-1/2}(1,1),\qquad
w_t=2^{-1/2}(e^{it},e^{-it}),\quad 0<t<\pi/2.
\]
Their projectors have the same coordinate diagonal, are distinct, and have trace distance 2sin(t). The two weighted minimizers are identical for every t. Meanwhile the full quantum common-state mass remains 1/2. This proves V3 and demonstrates directly why V1 cannot be read as a failure of the selector itself.

## 5. General gapped quantum endpoint comparison

This section uses one precisely scoped inherited lemma: on a fixed one-particle background space H, for epsilon-gapped self-adjoint B,B',
\[
e^{-D}\sigma_B\preceq\sigma_{B'}\preceq e^D\sigma_B,
\qquad D=\|B-B'\|_{\rm tr}/[\varepsilon(1-\varepsilon)].
\]
Here sigma is the normalized, number-preserving Gaussian density on Fock(H). This is the audited G16 ledger Section D, source #119 Section4, and the only external non-elementary input in this section. In particular
\[
\|\sigma_B-\sigma_{B'}\|_{\rm tr}\le2(1-e^{-D})\le2D, \tag{1}
\]
because sigma_B' = e^-D sigma_B + a positive residual of trace 1-e^-D.

Assume K,L commute respectively with P,Q and are epsilon-gapped. If P=Q use the identity rotation. Otherwise choose phases so <v,w>=cos(theta)>=0, let W span the two lines, and choose the real plane rotation R carrying v to w, equal to the identity on W-perp. Its two nontrivial eigenvalues are e^{i theta}, e^{-i theta}. Thus
\[
\|R-I\|_{\rm tr}=4\sin(\theta/2)
\le\sqrt2\,\|P-Q\|_{\rm tr}. \tag{2}
\]
The second quantization Gamma(R) has eigenvalues 1,e^{i theta},e^{-i theta}: on the W-vacuum and two-particle sectors its value is one, and outside W it is the identity. Consequently
\[
\|\Gamma(R)-I\|_{\rm op}=2\sin(\theta/2). \tag{3}
\]
There is no factor n in (2) or (3).

Put K'=RKR*. It commutes with Q and has the same spectral gap. Its marked-empty and marked-occupied endpoint densities are
\[
\rho_{a,K',Q}=\Gamma(R)\rho_{a,K,P}\Gamma(R)^*,\qquad a=0,1.
\]
For any density rho,
\[
\|\Gamma(R)\rho\Gamma(R)^*-\rho\|_{\rm tr}
\le2\|\Gamma(R)-I\|_{\rm op}\|\rho\|_{\rm tr}.
\]
Using (2)--(3) and trace normalization bounds this by
\(\sqrt2\|P-Q\|_{\rm tr}\).

On the common background space Q-perp, the restrictions B',B_L of K',L are both epsilon-gapped. Compression and the trace ideal inequality give
\[
\begin{aligned}
\|B'-B_L\|_{\rm tr}
&\le\|K'-L\|_{\rm tr}\\
&\le\|K-L\|_{\rm tr}
+2\|K\|_{\rm op}\|R-I\|_{\rm tr}\\
&\le\|K-L\|_{\rm tr}
+2\sqrt2(1-\varepsilon)\|P-Q\|_{\rm tr}. \tag{4}
\end{aligned}
\]
The marked eigenvalues need not coincide: these endpoint states depend only on their background, with the marked mode fixed empty or occupied. Embedding sigma_B into the empty subspace and the creation isometry into the occupied subspace preserves trace norms. Applying (1) to (4), then adding the rotation difference, proves V4 for both a=0 and a=1, including orthogonal marked lines theta=pi/2.

This comparison is pairwise only; no global choice of phases or rotations is required. It does not turn a positive state on one marked-empty subspace into a common positive substate, and it does not preserve coordinate one-birth edges under the rotation.

## 6. Exact relevance to FC

The fixed-P repair succeeds because both Gaussian backgrounds live on the same marked-empty subspace and admit a positive residual of small mass. Changing P destroys that support comparison even at a scalar K, while V2 and V4 show that trace continuity persists.

The lost-mass barrier applies to algorithms requiring a common positive quantum substate or a scalar Loewner-retained fraction. It does not apply to all positive classical flows. The scalar minimizer calculation gives a counterexample to any inference from this barrier to selector nonexistence.

The unresolved task is to pass from signed-current or quantum trace continuity to a single positive coordinate-edge rule satisfying exponent-one consistency for arbitrary finite lists. No such rule, and no selector-independent divergent family, is produced here.
