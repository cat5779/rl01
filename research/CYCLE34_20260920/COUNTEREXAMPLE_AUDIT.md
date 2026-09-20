# 最新反例、障碍与逻辑强度审计

审计日期：2026-09-20（Asia/Singapore）

## 0. 用途与总边界

本文只为 root 更新公开 README、反例地图和主实例交接提供冻结材料，不提出新数学路线，也不继承历史文件中的“正在跑”状态。证据来自 S74–S79 与 QWE08 的最新独立审查；未读取、未判断 S80。

最重要的总裁决是：

> 截至本次材料，没有 true sine-Toeplitz Shannon 熵率非凹反例。

已经出现的严格负号分别属于 mixed diagonal entry、单 pair 揭示漂移、逐旧背景条件漂移、点态 posterior 支付、weak-cut 系数、局部 reveal potential、任意 layer-bistochastic hybrid、或逐 monomial 展开。它们都否定了某个更强的局部闭包或证明机制，但没有给出 true sine 熵率 \(h_{\rho,c}\) 的反例。

“真实 sine 有限压缩中的反例”和“true-sine 熵率反例”必须分开：

- 前者只需一个有限 Toeplitz 主压缩中的某个局部量为负；
- 后者至少要让实际完整配置熵的有限体或弦缺陷以可传递方式产生错误符号，并支付 all-size 与极限桥；
- 局部 potential、单 pair、单 word、单 mixed coordinate 或一个展开 monomial 的错误符号都不够。

## 1. 证据等级

本文统一使用以下等级，避免把不同强度混写。

| 等级 | 含义 | 可以支持 | 不能自动支持 |
|---|---|---|---|
| ANALYTIC_EXACT | 闭式恒等式、精确级数或有理代数证明 | 题面量词内的一般结论 | 超出题面对象或参数的外推 |
| STRICT_INTERVAL | 外向舍入或整数定点区间，严格包住目标量并与零分离 | 指定有限模型、参数点或参数矩形的严格符号 | all-size、熵率或其他模型 |
| FINITE_CONTINUUM | 对固定有限尺寸、连续参数区间给出严格证书 | 该尺寸整个参数区间 | 尺寸趋于无穷或熵率 |
| FLOAT_DIAGNOSTIC | 双精度、高精度但无外向误差包围、有限网格或残差 | 实现核对、路线筛选 | “certified”、严格符号或连续参数结论 |

## 2. 快速总表

| 障碍 | 冻结模型/参数 | 证据等级 | 真正否定 | 不能否定 | 独审入口 |
|---|---|---|---|---|---|
| S74 负 mixed entry | \(N=6,\rho=1/2,c=19/20,a=1/40\)，\(3+3\) cut，独立扰动第 1、6 对角 | STRICT_INTERVAL | 每个 mixed diagonal entry/rectangle defect 都非负 | common identity convexity、\(M''\ge0\)、true-sine rate | PR64_FINAL |
| S75 条件星形负漂移 | 半密度 \(c=.95,a=1/2000\)，core \(\{0,7\}\)，旧叶 \(\{-1,1\}\)，加入 \(-3\)，旧 word 00 | STRICT_INTERVAL | 每个旧背景 word 下星形 pair 漂移非负 | 对旧背景实际平均后的星形正漂移 | PR65 |
| S75 非半密度 pair 负漂移 | \(\rho=9/20,c=19/20,a=1/200\)，sites \(\{0,3,4\}\)，pair \(\{0,3\}\)，揭示 4 | STRICT_INTERVAL | 任意 sine 几何中每个 individual pair 的无条件漂移非负 | 完整 \(\Chi\)、完整熵曲率、熵率 | PR65 |
| S76 点态 \(\Xi/\delta\) 障碍 | 半密度中点、actual cyclic Fourier、\(m=2\)、count-one 且 \(X=0\) atom | ANALYTIC_EXACT | contrast-independent 点态小系数，如 \(\Xi_O\le\delta_O\) | 四点总曲率；actual Toeplitz/sine rate | PR66_FINAL |
| S77 weak-cut \(\theta<1\) 障碍 | equal-marginal 两点严格 DPP，\(u=1/2\)，\(d=|z|^2\downarrow0\) | ANALYTIC_EXACT | 固定 \(\theta<1\) 加 quartic residual 的统一支付 | \(\theta=1\)、quadratic residual、结构化 sine 支付 | PR67 |
| S78 两个负 reveal 反例 | 半密度 \(c=.95,a=1/40\) 的两个有限 true-sine 主压缩 | STRICT_INTERVAL | leaf/center addition 的无条件零支付单调性 | 补偿定理、完整 Shannon 凹性、熵率 | PR68_FINAL |
| S78 \(R^{-4}\) 量词反例 | 半密度 sine，令 retained leaf \(i=q+1\) 随新增中心移动 | ANALYTIC_EXACT | 对所有移动 retained pairs 一致的 \(R^{-4}\) 包络 | 固定 pair 或 \(|q-i|\gtrsim|p-q|\) 下的 \(R^{-4}\) | PR68_FINAL |
| S79 generic layer hybrid | \(m=36,c=4/5\)，layers 16–20 identity，其余 shell mixing | STRICT_INTERVAL | 任意 layer-bistochastic 中点总凹性及 universal paid-shell | exterior-unitary、consecutive Fourier、true sine | PR69 |
| QWE08 负 monomial | 四点 parity-reordered \(C=s\begin{psmallmatrix}1&-1/3\\1&1\end{psmallmatrix}\) | ANALYTIC_EXACT | 逐 monomial 非负扩展 | 完整 \(M''<0\)、all-size MI、熵率 | PR70 |

