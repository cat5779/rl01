# Reviewed results and their scope

The full high-contrast target is OPEN. These are supplied baseline inputs.

## Earlier established inputs you may use, with their scope kept explicit

These are supplied prior results, not tasks to rediscover. If you need a stronger
version, it becomes your own proof obligation.

1. For every finite Hermitian positive contraction K and `0<=c<=37/40`,
   `H(DPP(aI+cK))''<=-n/50` in the legal interior; integrated concavity passes
   to stationary rates. This does not give the high-contrast range.
2. For every rank-one or co-rank-one projection P, `n>=2`, `1/2<=c<1`,
   `H(DPP(aI+cP))''<=-4n(n-1)/(n+2)`, with endpoint strong concavity by
   continuity. Arbitrary weights are allowed. This does not cover rank~rho*n.
3. Any FIXED two-bit input law in the stated channel has `H''<=-8`;
   products of independent blocks of size at most two have `H_n''<=-4n`.
   Arbitrary binary inputs in higher dimension do NOT enjoy general channel
   concavity. Negative dependence cannot be silently dropped.
4. For any fixed homogeneous input law, fixed dimension and fixed c,
   entropy is concave in sufficiently small endpoint neighborhoods. Their
   size may collapse with dimension. No fixed-interior thermodynamic conclusion
   follows from this fact or from termwise endpoint expansions.
5. For the TRUE Q_n above and every legal (a,c), a value tail is available:
   `0<=H_n(a,c)/n-h_rho(a,c) <= (c/n) Tr b(Q_n) =: e_n(c)`.
   Here `b(Q_n)` is matrix functional calculus and this is an ERROR BOUND,
   not an identity for configuration entropy. For the interval symbol,
   `Tr b(Q_n)=O((log n)^2)`. Thus `e_n->0`. This controls values, not Hessians.
6. Let P_{n,k} be the projection onto Fourier columns
   `U_{j,l}=n^(-1/2) exp(2*pi*i*j*l/n)`, `0<=j<n`, `0<=l<k`, with
   `k=floor(n*rho+1/2)`. A diagonal phase gauge, which DOES preserve atoms,
   compares this with Q_n in trace norm at most
   `d_n=1/2+(2 Harmonic(2n)-Harmonic(n)+3/2)/pi=O(log n)`.
   Consequently, writing `G_n(a)=H(DPP(aI+cP_{n,k}))`,
   `|H_n(a,c)-G_n(a)|<=n b(min(c*d_n/n,1/2))=O((log n)^2)`.
   Finite cyclic Jensen errors therefore transfer with sublinear value loss.
   Re-proving this bridge alone is not progress on the remaining sign.
7. `|H_n(a,c)-H_n(a',c)|/n<=b(min(|a-a'|,1/2))` is an available endpoint
   continuity modulus; the analogous rate bound follows. You may prove
   interior Jensen statements first and extend continuously.


## Reviewed S4-S6 results


These are usable prior inputs, not new tasks. None solves the sine target.

S4: Let P^[m] be the direct sum of m copies of the four-site projection P_(4,2).
At c=19/20, a=1/40, n=4m, k=2m, Gaussian localization Z_t=tX+B_t gives
H_(P^[m])'' - E H_(posterior at T)'' > 2mT for every
0<T<=1/16837989787238400000000. The full stochastic-path and actual output-law
averages are included, while the proposed integrated normalized-posterior
a-tangent energy is zero. Occupied sparse pinning of ell=m input sites also
has positive extensive curvature of the entropic-independence slack
I(X;Y)-(k/ell)I(J_ell;Y): it equals m^2 delta/(2m-1)>3n/8 with
delta in (3.1355,3.1356), while the proposed tangent payments vanish.
Here J_ell is a uniformly chosen ell-subset of the occupied input X.
The actual full entropy Hessian is approximately -122.979024*m, still negative.
Thus tangent-only localization closures fail, even after compatible averaging;
this does not rule out corrections retaining acceleration and output Fisher
information. This block-product family is NOT contiguous P_(4m,2m).

