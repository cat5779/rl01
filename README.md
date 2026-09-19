# 正弦 DPP 熵率承重地图（2026-09-18）

## 结论

当前最小已知承重瓶颈，仍是**实际 sine-Toeplitz 输出律中的近场有符号聚合**。

如果能在固定任意密度 `0<rho<1`、固定 `0<c<1`、非退化的合法 `a` 区间上，以不重复消耗 Fisher 预算的方式证明这一真实近场统一支付，并把有限体积二阶式稳定传递到熵率，那么最终凹性可以闭合。其余主路线已经大幅降为辅助路线。

这不是与原猜想同难度的改写。现有工作已经给出远场、观察误差、平衡线负曲率、修正律线性响应和多种精确障碍；真正未付的是：同一个真实 DPP 后验中的坏近场项，如何在**实际概率权重**下整体抵消。

## 研究对象

对 `1<=i,j<=n`，令

\[
Q_{\rho,n}(i,j)=
\begin{cases}
\rho,&i=j,\\
\dfrac{\sin(\pi\rho(i-j))}{\pi(i-j)},&i\ne j,
\end{cases}
\qquad
K_n(a)=aI+cQ_{\rho,n},
\]

其中

\[
0<\rho<1,\qquad 0<c<1,\qquad 0\le a\le1-c.
\]

`H_n(a)` 表示该 DPP 在全部 `2^n` 个配置上的 Shannon 熵。目标是证明

\[
h_{\rho,c}(a)=\lim_{n\to\infty}\frac{H_n(a)}n
\]

存在、允许二阶传递，并在整个合法 `a` 区间上凹。

有限 Toeplitz 压缩 `Q_{rho,n}` 一般不是有限维投影；`Tr b(K_n)` 是准自由量子熵，不是这里的经典配置熵；循环 Fourier 修正律也是辅助模型，不是真实 sine-Toeplitz 输出。这三个边界不能省略。

## 已审并计入当前状态

1. **通用整区间基线。** 当前已接受的通用阈值仍为 `c<=37/40`。这是真正覆盖全部合法 `a` 的基线，不是结构性新突破。

2. **平衡线推进。** 在

   \[
   \frac{37}{40}\le c\le\frac{937}{1000},
   \qquad a=\frac{1-c}{2},
   \]

   已有严格证书

   \[
   H''\le-\frac n{50}.
   \]

   在左端 `c=37/40` 还有更强的 `H''<=-n`。这些结果只覆盖平衡线，不能当作相同 `c` 下的整区间结论。

3. **真实 sine 定位工具。** 完整 Shannon Hessian 的定位、远场与观察误差已有已审版本。S41 的 posterior 投影、Schur 字典、outside/anchor flow、随机 anchor 平均和条件装配也已核对。尚未通过的是 complete-jet Lemma 5.1；没有它，所声称的

   \[
   O_c\!\left(\sqrt{\frac{\log N}{N}}\right)
   \]

   快速定位速率仍是条件结论。

4. **真实 sine 的 dyadic 桥。** 有限弦恒等式、绝对收敛、一侧截断、准自由互信息主控、标量核与数方差尾界都已通过。对 `n=6,12` 的全部真实 Toeplitz DPP 原子作 256 位外向舍入枚举后，第一 doubling 弦严格为正。其余 11 或 12 个带符号尺度尚未支付，所以还不能推出 benchmark 熵率弦为负。

5. **修正律的有符号响应。** 对冻结的修正循环半密度律、`c=19/20`、偶数 `n`，

   \[
   \limsup_{n\to\infty}\frac{W_n}{n}
   \le-2.689614884862\ldots,
   \qquad -W_n=\Theta(n).
   \]

   更一般地，固定 `c` 下已有 `|W_n|=O_c(n)`。因此旧的 `n^{3/2}` 尺度猜想已经被排除。

6. **修正律的 clock 项。** 完整修正响应是

   \[
   \widehat K_n''(a_*)=W_n+C_n,
   \qquad C_n\ge0.
   \]

   最新上包络为

   \[
   \limsup_{n\to\infty}\frac{C_n}{n}
   \le499.631158492115\ldots
   \qquad(c=.95).
   \]

   这个界远不足以和 `W_n` 的负系数配平，所以 `W_n+C_n` 的符号仍未决定。

这些结果说明真实路线和修正律路线都已明显变窄，但修正律即使最终闭合，也不能替代真实输出律的近场支付。

## 真正未付的承重瓶颈

