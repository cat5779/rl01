# Finite rate boxes and finitary pure-birth processes

## Abstract

We give a sufficient condition for a bounded measurable pure-birth process on a countable group to have a finitary realization from its supplied initial configuration. The condition concerns extrema over finite rate boxes: their expected widths must be controlled by an affine approximation whose infimum has an Osgood modulus. Finite chronological ancestor graphs then yield nested lower and upper processes. Their widths collapse, and the finite list of candidate times at each coordinate upgrades limiting agreement to a finite certificate for the entire coordinate path.

An explicit family on every countably infinite group of the form \(G\times C_2\) illustrates the criterion. Its prescribed marginals are diagonal determinantal processes, while its rates depend essentially on every off-root coordinate. The rates admit neither a finite-mean local-neighborhood mixture nor an everywhere continuous version agreeing almost surely. A separate two-orbit example shows that an Osgood mean-disagreement bound over all couplings of the prescribed marginals does not, by itself, imply relative finitarity.

## 1. Setting and inputs

Let \(\Gamma\) be a countable group acting on
\[
\Omega=\{0,1\}^{\Gamma}
\]
by left translations. Write \(x^{g,b}\) for the configuration obtained by replacing \(x_g\) by \(b\). A binary pure-birth path is a coordinatewise nondecreasing cadlag path in \(\Omega\). Each coordinate is initially occupied, has one birth, or remains vacant throughout \([0,1]\).

Consider jointly Borel, covariant intrinsic rates
\[
c_g:[0,1]\times\Omega\longrightarrow[0,M],\qquad M<\infty,
\]
independent of the center bit \(x_g\). The actual birth rates are
\[
a_g(t,x)=(1-x_g)c_g(t,x).                                      \tag{1.1}
\]
Center-bit independence of the intrinsic rate entails no restriction beyond the usual requirement that an actual birth rate vanish at occupied sites: one can take \(c_g(t,x)=a_g(t,x^{g,0})\).

A weak solution with these rates means a pure-birth process for which, for every bounded cylinder function \(f\),
\[
f(X_t)-f(X_0)
-\int_0^t\sum_{g\in\Gamma}a_g(v,X_{v-})
   \bigl[f(X_{v-}^{g,1})-f(X_{v-})\bigr]\,dv                   \tag{1.2}
\]
is a martingale in the usual natural filtration. Only the finitely many coordinates on which \(f\) depends contribute to the sum. We work with weak solutions having no simultaneous births at distinct coordinates. Bounded rates imply finite mean activity at each coordinate.

Let \((\mu_t)_{0\le t\le1}\) be a prescribed invariant marginal curve. The first input is the existence of at least one ordinary weak solution of (1.2) with these marginals. Invariance, a strong realization, and finitarity are not included in this input.

The second interface is compatible Poisson noise. For a weak solution in the preceding class, one can extend the probability space by a product family of Poisson random measures \(N_g\), independent of \(X_0\), of intensity \(dt\,du\) on \((0,1]\times(0,M]\), such that
\[
X_g(t)=X_g(0)\vee
\mathbf1\{\text{a proposal at }g\text{ is accepted before }t\},
\]
with a vacant site accepting a proposal \((t,u)\) precisely when
\[
u\le c_g(t,X_{t-}).                                          \tag{1.3}
\]
The noise has product, past-independent increments in a common filtration containing the process. Appendix A proves the bounded-rate completion statement, including joint independence. Merely specifying each coordinate compensator would not establish this interface.

In the determinantal application below, ordinary weak existence is supplied by the following input, kept separate from our finitary argument.

