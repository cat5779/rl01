# G6 原题与先行工作核查

DATE: 2026-10-01 (Asia/Singapore)
FULL_DPP_PRIOR_ART: UNCONFIRMED
FULL_FUSF_PRIOR_ART: UNCONFIRMED
NOVELTY: UNKNOWN / NOT_CERTIFIED
MATHEMATICAL_SCOPE: CONDITIONAL_ON_UNCERTIFIED_SAMPLER_CRITERION

本文独立查阅原论文、作者目录及论文的作者提交版本。搜索摘要只用来导航，未把聚合网站或模型回传当成定理证据。这里的“未确认覆盖”不等于“已确认无先例”，也不等于“当前公开状态已认证开放”。

## 1. 逐来源的核验及蕴含方向

| 原始来源、版本 | 精确位置与条件 | 对本轮结论的关系 |
|---|---|---|
| Lyons–Thom, *Invariant Coupling of Determinantal Measures on Sofic Groups*, [arXiv:1402.0969v2](https://arxiv.org/pdf/1402.0969v2), 2014-05-19 | Bernoulli 源定义 p.3；Theorem 7.3、Cor.7.4 p.24；Q7.7 p.25。前一定理要求 sofic Γ，算子属于 R(Γ) 或有限生成标签的 R(Γ,S)；后一结论要求 amenable Γ。 | **已覆盖子域**：amenable 场景的结论更强，给 Bernoulli 同构。sofic 场景只给 d-bar 有限依赖近似；尚需额外定理才能从这种近似推出 FIID。普适 W 源定理若成立，确实蕴含原文明确展开的 Q7.7；源转换见 audit01.md §7。 |
| Benjamini–Lyons–Peres–Schramm, *Uniform Spanning Forests* (2001), [作者原文](https://rdlyons.pages.iu.edu/pdf/usf.pdf) | 作者 PDF Theorem 7.8 p.25（无限图 transfer current）以及随后投影公式；Theorem 7.3 p.24（free=wired 判据）。 | **已覆盖工具**：FUSF 是闭有限循环空间正交补的 DPP；WUSF 是闭 star 空间的 DPP。该定理自身没有提供 iid 因子。 |
| Nam–Sly–Zhang, *Ising Model on Trees and Factors of IID*, [arXiv:2012.09484v2](https://arxiv.org/pdf/2012.09484v2), 2022-01-22 | Theorem 1 p.2：存在绝对 c,d0，对 d>=d0、beta>=0、tanh(beta)<=c/sqrt(d−1)，d 正则树的 free-boundary Ising 为 FIID。§2.2、Lemma 2.1 p.5：有限窗口的 `X_t=t tau+B_t` 弱解识别；Propositions 2.2–2.3 pp.5–6 处理半径与根变更的模型估计。 | **同方法**：Brownian 观察、后验漂移、从噪声强构造因子均有直接先行来源。**未覆盖一般结论**：所核验定理不量化任意二元法则或任意 DPP；无限树估计有 Ising/参数条件。不能把有限窗口的单个导数有界当作本轮全外场一致绝对行和界及普适无限系统定理。 |
| Mészáros, *Limiting Entropy of Determinantal Processes*, Ann. Probab. 48 (2020), 2615–2643, [作者提交 PDF](https://arxiv.org/pdf/1905.11459) | Theorems 2.4–2.5 p.9：有限图投影过程的局部极限和 tightness 假设下的归一化熵；Theorem 2.6 p.9：有限生成 sofic Γ、ℓ²(Γ×K) 上不变正压缩，给所有 sofic 近似相同的熵公式；Theorem 5.1 p.21 给 positive-contraction 的 p-tight 版本。 | **邻近结果，未覆盖 FIID**。熵公式与近似存在没有附带所需的等变因子映射。不能从“sofic 熵不依赖近似”反推 Bernoulli 因子。 |
| Angel–Ray–Spinka, *Uniform even subgraphs and graphical representations of Ising as factors of i.i.d.*, EJP 29 (2024), no.39, [正式论文作者机构版](https://dspace.library.uvic.ca/server/api/core/bitstreams/ec346c4f-76f7-4bb3-b54e-b95505de66de/content) | Theorem 1.4 正文 p.6；重述 Theorem 4.1 正文 p.22：连通 transient random rooted graph 的 WUSF 为 graph FIID。定理后的说明明确不要求 unimodularity。机构 PDF 比正文多一页封面，按正文页码定位。 | **已覆盖 WUSF 子域**，并且随机图统一构造比本轮固定图结论在该子域更强。对象是 wired；不能用此覆盖一般 FUSF。作者还明确未主张该 wired 结论本身的原创性。 |
| Timár, *Factor of iid's through stochastic domination*, [arXiv:2306.15120v2](https://arxiv.org/pdf/2306.15120v2), 2025-12-16；[HTML](https://arxiv.org/html/2306.15120v2) | §1 p.2 的 Theorem 1、Theorem 2；§3 p.5 的 Theorem 4、Cor.5；§4 p.6 的 Theorem 9。一般构造要求 invariantly amenable unimodular random graph 及文中 compatible monotone limit 条件；Cor.5 给 USF FIID，含 recurrent URG；Thm.9 给有限值 finitary 编码。 | **已覆盖 amenable/URG 子域**，并给更强 finitary 结论。其 §1 p.2 明确把一般 FUSF FIID 问题列为尚未解决。这是截至该版本日期的作者陈述，不能认证 2026-10-01 的全局开放状态。 |
| Lyons–Steif, *Stationary Determinantal Processes: Phase Multiplicity, Bernoullicity, Entropy, and Domination*, [作者 PDF](https://rdlyons.pages.iu.edu/pdf/dyn.pdf) | Theorem 3.1，作者 PDF p.15：任意可测 symbol `f:T^d->[0,1]` 对应的平稳 Z^d DPP 与 iid 同构。 | **已覆盖更窄子域且结论更强**。该陈述包括 indicator symbol 的投影端点，但不处理一般非 amenable 群或任意 Γ 集。 |

上表页码针对链接版本，未把预印本页码写成正式出版页码。尤其 Angel–Ray–Spinka 的正文页码与机构 PDF 物理页序不相同。

## 2. Mészáros 与 2024–2026 前向检索

直接打开 [Mészáros 作者主页](https://users.renyi.hu/~meszaros/)，网页自报更新日期为 2026-08-25。目录中最直接涉及 invariant DPP 的旧文仍包括上述 2020 熵论文，以及 2023 年的树匹配/邻接矩阵论文。没有把目录缺少某个标题用作不存在性证明。

对近期 DPP 相关条目另开作者提交页确认摘要范围：

| 近期条目 | 已读取来源与日期 | 核查结果与限制 |
|---|---|---|
| *Cocycles of determinantal hypertrees with small support* | [arXiv:2608.22255v1](https://arxiv.org/abs/2608.22255), 2026-08-23 | 作者摘要研究有限二维 determinantal hypertree 中小支撑 cocycle 的图型。未找到摘要中有一般 FIID 声明；这里只核了摘要，未声称审完全文。 |
| *The homology torsion growth of determinantal hypertrees* | [arXiv:2506.14694v2](https://arxiv.org/abs/2506.14694v2), 2026-04-23 修订，2025-06-17 初稿 | 作者摘要给归一化同调扭子对数的概率极限。未提供一般 DPP 等变采样器；这里只核摘要范围。 |
| *Coboundary expansion for the union of determinantal hypertrees* | [arXiv:2311.17897](https://arxiv.org/abs/2311.17897)，2024 年正式发表于 RSA | 原文摘要的对象是有限维 hypertree 独立并的高概率 coboundary expansion。没有从此结论导出本轮 FIID；没有做全文 FIID 不存在检索认证。 |

同时检索了下列关键词及年份变体，沿命中回到原论文或作者页面：

- `Mészáros determinantal iid`、`Mészáros determinantal processes factor iid 2024 2025 2026`。
- `determinantal processes factor of iid`、`determinantal measures Bernoulli shifts 2024 2025 2026`。
- `FUSF factor of iid 2024 2025 2026`、`free uniform spanning forest factor iid`。
- `covariance factors of iid stochastic localization`、`covariance factor of IID Brownian`。
- `Timár uniform spanning finitary 2025`、`Angel Ray Spinka uniform spanning factor iid`。

2024–2026 的实质相关命中包括 Angel–Ray–Spinka 正式版、Timár 2025 v2 和 Mészáros 的上述新论文。搜索也给出许多“有限 DPP 采样”“latent factor”“有限复形”同词异义命中，未纳入占位证据。

一条搜索片段似乎说 FUSF 已是 Γ-FIID；追到 [Oberwolfach Report 42/2013](https://oa.tib.eu/renate/server/api/core/bitstreams/a7a8364a-c6d7-4c43-887a-c1f6ae930bb1/content) 第 17–18 个 PDF 页面后，实际是条件句提出该问题，非已证明结果。检索系统标记的近期抓取/收录时间不等于论文时间。

未对所有引用数据库做穷尽式引用图检索，也未取得领域专家意见。因此当前裁决仍是 **完整占位未确认 / 新颖性 UNKNOWN**，不是“没有先行工作”。

## 3. 三种必须保留的区别

1. **原题蕴含**：若主采样判据成立，则其 DPP 应用覆盖 Lyons–Thom 明确展开的 regular 和有限自由标签情形。这是逻辑蕴含，独立于是否有别人在先证明。
2. **已有方法与子结果**：Brownian 观察/后验强构造方法、DPP 森林投影、amenable Bernoulli 同构、transient WUSF graph FIID、amenable URG 的 finitary USF 均已有原来源，不能作为本轮原创主张。
3. **未确认部分**：本次未核到一个既有定理直接推出所有可数 W、任意不变正压缩的规定 W 源总 Borel 因子，或所有固定局部有限简单图的 full-Aut FUSF 顶点源因子；但该检索结果不能颁发原创性或开放性证书。

## 4. 对 source.md 文献段的限定评价

已核验的承重比较与 source 的结论方向一致：Nam–Sly–Zhang 是直接方法前驱；Lyons–Thom 的 sofic 近似不能代替因子构造；wired 与自由森林应分开；Timár 的 amenable 条件不可删除。

source 声称附件中列有十六项来源，但附件在本审未读取。Fujisaki–Kallianpur–Kunita、各 stochastic localization/有限谱独立采样文章及 strongly Rayleigh 文献的所有细节**未在本次范围核验中逐条认证**。它们不能借本文被记成已全面审完；本报告也没有用“整张来源表已通过”掩盖该边界。

应用条件的独立推导、signed-action 处理、全输入 equivariance、顶点编码及原 Q7.7 蕴含见同目录 `audit01.md`。主定理正确性须由独立整稿审查处理。