第一瓶颈是来自**同一个真实 DPP 后验**的近场兼容二点表。需要证明坏 pair、坏 layer 或坏 posterior node 在实际权重下被其他项抵消；不能要求每一项单独非负或非正。

第二瓶颈是修正律中的联合量

\[
W_n+C_n.
\]

目前 `W_n` 有负线性上包络，`C_n` 有非负性和很松的线性界。分别估计二者再拼接，不会自动产生符号。需要同一层权重下的联合势、Poisson 方程校正或终端熵生产比较。

第三瓶颈是修正律到真实律的二阶桥。循环投影、有限 Fourier 模型和 corrected law 可以解释机制，但最终必须回到实际 Toeplitz 压缩的完整配置概率；函数值接近、熵差为 `o(n)` 或数值收敛，都不足以控制 Hessian。

第四瓶颈是极限交换。必须证明有限体积二阶信息能统一传递到

\[
h_{\rho,c}(a)=\lim H_n(a)/n.
\]

固定规模证书、MCMC 趋势和点态收敛不能替代这一步。

## 已经明确走不通，或不能再作为主闭包的路

- **逐 pair、逐 layer、逐 latent node 强迫好符号。** 真实 sine 可达后验中已有严格坏 pair；整体平均仍可能为好，但逐项闭包是假的。
- **completion recursion 每个节点非正。** 环节可以为正，而总 Hessian 仍可能为负；节点级符号不是必要条件。
- **纯 telescope。** 允许依赖被揭示坐标的权重后，会出现无统一好符号的 drift。
- **固定静态块。** 它不能独立承担完整的 `a` 曲率。
- **用乘积近似、计数熵或 `Tr b(K)` 代替完整配置熵。** 这些对象丢失空间相关或更换了熵的定义。
- **从 entropy-value 的 `o(n)` 直接求 Hessian。** 没有导数级统一控制时不合法。
- **假设所有 harmonic modes 共用一个标量 Bernoulli-Laplace clock。** 真实时钟依赖层和模式。
- **tangent-only midpoint closure。** 一阶退化不会消除 probability acceleration。
- **假设存在正的 Berezin 测度并直接使用 Jensen。** 该正性前提不成立。
- **把有限第一弦、有限 `n` 或 MCMC 正号当作熵率证明。** 它们只能筛选路线。

## 关键反例直接展开

### 1. 真实 sine 后验中的逐 pair 失败

在 `c=19/20` 的十点 sine Toeplitz 边缘中，存在一个正概率观察 word，使条件潜在 pair 是严格正收缩。256 位 Arb 证书给出

\[
g-2(\mathcal K+\mathcal D)
>0.0189617328647243.
\]

因此要求所有真实可达 posterior 都满足

\[
g<2(\mathcal K+\mathcal D)
\]

的旧路线被否定。这个反例不否定熵凹性；它只说明必须使用实际律平均或带符号聚合，不能逐状态支付。

### 2. `P=Q` 否定 S47 的原相对熵二阶式

取任意非平凡光滑概率族并令 `P=Q`。则

\[
D(P\|Q)\equiv0,
\qquad
\frac{d^2}{da^2}D(P\|Q)=0.
\]

S47 原式 (4) 却会多出

\[
\mathbb E_Ps_P^2>0
\]

这一 Fisher 项，所以原式被最小反例直接证伪。修正后的展开式成立，但它只是把未付义务改写成 `J_L''` 负部的 dyadic 和，没有证明该和有限或趋零。

### 3. 正文尺度不能推出小 `o`

S42 原稿建议

\[
L_J\asymp\eta^{-2}\log(1/\eta)
\]

以得到内部尾 `o(eta^2)`。实际若

\[
L_J\sim k\eta^{-2}\log(1/\eta),
\]

则已证尾界满足

\[
\frac{R_{\rm sharp}(C,L_J)}{\eta^2}
\longrightarrow\frac{4C}{\pi^2k}>0.
\]

所以只能得到 `O(eta^2)`。端点的 `eta^{-2}log^2(1/eta)` 尺度同样不够。要得到小 `o`，至少需要

\[
\frac{L_J\eta^2}{\log L_J}\to\infty
\]

，端点情形则需要以 `(log L_J)^2` 为分母的对应条件。

### 4. Draft 中的有限非凹证书

尚未整体合入的 Draft #5 含严格有限证书：在 `c=19/20,n=8` 时，辅助函数 `E_8(a)` 满足

\[
E_8''(1/200)<0,
\qquad
E_8''(1/50)>0,
\qquad
E_8''(1/40)>0.
\]

