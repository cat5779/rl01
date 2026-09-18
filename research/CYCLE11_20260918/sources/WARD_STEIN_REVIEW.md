# Ward–Stein PR2 独立审查

审查对象：`randomcat4/dpp-entropy-concavity` PR2，题为 “Research: Ward–Stein averaged budget for the sine curvature kernel”。本报告只审该 PR 实际提交的七个文件及其明确调用的冻结 SA03/V14 接口，不把 QWE02、PR123 或旧 PRO01 审查结论移植到本稿。

## 1. 总裁决

| 主张 | 裁决 |
|---|---|
| 固定计数 common-bias Ward 恒等式及完整二阶质量导数 | `VERIFIED_SCOPED` |
| 正可逆外部生成元、显式 score potential、Bayes 边反转 | `VERIFIED` |
| 有限投影的完整 Shannon Hessian 正 chord 表示 | `VERIFIED_SCOPED` |
| `d=2u delta` 与最终因子 `4` | `VERIFIED` |
| 无限 true-sine 公式 `Gamma=4(1-E B_c)/(1-c^2)` | `VERIFIED_RELATIVE_TO_FROZEN_V14` |
| Section 6 的 cyclic-to-V14 极限及 grouped double-flip tails | `VERIFIED_SCOPED` |
| 标量 envelope、单调性与 `c<=sqrt(3)/2` 正号 | `VERIFIED` |
| `c=19/20` 的正号或阈值改进 | `INCOMPLETE / NOT CLAIMED` |
| 全占据参考的有限 Woodbury 表示和误差式 | `VERIFIED_SCOPED` |
| 32 点 witness 对 universal wordwise closure 的反例 | `DISPROVED`，且证书 `REPRODUCED` |
| `E B_c=b J(c)` | `VERIFIED_EXACTLY` |
| 文中提到但 PR 未提交的其他回归测试 | `EVIDENCE_GAP` |
| 文献新颖性 | `NOT AUDITED / NOT CERTIFIED` |

总的判断是：稿件的有限 Ward–Stein 代数、正生成元和平均 chord 公式成立；Section 6 在其明确冻结的 V14 接口范围内也能闭合，未发现需要后来 S51/S55 才能补上的原始缺口。但是它在平均层面得到的目标与 S51 C1 的 actual-table cross-ratio 目标严格等价，并没有新增一个不同的高对比度判号量。真正新增的是正生成元/显式 potential 的组织方式，以及一个虽严格但目前极慢的有限参考词近似。

## 2. 有限 Ward 账本：没有删掉 moving-law 项

令潜在 spins 满足固定计数 `sum_i X_i=0`，观测通道为

\[
\Pr(S_i=s_i\mid X)=\frac{1+s_i(d_i+cX_i)}2,
\qquad r=c^2.
\]

在共同偏置 `d=0`，固定潜在词的 likelihood score 为

\[
\sum_i\frac{s_i}{1+cs_iX_i}
=\frac{M-c\sum_iX_i}{1-r}
=\frac M{1-r}.
\]

所以实际输出质量满足

