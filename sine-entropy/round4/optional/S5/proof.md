PROVED_SCOPED_LEMMA

# S5: the actual common-offset path in discrete transport geometry

## Status, quantifiers, and contribution

All logarithms are natural, and `0 log 0=0`. This document does **not** prove or disprove the sine-process entropy-rate target. It proves an exact pathwise decomposition and a previously unpaid covariant-acceleration estimate. It also disproves two specified transport connections, one by a rational/logarithm certificate and one by an analytic argument with a finite algebraic seed.

The exact differential decomposition also applies directly to the nonprojection Toeplitz block, with its actual count law specified in Section 2.3. The complete acceleration theorem applies to **every** dimension, **every** rank-one or co-rank-one projection, **every** contrast `0<c<1`, and **every** interior `0<a<1-c`. The class, with the zero and identity projections included, is closed under the genuine projection-conditioning formulas in the prompt. The contribution is the acceleration payment, not another proof of the supplied rank-one full-entropy concavity bound.

The first counterexample has the genuine Fourier projection `P_(6,2)`, `c=1/2`, and `a=49/100`. It disproves universal nonnegativity of the **aggregate non-Bochner remainder**, including layer-weight derivatives. It does not disprove that inequality restricted to high contrast.

The second obstruction applies, for every fixed `0<c<1`, to the middle conditional slice of the **true Fourier projections** `P_(8m,4m)` for every positive odd integer `m`. Their actual conditional path is not a time change of the normalized Bernoulli–Laplace heat flow on any nonempty open interval of the legal parameter range, even when the clock may reverse. This is an increasing-dimensional, fixed-density `rho=1/2` obstruction to importing the single-mode heat-clock argument. It is not an obstruction to every possible transport metric or to full-entropy concavity.

Results below are labelled **complete proof**, **exact finite certificate**, or **floating diagnostic**. “Exact finite certificate” means an explicitly specified finite computation in rational or algebraic arithmetic, with rigorous logarithm enclosures where required. It does not mean independent external certification. Self-review and our own reruns are not independent review.

## 1. Source conventions and hypotheses

The external geometry used here is the logarithmic-mean transport geometry of Erbar–Maas and Erbar–Maas–Tetali. The latter's displayed Bernoulli–Laplace rates, Section 1.2, are

\[
 q_l(S,T)=\frac{1}{l(n-l)}\mathbf1_{\{|S\triangle T|=2\}},
 \qquad S,T\in\Omega_{n,l}.
 \tag{1.1}
\]

Thus the total exit rate is one. We use these **displayed rates**, rather than infer normalization from a verbal waiting-time description. The invariant probability is uniform. Theorem 1.1 gives

\[
 \kappa_l=\frac{n+2}{2l(n-l)}\qquad(1\le l<n).
 \tag{1.2}
\]

Theorem 2.2 and equation (2.3) identify the corresponding entropy Hessian with the Bochner form and give its lower bound by `kappa_l` times the metric action. Their hypotheses are a finite, irreducible, reversible chain and strictly positive densities. Each nontrivial slice in the interior of our channel path meets them. Singleton layers are treated separately. The source concerns relative entropy and its geodesic Hessian, not concavity along an arbitrary parameterized probability path. [EMT, Theorems 1.1, 2.2, equations (2.1)–(2.3).]

The geodesic potential equation used to identify the acceleration is Erbar–Maas, Proposition 3.4; their Proposition 4.3 identifies the entropy Hessian. Their Markov-kernel notation has generator `K-I`; with (1.1) this is the generator below. All remaining channel, acceleration-payment, and clock-obstruction calculations are derived in this document. [EM, Propositions 3.4 and 4.3.]

Source locations and verification notes are in `sources.md`. No private sources were accessed.

## 2. The actual homogeneous channel and its disintegration — complete proof

Fix a probability law `mu` on the `k`-subsets of `n` labelled sites, allowing zero input atoms and deterministic laws. Fix `0<c<1`. Conditional on the input set `A`, the output bits are independent, with success probabilities `a+c` on `A` and `a` off `A`. Throughout the differentiation argument,

\[
 0<a<1-c.
\]

Every output atom is strictly positive: each conditional product probability is positive, and at least one input atom has positive mass. Write the actual channel atoms as `p_a(S)`, and let `M=|S|`. Put

\[
 N_l=\binom nl,\quad u_l(S)=N_l^{-1},\quad
 \pi_l(a)=\Pr(M=l),\quad
 r_l(S,a)=\frac{N_lp_a(S)}{\pi_l(a)}.
 \tag{2.1}
\]

Conditional on any input set, the count is a sum of independent binomials. Its probability generating function is exactly

\[
 \sum_{l=0}^n\pi_l(a)z^l
 =[1-a-c+(a+c)z]^k[1-a+az]^{n-k}.
 \tag{2.2}
\]

This expression does not depend on `mu`. For uniform input on the `k`-subsets, permutation invariance makes the output uniform within each layer, hence its full atom is `pi_l/N_l`.

Let

\[
 F_l=\langle r_l\log r_l\rangle_{u_l},\quad
 D=\sum_l\pi_lF_l,\quad
 \Phi=-\sum_l\pi_l\log(\pi_l/N_l).
 \tag{2.3}
\]

Splitting `log p_a(S)=log(pi_l/N_l)+log r_l(S)` gives exactly

\[
 H=\Phi-D.
 \tag{2.4}
\]

This is the supplied baseline, now checked for the actual channel. We use the supplied concavity of `Phi`; none of our new conclusions is inferred merely from `D>=0`.

### 2.1 Exact conditional jets

All primes in this document denote derivatives in `a`, with `c`, `n`, `k`, and the input law held fixed. The actual conditional density derivatives are