所以该有限辅助对象既非凹也非凸。它已有区间证书和独立源码检查，但尚未独立重跑，也不是实际熵率主命题的反例。

### 5. 五点复 Hermitian 核直接否定一般 DPP 熵的全局凹性

在五个标号点上取

\[
e=(1,1,1,1,1)^T,\qquad x=(-2,-1,0,1,2)^T,
\]

\[
u=(2,-1,-2,-1,2)^T,\qquad v=(-1,2,0,-2,1)^T,
\]

并令

\[
P=\frac{ee^T}{5}+\frac{xx^T}{10},\qquad
B=e\wedge x-\frac12u\wedge v,\qquad A=\mathrm iB,
\]

其中 `a wedge b=ab^T-ba^T`，`P` 是秩二正交投影。再设

\[
K_\varepsilon=\varepsilon I+(1-2\varepsilon)P.
\]

当 `0<\varepsilon<1/2` 且 `|t|<\varepsilon/\sqrt{50}` 时，`K_{\varepsilon}+tA` 都是严格正压缩并两两可交换，而且 `t` 与 `-t` 的完整配置律完全相同。取

\[
\varepsilon_0=10^{-6},\qquad h=10^{-10},
\]

精确有理对数区间证书给出

\[
\frac{566127}{10^6}
<D^2H(K_{\varepsilon_0})[A,A]
<\frac{566128}{10^6},
\]

以及

\[
\frac2{10^{21}}
<\frac{H(K_{\varepsilon_0}-hA)+H(K_{\varepsilon_0}+hA)}2
-H(K_{\varepsilon_0})
<\frac3{10^{21}}.
\]

中点熵严格小于两端熵的平均值，所以完整配置 Shannon 熵在一般复 Hermitian 边缘核上不是全局凹函数；这不是浮点拟合，而是覆盖全部 `2^5=32` 个配置的严格证书。

这个反例不否定本库的真实 sine-Toeplitz 猜想：它使用复方向 `A=\mathrm iB`，既不是共同对角平移 `aI+cK`，也没有平稳或 Toeplitz 结构；它同样没有解决实对称核的三点以上一般情形。

### 6. 六点 Fourier 投影否定“所有 Taylor 系数同号”

另一个反例针对的是证明方法，而不是熵凹性本身。令

\[
P_{6,3}=\operatorname{circ}
\left(\frac12,\frac13,0,-\frac16,0,\frac13\right),
\]

即六点循环群上 Fourier 模式 `{-1,0,1}` 的秩三正交投影；等价地，

\[
(P_{6,3})_{ij}
=\frac16\left(1+2\cos\frac{2\pi(i-j)}6\right).
\]

取 `X\sim\operatorname{DPP}(P_{6,3})`，再逐坐标独立通过真实二元信道

\[
\Pr(Y_i=1\mid X)=a+cX_i.
\]

记完整标号输出律为 `p_y`，所有导数都是固定 `c` 后对物理参数 `a` 求导，并定义

\[
H_{aa}
=-\sum_y p_{y,aa}\log p_y
-\sum_y\frac{p_{y,a}^2}{p_y},
\qquad
F_{\rm diag}
=\sum_i\sum_y\frac{(\partial_{a_i}p_y)^2}{p_y},
\]

\[
U_P(c)=
\left[H_{aa}+F_{\rm diag}\right]_{a=(1-c)/2}.
\]

这个量在 `|c|<1` 内解析。对全部 64 个输出 word 作精确有理枚举，得到

\[
[c^{36}]U_{P_{6,3}}(c)
=\frac{94817639921336320}{150094635296999121}>0,
\]

而 36 次以前的所有 Taylor 系数都非正。因此“对 consecutive-Fourier 输入，`U_P` 的每个 Taylor 系数都非正”这一逐系数闭包是假的。

但同一个见证在任务基准点

\[
a=\frac1{40},\qquad c=\frac{19}{20}
\]

满足严格区间

\[
-165.800<H_{aa}<-165.798,
\qquad
-77.281<U_P<-77.279.
\]

所以实际熵曲率仍严格为负，甚至这个点上的聚合支付不等式 `U_P\le0` 仍成立。反例只排除“逐 Taylor 系数统一好符号”的证明路线；它不反驳 unit-payment 本身，更不反驳真实 sine-Toeplitz 熵率凹性。

## 修正律辅助线的当前作用

