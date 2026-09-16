DISPROVED_ROUTE_LEMMA

# S6: a failed Berezin variational lower bound, its extensive Fourier obstruction, and the Shannon cost of a positive repair

## 0. Result and scope

**The sine-kernel entropy-concavity target is neither proved nor disproved here.** The complete result is a counterexample, in fact a general reverse inequality, to an unrestricted trial-action Jensen step in the specified principal-minor field-theory route. The counterexample applies to strictly positive definite L-ensembles, including the actual spatial Fourier projections of growing proportional rank at fixed high contrast. It is not a quantum-entropy argument.

Two complete results are proved below.

1. **Berezin trial-action obstruction.** If the quadratic part of the two-replica action is used as the trial action, the Jensen-corrected expression is strictly *larger* than the exact principal-minor partition function. A quantitative lower bound for the logarithmic overestimate holds for every dimension and every positive definite Hermitian L. For every even n >= 4, the Fourier projection P_(n,n/2), at c = 19/20 and a = 1/40, gives an overestimate exceeding **180 n** in log Z_2. Thus the error is extensive inside a fixed legal interior, not just at a singular endpoint.

2. **Shannon derivative obstruction for a positive product-Hölder repair.** A valid real-q lower bound can be constructed from product trial probabilities and the full spatial determinant generating polynomial. Its optimized tangent at q = 1 gives exactly the sum of the one-site entropies. For the true sine Toeplitz blocks, the omitted Shannon derivative is at least

   8 floor(n/2) c^4 [sin(pi rho)/pi]^4.

   Consequently, for all 0 < rho < 1, 0 < c < 1, and legal a,

   b(a+c rho) - h_rho(a,c) >= 4 c^4 [sin(pi rho)/pi]^4 > 0.

   This is a bound on the error of this specified product relaxation, not a replacement of measured entropy by a spectral quantity and not a sign for the target Jensen difference.

A separate **exact finite certificate** verifies all atoms, normalization, field identities, and the complete a-curvature for P_(4,2), c = 19/20, a = 1/40. At that point H_4'' is strictly negative. The certificate therefore does not suggest a target counterexample.

The results are new connecting steps in this round relative to the supplied baselines. No claim of literature-wide priority is made. The proof is self-contained apart from the supplied existence of the stationary entropy rate, used only for the displayed rate consequence.

## 1. Primary-source audit: exactly what is and is not imported

The source is M. N. Najafi, A. Ramezanpour and M. A. Rajabpour, *A field theory representation of sum of powers of principal minors and physical applications*, arXiv:2403.09874v1 (14 March 2024), abbreviated [NRR24]. See `sources/reading_notes.md` for URLs and checked page/equation locations.

The integer-replica Berezin identity, [NRR24, Eqs. (22)-(27)], and the two-replica discrete auxiliary-field identity, Eq. (31), are algebraic identities. They are independently proved below. The trial-action change of weight, Eq. (133), is also an algebraic identity. The unrestricted inequality in Eqs. (134)-(136) does not follow from it and is false for the trial considered here. Appendix I, PDF Eq. (I8), writes a covariance identity followed by a nonnegativity claim. Berezin integration is not a positive probability expectation; that terminal inequality is not a general algebraic consequence.

This does **not** establish that every self-consistent mean-field interpolation in Appendix I has negative curvature. Nor does it refute every special mean-field lower bound. Section 6 gives an independent, valid Cauchy-Schwarz proof for the density-only subfamily of the uncorrected mean-field bound. Mean-field or saddle-point values are not treated as exact partition functions. No error estimate for their Shannon derivative is supplied by this work.

## 2. Exact full-atom representation and a-dependence

Let n >= 1. On a compact subinterval of 0 < a < 1-c, take

K(a) = a I + c K_0,  where K_0 = K_0* and 0 <= K_0 <= I,  0 < c < 1.

Then 0 < K(a) < I. Define

D(a) = det(I-K(a)),
L(a) = K(a)(I-K(a))^(-1) = (I-K(a))^(-1)-I,
m_S(a) = det L(a)_S,  m_empty = 1.

All m_S and all p_a(S) = D(a)m_S(a) are positive. The configuration partition function is

