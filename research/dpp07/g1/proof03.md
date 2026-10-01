# A common iid monotone coupling at the Fuglede–Kadison parameter

STATUS: Complete proof; the mathematical scope and review record are stated in README.md.

## 1. Statement and conventions

Let \(\Gamma\) be any countable group, acting on itself by left translation. Fix a bounded complex Hermitian operator \(0\le Q\le I\) on \(\ell^2(\Gamma)\) commuting with this action. Write
\[
\tau(A)=\langle A\delta_e,\delta_e\rangle,
\qquad p=\operatorname{FK}(Q)=\exp\!\int_{[0,1]}\log\lambda\,d\nu_Q(\lambda),
\]
where \(\nu_Q\) is the spectral distribution for \(\tau\), and \(\exp(-\infty)=0\). Denote by \(\mu_Q\) the determinantal law characterized by
\[
\mu_Q\{B\subseteq Y\}=\det Q[B]\qquad(B\subset\Gamma\text{ finite}).
\]
The finite dimensional determinant probabilities are consistent and determine this law. A configuration is identified with its occupied subset of \(\Gamma\).

For \(p=0\) only, assume **H**: this fixed \(\mu_Q\) has a total Borel, everywhere equivariant sampler from the regular iid source \([0,1]^\Gamma\). No H is assumed when \(p>0\).

Then there is a total Borel map
\[
F_Q:[0,1]^\Gamma\longrightarrow\{0,1\}^\Gamma\times\{0,1\}^\Gamma
\]
which commutes with every group translation on every input and which, under iid uniform input, produces
\[
X\sim\operatorname{Ber}(p)^\Gamma,\qquad Y\sim\mu_Q,\qquad X\subseteq Y.
\]
The inclusion can be arranged on every input. The kernel is fixed throughout; no joint measurable dependence on all kernels and no finite coding radius are claimed.

We first treat \(0<p<1\). All rates below are real and all Hilbert space norms and orthogonal projections are the complex ones.

## 2. The operator path

For \(t>0\), define
\[
a_t=\frac p{\operatorname{FK}(Q+tI)},\quad
K_t=a_t(Q+tI),\quad r_t=\tau((Q+tI)^{-1}).
\]
Differentiation of the bounded spectral integrals on compact subsets of \((0,\infty)\) gives
\[
a'_t=-r_ta_t,\qquad K'_t=a_tI-r_tK_t. \tag{1}
\]
Put \(M=\|Q\|\). Since \(p>0\), the spectral logarithm is integrable and \(M>0\). For \(t>0\),
\[
\log\frac{\operatorname{FK}(Q+tI)}p
=\int\log(1+t/\lambda)\,d\nu_Q(\lambda)
\ge\log(1+t/M).
\]
Thus \(a_t(M+t)\le M\le1\), while \(K_t\ge a_ttI>0\). If \(M=1\), equality in the integral bound forces \(\nu_Q=\delta_1\), hence \(Q=I\) by faithfulness of the group trace, contrary to \(p<1\). Therefore \(\|K_t\|<1\). Both spectral gaps are uniform when \(t\) ranges in a compact subset of \((0,\infty)\).

Monotone convergence of the logarithmic integral at zero and expansion at infinity show
\[
K_t\longrightarrow Q\ (t\downarrow0),\qquad K_t\longrightarrow pI\ (t\to\infty)
\quad\text{in operator norm}. \tag{2}
\]
For any finite \(B\), the derivative of a determinant, or multilinearity in its rows, gives
\[
\frac d{dt}\det K_t[B]
=a_t\sum_{i\in B}\det K_t[B\setminus\{i\}]
-r_t|B|\det K_t[B]. \tag{3}
\]
Empty determinants equal one.

## 3. A continuous version of full exterior conditional odds

Let \(L\) be bounded with \(0<lI\le L\le uI<\infty\). If \(x\notin\eta\), set
\[
\lambda_L(x,\eta)=\inf_{h\in\ell^2(\eta)}
\langle L(\delta_x+h),\delta_x+h\rangle
=\|(I-\Pi_\eta^L)L^{1/2}\delta_x\|^2, \tag{4}
\]
where \(\Pi_\eta^L\) projects onto \(L^{1/2}\ell^2(\eta)\). This range is closed because \(L^{1/2}\) is bounded below. With \(D_\eta\) the coordinate projection, the shorted operator is
\[
\mathsf S_\eta(L)
=L-LD_\eta(D_\eta LD_\eta+I-D_\eta)^{-1}D_\eta L. \tag{5}
\]
Its \(x\)-diagonal is (4). In particular, \(l\le\lambda_L(x,\eta)\le u\), and \(\lambda_L\) decreases when \(\eta\) increases.

