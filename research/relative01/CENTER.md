# Relative finitary DPP processes from a central infinite cyclic subgroup

Let Gamma be any countable group with a specified central element z of infinite order. The construction below chooses a proper left-invariant metric and a strictly positive symmetric probability v, with H=T_v^2, M=110592, and delta=1/(32M). For every finite-support Hermitian background b satisfying the explicit weighted bound sum_g |b(g)| C_g<=1/32, the path K_t=I/2+T_b+delta tH has the stated relative pure-birth DPP realization. Smallness is relative to this weighted bound; an ordinary l1 threshold independent of the support is not asserted.

Every whole coordinate path has an almost-sure finite certificate under arbitrary outside completions, finite expected relative query count and finite first relative radius moment in the constructed metric. The separately imported gapped sampler gives a joint finitary iid process, with no composed moment bound. The increment has no nonzero finite-propagation positive square minorant. If Gamma is nonamenable, the background can be chosen not to commute with H.

Use the convolution conventions and the corrected analytic rate theorem of [GENERAL.md](GENERAL.md), the finite-query interface of [LOCAL.md](LOCAL.md), the explicit scalar coefficients of [FOURIER.md](FOURIER.md), and the imported initial sampler in [SAMPLER.md](SAMPLER.md). Product groups G x Z are a specialization. Section 7 gives a group not isomorphic to any such product. General ordered DPP factors remain open.

## 1. The walk on the ambient group

Let Z0=<z> be the specified central infinite cyclic subgroup of Gamma. Choose a sequence (g_i) listing every group element, repetitions permitted. Formal letters g_i and their inverses have cost i. The least representing-word cost ell is symmetric and subadditive, is positive away from the identity, and has ball bound |{g:ell(g)<=m}|<=3^m: the formal-word counting series is (1-s)/(1-3s). This gives a proper left-invariant metric. Put c_z=ell(z)<infinity, so ell(z^k)<=c_z |k|.

Define rho=1/243,

    zeta=(1-rho)/(2rho) sum_(i>=1) rho^i(delta_(g_i)+delta_(g_i^-1)),
    mu0=(31/32)delta_e+(1/32)zeta.

They are symmetric probabilities, zeta and mu0 have full support, and their 27^ell moments are at most 121/4 and 245/128, respectively. The geometric-series calculation only uses ell(g_i)<=i.

For the basic construction take mu=mu0. For the later noncommuting assertion, choose a lift h of a noncentral symmetric pair in Gamma/Z0 and arrange g_1=h. With nu=(delta_h+delta_(h^-1))/2, choose mu=(1-t)nu+t mu0, where 0<t<1 is rational and its pushforward to Gamma/Z0 is noncentral. Section 6 proves that this choice is possible. Its 27^ell moment is at most 27. The central element z need not have enumeration index one; its finite cost c_z only changes the radius constant below.

Set eta=1/128, Z=sum_(n>=0) eta^n/(n+1)^2, and

    w=Z^(-1)sum_(n>=0) eta^n mu^(*n)/(n+1)^2.

The same positive coefficient calculation gives w*w<=16w and w^3<=256w. Indeed the convolution of eta^n/(n+1)^2 with itself is at most 16 times that sequence, and Z>=1. The probability w is symmetric and strictly positive. Its identity mass is at least 1-eta, so W=T_w is positive invertible with W>=(1-2eta)I and norm at most one.

Subadditivity and the moment of mu give

    sum_g 27^ell(g) w(g) <=1/(1-27eta)=128/101<2,
    sum_(ell(g)>m) w(g)<=2*27^(-m).

For every g, mu(g)>0 and delta_g<=mu/mu(g). Shifting the coefficient sequence gives mu*w<=(4/eta)w, hence

    delta_g*w<=C_g w,    C_g=4/[eta mu(g)]<infinity.

The identity shift can instead use C_e=1. These inequalities hold on any countable group; no finite generation or commutativity was assumed.

## 2. Insert the central Fourier factor

Let vZ(k) be the coefficients from FOURIER.md of f(theta)=(1-2|theta|/pi)_+^3. Precisely vZ(0)=1/8 and, for k!=0,

    vZ(k)=6/(pi^2 k^2)-48(1-cos(k pi/2))/(pi^4 k^4).

The previously reviewed elementary integration and estimates give a strictly positive symmetric probability with

    [16(1+k^2)]^(-1)<=vZ(k)<=(1+k^2)^(-1),
    vZ^3<=432 vZ.

Embed it on Z0 as a(z^k)=vZ(k), zero elsewhere. Infinite order makes this definition unambiguous. Since Z0 is central, a commutes under convolution with every kernel on Gamma. The operator A=T_a is a positive contraction: on each coset of Z0 it is the same convolution with Fourier multiplier f>=0.