Z(q,a) = sum_(S subset [n]) exp(q log p_a(S))
       = D(a)^q M_q(L(a)),
M_q(L) = sum_S (det L_S)^q.

These are the supplied atom-law baselines, not claimed as new results. They explicitly retain every spatial atom, including the empty configuration.

The determinant expansion

sum_S det L_S = det(I+L)

follows by choosing, in each diagonal position of I+L, either its identity entry or its L contribution and then collecting permutation terms. Consequently,

D det(I+L) = 1,  Z(1,a) = 1.

For a projection P of rank k,

L(a) = alpha I + (beta-alpha)P,
alpha = a/(1-a),  beta = (a+c)/(1-a-c),
D(a) = (1-a)^(n-k) (1-a-c)^k.

In particular this is not a claim that the true Toeplitz block Q_n is a projection. Projection formulas below are applied to the finite cyclic P only.

For later differentiation, with A = I-K(a),

L' = A^(-2),  L'' = 2 A^(-3),
(log D)' = -Tr A^(-1),  (log D)'' = -Tr A^(-2).

If f_S = log p_a(S) and S is nonempty, then

f_S' = -Tr A^(-1) + Tr[L_S^(-1) (L')_S],

f_S'' = -Tr A^(-2)
        + Tr[L_S^(-1) (L'')_S
             - L_S^(-1)(L')_S L_S^(-1)(L')_S].

For S empty, the submatrix trace terms are zero. These traces are derivatives of log *atom weights*. None is a formula for the configuration entropy itself.

### 2.1 Integer-replica Berezin integral, including signs and normalization

For an integer m >= 1, introduce independent Grassmann variables bar(chi)_i^(r), chi_i^(r), 1 <= i <= n, 1 <= r <= m. Use the canonical variable order

(bar(chi)_1^(1), chi_1^(1), ..., bar(chi)_n^(1), chi_n^(1),
 ..., bar(chi)_1^(m), chi_1^(m), ..., bar(chi)_n^(m), chi_n^(m)).

The Berezin integral is **defined to extract the coefficient of the top monomial in this order**. This fixes its sign. Write

eta_i^(r) = bar(chi)_i^(r) chi_i^(r),
Q_L = sum_(r=1)^m sum_(i,j=1)^n bar(chi)_i^(r) L_ij chi_j^(r),
V_m = sum_(i=1)^n product_(r=1)^m eta_i^(r).

Then

M_m(L) = integral exp(Q_L + V_m),
Z(m,a) = D(a)^m integral exp(Q_(L(a)) + V_m).                 (2.1)

**Proof.** All eta's are even and commute, and each eta squares to zero. Thus

exp(V_m) = product_i [1 + product_r eta_i^(r)].

For a chosen set T of sites where the second term is used, those sites are already saturated in every replica. The only quadratic terms that can complete the top monomial lie on T^c. The coefficient in each replica is det L_(T^c), by the permutation expansion of a determinant. The integral of this term is therefore (det L_(T^c))^m. Summing over T proves (2.1). No continuation in m is used. For m=1 the result is det(I+L), providing a direct normalization check. QED.

Since (sum_r eta_i^(r))^m/m! = product_r eta_i^(r), this is precisely the convention-fixed version of the action in [NRR24, Eqs. (23)-(27)].

### 2.2 Exact discrete auxiliary field for two replicas

Let sigma_i be independent, uniformly distributed signs in {-1,1}. Then

M_2(L) = 2^(-n) sum_sigma det(L+diag(sigma))^2.               (2.2)

Indeed,

det(L+diag(sigma)) = sum_S det L_S product_(i notin S) sigma_i.

In its square, the sign average removes every cross term with distinct S and T. This proves (2.2), including 2^(-n). For Hermitian L every determinant in this display is real. This is [NRR24, Eq. (31)], and is used as an independent exact check, not as a q-near-one representation.

### 2.3 A real-q variational representation that does not use replicas

Let nu range over all probability distributions on the 2^n full configurations. For every real q,

log Z(q,a) = max_nu { H(nu) + q sum_S nu(S) log p_a(S) },     (2.3)

where H(nu) = -sum nu log nu. The unique maximizer is

