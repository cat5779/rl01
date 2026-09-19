# S69 Cycle18 独立数学与证书审查

审查日期：2026-09-19（Asia/Singapore）

## 总裁决

**`VERIFIED_SCOPED_AFTER_REPRODUCTION_REPAIR / FULL TARGET INCOMPLETE`。**

S69 的数学结论在下列冻结作用域内成立：固定

\[
\rho=\frac13,\qquad c=\frac{19}{20},\qquad
K=\left[\frac1{50},\frac{51}{2000}\right]=[0.02,0.0255].
\]

对每个整数 `n>=22` 和每个 `a in K`，

\[
H_n''(a)\le-\frac n{1000}+399.
\]

因此该真实完整配置熵率在 `K` 上满足系数为 `1/2000` 的严格弦隙：

\[
\operatorname{Gap}_\lambda h_{1/3,19/20}
\ge \frac1{2000}\lambda(1-\lambda)(a_1-a_0)^2.
\]

这把已经接受的 S63 区间 `[0.021,0.024]` 扩张到 `[0.02,0.0255]`；S63 在原区间上的更强模数不受影响。S69 没有解决完整目标 `[0.02,0.03]`，剩余区间是 `(0.0255,0.03]`。

第二个结论同样成立，但必须严格按证明架构解释：在 `a=0.026`，同一个 22 点最近邻 PSD 分配即使把局部二向量测试函数优化到实际 score，也仍有

\[
P_{\max}^{22}-(C^\dagger-1)d
\le-0.09633473233730599320.
\]

所以“只更换测试函数”不能把这个固定 22 点最近邻框架推进到 `0.026`。这不是熵率非凹反例，也不排除更大的窗口、更尖锐的全局 cap 或包含新边类的分配。

交付的并行重跑程序有一处可复现性缺陷：`payment_prepare_s69.cpp` 只在主线程设置 `FE_UPWARD`。同一 GCC 16.2/libgomp 环境下，8 线程探针得到 `workers=8, bad=7`，即七个工作线程没有继承向上舍入。本审查没有假定这一缺陷无害，而是在隔离副本中把每个相关并行区显式设置为 `FE_UPWARD`，再从 22 点全律重跑支付链。修复版产生的八组外向整数盒、九个公开系数盒和全部 Bernstein 证书与交付件逐字一致。因此数学结论通过，但原始 `run_from_scratch.sh` 在声称满足其自定舍入前提前需要这项小修复。

本审查不认证外部新颖性。

## 逐项裁决

| 对象 | 裁决 | 说明 |
|---|---|---|
| 全局条件 pair cap | VERIFIED | 1100 个闭参数单元、874,402 个区间盒全部通过 |
| 256 个 guard 的全区间证书 | VERIFIED | 从头重跑全部 11 个单元，共 2,816 个 word/cell、124,064,516 个分支盒 |
| 最近邻 PSD 与不重复计费 | VERIFIED | `min delta=6647/20000`，`min(C/2-delta)=4741/40000` |
| 22 点锚点实际律 | VERIFIED | 四个 prefix 覆盖全部 `2^22` 个 word；总质量区间包含一 |
| 移动律 nilpotent 展开 | VERIFIED_AFTER_REPAIR | 显式修复每个 OpenMP 工作线程的舍入模式后重跑 |
| 外向整数提取 | VERIFIED | 八组 `10^15` 分母整数端点与交付件逐字一致 |
| 支付系数与尾项 | VERIFIED | 九个 `10^8` 系数盒一致；尾界 `2.16243e-7<1e-6` |
| 两段 Bernstein 正性 | VERIFIED | 最小系数约 `1.72279e-5` 与 `3.37816e-6` |
| `P<19` | VERIFIED | `P<=18.67215583` |
| 有限体积结论 | VERIFIED | `n-21` 个窗口与边界支付给出 `-n/1000+399` |
| 熵率弦隙 | VERIFIED | 先积分有限体积曲率，再除以 `n` 取函数值极限；没有交换导数与极限 |
| `a=.026` cap/guard/PSD 合法性 | VERIFIED | 100 个 cap 单元、全部 256 个 guard、精确 PSD 全通过 |
| `a=.026` score-matched 上界 | VERIFIED_SCOPED | 覆盖全部 `2^22` 个 word，只否定固定分配中的 test-only repair |
| 三点 frame 引理 | PROVED_ALGEBRAIC / UNINSTANTIATED | 计数与 PSD 条件正确，但没有 distance-two guard、`gamma` 和支付证书 |
| 完整 `[.02,.03]` | INCOMPLETE | `(0.0255,0.03]` 未闭合 |

