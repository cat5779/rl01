# R16/G13 有限商极限定理独立对抗审查

STATUS: PASS

SCOPED_RESULT: RESIDUALLY_FINITE_FINITE_QUOTIENT_APPROXIMATION_CRITERION_PROVED

ASSUMPTION_SCOPE: PASS_REQUIRES_THE_EXPLICIT_TAIL_CLAUSE_IN_ITEMS_2_3

ARBITRARY_GROUP_W: NOT_PROVED

## 1. 来源与核对范围

- 冻结题面：`prompt.md`，SHA-256
  `585FF8CEE9B909D45810F8A57D928D5FC19B915ADB606B7391E20962E07A0791`。
- 被审原稿：`output.md`，SHA-256
  `8BA91B561636F817EC30AF3E7F2AE39F95985A1C7946899B7E7C53A882269D86`。
- 交叉核对的两时约化：`r15/g13/output.md`，SHA-256
  `3C5118C836C779C9CEB6FA0D1FB2927509543621EC4C56D8AC7946647E2C3CEA`；
  其独立审查为 `PASS`。
- 交叉核对的普通弱实现：`r12/g14/output.md`，SHA-256
  `A43E093553B065D9F6FA70ECD36B7F3E9652360CCF329BA1F7BD737D33A26D60`；
  其独立审查为 `PASS`。

本审查逐项核验 periodic lift、局部 birth-time 紧性、群不变性、一时 DPP
边缘、完整自然滤过鞅恒等式的 `L1` 闭合、路径支撑、局部活动、正时刻无同时
跳、时刻零，以及固定区间的极限端点律。

## 2. 总裁决

在冻结题面第 2--3 项的最后一句按其明文意图理解为**真正包含截断尾的一致
`L1` 生成元收敛**时，回传的 `PROVED` 成立。证明给出一条共同子列，其 periodic
lifts 在紧 birth-time 空间中弱收敛；极限是 `Gamma`-不变的，具有全部目标 DPP
一时边缘，并且对每个有界柱函数在完整自然滤过中满足精确生成元鞅问题。局部
活动、coordinatewise càdlàg pure birth、单坐标单跳和无同时正时刻跳也都闭合。

证明没有使用有限商之间的 projective consistency，没有使用不同区间或不同
分割之间的一致性，也没有借用群平均。它直接从每个有限商上的整条路径律取极限；
因而对每个固定区间限制极限律，所得两端点律确为动态可实现的目标端点律，并且
对角 `Gamma`-不变。这与 R15/G13 的 two-time reduction 相容，但严格只给出一个
residually finite approximation criterion，不解决任意群上的局部不变端点存在。

## 3. 第 2--3 项假设的精确边界

原稿第 4 节实际使用且足够的条件，是对每个目标柱函数 `f`（并对所考察的紧时间
区间）令

\[
b_m(t,x)=L_t^{(m)}f(x),\qquad b(t,x)=L_tf(x),
\]

存在有界、有限空间坐标依赖并在时间上连续的共同局部近似 `c_r`，使

\[
\|b-c_r\|_{L^1(dt\,\mu_t)}\longrightarrow0,
\tag{A2}
\]

以及在有限商作自然局部识别后

\[
\lim_{r\to\infty}\limsup_{m\to\infty}
\|b_m-c_r^{(m)}\|_{L^1(dt\,\mu_t^{(m)})}=0.
\tag{A3}
\]

这正是原稿式 (18)--(19)，也是后续 martingale closure 的承重输入。若题面第 2
项的“`L1` 局部生成元收敛”以及第 3 项的“includes the truncation tails needed for
martingale closure”按 (A2)--(A3) 解读，则该步骤没有增添前提：先截断，尾部由
第 3 项控制；固定截断的局部项由第 2 项识别；最后利用有限状态空间及局部 DPP
边缘收敛，把近似改成时间连续的有限柱函数。

必须明确记录：题面单独显示的

