# S55 cycle08 — A fixed-gap strong-resolvent transfer for actual Shannon curvature

## Status and main theorem

**PROVED, as a new author derivation, not an independent-review verdict.** The scope is the full compact two-parameter legal interior for the actual half-density cyclic and true-sine laws. No endpoint uniformity and no entropy-concavity sign are asserted.

Let
\[
\mathcal L=\{(c,d):0<c<1,\ |d|<(1-c)/2\}.
\]
For every compact \(D\Subset\mathcal L\),
\[
\boxed{\quad
 \lim_{\substack{n\to\infty\\ n\ {\rm even}}}
 \sup_{(c,d)\in D}
 \left|\frac1n\partial_d^2 H_n^{\rm cyc}(c,d)-h_c''(d)\right|=0.
 \quad}                                                    \tag{T}
\]
Here the finite law is exactly
\(\operatorname{DPP}((1-c)I/2+cP_n+dI)\), and \(h_c\) is the already-defined true full-configuration block entropy rate for
\(K_\infty=(1-c)I/2+cQ+dI\).

The proof establishes a stronger interface than a value comparison: both the cyclic Hessian density and the **all-anchor average of exact true-principal-block Hessians** converge to the same bounded quasilocal response. An exact finite-chord identity then identifies that response with the true entropy-rate second derivative. The accepted S51 cycle06 bridge identifies it with \(-\Gamma_c(d)\). Neither a cyclic/Toeplitz entropy discrepancy nor any unquantified thermodynamic value error is differentiated.

At the midpoint, with \(b=(1-c^2)/4\), the exact finite identities are
\[
\boxed{
 \frac1n H_{n,dd}^{\rm cyc}(c,0)
 =-\frac1b+J_n(c)
 =-4-\frac{R_n(c)}n,
 \qquad
 \frac{R_n(c)}n=\frac{c^2}{b}-J_n(c).
}                                                         \tag{M}
\]
Consequently,
\[
\boxed{
 J_n(c)\longrightarrow \frac1b-\Gamma_c(0),\qquad
 \frac{R_n(c)}n\longrightarrow\Gamma_c(0)-4.
}                                                         \tag{MC}
\]
These convergences are uniform when \(c\) ranges over a compact subset of \((0,1)\). The limit of \(J_n\) is also proved below to be the actual infinite all-exterior conditional-pair sum, with its observation limit and its spatial tail both controlled.

The mechanism is **local weak convergence with uniformly summable response, obtained from compact signed-resolvent orbits**. The infinite observation law is never differentiated as a density. Instead, the complete finite entropy Hessian is reorganized before taking limits.

---

## 1. Reusable transfer theorem: primitive assumptions, not an assumed response limit

Consider a parameter \(\theta=(\lambda,d)\) on an open set, with \(d\) the coordinate being differentiated. On \(\ell^2(\mathbb Z)\), let \(K_\theta\) be a translation-invariant Hermitian DPP kernel, norm-continuous in \(\theta\), with
\(K_{\lambda,d}=K_{\lambda,0}+dI\). Let \(K_{m,\theta}\) be finite Hermitian kernels on rooted sets \(V_m=\{0\}\cup C_m\), where every fixed finite subset of \(\mathbb Z\) is eventually contained in \(V_m\). Assume a common transitive permutation group preserves each finite **law family** at every parameter. Kernel translation covariance up to a parameter-independent diagonal gauge is enough.

On every compact parameter set, suppose the following primitive conditions hold.

**Gap.** For a fixed \(0<\varepsilon<1/2\),
\[
 \varepsilon I\preceq K_{m,\theta}\preceq(1-\varepsilon)I,
 \qquad
 \varepsilon I\preceq K_\theta\preceq(1-\varepsilon)I.       \tag{1.1}
\]
The finite families are diagonal shifts: \(\partial_dK_{m,\theta}=I_{V_m}\).

**Rooted strong convergence.** On \(\mathcal H=\ell^2(\mathbb Z\setminus\{0\})\), write
\[
 k_{m,0}=K_{m,00},\quad \xi_m=K_{m,C_m0},\quad
 T_m=E_m(K_{m,C_m}-I_{C_m}/2)E_m,
\]
where vectors and centered exterior operators are extended by zero; \(E_m\) is the coordinate projection onto \(C_m\). Define
\[
 k_0=K_{00},\quad \xi=K_{\mathbb Z\setminus0,0},\quad
 T=K_{\mathbb Z\setminus0}-I/2.
\]
Uniformly in the compact parameter set,
\[
 k_{m,0}\to k_0,\qquad \|\xi_m-\xi\|_2\to0,\qquad
 \|(T_m-T)x\|_2\to0\quad\text{for every fixed }x\in\mathcal H.
                                                               \tag{1.2}
\]
All gauges used in this condition are independent of \(d\). In particular they do not change the diagonal-shift derivative.

**Actual laws.** Finite probabilities and all expectations are those of the DPPs with these kernels. Their finite-cylinder probabilities converge uniformly in the parameter. This last property follows already from (1.2), the root convergence, and the finite determinant formula; it is not an extra probabilistic mixing assumption.

### Transfer theorem

Under these conditions,
\[
 \frac1{|V_m|}\partial_d^2 H(\operatorname{DPP}(K_{m,\theta}))
 \longrightarrow \partial_d^2 h(\theta)
\]
uniformly on compact parameter sets. Here \(h\) is the true stationary block entropy rate of \(K_\theta\). Its twice continuous differentiability in \(d\), and joint continuity of this second derivative in \(\theta\), follow as part of the proof.

No hypothesis about convergence of derivatives of infinite-volume laws, no summability hypothesis on the entries of \(|K|\), and no operator-norm convergence of finite kernels is required. The complete finite jet, the all-word quasilocality, and the spatial response tails are derived in Sections 2–5. Exact true principal blocks and all their anchors identify the limit in Section 7. Section 6 verifies all primitive assumptions for the assigned cycles.

---

## 2. Complete finite entropy response under a diagonal shift

### 2.1 Non-nullness of actual conditional laws

A gapped kernel \(\varepsilon I\preceq K\preceq(1-\varepsilon)I\) can be written
\[
 K=\varepsilon I+(1-2\varepsilon)L,\qquad 0\preceq L\preceq I.
\]
If \(X\sim\operatorname{DPP}(L)\), independently pass each coordinate through the channel
\[
 \Pr(Y_i=1\mid X_i)=\varepsilon+(1-2\varepsilon)X_i.
\]
For completeness, for a finite set \(A\), expansion gives
\[
 \mathbb E\prod_{i\in A}Y_i
 =\sum_{B\subset A}\varepsilon^{|A|-|B|}(1-2\varepsilon)^{|B|}
      \det L_B
 =\det K_A.
\]
Inclusion probabilities determine a binary law by inclusion-exclusion, so the output law is exactly \(\operatorname{DPP}(K)\). The case \(\varepsilon=1/2\) is simply the fair independent law.

