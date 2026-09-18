# S43 Cycle 03 独立数学审查报告

## 总评

- **原稿读取完整性：INCOMPLETE_REVIEW。** `S43_PARTIAL.md` 在第 5.2 节人口平均三阶差分证明中截断；transport flatness、count-Stein 曲率、辅助 Gibbs 响应和最终装配均未取得。附件正文也未取得。没有读取哈希文件。
- **实际 `B_m` 符号质量：VERIFIED_SCOPED。** 实际二阶计数核具有精确 `+,-,+` 符号型，且

\[
 \frac1n\sum_l(\kappa_l)_+\longrightarrow
 M_b=\frac{2e^{-1/2}}{\sqrt{2\pi},b}.
\]

四阶矩尾账本和全部补层处理成立。
- **径向 KL 极限：VERIFIED_SCOPED。** 使用已修正的真实初始律强 Rayleigh 论证，热重叠为 Poisson-binomial；实际时钟的均值、方差极限与 Gibbs 局部极限定理给

\[
 D(p_l^H\Vert q_l^G)\longrightarrow
 D_c=\frac12(\rho_c-1-\log\rho_c)
\]

在每个固定 `sqrt(n)` 中央层窗上一致成立，并在固定宏观带内一致有界。
- **带符号三阶 logdet 行和：VERIFIED_SCOPED。** 可见式 (34) 的 masked-matrix-product 证明成立；人口平均确实继承 `O(n^-2)` 的三阶有限差分。
- **heat/Gibbs evidence 的 `sqrt(n)` 层平坦性：VERIFIED_SCOPED（本报告独立重建）。** 三阶差分、两径向律的前三阶矩和统一尾界足够证明

\[
 \sup_{0\le r\le K\sqrt n}|v_{k-r}-v_k|\to0
\]

对每个固定 `K` 成立；其实际计数核加权贡献为 `o(n)`。
- **输出 KL 的带符号预算：VERIFIED_SCOPED。** 不需要 `U_l` 的导数或极限；仅用 `0<=U_l<=D_l`、中央 `D_l->D_c` 和实际核正负质量，即得其归一化贡献落在 `[-M_bD_c,M_bD_c]`。
- **辅助 Gibbs 曲率 `A_c,L_c`：CRITICAL_GAPS（承重证明缺失）。** 可见正文没有 count-Stein 恒等式、没有导出

\[
 -L_c\le\liminf \frac1n\sum_l\kappa_l\mathscr F_l
 \le\limsup \frac1n\sum_l\kappa_l\mathscr F_l\le-A_c,
\]

也没有说明边界项如何支付。仅给出常数定义和作者摘要，不能当作证明；本报告无法从第 1–5.2 节独立恢复这些特定常数。
- **最终负上包络及 `-W_n=Theta(n)`：NOT_REVIEWED。** 它们严格依赖缺失的辅助 Gibbs 曲率证书。当前能认证的是一条条件装配公式，而不是 `limsup W_n/n<=-2.6896...`。
- **作用域：CORRECTED_LAW_ONLY。** 即使缺失曲率日后补齐，也不自动决定 `W_n+C_n`，更不推出真实输出熵率凹性。

## 1. 审查材料与证据边界

主审材料：

`C:/game/gameproject/showa100/math/rl01-sa-cycle04-20260918/research/CYCLE04_20260918/S43_PARTIAL.md`。

可见文本共 791 行，在

> “the number of ordered triples is Theta...”

处中断。作者标题、主定理框和数值常数不是缺页证明的替代品。本报告只使用可见公式、冻结 corrected-law 定义、此前已独立核验的强 Rayleigh 修正及标准有限概率/矩阵工具。

## 2. 实际计数核与 `M_b`

**状态：VERIFIED_SCOPED。**

精确生成函数

\[
 \sum_m\frac{B_m}{n(n-1)}t^m
 =\phi(t)^{k-2}\psi_k(t)
\]

是 `n-2` 个 Bernoulli 概率生成函数的乘积，均值为 `k-1`，方差

\[
 V_B=(n-4)b+2\eta_k.
\]

中心 Fourier 缩放给

\[
 \frac{\kappa_{k-\lfloor x\sqrt n\rfloor}}{\sqrt n}
 \to\varphi_b''(x),
 \qquad
 \frac{w_{k-\lfloor x\sqrt n\rfloor}}n
 \to g_b(x)=-\varphi_b'(x),
\]

