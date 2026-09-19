# Claude 文献与方法清点：查过什么，真正试过什么

日期：2026-09-19。审计对象是此前交付稿、独立审查、任务包和本次重新检索的原始文献。**没有找到记录不等于证明从未有人读过；写进提示词不算已经尝试，原文检索也不算已完成方法迁移。**

## 先回答总问题

整个 c∈(37/40,1) 的真实 sine-DPP 完整配置熵率凹性仍未解决；也没有证明半密度版本覆盖整个区间。S70 的连续 c 条带仅为固定 rho=1/3、c∈[.95,.9535]、p∈[.42,.48]。不能将它说成统一阈值提高到 .9535。QWE07 的密度扩张和 S69 的偏置扩张同样有各自冻结参数，不能自动拼成联合参数区域。

此前的文献核查只完成了一部分，**没有证据支持“Claude 推荐的跨领域方案均已检索、去重并尝试完毕”**。本次补做的是原始论文定位与初步适用性筛查，不将今日补查倒记为昨日已完成工作。

## 历史执行与去重记录

以下本地证据路径以协调目录 `math/sa-dispatch-20260918/` 为基准；公开旧结果主要在 RL01 PR45 的相应 CYCLE 目录。审查 PR 编号均属于 RL01，特别标注 DPP 的除外。

| Claude 提议 | 找到的实际执行证据 | 去重与当前结论 |
|---|---|---|
| Entropic independence / approximate tensorization | `harvest/CYCLE11/S61/S61_CYCLE10_RESULT.md` §9 明确记录核查两篇原始文献；§10 列书目。 | **确实做过适用性检查，未闭合目标。** KL 收缩给出的方向不能直接支付该任务所需上界，条件熵张量化也缺目标桥梁。只排除直接套用，不宣判整类理论无用。S61 真正采用的是 strong-Rayleigh 随机覆盖与后验 fiber 耦合。 |
| Chatterjee / Stein | `harvest/CYCLE09/WARD_STEIN_PR2/proofs/ward-stein-budget-20260918/RESULT.md` §1.2、§3、参考文献 [C]。 | **实际用过交换对分部积分。** 建立正可逆链并直接推导有限恒等式；这不是 Lindeberg 逐坐标替换，不能因作者同名而去重掉后者。 |
| Guerra–Toninelli interpolation | 未找到已交付的 DPP 插值族、导数符号证明或失败证书。 | **未找到完整尝试记录。** QWE09 是已派候选工具任务，不是完成回执。 |
| Lindeberg / invariance | 未找到满足合法核、光滑性与余项预算的实际替换证明。 | **未找到完整尝试记录。** S52 做过 Rademacher 矩，Ward–Stein 做过交换对，两者均不能替代这项工作。 |
| cavity | 未找到针对实际熵/条件互信息的 cavity 递推及可求和误差。 | **未找到完整尝试记录。** QWE09 中作为工具种子提出。 |
| Cauchy minors → Borodin–Olshanski / z-measures | 已有 Cauchy–Binet、行列式和奇偶代数；未找到目标随机投影系综与该文献概率律的精确识别。 | **代数相似不等于已迁移可积结构。** 需要核/测度、参数、归一化以及所求观测量的映射。 |
| Candès–Tao / Rudelson–Vershynin RIP | 未找到适用于 Hilbert/Cauchy 奇偶矩阵、带坏事件支付的完整证明。 | **未找到完整尝试记录。** 随机坐标子集不等于随机 Fourier/Gaussian 测量；主子式良态也不直接推出熵曲率符号。 |
| Dobrushin-in-expectation / spectral independence | Claude PR50 已辨明所写行和是协方差量，不是 sup 条件影响；S61 有相邻的熵独立性核查。 | **关键桥梁仍缺，未找到完成的平均影响→全条件交叉比预算。** 本次未把“Dobrushin-in-expectation”这一宽泛标签认定为一条已定位、可直接调用的定理。 |
| 循环模型去掉 Fisher 边界亏损 | S52 的循环分解、S55 的定性传递（PR37/38）。 | **做过，属于已有工具。** 循环模型仍要证明带符号余项；有限尺寸正值不是无限体积符号证书。 |
| 最坏 pair 上界改成实际平均 | S67 首稿 PR51 含真实四点逐配置反例及六点单 pair 平均反例；新续稿另有 count-gauge/resolvent 改进，独立审查中。 | **做过部分且有明确反例。** 简单 factor-one 平均替换失败；跨 pair 的总补偿仍开放。不能把“平均化全死了”作为结论。 |
| 真 Toeplitz 曲率超加性 / 相邻块互信息 | Claude PR50 明确剩余命题；DPP PR130 的 QWE08 已派。 | **尚无完成证明。** 超加性不等于每个 n 的归一化序列单调；Fekete/Dini 不能填补未证前提。 |
| 重采样/缺陷分解 | S68 全稿和附录独立审查 PR48。 | **已做代数与有限体积部分。** 不能把重新命名的互信息项算作新符号估计；联合尺度、全外部条件与无限体积符号仍未闭合。 |
| c∈[.93,.97] 的精细循环证伪扫描 | 已有小尺寸检查与 Claude n=12 分解复算；未找到覆盖提议整张网格的完整回执。 | **不能声称已完成该扫描。** 其危险尺度解释未证；数值负/正曲率各自必须按模型、有限体积及精度解释。 |

