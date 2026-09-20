# 方法地图与下一轮投入 — 2026-09-20

主目标和严格覆盖见TARGET.md、STATUS.md；失败命题的冻结参数见COUNTEREXAMPLES.md。旧长表原样保存于docs/history/20260918-root/METHODS.md，旧“正在跑”不再代表当前状态。

## 当前值得继续的三条线

| 优先级 | 工具与接口 | 下一份成果必须交付什么 | 不值得续费的重复 |
|---|---|---|---|
| 1 | QWE08偏置矩／秩一二部MI + S77 Fisher–Burg | 真正高秩、任意尺寸的有符号分组，或结构化负环预算；精确进入M''=I_rel−B | 再证秩一、小尺寸网格、把负monomial删除 |
| 2 | S78真实揭示logdet补偿 + S75星形平均正性 | 多中心整体预算，压低核心截断并避免O(k*l)逐pair付费 | 只把已较小的远尾再压一倍；误称220倍改善即判号 |
| 3 | S76 D-sector + S79 exterior跨层一致性 | 利用同一个unitary跨层关系，支付K''+J''>=H_hat''或C_X实际预算 | 任意layer-bistochastic通道定理；只证比较shell凹 |

这三条都未闭合，且主要服务半密度。要覆盖整个(.925,1)与一般rho，须另付参数范围和真实率传递，不能隐去。

## S80的准确地位

RL01 PR71独审通过：Fisher–Burg tent、occupation dephasing互信息主控、相邻quantum MI精确dyadic telescope、R_L^q与Lambda_J c²D/(2L)、熵值极限传递；逐配置likelihood interaction ell的各阶导数界和DF=−E ell''也正确。

新贡献是精确相邻quantum telescope细化与逐word导数工具；finite-chord/rate bridge、dephasing主控继承S42/PR16，泄漏估计与S42/S64同族，gap inverse/off-block消项延续QWE02。

R_L^q=O(log L/L)不含tent面积。L=6,c=.95中点R≈.173606（浮点），而示例seed弦差/site≈.00010344，量级尚未支付。正确剩余义务是控制sum p_y'' ell_y，保留符号、边界规模、尺度可和与弦面积。不能据当前工具宣称新的局部曲率或全区间定理。

## 已暂停的做法

- 用统一逐word、逐pair、逐mixed-entry正性替代真实加权和；多处已有严格障碍。
- 不利用exterior结构的任意通道凹性；S79已经反驳。
- 将有限Toeplitz块当projection，或把count entropy、Tr b(K)当完整空间Shannon熵。
- 从熵值O(log n/n)、数值单调、拟合指数或固定n端点展开直接推熵率二阶导。
- 把超加性等同于H_n''/n逐n单调；将Dini用于未证单调/连续的对象。
- 把周期模型、单点.95或半密度中点的结果外推到全参数。
- 同一条已付冻结桥反复续费；例如QWE05/S61指定循环单侧条件信息义务已完成。

## 文献与工具去重要求

仓库已有S42准自由熵／dephasing、QWE02有限弦与真实权重远尾、S47/S77 nilpotent/Bochner、S75/QWE08偏置矩、S76/S79 exterior与second-chaos机制。提新工具前必须对这些具体接口去重。

Claude此前提到的Guerra–Toninelli、Lindeberg/Chatterjee、cavity、Cauchy可积结构、RIP、spectral/entropic independence，是迁移候选。现有归档并不证明每个文献方向都被彻底检索并实际尝试；接手者不得把“提到名称”登记为已试。尤其协方差行和不是Dobrushin sup影响，边际到全条件的桥仍要证明。

新题要列出：对象、全部量词、创造的工具、最小承重引理、进入最终弦差的公式、反例压力测试。理论优先；有价值的失败应给可复核的最小障碍，不以主观评分或重复命名作为进展。