S5: For any fixed law on k-subsets, M=|Y| has probabilities pi_l given by
Bin(k,a+c)+Bin(n-k,a), and with u_l uniform on l-subsets,
F_l=KL(p_a(.|M=l)||u_l), Phi=H(M)+sum_l pi_l log binom(n,l),
H=Phi-sum_l pi_l F_l. For the actual path, its discrete transport decomposition
retains every term:
H''=Phi''-sum_l [pi_l B_l+pi_l acc_l+2 pi_l' F_l'+pi_l'' F_l],
where F_l''=B_l+acc_l; B_l is the entropy Hessian in the chosen transport
metric and acc_l is the actual covariant acceleration contribution. This
identity is not a curvature bound. Phi is concave. For a single harmonic mode
r=1+lambda f, Lf=-gamma f, one has
acc=B+((log lambda)''/gamma) J, J=<log r,A_r log r>, with A_r the positive
logarithmic-mean Onsager operator. Rank/co-rank-one projections have a positive
extra term, but these ranks do not approach fixed density. A true P_(6,2)
example at c=1/2,a=49/100 disproves the universal claim that the aggregate
R_tr=sum_l[pi_l acc_l+2pi_l'F_l'+pi_l''F_l] is nonnegative, although
H''<-37 and each nonconstant slice has positive acceleration. This witness is
LOW contrast and does not decide a high-contrast-only claim.
For every positive odd m, the true contiguous P_(8m,4m) has nonzero degree-2
and degree-4 middle-slice harmonic components whose actual channel multipliers
cannot share one scalar clock for a fixed Bernoulli-Laplace generator on any
open a-interval, for any fixed 0<c<1, even allowing a reversing clock. The
certified input harmonic moments scale as 1/(8m^2) and 3/(64m^4). The theorem
does NOT bound the entropy cost of the mismatch or exclude paid approximations.

S6: The unrestricted Berezin/Jensen trial-action lower bound asserted in
arXiv:2403.09874v1, Eqs. (134)-(136), is false; a normalized Berezin functional
is not a positive probability measure. For positive definite L, G=L^-1,
d_i=G_ii and t>0, the relevant two-replica polynomial satisfies
M_L(t)/(det L)^2=sum_T t^|T| det(G_T)^2
<=prod_i(1+t d_i^2)<exp(t sum_i d_i^2), the free-Gaussian trial value.
The gap is extensive on even-n half-density cyclic Fourier projections at
c=19/20,a=1/40. This refutes the unrestricted trial claim, not every
self-consistent mean-field ansatz. A valid positive product-Holder replacement
has optimized q=1 tangent equal to sum_i b(K_ii), rather than full H(K).
For true Q_n, the omitted dependence is extensive:
n b(a+c rho)-H_n(a,c)>=8 floor(n/2)c^4[sin(pi rho)/pi]^4,
hence b(a+c rho)-h_rho(a,c)>=4c^4[sin(pi rho)/pi]^4.
This is a VALUE gap; its a-curvature sign is still unknown. Integer-replica
identities and the product-tangent calculation alone are not new progress.

## Reviewed S8 second-round addition

The [new rank-two proof](optional/S8/RESULT.md) and
[independent audit](optional/S8/INDEPENDENT_AUDIT.md) establish the following
SCOPED comparison. For a real rank-two projection frame, an equal-leverage pair
and exactly two opposite outside minor differences `+eta,-eta` admit a complex
quadrature deformation through genuine projection DPPs. If `beta` is the
operator norm of the frame contribution outside the four distinguished sites,
then `D_t''(a)>=2c^3(4c-beta)eta^2 t(1-t)>=0` for `c>=beta/4`.
Here `D_t=H_t-(1-t)H_0-tH_1`, and the endpoints are coordinate permutations.
The connected arbitrary-ambient-dimension family has FIXED rank two. A genuine
five-site consecutive-Fourier specialization is proved. This is neither an
absolute sign for H'' nor a fixed-positive-density theorem.

The new mechanism is a positive two-complex-dimensional Gaussian inverse-
determinant representation after exact four-cycle cancellation, with a common
frame-energy budget. This positive representation is different from the
invalid signed Berezin/Jensen step in S6.

Two exact [method obstructions](optional/S8/OBSTRUCTIONS.md) also pass review:
a real leverage-balancing rotation can increase H yet give negative H'' gain;
and a connected 34-site example disproves pointwise convexity of the Gaussian
density even after all outside output words are summed, although the integrated
Fisher curvature and actual entropy-curvature gain are positive. The latter
keeps integrated signed cancellation alive. Neither is a target counterexample.
