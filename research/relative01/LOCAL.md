# Summable local updates: graphical construction and forward uniqueness

This is a classical sufficient theorem. The proof below records the precise forward-equation interface used by [CENTER.md](CENTER.md). Section 8 gives the local totalization needed for arbitrary-completion finite certificates.

## 1. Statement and conventions

Let Gamma be any countable group and E={0,1}^Gamma with its product Borel structure and product topology. The action is (gamma x)_g=x_{gamma^{-1}g}. Finite Gamma is allowed. Time lies in [0,1]. A cylinder function means a bounded real function depending on finitely many coordinates.

Fix a countable index set, enumerated k=0,1,... . For every k fix a finite V_k subset Gamma containing e, a Borel function lambda_k:[0,1]->[0,infinity), and a Borel function b_k:[0,1]x{0,1}^{V_k}->[0,1]. Assume

\[
b_k(t,z)=0\quad(z_e=1),\qquad
\sum_k\lambda_k(t)|V_k|\le B<\infty\quad\text{for every }t.
\tag{1}
\]

Define

\[
a_g(t,x)=\sum_k\lambda_k(t)b_k(t,(x_{gv})_{v\in V_k}),\qquad
L_tf(x)=\sum_g a_g(t,x)[f(x^{g,+})-f(x)].
\tag{2}
\]

For a cylinder supported on F, the second sum has only sites g in F. Thus L_tf is jointly Borel, |L_tf|<=2B|F| ||f||_infinity, and 0<=a_g<=B. The field is covariant. The rate field and its mixture are fixed; their existence is an explicit hypothesis.

Independently for all g let N_g be Poisson random measures on (0,1]xN_0x[0,1], of deterministic intensity dt lambda_k(t)du. Their aggregate intensity at one site is at most B. At a mark (s,k,u) of N_g set g to one iff u<=b_k(s,X_{s-}|gV_k); otherwise do nothing.

Conclusions:

(i) There is one invariant Borel probability-one noise event on which this prescription gives a unique coordinatewise cadlag pure-birth solution for every deterministic initial x, simultaneously at all sites and all times. The total graphical map, extended by the constant initial path off that event, is Borel and exactly equivariant. For independent random initial data it is an adapted strong solution in the completed driving filtration. Each coordinate has at most one birth, local integrated activity is at most B, and no two coordinates have simultaneous positive-time births.

(ii) For any subinterval [r,T], the integrated cylinder forward equation has at most one Borel probability-law curve for each initial law. Precisely, if rho_t is Borel into Prob(E) and

\[
\rho_t(f)-\rho_r(f)=\int_r^t\rho_s(L_sf)\,ds
\quad(r\le t\le T)
\tag{3}
\]

for every cylinder f, it is uniquely determined by rho_r. No spatial density, invariant law, or extra initial continuity is assumed.

(iii) The coordinatewise cadlag pure-birth cylinder martingale problem is unique in law for every initial law. It has the graphical solution just constructed. If a prescribed DPP curve mu_t satisfies (3), then the graphical process started at mu_0 has Law(X_t)=mu_t for every t. If mu_0 is invariant, its full path law is invariant. If an equivariant iid sampler for mu_0 is supplied, use a separate independent iid layer for N to obtain an equivariant path iid factor.

## 2. Finite backward ancestry

A potential mark z=(g,s,k,u) consults gV_k. For a query (g,t), include every mark at g with time <=t; recursively, for an included mark (h,s,k,u), include every mark at every j in hV_k with time <s. This defines the ancestor cluster as a countable increasing union. Every included mark lies on a finite chronological chain ending in the queried site.

Here is a uniform bound. Put Q(s)=sum_k lambda_k(s)<=B. A backward dependency step out of a mark at h of type k may choose any j in hV_k, so its intensity-weighted number of choices is at most sum_k lambda_k(s)|V_k|<=B. For chains of n+1 marks whose last site is fixed, the expected total count is at most

