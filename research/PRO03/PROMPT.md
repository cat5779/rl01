# PRO03: SA04 — Deletion versus reverse-heat costs and weighted cancellation

## Materials and reading order

All paths below are inside this PR, relative to research/PRO03/:
1. inputs/TASK.md: full corrected-law definition, actual layer weights, and the C_n input.
2. inputs/SA04_REPORT.md: Section 0 definitions, Section 4 exact KL accounting, and Section 7 weighted response and tails.
3. SOL_REVIEW.md: the scoped SA04 audit.
4. inputs/STATUS_AND_REVIEW.md, inputs/COMPUTATION_HANDOFF.md, and inputs/sources/: historical boundaries and relevant S13 background. The old computation handoff is not a completed calculation. FILES.txt lists the packet.

## Fixed mathematical target

Work only with the specified corrected law. Let n=2k>=4, c=19/20, a*=1/40, p=39/40, q=1/40. P is the projection onto the first k Fourier columns on the n-cycle, and the input k-subset A has probability det P_A. The distributions q_l^max and u_l are the specified deletion/completion law and uniform law on layer l.

Use the original exchange generator G_l=l(n-l)L_l, P_l^s=exp(sG_l), and exactly the coefficient-defined multiplier theta in the inputs: s_l=-log(theta_(min(l,n-l)))/(2(n-1)). Set F_l(s)=D(q_l^max P_l^s || u_l) and h(l)=F_l(s_l), with uniform endpoint layers 0,1,n-1,n. Do not choose a different clock.

The actual count weights satisfy sum_l pi_l(a,c)t^l=[1-a-c+(a+c)t]^k[1-a+at]^k. Freeze h at a* and set W_n=sum_l pi_l''(a*,c)h(l); this is only the moving-weight response.

For 2<=l<=k, r=l-1, the exact costs are A_l=F_l(s_l)-F_r(s_l)>=0 and E_l=F_r(s_r)-F_r(s_l)>=0. Their difference d_l=h(l)-h(l-1)=A_l-E_l has no assumed sign. With B_m=sum_(i!=j)P(N_ij=m), B_-1=0, and w_l=B_(l-1)-B_(l-2)>=0, the existing exact identity is W_n=-2sum_(l=1)^k w_l d_l=2sum_(l=2)^k w_l(E_l-A_l). Here sum w_l=B_(k-1)=O(n^(3/2)). Previous work proves |d_l|<600 and |W_n|=O(n^(3/2)), not its actual growth rate. The n=4 example already refutes W_n>=0 for every n.

## Construct a new tool

Build a coupling, correction potential, or discrete-response representation treating deletion and clock variation jointly, so their cancellation can be proved rather than lost by separate absolute-value estimates.

P1. Give an explicit common local representation and exact difference accounting, retaining the Bayes reverse bridge, true conditional probabilities, and correctly normalized clock. Renaming d_l or W_n is not a construction.

P2. Prove useful regularity on an expanding central window, or directly prove cancellation under the actual w_l weights. One possible target is |W_n|<=Kn, but do not assume it is true. A pointwise bound K/sqrt(n) is a sufficient but potentially unnecessarily strong condition. If a more natural bound K(|l-k|+1)/n is proved, use actual weighted moments rather than a worst-window supremum.

P3. Pay every layer and all tails, and state whether the resulting information suffices to compare W_n+C_n. For an asymptotic leading term, provide quantifiers and a rigorous error. A fixed-width central limit or small-n fit is insufficient.

Possible transferable mechanisms include reversible-chain linear response and Green–Kubo corrections, Schrodinger bridges and deletion-chain commutators, or discrete Stein summation and orthogonal-polynomial/saddle-point methods that treat weights and costs together. Importing a positive forward heat correction is invalid without proof: n=6 already disproves the universal forward-clock rule.

The existing tail contribution is bounded by 2 max(A_*,E_*) n(n-1) exp[-2R^2/(n-2)]. A pointwise central argument therefore needs an expanding window of order sqrt(n log n), or a new weighted tail argument. Fixed R/sqrt(n) does not automatically pay the O(n) tail budget.

Only a positive lower limit for C_n/n is established, not C_n=Theta(n). Even W_n=O(n) does not settle W_n+C_n without adequate constants or signs. Do not transfer corrected-law conclusions to the true output or Toeplitz entropy rate, and do not import unreviewed SA05 claims. Seek a rigorous improvement over the old bound or a precise obstruction theorem; repeating the old KL decomposition is not new progress.

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
