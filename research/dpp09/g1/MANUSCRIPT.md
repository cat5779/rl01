# General positive increments: original mathematical manuscript

The unrestricted relative ordered-factor target remains **INCOMPLETE**. This file preserves the mathematical argument submitted for review; the labels inside it are the manuscript's claims, not a blanket acceptance of all auxiliary statements. The precise review and any necessary corrections are recorded separately. In particular, an exact positive continuity equation does not by itself construct a process driven by independent clocks, and the final selection-stability interface requires cross-approximation control.

The rank-one coupling lemma in Section 2 is a standard consequence of projection-DPP coupling and dilation; see SOURCES.md. No novelty claim is made for it.

---

# INCOMPLETE

The unrestricted relative-factor theorem is neither proved nor disproved. I prove three substantive intermediate results:

1. the target holds when \(D-C\) admits an increasing finite-support square exhaustion;
2. every arbitrary increment \(D-C\) admits an exact covariant positive **single-birth continuity equation** with support-independent source rate;
3. a common-noise stability criterion converts suitable finite-range approximations into the required all-input factor.

The remaining unproved step is a support-uniform measurable selection and sensitivity estimate for the rank-one monotone transports. A Fourier example proves that this step cannot generally be avoided by monotone finite-support square approximation.

Put
\[
H=D-C,\qquad T=H^{1/2},\qquad
v=T\delta_e,\qquad v_g=T\delta_g.
\]
Then
\[
H=\sum_{g\in\Gamma}v_gv_g^*
\tag{1}
\]
in the strong operator topology.

## 1. A complete extension under monotone square exhaustion

Call \(H\) algebraically square-exhaustible if there are equivariant finite-propagation operators \(T_n\) such that
\[
S_N:=\sum_{n\le N}T_nT_n^*\le H,
\qquad S_N\longrightarrow H
\quad\text{strongly}.
\tag{2}
\]

### PROVED_HERE — Theorem 1

Under (2), the target transition exists.

### Proof

Split every atomless iid label into countably many independent atomless labels. Starting with \(X_0=X\), apply the supplied Theorem R successively to
\[
C+S_{n-1}\longrightarrow C+S_n.
\]
Every intermediate kernel remains between \(C\) and \(D\), hence retains the common spectral gap. We obtain total Borel, all-input equivariant maps with
\[
X=X_0\subseteq X_1\subseteq X_2\subseteq\cdots,
\qquad
X_N\sim\mu_{C+S_N}.
\]

Set
\[
Y=\bigcup_NX_N.
\]
This is a total Borel equivariant function of \(X\) and the iid labels and contains \(X\) on every input. For every finite \(B\subseteq\Gamma\),
\[
\mathbf P[B\subseteq Y]
 =\lim_N\mathbf P[B\subseteq X_N]
 =\lim_N\det(C+S_N)[B]
 =\det D[B],
\]
because strong convergence gives entrywise convergence on every finite compression. Thus \(Y\sim\mu_D\). ∎

This covers any finite or countable sum of finite-support positive squares whose partial sums stay below \(H\).

## 2. Rank-one increments have one-point monotone couplings

Lyons’s stochastic-domination theorem states that \(0\le Q_1\le Q_2\le I\) implies \(\mu_{Q_1}\preccurlyeq\mu_{Q_2}\); Strassen’s theorem then gives a monotone coupling. 

### PROVED_HERE — Lemma 2

