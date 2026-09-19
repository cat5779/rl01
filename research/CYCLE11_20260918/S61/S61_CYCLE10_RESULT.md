# S61 — A posterior-transport bound for the actual deletion fibers

**Date:** 2026-09-18.  
**Task provenance:** `cat5779/rl01`, PR 43, branch `research/sa-cycle10-s61-20260918`, task `prompts/CYCLE10/S61.md`.  
**Status:** **PROVED — author claim, awaiting independent review.**

## Outcome

For the frozen Fourier-DPP prior and the prescribed corrected clock, there are constants \(K_0,K_1,n_0\), independent of the layer and of \(n\), such that
\[
\boxed{
\mathcal C_{l-1}\le K_1\frac{\log n}{l},
\qquad K_0\log n\le l\le n/2,\quad n\ge n_0.
}\tag{A}
\]
In particular, the bound is \(O(\log n/n)\) uniformly on \(n/4\le l\le n/2\). A separately paid count-flux tail gives
\[
\boxed{
0\le\sum_{m=3}^{k-1}\omega_{n,m}\mathcal C_m
\le K\sqrt n\log n=o(n).
}\tag{T-S61}
\]
Thus the task's sufficient target **(T) is PROVED**, using the reviewed QWE05 likelihood bound. Combining this with the two reviewed one-sided payments gives
\[
\boxed{W_{\rm rel}\ge-K\sqrt n(1+\log n)=-o(n).}\tag{B}
\]
This is a lower bound, not an absolute-value estimate for \(W_{\rm rel}\), the response sum, or the interpolation sum. It does not prove the other curvature estimates in the larger project or sine entropy-rate concavity. A uniform \(K/n\) deletion bound is **INCOMPLETE** here.

The new finite tool is a **truncated posterior-transport lemma**. It transfers local regularity of a *conditional-kernel likelihood* to regularity of the *full spatial likelihood*, using bounded-displacement couplings of the actual latent posteriors. It then controls the entropy on complete deletion fibers. No latent posterior KL term is dropped.

Novelty beyond the result/application established here is unconfirmed. Stochastic covering, preservation of real stability under symmetric exclusion, exponential tilting, and the bounded-range cumulant inequality are classical ingredients.

---

## 1. Exact laws and notation — PROVED

Fix an upper layer \(l=m+1\), \(4\le l\le k\), and write
\[
\mu(A)=\det(P_A),\qquad |A|=k,
\qquad z=\frac{1+\xi_*}{\xi_*}=1521.
\]
The actual conditional kernel, with the input \(A\) held fixed, is
\[
t_A(T)=\frac{z^{|A\cap T|}}{Z_l(z)},\qquad
Z_l(z)=\sum_{j=0}^l\binom kj\binom k{l-j}z^j,
\quad |T|=l.
\tag{1.1}
\]
Indeed, at the midpoint the success probabilities inside and outside \(A\) are \(39/40\) and \(1/40\). Conditioning the output count to be \(l\) gives the odds ratio \(z=39^2\); the count-normalization is independent of the shape of \(A\). Consequently the prior remains exactly \(\mu\).

Let \(h_A\) be the law obtained by choosing a uniform \(l\)-subset of \(A\) and applying the Johnson heat semigroup for **exactly** time \(\tau_l\). Then
\[
p(T)=q_l(T)=\sum_A\mu(A)t_A(T),\qquad
\widehat p(T)=\widehat q_l(T)=\sum_A\mu(A)h_A(T).
\tag{1.2}
\]
The second equality follows from linearity of the prescribed semigroup and the given formula for \(r_l^{\max}\). Neither the prior nor the clock has been changed.

Permutations within \(A\) and within \(A^c\) leave both conditional kernels invariant. With
\[
N_j=\binom kj\binom k{l-j},\qquad
w(j)=N_jt_A(T),\qquad \widehat w(j)=N_jh_A(T)
\quad (|A\cap T|=j),
\]
define
\[
H(j)=\frac{\widehat w(j)}{w(j)}.
\]
Both laws have full overlap support \(0,\ldots,l\), and
\[
h_A(T)=t_A(T)H(|A\cap T|).
\tag{1.3}
\]
These radial quantities describe conditional kernels only; no spatial entropy is replaced by their entropy.

Two elementary bounds will be useful:
\[
z^{-1}\le\frac{p(T-i+j)}{p(T)}\le z,
\qquad
p(T)\ge p_{\min}:=\binom nl^{-1}z^{-l}.
\tag{1.4}
\]
The first follows by averaging a conditional ratio in \(\{z^{-1},1,z\}\). For the second, use \(Z_l(z)\le\binom nl z^l\).

The reviewed input used below is QWE05's full spatial pointwise bound
\[
\frac{p(T)}{\widehat p(T)}\le M_n,
\qquad
M_n=9\exp\!\left(\frac14+D_0b_0^2\right)n^{2D_0},
\quad D_0=\frac{1000}{261},\quad b_0=\frac{13}{7}.
\tag{1.5}
\]
It holds for \(n\ge40\), \(4\le l\le k\). This is QWE05_RESULT §4, independently accepted in QWE05_REVIEW §2.3. Its proof and the interpolation proof are not repeated here.

