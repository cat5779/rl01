# S79 Cycle31 独立数学审查

审查日期：2026-09-20（Asia/Singapore）

## 总裁决

**`VISIBLE_SECTIONS_1_TO_10_REVIEWED / CORE_IDENTITIES_CORRECT / ARBITRARY_LAYER_BISTOCHASTIC_CONCAVITY_DISPROVED / ACTUAL_EXTERIOR_AND_SINE_TARGET_OPEN`。**

S79 的主要新计算是正确的：posterior/Boolean number identity、orientation-path 曲率、半密度中点的完整 (a)-方向 likelihood acceleration、真实 shell postprocessing、shell KL covariance/Jeffreys budget、exterior deletion intertwining、consecutive-Fourier Cauchy full-minor 性质，以及 total-shell 的 Shepp--Olkin 路线都能独立闭合。

作者的 (m=36,c=4/5) 通道反例也成立。本审查以独立 outward-rounded Decimal 实现得到

\[
H''\in[
10.474531138473981378185269240027167830874956427446392482274615847117374463338362,
10.474531138473981378185269240027167830874956427446392482274615847117374463482445
],
\]

并得到相对完全 shell randomizer 的严格差

\[
H''-H_\circ''\in[
304.77031674788825454132673313368192637138736454619470398695323098304905790126064,
304.77031674788825454132673313368192637138736454619470398695323098304905790144688
].
\]

因此以下两个普遍命题被严格证伪：

1. 每层双随机、保持 Hamming layer 的任意通道在该中点方向都熵凹；
2. 对所有这类任意通道，shell KL covariance 总能由相邻边 Jeffreys 损失支付。

反例是把不同 layer 的合法 bistochastic 块人为拼成的 hybrid。它不是同一个 unitary 的 exterior powers，不是 consecutive-Fourier 通道，也不是 true sine 模型。因此它**没有**证伪 actual exterior-unitary 或 sine 目标。

两处表述需要降格。第一，反例只说明 S79 列出的逐层条件不够，不能推出“所有不显式使用跨层 exterior coherence 的推理都失败”。更强的单层结构条件仍可能排除该 hybrid。第二，

\[
K''+J''\ge0
\]

只是推出实际熵凹性的方便充分条件，而且比精确所需条件更强；不能称为等价 reduction。可见稿在最终 ledger 中截断，所以本审查不声称读过完整手稿。

## 分项裁决

| 对象 | 裁决 | 说明 |
|---|---|---|
| posterior/Boolean number identity | **CORRECT** | (N_y\Lambda=k\partial_k\Lambda)，系数与符号正确 |
| orientation-path (C_X) | **CORRECT** | score、acceleration、输入曲率和 covariance 项一致 |
| full (a)-path acceleration | **CORRECT_AT_MIDPOINT** | (4/r) 系数正确；不是任意 (a) 的全局公式 |
| shell randomizer 是真实 postprocessing | **CORRECT** | (WW_\circ=W_\circ)，而非仅 matching marginals |
| shell KL covariance identity | **CORRECT** | 条件 KL (j_W) 给出精确 covariance 差 |
| Jeffreys shell budget | **CORRECT** | 逐边双向 data processing 给 (mathcal E_W-\mathcal E_\circ\ge0) |
| arbitrary layer-bistochastic 中点总凹性 | **DISPROVED** | (m=36,c=4/5) 严格正区间反例 |
| arbitrary layer-bistochastic paid-shell | **DISPROVED** | 曲率减壳基线严格为正 |
| 反例延伸到 exterior/sine | **NOT ESTABLISHED** | hybrid 不满足跨层 exterior consistency |
| “全部 layer-independent 论证失败” | **GAP / OVERCLAIM** | 只排除仅依赖已列逐层假设的论证 |
| deletion intertwining | **CORRECT** | 维数、方向、(1/n) 归一和 cofactor 求和正确 |
| consecutive-Fourier full-minor positivity | **CORRECT** | Cauchy 公式条件完整；Jacobi 补余 minor 使用正确 |
| total-shell Bernoulli 表示 | **CORRECT** | pgf、熵分解和二阶差分归一正确 |
| Shepp--Olkin 使用 | **CORRECT_WITH_ATTRIBUTION_FIX** | 应归因于 Hillion--Johnson 2017 完整证明 |
| (K''+J''\ge0) 是等价 reduction | **GAP** | 它是严格更强的充分条件 |
| 作者脚本 | **REPLAYED_EXIT_0** | 安全检查后原样重跑；有限表与严格反例复现 |
| actual consecutive-Fourier all-size 结论 | **OPEN** | paid-shell 和 (K'') 均未闭合 |
| true sine entropy-rate concavity | **OPEN** | 还缺有限体到 rate 的二阶桥及一般参数处理 |