nu_(q,a)(S) = p_a(S)^q / Z(q,a).

To prove this, subtract the expression in braces from log Z. The result is

sum_S nu(S) log[nu(S)/nu_(q,a)(S)] >= 0.

The inequality follows from log x <= x-1, applied with x = nu_(q,a)(S)/nu(S) on the support of nu. Equality forces nu = nu_(q,a). Thus (2.3) is an ordinary, positive, finite classical variational principle, with the actual spatial atom probabilities retained. It is not a Gaussian-state entropy formula.

At fixed n, Z(z,a) is entire in complex z because it is a finite sum of exp(z log p_a(S)). Z(1,a)=1, so log Z is analytic in a neighborhood of 1. On a compact legal a-interval all atoms have a positive minimum for this fixed n. Consequently the finite derivatives in a and q used here commute. **No n-uniform complex neighborhood or bound on these derivatives is asserted.**

In particular,

H_n(a) = -partial_q log Z(q,a)|_(q=1).

Integer replica values are not being used to select an analytic continuation: the continuation is defined directly by the finite positive atoms.

### 2.4 Complete curvature identity from this representation

For expectation under nu_(q,a), differentiation of the finite log-sum gives

partial_a^2 log Z = q E_q[f''] + q^2 Var_q(f').              (2.4)

At q=1, normalization gives E_p f'=0 and E_p[f''+(f')^2]=0. Differentiating (2.4) in q, including the derivative of the moving escort expectation, yields