本表中的 PR 本地路径在各节末尾给出。

## 3. S74：负 mixed diagonal entry

### 冻结模型

取实际六点半密度 sine 主压缩

\[
N=6,\qquad \rho=\frac12,\qquad c=\frac{19}{20},\qquad a=\frac1{40},
\]

切分

\[
A=\{1,2,3\},\qquad B=\{4,5,6\}.
\]

在冻结 sine 基点上，只分别扰动第 1、6 个 diagonal coordinates：

\[
K(u,v)=K+u e_1e_1^*+v e_6e_6^*.
\]

### 严格证据

审查者实际重放 directed fixed-point interval checker。它证明

\[
-0.0003790922420416860133
<
\mathcal M_{uv}(0,0)
<
-0.0003790922420416860132,
\]

并在整个

\[
0\le u,v\le10^{-10}
\]

矩形上证明 \(\mathcal M_{uv}<-3/10000\)，所以 rectangle defect 严格小于 \(-3\times10^{-24}\)。

证据等级：STRICT_INTERVAL；作者 interval checker 经独审重跑，另有独立 Decimal 与 PR63 数值交叉核对。

### 真正否定什么

- “每个跨 block mixed diagonal Hessian entry 都非负”；
- “每个小 mixed rectangle defect 都可逐项取非负”的极化捷径。

### 不能否定什么

- 共同 identity direction 的凸性；
- 该点的总 mutual-information curvature。事实上同一证书给
  \[
  D_F+C_{\rm acc}=M_{3,3}''\approx13.74976747035>0;
  \]
- true sine Shannon 熵率凹性。

### 独审路径

C:/game/gameproject/showa100/math/rl01-cycle19-harvest/research/CYCLE27_20260920/reviews/PR64_FINAL/S74_CYCLE26_REVIEW.md

## 4. S75：两个不同层级的 pair 漂移反例

### 4.1 给定旧背景 word 的星形负漂移

冻结半密度星形：

\[
\rho=\frac12,\quad c=\frac{19}{20},\quad a=\frac1{2000},
\]

核心 pair 为 \(\{0,7\}\)，旧叶为 \(\{-1,1\}\)，新增叶为 \(-3\)。固定旧背景 word 为 00 时，严格区间给

\[
\mathbb E[\Delta f_{0,7}\mid 00]
\in[-7.4327,-7.4325]\times10^{-7}<0.
\]

但对全部四个旧背景 words 按真实概率平均后，

\[
\mathbb E\Delta f_{0,7}
\approx1.38752717948\times10^{-5}>0.
\]

证据等级：STRICT_INTERVAL；作者 exact-rational interval certificate 经独审重放，另有独立全配置枚举。

真正否定：

- 把 S75 星形定理加强成“对每个旧背景 word 条件漂移都非负”。

不能否定：

