# S67 Cycle20 续稿独立数学审查

审查日期：2026-09-19（Asia/Singapore）

## 总裁决

`VERIFIED_SCOPED / MAIN TARGET INCOMPLETE`。

可接受的新结果是固定模型

\[
\rho=\tfrac12,\qquad c=\tfrac{19}{20},\qquad
(a_0,b,a_1)=(\tfrac1{50},\tfrac1{40},\tfrac3{100})
\]

上的实际完整配置律加速度上界

\[
\limsup_{n\to\infty}\frac{\mathcal C_n}{n}
\le \frac{110333}{166400000}
=0.000663058894230769\ldots .
\]

结合已审的 `c16` 下端点，这给出

\[
\limsup_{N\to\infty}A_{16\,2^N}
\le0.000516378413904885283217037721\ldots .
\]

count gauge、共同中心 odds-width 比较、补偿加权 resolvent、非投影
leakage，以及 count tilt 与有限压缩不交换所产生的 interaction-level
边界误差均可闭合。没有发现阻断这条 scoped 上界的数学错误。

但所需加速度 cap 只有

\[
C_*\le0.000392612480721685576393825706,
\]

新上界仍高出至少

\[
0.000270446413509083654375405063\ldots .
\]

因此连这一个固定 `rho=.5,c=.95` 中点弦都没有得到正熵率 gap；整个
`c in (37/40,1)`、全部 chord、全部密度和合法偏置更没有完成。该负预算只是
证明工具未闭合，不是熵凹性的反例。

## 1. 理论链核查

### 1.1 count gauge 与实际律权重

有限 L-ensemble 的共同人数倾斜严格满足

\[
\log p_{K^{(z)}}(x)=\log p_K(x)+|x|\log z-\log Z_K(z).
\]

二位混合差分消去后两项，故 `F_{K^(z)}=F_K` 是逐配置恒等式。正文只改变
被评估的 reference interaction，外层始终是实际 `P_a` 权重；没有把实际律换成
辅助律。

正文也正确否定了

`f_z(K_{b,n}) = uI+(v-u)Q_n`。

`n=1,z=6/5` 的精确反例成立。后续不是忽略不交换误差，而是直接比较两套
interaction。

### 1.2 common-center odds-width 引理

把负相关二元表写成 `r=BC/(AD)>=1` 与 `q=A+D` 后，四个条件 odds 共处
`[z/M,zM]` 推出

\[
q\ge \frac{2M}{M^2+2M+r}.
\]

中心 `z` 在这一步完全消去，所以共同 fugacity 不产生额外常数。对 `M<=20`
剩余函数 `phi(r)` 的两个临界点结构、`5.69/5.70` 有理夹逼以及
`e^(7/4)>5.70` 均重新核对通过，结论 `J<=3W/2` 成立。它没有恢复已被 PR51
反例推翻的 factor-one 比较，也不允许两个站点使用不同中心。

### 1.3 endpoint-matched transport

所选

\[
z(a)^2=\frac{a(a+c)}{(1-a)(1-a-c)}
\]

使实际 kernel 与辅助两层 kernel 在光谱两个端点的 L-odds 比互为倒数。
`f_R` 的凹性和 `f_{1/R}` 的凸性把端点关系推广到 `Q_n` 的全部光谱，得到

\[
R^{-1}L(\widehat K_a)\preceq L(K_a)\preceq R L(\widehat K_a).
\]

Schur complement 和 matrix-log path 随后分别给一站点、二站点的合法 likelihood
比较。路径导数是投影减正压缩与白化导数的 trace pairing；前者的算子范数不超过
1，故 k 维条件律的 `R^k` 常数没有漏掉因子二。

### 1.4 tilt/compression 不交换的导数级边界

Lemma 5.1 的承重点是对 `F_K` 本身沿 kernel 线段求导，而不是对一个熵值误差
求导。对 `B=(K-D_x)^(-1)`，谱隙给 `||B||<=epsilon^(-1)`；两次 flip 的概率比
给分母下界 `t0^2`。逐 pair 求导、Frobenius Cauchy--Schwarz 和 trace norm
控制确实产生

\[
L_n(\epsilon)=t_0^{-2}\epsilon^{-3}\sqrt n
+t_0^{-3}\epsilon^{-4}.
\]

另一方面，`f_z(K_b)` 与端点线性插值都是 `Q_n` 的函数，标量二阶插值误差给

\[
\|f_z(K_{b,n})-\widehat K_{a,n}\|_1
\le\frac{5c^2}{16}\operatorname{Tr}(Q_n-Q_n^2).
\]

半密度 sine compression 满足 `Tr(Q_n-Q_n^2)=O(log n)`，所以正文的
`E_n` 确实趋零。常数极大，只支持 limsup，不支持实用有限 stopping volume；
原稿对此范围声明准确。

### 1.5 补偿加权 resolvent

从