If configurations converge in the product topology, their coordinate projections converge strongly. The middle operators in (5) have common lower bound \(\min(l,1)I\), so their inverses converge strongly as well: use \(A_n^{-1}-A^{-1}=A_n^{-1}(A-A_n)A^{-1}\). Formula (5) proves product continuity. The same argument proves joint continuity when \(L\) varies in norm within common positive bounds. The formula is Borel and covariant under unitary translations.

For a gapped positive contraction \(K\), put \(L=K(I-K)^{-1}\). In a finite set, the generating determinant gives
\[
\mathbb P(X=\eta)=\det(I-K)\det L[\eta].
\]
Taking the ratio between \(\eta\cup\{x\}\) and \(\eta\) and using the Schur complement proves that the conditional occupation probability is
\[
q(x,\eta)=\frac{\lambda_L(x,\eta)}{1+\lambda_L(x,\eta)}. \tag{6}
\]
Here and below the argument of \(q\) or \(\lambda\) excludes \(x\).

The same formula is a version of the conditional probability given the entire exterior on \(\Gamma\). Indeed, exhaust \(\Gamma\) by finite sets \(F_n\) containing \(x\). The marginal kernel is \(P_{F_n}KP_{F_n}\). Extend it by a fixed scalar in the spectral gap on \(F_n^c\); these extended kernels converge strongly to \(K\), have common gaps, and their \(L\)-operators converge strongly to \(L\) by continuous functional calculus. Apply (5), using also \(D_{\eta\cap F_n}\to D_\eta\) strongly. This gives convergence of every finite conditional formula, for every exterior \(\eta\), to (6). For a sample from \(\mu_K\), the finite conditional probabilities form a bounded martingale; its limit is conditioning on the whole exterior. This identifies (6) almost surely without sacrificing its all-input continuous definition.

Apply this to \(L_t=K_t(I-K_t)^{-1}\). The variational problem with every site other than \(x\) available gives
\[
\lambda_{L_t}(x,\Gamma\setminus\{x\})
=\frac1{\langle L_t^{-1}\delta_x,\delta_x\rangle}
=\frac{a_t}{r_t-a_t}. \tag{7}
\]
For the first equality minimize the quadratic form subject to the \(x\)-coordinate being one; the minimizer is \(L_t^{-1}\delta_x/\langle L_t^{-1}\delta_x,\delta_x\rangle\). For the second use \(L_t^{-1}=K_t^{-1}-I\) and constant diagonals. In particular \(r_t-a_t>0\).

Define, for vacant \(x\),
\[
c_t(x,\eta)=(r_t-a_t)\lambda_{L_t}(x,\eta)-a_t
=\frac{r_tq_t(x,\eta)-a_t}{1-q_t(x,\eta)}. \tag{8}
\]
These rates are nonnegative by (7), bounded, covariant, and decreasing in the occupied exterior. Their full rate is zero at an occupied source.

Reverse time using
\[
t_s=s^{-1}-1,\qquad
\rho_s(x,\eta)=s^{-2}c_{t_s}(x,\eta)\quad(x\notin\eta),
\qquad b_s(x,\eta)=\mathbf1_{\{x\notin\eta\}}\rho_s(x,\eta). \tag{9}
\]
The distinction between the vacant-site rate \(\rho\) and the full rate \(b\) will be used throughout. When a vacant-site rate is written on an unrestricted configuration, its argument means that configuration with the source deleted.

