# G6 范围与森林原始来源核验

日期：2026-10-01；对象仅为 `excerpt.md` 的完整可见范围及森林段落。该输入严格为 **20,000 字符截断节选**，不是 G6 全文。本记录不认证候选 C 或任何新颖性。

## 已实际读取的原始来源

| 原始来源与实际版本 | 已读定位 | 用途及条件核对 |
|---|---|---|
| [Lyons–Thom, Invariant Coupling of Determinantal Measures on Sofic Groups](https://arxiv.org/pdf/1402.0969v2)，v2，2014-05-19；arXiv 元数据列期刊 2016 | §1 pp.3–4；Definition 3.1 p.6；R(Γ)、R(Γ,S) 与 Lemma 3.4 pp.8–9；准传递 joining 度量 p.23；Theorem 7.3、Corollary 7.4 p.24；Questions 7.5–7.7 p.25 | 原文自由／有限标记算子范围与 C 匹配。7.3 使用 sofic 和有限生成；7.4 使用 amenable；它们分别提供逼近、同构，均非一般 C。原文未明确要求任意目标作用配正则 Γ 源。 |
| [Benjamini–Lyons–Peres–Schramm, Uniform Spanning Forests](https://rdlyons.pages.iu.edu/pdf/usf.pdf)，Ann. Probab. 29 (2001), 1–65；实际作者 PDF 为 2009-01-27 版、72 页 | §4 p.12 eqs. (4.4)–(4.5)；Theorem 5.1 p.17；§7 pp.22–23 的能量、星与循环空间，Propositions 7.1–7.2；Theorem 7.8 p.25；§12 proper planar 定义 p.51；Theorem 12.2 p.52 | 单位电导时 FUSF 核为循环正交补投影，WUSF 核为星投影。Wilson rooted at infinity 要求瞬逝。平面对偶定理要求 proper planar 及局部有限对偶，给自由／有线互换，不是普遍 FUSF 因子定理。 |
| [Angel–Ray–Spinka, Uniform even subgraphs and graphical representations of Ising as factors of i.i.d.](https://arxiv.org/pdf/2112.03228v1)，v1，2021-12-06，33 页 | Theorem 1.4 与紧随注释 p.5；§2.1 pp.6–8；§4 pp.22–25，Theorem 4.1 p.23 | 连通、局部有限、几乎必然瞬逝的随机根图；WUSF 为 graph-FIID。此定理不要求幺模性。源在顶点上 iid，可取 Uniform[0,1]。该定理对 T4×C3 适用，但核是 Q_W。 |
| [Timár, Factor of iid's through stochastic domination](https://arxiv.org/pdf/2306.15120v2)，v2，2025-12-16，8 页 | 开放问题声明 p.2；§2 pp.2–3；Definition 1 和兼容单调极限 p.4；Theorem 4、Corollary 5 p.5；Theorem 9 p.6 | 主条件为 invariantly amenable URG；Theorem 4 必须结合 Definition 1 的兼容单调条件阅读。Corollary 5 给 USF 因子，Theorem 9 给有限值 finitary 因子。一般 FUSF 问题的开放声明不能确定具体非顺从 Cayley 单例。 |

页码均指上述实际 PDF 的页码，不混用期刊排版页码。BLPS 实际作者版为 2009 年修订稿，不能把本报告页码当作 2001 年期刊分页。

## 原题范围的核对方法

以 C 为条件，单标记得到 R(Γ)，有限标记得到 M_S(R(Γ))；有向 Cayley 弧坐标和二进制源拆分的完整推导见 [audit01.md](C:/game/ai4math/math/nosofic01/r04/g6/audit01.md)。这项结论是对象与作用的直接对应。

Question 7.6 明示准传递 W；Question 7.7 没有明示同样的全部量词，更没有明示任意 W 一律配正则 Γ 源。不能把相邻问题的条件扩大后作为 C 回答原题的必要条件。Prop.3 的反例只针对这样额外指定的版本。

## 文献所能支持的森林比较

- **以 C 为条件**，T4×C3 和一般有限生成 Cayley 图的 FUSF 因子结论有有效的投影及双弧推导。
- ARS 所给 WUSF 因子已知，与本例 FUSF 的律不同，不能替换主结论。
- 表面群 proper planar Cayley 图的 FUSF 可通过对偶 WUSF 与对偶补边推出；自由面轨道提供正则 Λ 源到对偶顶点源的明确转换。这是既有定理的推论，不是 C 的独立证据。
- Timár 的顺从情形因子／finitary 结论不覆盖 T4×C3。其一般问题开放声明只按版本日期记录。

## 访问与检索限制

对 T4×C3 使用了包含 `T_4 C_3 spanning factor iid` 和 `free uniform spanning forest factor product tree` 的补充检索。未定位精确同结论或反例仅记 **UNKNOWN / PRIOR_ART_UNRESOLVED_IN_THIS_AUDIT**；不是完整查新，也不证明“开放”或“新”。

节选的其余 Papangelou、shorting、动力学、finitary 文献比较表，以及截断的 Nam–Sly–Zhang 条目，不在本次来源认证范围内。ARS 的 2024 发表年份没有从这次实际访问的 arXiv 元数据独立核实；本报告依赖已读的 2021 v1 定理，不用该年份支撑数学结论。
