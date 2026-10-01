# G6 应用与范围独立核验

STATUS: CORRECT_CONDITIONAL_SCOPE
MAIN_SAMPLER_THEOREM: NOT_CERTIFIED_BY_THIS_AUDIT
PRIOR_ART_FULL_SCOPE: UNCONFIRMED
DATE: 2026-10-01 (Asia/Singapore)

## 1. 对象、隔离和结论边界

本文条件于 source §1 的 uniform-tilt covariance sampler criterion 及其明确写出的总 Borel 构造最终被证明。这里只核验其假设在 DPP 上成立、该具体构造的对称性范围，以及 source §4–5 的来源与应用。本文的 CORRECT 不得用于把 Brownian 后验、共同滤过、无限维强解或主定理记为已认证。

结论：在该条件下，任意与可数 Γ 集 W 的置换作用交换的 Hermitian 正压缩 Q 都满足应用条件；原论文明确研究的 Q7.7 情形被蕴含。进一步，带符号边作用可以通过“DPP 法则＋核绝对值窗口”直接进入判据，并得到每个固定连通可数局部有限简单图 G 上的总 Borel、全 Aut(G) 精确等变映射

\[
\Phi_G:[0,1]^{V(G)}\longrightarrow\{0,1\}^{E(G)},
\qquad (\Phi_G)_*\lambda^{V(G)}=\mathrm{FUSF}_G.
\]

等变恒等式对所有输入和所有自同构同时成立；FUSF 分布/其几乎处处支持性质是概率结论。没有断言每个异常输入都产生无有限分量的森林，也没有断言 G 变化时的联合 Borel 图因子。

## 2. 有限 DPP 外场：端点特征值不构成缺口

固定有限 F，令 K=Q_F，即实际无条件边缘的压缩核。它是 Hermitian 正压缩，因为对任何支持在 F 的向量 v，`0 <= <v,Qv> <= ||v||²`。任意正乘法外场等价于 h∈R^F，设 D=diag(exp h)，并置

\[
M=I-K+K^{1/2}DK^{1/2},\quad R=D^{1/2}K^{1/2},\quad H=RM^{-1}R^*.
\]

若 d 是 D 的最小对角元，则

\[
M\ge I+(d-1)K\ge\min(1,d)I>0,
\qquad M-R^*R=I-K\ge0.
\]

由 `M^{-1/2} R*R M^{-1/2} <= I` 可知 R M^{-1/2} 是压缩，故 `0 <= H <= I`。此处没有使用 K 或 I−K 可逆。

直接从 inclusion probabilities 展开得到有限 DPP 生成多项式

\[
g_K(z)=\mathbb E\prod_i z_i^{\eta_i}
=\det(I+(Z-I)K).
\]

外场后的生成函数为 g_K(Dz)/g_K(D)。利用 `det(I+AB)=det(I+BA)`，其分子等于

\[
\det\{I-K+K^{1/2}DZK^{1/2}\}
=\det\{M+R^*(Z-I)R\},
\]

因此商是 `det(I+(Z-I)H)`。这独立核实了原稿的外场核，包含复数核、投影、特征值 0 或 1、确定性位。

对任意这样的 H，记 p=H_xx，则

\[
\operatorname{Var}(\eta_x)=p(1-p),\qquad
\operatorname{Cov}(\eta_x,\eta_z)=-|H_{xz}|^2\quad(z\ne x).
\]

于是

\[
\sum_z|\operatorname{Cov}(\eta_x,\eta_z)|
=p(1-p)+(H^2)_{xx}-p^2
\le2p(1-p)\le\tfrac12.
\]

判据要的界因此对每个有限实际边缘、每个实外场、每一行成立。没有把有边界 Gibbs 法则替换成无条件边缘，也不需要定义任意无限外场的 DPP。

## 3. 支撑分量、有限窗口和独立性

令 D_n 的不同顶点 x,y 在 `|Q_xy| >= 1/n` 时相邻。由

\[
\sum_y|Q_{xy}|^2=\|Q\delta_x\|_2^2\le Q_{xx}\le1
\]

可知各度数至多 n²。令 E_n(x) 为 D_n 的半径 n 闭球：有限、含 x、随 n 嵌套。若 y 在 Q 非零支撑图中与 x 连通，取一条有限路径；只需 n 同时大于路径长度及所有路径边核模的倒数，该路径即落入 D_n，故 y∈E_n(x)。因此其并恰为支撑分量 C(x)。孤立点亦被覆盖。