Let \(\nu_s=\mu_{K_{t_s}}\) for \(s>0\). For the inclusion monomial \(f_B(\eta)=\mathbf1_{\{B\subseteq\eta\}}\), conditional expectation at \(i\in B\) gives
\[
\mathbb E_{\nu_s}\!\left[
\mathbf1_{\{B\setminus\{i\}\subseteq\eta\}}\mathbf1_{\{i\notin\eta\}}
c_{t_s}(i,\eta)\right]
=r_{t_s}\det K_{t_s}[B]-a_{t_s}\det K_{t_s}[B\setminus\{i\}].
\]
Together with (3) and \(dt_s/ds=-s^{-2}\), this proves
\[
\frac d{ds}\nu_s(f)=\nu_s(\mathcal L_sf),\qquad
\mathcal L_sf(\eta)=\sum_x b_s(x,\eta)
[f(\eta\cup\{x\})-f(\eta)] \tag{10}
\]
for every cylinder function, since inclusion monomials span their vector space. Only finitely many terms in the generator act on a cylinder function.

## 4. Sensitivity by covariant transport

Fix \(L\) as above and \(\eta\subseteq\zeta\). Set
\[
D=D_{\zeta\setminus\eta},\quad
T=(I-\Pi_\eta^L)L^{1/2}D=V|T|,\quad
P=VV^*=\Pi_\zeta^L-\Pi_\eta^L.
\]
The initial space of \(V\) is contained in \(\ell^2(\zeta\setminus\eta)\). For \(x\notin\zeta\),
\[
\lambda_L(x,\eta)-\lambda_L(x,\zeta)
=\|V^*L^{1/2}\delta_x\|^2. \tag{11}
\]
Every vector in the range of \(P\) belongs to \(L^{1/2}\ell^2(\zeta)\). Consequently \(PL^{-1/2}\delta_x=0\) for \(x\notin\zeta\), and for any scalar \(\ell>0\),
\[
V^*L^{1/2}\delta_x=V^*L^{-1/2}(L-\ell I)\delta_x.
\]
For \(x\notin\zeta\), \(y\in\zeta\setminus\eta\), put
\[
w(x,y)=|\langle V^*L^{-1/2}(L-\ell I)\delta_x,\delta_y\rangle|^2,
\]
and put \(w=0\) elsewhere. Its row sum equals (11), while both row sums and column sums are bounded by
\[
\kappa(L)=\|L^{-1}\|\,\|L-\ell I\|^2. \tag{12}
\]
For columns this follows from
\[
\sum_{x\notin\zeta}w(x,y)
=\|(I-D_\zeta)(L-\ell I)L^{-1/2}V\delta_y\|^2\le\kappa(L).
\]
All these coefficients are covariant and Borel. For example the polar part is the strong limit of \(T(T^*T+n^{-1}I)^{-1/2}\).

For arbitrary configurations \(U,V\), compare each to \(U\cap V\). At a source vacant in both, use the two preceding transports; at a source occupied in precisely one, add a diagonal term bounded by the supremum vacant-site rate. At a source occupied in both no term is needed. Taking \(\ell=p/(1-p)\), we obtain nonnegative covariant Borel coefficients supported on mismatched target sites such that
\[
|b_s(x,U)-b_s(x,V)|\le\sum_{y:U_y\ne V_y}A_s(x,y;U,V), \tag{13}
\]
with every row and column sum at most
\[
C_s=s^{-2}\left[\overline c_{t_s}
+2(r_{t_s}-a_{t_s})\kappa(L_{t_s})\right],\qquad
\overline c_t=\sup_{x\notin\eta}c_t(x,\eta). \tag{14}
\]
For every jointly invariant random pair \((U,V)\), countable mass transport gives
\[
\mathbb E|b_s(e,U)-b_s(e,V)|
\le C_s\mathbb P(U_e\ne V_e). \tag{15}
\]
Indeed, translating the summand for \((e,y)\) by \(y^{-1}\), summing, and using Tonelli changes the outgoing sum into the incoming sum at \(e\); the latter is at most \(C_s\mathbf1_{\{U_e\ne V_e\}}\). This uses no amenability.

## 5. The scalar entrance