截至本次远端读取，DPP PR130、PR131 都只有原任务包提交，无结果提交、无评论。**已派不等于已试成功或失败。**

## 本次补查的原始来源与迁移门槛

阅读层级逐项标明；这不是穷尽综述或外部新颖性认证。以下“迁移门槛”是本项目的适用性判断，不是论文声称 DPP 问题可解或不可解。

1. **Guerra–Toninelli**, *The Thermodynamic Limit in Mean Field Spin Glass Models*, cond-mat/0204280。本次读到 §2–4、Lemma 1、Theorem 1：论文的基本插值经 Gaussian 分部积分与 overlap 平方的凸性取得导数符号，并讨论非 Gaussian 扩展。可借鉴“整块—独立分块”的构造；iid 掩码本身不提供这些符号。必须构造实际目标的插值及全部误差，而不是直接引用自由能超加性来断言熵二阶导超加性。[原文](https://arxiv.org/pdf/cond-mat/0204280)

2. **Chatterjee**, *A generalization of the Lindeberg principle*, math/0508519。本次查看 Theorem 1.1 及逐坐标替换证明：误差由条件一、二阶矩失配和三阶光滑余项控制。DPP 迁移至少要给出沿替换路径仍有定义的熵泛函、导数预算与目标符号余量；任意 Gaussian 化掩码可能离开合法核集合。尚未完成这些步骤。[原文](https://arxiv.org/pdf/math/0508519)

3. **Aizenman–Sims–Starr**, *An Extended Variational Principle for the SK Spin-Glass Model*, cond-mat/0306386。本次定位原始论文及摘要，未完成正文定理适用性审查。它是 cavity/变分路线的具体阅读入口；不能把 SK 自由能变分式直接当目标熵的变分式。[原文入口](https://arxiv.org/abs/cond-mat/0306386)

4. **Anari–Liu–Oveis Gharan**, *Spectral Independence in High-Dimensional Expanders and Applications to the Hardcore Model*, 2001.00303。本次核对摘要和研究对象；关于所有条件化下相关谱控制到采样混合的结论，未自动提供参数 a 的熵曲率符号。仍需核查真实后验族及目标加权交叉比的桥梁。[原文入口](https://arxiv.org/abs/2001.00303)

5. **Anari–Jain–Koehler–Pham–Vuong**, *Entropic Independence I*, 2106.04105。S61 交付稿明确记录查过此文；本次复查原始摘要。保持外场/下降算子的精确定义和不等式方向，不能将 KL 收缩翻成所需上界。[原文入口](https://arxiv.org/abs/2106.04105)

6. **Caputo–Menz–Tetali**, *Approximate tensorization of entropy at high temperature*, 1405.0608。S61 交付稿明确记录查过；本次复查原始摘要及出版入口。需验证弱依赖条件、常数及目标转换。原文不是无条件的“平均替换 sup”定理。[原文入口](https://arxiv.org/abs/1405.0608)

7. **Rudelson–Vershynin**, *Sparse reconstruction by convex relaxation: Fourier and Gaussian measurements*, math/0602559。本次查看 §III 与 Lemma 3.5：随机 Fourier 采样及有界坐标向量的 Rademacher 和估计是具体机制。迁移须重新核对 Hilbert/Cauchy 矩阵的坐标界/相干性、稀疏阶数、概率以及坏事件的熵导数代价。[原文](https://arxiv.org/pdf/math/0602559)

8. **Candès–Tao**, *Near Optimal Signal Recovery From Random Projections: Universal Encoding Strategies?*, math/0410542。本次仅定位原始书目信息和摘要，未完成定理级阅读。作为随机测量的对照来源，不作现有证明输入。[原文入口](https://arxiv.org/abs/math/0410542)

9. **Borodin–Olshanski**, *Distributions on partitions, point processes, and the hypergeometric kernel*, math/9904010；*Meixner polynomials and random partitions*, math/0609806。本次核对原始摘要，未完成概率律识别。它们研究特定分拆测度及其行列式核；“同有 Cauchy 行列式”不足以移植其公式，更不足以推出 Shannon 熵曲率。[1999 原文入口](https://arxiv.org/abs/math/9904010)，[2006 原文入口](https://arxiv.org/abs/math/0609806)

## 去重后值得继续的对象

**优先等 QWE08 与 QWE09 的实际返回，不重复投放。** QWE08 已承担真块相邻互信息/超加性；QWE09 已承担奇偶 iid 系综与条件互信息的联合支付。其真正未做完的工作是创造适用于这些对象的插值或揭示不等式，而不是再次复述奇偶分解。

后续对整个 (.925,1) 的任务应要求交付参数化的定理/误差控制，并明确 c→1 时常数如何变化；固定 c=.95 的发现可作种子，但必须说明延拓桥梁。开区间全覆盖不要求常数在 c→1 保持有界，要求的是对每个目标 c 都能闭合符号，或有可覆盖区间的局部一致论证。有限个小条带不是这种覆盖。

下一轮理论选择建议：首先争取 QWE09 的“系综条件熵 + 条件互信息”联合结构估计；其次保留真实测度下跨 pair 的总补偿。RIP 与 z-measures 可作短适用性探针，先找精确连接，再决定是否投入整轮 PRO。没有新的适用性桥梁时，不继续购买同一固定见证的细网格复算。

## 来源状态更新

- S67：`S67_COUNT_GAUGE_SUPPORT.zip` 的 14 个文件已收到，完整原件在本目录 `S67/original/S67_CONTINUATION/`。两个 RESULT 文件是同一续稿的两个文件名，不能误认为其中一份是旧首稿。已交原有 Sol 单独审查，当前 AUTHOR_ONLY。作者自己明确主目标未完成，Fisher>=20.75 为未验证充分条件。
- S69：独立审查 PR55 已完成。接受固定 rho=1/3,c=.95,a∈[.02,.0255] 的局部结论。并行复算程序需逐工作线程设向上舍入；审稿者在隔离副本修复后重新生成全部支付证书，结果一致。应保留复现修复说明，不能把原脚本写成无需修复即可重跑。
- 本轮没有新增或重发任何网页版任务，没有新建 Sol 任务或子智能体，没有把源文件校验当数学验收。
