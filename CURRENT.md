# 当前 DPP 状态

快照：2026-10-03。本文是来源与已审范围索引，不构成新的证明或新颖性认证。这里的“已审”指所链接的仓库内数学审查；没有声称经过形式化验证或领域审稿人最终认证。固定核与核族、法则层 joining 与共同 iid 映射、弱过程与强过程分别记账。

H 允许任意可数指标集 W 与可数群的置换作用，并使用 W-indexed iid。C、D、F、JF、JO 以下默认可数群的正则作用、复 Hermitian 正压缩核；不能把 W 源自动替换成正则群源，也不能把固定核构造提升成跨核共同构造。

## 主理论

| 代号 | 当前已审结论 | 仍保留的边界 | 原稿与审查 |
|---|---|---|---|
| H | 对每个固定不变正压缩核，在 W-indexed iid 上有全输入 total Borel 等变 DPP 采样器；奇异和确定性核包含在内。当前论文进一步给出对核联合 Borel、对任意双射自然的规则 | 本项 H 本身不含 finitary 或有限查询结论；来源作用约定不能省略 | [原始定理](research/q77r05/g4/THEOREM.md)、[完整证明](research/q77r05/g4/PROOF.md)、[审查1](research/q77r05/g4/REVIEW01.md)、[审查2](research/q77r05/g4/REVIEW02.md)；[当前论文](research/paperA_r01/t1/paperA.md)、[图接口审查](research/paperA_r01/t1/AUDIT.md) |
| FUSF | 每个局部有限连通简单图上有统一、不读取根、与图同构交换的联合 Borel 顶点 iid FUSF 因子 | 无标记平行边有标签源障碍；该结论不提供一般连通性／群 cost 修复 | [当前论文](research/paperA_r01/t1/paperA.md)、[源审查](research/paperA_r01/t1/CROSSCHECK.md)、[Cayley 接口](research/lgr06/audit/VERDICT.md) |
| C | 每个固定 A≤B 存在不变单调 joining，适用于任意可数群的正则作用 | 弱极限只产生 law；一般 joint iid 不随之得到 | [可见完整核心](research/dpp07/g5/CORE.md)、[审查1](research/dpp07/g5/REVIEW01.md)、[审查2](research/dpp07/g5/REVIEW02.md) |
| D | 任意固定 A,B 有 d̄(μ_A,μ_B)≤τ\|A−B\|；有序时为 τ(B−A) | 这里的 d̄ 使用不变 joint law。当前论文的 sofic 叙述不撤销上述核心的任意可数群范围 | 同一 [核心](research/dpp07/g5/CORE.md) 与 [范围审查](research/dpp07/g5/REVIEW02.md) |
| F | Bern(FK(Q))≤st μ_Q≤st Bern(1−FK(I−Q))，任意可数群正则作用，包括复核与奇异端点 | FK 数据的统一标量锐性不等于每个固定非标量核的最优性 | [当前论文](research/paperA_r01/t1/paperA.md)、[FK 证明](research/paperA_r01/t2/RESULT.md)、[数学审查](research/paperA_r01/t2/AUDIT.md) |
| O | 通用逐核 FK 阈值等号已被 C3*C3 投影、gapped 与有限支撑扩展等反例否定；amenable 范围内由经典行列式必要性结合 F 得精确阈值 | 一般非 amenable 的正确分类仍开放；这没有否定 F | [反例与扩展](research/dpp07/g2/RESULT.md)、[核心审查](research/dpp07/g2/REVIEW_CORE.md)、[扩展审查](research/dpp07/g2/REVIEW_EXTENSIONS.md) |
| JF | 每个固定 Q 从一个正则 iid 输入同时产生 Bern(FK(Q))⊆DPP(Q)，全输入 Borel 等变；FK=0 使用 H | 上端由 complement 单独得到；没有自动形成三层 sandwich、grand coupling 或 true p₋ 的 endpoint 因子 | [入口](research/dpp07/g1/README.md)、[修正版证明](research/dpp07/g1/proof03.md)、[冻结修正版审查1](research/dpp07/g1/REVIEW02.md)、[审查2](research/dpp07/g1/REVIEW03.md) |
| JO | 当 B−A 属于 reduced group C* algebra 且 B−A≥δI>0 时，存在精确 ordered joint iid；允许奇异端点 | 任意有序核对的 exact joint iid 仍开放；η>0 的近最优相对转移不能直接令 η=0 | [核心 §2–3](research/dpp07/g5/CORE.md)、[限定范围审查](research/dpp07/g5/REVIEW02.md) |

