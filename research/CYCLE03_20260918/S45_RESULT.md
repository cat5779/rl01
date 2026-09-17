# S45 harvested research result

Status: AUTHOR_SUBMISSION_PENDING_INDEPENDENT_REVIEW. Complete visible message recovered; accompanying file bodies were not recovered. The theorem is specific to the frozen corrected law. It is not a sign theorem or a true-output entropy-rate result.

Source: task 6aabf703-2334-83e8-8d2f-b9c47caf07d0, completed response 6192c9d5-6e12-4136-a53b-de0ad6e89394. Citation tokens are preserved provenance, not independently verified references.

---

## S45 — CORRECTED_LAW_ONLY

**Status: PROVED, scoped.** I get the requested improvement
\[
\boxed{|F_k-F_{k-r}|\le C\left(1+\frac{r^2}{n}\right)}
\]
on a fixed macroscopic central band, and—using the **actual** \(B_m\) coefficients and \(w_l=B_{l-1}-B_{l-2}\)—the complete aggregation
\[
\boxed{|W_n|\le Cn.}
\]

This does **not** determine the sign of \(W_n\), does not prove \(W_n+C_n<0\), and does not prove the ultimate sine-Toeplitz DPP entropy-rate concavity theorem.

The key advance over S43 is that its \(\log n\) loss is not intrinsic. S43's loss enters when it replaces the heat-overlap entropy by the trivial \(H(p_l)\ge0\), producing \(D(p_l\|q_l)\le\log n+O(1)\). citeturn2view2 The exact heat overlap law has entropy \(\frac12\log n+O(1)\), and the Gibbs cross-entropy has the same \(\frac12\log n\) term, so those logarithms cancel.

### 1. The new entropy bridge

Conditional on a fixed latent \(A\), the heat process is precisely finite symmetric exclusion starting from a deterministic \(l\)-set. The classical Borcea–Brändén–Liggett preservation theorem says finite symmetric exclusion preserves the strongly-Rayleigh property. citeturn9search12

Specialize its stable multiaffine generating polynomial by putting \(z_i=x\) for \(i\in A^c\) and \(z_i=1\) for \(i\in A\). The resulting univariate pgf of
\[
R=|S\cap A^c|
\]
has only real nonpositive zeros. Hence
\[
\mathbb E x^R=\prod_\alpha(1-\xi_\alpha+\xi_\alpha x).
\]
So the **actual heat overlap count at the prescribed coefficient clock is Poisson-binomial**.

For any Poisson-binomial \(X\), with \(\sigma^2=\operatorname{Var}X\),
\[
|\phi_X(t)|
 \le e^{-2\sigma^2\sin^2(t/2)}.
\]
Fourier inversion therefore gives
\[
\max_jP(X=j)\le \frac C{\sqrt{1+\sigma^2}},
\]
and consequently
\[
H(X)\ge H_\infty(X)
\ge\frac12\log(1+\sigma^2)-C. \tag{1}
\]

This is the reusable entropy-comparison object.

### 2. Exact variance at the actual clock

For the heat overlap birth-death coordinate \(R\), the rates are
\[
\lambda_R=(l-R)(k-R),\qquad
\mu_R=R(k-l+R).
\]
Writing \(m(s)=E R\) and \(V(s)=\operatorname{Var}R\),
\[
m' =lk-nm,\qquad
m(s)=\frac l2(1-e^{-ns}).
\]
Since
\[
\lambda_R+\mu_R=lk-2lR+2R^2,
\]
we get
\[
V'=-2(n-1)V+lk-2lm+2m^2.
\]
Solving exactly from \(V(0)=0\),
\[
\boxed{
V(s)=
\frac{l(n-l)}{4(n-1)}
 (1-e^{-2(n-1)s})
+\frac{l^2}{4}e^{-2(n-1)s}(1-e^{-2s}).
} \tag{2}
\]

No half-step clock has been substituted.

At
\[
s=s_l=-\frac{\log\theta_l}{2(n-1)},
\]
S43's checked coefficient-clock relation is
\[
e^{-ns_l}=\theta_l^{\,n/[2(n-1)]}, \tag{3}
\]
and on \(k-\eta k\le l\le k\), \(\theta_l\) remains in a compact subset of \((0,1)\). citeturn0view1 Thus (2) gives
\[
c_0n\le V(s_l)\le C_0n. \tag{4}
\]
Applying (1),
\[
\boxed{H(p_l)\ge\tfrac12\log n-C.} \tag{5}
\]