- S75 已证的实际旧背景平均后正漂移；
- 星形无条件 theorem；
- 完整熵曲率或熵率。

### 4.2 非半密度真实 sine individual pair 负漂移

冻结模型：

\[
\rho=\frac9{20},\quad c=\frac{19}{20},\quad a=\frac1{200},
\]

取实际 sites \(\{0,3,4\}\)，核心 pair \(\{0,3\}\)，揭示 site 4。它可嵌入连续区间 \(\{0,1,2,3,4\}\)，未列 sites 被边缘化。严格证书给

\[
\mathbb E\Delta f_{03}
\in[-0.000177080,-0.000177078]<0.
\]

证据等级：STRICT_INTERVAL。

真正否定：

- 一般 sine 几何中“每个 individual cross pair 的无条件漂移都非负”。

不能否定：

- 完整 core 中所有 pairs 求和后的 \(\Chi\)；
- 连续 interval-core 总漂移；
- \(H_N''\) 或熵率符号。

### 独审路径

C:/game/gameproject/showa100/math/rl01-cycle19-harvest/research/CYCLE27_20260920/reviews/PR65/S75_CYCLE26_REVIEW.md

## 5. S76：点态 \(\Xi_O/\delta_O\) 系数障碍

### 冻结模型

半密度对称中点的 actual cyclic Fourier channel，\(m=2\)。选择 count-one、\(X=0\) 的输出 atom。精确后验只含 \(D=2,0\)，并有

\[
\frac{\Xi_O}{\delta_O}
=
\log\frac{r^2+s^2}{2r^2}.
\]

令 \(x=s/r=(1+k)/(1-k)\)，比值大于 1 等价于 \(1+x^2>2e\)。阈值为

\[
c>
\sqrt{\frac{\sqrt{2e-1}-1}{\sqrt{2e-1}+1}}
=
0.596783320897\ldots,
\]

且 \(c\uparrow1\) 时该比值发散。

证据等级：ANALYTIC_EXACT。阈值数值只是闭式阈值的显示值；反例本身不依赖浮点表。

### 真正否定什么

- \(\Xi_O\le\delta_O\) 这类 contrast-independent 点态单位系数；
- 任何要求每个输出 atom 都以小固定常数单独支付 \(C_X\) 的证明。

### 不能否定什么

- 同一 \(m=2\) actual cyclic channel 的总曲率；既有结果反而给总曲率为负；
- 利用不同 atoms 之间实际权重抵消的聚合支付；
- finite cyclic 到 actual sine-Toeplitz 的桥；
- true sine 熵率凹性。

### 独审路径

C:/game/gameproject/showa100/math/rl01-cycle19-harvest/research/CYCLE30_20260920/reviews/PR66_FINAL/S76_CYCLE28_REVIEW.md

## 6. S77：weak-cut 固定 \(\theta<1\) 不可能

### 冻结模型

equal-marginal 两点严格 DPP，在 \(u=1/2\) 共同平移方向，令

\[
d=|z|^2,\qquad x=4d.
\]

精确公式为

\[
D_F=\frac{8x}{1-x},
\qquad
C_{\rm acc}=4\log\frac{1-x}{1+x}.
\]

当 \(d\downarrow0\)，

\[
D_F=32d+O(d^2),
\qquad
-C_{\rm acc}=32d+O(d^3),
\qquad
\frac{-C_{\rm acc}}{D_F}\to1.
\]

若要求统一

\[
-C_{\rm acc}\le\theta D_F+C d^2
\]

且固定 \(\theta<1\)，除以 \(d\) 再令 \(d\downarrow0\) 即矛盾。

证据等级：ANALYTIC_EXACT。审查中的 \(d=10^{-2},\ldots,10^{-8}\) 比值表只是浮点示意，不承担证明。

### 真正否定什么

- 以固定 \(\theta<1\) 吃掉 leading Fisher term，再只留 quartic residual 的通用 weak-cut 方案。

### 不能否定什么

- \(\theta=1\)；
- 另一个 quadratic residual；
- exact Fisher–Burg cancellation；
- 使用固定 Toeplitz/sine 几何的非微扰估计；
- 两点总 \(M''\)。S77 还解析证明了 \(M''\ge C(u)d^2>0\)。

