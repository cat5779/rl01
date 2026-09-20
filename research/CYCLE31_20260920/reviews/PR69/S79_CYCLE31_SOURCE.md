# S79 Cycle31 来源与证据边界

审查日期：2026-09-20（Asia/Singapore）

## 收到的作者材料

来源目录：

`C:/game/gameproject/showa100/math/rl01-cycle19-harvest/research/CYCLE31_20260920/S79/`

收到三项材料：

- `S79_VISIBLE_RESULT_PARTIAL.md`：958 行、20120 字节；可见的第 1--10 节完整，但文件在最终 ledger 中断，末句停在 `The counterexample does not disprove an arbitrar`。
- `s79_second_chaos_shell.py`：404 行；本审查按原字节内容归档为 `S79_AUTHOR_SECOND_CHAOS_SHELL.py`。
- `s79_execution.txt`：作者提供的执行输出；原样归档为 `S79_SUPPLIED_EXECUTION.txt`。

因此本审查是 **COMPLETE_SCOPED_REVIEW_OF_VISIBLE_SECTIONS_1_TO_10**，不是完整手稿审查。缺失的最终 ledger 没有被猜测、补写或当成已经读取。

## 可继承边界

只继承 PR66/S76 已明确审计的有限模型边界：半密度中点的 pair-source/exterior-channel law、score 可测性、Boolean number operator 恒等式、以及此前的 compensated-curvature 框架。S79 新增的 orientation path、paid-shell 分解、混合 layer 反例、deletion intertwining、Cauchy minor 和 total-shell 路线均在本审查中重新核对。

本审查不把有限 cyclic 外推成 true Toeplitz/Hilbert 熵率结论，也不把中点公式外推到一般 (a)、一般密度或端点。

## 公开定理来源

S79 使用的 Bernoulli 和熵凹性是 Hillion--Johnson 2017 年证明的完整 Shepp--Olkin 猜想：

- E. Hillion and O. Johnson, *A proof of the Shepp--Olkin entropy concavity conjecture*, Bernoulli 23(4B), 2017, DOI 10.3150/16-BEJ860；[官方发表版 PDF](https://research-information.bris.ac.uk/ws/portalfiles/portal/113731936/euclid.bj.1495505104.pdf)。
- L. A. Shepp and I. Olkin, *Entropy of the Sum of Independent Bernoulli Random Variables and of the Multinomial Distribution*；[Stanford 技术报告页](https://statistics.stanford.edu/technical-reports/entropy-sum-independent-bernoulli-random-variables-and-multinomial-distribution)。

原始 1981 工作提出一般联合凹性猜想并处理若干特例；S79 所需的一般 affine Bernoulli 参数路径应归因于 2017 年的完整证明，而不是写成 1981 年已经证明了完整定理。

## 本地执行证据

- `S79_AUTHOR_SECOND_CHAOS_SHELL.py`：作者源码原样归档。
- `S79_SUPPLIED_EXECUTION.txt`：收到的作者日志原样归档。
- `S79_AUTHOR_EXECUTION.log`：本审查实际重跑归档源码所得输出，退出码 0。
- `s79_independent_check.py`：另写的标准库独立实现，不调用作者模块。
- `S79_INDEPENDENT_CHECK.json`：独立实现的机器可读结果。

本审查不使用 SHA、checksum 或哈希验收；源码一致性用原始内容逐字节比较，数学真实性由独立推导和独立程序承担。
