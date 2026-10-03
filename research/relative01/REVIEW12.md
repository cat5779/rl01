# R12 independent complete mathematical review

VERDICT: CORRECT_SCOPED_NOT_FRESH.

Frozen statement SHA256:bcb52e4e45939d40ebc0d1b3724cc0a030bee8dca781aff6fda48e045c45a7e4.
Frozen proof SHA256:dd1fba05fa0cbe6dfd78d43e3263e2306e4f3754b3dae99b2094d7a2eed94f5d.

I read both frozen files in full, independently reconstructed every new convolution, kernel, summability, sorting and geometric argument, and checked their interface to the already reviewed GENERAL/LOCAL/FOURIER/SAMPLER versions. This is a different-author reused-context review. It is not fresh, formal, an external referee report or a novelty certification. I did not modify either frozen source.

The accepted scope is the existence of this constructed increment/weighted-small-background relative finitary DPP process on every countable group containing an infinite-order element. Its moments use a constructed proper left-invariant metric. Arbitrary ordered pairs, groups without infinite-order elements, arbitrary large backgrounds and preassigned-metric/composed coding moments remain open.

## 1. Cyclic subgroup and quasi-Banach convolution bounds

The convolution convention is internally consistent: T_a f(i)=sum_g a(g)f(ig), so T_aT_c=T_(a*c), with (a*c)(g)=sum_h a(h)c(h^-1g). These operators commute with the left regular action.

For the infinite cyclic subgroup H=<z>, right multiplication by z stays inside each **left coset** xH. Its coset basis indexed by k has A=T_a as the Laurent convolution with the reviewed Fourier multiplier f>=0. This decomposition uses neither H normality nor centrality. The underlying coordinate action is still the single free regular action on Gamma; the coset argument does not invoke an unproved stabilizer sampler.

FOURIER's strictly positive coefficients on H have a(e)=1/8, sum1, symmetry and O(k^-2) decay. For p=3/5, 2p=6/5>1, hence L_p(a)<infinity.

For nonnegative kernels c,d,
\[
\begin{aligned}
\sum_x(c*d)(x)^p
&\le\sum_{x,h}c(h)^pd(h^{-1}x)^p\\
&=(\sum_hc(h)^p)(\sum_yd(y)^p).
\end{aligned}
\]
The inequality uses p-subadditivity and Tonelli; the change x=hy is a bijection in every group. Infinite nonnegative sums obey the same bound by monotone convergence. These are genuine pointwise coefficient estimates, not operator interpolation claims.

The geometric full-support zeta has mass1 and is symmetric even if enumeration/inversion produces repeated atoms. Its L_p upper bound follows by applying p-subadditivity to those separate atoms. Thus mu=(a+zeta)/2 is full support, symmetric and has finite L_mu. The chosen positive eta makes eta^p L_mu<=1/4.

Each mu^n is a symmetric probability: inversion reverses the product order, but all n factors are the same mu. Hence w is a symmetric full-support probability. Since w(e)>=1/Z>=1-eta, its off-identity convolution norm is at most1-w(e), giving W>=(1-2eta)I and W<=I. Operator positivity is correctly proved from identity mass rather than from entrywise positivity.

The proof's L_p(w)<=4/3 follows directly from the preceding kernel inequalities and its convergent geometric series. The coefficient convolution estimate sum_j c_jc_(n-j)<=16c_n has the correct half-sum estimate; dividing by Z^2 gives w*w<=16w/Z<=16w and w^3<=256w.

## 2. Both convolution directions and the sandwich

The shifted series estimate is
\[
\mu*w=w*\mu\le(4/\eta)w.
\]
Here the equality is only because w is a series of powers of mu. The proof never infers that a commutes with w.

Since a<=2mu, each of the two inequalities is derived separately:
\[
a*w\le2\mu*w\le8w/\eta,\qquad
w*a\le2w*\mu\le8w/\eta.
\]
Thus, in the exact displayed order,
\[
v=a*w*a\le(8/\eta)w*a\le64\eta^{-2}w.
\]
Retaining the two identity atoms of a gives v>=a(e)^2w=w/64. Its mass, symmetry and full support follow from the product, reversal of the palindromic factors and this lower bound.

