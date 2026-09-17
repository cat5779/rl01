# Local toolbox exclusion table

Frozen version: `frozen_theorem_v1.md`.

- Separate dimension-free bounds on `A_l` and `E_l`: **ALREADY_APPLIED** in
  the reviewed SA04 report; they give only `|d_l|<600`.
- Same-clock deletion intertwining plus Bayes reverse bridge:
  **ALREADY_APPLIED**; repeating the KL decomposition is not progress.
- Positive forward heat correction: **KNOWN_BARRIER**; the report's `n=6`
  counterexample rules it out in general.
- Worst-case central-window supremum plus Hoeffding tail:
  **KNOWN_BARRIER** unless an expanding `sqrt(n log n)` window is paid.
- Small-`n` curvature fitting: **EXHAUSTED AS PROOF**; C02 uses it only to
  select the non-vanishing-central-difference target.

External categories still allowed include binary hypothesis testing,
association-scheme harmonic analysis, local-limit/saddle-point analysis,
statistical-mechanical surface entropy, and Stein or Green--Kubo response.