\[
\int_{0<s_0<\cdots<s_n\le t}
B^{n+1}\,ds_0\cdots ds_n
=\frac{(Bt)^{n+1}}{(n+1)!}.
\tag{4}
\]

To see the inequality without a hidden independence assumption, first sum over all site/type sequences. For the latest mark sum lambda_k(s_n)|V_k|, choose its predecessor site, then do the same at the next mark; the earliest mark only needs its total intensity Q(s_0). These bounds give B^{n+1}. For each fixed sequence the factorial-moment formula of the independent Poisson measures gives the displayed ordered time integral. A site/type can occur repeatedly: strict chronological order means distinct Poisson points, precisely the setting of the factorial-moment formula. All terms are nonnegative, so Tonelli justifies the countable sums.

Summing (4) over n gives at most exp(Bt)-1. The number of distinct ancestor marks is bounded by the total number of these chains. Therefore every queried cluster has finite expectation and is finite almost surely. This proves more than absence of an infinite branch: it excludes infinitely many finite branches too.

For each site g its cluster at time 1 is finite almost surely. Intersect these events over the countable Gamma. Every earlier-time cluster is a subset of this cluster; hence this one event covers all g and all real t. At each site the projected point process has a finite non-atomic intensity measure and therefore has finitely many distinct times. Countable intersection over site pairs shows that no potential points at any sites have equal times, almost surely. In particular there are no marks at deterministic endpoints. Include these properties in the good event G. Its definition uses only the noise, is Borel by the countable ancestor recursion, and is invariant under the site action.

On G, for any x in E order a queried cluster chronologically. At a mark (h,s,k,u), all earlier marks at its consulted sites hV_k have already been processed; start those sites at the given coordinates of x. Thus their states at s- are known and the decision is unambiguous. A decision in a larger query cluster cannot alter a smaller-cluster decision because all of its own ancestors were already in the smaller cluster. Induction over the chronological order proves consistency of overlapping queries.

This defines X_g(t) for every g,t,x on the same G, without any exceptional initial set. Since each site changes only at its own finitely many marks, the paths are coordinatewise cadlag. They are pure birth because b_k=0 at occupied local patterns. In any summable product metric the full E-valued path is cadlag too, by first retaining finitely many coordinates and then bounding the metric tail.

For measurability, stop ancestor exploration after n generations and compute a queried value using, for example, the initial states at unresolved earlier histories. Each finite-depth exploration involves almost surely finitely many marks: at a site there are finitely many marks and each consulted neighborhood is finite. Point enumeration, finite recursion and the local Borel decisions are measurable. On G these query values stabilize as n increases. Consequently all coordinate evaluations are Borel. Alternatively restrict first to inputs for which the finite exploration exists and extend the finite approximations by fixed values elsewhere. The path can be encoded by its countable coordinate birth times in ([0,1] disjoint-union {infinity})^Gamma; a birth time is the infimum of rational times at which its coordinate is one, with the initial occupied value encoded at zero. Therefore the graphical map into this standard Borel path space is Borel. Off G return the constant initial path.

Both ancestor exploration and every update commute with left translation. G and the constant-path fallback do also. The resulting total map Phi satisfies exactly

\[
\Phi(\gamma x,\gamma N)=\gamma\Phi(x,N)
\quad\text{for every input }(x,N).
\tag{5}
\]

On G, any other path satisfying the same marked update rules must make identical decisions, by induction in each queried cluster. Hence it agrees at every site and time with Phi. This is all-input pathwise uniqueness for the marked prescription. Accepted births are a subset of the distinct potential times, so simultaneous positive-time births are absent.

## 3. Adaptation and the martingale equation

For a fixed t, the cluster for each query (g,t), and each finite-depth query approximation, uses only marks through t. The constructed value is therefore measurable with respect to initial data and the noise through t, after completing the filtration. The total fallback tests the full good event; it changes no probability law or adapted version because its complement is null. This distinction avoids claiming a causal formula on arbitrary exceptional noise inputs. The asserted strong solution is adapted in the completed driving filtration, while total equivariance and the all-initial-input uniqueness statement concern G.

