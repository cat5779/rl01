# Dynamic block environments: a finite-box obstruction with a continuous endpoint kernel

This supplements [Finite rate boxes and finitary pure-birth processes](RESULT.md). Its comparison point is the static two-type environment in that manuscript's Appendix B. Here every coordinate belongs to one regular orbit and has positive birth rate.

On the regular group Gamma=Z x C2, there is a bounded covariant Borel pure-birth field with the exact product determinantal marginals K_t=(1/2+t/8)I. It satisfies the all-coupling Osgood mean criterion and therefore has a unique prescribed-marginal weak law and a causal relative strong realization. Its exact finite rate-box widths nevertheless stay uniformly positive on an event of positive probability, so the finite-box sufficient criterion in RESULT.md cannot apply. In contrast with the static environment, the SINGLE root endpoint conditional probability has a Borel version continuous at almost every initial state against the entire initial-state space.

The last conclusion provides a relative finite certificate for that one binary conditional output by [the finite-output criterion](KERNEL.md). It does not construct the joint endpoint field or the whole process by finite queries. General invariant weak existence for arbitrary measurable rates on a nonamenable regular group remains open.

The ordinary DPP weak-existence theorem is the explicit version-linked input of RESULT.md Section 1. Compatible product-Poisson completion is proved in its Appendix A. [MEAN.md](MEAN.md) gives the complete bounded all-coupling Osgood argument used here. These inputs are separated from the finite-box criterion: a mean modulus does not imply its width hypothesis.

## Part I. Exact marginals, conditional clearing, and rate-box width

For g=(j,epsilon) let s=(0,1) and let I_n be the positive integer interval from 2^n-1 to 2^(n+1)-2. Define F_g(x) to indicate that every block g+I_n has a one, and set theta_g=F_g-F_(g+s). On t in [0,1] define

    p(t)=1/2+t/8,
    q(t)=1/[8(1-p(t))]=1/(4-t), d(t)=q(t)/2,
    c_g(t,x)=q(t)+d(t)theta_g(x)(p(t)-x_(g+s)),
    a_g(t,x)=(1-x_g)c_g(t,x).

The initial law is fair product measure. Every site is active; there is no static coordinate type.
## 1. The exact single-orbit field

All coordinates belong to Gamma=Z x Z2. Blocks I_n on the positive ray have lengths 2^n; their offsets run from 2^n-1 to 2^(n+1)-2. Let F_g check that every block on g's ray has a one; theta_g=F_g-F_(gs). Both rays are disjoint and avoid the updated pair {g,gs}. Thus theta_(gs)=-theta_g and the sign is exterior to that pair. These are Borel, left-covariant functions.

For these coefficients,

    11q/16<=c_g<=21q/16<=7/16,
    c_g>=11/64=:c_*.

The paired perturbation conditional on its exterior has product-Bernoulli expectation d theta p(1-p)^2 times

    (f10-f00)+(f11-f10)-(f01-f00)-(f11-f01)=0.

Only finitely many pairs meet a cylinder. The baseline q(1-x_g) differentiates the product density with p'=1/8. Hence every finite cylinder satisfies the exact continuity equation for K_t=p(t)I. The curve is linear, uniformly gapped, and equivariant, and all rates are finite bounded Borel. Ordinary weak existence applies; RESULT.md Appendix A supplies compatible product noise.

For any coupling of the full product-Bernoulli(p) marginals, the first-N block event checks S_N=2^(N+1)-2 bits. Its tail error is at most sum_(n>N)(1-p)^(2^n)<=sum_(n>N)2^(-2^n). The cutoff detailed in RESULT.md Appendix B gives

    E|F_g(U)-F_g(V)|<=7delta(1+log(1/delta)), 0<delta<=1/4.

This calculation uses product marginals within each copy, not independence between copies. Applying it to both rays and separating root occupancy and partner gives the same 4delta(1+log(1/delta)) rate bound as in that static example. The large-delta and zero cases are identical. The all-coupling criterion of MEAN.md therefore gives invariant prescribed-marginal weak existence, law uniqueness in that class, and a causal relative strong map with these SAME rates. It gives no finite certificate by itself.

## 2. Uniform conditional clearing of initially empty blocks

This argument applies to any pure-birth weak law with intrinsic rates between c_*>0 and a finite upper bound, regardless of its initial law or prescribed marginals. For a finite block B put f_B(x)=1{all its bits are zero}. Its cylinder generator is

    L_t f_B(x)=-f_B(x) sum_(i in B)c_i(t,x)
               <=-c_*|B| f_B(x).

