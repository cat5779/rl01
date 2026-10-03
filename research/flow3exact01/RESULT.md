# Resolution of cat5779/rl01#126: exact three-input flow consistency gap

## Status

**PROVED for the frozen subproblem in https://github.com/cat5779/rl01/pull/126.**

This note records a self-contained resolution of the bounded three-coordinate DPP transport problem that was previously only an unreviewed candidate.

For every 0 < η ≤ 1/10, with

- P = (1/3) · 11^T,
- K0 = (1/2)I + (η/21) A,
- A = [[-11,13,-2],[13,-2,-11],[-2,-11,13]],
- Ka = σ^a K0 σ^(-a), σ = (123),

the full positive birth-flow fibers Fa satisfy

    inf_{f in Fa, g in Fb} ||f-g||_1 = 48η/21    for a != b,

and

    inf_{fa in Fa} max_{a<b} ||fa-fb||_1 = 52η/21.

Therefore the exact simultaneous/pairwise ratio is

    (52η/21) / (48η/21) = 13/12.

This proves the finite three-input gluing obstruction asked for in rl01#126. It does not resolve the unrestricted dimension-free selector problem in rl01#123.

## Provenance

Frozen source:

- https://github.com/cat5779/rl01/pull/126
- frozen head: 428c693273332743e9618fce9856384a6eb9b9e5
- frozen task: research/flow3exact01/TASK.md

The earlier 13/12 value appeared in an explicitly unreviewed continuation. The derivation below is reconstructed from the displayed matrices and does not inherit the earlier verdict.

## 1. Spectrum and the common projector

Let t = η/21.

Direct multiplication gives

    A·1 = 0,
    A^2 = 441(I-P),
    tr(A) = 0.

Hence the eigenvalues of A are 0, +21, -21, so every Ka has spectrum

    {1/2 - η, 1/2, 1/2 + η}.

Because η ≤ 1/10, this lies in [2/5, 3/5], which verifies the common epsilon = 2/5 gap.

Permutation conjugation fixes P, and

    Ka P = P Ka = (1/2) P.

One terminology correction matters: the three Ka are not mutually commuting for η > 0. What is required and used here is that each Ka commutes with the same rank-one projector P.

## 2. Exact atoms and divergences

Put

    a = (-11,-2,13),
    q = 1/4 - η^2,
    h = 1/12 + η^2.

For i in {1,2,3}, and bar(i) the complementary two-set, exact determinant expansion gives

    p0(empty) = p0(123) = q/2,

    p0({i})   = 1/8 + a_i t/2 + η^2/6,
    p0(bar i) = 1/8 - a_i t/2 + η^2/6.

Differentiating the exact atoms in the P direction gives

    b0(empty) = -q,
    b0(123)   =  q,

    b0({i})   = -h - a_i t,
    b0(bar i) =  h - a_i t.

The other two inputs are cyclic relabelings:

    pa = R^a p0,
    ba = R^a b0.

These formulas are exact; no numerical LP is used.

## 3. Why the lower bounds cover the full fibers

The task allows arbitrary flows in the full positive fibers, not only a preferred coupling.

Take any nonnegative upward flow f with divergence Df = ba.

The empty and full vertices force total bottom and top edge mass to equal q. The singleton equations then imply every singleton outgoing mass is at most

    1/3 + 13t ≤ 83/210.

At the same time, every exact atom obeys the uniform lower bound

    pa(S) ≥ 79/840

throughout 0 < η ≤ 1/10.

Therefore

    5 pa(S) - f_out(S)
    ≥ 79/168 - 83/210
    = 3/40 > 0.

Thus the stated capacity constraints are automatic on the whole nonnegative divergence fiber.

The unit-mass condition is automatic too. Pairing the divergence with the vertex potential |S|, whose gradient is 1 on every upward edge, gives

    sum_e f_e = sum_S |S| ba(S) = 1.

So for this frozen family,

    Fa = { f ≥ 0 : Df = ba }.

This is the key point ensuring that the dual lower bounds below really apply to arbitrary full-fiber competitors.

## 4. Pairwise optimum: 48η/21

Set

    s = 1/12 - η^2/3,
    r = 1/12 + η^2/3.

Give all six outer edges mass s.