Let \(E\) be countable and
\[
0\le A\le A+ww^*\le I
\quad\text{on }\ell^2(E).
\]
There is a monotone coupling \((Z,Z')\) of \(\mu_A\) and \(\mu_{A+ww^*}\) such that
\[
|Z'\setminus Z|\le1
\quad\text{almost surely}.
\tag{3}
\]

### Proof

Apply Naimark dilation to the three effects
\[
A,\qquad ww^*,\qquad I-A-ww^*.
\]
The standard dilation is the isometry
\[
h\longmapsto
\bigl(A^{1/2}h,(ww^*)^{1/2}h,
      (I-A-ww^*)^{1/2}h\bigr).
\]
After identifying its range with the original coordinate subspace, this gives projections
\[
P_1\le P_2
\]
on a larger countable coordinate Hilbert space, with compressions \(A\) and \(A+ww^*\), and
\[
\operatorname{rank}(P_2-P_1)=1.
\]

Write
\[
\operatorname{ran}P_2=\operatorname{ran}P_1\oplus[z].
\]
Choose finite-dimensional \(V_n\uparrow\operatorname{ran}P_1\), and let \(P_{1,n}\) and \(P_{2,n}\) project onto \(V_n\) and \(V_n\oplus[z]\). Projection-DPP samples have cardinalities \(\dim V_n\) and \(\dim V_n+1\). Hence every monotone coupling of these two laws adds exactly one point.

Take a weakly convergent subsequence of those couplings. The marginals converge to the projection DPPs of \(P_1,P_2\), and
\[
\{(x,y):x\subseteq y,\ |y\setminus x|\le1\}
\]
is closed. Restricting both samples to the original coordinate set produces the required coupling because a restriction of a projection DPP has the DPP law of the compressed kernel. ∎

When the kernels depend Borel-measurably on a parameter, these couplings may also be selected Borel-measurably: their admissible set is a nonempty compact section of a Borel subset of the compact coupling space. The compact-section selection theorem and parameterized disintegration give a total Borel transition kernel. On the null set where a chosen disintegration fails to satisfy (3), replace it by the identity transition.

## 3. An exact positive flow for every \(D-C\)

Let
\[
K_t=C+tH,\qquad 0\le t\le1.
\]
If \(v=0\), equivariance gives \(H=0\), and the identity map suffices. Otherwise put
\[
h_0=\frac{\epsilon}{2\|v\|^2},
\qquad M=h_0^{-1}.
\tag{4}
\]
Then, for every \(t,g\),
\[
K_t+h_0v_gv_g^*\le (1-\epsilon/2)I.
\]

Choose measurably in \(t\) a coupling
\[
\pi_{t,g}
\quad\text{of}\quad
\mu_{K_t}
\ \text{and}\
\mu_{K_t+h_0v_gv_g^*}
\tag{5}
\]
as in Lemma 2, with
\[
\pi_{t,g}=g\pi_{t,e}.
\]
Let \(P_{t,g}(x,dy)\) be a total Borel disintegration, equal to \(\delta_x\) on its exceptional set. Define
\[
q_{t,g}(x,i)
 =
P_{t,g}\bigl(x,\{x\cup\{i\}\}\bigr)
\,\mathbf1_{\{i\notin x\}},
\]
and
\[
a_i(t,x)=M\sum_{g\in\Gamma}q_{t,g}(x,i).
\tag{6}
\]
This is a covariant nonnegative Borel function; it may be infinite on configurations outside the intended DPP law.

### PROVED_HERE — Theorem 3

For every \(i,t\),
\[
\int a_i(t,x)\,d\mu_{K_t}(x)
 =\sum_g|v_g(i)|^2
 =\langle H\delta_i,\delta_i\rangle
 =\tau(H).
\tag{7}
\]
Thus \(a_i(t,\cdot)<\infty\) \(\mu_{K_t}\)-almost surely. Moreover, every cylinder function \(f\) satisfies the exact forward equation
\[
\frac d{dt}\mu_{K_t}(f)
 =
\int\mathcal L_tf(x)\,d\mu_{K_t}(x),
\tag{8}
\]
where
\[
\mathcal L_tf(x)
 =
\sum_i a_i(t,x)
 [f(x\cup\{i\})-f(x)].
\tag{9}
\]
The expression in (8) is absolutely integrable.

### Proof

For finite \(F\subseteq\Gamma\), exact DPP probabilities are
\[
\mu_K[X\cap F=\eta]
 =
(-1)^{|F\setminus\eta|}
\det\!\bigl(K_F-P_{F\setminus\eta}\bigr).
\tag{10}
\]
Therefore every finite-cylinder expectation is affine on a rank-one line \(K+hww^*\). Consequently
\[
M\left(
 \mu_{K_t+h_0v_gv_g^*}(f)-\mu_{K_t}(f)
 \right)
 =
D_{v_gv_g^*}\mu_{K_t}(f).
\tag{11}
\]

Since \(\pi_{t,g}\) adds at most one point,
\[
\begin{aligned}
M\int q_{t,g}(x,i)\,d\mu_{K_t}(x)
&=
M\left[
 (K_t+h_0v_gv_g^*)_{ii}-(K_t)_{ii}
 \right]  \\
&=|v_g(i)|^2.
\end{aligned}
\]
Tonelli gives (7).

If \(f\) depends on finite \(F\), only \(i\in F\) contribute to (9), so (7) proves absolute integrability. Summing (11) over \(g\), and using (1), gives
\[
\sum_gD_{v_gv_g^*}\mu_{K_t}(f)
 =
D_H\mu_{K_t}(f)
 =
\frac d{dt}\mu_{K_t}(f).
\]
This is (8). ∎

Thus arbitrary square-summable columns cause no obstruction at the level of a positive, covariant, single-site flow with finite expected local activity. The missing issue is its strong common-noise realization.

## 4. A reusable common-noise closure theorem

### PROVED_HERE — Theorem 4

Let \(K_t^{(n)}\) be uniformly gapped equivariant DPP paths with
\[
K_0^{(n)}=C,
\qquad
K_t^{(n)}\longrightarrow K_t
\]
entrywise for every \(t\). Suppose total equivariant pure-birth solutions \(X^{(n)}\), driven by the same initial configuration and the same sitewise Poisson fields, have intrinsic rates \(a^{(n)}\).

Assume that for every jointly invariant pair \((U,V)\),
\[
\mathbf E\left|
a_e^{(n)}(t,U)-a_e^{(m)}(t,V)
\right|
\le
L(t)\mathbf P(U_e\ne V_e)+\rho_{n,m}(t),
\tag{12}
\]
where
\[
L\in L^1[0,1],
\qquad
\int_0^1\rho_{n,m}(t)\,dt\longrightarrow0.
\tag{13}
\]
Then a subsequence converges on the common input, coordinatewise as whole paths, to a total Borel, all-input equivariant pure-birth factor \(X_t\), with
\[
X_t\sim\mu_{K_t}.
\]

### Proof

Let \(d_{n,m}(T)\) be the probability that the two root paths disagree at some time up to \(T\). A first disagreement requires a common Poisson mark to fall between the two predictable thresholds. Compensation and (12) give
\[
d_{n,m}(T)
\le
\int_0^T
\bigl[L(t)d_{n,m}(t)+\rho_{n,m}(t)\bigr]\,dt.
\]
Hence
\[
d_{n,m}(1)
\le
\exp\!\left(\int_0^1L\right)
\int_0^1\rho_{n,m}.
\tag{14}
\]

Choose a subsequence for which consecutive bounds in (14) are summable. Borel–Cantelli, invariance and countability of \(\Gamma\) imply eventual agreement of every coordinate path. On this invariant conull set take the coordinatewise path limit; outside it return the constant initial path. The resulting map is total, Borel, equivariant and contains the initial configuration on every input.

For finite \(B\),
\[
\mathbf P[B\subseteq X_t]
 =
\lim_n\det K_t^{(n)}[B]
 =
\det K_t[B].
\]
Thus \(X_t\sim\mu_{K_t}\). ∎

The important estimate is the common-configuration mean estimate (12), not a sum of separate worst-case influences.

## 5. Finite-support positive approximation cannot suffice

Let \(\Gamma=\mathbb Z\), identify the commutant with Fourier multipliers on \(\mathbb T\), and choose a closed nowhere-dense set \(E\subset\mathbb T\) of positive Haar measure. Define
\[
C=\frac34I-\frac12P_E,
\qquad
D=\frac34I.
\tag{15}
\]
Then
\[
\frac14I\le C\le D\le\frac34I,
\qquad
H=D-C=\frac12P_E.
\]

If \(A=T_0T_0^*\) and \(T_0\delta_0\) has finite support, then \(A\) has a continuous nonnegative trigonometric multiplier \(a\). If
\[
C+A\le I,
\]
then on the dense open set \(E^c\),
\[
a\le\frac14.
\]
Continuity therefore gives \(a\le1/4\) everywhere. No sequence of such valid increments can converge weakly to \(H\), whose multiplier equals \(1/2\) on \(E\).

If one preserves the original upper gap,
\[
C+A\le\frac34I,
\]
then \(a=0\) on \(E^c\), hence \(a\equiv0\).

Thus neither monotone finite-support square exhaustion nor even arbitrary contraction-preserving finite-support-square approximation reaches this pair. This disproves only that approximation programme, not the target coupling.

## 6. Exact unresolved step

The general rates (6) satisfy only
\[
\mathbf E_{\mu_{K_t}}a_e(t,X)=\tau(H).
\tag{16}
\]
This does not control how the selected transport changes when the exterior configuration changes.

The smallest missing statement in this construction is:

### STRONGER_BLOCKER — Selection-stability lemma

The couplings in (5) can be selected and approximated by bounded finite-range covariant rates \(a^{(R)}\) so that, for every jointly invariant ordered pair \(U\le V\),
\[
\mathbf E\,
\operatorname{osc}_{[U,V]}
a_e^{(R)}(t,\cdot)
\le
L(t)\mathbf P(U_e\ne V_e)+\delta_R(t),
\tag{17}
\]
where
\[
L\in L^1[0,1],
\qquad
\int_0^1\delta_R(t)\,dt\longrightarrow0,
\tag{18}
\]
and the associated finite-block forward equations converge to (8).

Here \(\operatorname{osc}_{[U,V]}\) is the supremum minus infimum over configurations lying between \(U\) and \(V\). Equations (17)–(18) give the usual nested-envelope estimate and then Theorem 4 produces the desired pure-birth factor.

This lemma is stronger than the endpoint target because it constructs the prescribed full path and gives pathwise common-noise stability. No converse from an endpoint map to (17) is known.

Weak compactness is insufficient: a weak limit of monotone joint laws need not be a factor of the fixed input-plus-iid action, and vanishing order-violation probabilities do not imply common-input convergence.

A theorem for every gapped pair and every countable group would also imply invariant monotone couplings for all ordered equivariant contractions: apply it to
\[
C_\delta=\delta I+(1-2\delta)A,
\qquad
D_\delta=\delta I+(1-2\delta)B
\]
and let \(\delta\downarrow0\). Lyons–Thom establish invariant monotone couplings under their finitely generated sofic hypotheses; their theorem does not furnish the stronger relative iid transition for arbitrary countable groups. 
