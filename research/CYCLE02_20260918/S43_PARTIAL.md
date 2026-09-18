# S43 harvested response

Status: AUTHOR_SUBMISSION_PENDING_INDEPENDENT_REVIEW. PARTIAL_TEXT: the read tool returned only the first 20,000 characters. The ending is missing; do not claim the complete proof was recovered.
Source task: 6aabf6e9-b76c-83ee-a787-89a1e76292b2
Citation markers are preserved as provenance, not independent supporting evidence.

---

# S43 — A posterior-transport bound for the signed information response

**CORRECTED_LAW_ONLY**

I obtain an unconditional sub-\(n^{3/2}\) bound for the requested information aggregate. In fact, the same construction also bounds \(W_n\), without assuming the unavailable S16 radial argument.

Put
\[
\mathcal I_n
:=
2\sum_{l=2}^{k}w_l
\bigl[J_l(s_l)-J_{l-1}(s_{l-1})\bigr].
\]

**The result proved below is**
\[
\boxed{
|\mathcal I_n|+|W_n|
\le C\,n\log(n+1)
\qquad(n=2k\ge4),
}
\tag{1}
\]
where \(C<\infty\) depends only on the fixed \(c=19/20\). Consequently,
\[
\boxed{
\frac{\mathcal I_n}{n^{3/2}}\longrightarrow0,
\qquad
\frac{W_n}{n^{3/2}}\longrightarrow0
}
\tag{2}
\]
along even \(n\).

These are upper bounds, not assertions of a matching order or an eventual sign. In particular, this does **not** prove \(O(n)\).

The mechanism is a **moment-matched Bayesian ensemble transport**. An auxiliary Gibbs channel has an explicit determinantal posterior. The actual coefficient clock matches its overlap mean to within \(O(1)\). A bounded, averaged log-determinant Hessian then controls the change in Bayesian evidence. The remaining discrepancy is an explicit posterior KL divergence bounded by \(\log(n+1)+O(1)\). Its layer differences have no asserted sign; their contribution is paid by summation by parts with the **actual** \(w_l\).

The S16 radial asymptotic is not an input to this proof. Its visible harvest does not contain the missing attachment bodies and is marked pending independent review. citeturn860027view0

---

## 1. Exact model and theorem

All logarithms are natural. Write
\[
p=\frac{39}{40},\qquad q=\frac1{40},\qquad
b=pq=\frac{39}{1600},\qquad
z=\left(\frac pq\right)^2=1521,\qquad
\beta=\log z.
\]

On the \(n=2k\) cyclic sites, let
\[
U_{jr}=n^{-1/2}e^{2\pi i jr/n},
\qquad 0\le j<n,\quad 0\le r<k,
\]
and \(P=UU^*\). The latent law is
\[
\nu(A)=\det P_A,\qquad |A|=k.
\]

For \(l\le k\), conditional on \(A\), the process starts from a uniform \(l\)-subset of \(A\) and evolves under the original-rate generator
\[
(G_l f)(S)=
\sum_{i\in S,\ j\notin S}
\bigl[f(S-i+j)-f(S)\bigr].
\]
Denote its conditional law at time \(s\) by \(T^H_{l,s}(\cdot\mid A)\), its marginal by \(\mu_l(s)\), and set
\[
J_l(s)=I(A;S_{l,s}),\qquad
F_l(s)=D(\mu_l(s)\Vert u_l).
\]
These are the frozen model’s latent law and heat normalization. citeturn342519view0turn342519view1

The prescribed clock is, for \(2\le l\le k\),
\[
Z_l(z)=[t^l](1+t)^k(1+zt)^k,
\]
\[
a_j=[t^j](1+t)^{k-2}(1+zt)^{k-2},
\qquad
\alpha_l=\frac{l(l-1)}{k(k-1)},
\]
\[
\theta_l=\frac{(z-1)^2a_{l-2}}{\alpha_l Z_l(z)},
\qquad
s_l=-\frac{\log\theta_l}{2(n-1)}.
\tag{3}
\]
Thus no limiting half-step clock is substituted for the actual one. citeturn342519view2turn342519view1

