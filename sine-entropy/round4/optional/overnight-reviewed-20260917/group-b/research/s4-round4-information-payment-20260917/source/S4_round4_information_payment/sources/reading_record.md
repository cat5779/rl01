# Public reading record and primary-source matching

## Mandatory public snapshot

Read the assigned S4 file and all mandatory common files at commit

    c307fe1bcf46b56e4755655c90f60a681979bf13

Base URL:

    https://raw.githubusercontent.com/cat5779/rl01/c307fe1bcf46b56e4755655c90f60a681979bf13/sine-entropy/round4/

- `S4.md`: next-round continuation requirement, delta document, Gaussian common-offset interface, three mechanisms, falsification gates, growing-family scope.
- `TARGET.md`: true Toeplitz target, full configuration atoms, actual product channel, fixed-density/rank distinctions.
- `KNOWN_RESULTS.md`: scope of reviewed baseline, including the earlier S4 obstruction and S5/S6/S8/S9 limitations. The last author's round-3 MMSE theorem is not independently reviewed in this snapshot.
- `PITFALLS.md`: false completion inequality, moving-law derivatives, finite/rate limits, wrong entropy substitutions, unavailable auxiliary claims.
- `CONTRACT.md`: 90-minute/complete-new-result early-stop rule; at most three scouts/two attempts; independent-source and ZIP requirements.
- `READING_MAP.md`: optional evidence choices and portability guidance.

The first full reads preceded the 13:09:25 UTC checkpoint. S4/CONTRACT and KNOWN/READING_MAP were reread during final scope review. All mandatory public files were successfully read. Direct container HTTP downloading was unavailable; no claim is made that a local raw-source copy or source-byte hash was obtained. The mathematical inputs actually used are restated in `proof.md` and `DELTA_FROM_LAST_ROUND.md`.

## Optional-evidence choices

No optional S8 or S9 source proof is used. Their common-file summaries were read only to avoid importing an unavailable or fixed-rank/fixed-radius theorem. No optional S5/S6 proof is used. The earlier S4 witness and the most recent author's claim are fully defined by the conversation and delta document; the old full ZIP is not required to replay this package. No private repository, workspace, or source file was requested or searched.

## Primary source 1 — GSV vector I-MMSE

D. Guo, S. Shamai (Shitz), S. Verdu, *Mutual Information and Minimum Mean-square Error in Gaussian Channels*, arXiv:cs/0412108v1.

    https://arxiv.org/pdf/cs/0412108

Verified **Theorem 2, Eq. (22), PDF page 3**, including the surrounding definitions of vector noise and the natural-log convention. The page was inspected as a rendered screenshot as well as parsed text. Hypotheses: finite second moment for X, deterministic matrix H, standard independent Gaussian vector N independent of X. Here H=I and Z_t/sqrt(t)=sqrt(t)X+N; binary finite input satisfies finite power. Conditional application is at each Y while a is held fixed. It gives an SNR derivative, not common-offset concavity.

The independent posterior martingale calculation in proof Section 1 supplies the same factor 1/2. The new signed common-offset payment is not in this invoked statement.

## Primary source 2 — CE fixed-functional entropy drift

Y. Chen and R. Eldan, *Localization Schemes: A Framework for Proving Mixing Bounds for Markov Chains*, arXiv:2203.04163v2.

    https://arxiv.org/html/2203.04163v2

Verified **Section 3.2.3, Eq. (27)** and its preceding definitions: a fixed nonzero nonnegative test function f, the tilted law f nu_t/nu_t(f), the martingale nu_t(f), and its Ito entropy drift. We take identity diffusion matrix and f=f_y at each fixed a. This is only a convention/interface cross-check. No Proposition 39 or Lemma 40 hypothesis is used to assert a common-offset curvature sign; no mixing estimate is invoked.

## Primary source 3 — coding-theory generalized area theorem

C. Measson, A. Montanari, T. Richardson and R. Urbanke, *The Generalized Area Theorem and Some of its Consequences*, arXiv:cs/0511039v1.

    https://arxiv.org/pdf/cs/0511039

Verified **Definition 1 (Channel Smoothness), Theorem 1 (General Area Theorem), Eq. (3), PDF page 3**, both parsed and in a screenshot. Hypotheses: arbitrary finite input law, coordinatewise smooth memoryless channel families, and extra observation Omega satisfying conditional independence of Omega and Y given X. Our binary transition probabilities are smooth and strictly positive in the legal interior; take coordinate offsets a_i, then a_i=a, and Omega=F_T. The extra observation law is held independent of a. Converting the paper's bits to nats preserves the identity.

The source motivates the extrinsic-information bookkeeping. Its later BMS/degradation/decoder comparisons are not used. The pair second derivative, compatible rebase, scalar logarithmic-mean bound, and combined Fisher payment are proved here rather than imported.

## Source limitations

No global literature-exhaustion or universal novelty claim is made. No external theorem is cited as granting a missing curvature sign. The archive is self-contained for the mathematical argument and exact computations even without network access; the literature references identify verified interfaces and provenance.