### 额外证据边界

S77 六点的 \(\mathcal I_{\rm rel}-\mathcal B_+\) 正数和 45 点扫描是 FLOAT_DIAGNOSTIC，不是 outward interval certificate。PR64 对同一六点认证的是 \(D_F,C_{\rm acc},M''\)，没有认证 S77 新的 \(\mathcal B_+\) 数值。公开 README 不应写成“B+ finite seed 已严格认证”。

### 独审路径

C:/game/gameproject/showa100/math/rl01-cycle19-harvest/research/CYCLE31_20260920/reviews/PR67/S77_CYCLE31_REVIEW.md

## 7. S78：两个有限 true-sine reveal 反例与一个量词修正

### 7.1 same-parity center addition

冻结参数：

\[
\rho=\frac12,\qquad c=\frac{19}{20},\qquad a=\frac1{40}.
\]

retained pair 为 \(P=\{0,-3\}\)，旧集合 \(\{0,-3,1,3\}\)，新增 same-parity center \(-4\)。独立外向区间证书给

\[
\mathbb E\Delta f_{0,-3}
\in
[-0.001933130713983040159308864984082,
 -0.001933130713983040159308864984081]
<0.
\]

同时

\[
\mathbb E\Delta(\mathcal F-\ell)>0.
\]

### 7.2 opposite-parity leaf addition with two centers

同一参数，centers \(\{0,10\}\)，core leaf 7，旧观察叶 \(-3\)，新增叶 \(-1\)，定义

\[
\Chi=f_{0,7}+f_{10,7}.
\]

严格区间给

\[
\mathbb E\Delta\Chi
\in[-4.912434017602194,-4.912434017602193]\times10^{-7}<0.
\]

两项证据等级均为 STRICT_INTERVAL：独立外向区间证书通过；Cycle33 作者四个证书也经安全检查原样重放。

### 真正否定什么

- leaf addition 的 universal raw nonnegative drift；
- center addition 的 universal raw nonnegative drift；
- “所有 reveal 操作都可零支付望远镜”的路线。

### 不能否定什么

- S78 的 compensated rank-one reveal theorem；
- 完整配置 Shannon 熵凹性；
- true sine 熵率凹性。

两项都是实际 finite true-sine principal compressions，但测试的是局部 reveal potential，不是 \(H_N''>0\)，更不是 rate 反例。

### 7.3 \(R^{-4}\) 的量词必须固定 retained pair

第一交互粗界含直接项 \(|b_{qi}|^4\)。若固定 \((p,i)\) 而让新中心 \(q\) 远离，则 \(|q-i|\asymp|p-q|=R\)，完整 defect 可为 \(O(R^{-4})\)。

若允许 retained leaf 随 \(q\) 移动，取 \(i=q+1\)，则半密度 sine 中

\[
|b_{qi}|^4=(c/\pi)^4,
\]

完全不随 \(R\) 衰减。故合法量词只能是：

- 固定 retained pair \((p,i)\)；或
- 明写 \(|q-i|\gtrsim|p-q|\)。

证据等级：ANALYTIC_EXACT；\(0.0083617067\ldots\) 的数值表只是示意。

这项修正不影响 arbitrary-block log-barrier theorem，但禁止把 fixed-pair 空间尾无条件用于 growing core 的所有移动 pairs。

### 独审路径

C:/game/gameproject/showa100/math/rl01-cycle19-harvest/research/CYCLE33_20260920/reviews/PR68_FINAL/S78_CYCLE31_REVIEW.md

## 8. S79：generic layer-bistochastic hybrid 反例

### 冻结模型

\[
m=36,\qquad c=\frac45.
\]

通道在 Hamming layers 16–20 取 identity，在其余 layers 取完全 shell mixing。每一层分别保持该层、双随机并满足补余对称，但不同 layers 不是同一个 unitary 的 exterior powers。

独立 outward-rounded Decimal 得到

\[
H''\in[
10.4745311384739813781852692400271678,
10.4745311384739813781852692400271680
]>0,
\]

并且

\[
H''-H_\circ''
\in[
304.7703167478882545413267331336819263,
304.7703167478882545413267331336819264
]>0.
\]

证据等级：STRICT_INTERVAL；作者程序与独立实现均复现。

