# S13 independent follow-up: a uniform linear upper bound for the corrected-law acceleration

**Status:** `CORRECTED_LAW_ONLY` — `PROVED_UPPER_SCALE / INCOMPLETE_SHARP_COEFFICIENT`  
**Benchmark:** \(c=19/20\), \(a_*=(1-c)/2=1/40\), \(n=2k\ge 4\) even.  
All logarithms are natural.

## 1. Result

Let the corrected law, count weights, total-rate-one Bernoulli--Laplace generator, coefficient multiplier, corrected clock, layer entropy, and entropy production be exactly those specified in the frozen SA04/S13 model:

\[
L_l f(S)=\frac1{l(n-l)}\sum_{i\in S,\,j\notin S}[f(S-i+j)-f(S)],
\]

\[
\widehat\tau_l(a)=-\frac{\log\theta_{n,l}(z(a,c))}{\gamma_{2,l}},
\qquad
\gamma_{2,l}=\frac{2(n-1)}{l(n-l)},
\]

\[
K_l(t)=D\!\left(u_l e^{tL_l}r_l^{\max}\middle\|u_l\right),
\qquad
\mathcal I_l^L(t)=-K_l'(t),
\]

and at the midpoint

\[
C_n=\sum_l\pi_l(a_*)[-\widehat\tau_l''(a_*)]\,
\mathcal I_l^L(\widehat\tau_l(a_*)).
\]

On \(l=0,1,n-1,n\), the prescribed corrected law is uniform and the contribution is defined to be zero.

### Theorem

For every even \(n\ge4\),

\[
0\le C_n\le K_* n,
\]

where

\[
\boxed{
K_*=\frac{1600\log 2}{\log(761/760)}
=843421.3677805425\ldots .
}
\]

Consequently \(C_n=o(n^{3/2})\). Combined with the supplied positive-liminf theorem

\[
\liminf_{n\to\infty,\ n\text{ even}}\frac{C_n}{n}>0,
\]

the corrected-law acceleration has the order

\[
C_n=\Theta(n)
\]

along even \(n\). The lower theorem is a supplied dependency, not re-audited here; the upper bound above is proved below from the frozen definitions.

The proof is all-layer: it uses the actual \(\pi_l(a_*)\), does not truncate to a central window, and requires no tail estimate.

---

## 2. Exact rate conversion and midpoint clock acceleration

Write

\[
G_l=l(n-l)L_l,
\qquad
P_l^s=e^{sG_l}.
\]

The original-rate heat time corresponding to the corrected total-rate-one time is

\[
s_l(a)=\frac{\widehat\tau_l(a)}{l(n-l)}
=-\frac{\log\theta_{n,l}(z(a,c))}{2(n-1)}.
\]

Let

\[
F_l(s)=D\!\left(u_lP_l^s r_l^{\max}\middle\|u_l\right),
\qquad
\mathcal I_l^G(s)=-F_l'(s).
\]

Then

\[
F_l(s)=K_l(l(n-l)s),
\qquad
\mathcal I_l^G(s)=l(n-l)\mathcal I_l^L(l(n-l)s).
\]

For

\[
z(a,c)=\frac{(a+c)(1-a)}{a(1-a-c)},
\]

put \(g=\log z\). At \(a_*=(1-c)/2\),

\[
g'(a_*)=0,
\qquad
z'(a_*)=0,
\]

and

\[
g''(a_*)=2\left[\frac1{((1-c)/2)^2}-\frac1{((1+c)/2)^2}\right],
\]

so

\[
\boxed{
z''(a_*)=\frac{32c}{(1-c)^4}.}
\]

At the benchmark,

\[
z_*=1521,
\qquad
z''(a_*)=4,864,000.
\]

