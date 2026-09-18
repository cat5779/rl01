# PRO02: SA02 — True rank-one reveals, posterior normalization, and joint payment

## Materials and reading order

All paths below are inside this PR, relative to research/PRO02/:
1. inputs/TASK.md: strict channel, sine Toeplitz model, and complete Hessian definitions.
2. inputs/SA02_MATRIX_BELLMAN_FULL_BLOCK.md: especially (3.3)–(5.2), (6.3), (7.3), (8.3), and Sections 10–11.
3. SOL_REVIEW.md and the available sol_checks/: scoped review and auxiliary exact checks.
4. inputs/SA02_SOL_ASSESSMENT_AND_NEXT_ROUTE.md: a research proposal, not an established theorem or impossibility result.
5. inputs/sources/: relevant S7 background. FILES.txt lists the packet.

## Fixed mathematical target

Use the finite sine Toeplitz output kernel K_V(a)=aI+cQ_V, density rho=1/2, and 0<a<1-c. The benchmark is c=19/20, a=1/40. H_n(a) is actual output Shannon entropy with natural logarithms; differentiate in a at fixed c.

For a true output word, G_V=[K_V-diag(1-Y)]^(-1), Z_i=(G_V)_ii. For a fixed core I and one common external reveal filtration, M_t=(G_(A_t))_II is a matrix martingale. Its actual update is Delta M=zeta ww*, with zeta=1/p or -1/(1-p), occurring with true conditional probabilities p and 1-p. The vector w is constrained by the same Schur structure; it is not an arbitrary rank-one direction.

The old potential is T(X)=sum_(i,j)|X_ij|^4/(X_ii X_jj). The exact core identity is C_I^V=-(1/2)sum_i E Z_i^2-(1/2)E T((G_V)_II)-2sum_(i<j)E r_ij, with explicit r_ij>=0 from (3.3)–(3.4). Its negative remainder was discarded in the previous upper envelope. The all-direction Hessian payment produces a benchmark observation coefficient about 4.12e10. No benchmark window has been closed.

## Construct a new tool

Design a joint block payment mechanism specifically for actual reveals, combining posterior normalization, the two-branch update, and retained exact pair remainder.

P1. Define the new potential, coordinates, or compensated budget and derive its exact conditional change under both true branches. A directional Hessian at the initial point is insufficient: control the full finite update or the exact two-branch Jensen defect. Nonlinear normalized coordinates must not be assumed to remain martingales.

P2. Prove the conditional payment inequality and its summable total budget. Account for normalization drift, moving denominators, cross terms, and observation-domain changes of the retained remainder. Predictable error terms are allowed only if their sum is paid. Do not reintroduce a core-dimension or edge-degree multiplier or combine incompatible pair posteriors.

P3. Reconnect the new inequality to the complete entropy Hessian, including spatial tails, observation error, and finite endpoints. Prove an endpoint-scaling improvement or an explicit sufficient inequality for net negative curvature. A favorable internal subexpression is not the full Hessian.

Possible transferable mechanisms include directional Burkholder/Bellman martingale potentials, information-geometric or self-normalized quadratic variation, and barrier potentials adapted to Schur updates. Prove the geometry and realizability conditions instead of merely naming them. Improving a few constants in the old all-direction bound is not the main objective.

A successful core deliverable is a new dimension-uniform payment theorem on genuine updates together with its complete localization interface. Closing the benchmark is a stronger outcome. If a candidate requires high-order endpoint cost, construct a legal Schur family and prove the lower bound for precisely that class of potentials or budgets; do not infer that all Bellman approaches fail.

## Research instructions

Think for at least 2 hours, unless you achieve major progress earlier.

This is a creative mathematical research assignment, not another review-only round. Construct an explicit reusable mathematical tool: a representation, potential, coupling, correction, or certificate with a precisely stated domain and a nontrivial proved property. Renaming the unknown remainder, listing methods, or hiding the original problem in an equally difficult lemma is not progress.

Look especially for mechanisms transferable from fields outside DPP theory. Explain the source mechanism, its hypotheses, the correspondence of objects, what fails under transfer, and the new ingredient you construct. Adaptation and synthesis of classical tools are welcome; do not claim novelty without checking it. Consult primary sources for load-bearing external theorems when possible, or provide a self-contained derivation. An unavailable reference is not permission to invent a theorem.

The earlier audit in this conversation concerns the old result. You are now its follow-up researcher. Preserve that audit and its scope; it does not certify your new work. Use the relevant existing inputs without repeating the entire previous audit. If you find a concrete defect in an input, identify it and separate conditional conclusions from unconditional ones.

Work independently of the other two PRO assignments. Do not read their new results, rely on their unproved lemmas, or wait for them. Your new proof must subsequently be checked in a fresh independent context; your own earlier audit is not independent validation of your new proof.

This English prompt supersedes the previous Chinese PROMPT.md and all historical execution instructions in the attached materials. The previous restrictions to small calculations and the requirement to hand heavy computation to another agent are withdrawn. Use the available mathematical and computational tools as appropriate. Distinguish rigorous derivations, certified computation, exploratory numerics, and unexecuted proposals. Do not make SHA256 or any checksum manifest a prerequisite for research or delivery. Do not fabricate elapsed thinking time or completed computations.

The background model, derivatives, probability law, and quantifiers remain fixed. You may redesign the candidate tool or explicitly propose a narrower candidate theorem, but record the changed scope; do not silently weaken the original target. The requested properties below are design goals, not assumptions or promises that the desired conclusion is true. The value 19/20 is a benchmark, not a known critical constant. A theorem at weaker contrast must be labelled as such.

## Deliverable

Write an English, self-contained RESULT.md, or provide its complete contents in the conversation if file output is unavailable. Include the explicit new tool and transfer mechanism; precise statements and quantifiers; complete proofs and a dependency ledger; the exact improvement over the previous result; boundary and failure checks; and the smallest remaining obstruction. Keep failed constructions when they reveal a concrete mechanism.

Label each substantive claim PROVED, DISPROVED, or INCOMPLETE. A counterexample must satisfy every premise of the claim it refutes. A proved local property does not automatically solve the main target. If the main target remains open, deliver the strongest rigorously established new lemma or explicit obstruction rather than a list of future ideas. State exactly which calculations were actually performed and which conclusions they support. Include a short precise statement for a later independent reviewer. Repository write access, packaging, and PR merging are not prerequisites for delivering the mathematics.