\[
 r_l'=\frac{N_lp_a'}{\pi_l}-\frac{\pi_l'}{\pi_l}r_l,
\qquad
 r_l''=\frac{N_lp_a''}{\pi_l}
       -2\frac{\pi_l'}{\pi_l}r_l'
       -\frac{\pi_l''}{\pi_l}r_l.
 \tag{2.5}
\]

In particular, both derivatives have zero `u_l`-mean. We do not substitute an affine approximation to `p_a` or a semigroup derivative for either jet.

### 2.2 A useful exact conditional-kernel parameter

Set

\[
 w=a(1-c-a)>0,\qquad z=1+\frac c w.
 \tag{2.6}
\]

For `t=|A intersect S|` and `|S|=l`, the conditional product probability equals

\[
 a^l(1-a)^{n-k-l}(1-a-c)^k z^t.
\]

The equality is valid in the interior, including when the displayed exponent `n-k-l` is negative: it is simply an algebraic factorization of positive factors. Summing over `S` shows that the actual kernel conditional on the count is

\[
 T_z(A,S)=\frac{z^{|A\cap S|}}{Z_{n,k,l}(z)},\qquad
 Z_{n,k,l}(z)=\sum_t\binom kt\binom{n-k}{l-t}z^t.
 \tag{2.7}
\]

The sum is over feasible `t`. Thus

\[
 r_l(S)=N_l\sum_A\mu(A)T_z(A,S).
 \tag{2.8}
\]

All conditional densities depend on `a` only through `w`. In particular, for **every homogeneous input law**,

\[
 r_l'((1-c)/2)=0.
 \tag{2.9}
\]

At this midpoint every slice transport velocity and Bochner term below vanishes. Conditional acceleration and layer-weight terms can remain. Therefore a positive slice curvature constant alone cannot pay the midpoint curvature of the actual full law.

### 2.3 The true nonprojection Toeplitz block is also covered by the differential identity

The definitions (2.1), (2.3), the entropy identity (2.4), and the jets (2.5) make sense for any positive full probability path, without homogeneity. Recall explicitly that `DPP(K)` is specified by `Pr(A subset X)=det K_A`; its full atoms are

\[
 p_K(S)=\sum_{B\subseteq[n]\setminus S}(-1)^{|B|}\det K_{S\cup B},
 \qquad \det K_\varnothing=1,
\]

and its configuration entropy is `-sum_S p_K(S)log p_K(S)`. For a fixed Hermitian contraction `K_0`, including the true `Q_n`, the actual DPP channel count has generating function

\[
 \mathbb E z^M
 =\sum_{A\subseteq[n]}(z-1)^{|A|}\det(aI+cK_0)_A
 =\det[I+(z-1)(aI+cK_0)]
 =\prod_{j=1}^n[1-a-c\eta_j+(a+c\eta_j)z],
 \tag{2.10}
\]

where `eta_j` are the eigenvalues of `K_0`. The first equality expands the product of `1+(z-1)Y_i` and uses the defining inclusion probabilities; the second is determinant multilinearity. This is a proof about the **count only**, not an invariance of full configuration entropy under a change of spatial basis.

Thus for `Q_n` one can take these exact count probabilities and the actual full atoms just displayed in (2.5). Every formula in Section 3 holds unchanged. Its count entropy is concave by the general Shepp–Olkin theorem: Hillion–Johnson, Theorem 1.2, applies to any finite independent Bernoulli sum and is concave in the full parameter vector. Here those parameters are the legal affine functions `a+c eta_j`. This exact hypothesis was checked in the primary paper [HJ]. For completeness the other summand `E log binom(n,M)` is concave: its second derivative under the independent Bernoulli representation in (2.10) is `2 sum_(i<j) E Delta^2 log binom(n,M_(-i,-j))<=0`.

We do not apply the homogeneous kernel formula (2.7), its midpoint symmetry (2.9), or the homogeneous single-mode results to `Q_n` itself. Equation (2.10) makes explicit what replaces (2.2) in the true nonprojection setting. It supplies an exact identity, not the unpaid sign of the spatial correction.

## 3. The exact continuity equation and second derivative — complete proof

Fix one nontrivial layer and suppress `l`. For functions on this layer define

\[
 Lf(S)=\sum_Tq(S,T)[f(T)-f(S)],\qquad
 \nabla f(S,T)=f(T)-f(S).
\]

For antisymmetric edge fields, `div V(S)=sum_T q(S,T)V(S,T)`. The edge pairing is

\[
 \langle V,W\rangle_e
 =\frac12\sum_{S,T}u(S)q(S,T)V(S,T)W(S,T).
 \tag{3.1}
\]

It satisfies `L=div grad` and integration by parts. Let

\[
 \theta(x,y)=\int_0^1x^{1-t}y^t\,dt
 =\frac{y-x}{\log y-\log x},\qquad \theta(x,x)=x.
 \tag{3.2}
\]

Use `hat r(S,T)=theta(r(S),r(T))`. Our mobility operator and metric are

\[
 A_r=-\operatorname{div}(\hat r\nabla),\qquad
 g_r(v,v)=\langle\hat r\nabla\psi,\nabla\psi\rangle_e,
 \quad A_r\psi=v.
 \tag{3.3}
\]

Strict positivity of `r` and connectedness of the slice graph imply that `A_r` is invertible on the mean-zero subspace.

### 3.1 Velocity: solve for the actual path, not an unrelated flow

The actual velocity potential is the unique zero-mean solution

\[
 \boxed{\psi=A_r^{\dagger}r',\qquad
 r'+\operatorname{div}(\hat r\nabla\psi)=0.}
 \tag{3.4}
\]

Here `r'` is (2.5). The dagger denotes inversion only on the mean-zero subspace. No heat-flow or geodesic assumption has been made.

For a tangent vector `v`, define

\[
 A_r'[v]=-\operatorname{div}\bigl(
 [\theta_1(r(S),r(T))v(S)+\theta_2(r(S),r(T))v(T)]\nabla
 \bigr).
\]

Differentiating (3.4) with the zero-mean normalization gives

\[
 \psi'=A_r^{\dagger}\bigl(r''-A_r'[r']\psi\bigr).
 \tag{3.5}
\]

Also define

\[
 \Gamma_r(\psi)(S)
 =\sum_Tq(S,T)\theta_1(r(S),r(T))
                [\psi(T)-\psi(S)]^2.
 \tag{3.6}
\]

The covariant-acceleration vector, in density coordinates, is

\[
 C_r=r''-A_r'[r']\psi+\tfrac12A_r\Gamma_r(\psi)
    =A_r(\psi'+\Gamma_r(\psi)/2).
 \tag{3.7}
\]

Indeed, the geodesic potential equation is `psi'=-Gamma/2`, modulo spatial constants. Substituting this equation in the derivative of (3.4) gives precisely the zero-covariant-acceleration equation associated with (3.7). We are **measuring the failure of the actual path to satisfy it**, not imposing it on that path.

Set

\[
 \operatorname{acc}(r)=\langle\log r,C_r\rangle_u
 =-\langle Lr,\psi'+\Gamma_r(\psi)/2\rangle_u.
 \tag{3.8}
\]

The second equality uses the logarithmic-mean identity

\[
 A_r\log r=-Lr.
 \tag{3.9}
\]

### 3.2 Bochner form and the acceleration payment that is missing in curvature alone

Put

\[
 \widehat{Lr}(S,T)
 =\theta_1(r(S),r(T))Lr(S)+\theta_2(r(S),r(T))Lr(T)
\]

and

\[
 B(r,\psi)
 =\tfrac12\langle\widehat{Lr}\nabla\psi,\nabla\psi\rangle_e
  -\langle\hat r\nabla\psi,\nabla L\psi\rangle_e.
 \tag{3.10}
\]

The actual metric action is

\[
 \mathcal E(r,\psi)=\langle\hat r\nabla\psi,\nabla\psi\rangle_e.
\]

The verified EMT theorem gives `B>=kappa_l E` for this slice. It gives no automatic sign to (3.8).

For `F=<r log r>_u`, direct differentiation yields

\[
 F'=\langle\log r,r'\rangle_u=-\langle Lr,\psi\rangle_u.
\]

Consequently,

\[
 F''=-\langle Lr',\psi\rangle_u-\langle Lr,\psi'\rangle_u.
\]

Use `r'=A_r psi`, self-adjointness, integration by parts, and

\[
 \langle Lr,\Gamma_r(\psi)\rangle_u
 =\langle\widehat{Lr}\nabla\psi,\nabla\psi\rangle_e.
\]

This proves the exact identity

\[
 \boxed{F''=B(r,\psi)+\operatorname{acc}(r).}
 \tag{3.11}
\]

Independently, ordinary probability differentiation gives

\[
 \boxed{F''=I+\langle\log r,r''\rangle_u,\qquad
 I=\left\langle\frac{(r')^2}{r}\right\rangle_u.}
 \tag{3.12}
\]

Thus the Fisher term has not been removed; it is exactly part of the right side of (3.11). Both identities hold for every smooth positive density path, with the velocity obtained from (3.4).

### 3.3 The complete full-entropy identity, including moving weights

For the singleton layers `l=0,n`, put `F_l=B_l=acc_l=I_l=0`. Differentiating (2.4) twice gives

\[
 \boxed{
 H''=\Phi''-\sum_{l=0}^n
 \left[
 \pi_lB_l+\pi_l\operatorname{acc}_l
 +2\pi_l'F_l'+\pi_l''F_l
 \right].}
 \tag{3.13}
\]

Here

\[
 \boxed{
 \Phi''=-\sum_l\pi_l''\log(\pi_l/N_l)
         -\sum_l\frac{(\pi_l')^2}{\pi_l}.}
 \tag{3.14}
\]

The outer weight derivatives in (3.13) and the reference-count derivatives in (3.14) are essential. The slice generator does not change the count. We apply it only to the conditional density, and keep **all** count motion outside it. In particular the full mass balance is

\[
 p_a'(S)=\frac{\pi_l'}{N_l}r_l(S)
         +\frac{\pi_l}{N_l}A_{r_l}\psi_l(S),\qquad |S|=l.
 \tag{3.15}
\]

No claim that the full channel law follows a block-diagonal Bernoulli–Laplace semigroup is being made.

For an independent check, expand `p'=pi' r/N+pi r'/N` and use `mean(r')=0`. This gives the exact Fisher decomposition

\[
 \boxed{
 \sum_S\frac{(p_a'(S))^2}{p_a(S)}
 =\sum_l\frac{(\pi_l')^2}{\pi_l}+\sum_l\pi_l I_l.}
 \tag{3.16}
\]

Similarly,

\[
 p_a''(S)=\frac{\pi_l''r_l(S)+2\pi_l'r_l'(S)+\pi_lr_l''(S)}{N_l}.
 \tag{3.17}
\]

Combining (3.12), (3.14), (3.16), and (3.17) reproduces, term for term,

\[
 H''=-\sum_Sp_a''(S)\log p_a(S)
      -\sum_S\frac{(p_a'(S))^2}{p_a(S)}.
 \tag{3.18}
\]

This is the requested direct full-atom comparison at the algebraic level; finite checks appear in Section 6.

For later reference define

\[
 \mathcal B=\sum_l\pi_l B_l,\qquad
 \mathcal R_{\rm tr}=\sum_l
 \bigl[\pi_l\operatorname{acc}_l+2\pi_l'F_l'+\pi_l''F_l\bigr].
 \tag{3.19}
\]

Then `D''=Bcal+R_tr` and `H''=Phi''-Bcal-R_tr` exactly.

## 4. A single-mode acceleration-payment lemma — complete proof

**Lemma 4.1.** Let `L` be a fixed finite irreducible reversible generator. Let `f` have zero invariant mean and satisfy `Lf=-gamma f`, with `gamma>0`. Suppose the actual positive density path is

\[
 r(a)=1+\lambda(a)f,\qquad \lambda(a)>0,
 \tag{4.1}
\]

where `lambda` is twice continuously differentiable. Define

\[
 \beta=\frac{\lambda'}{\gamma\lambda},\quad
 J=\langle\log r,-Lr\rangle_u,\quad B_0=B(r,\log r).
\]

For the actual continuity potential (3.4), modulo constants,

\[
 \psi=\beta\log r,
 \qquad
 B(r,\psi)=\beta^2B_0,
 \tag{4.2}
\]

and the exact unpaid acceleration is

\[
 \boxed{
 \operatorname{acc}=B(r,\psi)+\beta'J,
 \qquad
 F''=2B(r,\psi)+\beta'J.}
 \tag{4.3}
\]

In particular, if `(log lambda)''>=0`, then `acc>=B>=0`. On a normalized Bernoulli–Laplace slice,

\[
 \operatorname{acc}\ge B\ge\kappa_l\mathcal E\ge0.
 \tag{4.4}
\]

**Proof.** Equation (3.9) and the eigenfunction identity give

\[
 A_r(\beta\log r)=-\beta Lr=\lambda'f=r'.
\]

Thus (4.2) identifies the **actual** velocity, rather than choosing a convenient one. At equal arguments the following identity is understood by continuity; at unequal arguments it follows by differentiating (3.2):

\[
 \theta_1(x,y)(\log y-\log x)^2
 =\frac{y-x}{x}-(\log y-\log x).
 \tag{4.5}
\]

Therefore

\[
 \Gamma_r(\log r)=\frac{Lr}{r}-L\log r.
 \tag{4.6}
\]

Differentiating the actual potential, modulo constants, gives

\[
 \psi'=\beta'\log r-\beta^2\frac{Lr}{r}.
\]

Substitution into (3.8) yields

\[
 \operatorname{acc}=\beta'J+
 \frac{\beta^2}{2}\left[
 \left\langle\frac{(Lr)^2}{r}\right\rangle_u
 +\langle Lr,L\log r\rangle_u\right].
 \tag{4.7}
\]

On the other hand, using (4.6) and `hat r grad log r=grad r` in (3.10) gives directly

\[
 B_0=\frac12\left[
 \left\langle\frac{(Lr)^2}{r}\right\rangle_u
 +\langle Lr,L\log r\rangle_u\right].
 \tag{4.8}
\]

This proves (4.3) by (3.11).

For the sign, `J` is the nonnegative Dirichlet pairing of the increasing logarithm with `r`. There is also an elementary proof that `B_0>=0` in this eigenmode setting, without assuming nonnegative Ricci curvature. Write `F(lambda)=< (1+lambda f)log(1+lambda f)>`. Then

\[
 F_\lambda=\langle f\log(1+\lambda f)\rangle_u\ge0,
 \qquad F_{\lambda\lambda}=\left\langle\frac{f^2}{1+\lambda f}\right\rangle_u\ge0,
\]

since `F_lambda(0)=0` and `F_lambdalambda>=0`. Self-adjointness and the eigenfunction relation turn (4.8) into

\[
 B_0=\frac{\gamma^2}{2}
       [\lambda^2F_{\lambda\lambda}+\lambda F_\lambda].
 \tag{4.9}
\]

Finally, `beta'=(log lambda)''/gamma`. On the Bernoulli–Laplace slice apply the verified curvature bound to the actual potential. This proves all assertions. QED.

A useful exact computational form of (4.9) is

\[
 B(r,\psi)=\frac{(\lambda')^2}{2}
 \left(F_{\lambda\lambda}+\frac{F_\lambda}{\lambda}\right).
 \tag{4.10}
\]

This lemma does identify a time change of heat flow, but only **after** proving (4.1) for the actual path: `r'=-beta Lr`, with heat clock `tau=-(log lambda)/gamma`. The clock reverses on the second half of the channel interval. Its acceleration contribution `beta'J` is explicitly paid in (4.3), not discarded.

## 5. A growing family closed under genuine projection minors — complete proof

### 5.1 Rank-one projections

Let `P=vv*`, where `sum_i |v_i|^2=1`, and put `omega_i=|v_i|^2`. These are the actual singleton input probabilities. For `1<=l<n`, define

\[
 f_l(S)=\frac nl\sum_{i\in S}\omega_i-1,
 \qquad d_l=\frac{cl}{n},\qquad
 \lambda_l=\frac{d_l}{w+d_l}.
 \tag{5.1}
\]

For `k=1`, the numerator in (2.8) is `1+(z-1) sum_{i in S}omega_i`. Its uniform average is `1+(z-1)l/n`. Consequently the **actual** conditional density is

\[
 r_l=1+\lambda_l f_l.
 \tag{5.2}
\]

Under (1.1), a coordinate function satisfies

\[
 L_l(\mathbf1_{i\in S}-l/n)
 =-\frac{n}{l(n-l)}(\mathbf1_{i\in S}-l/n).
\]

Indeed, the unnormalized exchange generator sends `1_{i in S}` to `l-n 1_{i in S}`. Thus `f_l` has eigenvalue

\[
 \gamma_l=\frac{n}{l(n-l)}.
 \tag{5.3}
\]

Since `w'=1-c-2a` and `w''=-2`,

\[
 \beta_l=-\frac{1-c-2a}{\gamma_l(w+d_l)},
\]

\[
 \boxed{
 \beta_l'=\frac1{\gamma_l}\left[
 \frac2{w+d_l}+\frac{(1-c-2a)^2}{(w+d_l)^2}
 \right]>0.}
 \tag{5.4}
\]

Lemma 4.1 now proves, for every rank-one projection and every nontrivial layer,

\[
 \boxed{
 \operatorname{acc}_l
 =B_l+\frac{J_l}{\gamma_l}\left[
 \frac2{w+cl/n}+\frac{(1-c-2a)^2}{(w+cl/n)^2}
 \right]
 \ge B_l\ge\frac{n+2}{2l(n-l)}\mathcal E_l.}
 \tag{5.5}
\]

No strictly positive input weights are required. If the input is uniform then `f_l=0`; if it is deterministic some input weights vanish. Both cases are already included, because the channel output is positive in the interior.

### 5.2 Co-rank-one, zero, and identity projections

For `P=I-vv*`, complement the input and the output. The transformed channel has `a_tilde=1-c-a`, the same `c`, and `w(a_tilde)=w(a)`. Complementation identifies the `l`-slice with the `n-l`-slice, preserves the normalized rates, and reverses velocity but not the quadratic Hessian or second derivative. Therefore (5.5) holds with `d_l` replaced by `c(n-l)/n` and the corresponding complemented `f_l`. The same positive formula (5.4) holds for the derivative of `beta` defined in the original parameter.

For the zero and identity projections the input is deterministic empty or full. The output is an iid Bernoulli law, conditional densities are identically one, and all slice geometric terms vanish. Dimension one has only singleton layers and is included in this trivial convention.

### 5.3 Genuine conditioning, not freely chosen child laws

The family

\[
 \mathfrak F=\{0,I,\text{all rank-one projections},
                         \text{all co-rank-one projections}\}
\]

across all dimensions is closed under every feasible coordinate conditioning.

For rank one, split coordinate `i` with `q=omega_i` in `(0,1)`. Direct substitution into the prompt's projection-minor formulas gives

\[
 P^{(1)}=0,\qquad
 P^{(0)}=\frac{v_{-i}v_{-i}^*}{1-q}.
 \tag{5.6}
\]

The latter is a rank-one projection because `||v_-i||^2=1-q`. The occupation-branch probability is exactly `q`, and the unoccupied branch has probability `1-q`. These are the genuine minors of the same parent projection. When `q=0` or `q=1`, retain only the feasible branch; the same conclusion follows directly. Complementation proves the co-rank-one statement, and zero/identity projections remain zero/identity on the remaining coordinates. Iterating proves closure for any finite conditioning sequence.

This establishes an unpaid geometric correction for a genuinely minor-compatible growing family. It neither proves the false coordinate-completion inequality `(C)` from the prompt nor relies on it. The supplied full-entropy bounds already cover this family; (5.5) isolates new information about the geometry of its actual channel path.

### 5.4 An additional single-mode family needed for the finite certificate

Let `mu` be any homogeneous law on pairs with all one-site marginals `2/n`. For `2<=l<=n-2`, put

\[
 T(S)=\Pr_\mu(A\subseteq S),\qquad
 \alpha_l=\frac{l(l-1)}{n(n-1)},\qquad f_l=T/\alpha_l-1.
\]

Expanding `z^t`, where `t` is 0, 1, or 2, gives

\[
 \mathbb E_\mu z^{|A\cap S|}
 =1+\frac{2l}{n}(z-1)+(z-1)^2T(S).
\]

Hence the actual conditional density is again `1+lambda_l f_l`, now with

\[
 \lambda_l=\frac{c^2\alpha_l}
 {w^2+(2cl/n)w+c^2\alpha_l}.
 \tag{5.7}
\]

The unnormalized exchange generator on `x_i x_j` is

\[
 L_0(x_i x_j)=-2(n-1)x_i x_j+(l-1)(x_i+x_j).
\]

Summing with pair probabilities and using the uniform marginals gives

\[
 L_0T=-2(n-1)(T-\alpha_l),\qquad
 \gamma_l=\frac{2(n-1)}{l(n-l)}.
 \tag{5.8}
\]

Factor the denominator in (5.7) as `(w+u_l)(w+v_l)`, where

\[
 u_l,v_l=\frac cn
 \left[l\mathbin\pm\sqrt{\frac{l(n-l)}{n-1}}\right]>0.
\]

Then

\[
 (\log\lambda_l)''
 =\sum_{d\in\{u_l,v_l\}}
 \left[\frac2{w+d}+\frac{(w')^2}{(w+d)^2}\right]>0.
 \tag{5.9}
\]

Lemma 4.1 applies. The `l=1,n-1` conditional densities are uniform; the endpoint layers are singletons. This includes genuine rank-two Fourier projections for every `n>=4`.

**Scope restriction:** uniform one-site marginals of a rank-two projection are not generally preserved by projection conditioning. We do **not** claim that this ancillary family is minor-closed. The minor-compatible theorem is Sections 5.1–5.3. We also do not require all conditional entropies to be concave outside these explicitly proved single-mode classes.

## 6. A certified negative aggregate remainder

### 6.1 The proposed connection and its exact counterexample

A natural attempted completion of the positive-Bochner argument is

\[
 \mathcal R_{\rm tr}\ge0
 \quad\text{for every projection input and every legal interior point.}
 \tag{6.1}
\]

Together with `Phi''<=0` and `Bcal>=0`, this would prove finite full-entropy concavity. It is a genuine additional correction estimate, not a consequence of positive curvature. It is **false**, even when each conditional-slice acceleration is favorable.

Take `n=6`, `k=2`, and the genuine Fourier columns

\[
 U_{j,m}=6^{-1/2}e^{2\pi i jm/6},
 \qquad 0\le j<6,\quad m=0,1.
\]

The projection input pair probabilities, by shorter cyclic distance `d`, are

\[
 \mu(\{i,j\})=\begin{cases}
 1/36,&d=1,\\
 1/12,&d=2,\\
 1/9,&d=3.
 \end{cases}
 \tag{6.2}
\]

This follows from the two-column Vandermonde determinant; it is not an arbitrary homogeneous input. Set

\[
 c=1/2,\qquad a=49/100.
 \tag{6.3}
\]

The standard-library exact script `scripts/certify_fourier6.py` proves, with rational arithmetic and rigorously enclosed logarithms,

\[
 \boxed{-184/1000<\mathcal R_{\rm tr}<-183/1000,\qquad H''<-37.}
 \tag{6.4}
\]

It also proves that every nonconstant conditional layer, `l=2,3,4`, has strictly positive `F_l''` and strictly positive `acc_l`; analytically these follow from Section 5.4 as well. Thus this counterexample does not reuse the supplied failure of universal conditional-entropy concavity.

For transparent magnitude comparison, the following are rigorous, outward-rounded decimal enclosures, not merely floating estimates:

| Quantity | Strict enclosing interval |
|---|---|
| `H''` | `(-37.358807783041, -37.358807783040)` |
| `Phi''` | `(-35.709767293693, -35.709767293692)` |
| `D''` | `(1.649040489347, 1.649040489348)` |
| `Bcal` | `(1.832347024488, 1.832347024489)` |
| `sum_l pi_l acc_l` | `(3.805244954476, 3.805244954477)` |
| `sum_l (2 pi_l' F_l'+pi_l''F_l)` | `(-3.988551489618, -3.988551489617)` |
| `R_tr` | `(-0.183306535141, -0.183306535140)` |

The last two terms demonstrate the mechanism: favorable within-slice acceleration is outweighed by the changing layer weights. The complete full entropy remains strictly concave at this point.

This example lies in the **supplied solved contrast range**. It disproves (6.1) with its displayed universal quantifiers. It does **not** disprove a version restricted to `37/40<c<1`, and it is not a sine-target counterexample.

### 6.2 What makes the certificate exact

The code builds every full atom and its first two derivatives by multiplying the actual four channel factors as rational second-order jets. It constructs the count weights independently by convolution of Bernoulli jets and checks equality with the sum of full atoms in every layer. It checks (3.17) coefficientwise and (3.16) as an exact rational identity. In its single-mode cases it checks (5.2)/(5.7), the first two density jets, and the normalized generator eigenfunction equations at every state.

For a positive rational `x`, scale by a power of two to `x=2^m y`, `1<=y<2`. With `z=(y-1)/(y+1)`, use

\[
 \log y=2\sum_{j=0}^{N-1}\frac{z^{2j+1}}{2j+1}+R_N,
 \qquad
 0\le R_N\le\frac{2z^{2N+1}}{(2N+1)(1-z^2)}.
 \tag{6.5}
\]

The same formula encloses `log 2`. The script takes `N=80`; every bound and interval operation uses `fractions.Fraction`. No floating-point assertion is used. Its coarse sign assertions are (6.4), not a test that a decimal happens to be negative.

Bochner terms are evaluated using the **proved** identity (4.10), not by subtracting the desired answer from (3.11). The coefficient identity underlying (4.3) is checked rationally. Interval overlap with zero in a comparison is not claimed to prove equality: equality is proved in Section 3, and the exact rational coefficient identities supply the finite algebraic cross-check.

Frozen evidence is `evidence/fourier6_certificate.json`, containing all input probabilities, full atom jets, count jets, layer terms, and 40-place outward enclosures. It also exports `R_tr` as an exact rational constant plus a finite sum of rational coefficients times logarithms of positive rationals; this expression can be checked with a separately implemented logarithm enclosure.

### 6.3 Direct full-atom comparison before general conclusions

The exact certificate also checks the complete formulas for a nonuniform two-site rank-one projection, a deterministic three-site rank-one projection, a three-site zero projection, and the genuine four-site Fourier rank-two projection. Their parameters are listed in the certificate and README.

Separately, `scripts/diagnostic_smoke.py` constructs the full edge mobility matrices, solves (3.4) and (3.5), and evaluates (3.8) and (3.10) directly. It does not use the single-mode simplification. Its selected cases include an eight-site Fourier rank-four projection at `c=19/20`, the midpoint of that path, a random complex rank-three projection, and a genuine four-site Toeplitz block at `rho=1/2` (not a projection). The Toeplitz case also compares the actual count jets to (2.10). In the frozen run the largest absolute residuals were below `2.1e-12` for the slice identity and below `9.1e-13` for the full transport identity. This is a **floating diagnostic only**, not proof of a sign or independent certification.

## 7. A high-contrast obstruction to a common Bernoulli–Laplace clock

The single-mode lemma suggests a second possible connection: perhaps every actual conditional slice path is a scalar time change of the fixed Bernoulli–Laplace heat flow. This section disproves that connection on genuine Fourier inputs, including a growing true-Fourier subsequence at fixed density. A reversing scalar clock is allowed, so the obstruction is not the elementary reversal at the midpoint.

### 7.1 Harmonics and exact channel multipliers — complete proof

Let `n=2k`, `k>=4`, and consider the output layer `l=k`. Choose `d` disjoint coordinate pairs, with `d<=k`, and set

\[
 h_d(S)=\prod_{r=1}^d
 (\mathbf1_{i_r\in S}-\mathbf1_{j_r\in S}).
 \tag{7.1}
\]

Then for the normalized slice generator,

\[
 Lh_d=-\gamma_d h_d,
 \qquad \gamma_d=\frac{d(2k-d+1)}{k^2}.
 \tag{7.2}
\]

To verify this without an unquoted spectral theorem, first suppose `h_d(S)!=0`, so each pair has one occupied site. Exchanging the two sites of a pair contributes `-2h_d(S)` for each of `d` moves. Exchanges between two selected pairs contribute `-h_d(S)` for `d(d-1)` moves. Exchanges between selected pairs and unpaired sites contribute `-h_d(S)` for `d(n-2d)` moves. Other moves contribute zero. The total is `-d(n-d+1)h_d(S)` before division by `k^2`. If `h_d(S)=0`, swapping a pair with equal occupancy fixes `S`, reverses `h_d`, and preserves the neighbor sum; hence `Lh_d(S)=0`. This proves (7.2).

The symmetric conditional kernel in (2.7) satisfies

\[
 \sum_A z^{|A\cap S|}h_d(A)
 =(z-1)^d\left[\sum_{t=0}^{k-d}\binom{k-d}{t}^2z^t\right]h_d(S).
 \tag{7.3}
\]

For nonzero `h_d(S)`, summing the two choices in each selected pair supplies a factor `z-1`, with the sign `h_d(S)`. The remaining sites have `k-d` occupied and `k-d` empty positions, giving the displayed sum. For zero `h_d(S)`, the same pair-swap cancellation proves both sides zero.

Put

\[
 s=w/c>0,\qquad
 F_m(s)=\sum_{t=0}^m\binom mt^2s^{m-t}(1+s)^t
       =\sum_{j=0}^m\binom mj\binom{m+j}{j}s^j.
 \tag{7.4}
\]

The polynomial symbols `F_m(s)` in this section are distinct from the earlier conditional entropies `F_l(a)`. The second expression follows by taking the coefficient of `s^j` and applying the elementary Vandermonde sum
`sum_r binom(j,r)binom(m,r)=binom(m+j,j)`.

After normalizing (7.3), the actual channel multiplier of `h_d` is

\[
 \lambda_d(s)=F_{k-d}(s)/F_k(s).
 \tag{7.5}
\]

In particular, if the input moment `m_d=E_mu h_d` is nonzero, the output conditional moment is exactly `m_d lambda_d(s)`.

### 7.2 No scalar clock with two nonzero modes — complete proof

Suppose both `m_2` and `m_4` are nonzero. If on some open interval the actual conditional density satisfied

\[
 r'(a)=\tau'(a)Lr(a)
 \tag{7.6}
\]

for a continuously differentiable scalar clock `tau`, then testing against `h_2` and `h_4` would imply

\[
 \gamma_2(\log\lambda_4)'_a
 -\gamma_4(\log\lambda_2)'_a=0.
 \tag{7.7}
\]

Let

\[
 \Delta(s)=\gamma_2(\log\lambda_4)'_s
          -\gamma_4(\log\lambda_2)'_s.
\]

All `F_m` have positive coefficients and constant term one. Write `J_m=m(m+1)`. From (7.4),

\[
 (\log F_m)'(0)=J_m,
 \qquad (\log F_m)''(0)=-J_m(J_m+2)/2.
 \tag{7.8}
\]

Since `J_k-J_(k-d)=k^2 gamma_d`, these expressions give

\[
 \Delta(0)=0,\qquad
 \boxed{\Delta'(0)=\frac{k^4}{2}\gamma_2\gamma_4(\gamma_2-\gamma_4)<0.}
 \tag{7.9}
\]

For `k>=4`, `gamma_4>gamma_2`. Therefore `Delta` is an analytic function which is not identically zero; it cannot vanish on an open interval. Every nonempty open interval in `a` contains a subinterval off the midpoint, on which `s'(a)!=0` and the image is an open interval of `s`. Equation (7.7) would force `Delta=0` there, a contradiction. This proves that **no clock (7.6) exists on any nonempty open legal interval**, for any fixed `0<c<1`. QED.

This statement only rules out a time change of this fixed generator. It does not prohibit the actual continuity velocity (3.4), another generator, or a full transport argument retaining nonzero acceleration.

### 7.3 Exact genuine Fourier seed and a fixed high-contrast point

Take `P_(8,4)` with the actual first four Fourier columns. Its projection input probabilities are

\[
 \mu(A)=8^{-4}\prod_{i<j\in A}
   [2-2\cos(\pi(j-i)/4)],\qquad |A|=4.
 \tag{7.10}
\]

All factors are positive, so it has full support. These probabilities lie in `Q(sqrt(2))`. Use

\[
 h_2=(X_0-X_1)(X_2-X_3),
\]

\[
 h_4=(X_0-X_2)(X_1-X_3)(X_4-X_6)(X_5-X_7).
 \tag{7.11}
\]

The exact finite certificate enumerates all 70 input states and gives

\[
 \mathbb E h_2=1/8,\qquad \mathbb E h_4=3/64.
 \tag{7.12}
\]

For a compact hand-checkable aggregation of the same finite sums, the total input masses on `h_2=+1,-1` are respectively

\[
 35/128+3\sqrt2/64,\qquad 19/128+3\sqrt2/64;
\]

the total masses on `h_4=+1,-1` are `7/64` and `1/16`. Their differences give (7.12). Formula (7.10) and these finite sums are independently reproducible in `scripts/certify_clock.py` using exact pairs of rational numbers.

Here `gamma_2=7/8`, `gamma_4=5/4`, and

\[
 F_4=1+20s+90s^2+140s^3+70s^4,\qquad F_2=1+6s+6s^2.
\]

An exact polynomial identity gives the stronger pointwise expression

\[
 \Delta(s)
 =\frac{3F_4'F_2-10F_2'F_4}{8F_4F_2}
 =\boxed{\frac{-420s(1+s)(1+2s)^3}{8F_4(s)F_2(s)}<0}
 \quad(s>0).
 \tag{7.13}
\]

At the fixed high-contrast point

\[
 c=19/20,\qquad a=1/100,
\]

we have `w=1/2500`, `s=1/2375`, `s'=3/95`. The exact `a`-clock mismatch is

\[
 \boxed{
 \gamma_2(\log\lambda_4)'_a
 -\gamma_4(\log\lambda_2)'_a
 =-\frac{25129540296006300}{36287470978618801709}<0.}
 \tag{7.14}
\]

This certificate uses rational and `Q(sqrt(2))` arithmetic only, without logarithm approximation: logarithmic derivatives are rational functions. It rules out even instantaneous proportionality of the actual velocity to `Lr` at this legal high-contrast point.

### 7.4 Growth along true Fourier projections at fixed density — complete proof

Let `m` be any positive odd integer, let `n=8m`, `k=4m`, and take the **true first-`k`-column Fourier projection** `P_(n,k)`, not a direct sum. Select the eight labelled sites

\[
 J=\{0,m,2m,\ldots,7m\}.
\]

Write `m=2r+1`. In the sum over the `4m=8r+4` Fourier columns, each full run of eight contributes zero to the off-diagonal entries of the selected principal submatrix. Four columns remain. The diagonal is `1/2`. Therefore, with selected labels identified with `0,...,7`, the exact principal submatrix is

\[
 (P_{8m,4m})_J
 =\tfrac12 I_8+\frac1m(P_{8,4}-\tfrac12 I_8).
 \tag{7.15}
\]

This is a principal **marginal** identity, not a claim that the principal submatrix is a projection or a replacement for the genuine conditioning formulas.

For any DPP with kernel `K` and a constant `q`, expansion of principal minors gives

\[
 \mathbb E\prod_{i\in B}(X_i-q)=\det(K_B-qI_B).
 \tag{7.16}
\]

Every product in the expansion of `h_d` in (7.11) uses `d` distinct selected sites, and the differences can be written using `X_i-1/2`. Equations (7.15) and (7.16) imply that its expectation scales by `m^{-d}` relative to the eight-site seed. Thus, with all labels in (7.11) multiplied by `m`,

\[
 \mathbb E_{P_{8m,4m}}h_2=\frac1{8m^2},\qquad
 \mathbb E_{P_{8m,4m}}h_4=\frac3{64m^4}.
 \tag{7.17}
\]

They are nonzero for every positive odd `m`. Section 7.2, with its middle-slice parameter `k=4m`, now proves the claimed no-common-clock theorem for this increasing-dimensional true-Fourier family at the fixed density `rho=1/2`, for every fixed contrast `0<c<1`.

The same abstract theorem also applies to direct sums of copies of `P_(8,4)`: moments supported in one block remain nonzero. That optional extension is not needed for (7.17) and is not confused with the true Fourier family. Neither family is asserted to have all conditioned children carrying the same two nonzero harmonic moments. The separate acceleration theorem's minor closure was proved in Section 5.3.

## 8. Deterministic inputs, vanishing layers, and closed endpoints

All interior formulas hold for deterministic or sparse homogeneous input laws because output atoms are strictly positive. There is no need to replace a projection law by a non-projection regularization.

As `a` approaches either legal endpoint, `w` tends to zero and `z` tends to infinity. In (2.7) the leading power is `min(k,l)` and its coefficient is positive. The conditional kernel therefore has a unique finite limit:

\[
 T_\infty(A,S)=
 \begin{cases}
 \mathbf1_{S\subseteq A}/\binom kl,&l\le k,\\
 \mathbf1_{A\subseteq S}/\binom{n-k}{l-k},&l\ge k.
 \end{cases}
 \tag{8.1}
\]

The two formulas agree when `l=k`. This proves continuity of every conditional density along the interior path to the endpoint, even when that layer has zero limiting count mass. The limiting conditional law on a zero-mass layer is an interior-path convention, not an independently observable conditional distribution at the endpoint.

For each layer, `0<=F_l<=log N_l`; its limiting value exists by continuity of `x log x` at zero. Hence `pi_l F_l` tends to zero whenever `pi_l` tends to zero. This proves the continuous endpoint extension of (2.4). Full entropy is also continuous directly because every full atom is a polynomial and `-x log x` is continuous on `[0,1]`.

In the scoped single-mode families, `F_l''>=0` in the interior; restricting to compact interior intervals and then taking endpoints to the boundary proves convexity of `F_l` on the closed interval. This is the appropriate integrated endpoint consequence. **We do not assert that the separate Fisher, acceleration, or Hessian terms in (3.13) have finite endpoint limits.** Logarithms and inverse probabilities may diverge. Any future full-entropy Jensen proof must first be established in the interior and extended at the value level, rather than evaluate an undefined conditional Hessian on a zero-mass layer.

## 9. What remains unpaid for the sine target

For clarity, the original frozen target is the following. For fixed `0<rho<1` and `0<c<1`, let

\[
 H_n(a,c)=H(\mathrm{DPP}(aI_n+cQ_n)),\qquad
 h_\rho(a,c)=\lim_{n\to\infty}H_n(a,c)/n.
\]

It asks, for all `a_0,a_1 in [0,1-c]` and `t in [0,1]`, whether

\[
 h_\rho((1-t)a_0+ta_1,c)
 \ge (1-t)h_\rho(a_0,c)+t h_\rho(a_1,c).
\]

The original target concerns the configuration entropy of

\[
 K_n(a)=aI_n+cQ_n,
\]

where `Q_n` is the true Toeplitz principal block with diagonal `rho` and off-diagonal entries `sin(pi rho(i-j))/(pi(i-j))`. It asks concavity in `a` of the stationary limiting entropy rate at every fixed `rho`, including fixed `37/40<c<1` as `n` grows. We do not replace that entropy by a count entropy or a spectral entropy.

The rank-one/co-rank-one payment does not reach rank proportional to dimension. The uniform-marginal rank-two payment does not remedy this or give a minor-closed rank-two induction. The no-clock theorem already applies to true Fourier projections at density `1/2`, but disproving a convenient flow representation does not give the opposite sign of `H''`. Its selected harmonic moments scale to zero as `m^-2` and `m^-4`; no uniform lower bound on the entropy impact of the mismatch is proved. An asymptotically accurate flow approximation with a paid error is not ruled out.

For general high-rank projections, the sign or an adequate lower bound for `R_tr` is still unproved. Rewriting the desired finite curvature as

\[
 \mathcal R_{\rm tr}\ge\Phi''-\mathcal B
\]

would be merely the original inequality in new notation. We expressly do not count that as progress. Universal `R_tr>=0` was independently tested and disproved; the high-contrast-only version remains neither proved nor disproved here. Positive acceleration at each slice, even where available, is not sufficient without paying the weight terms, as Section 6 demonstrates.

A new theorem with uniform finite-dimensional Jensen control or sublinear total Jensen loss for the actual growing Fourier family would interact with the supplied cyclic-to-Toeplitz and value-tail bounds. No such control is proved in this package. We do not differentiate the limiting entropy rate or infer a Hessian estimate from the supplied value errors. The sine target therefore remains unresolved by this route.

## References

[EMT] Matthias Erbar, Jan Maas, and Prasad Tetali, *Discrete Ricci curvature bounds for Bernoulli–Laplace and random transposition models*, arXiv:1409.8605. https://arxiv.org/abs/1409.8605 ; original paper PDF https://arxiv.org/pdf/1409.8605 . Relevant locations: Section 1.2 and Theorem 1.1, printed page 3; equations (2.1)–(2.3), printed pages 5–6; Theorem 2.2, printed page 7.

[EM] Matthias Erbar and Jan Maas, *Ricci curvature of finite Markov chains via convexity of the entropy*, arXiv:1111.2687. https://arxiv.org/abs/1111.2687 ; author-hosted paper https://www.janmaas.org/papers/Ricci.pdf . Relevant locations: Proposition 3.4, printed page 19; Proposition 4.3, printed pages 20–21.

[HJ] Erwan Hillion and Oliver Johnson, *A proof of the Shepp–Olkin entropy concavity conjecture*, arXiv:1503.01570, Theorem 1.2. https://arxiv.org/abs/1503.01570 ; primary full text https://arxiv.org/html/1503.01570v1 . This theorem is used only for count entropy, never for the full dependent configuration law.