有限自由标签 Γ×S、双侧谱隙下的 finite-site／all-completions 证书有独立后继记录；其全文与审查未在本公开库发布。公开旧 [#83](https://github.com/cat5779/rl01/pull/83) 仍按历史候选保全，本页不以 H 或未公开后继认证旧稿。

## R1b：正流选择器

原目标是非对角、有隙核、任意 rank-one 支撑上的单一 Borel、置换等变、正的 capacitated birth-flow 选择器，稳定常数不依赖维数或支撑大小。这个目标仍开放。

| 当前节点 | 已审范围与证据 |
|---|---|
| 固定有限支撑界 s | 全正流 fiber 的 least-Euclidean-norm 选择器具有 C(ε,s)，独立于环境维数；[证明](research/dpp15/g11/RESULT.md)、[审查](research/dpp15/g11/REVIEW.md) |
| 对角核、任意支撑 | 显式公式有 C=2；[证明](research/dpp15/g12b/RESULT.md)、[公式审查](research/dpp15/g12b/REVIEW.md) |
| canonical 分量大小≤固定 r | 单一、原 fiber 内、Borel、置换等变选择器有 C(ε,r)，独立于分量数及环境维数；可取 10ε^−2(r!)²2^((r−1)(r+4))；[完整763行证明](research/dpp18/g17/RESULT.md)、[分离的主审](research/dpp18/g17/REVIEW02.md) |
| 两个真实否定结果 | dimension-free **全 fiber Hausdorff** 命题被[坏流反例](research/dpp13/g12/RESULT.md)及[审查](research/dpp13/g12/REVIEW.md)否定；实际 global least-norm 选择器的支撑一致常数被[√s 反例](research/dpp16/g11/RESULT.md)及[审查](research/dpp16/g11/REVIEW.md)否定。两者均没有排除另一个稳定选择器 |
| commuting 工具包，PARTIAL | 已审 signed current、2J+ 正 fiber 容量、固定 P endpoint repair、scalar-complement 及有限一致性等价；[原稿](research/dpp17/g11/RESULT.md)、[部分范围审查](research/dpp17/g11/REVIEW.md)。整类 COM 与变化 P 的 exponent-one 选择器仍开放 |

r 与 s 固定的定理不能提升成随 r、s 增长一致的定理。较早的显式低支撑、半核、共同 partition 与 matching 常数作为辅助历史保留在 ARCHIVE。

## R1c 与强过程

| 当前节点 | 已审结论 | 剩余接口 |
|---|---|---|
| Ordinary weak | 在所列可测、连续性及平均活动假设下存在 countable pure-birth prescribed-marginal realization；[抽象证明](research/dpp12/g14/RESULT.md)、[审查](research/dpp12/g14/REVIEW01.md) | 没有不变性、唯一性或强噪声因子 |
| DPP weak superposition | ordinary weak 与 countable amenable invariant weak 已审；[完整17页原稿](research/dpp10/g9/RESULT.pdf)、[正文](research/dpp10/g9/RESULT.md)、[独立范围审查](research/dpp10/g9/REVIEW.md) | 任意非 amenable 不变弱实现仍需 local fixed-point 存在；强提取需要额外 causal joint product-Poisson 与 AL，尚未由一般 DPP 率推出 |
| Complete endpoint reduction | global invariant weak 当且仅当沿 mesh→0 分割可独立选择 local dynamically admissible invariant endpoint laws；无需 refinement compatibility；[完整证明](research/dpp15/g13/RESULT.md)、[审查](research/dpp15/g13/REVIEW.md) | 这是等价约化，没有证明任意群的 local endpoints 存在 |
| Residually finite quotient criterion | 在商解、局部 DPP／生成元收敛、截断尾及 UI 的明确假设下可取商极限；[证明](research/dpp16/g13/RESULT.md)、[审查](research/dpp16/g13/REVIEW.md) | 不提供所需商解或一般不变存在性 |
| Fixed finite-range Harris theorem | 对一套固定、uniformly bounded、finite-range covariant rates，共同独立 PRM 在一个好事件上覆盖全部初态；路径唯一、柱 forward equation 唯一、精确 DPP 边缘；[证明](research/dpp17/g13/RESULT.md)、[完整范围审查](research/dpp17/g13/REVIEW.md) | 无界／非局部、跨逼近共同噪声闭合和一般 JO 均没有由此解决 |

## 当前开放入口

以下链接固定到本次审计 head；未把它们合入已审结果目录。

- [#97](https://github.com/cat5779/rl01/pull/97)：C3*C3 true threshold p₋=1/2 的 invariant endpoint／joint iid。已审无限 branching、两条路径障碍及 LP 等价；未审独立窗口证书不计入。 [冻结证据](https://github.com/cat5779/rl01/blob/d7306c4bf0e5354137eb20dc8ef1c74952a1b3bf/research/dpp08/g2/REVIEW.md)；head `d7306c4bf0e5354137eb20dc8ef1c74952a1b3bf`。
- [#102](https://github.com/cat5779/rl01/pull/102)：一般 R1b 任意支撑目标任务。受限子路线未解决这个全目标。 [冻结证据](https://github.com/cat5779/rl01/blob/1c6abe9c973c0678ef2bee7d1d177cb23f7e0a4c/research/dpp11/g11/TASK.md)；head `1c6abe9c973c0678ef2bee7d1d177cb23f7e0a4c`。
- [#122](https://github.com/cat5779/rl01/pull/122)：G15 endpoint-capacity attack，PARTIAL。独立审查仅认证已有范围；新 all-dimensional energy／Hessian 推导没有整证明接受。 [冻结证据](https://github.com/cat5779/rl01/blob/e5be923236f109968a1acc8a46115744c3e6a57c/research/dpp18/g15/REVIEW02.md)；head `e5be923236f109968a1acc8a46115744c3e6a57c`。
- [#123](https://github.com/cat5779/rl01/pull/123)：G16 commuting finite consistency，OPEN。仅 continuation §1 的 fixed-P 完整正 fiber repair（4/ε）新获主审；其余续稿仍候选。 [冻结证据](https://github.com/cat5779/rl01/blob/b279b112c9bc4b25c7827dd7fb4ae9dc445ae214/research/dpp18/g16/REVIEW02.md)；head `b279b112c9bc4b25c7827dd7fb4ae9dc445ae214`。

## 高对比度熵与连通性

真实 sine Toeplitz DPP 的全部空间配置 Shannon 熵率，固定每个 0<ρ,c<1、全合法 a∈[0,1−c] 的凹性仍开放。真实窄区继续有效；局部扩张只能取已有集合的并，不能拼成未经证明的参数笛卡尔盒。精确方法反例也不等于该目标的反例。

当前[高对比度账本](research/ledger_hc01/ledger.md)与[机器表](research/ledger_hc01/ledger.csv)分别记录21项限定正面闭合、29项精确方法反例、6项见证／分配失败、17项未修缺口、7项已修继承、12项无结果中止。这92行不是所有库内子主张的穷尽认证。账本引用的其他库证明必须按其固定提交独立读取；本页没有把那些跨库原稿重新认证。其 PDF 是历史快照报告，列在 ARCHIVE。

一般 LG／group-cost 目标仍开放。H/FUSF 因子不提供 cheap connected repair。森林子关系、relative cost、cycle defect、exchange 等价和 F2×F2 cost-one 特例的来源与审查作为历史辅助保留，见 ARCHIVE；它们不构成 fixed-price 或一般 cost 定理。

## 来源与版本规则

本页每条当前结论的冻结 SHA 及完整文件 blob／SHA256 见 [来源索引](docs/dpp20261003/index01.json)。旧 roadmap、补充稿、自审与历史 PR 的原始状态字样保留，不作为当前结果范围。数学原稿未改写。候选材料归档仅表示保全与退出活动入口，不表示证明接受、撤回或 PR 已合并。