Define v=a*w. It is a symmetric probability, and is strictly positive because v(g)>=a(e)w(g)>0. Centrality, positivity and the preceding convolution estimates imply

    v^3=a^3*w^3<=432*256 a*w=Mv,    M=110592.

Also v(e)>=w(e)/8>=(1-eta)/8. The operators A and W commute; V=T_v=AW is a positive contraction and H=V^2=A^2W^2. Neither positivity nor this factorization requires Gamma to be a direct product.

For any g, centrality gives delta_g*v=a*(delta_g*w)<=C_g v. Thus every finite-support Hermitian b has

    |b|*v<=kappa v,    kappa=sum_g |b(g)| C_g.

Scaling b makes kappa<=1/32. Fix delta=1/(32M). Then kappa+delta M<=1/16, inside GENERAL.md's 1/8 budget. Its exact same rates

    a_i(t,x)=-delta(1-x_i) Re[H(K_t-D_(x^c))^(-1)]_(ii),
    K_t=I/2+T_b+delta tH,

are everywhere nonnegative, bounded by 4delta, continuous and equivariant, and satisfy every finite-cylinder DPP equation. GENERAL.md with its incorporated envelope-order correction supplies their causal relative strong process and the exact prescribed marginals. There is a common two-sided gap, at least [3/8,5/8].

## 3. The new squared tail estimate

Put B_m={g:ell(g)<=m} and Z_m={z^k:|k|<=9^m}; let V_m=B_m Z_m for m>=1 and V_0={e}. These sets are nested, finite, contain the identity and exhaust Gamma. Even if some products coincide,

    |V_m|<=3^m(2*9^m+1)<=3*27^m,
    max_(x in V_m) ell(x)<=m+c_z9^m<=(1+c_z)9^m.

Write w=w_in+w_out by restriction to B_m, and a=a_in+a_out by restriction to Z_m. As a is central, v=w*a. The nonnegative term w_in*a_in is supported inside V_m. Hence pointwise outside V_m,

    v <= w_out*a+w_in*a_out.

Young's l1*l2 bound on a discrete group, followed by (u+v)^2<=2u^2+2v^2, gives

    sum_(x outside V_m) v(x)^2
       <=2||w_out||_1^2 ||a||_2^2
          +2||w_in||_1^2 ||a_out||_2^2.

The probability norms are at most one. The w-tail is at most 2*27^(-m), and

    ||a_out||_2^2 <= 2 sum_(k>9^m) k^(-4)
                   <=(2/3)9^(-3m).

Consequently

    sum_(x outside V_m) v(x)^2 <=(28/3)3^(-6m).             (1)

This bound replaces the product-coordinate tail calculation; no uniqueness of the representation x=g z^k was used.

## 4. Finite certificates and relative moments

For the inverse majorant of GENERAL.md put u=|b|+delta(v*v), sigma=kappa+delta M<=1/16. Then u*v<=sigma v and delta_e<=v/v(e). Induction gives u^(*n)<=sigma^n v/v(e). Its positive inverse series therefore satisfies

    r<=A0 v,    A0=2/[v(e)(1-2sigma)]<20.

Here A0 is a scalar bound, not the operator A. GENERAL.md's intrinsic forced-vacant influence is

    q(g)=5delta[(v*v)*r](g)r(g^-1)
         <=5delta M A0^2 v(g)^2<=63v(g)^2.

Using (1),

    sum_(g outside V_m)q(g)<=588*3^(-6m).                  (2)

Take local infima of the continuous actual rate on each finite-pattern fiber V_m. The influence estimate bounds their uniform error by (2). Successive differences yield an exact nonnegative local-update mixture with

    lambda_0=lambda_1=4delta,
    lambda_m=588*3^(-6(m-1)) for m>=2.

Each local normalized update lies in [0,1] and vanishes when the center is occupied. Zero differences can be assigned the zero function. The first two weights are harmless upper bounds; the later weights bound the preceding neighborhood's oscillation. The sum telescopes uniformly to the actual rate.

The dependency budget B=sum_m lambda_m |V_m| is finite: its tail ratio is 27/729=1/27. The length-weighted budget B1=sum_m lambda_m sum_(g in V_m)ell(g) is finite: its ratio is 27*9/729=1/3. Their constants can depend on Gamma's chosen enumeration and c_z.

The corrected local graphical construction gives a finite ancestor query for every whole coordinate path on a common noise-only conull event for every initial input. A successful query reads complete site labels and strictly earlier predecessor lists; tied times are processed in batches from pre-time states, and a failed query has only its own coordinate's constant fallback. Thus arbitrary changes to unread inputs cannot invalidate a successful certificate. Counting dependency chains gives expected relative query count <=exp(B) and expected relative radius <=B1 exp(B). GENERAL.md's exact DPP equation and the local-mixture forward-uniqueness theorem identify every marginal.