At layer \(1\), the corrected marginal is uniform and there is no prescribed nontrivial clock. For the information ledger, \(s_1\ge0\) can be any auxiliary time: all conclusions below are uniform in this choice. Indeed, the unconditional one-point initial law is uniform, and remains so under heat.

For the actual weights, take independent bits \(X_1,\ldots,X_n\), the first \(k\) with success probability \(p\), the others with probability \(q\), and define
\[
B_m=\sum_{i\ne j}
\Pr\!\left(\sum_{a\notin\{i,j\}}X_a=m\right),
\qquad
w_l=B_{l-1}-B_{l-2},
\quad B_{-1}=0.
\tag{4}
\]
These are precisely the actual count weights, not substitute Gaussian weights. citeturn241990view1

Here is the uniform estimate that drives (1).

### Theorem

Let
\[
\eta=\frac q4.
\]
There exist \(C_0,N_0<\infty\), depending only on \(c=19/20\), such that for every even \(n\ge N_0\) and every integer \(0\le r\le\eta k\),
\[
\boxed{
\begin{aligned}
|J_k(s_k)-J_{k-r}(s_{k-r})|
&\le C_0\left(\log(n+1)+\frac{r^2}{n}\right),\\
|F_k(s_k)-F_{k-r}(s_{k-r})|
&\le C_0\left(\log(n+1)+\frac{r^2}{n}\right).
\end{aligned}}
\tag{5}
\]

These are **prefix estimates**, not estimates obtained by differentiating a static entropy approximation.

Together with the actual-weight estimates proved in Section 6, they imply (1) for every even \(n\ge4\), after enlarging \(C\) to cover the finitely many \(n<N_0\).

---

## 2. The new tool: a determinantal Bayesian transport ledger

Introduce an auxiliary channel, for \(|S|=l\),
\[
T^G_l(S\mid A)=\frac{z^{|A\cap S|}}{Z_l(z)}.
\tag{6}
\]
It is a comparison device only; the variables in the theorem remain those of the actual heat channel.

Let
\[
\Lambda=I+(z-1)P,\qquad
\ell(S)=\log\det\Lambda_S.
\]

Cauchy–Binet gives
\[
\begin{aligned}
\mathbb E_\nu z^{|A\cap S|}
&=\det\!\left(U^*\operatorname{diag}
       (z^{\mathbf1_{\{i\in S\}}})U\right)\\
&=\det\bigl(I+(z-1)P_S\bigr)
=\det\Lambda_S.
\end{aligned}
\]
Therefore the Gibbs marginal and posterior are explicit:
\[
\gamma_l(S)=\frac{\det\Lambda_S}{Z_l(z)},
\tag{7}
\]
\[
\nu^G_{l,S}(A)
=\frac{\det P_A\,z^{|A\cap S|}}{\det\Lambda_S}.
\tag{8}
\]

In particular, the posterior is itself a projection DPP. If
\[
D_S=\operatorname{diag}\bigl(z^{\mathbf1_{\{i\in S\}}/2}\bigr),
\qquad V_S=D_SU,
\]
its kernel is
\[
K^{\mathrm{post}}_S
=V_S(V_S^*V_S)^{-1}V_S^*.
\tag{9}
\]
Taking a \(k\times k\) principal minor verifies (8).

Write
\[
\mathscr J_l=I_{\nu T^G_l}(A;S),\qquad
\mathscr F_l=D(\gamma_l\Vert u_l).
\]

For the actual heat law at \(s_l\), define
\[
\mathsf{Post}_l
=\mathbb E_{\mu_l(s_l)}
D\!\left(\nu^H_{l,S}\Vert\nu^G_{l,S}\right),
\qquad
\mathsf{Out}_l=D(\mu_l(s_l)\Vert\gamma_l).
\tag{10}
\]
Also put
\[
\delta m_l
=\mathbb E_H|A\cap S|-\mathbb E_G|A\cap S|,
\]
\[
v_l=\mathbb E_H\ell(S)-\mathbb E_G\ell(S).
\]

