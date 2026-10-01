PROVED

The strict positive lower bound is sufficient. Both the **full-observed-past intensity** and the **common-filtration Poisson completion** hold. Moreover, the uniqueness issue can be resolved more strongly than by assuming an invariant coupling: there is a conull set of iid Poisson inputs on which **every** solution path from the empty configuration is the same solution.

## Theorem

Let \(\Gamma\) be countable, let \(S\) be finite and nonempty, and let \(W=\Gamma\times S\), with left translation on the first coordinate. Suppose \(Q\) is an equivariant self-adjoint operator satisfying
\[
cI\le Q\le I,\qquad c>0.
\]
Use \(Z,E,Y,t_s,A_s,b_s\) as in the question.

Write
\[
\mathcal H_t^0=\sigma\bigl(Y_r(x):x\in W,\ 0\le r\le t\bigr),
\]
and let \(\mathcal H\) be its completed right-continuous augmentation.

Then, for each \(x\) and deterministic \(s>0\),
\[
\mathbb E\!\left[1_{\{x\in Z,E_x>s\}}\mid\mathcal H^0_{s-}\right]
=b_s(x,Y_{s-})\quad\text{a.s.}                                      \tag{1}
\]
The right side is predictable and is the compensator density of \(Y(x)\) in \(\mathcal H\).

There is an equivariant independent extension carrying a complete right-continuous filtration \(\mathcal G\supseteq\mathcal H\) and a \(\mathcal G\)-Poisson random measure \(N\) on
\[
W\times(0,\infty)\times(0,1]
\]
with deterministic intensity
\[
\nu(dx\,ds\,du)=\#_W(dx)\,ds\,du,
\]
such that \((Y,N)\) is jointly invariant and
\[
Y_t(x)=1\left\{\exists(s,u)\in N_x:
0<s\le t,\ u\le b_s(x,Y_{s-})\right\}.                              \tag{2}
\]
In particular, the entire coordinate processes \(N_x\) are mutually independent and identically distributed, and their future increments are independent of the **common** \(\mathcal G\)-past.

There is a measurable equivariant nonanticipating map \(N\mapsto X(N)\) solving (2). On one noise-only conull set, every coordinatewise càdlàg configuration-valued solution of (2) from \(\varnothing\) equals \(X(N)\), without any invariance or adaptation assumption on the competing path. Consequently,
\[
Y=X(N),\qquad Z=\bigcup_{k\ge1}X_k(N),
\]
so the path and terminal DPP are factors of iid.

If the desired mark space is \((0,\infty)\), append an independent PRM on \(u>1\). Those additional points never affect (2).

## 1. Shorting identities and continuity

For a positive operator \(aI\le A\le I\), let \(D_\eta\) be the coordinate projection onto \(\ell^2(\eta)\), and put
\[
C_\eta(A)=D_\eta A D_\eta+I-D_\eta,
\]
\[
B_\eta(A)
=A-AD_\eta C_\eta(A)^{-1}D_\eta A.                                 \tag{3}
\]
The inverse exists because \(C_\eta(A)\ge\min(a,1)I\).

Quadratic minimization gives
\[
\langle B_\eta(A)v,v\rangle
=\inf_{w\in\ell^2(\eta)}\langle A(v-w),v-w\rangle.                    \tag{4}
\]
Indeed, the minimizer solves
\[
D_\eta A D_\eta w=D_\eta Av
\]
on \(\ell^2(\eta)\); substitution yields (3). Since \(A^{1/2}\) is bounded below, \(A^{1/2}\ell^2(\eta)\) is closed. Thus \(B_\eta(A)\) is exactly the shorted operator appearing in the question.

In particular,
\[
a(I-D_\eta)\le B_\eta(A)\le A\le I.                                \tag{5}
\]
The lower bound follows by replacing the quadratic form in (4) by \(a\|v-w\|^2\). The operator kills \(\ell^2(\eta)\). Hence
\[
b_A(x,\eta)=0\quad(x\in\eta),\qquad
a\le b_A(x,\eta)\le1\quad(x\notin\eta).
\]
Also, \(B_\eta(A)\) decreases when \(\eta\) increases.