With X_0 independent of N, for a cylinder f supported on F the pathwise jump formula is

\[
f(X_t)-f(X_r)=
\sum_{g\in F}\sum_k\int_{(r,t]\times\{k\}\times[0,1]}
[f(X_{s-}^{g,+})-f(X_{s-})]
1_{\{u\le b_k(s,X_{s-}|gV_k)\}}\,N_g(ds,dk,du).
\tag{6}
\]

The local integrands are predictable: each finite local state at s- is predictable and the deterministic time/local-state function b_k is Borel. The total compensator mass on F is bounded by B|F|. Compensating (6), or first compensating its finite type truncations and taking L1 limits, gives the integrable martingale

\[
M_t^f=f(X_t)-f(X_0)-\int_0^t L_sf(X_{s-})\,ds.
\tag{7}
\]

It is a martingale also in the smaller natural filtration of X, by the tower property. Since each path has at most countably many coordinate jump times, X_s=X_{s-} for Lebesgue-almost every s on each path. Taking expectations gives (3). The distributional curve is Borel. Local integrated activity obeys integral a_g<=B pathwise.

## 4. A uniform summable-oscillation estimate

This estimate is the step needed to identify arbitrary law curves, rather than merely the graphical one.

Retain types k<=m and any finite set Lambda, freezing the exterior to zero. Its finite-volume rate at g in Lambda is

\[
a_g^{m,\Lambda}(s,x)=
\sum_{k\le m}\lambda_k(s)b_k(s,(\bar x_{gv})_{v\in V_k}),
\tag{8}
\]

where bar x equals x in Lambda and zero elsewhere. Its generator is a finite-state bounded Borel-time pure-birth generator. Let u_s(x)=E_{s,x}^{m,Lambda} f(Y_T), where f is supported on F subset Lambda. Then u_T=f and u_s is absolutely continuous in s in each finite state and solves the backward equation for almost every s.

For a function v on the finite configuration space write

\[
\delta_i v=\sup\{|v(x)-v(y)|:x_j=y_j\text{ for }j\ne i\}.
\]

We claim, uniformly in m,Lambda and r<=s<=T,

\[
\sum_i\delta_i u_s\le 2\|f\|_\infty |F|e^{B(T-s)}=:C_f(s).
\tag{9}
\]

Couple initial configurations differing only at i with the same local clocks. A new disagreement at h can be created only by a mark whose consulted neighborhood contains an earlier disagreement. Thus a terminal disagreement at j in F requires a chronological chain of marks from initial i to j; the zero-mark chain is possible only if i=j. Define

\[
C_{hj}(s)=\sum_{k\le m}\lambda_k(s)1_{\{j\in hV_k\cap\Lambda\}}.
\]

Its row sums are at most B. The sum over all initial sites i of the expected number of length-n chains into a fixed terminal j is at most (B(T-s))^n/n!, by the same nonnegative factorial-moment calculation as before. A discrepancy event is bounded by the sum of its chain counts. Summing that bound over i and j in F and multiplying by 2||f|| proves (9). The argument is independent of the actual decisions, input pattern, volume, or finite-type range, so taking the supremum defining each delta_i is legitimate: the same chain-presence upper bound controls every input pair differing at i. No summation of different configuration-dependent influences is used.

## 5. Cylinder forward uniqueness for merely Borel law curves

Let rho and rho-tilde satisfy (3) on [r,T] with the same initial law. All expectations in (3) are well-defined: a Borel probability kernel t->rho_t integrates the jointly Borel bounded L_tf measurably. The equation itself shows that every finite-pattern probability is absolutely continuous, with bounded derivative. In particular initial right continuity for cylinder tests is a consequence, not an extra hypothesis.