## 1. 审查范围与冻结前提

收到的可见稿共 958 行。第 1--10 节完整，最终 ledger 在句中截断。因此下文只裁决可见内容；没有推测缺失尾部可能加入的限定。

本轮只继承 PR66/S76 明确建立的有限模型边界：半密度中点 pair source、保持 layer 的通道、Boolean number calculus 和 compensated curvature identities。未继承任何“实际 sine 已证”“all-size exterior 已证”或“finite cyclic 可直接求导到 rate”的结论。

沿用 S79 记号：(Y) 是可见 source 字，(Z) 是送入 layer channel 的字，(T) 是通道输出，(Lambda(y,t)) 是相对均匀参考的 likelihood，(X=|Y|+|T|-m)，而 (delta(y,t)) 是 posterior equal-pair count 的条件均值。所有本节导数均在半密度对称中点 (a_0) 评价。

## 2. Posterior 与 Boolean number identity

在 (y) 的 Walsh 展开中，每个 degree-(d) 项恰带 (k^d)。因此 Boolean number operator 满足

\[
N_y\Lambda=k\partial_k\Lambda.
\]

从输入 likelihood 的 (k)-score 逐项条件化到输出得到

\[
\frac{N_y\Lambda}{\Lambda}
=\frac{km}{1+k}-\frac{2k}{1-k^2}\,\delta.
\]

解出 posterior 统计量即

\[
\delta\Lambda=2mr\Lambda-\beta N_y\Lambda,
\qquad
\beta=\frac{1-k^2}{2k}.
\]

这里没有用“把 posterior 均值替换成其 layer 均值”的近似；(delta(y,t)) 的完整输出依赖被保留。独立 (m=3) 有理数通道检查的恒等式残差精确为 0。

## 3. Orientation path 与完整 (a)-方向曲率

对 orientation 扰动，把每对中两个有向 atom 的概率写成 (r+\theta) 与 (r-\theta)。在 (	heta=0)，输入 score 和 acceleration 分别为

\[
S_\theta=\frac Xr,
\qquad
A_\theta=\frac{X^2-D}{r^2}.
\]

通道保持 Hamming layer，故 (|Z|=|T|)，从而

\[
X=|Y|+|Z|-m=|Y|+|T|-m
\]

是输出可测量。条件化给出

\[
\dot\Lambda=\frac Xr\Lambda,
\qquad
\ddot\Lambda=\frac{X^2-\delta}{r^2}\Lambda.
\]

于是 orientation 曲率为

\[
H_{\rm orient}''
=-\frac1{r^2}\operatorname{Cov}(X^2,\log\Lambda)
-\frac\beta{r^2}\mathcal E_W
-\frac{2m}{r}.
\]

最后一项确为输入 orientation entropy curvature：条件于 (D) 时 (mathbb E[X^2-D\mid D]=0)，没有漏掉 posterior fluctuation。

把上一节 posterior identity 代回 S76 的实际 (a)-path acceleration，得到

\[
\Lambda_{aa}
=\frac{X^2-2mr}{r^2}\Lambda+\frac4rN_y\Lambda.
\]

所以 (4/r) 系数正确。必须保留限定：这是**实际 (a)-方向在对称中点的完整二阶式**，不是声称对所有 (a) 都保持相同形式。

## 4. 完全 shell randomizer 与 paid-shell 恒等式

定义

\[
W_\circ(z,t)=\frac{\mathbf 1\{|z|=|t|\}}{\binom m{|t|}}.
\]

对任意 layer-preserving bistochastic (W)，采用“行是输入 (z)、列是输出 (t)”约定，直接求和给

\[
WW_\circ=W_\circ.
\]

所以 (Q_\circ) 确实是 (Q_W) 的随机后处理，不只是具有相同的 ((Y,|T|)) marginal。所有这类 (W) 的

\[
\mu=\mathcal L(Y,N),\qquad N=|T|,
\]

相同。令 (q_W(\cdot\mid Y,N)) 是 shell 内条件律，(u_N) 是该 shell 的均匀律，并记

\[
j_W(Y,N)=D(q_W\Vert u_N).
\]

则

\[
\mathbb E_{Q_W}[\log\Lambda_W\mid Y,N]
=\log\Lambda_\circ+j_W.
\]

因此实际与 shell 的 covariance 差精确等于

\[
\operatorname{Cov}_\mu(X^2,j_W).
\]

另一方面，每条相邻 (y)-edge 的两个 KL 方向都在 postprocessing 下收缩，所以

\[
\Delta\mathcal E
:=\mathcal E_W-\mathcal E_\circ\ge0.
\]

注意这里的 (Delta\mathcal E) 定义方向与早先 S76 中“identity 减 channel”的记号不同；S79 在本节已重新定义，公式内部一致。综合两项得到