For every finite \(T\),
\[
a_T I\le A_s\le I\quad(0\le s\le T),\qquad
a_T=\frac{e^{-T}c}{1-(1-e^{-T})c}>0.                               \tag{6}
\]
This follows by applying the increasing scalar function
\[
q\longmapsto \frac{e^{-s}q}{1-(1-e^{-s})q}
\]
to the spectrum of \(Q\). The map \(s\mapsto A_s\) is norm continuous.

If \(\eta_n\to\eta\) coordinatewise, then \(D_{\eta_n}\to D_\eta\) strongly. With a common positive lower bound, strong convergence of the relevant operators implies strong convergence of \(C_n\) and their inverses, using
\[
C_n^{-1}-C^{-1}=C_n^{-1}(C-C_n)C^{-1}.
\]
Equation (3) then gives strong convergence of the shortings. In particular, \(b_s(x,\eta)\) is jointly Borel in \((s,\eta)\), and continuous under coordinatewise configuration convergence at each finite time.

These statements apply to arbitrary infinite configurations.

## 2. The complete observed past

### Finite histories

The defining DPP inclusion probabilities show that restriction to a finite \(F\subset W\) has kernel \(Q^F=P_FQP_F\) acting on \(\ell^2(F)\). They also show directly that
\[
\mathbb P(B\subseteq Y_s)
=t_s^{|B|}\det Q[B]
=\det(t_sQ)[B]
\]
for every finite \(B\). Thus thinning gives kernel \(t_sQ\). The underlying discrete DPP characterization and positive-contraction construction are recorded in Lyons’s *Determinantal Probability: Basic Properties and Conjectures*, equation (1.1) and Section 2.3. :chatgpt-content-reference{index="0"}

Fix \(s>0\). In a finite \(F\), let \(\eta\) be the sites born before \(s\), with observed birth times \(r_y<s\). For a terminal set \(T_0\supseteq\eta\), the history likelihood contains the factor
\[
\mathbb P(Z\cap F=T_0)\,
e^{-s|T_0\setminus\eta|}
\prod_{y\in\eta}e^{-r_y}.                                         \tag{7}
\]
The factor involving the actual observed times is independent of \(T_0\). Thus this calculation conditions on the **whole finite temporal history**, not just the configuration.

Writing \(\mu_s^F\) for exact configuration probabilities, summing (7) gives, for \(x\notin\eta\),
\[
\mathbb E\!\left[1_{\{x\in Z,E_x>s\}}\mid\mathcal H^F_{s-}\right]
=\frac{e^{-s}}{t_s}
  \frac{\mu_s^F(\eta\cup\{x\})}{\mu_s^F(\eta)}.                     \tag{8}
\]

Set \(K=t_sQ^F\). Its spectrum lies in \([t_sc,t_s]\subset(0,1)\). With \(L=K(I-K)^{-1}\),
\[
\mu_s^F(\eta)=\det(I-K)\det L[\eta].                               \tag{9}
\]
For completeness, the inclusion determinants give the generating polynomial
\[
\mathbb E\prod_{x\in F}z_x^{Y_s(x)}
=\det(I-K+K\operatorname{diag}z).
\]
Factor out \(I-K\) and expand the remaining determinant by principal minors to obtain (9). This is also Lyons’s equation (2.12); its finite-set and \(\|K\|<1\) hypotheses hold here. All determinants in the denominator are positive. :chatgpt-content-reference{index="1"}

The ratio in (8) is a Schur complement. By homogeneity of shorting,
\[
\mathbb E\!\left[1_{\{x\in Z,E_x>s\}}\mid\mathcal H^F_{s-}\right]
=b_{A_s^F}(x,Y_{s-}\cap F),                                      \tag{10}
\]
where
\[
A_s^F=e^{-s}Q^F(I-t_sQ^F)^{-1}.
\]
For an already-born \(x\), both sides are zero.

### Moving finite windows