Let \(u=1/t\), \(m=\tau(Q)\), and \(\ell=p/(1-p)\). Norm functional calculus at \(u=0\) gives
\[
\begin{split}
a_t&=pu-pmu^2+O(u^3),&r_t&=u-mu^2+O(u^3),\\
K_t&=pI+pu(Q-mI)+O(u^2),&
L_t&=\ell I+uG+O(u^2),\\
G&=\frac p{(1-p)^2}(Q-mI).&&
\end{split} \tag{16}
\]
The remainders are operator-norm remainders. Equivariance and \(\tau(G)=0\) give \(G_{xx}=0\) at every site. In (5), at a vacant site the direct diagonal is \(\ell+O(u^2)\), and the off-diagonal vector \(D_\eta L_t\delta_x=uD_\eta G\delta_x+O(u^2)\) has norm \(O(u)\), uniformly in \(\eta,x\). The inverses in (5) are uniformly bounded. Therefore
\[
\lambda_{L_t}(x,\eta)=\ell+O(u^2)\quad\text{uniformly in }x\notin\eta. \tag{17}
\]
Substitute this into (8). The coefficients of both \(u\) and \(u^2\) vanish, since \((1-p)\ell=p\). Thus
\[
\overline c_t=O(u^3),\qquad
(r_t-a_t)\kappa(L_t)=O(u^3). \tag{18}
\]
As \(u=s/(1-s)\), the time-changed rates and \(C_s\) are \(O(s)\). Define \(\rho_0=b_0=0\), \(C_0=0\), and \(\nu_0=\operatorname{Ber}(p)^\Gamma\). On every \([0,S]\), \(S<1\), the vacant-site rates are jointly continuous and bounded, \(C\) is integrable, and \(\nu_s\) is weakly continuous. The positive finite cylinder probabilities are continuous and bounded away from zero for any fixed cylinder on this compact interval. Formula (10) extends in its integral form through zero, since its right side tends to zero. These observations verify all hypotheses of the construction below.

## 6. Direct construction from independent noise

We give the probabilistic argument on a fixed \([0,S]\), with rate bound \(B<\infty\). It applies to any covariant nonnegative vacant-site rates \(\rho\) which decrease in the exterior, are jointly continuous on this compact interval and configuration space, and whose full rates \(b\) satisfy (15) for an integrable \(C\). Suppose invariant laws \(\nu_s\) have positive finite cylinder probabilities, start at \(\operatorname{Ber}(p)^\Gamma\), and satisfy (10) in integral form. The continuous rates and weakly continuous laws used here suffice for all conditional rates below.

Start with an iid Bernoulli field \(\xi\) and, independently, iid Poisson random measures \(N_x\) on \((0,S]\times[0,\infty)\) of intensity \(ds\,du\). Use the filtration generated by \(\xi\) and all the Poisson points up to the current time. Independence of the drivers is an input to this construction.

For an adapted pure-birth path \(V\), define
\[
\Phi(V)_x(t)=\xi_x\vee
\mathbf1\left\{\exists(r,u)\in N_x:\ 0<r\le t,
\ u\le b_r(x,V_{r-})\right\}. \tag{19}
\]
Only finitely many points with \(u\le B\) occur at any one site on this interval. Put \(V^0_t=\xi\) and \(V^{k+1}=\Phi(V^k)\). Each iterate is an adapted, equivariant Borel function of the same inputs, with coordinatewise càdlàg increasing paths.

If \(U,V\) are jointly invariant adapted paths, the event that \(\Phi(U)\) and \(\Phi(V)\) disagree at the root at some time up to \(t\) requires a root proposal between their two thresholds. Poisson compensation and (15) imply
\[
\mathbb P\bigl(\Phi(U)_e\not\equiv\Phi(V)_e\text{ on }[0,t]\bigr)
\le\int_0^t C_r\,
\mathbb P\bigl(U_e\not\equiv V_e\text{ on }[0,r]\bigr)\,dr. \tag{20}
\]
The left-limit states in the integrand are predictable. Their mismatch is bounded by the displayed path mismatch. Countable independent Poisson measures have no point at a fixed deterministic time; all iterates jump only at proposals, so the harmless choice of endpoint in this bound does not affect the integral.

Set \(D_k(t)=\mathbb P(V^{k+1}_e\not\equiv V^k_e\text{ on }[0,t])\) and \(A(t)=\int_0^t C_rdr\). Since \(D_0\le1\), (20) yields
\[
D_k(t)\le\frac{A(t)^k}{k!}. \tag{21}
\]
Hence, almost surely, the whole path at each coordinate stabilizes as \(k\to\infty\). This holds simultaneously at all sites and all rational compact horizons. For probabilistic estimates take the coordinatewise pointwise limsup as an adapted version of the limit \(Z\), and take the coordinatewise limsup of the left limits for its predictable integrands. On the probability-one stabilization event these are the limiting path and its left limits. Thus \(Z\) is almost surely increasing and coordinatewise càdlàg, and is jointly invariant with its drivers. Completing the filtration by null events causes no change to the independent Poisson compensation identities.

