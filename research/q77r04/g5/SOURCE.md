## 1. Statement

Let \(\Gamma\) be a countable discrete group, let \(S\) be a fixed finite nonempty set, and put
\[
W=\Gamma\times S,\qquad
\gamma\cdot(g,s)=(\gamma g,s).
\tag{1}
\]
Let \(Q\) be a bounded self-adjoint \(\Gamma\)-equivariant operator on
\(\mathcal H=\ell^2(W)\) satisfying
\[
0<aI\le Q\le bI<I
\qquad (a>0,\ b<1).
\tag{2}
\]

### Theorem

There is a \(\Gamma\)-equivariant measurable map
\[
\Phi:[0,1]^\Gamma\longrightarrow \{0,1\}^{\Gamma\times S}
\tag{3}
\]
such that, for iid uniform input \(U=(U_g)_{g\in\Gamma}\),
\[
\Phi(U)\sim {\bf P}^Q.
\tag{4}
\]
Moreover, for every \(x=(g,s)\in W\), with probability one there is a finite random set
\(K_x(U)\subset\Gamma\) such that \(\Phi(U)_x\) is determined by
\(U|_{K_x(U)}\). Thus \({\bf P}^Q\) is a measure-theoretic finitary factor of the
one-label-per-group-coordinate Bernoulli shift.

No deterministic query bound, tail estimate, finite expected query count, or effective computability assertion is included.

The point requiring work beyond the one-orbit case is that the trace, the disagreement mass, the backward graph, and the iid noise all have to be handled by type and then recombined without losing a factor \(|S|\) in the Gronwall coefficient.

## 2. One uniform label per group element supplies all typed Poisson fields

Write \(m=|S|\) and fix once and for all an enumeration of \(S\). Put
\[
M=\frac{b}{1-b}.
\tag{5}
\]
Let \(\mathcal N\) be the standard Borel space of finite point configurations on
\([0,1]\times[0,M]\), equipped with the law of a Poisson random measure of intensity
\(dt\,du\).

There is a Borel map
\[
D:[0,1]\longrightarrow \mathcal N^S
\tag{6}
\]
whose push-forward of Lebesgue measure is the product of \(m\) copies of that Poisson law.
For example, use the binary digits of one uniform variable, partition the digit positions into
countably many infinite streams, thereby obtain countably many independent uniform variables,
and for each type use one stream to sample a Poisson\((M)\) count and further streams to sample
the iid point locations. Fix arbitrary conventions on dyadic expansions and the null endpoint
exceptions to make the map total and Borel.

For every \(g\in\Gamma\), decode
\[
(N_{g,s})_{s\in S}=D(U_g).
\tag{7}
\]
Under iid \(U_g\), the fields \(N_{g,s}\) are independent over all \((g,s)\in W\), and each has
intensity \(dt\,du\). Importantly, querying the single input coordinate \(U_g\) reveals all
typed clocks at the group coordinate \(g\).

## 3. Shorted radial birth rates

For \(0\le t\le1\), define
\[
R_t=Q(I-tQ)^{-1}.
\tag{8}
\]
Functional calculus gives
\[
aI\le R_t\le MI,
\qquad
M=\frac b{1-b},
\tag{9}
\]
and \(t\mapsto R_t\) is norm-continuous.

For a configuration \(\eta\subseteq W\), let \(P_\eta\) denote the coordinate projection onto
\(\ell^2(\eta)\), and let \(\Pi_t(\eta)\) be the orthogonal projection onto the closed subspace
\[
\mathcal H_t(\eta)=R_t^{1/2}\ell^2(\eta).
\tag{10}
\]
The subspace is closed because \(R_t^{1/2}\) has a bounded inverse. Define
\[
\mathcal S_t(\eta)
=
R_t^{1/2}(I-\Pi_t(\eta))R_t^{1/2},
\qquad
c_x(t,\eta)
=
\langle\delta_x,\mathcal S_t(\eta)\delta_x\rangle.
\tag{11}
\]
Equivalently,
\[
c_x(t,\eta)
=
\inf_{v\in\ell^2(\eta)}
\langle \delta_x-v,R_t(\delta_x-v)\rangle.
\tag{12}
\]