\[
H_W''-H_\circ''
=\frac{-\operatorname{Cov}_\mu(X^2,j_W)-4r\Delta\mathcal E}{r^2}.
\]

故 S79 的 paid-shell 条件

\[
-\operatorname{Cov}_\mu(X^2,j_W)
\le4r\Delta\mathcal E
\tag{F-PS}
\]

是 (H_W''\le H_\circ'') 的精确条件。此处“精确”只比较 (W) 与 shell baseline；它没有自动证明 (H_\circ''\le0)，也不等于最终 actual-exterior 定理。

## 5. 粗通用界真正说明了什么

S79 计算

\[
\operatorname{Var}_\mu(X^2)
=2mr+(8m^2-12m)r^2
\]

正确。又因 (0\le j_W\le m\log2)，有

\[
\operatorname{Var}(j_W)\le\frac{(m\log2)^2}{4}.
\]

Cauchy--Schwarz 给出的 covariance 上界因此可达 (O(m^2))，而可用 Jeffreys budget 只有 (O(m))。这严谨地说明：仅靠该 range/variance 估计会损失一个 (m) 的幂。

它不严谨地推出“任何 hypercontractive 思路”或“任何 layer-independent 思路”都必败。若某个更强的单层假设直接约束 (j_W) 的二阶混沌投影，它可能排除反例而无需显式写跨层关系。合法结论应缩为：**仅依赖 layer bistochasticity、complement symmetry 及上述粗 moment/range 数据的普遍证明不可能成立。**

## 6. (m=36,c=4/5) 严格反例及其作用域

作者通道在某些 Hamming layers 取 identity，在其余 layers 取 full mixing；每一块分别都是双随机的，并保持 complement symmetry。作者高精度程序给出严格正曲率区间，本审查用不同的 Decimal/outward-rounding 实现独立复现。

独立实现还直接算出 shell baseline 严格为负，且 (H_W''-H_\circ'') 的整个区间严格为正。因此 (F-PS) 对该通道确实失败，并非从两个普通浮点数的差猜测符号。

这个反例证明：

- 任意 layer-bistochastic 类过大；
- 逐层合法不保证跨层二阶曲率相容；
- 仅把 S76 的 (D)-sector payment 与一个无结构的 (C_X) 粗界拼接不能闭合。

它不证明：

- exterior powers (W_n=|\wedge^nU|^2) 中存在同样反例；
- consecutive-Fourier family 中存在同样反例；
- true sine entropy rate 不凹；
- 一切没有显式交叉引用相邻 layer 的论证都不可能成功。

作者输出的 `-Cov=6.1305...`、`4rDeltaE=3.6618...`、`gap=2.4686...` 是有用的机制诊断，但各自属于普通浮点；本审查只把总曲率与 shell 曲率差的 outward intervals 称为严格证书。

## 7. Exterior deletion intertwining

令 (W_n(A,B)=|\det U_{A,B}|^2)，其中行列都索引 (n)-子集。删除核采用

\[
D_n(A,C)=\frac1n\mathbf 1\{C\subset A\},
\]

行索引 (n)-subset，列索引 ((n-1))-subset。因此 (W_nD_n) 与 (D_nW_{n-1}) 都从 (n)-layer 映到 ((n-1))-layer，矩阵方向一致。

固定 (A,C) 后，左侧对新增 column (j\notin C) 求和。用 Laplace 展开 minor，再用 (U) 的行正交性消去交叉项，结果等于右侧对删除 row (i\in A) 的 cofactor 平方和。两边共同的 (1/n) 正是均匀删除归一，故

\[
W_nD_n=D_nW_{n-1}.
\]

本审查以 (m=4) permutation unitary 做了精确有理数索引检查。S79 的任意-layer hybrid 在 (n=16) 取 (W_{16}=I)、(W_{15}=W_\circ) 时立刻破坏该式：选 (C\not\subset A)，左边为 0，右边为 (1/\binom{36}{15}>0)。这准确定位了反例缺少的跨层 exterior coherence。

## 8. Consecutive Fourier 的 full-minor 性质

对 consecutive Fourier 子矩阵提取行列相位后，minor 化为 Cauchy 型行列式。相应变量 (x_a,y_b) 两两不同，且 (x_ay_b\ne1)，所以 Cauchy determinant 公式的分子、分母都非零；每个方形 minor 都严格非零。

对 unitary 使用 Jacobi complementary-minor identity 还得到互补 minor 的绝对值相等。这些结论正确地区分了 actual consecutive-Fourier family 与 hybrid 反例。

但 full spark、complement symmetry 和 deletion intertwining 本身都没有给出 (F-PS) 的符号；它们是下一步证明允许使用的结构输入，不是已经完成的 payment。