Since \(z'(a_*)=0\), exact differentiation gives, for every interior layer,

\[
-\widehat\tau_l''(a_*)
=\frac{z''(a_*)}{\gamma_{2,l}}\,\partial_z\log\theta_{n,l}(z_*),
\]

and

\[
-s_l''(a_*)
=\frac{z''(a_*)}{2(n-1)}\,\partial_z\log\theta_{n,l}(z_*).
\]

Therefore the apparently singular layer factor cancels exactly:

\[
\boxed{
[-\widehat\tau_l'']\mathcal I_l^L
=[-s_l'']\mathcal I_l^G
=\frac{z''}{2(n-1)}\,
\partial_z\log\theta_{n,l}\,\mathcal I_l^G(s_l).
}
\]

This is the first essential mechanism. One must combine clock acceleration and entropy production before bounding either separately.

---

## 3. A reusable clock--dissipation quotient lemma

Let \(u\) be invariant for a finite-state Markov generator \(G\), let \(P_s=e^{sG}\), and let

\[
F(s)=\operatorname{Ent}_u(P_s f),
\qquad
I(s)=-F'(s).
\]

Assume \(I(s)\) is nonincreasing. Let

\[
s(a)=-\frac{\log\theta(z(a))}{\Lambda}
\]

with \(0<\theta<1\), \(z'(a_*)=0\), and \(\partial_z\theta\ge0\). Then

\[
[-s''(a_*)]I(s(a_*))
\le
z''(a_*)F(0)
\frac{\partial_z\log\theta(z_*)}{-\log\theta(z_*)}.
\]

Indeed,

\[
-s''(a_*)=\frac{z''(a_*)}{\Lambda}\partial_z\log\theta(z_*),
\]

while monotonicity gives

\[
sI(s)\le\int_0^s I(t)\,dt=F(0)-F(s)\le F(0).
\]

Substituting \(s=(-\log\theta)/\Lambda\) cancels \(\Lambda\).

For the present chain, \(\Lambda=2(n-1)\).

---

## 4. Verification that the original-rate entropy production is nonincreasing

On the \(l\)-slice,

\[
G_l=\sum_{1\le i<j\le n}(T_{ij}-I),
\]

where \(T_{ij}\) is the coordinate transposition. Terms for which both sites are occupied or both are empty vanish, so this is exactly the specified original-rate Bernoulli--Laplace generator.

For a positive density \(f\),

\[
\mathcal I_l^G(f)
=\frac12\sum_{i<j}\mathbb E_{u_l}
\Psi(f,T_{ij}f),
\qquad
\Psi(x,y)=(x-y)(\log x-\log y).
\]

The function \(\Psi\) is jointly convex. Its Hessian is

\[
\nabla^2\Psi(x,y)=
\begin{pmatrix}
(x+y)/x^2&-(1/x+1/y)\\
-(1/x+1/y)&(x+y)/y^2
\end{pmatrix},
\]

which is positive semidefinite: the diagonal entries are positive and the determinant is zero.

The generator \(G_l\) is invariant under relabeling, hence \(P_l^t\) commutes with every \(T_{ij}\). Jensen's inequality gives pointwise

\[
\Psi(P_l^t f,P_l^tT_{ij}f)
\le P_l^t\Psi(f,T_{ij}f).
\]

Integrating against the invariant law \(u_l\) yields

\[
\mathcal I_l^G(P_l^t f)\le\mathcal I_l^G(f).
\]

Applying this with \(f=P_l^s r_l^{\max}\) proves that \(s\mapsto\mathcal I_l^G(s)\) is nonincreasing.

If the initial density has zeros, apply the argument for positive times and pass to zero by finite-state continuity. Thus the lemma from Section 3 applies at the corrected time.

---

## 5. Uniform initial entropy budget

Let \(m=\min(l,n-l)\). First suppose \(l=m\le k\). The projection-DPP inclusion identity gives

\[
q_m^{\max}(S)=\frac{\det P_S}{\binom{k}{m}}.
\]

Here is a direct Cauchy--Binet verification.  Write \(P=UU^*\) with
\(U^*U=I_k\), and let \(X=\operatorname{diag}(x_1,\ldots,x_n)\).  Then

\[
\det(U^*XU)
=\sum_{|A|=k}|\det U_A|^2\prod_{i\in A}x_i
=\sum_{|A|=k}\det(P_A)\prod_{i\in A}x_i.
\]

Set \(x_i=1+t_i\).  The coefficient of \(\prod_{i\in S}t_i\) on the
right is \(\sum_{A\supset S}\det P_A\).  On the left,

\[
\det(I_k+U^*TU)=\det(I_n+TP),
\]

and the principal-minor expansion shows that the same coefficient is
\(\det P_S\).  Hence \(\Pr(S\subset A)=\det P_S\), which gives the
displayed formula after uniform subsampling from \(A\).

Since \(P_{ii}=1/2\), Hadamard's inequality gives

\[
\det P_S\le2^{-m}.
\]

Therefore the density relative to \(u_m\) obeys

\[
r_m^{\max}(S)
\le
\frac{\binom{2k}{m}}{2^m\binom{k}{m}}.
\]

For \(0\le m\le k\),

\[
\frac{\binom{2k}{m}}{\binom{k}{m}}
=\prod_{j=0}^{m-1}\frac{2k-j}{k-j}
\le4^m.
\]

To see the last inequality, the factors are increasing in \(j\), so the mean of their first \(m\) logarithms is at most the mean of all first \(k\) logarithms; their full product is \(\binom{2k}{k}\le4^k\).

Hence

\[
\|r_m^{\max}\|_\infty\le2^m
\]

and

\[
\boxed{F_m(0)\le m\log2.}
\]

For \(l>k\), complementation identifies the law with the same construction at minority size \(m=n-l\) for the complementary projection \(I-P\), whose diagonal is also \(1/2\). Thus the same bound holds on every layer.

For \(l=0,1,n-1,n\), the prescribed law is uniform: at \(l=1\), for example,

\[
q_1^{\max}(\{i\})=\frac{P_{ii}}k=\frac1n.
\]

Therefore \(F_l(0)=\mathcal I_l^G=0\) on the endpoint layers.

---

## 6. Two uniform coefficient-response bounds

For \(2\le m\le k\), define

\[
Z_m(z)=\sum_j\binom kj\binom k{m-j}z^j,
\]

\[
A_{m-2}(z)=\sum_j\binom{k-2}j\binom{k-2}{m-2-j}z^j,
\]

\[
\alpha_m=\frac{m(m-1)}{k(k-1)},
\qquad
\theta_m(z)=\frac{(z-1)^2A_{m-2}(z)}{\alpha_mZ_m(z)}.
\]

### 6.1 Logarithmic derivative

Let \(J_Z\) and \(J_A\) be the indices under the probability weights proportional to the summands of \(Z_m\) and \(A_{m-2}\), respectively. Then

\[
\partial_z\log\theta_m
=\frac2{z-1}+\frac{\mathbb EJ_A-\mathbb EJ_Z}{z}.
\]

The ratio of the \(j\)-th coefficient of \(A_{m-2}\) to the \(j\)-th coefficient of \(Z_m\) is

\[
w_j=
\frac{(k-j)(k-j-1)(m-j)(m-j-1)}{k^2(k-1)^2}.
\]

This is nonincreasing in \(j\). Hence the \(A\)-law is the \(Z\)-law tilted by a decreasing weight, and

\[
\mathbb EJ_A-\mathbb EJ_Z
=\frac{\operatorname{Cov}_Z(J,w_J)}{\mathbb E_Zw_J}\le0.
\]

Therefore

\[
\boxed{\partial_z\log\theta_m(z)\le\frac2{z-1}.}
\]

For completeness, positivity follows directly after putting \(y=z-1\). One has

\[
Z_m(1+y)=\sum_{r=0}^m c_ry^r,
\quad
c_r=\binom kr\binom{2k-r}{m-r},
\]

and

\[
y^2A_{m-2}(1+y)=\sum_{r=0}^mc_rq_ry^r,
\]

with

\[
q_r=
\frac{r(r-1)(2k-m)(2k-m-1)}
{k(k-1)(2k-r)(2k-r-1)}.
\]

The sequence \(q_r\) is increasing. If \(R\) has weights proportional to \(c_ry^r\), then

\[
\theta_m=\frac{\mathbb E q_R}{\alpha_m},
\qquad
y\partial_y\theta_m=\frac{\operatorname{Cov}(R,q_R)}{\alpha_m}\ge0.
\]

Thus

\[
0\le\partial_z\log\theta_m(z)\le\frac2{z-1}.
\]

### 6.2 Clock is uniformly separated from zero

Let

\[
f(t)=(1+t)(1+zt),
\qquad
a_j=[t^j]f(t)^{k-2},
\]

with \(a_j=0\) for negative indices. Differentiating \(f(t)^k\) twice and extracting the coefficient of \(t^{m-2}\) gives the exact identity

\[
\frac{(z-1)^2}{\theta_m}
=(z+1)^2+\frac{2z}{k-1}
+z(z+1)\left(4+\frac2{k-1}\right)\frac{a_{m-3}}{a_{m-2}}
+z^2\left(4+\frac2{k-1}\right)\frac{a_{m-4}}{a_{m-2}}.
\]

Every added term is nonnegative. Hence

\[
\theta_m(z)
\le\left(\frac{z-1}{z+1}\right)^2,
\]

and therefore

\[
\boxed{
-\log\theta_m(z)
\ge\beta(z):=2\log\frac{z+1}{z-1}>0.
}
\]

Combining the two coefficient bounds,

\[
\boxed{
0\le
\frac{\partial_z\log\theta_m(z)}{-\log\theta_m(z)}
\le
\frac{2}{(z-1)\beta(z)}.
}
\]

---

## 7. All-layer aggregation with the actual count probabilities

Apply the clock--dissipation quotient lemma, the initial entropy bound, and the coefficient-response estimate. For every interior layer,

\[
\begin{aligned}
[-\widehat\tau_l'']\mathcal I_l^L
&=[-s_l'']\mathcal I_l^G\\
&\le z''F_l(0)
\frac{\partial_z\log\theta_m}{-\log\theta_m}\\
&\le
\frac{2z''\log2}{(z-1)\beta(z)}\,m,
\qquad m=\min(l,n-l).
\end{aligned}
\]

The endpoint contributions are zero. Summing with the actual midpoint weights gives

\[
\begin{aligned}
C_n
&\le
\frac{2z''\log2}{(z-1)\beta(z)}
\sum_{l=0}^n\pi_l(a_*)\min(l,n-l)\\
&\le
\frac{2z''\log2}{(z-1)\beta(z)}\frac n2\\
&=
\frac{z''\log2}{(z-1)\beta(z)}n.
\end{aligned}
\]

No layer was discarded. In particular, count tails require no separate estimate.

At the benchmark,

\[
z=1521,
\quad z-1=1520,
\quad\beta=2\log(761/760),
\quad z''=4,864,000.
\]

Therefore

\[
\frac{z''\log2}{(z-1)\beta}
=
\frac{4,864,000\log2}{1520\cdot2\log(761/760)}
=
\frac{1600\log2}{\log(761/760)}
=K_*.
\]

This proves the theorem.

The same proof, incidentally, gives for every fixed \(0<c<1\) at its symmetric shift

\[
C_n(c)\le
\frac{4\log2}{(1-c)^2\log((1+c^2)/(2c))}\,n.
\]

Only the benchmark statement is needed here.

---

## 8. Exact conditional implication for a separate moving-count result

Suppose another proof, independent of this one, establishes that for some \(\gamma>0\) and all sufficiently large even \(n\),

\[
W_n\le-\gamma n^{3/2}.
\]

Then the present theorem implies

\[
\widehat K_n''(a_*)=W_n+C_n
\le-\gamma n^{3/2}+K_*n.
\]

Consequently, for

\[
n\ge\left(\frac{2K_*}{\gamma}\right)^2,
\]

one has

\[
\widehat K_n''(a_*)\le-\frac\gamma2n^{3/2}.
\]

This is only a midpoint statement for the prescribed corrected law. It does not prove the premise about \(W_n\), does not transfer to fixed-chord Jensen, and does not imply any statement about the true output entropy.

---

## 9. Bottleneck diagnosis

The upper scale is not blocked by count tails, endpoint singularities, or an uncontrolled correlation between clock curvature and entropy production:

1. The factor \(l(n-l)\) cancels exactly when the clock and entropy production are expressed in the same time normalization.
2. The remaining clock sensitivity is the dimension-free quotient
   \[
   R_{n,m}(z)=\frac{\partial_z\log\theta_m(z)}{-\log\theta_m(z)},
   \]
   and it is uniformly bounded.
3. The only extensive budget in the proof is the initial layer entropy \(F_l(0)\le m\log2\).
4. Actual count weighting costs no extra power of \(n\), because \(m\le n/2\) on every layer.

Thus the order bottleneck is settled. The bottleneck for a sharp limiting coefficient is the entropy-production factor itself: one would need controlled central-window asymptotics for

\[
\frac{\mathcal I_l^G(s_l)}{n^2}
\]

jointly with the smooth layer dependence of \(R_{n,m}(z_*)\). The estimate \(sI(s)\le F(0)\) is deliberately too coarse to identify that coefficient.

---

## 10. Dependency ledger

### Used from the frozen supplied model

- The exact corrected multiplier formula \(\theta_{n,l}\).
- The exact corrected clock and total-rate-one generator.
- The actual count weights \(\pi_l(a_*,c)\).
- The decomposition defining \(C_n\).
- The endpoint convention.
- For the final \(\Theta(n)\) corollary only: the supplied positive liminf for \(C_n/n\).

### Re-derived here

- \(z'(a_*)=0\) and the exact value of \(z''(a_*)\).
- The exact conversion between \(L_l\)-time and \(G_l\)-time.
- Cancellation of \(l(n-l)\) in \([ -\widehat\tau_l'']\mathcal I_l\).
- Monotonicity of original-rate entropy production.
- The valid bound \(s\mathcal I^G(s)\le F(0)\) at the correct clock.
- The all-layer initial entropy bound \(F_l(0)\le m\log2\).
- The coefficient inequalities
  \[
  0\le\partial_z\log\theta_m\le2/(z-1),
  \quad
  -\log\theta_m\ge2\log((z+1)/(z-1)).
  \]
- The actual-weight all-layer aggregation and explicit constant.

### Not used

- Any new conclusion about \(W_n\).
- Any unreviewed midpoint cusp claim from earlier S13 rounds.
- Any other researcher's new proof conclusions.
- Any identification of the corrected law with the true conditional output.
- Any cyclic-to-Toeplitz transfer.

---

## 11. Labels

- `PROVED`: For every even \(n\ge4\), \(0\le C_n\le K_*n\) with the explicit \(K_*\) above.
- `PROVED_FROM_SUPPLIED_LOWER_PLUS_NEW_UPPER`: \(C_n=\Theta(n)\) along even \(n\).
- `PROVED_CONDITIONAL`: If separately \(W_n\le-\gamma n^{3/2}\), then \(W_n+C_n\le-(\gamma/2)n^{3/2}\) for all sufficiently large even \(n\).
- `INCOMPLETE`: The sharp constant or a limit of \(C_n/n\) is not established.
- `INCOMPLETE`: No conclusion is made about the true sine output entropy, fixed-chord Jensen, or Toeplitz limit.