\[
\sup_m\int_0^1\!\int a_e^{(m)}\,d\mu_t^{(m)}dt<\infty
\]

只是统一 `L1` 有界，**不等于 uniform integrability**，也不能单独推出 (A3)。
例如高度为 `m`、支撑长度为 `1/m` 的非负函数具有统一 `L1` 范数但截断尾不消失。
同样，若第 2 项只被弱化成逐局部状态或依概率收敛，也不足以通过无界漂移。
所以本 `PASS` 依赖题面已经写出的 tail clause；若后续正式定理删除该从句而只保留
显示的上界，裁决必须降为 `PARTIAL/UNPROVED`。建议正式版本直接以 (A2)--(A3)
替换“includes the truncation tails”这句自然语言，以消除不同读法。

对有限支持柱函数需要的是相应有限坐标集合上所有局部生成元的 (A2)--(A3)，而
不仅是单位元 `e` 的一个均值上界。若有限商率已协变，这由单位元条件平移得到；
否则应把 coordinatewise tail condition 明写。现冻结题面第 2 项量化到每个坐标，
并在第 3 项把 tail 纳入 generator convergence，故在上述明文读法下足够。

## 4. 逐项承重核验

| 承重项 | 裁决 | 核验要点 |
|---|---|---|
| periodic lift 的定义 | PASS | `ell_m tau` 以商映射 `pi_m` 把同一商坐标复制到每个 `N_m`-陪集。它连续，像律只支撑于 `N_m`-周期路径；原稿明确没有把该周期律误认成无限体积 DPP。 |
| `Gamma`-不变性 | PASS | lift 与 `Gamma -> Q_m` 的坐标平移严格交织。`P_m` 的 `Q_m`-不变性因此给每个 lift 精确 `Gamma`-不变；坐标置换在 birth-time 乘积拓扑中连续，所以任一弱极限仍不变。 |
| 紧性与共同子列 | PASS | `B=[0,1] disjoint-union {infinity}` 被实现为 `[0,1] union {2}`，故 `B^Gamma` 对可数 `Gamma` 紧且可度量。由此一次性抽取整条路径律的共同弱收敛子列；后续没有按柱测试再次抽子列。 |
| 局部 DPP 边缘 | PASS | injectivity radius 趋无穷使任意固定有限坐标块最终无碰撞。有限 pattern 概率是有限压缩相关行列式的有限线性组合，所以核压缩的一致收敛给有限块边缘的一致总变差收敛。 |
| 单坐标 birth-time 律 | PASS | quotient pure-birth 路径给 `P_m(T_g<=t)=K_t^{(m)}(g,g)`。结合共同弱极限与一致分布函数收敛，可用 Portmanteau 夹逼恢复目标律 `K_0(g,g) delta_0 + H(g,g)dt + (1-K_1(g,g))delta_infinity`。因此每个确定正时刻无原子。原稿将这个标准夹逼压缩为一句，但结论正确。 |
| 所有一时边缘 | PASS | 对 `t>0`，有限块评价只在某坐标 birth time 等于 `t` 时不连续，而该集合在极限律下为零；连续映射定理与局部 DPP 收敛给 `mu_t`。`t=0` 单独由 `P(X_r^F != X_0^F) <= r sum H(g,g)` 及 `mu_r^F -> mu_0^F` 恢复，没有把正时刻结论错误外推到零。 |
| 无界 Borel 漂移的闭合 | PASS（按 A2--A3） | quotient 鞅恒等式先把真漂移换成共同有界局部近似；误差精确由固定一时边缘下的 `L1` 范数控制。固定近似的时间积分是 birth-time 拓扑中的连续函数，有限正时刻历史与端点评价则为极限律的 a.s. 连续函数。先取 `m` 极限、再撤去近似，即得精确目标漂移。 |
| 完整自然历史 | PASS | 正时刻有限柱评价的代数生成 `F_s`：较早评价由右连续逼近，`X_0` 由正时刻下降到零恢复。所得增量可积，故有限签名测度/单调类把恒等式扩到任意有界 `F_s` 测试。 |
| 时刻零 | PASS | 对 `h(X_r)(M_t^f-M_r^f)` 使用正时刻结果；局部 birth-time 律给 `h(X_r)->h(X_0)` 和 `f(X_r)->f(X_0)`，目标平均活动给 `[0,r]` 漂移趋零，故 `M_r^f->0` 于 `L1`。令 `r downarrow 0` 即闭合 `F_0=sigma(X_0)`。 |
| 所有柱测试同时成立 | PASS | 子列在选择 `f,s,t,G` 前已经固定。每个任意柱测试都使用同一 (A2)--(A3) 机制；无需 test-dependent diagonal extraction。有限模式指标还给出可数决定族。 |
| 路径支撑与局部活动 | PASS | 极限直接位于 birth-time 空间，所以每个坐标自动 pure birth、càdlàg 且至多跳一次。恢复一时边缘后，Tonelli 把目标平均活动原样转成极限补偿子的期望，有限期望又给路径上几乎处处有限。 |
| 无同时正时刻跳 | PASS | 对 `x_i`、`x_j`、`x_i x_j` 的已闭合鞅问题与有限变差乘积分部公式比较，公共跳计数是从零开始的非负有界递增局部鞅，故恒为零；再对可数坐标对取交。该性质不是被错误地当作弱拓扑闭性质。 |
| 固定区间端点律 | PASS | 限制同一个全局极限 `P` 到任意 `[u,v]`，即得到具有正确中间边缘与生成元的区间解，其两端点律自动对角不变。因此它属于目标 dynamically admissible endpoint set。`u,v>0` 时 lifted endpoint laws 由 a.s. 连续映射直接收敛；`u=0` 可先以 `r>0` 逼近，再用零时刻估计。 |