Choose arbitrary finite \(F_n\uparrow\Gamma\), and write \(W_n=F_n\times S\), \(P_n=P_{W_n}\). Extend
\[
Q_n=P_nQP_n,\qquad A_{s,n}=f_s(Q_n)
\]
by zero outside \(W_n\). Then \(Q_n\to Q\) strongly. The expansion
\[
A_{s,n}=e^{-s}\sum_{k\ge0}t_s^kQ_n^{k+1}
\]
has uniformly small tails for \(s\le T\), so \(A_{s,n}\to A_s\) strongly. Also
\[
A_{s,n}\ge a_TP_n.
\]

Fix an **arbitrary** \(\eta\subseteq W\), and let
\[
D_n=D_{\eta\cap W_n},\quad D=D_\eta,\quad
C_n=D_nA_{s,n}D_n+I-D_n.
\]
Then
\[
C_n\longrightarrow C=DA_sD+I-D
\]
strongly, with \(C_n\ge\min(a_T,1)I\). Therefore
\[
\begin{aligned}
&A_{s,n}-A_{s,n}D_nC_n^{-1}D_nA_{s,n}\\
&\hspace{20mm}\longrightarrow
A_s-A_sDC^{-1}DA_s
\end{aligned}                                                     \tag{11}
\]
strongly. Consequently,
\[
b_{A_s^{[n]}}(x,\eta\cap W_n)\longrightarrow b_s(x,\eta).            \tag{12}
\]
This handles both moving operators and moving constraints.

For fixed \(s,x\), the finite observed-past sigma-fields increase to \(\mathcal H^0_{s-}\), because \(W\) is countable. Apply the upward conditional-expectation theorem to the bounded random variable
\[
R_x(s)=1_{\{x\in Z,E_x>s\}}.
\]
The exact theorem used is Lyons’s *Lecture Notes on Martingales*, Theorem 35.6: conditional expectations of an integrable variable converge along increasing sigma-fields to the conditional expectation on their generated union. :chatgpt-content-reference{index="2"}

Combining (10) and (12), with \(\eta=Y_{s-}\), proves (1).

There is no conditioning on a zero-probability exact infinite configuration and no substitution of finite-dimensional convergence for conditioning on the entire observed history.

## 3. Actual compensation and usual augmentation

The right side of (1) is predictable: \(Y_{s-}\) has predictable coordinates, \(W\) is countable, and \(b\) is jointly Borel.

Temporarily use the larger filtration that reveals \(Z\) at time zero but reveals the exponential clocks only through their censored histories. Exponential memorylessness gives the martingale
\[
Y_t(x)-\int_0^t1_{\{x\in Z,E_x\ge r\}}\,dr.
\]
Indeed, conditional on survival to time \(a\), both the expected birth increment by \(b\) and the expected integrated survival indicator on \((a,b]\) equal \(1-e^{-(b-a)}\). Independence of the clocks makes the same calculation valid conditional on all other clock histories and \(Z\).

Thus, for every bounded nonnegative raw-\(\mathcal H\)-predictable \(U\) supported in a finite time interval,
\[
\begin{aligned}
\mathbb E\int U_s\,dY_s(x)
&=\mathbb E\int U_sR_x(s)\,ds\\
&=\mathbb E\int U_sb_s(x,Y_{s-})\,ds. 
\end{aligned}                                                     \tag{13}
\]
The second equality uses (1) at deterministic \(s\) and Tonelli. This proves compensation, rather than merely a fixed-time posterior identity.

The augmentation issue is handled by the following lemma.

**Augmentation lemma.** Suppose \(M\) is a càdlàg martingale in a raw filtration \(\mathcal F^0\), dominated on each bounded time interval by an integrable random variable. Then \(M\) remains a martingale in
\[
\mathcal F_t=\bigcap_{r>t}(\mathcal F_r^0\vee\mathcal N).
\]

**Proof.** Choose \(a_n\downarrow a\), with \(a_n<b\). Reverse conditional-expectation convergence gives
\[
\begin{aligned}
\mathbb E[M_b\mid\mathcal F_a]
&=\lim_n\mathbb E[M_b\mid\mathcal F_{a_n}^0\vee\mathcal N]\\
&=\lim_nM_{a_n}=M_a.
\end{aligned}
\]
The last limit follows from right continuity, also in \(L^1\) by domination. The reverse convergence theorem used here is Lyons’s Theorem 35.9; its hypotheses are decreasing sigma-fields and an integrable terminal variable. :chatgpt-content-reference{index="3"}

