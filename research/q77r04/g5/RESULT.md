# PROVED

Let \(m:=|S|\), \(W=\Gamma\times S\), and

\[
M:=\frac{b}{1-b}.
\]

I will prove the exact frozen statement, including a total equivariant Borel map, an almost-surely terminating finite-site query procedure, and a certificate valid against **every** completion of the unqueried labels. The proof does not establish finite expected query count, finite-bit computability, or a universal geometric coding-radius tail.

## 1. A proper exhaustion, with no finite-generation assumption

Choose a proper left-invariant metric \(d\) on \(\Gamma\). Such a metric exists for every countable group: enumerate \(\Gamma\setminus\{e\}\) symmetrically, give the enumerated elements symmetric positive integer weights tending to infinity, and use the associated weighted word length. Its finite balls

\[
F_R:=\{g\in\Gamma:d(e,g)\le R\},\qquad R\ge 1,
\]

are nested, contain \(e\), and exhaust \(\Gamma\). Set

\[
K_R:=F_R\times S,\qquad
K_R(g,s):=gF_R\times S.
\]

No finite generating set is used.

Fix a total Borel decoder

\[
D:[0,1]\longrightarrow \prod_{s\in S}\mathcal N_s,
\]

where each \(\mathcal N_s\) is the standard Borel space of finite point configurations on

\[
[0,1)\times[0,M)
\]

with Poisson law of intensity \(dt\,du\), and the push-forward of Lebesgue measure is the product of these \(m\) Poisson laws. Such a decoder exists because every standard Borel probability law is a Borel image of Lebesgue measure. Null exceptional labels may be assigned arbitrary finite configurations to make \(D\) total.

For each \(g\), decode \(U_g\) into \((N_{g,s})_{s\in S}\). Under iid uniform labels, the point processes \(N_{g,s}\), indexed by all \((g,s)\in W\), are independent. Querying the one whole label \(U_g\) reveals every typed field at \(g\).

For exceptional deterministic inputs, fix these total-map conventions:

1. A mark \((t,u)\) is accepted only if \(u<c\), with strict inequality.
2. Marks having exactly the same time are processed simultaneously from their common left state.
3. If no finite successful window exists at a coordinate, the total map outputs \(0\).

The simultaneous convention avoids choosing a non-equivariant global order on \(\Gamma\). Under the iid law, simultaneous times and equality with a threshold have probability zero.

## 2. Shorted intensities

For \(0\le t\le 1\), define

\[
R_t:=Q(I-tQ)^{-1}.
\]

Functional calculus gives

\[
aI\le R_t\le MI.
\tag{2.1}
\]

For a configuration \(\eta\subseteq W\), let \(\Pi_t(\eta)\) be the orthogonal projection onto

\[
\mathcal H_t(\eta):=R_t^{1/2}\ell^2(\eta).
\]

This is closed because \(R_t^{1/2}\) is boundedly invertible. Define

\[
\mathcal S_t(\eta)
=
R_t^{1/2}(I-\Pi_t(\eta))R_t^{1/2}
\]

and

\[
c_x(t,\eta)
=
\langle \delta_x,\mathcal S_t(\eta)\delta_x\rangle.
\]

Equivalently,

\[
c_x(t,\eta)
=
\inf_{v\in\ell^2(\eta)}
\langle \delta_x-v,R_t(\delta_x-v)\rangle.
\tag{2.2}
\]

Consequently:

\[
x\in\eta\implies c_x(t,\eta)=0,
\tag{2.3}
\]

and, if \(x\notin\eta\),

\[
a\le c_x(t,\eta)\le M.
\tag{2.4}
\]

Moreover,

\[
\eta\subseteq\xi
\implies
c_x(t,\eta)\ge c_x(t,\xi),
\tag{2.5}
\]

and covariance of \(Q\) gives covariance of \(c\).

### Continuity in the configuration

For fixed \(t\), suppose \(\eta_n\uparrow\eta\). Then the spaces
\(R_t^{1/2}\ell^2(\eta_n)\) increase and their union is dense in
\(R_t^{1/2}\ell^2(\eta)\), so the corresponding projections converge strongly.

If \(\eta_n\downarrow\eta\), then invertibility of \(R_t^{1/2}\) gives

\[
\bigcap_nR_t^{1/2}\ell^2(\eta_n)
=
R_t^{1/2}\left(\bigcap_n\ell^2(\eta_n)\right)
=
R_t^{1/2}\ell^2(\eta),
\]

