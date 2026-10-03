# 独立对抗审查

## 总裁决

- **有序 DPP 不变耦合与尖锐 dbar 界：CORRECT（限于稿件精确陈述的正则作用框架）。** `proof83.tex` 给出的折线路径确实停留在正压缩区间内；任意可数群上的有序耦合构造，其条件核、局部出生流、平均迹估计、有限范围包络、边缘识别和弱极限接口形成闭合链。未发现需要 amenability、soficity 或有限生成性的隐藏使用。
- **Fuglede--Kadison Bernoulli 支配不等式：CORRECT；Conjecture 5.7 连同逐核 optimality：INCOMPLETE。** `proof14.tex` 证明了两侧普通随机序不等式，而且适用于任意可数群的正则作用。但原猜想逐字包含 “these bounds are optimal”；稿件第 89--91 行只证明并明确解释为按所示 determinant data 的类上一致最优，未证明对每个固定非标量 `Q`，`FK(Q)` 恰为最大可支配 Bernoulli 参数且 `1-FK(I-Q)` 恰为最小上支配参数。
- **W 索引 iid 的单边缘等变 factor：CORRECT（接口复核）。** `proof01.md` 的构造给出每个固定等变正压缩核的一个全定义 Borel 等变 factor。本文对该文件作了全文接口核查；未重新逐式认证其全部随机分析细节。
- **由上述三项推出“同一 iid 输入上的联合保序 factor”：INCOMPLETE。** 三份材料没有证明这一更强命题。分别存在的 factor 不能自动合成为逐点有序的共同 factor；普通 Strassen 耦合也不自动是不变耦合或 factor coupling。

## 1. 原题语境与范围

ICM 第 5.2 节开头先固定 `Gamma` 为 sofic 群，并允许一般有限轨道的 `Gamma`-集合 `E` 来陈述相邻定理；Conjecture 5.7 本身又收窄到 `ell^2(Gamma)`，即正则作用。它逐字断言两侧普通 stochastic domination，随后还有 “and these bounds are optimal”。因此原题至少包含两个逻辑部分：支配不等式，以及两个 FK 参数对固定核的锋利性。原文还明确说该问题即使对有限群也开放。它不是关于任意 `Gamma` 集合 `W` 上所有作用的陈述。[原始 ICM 论文，Conjecture 5.7](https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf)