Apply this lemma to \(Y_t(x)-\int_0^t\lambda_x(s)\,ds\), which is bounded in absolute value by \(1+T\) on \([0,T]\). Hence the compensator remains valid in \(\mathcal H\).

Furthermore, for \(s>0\),
\[
\mathcal H_{s-}=\mathcal H^0_{s-}\vee\mathcal N.
\]
For the nontrivial inclusion, between any \(r<s\) and \(s\), choose \(q\) with \(r<q<s\); then \(\mathcal H_r\subseteq\mathcal H_q^0\vee\mathcal N\).

No triviality of a right germ is assumed. No globally locally finite jump process is required: compensation is checked on finite site sets, while predictable test variables may depend on **all** sites.

## 4. Progressive Poisson completion

Independently add iid \(V_x\sim U(0,1)\) and independent unit-intensity PRMs \(M_x\) on \((0,\infty)\times(0,1]\). The auxiliary intensities are sigma-finite, so they meet the existence hypothesis of Last–Penrose, *Lectures on the Poisson Process*, Theorem 3.6. :chatgpt-content-reference{index="4"}

Write \(\tau_x=E_x\) when \(x\in Z\), and \(\tau_x=\infty\) otherwise. Define the raw filtration
\[
\mathcal K_t^0
=\sigma\!\left(
Y_r(x),\,V_xY_r(x),\,M_x((0,r]\times B):
x\in W,\ r\le t,\ B\text{ a rational interval}
\right),                                                         \tag{14}
\]
and let \(\mathcal G\) be its usual augmentation.

Thus \(V_x\) is revealed only when \(x\) is born.

### Preservation of the unmarked intensity

For every bounded \(\mathcal K_a^0\)-measurable \(F\),
\[
\mathbb E[F\mid\sigma(Y_r:r\ge0)]
\quad\text{is }\mathcal H_a^0\text{-measurable}.                    \tag{15}
\]
For cylinder functions of the generators in (14), integrate the independent \(V\)'s and \(M\)'s conditional on the whole \(Y\)-path. The revealing masks involve only \(Y\) through \(a\). A monotone-class argument proves (15) generally.

The unmarked compensated martingale is a function of \(Y\). Testing its increment against \(F\) and using (15) shows that it remains a \(\mathcal K^0\)-martingale.

### Real marked compensation

At a real birth at \((x,s)\), put a point with mark
\[
u=\lambda_x(s)V_x,
\]
and call the resulting measure \(L\). By (5)–(6), \(\lambda_x(s)>0\) at each finite real birth.

For a predictable elementary test
\[
H_s(u)=F1_{(a,b]}(s)1_B(u),
\qquad F\in\mathcal K_a^0,
\]
the event \(\{\tau_x>a\}\) ensures that \(F\) has not seen \(V_x\). Therefore, with
\[
q_B(l)=\int_0^1 1_B(lv)\,dv\qquad(l>0),
\]
independence of \(V_x\) gives
\[
\begin{aligned}
&\mathbb E\!\left[
F1_{\{a<\tau_x\le b\}}1_B(\lambda_x(\tau_x)V_x)
\right]\\
&\qquad=
\mathbb E\!\left[
F1_{\{a<\tau_x\le b\}}q_B(\lambda_x(\tau_x))
\right]\\
&\qquad=
\mathbb E\int_a^b F\lambda_x(s)q_B(\lambda_x(s))\,ds\\
&\qquad=
\mathbb E\int_a^b F\int_0^{\lambda_x(s)}1_B(u)\,du\,ds.
\end{aligned}
\]
The middle equality uses the preserved unmarked compensator. Predictable monotone class now gives real marked compensator
\[
1_{\{0<u\le\lambda_x(s)\}}\,ds\,du.                               \tag{16}
\]

This is a direct proof for the non-Poisson real birth process; it does not misapply a Poisson independent-marking theorem.

