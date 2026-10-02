# References and source audit

只列本次实际打开并核对到相关定理/段落的来源。近期研究稿用于发现和交叉检查，
不被当作已发表先例或独立正确性认证。

## Primary literature

1. Russell Lyons, **Determinantal probability: basic properties and conjectures**,
   Proceedings of the ICM 2014, Vol. IV, 137--161.
   [Author PDF](https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf).
   - Theorem 5.2, printed p. 157：abelian 几何平均双侧支配及最优性摘要。
   - §5.2 opening and Conjecture 5.7, printed pp. 157--158：sofic 上下文、
     \(\ell^2(\Gamma)\) 单轨道题面和 FK 公式。
   - Theorem 2.4：有限 mixed-pattern DPP 行列式公式；本报告树条件化也给出
     了所需 Schur 补推导。
   - 同时核对了作者的 [ICM errata](https://rdlyons.pages.iu.edu/errata/icm.pdf)
     （页面标注 2025-12-30）；其中没有修改或撤回 Conjecture 5.7。

2. Russell Lyons and Jeffrey E. Steif,
   **Stationary determinantal processes: phase multiplicity, Bernoullicity,
   entropy, and domination**, Duke Math. J. 120 (2003), 515--575.
   [Author PDF](https://rdlyons.pages.iu.edu/pdf/dyn.pdf).
   - Theorem 5.3：一维中普通随机序阈值对每个固定符号的充要刻画。
   - Theorem 5.11：\(\mathbb Z^d\) 中每个固定可测符号的普通/顺序支配
     if-and-only-if；这直接支持 ICM “最优”更自然的逐点语义。
   - Definition 5.15 and Theorem 5.16 属于更强的 full-conditioning 概念；本报告
     不把它与普通随机序混用。

3. Hanfeng Li and Andreas Thom,
   **Entropy, Determinants, and \(L^2\)-Torsion**,
   J. Amer. Math. Soc. 27 (2014), 239--292.
   [arXiv PDF](https://arxiv.org/pdf/1202.1213),
   [arXiv record](https://arxiv.org/abs/1202.1213).
   - Theorem 1.4：可数 amenable 群、任意正
     \(g\in M_d(\mathcal N\Gamma)\) 的有限压缩 FK 行列式 infimum/Følner 极限；
     题面允许奇异正元素。

4. Russell Lyons and Andreas Thom,
   **Invariant Coupling of Determinantal Measures on Sofic Groups**,
   Ergodic Theory Dynam. Systems 36 (2016), 574--607.
   [arXiv HTML, v2](https://arxiv.org/html/1402.0969).
   - §3 Lemma 3.4：\(R(\Gamma,S)=M_S(R(\Gamma))\)。
   - Lemma 后紧接的定义：自然有限标签迹
     \(\tau_S(T)=\sum_{s\in S}\tau(p_sTp_s)\)，所以 \(\tau_S(I)=|S|\)，不是
     每坐标归一化迹。
   - Theorem 2.1：有限 DPP 的算子序推出随机序；本报告的 FK 插值证明没有把
     该算子序误用于不可比较的端点。第 5.3 节只在每个有限压缩上使用该有限定理，
     再由递增柱事件定义传到可数空间。

5. Gábor Elek and Endre Szabó,
   **Sofic representations of amenable groups**,
   Proc. Amer. Math. Soc. 139 (2011), 4285--4291.
   [AMS PDF](https://www.ams.org/proc/2011-139-12/S0002-9939-2011-11222-X/S0002-9939-2011-11222-X.pdf),
   [arXiv record](https://arxiv.org/abs/1010.3424).
   - Theorem 1：sofic 群沿 amenable 子群的 amalgamated free product 仍 sofic；
     平凡 amalgam 给 \(C_3*C_3\) 的 sofic 性。这里只用于核对反例仍在 ICM
     原上下文内。

6. Itai Benjamini, Russell Lyons, Yuval Peres and Oded Schramm,
   **Uniform spanning forests**, Ann. Probab. 29 (2001), 1--65.
   [Author PDF](https://rdlyons.pages.iu.edu/pdf/usf.pdf).
   - §11 and proof of Theorem 11.1：regular-tree wired forest 下的独立
     parent-hitting percolation 支配是经典机制。RESULT.md 同时给了独立的
     Hilbert-space/BFS 推导，不把这一历史来源当作省略证明的黑箱。

## Current public research artifact (not a literature-status certificate)

7. **Pointwise FK thresholds: counterexamples and the amenable boundary**,
   public draft pull request
   [#93](https://github.com/cat5779/rl01/pull/93), especially
   `research/dpp07/g2/RESULT.md` and `SOURCES.md`.
   - 本次逐式重查的树投影、双侧谱隙扰动和 amenable 边界候选来源。
   - PR 内 review 文件没有被用作证明证据；RESULT.md 的承重步骤已在本交付中
     自包含重写，有限接口另由 `check01.py` 精确复算。

8. **A common iid monotone coupling at the Fuglede--Kadison parameter**,
   public draft pull request [#92](https://github.com/cat5779/rl01/pull/92), especially
   `research/dpp07/g1/proof03.md`.
   - 实际核对了其联合 iid 耦合路线；本报告只证明普通随机序，不依赖该稿的
     total Borel sampler、等变耦合或额外的零参数假设，因此没有把这些结论导入。

## User-provided proof candidate

9. **Bernoulli domination for invariant determinantal measures**, dated
   27 September 2026, 用户提供候选 A（无公开链接）。
   - 实际依赖范围：Lemma 1 的有限维条件 odds 与导数方向，以及 §3 对 Theorem 1
     的 FK 等值插值、逆压缩、正则化和补核论证。
   - 本报告逐项重算了 inclusion-basis 导数恒等式、Schur 补变分式、路径导数、
     有限压缩方向和奇异极限；候选稿的自述或审阅状态没有被当作正确性证据。

## Search and errata scope

- 实际检索组合包括 `Lyons Conjecture 5.7 Fuglede--Kadison`、
  `Bernoulli domination Fuglede--Kadison determinantal`、
  `stationary determinantal geometric mean domination`、
  `amenable finite compression determinant`、`sofic amenable amalgam free product`。
- 实际打开并比对了 ICM 已发表作者 PDF、作者 errata、Lyons--Steif 原文、
  Li--Thom 原文、Lyons--Thom 原文、Elek--Szabó 原文、BLPS 原文以及上述两份
  当前公开研究稿。检索目的仅为查找直接先例和核对定理前提，不支持穷尽性或
  新颖性结论。

## Source-boundary notes

- ICM 原句没有形式定义“optimal”，所以本文给出的是基于相邻定理的语义判断，
  不是作者通信或心理意图断言。
- “近期未发现相同表述”不等于新颖性证明。本交付不提出首次发现或穷尽文献主张。
- 用户提供候选 A 的可公开识别信息和实际依赖范围已列于第 9 项；未公开的存储
  位置、仓库信息和版本标识不进入公开稿。
