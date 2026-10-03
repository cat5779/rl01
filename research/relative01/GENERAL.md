# A relative prescribed-rate process under a weak convolution background

## 1. Conventions and operator estimates

Let Gamma be any countable group, with left action \((\lambda_\gamma f)(i)=f(\gamma^{-1}i)\). Use
\[
(a*c)(g)=\sum_k a(k)c(k^{-1}g),\qquad
(T_af)(i)=\sum_g a(g)f(ig)=\sum_j a(i^{-1}j)f(j).
\]
Thus \(T_aT_c=T_{a*c}\), and every \(T_a\) commutes with the left action, without requiring Gamma to be commutative.

Assume the following hypotheses: \(v>0\) is symmetric, \(\sum v=1\), \(v^{*3}\le Mv\); \(b\in\ell^1(\Gamma;\mathbb C)\), \(b(g^{-1})=\overline{b(g)}\), and \(|b|*v\le\kappa v\); \(\delta>0\) and \(\kappa+\delta M\le1/8\). Put
\[
V=T_v,\quad h=v*v,\quad H=V^2=VV^*=T_h,\quad
B=T_b,\quad C=I/2+B,\quad K_t=C+\delta tH.
\]
Summing the positive inequalities gives \(M\ge1\) and \(\|b\|_1\le\kappa\). Young's bound gives \(\|V\|\le1\), \(0\le H\le I\), \(\|B\|\le\kappa\), and
\[
\|B+\delta tH\|\le\kappa+\delta\le1/8.
\]
Hence every \(K_t\) lies between \(3I/8\) and \(5I/8\), in particular has the required common gap \(\varepsilon=1/4\). There is no assumption that \(B\) commutes with \(H\).

For a configuration \(x\), define
\[
G_{t,x}=(K_t-D_{x^c})^{-1},\qquad
a_i(t,x)=-\delta(1-x_i)\operatorname{Re}(HG_{t,x})_{ii}. \tag{1}
\]
We construct the required relative process from its supplied initial \(X\sim\mu_C\).

## 2. Absolute convolution majorant and uniform finite-volume convergence

Let \(R_x=2D_x-I\), \(T_t=B+\delta tH\), and let \(u=|b|+\delta h\) be a nonnegative convolution kernel. Its sum
\[
m:=\|u\|_1=\|b\|_1+\delta\le\kappa+\delta\le1/8.
\]
The inverse has uniformly convergent Neumann expansion
\[
G_{t,x}=2\sum_{n\ge0}(-2)^n(R_xT_t)^nR_x. \tag{2}
\]
Because \(|T_t(i,j)|\le u(i^{-1}j)\), define the entrywise majorant
\[
\mathcal R=2\sum_{n\ge0}2^nT_u^n,\qquad
r=2\sum_{n\ge0}2^nu^{*n}.
\]
Then
\[
|G_{t,x}(i,j)|\le r(i^{-1}j),\qquad
|(HG_{t,x})(i,j)|\le (h*r)(i^{-1}j), \tag{3}
\]
\[
\|G_{t,x}\|\le\frac2{1-2m}\le4,\qquad
\|r\|_1=\frac2{1-2m}\le4. \tag{4}
\]
Absolute values replace each sign/complex walk factor by its nonnegative \(u\) factor. Products are taken in the displayed order. The kernel \(r\) is symmetric under inversion, as \(u\) is; **\(h*r\) need not be symmetric and is not treated as such**.

For finite \(\Lambda\), compress \(B,H,K_t\) to \(\Lambda\) and use the corresponding inverse \(G^\Lambda\). The compressions have the same gap and walk majorants. For fixed \(i\),
\[
\sup_{t,x}|(H^\Lambda G^\Lambda_{t,x})_{ii}-(HG_{t,x})_{ii}|
\longrightarrow0\quad(\Lambda\uparrow\Gamma,\ i\in\Lambda). \tag{5}
\]
For a fixed Neumann index \(n\), the finite-volume expression keeps exactly the walks whose intermediate sites stay in \(\Lambda\). The omitted mass is bounded by the countable nonnegative walk sum with one \(h\) and \(n\) factors \(u\), whose total mass is \(m^n\); the omitted mass tends to zero by monotone convergence. This convergence is uniform in configurations, complex phases, and time. The remaining tail is bounded by \(2\sum_{n>N}(2m)^n\). The same argument gives uniform convergence of each fixed inverse entry.

Finite-volume diagonal expressions are jointly continuous in time and the finite configuration. Their uniform limit is therefore jointly continuous on the compact space \([0,1]\times\{0,1\}^{\Gamma}\). This proves the infinite-volume continuity needed below; it is stronger than a merely strong-operator pointwise limit.