The channel noise at an unobserved site is independent of every other output coordinate conditional on \(X\). Thus for any observation sigma-field not containing that site,
\[
 \varepsilon\le\Pr(Y_i=1\mid\text{observations})\le1-\varepsilon.
                                                               \tag{2.1}
\]
For two unobserved sites, each of their four joint conditional atoms is at least \(\varepsilon^2\). These assertions also hold for infinite observation sigma-fields by conditional expectation. Every finite observation atom is positive.

For the assigned models one may use the original latent projections directly: the channel probabilities are
\[
 \alpha=(1-c)/2+d,\qquad \beta=(1+c)/2+d.
\]
On a compact legal set both lie in \([\varepsilon,1-\varepsilon]\). True principal blocks use the marginal of the same latent infinite process, not a fictitious projection block.

### 2.2 Signed-coordinate transport of the entire actual probability vector

Let \(V\) be finite, \(p_d(y)\) its actual DPP probability, and \(\sigma_i=2y_i-1\). Inclusion-exclusion and determinant multilinearity give
\[
 p_d(y)=(-1)^{|V|-|y|}
       \det\bigl(K_d-\operatorname{diag}(1-y)\bigr).        \tag{2.2}
\]
Because \(K_d'=I\), differentiating its determinant by diagonal cofactors gives the exact identity
\[
 \boxed{
 p_d'(y)=\sum_{i\in V}\sigma_i(y)\,p_{d,V\setminus i}(y_{-i}).
 }                                                        \tag{2.3}
\]
The sign is positive for \(y_i=1\) and negative for \(y_i=0\). This is a signed affine-channel derivative, not a Markov generator with asserted nonnegative rates.

Consequently, for every differentiable function \(f_d\) of a finite observation set \(C\),
\[
 \frac d{dd}\mathbb E_d f_d(Y_C)
 =\mathbb E_d\partial_df_d(Y_C)
  +\sum_{j\in C}\mathbb E_{d,C\setminus j}\Delta_jf_d,       \tag{2.4}
\]
where \(\Delta_jf=f(y_j=1)-f(y_j=0)\). All marginal laws on the right are actual marginals of \(p_d\).

Write
\[
 q_i(z)=\Pr_d(Y_i=1\mid Y_{V\setminus i}=z),\qquad
 h_i(z)=\log\frac{q_i(z)}{1-q_i(z)}.
\]
Since \(\sum_yp_d'(y)=0\), substituting (2.3) in the derivative of Shannon entropy and pairing \(y_i=0,1\) yields
\[
 \boxed{H_V'(d)=-\sum_{i\in V}\mathbb E_d h_i.}              \tag{2.5}
\]
Differentiate this **exact identity**, including its observation marginal, using (2.4):
\[
 \boxed{
 H_V''(d)=
 -\sum_i\mathbb E_d\partial_dh_i
 -\sum_{i\ne j}\mathbb E_{d,V\setminus\{i,j\}}\Delta_jh_i.
 }                                                        \tag{2.6}
\]
In particular the second sum is over ordered pairs. It is the moving-observation-law contribution and cannot be discarded.

This is a regrouping of the full classical Hessian
\[
 H_V''=-\sum_yp_d''(y)\log p_d(y)
       -\sum_y\frac{(p_d'(y))^2}{p_d(y)}.                   \tag{2.7}
\]
It is not the second derivative of a single-site conditional entropy. No posterior-acceleration or score term has been omitted: (2.5) is the first derivative of the entire entropy, and (2.6) differentiates both factors of each actual expectation.

### 2.3 Resolvent form of the fixed-word derivative

At an anchor, call its observation set \(C\), and write
\[
 K=\begin{pmatrix}k_0&\xi^*\\ \xi&K_C\end{pmatrix},\qquad
 S_z=\operatorname{diag}(2z_j-1),
\]
\[
 B_z=K_C-\operatorname{diag}(1-z)=S_z/2+T,
 \quad T=K_C-I_C/2,
 \quad G_z=B_z^{-1},\quad v_z=G_z\xi.                      \tag{2.8}
\]
The spectral gap implies \(\|T\|\le1/2-\varepsilon\). Factoring
\(B_z=(S_z/2)(I+2S_zT)\) gives
\[
 G_z=2\sum_{r\ge0}(-2S_zT)^rS_z,
 \qquad \|G_z\|\le\varepsilon^{-1},                        \tag{2.9}
\]
uniformly in every observation word and every volume.

The Schur complement in (2.2) gives
\[
 q_z=k_0-\xi^*G_z\xi.                                    \tag{2.10}
\]
Since \(k_0'=1\), \(\xi'=0\), and \(G_z'=-G_z^2\),
\[
 q_z'=1+\|v_z\|_2^2=:A_z,
 \qquad
 \partial_d\log\frac{q_z}{1-q_z}
    =\frac{A_z}{q_z(1-q_z)}.                              \tag{2.11}
\]
Hermiticity is important here: \(\xi^*G_z^2\xi=\|G_z\xi\|^2\), also for the complex cyclic kernel.

---

## 3. The quadratic influence certificate

Let \(z^j\) denote the flip of bit \(j\), and let
\[
 w_z=\Pr(Y_C=z),\qquad o_j(z)=w_{z^j}/w_z.
\]
Non-nullness gives
\[
 \frac{\varepsilon}{1-\varepsilon}\le o_j\le
 \frac{1-\varepsilon}{\varepsilon}.                       \tag{3.1}
\]
A flip changes \(B_z\) to \(B_z-\sigma_je_je_j^*\). The determinant lemma, including the sign change in (2.2), and the rank-one inverse formula give
\[
 o_j=\sigma_j(G_z)_{jj}-1,
\]
\[
 G_{z^j}=G_z-\frac{\sigma_j}{o_j}G_ze_je_j^*G_z,
 \qquad
 q_{z^j}-q_z=\frac{\sigma_j|v_{z,j}|^2}{o_j}.              \tag{3.2}
\]
Let \(g(q)=\log(q/(1-q))\), and define the nonnegative pair influence
\[
 \ell_j(z)=g(q(z^{j,0}))-g(q(z^{j,1}))
          =\sigma_j[g(q(z^j))-g(q(z))].                   \tag{3.3}
\]
It is independent of the current value of \(z_j\). Since
\(\sup_{[\varepsilon,1-\varepsilon]}g'=1/[\varepsilon(1-\varepsilon)]\),
\[
 \boxed{
 0\le\ell_j(z)\le\varepsilon^{-2}|v_{z,j}|^2.
 }                                                       \tag{3.4}
\]
This bound covers occupied and unoccupied observation sites at once.

Define the finite anchored response
\[
 \boxed{
 \mathcal T_C(\theta,z)=
 -\frac{1+\|v_z\|_2^2}{q_z(1-q_z)}+\sum_{j\in C}\ell_j(z).
 }                                                       \tag{3.5}
\]
Because each \(\ell_j\) is independent of \(z_j\), its expectation under \(Y_C\) equals its expectation under the actual remaining marginal \(Y_{C\setminus j}\). Equations (2.6) and (2.11) therefore become
\[
 \boxed{
 H_V''(\theta)=\sum_{i\in V}
    \mathbb E_\theta\mathcal T_{V\setminus i}^{(i)}.
 }                                                       \tag{3.6}
\]

The gap already bounds every off-diagonal root column by \(1/2-\varepsilon\), because it is a coordinate compression of \((K-I/2)e_i\). Let \(B_*\) be this bound or a sharper model-specific bound, and set
\[
 V_*=B_*/\varepsilon,\qquad
 L_\varepsilon=\frac1{\varepsilon(1-\varepsilon)}.
\]
A dimension-free, all-word bound is
\[
 |\mathcal T_C|\le
 M:=L_\varepsilon(1+V_*^2)+\varepsilon^{-2}V_*^2.           \tag{3.7}
\]
More importantly, for any spatial cutoff \(F\),
\[
 \boxed{
 \sum_{j\notin F}\ell_j(z)
 \le\varepsilon^{-2}\|1_{F^c}v_z\|_2^2.
 }                                                       \tag{3.8}
\]
The remainder of the proof derives the needed uniform tail on the right; it does not assume it.

---

## 4. Abstract signed-resolvent compactness lemma

This section is a functional-analysis tool with no DPP assumption.

Let \(\Theta\) be compact and \(\Omega=\{0,1\}^{\mathbb Z\setminus0}\) have its product topology, with \(S_z=\operatorname{diag}(2z_j-1)\). Let \(T_\theta\) be a norm-continuous family of self-adjoint operators and \(\xi_\theta\) a norm-continuous vector family, with
\[
 \|T_\theta\|\le1/2-\varepsilon.
\]
Let \(T_{m,\theta}\) satisfy the same bound and converge strongly to \(T_\theta\), uniformly in \(\theta\) on each fixed vector. Suppose \(\xi_{m,\theta}\to\xi_\theta\) uniformly in norm. Put
\[
 v(\theta,z)=(S_z/2+T_\theta)^{-1}\xi_\theta,
 \qquad
 v_m(\theta,z)=(S_z/2+T_{m,\theta})^{-1}\xi_{m,\theta}.
\]

### Lemma 4.1

The map \((\theta,z)\mapsto v(\theta,z)\) is continuous into \(\ell^2\). Its image has compact closure. Moreover,
\[
 \boxed{
 \sup_{\theta,z}\|v_m(\theta,z)-v(\theta,z)\|_2\longrightarrow0.
 }                                                       \tag{4.1}
\]
For the coordinate sets \(F_R=\{j:0<|j|\le R\}\), write \(E_R\) for the associated coordinate projections. Then
\[
 \tau_R:=\sup_{\theta,z}\|(I-E_R)v(\theta,z)\|_2
 \longrightarrow0,                                      \tag{4.2}
\]
and
\[
 \lim_{R\to\infty}\limsup_m\sup_{\theta,z}
 \|(I-E_R)v_m(\theta,z)\|_2=0.                            \tag{4.3}
\]

### Proof

First, if \(z_r\to z\) in the product topology, then
\(S_{z_r}x\to S_zx\) in \(\ell^2\) for every fixed \(x\). To see this, choose a finite coordinate set carrying all but an arbitrarily small squared tail of \(x\). Signs agree on that finite set eventually, and the squared error on the complement is at most four times that tail.

All inverses have norm at most \(\varepsilon^{-1}\) by (2.9). For convergent \((\theta_r,z_r)\to(\theta,z)\), the resolvent identity gives, with \(v=v(\theta,z)\),
\[
 v(\theta_r,z_r)-v
 =(S_{z_r}/2+T_{\theta_r})^{-1}
 \left[\xi_{\theta_r}-\xi_\theta
 -(T_{\theta_r}-T_\theta)v
 -(S_{z_r}-S_z)v/2\right].                               \tag{4.4}
\]
The bracket tends to zero in norm. Thus the map is continuous. Since \(\Theta\times\Omega\) is compact, its vector image \(\mathcal V\) is compact.

Uniformly bounded strong convergence is uniform on compact vector sets: cover \(\mathcal V\) by a finite small norm net, use strong convergence on the finitely many net points, and use the common operator bound to control the approximation errors. This argument remains uniform in \(\theta\), because the assumed strong convergence is uniform on every fixed vector.

Now use the comparison identity
\[
 v_m-v=(S_z/2+T_{m,\theta})^{-1}
        [\xi_{m,\theta}-\xi_\theta-(T_{m,\theta}-T_\theta)v].
                                                               \tag{4.5}
\]
Uniform convergence on the compact set \(\mathcal V\) and the inverse bound imply (4.1).

A compact set of \(\ell^2\) vectors has uniformly vanishing coordinate tails: take a finite small norm net and then a cutoff controlling every net point. This proves (4.2). Finally
\[
 \|(I-E_R)v_m\|\le\tau_R+\sup_{\theta,z}\|v_m-v\|
\]
proves (4.3). This pays both the all-sign-word supremum and the spatial tail. No convergence in operator norm was used. \(\square\)

### An explicit two-scale comparison bound

Write
\[
 \delta_m=\sup_{\theta,z}\|v_m-v\|,
 \quad \beta_m=\sup_\theta\|\xi_m-\xi\|,
 \quad a_m(R)=\sup_\theta\|(T_m-T)E_R\|.
\]
The proof gives
\[
 \boxed{
 \delta_m\le\varepsilon^{-1}
 [\beta_m+V_*a_m(R)+(1-2\varepsilon)\tau_R].
 }                                                       \tag{4.6}
\]
For each fixed \(R\), \(a_m(R)\to0\) by finite dimensionality. Equation (4.2) proves \(\tau_R\to0\). Thus (4.6) is a proved vanishing modulus, not a hypothesized response limit.

The Neumann series also has the honest gap-dependent truncation estimate
\[
 \left\|v-2\sum_{r=0}^{N}(-2S_zT)^rS_z\xi\right\|
 \le \frac{B_*}{\varepsilon}(1-2\varepsilon)^{N+1}.         \tag{4.7}
\]
No explicit rate in the physical volume is claimed here.

---

## 5. Transfer of the complete response and of the moving actual expectation

### 5.1 Uniform all-word convergence of the response

Apply Lemma 4.1 to the exterior operators and root columns in Section 1. The root scalar convergence and (2.10) imply
\[
 \eta_m:=\sup_{\theta,z}|q_m-q|\longrightarrow0,
 \qquad
 \sup_{\theta,z}|A_m-A|\longrightarrow0.                  \tag{5.1}
\]
Here \(A=1+\|v\|^2\). For example,
\[
 \eta_m\le\sup_\theta|k_{m,0}-k_0|+V_*\beta_m+B_*\delta_m.
                                                               \tag{5.2}
\]
The infinite posterior is obtained also from true finite observation windows, as proved in Section 7. Therefore it has the same all-word range \([\varepsilon,1-\varepsilon]\). Define \(\ell_j\) by (3.3) using this posterior. Taking limits of the finite rank-one inequalities for any fixed \(j\) gives
\[
 0\le\ell_j\le\varepsilon^{-2}|v_j|^2.                    \tag{5.3}
\]
Thus \(\sum_j\ell_j\) converges uniformly over parameters and all words, with tail at most \(\varepsilon^{-2}\tau_R^2\). Define
\[
 \mathcal T_\infty=-\frac{1+\|v\|^2}{q(1-q)}+\sum_{j\ne0}\ell_j.
                                                               \tag{5.4}
\]
It is bounded by \(M\) and jointly continuous in the parameter and the product word topology.

Each fixed flip is a homeomorphism of word space, and (5.1) is uniform over all words. Therefore finite collections of \(\ell_{m,j}\) converge uniformly. Their omitted tails are bounded by (3.8) and Lemma 4.1. Consequently,
\[
 \boxed{\sup_{\theta,z}|\mathcal T_m-\mathcal T_\infty|\to0.}
                                                               \tag{5.5}
\]
An explicit estimate, with \(F_R\) containing \(2R\) sites, is
\[
\begin{split}
 \|\mathcal T_m-\mathcal T_\infty\|_\infty
 \le{}&2V_*L_\varepsilon\delta_m
 +[(1+V_*^2)L_\varepsilon^2+4RL_\varepsilon]\eta_m\\
 &+\varepsilon^{-2}[(\tau_R+\delta_m)^2+\tau_R^2].          \tag{5.6}
\end{split}
\]
Indeed, the derivative of \(1/[q(1-q)]\) has absolute value at most \(L_\varepsilon^2\), each retained \(\ell_j\) changes by at most \(2L_\varepsilon\eta_m\), and the two tails have the displayed square bounds. Taking \(m\to\infty\) first and \(R\to\infty\) second proves (5.5).

The proof does not estimate \(n-1\) influences individually by one error and then multiply by \(n\). It truncates the sum first, using the proved squared-response tail.

### 5.2 Local weak convergence with varying observables and varying laws

The following elementary probability lemma is independent of DPP theory. Suppose \(\mu_{m,\theta}\) and \(\mu_\theta\) are laws on product word space whose probabilities on each fixed finite cylinder converge uniformly in \(\theta\). Suppose \(f\) is continuous on the compact product \(\Theta\times\Omega\), and \(\|f_m-f\|_\infty\to0\). Then
\[
 \sup_\theta|\mathbb E_{\mu_{m,\theta}}f_m
                   -\mathbb E_{\mu_\theta}f|\to0.         \tag{5.7}
\]

To prove it, fix a default outside word and replace \(f\) by the function \(f^{[R]}\) obtained by retaining only the coordinates \(F_R\). Compactness and continuity give \(\|f-f^{[R]}\|_\infty\to0\). The expectation difference for \(f^{[R]}\) is a finite sum controlled by the finite-cylinder total-variation distance. Finally control \(f_m-f\) by its sup norm. Equivalently, the error is at most
\[
 \|f_m-f\|_\infty+2\|f-f^{[R]}\|_\infty
       +2\|f\|_\infty\operatorname{TV}(
                  \mu_{m,\theta}|_{F_R},\mu_\theta|_{F_R}).
                                                               \tag{5.8}
\]
Finite-cylinder continuity in \(\theta\) proves continuity of \(\theta\mapsto\mathbb E_{\mu_\theta}f\) by the same argument.

Apply this to \(\mathcal T_m\) and \(\mathcal T_\infty\), with the **actual parameter-dependent exterior laws**. Set
\[
 C(\theta)=\mathbb E_{\mu_\theta}\mathcal T_\infty(\theta,Y_{\ne0}).
                                                               \tag{5.9}
\]
Then \(C\) is jointly continuous. Transitivity of the finite laws and the exact all-anchor identity (3.6) give
\[
 \frac1{|V_m|}H_{V_m}''(\theta)
 =\mathbb E_{\mu_{m,\theta}}\mathcal T_m
 \longrightarrow C(\theta)                               \tag{5.10}
\]
uniformly on compact parameter sets. Section 7 identifies \(C\) with the true entropy-rate derivative rather than merely naming it a curvature limit.

---

## 6. Verification for the exact cycles: gauge, wrap-around, gap, and local laws

Fix \(D\Subset\mathcal L\), and put
\[
 \varepsilon=\min_{(c,d)\in D}\left((1-c)/2-|d|\right)>0,
 \qquad c_* =\max_D c.
                                                               \tag{6.1}
\]
For all cycles and all true principal blocks, the actual kernels have spectra in \([\varepsilon,1-\varepsilon]\). Their root columns have norm at most \(c_*/2\), so in Sections 3–5 one can take
\[
 B_*=c_*/2,\qquad V_*=c_*/(2\varepsilon).                  \tag{6.2}
\]

### 6.1 Exact rooted gauge

Let \(n=2k\), and label the cycle by the consecutive representatives
\(I_n=\{-k,-k+1,\ldots,k-1\}\). For \(s,t\in I_n\), \(s\ne t\), a finite geometric sum gives
\[
 P_n(s,t)=
 e^{\pi i(k-1)(s-t)/n}
 \frac{\sin(\pi(s-t)/2)}{n\sin(\pi(s-t)/n)}.              \tag{6.3}
\]
Define the diagonal unitary
\[
 U_n(s,s)=e^{-\pi i(k-1)s/n}.
\]
The gauged projection is exactly
\[
 \widetilde P_n=U_nP_nU_n^*,\qquad
 \widetilde P_n(s,t)=
 \begin{cases}
 1/2,&s=t,\\
 \displaystyle\frac{\sin(\pi(s-t)/2)}{n\sin(\pi(s-t)/n)},&s\ne t.
 \end{cases}                                             \tag{6.4}
\]
Every principal determinant, and therefore the entire actual DPP law, is unchanged by this gauge.

The gauge need not be periodic as a function of an arbitrary integer representative: its boundary twist is \((-1)^{k-1}\). That does not invalidate the gauge on the chosen finite set. Nor is the gauged matrix silently treated as an ordinary real circulant matrix. Its law remains cyclically transitive because the original Fourier kernel is circulant.

For distinct sites, write \(\operatorname{dist}_n(s,t)\) for cyclic distance. Since \(\sin x\ge2x/\pi\) on \([0,\pi/2]\), (6.4) gives
\[
 |\widetilde P_n(s,t)|\le\frac1{2\operatorname{dist}_n(s,t)}.
                                                               \tag{6.5}
\]
At the root \(0\), \(\operatorname{dist}_n(0,j)=|j|\) for our representatives, including the single antipodal site. Thus the remote root-column squared mass is at most \(1/(2R)\) outside \(0<|j|\le R\). The seam is not mistaken for a nearby site or discarded.

### 6.2 Strong, not merely entrywise, convergence

Extend \(\widetilde P_n\) by zero to \(\ell^2(\mathbb Z)\), calling the resulting orthogonal projection \(\Pi_n\). For fixed \(s,t\), (6.4) tends to
\[
 Q_{st}=\frac{\sin(\pi(s-t)/2)}{\pi(s-t)}
\]
with the diagonal convention \(Q_{ss}=1/2\). The Fourier multiplier of \(Q\) is the indicator of \([-\pi/2,\pi/2]\), so \(Q\) is indeed an orthogonal projection.

For a fixed coordinate \(j\), entry convergence and the uniform operator bound imply \(\Pi_ne_j\rightharpoonup Qe_j\). Furthermore, eventually
\[
 \|\Pi_ne_j\|^2=(\Pi_n)_{jj}=1/2
              =Q_{jj}=\|Qe_j\|^2.
\]
Weak convergence together with convergence of these norms gives strong convergence of each column. Density of finitely supported vectors and \(\|\Pi_n\|,\|Q\|\le1\) imply
\[
 \boxed{\Pi_n\to Q\quad\text{strongly on }\ell^2(\mathbb Z).}
                                                               \tag{6.6}
\]
This explicit norm argument is the upgrade beyond entrywise local convergence.

For comparison, operator-norm convergence is impossible: \(\Pi_n\) has finite rank while \(Q\) has infinite rank. Choose a unit vector in \(\operatorname{ran}Q\cap\ker\Pi_n\); then \(\|(\Pi_n-Q)x\|=1\). In fact \(\|\Pi_n-Q\|=1\). This disproves an unnecessary operator-norm ansatz, not the assigned curvature theorem.

### 6.3 Centered exterior operators

Let \(E\) remove the root and let \(E_n\) project onto \(I_n\setminus\{0\}\). On \(\mathcal H\), define
\[
 T_n(c,d)=c(E\Pi_nE-E_n/2)+dE_n,
 \qquad \xi_n(c)=cE\Pi_ne_0,
\]
\[
 T(c,d)=c(Q_{\mathbb Z\setminus0}-I/2)+dI,
 \qquad \xi(c)=cQ_{\mathbb Z\setminus0,0}.
                                                               \tag{6.7}
\]
Both centered operators have norm at most \(c/2+|d|\le1/2-\varepsilon\). Equation (6.6) and \(E_n\to I\) strongly give (1.2), uniformly in \((c,d)\in D\), because the parameter dependence is affine with bounded coefficients. Also
\[
 k_{n,0}=k_0=1/2+d,\qquad
 \|\xi_n(c)\|=\|\xi(c)\|=c/2.                             \tag{6.8}
\]
Thus every primitive operator hypothesis of the transfer theorem is verified.

Only the **centered exterior perturbation** is zero-extended in the signed inverse. Outside the finite observation set, \((S_z/2+T_n)^{-1}=2S_z\), and \(v_n=0\). These outside coordinates cannot contribute a flip term. One may extend the finite output law by independent fair bits outside \(I_n\); this changes none of its finite actual probabilities or responses.

### 6.4 Actual local laws and all finite anchors

For any fixed finite set \(F\), eventually \(F\subset I_n\). Its actual atom probabilities are
\[
 \Pr_{n,c,d}(Y_F=y)
 =(-1)^{|F|-|y|}
  \det\left((K_{n}^{\rm gauged})_F-\operatorname{diag}(1-y)\right).
                                                               \tag{6.9}
\]
The matrix entries converge uniformly on \(D\). This finite collection of determinant polynomials therefore converges uniformly, hence in total variation on each fixed \(F\), to the true sine marginal. This is convergence of the actual observation laws, not a corrected or count-conditioned law.

Cyclic transitivity holds for the law at every parameter. Therefore (3.6) is exactly \(n\) times its rooted expected response. No arbitrary Toeplitz boundary anchor has been substituted for a central one.

---

## 7. All-exterior observation limit, all true-block anchors, and rate identification

This section applies to the limiting translation-invariant kernel of the general transfer theorem. For the assigned application its auxiliary parameter is denoted by \(c\); the same proof applies with \(\lambda\) in its place.

### 7.1 True finite observation sets approaching the whole exterior

Use the limiting exact kernel. For any finite \(C\subset\mathbb Z\setminus0\), the exact finite-observation signed inverse is represented on \(\mathcal H\) by
\[
 T_C=E_CTE_C,\qquad \xi_C=E_C\xi,
 \qquad G_C=(S_z/2+T_C)^{-1}.                             \tag{7.1}
\]
It yields exactly \(q_C=\Pr(Y_0=1\mid Y_C)\), by the Schur complement; it is not a projection-Ward approximation.

This convergence is uniform over **all** finite sets containing a growing centered neighborhood. For a fixed vector \(x\), whenever \(C\supset F_R\),
\[
 \|(E_CTE_C-T)x\|
 \le\|T\|\|(I-E_R)x\|+\|(I-E_R)Tx\|.                     \tag{7.2}
\]
The right side tends to zero uniformly in the compact parameter set. For the second term this follows from compactness of \(\{T_\theta x:\theta\in D\}\). Also
\(\|(E_C-I)\xi\|\le\|(I-E_R)\xi\|\), uniformly in \(\theta\).

Lemma 4.1 applies with the directed condition \(C\supset F_R\). Its proof only uses these uniform strong bounds and is unchanged for this directed family. Hence
\[
 \sup_{C\supset F_R}\sup_{\theta,z}\|v_C-v\|\to0,
 \qquad
 \sup_{C\supset F_R}\sup_{\theta,z}|q_C-q|\to0.            \tag{7.3}
\]
For \(C=F_R\), \(q_C(Y_C)\) is a bounded conditional-expectation martingale. Its almost-sure and \(L^1\) limit is the actual posterior conditioned on all exterior output coordinates. Uniform convergence in (7.3) proves that the resolvent formula defines a continuous version of this actual posterior. In particular its all-word values lie in \([\varepsilon,1-\varepsilon]\), as used in Section 5.

For any fixed flip \(j\), take \(R\ge|j|\) in the finite identities. This proves (5.3) for the infinite version. The same finite-index-plus-squared-tail argument as (5.6) gives
\[
 \omega_R:=\sup_{C\supset F_R}\sup_{\theta,z}
             |\mathcal T_C-\mathcal T_\infty|\longrightarrow0.
                                                               \tag{7.4}
\]
There is no assumption that all such \(C\) are symmetric intervals.

### 7.2 Every anchor of an exact Toeplitz block

Let \(A_L=\{1,\ldots,L\}\) and let \(H_L^{\rm true}\) be its full configuration entropy. For an anchor \(i\) at distance at least \(R\) from both ends, shift coordinates by \(-i\). Its exact observation set is
\(C=(A_L-i)\setminus\{0\}\supset F_R\). By stationarity its expected response differs from \(C(\theta)\) in (5.9) by at most \(\omega_R\).

There are at most \(2R\) boundary anchors, and each finite and infinite response is bounded by \(M\). Thus for \(L>2R\), the exact all-anchor Hessian identity gives
\[
 \boxed{
 \sup_{\theta\in D}
 \left|\frac1L\partial_d^2H_L^{\rm true}(\theta)-C(\theta)\right|
 \le\omega_R+\frac{4MR}{L}.
 }                                                       \tag{7.5}
\]
First send \(L\to\infty\), then \(R\to\infty\). This proves compact-uniform true-block Hessian convergence, with every anchor and its boundary geometry paid.

### 7.3 Identification with the already-defined true entropy rate

Stationarity and subadditivity give
\[
 h_c(d)=\lim_{L\to\infty}\frac1L H_L^{\rm true}(c,d).
\]
Equation (2.5) and non-nullness imply the uniform derivative bound
\[
 \left|\frac1L\partial_d H_L^{\rm true}\right|
 \le\log\frac{1-\varepsilon}{\varepsilon}.                 \tag{7.6}
\]
Hence the pointwise limit \(h_c\) is locally Lipschitz, in particular continuous.

Fix \(c\) and a chord \([d-t,d+t]\) inside the legal interval. Apply the preceding estimates on a compact legal set containing this chord. For every \(L\), ordinary finite calculus gives
\[
 \Delta_t\left(\frac1L H_L^{\rm true}\right)(c,d)
 =\int_{-t}^{t}(t-|s|)
       \frac1L\partial_d^2H_L^{\rm true}(c,d+s)\,ds.       \tag{7.7}
\]
Pointwise value convergence at the three chord points and the already proved uniform Hessian convergence (7.5) give
\[
 \Delta_t h_c(d)=\int_{-t}^{t}(t-|s|)C(c,d+s)\,ds.         \tag{7.8}
\]
Since \(C\) is continuous, choose a twice differentiable function with second derivative \(C(c,\cdot)\) and subtract it from \(h_c\). The continuous difference has every symmetric second difference equal to zero, hence is affine on each interval. Therefore
\[
 \boxed{h_c\in C^2,\qquad h_c''(d)=C(c,d).}                \tag{7.9}
\]
This proof does not differentiate a value error: the curvature convergence was established first from the complete finite response; values enter only at three fixed points in the exact chord identity.

The accepted S51 cycle06 result identifies this same true entropy-rate derivative as \(h_c''(d)=-\Gamma_c(d)\) on compact legal interiors [R1–R2]. Thus
\[
 C(c,d)=-\Gamma_c(d).                                    \tag{7.10}
\]
The use of that accepted result is solely for the identification with its named \(\Gamma\); no pending S51 C1 renormalization, S52, S54, or QWE claim is an input.

Combining (5.10), the verification in Section 6, and (7.9) proves (T), uniformly over every compact two-parameter legal set. No cyclic value convergence is needed at all. This completes the reusable transfer theorem and its application. \(\square\)

---

## 8. Exact midpoint Ward identity, entropy signs, and ordered-pair factors

### 8.1 Leakage-free Ward identity for a full projection

Let \(P\) be a finite orthogonal projection, \(K=(1-c)I/2+cP\), and \(b=(1-c^2)/4\). Then
\[
 K(I-K)=bI.                                               \tag{8.1}
\]
Condition at an anchor on its entire finite exterior. In (2.8), put
\(D_z=\operatorname{diag}(1-z)\), \(v=(K_C-D_z)^{-1}\xi\), and
\[
 x=\begin{pmatrix}1\\-v\end{pmatrix}.
\]
The defining exterior equation gives
\[
 Kx=\begin{pmatrix}q\\-D_zv\end{pmatrix}.
\]
Since \(D_z^2=D_z\),
\[
 x^*Kx=q+v^*D_zv,
 \qquad \|Kx\|^2=q^2+v^*D_zv.
\]
Subtracting and using (8.1),
\[
 \boxed{q(1-q)=b(1+\|v\|^2).}                            \tag{8.2}
\]
This is a fixed-word identity. Together with (2.11) it proves
\[
 \left.\partial_d h_i(z)\right|_{d=0}=1/b                 \tag{8.3}
\]
for every exterior word, not only after expectation.

### 8.2 What changes for a true finite Toeplitz block

For \(Q_A\) a principal compression of the infinite projection,
\[
 K_A(I-K_A)=bI_A+c^2(Q_A-Q_A^2).
\]
The same quadratic-form computation gives the **correct** finite-block identity
\[
 \boxed{
 q(1-q)=b(1+\|v\|^2)+c^2x^*(Q_A-Q_A^2)x.
 }                                                       \tag{8.4}
\]
The leakage is nonnegative and generally nonzero. The proof of the transfer never removes this term on finite true blocks.

For the singleton \(A=\{0\}\), \(Q_A=1/2\), \(q=1/2\), \(v=0\), and the omitted leakage would be \(c^2/4\). Thus the leakage-free finite-Toeplitz shortcut is **DISPROVED**. This is a counterexample to that shortcut, not to the cyclic projection model or theorem (T).

### 8.3 Actual pair cross-ratios

Fix distinct \(i,j\) and condition on all remaining sites. Let the actual four conditional probabilities be \(p_{ab}^{(i,j)}\), with \(a\) the bit at \(i\). Then
\[
 h_i(Y_j=1)=\log\frac{p_{11}}{p_{01}},\qquad
 h_i(Y_j=0)=\log\frac{p_{10}}{p_{00}},
\]
so
\[
 \Delta_jh_i
 =\log\frac{p_{11}p_{00}}{p_{01}p_{10}}
 =-\log\frac{p_{10}p_{01}}{p_{00}p_{11}}.                 \tag{8.5}
\]
Insert (8.3) and (8.5) into the full finite entropy identity (2.6):
\[
 H_{n,dd}^{\rm cyc}(c,0)
 =-n/b+\sum_{i\ne j}\mathbb E
          \log\frac{p_{10}^{(i,j)}p_{01}^{(i,j)}}
                    {p_{00}^{(i,j)}p_{11}^{(i,j)}}
 =-n/b+nJ_n(c).                                          \tag{8.6}
\]
The sum is ordered. There is no factor \(1/2\).

By the definition in the task,
\[
 R_n=-nJ_n+nc^2/b.
\]
Since \(4b+c^2=1\), this proves every identity in (M).

A two-site check makes the factor visible. At \(n=2\), put \(t=(1+c^2)/4\). The four midpoint atom probabilities are \(b,t,t,b\), so
\[
 J_2=2\log(t/b),\qquad
 H_{2,dd}^{\rm cyc}/2=-1/b+2\log(t/b).
\]
This agrees with differentiating the four exact probabilities
\(b-d+d^2,t-d^2,t-d^2,b+d+d^2\).

---

## 9. The actual infinite conditional-pair sum

For each \(j\ne0\), let
\[
 \mathcal F_j=\sigma(Y_i:i\notin\{0,j\}),\qquad
 p_{ab}^{(0,j)}=\Pr(Y_0=a,Y_j=b\mid\mathcal F_j)
\]
under the true sine output law. These are genuine all-exterior conditional probabilities: they are limits of the corresponding conditional-expectation martingales over finite observation sets. Non-nullness gives \(p_{ab}^{(0,j)}\ge\varepsilon^2\) almost surely.

Let \(q_b\) be the continuous all-exterior posterior from Section 7 with its \(j\)-th bit set equal to \(b\). The tower property gives
\[
 p_{1b}^{(0,j)}=q_b\,[p_{0b}^{(0,j)}+p_{1b}^{(0,j)}].       \tag{9.1}
\]
Indeed, condition \(1_{\{Y_j=b\}}\mathbb E[Y_0\mid Y_{\ne0}]\) on \(\mathcal F_j\); \(q_b\) is \(\mathcal F_j\)-measurable. Thus, almost surely,
\[
 \log\frac{p_{10}^{(0,j)}p_{01}^{(0,j)}}
           {p_{00}^{(0,j)}p_{11}^{(0,j)}}
 =g(q_0)-g(q_1)=\ell_j.                                 \tag{9.2}
\]
For a fixed pair, finite-observation versions converge uniformly by (7.3), including after the flip of \(j\). No entrywise-kernel argument is substituted for the all-exterior observation limit.

The deterministic bound
\[
 \sup_{\theta,z}\sum_{|j|>R}\ell_j(\theta,z)
 \le\varepsilon^{-2}\tau_R^2\longrightarrow0             \tag{9.3}
\]
pays the infinite spatial sum. Hence define the genuine, finite quantity
\[
 \boxed{
 J_\infty(c,d)=\sum_{j\ne0}\mathbb E_{c,d}
       \log\frac{p_{10}^{(0,j)}p_{01}^{(0,j)}}
                 {p_{00}^{(0,j)}p_{11}^{(0,j)}}
 =\mathbb E_{c,d}\sum_{j\ne0}\ell_j.
 }                                                       \tag{9.4}
\]
Interchanging expectation and summation is justified by (9.3), or by nonnegativity together with the finite uniform bound. The sum contains both positive and negative integer offsets; this is the per-root ordered-pair normalization.

Cyclic transitivity, fixed-pair convergence of actual expectations from Section 5, and the cyclic version of the same uniform tail prove
\[
 J_n(c)\longrightarrow J_\infty(c,0)                       \tag{9.5}
\]
uniformly on compact \(c\)-sets. This passage controls all \(n-1\) terms rather than only finitely many specified pairs.

The infinite projection itself also satisfies the Ward identity (8.2): use \(x=(1,-v)\in\ell^2(\mathbb Z)\), the bounded operator \(K_\infty\), and the exterior diagonal projection \(D_z\) in the same quadratic-form computation. All terms are finite because \(v\in\ell^2\). Therefore at the midpoint
\[
 h_c''(0)=-1/b+J_\infty(c,0).
\]
Combining this with the accepted identification \(h_c''(0)=-\Gamma_c(0)\),
\[
 \boxed{\Gamma_c(0)=1/b-J_\infty(c,0).}                   \tag{9.6}
\]
This is an independently supplied fixed-gap proof of that identity. It is not an invocation or certification of the pending S51 C1 endpoint-renormalization paper. No assertion as \(c\to1\) follows from it here.

---

## 10. Scoped comparison with the corrected-law ledger

This section uses only the separately reviewed S43 ledger [R3–R4], at each fixed \(c\):
\[
 W_n+C_n=R_n+n\Psi_n+o(n),\qquad
 \widehat H_n''(a_*)=-4n-W_n-C_n+o(n),
\]
\[
 \Psi_n=\frac1n\sum_l\kappa_lD(\mu_l\Vert\gamma_{l,c}),
 \qquad a_*=(1-c)/2.
                                                               \tag{10.1}
\]
Here \(\mu_l\) is the prescribed corrected heat law and \(\gamma_{l,c}\) is the actual cyclic law conditioned on count. They remain different laws. The asymptotic remainders in this imported ledger are not asserted to be uniform in \(c\).

Use (M) and theorem (T), without differentiating a ledger remainder:
\[
 \boxed{
 \frac1n\widehat H_n''(a_*)=h_c''(0)-\Psi_n(c)+o(1)
                         =-\Gamma_c(0)-\Psi_n(c)+o(1).
 }                                                       \tag{10.2}
\]

If
\[
 L\le\liminf_n\Psi_n\le\limsup_n\Psi_n\le U,
\]
then the correct directions are
\[
 \boxed{
 h_c''(0)-U
 \le\liminf_n\frac{\widehat H_n''}{n}
 \le\limsup_n\frac{\widehat H_n''}{n}
 \le h_c''(0)-L.
 }                                                       \tag{10.3}
\]
Thus a **lower** bound on \(\Psi_n\) gives an upper bound on corrected curvature. If \(h_c''(0)<L\), corrected curvature is eventually strictly negative. If \(h_c''(0)>U\), it is eventually strictly positive. Borderline non-strict inequalities imply asymptotic bounds, not an eventual finite-volume sign in the presence of \(o(1)\).

Conversely, asymptotic corrected concavity, \(\limsup\widehat H_n''/n\le0\), together with the upper bound \(\limsup\Psi_n\le U\), implies only \(h_c''(0)\le U\). It implies true concavity from these data when \(U\le0\), not for an arbitrary positive budget. True concavity by itself need not imply corrected concavity if the unknown signed correction can be negative.

The reviewed budget is
\[
 -B_c\le\liminf\Psi_n\le\limsup\Psi_n\le B_c,
\]
\[
 B_c=M_bD_c,\quad
 M_b=\frac{2e^{-1/2}}{\sqrt{2\pi}\,b},\quad
 D_c=\frac{\rho_c-1-\log\rho_c}{2},\quad
 \rho_c=1-\frac{c^2\log c}{2b}.                            \tag{10.4}
\]
It yields
\[
 h_c''(0)-B_c\le\liminf\widehat H_n''/n
 \le\limsup\widehat H_n''/n\le h_c''(0)+B_c.
\]
For example, the strict sufficient condition \(\Gamma_c(0)>B_c\) would ensure eventual corrected midpoint concavity. No such sign or margin is proved here. S54's pending smaller loss is not used.

---

## 11. Finite diagnostics and precise limitations

The accompanying `S55_CYCLE08_checks.py` uses analytic determinant derivatives and the signed-coordinate transport, not numerical differentiation of fitted entropy rates. It checks the following independently implemented finite quantities: actual atom normalization and its two jets; the full Shannon Hessian (2.7); the anchored formula (3.6); Schur posteriors and fixed-word derivatives; rank-one posterior flips and the squared-influence bound; actual conditional-pair cross-ratios; the full-projection Ward identity; the true Toeplitz Ward identity **with leakage**; and the exact gauge including all finite-matrix entries.

The executed checks passed 30 cyclic parameter cases, 12 true Toeplitz cases using every anchor, and a generic gapped complex Hermitian-kernel case. The gauge was also checked through \(n=64\). The displayed cyclic cases at \(c=0.95,d=0\) are:

| n | \(H_{n,dd}^{\rm cyc}/n\) | \(J_n\) | \(R_n/n\) |
|---:|---:|---:|---:|
| 2 | -35.083497602177 | 5.942143423464 | 31.083497602177 |
| 4 | -30.744756016978 | 10.280885008663 | 26.744756016978 |
| 6 | -27.633173905620 | 13.392467120021 | 23.633173905620 |
| 8 | -25.348369922363 | 15.677271103278 | 21.348369922363 |
| 10 | -23.622432385197 | 17.403208640444 | 19.622432385197 |

These floating-point calculations are sanity checks, not independent review, rigorous interval arithmetic, a sign proof, or an asymptotic fit. The thermodynamic proof is Sections 1–9.

**PROVED:** compact-interior two-parameter cyclic-to-true-sine curvature transfer; a reusable operator-to-response mechanism with all primitive assumptions verified; complete finite moving-law entropy identities; all-exterior posterior identification; all-anchor and spatial-tail control; the midpoint finite identities and the actual infinite pair-sum identity.

**DISPROVED only as shortcuts:** operator-norm convergence of the zero-extended cyclic projections, and leakage-free projection Ward identities for genuine finite Toeplitz compressions. Neither is a counterexample to the assigned actual cyclic model.

**INCOMPLETE / NOT CLAIMED:** the ultimate concavity sign, endpoint or \(c\to1\) renormalization, the remaining QWE budgets, any equivalence of true and corrected concavity without the signed \(\Psi_n\) correction, and a physical-volume convergence rate uniform near a closing spectral gap.

---

## 12. Sources, scope of imported inputs, and access record

Repository: `cat5779/rl01`.
Branch: `research/sa-cycle08-harvest-transfer-20260918`.
Raw root:

`https://raw.githubusercontent.com/cat5779/rl01/research/sa-cycle08-harvest-transfer-20260918/`

**[R1]** `research/CYCLE08_20260918/S51_C1/S51_C1_RENORMALIZATION/DEPENDENCY_S51_CYCLE06_RESULT.md`.
Imported only for the identification of the true entropy-rate derivative with the accepted named noise-flow \(\Gamma_c\), after the new response has independently been identified with that derivative.

**[R2]** `research/CYCLE08_20260918/reviews/S51_CYCLE06.md`.
The independent scoped review confirms the legal-interior half-density bridge; no endpoint or sign result is imported.

**[R3]** `research/INDEPENDENT_REVIEW_20260918/S43_CYCLE05.md`.
Used only in Section 10 for the scoped corrected-law ledger and signed-KL budget.

**[R4]** `research/CYCLE08_20260918/sources/S43_CYCLE05_RESULT.md`.
Used for the same ledger, actual direction \(D(\mu_l\Vert\gamma_{l,c})\), normalization, and fixed-\(c\) quantifiers.

**[R5, methodological comparison only]** Amir Dembo and Andrea Montanari, *Ising models on locally tree-like graphs*, arXiv:0804.4726, `https://arxiv.org/abs/0804.4726`. This is a non-DPP example of identifying thermodynamic quantities through local convergence. No theorem about Ising models, tree limits, or uniqueness is imported. The functional-analysis compactness and local-weak expectation transfer actually needed here are proved in Sections 4 and 5.

All four required raw sources were accessible and read through the web tool. Direct attempts to download the raw files into the local container failed (DNS/download errors); no unavailable source content was fabricated. No repository checkout, commit, or remote update was performed. The result, executable diagnostic script, and its outputs were created in the local working environment.

The optional pending S51 C1, S52, S54, and QWE02 author sources were not used as premises. The proof does not depend on receiving any QWE03–QWE06 submission.
