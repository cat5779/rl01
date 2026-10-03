# A star-calibrated quotient lift can have a wrong distant-pair law

This exact-arithmetic proof concerns the statement in [STATEMENT.md](STATEMENT.md). It shows a limitation of the specified quotient lift, not a counterexample to the Bernoulli/WUSF endpoint joining problem. The scoped review is in [REVIEW.md](REVIEW.md).

## 1. The probability law and the quantities to be bounded

Write T for the three-regular tree and let B be iid Bernoulli(1/2) on its
edges. Its open clusters are finite almost surely. For lambda>1, contract
these clusters. A closed original edge uv has resistance

    r_lambda(uv)=lambda^(deg_B(u)+deg_B(v)).

These resistances lie in [1,lambda^4]. The quotient is locally finite,
and each forward quotient half-tree is transient: Rayleigh comparison
with the uncontracted binary half-tree whose resistances all equal
lambda^4 bounds its wired resistance above by lambda^4. The finite root
cluster has a finite positive-resistance boundary cutset, so this wired
resistance is positive almost surely.

Conditional on B, take the canonical oriented WUSF of this transient
network, and lift the selected quotient edges while adjoining B. The
oriented WUSF exists by Wilson's algorithm rooted at infinity; its law
does not depend on the enumeration and is covariant under network
isomorphisms. Its orientation gives one outgoing edge at each quotient
vertex. Orient the finite internal B-tree toward the tail of that edge.
Then each original vertex has one outgoing edge. Denote the resulting
unoriented upper law by T_lambda. This is a measurable invariant
probability law, not a claimed equivariant iid sampling map. The
construction and its orientation are justified in CONSTRUCTION, Section 1,
using BLPS Definition 5.2 and Proposition 5.3. No one-endedness statement
for this random quotient is assumed.

The original-tree mass-transport identity gives expected degree two.
The construction is covariant under all automorphisms of T, so

    P(e absent from T_lambda)=1/3

for every edge. No vertex is isolated. In particular the probabilities
of its three absent pairs are equal. Let P_lambda be the probability of
one adjacent absent pair. Let D_lambda be the probability that e1,e3
are absent in a three-edge path e1,e2,e3.

For the unit WUSF, the complement transfer-current kernel has diagonal
1/3, adjacent off-diagonal absolute value 1/6, and distance-two
off-diagonal absolute value 1/12. Thus its corresponding pair vacancies
are 1/12 and 5/48. Its star has no isolated vertex. Our objective is
to separate P_lambda and D_lambda at the exact interval

    a=1137/1000,   b=229/200.

## 2. Six infinite half-tree laws and their certified enclosures

Let R_(s,k)(lambda) be the forward wired resistance given parent-open
bit s in {0,1} and forward-open count k in {0,1,2}. The parent edge is
excluded from this half-network; its status affects the root's B-degree.
Let pi=(1,2,1)/4. With independent child draws J having law pi, put

    O=R_(1,J),     C_d=lambda^(d+J)+R_(0,J).