\[
\frac{p'_0(s)}{p_0(s)}=\frac M{1-r},
\qquad
\sum_s\frac{p'_0(s)^2}{p_0(s)}=\frac n{1-r}.
\]

坐标质量导数算子彼此交换且单坐标平方为零，故二阶导数是有序双翻位和。直接 likelihood 微分给出

\[
p''_0(s)=\frac{M^2}{(1-r)^2}p_0(s)
-\frac1{1-r}\sum_i p_0(s^i).
\]

因此 Shannon 二阶导数中的 `p'' log p` 没有被 Fisher 项替代或删除。这个核对尤其重要：本稿不是只验证 score 方差后便宣称得到完整 Hessian。

固定中心、只观察外部词时，条件固定计数给出

\[
\frac{w'_0}{w_0}=\frac{M_C+cm}{1-r},
\qquad
m'_0=\frac{c(1-m^2)}{1-r}.
\]

第二式包含 posterior denominator 的移动，方向和系数正确。

## 3. 正可逆生成元与 chord 转换

对实际外部律定义

\[
o_j(s)=\frac{w(s^j)}{w(s)},
\qquad
\lambda_j(s)=1-cs_ja_j(s)=\frac{1-r}{2}(1+o_j(s)).
\]

则

\[
w(s)\lambda_j(s)=w(s^j)\lambda_j(s^j),
\]

所以生成元

\[
(\mathcal A_Cf)(s)=\sum_j\lambda_j(s)[f(s^j)-f(s)]
\]

严格正且对实际外部律可逆。固定计数给出

\[
\mathcal A_CM_C=-2(M_C+cm),
\]

从而 `M_C/[2(1-r)]` 是显式 score potential；这里没有借用未知谱隙或抽象 Poisson 可解性。

令

\[
\kappa_j=-\operatorname{Cov}(X_i,X_j\mid S_C)\ge0.
\]

Bayes 单边更新和 covariance determinant 变换给出

\[
m(s^j)-m(s)=\frac{2cs_j\kappa_j(s)}{(1-r)o_j(s)},
\qquad
\kappa_j(s^j)=\frac{\kappa_j(s)}{o_j(s)^2}.
\]

用 detailed balance 对 `o_j^{-1}` 项反向换边后，严格得到

\[
-\mathbb E[(M_C+cm)f(m)]
=c\mathbb E\sum_j\kappa_j[f]_{m,m^j}.
\]

这一步保留了真实移动权重；把边两端权重冻结会破坏恒等式。审查未发现因子 `1/2`、方向或有序边归一化错误。

## 4. 投影后验几何与完整 Shannon Hessian

对秩 `n/2` 投影 DPP，任意正外场后的潜在 posterior 仍是 Gram 投影。因此

\[
\kappa_j=4|(P_D)_{ij}|^2,
\qquad
\sum_{j\ne i}\kappa_j=1-m^2.
\]

平衡观测核 `K=(I+cJ)/2` 满足

\[
K(I-K)=\frac{1-r}{4}I.
\]

Schur 向量计算给出

\[
q(1-q)=\frac{1-r}{4}(1+\|v\|^2),
\qquad
\|v\|^2=\frac{r(1-m^2)}{1-r},
\]

以及更强的后验区间

\[
|2q-1|\le r,
\qquad |m|\le c.
\]

一次翻位再给出

\[
\kappa_j=\frac{1-r}{r}|v_j|^2.
\]

这些式子的 `r=c^2` 归一化均正确。

对独立坐标偏置先求一阶导，再沿共同偏置求导，外部质量 score 与 posterior derivative 同时保留。负 Hessian 的第 `i` 行和为

\[
R_i=\frac{1+
\mathbb E[(M_C+cm)\operatorname{atanh}(cm)]}{1-r}.
\]

应用上一节的 chord identity，定义

\[
\mathcal B_{i,c}
=c\sum_j\kappa_j
[\operatorname{atanh}(c\,\cdot)]_{m,m^j},
\]

便有

\[
R_i=\frac{1-\mathbb E\mathcal B_{i,c}}{1-r},
\qquad
-\frac4nH''(0)
=\frac4{1-r}\left(1-\frac1n\sum_i\mathbb E\mathcal B_{i,c}\right).
\]

正 budget 是从显式正项中被减去，而不是正耗散下界。因子 `4` 来自原题 kernel-diagonal 位移 `delta` 与 spin bias `d` 的关系 `d=2u delta`；两次求导产生 `4`。稿件对此处理正确。

## 5. Ward–Stein 预算与 S51 C1 的 cross-ratio 完全等价

令

\[
b=\frac{1-c^2}{4}.
\]

由

\[
[\operatorname{atanh}(c\,\cdot)]_{m,m^j}
=\frac c4[\operatorname{logit}]_{q,q^j}
\]

及 `kappa_j=(1-c^2)|v_j|^2/c^2`，逐完整外部词有

\[
\mathcal B_c(z)
=b\sum_j|v_j(z)|^2
[\operatorname{logit}]_{q(z),q(z^j)}.
\]

现在给定除中心和 `j` 外的全部输出。记

\[
\pi_b=\Pr(Y_j=b\mid\text{rest}),
\qquad q_b=\Pr(Y_0=1\mid\text{rest},Y_j=b),
\]

\[
J_j=\operatorname{logit}(q_0)-\operatorname{logit}(q_1)\ge0.
\]

在端点 `Y_j=b` 上，flip odds 为 `o_b=pi_{1-b}/pi_b`，秩一翻位式直接给出

\[
|v_j(b)|^2
[\operatorname{logit}]_{q_b,q_{1-b}}
=o_bJ_j.
\]

按实际条件权重求和后，

\[
\sum_{b=0}^1\pi_bo_bJ_j=J_j.
\]

再对 rest 和 `j` 求和，严格得到

\[
\boxed{
\mathbb E\mathcal B_c=b\,\mathcal J(c),
}
\]

其中 `J(c)` 正是 S51 C1/S55 审查中的 actual-law 条件交叉比总和。因而

\[
\frac4{1-c^2}(1-\mathbb E\mathcal B_c)
=\frac1b-\mathcal J(c).
\]

这是直接条件表计算，不只是因为两种公式碰巧等于同一个 `Gamma`。

必须保留的范围区别是：`B_c(z)` 是给定完整外部词后的 covariance-chord 和；S51 的 `J_j` 定义在删去 `j` 后的二点条件表上。上式只证明实际期望相同，不证明逐 word 对象、分布、尾事件或 pointwise 上界相同。

## 6. Section 6：原始冻结 V14 接口与双翻位尾

本审查读取并核对了原始 `SA03_TRANSPORT.md`、`SA03_VOLUME_LIMIT.md` 与 `SA03_EFFECTIVE_REMAINDER.md` 中实际使用的公式，而不是用后来 S51/S55 的结论替代它们。

### 6.1 原稿实际需要的冻结接口

冻结接口对

\[
K(u,\delta)=I/2+uH+u\delta I,
\qquad \|H\|\le c/2,
\]

给出有限体完整 moving-law 恒等式

\[
\partial_\delta^2\mathbb E\phi(q)|_0
=u^2\mathbb E\overline{\mathcal G},
\]

并把所有一次、二次翻位项保持为同一个 grouped V14 核。原始 volume-limit 附录明确证明的尾部 prototype 包括

\[
|G_{ij}||v_i|^3|v_j|,
\quad |G_{ij}|^2|v_i|^4,
\quad |G_{ij}|^2|v_i|^2|v_j|^2,
\quad |G_{ij}|^4|v_i|^4,
\]

及交换指标版本和 `|d_j|D_{ij}^2`。它没有宣称裸 `sum_{ij}|Delta_jd_i|` 可和。

### 6.2 循环逼近确实满足所需 primitive hypotheses

Ward–Stein 稿取 `n=4L+2` 的半秩 Fourier 投影。零延拓后，矩阵元局部趋于 true sine 投影；`1/d` 条目界给每个固定列统一平方尾，因此固定列范数收敛。结合统一算子范数，得到强算子收敛和中心列的 `ell^2` 收敛。

共同谱隙使 Neumann 余项对全部 `u` 和 sign words 一致。固定阶作用于紧向量族，故强收敛在这些族上一致。于是

\[
\tau_M=\sup_{n,u,z}\sum_{|i|>M}|v_{n,i}|^2\to0,
\]

且每个固定 `i` 的 resolvent 列尾也一致消失。上列四种 prototype 分别由 Cauchy–Schwarz、行平方和，或“先固定较小窗口、再支付 `v` 尾”的两尺度论证控制；`|d_j|D_{ij}^2` 使用原始 V14 的带权尾界。故 Section 6 的结论不是只验证有限条目后便忽略双重和。

### 6.3 熵流和因子四

有限体沿 noise flow 精确满足

\[
u\partial_uH_n(u,\delta)
=-\sum_i\mathbb E\phi(q_i).
\]

路径端点的 spin bias 是 `2delta`，故

\[
\frac{H_n(c,2\delta)}n
=\log2-
\int_0^1\frac1n\sum_i\mathbb E_{u,\delta}\phi(q_i)\,\frac{du}{u}.
\]

对 `delta` 求两次导并使用冻结接口，得到

\[
-\frac4nH_{n,dd}(c,0)
=\int_0^1u\,
\mathbb E\overline{\mathcal G}_{n,u}\,du.
\]

固定窗口的真实概率由 determinant 公式收敛，grouped V14 核又可统一 cylinder 逼近，故右端趋于原 SA03 定义的 true-sine `Gamma(c)`。独立地，一次翻位 Ward–Stein kernel 由 `D_1|v_j|^2` 支配并具有相同的平方尾，因此也可取极限。

裁决为 `VERIFIED_RELATIVE_TO_FROZEN_V14`：有限 entropy-flow 与适配到循环逼近的尾部论证已核对；冻结 V14 的完整 finite-jet 身份仍是明确的输入边界。后来获审的 S51 Cycle 06 和 S55 提供了独立的真熵率/循环传递路线，能再次确认同一对象，但本裁决没有用它们倒填原稿。

## 7. 标量 envelope 与精确证书

由 `sum kappa_j=1-m^2`、`|m|<=c` 和 `atanh(c t)` 的凸 secant，稿件得到

\[
\mathcal B_c(z)\le b(r),
\qquad
b(r)=\max_{0\le x\le r}
\frac{(r-x^2)(\operatorname{atanh}r-
\operatorname{atanh}x)}{r-x},
\quad r=c^2.
\]

写 `x=rt` 后的积分表示逐 `r` 单调；导数分子

\[
1-2rt^2+r^2z^2
\ge1-r(2-r)t^2
\ge(1-r)^2
\]

为正，因此 `b(r)` 单调增加。

随附 Bernstein 脚本仅使用 `Fraction` 算术。独立重放得到：

```text
3/4       997/1000   EXACT_RATIONAL_PASS
361/400   1587/1000  EXACT_RATIONAL_PASS
```

首个证书与单调性给出

\[
\Gamma(c)\ge\frac{3}{250(1-c^2)}>0,
\qquad 0<c\le\sqrt3/2.
\]

这是严格正确但较弱的区间。既有接受基线已到 `c<=37/40`，而 `sqrt(3)/2<37/40`，所以本稿没有提高正号阈值。

在 `c=19/20`，证书只给

\[
-\frac{4696}{195}
\le\Gamma(19/20)
\le\frac{1600}{39},
\]

区间跨过零；该点正号仍未证明。

## 8. 全占据参考、Woodbury 与有效误差

对 true sine 外部算子，令 `a=J_{C0}`。由 `J_Ca=0`、`J_C^2=I-aa^*`，全占据参考逆确为

\[
G_+=\frac2{1-r}(I-cJ_C-raa^*),
\qquad v_+=ca,
\qquad q_+=\frac{1-r}{2}.
\]

对有限窗口中的 holes 集 `D`，`W_D=I-(G_+)_{DD}` 为负定可逆，Woodbury 给出

\[
q_D=\frac{1-r}{2}-ra_D^*W_D^{-1}a_D,
\]

\[
v_{D,j}=ca_j+c(G_+)_{jD}W_D^{-1}a_D.
\]

`Gamma_M^+` 的平均权重是 true `2M` 位边际 `w_M`。全占据 exterior 只用于计算 cylinder function 的连续版本；稿件没有把零概率的无限参考事件当成条件律。

Neumann 两尺度尾给出统一中心列包络 `t_c(M)`。若实际词与参考延拓在窗口内相同，resolvent identity 确有

\[
\|v-\widetilde v\|\le a_0t_c(M),
\qquad
|q-\widetilde q|\le t_c(M)^2.
\]

结合 logit secant 的 `D_1,D_2` 界，得到

\[
|\Gamma-\Gamma_M^+|
\le2a_0WD_1t_c(M)
+(D_1+W^2D_2)t_c(M)^2.
\]

数学上这是 target-independent 的有限表示；但 `t_c(M)` 只有 `exp[-eta_c sqrt(log M)]` 型衰减，且 `c→1` 时常数很大。在 `.95` 没有计算任何能判号的 cutoff 或 `Gamma_M^+`。因此它目前是严格的可计算性接口，不是实用高对比度证书。

## 9. 32 点 pointwise 反例的精确范围

第二个随附脚本使用 `Hadamard(16)/4` 构造

\[
J=\begin{pmatrix}0&U\\U^T&0\end{pmatrix},
\qquad Q=(I+J)/2.
\]

因为 `U` 正交，`J^2=I`；所以 `Q` 是真实的 32 点秩 16 投影，且对角为 `1/2`。脚本以 exact rational Schur inverse 计算 `q,v,q^j`，再用带有有理几何尾的 `atanh` 正项级数作定向包络。

在可用 SymPy 的离线环境中独立重放得到

```text
B in 1.1776728191029975 1.1776728191029975
EXACT: B>117/100>1
```

所以 universal finite-projection wordwise 命题

\[
\mathcal B_{19/20}(z)\le1
\]

被严格反驳。它只否定一般平衡投影类的逐 word closure；不否定 `E_sine B_c<1`，不确定真实 sine 平均的符号，也不是 true-sine `Gamma` 的反例。

## 10. PR 中缺失的 claimed companion checks

PR 实际提交的计算文件只有两个决定性脚本及其 JSON：标量 Bernstein 证书和 32 点反例。稿件 §10 还称已有：

- finite rational Ward/Stein algebra regressions；
- reference inverse、Woodbury、projection energy 和 single-flip endpoint regressions；
- 四点 complex Hermitian conference projection regression。

这些脚本和输出不在 PR 的七个文件中，因此本审查不能把它们记为已独立重放。状态是 `EVIDENCE_GAP`，不是上述解析定理的反例：本报告已直接核对主公式，但不会把未提交的 regression ledger 当作额外证据。

## 11. 相对 S51/S55 的实际新增内容

精确关系 `E B_c=b J(c)` 表明：

- 平均高对比度目标不是新目标；它与 S51 C1/S55 的 actual-law cross-ratio 补偿完全相同；
- `sum kappa=1-m^2`、posterior interval 和投影 Ward 能量主要是同一几何账本的不同组织；
- 不能从期望相等推出 Ward wordwise budget 与 S51 conditional-table integrand 逐点相等。

相对已审工作，本稿真正可复用的新增内容是：

1. 一个严格正、对实际外部律可逆的 generator；
2. 显式 magnetization score potential，而非抽象 Poisson 解；
3. Bayes edge reversal 把 moving-law score 直接变成正 covariance chord 的公式；
4. 变换后只需 single-flip 空间尾的全占据参考有限表示。

标量 envelope 的正号区间弱于既有 `37/40`，不应作为新阈值成果；有限表示因慢尾和巨大 gap 常数，目前也没有实际 benchmark 判号能力。未做文献检索，故不认证这些结构在文献意义上的新颖性。

## 12. 后续研究建议

不要再启动一条只优化 universal wordwise supremum 的路线：32 点证书已经证明该 closure 在一般投影类失败，而当前 scalar envelope 又弱于接受基线。也不必重新推导 `E B_c<1` 与 `b J(c)<1` 的等价性。

Ward–Stein 对未来轮次仍有两个有用输入：

- 将 actual-table 的分布性估计通过 edge reversal 翻译为正 chord/conductance 语言；
- 若能显著改善 `t_c(M)`，用 `Gamma_M^+` 形成真正可执行的有限认证。

当前 S59 已被单独安排研究 actual-table 的分布性符号机制；本审查没有给它追加任务或重启它。最不重复的未来组合方式，是等 S59 产生新的平均不等式后，再用本报告的 `E B_c=b J(c)` 和正 generator 身份作翻译与交叉验证。S60 的 common-shift rank-one Fisher convexity属于另一条接口，不应在本轮强行合并。

最终建议：将 Ward–Stein PR2 归档为 **`VERIFIED STRUCTURAL REPACKAGING / LIVE AVERAGED ROUTE / NO THRESHOLD IMPROVEMENT`**。它值得保留为未来平均法的结构工具，但不应被描述为已经推进 `.95` 正号或提供了新的独立目标。