Fix cylinder f supported on finite F and fix m. Let W_m={e} union the V_k and their inverses for k<=m. It is finite and symmetric. Give Gamma the undirected graph with neighbor sets gW_m, and let d_m be its graph distance (infinity between distinct components). Put Lambda_n={g:d_m(g,F)<=n}. This is finite. Even if the graph is disconnected, all truncated influences of F stay in these components. Let D_m=|W_m|. The number of sites at distance n is at most |F|D_m^n.

Use (8) with Lambda_n, and denote its backward terminal-f function by u_s^{m,n}. At a site of distance at most n-1 every retained neighborhood is inside Lambda_n, so the truncated and finite-volume rates agree. Only sites at distance exactly n can contribute to the truncated boundary residual. A same-noise discrepancy starting at such a site must traverse at least n edges before affecting F. Since total potential intensity at a site is at most B, ordered-chain counting gives

\[
\delta_i u_s^{m,n}\le
2\|f\|_\infty\sum_{\ell\ge d_m(i,F)}
\frac{(BD_m(T-s))^\ell}{\ell!}.
\tag{10}
\]

Consequently the truncated boundary residual is uniformly bounded, at all times where the backward derivative exists, by

\[
\epsilon_{m,n}=2B\|f\|_\infty|F|D_m^n
\sum_{\ell\ge n}\frac{(BD_m)^\ell}{\ell!}
\le 2B\|f\|_\infty|F|e^{BD_m}
\frac{(BD_m^2)^n}{n!}\longrightarrow0
\tag{11}
\]

for each fixed m. B=0 gives constant processes and uniqueness immediately, so factorial expressions can be read with that case removed.

Set R_m(s)=sum_{k>m}lambda_k(s). Then R_m(s)<=B and R_m(s)->0 for every s. The difference of full and truncated generators acting on the cylinder u_s^{m,n} is at most R_m(s)sum_i delta_i u_s^{m,n}. By (9),

\[
\sup_x| (\partial_s+L_s)u_s^{m,n}(x)|
\le \epsilon_{m,n}+2\|f\|_\infty|F|e^B R_m(s)
\quad\text{for a.e. }s.
\tag{12}
\]

The forward equation extends to this absolutely continuous time-dependent cylinder test. Indeed expand u_s^{m,n} in the finitely many Lambda_n pattern indicators with absolutely continuous coefficients. Their rho_s probabilities are absolutely continuous by (3); the finite scalar product rule then gives

\[
\rho_T(f)-\rho_r(u_r^{m,n})
=\int_r^T\rho_s((\partial_s+L_s)u_s^{m,n})\,ds.
\tag{13}
\]

There is no use of a forward equation for a noncylinder test here. Apply (12)-(13) to both curves and use their equal initial laws:

\[
|\rho_T(f)-\widetilde\rho_T(f)|
\le 2(T-r)\epsilon_{m,n}
+4\|f\|_\infty|F|e^B\int_r^T R_m(s)\,ds.
\tag{14}
\]

First let n->infinity with m fixed. Then let m->infinity; dominated convergence applies to R_m. The right side tends to zero. Since f,T were arbitrary, all cylinder expectations agree at every time, and cylinders determine laws on E. This proves conclusion (ii) on every time subinterval.

## 6. Martingale-problem uniqueness and identification

For completeness we now distinguish pathwise uniqueness for the local-mark prescription from uniqueness of an arbitrary martingale solution.

Let P be any coordinatewise cadlag pure-birth law satisfying the natural-filtration cylinder martingale problem for (2), with a specified initial law. The bounded rate ensures the integrability of every cylinder drift. Fix a deterministic rational s and disintegrate the future path conditional on its past through s. There is one conditional probability-one set on which the martingale identities from s to rational t hold for every finite-pattern indicator: multiply the unconditional identities by all bounded past tests, then use conditional expectation and intersect the countable determining family. Right continuity of cylinder evaluations and the deterministic drift bound extend these conditional identities from rational t to every t>=s. Conditional future one-time laws are a Borel kernel in t, obtained from the Borel coordinate path evaluations.

