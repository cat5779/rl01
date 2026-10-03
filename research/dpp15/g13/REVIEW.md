# R15/G13 完整原稿独立对抗审查

STATUS: PASS

SCOPED_RESULT: LOCAL_TWO_TIME_FIXED_POINT_EQUIVALENCE_PROVED

GLOBAL_ARBITRARY_GROUP_W: INCOMPLETE

## 1. 来源与完整性

- 冻结题面：`prompt.md`，SHA-256
  `DF991DAB305E27AEE02080DF48F6E8EFE568F10FCA97D526A8BBBDE196BC77F5`。
- 审查原稿：`output.md`，11,981 字节、11,957 个 Unicode 字符、372 个物理行，
  SHA-256
  `3C5118C836C779C9CEB6FA0D1FB2927509543621EC4C56D8AC7946647E2C3CEA`。
- 原稿是完整正文，不是 20,000 字符读取上限所得节选；末尾含有完整 iff 收束、
  独立选择说明及作用域限制，并满足题面“不超过 18,000 字符”的约束。

本审查逐段与 R14/G13 的可见节选、R14 的 scoped audit、R13/G13 的缺口审查及
R12/G14 的 ordinary weak realization 闭性论证交叉核对。R13 指出的时刻零、
共同跳、拼接共同满测集等缺口，在本稿中均有实质补证。

## 2. 总裁决

回传的 `PROVED` 在冻结范围内成立。它证明的是下述精确等价：存在全局
`Gamma`-不变 prescribed-generator 弱路径律，当且仅当在某一列网格趋零的有限
分割上，每个相邻区间的**动态可实现**两端点律集合
`E_{u,v}` 含有一个对角 `Gamma`-不变元。不同单元及不同细分层的端点选择可以
彼此独立，不需要 projective consistency。

充分性链条闭合：区间解在共同共零集上解体并拼接为真实解；不变端点核给出不变
网格骨架；精确等变的 canonical interpolation 与真实出生时刻的距离至多网格
宽度；紧 birth-time 空间中的共同弱极限因此不变；固定边缘的
`L1(dt mu_t)` 近似闭合仅 Borel、全局无界的漂移；最后补齐时刻零自然历史并从
极限鞅问题重新推出无同时正时刻跳。

证明没有使用群平均、amenability、端点唯一性、跨网格一致性、强解或因子结构。
它也没有证明任意群上局部不变端点元总存在。因此一般的 arbitrary-group (W)
仍为 `INCOMPLETE`；本结果是一个严格保留动态可实现性条件的等价约化，不是 (W)
本身的正面解决。

## 3. 逐项承重核验