**Ordinary weak-existence input for DPP curves.** A linear equivariant kernel curve \(K_t=C+tH\), uniformly bounded away from \(0\) and \(I\), with \(H\ge0\), admits an ordinary prescribed-marginal pure-birth weak law if its finite-valued Borel covariant birth rates satisfy the exact continuity equation for every finite cylinder and have finite integrated mean activity at each coordinate. The weak law is taken in the non-simultaneous-birth class above. This input does not assert invariant weak existence on a nonamenable group. Its preserved mathematical source is [G9 RESULT.md](https://github.com/cat5779/rl01/blob/837abbc1eb9ea43245f8a53ef02a5484e750d168/research/dpp10/g9/RESULT.md), with [its scope review](https://github.com/cat5779/rl01/blob/837abbc1eb9ea43245f8a53ef02a5484e750d168/research/dpp10/g9/REVIEW.md). The imported ordinary weak theorem is not re-proved here.

### Relative finite certificates

The input at site \(g\) consists of its supplied initial bit \(x_g\) and a fresh noise label \(\eta_g\), here a complete finite candidate-clock list. A total map
\[
\Phi:\Omega\times\mathcal N^\Gamma
   \longrightarrow D([0,1],\Omega)
\]
has a finite certificate for the whole path at \(g\) at an input \((x,\eta)\) if a finite set \(Q\subset\Gamma\) has the following property: every input \((x',\eta')\) agreeing with \((x,\eta)\) on all site labels in \(Q\) gives the same entire coordinate path,
\[
\Phi_g(x',\eta')|_{[0,1]}=\Phi_g(x,\eta)|_{[0,1]}.
\]
The agreement must hold under every outside completion, including completions outside a probability-one good set. Relative finitarity means the certificate exists almost surely under the specified initial law and independent fresh noise. No bound on its expected size or radius is part of the definition.

## 2. A shrinking-box theorem

Fix nested finite sets \(F_R\subset\Gamma\), \(R\ge1\), containing the identity. Their union need not exhaust the group. For local binary patterns \(l\le u\) on \(gF_R\), let
\[
B_g^R(l,u)=\{z\in\Omega:l_j\le z_j\le u_j,\ j\in gF_R\}.
\]
Define exact intrinsic rate-box extrema
\[
\ell_g^R(t,l,u)=\inf_{z\in B_g^R(l,u)}c_g(t,z),\qquad
h_g^R(t,l,u)=\sup_{z\in B_g^R(l,u)}c_g(t,z).                  \tag{2.1}
\]
The boxes are nonempty. We impose the following measurable-extremum hypothesis.

**BOX.** Both quantities in (2.1) are jointly Borel in time and the finite patterns.

Spatial Borelness of \(c_g\) alone is not asserted to imply BOX. Neither attainment of the extrema nor spatial continuity is required.

Using the independent candidate clocks, start lower and upper processes at the same supplied initial configuration. At radius \(R\), a proposal at \(g\) updates them from their left-limit patterns by
\[
\begin{aligned}
L_g^R&\leftarrow L_g^R\vee
\mathbf1\{u\le\ell_g^R(t,L^R|_{gF_R},U^R|_{gF_R})\},\\
U_g^R&\leftarrow U_g^R\vee
\mathbf1\{u\le h_g^R(t,L^R|_{gF_R},U^R|_{gF_R})\}.
\end{aligned}                                               \tag{2.2}
\]
These finite-neighborhood systems are defined through finite chronological ancestor graphs, as described in the proof. Their law is determined solely by \(\mu_0\), the rates, the neighborhoods, and product noise. It does not require an unknown invariant weak solution.

Write
\[
\delta_R(t)=\mathbb P(L_e^R(t)\ne U_e^R(t))
\]
and let \(W_e^R(t)\) be the difference between the two intrinsic thresholds in (2.2), evaluated at the left states.

**WIDTH.** There are finite constants \(A_n,\tau_n\ge0\), with \(\tau_n\to0\), and a nonnegative \(L\in L^1([0,1])\), such that outside one Lebesgue-null set,
\[
\mathbb E W_e^R(t)
\le L(t)\bigl[A_n\delta_R(t)+\tau_n\bigr]
\quad\text{for every }n\ge1,\ R\ge n.                         \tag{2.3}
\]
Set
\[
\omega(r)=\inf_{n\ge1}(A_nr+\tau_n),\qquad 0\le r\le1.        \tag{2.4}
\]
Assume either \(\omega\equiv0\), or \(\omega(r)>0\) for every \(r>0\) and
\[
\int_{0+}\frac{dr}{\omega(r)}=\infty.                         \tag{2.5}
\]

**Theorem 2.1.** Under the ordinary weak input, BOX, WIDTH, and the modulus alternative in (2.4)--(2.5), there is a total Borel, exactly equivariant map \(\Phi\) preserving every supplied initial configuration and giving pure-birth cadlag coordinate paths. Under \(\mu_0\) and independent candidate noise, it realizes the prescribed weak law and has a finite arbitrary-completion certificate for every whole coordinate path almost surely.

The prescribed-marginal weak law is unique in the stated weak class and is invariant. The map is causal almost surely in the completed initial/noise-past filtration. If \(\mu_0\) has a finitary uniform-iid sampler with the same arbitrary-completion convention, composition gives a whole-coordinate-path finitary uniform-iid process. No query or radius moment, and no common collapse event for every deterministic initial input, is asserted.

### Proof

**Finite ancestors.** To evaluate a whole path at a root and radius \(R\), inspect its complete own proposal list. For each included proposal \((g,t,u)\), inspect the complete labels and initial bits at \(gF_R\), and include all proposals there at strictly earlier times. Iterate to the least closure. An inspected empty earlier list is part of the certificate.

Every site list is finite almost surely. The Poisson factorial-moment estimate for strict-time chains of length \(k\) is
\[
\mathbb E[\text{number of depth-}k\text{ occurrences}]
\le\frac{(M|F_R|)^k}{k!}.                                    \tag{2.6}
\]
Repeated sites involve distinct strictly ordered marks and satisfy the same estimate. Its sum is finite. Hence each local closure is finite almost surely. Countably intersecting radii and roots gives one noise-only conull event on which every such graph is finite for every initial input.

Finite closure is a Borel predicate: it occurs when some finite iteration produces no new nodes. On a finite graph evaluate (2.2) chronologically. For off-law tied times use left-limit patterns for the whole batch; combine multiple proposals at one site by OR. No global tie test and no remote whole-path fallback enters a graph calculation.

**Nesting and trapping.** Infima increase and suprema decrease when a box narrows. A successful larger-radius graph contains every smaller-radius computation. Induction in that finite graph gives
\[
L^R\le L^S\le U^S\le U^R\qquad(R\le S).                       \tag{2.7}
\]
Occupied persistence handles sites already occupied.

Complete any ordinary weak reference \(X\) by Appendix A. At each queried proposal, its local state is inside the current box if it was trapped before that proposal. Its actual intrinsic rate lies between the two extrema. Thus the same finite induction gives
\[
L^R\le X\le U^R                                               \tag{2.8}
\]
at every coordinate and time, almost surely. Only \(X\) follows the actual rate \(c_g\); the envelopes need not do so.

The finite-radius construction is equivariant. Its input law \(\mu_0\) times product noise is invariant, so discrepancy probabilities are the same at every coordinate. This requires no invariant reference law. Causal prefix computations give adapted versions of the envelopes and predictable threshold widths in the completed input/noise-past filtration.

**The width limit.** A discrepancy can first be created only by a proposal between the lower and upper thresholds. Counting all such proposals and applying compensation gives, for every \(t\),
\[
\delta_R(t)\le\int_0^t\mathbb E W_e^R(v)\,dv.                 \tag{2.9}
\]
By (2.7), the exact finite boxes narrow. Therefore \(W_e^R\) decreases to a bounded limit \(W_e^\infty\), and the binary discrepancies decrease to
\[
\delta(t)=\mathbb P(L_e^\infty(t)\ne U_e^\infty(t)).
\]
Bounded convergence in (2.9) yields
\[
\delta(t)\le\int_0^t\mathbb E W_e^\infty(v)\,dv.              \tag{2.10}
\]
For each fixed \(n\), take \(R\to\infty\) in (2.3), then take the countable infimum:
\[
\mathbb E W_e^\infty(t)\le L(t)\omega(\delta(t))
\quad\text{for almost every }t.                              \tag{2.11}
\]
This order matters. No equality between limiting extrema and extrema over an infinite-box intersection is used, and no infimum is moved across an integral.

**Osgood collapse.** The affine-infimum definition makes \(\omega\) finite, nonnegative, nondecreasing, and concave. Since \(\tau_n\to0\), it is continuous at zero with \(\omega(0)=0\). It is continuous on \((0,1)\) by concavity, and
\[
r\omega(1)\le\omega(r)\le\omega(1)
\]
proves continuity at \(1\). If \(\omega\equiv0\), (2.10)--(2.11) immediately imply \(\delta=0\).

Otherwise extend \(\omega\) constantly beyond \(1\), and define
\[
D(t)=\int_0^t L(v)\omega(\delta(v))\,dv.
\]
Then \(\delta\le D\), and \(D'\le L\widetilde\omega(D)\) almost everywhere. For \(\eta>0\),
\[
\int_\eta^{D(t)+\eta}\frac{dr}{\widetilde\omega(r)}
=\int_0^t\frac{D'(v)}{\widetilde\omega(D(v)+\eta)}\,dv
\le\int_0^tL(v)\,dv.
\]
If \(D(t)>0\), the left side diverges as \(\eta\downarrow0\), contradicting \(L\in L^1\). Thus \(D=\delta=0\).

**Whole-path stabilization.** At each coordinate all radius paths choose their birth times from the same finite own-clock list, or have initial occupancy or no birth. Each monotone radius sequence therefore eventually stabilizes as an entire coordinate path. The two limiting paths agree almost surely at every rational time and at \(1\), by \(\delta=0\) and countability. Their cadlag paths then agree everywhere, and (2.8) identifies them with \(X\). Consequently, at each coordinate some finite radius already has equal whole lower and upper paths. Equality only at time \(1\) would not suffice.

**The local totalization and its certificate.** At each coordinate choose the least radius with a finite local graph and equal whole paths; return their common path. If no radius succeeds, return only that coordinate's constant initial path. Graph finiteness, Borel thresholds, and equality of birth times from a finite list make this rule Borel. It is exactly equivariant and preserves initial values on every input.

A successful graph reads finitely many initial bits and complete clock labels. Every outside completion preserves the same graph, inspected empty predecessor lists, thresholds, and batch calculation. Every smaller-radius graph is contained in it, so the least-success choice is preserved too. Failures elsewhere cannot trigger a global reset. This is the asserted arbitrary-completion certificate.

Almost surely all coordinates succeed, and the map equals \(X\) as a whole path. It is causal almost surely because it equals the limit of causal finite-radius systems. Pointwise causality on exceptional inputs is not required.

**Uniqueness and composition.** Complete any other prescribed-marginal weak law by Appendix A. Its initial state and candidate field have the same product law, so the same collapse event occurs. Deterministic trapping identifies that law with the same total map. This proves uniqueness. Equivariance of the map and invariance of its input law give invariance of the path law.

For an initial finitary sampler, a successful relative query reads finitely many initial coordinates. Almost surely each has a finite source certificate. Their finite union, together with the queried fresh clock labels, fixes the whole output path under every outside completion. This proves the iid composition assertion without transferring any moment bound. \(\square\)

## 3. An explicit family with full-group dependence

Let \(G\) be any countably infinite group, and fix any enumeration \(g_1,g_2,\ldots\) of \(G\setminus\{e_G\}\) without repetitions. Set
\[
\Gamma=G\times C_2,\qquad s=(e_G,1),\qquad w_k=(g_k,0).
\]
The same fixed enumeration is used as right offsets at every root. Put
\[
p(t)=\frac12+\frac t8,\qquad
q(t)=\frac1{8(1-p(t))},\qquad d(t)=\frac{q(t)}2.
\]
Let \(\theta_h(x)\) be the lexicographic sign comparing
\[
(x_{hw_k})_{k\ge1}\quad\text{and}\quad(x_{hsw_k})_{k\ge1},
\]
with sign zero at equality. Define
\[
c_h(t,x)=q(t)+d(t)\theta_h(x)\bigl(p(t)-x_{hs}\bigr),\qquad
a_h(t,x)=(1-x_h)c_h(t,x).                                    \tag{3.1}
\]

**Theorem 3.1.** Using the ordinary DPP weak-existence input in Section 1, the rates (3.1) admit an invariant prescribed-generator process with marginals
\[
\mu_t=\operatorname{Bernoulli}(p(t))^\Gamma.
\]
Its whole coordinate paths have a total equivariant relative finitary realization and hence a finitary uniform-iid realization.

At every fixed time every off-root coordinate has strictly positive essential influence on the root rate. No version agreeing \(\mu_t\)-almost surely can depend only on a proper subgroup. The rates have no finite-mean full-local-neighborhood mixture and no everywhere continuous almost-sure representative, although they are themselves \(\mu_t\)-almost everywhere continuous. No query or radius moment is asserted.

### Proof

**Distinct offsets and the exact equation.** The pairs \(\{w_k,sw_k\}\) are disjoint and avoid \(\{e,s\}\): their first entries lie in one \(C_2\) layer, their second entries in the other, and the enumeration is nonrepeating and excludes the identity. Involutions in \(G\) cause no difficulty. Thus \(\theta_h\) is exterior to the updated pair \(\{h,hs\}\), and
\[
\theta_{hs}=-\theta_h
\]
at every input. Finite first-difference events make it Borel, and fixed right offsets make the rates covariant. Since \(p\in[1/2,5/8]\),
\[
\frac{11q}{16}\le c_h\le\frac{21q}{16}\le\frac7{16}=M.       \tag{3.2}
\]

The kernel \(K_t=p(t)I\) is linear, equivariant and uniformly gapped; its DPP is precisely \(\mu_t\). For a pair \(\{i,j\}=\{h,hs\}\), condition on its exterior. The pair perturbation has expectation \(d\theta_i p(1-p)^2\) times
\[
(f_{10}-f_{00})+(f_{11}-f_{10})
-(f_{01}-f_{00})-(f_{11}-f_{01})=0.                          \tag{3.3}
\]
Only finitely many pairs meet a cylinder support. The baseline rates \(q(1-x_h)\) give \(p'=q(1-p)=1/8\), so (3.3) proves the exact continuity equation for every finite cylinder, not merely the one-site identities. The bounded rates have the required finite mean activity. The ordinary weak input therefore applies.

**Finite box formula.** Take
\[
F_R=\{e,s,w_k,sw_k:1\le k\le R\}.
\]
For a finite box, enumerate its allowed partner bits and assignments of the first \(R\) paired labels. A first unequal pair fixes the sign. If the prefix is equal, all three tail signs are possible because infinitely many unused pairs remain. The extrema are the minimum and maximum of the finitely many allowed numbers
\[
q(t)+d(t)\varepsilon(p(t)-b),\qquad
\varepsilon\in\{-1,0,1\}.
\]
This is an exact Borel formula for BOX. It uses neither a Borel projection theorem nor continuity of the full rate.

**Width estimate.** Complete an ordinary weak reference using Appendix A and trap it between the finite-radius envelopes. For \(n\le R\), if all \(2n\) reference prefix labels are unambiguous and have a first unequal pair, the sign is fixed throughout the box. Then only partner ambiguity can change the intrinsic rate, by at most \(d\).

Otherwise bound the width by \(2dp\le5d/4\). The probability of some prefix ambiguity is at most \(2n\delta_R(t)\), using invariant envelope laws. Under the reference marginal, the equal-prefix probability is
\[
[p(t)^2+(1-p(t))^2]^n\le(17/32)^n.
\]
No independence between the ambiguity event and the reference is needed. Consequently
\[
\mathbb E W_e^R(t)
\le\left(\frac16+\frac{5n}{12}\right)\delta_R(t)
  +\frac5{24}(17/32)^n.                                     \tag{3.4}
\]
The envelope marginals are not assumed to be DPP marginals.

Thus WIDTH holds with \(L=1\), \(A_n=1/6+5n/12\), and
\(\tau_n=(5/24)(17/32)^n\). The affine-infimum modulus satisfies
\[
\frac7{12}r\le\omega(r)\le2r(1+\log(1/r)),\qquad0<r\le1,
\]
where the upper bound follows by choosing
\[
n=\max\{1,\lceil\log(1/r)/\log(32/17)\rceil\}.
\]
Its reciprocal integral diverges. Theorem 2.1 supplies the asserted process and whole-path certificates. The initial law is already iid Bernoulli\((1/2)\), so uniform-iid composition is immediate.

**Essential dependence.** For an offset \(h\ne e\), define
\[
\Delta_h(t)=\mathbb E_{\mu_t}
\left|a_e(t,X^{h,1})-a_e(t,X^{h,0})\right|.                  \tag{3.5}
\]
For \(h=w_k\), fix \(x_e=x_s=0\), every earlier label pair equal to \((0,0)\), \(x_{sw_k}=0\), and the next pair equal to \((0,1)\). Forcing \(x_{w_k}\) from zero to one changes the sign from \(-1\) to \(+1\), and the rate by \(2dp\). This finite cylinder on the other coordinates specifies \(2k+2\) zeros and one one. Hence
\[
\Delta_{w_k}(t)\ge2d(t)p(t)^2(1-p(t))^{2k+2}>0.              \tag{3.6}
\]
For \(h=sw_k\), use earlier zero pairs, \(x_{w_k}=0\), and the next pair \((1,0)\), again with the root pair vacant. Forcing the second label changes the sign from \(+1\) to \(-1\), giving the same lower bound:
\[
\Delta_{sw_k}(t)\ge2d(t)p(t)^2(1-p(t))^{2k+2}>0.             \tag{3.7}
\]
Finally set \(x_e=x_{sw_1}=0\), \(x_{w_1}=1\). The sign is \(+1\), independently of \(x_s\); forcing the partner changes the rate by \(d\), so
\[
\Delta_s(t)\ge d(t)p(t)(1-p(t))^2>0.                         \tag{3.8}
\]

If a version of the root rate were measurable in coordinates of a subgroup \(J\), any omitted coordinate would have zero influence: conditioning on all other coordinates, its Bernoulli bit has both values with positive probability, and almost-sure equality would force the two forced-bit rate values to agree. Equations (3.6)--(3.8) rule out every omission. Thus \(J=\Gamma\). The same conclusion holds for \(dt\,\mu_t\)-almost-sure versions on a fixed proper subgroup, by Fubini.

The essential-dependency graph actually contains every off-root edge. In particular, for finitely generated nonamenable \(G\), it contains any generating Cayley graph of \(G\times C_2\). The interaction is not reducible to amenable cosets.

**Local-mixture and continuity obstructions.** Every \(w_k\) has worst-case coordinate oscillation at least \(2dp\), by the same configurations. In a representation
\[
a_e(t,x)=\sum_m\lambda_m(t)b_m(t,x),\qquad
\lambda_m(t)\ge0,\quad0\le b_m\le1,
\]
with \(b_m\) depending on finite \(V_m\), summed coordinate oscillation is at most \(\sum_m\lambda_m(t)|V_m|\). Here it is infinite. No finite-mean neighborhood representation of this kind is possible.

At the all-zero configuration, putting a sole one at \(w_k\) or at \(sw_k\) gives root rates \(q+dp\) and \(q-dp\), respectively. Both configuration sequences converge coordinatewise to zero. Each value is constant on the corresponding open finite first-difference cylinder with the root pair vacant. Full support of \(\mu_t\) forces any continuous almost-sure representative to equal the constant throughout that cylinder, which contradicts continuity at zero. Nevertheless the actual rate is almost everywhere continuous: the first unequal label pair is finite almost surely, since its infinite-tie probability is \(\lim_n[p^2+(1-p)^2]^n=0\). \(\square\)

### The mean Osgood estimate

This family also has a mean-disagreement bound, distinct from its box estimate. For any coupling \(U,V\) with both marginals \(\mu_t\), put
\(\delta=\sup_j\mathbb P(U_j\ne V_j)\). Agreement at the first \(2n\) labels and a finite first difference there force equal signs, so
\[
\mathbb E|\theta_h(U)-\theta_h(V)|
\le4n\delta+2(17/32)^n.
\]
Separating center occupancy, partner, and sign yields
\[
\mathbb E|a_h(t,U)-a_h(t,V)|
\le\left(\frac{29}{48}+\frac{5n}{12}\right)\delta
 +\frac5{24}(17/32)^n
\le2\delta(1+\log(1/\delta)).
\]
The zero convention follows from countability. This estimate alone is not the reason for finitarity: Theorem 2.1 used the separate extrema bound (3.4).

## 4. A boundary for mean-disagreement criteria

The following proposition uses two free orbit types, an active orbit and a static environment orbit. This distinction is essential to its stated scope.

**Proposition 4.1.** On the two-orbit \((\mathbb Z\times C_2)\)-set there are bounded Borel covariant pure-birth rates with a causal exactly equivariant relative strong realization and full prescribed diagonal-DPP marginals, satisfying
\[
\sup_i\mathbb E|a_i(t,U)-a_i(t,V)|
\le4\delta(1+\log(1/\delta))
\]
for every coupling of those full marginals. Nevertheless no relative realization from the supplied initial configuration and independent fresh noise can have an almost-sure finite arbitrary-completion certificate even for the root active endpoint.

Appendix B gives the full construction and proof. The example does not disprove invariant weak existence, and it is not a single-regular-orbit or nonamenable counterexample. It concerns the prescribed dynamics from the supplied initial state. Its product endpoint marginal laws can be joined by other finitary monotone mechanisms.

## Appendix A. Compatible product-Poisson completion in the bounded case

Let \(X\) be a weak pure-birth law of Section 1. Put \(J_g(t)=X_g(t)-X_g(0)\). The coordinate martingale in (1.2) gives compensator
\[
\int_0^t a_g(v,X_{v-})\,dv.
\]
There is at most one actual birth at each coordinate.

Adjoin independent uniform variables \(U_g\) and independent auxiliary PRMs \(Q_g\), all independent of the whole original path. If a birth occurs at time \(T_g\), reveal \(U_g\) only at that time and mark the birth with height
\[
a_g(T_g,X_{T_g-})U_g.
\]
Zero rate at an actual birth has probability zero, by compensating
\(\int\mathbf1_{\{a_g=0\}}\,dJ_g\). In the common filtration use the path past, revealed birth marks, and the auxiliary-PRM past. Do not expose future \(U_g\)'s.

Uniform marking gives the actual-birth measure predictable compensator
\[
\mathbf1_{\{0<u\le a_g(t,X_{t-})\}}\,dt\,du.
\]
The auxiliary measure restricted to rejected heights,
\[
\mathbf1_{\{a_g(t,X_{t-})<u\le M\}}Q_g(dt\,du),
\]
has the complementary compensator. Original path martingales survive this progressive enlargement: the uniforms and auxiliary fields are independent of the original whole path, and only already occurred birth marks are revealed. Add actual marked births and rejected auxiliary marks to obtain \(N_g\). Its compensator is the deterministic \(dt\,du\).

Joint product independence still needs proof. For a finite set \(E\subset\Gamma\), the total count is dominated by \(|E|+\sum_{g\in E}Q_g((0,1]\times(0,M])\), so it is nonexplosive. The original no-simultaneous-birth assumption, diffuse independent auxiliary times, and independence from the original path make the combined finite marked field simple in time almost surely.

For nonnegative bounded deterministic functions \(f_g\), \(g\in E\), the exponential
\[
Z_t=\exp\left\{
-\sum_{g\in E}\int_{(0,t]\times(0,M]} f_g(v,u)\,N_g(dv\,du)
+\sum_{g\in E}\int_0^t\int_0^M(1-e^{-f_g(v,u)})\,du\,dv
\right\}
\]
is a local martingale by the jump formula and the deterministic compensators. It is bounded by \(e^{|E|M}\), hence a true martingale. Applying the same expression to a future interval \((s,t]\) yields, conditionally on the full common past,
\[
\mathbb E\!\left[
\exp\!\left(-\sum_{g\in E}\int_{(s,t]\times(0,M]}f_g\,dN_g\right)
\middle|\mathcal G_s\right]
=\exp\!\left(-\sum_{g\in E}\int_s^t\int_0^M(1-e^{-f_g})\,du\,dv\right).
\]
This is the joint conditional Laplace functional of product PRMs. Finite sets and a monotone-class argument give the entire countable product field, independent of \(X_0\), with future increments independent of the common past. Completion and right-continuous augmentation preserve the statement by bounded conditional-expectation limits.

Actual births supply exactly the marks below the current rate; auxiliary marks are strictly above it. Thus (1.3) holds simultaneously at all coordinates and times. This establishes compatibility for every weak law in the stated class, not just for an initially invariant one.

## Appendix B. Static block environments: Osgood control without relative finitarity

Let \(\Gamma=\mathbb Z\times C_2\), \(s=(0,1)\), and \(w_j=(j,0)\), \(j\ge1\). Coordinates have two types: active bits \(x_g\) and environmental bits \(\xi_g\). Initially all bits are independent fair Bernoulli. Partition the positive indices into consecutive disjoint blocks \(I_n\) of length \(2^n\), \(n\ge1\). Define
\[
A=\{\text{every block contains a one}\},\qquad
F_g(\xi)=\mathbf1_A((\xi_{gw_j})_{j\ge1}),\qquad
\theta_g=F_g-F_{gs}.
\]
The environment rates are zero. The active rates are
\[
a_g(t,x,\xi)
=(1-x_g)\left[q(t)+d(t)\theta_g(\xi)(p(t)-x_{gs})\right],      \tag{B.1}
\]
with the same \(p,q,d\) as in Section 3.

### B.1. Exact process and mean modulus

The event \(A\) is closed and has empty interior. Indeed every finite cylinder can be refined by forcing a wholly unread block to zero. Its probability is positive, since
\[
\mathbb P(A^c)\le\sum_{n\ge1}2^{-2^n}\le\frac13.
\]
Its complement has positive conditional measure in every finite cylinder.

Conditional on the environment, the active coordinates split into independent pairs \(\{g,gs\}\) with constant opposite signs. The cancellation (3.3) applies to each pair. Its finite-state forward equation has unique product Bernoulli\((p(t))\) solution from its independent fair pair. Independent pair clocks give a Borel equivariant causal strong realization. At time \(t\), conditional on any environment, every pair has the same product law, independent of its sign. Thus the full active law is iid Bernoulli\((p(t))\), independent of the unchanged fair environment. This proves every mixed cylinder of the prescribed diagonal DPP.

Let \(A_N\) check only the first \(N\) blocks, with \(A_0\) the whole space. These use
\(S_N=2^{N+1}-2\) bits. For \(q=2^{-2^{N+1}}\),
\[
\mathbb P(A_N\setminus A)
\le q+q^2+q^4+\cdots\le\frac q{1-q}.                          \tag{B.2}
\]
For any coupling of two fair product rays, with per-bit disagreement at most \(\delta\),
\[
\mathbb E|\mathbf1_A(Y)-\mathbf1_A(Z)|
\le S_N\delta+2\mathbb P(A_N\setminus A).                     \tag{B.3}
\]
For \(0<\delta\le1/4\), let \(x=\log_2(1/\delta)\) and choose the least \(N\ge0\) with \(2^{N+1}\ge x\). Then \(S_N\le2x\), \(q\le\delta\), and (B.2)--(B.3) give
\[
\mathbb E|\mathbf1_A(Y)-\mathbf1_A(Z)|
\le2\delta\log_2(1/\delta)+4\delta
\le7\omega(\delta),\quad \omega(r)=r(1+\log(1/r)).
\]
This includes \(N=0\) when \(\delta=1/4\).

For any coupling of the full active/environment marginals, the two ray estimates give
\(\mathbb E|\theta(U)-\theta(V)|\le14\omega(\delta)\). Therefore
\[
\mathbb E|a_g(U)-a_g(V)|
\le\frac{29}{48}\delta+\frac5{48}\mathbb E|\theta(U)-\theta(V)|
\le\frac{99}{48}\omega(\delta)<4\omega(\delta).
\]
For \(\delta\ge1/4\), use \(0\le a_g\le7/16\); at zero use countability. Environmental differences are zero. The estimate requires no independence between coupled copies or between discrepancy events.

### B.2. A continuity necessity for arbitrary-completion certificates

Let \(F(y,z)\) be any Borel binary output from supplied initial state \(y\) and independent fresh noise \(z\) of fixed law \(\nu\). Suppose finite arbitrary-completion certificates exist on a measurable conull set. Fubini gives a full noise section for almost every \(y\).

Fix such a \(y\) and any sequence \(y_n\to y\). For every noise input in that full section, keep the entire noise fixed. Eventually \(y_n\) agrees on the finite initial coordinates in its certificate. Hence
\[
F(y_n,z)=F(y,z)\quad\text{eventually}.
\]
Bounded convergence implies
\[
h(y_n)\to h(y),\qquad h(y)=\int F(y,z)\,d\nu(z).
\]
Thus the everywhere-defined conditional output-probability representative \(h\) is continuous at almost every supplied initial state. The arbitrary-completion convention is essential: the configurations \(y_n\) need not themselves be in the good set.

### B.3. The generator forces a discontinuous conditional kernel

Consider any process with the supplied initial law and rates (B.1) in its natural filtration. Zero environmental rates force the environment to remain constant. If the initial active pair at \(e,s\) is \((0,1)\), the partner remains occupied, and until the root birth its hazard is
\[
q(t)+d(t)\theta_e(p(t)-1)=q(t)-\theta_e/16.
\]
Conditioning the root coordinate martingale on the entire initial configuration gives its scalar survival integral equation. Boundedness gives its unique solution. Since \(\int_0^1q(t)\,dt=\log(4/3)\), the conditional endpoint probability is necessarily
\[
b(\theta_e)=1-\frac34 e^{\theta_e/16}                         \tag{B.4}
\]
for almost every supplied state on this initial pair event. This does not assume a particular Poisson representation or Markovness of the whole process.

Take the positive-measure initial set \(D\) on which the active pair is \((0,1)\), the \(e\)-ray belongs to \(A\), and the first block of the \(s\)-ray is all zero. On \(D\), \(\theta_e=1\).

Suppose a representative of (B.4) were almost surely correct and continuous at almost every initial state. Choose a correct continuity point \(y\in D\). In each increasing finite cylinder matching \(y\), choose a wholly unread \(e\)-ray block and force it to zero. Preserve the active pair and the already forced zero \(s\)-block. The resulting subcylinder has positive measure and forces \(\theta_e=0\). Intersect it with the full correctness set and choose \(y_n\) there. Then \(y_n\to y\), but the representative equals \(b(0)\) at every \(y_n\) and \(b(1)\) at \(y\), with \(b(0)\ne b(1)\). This contradicts continuity.

The necessity in B.2 rules out every supplied-state relative endpoint realization with almost-sure finite arbitrary-completion certificates. A whole-path certificate would give an endpoint certificate, so it is ruled out as well. This proves Proposition 4.1.

## Sources and relation to earlier formulations

Finite chronological ancestry and graphical particle-system constructions are classical tools; see Jan M. Swart, [A Course in Interacting Particle Systems, author notes](https://staff.utia.cas.cz/swart/lecture_notes/partic24_10_14.pdf), Chapter 4. For finite-neighborhood mixtures under spatial continuity and their relation to particle-system simulation, see A. Galves, N. L. Garcia, E. Löcherbach and E. Orlandi, [Kalikow-type decomposition for multicolor infinite range particle systems](https://arxiv.org/abs/1008.2740). A finite-neighborhood decomposition and finite mean neighborhood cost are different hypotheses. The present argument makes no priority claim for these construction tools.

The following table records mathematical source correspondence. Earlier formulations are not additional assumptions of Theorem 2.1.

| Source label | Mathematical role in this manuscript |
|---|---|
| Ordinary DPP weak input, G9 | Ordinary prescribed-marginal weak existence stated in Section 1; no invariant conclusion is imported. |
| B03 | Progressive product-Poisson completion; the bounded case is proved in Appendix A. |
| B04 | All-coupling Osgood mean criterion; the mean estimate in Section 3 is supplementary. |
| B05 with its Osgood-domain clarification | Finite rate boxes, local success, and whole-path stabilization method. |
| B06 | Two-generator predecessor of the exhaustive-offset family. |
| B07 | The exhaustive \(G\times C_2\) family of Section 3. |
| B08 | The finite-box criterion of Section 2. |
| R09 | The separate two-orbit boundary in Section 4 and Appendix B. |

The diagonal marginals used in the examples are elementary iid laws. The assertions concern their prescribed nonlocal generators and relative whole-path realizations. No result here establishes invariant weak existence for every finite-valued Borel exact-DPP rate field on an arbitrary nonamenable regular group.