## 1. 审查范围与证据纪律

审查对象是 `S69_delivery/` 的全部 85 个文件，包括：

- `RESULT.md` 与 `README_CERTIFICATES.md`；
- 全部 C++/Python 验证器；
- `alpha60.txt`、256 组 guard cap、原始整数提取、支付系数和 Bernstein 列表；
- 全部随附日志与 `run_from_scratch.sh`。

没有把 checksum、manifest 或作者日志中的 `PASS` 字样当成证明前提。旧 S63 理论接口按任务要求接受，但本次从头重算了全部 11 个 guard 单元，而不是只复用其中六个。

## 2. 独立工具链与重放

隔离副本使用：

- GCC 16.2.0；
- Boost 1.92.0；
- `-O3 -frounding-math -ffp-contract=off -std=c++17`；
- OpenMP 程序再加 `-fopenmp`；
- 64 位 significand 的 x86 `long double`。

十个 C++ 程序全部从源代码重新编译。全局 cap 主程序重放结果为 1100/1100 单元通过、874,402 个节点。guard 主程序从头覆盖 11 个单元：

```text
SUMMARY passed 2816 failed 0 nodes 124064516
GUARD LOG CHECK ALL PASS cells [0,...,10] words 2816
```

四个锚点 prefix 各生成 1,048,576 个概率记录，合计覆盖全部 4,194,304 个配置。支付准备给出

```text
mass in [0.999999999999731229642468,
         1.00000000000026888007879]
|V0|_inf < 1500, |V1|_inf < 10000.
```

修复并行舍入后，`k=0,...,7` 的全向量推进和外向整数提取重新运行。所得 `raw_integer_s69_0.txt` 至 `raw_integer_s69_7.txt`、`payment_coefficients_s69_integer.txt` 与 `bernstein_payment_s69.txt` 都与原交付逐字一致。

## 3. 并行舍入缺陷与审查者修复

`cert_interval.hpp` 的公开算术模型要求向上舍入。guard、score ceiling、payment sum 和整数提取的并行区都显式调用 `fesetround(FE_UPWARD)`；`payment_prepare_s69.cpp` 的并行区没有。`payment_step_s69.cpp` 的两个独立 `parallel for` 也只依赖前一个 parallel region 留下的线程状态。

同工具链探针结果：

```text
OPENMP_FENV workers 8 bad 7
```

审查者隔离修复做了两件事：

1. 把 `payment_prepare_s69.cpp` 的 `parallel for` 改为显式 parallel region，在每个 worker 进入时调用 `fesetround(FE_UPWARD)`；
2. 对 `payment_step_s69.cpp` 的演化和缩放并行区作同样处理。

修复没有改变任何数学公式、输入、分割或公开阈值。浮点端点只在末尾若干位发生预期变化；向外取整后的所有整数端点完全相同，最终有理闭包完全相同。

因此此问题是**源包重跑脚本的可复现性缺陷**，不是已发现的定理反例。原始源包应补上 worker 级舍入设置后再宣称未经修改的全自动重放满足自身算术模型。

## 4. 全局 cap、guard 与 PSD

新仿射 cap 是

\[
\bar C(a)=\frac{6501}{5000}+\frac{2067}{400}a.
\]

全局程序在 `K` 的 1100 个闭子区间上覆盖完整可行 odds-ratio 区域。guard 程序读取同一组 256 个 `(L_z,U_z)`，11 个参数单元共同覆盖整个 `[.02,.0255]`。旧六单元的假设没有因新 cap 改变：guard 上界只依赖固定 `rho,c,a` 单元和 guard-cap 数据；新 cap 只进入后续 PSD/分配检查。

精确端点运算给出

\[
\delta_z\ge\frac{6647}{20000},\qquad
\frac{\bar C}{2}-\delta_z\ge\frac{4741}{40000}.
\]

所以每个 `2x2` edge matrix 都严格 PSD。连续最近邻边使每个内部站点恰好收到两份 `C/2`，边界站点只会少收，未重复使用 diagonal Fisher 预算。

## 5. 22 点移动律支付

锚点 `a_*=1/40` 的全部 22 点概率由 checked 192-bit fixed-point 主子式枚举重建。公共平移满足