### 真正否定什么

- 任意 layer-preserving bistochastic channel 的中点总凹性；
- 对所有这类通道都成立的 universal paid-shell inequality；
- 只依赖 layer bistochasticity、补余对称及粗 range/variance 数据的普遍闭包。

### 不能否定什么

- exterior-unitary family \(W_n=|\wedge^nU|^2\)；
- consecutive-Fourier；
- true sine；
- 所有不显式跨层的可能证明。更强的单层结构条件也可能排除 hybrid。

### \(K''+J''\) 的精确阈值

必须区分

\[
H_U,\qquad H_\circ,\qquad \widehat H,
\]

以及

\[
J=H_\circ-H_U,\qquad K=\widehat H-H_\circ.
\]

值层 \(J,K\ge0\) 不推出 \(J'',K''\ge0\)。精确恒等式为

\[
H_U''=\widehat H''-(K''+J'').
\]

因此实际凹性的精确充要阈值是

\[
H_U''\le0
\quad\Longleftrightarrow\quad
K''+J''\ge\widehat H''.
\]

这里 \(\widehat H''<0\)。所以

\[
K''+J''\ge0
\]

只是更强的充分条件，不是等价 reduction；分别要求 \(K''\ge0,J''\ge0\) 更强。paid-shell 只提供 \(J''\ge0\) 的结构化充分条件，仍需 \(K''\) 或 combined compensation。

公开文档若把阈值写成 0，会夸大未解义务；若从 \(J,K\ge0\) 推导二阶非负，则是值与曲率混淆。

### 独审路径

C:/game/gameproject/showa100/math/rl01-cycle19-harvest/research/CYCLE31_20260920/reviews/PR69/S79_CYCLE31_REVIEW.md

## 9. QWE08：负 monomial，不是负曲率

### 冻结模型

四点 parity-reordered cross block 为

\[
C=s
\begin{pmatrix}
1&-1/3\\
1&1
\end{pmatrix}.
\]

在 \((1+u)\log(1+u)\) 展开中，提取

\[
x_1^3x_2^2y_1^2y_2^3s^{10}
\]

的系数，精确得到

\[
-\frac1{27},
\]

所以对应 monomial 是 \(-s^{10}/27\)。相应 Bernoulli moment
\(\mu_3^2\mu_2^2\ge0\)，负号不会被取期望自动消掉。

证据等级：ANALYTIC_EXACT；有理多项式独立复核。

### 真正否定什么

- 把 rank-one 非负图/monomial 机制逐项延伸到 rank two；
- “每个 determinant-loop monomial 都非负”的证明。

### 不能否定什么

- 完整 mutual-information curvature \(M''\ge0\)；
- all-size MI convexity；
- Shannon 熵率凹性。

完整 \(M''\) 还包含同阶及其他阶项。QWE08 同时给出正的有限连续参数证书：

\[
c=\frac{19}{20},\qquad
a\in[1/50,3/100],\qquad
m+n\le4,
\]

全部相邻切割的 \(M''\) 有严格统一正下界 \(>1.5454668697424\)。这属于 FINITE_CONTINUUM：它覆盖连续 \(a\)-区间，但尺寸固定不超过 4，不是 all-size 或 rate 定理。

### 独审路径

C:/game/gameproject/showa100/math/rl01-cycle19-harvest/research/CYCLE33_20260920/reviews/PR70/QWE08_CYCLE33_REVIEW.md

## 10. 有限 seed、浮点、continuum 与熵率的四层区别

### 10.1 固定点有限证书

严格 interval 在一个固定 \(N,c,a\) 上给出的符号，只说明该有限对象。S74、S75、S78 的反例即使位于 actual finite sine compression，也不能自动传到 \(N\to\infty\)。

### 10.2 浮点有限诊断

没有 outward rounding、解析余项或精确有理误差界的正数只能作为诊断。特别是：

- S77 的 \(\mathcal I_{\rm rel}-\mathcal B_+\) 六点正数；
- S77 的 45 点参数扫描；
- 小尺寸 consecutive-Fourier 表；
- 有限差分残差。

它们不能写成 certified seed，也不能把网格正号外推到连续参数。

### 10.3 有限 continuum certificate