不同分量间 Q 为零，故任意有限 inclusion determinant 按分量分解。对有限指定的 1 集 A 和 0 集 B，容斥公式

\[
\mathbb P(A\subset\eta,\ B\cap\eta=\varnothing)
=\sum_{T\subset B}(-1)^{|T|}\det Q_{A\cup T}
\]

也按分量分解。柱集生成各分量的 σ 域，故各完整分量限制联合独立。这不是仅验证两两独立。

若 Γ 的置换作用与 Q 交换，则法则、D_n、E_n 均相容。加上 §2 的 L=1/2，即满足待认证判据的全部应用假设。

## 4. FUSF 原来源及带符号作用

原始来源为 Benjamini–Lyons–Peres–Schramm, *Uniform Spanning Forests*（2001），作者 PDF 的 Theorem 7.8，第 25 页，及其后的投影写法：自由森林用闭有限循环空间的正交补投影，wired 森林用闭 star 空间投影。Theorem 7.3，第 24 页，给出二者相等与有限能量调和函数只有常数的等价条件。[作者原文](https://rdlyons.pages.iu.edu/pdf/usf.pdf)

具体在每条无向边选一个参考方向，以这些参考边为 ℓ²(E) 的正交基。局部有限性使有限支撑顶点函数的梯度属于 ℓ²(E)。置

\[
\mathcal C=\overline{\operatorname{span}\{\text{有限有向循环的带符号边向量}\}},
\qquad \mathcal S=\overline{dC_c(V)}.
\]

则 `Q_F=P_(C perp)` 给 FUSF，`Q_W=P_S` 给 WUSF。不能交换这两个核。

对于 g∈Aut(G)，存在 ε_g(e)∈{−1,1} 使

\[
U_g\delta_e=\varepsilon_g(e)\delta_{ge}.
\]

U_g 把有限循环向量送到有限循环向量，故保持 C，也保持 C 的正交补，因而 `U_g Q_F U_g* = Q_F`。这通常不是无符号置换交换关系；恰当的逐项关系为

\[
(Q_F)_{ge,gf}=\varepsilon_g(e)\varepsilon_g(f)(Q_F)_{ef}.
\]

有限主子式中的行、列符号各出现一次，行列式不变。因此 FUSF 的**无符号边占据法则**在 Aut(G) 下不变；同时核模不变，故 §3 的窗口等变。分量独立及外场协方差界仍适用。于是可直接对这个无向边法则应用采样判据，完全不必把 Q_F 错当成与无符号边作用交换的核。

这一路也没有从 WUSF-FIID 推出 FUSF-FIID；自由森林本身的投影被单独使用。

## 5. 非可数 Aut(G)：具体构造的全输入自然性

若只拿“对每个可数 Γ 存在一个 Γ 因子”的存在性黑盒，不能直接推出一个对整个 Aut(G) 等变的共同因子。source 提供了额外的具体构造，使此处可逐式核验。

对**任意**保持 µ 与窗口的置换 g、任意有限窗口 n、任意确定性场 y，有限 tilted marginal 的变量更名立即给出

\[
b^n_{t,gx}(g y)=b^n_{t,x}(y).
\]

这等式没有异常集。逐点 limsup、逐坐标 Lebesgue 时间积分、同一起始输入的 Picard 迭代、收敛极限、整数时间阈值及 liminf 都与坐标置换交换。相同单站点 Borel Brownian 编码 κ 也交换。因此，**条件于这些步骤确实构成 source §1 所述总解及采样器**，有

\[
\Phi_E(g u)=g\Phi_E(u)
\quad\text{对所有 }u\in[0,1]^E\text{ 和所有 }g\in\operatorname{Aut}(G).
\]

没有对“每个 g 的概率一事件”取不可数交；这一点由确定性恒等式解决。概率正确性使用的可数对象是 E、时间的可数确定化检查以及各分量，不是 Aut(G)。故非可数群不是这里新增的障碍。

本节仅检查具体构造的自然性，不替代主审对积分、收敛、强逆或 Brownian 法则的证明认证。

## 6. 顶点 iid 到边 iid：完整 ties/rank 核验

使用一个固定总 Borel 概率空间编码，把每个 U_v∈[0,1] 变为

\[
(A_v,B_{v,1},B_{v,2},\ldots),
\]

在 iid 输入下所有坐标均为独立 Uniform[0,1]。二进制数位拆流即可实现；固定二进制表示的约定同时处理 dyadic 数和端点，使用同一编码于每个顶点。

设 D 为所有 A_v 两两不同的输入集合。V 可数，所以 D 是 Borel、Aut(G) 不变且概率为 1。对 u∈D 及边 e={v,w}，把 e 分配给键较小的端点，例如 A_v<A_w 时令

\[
r_v(w)=1+\#\{z\in N(v):A_z<A_w\},\qquad L_e=B_{v,r_v(w)}.
\]

局部有限性保证 r_v(w) 是有限正整数；简单图保证不同归属 v 的边有不同另一端点。D 上排名无并列，故不同归属 v 的边使用不同槽；不同归属端点的槽当然不同。给定整组键 A，槽位选择是一对一的确定性选择，而 B 栈与 A 独立，所以任何有限组边标号的条件联合分布都是 Lebesgue 乘积。这给出全部边标号 iid，并且其条件分布不依赖 A。

在 D 的补集统一令所有 L_e=0。这个补集是包括任意远处键并列在内的**全局**事件，分支本身等变；因此编码 `L:[0,1]^V -> [0,1]^E` 在所有输入上 Borel 且精确 Aut(G) 等变。无需为 ties 指定不等变的外部顶点排序。

组合 `Phi_G=Phi_E o L` 即得所述顶点源结论。若 G 只有一个顶点而无边，取唯一空输出即可。没有加入有界度、传递性、可和性或 unimodularity 条件。

## 7. Q7.7 的精确蕴含与源的区别

Lyons–Thom, arXiv:1402.0969v2（2014-05-19），第 3 页允许 countable Γ-set W 上的产品源。第 25 页 Q7.7 的原句为：

> Are determinantal probability measures associated to equivariant positive contractions factors of Bernoulli shifts?

第 24 页 Theorem 7.3 / Corollary 7.4 明确展开 R(Γ) 与 R(Γ,S)=M_S(R(Γ)) 的正压缩情形；S 为有限生成集。原文给出 sofic 情形的有限依赖近似，amenable 情形的 Bernoulli 同构，并没有由近似直接得到一般 FIID。[原始 v2](https://arxiv.org/pdf/1402.0969v2)

因此待认证的普适 W 源 DPP 定理取 W=Γ，或 W=Γ×S，就覆盖原文明确展开的 Q7.7 目标。后者的图弧对应 `(g,s) -> (g,gs)` 保持左作用。令 m=|S|，把每个 U_g 的二进制位按模 m 分到 m 条流，即得 iid `V_(g,s)`。这一转换在所有输入上用统一数位约定而等变，且几乎处处给正确产品分布，所以此自由有限标签情形还得到 regular Γ 源。

不能由此宣称任意非自由 W 都可替换成 regular Γ 源。source 的反例可独立核实：Γ=F_2，H=<a> 无限，W=Γ/H，Q=pI，0<p<1。若存在 regular Γ 源因子，则 H 坐标的目标位是 H 不变且非常数的函数。H 在 Γ 索引 Bernoulli 源上的限制作用是遍历的：对有限坐标柱集，可选 h∈H 使 hK 与 K 不交，以独立性逼近一个不变事件得到其概率等于概率平方。矛盾。

这反例只否定更强的任意非自由作用 regular-source 替换；不否定 W 源定理，也不妨碍上面的自由有限标签 Q7.7 蕴含。

## 8. 审计裁决与未覆盖项

| 项目 | 本审结果 |
|---|---|
| DPP 满足所有有限正外场协方差界及独立分量窗口假设 | 核验通过，L=1/2 |
| 主采样判据本身的概率/分析证明 | 本审未认证 |
| 原 Q7.7 明确展开情形 | 被候选普适 W 源定理条件蕴含 |
| FUSF signed 边作用 | 可直接在无向占据法则上应用判据 |
| full Aut(G) 全输入等变 | 由明确构造的确定性自然性条件成立 |
| 顶点 iid → 边 iid | ties、端点、有限排名、条件独立及组合均核验通过 |
| 一般 FUSF 与 wired FUSF 区别 | 本审使用自由投影，未偷换 |
| 任意非自由作用的 regular Γ 源 | source 反例成立 |
| finitary/有限熵源/算法速率/变化随机图的联合编码 | 不在本结论内 |
| 一般 DPP / 一般 FUSF 的完整先行占位 | 未确认；见 prior01.md |