\[
K^2-(u+v)K+uvI=-(v-u)^2(Q_n-Q_n^2)
\]

代入 `K=B^(-1)+D_x`，可逐项恢复式 (6.1)。按配置使用
`s_i=uv` 或 `(1-u)(1-v)` 后，无序 pair 的权为
`s_i/s_j+s_j/s_i>=2`，非投影 leakage 保持有利符号。

对单站点 actual 条件概率 `q` 和 reference 条件概率 `r`，先保留好坏两项再平均，
得到正文的补偿项，而不是分别取绝对值。odds ratio squeeze 给式 (6.4)。与 pair
的 `R^2` 支付、单点 Fisher 的 `R^(-2)` 下界拼接后，两个 transport 因子正确抵消，
得到式 (6.7)。

### 1.6 三点 Fisher、标量包络和最终常数

中心两邻点相距 2，sine kernel entry 为零，所以邻点边际独立。四种外部配置完整
进入 `d3(a)`；正文的 `D02+D1` 分解及分母正性给

\[
d_3(a)>63/10.
\]

`n-2` 个三点窗加两个单点边界给
`d_n^loc>=63/10-23/(5n)`。count-gauge 标量包络的有理常数复算后给

\[
\frac{\mathcal C_n}{n}
\le\frac{110333}{166400000}
+\frac{69}{800000n}+\mathcal E_n,
\]

从而得到所声称的 limsup。这里接受的 `B16,gamma16,c16` 仍只是 PR46/PR51
已审接口；本轮没有重跑原 S64 的 n=15/16 全枚举，也没有把旧日志冒充新运行。

## 2. 20.75 条件的准确地位

若某个固定奇数窗口能在整个实际 chord 上证明中央局部对角 Fisher

\[
d_m(a)\ge83/4,
\]

则用 `n-m+1` 个内部窗和至多 `m-1` 个单点边界，正文式 (9.1) 的蕴含成立。
精确代数给条件上界

\[
\frac{65249}{166400000}=0.000392121394230769\ldots
\]

以及大于 `4.9e-7` 的正 gap。

但是 `83/4` **没有被证明**。正文给出的朴素统一上限约为
`21.56406887024495`，目标已达到该上限的约 96.2%。独立的全配置 L-ensemble
浮点诊断得到中点值：

| m | 3 | 15 | 17 | 19 | 21 |
|---:|---:|---:|---:|---:|---:|
| `d_m(.025)` | 6.30246 | 8.87010 | 8.96235 | 9.04440 | 9.10122 |

这些值不是区间证书，不能严格否定 20.75；但它们说明当前没有“大几个窗口即可
达到条件”的计算证据。条件推论可以接受，条件本身必须保持 `UNVERIFIED`。

## 3. PR51 障碍能否迁移

不能直接迁移。

PR51 的障碍冻结了旧的 `kappa=3/2`、最坏 likelihood transport 和
diagonal-only square allocation，证明在那些常数下只增大 Fisher 窗口仍有严格
floor。续稿通过共同 count gauge 把残余 transport 从一阶降到二阶，并在实际律下
合并好坏单点项；式 (9.1) 的标量常数因此不是旧架构常数。旧定理不蕴含新条件
不可能。

反过来，避开旧定理也不意味着新条件可达。上面的窗口诊断只增长到约 9.10；
所以合理结论是“旧障碍不适用，新充分条件仍无证据”，而不是“障碍已被解决”。

## 4. 独立复现

在隔离副本中执行：

* `verify_exact.py`：标准库 exact rational 检查全部通过，独立复得 U、A 上界、
  未支付缺口、条件 20.75 的蕴含及 32 个精确矩阵/配置恒等式；
* `check_small_actual_sine.py`：隔离 Python 初次因可选 `mpmath` 缺失而诚实返回
  `SKIPPED`；在复现目录安装 `mpmath 1.4.1` 后重跑，n=2,4,6 的全部 84 个
  配置记录通过，状态保持 `PASS_DIAGNOSTIC_NOT_CERTIFICATE`；
* 独立 L-ensemble 枚举脚本覆盖每个外部占据集，得到上表及 a=.02,.03 的对称
  诊断值；它不作为定理接受门槛。

两个稿件文件逐字节相同，确为同一续稿副本。没有使用 hash、旧 PASS 字样、ZIP
或作者运行时间作为数学验收门槛。

## 5. 最终范围

接受：新的固定 benchmark 实际律 acceleration limsup 上界、count-gauge
odds-width 工具、补偿 resolvent 分配、显式不交换边界，以及 20.75 的条件蕴含。

不接受为已完成：20.75 实际 Fisher 下界、固定 benchmark 的正熵率弦、整个
`[.02,.03]` 的所有弦、任意其他 `rho/c/a`，或 `c in (37/40,1)` 的主目标。

最终状态：**续稿数学在明示范围内 VERIFIED_SCOPED；主目标 INCOMPLETE。**