continuum 指参数 \(a\) 的整个连续区间经过解析/区间尾认证，不等于尺寸 continuum。QWE08 在 \(m+n\le4\)、\(c=.95\)、\(a\in[.02,.03]\) 的结果是严格 finite-continuum seed；它仍然没有覆盖所有尺寸。

同理，S74 的 \([0,10^{-10}]^2\) mixed rectangle 是扰动参数矩形上的严格证书，不是 common identity 的全参数结论。

### 10.4 all-size 与熵率

熵率结论还需要：

1. 全部所需尺寸或一个可求和的 almost-superadditive defect；
2. 参数区间上一致控制；
3. 有限体到 entropy rate 的合法 bridge；
4. 不从 entropy-value 的 \(o(n)\) 直接求二阶导。

有限正 seed 只有在 merge/Fekete/弦接口的其余尺度与 defect 都被支付后才承重。有限负局部量也只有在能进入完整 \(H_N''\) 并以可传递尺度存活时，才可能形成 rate 反例。

## 11. 对历史 README/METHODS 的修正提醒

历史根文件：

- C:/game/gameproject/showa100/math/rl01-cycle19-harvest/README.md
- C:/game/gameproject/showa100/math/rl01-cycle19-harvest/METHODS.md

可用于背景，但日期停在 2026-09-18，不能继承其中任何“正在研究”“已派题”“待审”等运行状态。建议 root 更新时注意以下陷阱。

1. “逐 pair 路线失败”不能写得过宽。S75 否定的是任意几何中每个 individual pair 都有好符号；S78 否定的是两个 raw reveal monotonicity。实际权重聚合、补偿势和 block theorem 仍可行。

2. “逐 layer 失败”也不能写成 actual sine 失败。S79 的 hybrid 只满足逐层 bistochastic/complement 条件，不满足同一 exterior unitary 的跨层一致性。

3. “真实 sine 反例”必须加有限对象和量名。S74/S75/S78 都在 actual finite sine 主压缩中，但反例量不是 entropy rate，很多甚至不是完整 \(H_N''\)。

4. 约 220 倍只能称为 S78 方法误差包络改善：
   \[
   107974.9489\ldots\to490.6744\ldots.
   \]
   扣除现有基线和星形下界后仍约 \(490.391684>0\)，MAIN_INCOMPLETE。

5. S77 的 B+ 表是浮点诊断。不要使用“certified lower bound”描述 \(\mathcal I_{\rm rel}-\mathcal B_+\)；严格认证的是 PR64 中的 \(D_F,C_{\rm acc},M''\)。

6. QWE08 的 continuum certificate 是固定小尺寸的连续 \(a\)-区间，不是 all-size continuum 或熵率证书。

7. S76 的 actual cyclic、S79 的 generic layer hybrid、finite consecutive-Fourier exterior family 与 actual Toeplitz sine 必须分栏。cyclic/exterior 机制不能无桥替代 Toeplitz 输出律。

8. \(K''+J''\) 的精确阈值是 \(\widehat H''\)，不是 0。零阈值是更强充分条件。

9. 负 monomial、负 mixed entry、负 conditional word、负 individual pair、负 raw reveal drift 是五个不同对象，不应在反例栏合并成“MI/熵曲率为负”。

10. 公开首页应保留一句醒目标注：
    **当前没有 true-sine Shannon 熵率反例，也没有全参数凹性证明。**

## 12. 主实例交接最短版

如果 root 只取一段，可直接采用以下边界：

> 最新反例已经系统排除了 entrywise mixed positivity、逐旧背景条件 positivity、任意 individual-pair positivity、固定 \(\theta<1\) 的 weak-cut、零支付 reveal monotonicity、任意 layer-bistochastic paid-shell，以及逐 monomial positivity。它们没有给出 true-sine 熵率反例。S79 的 exact threshold 是 \(K''+J''\ge\widehat H''\)，而非 \(K''+J''\ge0\)；后者只是更强充分条件。S77 的 B+ 数值仍是浮点，QWE08 的 continuum certificate 仍是有限尺寸，S78 的约 220 倍仅是误差包络改善。后续 README 必须按“有限对象/实际 sine 与否/证据等级/否定范围”四列陈述，不能把局部方法障碍升级成主猜想反例。
