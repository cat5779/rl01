# RL01 PR #124 transfer: bounded canonical-component DPP selector

This research packet transfers a claimed positive solution of the bounded
canonical-component selector problem into the DPP conjecture repository for
review.

## Exact source correspondence

- Source repository: `cat5779/rl01`.
- Source pull request: **cat5779/rl01#124**, titled
  `DPP R18 G17: bounded canonical components`.
- Frozen source head: `8f7f8d0460f7e6c59f2ae47d3ca631629601922b`.
- Frozen source task path: `research/dpp18/g17/TASK.md`.
- Frozen source task blob: `29cc8409931a291eaae57e76d62498c2d0b492c3`.
- Frozen source handoff prompt blob: `a179e525f1b2cd121fc5621fb6650537fe17c3b6`.

`TASK.md` and `PROMPT.md` in this directory are copied verbatim from that
frozen source head. The theorem has not been weakened by inserting a common
partition, restricting the rank-one direction, replacing the original
capacity, or allowing a constant depending on the ambient dimension.

## Claimed result

`RESULT.md` claims **PROVED** for every fixed finite component bound
(r\ge1). A nonoptimal explicit constant given there is

\[
C_{\varepsilon,r}
=\frac{10}{\varepsilon^2}(r!)^2 2^{(r-1)(r+4)}.
\]

The proof constructs refinement-compatible finite-dimensional selectors,
extends them while fixing every splitting stratum exactly, tensorizes over
canonical components, and compares incompatible canonical partitions through
their common refinement rather than a potentially large common coarsening.

## Verification status

`REVIEW.md` records an adversarial re-review of the proof. It found no
mathematical gap, but it is **not an independent external referee report** and
is not formal verification. The source PR #124 was an open task and did not
already contain this proof.

This destination PR should remain **draft** pending an independent
mathematical review. No novelty or priority claim is made.