The natural filtration includes the full initial state. Multiplying the cylinder martingale by bounded initial-state functions and conditioning gives the corresponding conditional integral equation. Its absolutely continuous version satisfies

    S_B'(t)<=-c_*|B| S_B(t),
    S_B(0)=1{X_0|B is zero}.

Thus, almost surely in the supplied initial state,

    P(X_t|B is zero | X_0)
      <=1{X_0|B is zero} exp(-c_*|B|t).                       (1)

One may first intersect rational times; bounded conditional expectations of the cadlag decreasing f_B paths are right-continuous, extending (1) to every t. Countability of finite blocks gives a common initial full set. Equivalently the compatible clocks below c_* force a birth independently at every initially vacant coordinate, but independence is not needed for this cylinder-martingale proof.

Let F_g^N check only the first N blocks. Since F_g^N>=F_g,

    |F_g(X_t)-F_g^N(X_t)|
       <=sum_(n>N)1{block n on g's ray is empty at t}.

Conditional Tonelli, (1), and integration give

    E[integral_0^1 |F_g(X_t)-F_g^N(X_t)|dt | X_0]
      <=sum_(n>N)1/(c_*2^n)=2^(-N)/c_*.                     (2)

The inequality is uniform almost surely over supplied initial states. At positive time the unintegrated error is bounded by sum_(n>N)exp(-c_*t2^n). For two rays, |d(p-x_(gs))|<=5/48 therefore gives BOTH the intrinsic and actual same-path rate bounds

    E[integral_0^1 |c_g(t,X_t)-c_g^N(t,X_t)|dt | X_0]
      <=(40/33)2^(-N),                                      (3)

and the same for a_g versus a_g^N, where theta^N=F_g^N-F_(gs)^N. Deterministic-time left/right states agree almost surely; hence (3) also bounds the predictable proposal-acceptance differences. It is an estimate along ONE actual reference path. It is not, without an additional comparison argument, a stability estimate between solutions with different global rates.

In the static example of RESULT.md Appendix B a failed block remains failed forever. Here its expected waiting time for a first birth is at most 1/(c_*|B|). The initial sign no longer determines a fixed root hazard on the initial pair (0,1). The survival formula 1-(3/4)exp(theta(X_0)/16) therefore cannot simply be reused.

## 3. Exact finite-box extrema

On a finite bit box l<=u on J, the value F_e=0 is always attainable: force a wholly unread block to zero. The value F_e=1 is attainable exactly when no entire block is constrained to have all upper bits zero. There are only finitely many fully constrained blocks; all remaining blocks have a free or allowed-one coordinate, which can be chosen as a one. The analogous criterion holds for F_s. The two rays are disjoint, so the choices of their values are independent. The partner bit belongs to neither ray.

Enumerate these allowed F_e,F_s values and the allowed partner bits b; minimize or maximize the finite list q+d(F_e-F_s)(p-b). This is the exact intrinsic infimum/supremum and is a finite minimum/maximum of continuous time functions. Hence its joint Borelness is proved explicitly for every finite J and every nonempty bit box.

If the box contains a state x with F_e(x)=F_s(x)=1, it admits both theta signs while keeping b=x_s fixed. To get theta=-1, change a wholly unread e-ray block to zero and retain the other ray of x. To get theta=+1, do the corresponding change on the s-ray. Both completions retain all constrained bits, the partner and the root. Their intrinsic rates differ by

    2d|p-b|>=2d(1-p)=q(1-p)=1/8.                            (4)

This is a width obstruction at every finite box, even though the conditional mean error (2) tends to zero.

Under the fair initial product law, the two-ray event E={F_e(X_0)=F_s(X_0)=1} has probability at least (2/3)^2=4/9. Every nonempty block remains nonempty under pure birth, so E implies F_e(X_t)=F_s(X_t)=1 at all times. Any trapped finite-box envelope contains X_t; (4) applies to it. Therefore

    E W_e^R(t)>=1/18                                        (5)

for every R and deterministic t, for ANY choice of nested finite query sets. This statement concerns the intrinsic thresholds exactly as defined in RESULT.md Section 2, including occupied persistence outside them.

If the finite-box WIDTH and Osgood hypotheses of RESULT.md held, the theorem's radius-limit argument would give delta=0 and E W_infinity<=L inf_n tau_n=0 almost everywhere, contrary to (5) and bounded convergence. Thus this exact-box method cannot meet those hypotheses. No conclusion about every possible relative sampler follows from this method obstruction.


## Part II. Continuity of the single root endpoint kernel

## 1. Objects and the conditional estimates being used

Write Gamma=Z x Z2, e=(0,0), s=(0,1), and

    I_n={2^n-1,...,2^(n+1)-2}, n>=1.

For g=(j,epsilon), its ray block is g+I_n={(j+k,epsilon):k in I_n}. Put

    F_g(z)=product_(n>=1) 1{g+I_n has an occupied coordinate in z},
    F_g^N(z)=product_(1<=n<=N) 1{g+I_n has an occupied coordinate in z},
    p(t)=1/2+t/8, q(t)=1/(4-t), d(t)=q(t)/2,
    c_g(t,z)=q(t)+d(t)(F_g(z)-F_(g+s)(z))(p(t)-z_(g+s)),
    a_g(t,z)=(1-z_g)c_g(t,z).

All time intervals in this proof are [0,1]. The initial law mu is fair product measure on E={0,1}^Gamma. We use the prescribed product-DPP law and its causal relative strong representation furnished by the interfaces stated in Part I and proved in RESULT.md Appendix A and MEAN.md. Let Phi(x,N) be an everywhere defined Borel representative of that map, and let nu be the product law of the independent candidate PRMs N_g on [0,1] x [0,M], M=7/16. Their intensity is dt du, independent of the entire initial configuration. For mu x nu almost every (x,N), X=Phi(x,N) is pure birth, starts from x, and accepts a mark (t,u) at a vacant g exactly when u<=c_g(t,X_(t-)). The rate bounds are

    c_*:=11/64 <= c_g <= M.

Let c_g^N denote the displayed intrinsic rate with F replaced by F^N. It has the same upper bound M. From Part I Section 2, for every g and N, on one common mu-full initial set,

    E_nu integral_0^1 |c_g(t,Phi(x,N)_(t-))
                         -c_g^N(t,Phi(x,N)_(t-))|dt
         <= C 2^(-N), C=40/33.                              (1)

This is a same-path estimate, not a cross-generator stability statement. It follows from the conditional empty-block survival bound exp(-c_*2^n t), and so the constant does not depend on the supplied good initial state.

There is also a conditional proposal-count form of (1). To avoid overloading N, write the cutoff as m and the noise as calN. Define

    Z_(g,m)(x,calN)
      = integral 1{the tests u<=c_g(t,Phi(x,calN)_(t-))
                       and u<=c_g^m(t,Phi(x,calN)_(t-))
                       disagree} calN_g(dt du).

The integrand is predictable in the common filtration containing the whole initial state, the past of all candidate PRMs, and the past of X. Poisson compensation, multiplied by any bounded measurable function of X_0, gives

    E_nu Z_(g,m)(x,calN)<=C 2^(-m)                          (2)

for mu-almost every x. In particular this is not obtained by assuming independence of a random ancestor graph and a bad-proposal count. Countability of g and m permits one common initial good set for (1)--(2). This conditional use of compensation is legitimate because calN is product Poisson and independent of X_0 in the causal completion; individual point-process compensators alone would not provide it.

## 2. A logarithmic bound on initially empty blocks

For x in E, let E_g(x) be the set of n for which g+I_n is initially all zero. Let

    L_g(x)=max{2^n:n in E_g(x)},

with value 0 when the set is empty, and infinity if it is unbounded. At each fixed g, the probabilities of the empty-block events are 2^(-2^n), with a summable total. Thus E_g(x) is finite for mu-almost every x; this holds simultaneously at every g by countability.

We need more than pointwise finite neighborhoods. For T>=2,

    mu{L_g>=T}<=sum_(2^n>=T)2^(-2^n)<=2*2^(-T).

Choose C0=8/log 2 and T_j=C0 log(2+|j|). Then

    mu{L_(j,epsilon)>=T_j}<=2(2+|j|)^(-8).

The sum over j and both layers is finite. Borel--Cantelli implies that only finitely many positions violate the bound. Enlarging the constant to cover those finitely many positions proves that on a Borel mu-full set G0 there is a finite C_x such that

    L_(j,epsilon)(x)<=C_x log(2+|j|)                        (3)

for every j and epsilon. One can take a measurable finite enlargement of the supremum of these countably many ratios. No deterministic uniform bound on neighborhood sizes is claimed.

Along every pure-birth path from x, each initially nonempty block stays nonempty. Consequently the actual rate at g equals the finite dependency function

    b_(g,x)(t,z)
      =q+d[ product_(n in E_g(x))1{z on g+I_n is nonzero}
             -product_(n in E_(g+s)(x))1{z on g+s+I_n is nonzero}]
             (p-z_(g+s)),                                  (4)

where an empty product is 1. Define U_g(x) to contain g, g+s, and the coordinates of all initially empty blocks in both rays at g and g+s. Then (4) depends only on U_g(x). Since the sum of dyadic lengths up to their maximum L is less than 2L, (3) gives

    |U_(j,epsilon)(x)|<=2+4C_x log(2+|j|).

Every integer-coordinate displacement in U_g(x) is between 0 and 2C_x log(2+|j|). These are fixed neighborhoods for a fixed x, not neighborhoods selected by exposing future noise.

## 3. Nonexplosion of the fixed-initial-state ancestor graph

Fix x in G0. Explore all strict-time ancestors of the candidate proposals at the root e in [0,1], using U_g(x) at each proposal. A query for the state at g immediately before time t reads its initial bit and its candidate proposals strictly before t; each such proposal queries all sites in U_g(x) at its own strictly earlier state. Own-site queries allow chronological evaluation. Each site has finitely many proposals nu-almost surely. Ties between different proposals have nu-probability zero, simultaneously over all sites.

Along a chain with k dependency steps, its integer coordinates satisfy

    |j_(k+1)|<=|j_k|+K_x log(2+|j_k|), K_x=2C_x.

There exists A_x finite such that all such chains from the root obey

    |j_k|<=A_x(k+1)^2.

For completeness choose A large enough to dominate the initial coordinate, K_x, and satisfy 3A>=K_x log(A+2). Use

    log(2+A(k+1)^2)<=log(A+2)+2 log(k+1),
    log(k+1)<=k.

Then the next increment is at most K_x log(A+2)+2K_x k<=A(2k+3), proving the induction. Enlarging A if necessary covers any fixed starting site.

It follows that every neighborhood encountered by depth k has size at most D_x(1+log(k+2)), for a finite D_x. An ordered k-proposal chain has a time simplex of volume 1/k!. The factorial moment formula for the product PRMs, including repeated sites with distinct strictly ordered marks, therefore bounds the expected number of such chains by

    [M D_x(1+log(k+2))]^k/k!                               (5)

after enlarging D_x to cover the harmless first step. The expression tends to zero, since k!>=(k/e)^k and log k/k tends to zero. Existence of an infinite chain would imply chains of every length. Their probabilities are bounded by (5), so there is no infinite chain nu-almost surely.

The explored tree is finitely branching: its dependency neighborhoods and site proposal lists are finite. If it were infinite, the elementary infinite-tree lemma would give an infinite branch. Hence its entire root closure, and the set Q_x(calN) of sites queried by that closure, are finite nu-almost surely. The conclusion is for EACH fixed x in G0 under its conditional noise law nu. There is no assertion of one noise event working simultaneously for all uncountably many x.

When Phi(x,calN) solves the actual clock equations and is pure birth, it also solves (4) along its path. Chronological induction on this finite graph identifies its root path with the finite-graph evaluation. Thus the preceding graph describes the reference root path on a conditional noise-full event for every x in a further mu-full set.

## 4. One common initial good set

Choose a Borel mu-full subset G of G0 on which all the following hold:

* Phi(x,calN), for nu-almost every calN, is a pure-birth path from x and satisfies all countably many coordinate clock equations;
* the simultaneous conditional bounds (1) and (2) hold at all g and m.

Such a set exists by disintegrating the joint full-measure clock-equation event and the countably many compensation inequalities. The maps in question are Borel; row integrals are Borel. If a completed-measure version was used initially, take a Borel full-measure subset of its good set. The fixed-x graph nonexplosion holds for every x in G0, hence for every x in G. Every conditional statement below is made on this SAME G.

Define the Borel row probability

    h(x)=integral 1{Phi_e(x,calN)(1)=1} nu(dcalN)

on all E. On G it is the desired conditional endpoint probability.

## 5. Uniform comparison to all good nearby initial states

Fix x in G and eta>0. Because Q_x is finite nu-almost surely, choose a deterministic finite set K containing e such that

    nu{Q_x subset K}>=1-eta.                               (6)

This follows by exhausting the countable sites with deterministic finite sets. K may depend on x and eta, but not on the sampled calN.

Choose m larger than every index in E_g(x) and E_(g+s)(x), for every g in K. Increase m until

    |K| C 2^(-m)<eta.                                      (7)

Let J be the finite union of K, their partners, and the first m blocks on both rays at every g in K. The cylinder V fixes x on J. For every y in V, all initially empty/nonempty statuses of the first m blocks at these sites agree with those of x. For a pure-birth path Y from y, the initially nonempty prefix blocks stay nonempty. Since x has no initially empty block beyond m at these sites, this proves the identity

    c_g^m(t,Y_(t-))=b_(g,x)(t,Y_(t-)), g in K.             (8)

Use the SAME calN to run X=Phi(x,calN) and Y=Phi(y,calN), for any y in G intersect V. Both paths satisfy their equations on a noise-full event depending on x and y; no common null event over all y is required. On the event Q_x subset K and Z_(g,m)(y,calN)=0 for every g in K, the root paths agree. Indeed, all initial bits in the finite reference closure match. Evaluate its marks in increasing time order. At each mark, its needed earlier bits match by induction; (8) and (4) give the same reduced threshold, and the absence of a bad proposal identifies Y's actual test with that threshold. Occupied persistence is identical in both paths. This identifies all root marks and all intervals between them.

No independence is used between Q_x and the bad-proposal counts. A union bound, (2), (6), and (7) give, for EVERY y in G intersect V,

    nu{X_e as a whole path differs from Y_e}
       <=eta+sum_(g in K) E_nu Z_(g,m)(y,calN)
       <=eta+|K| C 2^(-m)<2eta.                            (9)

The bound is uniform over all such y. The initial cylinder expands when m is increased, but the fixed-x reference graph and K do not expand. This is the reason the tail bound in (7) is usable; a global cutoff graph with degree of order 2^m would not give this argument.

In particular |h(y)-h(x)|<2eta for every y in G intersect V. Thus h restricted to G is continuous. The stronger full-space-version assertion still needs an extension, given next.

## 6. A Borel probability-vector version continuous against all inputs

The fair product law has full support, so its full set G is dense in E. Choose a countable subset D of G meeting every nonempty basic cylinder. It is dense in E. Let J_l be an increasing deterministic exhaustion of Gamma by finite sets, and set

    H_l(z)=sup{h(d):d in D, d|J_l=z|J_l},
    H(z)=inf_l H_l(z).

Every displayed supremum is over a nonempty set. For a fixed l, H_l is constant on each of finitely many cylinders, hence Borel and continuous. The sequence is decreasing, so H is Borel and takes values in [0,1].

For x in G and epsilon>0, Section 5 gives a cylinder V about x on which all values h(y), y in G intersect V, are within epsilon of h(x). In particular the same is true of all D points in V. Once J_l contains the coordinates defining V, all D points in the J_l-cylinder of any z in V lie in V. Their supremum belongs to [h(x)-epsilon,h(x)+epsilon], as does its decreasing limit H(z). Therefore H is continuous at x AGAINST THE ENTIRE space E and H(x)=h(x). This holds for every x in G, not merely for sequences of good inputs.

For the binary endpoint the everywhere probability vector is

    k_0(z)=1-H(z), k_1(z)=H(z).

It is Borel, sums to one everywhere, and both components are continuous at all points of G. Both agree with the conditional probabilities mu-almost surely. This constructs the components simultaneously; independently taking upper extensions of all components would not preserve their sum.

The finite-output criterion of KERNEL.md now supplies a relative arbitrary-completion finitary sampler for this SINGLE binary endpoint probability, using one fresh uniform label and strict threshold margins. The sampler only realizes this one conditional distribution. Applying a one-output criterion independently at other sites would change joint distributions and would not supply a realization of the given generator.

## 7. Scope and the remaining interface

The direct all-active promotion of the static example of RESULT.md Appendix B loses its fixed static sign and, more strongly, its one-root endpoint conditional-kernel discontinuity obstruction. For the same rate field Part I still shows that the exact finite-box width method fails. These statements are consistent: a rate can have large arbitrary-completion box width while its time-integrated one-output probability has a full-space almost-everywhere continuous version.

This proof does not establish relative finitarity of the actual joint process, all-initial weak uniqueness, or a single-orbit counterexample to general invariant weak existence. It uses the already available causal product-Poisson representation for this prescribed law. The new comparison is uniform only over a common full set of supplied initial states; the extension addresses the one-output probability vector, not a joint path-space conditional law.

No priority or external-certification claim is made. The restriction explains why this particular static obstruction cannot be transferred just by giving all its environment coordinates positive birth rates. The general prescribed-generator invariant weak-existence problem remains open.