so the decreasing projections also converge strongly.

For arbitrary product-topology convergence, if \(\zeta\) agrees with \(\eta\) on \(K_R\), then

\[
\eta\cap K_R\subseteq \zeta\subseteq \eta\cup K_R^c.
\]

By antitonicity,

\[
c_x(t,\eta\cap K_R)
\ge c_x(t,\zeta)
\ge c_x(t,\eta\cup K_R^c),
\]

and both bounds converge to \(c_x(t,\eta)\). Hence \(c_x(t,\cdot)\) is continuous.

### Uniformity in time

Let \(v_t\) be the minimizer in (2.2). Comparing with \(v=0\),

\[
a\|\delta_x-v_t\|^2
\le c_x(t,\eta)
\le M.
\]

Thus

\[
|c_x(r,\eta)-c_x(t,\eta)|
\le \frac{M}{a}\|R_r-R_t\|.
\tag{2.6}
\]

Therefore \(c_x\) is jointly continuous on the compact space

\[
[0,1]\times\{0,1\}^W.
\]

For \(s\in S\), define the finite-window oscillation

\[
\delta_{R,s}
:=
\sup_{\substack{0\le t\le1\\
\eta|_{K_R}=\zeta|_{K_R}}}
\left|
c_{(e,s)}(t,\eta)-c_{(e,s)}(t,\zeta)
\right|,
\]

and put

\[
\Delta_R:=\sum_{s\in S}\delta_{R,s}.
\]

Uniform continuity implies

\[
\delta_{R,s}\downarrow0,
\qquad
\Delta_R\longrightarrow0.
\tag{2.7}
\]

## 3. The type-summed trace estimate

Let \(\eta\subseteq\xi\) be any jointly \(\Gamma\)-invariant random ordered pair of configurations. For a uniformly bounded covariant random operator \(A\), define

\[
\tau(A)
=
\sum_{s\in S}
\mathbb E
\langle\delta_{(e,s)},A\delta_{(e,s)}\rangle.
\tag{3.1}
\]

This trace is deliberately not normalized:

\[
\tau(I)=m.
\]

It is tracial. Indeed,

\[
\tau(AB)
=
\sum_{s,r\in S}\sum_{g\in\Gamma}
\mathbb E
\left[
A_{(e,s),(g,r)}
B_{(g,r),(e,s)}
\right].
\]

The series is absolutely integrable because, pointwise,

\[
\sum_{g,r}
|A_{(e,s),(g,r)}B_{(g,r),(e,s)}|
\le
\|A^*\delta_{(e,s)}\|
\|B\delta_{(e,s)}\|
\le
\|A\|\,\|B\|.
\]

Translating the environment by \(g^{-1}\), using covariance and invariance, reindexing \(g^{-1}\), and interchanging the finite type indices gives

\[
\tau(AB)=\tau(BA).
\tag{3.2}
\]

Let

\[
D:=\xi\setminus\eta,\qquad
Z:=\Pi_t(\xi)-\Pi_t(\eta).
\]

Since the two subspaces are nested, \(Z\) is the orthogonal projection onto

\[
\mathcal H_t(\xi)\ominus\mathcal H_t(\eta).
\]

Define

\[
B:=(I-\Pi_t(\eta))R_t^{1/2}P_D.
\]

For \(v\in\ell^2(D)\),

\[
\begin{aligned}
\|Bv\|
&=
\operatorname{dist}
\left(R_t^{1/2}v,R_t^{1/2}\ell^2(\eta)\right)\\
&\ge
\sqrt a\,
\operatorname{dist}(v,\ell^2(\eta))\\
&=
\sqrt a\,\|v\|.
\end{aligned}
\tag{3.3}
\]

Also,

\[
\operatorname{Ran}B
=
\mathcal H_t(\xi)\ominus\mathcal H_t(\eta).
\]

Indeed, every vector in the latter space is the component orthogonal to
\(\mathcal H_t(\eta)\) of \(R_t^{1/2}(v_\eta+v_D)\), hence equals \(Bv_D\).

The polar partial isometry \(V\) of \(B\) therefore satisfies

\[
V^*V=P_D,\qquad VV^*=Z.
\tag{3.4}
\]

It can be chosen measurably and covariantly, for example as

\[
V=B(B^*B+I-P_D)^{-1/2}.
\]

By traciality,

