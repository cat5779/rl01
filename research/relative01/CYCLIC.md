# Relative finitary dynamics along any infinite cyclic subgroup

Let Gamma be any countable group containing an infinite-order element. The construction below gives a relative finitary DPP birth process for explicit spectral-zero increments and weighted-small finite-support Hermitian backgrounds, with finite relative query and radius expectations in a constructed proper metric. It does not require a central or normal cyclic subgroup.

Dependencies are [GENERAL](GENERAL.md), [LOCAL](LOCAL.md), [FOURIER](FOURIER.md), and the imported [SAMPLER](SAMPLER.md). The complete new sandwich and coefficient-ordering arguments follow. The stated scope is independently reviewed in [REVIEW12.md](REVIEW12.md).

## 1. A cyclic probability and a full-support walk

Use convolution (f*g)(x)=sum_y f(y)g(y^-1 x) and right convolution T_f u(x)=sum_g f(g)u(xg), so T_f T_g=T_(f*g). Every such operator commutes with left translation. Fix p=3/5 and write L_p(f)=sum_g |f(g)|^p. For nonnegative kernels,

    L_p(f*g) <= L_p(f)L_p(g),

by (sum a_i)^p<=sum a_i^p, Tonelli, and the group change of variables. The same subadditivity bounds infinite sums of nonnegative kernels.

Let a(z^k) be FOURIER's coefficients of f(theta)=(1-2|theta|/pi)_+^3, and set a=0 off <z>. This is a symmetric probability, a(e)=1/8, with 0<a(z^k)<=1/(1+k^2). Thus L_a:=L_p(a)<infinity since 2p=6/5>1. On every left coset of <z>, right convolution A=T_a is the same positive contraction with multiplier f. This assertion does not use normality of <z>.

Choose any enumeration g_j, j>=1, of Gamma, take rho=1/4, and put

    zeta=(1-rho)/2 sum_(j>=1) rho^(j-1)(delta_gj+delta_gj^-1).

Repetitions caused by inverses do not affect its probability normalization, symmetry or full support. Subadditivity gives

    L_p(zeta) <= 2((1-rho)/2)^p/(1-rho^p) < infinity.

Set mu=(a+zeta)/2. It is a symmetric full-support probability, dominates a/2, and L_mu:=L_p(mu)<infinity. Choose

    0<eta<=min(1/128,(4 L_mu)^(-1/p)).

Let Z=sum_(n>=0) eta^n/(n+1)^2 and

    w=Z^-1 sum_(n>=0) eta^n mu^(*n)/(n+1)^2,   W=T_w.

It is a symmetric full-support probability. Since 1<=Z<=1/(1-eta), w(e)>=1/Z>=1-eta. The norm of the off-identity convolution is at most 1-w(e), giving

    (1-2eta)I <= W <= I.

The upper bound follows also from its probability norm and self-adjointness. Operator positivity is supplied by identity mass, not inferred from nonnegative coefficients alone.

Subadditivity and the convolution inequality give

    L_p(w) <= Z^-p sum_n eta^(np) L_mu^n/(n+1)^(2p)
            <= 1/(1-eta^p L_mu) <= 4/3.                 (1)

For c_n=eta^n/(n+1)^2, splitting the sum at n/2 gives

    sum_(j=0)^n c_j c_(n-j) <= 16 c_n.

Indeed on the half with j<=n/2, (n-j+1)^-2<=4(n+1)^-2 and sum_j(j+1)^-2<2; doubling gives16. Therefore w*w<=16w/Z<=16w and w^(*3)<=256w.

Shifting the series index also gives

    mu*w=w*mu <= (4/eta)w.                             (2)

For n>=1 the ratio of eta^(n-1)/n^2 to eta^n/(n+1)^2 is at most4/eta. In particular a*w<=8w/eta and w*a<=8w/eta. The two sides are proved separately; a and w are not assumed to commute.