\[
p_{a_*+h}=e^{hD}p_{a_*},\qquad D_i^2=0,
\]

并以 `t=200(a-a_*)` 展开。程序保留整条 4,194,304 维概率向量，没有稀有 word 截断。

重放产生的公开系数盒是：

```text
k : lower, upper  (denominator 10^8)
0 : 1770373694, 1770373697
1 :  -81934787,  -81934784
2 :  -14609597,  -14609594
3 :    -295650,     -295647
4 :       1741,        1744
5 :         -2,           1
6 :         -2,           1
7 :         -1,           2
8 :         -1,           2
```

全向量尾界为

\[
1550\frac{(11/50)^8}{8!}\frac1{1-(11/50)/9}
=\frac{6645125311}{30730000000000000}<10^{-6}.
\]

对 `t<=0` 的左段按幂次奇偶选择安全系数端点，对 `t>=0` 的右段取全部下端点。乘正分母后得到两个 12 次有理多项式；它们的 Bernstein 系数全部严格为正，最小值分别是

\[
\frac{129209164651}{7500000000000000}>0,
\]

\[
\frac{1621518449149069788538367}
{480000000000000000000000000000}>0.
\]

这证明

\[
P(a)-(\bar C(a)-1)d(a)\ge\frac1{1000}
\quad(a\in K),
\]

同时 `P(a)<19`。

## 6. 有限体积与熵率接口

长度 `n` 中恰有 `n-21` 个 22 点窗口，因此

\[
\begin{aligned}
H_n''(a)
&\le n(\bar C-1)d-(n-21)P\\
&=-n\{P-(\bar C-1)d\}+21P\\
&\le-\frac n{1000}+399.
\end{aligned}
\]

熵率结论的传递方式正确：对有限体积二阶不等式沿弦积分，除以 `n`，再用平稳过程块熵的函数值极限。证明没有声称 `H_n''/n` 收敛，也没有把函数值的 `o(n)` 误微分。

## 7. `a=.026` 架构障碍

在 `[.0255,.026]` 上使用

\[
C^\dagger=\bar C+\frac1{1000}.
\]

独立重放得到：

- global probe：100 个单元、33,134 个节点通过；
- guard probe：256 个 word、12,118,054 个节点通过；
- 精确 PSD 检查通过；
- `a=.026` 的全部 4,194,304 个配置重新生成，总质量区间包含一。

因为 `B_z` PSD，对任意 22 点 word 的二向量函数 `f`，

\[
2Z_A^TB_zf-f^TB_zf
=Z_A^TB_zZ_A-(Z_A-f)^TB_z(Z_A-f)
\le Z_A^TB_zZ_A.
\]

所以 `f=Z_A` 给出固定分配内所有二向量测试的最大值。外向重放得到

\[
P_{\max}^{22}\le17.56799346358776726593,
\]

\[
(C^\dagger-1)d\ge17.66432819592507325913,
\]

从而差值上端严格小于 `-0.09633473233730599320`。

这只说明该固定 22 点最近邻架构至少还缺 `0.096334732337306` 的新资源。它不是实际熵曲率的下界，不能解释为熵非凹。

## 8. 三点 frame 引理

三点矩阵取对角 `q=C/3`、两个最近邻项 `delta_i/2,delta_{i+1}/2` 和一个距离二项 `gamma_i`。计数正确：每点进入三个 triple、每条最近邻边进入两个 triple、每条距离二边只进入一个 triple。因此在逐点 PSD 和 endpoint-excluding guard 条件下，不重复计费的 conditional-score Jensen 接口成立；给出的三阶行列式公式也正确。

但 S69 没有提供距离二 guard、`gamma_i` 的合法下界或新支付证书。该引理只能记为已经证明的代数接口，不能把 `[.02,.0255]` 再向上扩张。

## 9. 昨日目标是否解决

- 若“昨日问题”指在固定 `rho=1/3,c=.95` 下把已认证区间从 `[.021,.024]` 扩到包含 `a=.02` 并越过 `.024`：**已解决到 `[.02,.0255]`**。
- 若指完整 `[.02,.03]`：**没有解决**；结论仍是 `INCOMPLETE`。
- `a=.026` 的失败只定位了当前证明架构的第一处硬障碍，没有给出熵率反例。

下一步必须改变至少一种资源：更大的条件 score 窗口、更尖锐的全局 cap，或带距离二/其他边类且有完整 guard 与支付证书的 PSD frame。