Order the six middle edges as

    1->12, 2->12, 2->23, 3->23, 3->13, 1->13.

Define F0 by middle-edge masses

    r + t(-8,-5,3,8,5,-3),

and let Fa = R^a F0.

Let C be the middle six-cycle circulation

    C = (1,-1,1,-1,1,-1),

with DC = 0.

For the pair (0,1), use

    G1 = F1 + 2t C.

Then the difference on the middle edges is

    F0 - G1 = t(-15,0,9,15,0,-9),

with zero outer-edge difference, so

    ||F0-G1||_1 = 48t = 48η/21.

All displayed masses stay strictly positive throughout the full interval; for example

    r - 8t ≥ 19/420 > 0.

For the lower bound, use the vertex potential with values

    phi(empty) = phi(123) = 0,

and on the singletons and complementary two-sets,

    (1/2, -1/2, -1/2).

Its gradient on every edge has absolute value at most 1. Therefore, for arbitrary f in F0 and g in F1,

    ||f-g||_1
    ≥ <phi, b0-b1>
    = 48t.

Upper and lower bounds agree:

    inf ||f-g||_1 = 48t = 48η/21.

Cyclic relabeling gives the same value for every distinct pair.

## 5. Simultaneous optimum: 52η/21

The cyclic triple

    (F0,F1,F2)

is feasible, and direct subtraction gives

    ||Fa-Fb||_1 = 52t

for every a != b.

So the simultaneous optimum is at most 52t.

For the lower bound, define a vertex potential psi0 by

    psi0(empty) = psi0(123) = 2/3,

    (psi0(1), psi0(2), psi0(3)) = (1,1,0),

    (psi0(12), psi0(23), psi0(13)) = (0,1,1),

and let psia = R^a psi0.

For every fixed edge e, let wa(e) be the edge gradient of psia. The three weights satisfy

    sum_a wa(e) = 0,

and the sum of their positive parts is at most 1.

Hence for any three real edge values v0,v1,v2,

    sum_a wa va
    ≤ max(va) - min(va)
    = (1/2) sum_{a<b} |va-vb|.

Applying this inequality edge-by-edge to arbitrary feasible f0,f1,f2 gives

    (1/2) sum_{a<b} ||fa-fb||_1
    ≥ sum_a <psia, ba>.

Direct substitution gives

    <psi0,b0> = 26t,

and cyclic symmetry gives the same for a = 1,2. Therefore

    sum_{a<b} ||fa-fb||_1 ≥ 156t,

so

    max_{a<b} ||fa-fb||_1 ≥ 52t.

Together with the explicit cyclic triple,

    inf max_{a<b} ||fa-fb||_1
    = 52t
    = 52η/21.

This lower bound applies directly to arbitrary feasible triples. No equivariance assumption is imposed on the competitors.

## 6. Why the three pairwise optima do not glue

The equality conditions in the pairwise dual certificate rigidly determine the pairwise-optimal difference for inputs 0 and 1:

    d01 = t(-15,0,9,15,0,-9)

on the middle six-cycle, with zero outer-edge difference.

The other two independently pairwise-optimal differences are the cyclic rotations

    R d01,
    R^2 d01.

But direct addition gives

    d01 + R d01 + R^2 d01 = -6t C != 0.

Actual differences of three vectors must telescope:

    (f0-f1) + (f1-f2) + (f2-f0) = 0.

So the three independently optimal pair differences cannot all come from one triple. The simultaneous optimum repairs exactly this cycle-closing defect, and the necessary repair raises the worst distance from 48t to 52t.

This is the concrete meaning of the factor 13/12.

## 7. Scope boundary

What is proved here:

- both frozen formulas in cat5779/rl01#126;
- explicit attaining flows;
- full-interval nonnegativity and capacity checks;
- an exact pairwise full-fiber dual certificate;
- an exact simultaneous three-input dual certificate;
- the structural explanation of the 13/12 incompatibility.

What is not proved here:

- no divergent lower bound in dimension;
- no disproof of a universal finite-consistency selector;
- no resolution of cat5779/rl01#123;
- no novelty claim.

Per this repository's research protocol, this is intentionally submitted as a draft proof candidate. It should receive independent mathematical review before the frozen #126 result is promoted to certified status or copied into a proof ledger.