The following facts are immediate or standard Hilbert-space consequences of (12).

* If \(x\in\eta\), then \(c_x(t,\eta)=0\).
* If \(x\notin\eta\), then
\[
a\le c_x(t,\eta)\le M.
\tag{13}
\]
Indeed, \(\delta_x\perp\ell^2(\eta)\).
* If \(\eta\subseteq\xi\), then
\[
c_x(t,\eta)\ge c_x(t,\xi).
\tag{14}
\]
* The rates are covariant:
\[
c_{\gamma x}(t,\gamma\eta)=c_x(t,\eta).
\tag{15}
\]

They are also continuous in the full configuration. If \(\eta_n\uparrow\eta\), the spaces
\(\mathcal H_t(\eta_n)\) increase with dense union in \(\mathcal H_t(\eta)\). If
\(\eta_n\downarrow\eta\), then
\[
\bigcap_n \mathcal H_t(\eta_n)=\mathcal H_t(\eta),
\tag{16}
\]
because \(R_t^{1/2}\) is invertible. Hence the projections converge strongly in both monotone
cases. General product-topology convergence follows by squeezing between the completions
which are empty and full outside a finite window.

For time continuity, a minimizer \(v\) in (12) satisfies
\[
a\|\delta_x-v\|^2\le M
\tag{17}
\]
by comparison with \(v=0\). Comparing minimizers at times \(r\) and \(t\) gives
\[
|c_x(r,\eta)-c_x(t,\eta)|
\le \frac{M}{a}\|R_r-R_t\|.
\tag{18}
\]
Thus \(c_x\) is jointly continuous on
\([0,1]\times\{0,1\}^{W}\).

Choose nested finite sets \(F_R\uparrow\Gamma\), each containing the identity \(e\), and let
\[
K_R=F_R\times S.
\tag{19}
\]
For each type \(s\in S\), set
\[
\delta_{R,s}
=
\sup_{\substack{0\le t\le1\\
\eta|_{K_R}=\zeta|_{K_R}}}
|c_{(e,s)}(t,\eta)-c_{(e,s)}(t,\zeta)|.
\tag{20}
\]
Compactness and uniform continuity imply
\[
\delta_{R,s}\downarrow0.
\tag{21}
\]
Since \(S\) is finite,
\[
\Delta_R:=\sum_{s\in S}\delta_{R,s}\longrightarrow0.
\tag{22}
\]

## 4. The non-normalized finite-type trace

Let \(\eta\subseteq\xi\) be any jointly \(\Gamma\)-invariant random ordered pair of
configurations on \(W\). No DPP law is assumed. For a uniformly bounded covariant random
operator \(A\) on \(\ell^2(W)\), define
\[
\tau(A)
=
\sum_{s\in S}
\mathbb E\langle\delta_{(e,s)},A\delta_{(e,s)}\rangle.
\tag{23}
\]
This is deliberately not normalized:
\[
\tau(I)=|S|.
\tag{24}
\]

The functional is tracial. For uniformly bounded covariant random operators \(A,B\),
\[
\begin{aligned}
\tau(AB)
&=
\sum_{s\in S}\sum_{g\in\Gamma,r\in S}
\mathbb E\!\left[
A_{(e,s),(g,r)}B_{(g,r),(e,s)}
\right].
\end{aligned}
\tag{25}
\]
The sum is absolutely integrable after expectation by Cauchy--Schwarz:
\[
\sum_{g,r}\mathbb E|A_{(e,s),(g,r)}B_{(g,r),(e,s)}|
\le \|A\|_\infty\|B\|_\infty.
\tag{26}
\]
Translate the random environment by \(g^{-1}\), use covariance, reindex \(g^{-1}\), and
interchange the two finite type indices. This gives
\[
\tau(AB)=\tau(BA).
\tag{27}
\]