### Deletion normalization

Write \(P_-=K_{l-1}p\) and \(\widehat P_-=K_{l-1}\widehat p\). Thus
\[
P_-(S)=\frac1l\sum_{T\supset S,\,|T|=l}p(T),\qquad |S|=l-1.
\tag{1.6}
\]
For \(r=p/\widehat p\) and \(\bar r(S)=\mathbb E_{\alpha_{\widehat p}(\cdot\mid S)}r(S+x)\),
\[
P_-(S)=\widehat P_-(S)\bar r(S),\qquad
\alpha_p(x\mid S)=\alpha_{\widehat p}(x\mid S)\frac{r(S+x)}{\bar r(S)}.
\]
Consequently
\[
\mathcal C_{l-1}
=\sum_S\widehat P_-(S)\operatorname{Ent}_{\alpha_{\widehat p}(\cdot\mid S)}(r)
=D(p\Vert\widehat p)-D(P_-\Vert\widehat P_-).
\tag{1.7}
\]
In particular
\[
0\le\mathcal C_{l-1}\le D(p\Vert\widehat p)\le\log M_n.
\tag{1.8}
\]
Identity (1.7) alone is not the result. The next lemma bounds its fiber entropy.

---

## 2. The finite posterior-transport tool — PROVED

### Theorem 2.1

Let \(p,\widehat p\) be strictly positive laws on the \(l\)-subsets of an \(n\)-point set, and let the latent index set be finite. Suppose they admit a common-prior representation
\[
p(T)=\sum_A\mu(A)t_A(T),\qquad
\widehat p(T)=\sum_A\mu(A)t_A(T)H(J_T(A)),
\tag{2.1}
\]
where \(H\) is a positive function on an integer interval and \(J_T(A)\) is integer-valued. The kernels in (2.1) are normalized probability laws for each \(A\).

Write
\[
\rho_T(A)=\frac{\mu(A)t_A(T)}{p(T)},\qquad
F(T)=\mathbb E_{\rho_T}H(J_T),
\]
so that \(\widehat p(T)=p(T)F(T)\). Assume the following verifiable properties:

1. For every Johnson-adjacent pair \(T,T'\), there is a coupling of \(\rho_T,\rho_{T'}\) under which \(|J_T(A)-J_{T'}(A')|\le b\), for a fixed integer \(b\).
2. \(p(T')/p(T)\le B\) for adjacent pairs; \(p/\widehat p\le M\); and \(p(T)\ge p_{\min}>0\).
3. For some real center \(a\), radius \(R>b\), and number \(L\ge0\),
   \[
   |\log H(j+1)-\log H(j)|\le L
   \]
   whenever both consecutive integers are in \([a-R,a+R]\).

Let
\[
\varepsilon=
\Pr_{\widehat{\mathbb P}}\{|J_T(A)-a|>R-b\},
\quad
\widehat{\mathbb P}(A,T)=\mu(A)t_A(T)H(J_T(A)),
\]
and put \(D_* =\log(M/p_{\min})\). For every \(0<\delta<1\),
\[
\boxed{
\mathcal C_{l-1}\le
\frac{[bL-\log(1-\delta)]^2}{8}
+D_*\min\!\left\{1,
[1+B(n-l)]\frac{M\varepsilon}{\delta}\right\}.
}\tag{2.2}
\]
The statement concerns the actual marginal laws \(p,\widehat p\), not deletion conditioned on \(A\).

### Proof

The corrected posterior is
\[
\widehat\rho_T(A)=\rho_T(A)\frac{H(J_T(A))}{F(T)}.
\tag{2.3}
\]
Define its conditional tail probability
\[
\beta_T=
\widehat\rho_T\{|J_T-a|>R-b\},
\qquad
\mathcal G=\{T:\beta_T\le\delta\}.
\]
The exact transfer between the two marginal measures is
\[
\begin{aligned}
p(\mathcal G^c)
&\le\delta^{-1}\sum_Tp(T)\beta_T\\
&=\delta^{-1}\sum_T\widehat p(T)\frac{p(T)}{\widehat p(T)}\beta_T\\
&\le\frac{M\varepsilon}{\delta}.
\end{aligned}
\tag{2.4}
\]
This is where the change of posterior and averaging measure is paid.

Take adjacent \(T,T'\in\mathcal G\), and a coupling \(\Gamma\) from hypothesis 1. Let \(j=J_T(A)\), \(j'=J_{T'}(A')\), and
\[
E=\{|j-a|\le R,\ |j'-a|\le R\}.
\]
Because \(|j-j'|\le b\), the complement of \(E\) implies \(|j-a|>R-b\), and also implies \(|j'-a|>R-b\). By (2.3),
\[
\mathbb E_\Gamma[H(j)\mathbf1_E]\ge(1-\delta)F(T),\qquad
\mathbb E_\Gamma[H(j')\mathbf1_E]\ge(1-\delta)F(T').
\tag{2.5}
\]
On \(E\), hypothesis 3 gives \(e^{-bL}H(j)\le H(j')\le e^{bL}H(j)\). Hence
\[
(1-\delta)e^{-bL}\le\frac{F(T')}{F(T)}
\le\frac{e^{bL}}{1-\delta}.
\]
Since \(r=p/\widehat p=1/F\),
\[
|\log r(T')-\log r(T)|\le bL-\log(1-\delta)=:u.
\tag{2.6}
\]

Call a retained set \(S\) bad if it has at least one extension in \(\mathcal G^c\). Using the **probability** deletion factor \(1/l\),
\[
\begin{aligned}
P_-(S\text{ bad})
&\le\sum_{T\in\mathcal G^c}\sum_{\substack{S\subset T\\|S|=l-1}}P_-(S),\\
\sum_{\substack{S\subset T\\|S|=l-1}}P_-(S)
&=p(T)+\frac1l\sum_{i\in T,j\notin T}p(T-i+j)\\
&\le[1+B(n-l)]p(T).
\end{aligned}
\tag{2.7}
\]
Thus the bad retained-set mass is at most the minimum in (2.2).

If \(S\) is not bad, all its extensions are in \(\mathcal G\). Any two are adjacent, so \(U(x)=\log r(S+x)\) has range at most \(u\). For \(a_S=\alpha_p(\cdot\mid S)\),
\[
D(\alpha_p\Vert\alpha_{\widehat p})
=\mathbb E_{a_S}U+\log\mathbb E_{a_S}e^{-U}
\le\frac{u^2}{8}.
\tag{2.8}
\]
For completeness, center \(U\) and differentiate its log moment-generating function twice. Under every exponential tilt its variance is at most \(u^2/4\). The value and first derivative at zero vanish; integrating the second derivative over \([0,1]\) with weight \(1-t\) gives (2.8).

On every fiber, including a bad one,
\[
\alpha_{\widehat p}(x\mid S)
=\frac{\widehat p(S+x)}{\sum_y\widehat p(S+y)}
\ge\widehat p(S+x)\ge\frac{p_{\min}}M.
\]
It follows that \(D(\alpha_p\Vert\alpha_{\widehat p})\le D_*\). Average this bound on the bad fibers and (2.8) on the others. This proves (2.2). \(\square\)

The theorem neither invokes reverse data processing nor infers fiber regularity from a deleted marginal.

---

## 3. The actual posterior has the required coupling — PROVED

Let \(V\) be the actual Fourier frame,
\[
V_{sr}=n^{-1/2}e^{2\pi i rs/n},\qquad 0\le r<k.
\]
Then \(P=VV^*\), \(V^*V=I_k\), and Cauchy--Binet gives the generating polynomial
\[
\sum_{|A|=k}\mu(A)\prod_{i\in A}x_i
=\det(V^*\operatorname{diag}(x_i)V).
\tag{3.1}
\]
If every \(x_i\) has positive imaginary part, the matrix on the right has positive-definite imaginary part, hence is nonsingular. Thus (3.1) is real stable: the exact Fourier prior is strongly Rayleigh.

Multiplication by positive external fields preserves this property by positive rescaling of the variables. The actual posterior
\[
\rho_T(A)\propto\mu(A)\prod_{i\in A}z^{\mathbf1_{i\in T}}
\tag{3.2}
\]
is therefore a homogeneous strongly Rayleigh law.

We use the classical stochastic-covering theorem: conditioning a homogeneous strongly Rayleigh law on a single site being absent or present admits a coupling on the remaining sites in which the absent-site configuration contains the present-site configuration and differs by one element. See Pemantle--Peres, Proposition 2.2; this follows from strong-Rayleigh negative dependence and homogeneity.

Here is the field-change consequence needed for the application. Changing one positive external field changes only the mixing probability of the site's indicator; its two conditional laws on the remaining sites stay unchanged. Couple the two indicators monotonically. When equal, use identical remaining configurations. When unequal, use the preceding covering coupling. The two full \(k\)-sets then differ by at most one exchange. Degenerate indicators cause no difficulty: the field change has no effect there.

For \(T'=T-i+j\), (3.2) changes two fields. Compose the two one-field couplings. The resulting \(A,A'\) differ by at most two exchanges. Therefore
\[
\big||A\cap T|-|A'\cap T'|\big|
\le\big||A\cap T|-|A'\cap T|\big|
 +\big||A'\cap T|-|A'\cap T'|\big|
\le2+1=3.
\tag{3.3}
\]
Theorem 2.1 applies with \(b=3\) and, by (1.4), \(B=z\).

No covering property is assumed for the corrected posterior. Its tails enter only through the exact weighting formula (2.3).

---

## 4. Actual and corrected overlap laws: root structure and moments — PROVED

### 4.1 Both overlap laws are Poisson-binomial

A polynomial with nonnegative coefficients and strictly negative real zeros, normalized to take value one at one, is the probability generating function of a sum of independent Bernoulli variables. This is a factorization statement, not a claim of independence of the physical sites.

For the true overlap law, start with the elementary symmetric polynomial \(e_l\) in \(2k\) variables. It is real stable: obtain it by differentiating \(\prod_i(t+x_i)\) in \(t\) and setting \(t=0\). Set the variables in \(A\) equal to \(s\) and the other variables equal to one. The result, normalized at \(s=1\), is
\[
G_{k,l}(s)/G_{k,l}(1),\qquad
G_{k,l}(s)=\sum_j\binom kj\binom k{l-j}s^j.
\]
Specialization at real constants preserves stability by a limit. The polynomial has positive coefficients and degree \(l\), so all its zeros are strictly negative. Tilting by \(z\) preserves this structure and gives \(w\).

For the corrected conditional kernel, the initial generating polynomial is
\[
\binom kl^{-1}e_l((x_i)_{i\in A}),
\]
which is real stable. On this layer,
\[
L_l=\frac1{l(n-l)}\sum_{i<j}(\sigma_{ij}-I),
\tag{4.1}
\]
where \(\sigma_{ij}\) exchanges two site variables. The classical partial-symmetrization theorem of Borcea--Brändén--Liggett, Theorem 4.20, preserves real stability under a convex combination of the identity and a transposition. Each factor
\[
e^{s(\sigma_{ij}-I)}
=\frac{1+e^{-2s}}2 I+\frac{1-e^{-2s}}2\sigma_{ij}
\]
has this form. The Lie--Trotter product formula and closure under coefficient limits prove preservation by the exact semigroup in (4.1), at the prescribed time \(\tau_l\). This is also BBL Proposition 5.1/Theorem 5.2.

Specialize again to the variables counting \(|A\cap T|\). The corrected overlap generating polynomial has strictly negative real zeros and degree \(l\). Thus \(\widehat w\) is also Poisson-binomial. Positivity on all overlap classes follows from irreducibility at positive heat time.

Only this property of the corrected *conditional kernel* is needed. No unproved weak-dependence property of the full corrected law is used.

### 4.2 The prescribed clock matches a conditional quadratic moment

Set
\[
v_0=\frac{l(n-l)}{4(n-1)},\qquad
H_0=\frac{nl(l-1)}{4(n-1)}=\frac{l^2}{4}-v_0,
\qquad H_2(j)=(j-l/2)^2-v_0.
\]
With \(d=k-l+1\), the following identities follow directly from the finite polynomial coefficients:
\[
G_{k,l}\!\left(\frac{1+\xi}{\xi}\right)
=\binom kl\xi^{-l}Q_l^{(d)}(\xi),
\tag{4.2}
\]
\[
Q_l^{(d)}-Q_{l-2}^{(d)}
=\frac{2(n-1)}d\,\xi(1+\xi)Q_{l-2}^{(d+1)}.
\tag{4.3}
\]
An explicit coefficient verification is provided in Appendix A.

The factorial-moment identity
\[
\mathbb E_w[J(l-J)]
=k^2z\frac{G_{k-1,l-2}(z)}{G_{k,l}(z)}
\]
combined with (4.2)--(4.3) gives
\[
\mathbb E_w[J(l-J)]
=H_0\left(1-\frac{Q_{l-2}^{(d)}}{Q_l^{(d)}}\right).
\]
As \(H_2(j)=H_0-j(l-j)\),
\[
\mathbb E_w H_2(J)=H_0\theta,
\qquad\theta=\frac{Q_{l-2}^{(d)}(\xi_*)}{Q_l^{(d)}(\xi_*)}.
\tag{4.4}
\]
This is an identity for each fixed input \(A\), not merely a statement about a Fourier mode after averaging the prior.

A direct generator computation gives
\[
L_l(J-l/2)=-\frac n{l(n-l)}(J-l/2),\qquad
L_lH_2=-\frac{2(n-1)}{l(n-l)}H_2.
\tag{4.5}
\]
Initially \(J=l\) under the corrected kernel. Since \(e^{-\gamma_{2,l}\tau_l}=\theta\), equations (4.4)--(4.5) prove
\[
\mathbb E_{\widehat w}H_2=\mathbb E_wH_2.
\tag{4.6}
\]

### 4.3 Uniform nondegenerate variances

Represent the untilted overlap as \(\sum_{a=1}^l B_a\), with independent Bernoulli parameters \(p_a\). Exponential tilting by \(z\ge1\) changes them to
\[
p_a(z)=\frac{zp_a}{1+(z-1)p_a}.
\]
For every \(a\),
\[
p_a(z)(1-p_a(z))\ge z^{-1}p_a(1-p_a).
\]
The untilted hypergeometric variance is \(v_0\), so
\[
\operatorname{Var}_wJ\ge v_0/z.
\tag{4.7}
\]
For \(a\ne b\), similarly,
\[
p_a(z)(1-p_b(z))\ge z^{-1}p_a(1-p_b).
\]
Summing gives
\[
\mathbb E_w[J(l-J)]\ge z^{-1}\mathbb E_{z=1}[J(l-J)]=H_0/z.
\]
By (4.4), \(1-\theta\ge1/z\).

Writing \(\widehat v=\operatorname{Var}_{\widehat w}J\), (4.5) yields the exact formulas
\[
\widehat\mu=\frac l2\left(1+\theta^{n/[2(n-1)]}\right),
\tag{4.8}
\]
\[
\widehat v
=v_0(1-\theta)+\frac{l^2}{4}
\left(\theta-\theta^{n/(n-1)}\right)
\ge v_0/z.
\tag{4.9}
\]
Both laws are sums of \(l\) Bernoullis, so their variances are at most \(l/4\). For all \(l\le k\), therefore,
\[
\boxed{
\nu l\le v,\widehat v\le l/4,
\qquad \nu=\frac1{8z}>0.
}\tag{4.10}
\]
In particular, the corrected variance lower bound is proved at the prescribed heat time; it is not an extra regularity assumption.

### 4.4 The two overlap means differ by a bounded amount

Write \(\mu=\mathbb E_wJ\), \(y=l-\mu\), and \(v=\operatorname{Var}_wJ\). The exact neighboring-probability recurrence
\[
(j+1)(k-l+j+1)w(j+1)=z(l-j)(k-j)w(j)
\]
gives, after summing and using \(z=(1+\xi)/\xi\),
\[
y^2+(k-l+n\xi)y+v=lk\xi.
\tag{4.11}
\]
Let \(\rho=\sqrt{\xi(1+\xi)}-\xi\). The increasing quadratic
\(F(y)=y^2+(k-l+n\xi)y-lk\xi\) satisfies
\[
F(l\rho)=l(k-l)\rho(1-\rho)\ge0,
\qquad F(y)=-v\le0.
\]
Hence \(y\le l\rho\). At \(\xi_*\), \(\rho=1/40\), so
\[
\mu-l/2\ge cl/2.
\tag{4.12}
\]
Also \(\widehat\mu\ge l/2\) by (4.8). The exact match (4.6) now implies
\[
(\mu-\widehat\mu)(\mu+\widehat\mu-l)=\widehat v-v.
\]
Using (4.10) and (4.12),
\[
\boxed{|\mu-\widehat\mu|\le\frac1{2c}.}\tag{4.13}
\]
The two variances need not be close. Bounded mean displacement and linear variance are sufficient.

---

## 5. A local probability-ratio lemma — PROVED

### Lemma 5.1

Let \(X\) be a sum of \(N\) independent Bernoulli variables, each with parameter strictly between zero and one. Suppose \(\operatorname{Var}X=v\ge\nu N\). There are constants \(C_\nu,N_\nu\) such that, for \(N\ge N_\nu\) and any integer \(j\) with
\[
|j-\mathbb EX|\le\frac{\nu N}{2e},
\]
\[
\boxed{
\left|\log\frac{\Pr(X=j+1)}{\Pr(X=j)}\right|
\le C_\nu\left(\frac{|j-\mathbb EX|}{N}+N^{-1/2}\right).
}\tag{5.1}
\]

### Proof

First suppose the mean is the integer \(j\). For the characteristic function \(\phi\),
\[
|\phi(t)|\le\exp[-2v\sin^2(t/2)]
\le\exp[-2vt^2/\pi^2],\qquad |t|\le\pi.
\tag{5.2}
\]
Fourier inversion consequently gives
\[
|\Pr(X=j+1)-\Pr(X=j)|
\le\frac1{2\pi}\int_{-\pi}^{\pi}|t|e^{-2vt^2/\pi^2}\,dt
\le C/v.
\tag{5.3}
\]
For the centered characteristic function, a Taylor expansion at zero gives, uniformly in the Bernoulli parameters,
\[
\log(e^{-ijt}\phi(t))=-vt^2/2+O(v|t|^3)
\tag{5.4}
\]
for \(|t|\) at most a fixed small constant. To verify uniformity, the third derivative of
\(\log(1-p+pe^{it})-ipt\) is bounded in absolute value by a universal constant times \(p(1-p)\) on that interval. Summing gives (5.4).

Choose the interval small enough that the remainder in (5.4) is at most \(vt^2/4\). On it, the difference between the centered characteristic function and \(e^{-vt^2/2}\) is at most \(Cv|t|^3e^{-vt^2/4}\), whose integral is \(O(v^{-1})\). Outside it, (5.2) supplies an exponentially small integral. Hence
\[
\Pr(X=j)=(2\pi v)^{-1/2}+O(v^{-1})\ge c_1v^{-1/2}
\tag{5.5}
\]
for sufficiently large \(v\). Dividing (5.3) by (5.5), and then taking logarithms, bounds the centered consecutive log ratio by \(C/\sqrt v\).

For a general \(j\), note that \(v\le\min(\mathbb EX,N-\mathbb EX)\), so the stated range lies strictly inside the support. Exponentially tilt by \(e^{sX}\). Its variance \(v(s)\) satisfies
\[
e^{-|s|}v\le v(s)\le e^{|s|}v.
\tag{5.6}
\]
Since the derivative of the tilted mean is \(v(s)\), the stated range of \(j\) permits a tilt with mean exactly \(j\) and
\[
|s|\le e|j-\mathbb EX|/v\le1/2,
\qquad v(s)\ge v/e.
\]
The original consecutive ratio is \(e^{-s}\) times the tilted consecutive ratio. Apply the centered estimate and \(v\ge\nu N\). This proves (5.1). \(\square\)

### Consequence for the actual kernel likelihood

Apply Lemma 5.1 to \(w\) and \(\widehat w\), using (4.10)--(4.13). On an integer window of radius \(R\) about \(\widehat\mu\), provided \(R+1+1/(2c)\le\nu l/(2e)\),
\[
\boxed{
\max |\log H(j+1)-\log H(j)|
\le K_c\left(\frac{R+1}{l}+l^{-1/2}\right).
}\tag{5.7}
\]
The maximum is over consecutive integers inside the window. This is the missing conditional-kernel likelihood regularity, now proved rather than assumed.

---

## 6. Apply the tool and obtain an actual fiber bound — PROVED

Take \(M=M_n\), \(b=3\), \(B=z\), and choose
\[
\delta=n^{-2},\qquad
R=3+\sqrt{\frac l2[\log(2M_n)+10\log n]}.
\tag{6.1}
\]
Since \(\widehat w\) is a sum of \(l\) independent Bernoulli variables, the bounded-range exponential-moment bound and Chernoff's method give
\[
\Pr_{\widehat w}\{|J-\widehat\mu|>R-3\}
\le2e^{-2(R-3)^2/l}
=\frac1{M_n n^{10}}.
\tag{6.2}
\]
This probability equals the corrected joint tail \(\varepsilon\) in Theorem 2.1, because the overlap distribution is the same for every fixed input.

Write \(\log M_n=a_0+a_1\log n\), where \(a_0,a_1\) are fixed. Taking \(K_0\) sufficiently large ensures that, whenever \(l\ge K_0\log n\), the window (6.1) lies within the moderate-deviation range of (5.7). Indeed \(R/l\le K\sqrt{\log n/l}+3/l\). Thus
\[
L\le K\sqrt{\frac{\log n}{l}}.
\tag{6.3}
\]
All constants here depend only on the fixed \(c\), not on \(n\) or the layer.

The exceptional output mass from (2.4) is at most \(n^{-8}\), and the exceptional retained-set mass from (2.7) is at most \([1+z(n-l)]n^{-8}=O(n^{-7})\). Also
\[
D_*\le\log M_n+\log\binom nl+l\log z\le K n.
\tag{6.4}
\]
The exceptional contribution in (2.2) is therefore \(O(n^{-6})\), not an unpaid tail. Its regular contribution is bounded by
\[
\frac{[3L-\log(1-n^{-2})]^2}{8}
\le K\frac{\log n}{l}.
\]
This proves (A), after absorbing \(O(n^{-6})\).

In particular,
\[
\mathcal C_m\le K\frac{\log n}{n}
\quad\text{when }n/4\le m+1\le k,
\tag{6.5}
\]
for all sufficiently large even \(n\). The endpoint \(m=k-1\) is included.

---

## 7. Exact count-flux tail and target (T) — PROVED

For every layer \(4\le l\le k\), including those outside the range of (A), equation (1.8) gives \(\mathcal C_{l-1}\le\log M_n=O(\log n)\).

Let \(q_0=1/40\). The exact count polynomial satisfies
\[
p_0(t)=(1-q_0+q_0t)(q_0+(1-q_0)t),
\qquad B_n(1)=n(n-1).
\]
The normalized polynomial \(B_n/B_n(1)\) is a mixture of the following two probability generating functions:
\[
p_0^{k-1},\qquad \frac{(1+t)^2}{4}p_0^{k-2}.
\]
Each component is a sum of exactly \(n-2\) independent Bernoulli variables and has mean \(k-1\). Therefore, with \(r=\lfloor n/4\rfloor\),
\[
B_{n,r}\le n(n-1)
\exp\!\left[-\frac{2(k-1-r)^2}{n-2}\right]
\le n^2e^{-n/32}
\tag{7.1}
\]
for sufficiently large \(n\) (in fact the displayed rough exponent is valid once \(n\ge8\)).

By telescoping the exact nonnegative fluxes,
\[
\sum_{m=0}^{r}\omega_{n,m}=B_{n,r}.
\]
Consequently the layers with \(m+1<n/4\) contribute at most
\[
\sum_{\substack{3\le m<k\\m+1<n/4}}
\omega_{n,m}\mathcal C_m
\le (\log M_n)n^2e^{-n/32}.
\tag{7.2}
\]
In particular \(m=3\) is retained and paid. Nothing here says \(\mathcal C_3=0\).

On the remaining layers use (6.5) and the reviewed exact-flux mass bound \(\sum_{m<k}\omega_{n,m}=O(n^{3/2})\). This gives
\[
\sum_{m=3}^{k-1}\omega_{n,m}\mathcal C_m
\le K\sqrt n\log n+K n^2\log n\,e^{-n/32}
=O(\sqrt n\log n)=o(n).
\tag{7.3}
\]
The count weights have not been replaced, frozen, or differentiated after a static inequality.

---

## 8. Reviewed ledger and scope of the conclusion

Use the supplied, reviewed identities and one-sided inequalities:
\[
W_{\rm rel}=-2\sum_{m=3}^{k-1}\omega_{n,m}
[\mathcal C_m+\eta_mR_{m,\xi}+\mathcal J_m],
\]
\[
\sum_m\omega_{n,m}\eta_mR_{m,\xi}\le K\sqrt n,
\qquad
\sum_m\omega_{n,m}\mathcal J_m\le K\sqrt n(1+\log n).
\]
Equation (7.3) proves (B). Only the upper bounds on the two signed sums are used. No absolute-value payment is asserted.

| Claim | Status | Scope |
|---|---|---|
| Finite truncated posterior-transport tool (2.2) | PROVED | Arbitrary positive kernels satisfying its explicit coupling, local-ratio, tail, and domination hypotheses |
| Actual Fourier posterior bounded-displacement coupling | PROVED | Positive-field tilts of the exact Fourier determinant prior; displacement at most three in overlap |
| Required corrected overlap root property and local likelihood bound | PROVED | Prescribed Johnson semigroup; no assumption about corrected posterior covering |
| Actual bound (A) and sufficient target (T) | PROVED | Author claim using reviewed QWE05 pointwise domination |
| Original lower-bound goal \(W_{\rm rel}\ge-o(n)\) | PROVED | Also uses the two reviewed one-sided ledger payments |
| Uniform \(\mathcal C_m\le K/n\) | INCOMPLETE | Neither proved nor disproved by this argument |
| Other curvature budgets and sine entropy-rate concavity | INCOMPLETE | Outside the reward supplied by this result |

The proof does not cross the central layer: \(l=k\) is the last upper layer used. It does not infer an equivalence between (T) and the weaker \(W_{\rm rel}\) lower bound. In particular, failure of a sufficient condition such as (T) would not by itself refute that lower bound. No actual asymptotic counterexample is asserted.

### Dependency ledger

**Reviewed mathematical inputs used:** QWE05's polynomial pointwise domination (1.5); the deletion ledger; the S14 one-sided response payment; QWE05's independently checked one-sided interpolation payment; and the exact nonnegative flux mass estimate supplied in the task.

**Classical theorems used:** strong-Rayleigh stochastic covering (Pemantle--Peres, Proposition 2.2); real-stability closure under differentiation, real specialization, positive fields, and coefficient limits; and partial symmetrization/symmetric-exclusion preservation (BBL, Theorem 4.20 and Proposition 5.1/Theorem 5.2).

**Proved in this submission:** the finite posterior-to-fiber transfer inequality; the actual posterior field-change coupling; the conditional quadratic-clock identity by finite coefficients; two-sided linear overlap-variance bounds and bounded mean displacement; the local Poisson-binomial consecutive-ratio estimate; the actual central/large-layer fiber estimate; and the explicit count-flux tail payment.

**Not consumed:** corrected deleted-marginal chi-square, the full-mode heat-source norm, any S14 Dirichlet budget a second time, or an unproved regularity property of the likelihood.

---

## 9. Candidate mechanisms not used

**Entropic-independence/approximate-tensorization shortcut — INCOMPLETE as a route to the requested upper bound.** Entropic Independence I defines and uses KL contraction under down operators; such contraction is naturally a lower bound on lost information, not the required upper bound. Approximate tensorization similarly bounds total entropy by conditional entropy production under verified dependence hypotheses. Neither result alone supplies (A). Both primary sources were checked; their inequalities are not cited as proofs of (T).

**Unqualified latent conditional-KL comparison — INCOMPLETE.** Merely bounding deletion after revealing \(A\) leaves posterior-information terms when one removes \(A\). The successful replacement is (2.3)--(2.7): it compares the actual marginal likelihood normalizers, transfers corrected posterior tails under the actual marginal with the explicit factor \(M_n\), and pays every bad fiber.

**Deleted-marginal or heat-source control alone — INCOMPLETE as a route to (T), and not used.** The already identified kernel obstruction is not a counterexample to the actual Fourier result and is not offered as new progress. The successful proof supplies additional, model-verified likelihood regularity on the fibers themselves.

---

## 10. Useful checks and their limitations

The bundled `s61_checks.py` was run with `--max-n 16 --radial-max 8192`.

* There are 153 exact-rational polynomial cases, all even \(8\le n\le40\), \(4\le l\le k\). They check the normalization transformation, the contiguous identity (4.3), and an additional differentiated-moment identity.
* There are 15 full spatial Fourier cases, all even \(8\le n\le16\), \(4\le l\le k\). The actual law is calculated using \(\Lambda=39P+(I-P)/39\); the corrected law is calculated using the full sparse Johnson generator. Both deletion normalizations, the KL chain rule, the fiber-entropy representation, and finite versions of the transfer estimates are checked.
* The latent mixtures over the actual Fourier determinant prior are independently checked for \(n\le12\). A small posterior field-change coupling is explicitly constructed by linear programming and glued across two field changes.
* There are 15 radial moment checks at \(n=32,128,512,2048,8192\), three layers each. These check formulas and scales, not the spatial target by substitution.

Recorded maximum errors: KL chain rule \(3.99\times10^{-16}\); fiber-entropy representation \(5.17\times10^{-17}\); actual/corrected latent-mixture comparison \(1.88\times10^{-16}\); explicit posterior-coupling marginal error \(3.50\times10^{-10}\); large radial heat-moment error \(1.09\times10^{-10}\).

These are finite sanity checks, not an asymptotic proof or independent review. The proof of (T) is Sections 2--7, not a numerical trend.

---

## Appendix A. Finite coefficient details — PROVED

For (4.2), the coefficient of \(\xi^s\) in \(\xi^lG_{k,l}((1+\xi)/\xi)\) equals
\[
\sum_{u=0}^s\binom k{l-u}\binom ku\binom{l-u}{s-u}
=\binom k{l-s}\binom{2k-l+s}{s},
\]
by a binomial-factor rearrangement followed by Vandermonde's identity. Divide by \(\binom kl\) to obtain exactly the coefficient prescribed for \(Q_l^{(d)}\).

For (4.3), write
\[
a_{r,d}(s)=\frac{r_{\underline s}(r+2d-1)_{\overline s}}
{d_{\overline s}s!},
\]
with value zero outside \(0\le s\le r\). The coefficient statement is
\[
a_{l,d}(s)-a_{l-2,d}(s)
=\frac{2(n-1)}d\big[a_{l-2,d+1}(s-1)+a_{l-2,d+1}(s-2)\big].
\tag{A.1}
\]
At \(s=0\) both sides are zero, and \(s=1\) is immediate. For \(2\le s\le l\), put \(v=l+2d-1\) and divide by
\[
\frac{(l-2)_{\underline{s-2}}v_{\overline{s-2}}}{d_{\overline s}s!}.
\]
Then (A.1) becomes the elementary polynomial identity
\[
\begin{aligned}
&l(l-1)(v+s-2)(v+s-1)
-(l-s)(l-s-1)(v-2)(v-1)\\
&\qquad=2(l+v-2)s
\big[(l-s)(v+s-2)+(s-1)(d+s-1)\big],
\end{aligned}
\]
which follows by expansion using \(v=l+2d-1\). Since \(l+v-2=n-1\), this is (A.1). All higher coefficients vanish. This proves (4.3).

For the factorial moment in §4.2, use
\[
j(l-j)\binom kj\binom k{l-j}
=k^2\binom{k-1}{j-1}\binom{k-1}{l-j-1}.
\]
The ratio of the binomial normalizers is
\[
k^2\frac{\binom{k-1}{l-2}}{\binom kl}
=\frac{kl(l-1)}d
=H_0\frac{2(n-1)}d.
\]
Together with \(z\xi^2=\xi(1+\xi)\), these identities complete the calculation of (4.4).

---

## Sources

Repository source identifiers, read as mathematical inputs:

- `research/CYCLE10_20260918/sources/QWE05_REVIEW.md`
- `research/CYCLE10_20260918/sources/QWE05_RESULT.md`
- `research/CYCLE10_20260918/sources/QWE05_TASK.md`
- `research/CYCLE10_20260918/sources/SA05_CROSS_LAYER.md`
- `research/CYCLE10_20260918/sources/S14_REPAIR.md`
- `research/CYCLE10_20260918/sources/S14_INDEPENDENT_REVIEW.md`

Primary literature:

**[BBL]** Julius Borcea, Petter Brändén, Thomas M. Liggett, *Negative dependence and the geometry of polynomials*, arXiv:0707.2340. Theorem 4.20 and Proposition 5.1/Theorem 5.2 are the preservation results used.

**[PP]** Robin Pemantle, Yuval Peres, *Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures*, arXiv:1108.0687. Proposition 2.2 is the stochastic-covering input.

**[EI]** *Entropic Independence I: Modified Log-Sobolev Inequalities for Fractionally Log-Concave Distributions and High-Temperature Ising Models*, arXiv:2106.04105. Checked for inequality direction; not a proof input for (T).

**[AT]** Pietro Caputo, Georg Menz, Prasad Tetali, *Approximate tensorization of entropy at high temperature*, arXiv:1405.0608. Checked as a neighboring mechanism; not a proof input for (T).

`SOURCES.md` in the bundle supplies the exact source locations. The research claims above remain author claims until independent review.