With independent arms on every right-hand side, the six-state recursion is

    R_(s,0)=parallel(C_s,C_s'),
    R_(s,1)=parallel(O,C_(s+1)),
    R_(s,2)=parallel(O,O'),

where parallel(x,y)=xy/(x+y), including parallel(0,0)=0. The discrete
J conditioning is retained whenever the selected edge resistance uses J.
This follows from finite wired half-trees and their resistance limit;
it asserts no independence between two different conditional resistances
on the same child tree.

We use bounded subsolutions and supersolutions of this law-valued map.
Here is the infinite bridge. In the contracted half-tree every quotient
vertex has at least two forward edges: a root half-cluster of n original
vertices has n+1 boundary edges, and an interior cluster has n+2 with
one removed as its parent. For C>=lambda^4, assign arbitrary resistances
in [0,C] to the cut vertices of a quotient truncation at depth n. All
forward effective resistances are at most C. Every positive arm has
resistance in [1,2C]. In its minimizing unit flow the current through
any chosen arm is at most c=2C/(1+2C)<1 times its entering current,
because a competing arm has resistance at most 2C. Hence the largest
cut current is at most c^n and the squared cut currents sum to at most
c^n. Extending the wired minimizing flow through the added cut
resistances, Thomson and Rayleigh give

    0 <= R_n(z)-R_n(0) <= C c^n.

All bounded boundary assignments therefore have the same wired limit.
Every fixed finite quotient ball is eventually contained in an original
finite-depth truncation, since all its finitely many open clusters are
finite. This identifies the original-depth recursion limit with the
quotient wired resistance. Expanding any bounded six-state recursive law
at the boundary gives the same conclusion, so the bounded law-valued
recursion has a unique fixed law and all bounded initial laws converge
to it. This is proved in full in BRIDGE. Consequently, for its exact
map T, componentwise stochastic inequalities

    L <= T(L),    T(U) <= U

certify L<=law(R_wired)<=U. This argument uses no assumption on the mean
cluster size, no chosen root/end in the original invariant construction,
and no new one-endedness claim.

The integer grid uses M=16384, Q=1024, D=2^28 and masses summing to D.
An index i represents resistance i/M. A closed resistance lambda^j is
rounded down/up in units 1/(MQ). To pair integer arm units x,y, compute

    floor or ceil of xy/[Q(x+y)],

which is the index of the parallel resistance. Each pair mass totals
16D^2. At index i, floor the cumulative mass divided by 16D for the
upper law, and ceil it for the lower law. These CDF directions make the
output respectively stochastically larger/smaller. Thus the directed
maps satisfy Tlo(X)<=T(X)<=Tup(X).

The three final PMF files are

- grid06a1137q1000m16384upper.json: an upper law at a;
- grid06b229q200m16384lower.json: a lower law at b;
- grid06b229q200m16384upper.json: an upper law at b.

They are supported in [0,C], where C=ceil(M lambda^4)/M. The independent
ordered integer checker verify05 computes one full update and verifies
Tup(U)<=U or L<=Tlo(L) in every state by CDF comparisons. These one-step
inequalities, rather than the author's warm-start search, certify the
actual infinite resistances. The verifier uses pure integer Cartesian
products with total 16D^2=2^60 and explicit product/sum overflow bounds.

## 3. The two finite circuit formulas

For an adjacent pair, the two selected edges must both be closed in B.
Condition on their independent endpoint counts J1,J2 and exterior
resistances x=R_(0,J1), y=R_(0,J2). The third incident edge is open with
probability 1/2. For selected resistances r1,r2 and its external arm t,
the complement transfer-current determinant is

    F(r1,r2,x,y,t)=r1 r2/[(r1+x)(r2+y)+(r1+r2+x+y)t].

Therefore

    P_lambda=(1/8) E[
      F(lambda^J1,lambda^J2,x,y,C_0)
      +F(lambda^(J1+1),lambda^(J2+1),x,y,O)].

This is CONSTRUCTION, equations (4)--(5). F is decreasing and separately
convex in x,y,t, and increasing in the selected r1,r2. For example,
as a function of any one external resistance it is a positive constant
divided by a positive affine denominator; direct differentiation proves
the convexity. The selected monotonicity also follows by differentiating
finite spanning-tree weights: the event is impossible if a selected
edge is included, so increasing its conductance decreases this vacancy.

For the distant pair, set external resistances s0,s1,s2,s3 at the four
vertices of the path, and let r1,r2,r3 be its edge resistances. Put

    A=r1+s0,   B=r3+s3,   C=r2+s1+s2,
    Z=AB C+r2(s1 B+s2 A+s1 s2)+s1 s2(A+B).

Then

    G(r1,r2,r3,s0,s1,s2,s3)=r1 r3(r2+s1+s2)/Z.

One direct derivation is the finite spanning-tree partition function on
the path with a ground arm of resistance s_i at each vertex. If selected
edges 1 and 3 are absent, the endpoint arms must be present; the middle
two vertices connect to ground by the three-edge triangle with
resistances r2,s1,s2. Clearing the resistance denominators gives the
numerator r1 r3(r2+s1+s2). The full tree polynomial is Z. Equivalently
it is r1 r2 r3 det(I+S L_path), with S=diag(s0,...,s3). Its 21-term
polynomial expansion is checked exactly in far04check. Schur reduction
of the disjoint exterior half-trees and the wired transfer-current limit
give the same formula for the infinite conditional network.

If the middle edge is open, contract it and set r2=0. The continuous
formula is

    G=r1 r3/[AB+(A+B)s1 s2/(s1+s2)],

with value r1 r3/(AB) when s1=s2=0. All limiting zero-resistance cases
are covered by finite positive circuits followed by contraction.

Conditional on selected edges 1,3 being B-closed (probability 1/4), let
m be the middle-open bit and b1,b2 the open bits of the two internal
external edges. These three fair independent bits and independent
J0,J1,J2,J3 with law pi specify

    r1=lambda^(J0+m+b1),  r3=lambda^(J3+m+b2),
    r2=lambda^(b1+b2) if m=0, and r2=0 if m=1;
    s0=R_(0,J0),  s3=R_(0,J3);
    si=R_(1,Ji) if bi=1,
    si=lambda^(m+Ji)+R_(0,Ji) if bi=0, for i=1,2.

The four descendant environments are independent given these bits and
counts. In particular internal counts J1,J2 may be mixed after fixing
m,b1,b2; they do not enter a selected-edge resistance. Endpoint counts
J0,J3 must remain conditioned until the selected resistances are set.

## 4. Uniform interval bounds and compression

In a finite connected weighted graph, for an unselected edge of
conductance g, conditioning its inclusion decreases the selected-edge
DPP kernel by a positive rank-one Schur term. Its selected vacancy
determinant therefore increases. Thus Cov(vacancy,edge-included)>=0,
and differentiation of the finite tree-weight sum gives
dP(vacancy)/dg>=0. The vacancy decreases with the unselected resistance.
Its ratio of tree-weight sums is affine-over-affine in that resistance,
and differentiating gives separate convexity; for a bridge the ratio is
constant. Strictly positive circuits and their contraction limits cover
zeros. This full finite argument is in CONVEX and its scoped review.

Consequently G increases with r1,r3 and decreases and is separately
convex in the unselected r2,s0,s1,s2,s3. Fix the complete Bernoulli
environment. Its external wired resistances are nondecreasing in lambda
by Rayleigh in finite exhaustions and their limit. For every lambda in
[a,b], a pointwise lower bound therefore takes selected r1,r3 at a and
all unselected middle/exterior resistances at b, retaining the same bits
and counts. A uniform lower bound needs only the conditional upper PMFs
at b. No monotonicity of the whole function D_lambda in lambda is assumed.

For a lower bound, after replacing messages by these independent upper
laws, partition each conditional message into fixed bins. Separate
Jensen replaces its value in a bin by its conditional mean. Rounding
that mean upward in the common resistance units decreases the value
again. Conditional independence permits successive replacements; the
endpoint J counts remain retained. This gives a lower bound. For the
star upper bound at b, first replace messages and unselected closed
resistances by lower ones. Each convex function lies below its secant on
a bin [lo,hi]. Replace an atom i by endpoint weights hi-i and i-lo,
dividing by the width. This gives an upper expectation by successive
independent replacements. Selected resistances are rounded upward for
this bound, and downward for the lower star bound at a.

All bin masses, means and interpolation weights are exact integers.
Finally round each F or G down/up to denominator H=2^40 in the appropriate
bound direction. The bin widths are the ceilings of P Q divided by the
requested bin number; occupied bins alone are summed. There is no
floating-point population or limiting-depth error in these inequalities.

## 5. Three strict integer signs

The two star bounds use 128 bins and post05, whose sum is over every
ordered endpoint pair. For the lower bound at a it obtains

    N_a=907615816540512031966105095975026920895,
    E_a=10889035741470030830827987437816582766592,
    12 N_a-E_a=2354057016113552765273713883740284148 > 0.

Thus P_a>=N_a/E_a>1/12. For the upper bound at b it obtains

    N_b=10375198916571758994541912483955938544055079160243483520,
    E_b=124509819072751725907511780634980506862675892425377972224,
    E_b-12 N_b=7432073890617973008830827509244334014942502456169984 > 0.

Thus P_b<=N_b/E_b<1/12. The different denominators include the exact
secant interpolation mass factors.

For the uniform distant-pair lower bound, use 64 bins, exact selected
resistances at a, and exact unselected resistances at b. The common
resistance unit denominator is 16384000000000000. Each side has mass
(4D)^2, the three bit probabilities and the selected-closed event give
1/32, and H rounds the circuit value downward. The final certificate is

    N_d=4882334926812363121937250918399651515955288337110,
    E_d=46768052394588893382517914646921056628989841375232,
    48 N_d-5 E_d=511814514048962940398470848577989620904633305120 > 0.

Hence for every lambda in [a,b], D_lambda>=N_d/E_d>5/48.

The search sum far04 folds left-right symmetry. An independent verifier,
farverify04, rebuilds all compressed laws from the original frozen PMFs,
sums all eight bit configurations and every ordered side pair, and uses
the different denominator factorization

    B2=r1+s0+s1,  B0=r2 B2+s1(r1+s0),
    Z=B0(r3+s2+s3)+B2 s2(r3+s3).

The exact formal polynomial check shows this is the same 21-term Z. The
verifier checks the total N_d,E_d and each symmetry-folded case. The
manifest SOURCE.json records hashes of the final PMFs, inequalities and
independent verification artifacts. The search histories do not
serve as additional assumptions.

## 6. A calibrated star and its wrong distant pair

The continuity argument in CONSTRUCTION applies to the actual infinite laws.
For a fixed Bernoulli environment, when lambda' approaches lambda, the
closed-edge resistance ratios lie between the extreme powers of
lambda'/lambda with exponent in [0,4]. Rayleigh gives the same ratio
bounds for positive wired half-resistances. Therefore these resistances
are continuous. The finite circuit probabilities are bounded and
continuous, so dominated convergence makes P_lambda continuous. The
two strict star signs and the intermediate value theorem give some
lambda_* in (a,b) with P_lambda*=1/12.

Write vacancies for a vertex star. Their one-edge probabilities are
1/3, their pair probabilities are now 1/12, and their triple probability
is zero. Inclusion-exclusion gives its degree distribution

    degree 1: 1/4,  degree 2: 1/2,  degree 3: 1/4,

with equal probabilities within each degree by automorphism covariance.
These are all eight star configurations of the unit WUSF. Thus every
single vertex star has exactly the unit WUSF law. However lambda_* lies
in [a,b], where its distant-pair vacancy exceeds 5/48. Its full upper
marginal consequently differs from the unit WUSF.

This proves the frozen interval statement. It does not identify a unique
lambda_*, exclude a star root outside the interval, or refute any other
invariant or iid endpoint construction. The original optimal endpoint
problem remains open.

## 7. Reproduction boundary

The necessary computation is finite: the three one-step message CDF
checks, two ordered star sums, the formal polynomial identity, and the
independent ordered distant-pair sum. The commands and expected source
hashes are in RUN.md and SOURCE.json. The actual infinite bridges are
the preceding analytic arguments, not the output of those programs.
This proof has no complete Lean formalization and makes no novelty claim.