### Virtual proposals

Define
\[
N_x(ds\,du)
=L_x(ds\,du)+1_{\{u>\lambda_x(s)\}}M_x(ds\,du).                     \tag{17}
\]
The entire \((Y,V)\) is independent of \(M\), so \(M\)'s future increments are independent of the raw common past. Predictable restriction gives virtual compensator
\[
1_{\{\lambda_x(s)<u\le1\}}\,ds\,du.
\]
Together with (16), this gives deterministic compensator \(ds\,du\).

For finite \(F\subset W\) and \(T<\infty\), all relevant counts are dominated by
\[
|F|+\sum_{x\in F}M_x((0,T]\times(0,1]),
\]
which is integrable. Their compensated processes are càdlàg. Applying the augmentation lemma, first to a countable generating algebra of mark sets and then by monotone class, preserves these compensators in \(\mathcal G\).

Thus the completion has deterministic compensator in the **common usual filtration**, despite infinite global jump rate.

## 5. Joint Poisson law, not merely coordinate intensities

On finite site sets, point times are almost surely distinct. Conditional on \(Z\), real birth times are independent continuous exponentials. The independent diffuse \(M\)-times do not coincide with one another or with real times.

Fix finite \(F\), \(0\le t<T\), and bounded deterministic \(h\ge0\) supported in
\[
F\times(t,T]\times(0,1].
\]
For \(t\le r\le T\), put
\[
Z_r^h=
\exp\!\left[
-\int_{F\times(t,r]\times(0,1]}h\,dN
+\int_{F\times(t,r]\times(0,1]}(1-e^{-h})\,d\nu
\right].
\]
The finite-jump product rule, using the absence of simultaneous point times, gives
\[
dZ_r^h
=\int Z_{r-}^h(e^{-h(x,r,u)}-1)(N-\nu)(dx\,dr\,du).
\]
The integrand is \(\mathcal G\)-predictable and bounded on this window, while
\[
0\le Z_r^h\le e^{|F|(T-t)}.
\]
Compensation therefore makes \(Z^h\) a true \(\mathcal G\)-martingale. Hence
\[
\mathbb E\!\left[e^{-\int h\,dN}\mid\mathcal G_t\right]
=\exp\!\left[-\int(1-e^{-h})\,d\nu\right].                         \tag{18}
\]

Taking \(h\) simple on finitely many disjoint site/time/mark cells proves that their future counts are independent Poisson variables, with joint law independent of \(\mathcal G_t\). Approximation and finite-site exhaustion prove the full common-filtration PRM assertion.

The distributional characterization is Last–Penrose Theorem 3.9. Importantly, its distributional statement is not being substituted for the filtration claim: the conditional identity (18) proves that additional claim. :chatgpt-content-reference{index="5"}

Every real point lies below \(\lambda\), and every virtual point lies above it. Since \(b_s(x,\eta)=0\) on occupied sites, (17) gives (2). The construction commutes with translations, so \((Y,N)\) is jointly invariant.

There is a genuine anticipative pitfall, but it is not present here: for a singleton \(W\) and \(Q=I\), revealing \(V\) initially would reveal the mark of the future first point. The resulting process would not be a PRM relative to that initially enlarged filtration. Filtration (14) specifically avoids this.

## 6. Discrepancy estimate for infinite configurations

Fix \(aI\le A\le I\), let \(\eta,\xi\subseteq W\), and set
\[
C=\eta\cap\xi,\qquad \Delta=\eta\triangle\xi,\qquad B=B_C(A).
\]
For \(J=\eta\setminus C\), nested minimization in (4) gives
\[
B-B_\eta(A)
=BD_J(D_JBD_J+I-D_J)^{-1}D_JB
\le a^{-1}BD_JB.                                                 \tag{19}
\]
The inverse is valid because \(B\ge a(I-D_C)\) and \(J\cap C=\varnothing\). This argument works for infinite \(J\): minimizing successively over \(\ell^2(C)\) and \(\ell^2(J)\) is minimizing over their coordinate direct sum.