## 3. Nonnegative finite currents for all compressions and all inputs

We first prove the finite weighted-positivity lemma, including complex phases. Suppose \(L\) is \(\varepsilon\)-gapped and a nonzero vector \(w\) obeys
\[
\sum_{j\ne i}|L_{ij}||w_j|\le(\varepsilon/2)|w_i|. \tag{6}
\]
Then for every upward edge the current
\[
J_w(S,i)=-p_L(S)\operatorname{Re}
(ww^*(L-D_{S^c})^{-1})_{ii},\qquad i\notin S,
\]
is nonnegative. If \(w_i=0\), (6) forces couplings from that coordinate into the support of \(w\) to vanish; the row of \(ww^*\) is zero. On the support put
\[
z_i=((L-D_{S^c})^{-1}w)_i/w_i,\quad
d_i=L_{ii}-\mathbf1_{i\notin S},\quad
A_{ij}=L_{ij}w_j/w_i\quad(i\ne j).
\]
Then \((D+A)z=\mathbf1\), \(|d_i|\ge\varepsilon\), and the absolute row sum of \(A\) is at most \(\varepsilon/2\). Neumann inversion in the maximum norm gives \(\|z\|_\infty\le2/\varepsilon\). Consequently
\(\operatorname{Re}(d_i z_i)=1-\operatorname{Re}\sum_{j\ne i}A_{ij}z_j\ge0\).
For \(i\notin S\), \(d_i<0\), so
\(\operatorname{Re}(w_i\overline{((L-D_{S^c})^{-1}w)_i})=|w_i|^2\operatorname{Re}z_i\le0\).
This proves the lemma; it requires neither normalization of \(w\) nor commutation.

For \(g\in\Gamma\), let \(w_g^\Lambda=P_\Lambda V\delta_g\), with positive coordinates \(v(i^{-1}g)\). By the exact convolution convention,
\[
\begin{aligned}
\sum_{\substack{j\in\Lambda\\j\ne i}}
 |(K_t^\Lambda)_{ij}|(w_g^\Lambda)_j
&\le ((|b|+\delta h)*v)(i^{-1}g)\\
&\le(\kappa+\delta M)v(i^{-1}g)
\le\tfrac18(w_g^\Lambda)_i .
\end{aligned} \tag{7}
\]
Thus (6) applies with \(\varepsilon=1/4\). Moreover
\[
H^\Lambda=\sum_{g\in\Gamma}w_g^\Lambda(w_g^\Lambda)^*. \tag{8}
\]
Indeed symmetry of \(v\) identifies its entries with \((v*v)(i^{-1}j)\). The sum converges in finite-dimensional trace norm because
\(\sum_g\|w_g^\Lambda\|_2^2=\operatorname{tr}H^\Lambda<\infty\).

The current is linear in the Hermitian direction. Summing the positive currents in (8) proves
\[
a_i^\Lambda(t,x)
=-\delta(1-x_i)\operatorname{Re}(H^\Lambda G^\Lambda_{t,x})_{ii}\ge0. \tag{9}
\]
The finite kernel is not falsely assumed to commute with any of the column directions. Passing (9) through (5) proves \(a_i\ge0\) for every infinite input.

Using (4),
\[
0\le a_i(t,x)\le\delta\|H\|\|G_{t,x}\|\le4\delta=:B_0. \tag{10}
\]
It is jointly continuous by Section 2 and is covariant by left conjugation of all operators.

Define the intrinsic vacant-site rate
\[
c_i(t,x)=-\delta\operatorname{Re}(HG_{t,x^{i,0}})_{ii}. \tag{11}
\]
Here \(x^{i,0}\) forces site \(i\) vacant. This rate is independent of \(x_i\), nonnegative and bounded by \(B_0\); the actual rate is \((1-x_i)c_i(t,x)=a_i(t,x)\). Forcing vacancy is essential when taking envelope infima over a box that may contain both values at the updating site.

## 4. Uniform summable worst-case influences