Thus on that one conditional conull set the future marginal curve satisfies (3) with initial law delta_{X_s}. By conclusion (ii) it equals the graphical transition curve started at that very X_s and at time s. The graphical transition kernel is Borel in its initial configuration by Section 2, and fresh Poisson increments after s provide its time-inhomogeneous Markov realization. Therefore

\[
E_P[f(X_t)\mid\mathcal F_s]
=P_{s,t}f(X_s)\quad(s\text{ rational},\ t\ge s)
\tag{15}
\]

for every cylinder f. A monotone class extends this to all bounded Borel f. Induction over any finite list of rational times, including zero, fixes every rational-time finite-dimensional distribution. Cadlag coordinate paths are determined by their rational evaluations and the terminal evaluation, so these distributions determine P. This is uniqueness in law of the stated pure-birth martingale problem. It does not assume an arbitrary solution was originally supplied with product Poisson noise.

For a prescribed DPP curve mu_t satisfying the exact integrated cylinder continuity equation, both mu_t and the graphical marginal curve start from mu_0 and satisfy (3). Hence

\[
\operatorname{Law}(X_t)=\mu_t\quad\text{for every }t\in[0,1].
\tag{16}
\]

The DPP properties themselves are unnecessary for forward uniqueness; they enter only by specifying the target curve and its equation. If K_t is equivariant, mu_0 is invariant. The input law of independent (X_0,N) is then invariant, and exact equivariance (5) makes the entire path law invariant on any countable Gamma, amenable or not.

If X_0=Psi(U) is a supplied equivariant iid sampler, let V be an independent iid field coding the sitewise N_g. Since each N_g has the same deterministic intensity, a Borel probability-space coding of this standard Borel Poisson law exists. Then Phi(Psi(U),N(V)) is an equivariant factor of the enlarged iid field. This conclusion assumes the initial sampler and keeps the layers independent; it is not inferred from a weak limit.

## 7. A sufficient rate criterion stated without an unknown decomposition

Suppose a_e(t,x) is Borel in (t,x), continuous in x for each t, 0<=a_e<=M, and vanishes when x_e=1. Let {e}=V_0 subset V_1 subset ... be finite sets exhausting Gamma. Suppose explicit numbers eta_n>=0 satisfy

\[
|a_e(t,x)-a_e(t,y)|\le\eta_n
\quad\text{whenever }x|_{V_n}=y|_{V_n},\quad\text{for every }t,
\]
\[
\eta_n\to0,\qquad
\sum_{n\ge1}|V_n|\eta_{n-1}<\infty.
\tag{17}
\]

Set l_n(t,z)=inf{a_e(t,x):x|_{V_n}=z}. For each of finitely many z choose a fixed countable dense set in the compact extension fiber. Spatial continuity makes the infimum equal to the countable infimum on that set; thus l_n is Borel in (t,z). The lower envelopes are increasing along matching patterns, and (17) gives 0<=a_e-l_n<=eta_n. Also 0<=l_n-l_{n-1}<=eta_{n-1}: both terms lie between the infimum and supremum over the larger V_{n-1} fiber.

Use type zero lambda_0=M, b_0=l_0/M, and, for n>=1 with eta_{n-1}>0, lambda_n=eta_{n-1}, b_n=(l_n-l_{n-1})/eta_{n-1}. A zero denominator contributes the zero function. The M=0 case is trivial. Each b_n is a local [0,1] Borel function and vanishes at occupied patterns. The telescope converges pointwise to a_e; its dependency cost is at most

\[
M+\sum_{n\ge1}|V_n|\eta_{n-1}<\infty.
\tag{18}
\]

Translate the template to all sites. This supplies exactly (1)-(2), a directly checkable sufficient condition. Spatial continuity is explicit; it has not been derived from Borelness. The condition is stronger than plain continuity and is not asserted necessary. This lower-envelope device is a special case of classical local-mixture/Kalikow techniques.

## 8. Local totalization and finite certificates