Applying (19) also to \(\xi\setminus C\) yields
\[
|b_A(x,\eta)-b_A(x,\xi)|
\le a^{-1}\sum_{y\in\Delta}|B(x,y)|^2.                            \tag{20}
\]

Suppose now that \(A\) is equivariant and \((\eta,\xi)\) is jointly invariant. Reindexing \(g\mapsto g^{-1}\) under the group action gives
\[
\begin{aligned}
&\sum_{i,j\in S}\sum_{g\in\Gamma}
\mathbb E\!\left[
1_{\{(g,j)\in\Delta\}}|B((e,i),(g,j))|^2
\right]\\
&\quad=
\sum_{j\in S}\mathbb E\!\left[
1_{\{(e,j)\in\Delta\}}
\sum_{g\in\Gamma,i\in S}|B((g^{-1},i),(e,j))|^2
\right]\\
&\quad\le\sum_{j\in S}\mathbb P((e,j)\in\Delta).
\end{aligned}
\]
The last inequality uses \(\|B\delta_{(e,j)}\|^2\le1\); Tonelli justifies the sums. Therefore
\[
\sum_{i\in S}\mathbb E
|b_A((e,i),\eta)-b_A((e,i),\xi)|
\le a^{-1}\sum_{i\in S}
\mathbb P((e,i)\in\eta\triangle\xi).                              \tag{21}
\]

This verifies the precise use of joint invariance and finite \(S\).

## 7. Strong construction and the exact uniqueness class

On canonical iid PRM noise, define the absorbing first-acceptance map
\[
\Phi(U)_t(x)=
1\left\{\exists(s,u)\in N_x:
0<s\le t,\ u\le b_s(x,U_{s-})\right\}.                            \tag{22}
\]
This is a binary path, not a count of all accepted proposals. Local finiteness at each site makes it well-defined. Rational left approximations to \(U_{s-}\) show measurability; the map is nonanticipating and equivariant.

Set
\[
X^0\equiv\varnothing,\qquad X^{n+1}=\Phi(X^n).
\]
Every iterate is adapted, nondecreasing in time, and coordinatewise càdlàg. Their joint laws are invariant.

If \(\Phi(U)(x)\) and \(\Phi(V)(x)\) differ anywhere on \([0,t]\), some proposal through \(t\) has different acceptance indicators. Hence
\[
\begin{aligned}
&1_{\{\Phi(U)(x)|_{[0,t]}\ne\Phi(V)(x)|_{[0,t]}\}}\\
&\quad\le
\int_0^t\int_0^1
\left|
1_{\{u\le b_s(x,U_{s-})\}}
-1_{\{u\le b_s(x,V_{s-})\}}
\right|N_x(ds\,du).
\end{aligned}                                                     \tag{23}
\]

Fix \(T\), write \(m=|S|\), and define
\[
d_n(t)=\sum_{i\in S}
\mathbb P\!\left(
X^{n+1}(e,i)|_{[0,t]}\ne X^n(e,i)|_{[0,t]}
\right),\qquad t\le T.
\]
PRM compensation in (23), followed by (21), gives
\[
d_0(t)\le m,\qquad
d_n(t)\le a_T^{-1}\int_0^t d_{n-1}(r)\,dr.
\]
Induction yields
\[
d_n(t)\le m\,\frac{(t/a_T)^n}{n!}.                               \tag{24}
\]
Thus \(\sum_n d_n(T)<\infty\). Tail union bounds show that successive iterates eventually agree as entire coordinate paths on \([0,T]\). By invariance and countability, this holds simultaneously at every site and every integer horizon, on a noise-only conull event.

The deterministic order structure is crucial. Since \(b\) is antitone,
\[
U\le V\implies\Phi(U)\ge\Phi(V).
\]
Consequently,
\[
X^{2n}\le X^{2n+2}\le X^{2n+3}\le X^{2n+1}.                       \tag{25}
\]
Define \(X\) as the increasing limit of the even iterates. It is measurable, equivariant and adapted. Its coordinate paths are càdlàg: all possible finite birth times lie in the locally finite proposal set of that coordinate, so no new finite accumulation birth time can appear.

We must still pass through the acceptance threshold. On the conull con