且差分乘子分别带 `|u|`、`u^2`，故误差对全部格点有统一可积包络。

`phi` 与 `psi_k` 均分解为正线性因子。正线性卷积具有 variation-diminishing 性质；从 `(1-t)^2` 的两个符号变化出发，`kappa` 至多有两个符号变化。端点为正、序列对称且总和为零，所以忽略零项后的符号型只能是

\[
 +,-,+.
\]

令 `D_m=B_m-B_{m-1}`，则 `kappa_m=D_m-D_{m-1}`。上述符号型使 `D_m` 先升、后降穿零、再升至零，因此

\[
 \sum_l(\kappa_l)_+=2\max_mD_m.
\]

局部极限中 `max g_b` 位于 `x=sqrt(b)`，故

\[
 \frac1n\sum_l(\kappa_l)_+	o
 2\max g_b
 =\frac{2e^{-1/2}}{\sqrt{2\pi},b}=M_b.
\]

本报告以精确有理系数对 `n=8,12,20,40` 重算了符号块、总和为零及下节四阶矩恒等式，均一致；有限数值只作交叉检查。

## 3. 全尾矩账本

**状态：VERIFIED_SCOPED。**

离散两次分部求和确实给

\[
 \sum_l\kappa_l(l-k)^4
 =\sum_mB_m[12(m-k+1)^2+2]
 =n(n-1)(12V_B+2).
\]

负部由符号型和中心局部极限限制在固定 `sqrt(n)` 带中，总变差为 `O(n)`。所以

\[
 \sup_n\frac1n\sum_l|\kappa_l|
 \left(1+\frac{(l-k)^4}{n^2}\right)<\infty.
\]

Markov 型截断即得

\[
 \frac1n\sum_{|l-k|>K\sqrt n}|\kappa_l|
 \left(1+\frac{(l-k)^2}{n}\right)
 \le\frac{C_b}{K^2}.
\]

该式是真实权重的全层尾界，不是 Gaussian 替代权重。

## 4. Bayesian 账本

**状态：VERIFIED_SCOPED。**

辅助 Gibbs 通道的输出律为

\[
 \gamma_l(S)=\frac{\det\Lambda_S}{Z_l},
 \qquad \Lambda=I+(z-1)P.
\]

令

\[
 U_l=D(\mu_l\Vert\gamma_l),
 \qquad
 v_l=E_H\ell(S)-E_G\ell(S).
\]

直接展开得到

\[
 F_l=\mathscr F_l+U_l+v_l.
\]

两个条件通道在重叠壳内均匀，因此联合 KL 精确降为径向 KL，链式法则给

\[
 0\le U_l\le D(p_l^H\Vert q_l^G).
\]

粒子–空穴对称把三个分量都对称延伸到上半层；端层账本为零。没有从 `U_l>=0` 推断其相邻差符号。

## 5. 径向 KL 极限 `D_c`

**状态：VERIFIED_SCOPED。**

### 5.1 Gibbs 径向律

Gibbs 相邻概率比具有固定内部区域内 `-Theta(1/n)` 的对数差。模态与四个人口边界保持线性距离，故模态质量为 `Theta(n^-1/2)`，具有统一 Gaussian 尾和全部 `O(n^{j/2})` 中心绝对矩。

对 `l=k-O(sqrt n)`，鞍点 Hessian 给

\[
 \frac{\operatorname{Var}_G R}{n}\to v_G=\frac b4,
\]

并在标准化有界窗内具有一致 lattice Gaussian 局部极限。全局负对数由中央二次界和外部几何比率拼接支付。

### 5.2 实际热律

真实条件初始律是 `A` 内均匀 `l`-子集，其生成多项式 `e_l(z_A)/binom(k,l)` 实稳定。Borcea–Branden–Liggett 的有限对称排斥保持定理适用于完整图对称交换生成元。把演化后多项式在 `A` 内设为 `1`、外部设为一元变量，得到非正实根的一元概率多项式，所以热重叠正是 Poisson-binomial。

实际时钟恒等式和精确矩方程给

\[
 E_HR-E_GR\to-\frac{c\log c}{4},
\]

\[
 \frac{\operatorname{Var}_HR}{n}	o
 v_H=\frac b4-rac{c^2\log c}{8}.
\]

Poisson-binomial 的统一局部 CLT 与熵尾一致可积性给

\[
 H(p_l^H)=\frac12\log(2\pi e,n v_H)+o(1).
\]