\[
\tau(Z)=\tau(P_D)
=
\sum_{s\in S}
\mathbb P\bigl((e,s)\in\xi\setminus\eta\bigr).
\tag{3.5}
\]

Finally,

\[
\begin{aligned}
\sum_{s\in S}
\mathbb E
\left[
c_{(e,s)}(t,\eta)-c_{(e,s)}(t,\xi)
\right]
&=
\tau(R_t^{1/2}ZR_t^{1/2})\\
&=
\tau(ZR_t)\\
&=
\tau(ZR_tZ)\\
&\le
M\tau(Z).
\end{aligned}
\]

Thus

\[
\boxed{
\sum_{s\in S}
\mathbb E
\left[
c_{(e,s)}(t,\eta)-c_{(e,s)}(t,\xi)
\right]
\le
M\sum_{s\in S}
\mathbb P((e,s)\in\xi\setminus\eta).
}
\tag{3.6}
\]

There is no additional factor \(m\).

## 4. Finite-window lower and upper envelopes

For a complete configuration \(\zeta\), define the one-mark update

\[
H_x(t,\zeta,u)
=
\zeta_x\vee\mathbf 1\{u<c_x(t,\zeta)\}.
\tag{4.1}
\]

For ordered states \(l\le v\), put

\[
\mathcal A_R(x;l,v)
=
\left\{
\zeta\subseteq W:
l_y\le\zeta_y\le v_y
\text{ for every }y\in K_R(x)
\right\}.
\]

Starting from the empty state, at a candidate mark at \(x\) define

\[
L_x^R
\leftarrow
\min_{\zeta\in\mathcal A_R(x;L^R,U^R)}
H_x(t,\zeta,u),
\]

\[
U_x^R
\leftarrow
\max_{\zeta\in\mathcal A_R(x;L^R,U^R)}
H_x(t,\zeta,u).
\tag{4.2}
\]

The extrema are Borel functions. For each of the finitely many patterns on \(K_R(x)\), the continuous function \(c_x(t,\cdot)\) attains its infimum and supremum on the corresponding compact cylinder. With the strict convention, the lower and upper decisions are comparisons with those attained extrema.

At a time shared by several candidate points, every proposal is computed from the common pre-time state and the coordinatewise OR of the proposals is taken.

## 5. Backward dependency exploration

To determine the envelope states on a finite typed root set \(A\) at time \(T\), construct a reverse tree as follows.

A state query \((y,T')\) examines all candidate points at typed site \(y\) having time \(t<T'\). Every such point creates predecessor state queries

\[
(z,t),\qquad z\in K_R(y).
\]

Time strictly decreases along each dependency path. Every event has at most

\[
B_R:=m|F_R|
\tag{5.1}
\]

typed predecessor choices.

Let \(Z_n\) be the number of time-ordered path occurrences of length \(n\) starting from \(A\). There are at most \(B_R^n\) typed spatial sequences. For each such sequence, the Poisson factorial-moment formula gives volume

\[
M^n\frac{T^n}{n!}
\]

for strictly decreasing event times. This remains valid if a path revisits a typed site, because strict time decrease forces distinct Poisson points. Hence

\[
\mathbb E Z_n
\le
|A|\frac{(MB_RT)^n}{n!}.
\tag{5.2}
\]

Therefore

\[
\mathbb E|\mathcal C_R(A,T)|
\le
|A|e^{MB_RT}<\infty,
\tag{5.3}
\]

where the graph may be counted as a tree of path occurrences. In particular, the reverse graph is finite almost surely. Its projection to \(\Gamma\) is finite.

The graph includes every predecessor typed site, including sites whose relevant interval contains no point. This is essential: querying such a site certifies the absence of a relevant point.

### Nesting in \(R\)

If \(R<R'\), then \(F_R\subseteq F_{R'}\). Whenever both finite computations exist, induction over the finite union of their dependency graphs gives

\[
L^R\le L^{R'}\le U^{R'}\le U^R.
\tag{5.4}
\]

