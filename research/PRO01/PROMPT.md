# PRO01: SA03 — A sign tool for the infinite local curvature kernel

## Materials and reading order

All paths below are inside this PR, relative to research/PRO01/:
1. inputs/TASK.md: frozen definitions and derivative conventions, not the old execution instructions.
2. inputs/SA03_S9_SIGNED_TRANSPORT.md: finite signed transport and weighted cancellation.
3. inputs/SA03_VOLUME_LIMIT.md: V1–V17, especially the explicit infinite kernel V14.
4. inputs/SA03_EFFECTIVE_REMAINDER.md: the existing explicit but very conservative truncation bounds.
5. SOL_REVIEW.md: the scoped Sol audit. The structural refinement, uniform weak-noise, fixed-R next-term files, and inputs/sources/ are available as needed. FILES.txt lists the packet.

## Fixed mathematical target

At density rho=1/2 and initially c=19/20, use the true Fejer Toeplitz model defined in the inputs: positive odd R, N=R+1, Fourier coefficients q_0=1/2 and q_j=sin(pi*j/2)/(pi*j), and symbol f_(R,u,delta)=1/2+u[c(p_R-1/2)+delta]. Here u lies in [1/N,1] and |delta|<(1-c)/2.

Let q_R be the actual posterior probability of Y_0=1 conditional on the external word, phi(q)=(q-1/2)log(q/(1-q)), and A_R(delta)=integral E[phi(q_R)] du/u. Differentiate with respect to delta at zero, keeping R and c fixed and differentiating the actual probability weights too.

The previous result proves A_R''(0) -> Gamma(c), where Gamma(c)=integral_0^1 u E_(infinity,u)[barG_(infinity,u)]du and barG is the explicit absolutely summable kernel V14. The expectation uses the true unsmoothed infinite DPP, not an independent-word surrogate. Existing constants involving powers such as (1-c)^(-18) cannot settle the sign at 19/20. The sign is unknown. This local production functional is not normalized block entropy, so its curvature is not automatically the entropy-rate Hessian.

## Construct a new tool

Seek a rigorous sign determination for Gamma(19/20). A substantive intermediate success is a new analytic one-sided estimate or rigorously controlled finite representation that improves the actual obstruction.

P1. Construct an explicit sign-preserving representation, dual certificate, or correction kernel. Do not hide Gamma in an unproved Poisson solvability condition or an unknown constant.

P2. Prove the remainder and spatial-tail bounds under the actual probability law, retaining single- and double-flip terms, u factors, and changing weights. If you use Gamma_M, define it explicitly and prove an effective bound such as |Gamma-Gamma_M| <= epsilon_M or a correctly directed one-sided inequality. Its error must not depend on the unknown target.

P3. Establish the sign, or prove a genuinely stronger structural estimate and quantify the remaining gap. Do not assume positivity, a power-law expansion, or that a weak-coupling expansion reaches 19/20.

Possible transferable mechanisms include Stein control variates and Poisson corrections, variational duality or completion of squares, and connected expansions or multiscale average bounds from statistical mechanics. These are optional starting points, not a checklist. The existing transport is signed: positive Markov dissipation cannot simply be imported. Finite examples and fitted asymptotics cannot replace a uniform theorem. If a sign certificate is formulated but not evaluated, label it conditional rather than claiming the sign.

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