把 Gibbs 全局负对数展开对热律积分，均值的 `O(1)` 位移在 `sqrt(n)` 尺度消失，得到

\[
 D(p_l^H\Vert q_l^G)	o
 \frac12\left(\frac{v_H}{v_G}-1-log\frac{v_H}{v_G}\right)
 =D_c.
\]

其中

\[
 \frac{v_H}{v_G}
 =1-rac{c^2\log c}{2b}=\rho_c.
\]

所有估计在固定中央 `sqrt(n)` 层窗上一致。宏观带内只使用最大质量熵下界和 Gibbs 全局交叉熵界，即可得统一 `O(1)` KL。

## 6. 三阶 logdet 行和

**状态：VERIFIED_SCOPED。**

对 Schur 补作对角归一化后，矩阵 `R` 满足

\[
 z^{-1}I\preceq R\preceq zI,
 \qquad R_{ii}=1.
\]

三点 inclusion–exclusion 差为

\[
 \delta_{ijk}\ell
 =2\Re(R_{ij}R_{jk}R_{ki})+E_{ijk},
\]

且

\[
 |E_{ijk}|\le C_z(
 |R_{ij}|^2|R_{ik}|^2+
 |R_{ij}|^2|R_{jk}|^2+
 |R_{ik}|^2|R_{jk}|^2).
\]

对任意 `J,K`，主项求和是 masked matrix product

\[
 R_{i,*}\Pi_JR\Pi_KR_{*,i},
\]

由算子范数和行 `ell^2` 范数统一控制。三个余项的绝对和分别由 `sum_j|R_ij|^2<=z^2` 支付。因此

\[
 \left|\sum_{j\in J,k\in K}\delta_{ijk}\ell\right|
 \le C_z.
\]

重复指标只损失二阶行和的常数。

## 7. 人口平均三阶差分

**状态：VERIFIED_SCOPED（补完截断句）。**

令 `a_n(h,r)` 为固定 `A` 时对两个人口各自均匀选点后的 `ell(S)` 平均，再对 `A` 平均。均匀子集扩展把每个纯或混合三阶有限差分表示为：在一个基集合外，对三个不同新增点的 inclusion–exclusion 差作平均。

若可选人口均至少为 `epsilon n`，固定第一个新增点 `i` 后，上一节对其余两个新增人口集合的带符号双和为 `O(1)`；再对 `i` 求和，未归一化分子为 `O(n)`。有序三元组总数为 `Theta(n^3)`，故

\[
 |\Delta^3a_n(h,r)|\le C_{z,\epsilon}n^{-2}.
\]

同理，二阶行和除以 `Theta(n^2)` 给 `O(n^-1)`，一阶增量由 `0<=Delta ell<=beta` 控制。可见式 (36) 全部成立。

## 8. evidence 平坦性的独立重建

**状态：VERIFIED_SCOPED（原稿缺页，本报告独立证明）。**

固定层 `l`，令

\[
 f_l(r)=a_n(l-r,r),
 \qquad
 v_l=E_Hf_l(R)-E_Gf_l(R).
\]

在 Gibbs 均值 `mu_l` 处作三阶离散 Taylor。由上一节，内部区域中

\[
 |\Delta f_l|\le C,
 \quad |\Delta^2f_l|\le C/n,
 \quad |\Delta^3f_l|\le C/n^2.
\]

两径向律具有 `O(n^{j/2})` 的前三阶中心绝对矩和统一亚 Gaussian 尾。故 Taylor 余项期望为

\[
 O(n^{-2}n^{3/2})=O(n^{-1/2}),
\]

外部尾由全局 Lipschitz 界支付。于是

\[
 v_l=
 \Delta f_l(\mu_l)(E_HR-E_GR)
 +\frac12\Delta^2f_l(\mu_l)
 [\operatorname{Var}_HR-operatorname{Var}_GR]
 +o(1),
\]

其中离散取整只改变 `o(1)`。

当层从 `k` 移动 `O(sqrt n)`：

- 均值差与归一化方差差由第 5 节一致收敛到同一常数；
- 一阶系数逐层变化由二阶人口差控制，为 `O(1/n)`；
- `n` 倍二阶系数逐层变化由三阶人口差控制，为 `O(1/n)`。

累积 `O(sqrt n)` 层后两种系数变化均为 `o(1)`。因此

\[
 \sup_{0\le r\le K\sqrt n}|v_{k-r}-v_k|\to0.
\]