Put
\[
D=\xi\setminus\eta,\qquad
Z=\Pi_t(\xi)-\Pi_t(\eta).
\tag{28}
\]
Since \(\mathcal H_t(\eta)\subseteq\mathcal H_t(\xi)\), \(Z\) is the orthogonal projection
onto \(\mathcal H_t(\xi)\ominus\mathcal H_t(\eta)\). Define
\[
B=(I-\Pi_t(\eta))R_t^{1/2}P_D.
\tag{29}
\]
For \(v\in\ell^2(D)\),
\[
\begin{aligned}
\|Bv\|
&=
\operatorname{dist}\!\left(
R_t^{1/2}v,R_t^{1/2}\ell^2(\eta)
\right)\\
&\ge
\sqrt a\,\operatorname{dist}(v,\ell^2(\eta))
=
\sqrt a\,\|v\|.
\end{aligned}
\tag{30}
\]
Moreover,
\[
\operatorname{Ran}B
=
\mathcal H_t(\xi)\ominus\mathcal H_t(\eta).
\tag{31}
\]
Indeed every vector in the latter space is the orthogonal-to-\(\mathcal H_t(\eta)\) part of
\(R_t^{1/2}(v_\eta+v_D)\), hence equals \(Bv_D\).

The polar partial isometry \(V\) of \(B\) therefore satisfies
\[
V^*V=P_D,\qquad VV^*=Z.
\tag{32}
\]
Measurability and covariance can be made explicit, for example, by writing \(V\) through
functional calculus of
\(B^*B+I-P_D\), which is uniformly invertible on the two random coordinate blocks.
Traciality gives
\[
\tau(Z)=\tau(P_D)
=
\sum_{s\in S}
\mathbb P\bigl((e,s)\in\xi\setminus\eta\bigr).
\tag{33}
\]

Finally, by (11),
\[
\begin{aligned}
\sum_{s\in S}
\mathbb E\!\left[c_{(e,s)}(t,\eta)-c_{(e,s)}(t,\xi)\right]
&=
\tau(R_t^{1/2}ZR_t^{1/2})\\
&=
\tau(ZR_tZ)\\
&\le
M\tau(Z).
\end{aligned}
\tag{34}
\]
Thus the finite-type oscillation estimate is
\[
\boxed{
\sum_{s\in S}
\mathbb E[c_{(e,s)}(t,\eta)-c_{(e,s)}(t,\xi)]
\le
M\sum_{s\in S}
\mathbb P((e,s)\in\xi\setminus\eta).
}
\tag{35}
\]
There is no extra factor \(|S|\) multiplying \(M\).

## 5. Typed finite-window envelopes and the reverse query graph

For \(x=(g,s)\), write
\[
K_R(x)=gF_R\times S.
\tag{36}
\]
At a candidate point \((t,u)\in N_{g,s}\), define the complete-configuration update
\[
H_x(t,\zeta,u)
=
\zeta_x\vee{\bf 1}\{u<c_x(t,\zeta)\}.
\tag{37}
\]
The occupied-site term is essential.

For a pair of current configurations \(l\le v\), let
\[
\mathcal A_R(x;l,v)
=
\{\zeta\subseteq W:
l_y\le\zeta_y\le v_y\text{ for all }y\in K_R(x)\}.
\tag{38}
\]
Starting from the empty configuration, define lower and upper radius-\(R\) envelopes by the
same typed candidate clocks. At a clock at \(x\), replace only the \(x\)-coordinate by
\[
\begin{aligned}
L_x^R&\leftarrow
\min_{\zeta\in\mathcal A_R(x;L^R,U^R)}
H_x(t,\zeta,u),\\
U_x^R&\leftarrow
\max_{\zeta\in\mathcal A_R(x;L^R,U^R)}
H_x(t,\zeta,u).
\end{aligned}
\tag{39}
\]
The extrema are Borel functions. Indeed, there are finitely many local binary patterns in
\(K_R(x)\); on each corresponding compact cylinder the continuous rate attains its extrema.