Set L0=64eta^-2,c0=1/64. Nonnegative convolution is order-preserving without commutativity, so
\[
v^3\le L0^3w^3\le256L0^3w
 \le(256L0^3/c0)v=2^{32}\eta^{-6}v.
\]
This verifies the stated finite M.

For the required **left** shift,
\[
\mu(g)\delta_g*w\le\mu*w\le4w/\eta.
\]
Combining the upper and lower comparisons gives
\[
\delta_g*v\le L0\delta_g*w
 \le(L0/c0)\frac4{\eta\mu(g)}v
 =\frac{16384}{\eta^3\mu(g)}v.
\]
The constant is finite and symmetric under g->g^-1 because mu is symmetric. Its orientation is exactly the |b|*v estimate needed by GENERAL. Consequently every finite Hermitian background satisfying sum_g|b(g)|C_g<=1/32 meets that analytic theorem. Scaling any fixed finite-support Hermitian shape suffices, with an explicitly support-dependent bound.

## 3. Positivity and the exact kernel of AWA

A is a positive contraction and (1-2eta)I<=W<=I. Therefore
\[
0\le V=AWA\le A^2\le I,\quad
\langle x,Vx\rangle=\langle Ax,W Ax\rangle
 \ge(1-2eta)\|Ax\|^2.
\]
If Vx=0 then Ax=0; the reverse implication is immediate. Thus
\[
\ker V=\ker A,\qquad\ker V^2=\ker A.
\]
The latter also follows from selfadjoint positivity and ||Vx||^2=<x,V^2x>. No AW=WA assumption occurs.

With delta=1/(32M), sigma=kappa+delta M<=1/16. GENERAL's two-sided gap and exact real-part/self-vacancy rates apply unchanged; b need not commute with V or H=V^2.

For u=|b|+delta(v*v), u*v<=sigma v and delta_e<=v/v(e). Left-convolving this initial inequality repeatedly gives u^n<=sigma^n v/v(e). Therefore the same inverse majorant is bounded by A0 v, with A0=2/[v(e)(1-2sigma)]. The product orientation in the influence estimate is retained:
\[
((v*v)*R)(g)\le A0 v^3(g)\le A0 Mv(g).
\]
Together with R(g^-1)<=A0v(g^-1)=A0v(g), this yields q<=Q0v^2. It requires symmetry of v only; it does not make (v*v)*R symmetric or reorder it.

## 4. Exhaustive sorting and constructed proper metric

The quasi-norm convolution estimate gives L_p(v)<=L_p(a)^2L_p(w)<=4L_a^2/3<infinity. All nonidentity inverse-pair weights are positive.

For precision, a descending exhaustive ordering exists as follows. Any positive threshold has only finitely many weights at least that threshold. Among the remaining weights the supremum is positive and is attained: the weights above half that supremum form a finite set. Choose a maximum, with the fixed auxiliary tie rule, and repeat. Every fixed positive weight has only finitely many weights above or equal to it, hence is eventually selected. This proves exhaustiveness, not merely existence of an arbitrary enumeration.

At the j-th pair,
\[
L\ge\sum_{k=1}^jv(h_k)^p\ge jv(h_j)^p.
\]
This bound remains valid for order-two singleton pairs because each pair contributes at least one group element. Its omitted multiplicity is harmless for an upper bound.

Assign h_j and its inverse equal integer cost j and take the least representing-word cost. Every element has a one-letter representation, inverse words have the same cost, and concatenation gives subadditivity. A nonidentity cannot have cost0. For any fixed integer budget only finitely many letters and boundedly many words have that budget. Relations can only identify their values; they cannot create infinitely many values. This proves a proper left-invariant metric.

