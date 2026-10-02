# 题 1 参考文献与检索记录

以下只列实际打开并核对过的来源。页码按所链接版本；预印本版本与正式版页码不混用。

## 原始与承重来源

1. **Ádám Timár**, *Factor of iid's through stochastic domination*, arXiv:2306.15120v2, 2025-12-16. 读取 TeX 原件全文，重点核对：Introduction 对一般 FUSF 问题的开放陈述；Section 2 的 \(\mathcal G_*\)、\(\mathcal G_{**}\)、MTP 与 fiid 定义；Theorem 1、Theorem 2、Theorem 4、Corollary 5；compatible monotone limits 定义后的 FUSF 例。
   <https://arxiv.org/abs/2306.15120v2>

2. **Omer Angel, Gourab Ray, Yinon Spinka**, *Uniform even subgraphs and graphical representations of Ising as factors of i.i.d.*, Electronic Journal of Probability **29** (2024), paper 39, DOI 10.1214/24-EJP1082；对应 arXiv:2112.03228。读取并核对正式 EJP PDF（尤其 pp. 6--7 的 Section 2.1、p. 22 的 Theorem 4.1、p. 28 的 Question 6.1），也用 arXiv TeX 核对可搜索原文：graph factor、rerooting、canonical representative 脚注、vertex/edge labels；Section 2.2 MTP；Theorem 1.4/4.1 的 transient WUSF；Question 6.1。
   <https://doi.org/10.1214/24-EJP1082>
   <https://dspace.library.uvic.ca/server/api/core/bitstreams/ec346c4f-76f7-4bb3-b54e-b95505de66de/content>
   <https://arxiv.org/abs/2112.03228>

3. **Itai Benjamini, Russell Lyons, Yuval Peres, Oded Schramm**, *Uniform Spanning Forests*, Annals of Probability **29** (2001), 1--65. 读取作者 PDF；Theorem 7.8 给无限图 Transfer Current determinant 公式，并在其后明确写出 FSF 对应 \(P_{\diamond^\perp}\)、WSF 对应 star projection。
   <https://rdlyons.pages.iu.edu/pdf/usf.pdf>

4. **David Aldous, Russell Lyons**, *Processes on Unimodular Random Networks*, Electronic Journal of Probability **12** (2007), paper 54, 1454--1508. 实际打开并全文转录检索 EJP 正式 PDF 镜像；§2、printed p. 1460 显式构造 rooted-isomorphism class 到编号网络的 continuous canonical representative；printed p. 1461 的 Definition 2.1 定义 \(\mathcal G_*\)、\(\mathcal G_{**}\) 与 Mass-Transport Principle，公式编号为 (2.1)。
   <https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/463/463-1495-1-PB.pdf>
   <https://doi.org/10.1214/EJP.v12-463>

5. **Russell Lyons, Andreas Thom**, *Invariant coupling of determinantal measures on sofic groups*, Ergodic Theory and Dynamical Systems **36** (2016), 574--607. 核对其 countable \(W\) 上 DPP 框架、FUSF/WUSF 应用背景及 Bernoulli-factor 问题边界；该文的 sofic/amenable 结果本身不推出本文所需的随机图 joint-Borel 选择。
   <https://doi.org/10.1017/etds.2014.70>
   <https://arxiv.org/abs/1402.0969>

## 近三日公开候选证明与接口审查

6. **公开 pull request 85**, *Frozen prescribed-W DPP theorem*. 实际读取 `research/q77r05/g4/THEOREM.md` 和 `research/q77r05/g4/PROOF.md` §§1--6；后者依次处理有限阈值集合与分量独立、奇异/复核有限倾斜、total drift 与 Picard、完整观察 posterior、共同 usual filtration innovations、每索引一个 Uniform 与同噪声极限。其冻结定理只陈述固定 \(W\) 与可数群作用；本文所需“任意双射自然”及“随核/随机图 joint Borel”在 `RESULT.md` 第 4--5 节另行证明，不从 PR 状态推出。
   <https://github.com/cat5779/rl01/pull/85>

7. **公开 pull request 91**, *Directed-double-cover interface audit*. 实际读取 `research/lgr06/audit/REVIEW_INTERFACE.md` §§1--6；其中核对双弧 intertwiner、同边最多选一个方向、忘掉方向的 DPP 主子式，并明确把“full automorphism group”与“varying random graph joint Borel”列为尚未由 fixed-graph 接口解决的边界。本文在 `RESULT.md` 第 3、5 节重证双弧 pushforward 并补 joint-Borel 缝，不把审查的 `STATUS` 当数学证据。
   <https://github.com/cat5779/rl01/pull/91>

此外读取了 2026-10-01 至 2026-10-02 的相关公开工作材料，范围包括：

* prescribed-index \(W\)-DPP total Borel sampler 的完整候选证明；
* 两份对其有限外场、无限维 Picard、完整观察后验、共同滤过 innovations 与同噪声解码的审查；
* fixed-graph FUSF signed-action / directed-double-cover 接口；
* 对“fixed graph”不能自动升级成“varying random graph joint Borel rule”的明确边界审查；
* 后续 DPP birth-flow、共同噪声和 spanning-forest/cost 路线的状态材料。

本文没有把“审查标为通过”当作证明。`RESULT.md` 第 3--5 节重新给出了本题真正承重的 kernel joint-Borel、自然 DPP sampler 与双弧 pushforward 推导。这些候选材料不用于任何新颖性或优先权主张。

## 搜索记录与限制

实际检索词包括：

* `"Free Uniform Spanning Forest" "graph factor of i.i.d."`
* `"FUSF" "factor of iid" 2025 2026`
* `"free uniform spanning forest" "factor of iid" Timar`
* `determinantal processes factor of iid`
* `random rooted graph factor iid FUSF`

检索命中回到上述原论文、作者 PDF 或正式期刊页。一个 Oberwolfach 2013 搜索片段看似声称 FUSF 已为 equivariant FIID；打开原报告后，该句实际是条件式“若 FUSF 另为 FIID 则……”，不是证明。

本轮没有完成所有数据库的穷尽前向引用图、MathSciNet/Zentralblatt 全记录核对或领域专家确认。因此文献结论严格为：

* Timár v2 的原文截至 2025-12-16 仍把一般 FUSF 因子问题列为开放；
* 本轮搜索**未定位到**公开发表的同量词 joint-Borel 定理；
* “未定位到”不等于“没有”，新颖性保持 **NOT CERTIFIED**。
