# S41 cycle 04 — transferred S44 obligation — Actual-law observation localization of the complete curvature jet

This is a mathematical derivation and tool-creation task, to be solved in this chat. Do not route the user to Work, Codex, another chat, or an external agent. Think for at least 90 minutes, unless you achieve major progress earlier. Do not fabricate elapsed time or wait idly. Theory is central; appropriate computation is allowed without a small-calculation restriction or mandatory handoff. Do not perform hash/checksum verification. These instructions override older workflow restrictions in the background files.

The ultimate target remains TARGET.md: for every fixed 0<rho<1 and 0<c<1, the true sine Toeplitz full-configuration Shannon entropy rate h_rho(a,c) is concave for every legal 0<=a<=1-c. A half-density, balanced-point, finite-volume, or corrected-law theorem does not complete that target. Keep the frozen model, actual atom weights, all moving-law derivatives and boundary terms. Never replace Shannon entropy by Tr b(K), or treat a finite Toeplitz compression as a projection.

Create a concrete mathematical tool, using a transferable mechanism from outside the immediate DPP literature where productive. Define the object, derive the estimates and explain exactly which obstacle it pays. A renamed remainder, an unevaluated reformulation of the target, or a research plan is insufficient. Verification is assigned separately to sidebar Sol; you are a discoverer. Imported author claims below remain conditional until independently established. Prove a useful weaker theorem or an actual-model obstruction if the ambitious candidate fails; do not silently change the model.

Deliver the complete core theorem/proof or obstruction in readable English in this chat, before optional extensions. Distinguish PROVED / DISPROVED / INCOMPLETE by precise scope. Provide an agent-labelled result manuscript and useful code/archive if available; attachment cards alone are insufficient. Do not claim novelty without checking primary sources.

Repository: cat5779/rl01
Branch: research/sa-cycle04-20260918
This cycle's sources: research/CYCLE04_20260918/
Read TARGET.md first.

Your prompt is prompts/CYCLE04/S41_TRANSFER.md. This is new research building on your cycle03 result; the S44 window again produced no answer. Do not repeat your existing worst-word proof as new progress.
Essential attachments on this branch:
research/CYCLE04_20260918/S41_PARTIAL.md
research/CYCLE03_20260918/reviews/S42.md
research/HARVEST_20260918/S17_RESULT.md
results/SA03/SA03_VOLUME_LIMIT.md
results/SA03/SA03_EFFECTIVE_REMAINDER.md
Direct seed:
https://raw.githubusercontent.com/cat5779/rl01/research/sa-cycle04-20260918/research/CYCLE04_20260918/S41_PARTIAL.md

The prior S44 window produced no assistant result: that was an execution failure, not a mathematical obstruction. The new seed is S41's cycle-03 proof. Only its first 20,000 characters were recovered. Sections 1–7 contain the claimed explicit finite-observation certificate; section 8 is cut off at the start of a proposed faster scalar theorem. Do not assume the omitted theorem or invent its proof. S41 is under separate Sol review.

Work initially at rho=1/2, with 0<c<1 and x=cu. On C_R={-R,...,-1,1,...,R}, use the actual unsmoothed sine marginal K_x(h)=hI+x(Q-I/2), B_z=K_x,C_R(h)-diag(1-z), G=B_z^-1, b_R=xQ_C_R,0, q_R=h-b_R*G b_R and the exact marginal word weight w_R,z(h). Define
phi(q)=(q-1/2)log(q/(1-q)),
F_x,R(h)=sum_z w_R,z(h) phi(q_R(h)),
Gamma_R^obs(c)=integral_0^1 u F_cu,R''(1/2) du.
The frozen Gamma(c) uses the actual infinite exterior posterior. Read the full seed for its exact conventions.

S41 claims a deterministic vanishing observation error, but obtains enormous powers of 2/(1-c) and a rate only of the form exp[-kappa^(3/2)(log R)^(1/4)/16], kappa=min(1/2,-log c). This is a formal finite certificate with no useful positive lower bound yet. The already independently checked coordinate-energy tail is not an observation-domain estimate: full-posterior q and v_j are not measurable from the observed finite word.

Create an actual-law averaged localization tool for the COMPLETE curvature jet, strong enough to replace this worst-word loss. A concrete success is an explicit estimate
|Gamma(c)-Gamma_R^obs(c)| <= E_c(R), E_c(R)->0,
with a substantially useful rate and transparent constants, or a one-sided finite-observation variational certificate whose error has that property. A power of (log R)/R would be valuable if true; it is a design target, not an assumption. Pay the derivative terms w'' phi + 2 w' phi' q' + w(phi''(q')^2+phi' q''). A scalar estimate for q_R-q_infty alone is insufficient unless you prove how it controls these terms.

Promising transferable mechanisms include score-projected martingale/Galerkin approximation, differentiated conditional expectation, posterior covariance energy, or a parameterized variational witness with a controlled derivative remainder. Derive any score orthogonality, random-window averaging and boundary terms in the actual law. In particular, L2 closeness of q does not automatically give closeness of q' or q'', and conditioning on more observations changes both the posterior and its law.

Use exact sine principal marginals so no Fejer replacement is needed. Keep response-coordinate loss distinct from observation loss. Start with fixed c bounded away from 1; show the c dependence and explain what prevents extension to c near 1 or to other rho and a. You need not re-audit every constant in S41. You may take its definitions and scoped identities as seeds and develop a new independent mechanism.

Main deliverable: one effective observation/jet theorem or a rigorous obstruction that specifies which weaker observable remains local. State whether any finite radius actually certifies Gamma(19/20)>0; do not promise positivity from a rate alone. Use filenames S41_CYCLE04_RESULT.md, S41_CYCLE04_checks.py and S41_CYCLE04_result.zip as applicable.