### Exact transport identity

For every \(2\le l\le k\),
\[
\boxed{
J_l(s_l)=\mathscr J_l+\mathsf{Post}_l+\beta\delta m_l-v_l,
}
\tag{11}
\]
\[
\boxed{
F_l(s_l)=\mathscr F_l+\mathsf{Out}_l+v_l.
}
\tag{12}
\]

To prove this, let \(d_l\) be the relative entropy between the heat and Gibbs **joint** laws. Their latent marginals agree, so
\[
d_l=\mathbb E_\nu
D(T^H_{l,s_l}(\cdot\mid A)\Vert T^G_l(\cdot\mid A)).
\]
The KL chain rule gives
\[
d_l=\mathsf{Out}_l+\mathsf{Post}_l.
\tag{13}
\]
Moreover,
\[
\log\frac{T^G_l(S\mid A)}{\gamma_l(S)}
=\beta|A\cap S|-\ell(S).
\]
Substitution in the definition of mutual information yields (11). Expanding \(D(\mu_l\Vert\gamma_l)\) yields (12).

The quantitative content, proved next, is that throughout
\[
(1-\eta)k\le l\le k,
\]
for all sufficiently large even \(n\),
\[
\boxed{
|\delta m_l|+|v_l|\le C,
\qquad
0\le\mathsf{Post}_l,\mathsf{Out}_l
\le\log(n+1)+C.
}
\tag{14}
\]

Thus the layer–clock discrepancy is isolated as a bounded energy correction plus an explicitly defined posterior KL term. Positivity of that term does **not** assert any sign for its adjacent-layer difference.

---

## 3. Why the exact coefficient clock supplies moment matching

Let
\[
X=|A\cap S|,\qquad R=l-X.
\]

Under the Gibbs channel,
\[
\Pr_G(X=j)
=\frac{\binom kj\binom k{l-j}z^j}{Z_l(z)}.
\tag{15}
\]

### 3.1 Gibbs variance and location

First,
\[
\operatorname{Var}_G X\le\frac k4.
\tag{16}
\]

Here is an elementary proof. A fixed-size weighted-subset law has nonpositive pair covariances. For two sites of weights \(a,b>0\), let \(e_j\) be the elementary symmetric coefficients of the remaining weights. With
\[
Z=e_l+(a+b)e_{l-1}+ab e_{l-2},
\]
direct calculation gives
\[
\operatorname{Cov}(\mathbf1_i,\mathbf1_j)
=\frac{ab}{Z^2}
\left(e_{l-2}e_l-e_{l-1}^2\right)\le0.
\]
The required coefficient log-concavity follows inductively under multiplication by \(1+wt\). If \(b_j=a_j+wa_{j-1}\), then
\[
\begin{aligned}
b_j^2-b_{j-1}b_{j+1}
={}&(a_j^2-a_{j-1}a_{j+1})\\
&+w(a_ja_{j-1}-a_{j-2}a_{j+1})\\
&+w^2(a_{j-1}^2-a_{j-2}a_j),
\end{aligned}
\]
and every term is nonnegative for a nonnegative log-concave sequence with no internal zeros. Summing the covariances over sites in \(A\) proves (16).

