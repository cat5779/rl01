# 已失败的方法与仍开放的修改

> 2026-09-18 更新：本页后文保留历史表述；当前权威结论以 [STATUS.md](STATUS.md) 为准。特别是冻结修正律中的旧 `O(n^(3/2))` / 符号未知状态，已被 S45 的 `O(n)` 和 S43 在 `c=.95` 的负线性上包络推进；仍未解决的是 `W_n+C_n` 与真实输出桥。

本清单不是方法穷尽证明。最新补充：

- [S19](results/S19/README.md)：指定 gamma<=2 的正部例外总量不是 o(n)；仍不排除有符号分组。
- [S3](results/S3/README.md)：逐原子 pooled 支付失败，但坏原子概率很小，不能推出真实期望支付失败。
- [S5](results/S5/README.md)：相邻层 Jeffreys 项非负仍不足以忽略计数协方差；旧 round4 剩余项未审。
- S13 的 clock 正项不等于全曲率已付清；S9 主阶抵消也不等于次阶符号已知。

## 既有方法记录

# Failed methods and distinctions to preserve
 that this round must respect

For a projection P, split on an input site i with `q=P_ii in (0,1)`. On the
remaining sites,
`P^(1)=P_-i,-i-P_-i,i P_i,-i/q`,
`P^(0)=P_-i,-i+P_-i,i P_i,-i/(1-q)`.
With `H_P(a)=H(DPP(aI+cP))`, define
`R_P=H_P''-(1-q)H_{P^(0)}''-q H_{P^(1)}''`.
The proposed universal completion inequality (C), `R_P<=0`, is FALSE.
For `P=vv*`, `v=(1,sqrt(99))/10`, splitting on the second site, at
`c=19/20,a=1/1000`, an exact certificate gives `R_P>15` while `H_P''<-552`.
Thus it is the sufficient recursion step, not full entropy concavity, that fails.

More strongly, for any fixed `0<c<1`, choose an integer `r>c/(1-c)` and the
first r Fourier columns on n=2r sites. Every site has q=1/2 and the input has
full support on the r-subsets. At every possible first coordinate,
`R_P(a,c)=[c^(r-1)/2]*(r*(1-c)-c)/a+O(1+|log a|)` as a decreases to 0,
with the same positive right-end obstruction by complementation. Dimension
is fixed BEFORE taking the endpoint limit. Coordinate ordering alone cannot
make (C) universal. Signed cancellation across a whole latent tree remains
possible; requiring each node's excess to be nonpositive is forbidden.

Further, unrestricted pair-smoothing curvature for all homogeneous input laws
is false (a five-bit non-DPP example exists). Atomwise log-concavity, count
entropy concavity, and a positive Fisher term alone do not settle complete
entropy curvature. A new obstruction to an auxiliary claim is valuable, but
must not be advertised as a counterexample to the sine target.




## Additional pitfalls from the reviewed second round

- A globally averaged localization correction can have positive curvature even
  when every normalized-posterior first derivative vanishes. Keep second
  response and output-law derivatives. See S4 in KNOWN_RESULTS.md.
- No exact common Bernoulli-Laplace clock exists on the supplied growing Fourier
  family, but its exhibited harmonic moments shrink with size. Nonzero mismatch
  is not yet an extensive entropy obstruction. See S5.
- A low-contrast counterexample does not settle a high-contrast-only estimate.
- A Berezin integral is not a positive probability measure. Unrestricted Jensen
  has been disproved. Integer replicas do not grant real-q continuation.
- Replacing the full law by a product loses extensive spatial dependence. A
  value error bound does not control the a-curvature of its error. See S6.
- S7's first two stalled runs supplied no theorem. Its later accepted spatial
  results are now included in the 2026-09-17 review ledger; do not confuse the rounds.
- This packet's exact finite checks verify their stated finite identities and
  signs; they do not prove the fixed-density entropy-rate target.

## S8's new boundaries

Entropy increase under a real leverage-balancing rotation does not imply convex
curvature gain. Pointwise positivity/convexity inside a Gaussian representation
can fail while the integral has the desired sign. Do not discard signed terms
individually. The reviewed rank-two comparison is a curvature DIFFERENCE; an
iterable path to a solved reference and a fixed-density sign remain unpaid.

## S9's finite positive result does not close the limit

Full R=3 production positivity is now an accepted regression/starting theorem.
It does not provide a vanishing approximation error as R grows. A new R=3
replay is not new research credit. Individual count layers can still have the
wrong sign despite positivity of the full finite sum. The intact repaired growing-radius Theorems A/B are now separately accepted
as method obstructions; see the current KNOWN_RESULTS and repair audit.

## Newly reviewed boundaries

Do not repackage the S6 10^(-13)-wide contrast strip or its real-q block error
as a new discovery. Advance the contrast/shift coverage or pay the remaining
main-term sign. A value-to-curvature passage is justified here by the special
full-atom polynomial expansion and nested derivative estimates; an arbitrary
small entropy value error still does not justify differentiating it.

S9's total negative layer mass is provably nonvanishing. A new approach must
retain the positive-negative compensation, not demand all layers be convex.

## Reviewed synchronization — 2026-09-17

This packet now includes the accepted scopes of the latest three-reviewer
integration. Full high-contrast sine entropy-rate concavity remains OPEN.
Read the [new review ledger](https://github.com/cat5779/rl01/blob/7f081d311ced85cbf850605646808425f6b70129/sine-entropy/round4/optional/overnight-reviewed-20260917/README.md)
and the independent audit of every imported claim.

- S4: for every finite Hermitian contraction with mean density <=.01 or >=.99,
  c in [.925,.959], and a in [(1-c)/4,3(1-c)/4], H''<=-11n/250; the associated
  sine-rate strong Jensen gain is 11t(1-t)(a1-a0)^2/500. Ordinary densities and
  the remaining channel region are open.
- S1: weighted actual-output count tails at half density, c=.95,
  a in [.02,.03]; the imported all-odds identity was not certified by this audit.
- S2: the stated growing odd-n consecutive-Fourier second affine step is not
  any contraction DPP law; the seven-site physical curvature reversal is exact.
- S7: complete Shannon Hessian localization and quantitative posterior spatial
  tails accepted. Near-field sign remains open. Missing six-site scripts and
  payloads are NOT independent certificate evidence. Earlier statements that
  S7 has no accepted theorem refer only to its first two stalled runs.
- S9: production-weighted critical-scale Gaussian limit and opposite order-R
  band/complement curvatures accepted; the subleading complete sign is unpaid.
- S11/S12: precise method-budget and mixed-response obstructions accepted;
  these are not counterexamples to the entropy-concavity target.
- S13: for each fixed 0<c<1 along even n, liminf C_n/n >=
  2D_pair(c)/(1-c^2)>0. This is only a favorable midpoint component. W_n and
  off-midpoint response remain unpaid. Round-2 asymptotics are not promoted.
- New S3/S5 archives were missing; their new chat claims are not accepted here.

Each new unit received one independent Sol review, not a second review.
Historical author and unreviewed files are preserved for provenance; the
explicit acceptance boundaries override their original completion labels.