The infinite system is evaluated by a typed backward query graph, so no global ordering of
\(\Gamma\) is introduced. To determine a finite typed set \(A\subset W\) at time \(T\), trace
back each required candidate clock. A clock at \(y=(h,r)\) requires the pre-clock states of
all typed sites in
\[
K_R(y)=hF_R\times S.
\tag{40}
\]
Thus each event branches to at most
\[
B_R=m|F_R|
\tag{41}
\]
typed predecessor sites.

The expected number of strictly time-ordered clock paths of length \(n\) from \(A\) is at most
\[
|A|\frac{(M B_R T)^n}{n!}.
\tag{42}
\]
Hence the expected total number of such path occurrences is finite, and the entire typed
reverse graph is almost surely finite. Its projection to \(\Gamma\) is therefore finite as well.
The graph includes all queried predecessor sites, including sites whose relevant time interval
contains no clock.

If \(F_R\subseteq F_{R+1}\), the radius-\((R+1)\) admissible set is contained in the radius-\(R\)
admissible set once the inductive inequalities hold. Induction on the finite union of the two
backward graphs gives, for every queried coordinate and time,
\[
L^R\le L^{R+1}\le U^{R+1}\le U^R.
\tag{43}
\]
By countability this yields jointly defined equivariant envelope fields.

## 6. Aggregate disagreement closes under Gronwall

For \(s\in S\), define
\[
p_{R,s}(t)
=
\mathbb P\bigl(L_t^R(e,s)\ne U_t^R(e,s)\bigr),
\qquad
P_R(t)=\sum_{s\in S}p_{R,s}(t).
\tag{44}
\]
Because the envelopes are ordered, disagreement means lower \(0\) and upper \(1\).

Suppose both envelopes at \(x=(e,s)\) are zero just before a root clock. For any
\(\zeta\in\mathcal A_R(x;L^R,U^R)\), replace its values on \(K_R\) by those of \(L^R\).
The resulting \(\zeta^-\) satisfies \(\zeta^-\le\zeta\) and agrees with \(L^R\) on \(K_R\).
By antitonicity and (20),
\[
c_x(t,\zeta)
\le c_x(t,\zeta^-)
\le c_x(t,L^R)+\delta_{R,s}.
\tag{45}
\]
Likewise, replacing the window by the upper values gives
\[
c_x(t,\zeta)
\ge c_x(t,U^R)-\delta_{R,s}.
\tag{46}
\]
Therefore the interval of marks which can create a new lower/upper disagreement at type \(s\)
has length at most
\[
c_x(t,L^R)-c_x(t,U^R)+2\delta_{R,s}.
\tag{47}
\]
Existing disagreements can be destroyed by later lower births; discarding that negative
contribution and compensating the root Poisson field gives
\[
p_{R,s}(t)
\le
\int_0^t
\left(
\mathbb E[c_{(e,s)}(r,L_r^R)-c_{(e,s)}(r,U_r^R)]
+
2\delta_{R,s}
\right)\,dr.
\tag{48}
\]
The pair \(L_r^R\le U_r^R\) is jointly invariant, so summing (48) over \(s\) and applying
(35) yields the closed scalar inequality
\[
P_R(t)
\le
\int_0^t
\left(MP_R(r)+2\Delta_R\right)\,dr.
\tag{49}
\]
Consequently,
\[
P_R(t)
\le
\frac{2\Delta_R}{M}(e^{Mt}-1)
\le
2\Delta_R\, t e^{Mt}.
\tag{50}
\]
Since \(\Delta_R\to0\), the aggregate envelope disagreement tends to zero. Again, the
Gronwall coefficient is \(M\), not \(mM\).

Define for every input field and every \(t\)
\[
\underline X_t=\sup_R L_t^R,\qquad
\overline X_t=\inf_R U_t^R.
\tag{51}
\]
For each fixed \(t\),
\[
\mathbb P(\underline X_t(e,s)\ne\overline X_t(e,s))
\le \lim_R P_R(t)=0.
\tag{52}
\]
By equivariance and countability, equality holds simultaneously at all typed coordinates for
each fixed \(t\) on a conull event.

## 7. The full-space finitary stopping certificate