To verify the fixed point without making any assertion about threshold ties, apply the compensation estimate to \(V^k,Z\). For each \(r\), their root paths agree eventually almost surely, and the bound by \(C_r\) is integrable. Dominated convergence in (20) gives \(\Phi(V^k)\to\Phi(Z)\) in probability for root path equality, whereas \(V^{k+1}\to Z\) almost surely. Thus \(Z=\Phi(Z)\) almost surely, simultaneously over all coordinates and compact horizons. The same estimate and Gronwall give uniqueness among jointly invariant adapted solutions with these drivers and initial field. Existence, rather than uniqueness, is what will identify the marginals below.

## 7. Finite dependency envelopes and the backward-chain lemma

Choose finite symmetric \(D_n\uparrow\Gamma\) containing \(e\). At a vacant source \(x\), define
\[
\begin{split}
\overline\rho_s^n(x;L,U)
&=\rho_s\bigl(x,(L\cap xD_n)\setminus\{x\}\bigr),\\
\underline\rho_s^n(x;L,U)
&=\rho_s\bigl(x,((U\cap xD_n)\cup(\Gamma\setminus xD_n))\setminus\{x\}\bigr).
\end{split} \tag{22}
\]
At each proposal at \(x\), a vacant lower coordinate is born if its mark is below \(\underline\rho^n\), and a vacant upper coordinate is born if below \(\overline\rho^n\). Both start at \(\xi\). These are cross-dependent envelope rates: the lower threshold uses the upper exterior, and the upper threshold uses the lower exterior.

Here is a precise construction and comparison principle for these finite dependency systems. Retain only proposals with marks at most \(B\), and put \(d=|D_n|\). Almost surely no two proposals, whether at the same or at different sites, have the same time: each fixed finite-site Poisson family has diffuse times, and there are countably many site pairs. A chain of length \(j\) from a site \(x\) consists of proposals at sites \(x_0=x,x_1,\ldots,x_{j-1}\), with \(x_{i+1}\in x_iD_n\), at strictly decreasing times in \((0,S]\). The expected number of such chains is at most
\[
\frac{(BdS)^j}{j!}. \tag{23}
\]
For a fixed site sequence this is the Poisson factorial-moment integral over the time simplex. The formula remains valid if sites repeat, since strictly decreasing times select distinct points. There are at most \(d^{j-1}\le d^j\) site sequences. In particular the probability of an infinite backward chain is zero. This holds simultaneously for all starting sites. At each node there are finitely many earlier proposals in the finitely many dependency sites. The dependency tree therefore has finite depth and finitely many vertices almost surely. Recursion from its initial states defines each queried coordinate path. This constructs \((L^n,U^n)\) equivariantly and in the common filtration, without a finite total spatial rate.

The same recursion proves \(L^n\le U^n\). When a source is vacant in both and the local order holds, the padded lower exterior contains the truncated upper exterior, so \(\underline\rho^n\le\overline\rho^n\). If a source is already occupied only in the upper process, subsequent births also preserve order.

More generally suppose a process \(W\), driven by the same proposals, has at each site a threshold between the two envelope thresholds whenever \(L^n\le W\le U^n\) on \(xD_n\) immediately before that proposal. Then \(L^n\le W\le U^n\) for all times. To prove this on the infinite graph, argue by a purported first violation at a fixed site. A violation can only occur at a proposal there, and it cannot occur if local order was intact just before it. Thus some dependency site had an earlier violation. Take its first violation and repeat. The initial order prevents this chain from reaching time zero. It would therefore give an infinite strictly decreasing proposal chain, which has probability zero by (23). This argument does not assume that the original decreasing birth rates define an attractive process.

In particular \(W=Z\) satisfies the required bracket: local order gives
\[
(L^n\cap xD_n)\setminus\{x\}
\subseteq Z\setminus\{x\}
\subseteq((U^n\cap xD_n)\cup(\Gamma\setminus xD_n))\setminus\{x\},
\]
and the rate decreases in its exterior. At a source where an order violation could be created the relevant coordinates are vacant, so this is the needed comparison. Therefore
\[
L^n_t\subseteq Z_t\subseteq U^n_t\qquad(0\le t\le S) \tag{24}
\]
simultaneously at all sites, almost surely.