H_n''(a) = -E_p[(f')^2] - E_p[(f''+(f')^2) f]
         = -sum_S (p_a'(S))^2/p_a(S)
           -sum_S p_a''(S) log p_a(S).                    (2.5)

For example, partial_q E_q[g] = Cov_q(g,f), and

partial_q Var_q(f') = Cov_q((f'-E_q f')^2,f).

These terms are included in (2.5). Equation (2.5) is the supplied complete entropy identity recovered from the exact partition function; it is **not** a new sign theorem. The acceleration term remains uncontrolled in general.

## 3. Coupled Fourier check, with every atom retained

Use labelled sites 0,1,2,3 and

U_(j,0)=1/2,  U_(j,1)=i^j/2,  P=UU* = P_(4,2),
c=19/20,  a=1/40.

Then

P_ij = (1+i^(i-j))/4,
L = (1/39)I + (1520/39)P,
D = 1521/2560000,
det L = 1.

The latent projection law has weight 1/8 on each of the four cyclic adjacent pairs and 1/4 on each of the two opposite pairs. This follows directly from |det U_A|^2. It is a coupled rank-two, co-rank-two law; the kernel's nonzero off-diagonal graph is connected.

The complete output atom table is as follows. Each row specifies the value for **each** atom of that type. Derivatives are with respect to a, keeping P and c fixed.

| Occupied set type | Multiplicity | p | p' | p'' |
|---|---:|---:|---:|---:|
| empty | 1 | 1521/2560000 | -39/800 | 839/400 |
| singleton | 4 | 29679/2560000 | -761/1600 | 361/400 |
| cyclic adjacent pair | 4 | 290321/2560000 | 0 | -761/400 |
| opposite pair | 2 | 579121/2560000 | 0 | -761/400 |
| triple | 4 | 29679/2560000 | 761/1600 | 361/400 |
| full | 1 | 1521/2560000 | 39/800 | 839/400 |

The numerator sum, with multiplicities, is 2560000, and the first and second derivative sums are zero. No count-only entropy is being computed: adjacent and opposite pairs have different probabilities.

For all real q, the exact full-atom partition function is

Z_4(q) = 2(1521/2560000)^q + 8(29679/2560000)^q
       + 4(290321/2560000)^q + 2(579121/2560000)^q.          (3.1)

The principal minors of sizes 0 and 4 are 1; those of sizes 1 and 3 equal d=761/39. Adjacent-pair minors are h=290321/1521; opposite-pair minors are j=579121/1521. Thus the exact two-replica coupling polynomial is

M_L(t) := integral exp(Q_L+t V_2)
        = 1 + 4d^2 t + (4h^2+2j^2)t^2 + 4d^2 t^3 + t^4.  (3.2)

It satisfies D^2 M_L(1)=Z_4(2), with

Z_4(2) = 63434923041/409600000000.

The executable certificate verifies the same atoms by three independent constructions: the supplied latent channel formula with second-order derivative jets; inclusion-exclusion of principal K minors; and D det L_S. It verifies (3.2) by explicit sparse Grassmann coefficient extraction, not by calling the principal-minor formula, and also verifies the sign average (2.2).

## 4. Complete theorem: the unrestricted Berezin Jensen lower bound is reversed

### Theorem 4.1

For every n >= 1 and positive definite Hermitian L, let

G=L^(-1),  d_i=G_ii>0,
M_L(t)=integral exp(Q_L+t V_2),  t>=0,
J_L(t)=(det L)^2 exp(t sum_i d_i^2).

The Gaussian trial action is S_trial=Q_L. Its normalized Berezin functional has

< V_2 >_0 = sum_i d_i^2,
J_L(t) = M_L(0) exp(t <V_2>_0).

For every t>0,

log[J_L(t)/M_L(t)]
  >= sum_i {t d_i^2 - log(1+t d_i^2)}
  >= sum_i t^2 d_i^4 / [2(1+t d_i^2)] > 0.                 (4.1)

In particular, the trial-action assertion M_L(1)>=J_L(1), obtained by applying the unrestricted [NRR24, Eqs. (134)-(136)] to this trial, is false.

Moreover,

(d^2/dt^2)log M_L(t)|_(t=0)
 = -sum_i d_i^4
   + sum_(i != j) { |G_ij|^4 - 2 d_i d_j |G_ij|^2 }
 <= -sum_i d_i^4 < 0.                                    (4.2)

Thus the covariance expression for this Berezin trial is strictly negative, despite L>0 and a strictly positive scalar partition function for every t>=0.

### Proof

The field expansion in Section 2 gives

M_L(t)=sum_T t^|T| (det L_(T^c))^2.                        (4.3)

For completeness, the complementary-principal-minor identity is

det L_(T^c) = det L det G_T.

When T and T^c are nonempty, order the matrix into these two blocks. The determinant of L is det L_(T^c) times the determinant of its Schur complement, while G_T is the inverse of that Schur complement. This proves the identity. Empty/full cases follow from the empty determinant convention.

Therefore

M_L(t)/(det L)^2 = sum_T t^|T| (det G_T)^2.                 (4.4)

Since G is positive definite, the Gram-Schmidt volume formula gives the Hadamard bound

0 < det G_T <= product_(i in T) d_i.

Indeed, write G_T as a Gram matrix; each orthogonalized squared length is at most its original squared length d_i, and their product is the determinant. Applying this bound separately to every nonnegative term in (4.4),

M_L(t)/(det L)^2 <= product_i (1+t d_i^2).                 (4.5)

The linear coefficient of (4.4) gives <V_2>_0=sum_i d_i^2. Subtracting the logarithm of (4.5) from log J_L(t) proves the first inequality in (4.1). For x>=0,

x-log(1+x) = integral_0^x u/(1+u) du
            >= x^2/[2(1+x)].

Taking x=t d_i^2 proves the remainder of (4.1), including strict positivity.

For (4.2), differentiate (4.4) twice at zero. Its first derivative is sum_i d_i^2. Its second derivative is

sum_(i != j) (d_i d_j-|G_ij|^2)^2.

Subtracting the square of the first derivative gives (4.2). Positive definiteness implies |G_ij|^2 <= d_i d_j, so each off-diagonal summand in braces is nonpositive. The strictly negative diagonal sum remains. QED.

### 4.2 What exactly has failed

The change-of-weight equality

M_L(t)=M_L(0) <exp(t V_2)>_0

is exact. The implication

<exp(t V_2)>_0 >= exp(t <V_2>_0)

is false. There is no positive probability measure on Grassmann values to which ordinary Jensen can be applied here. Already for a single site L=[1], M_L(t)=1+t and J_L(t)=exp(t); at t=1, exp(1)>1+1+1/2>2. Theorem 4.1 is much stronger than this scalar warning because it quantifies the failure for every positive definite L and for the growing coupled Fourier family below.

The parameter t in this theorem scales the replica interaction. It is **not** the channel parameter a, the replica count q, or the interpolation weight in the target Jensen inequality. The theorem is an obstruction to an auxiliary proof step, not a positive a-curvature example.

## 5. Projection/Fourier geometry makes the obstruction extensive

For K(a)=aI+cP with P a projection,

G(a)=L(a)^(-1)
    = [(1-a)/a](I-P) + [(1-a-c)/(a+c)]P.                  (5.1)

For the specified Fourier projection P_(n,k), each spatial diagonal entry of P is k/n, because each Fourier-column entry has squared modulus 1/n. Hence all d_i are equal to

d_(n,k)(a,c) = (1-k/n)(1-a)/a
              + (k/n)(1-a-c)/(a+c).                      (5.2)

No spatial basis change has been made. In particular this uses the Fourier projection's actual constant diagonal, not spectral entropy.

Define the *normalized* trial expression

B_2(a)=D(a)^2 (det L(a))^2 exp(sum_i d_i(a)^2).

At t=1, Theorem 4.1 proves

log[B_2(a)/Z(2,a)]
 >= n {d_(n,k)^2 - log(1+d_(n,k)^2)} > 0.                 (5.3)

All a-dependent determinant normalizations have canceled in the **ratio**, rather than being discarded. If k=floor(n rho+1/2), fixed 0<rho<1, fixed 0<c<1, and fixed 0<a<1-c, then d_(n,k) tends to the strictly positive number given by replacing k/n with rho in (5.2). Thus the lower bound per site in (5.3) has a strictly positive limit. This is a growing proportional-rank obstruction for every such fixed interior choice.

For an explicit high-contrast constant, take every even n>=4, k=n/2, c=19/20 and a=1/40. Then

d=761/39,  x=d^2=579121/1521,

x-log(1+x) >= x^2/[2(1+x)]
 = 335381132641/1766312964 > 180.                          (5.4)

Equations (5.3)-(5.4) show

B_2(a) > exp(180 n) Z(2,a).

The false lower bound is therefore not repairable merely by taking a thermodynamic limit and declaring its error sublinear. This statement is at q=2; it is not being promoted to a Shannon sign. The next section addresses a precisely defined real-q repair directly.

## 6. A valid positive repair, and its exact Shannon derivative

### 6.1 The restricted density-only mean-field bound is not refuted

Let z_i>=0. Principal-minor expansion and ordinary Cauchy-Schwarz on the 2^n scalar coefficients give

|det(L+diag z)|^2
 <= [sum_S (det L_S)^2] [sum_S product_(i notin S) z_i^2]
 = M_2(L) product_i(1+z_i^2).

Consequently,

M_2(L) >= det(L+diag z)^2 / product_i(1+z_i^2)
        >= exp(-sum_i z_i^2) det(L+diag z)^2.              (6.1)

For L>0 and z_i>=0 all determinants are positive. The last expression is the density-only Gaussian mean-field functional, with no replica-mixing or pairing field. Thus this subfamily has a sound lower bound independently of Berezin Jensen. It is essential not to confuse this **uncorrected** functional with the unrestricted Jensen-corrected functional disproved in Theorem 4.1. At z=0 the latter contains exp(sum d_i^2), while the former does not.

Equation (6.1) does not prove a Shannon approximation or a-curvature inequality. No claim is made here about the validity of all pairing-field, dual-space, or self-consistent variants.

### 6.2 Real-q product-Hölder bound

Fix a strictly positive full-configuration law p, in particular the L-ensemble p_a above. Let 0<pi_i<1 and define the product law

w_pi(S)=product_(i in S) pi_i product_(i notin S)(1-pi_i).

For q>1 put epsilon=(q-1)/q. Ordinary Hölder on the full configuration space proves

log Z(q,a) >= B(q,a;pi),
B(q,a;pi) := q log [sum_S p_a(S) w_pi(S)^epsilon].          (6.2)

To see this, apply Hölder with exponents q and q/(q-1) to p_a(S) and w_pi(S)^epsilon, and use sum_S w_pi(S)=1. The right side of (6.2) is a positive classical expression, not a Berezin average.

It still has an exact spatial principal-minor determinant evaluation. Set r_i=pi_i/(1-pi_i). Then

sum_S p_a(S) w_pi(S)^epsilon
 = D(a) product_i(1-pi_i)^epsilon
   det[I+L(a) diag(r_i^epsilon)].                         (6.3)

The determinant expansion proves (6.3). All normalization and a-dependence are explicit.

At fixed n, both sides of (6.2) vanish at q=1 and are differentiable there. Direct differentiation, without replicas, gives

partial_q B(1,a;pi) = sum_S p_a(S) log w_pi(S)
 = sum_i {K_ii(a) log pi_i + [1-K_ii(a)] log(1-pi_i)}.

The right derivative of the nonnegative difference in (6.2) is

partial_q[log Z-B]|_(q=1)
 = sum_S p_a(S) log[p_a(S)/w_pi(S)]
 = D_KL(p_a || w_pi).                                    (6.4)

The best tangent over product choices pi_i is obtained at pi_i=K_ii(a). This follows by differentiating each binary cross-entropy, or by its strict convexity. It yields

H(K(a)) <= sum_i b(K_ii(a)),

and the derivative error at that optimum is exactly

sum_i b(K_ii(a)) - H(K(a)).                              (6.5)

This proves the scope of the repair: its optimized product tangent at q=1 captures one-site entropies and omits spatial dependence. There is no assertion about more general, correlated trial laws. If arbitrary full-configuration trial laws are allowed, the exact Gibbs principle (2.3) is recovered, but then its maximization still contains the original difficulty.

## 7. Complete growing-family bound on the missing Shannon derivative

### Theorem 7.1

For the true Q_n in the question, every n>=2, every 0<rho<1, every 0<c<1 and every legal a,

n b(a+c rho) - H_n(a,c)
 >= floor(n/2) J(a+c rho, c^2[sin(pi rho)/pi]^2)
 >= 8 floor(n/2) c^4[sin(pi rho)/pi]^4,                   (7.1)

where, writing r=a+c rho and delta=c^2[sin(pi rho)/pi]^2,

J(r,delta)
 = (r^2-delta) log[(r^2-delta)/r^2]
   +2[r(1-r)+delta] log{[r(1-r)+delta]/[r(1-r)]}
   +[(1-r)^2-delta] log{[(1-r)^2-delta]/(1-r)^2}.         (7.2)

The interior proof below extends to legal endpoints by continuity. Using only the supplied entropy-rate limit, (7.1) implies

b(a+c rho)-h_rho(a,c)
 >= (1/2)J(r,delta)
 >= 4 c^4[sin(pi rho)/pi]^4 > 0.                         (7.3)

### Proof

The exact two-site marginal on neighboring sites of K_n has diagonal r and off-diagonal c sin(pi rho)/pi. DPP inclusion probabilities therefore give the four atoms

P(11)=r^2-delta,
P(10)=P(01)=r(1-r)+delta,
P(00)=(1-r)^2-delta.                                    (7.4)

Their marginals are Bernoulli(r). Thus their mutual information is J(r,delta), and their joint Shannon entropy is 2b(r)-J(r,delta). These are probabilities of spatial configurations, not eigenvalue occupations.

Partition the n sites into floor(n/2) disjoint adjacent pairs and at most one remaining site. Entropy subadditivity, with no independence assumption between pairs, gives

H_n <= floor(n/2)[2b(r)-J(r,delta)]
       +(n-2 floor(n/2)) b(r),

which is the first inequality of (7.1). For completeness, subadditivity follows by the chain rule and nonnegativity of classical mutual information, the latter being the same log x <= x-1 argument used in Section 2.3.

For a quantitative estimate not requiring any external divergence theorem, fix r and let u vary from 0 to delta. Along (7.4), all four probabilities are positive in the interior, J(r,0)=0, and partial_u J(r,0)=0. Differentiating (7.2) twice gives

partial_u^2 J(r,u)
 = 1/(r^2-u) + 2/[r(1-r)+u] + 1/[(1-r)^2-u]
 >= 16.                                                (7.5)

Indeed, the four positive denominators are the four probabilities summing to 1; Cauchy-Schwarz gives (sum 1/p_j)(sum p_j)>=4^2. Integrating (7.5) twice gives J(r,delta)>=8 delta^2, proving (7.1).

The relevant two-site probabilities are positive for interior legal a because 0<K_n<I; equivalently their inclusion/exclusion expressions are principal L-ensemble atoms. The entire segment 0<=u<=delta lies in the positive simplex. Endpoints follow by continuity. Finally divide (7.1) by n and take the supplied value limit H_n/n -> h_rho. There is no differentiation after taking n to infinity. QED.

### Consequence for the repaired principal-minor route

For the optimized product tangent in (6.2), equations (6.4)-(7.1) give an explicit extensive lower bound on the omitted **q-derivative at q=1**, for every finite true Toeplitz block. Thus it is not legitimate to declare this particular relaxation asymptotically exact for measured Shannon entropy. The order of operations is finite-n differentiation first, followed by an explicit inequality and the supplied entropy-value limit. No uniform analyticity or derivative-limit interchange is assumed.

The positive difference in (7.3) does **not** determine its a-curvature. Subtracting an extensive, unknown-curvature error from a concave one-site entropy does not prove target concavity. This is the precise remaining obstruction for this repair.

## 8. Exact finite curvature certificate, not a target theorem

For the coupled example in Section 3, put

p0=1521/2560000, p1=29679/2560000,
pA=290321/2560000, pO=579121/2560000.

The Fisher term in (2.5) is exactly

sum_S (p'_S)^2/p_S = 6400/39.

The acceleration contribution is

A = -(839/200)log p0 -(361/50)log p1
    +(761/100)log pA +(761/200)log pO.

It is **positive**, not automatically favorable. The exact rational-log enclosures in `evidence/certificate.json` imply

41.12354003 <= A <= 41.12354004,

-122.97902407 <= H_4''(1/40,19/20) <= -122.97902406.        (8.1)

For the same example,

1510.00903494 <= log[B_2/Z_4(2)] <= 1510.00903495.

These are exact outward enclosures, not floating-point sign tests. They are based on the following elementary logarithm enclosure. Reduce a positive rational x to x=2^k y with 1<=y<=2, and write z=(y-1)/(y+1), so 0<=z<=1/3. For N>=1,

2 sum_(j=0)^(N-1) z^(2j+1)/(2j+1)
 <= log y
 <= 2 sum_(j=0)^(N-1) z^(2j+1)/(2j+1)
    + 2 z^(2N+1)/[(2N+1)(1-z^2)].                       (8.2)

The same enclosure at y=2 treats k log 2, with endpoints reversed when multiplying by negative k. The bound follows by expanding 2 atanh z and bounding the positive tail geometrically. The scripts use N=40 and rational arithmetic throughout, then round **outward** to the displayed terminating decimals. The interval endpoints stored before rounding are exact fractions.

The proof of Theorem 4.1 and the growing-family bounds do not depend on this computation. The computation is a reproducible finite check of normalization, geometry, derivatives and signs, not an independently certified thermodynamic result.

## 9. What still blocks the sine target

The field representation and positive Gibbs representation leave the term sum_S p_a''(S) log p_a(S) in (2.5). No new bound on that term, adequate to prove the high-contrast target, is established here. The failed unrestricted Gaussian-trial Jensen step cannot supply such a bound. Its density-only Cauchy-Schwarz repair remains a valid q=2 bound, but q=2 is not Shannon. The specified real-q product repair misses an extensive Shannon derivative, and the a-curvature of that missing dependence term is unknown.

No statement about a true Q_n as a finite projection, no arbitrary spatial unitary invariance of H, no negligible quantum measurement loss, no favorable sign at each latent-tree node, and no unproved maximum-measured-entropy principle is used. The supplied Toeplitz/Fourier approximation bridge is not reproved or offered as new progress. None of the counterexamples above is a counterexample to h_rho concavity.

The delivered status is therefore **DISPROVED_ROUTE_LEMMA**, specifically for the unrestricted Berezin trial-action Jensen lower-bound connection, with complete extensive Fourier and true-Toeplitz product-relaxation obstruction estimates. Independent reproduction and review remain necessary; self-review is not certification.