| 承重项 | 裁决 | 对抗核验 |
|---|---|---|
| 必要性与量词 | PASS | 全局不变解限制到任意 `[u,v]` 仍是 prescribed-generator 区间解，且两端点律对角不变，所以必要性甚至对每个分割成立。充分性只使用“存在一列 mesh 趋零的分割”；每格、每层独立选择，未偷换为相容选择。 |
| 同一共零集上的 disintegration | PASS | 对每段先按左端状态解体。初态、coordinatewise càdlàg pure-birth 支撑、每坐标补偿子可积性，以及由有限模式指标、稠密时间和过去柱事件组成的可数鞅决定族被同时放到一个左边缘共零 Borel 集 `D_k` 上。稠密时间恒等式先以单调类扩到完整相应历史，再用路径右连续和漂移的 `L1` 小区间连续性扩到任意 `s<t`。 |
| 段拼接与网格边界 | PASS | Ionescu--Tulcea 拼接在每个左边缘仍输入精确的 `mu_{t_{k-1}}`，故几乎必然落入 `D_k`，每段无条件律精确恢复为原 `P_k`，从而全部一时边缘保留。式 (6) 对“旧过去 × 当前段历史”写出塔式条件期望；跨格增量逐格分解。线性对角边缘给每坐标在任一正确定时刻无出生原子，可数并后排除任何正网格边界跳。 |
| 不变网格骨架 | PASS | 不变端点律与不变第一边缘的正则条件分布唯一性给 `Q_k(gx,gA)=Q_k(x,A)` 的边缘几乎处处版本。群和状态决定代数可数，能够同时选版本；逐层输入始终是对应 `mu`，所以 Markov 乘积骨架确实不变。这里不要求完整区间条件律 `R_k` 等变。 |
| canonical interpolation 与 mesh coupling | PASS | birth-time 空间 `B^I`（`B=[0,1]` 加孤立 `infinity`）紧且可度量。由单调骨架取“首次占据网格时刻”的规则逐点与坐标置换交换，故像律精确不变。用真实路径及其自身骨架耦合时，有限出生只向右移到所在格右端，`0` 与 `infinity` 不动；加权乘积距离逐路径不超过 mesh，因此 Prokhorov 距离同样受控。 |
| 不变性传到共同极限 | PASS | 先从真实解律 `P_n` 抽取一条与任何测试无关的共同弱收敛子列；mesh coupling 迫使对应不变插值律收敛到同一极限。坐标置换在 birth-time 乘积拓扑中连续，故不变概率律集合弱闭。无跨层一致性也无群平均。 |
| 全部一时 DPP 边缘含 `t=0` | PASS | 每个 `P_n` 的单坐标 birth-time 律完全相同，连续坐标投影把该律传到极限，因而每个正确定时刻无原子。正时刻有限块评价于是为极限律的几乎处处连续映射，联合 DPP 边缘传递。`t=0` 没有误用评价连续性，而是以 `P(X_r^F != X_0^F) <= r sum H(ii)` 及有限压缩 DPP 概率随 `K_r` 连续单独恢复。 |
| Borel 全局无界率的闭性 | PASS | 对柱函数 `f`，漂移 `b_f=L_t f` 由逐坐标活动假设属于 `L1(rho)`，`rho=dt mu_t`。时间连续、空间有限坐标的有界函数在该 `L1` 中稠密；所有近似律和极限律具有同一固定一时边缘，所以路径积分近似误差统一且精确等于相应 `L1(rho)` 误差。对连续柱近似，时间积分在 birth-time 拓扑下连续；端点与有限正时刻历史评价在极限律下几乎处处连续。故先弱收敛、后撤去近似即可恢复真漂移，不需有界率或额外子列。 |
| 正时刻完整自然历史 | PASS | 正时刻有限历史乘积测试上的恒等式先成立。对固定 `s>0`，`X_s` 与 `s` 前正有理时刻评价生成 `F_s`：任意较早评价由右侧有理时刻逼近，`X_0` 由正时刻下降到零恢复。有限签名测度/单调类因此扩到所有有界 `F_s` 测试。 |
| `r downarrow 0` | PASS | 对 `h(X_r)(M_t^f-M_r^f)` 使用正时刻结果。birth-time 路径右连续给 `h(X_r)->h(X_0)`、`f(X_r)->f(X_0)`；固定边缘 `L1` 可积性使 `[0,r]` 漂移趋零，故 `M_r^f->0` 于 `L1`。支配收敛与单调类随即给完整 `F_0=sigma(X_0)` 鞅恒等式。 |
| 同一个法律满足全部柱测试 | PASS | 有限模式指标为可数决定族，并在每个有限坐标块线性张成全部有界函数。共同子列早于任何 `f,s,t,G` 选定，后续每个测试使用同一固定边缘误差控制；没有 test-dependent diagonal subsequence。 |
| pure-birth/càdlàg 路径支撑 | PASS | 极限直接取在 birth-time 乘积空间，故每个样本的每坐标至多一个出生且 coordinatewise càdlàg。任意可和乘积度量下的全路径 càdlàg 性由坐标逐点极限与权重支配收敛得到，不是依赖一个未证的路径子集弱闭性。 |
| 从极限鞅问题重证无同时跳 | PASS | 对 `x_i,x_j,x_i x_j` 的已闭合鞅问题与有限变差乘积分部公式比较，公共跳计数 `S_ij=sum Delta X_i Delta X_j` 等于三个局部鞅的组合，故本身为局部鞅；它又非负、递增、从零开始且有界于 1，因此恒为零。对可数坐标对取交即排除任意同时正时刻跳。该性质没有被错误地当作 birth-time 弱拓扑下的闭性质。 |

## 4. 对抗性边界与非关键文字事项

1. 第 7 节写 `L_t x_i=a_i` 以及
   `L_t(x_i x_j)=a_i x_j+a_j x_i` 时使用了项目中一贯的 pure-birth
   规范化 `a_i(t,x)=0` 于 `x_i=1`。若把“birth rate”理解为在已占据状态仍可
   任意赋值，则应全文将这里的 `a_i` 写成有效率
   `(1-x_i)a_i`；这只是对生成元无影响的规范化，不改变证明或结论，但正式独立
   版本宜补一句。
2. `D_k` 的支撑清单显式列出 pure-birth/càdlàg/单坐标单跳，没有单列区间内
   “无同时跳”。这不造成缺口：每个被选的 `P_k` 本来就是 ordinary solution，
   拼接后每段无条件律仍精确等于 `P_k`，而正网格边界根本无跳；如需让“路径
   支撑”清单完全逐字覆盖 ordinary 定义，可把这一概率一事件也加入同一个可数
   共零集。
3. 第 7 节式 (33) 中的有界可预测随机积分可以明确说明先作 localization。
   这里 `X_i,X_j` 有界、每坐标补偿子期望有限，相关积分实际为真鞅；即便只按
   局部鞅使用，非负递增且有界的 `S_ij` 也足以推出恒零。
4. 证明没有提出 endpoint-law uniqueness 推论，因而不存在 R13 所警告的
   “strictly weaker” 未获严格分离问题。

这些都是规范化或可读性增强，不需要新增数学假设，也不降低 `PASS`。

## 5. 可登记范围

- local two-time invariant endpoint fixed-point reduction：
  `PROVED / CORRECT_SCOPED`。
- 每格、每层独立端点选择且无需 projective consistency：`PROVED`。
- 固定边缘、完整自然滤过柱鞅问题、逐坐标 pure birth、无同时正时刻跳：
  `PROVED`。
- arbitrary-group 局部端点不变元的存在：`NOT PROVED`。
- 一般 exact JO / 全局不变弱过程 (W)：`INCOMPLETE`，除非另行闭合每个所需
  小区间的动态端点固定点。
- strong/Poisson common-input realization、factor-of-iid、pathwise uniqueness：
  `NOT CLAIMED`。
- 新颖性与文献优先权：`NOT AUDITED HERE`。