Let \(u_l\) be the unique root in \([0,l]\) of
\[
z(k-u)(l-u)=u(k-l+u).
\tag{17}
\]
The probability ratio in (15) is
\[
\frac{\Pr_G(X=j+1)}{\Pr_G(X=j)}
=\frac{z(k-j)(l-j)}{(j+1)(k-l+j+1)}.
\tag{18}
\]
Consequently, for
\[
B(u)=z(k-u)(l-u)-u(k-l+u),
\]
we have \(\mathbb E_G B(X)=0\). Since
\[
B'(u)\le-2k\qquad(0\le u\le l\le k),
\]
and \(B\) has quadratic coefficient \(z-1\),
\[
B(\mathbb E_GX)=-(z-1)\operatorname{Var}_G X.
\]
It follows that
\[
0\le\mathbb E_GX-u_l\le\frac{z-1}{8}.
\tag{19}
\]
Equation (18) also puts every mode within distance \(2\) of \(u_l\): at a mode \(m\), comparison with its two neighbors gives
\[
B(m)\le2k+1,\qquad B(m-1)\ge0,
\]
which, together with \(B'\le-2k\), proves the assertion.

The root in (17) has a useful exact expression. Put \(\lambda=l/k\) and
\[
A_z=\frac{z+1}{z-1}.
\]
Then
\[
u_l=\frac{k}{2}\bigl(\lambda+d(\lambda)\bigr),
\qquad
d(\lambda)=A_z-\sqrt{A_z^2-1+(1-\lambda)^2}.
\tag{20}
\]
At \(\lambda=1\),
\[
d(1)=c,\qquad \sqrt{A_z^2-1}=\frac{2b}{c}.
\]
Hence, for \(r=k-l\),
\[
\boxed{
\left|u_{k-r}-\left(pk-\frac r2\right)\right|
\le\frac{c\,r^2}{8bk}.
}
\tag{21}
\]

For \(0\le r\le\eta k\), \(\eta=q/4\), equations (19)–(21) show that the Gibbs mean and mode, and all four selected/unselected population counts around them, stay a fixed positive fraction of \(k\) away from their boundaries, once \(k\) is sufficiently large.

### 3.2 Actual heat moments

Conditional on \(A\), the heat law is uniform within each overlap orbit. Its \(R\)-coordinate has rates
\[
\lambda_R=(l-R)(k-R),\qquad
\mu_R=R(k-l+R),
\]
and starts at \(R=0\).

Its drift is \(kl-nR\), so exactly
\[
\mathbb E_HR=\frac l2(1-e^{-ns}),
\qquad
\mathbb E_HX=\frac l2(1+e^{-ns}).
\tag{22}
\]
For \(V(s)=\operatorname{Var}_H R\),
\[
V'(s)=-2nV(s)+\mathbb E_H(\lambda_R+\mu_R).
\]
The transitions changing \(R\) are a subset of the \(l(n-l)\) possible exchanges. Therefore
\[
\boxed{
\operatorname{Var}_H R
\le\frac{l(n-l)}{2n}
\le\frac n8.
}
\tag{23}
\]

### 3.3 Reconstructing the coefficient identity

Let
\[
m_l=\mathbb E_GX,\qquad
\sigma_l^2=\operatorname{Var}_G X,\qquad
a_l=\frac{2m_l-l}{l}.
\]
The exact identity needed here is
\[
\boxed{
\theta_l
=a_l^2+
\frac{4(n-1)\sigma_l^2-l(n-l)(1-a_l^2)}
     {nl(l-1)}.
}
\tag{24}
\]

For completeness, choose distinct \(i_1,i_2\in A\) and
\(j_1,j_2\notin A\), and test
\[
(\mathbf1_{i_1\in S}-\mathbf1_{j_1\in S})
(\mathbf1_{i_2\in S}-\mathbf1_{j_2\in S}).
\]
Conditional on \(X\), its expectation is
\[
\frac{\mathbb E[X(X-1)+(l-X)(l-X-1)]}{k(k-1)}
-\frac{2\mathbb E[X(l-X)]}{k^2}.
\]
On the other hand, combining the four coefficient formulas gives
\[
\frac{(z-1)^2a_{l-2}}{Z_l}.
\]
Dividing by \(\alpha_l\), and substituting
\(m_l=l(1+a_l)/2\), proves (24).

The clock is positive without an asymptotic argument. Indeed, with
\(f(t)=(1+t)(1+zt)\),
\[
\alpha_lZ_l
=[t^{l-2}]f^{k-2}
\left((f')^2+\frac{ff''}{k-1}\right).
\]
The bracket has nonnegative coefficients and constant coefficient
\[
(z+1)^2+\frac{2z}{k-1}>(z-1)^2.
\]
Thus \(0<\theta_l<1\).

In the stated central band, \(a_l\) is uniformly bounded away from both \(0\) and \(1\). By (16) and (24),
\[
|\theta_l-a_l^2|\le\frac Cn.
\tag{25}
\]
But the **actual** clock gives
\[
e^{-ns_l}=\theta_l^{\,n/[2(n-1)]}.
\]
On the resulting fixed compact interval of positive \(\theta_l\),
\[
\left|\theta_l^{\,n/[2(n-1)]}-a_l\right|
\le\frac Cn.
\]
Combining this with (22) proves
\[
\boxed{
|\mathbb E_HX-\mathbb E_GX|\le C.
}
\tag{26}
\]

This is a finite-\(n\), coefficient-clock comparison. It does not assume that the adjacent clock increment is already close to a half-step.

---

## 4. Determinantal curvature pays the information-transport error

### 4.1 A dimension-free row bound

For \(T\subset[n]\), let \(M\) be the Schur complement of \(\Lambda_T\) in \(\Lambda\), indexed by \(T^c\). Since
\[
I\preceq\Lambda\preceq zI,
\]
we also have
\[
I\preceq M\preceq zI.
\]

For distinct \(i,j\notin T\), define
\[
\delta_{ij}\ell(T)
=\ell(T+i+j)-\ell(T+i)-\ell(T+j)+\ell(T).
\]
The determinant formula for a \(2\times2\) Schur complement yields
\[
\delta_{ij}\ell(T)
=\log\left(1-\frac{|M_{ij}|^2}{M_{ii}M_{jj}}\right)\le0.
\tag{27}
\]
The quantity inside the logarithm is at least \(z^{-2}\). Using
\(-\log(1-x)\le x/(1-x)\),
\[
|\delta_{ij}\ell(T)|\le z^2|M_{ij}|^2.
\]
Consequently,
\[
\boxed{
\sum_{j\ne i}|\delta_{ij}\ell(T)|\le z^4.
}
\tag{28}
\]
Also,
\[
0\le\ell(T+i)-\ell(T)\le\beta.
\tag{29}
\]

The key point is that the row sum in (28) has **no factor of \(n\)**.

### 4.2 Averaging over two populations

For fixed \(A\), average \(\ell(S)\) over sets selecting \(h\) points from \(A\) and \(r\) from \(A^c\). Then average over \(A\sim\nu\); call the result \(a(h,r)\).

Coupling uniform subsets by adding one or two uniformly chosen remaining points gives
\[
|\Delta_h^2a(h,r)|\le\frac{z^4}{k-h-1},
\]
\[
|\Delta_r^2a(h,r)|\le\frac{z^4}{k-r-1},
\]
\[
|\Delta_h\Delta_ra(h,r)|
\le\frac{z^4}{\max(k-h,k-r)},
\tag{30}
\]
whenever the indicated differences are defined.

For example, the first inequality averages (27) over two distinct remaining points of \(A\). Summing first over the second point and applying (28) gives the denominator \(k-h-1\). The mixed inequality follows in the same way from the two distinct populations.

For fixed total \(l\), set
\[
a_l(r)=a(l-r,r).
\]
Its first differences satisfy
\[
|\Delta a_l(r)|\le\beta.
\tag{31}
\]
Its second differences are \(O(1/n)\) in every fixed interior population rectangle. An explicit verification uses a base set with \(l-r-1\) points of \(A\) and \(r-1\) of \(A^c\), and two additional points from each population. The second difference is the expectation of
\[
\delta_{a_1a_2}\ell
+\delta_{b_1b_2}\ell
-2\delta_{a_1b_1}\ell,
\]
so (28) proves the assertion.

### 4.3 The finite Taylor estimate being used

Suppose a sequence \(f\) has globally bounded first differences and
\[
|\Delta^2f(j)|\le C/n
\]
within distance \(\delta n\) of an interior integer \(j_0\), where \(\delta>0\) is fixed.

Summing first differences gives, locally,
\[
\left|f(j)-f(j_0)-(j-j_0)\Delta f(j_0)\right|
\le\frac Cn\bigl((j-j_0)^2+|j-j_0|\bigr).
\]
Outside that neighborhood, the global Lipschitz bound gives the same type of bound, because
\[
|j-j_0|\le\frac{(j-j_0)^2}{\delta n}.
\]

It follows that if two random indices have variances \(O(n)\), means within \(O(1)\) of \(j_0\), and means differing by \(O(1)\), their expectations of \(f\) differ by \(O(1)\).

Apply this to \(a_l\), using (16), (23), (26), and the bulk location from Section 3. We obtain
\[
\boxed{
|\mathbb E_H\ell(S)-\mathbb E_G\ell(S)|\le C.
}
\tag{32}
\]

This proves the bounded evidence-transport error in (14).

### 4.4 Bounding the remaining posterior KL

Let \(p_l(r)\) and \(q_l(r)\) be the heat and Gibbs laws of \(R\). Uniformity within overlap orbits gives exactly
\[
d_l=D(p_l\Vert q_l).
\tag{33}
\]

Let \(r_*\) be a mode of \(q_l\). Section 3 shows that it is in a fixed interior region and differs from both overlap means by \(O(1)\).

Now
\[
\log q_l(r)
=\log\binom kr+\log\binom k{l-r}
+\beta(l-r)-\log Z_l.
\]
Its second differences are \(O(1/n)\) near \(r_*\). At the mode, its adjacent first differences bracket zero; therefore those first differences have size \(O(1/n)\). Since
\[
q_l(r_*)\ge\frac1{n+1},
\]
finite Taylor summation gives a local quadratic upper bound on
\(-\log q_l(r)\).

Globally,
\[
-\log q_l(r)\le n(\beta+\log2),
\]
because every numerator in (15) is at least \(1\), while
\(Z_l\le2^nz^n\). Outside the fixed interior neighborhood this global bound is absorbed by \((r-r_*)^2/n\). Thus, for all admissible \(r\),
\[
-\log q_l(r)
\le\log(n+1)+C\left(1+\frac{(r-r_*)^2}{n}\right).
\tag{34}
\]
Equations (23) and (26) imply
\[
\mathbb E_H(R-r_*)^2\le Cn.
\]
Using nonnegativity of Shannon entropy,
\[
\boxed{
D(p_l\Vert q_l)
\le\mathbb E_H[-\log q_l(R)]
\le\log(n+1)+C.
}
\tag{35}
\]

Finally, (13), (26), and (32) prove all of (14).

This completes the quantitative posterior-transport tool.

---

## 5. Uniform central regularity of the Gibbs comparison

### 5.1 Fourier particle–hole symmetry

Let
\[
D=\operatorname{diag}((-1)^j).
\]
For the half-density Fourier projection,
\[
DPD^*=I-P.
\tag{36}
\]
Complementary minors of the full Fourier unitary then give
\[
\nu(A^c)=\nu(A).
\tag{37}
\]

Also,
\[
\Lambda^{-1}=z^{-1}D\Lambda D^*,
\qquad
\det\Lambda=z^k.
\]
Jacobi’s complementary-minor identity yields
\[
\boxed{
\ell(S)=\beta(|S|-k)+\ell(S^c).
}
\tag{38}
\]

Define
\[
g(h,r)=\beta h-a(h,r).
\]
Using (37) to interchange the two populations, and then (38), gives
\[
\boxed{
g(h,r)=g(k-r,k-h).
}
\tag{39}
\]

By (29), \(g\) is globally \(\beta\)-Lipschitz in each coordinate. Its pure and mixed second differences are \(O(1/n)\) in the fixed interior regions under consideration.

### 5.2 Gibbs information has a quadratic central prefix

The Gibbs information is exactly
\[
\mathscr J_l
=\mathbb E_G\bigl[\beta X-\ell(S)\bigr]
=\mathbb E_G g(X,l-X).
\tag{40}
\]
The finite Taylor estimate of Section 4, together with the variance bound, shows that replacing \(X\) by an integer nearest its mean changes (40) by \(O(1)\).

Choose an integer \(h_0\) nearest \(pk\), and put \(r_0=k-h_0\). Consider
\[
b_t=g(h_0+t,r_0+t).
\]
Equation (39) says \(b_t=b_{-t}\). Equation (30) implies
\[
|b_{t+1}-2b_t+b_{t-1}|\le C/n
\]
throughout a fixed central range. For clarity, the diagonal second difference is controlled by
\[
(E_hE_r-I)^2
=\Delta_h^2+2E_h\Delta_h\Delta_r+E_h^2\Delta_r^2.
\]
Evenness controls the first increment at \(t=0\); summing the second-difference bound gives
\[
|b_t-b_0|\le Ct^2/n.
\tag{41}
\]

At layer \(k-r\), (19) and (21) place the two population means within
\[
O\!\left(1+\frac{r^2}{n}\right)
\]
of
\[
\left(pk-\frac r2,\ qk-\frac r2\right).
\]
For even \(r\), this is the diagonal path in (41). For odd \(r\), one extra coordinate step costs at most \(\beta\). The global Lipschitz bound pays the displacement from the exact means.

Hence
\[
\boxed{
|\mathscr J_k-\mathscr J_{k-r}|
\le C\left(1+\frac{r^2}{n}\right)
}
\tag{42}
\]
uniformly for \(0\le r\le\eta k\).

Combining (42) with (11) and (14) proves the information part of (5).

### 5.3 The marginal-entropy comparison, without a radial assumption

For the Gibbs marginal,
\[
\mathscr F_l
=\log\binom nl-\log Z_l+\beta m_l-\mathscr J_l.
\tag{43}
\]

We need only a crude, uniform normalizer estimate—not an entropy local limit.

Let \(\pi_l=\pi_l(a_*,c)\) be the actual count probability. Its generating polynomial gives exactly
\[
\pi_l=b^kz^{-l/2}Z_l.
\tag{44}
\]
For \(l=k-r\),
\[
\left|
\log Z_l-\log Z_k+\frac{\beta r}{2}
\right|
\le C\left(\log(n+1)+\frac{r^2}{n}\right).
\tag{45}
\]

Here is a direct proof. If \(Y\sim\operatorname{Bin}(k,p)\), then, for an integer \(j\) in a fixed interior range,
\[
\Pr(Y=j)
\ge\frac1{k+1}
\exp\!\left[-k\,\operatorname{kl}(j/k,p)\right].
\]
Indeed, \(j\) is a mode of \(\operatorname{Bin}(k,j/k)\), so its probability there is at least \(1/(k+1)\); changing the parameter gives the displayed identity. On the fixed interior range,
\[
\operatorname{kl}(x,p)\le C(x-p)^2.
\]
Apply this to independent \(\operatorname{Bin}(k,p)\) and
\(\operatorname{Bin}(k,q)\), choosing counts summing to \(k-r\), each within \(r/2+1\) of its mean. Thus
\[
\pi_{k-r}\ge(k+1)^{-2}
\exp\!\left[-C\left(1+\frac{r^2}{k}\right)\right].
\]
The same estimate at \(r=0\), together with \(\pi_l\le1\), bounds
\(|\log\pi_{k-r}-\log\pi_k|\). Equation (44) proves (45).

Furthermore,
\[
\left|\log\binom n{k-r}-\log\binom nk\right|
\le C\frac{r^2}{n},
\tag{46}
\]
by summing
\[
\log\frac{k+j+1}{k-j},\qquad 0\le j<r.
\]
And (19), (21) give
\[
m_{k-r}-m_k=-\frac r2+
O\!\left(1+\frac{r^2}{n}\right).
\tag{47}
\]

Substituting (42), (45)–(47) in (43), the two linear
\(-\beta r/2\) terms cancel:
\[
|\mathscr F_k-\mathscr F_{k-r}|
\le C\left(\log(n+1)+\frac{r^2}{n}\right).
\tag{48}
\]
Finally, (12) and (14) prove the second part of (5).

This establishes both uniform central prefix estimates without invoking a static-entropy derivative or S16’s radial remainder.

---

## 6. Paying the actual weights and every complementary layer

The actual \(B_m\) admit the exact factorization
\[
\sum_{m=0}^{n-