Lyons--Steif Theorem 5.11 在 `Z^d` 的平稳卷积核情形给出逐 `f` 的 iff：`mu_p <= P^f` 当且仅当 `p<=GM(f)`，上侧同理。因此 Theorem 5.2 的 “optimal” 是每个固定核的阈值最优，而不只是整个类上由标量核见证的一致最优。该定理还把这一阈值等价于依赖一个排序的 stronger order；后者只是交换情形的额外比较，不是 Conjecture 5.7 原题要求。[Lyons--Steif，Theorem 5.11](https://rdlyons.pages.iu.edu/pdf/dyn.pdf)

Lyons--Thom Theorem 5.1 处理有限生成 sofic 群上的**算子有序核** `Q1 <= Q2`，给出不变单调耦合；Question 7.7 单独询问 DPP 是否为 Bernoulli factor。这两个结论在原文中是不同接口。[Lyons--Thom，Theorem 5.1 与 Question 7.7](https://rdlyons.pages.iu.edu/pdf/couple-pub.pdf)

因此：`proof14.tex` 正确证明 Conjecture 5.7 的两侧支配不等式，并把群范围从该小节的 sofic 语境扩到任意可数群；但它没有证明原题随附的逐核最优阈值，故不能称完整解决 Conjecture 5.7。`proof83.tex` 的任意可数群结果是正则作用上的不变耦合及 dbar 结论；`proof01.md` 则在任意可数 `Gamma` 集合 `W` 上证明单边缘 factor。

## 2. `proof83.tex` 的承重步骤

### 2.1 折线路径与常数 1

令 `D=B-A=D_+-D_-`。稿件的

`R_k=((N-k)A+kB)/(N+1)`，`S_k=R_k+D_+/(N+1)`

满足 `0<=R_k<=N I/(N+1)`、`0<=S_k<=I`，而相邻差分别为正算子 `D_+/(N+1)` 与 `D_-/(N+1)`。故每段都可使用有序耦合，路径总成本趋于 `tau|A-B|`。这里没有把不交换的正负部分误当成与 `A,B` 对易；也没有使用迹范数对压缩与乘积的错误交换。`A=0,B=pI` 确认常数 1 一致最优。

### 2.2 条件核与平均迹

谱隙下，`Q_RR-P_{R\x}` 经符号算子左乘后具有至少 `epsilon I` 的厄米部分，因而可逆且逆范数至多 `epsilon^{-1}`。有限条件化、强收敛及一致逆界给出的全外部条件核是合法版本；逐点条件化保持双侧谱隙，故有限精确模式概率有统一正下界。

对 `X subset Y`，逆差恒等式给出

`G_X-G_Y=G_X P_{Y\X} G_Y`。

在不变联合律下，“期望的原点对角元”对协变有界随机算子是迹。由极分解和压缩迹估计得到 `E|G_X-G_Y|(e,e)<=epsilon^{-2}p`。随后只在有限 `S` 上压缩，并使用 `Tr|P_S Z P_S|<=Tr(P_S|Z|P_S)`；稿件没有对失去协变性的删点算子直接套原点迹。这一非交换步骤方向正确。

### 2.3 出生流、存在唯一性与极限

有限布尔格上，秩一正扰动的导数向量位于有向边散度锥；固定多面体三角剖分和顶点原像给出连续分片仿射选择。谱隙给出配置概率下界，因此流除以概率后仍一致有界且 Lipschitz。

有限范围上下包络直接对完整更新值取极值，正确处理了“已占据点速率为零”。反向依赖图的阶乘界保证有限查询在有限时刻几乎处处只依赖有限输入。平均振荡估计闭合 Gronwall；再以“先固定半径令有限集穷尽、后令半径趋于无穷”的顺序识别边缘。该顺序不可互换，稿件已明确遵守。

最后 Kaplansky 逼近同时控制列算子及伴随，构造 `A_n=U_n^*U_n <= B_n=A_n+W_n^*W_n <=I`。端点耦合的弱极限保留两边缘、不变性和闭的包含关系；无需在极限中保留速率常数或整条路径。

### 2.4 精确范围

该证明直接覆盖 `ell^2(Gamma)` 的正则作用。它没有证明任意作用 `Gamma curvearrowright W` 上相应 dbar 定理；矩阵放大或准传递作用需要另写陈述并核对归一化迹。稿件保证在 `A<=B` 时有逐核等号 `dbar(P^A,P^B)=tau(B-A)`；它不声称一般核对取等，也不声称“取等当且仅当有序”。一般核对只证明上界。常数 1 是类上一致锋利，不是声称每个固定非标量核对都取等。

一般核对普遍取等确实为假。取 `Gamma=Z/2`，在正则基下令

`A=[[1/2,1/4],[1/4,1/2]]`，`B=[[1/2,-1/4],[-1/4,1/2]]`。

两者都是与左平移交换的循环矩阵，谱均为 `{1/4,3/4}`，故为等变正压缩。二者的一阶主子式都为 `1/2`，二阶主子式都为 `1/4-1/16=3/16`，所以全部包含概率相同，DPP 法律相同，因而 `dbar(P^A,P^B)=0`。另一方面，`A-B=[[0,1/2],[1/2,0]]` 的两个奇异值均为 `1/2`，归一化迹给出 `tau|A-B|=1/2`。这只否定一般核对的普遍等号，不影响上界。

## 3. `proof14.tex` 的承重步骤

有限维引理是正确的。对任意函数，以包含事件指标为线性基，确有

`d/ds E^{K+s(I-rK)}f|_0 = sum_i E[(1-r q_i) Delta_i f]`。

L-ensemble 的 Schur 补给出 `q_i(A)>=1/(K^{-1})_{ii}`，所以在 `r>=max_i(K^{-1})_{ii}` 时，对递增 `f` 导数非正。

FK 等值路径 `K_t=a_t(Q+tI)` 满足

`K'_t=a_t(I-tau(K_t^{-1})K_t)`。

对有限柱集 `V`，逆压缩不等式给出 `((K_t)_V^{-1})_{ii}<=tau(K_t^{-1})`；等号中的常数对角元只使用正则作用下的等变性。因此有限维引理逐柱函数适用。正则化 `Q_eta=(Q+eta I)/(1+2eta)` 后，FK 由单调收敛趋于原值，有限模式概率由矩阵元连续性收敛。补集核 `I-Q` 给出上界。端点处理正确。

稿件最后用 `Q=pI` 证明按 determinant data 的**类上一致锋利**。这没有证明对每个固定非标量 `Q` 的 iff 阈值

`P^{qI} <= P^Q iff q<=FK(Q)`，以及 `P^Q <= P^{qI} iff q>=1-FK(I-Q)`。

Lyons--Steif Theorem 5.11 在交换卷积核情形证明的正是这种逐核 iff。故 `proof14.tex` 对完整原猜想（含 optimality）的裁决是 **INCOMPLETE**，缺口仅在逐核必要性，不在两侧支配不等式。

### 一个必须保留的接口反例

FK 路径不能直接套 `proof83.tex` 的“有序核”定理。取二点循环群上的等变核，其两个傅里叶特征值为 `0.2,0.8`。在 `t=0`，

`tau(Q^{-1})=(5+1.25)/2=3.125`，

故切向方向 `I-tau(Q^{-1})Q` 的两个特征值为 `0.375` 与 `-1.5`，是不定的。于是相邻路径核既非单调增加也非单调减少。`proof14.tex` 成功之处正是另证了测度导数符号，而非假装存在 Loewner 有序路径。

## 4. factor 与联合耦合接口

`proof01.md` 为每个固定 `Q` 从 `W` 索引 iid Uniform 构造等变 factor；其图分量分解、有限倾斜的一致 Lipschitz 界、全输入 Picard 解以及同噪声时间极限，为单边缘结论提供了接口。

但若分别把该构造用于 `Q_1,Q_2`，文中没有证明输出满足 `F_{Q_1}(u)<=F_{Q_2}(u)`；漂移对核参数的单调性也未建立。另一方面，`proof14.tex` 给出的普通随机序只保证某个 Strassen 单调耦合，既不自动保证该耦合不变，也不自动保证它是 iid 的等变 factor。因此以下两个独立的更强升级均为 **INCOMPLETE**：

1. 从 FK Bernoulli 支配得到不变单调联合律；
2. 从两个单边缘 factor 得到同一 iid 输入上的逐点保序 factor；

这些不是对 Conjecture 5.7 的反例，也不削弱 `proof14.tex` 已证明的普通随机序结论。Lyons--Steif 的 strong domination 仅用于解释交换情形的更强已知结论；它不是 Conjecture 5.7 的要求，也不计入本稿的缺口。

## 5. 分项裁决

| 项目 | 裁决 | 说明 |
|---|---|---|
| 正则轨道、任意可数群的有序核不变耦合 | CORRECT | `proof83.tex` 自包含构造闭合 |
| 任意作用 `Gamma curvearrowright W` 的同类 dbar/FK 结论 | INCOMPLETE | 未由两份核心稿陈述或证明 |
| 每一对有序核存在不变单调耦合 | CORRECT | 每对分别存在；不要求全体核的共同可测选择 |
| 全核族上的共同/可测单调选择 | INCOMPLETE | 稿件没有此量词，原结论也不需要 |
| Conjecture 5.7 的两侧普通随机序不等式 | CORRECT | `proof14.tex` 逐柱函数证明；群范围还强于原文 sofic 小节语境 |
| Conjecture 5.7 的逐固定核 FK 最优阈值 | INCOMPLETE | 标量核只证类上一致锋利，未证非标量 `Q` 的 iff 必要性 |
| 单边缘等变 factor | CORRECT | `proof01.md` 的精确结论 |
| 联合保序 factor | INCOMPLETE | 缺少共同噪声下的核参数单调性 |
| 条件核/出生过程路径存在与边缘唯一识别 | CORRECT | 唯一性只用于有限链 ODE 与确定性积分方程，未偷用一般无限前向方程唯一性 |
| 压缩、逆差与迹范数估计 | CORRECT | 非交换次序与协变性使用均合法 |
| 极限保留边缘、不变性、包含关系 | CORRECT | 由有限行列式、弱闭性与闭支撑集合得到 |
| dbar 对一般核对普遍取等 | INCORRECT | 二点例有相同 DPP，故 dbar 为 0，而 `tau|A-B|=1/2`；稿件只保证有序对取等，不作 iff 声明 |
| FK 路径直接套有序核定理 | INCORRECT | 二点显式不定切向量反例见上 |
| ICM Conjecture 5.7 完整原题（含 “these bounds are optimal”） | INCOMPLETE | 支配部分通过；逐核 optimality 未证 |
