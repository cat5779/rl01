# G6 原题与先行工作核查

DATE: 2026-10-01 (Asia/Singapore)
FULL_DPP_PRIOR_ART: UNCONFIRMED
FULL_FUSF_PRIOR_ART: UNCONFIRMED
NOVELTY: UNKNOWN / NOT_CERTIFIED
MATHEMATICAL_SCOPE: CONDITIONAL_ON_UNCERTIFIED_SAMPLER_CRITERION

## 1. 逐来源的核验及蕴含方向

上表页码针对链接版本，未把预印本页码写成正式出版页码。尤其 Angel–Ray–Spinka 的正文页码与机构 PDF 物理页序不相同。

## 2. Mészáros 与 2024–2026 前向检索

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