The neighborhoods are explicit coefficient prefixes, **not metric balls**:
\[
V_m=\{e\}\cup\{h_j^{\pm1}:j\le2^m\},\quad
|V_m|\le3\cdot2^m,\quad \max_{g\in V_m}\ell(g)\le2^m.
\]
No prescribed growth bound is used. The inverse-pair multiplicity at most2 and the decreasing-series integral give
\[
\sum_{g\notin V_m}v(g)^2
 \le2L^{10/3}\sum_{j>2^m}j^{-10/3}
 \le(6/7)L^{10/3}2^{-7m/3}.
\]
The exponent and constant are correct.

## 5. Local-mixture, all-input certificates and moments

The neighborhoods contain the center. For configurations agreeing there, the actual rates have the same occupation factor, and their remaining oscillation is at most the q-tail. GENERAL's joint continuity ensures the lower cylinder infima are Borel and continuous in time for each fixed pattern.

The lower envelopes increase and have a uniform error tending to zero. Their positive increments are bounded by the preceding cylinder's oscillation. Dividing by lambda_m=T0 2^(-7(m-1)/3) puts every normalized update in [0,1]. The initial lambda0=4delta bounds l0. The center-occupied patterns give zero in every component.

Here V0 contains the first inverse pair, rather than just e. That is allowed by LOCAL Section1, which only requires a finite neighborhood containing e. The proof directly uses that theorem, not an inappropriate restriction of its Section7 example.

For m>=1 the count budget is bounded by a constant times2^(-4m/3), and the length budget by a constant times2^(-m/3); their geometric ratios are2^-4/3 and2^-1/3. The finite m=0 term has |V0|<=3 and radius<=1. Thus both B and B1 are finite.

The reviewed LOCAL Section8 version has strict-time ancestors, complete consulted labels, tie batches, and a coordinate-local fallback. Its noise-only finite-ancestry event works simultaneously for every initial configuration. A successful whole-path query is stable under arbitrary outside completions. GENERAL's global fallback is not imported as a finitary totalization.

The independently checked LOCAL Section9 chain calculation includes markless endpoint sites; it gives mean label count<=exp(B) and mean radius<=B1exp(B). These are relative to the supplied initial configuration and in the constructed metric. No composed coding moment is asserted.

The exact DPP cylinder equation from GENERAL and forward uniqueness from LOCAL identify all fixed-time marginals of the new local-clock realization, starting at the supplied independent X~DPP(I/2+T_b). The gapped imported sampler applies to this one free regular orbit. Splitting independent channels and unioning finitely many initial certificates with the finite relative clock-label set gives the claimed joint iid finitary endpoint map. It does not require a sampler for the nongapped increment V^2.

## 6. Fourier obstruction and scope

Each left coset has every L2 zero-arc field in ker A=ker(V^2). A finitely supported vector y with yy*<=V^2 must be orthogonal to all those fields. On each coset its Fourier transform is a finite Laurent polynomial zero almost everywhere on an open arc; continuity and polynomial uniqueness force that component to vanish. Thus y=0.

A bounded finite-propagation T in the proper metric has finite-support columns. Each column y=Tdelta_i obeys yy*<=TT*<=V^2, so all columns vanish. This argument is independent of T equivariance and subgroup normality.

F2 is covered by an infinite-order generator while its center is trivial, establishing the strict ambient-group enlargement relative to the central-cyclic hypothesis. The proof does not claim that the particular R10 kernels are literally reproduced, nor import R10's optional noncommuting assertion into all new groups.

No mathematical correction is required. The original frozen statement remains exactly restricted to constructed increments, weighted-small finite backgrounds and the constructed metric, with no general JO, arbitrary-background or moment-upgrade claim.

## 7. Auxiliary verification

CHECK12.py and CHECK12.json independently checks exact right-convolution/sandwich/coset bookkeeping in S3 with a **nonnormal** subgroup and noncommuting A,W. It verifies ranks of A,AWA,(AWA)^2, left-coset preservation, finite shift bounds and the constants2^32/16384. It also checks121 coefficient inequalities and finite formal-word counts.

This finite example is a sanity fixture, not an infinite-order subgroup, spectral-zero-arc proof or formal verification. The infinite bridge is the analytic derivation above.
