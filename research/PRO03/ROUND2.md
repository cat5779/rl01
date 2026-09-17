# PRO03 — Round 2: test central non-vanishing rather than assuming strong cancellation

Think for at least 2 hours, unless you achieve major progress earlier. Do not fabricate elapsed thinking time. The small-calculation restrictions and mandatory heavy-computation handoff remain withdrawn. Use appropriate mathematics and computation. No SHA256 or checksum gate.

Repository: cat5779/rl01
PR: https://github.com/cat5779/rl01/pull/4
Branch: research/pro03-sa04-cancellation
Original assignment and inputs: research/PRO03/PROMPT.md and research/PRO03/inputs/
This follow-up: research/PRO03/ROUND2.md

Continue from your deletion/completion identity K_l* K_l=I+epsilon_l G_l, exact skew/Green–Kubo response ledger, and claimed expanding-band lower bound for deletion cost. These are new author submissions, not yet independently certified. Preserve the full first-round report and proofs; check load-bearing steps you use, and mark conditional dependencies if they cannot be established.

New, explicitly EXPLORATORY evidence is available from the local Sol task, COMPUTE01/C02:
https://github.com/cat5779/rl01/pull/5
Branch: research/compute01-certified-diagnostics
Files:
research/COMPUTE01/SA04_CENTRAL_SCALE.md
research/COMPUTE01/sa04_central_scale.py
research/COMPUTE01/sa04_central_scale_result.json
research/COMPUTE01/sa04_central_scale_large_result.json
Direct note:
https://raw.githubusercontent.com/cat5779/rl01/research/compute01-certified-diagnostics/research/COMPUTE01/SA04_CENTRAL_SCALE.md

The code uses the prescribed original clock, a birth–death reduction for fixed latent sets, and the actual DPP overlap mixture. On n=6,...,20 it reports d_k increasing from about 0.156 to 0.609, while E_k remains much smaller than A_k. At n=20, A_k approximately 0.639656, E_k approximately 0.031132, and W_n approximately -150.682781. The two complete W formulas agree within about 5.7e-14. These are binary64 diagnostics, NOT interval certificates or asymptotic theorems. Read only C02/SA04 materials; do not import SA05 conclusions.

Change the research priority: do not keep O(n) cancellation as a presumed truth. Determine whether the corrected law instead has a non-vanishing central entropy difference and a negative order-n^(3/2) response, or rigorously explain why the finite data eventually cross over.

Primary targets:
1. Prove a positive lower bound for d_l=A_l-E_l on a region carrying a quantitatively controlled fraction of the actual w_l mass, or derive its central scaling profile. A result only at l=k is insufficient for W. The relevant mass may live at distances of order sqrt(n), and sign-changing contributions outside the proved region must be paid.
2. Use your exact response ledger to control reverse-heat cost against deletion, or control the combined cubic skew and entropy-production curvature directly. Identify which term creates or prevents order-one d_l. Do not assume the skew has a favorable sign.
3. Establish the sign and order of the FULL actual weighted W_n if possible. To claim -Theta(n^(3/2)), prove a negative upper bound of that order with all complementary layers controlled, together with the known absolute upper bound; a positive central deletion cost alone is not enough.

Seek a reusable tool, potentially from entropy comparison for channels, reversible-chain response, spectral mode separation, or a genuine continuum layer limit. Prove any transfer hypotheses. Your chi-square ordering cannot be promoted to KL without an additional theorem.

Remain strictly CORRECTED_LAW_ONLY. Even a negative order-n^(3/2) W does not settle W+C: only a positive lower bound for C_n/n is presently supplied, not an upper bound. A full comparison needs additional control of C_n.

Deliver a self-contained English ROUND2_RESULT.md, with precise claims, complete proofs, the actual weighted-tail accounting, and honest PROVED/DISPROVED/INCOMPLETE labels. If strong cancellation turns out to hold, prove it and explain the finite-size diagnostics. Supply the full first-round and new proof artifacts in an accessible form rather than only attachment cards. New results remain pending fresh independent review.