### 3. The Gibbs cross-entropy supplies the other half-log

For \(R=l-|A\cap S|\), the Gibbs law is
\[
q_l(r)\propto
 {k\choose r}{k\choose l-r}z^{l-r},
\]
so
\[
\frac{q_l(r+1)}{q_l(r)}
=z^{-1}
 \frac{k-r}{r+1}
 \frac{l-r}{k-l+r+1}. \tag{6}
\]

Its mode \(r_*\) stays a fixed fraction of \(n\) from the four relevant population boundaries; this is exactly the bulk localization supplied by the coefficient-clock/Gibbs calculation in S43. citeturn0view1

Taking one difference of \(\log(6)\) gives, throughout that bulk,
\[
-\frac Cn
\le
\Delta\log\frac{q_l(r+1)}{q_l(r)}
\le-\frac cn. \tag{7}
\]
Summing from the mode gives Gaussian decay. Summing in the reverse direction for \(|r-r_*|\le\sqrt n\) shows that at least \(c\sqrt n\) sites have probability comparable to the modal probability. Therefore
\[
q_l(r_*)\asymp n^{-1/2}. \tag{8}
\]
A second summation of (7), followed outside the bulk by the geometric ratio bound, yields globally
\[
-\log q_l(r)
\le
\frac12\log n+C+
C\frac{(r-r_*)^2}{n}. \tag{9}
\]

The exact-clock mean matching gives
\[
|E_HR-r_*|\le C,
\]
while (4) gives
\[
E_H(R-r_*)^2\le Cn.
\]
Consequently
\[
E_H[-\log q_l(R)]
\le\tfrac12\log n+C. \tag{10}
\]

Subtracting (5),
\[
\boxed{
D(p_l\|q_l)
=E_H[-\log q_l(R)]-H(p_l)
\le C.
} \tag{11}
\]

That is the missing cancellation.

S43 already derived the exact identity that the heat/Gibbs joint KL is precisely this one-dimensional overlap KL, and its chain rule decomposes it into the output and posterior KL terms. citeturn2view2 Therefore
\[
\boxed{
0\le\mathsf{Out}_l,\mathsf{Post}_l\le C.
} \tag{12}
\]
The previous \(\log n\) has disappeared.

### 4. The normalizer logarithm disappears too

A second logarithm was introduced in S43 through the crude lower bound on the actual count probability \(\pi_{k-r}\), leading to its equation (45). citeturn2view3

Here the actual count law is itself particularly simple:
\[
\pi_l=[t^l](q+pt)^k(p+qt)^k.
\]
It is a Poisson-binomial law consisting of \(k\) Bernoulli-\(p\)'s and \(k\) Bernoulli-\(q\)'s.

Exponential tilting gives, uniformly for \(|r|\le\eta n\),
\[
\boxed{
\left|\log\frac{\pi_{k-r}}{\pi_k}\right|
\le C\left(1+\frac{r^2}{n}\right).
} \tag{13}
\]
The proof is finite-\(n\): choose the tilt \(t\) whose tilted mean is \(k-r\). All tilted Bernoulli parameters remain uniformly nondegenerate, \(K''(t)\asymp n\), \(t=O(r/n)\), and Fourier inversion at the tilted mean gives mass \(\asymp n^{-1/2}\). The tilt rate is \(O(r^2/n)\).

Using the exact identity
\[
\pi_l=b^kz^{-l/2}Z_l
\]
therefore gives
\[
\boxed{
\left|
\log Z_{k-r}-\log Z_k+\frac{\beta r}{2}
\right|
\le C\left(1+\frac{r^2}{n}\right).
} \tag{14}
\]

Now insert this into
\[
\mathscr F_l
=\log {n\choose l}-\log Z_l+\beta m_l-\mathscr J_l.
\]
The linear \(\beta r/2\) terms cancel exactly, while the binomial coefficient, mean displacement, and Gibbs-information terms are all \(O(1+r^2/n)\). Hence
\[
|\mathscr F_k-\mathscr F_{k-r}|
\le C(1+r^2/n). \tag{15}
\]