If only coordinate \(j\) is flipped, \(M'=M+\sigma e_je_j^*\), \(\sigma=\pm1\). Both inverses exist. Sherman-Morrison and its diagonal identity give
\[
G'-G=-\frac{\sigma}{1+\sigma G_{jj}}Ge_je_j^*G,\qquad
|(1+\sigma G_{jj})^{-1}|=|1-\sigma G'_{jj}|\le1+\|G'\|\le5. \tag{12}
\]
This denominator bound uses actual invertibility and (4), not an unproved infinite conditional probability.

For \(j\ne i\), use (12) on the configurations with \(i\) forced vacant. Define
\[
q(g)=5\delta(h*r)(g)r(g^{-1}),\qquad
I_0:=\sum_gq(g).
\]
Then
\[
\sup_{t,x}|c_i(t,x^j)-c_i(t,x)|\le q(i^{-1}j),\qquad
I_0\le5\delta\|h*r\|_1\|r\|_\infty
\le\frac{20\delta}{(1-2m)^2}<\infty. \tag{13}
\]
The self influence of \(c_i\) is zero. No symmetry of \(h*r\), and no commutation of \(B,H\), is needed: for every summable function \(q\), the regular kernel \(q(i^{-1}j)\) has the same finite row and column sums, by the group bijections.

Telescoping finitely many flips and then taking a product limit gives
\[
|c_i(t,x)-c_i(t,y)|
\le\sum_{j\ne i}q(i^{-1}j)\mathbf1_{x_j\ne y_j}. \tag{14}
\]
Continuity justifies the limit, and the series is absolutely convergent. The actual rates satisfy (14) plus \(B_0\mathbf1_{x_i\ne y_i}\). Thus every requested worst-case influence is summable, uniformly in time and configuration.

## 5. Exact cylinder continuity equation

For a finite gapped Hermitian matrix \(L\), the exact atom formula and derivative in a Hermitian direction \(T\) are
\[
p_L(S)=(-1)^{|S^c|}\det(L-D_{S^c}),\qquad
D p_L[T](S)=p_L(S)\operatorname{tr}(T(L-D_{S^c})^{-1}).
\]
The inverse exists with norm at most \(\varepsilon^{-1}\), by writing \(L-D_{S^c}=(L-I/2)+(I/2-D_{S^c})\).
The upward signed current
\[
J_T(S,i)=-p_L(S)\operatorname{Re}(T(L-D_{S^c})^{-1})_{ii}
\]
has divergence \(Dp_L[T]\). For a rank-one \(T=ww^*\), the update
\(M_{S+i}=M_S+e_ie_i^*\) gives
\[
p_L(S+i)=-p_L(S)(1+(M_S^{-1})_{ii}),\quad
(M_{S+i}^{-1}w)_i=(M_S^{-1}w)_i/(1+(M_S^{-1})_{ii}).
\]
Hence each edge equals its corresponding incoming expression at its target. Summing incoming minus outgoing gives the derivative. A spectral decomposition of arbitrary Hermitian \(T\) proves the general identity by real linearity, with no commutation assumption.

Apply it to \(L=K_t^\Lambda\), \(T=\delta H^\Lambda\). The current is nonnegative by Section 3, and the exact finite equation is
\[
\frac d{dt}\mu_{K_t^\Lambda}(f)
=\mu_{K_t^\Lambda}\!\left[
\sum_{i\in\Lambda}a_i^\Lambda(t,x)(f(x^{i,1})-f(x))\right]. \tag{15}
\]
For a cylinder \(f\) on finite \(F\), its left side equals \(d\mu_{K_t}(f)/dt\) for every \(\Lambda\supset F\), because all its determinantal correlation minors are the same compression on \(F\). Only \(i\in F\) contribute on the right.

Extend finite configurations by any fixed exterior configuration. Their laws converge on every cylinder to \(\mu_{K_t}\). Replace rates by the infinite rates using (5); then approximate each jointly continuous rate uniformly by cylinder functions on the compact time/configuration space. This passes all expectations, giving
\[
\boxed{\frac d{dt}\mu_{K_t}(f)=\mu_{K_t}(\mathcal L_t f),\qquad
\mathcal L_t f=\sum_{i\in F}a_i(t,x)(f(x^{i,1})-f(x)).} \tag{16}
\]
The derivatives at 0 and 1 are one-sided. This calculation uses no infinite operator trace and retains exactly the stated rates.

## 6. An intrinsic common-clock construction

Use independent sitewise Poisson marks \((t,z)\in(0,1]\times[0,B_0]\) of intensity \(dt\,dz\). This is regular iid noise on a standard Borel site space of finite lists; it can be encoded by iid uniform labels. Initial \(X\) is independent of these clocks.

For any input \(x\), initially occupied sites stay occupied. Every vacant site can accept only its first accepted own-site mark. Set \(L^0=x\), constant in time; let \(U^0_i\) accept its first potential mark. Given the preceding box
\([L^n(t-),U^n(t-)]\), put
\[
\ell_i^n(t)=\inf_{y\in[L^n(t-),U^n(t-)]}c_i(t,y),\qquad
u_i^n(t)=\sup_{y\in[L^n(t-),U^n(t-)]}c_i(t,y).
\]
Let \(L_i^{n+1}\) accept its first mark with \(z<\ell_i^n(t)\), and \(U_i^{n+1}\) its first mark with \(z\le u_i^n(t)\).

These extrema are measurable and predictable. To verify measurability directly, configurations equal to the lower bound except on a finite set of free coordinates where they equal the upper bound form a countable dense subset of the compact box. Continuous \(c_i\) has the same infimum/supremum over that subset. The collection of all finite subsets is intrinsic and translation-natural. The threshold processes are predictable because they are Borel functions of left-limit adapted paths and time.

Ordered thresholds and shrinking boxes give, on every input,
\[
L^n\le L^{n+1}\le U^{n+1}\le U^n.
\]
At a fixed site each entire path selects a birth time from its finite own-site clock list or infinity. Thus both sequences stabilize as entire paths at that site after finitely many iterations; denote their limits by \(L,U\). Compactness and continuity pass extrema to the limiting box \([L(t-),U(t-)]\).

A relaxed **actual-rate** solution starts at \(x\), has only own-clock births, accepts every strictly sub-threshold mark for \(c_i(t,Z(t-))\) while vacant, rejects every strictly super-threshold mark, and may choose either action at equality. Every such solution \(Z\) is trapped between every \(L^n,U^n\). Indeed, once \(L^n\le Z\le U^n\), the actual rate lies between their box infimum and supremum. Lower strict acceptance forces acceptance by a still-vacant \(Z\); if \(Z\) was already occupied, the order already holds. The upper argument is analogous. This trapping assertion is deterministic.

Write
\[
\ell_i(t)=\inf_{y\in[L(t-),U(t-)]}c_i(t,y),\qquad
u_i(t)=\sup_{y\in[L(t-),U(t-)]}c_i(t,y).
\]
These limiting box thresholds are the limits of the iterated thresholds, by nested compact boxes and continuity. The lower limiting path accepts/rejects its own marks according to \(\ell_i\), with either action permitted at equality; the upper limiting path does the same according to \(u_i\). This follows because each site's entire path stabilizes among a finite list of birth times, while the corresponding thresholds converge at each of its marks. No actual-\(c_i(t,L)\) or actual-\(c_i(t,U)\) equation is asserted yet.

Both limiting box thresholds are predictable, as limits of the iterated predictable thresholds. For independent Poisson clocks, compensation gives probability zero to any mark whose vertical coordinate equals either threshold. Hence almost surely the limiting envelopes satisfy their exact respective **box-threshold** clock equations.


By (14), the limiting threshold interval has length at most
\[
u_i(t)-\ell_i(t)
\le\sum_{j\ne i}q(i^{-1}j)(U_j(t-)-L_j(t-)).
\]
A discrepancy can first be created only at a mark in this interval. With
\(d_i(t)=\mathbb P(L_i(t)\ne U_i(t))\), compensation gives
\[
d_i(t)\le\sum_{j\ne i}q(i^{-1}j)\int_0^t d_j(s)\,ds.
\]
For \(D(t)=\sup_i d_i(t)\), a measurable bounded function, (13) gives
\(D(t)\le I_0\int_0^tD(s)\,ds\). Gronwall yields \(D=0\).
Countably many sites and rational times identify the entire paths, since a discrepancy between distinct birth times persists over a nonempty interval. Hence \(L=U=:Y\) almost surely.

The limiting box is now a singleton at every time:
\([L(t-),U(t-)]=\{Y(t-)\}\).
Consequently
\(\ell_i(t)=u_i(t)=c_i(t,Y(t-))\).
The respective exact box-threshold equations proved before collapse therefore become the exact **actual-rate** clock equation for \(Y\). This is the first point at which the limiting envelope is asserted to satisfy the actual rate. Adaptation follows from its construction as an adapted envelope limit. The deterministic trapping statement above then yields pathwise uniqueness among every actual-rate relaxed solution on the same clocks, including nonadapted ones.


This works for each fixed deterministic initial input, and therefore also by conditioning for every independent random initial input. It does not assert a single good-noise event for all deterministic initial inputs. The common path is adapted to the graphical filtration. The trapping statement gives pathwise uniqueness even among nonadapted relaxed solutions on these clocks.

## 7. Actual same-input finite-chain limits and DPP marginal identification

The formal equation (16) is not by itself used to identify the constructed process. For finite \(\Lambda\), every atom of \(\mu_{K_t}|_\Lambda\) is strictly positive: along a gapped segment from \(I/2\), the signed exact-pattern determinant never vanishes. Define
\[
\widehat c_i^\Lambda(t,\eta)
=\mathbb E_{\mu_{K_t}}[c_i(t,X)\mid X_\Lambda=\eta],
\qquad i\in\Lambda.
\]
They are between 0 and \(B_0\) and continuous in time. For the numerator, uniformly approximate the jointly continuous integrand by cylinder functions and use finite determinant continuity; the denominator is a strictly positive continuous exact pattern probability.

For every pattern indicator, (16) is precisely the finite forward equation for birth rates
\((1-\eta_i)\widehat c_i^\Lambda(t,\eta)\).
The finite chain started at \(\mu_C|_\Lambda\) therefore has law \(\mu_{K_t}|_\Lambda\), by uniqueness of its finite time-dependent linear forward ODE.

Run it on the supplied \(X|_\Lambda\) and the *same* site clocks as Section 6, leaving exterior sites at their initial values. Joint uniform continuity gives, for each fixed \(i\),
\[
\sup_{\substack{t,x,\eta\\x|_\Lambda=\eta}}
|\widehat c_i^\Lambda(t,\eta)-c_i(t,x)|
\le\operatorname{osc}_i(\Lambda)\longrightarrow0. \tag{17}
\]
This is uniform over all patterns and inputs; it does not divide by a small pattern probability.

For any exhaustion and any subsequence, the fixed finite clock list at each site permits a subsubsequence on which every site's entire finite-chain path stabilizes, by a countable diagonal extraction. Let \(Z\) be its limit. At every own-site mark, pre-mark configurations converge coordinatewise to \(Z(t-)\), because entire site paths stabilized. By (17) and product continuity, every limiting acceptance/rejection satisfies the relaxed rule for \(c_i(t,Z(t-))\). On the good common input, trapping gives \(Z=Y\). Thus all cluster limits coincide and the *full sequence* converges coordinatewise as entire paths on the actual common input. This is not a weak-limit or iid-limit inference.

For finite \(F\) and every deterministic \(t\), bounded convergence gives
\[
\mathbb P(F\subset Y_t)
=\lim_\Lambda\mathbb P(F\subset X_t^\Lambda)
=\det(K_t|_F).
\]
Inclusion-exclusion identifies all patterns, so \(Y_t\sim\mu_{K_t}\), including \(Y_0=X\sim\mu_C\).

## 8. Total Borel equivariance, all-input order, and natural-filtration rates

The envelope iterates and limiting coordinate birth times are Borel functions of initial configuration and clocks. Agreement of their paths is a Borel condition, checked on countably many sites and rational times. Include the almost-sure simple-clock and limiting threshold-nontie conditions in a Borel good set. Every operation and this good set are exactly invariant under left translation: the kernels are covariant and boxes/extrema select no distinguished root or spatial order.

Return the common envelope path on the good set, and the constant initial path on its complement. This is a total Borel, exactly equivariant map. Every output is coordinatewise cadlag and pure-birth and contains its supplied initial configuration at every time. The exceptional fallback therefore preserves all-input containment. Coordinatewise cadlag paths are also cadlag in the countable product topology by approximating a product metric with finitely many coordinates.

For the probabilistic input the fallback has probability zero. For a cylinder \(f\), the graphical clock equation yields
\[
f(Y_t)-f(Y_0)-\int_0^t\mathcal L_s f(Y_{s-})\,ds
\]
as a compensated Poisson integral over finitely many sites, with bounded predictable integrands. It is a martingale in the graphical filtration. The integral and the process are measurable in the natural past of \(Y\); conditioning down by the tower rule gives the same martingale in the natural filtration. These are exactly rates (1), not the conditional average rates used only for marginal verification.

Almost surely no two sites' marks share a time, by countably many pairs of finite Poisson lists. Hence all actual jumps are individual births. No finite range, amenability, invariant weak-solution fixed point, or hidden conditional sampler was used.

## 9. Endpoint joint iid and statement scope

Given the stipulated equivariant iid sampler of \(\mu_C\), split regular iid labels into independent sampler and clock channels and compose it with the relative map. This gives an ordered endpoint pair jointly as an exactly equivariant iid image, with laws \(\mu_C,\mu_{C+\delta H}\). Containment is valid on all inputs, including fallback. This proves the joint-iid conclusion under precisely its supplied-sampler premise.

The relative theorem requires only a supplied initial DPP independent of new clocks. Its convolution hypotheses remain explicit. A finitary strengthening for a concrete central-cyclic-group family is proved in [CENTER.md](CENTER.md), using [LOCAL.md](LOCAL.md). The global fallback in this measurable theorem is not used for that finite-certificate strengthening. General ordered DPP factors remain open.