## 9. Total-shell entropy 与 Shepp--Olkin

令

\[
S=|Y|+|T|=|Y|+|Z|.
\]

每个 pair 对 (S) 的生成函数是

\[
(1-a+ax)(1-a-c+(a+c)x),
\]

所以 (S) 与 (m) 个参数 (a) 和 (m) 个参数 (a+c) 的独立 Bernoulli 变量之和同分布。沿 (a\in(0,1-c)) 两组参数都作 affine slope (+1) 运动，Hillion--Johnson 2017 的完整 Shepp--Olkin 定理适用，给 (H(S)''\le0)。

若在给定 (S=j) 后把全部 (2m)-bit 配置均匀化，记所得熵为

\[
\widehat H=H(S)+\mathbb E\log\binom{2m}{S}.
\]

对 (f(j)=\log\binom{2m}{j})，独立 Bernoulli 参数的二阶导公式为

\[
\frac{d^2}{da^2}\mathbb Ef(S)
=\sum_{i\ne j}\mathbb E\,\Delta^2 f(S^{\setminus\{i,j\}}).
\]

并且

\[
\Delta^2f(t)\le2\log\frac m{m+1}.
\]

有 (2m(2m-1)) 个有序 pair，故

\[
\widehat H''
\le-4m(2m-1)\log(1+1/m)<0.
\]

按 (2m) 个 sites 归一后右侧趋于 (-4)，常数和 ordered-pair 计数正确。

来源表述应写成“2017 年 Hillion--Johnson 证明的 Shepp--Olkin 猜想”。1981 年 Shepp--Olkin 原文是猜想来源及特例结果，不能被误写为完整一般定理的证明来源。

## 10. 三种熵与逻辑强度

必须区分：

- (H_U)：实际 consecutive-Fourier exterior channel 的输出熵；
- (H_\circ)：保留完整 ((Y,N)) law，只把 (T) 在其 (|T|=N) shell 内均匀化；
- (widehat H)：只保留 total count (S=|Y|+|T|)，再在全部 (2m)-bit 配置中按 (S) 均匀化。

定义值层 gap

\[
J=H_\circ-H_U=D(Q_U\Vert Q_\circ),
\qquad
K=\widehat H-H_\circ=D(Q_\circ\Vert\widehat Q).
\]

虽然 (J,K\ge0)，值非负不推出 (J''\ge0) 或 (K''\ge0)。精确恒等式是

\[
H_U''=\widehat H''-(K''+J'').
\]

所以实际凹性的精确条件为

\[
H_U''\le0
\quad\Longleftrightarrow\quad
K''+J''\ge\widehat H''.
\]

由于 (widehat H''<0)，要求 (K''+J''\ge0) 是更强的充分条件，不是等价 reduction。再分别要求 (K''\ge0,J''\ge0) 更强。

(F-PS) 只给 (J''\ge0)，它自身已经是相对最终目标更强的 structure-specific 条件；即使证明，也仍需 (K'') 或一个允许二者互相补偿的 combined estimate。

## 11. 精确剩余义务与最小下一接口

### 仍然开放

1. 对实际 consecutive-Fourier (U_m)，证明或反驳 all-size 的 (F-PS)：

   \[
   -\operatorname{Cov}_\mu(X^2,j_{U_m})
   \le4r(\mathcal E_{U_m}-\mathcal E_\circ).
   \]

2. 控制 (K'')，或直接证明允许 (K,J) 补偿的精确目标

   \[
   K''+J''\ge\widehat H''.
   \]

3. 把 finite consecutive-Fourier cyclic 模型的二阶结论合法转移到 true sine/Toeplitz entropy rate；不能对一个只知值收敛的极限直接求两次导数。
4. 处理 off-midpoint、一般密度和端点一致性。

### 建议的最小下一 PRO 接口

最小、可证伪、不会被本轮 hybrid 反例直接击中的接口是：

> 固定实际 consecutive-Fourier exterior family (W_n=|\wedge^nU_m|^2)，允许使用 deletion intertwining、Cauchy full-minor positivity、Jacobi complement symmetry 及同一 (U_m) 的跨层一致性；证明或反驳上述 (F-PS)，量词必须明确写出 (m,c) 的范围。

若目标是直接闭合实际凹性，则还应另列一个 (K'') 接口，或者直接研究 combined target (K''+J''\ge\widehat H'')。不能把任意 layer-bistochastic 类上的失败再次当作 actual exterior/sine 的反例；后续反例搜索必须落在同一 unitary 的 exterior family，或真正的 sine 极限内。

最终状态：**S79 正确找到任意逐层双随机推广的严格反例，并识别了 actual exterior 需要的跨层结构；它没有完成 actual consecutive-Fourier 或 true sine 的总凹性证明，也没有反驳它们。**