## 2. Sandwiching preserves the kernel and supplies every majorant

Put v=a*w*a and V=A W A. Then v is symmetric, strictly positive and a probability. Nonnegative convolution and (2) give

    w/64 <= v <= (64/eta^2)w.                          (3)

The lower bound retains both identity atoms of a; the upper bound first uses a*w<=8w/eta and then w*a<=8w/eta. Thus

    v^(*3) <= (64/eta^2)^3 w^(*3)
            <= 2^32 eta^-6 v =: Mv.                   (4)

Furthermore V is a positive contraction, because W is positive and bounded above by I and A is a positive contraction. Its kernel is exactly ker A:

    <Vx,x>=<WAx,Ax> >= (1-2eta)||Ax||^2.

Conversely Ax=0 implies Vx=0. In particular ker(V^2)=ker A, without any commutation between A and W.

For each g, mu(g)delta_g<=mu and (2) imply

    delta_g*w <= 4w/[eta mu(g)].

Combining this with (3) gives the valid left-shift bound

    delta_g*v <= C_g v,   C_g=16384/[eta^3 mu(g)].       (5)

All C_g are finite and C_g=C_(g^-1). Right shifts are available by inversion but are not required for the background estimate. For any finite-support Hermitian b satisfying

    kappa:=sum_g |b(g)| C_g <=1/32,                    (6)

we have |b|*v<=kappa v. Every chosen finite-support Hermitian shape can be scaled to satisfy (6). This is a support-dependent weighted condition, not a support-independent ordinary l1 threshold.

Take delta=1/(32M), H=V^2 and K_t=I/2+T_b+delta tH. Then sigma=kappa+delta M<=1/16. All GENERAL hypotheses hold, with a common gap [3/8,5/8]. Its exact continuous nonnegative birth rates are

    r_i(t,x)=-delta(1-x_i) Re[H(K_t-D_(x^c))^-1]_(ii),

bounded by4delta. GENERAL, including its envelope-before-collapse correction, supplies the exact DPP cylinder equations, common-input process and marginal identification. No new argument silently changes the rate or the prescribed initial configuration.

For quantitative tails, put v0=v(e)>0 and u=|b|+delta(v*v). Then u*v<=sigma v and delta_e<=v/v0, hence u^(*n)<=sigma^n v/v0. The inverse majorant in GENERAL therefore satisfies

    R=2 sum_n 2^n u^(*n) <= A0 v,
    A0=2/[v0(1-2sigma)].

Consequently its vacant-site influence kernel obeys

    q(g)=5delta[(v*v)*R](g) R(g^-1)
        <= Q0 v(g)^2,   Q0=5delta M A0^2 < infinity.    (7)

This uses symmetry of v, not symmetry or commutation of the general convolution product (v*v)*R.

## 3. Ordering coefficients gives finite query and radius costs

By the ell_p convolution bound and (1),

    L:=L_p(v) <= (4/3)L_a^2 < infinity.                 (8)

Enumerate the inverse-pairs in Gamma minus {e} as {h_j,h_j^-1}, in nonincreasing order of v(h_j), breaking ties using any fixed enumeration. Order-two elements form singleton pairs. This enumeration exists and exhausts the pairs: all coefficients are positive, and at any positive threshold only finitely many can exceed it by (8). Each pair weight obeys

    v(h_j) <= (L/j)^(1/p).                            (9)

Assign both letters h_j and h_j^-1 cost j. Define ell(g) to be the smallest total cost of a finite word representing g. Every element is one of the letters or the identity, so ell is finite, symmetric and subadditive. Nonidentity lengths are positive integers. For any cost bound only finitely many letters and words are possible, hence ell defines a proper left-invariant metric on Gamma. In particular ell(h_j)<=j.

For m>=0 put

    V_m={e} union {h_j,h_j^-1: j<=2^m}.