Only time \(1\) is needed for the factor. For a deterministic input field \(u\), let
\(r_x(u)\) be the least \(R\ge1\) for which the radius-\(R\) backward query graph for
\((x,1)\) is finite and the computed envelope values satisfy
\[
L_1^R(x)=U_1^R(x).
\tag{53}
\]
If no such \(R\) exists, set \(\Phi(u)_x=0\). Otherwise set \(\Phi(u)_x\) equal to the common
value in (53).

The exploration events and the computed finite graph values are Borel, so \(\Phi\) is
measurable. Translation of the group labels translates the entire typed graph while preserving
the type, so \(\Phi\) is \(\Gamma\)-equivariant on the whole input space.

Under iid input, every fixed-\(R\) backward graph is finite almost surely. Also, by (43) and
(52) at \(t=1\), the nested binary lower and upper sequences have the same limit. Two nested
binary sequences with the same limit must coincide at some finite \(R\). Thus \(r_x(U)<\infty\)
almost surely, simultaneously for all \(x\in W\).

Let \(\mathcal G_x(U)\subset\Gamma\) be the projection to group coordinates of the successful
typed reverse graph. This is finite. Querying \(U_g\) for \(g\in\mathcal G_x(U)\) reveals all
typed Poisson fields used by the graph. If another input \(u'\) agrees with \(u\) on those
group coordinates, the same radius-\(R\) graph is finite and has the same common envelope
value. If \(u'\) happens to have a successful smaller radius, the nesting (43) forces that
smaller-radius common value to equal the radius-\(R\) common value. Therefore
\[
u'|_{\mathcal G_x(u)}=u|_{\mathcal G_x(u)}
\quad\Longrightarrow\quad
\Phi(u')_x=\Phi(u)_x.
\tag{54}
\]
This is the required finite group-coordinate certificate.

## 8. Moving-window Schur complements for \(W=\Gamma\times S\)

It remains to identify the law. Put
\[
\mu_t={\bf P}^{tQ}.
\tag{55}
\]
Choose finite \(F_n\uparrow\Gamma\) and let
\[
W_n=F_n\times S,\qquad P_n=P_{W_n},\qquad Q_n=P_nQP_n|_{\ell^2(W_n)}.
\tag{56}
\]
Since (2) compresses to every finite subspace,
\[
aI_{W_n}\le Q_n\le bI_{W_n}.
\tag{57}
\]
For \(t>0\), define
\[
A_{t,n}=Q_n(I-tQ_n)^{-1}.
\tag{58}
\]
The restriction of \(\mu_t\) to \(W_n\) is the finite DPP with kernel \(tQ_n\), whose
\(L\)-ensemble matrix is \(tA_{t,n}\). If \(x\in W_n\) and
\(E\subseteq W_n\setminus\{x\}\), the exact configuration-weight ratio is
\[
\frac{\mu_t(X\cap W_n=E\cup\{x\})}
{\mu_t(X\cap W_n=E)}
=
t\,\beta_{t,n}(x,E),
\tag{59}
\]
where
\[
\beta_{t,n}(x,E)
=
\inf_{v\in\ell^2(E)}
\langle\delta_x-v,A_{t,n}(\delta_x-v)\rangle.
\tag{60}
\]

The important point is that \(A_{t,n}\) is built from the compressed \(Q_n\), not by
compressing \(R_t\). Extend \(A_{t,n}\) by zero outside \(W_n\). Since
\[
P_nQP_n\longrightarrow Q
\quad\text{strongly}
\tag{61}
\]
and \(f_t(z)=z/(1-tz)\) is continuous on \([0,b]\) with \(f_t(0)=0\), bounded continuous
functional calculus gives
\[
A_{t,n}\longrightarrow R_t
\quad\text{strongly}.
\tag{62}
\]

Fix a full exterior configuration \(\eta\subseteq W\setminus\{x\}\), and put
\[
D_n=P_{\eta\cap W_n},\qquad D=P_\eta.
\tag{63}
\]
Define
\[
C_n=D_nA_{t,n}D_n+I-D_n,
\qquad
C=DR_tD+I-D.
\tag{64}
\]
Then \(C_n\to C\) strongly and
\[
C_n,C\ge \min(a,1)I.
\tag{65}
\]
The resolvent identity therefore implies
\[
C_n^{-1}\longrightarrow C^{-1}
\quad\text{strongly}.
\tag{66}
\]
Completing the square gives the finite shorted operator
\[
T_n
=
A_{t,n}
-
A_{t,n}D_nC_n^{-1}D_nA_{t,n}.
\tag{67}
\]
All factors are uniformly bounded and converge strongly, hence
\[
T_n
\longrightarrow
R_t-R_tDC^{-1}DR_t
=
\mathcal S_t(\eta)
\quad\text{strongly}.
\tag{68}
\]
In particular,
\[
\beta_{t,n}(x,\eta\cap W_n)
\longrightarrow
c_x(t,\eta).
\tag{69}
\]

For fixed \(x\), the finite conditional probabilities under \(\mu_t\) are therefore
\[
\mu_t(X_x=1\mid X|_{W_n\setminus\{x\}})
=
\frac{t\beta_{t,n}}{1+t\beta_{t,n}}.
\tag{70}
\]
The conditioning sigma-fields increase to the full exterior sigma-field. Martingale
convergence together with the pointwise limit (69) yields
\[
\mu_t(X_x=1\mid X|_{W\setminus\{x\}})
=
\frac{t\,c_x(t,X\setminus\{x\})}
{1+t\,c_x(t,X\setminus\{x\})}
\quad\mu_t\text{-a.s.}
\tag{71}
\]
Equivalently, the full-exterior conditional odds are
\[
\frac{\mu_t(X_x=1\mid X_{W\setminus\{x\}})}
{\mu_t(X_x=0\mid X_{W\setminus\{x\}})}
=
t\,c_x(t,X\setminus\{x\}).
\tag{72}
\]
The denominator is bounded below by \(1/(1+tM)\).

## 9. Forward equation and finite conditional-mean chains

For a cylinder function \(f\), define
\[
(\mathcal L_t f)(\eta)
=
\sum_{x\notin\eta}
c_x(t,\eta)\,[f(\eta\cup\{x\})-f(\eta)].
\tag{73}
\]
Only finitely many terms are nonzero. The odds identity (72), conditioned one site at a time,
gives
\[
\mu_t(\mathcal L_t f)
=
\frac1t
\mathbb E_{\mu_t}
\sum_{x\in X}
[f(X)-f(X\setminus\{x\})].
\tag{74}
\]
For the inclusion cylinder \(f_H(X)={\bf1}\{H\subseteq X\}\),
\[
\mu_t(f_H)=t^{|H|}\det Q[H],
\tag{75}
\]
and the right side of (74) is exactly its derivative. Inclusion cylinders span the finite
cylinder functions, so
\[
\frac{d}{dt}\mu_t(f)=\mu_t(\mathcal L_t f)
\qquad (t>0).
\tag{76}
\]
Bounded rates let the integral form extend to \(t=0\), where \(\mu_0\) is the empty law.

Now fix a finite typed set \(E\subset W\). For \(t>0\), \(x\in E\), and
\(\zeta\subseteq E\), define
\[
c_x^E(t,\zeta)
=
\mathbb E_{\mu_t}
[c_x(t,X)\mid X|_E=\zeta].
\tag{77}
\]
Every pattern \(\zeta\) has positive probability: the finite kernel \(tQ_E\) has spectrum in
\((0,1)\), so its \(L\)-ensemble matrix is positive definite and every exact configuration
weight is positive. The functions in (77) are bounded by \(M\), vanish when \(x\in\zeta\),
and are Borel in \(t\). Values at \(t=0\) may be chosen arbitrarily within these bounds.

Conditioning (73) on \(X|_E\) shows that \(\mu_t|_E\) satisfies the forward equation of the
finite time-inhomogeneous pure-birth chain with rates \(c_x^E\). The corresponding finite
bounded linear integral equation is unique from the empty initial state. Therefore a chain
\(Y^E\) driven by the same typed candidate clocks, accepting a mark \(u\) at \(x\) when
\(u<c_x^E(t,Y^E_{t-})\), has
\[
Y_t^E\sim\mu_t|_E.
\tag{78}
\]

## 10. Comparing the finite chains to the envelopes

Fix a finite typed query set \(A\subset W\), a radius \(R\), and time \(t\). Let
\(\mathcal C_R(A,t)\) be the typed radius-\(R\) reverse graph. On the event
\[
\mathcal C_R(A,t)\subseteq E,
\tag{79}
\]
compare \(Y^E\) to \(L^R,U^R\) along the finitely many relevant state queries and clocks.

At a relevant clock at \(x\), the reverse graph contains every site in \(K_R(x)\). By
induction, the finite-chain local pattern lies between the two envelope patterns there. Every
full configuration appearing in the conditional law defining \(c_x^E\) agrees with the
finite-chain pattern on \(E\), hence in particular its restriction to \(K_R(x)\) is admissible
for the envelope update. If the chain has \(x=0\), its conditional-mean rate is a convex
average of admissible \(x=0\) rates, hence lies between their minimum and maximum. If the
chain has \(x=1\), its update is identically \(1\). In either case the common mark preserves
\[
L^R\le Y^E\le U^R
\tag{80}
\]
at every relevant query.

Notice that \(c_x^E\) may depend on the entire state of \(E\), including far-away sites.
This does not invalidate the comparison: far-away coordinates can alter the conditional mean,
but a conditional mean of admissible full-space rates remains inside the convex hull of those
rates. They never directly alter the state of a queried site; every clock at a queried site is
already included in the reverse graph.

Let \(X_t=\underline X_t\) from (51). Then
\[
\begin{aligned}
\mathbb P(Y_t^E|_A\ne X_t|_A)
&\le
\mathbb P(\mathcal C_R(A,t)\not\subseteq E)
+
\sum_{x\in A}\mathbb P(L_t^R(x)\ne U_t^R(x))\\
&\le
\mathbb P(\mathcal C_R(A,t)\not\subseteq E)
+
|A|P_R(t).
\end{aligned}
\tag{81}
\]
Take \(E=W_n=F_n\times S\) and let \(n\to\infty\). The first term tends to zero because the
reverse graph is almost surely finite. By (78), \(Y_t^{W_n}|_A\) has law \(\mu_t|_A\) for
every sufficiently large \(n\). Hence
\[
d_{\rm TV}(\mathcal L(X_t|_A),\mu_t|_A)
\le |A|P_R(t).
\tag{82}
\]
Letting \(R\to\infty\) and using (50) gives
\[
X_t|_A\sim \mu_t|_A.
\tag{83}
\]
Since \(A\) was arbitrary finite,
\[
X_t\sim{\bf P}^{tQ},
\qquad 0\le t\le1.
\tag{84}
\]
In particular \(X_1\sim{\bf P}^Q\), and Section 7 shows that the total map \(\Phi\) agrees
with \(X_1\) almost surely and is a finitary factor from one iid uniform label per group
coordinate.

## 11. Exact scope and relation to Lyons--Thom

Lyons--Thom identify the edge action of a Cayley diagram with the left action on
\(\Gamma\times S\), identify the corresponding equivariant algebra with
\(M_S(R(\Gamma))\), and use the natural non-normalized trace which sums the root diagonals
over \(s\in S\). Their Question 7.7 asks whether determinantal measures associated with
equivariant positive contractions are factors of Bernoulli shifts.

The theorem proved here is a restricted positive result for a finite union of free regular
orbits and a two-sided spectral gap. It does not answer Question 7.7 for arbitrary positive
contractions and does not address general quasi-transitive actions with stabilizers.

The source paper is:

Russell Lyons and Andreas Thom, *Invariant coupling of determinantal measures on sofic
groups*, Ergodic Theory and Dynamical Systems 36 (2016), 574--607,
https://rdlyons.pages.iu.edu/pdf/couple-pub.pdf

This draft was derived independently from the finite-type formulation requested in round 02.
The fact that a proof closes mathematically under the stated assumptions does not establish
that the result or method is new in the literature.