Indeed, assuming these inequalities for all predecessor states, the admissible set for the \(R'\)-update is contained in the admissible set for the \(R\)-update. Its minimum is therefore at least the smaller-window minimum, and its maximum is at most the smaller-window maximum. Simultaneous updates preserve the same inequalities.

This deterministic nesting statement is valid for exceptional inputs as long as the two graphs being compared are finite.

## 6. Disagreement closes under the type-summed trace

For \(s\in S\), set

\[
p_{R,s}(t)
=
\mathbb P
\bigl(
L_t^R(e,s)\ne U_t^R(e,s)
\bigr),
\]

and

\[
P_R(t):=\sum_{s\in S}p_{R,s}(t).
\]

Because the envelopes are ordered, disagreement is exactly the state pair \((0,1)\).

Suppose immediately before a candidate point at \(x=(e,s)\), both envelope states equal \(0\). For any admissible \(\zeta\), replace its values on \(K_R\) by the lower local pattern, obtaining \(\zeta^-\le\zeta\). Then

\[
c_x(t,\zeta)
\le c_x(t,\zeta^-)
\le c_x(t,L^R)+\delta_{R,s}.
\tag{6.1}
\]

Similarly, replacing the window by the upper local pattern gives \(\zeta\le\zeta^+\) and

\[
c_x(t,\zeta)
\ge c_x(t,\zeta^+)
\ge c_x(t,U^R)-\delta_{R,s}.
\tag{6.2}
\]

Thus the interval of vertical marks that can create a new disagreement has length at most

\[
c_x(t,L^R)-c_x(t,U^R)+2\delta_{R,s}.
\tag{6.3}
\]

Once the state is \((0,1)\), a later lower birth may destroy disagreement; ignoring that negative contribution only enlarges the bound.

The envelope state immediately before a candidate point is measurable with respect to strictly earlier points. Hence predictable Poisson compensation applies even though the exploration is adaptive. It yields

\[
p_{R,s}(t)
\le
\int_0^t
\left(
\mathbb E[
c_{(e,s)}(r,L_r^R)
-
c_{(e,s)}(r,U_r^R)
]
+
2\delta_{R,s}
\right)\,dr.
\tag{6.4}
\]

The pair \(L_r^R\le U_r^R\) is jointly invariant. Summing (6.4) over \(s\) and applying (3.6),

\[
P_R(t)
\le
\int_0^t
\left(
MP_R(r)+2\Delta_R
\right)\,dr.
\]

Gronwall’s inequality gives

\[
\boxed{
P_R(t)
\le
\frac{2\Delta_R}{M}(e^{Mt}-1)
\le
2\Delta_R\,t e^{Mt}.
}
\tag{6.5}
\]

Therefore

\[
P_R(t)\longrightarrow0.
\tag{6.6}
\]

Define

\[
\underline X_t:=\sup_R L_t^R,\qquad
\overline X_t:=\inf_R U_t^R.
\]

For a fixed coordinate, the disagreement events decrease with \(R\), so

\[
\mathbb P(\underline X_t(x)\ne\overline X_t(x))
=
\lim_R
\mathbb P(L_t^R(x)\ne U_t^R(x))
=
0.
\]

By countability of \(W\), the two limits agree simultaneously at all coordinates almost surely. Denote the common field by \(X_t\).

## 7. Identification of the law

Let

\[
\mu_t:={\bf P}^{tQ}.
\]

The existence and uniqueness of the DPP associated with a positive contraction on a countable set is standard; Lyons and Lyons–Thom are convenient references. 

### 7.1 Finite conditional odds and their limit

Choose finite \(W_n\uparrow W\), with coordinate projections \(P_n\), and put

\[
Q_n=P_nQP_n|_{\ell^2(W_n)}.
\]

Then

\[
aI_{W_n}\le Q_n\le bI_{W_n}.
\]

For \(t>0\), define

\[
A_{t,n}:=Q_n(I-tQ_n)^{-1}.
\]

The restriction of \(\mu_t\) to \(W_n\) is the finite DPP with kernel \(tQ_n\). Its finite \(L\)-matrix is

\[
tA_{t,n}.
\]

Indeed, \(L=tQ_n(I-tQ_n)^{-1}\), and the principal-minor expansion gives exact configuration weights

\[
\mu_t(X\cap W_n=E)
=
\det(I-tQ_n)\det(tA_{t,n})[E].
\tag{7.1}
\]

Every exact pattern has positive probability because \(tA_{t,n}\) is positive definite.

For \(x\in W_n\) and \(E\subseteq W_n\setminus\{x\}\), the determinant Schur complement gives

\[
\frac{
\mu_t(X\cap W_n=E\cup\{x\})
}{
\mu_t(X\cap W_n=E)
}
=
t\beta_{t,n}(x,E),
\tag{7.2}
\]

where

\[
\beta_{t,n}(x,E)
=
\inf_{v\in\ell^2(E)}
\langle\delta_x-v,A_{t,n}(\delta_x-v)\rangle.
\tag{7.3}
\]

Extend \(P_nQP_n\) and \(A_{t,n}\) by zero outside \(W_n\). Since

\[
P_nQP_n\longrightarrow Q
\]

strongly, and

\[
f_t(z)=\frac{z}{1-tz}
\]

is continuous on \([0,b]\) with \(f_t(0)=0\), polynomial approximation gives

\[
A_{t,n}=f_t(P_nQP_n)\longrightarrow R_t
\]

strongly.

Fix a full exterior configuration
\(\eta\subseteq W\setminus\{x\}\), and let

\[
D_n=P_{\eta\cap W_n},\qquad D=P_\eta.
\]

Set

\[
C_n=D_nA_{t,n}D_n+I-D_n,\qquad
C=DR_tD+I-D.
\]

Then \(C_n\to C\) strongly, and

\[
C_n,C\ge\min(a,1)I.
\]

Thus \(C_n^{-1}\to C^{-1}\) strongly. Completing the square in (7.3) gives

\[
T_n
=
A_{t,n}
-
A_{t,n}D_nC_n^{-1}D_nA_{t,n}.
\]

All factors are uniformly bounded and converge strongly, so

\[
T_n
\longrightarrow
R_t-R_tDC^{-1}DR_t.
\tag{7.4}
\]

The operator on the right is precisely the shorted operator
\(\mathcal S_t(\eta)\), by the same variational normal-equation calculation as in (2.2). Hence

\[
\beta_{t,n}(x,\eta\cap W_n)
\longrightarrow
c_x(t,\eta).
\tag{7.5}
\]

The finite conditional probability is

\[
\mu_t
\left(
X_x=1
\mid
X|_{W_n\setminus\{x\}}
\right)
=
\frac{t\beta_{t,n}}{1+t\beta_{t,n}}.
\]

These conditional expectations form a bounded martingale for the increasing exterior sigma-fields. Martingale convergence and (7.5) imply

\[
\boxed{
\mu_t
\left(
X_x=1
\mid
X|_{W\setminus\{x\}}
\right)
=
\frac{
t\,c_x(t,X\setminus\{x\})
}{
1+t\,c_x(t,X\setminus\{x\})
}
}
\tag{7.6}
\]

almost surely. Equivalently, the full-exterior conditional odds are

\[
\frac{
\mu_t(X_x=1\mid X_{W\setminus\{x\}})
}{
\mu_t(X_x=0\mid X_{W\setminus\{x\}})
}
=
t\,c_x(t,X\setminus\{x\}).
\tag{7.7}
\]

### 7.2 The forward equation

For a cylinder function \(f\), define

\[
(\mathcal L_tf)(\eta)
=
\sum_{x\notin\eta}
c_x(t,\eta)
\bigl[
f(\eta\cup\{x\})-f(\eta)
\bigr].
\tag{7.8}
\]

Only finitely many terms affect \(f\).

Conditioning on the exterior of \(x\) and using (7.7) gives, for \(t>0\),

\[
\mu_t(\mathcal L_tf)
=
\frac1t
\mathbb E_{\mu_t}
\sum_{x\in X}
\bigl[
f(X)-f(X\setminus\{x\})
\bigr].
\tag{7.9}
\]

For the inclusion indicator

\[
f_H(X)=\mathbf1\{H\subseteq X\},
\]

we have

\[
\mu_t(f_H)=t^{|H|}\det Q[H],
\]

and the right side of (7.9) is exactly its derivative. Inclusion indicators span all functions depending on a fixed finite coordinate set. Therefore

\[
\frac{d}{dt}\mu_t(f)
=
\mu_t(\mathcal L_tf),
\qquad t>0.
\tag{7.10}
\]

Bounded rates and continuity of cylinder probabilities extend the integral form to \(t=0\), where \(\mu_0\) is the empty law.

### 7.3 Finite conditional-mean chains

Fix finite \(E\subset W\). For \(x\in E\), \(t>0\), and \(\zeta\subseteq E\), define

\[
\bar c_x^E(t,\zeta)
=
\mathbb E_{\mu_t}
[
c_x(t,X)
\mid
X|_E=\zeta
].
\tag{7.11}
\]

Every pattern \(\zeta\) has positive probability, as noted above. These rates are bounded by \(M\) and vanish when \(x\in\zeta\).

They are Borel, in fact continuous for \(t>0\): the event \(X|_E=\zeta\) is clopen, \(c_x(t,\cdot)\) is jointly continuous, and \(t\mapsto\mu_t\) is weakly continuous because all finite cylinder probabilities are polynomials in \(t\).

Conditioning (7.10) on \(X|_E\) shows that \(\mu_t|_E\) solves the finite-state forward equation with birth rates \(\bar c_x^E\). Bounded finite-state time-inhomogeneous integral equations have unique solutions by Gronwall. Hence the pure-birth chain \(Y^E\), driven by the same candidate fields and accepting a point \((t,u)\) at \(x\) when

\[
u<\bar c_x^E(t,Y^E_{t-}),
\]

satisfies

\[
Y_t^E\sim\mu_t|_E.
\tag{7.12}
\]

### 7.4 Comparison with the envelopes

Fix a finite typed root set \(A\), a radius \(R\), and time \(t\). On the event

\[
\mathcal C_R(A,t)\subseteq E,
\]

compare \(Y^E\) with \(L^R,U^R\) along the finite reverse graph.

Suppose inductively that the chain pattern on \(K_R(x)\) lies between the two envelope patterns immediately before a relevant point. If the chain has \(x=0\), every full configuration occurring in the conditional expectation (7.11) has that same local chain pattern, and therefore belongs to the envelope’s admissible local class. Thus the conditional mean rate lies between the minimum and maximum admissible rates.

Consequently:

- if the lower envelope accepts the common mark, the chain accepts it;
- if the chain accepts it, the upper envelope accepts it.

If the chain already has \(x=1\), it remains \(1\), and the inequalities are preserved. The same argument works coordinatewise for simultaneous points. Therefore

\[
L^R\le Y^E\le U^R
\tag{7.13}
\]

at every relevant graph query.

The rate \(\bar c_x^E\) may depend on far-away coordinates of \(E\), but this does not invalidate the comparison: those coordinates can move the conditional average only within the admissible local min–max interval, and they cannot directly change a queried coordinate.

It follows that

\[
\begin{aligned}
\mathbb P(Y_t^E|_A\ne X_t|_A)
\le{}&
\mathbb P(\mathcal C_R(A,t)\not\subseteq E)\\
&+
\sum_{x\in A}
\mathbb P(L_t^R(x)\ne U_t^R(x)).
\end{aligned}
\tag{7.14}
\]

Take \(E=W_n\uparrow W\). The first term tends to zero because the reverse graph is almost surely finite. By (7.12), the law of \(Y_t^{W_n}|_A\) is \(\mu_t|_A\). Hence

\[
d_{\rm TV}
\bigl(
\mathcal L(X_t|_A),\mu_t|_A
\bigr)
\le
|A|P_R(t).
\]

Letting \(R\to\infty\) and using (6.5),

\[
X_t|_A\sim\mu_t|_A.
\]

Since this holds for every finite \(A\),

\[
\boxed{
X_t\sim{\bf P}^{tQ}.
}
\tag{7.15}
\]

In particular,

\[
X_1\sim{\bf P}^Q.
\tag{7.16}
\]

## 8. The total equivariant Borel map

For a deterministic input \(\omega\in[0,1]^\Gamma\), a typed coordinate \(x\), and an integer \(R\), call \(R\) **successful** if:

1. the radius-\(R\) reverse graph rooted at \((x,1)\) is finite; and
2. its computed root envelopes agree:

\[
L_1^R(x;\omega)=U_1^R(x;\omega).
\]

Let \(r_x(\omega)\) be the least successful \(R\), if one exists. Define

\[
\Phi(\omega)_x
=
\begin{cases}
L_1^{r_x(\omega)}(x;\omega),
&
r_x(\omega)<\infty,\\[2mm]
0,
&
r_x(\omega)=\infty.
\end{cases}
\tag{8.1}
\]

### Borel measurability

For fixed \(x,R\), each finite-depth truncation of the locally finite reverse tree is Borel in the decoded labels. A locally finite rooted tree is finite iff, for some finite depth, no new nodes appear. Thus graph finiteness is Borel.

On the graph-finite event, the lower and upper values are obtained through a finite recursion involving Borel extrema and comparisons. Therefore success is Borel. Taking the least successful integer and applying (8.1) gives a total Borel map.

### Equivariance

Left translation carries \(K_R(g,s)=gF_R\times S\) to the corresponding translated window, carries the decoded point fields to translated point fields, and preserves types and all update rules. Therefore

\[
\Phi(\gamma\omega)=\gamma\P