Combining (12), (15), and S43's already-derived bounded determinantal evidence correction gives the requested prefix theorem:
\[
\boxed{
|F_k-F_{k-r}|
\le C\left(1+\frac{r^2}{n}\right),
\qquad0\le r\le\eta k.
} \tag{16}
\]

### 5. Paying the actual \(B_m\) weights at order \(n\)

The frozen actual coefficients satisfy the exact factorization
\[
\sum_m\frac{B_m}{n(n-1)}t^m
=\phi(t)^{k-2}\psi_k(t), \tag{17}
\]
where
\[
\phi(t)=(q+pt)(p+qt)
\]
and \(\psi_k\) is another complementary Bernoulli pair. This exact \(B_m\) representation is part of the frozen corrected-law ledger. citeturn6view0

Thus
\[
P_B(m):=\frac{B_m}{n(n-1)}
\]
is another symmetric Poisson-binomial law, centered at \(k-1\).

The same exponential-tilt Fourier argument, now retaining the two factors inserted by two coefficient differences, gives the nonuniform estimate
\[
\boxed{
|\Delta^2P_B(k-1-r)|
\le
Cn^{-3/2}
\left(1+\frac{r^2}{n}\right)e^{-cr^2/n}
} \tag{18}
\]
through a fixed macroscopic central band; outside that band the saddlepoint rate is \(e^{-cn}\).

Set
\[
G_r=F_k-F_{k-r},\qquad
v_r=w_{k-r}.
\]
Since
\[
F_{k-r}-F_{k-r-1}=G_{r+1}-G_r,
\]
Abel summation gives
\[
\sum_{r<R}v_r(G_{r+1}-G_r)
=
v_{R-1}G_R+
\sum_{r=1}^{R-1}(v_{r-1}-v_r)G_r. \tag{19}
\]

But
\[
|v_{r-1}-v_r|
=n(n-1)|\Delta^2P_B(k-1-r)|.
\]
Using (16) and (18),
\[
\begin{aligned}
\sum_r|v_{r-1}-v_r|\,|G_r|
&\le
Cn^2\sum_{r\ge0}
n^{-3/2}
(1+r^2/n)^2e^{-cr^2/n}\\
&=O(n), \tag{20}
\end{aligned}
\]
because the discrete Gaussian sum is \(O(\sqrt n)\).

Choose the cutoff at a fixed macroscopic distance \(R=\lfloor\delta n\rfloor\). The boundary term in (19) is exponentially small. Beyond it, the existing all-layer \(O(1)\) entropy-increment bound combines with exponentially small actual coefficient mass. The endpoint \(F_1=0\) is retained and no endpoint clock is invented. The upper half is already incorporated by the exact particle-hole reduction.

Therefore
\[
\boxed{
|W_n|
=
2\left|
\sum_{l=2}^kw_l(F_l-F_{l-1})
\right|
\le Cn.
} \tag{21}
\]

This improves the frozen SA04 all-layer \(O(n^{3/2})\) bound, whose exact coefficient factorization and tail accounting were already established. citeturn6view0 It also goes beyond the recovered S16 result, which explicitly left \(W_n=O(n)\) unresolved. citeturn8view1

## Exact remaining obligation

The logarithmic loss is removed at the corrected-law layer-response level:
\[
\boxed{D(p_l\|q_l)=O(1)},\qquad
\boxed{|F_k-F_{k-r}|\le C(1+r^2/n)},\qquad
\boxed{|W_n|\le Cn}.
\]

What remains **INCOMPLETE** is the signed \(n\)-scale analysis. An \(O(n)\) upper bound alone does not establish \(W_n+C_n<0\); neither the sharp coefficient of \(W_n/n\) nor the required comparison with the acceleration term \(C_n\) follows here. Likewise, nothing here transfers corrected-law concavity to the true sine-Toeplitz DPP.

The main reusable mechanism is:

\[
\boxed{\text{symmetric exclusion}
\Rightarrow\text{strong Rayleigh}
\Rightarrow\text{Poisson-binomial overlap}
\Rightarrow H(p_l)\sim\tfrac12\log n}
\]

combined with a saddlepoint finite-difference calculus for the **actual complementary-Bernoulli \(B_m\) law**.

Files:

:chatgpt-content-reference{index="10"}  
:chatgpt-content-reference{index="11"}  
:chatgpt-content-reference{index="12"}