- **S13 / S45 clock：** clock 分量是线性尺度，并有显式上包络；尚未与 `W_n` 联合支付。
- **S14 计数运输：** 精确运输与删除链成立；无条件主剩余项符号仍开。
- **S16 径向分解：** 径向项为 `o(n^{3/2})`；但后续 S45 已把完整 `W_n` 推进到 `O(n)`。
- **S43 有符号响应：** 在 `c=.95` 已得到负线性上包络，是当前修正律最强结果。
- **S17 / SA03 极限核：** 有限证书机制和有效余项成立；`Gamma(19/20)` 的决定性符号仍开。

这些结果说明修正律路线已经从“尺度未知”推进到“只差联合支付”，但它仍是辅助线。

## 待独立审阅，不计入已审结论

- Draft #5 的 SA05 `n=8` 区间证书、SA03 有限诊断、SA04 作者证明和 MCMC 记录仍按证据等级分开保存。
- SA04 deletion lower bound 与中央 clock-gap 渐近仍是作者证明，尚未通过独立验缝。
- SA03 的 `R=9` wordwise 负核和半参数有限反例仍待区间化、独立复现。
- Cycle 05 的 S41 complete-jet 修复与 S43 联合 `W+C` 工具正在研究；已派题不等于已有结果。

## 优先级

**第一优先：真实律近场聚合。** 要求共同后验、实际概率权重和不可重复计费的有符号支付。

一个有价值的里程碑是：在

\[
\rho=\frac12,qquad c=\frac{19}{20}
\]

上，对一个固定的非退化 `a` 区间给出维数一致的严格余量，或者证明真实近场残差为 `o(n)`。

**第二优先：修正律联合量。** 直接控制 `W_n+C_n`，并同时说明哪些部分能够穿过真实律 / 修正律二阶桥。

**第三优先：complete-jet。** 为 S41 Lemma 5.1 提供完整展开和逐项账本，或建立一个对翻位、Bregman 余项和微分封闭的加权范数代数。

不再优先：tiny-contrast extension、逐项 positivity、只改常数、只做数值正号、只证明修正律而不付桥。

## 状态边界

本页是研究决策地图，不是新证明。这里严格区分：

- **已审结论：** 有独立报告并明确写出作用域；
- **作者级结论：** 有证明稿但尚未独立验缝；
- **有限证书：** 只说明固定规模、固定参数；
- **探索证据：** 浮点、MCMC 或路线诊断；
- **方法反例：** 否定某个充分条件，不自动否定最终猜想。

当前没有实际 sine 熵率的全参数反例，也没有全参数凹性证明。

## 证据与复现入口

正文已经给出承重关系和关键反例。下面的链接只用于核对细节，不是理解本页的前置条件。

| 内容 | 入口 |
|---|---|
| 精确题面、量词与最终成功标准 | [TARGET.md](TARGET.md) |
| 当前全部路线的紧凑裁决 | [STATUS.md](STATUS.md) |
| S43 负线性响应 | [S43 cycle03 独立审查](research/INDEPENDENT_REVIEW_20260918/S43_CYCLE03.md) |
| S45 的 `O(n)` 响应界与 clock 上包络 | [S45 cycle03](research/INDEPENDENT_REVIEW_20260918/S45.md) · [S45 cycle04](research/INDEPENDENT_REVIEW_20260918/S45_CYCLE04.md) |
| S42 dyadic 桥、小 `o` 纠正和第一弦证书 | [S42 cycle03](research/INDEPENDENT_REVIEW_20260918/S42_CYCLE03.md) |
| S41 posterior 骨架与 complete-jet 缺口 | [S41 cycle03](research/INDEPENDENT_REVIEW_20260918/S41_CYCLE03.md) · [S41 cycle04](research/INDEPENDENT_REVIEW_20260918/S41_CYCLE04.md) |
| 平衡线覆盖与真实 sine 后验障碍 | [SA02 边界审查](research/INDEPENDENT_REVIEW_20260918/SA02_C37_BOUNDARY.md) |
| S47 的 `P=Q` 反例 | [S47 cycle04](research/INDEPENDENT_REVIEW_20260918/S47_CYCLE04.md) |
| 尚未整体合入的有限证书与诊断 | [Draft PR #5](https://github.com/cat5779/rl01/pull/5) |
| 全部独立审查 | [审查索引](research/INDEPENDENT_REVIEW_20260918/README.md) |
| 历史证明、证书和复验代码 | [RESULTS.md](RESULTS.md) |
| 已失败方法及外推边界 | [METHODS.md](METHODS.md) |
| 当前研究题面 | [Cycle 05](prompts/CYCLE05/README.md) |