Joint continuity on the compact time/configuration space implies
\[
\omega_n=\sup\{|\rho_s(e,\eta)-\rho_s(e,\zeta)|:
0\le s\le S,\ e\notin\eta\cup\zeta,\ \eta|_{D_n}=\zeta|_{D_n}\}\longrightarrow0. \tag{25}
\]
Let \(p_n(t)\) be the probability that the two envelope root paths disagree anywhere on \([0,t]\). The first root disagreement can only be created when both root sites are vacant. At such a time the threshold gap is bounded by
\[
2\omega_n+|b_s(e,L^n_{s-})-b_s(e,U^n_{s-})|.
\]
Compensation and (15), applied to the jointly invariant pair of envelopes, give
\[
p_n(t)\le2t\omega_n+\int_0^tC_sp_n(s)ds,
\qquad p_n(S)\le2S\omega_n e^{A(S)}\longrightarrow0. \tag{26}
\]

## 8. Exact marginal identification by finite conditional chains

Fix a finite set \(F\). For \(x\in F\), \(\xi_x=0\), define
\[
\widehat\rho_{s,F,x}(\xi)
=\mathbb E_{\nu_s}[\rho_s(x,X)\mid X_F=\xi]. \tag{27}
\]
Positive finite cylinder probabilities make this defined for every \(\xi\). It is a continuous bounded function of \(s\): its numerator is the integral of a jointly continuous function times a cylinder indicator, and its denominator is continuous and positive. Its bound is \(B\).

Apply (10) to functions depending on \(F\), and condition on \(X_F\). The finite probability vector \(\nu_s|_F\) satisfies the forward equation of the pure-birth chain with rates (27) and initial law \(\operatorname{Ber}(p)^F\). A finite bounded continuous-rate matrix has a unique solution to its forward integral equation, as follows directly by Gronwall for the difference of two solutions. Construct a chain \(V^F\) from the initial field \(\xi|_F\) and the already chosen proposals \(N_x\), \(x\in F\), accepting at threshold (27). Finite chronological recursion defines it, and its usual one-step conditional transition computation gives the forward equation. Consequently
\[
\mathcal L(V^F_s)=\nu_s|_F. \tag{28}
\]
This is a joint coupling of \(V^F,L^n,U^n,Z\) using precisely the same initial field and proposals.

Define the dependency boundary
\[
\partial_nF=\{x\in F:xD_n\not\subset F\}.
\]
At an interior site \(x\notin\partial_nF\), if \(L^n\le V^F\le U^n\) on \(xD_n\) immediately before a proposal and \(V^F_x=0\), every completion of \(V^F_F\) to a full exterior lies between the truncated lower exterior and padded upper exterior in (22). Antimonotonicity, followed by conditional expectation, gives
\[
\underline\rho_s^n(x;L^n,U^n)
\le\widehat\rho_{s,F,x}(V^F)
\le\overline\rho_s^n(x;L^n,U^n). \tag{29}
\]
Thus a first order violation at an interior site must be preceded by an earlier violation at a dependency site. Iterating either reaches \(\partial_nF\) or gives an infinite backward chain. The latter has probability zero by (23).

For finite \(B_0\subset F\), let \(k=k(F,n,B_0)\) be the minimum dependency-graph distance from \(B_0\) to \(\partial_nF\), with distance infinity if there is no such path. Tracing an order violation backwards gives at least \(k\) chronologically ordered proposals. Therefore the probability that any site in \(B_0\) violates either order at any time up to \(S\) is at most
\[
\varepsilon_{F,n,B_0}(S)
=|B_0|\min\!\left\{1,\sum_{j\ge k}\frac{(BdS)^j}{j!}\right\}. \tag{30}
\]
Interpret the sum as zero for \(k=\infty\). The estimate deliberately permits arbitrary failures on the dependency boundary. No invariance of the finite chain is being assumed.