These symmetric neighborhoods are nested and exhaust Gamma. They satisfy |V_m|<=3*2^m and radius(V_m)<=2^m. By (9) and the integral bound for a decreasing power series,

    sum_(g outside V_m) v(g)^2
       <=2 L^(2/p) sum_(j>2^m) j^(-2/p)
       <= [2L^(2/p)/(2/p-1)] 2^(m(1-2/p))
        = (6/7)L^(10/3) 2^(-7m/3).                   (10)

Set T0=Q0(6/7)L^(10/3). The actual rates have oscillation at most T0 2^(-7m/3) on configurations agreeing on V_m, since V_m contains the center and the vacant-site influence bound (7) controls every other coordinate. The estimate is uniform in time.

Let l_m(t,x) be the infimum of the root rate over the finite cylinder x|V_m. Compactness and joint continuity make l_m Borel (in fact continuous in t for each cylinder). These local functions increase to the actual rate uniformly. Decompose

    r_e=l_0+sum_(m>=1)(l_m-l_(m-1)).

Use constant mixture weights lambda_0=4delta and lambda_m=T0 2^(-7(m-1)/3), m>=1, dividing each respective nonnegative increment by its weight. Each component takes values in [0,1], depends only on V_m, and vanishes at an occupied center. These are exactly the LOCAL hypotheses. The resulting costs satisfy

    B=sum_m lambda_m |V_m|<infinity,
    B1=sum_m lambda_m sum_(g in V_m) ell(g)<infinity.

Their tails are geometric with ratios 2^(-4/3) and 2^(-1/3), respectively, using |V_m| radius(V_m)<=3*2^(2m). No growth bound for preassigned word balls has been assumed.

LOCAL's strict-time ancestry, batch convention and query-local fallback consequently give an everywhere Borel, exactly equivariant relative map, with a finite arbitrary-completion certificate for each whole coordinate path almost surely. It uses the supplied initial configuration and independent complete site labels. The query-count and maximum-radius expectations are bounded by exp(B) and B1 exp(B), respectively. These are relative moments in this constructed metric. The accepted graphical uniqueness and cylinder-equation arguments identify its marginals as DPP(K_t).

Applying the separately imported gapped initial sampler to I/2+T_b and taking finite unions of its certificates at the finitely many queried initial sites gives a joint iid finitary ordered endpoint map. This does not assert finite composed coding moments, finite random-bit complexity or effective computation of every threshold.

## 4. No finite-propagation square minorant

The orthogonal decomposition over left cosets x<z> makes A the same Laurent multiplier f in each coset. Every L2 field supported on the open zero arc of f in one coset belongs to ker A=ker H.

Suppose y has finite support and yy*<=H. Testing the inequality against every such kernel vector shows that y is orthogonal to all zero-arc fields in every coset. Its finitely supported Fourier component on each coset is a Laurent polynomial, zero almost everywhere on an open arc. Continuity and polynomial uniqueness force each component to be zero; hence y=0.

If a bounded finite-propagation T in the constructed proper metric satisfies TT*<=H, each y=T delta_i has finite support and yy*<=TT*<=H. Thus every column vanishes, so T=0. Equivariance of T is not needed. This shows that the current increment is outside every nonzero finite-propagation square-minorant construction even though its relative process has finite certificates.

## 5. Strict enlargement and scope

The free group F2 contains infinite-order elements but has trivial center. It is covered by this construction and was not covered by the central-infinite-cyclic hypothesis. Thus the ambient-class enlargement is strict, independently of any novelty claim.

No centrality, normality, amenability or finite generation was used. Groups without infinite-order elements, arbitrary increments, arbitrary backgrounds, preassigned metric moments, and general JO remain outside this theorem. The theorem does not need to assert that the chosen background fails to commute with H. the earlier central-cyclic construction in CENTER.md's separately proved optional noncommuting examples remain valid, but are not imported as an unproved all-group extension here.