## 5. 是否偷用全局一致性

没有。证明只需要：

1. 每个 `m` 上已有一条完整有限商路径律；
2. 对这些路径律任取一个共同弱收敛子列；
3. 每个固定局部测试最终可在商中无碰撞地识别；
4. (A2)--(A3) 对同一子列成立。

它没有要求 `P_{m+1}` 投影到 `P_m`，没有在不同商之间构造耦合，也没有要求
不同区间的端点选择或不同 partition refinement 相容。最终所有区间端点都来自同一个
已经构造出的极限路径律；这是结论，不是被偷用的输入。

## 6. 非关键文字修正

1. 第 4 节应把题面第 2--3 项直接命名为 (A2)--(A3)，避免读者误以为显示的
   `sup L1` 上界本身就推出尾部一致可积。
2. 第 2 节由分布函数收敛得到式 (11) 时，可补两行 Portmanteau 闭集/开集夹逼；
   现有论证虽压缩，但无数学缺口。
3. 第 9 节若要逐字声称 `u=0` 的 lifted endpoint laws 也沿子列收敛，可写出有限块
   上先令 `m->infinity`、再令 `r downarrow 0` 的统一估计。端点集合非空本身已由
   `P` 的限制直接得到，因此这不影响主结论。

## 7. 可登记范围

- 有限生成 residually finite 群、给定正规子群链及题面局部核/生成元/尾部近似下的
  `Gamma`-不变 prescribed-generator 弱 pure-birth 极限：`PROVED / PASS`。
- 每个固定区间的 invariant dynamically admissible endpoint law：`PROVED`。
- 任意群上的 invariant weak process (W)：`NOT PROVED`。
- exact JO、strong/common-input realization、factor-of-iid、pathwise uniqueness：
  `NOT CLAIMED`。
- 若仅保留显示的 `sup_m L1` 均值上界而删除截断尾条件：`UNPROVED`。
- 新颖性及文献优先权：`NOT AUDITED HERE`。