At a time \(s\le S\), if the order holds at \(B_0\) and the two envelopes agree there, (24) implies \(V^F_s|_{B_0}=Z_s|_{B_0}\). The coupling inequality and (26), (28), (30) yield
\[
\|\mathcal L(Z_s|_{B_0})-\nu_s|_{B_0}\|_{\mathrm{TV}}
\le |B_0|p_n(S)+\varepsilon_{F,n,B_0}(S). \tag{31}
\]
First fix \(n,S,B_0\) and exhaust \(\Gamma\) by finite \(F\). Every fixed finite dependency neighborhood of \(B_0\) eventually lies in \(F\), so \(k\to\infty\) and the boundary term tends to zero. Then let \(n\to\infty\) and use (26). This proves \(Z_s\sim\nu_s\) for each \(s\le S\), including the initial time. Finite groups cause no exception: take \(F=\Gamma\), making the boundary term zero.

This completes the finite-flow construction entirely on the original independent noise space. No weak path limit, compensator passage through weak convergence, or Poisson completion is used.

## 9. A single path, endpoint limits, and totalization

For the rates (9), take one iid field of Poisson measures on \((0,1)\times[0,\infty)\), independent of \(\xi\). Define (19) and every Picard iterate on the whole interval \([0,1)\). Local boundedness makes the restriction to each compact interval the construction already proved. The iterates are independent of the chosen horizon; their limits therefore give one path. Intersecting the probability-one assertions over countably many rational \(S<1\) gives
\[
Z_0\sim\operatorname{Ber}(p)^\Gamma,\qquad
Z_s\sim\mu_{K_{t_s}}\quad(0<s<1),
\qquad Z_s\subseteq Z_{s'}\ (s\le s'). \tag{32}
\]
Define
\[
X=Z_0,\qquad Y=\bigcup_{s\in\mathbb Q,\ 0\le s<1}Z_s.
\]
For each finite \(B\), monotone convergence and (2) give
\[
\mathbb P(B\subseteq Y)
=\lim_{s\uparrow1}\det K_{t_s}[B]=\det Q[B]. \tag{33}
\]
These inclusion probabilities determine all finite cylinder probabilities by inclusion-exclusion. Hence \(Y\sim\mu_Q\) and \(X\subseteq Y\).

If \(\varepsilon I\le Q\le(1-\varepsilon)I\), the rates and transport bounds extend continuously through \(s=1\): the endpoint operators and inverses in the displayed formulas are uniformly bounded. The same construction on \([0,1]\) then gives \(Y=Z_1\sim\mu_Q\). Without this gap only the increasing union is needed.

For clarity, all measurability and exceptional-input details can be made explicit. A single uniform label at each site can be split, by its binary digits with a fixed convention on dyadic rationals, into countably many independent uniforms. These generate the Bernoulli bit and independent Poisson measures on the countably many mark strips \([j,j+1)\). Exponential waiting times and uniform marks give Borel decoders. Assign the empty measure at any label where this decoding fails to produce the stipulated locally finite point measure. This sitewise convention is total and translation covariant, and affects only a null set under the product law.

Each Picard iterate is a total Borel covariant map on the decoded configuration and point-measure space: each coordinate uses only a countable list of proposal points and Borel comparisons, with finitely many relevant points on each compact interval. The property that every coordinate's iterates eventually agree as entire paths on every rational compact horizon is Borel. One can test equality of these càdlàg binary paths at rational times and at the horizon. This property is invariant under translation. It holds almost surely by (21). On this set take the stabilized coordinate paths. They are càdlàg and increasing on every compact interval. The condition that they satisfy (19) is also Borel and invariant: test the graphical equation at all coordinates and rational times, using the countable proposal lists. It holds almost surely by the fixed-point argument. Countable intersections retain both Borelness and invariance.

On this invariant conull set output the pair from (32)–(33); off it output \((\varnothing,\varnothing)\). This is a total Borel, everywhere equivariant map, and inclusion holds on every input. Enumerations used to test countably many properties do not select an orbit representative; each tested property is imposed at every coordinate, and the construction itself uses only covariant rates and translated proposals.

Finally, if \(p=0\), use H to sample \(Y\) and set \(X=\varnothing\). If \(p=1\), the nonnegative spectral function \(-\log\lambda\) has integral zero, so \(\nu_Q=\delta_1\). Faithfulness implies \(Q=I\), and the constant map \(X=Y=\Gamma\) works. This proves the stated result for all cases under exactly the declared use of H.