宏观中央带内已有 `|v_l|<=C`；带外用 `|ell(S)|<=beta n`。把实际 `kappa` 和第 3 节尾界分成 `K sqrt(n)` 中央、宏观带剩余、线性大偏差三块，先令 `n->infty` 再令 `K->infty`，得到

\[
 \frac1n\sum_l\kappa_lv_l\to0.
\]

## 9. 输出 KL 的完整带符号预算

**状态：VERIFIED_SCOPED。**

中央固定窗上 `D_l:=D(p_l^H||q_l^G)->D_c`，且

\[
 0\le U_l\le D_l.
\]

于是正 `kappa_l` 部分对上界最多贡献 `D_c` 乘正质量，负部分因 `U_l>=0` 只会降低；对下界反向使用负质量。结合正负质量都趋于 `M_bn` 以及尾部统一 KL 界，得到

\[
 -M_bD_c
 \le\liminf\frac1n\sum_l\kappa_lU_l
 \le\limsup\frac1n\sum_l\kappa_lU_l
 \le M_bD_c.
\]

这一步不需要 `U_l` 平滑，也不声称其 profile 收敛。

## 10. 缺失的辅助 Gibbs 曲率

**状态：CRITICAL_GAPS。**

要完成作者定理，还必须证明

\[
 -L_c\le\liminf\frac1n\sum_l\kappa_l\mathscr F_l
 \le\limsup\frac1n\sum_l\kappa_l\mathscr F_l
 \le-A_c,
\]

其中

\[
 A_c=\frac{16c^4}{b\pi^4},
 \qquad
 L_c=\frac{c^4}{4b^2}+rac cb\log\frac pq.
\]

可见正文只说明“count-Stein curvature certificate”将完成此事，却在该证明之前截断。缺少至少以下承重内容：

1. 将 `sum kappa_l mathscr F_l` 变成可定号的 Stein/交换恒等式；
2. 产生 `16/pi^4` 的 sine/Fourier 下界；
3. 产生 `L_c` 两项的全局上界；
4. 支付中央原子、端层和宏观带外边界；
5. 证明不等式方向与式 (10) 的符号归一一致。

这些不能由已有的 `O(1+r^2/n)` 前缀界推出：该前缀界只给 `O(n)` 量级，不给负号或常数。也不能从作者列出的十进制值逆向认证。

## 11. 当前可认证的最终装配

令

\[
 G_n^{\mathrm{aux}}=rac1n\sum_l\kappa_l\mathscr F_l.
\]

由第 8、9 节，严格可保留的是

\[
 \limsup\frac{W_n}{n}
 \le\limsup G_n^{\mathrm{aux}}+M_bD_c,
\]

\[
 \liminf\frac{W_n}{n}
 \ge\liminf G_n^{\mathrm{aux}}-M_bD_c.
\]

若未来独立证明第 10 节缺失的辅助曲率界，则作者的区间 (T) 随即成立。当前没有该证明，所以

\[
 \limsup W_n/n\le-A_c+M_bD_c
\]

以及 `-W_n=Theta(n)` 均不能升级为已验证结论。

在 `c=19/20`，常数的数值复算确为

\[
 D_c=0.140983882778\ldots,
 \quad M_bD_c=2.799095159908\ldots,
 \quad A_c-M_bD_c=2.689614884862\ldots.
\]

这只验证算术，不验证缺失的 `A_c` 曲率不等式。

## 12. 最强可信结论与剩余义务

可以认证：

1. 实际二阶计数核的符号型、`M_b` 正质量和全尾矩账本；
2. 径向 KL 在中央窗趋于 `D_c`；
3. 带符号三阶 logdet 行和及人口 `O(n^-2)` 三阶差分；
4. evidence 在 `sqrt(n)` 层尺度平坦，且其实际核响应为 `o(n)`；
5. 输出 KL 响应位于 `[-M_bD_c,M_bD_c]`；
6. 把完整问题约化为单独的辅助 Gibbs 曲率响应。

仍未认证：

- `A_c,L_c` 的 count-Stein 推导；
- `limsup W_n/n<0`；
- `-W_n=Theta(n)`；
- `W_n+C_n` 的符号；
- 真实输出或 Toeplitz 熵率结论。

因此本轮最有价值的新结果是：作者主定理只剩一个清晰、独立且承重的辅助 Gibbs 曲率义务；其余两项误差预算可以闭合。