The existing gapped finite-free-type DPP sampler applies to I/2+T_b on the one regular orbit. Its source/version and limitations are recorded in SAMPLER.md. Composing independent initial and clock channels, and taking the finite union of initial certificates at the finitely many relative queried sites, gives a whole-path joint finitary iid process. No query or radius moment is claimed after that composition.

## 5. No finite-propagation positive square minorant

Because W is positive invertible and commutes with A, ker H=ker A. Decompose l2(Gamma) as the orthogonal sum over cosets of Z0; on every coset A acts as the same Laurent convolution with multiplier f. The zero arc pi/2<|theta|<pi supplies all square-integrable fields supported in that arc to ker A on each coset.

If a finitely supported vector y satisfies yy*<=H, it is orthogonal to ker H: test the quadratic inequality on each vector in the kernel. On each coset its Fourier transform is a finite Laurent polynomial, and orthogonality to the zero-arc fields makes that polynomial zero almost everywhere on the arc. Continuity and uniqueness of a polynomial force it to vanish identically. Thus every coset component of y is zero, so y=0.

If T is a finite-propagation operator in the proper metric and TT*<=H, each column y=T delta_i has finite support and yy*<=TT*<=H. Every column is therefore zero, hence T=0. Equivariance of T was not assumed. This is a spectral-zero obstruction to square-minorant methods, not to the relative coupling just constructed.

## 6. A noncommuting background detected in the quotient

Assume Gamma is nonamenable and set Q=Gamma/Z0. Since Z0 is amenable, amenability of Q would imply amenability of Gamma by the extension closure. Thus Q is nonamenable. These closure facts are classical; a primary reference is [Juschenko's Lecture 2](https://web.ma.utexas.edu/users/juschenko/files/Lecture2.pdf), Sections 0.3--0.4.

In a nonamenable countable group there exists a noncentral symmetric pair measure. Otherwise each element has at most the two conjugates {g,g^-1}; every finitely generated subgroup then has a finite-index center, obtained by intersecting the finitely many generator centralizers. It is virtually abelian and amenable, so local amenability would make the whole group amenable. Apply this to Q and lift its pair to h in Gamma.

Let pi be the positive l1 convolution homomorphism to Q, (pi c)(q)=sum_(g in q)c(g). For nu and mu0 of Section 1, at most one t can make pi((1-t)nu+t mu0) central: two such affine combinations would imply pi nu central. Choose a different rational t in (0,1), obtaining the asserted mu and noncentral bar mu=pi mu.

Write bar w=pi w. On l2(Q), T_(bar w)=F(T_(bar mu)), where

    F(x)=Z^(-1) integral_0^1 [-log s]/[1-eta s x] ds.

Its derivative is strictly positive for -1<=x<=1. Thus T_(bar mu) is a continuous function of T_(bar w). Noncentrality of bar mu provides a right-convolution unitary not commuting with it; at least one Hermitian real or imaginary part also fails to commute. Let bar b0 be that finite-support Hermitian kernel and lift it to a finite-support Hermitian b0 on Gamma using a lift of the unitary's group element. Commutation with T_(bar w)^2 would imply commutation with its positive square root and then with T_(bar mu), a contradiction.

Crucially pi a=delta_e, because all of a is supported on the quotient kernel and its mass is one. Therefore the l1 kernel of the commutator satisfies

    pi([b0, a^2*w^2])=[bar b0,bar w^2]!=0.

The regular representation is faithful on l1 kernels, so [T_(b0),H]!=0. Scale b0 by a nonzero sufficiently small real number to meet kappa<=1/32; noncommutation persists. The spectral zero cannot erase this commutator, since it has already been detected by the quotient homomorphism. The unitaries here are RIGHT convolution, not the left regular action, which commutes with every equivariant operator in the theorem.

## 7. A group covered here that cannot split off Z

Let H3(Z) be the integer Heisenberg group, represented by upper unitriangular 3-by-3 integer matrices. Direct multiplication shows its center consists exactly of the top-right-coordinate matrices, an infinite cyclic group generated by z, and z is the commutator of the two elementary adjacent-coordinate generators. Let Gamma=H3(Z) x F_2. The free group F_2 has trivial center, so the center of Gamma is precisely <z>, entirely contained in its commutator subgroup. Gamma is nonamenable because it maps onto F_2.

Any abstract group G x Z has a central infinite-order element (e,1) whose image in its abelianization is nonzero. It therefore cannot have its entire center contained in its commutator subgroup. The displayed Gamma cannot be isomorphic to any G x Z, but satisfies this theorem. Thus the central-cyclic hypothesis extends the ambient class of the preceding product construction. This is an internal scope enlargement; no global novelty assertion is made.

General groups without a central infinite-order element, arbitrary large backgrounds, arbitrary increments, preassigned metric moment bounds, and unrestricted JO remain outside the claim.