Decode each site's label to a finite list of marks (s,n,z) on (0,1] times
N_0 times [0,1]. A total Borel decoder into finite lists exists; under the
iid law it has the specified finite Poisson distribution. Multiplicity
and same-time marks on exceptional inputs are permitted in this list space.

For the output at site i, start from ALL its marks through time 1. For each
included mark (h,s,n,z), read the labels and initial values at all j in hV_n,
and include all their marks with time STRICTLY LESS than s. Repeat. Include
i itself, even when its list is empty. Let A_i be the least such ancestor
closure. This recursion uses only the sites reached by the query and never
tests goodness elsewhere in the full input.

If A_i is finite, all its consulted initial coordinates form a finite set.
Evaluate the finite marks chronologically. At any time tie, first calculate
all the tied proposals from their respective left-limit local patterns.
For multiple proposals at the same site and time, set that site to one
if at least one proposal accepts, or if it was already one. Thus processing
a time batch is unambiguous and does not choose a spatial ordering. No
within-batch update is consulted by another mark in that batch. Because
ancestry includes only strictly earlier marks, every required pre-mark
state has already been evaluated. Return the resulting whole path at i.

If A_i is infinite, return only for this coordinate the constant path equal
to its supplied initial value. Other coordinates use their own queries.
When computing a successful query, its finite subqueries are evaluated
inside that query. The algorithm does not call another coordinate's final
whole-path output, which might have failed due to ancestors at later times.

For fixed i, finite closure is a Borel event: after finite-stage exploration
the finite discovered set eventually has no new required marks or sites.
Every stage involves finitely many finite lists and finite neighborhoods.
Its evaluated path is a Borel function of those lists and initial values.
The infinite-closure alternative is therefore Borel too. Each coordinate
output is always a binary nondecreasing cadlag path starting at its own
initial value. These coordinate paths define a product-cadlag path by the
usual finite-coordinate/tail metric argument, even on exceptional inputs.

All rules commute with left translation, including ties and the coordinatewise
constant fallback. Thus the total map is exactly equivariant and preserves
the supplied initial state on every input. On exceptional inputs the output
is not asserted to solve the prescribed clock equations simultaneously;
that assertion is probabilistic and remains on the good noise event below.

### Certificate proof

Suppose a query at i succeeds. Retain the labels of every consulted site
and its consulted initial values. For any completion outside that finite
set, exploration reads exactly the same lists, their types and all strictly
earlier dependency marks. Induction over its finitely many stages reproduces
the same closed finite graph. Batch evaluation is therefore identical and
the output path at i is unchanged. No remote failure can trigger a fallback
at i. This proves the certificate for arbitrary completions, including
completions at which some OTHER queries have infinite ancestry or time ties.

The factorial-chain argument in Section 2 shows every A_i is finite almost
surely. A countable intersection yields a single noise event on which this
holds simultaneously at all sites and for every initial configuration.
The iid Poisson lists also have no time ties almost surely. On that event
the local query evaluations are consistent on all overlaps and give the
same genuine graphical process as in Sections 2--3. Consequently its rate martingales, DPP marginal identification and causal property are unchanged. The quantitative query bounds are stated next. No initial-state-dependent
exceptional event has been introduced.


## 9. Relative query costs

Suppose the mixture weights are constant in time. Put B=sum_k lambda_k |V_k|. In a fixed left-invariant metric with subadditive length, put B1=sum_k lambda_k sum_(v in V_k) |v|. A queried initial site has a strictly decreasing-time dependency chain from the output. Summing chain counts of length n bounds the expected number of consulted site labels by sum_(n>=0) B^n/n! = exp(B); the length-zero term includes the output site. Repeated visits only reduce the number of distinct consulted sites.

The distance to the endpoint of a chain is at most the sum of its step lengths. Summing these over all chains, with one step carrying its distance and the other n-1 steps their usual weights, gives sum_(n>=1) n B1 B^(n-1)/n! = B1 exp(B). The maximum queried radius is at most this sum. These estimates concern the relative construction from the supplied initial configuration; composition with a separate initial sampler does not inherit them automatically.
