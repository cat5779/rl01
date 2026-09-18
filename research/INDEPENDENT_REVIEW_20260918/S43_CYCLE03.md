# S43 Cycle 03 独立数学审查报告

## 总评

- **原稿读取完整性：COMPLETE_SOURCE_REVIEW。** 初次取得的 `S43_PARTIAL.md` 在第 5.2 节截断；随后先取得完整可见的补证明，再取得原始完整 `S43_RESULT.md` 与原附件版 `S43_CYCLE03_MISSING_PROOF.md`。原主稿第 6–9 节已直接核对，不再存在 count-Stein 来源缺失；没有读取哈希文件。
- **实际 `B_m` 符号质量：VERIFIED_SCOPED。** 实际二阶计数核具有精确 `+,-,+` 符号型，且

\[
 \frac1n\sum_l(\kappa_l)_+\longrightarrow
 M_b=\frac{2e^{-1/2}}{\sqrt{2\pi}\,b}.
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
- **条件赔率与 count-Stein 曲率：VERIFIED_SCOPED。** 潜变量条件 Bernoulli 分部积分给出精确二阶 Stein 恒等式；DPP 条件赔率的 log-submodularity、邻点协方差和 logit 响应共同导出

\[
 -L_c\le\liminf \frac1n\sum_l\kappa_l\mathscr F_l
 \le\limsup \frac1n\sum_l\kappa_l\mathscr F_l\le-A_c,
\]

补发正文中的不等式方向、`16/pi^4` 来源和 `L_c` 两项均正确。
- **actual-count/field 转换：VERIFIED.** 式 (16) 精确区分共同平移参数 `a` 与平衡参数 `c`；式 (18) 的 KL 链式分解把 count-only 修正隔离出来。中央局部极限和统一可积性给 `R_n''(0)=o(n)`，平衡 score 项也仅为 `O(sqrt(n))=o(n)`，故

\[
 \sum_l\kappa_l\mathscr F_l
 =\frac{\mathcal D_n''(0)}{b^2}+o(n).
\]

- **端层和最终装配：VERIFIED_SCOPED。** 四个规定端层的 heat/Gibbs 律均为均匀律，所有四个账本量为零；实际 `kappa` 尾、evidence 和输出 KL 预算覆盖其余全部层，没有丢失中央或边界项。
- **最终负上包络及 `-W_n=Theta(n)`：VERIFIED_SCOPED。** 在 `c=19/20`，解析界直接证明 `A_c-M_bD_c>0`，从而

\[
 \limsup W_n/n\le-2.689614884862\ldots<0,
 \qquad -W_n=\Theta(n)
\]

沿充分大的偶数 `n` 成立；不声称 `W_n/n` 极限存在。
- **未发现反例：NO_DISPROOF。** 补发证明中的承重恒等式均可从冻结模型逐式推出。
- **作用域：CORRECTED_LAW_ONLY。** 该结论不决定 `W_n+C_n`，也不推出真实输出或 sine-Toeplitz 熵率凹性。

## 1. 审查材料与证据边界

主审材料：

1. 原始完整主稿 `C:/game/gameproject/showa100/math/rl01-sa-cycle04-20260918/research/CYCLE04_20260918/recovered/S43_cycle03/S43_RESULT.md`（36,587 字节）；
2. 原附件版 `C:/game/gameproject/showa100/math/rl01-sa-cycle04-20260918/research/CYCLE04_20260918/recovered/S43_cycle03/S43_CYCLE03_MISSING_PROOF.md`（16,369 字节）；
3. 初次取得的 `C:/game/gameproject/showa100/math/rl01-sa-cycle04-20260918/research/CYCLE04_20260918/S43_PARTIAL.md`；
4. 带获取说明的补发稿 `C:/game/gameproject/showa100/math/rl01-sa-cycle04-20260918/research/CYCLE04_20260918/S43_CYCLE03_MISSING_PROOF.md`。

首份文本共 791 行，在

> “the number of ordered triples is Theta...”

处中断。后来取得的原始完整主稿直接包含第 6–9 节；补证明版把这些段落重排并展开中间代数。本报告把两者都当作作者证明而非独立证书，数学状态仍来自逐式独立检查；完整文件的到达本身没有触发结论升级。

### 1.1 原主稿与补证明的一致性

**状态：NO_SUBSTANTIVE_CHANGE。**

逐段映射如下：

- 原主稿 §§6.1–6.3 对应补证明的 Gibbs 层正则性、式 (16) 的实际计数微分以及 count-only correction；
- 原主稿 §§7–7.1 对应补证明的有限 count-Stein、条件赔率和 Fourier 邻点严格性；
- 原主稿 §§8–9 对应补证明的输出 KL 预算、端层装配与解析正 margin。

补证明把 Stein 部分移到转换之前，并显式写出有限 `n` 曲率区间、端层说明及若干中间等式。两份文本的 `Q, mathcal D_n, W_n^G, A_c, L_c, M_b, D_c` 定义、偶数 `n` 量词和最终区间完全一致，没有新增前提或改变结论。

原附件版式 (30) 中 `\\rm even` 被文件转义成一次行内回车，属于 TeX 排版损伤；原主稿 (0.1)、(0.3) 和相邻文字均清楚写明沿偶数 `n`。本报告使用原主稿的无损量词，不把该排版问题记为数学缺口。

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
 \frac1n\sum_l(\kappa_l)_+\to
 2\max g_b
 =\frac{2e^{-1/2}}{\sqrt{2\pi}\,b}=M_b.
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
 \frac{\operatorname{Var}_HR}{n}\to
 v_H=\frac b4-\frac{c^2\log c}{8}.
\]

Poisson-binomial 的统一局部 CLT 与熵尾一致可积性给

\[
 H(p_l^H)=\frac12\log(2\pi e\,n v_H)+o(1).
\]

把 Gibbs 全局负对数展开对热律积分，均值的 `O(1)` 位移在 `sqrt(n)` 尺度消失，得到

\[
 D(p_l^H\Vert q_l^G)\to
 \frac12\left(\frac{v_H}{v_G}-1-\log\frac{v_H}{v_G}\right)
 =D_c.
\]

其中

\[
 \frac{v_H}{v_G}
 =1-\frac{c^2\log c}{2b}=\rho_c.
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
 [\operatorname{Var}_HR-\operatorname{Var}_GR]
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

## 10. 补发的 count-Stein / Gibbs 曲率

**状态：VERIFIED_SCOPED。**

### 10.1 潜变量 Bernoulli 分部积分

定义联合 Gibbs 场

\[
 Q(S)=\pi_{|S|}\gamma_{|S|}(S)
 =b^kz^{-|S|/2}\det\Lambda_S.
\]

Cauchy–Binet 给出等价生成方式：先取投影 DPP 的潜在 \(k\)-集 \(A\)，再令各位在 \(A\) 内以 \(p\)、在 \(A^c\) 内以 \(q\) 独立取一。给定 \(A\) 后，每位方差都等于 \(b=pq\)，而条件均值之和恒为 \(k\)。因此对任意立方体函数 \(f\)，

\[
 E_Q[Xf]=b\sum_iE_Q\partial_i f,
 \qquad X=N-k.
\]

对 \(Xf\) 再应用一次，并使用逐点恒等式

\[
 \partial_i(Xf)=X\partial_i f+f(Y^i),
\]

得到

\[
 \operatorname{Cov}(X^2,f)
 =b^2\sum_{i\ne j}E\partial_{ij}f
 +bE\mathcal Lf.
\]

这里没有把潜变量混合误当成独立场；分部积分是在给定 \(A\) 后成立，再对 \(A\) 平均。

### 10.2 条件赔率响应与曲率恒等式

对计数倾斜

\[
 Q_t=\frac{e^{tX}Q}{E_Qe^{tX}},
 \qquad
 \mathcal D_n(t)=D(Q_t\Vert\operatorname{Ber}(m_t)^{\otimes n}),
\]

有 \(m_0=1/2\)、\(m'_0=b\)，且对称性给三阶中心矩为零。直接微分

\[
 \mathcal D_n(t)=nH_{\rm Ber}(m_t)-H(Q_t)
\]

得到

\[
 \mathcal D_n''(0)
 =\operatorname{Cov}(X^2,\log Q)+nbc^2.
\]

令

\[
 r_i=Q(Y_i=1\mid Y_{-i}),\quad
 h_i=\log\frac{r_i}{1-r_i},\quad
 x_i=2r_i-1,\quad
 v_i=E[r_i(1-r_i)].
\]

潜变量表示立即给 \(q\le r_i\le p\)。正定 \(L\)-ensemble 的 Schur 补公式给

\[
 \partial_jh_i
 =\partial_{ij}\log Q
 =\log\left(1-\frac{|M_{ij}|^2}{M_{ii}M_{jj}}\right)\le0.
\]

翻位生成元逐条件平均又给

\[
 E\mathcal L\log Q=-\sum_iE[x_ih_i].
\]

故

\[
 \mathcal D_n''(0)
 =b^2\sum_{i\ne j}E\partial_jh_i
 -b\sum_iE[x_ih_i]+nbc^2.
\]

承重赔率响应恒等式也成立：

\[
 b\sum_{j\ne i}E\partial_jr_i
 =\operatorname{Cov}(N,r_i)=b-v_i.
\]

其中 \(E[X Y_i]=b\) 来自第一次 Stein 恒等式，而

\[
 \operatorname{Cov}(N,Y_i-r_i)=E[r_i(1-r_i)]=v_i.
\]

由于 logit 导数在 \([q,p]\) 上介于 \(4\) 与 \(1/b\)，且所有 \(\partial_jr_i\le0\)，

\[
 \frac1b\partial_jr_i\le\partial_jh_i\le4\partial_jr_i.
\]

上侧结合 \(4b+c^2=1\) 与

\[
 x\log\frac{1+x}{1-x}\ge2x^2
\]

得到

\[
 \mathcal D_n''(0)\le-b\sum_iE x_i^2.
\]

下侧使用 \(v_i\le1/4\) 及 \(x_ih_i\le c\log(p/q)\)，得到

\[
 \mathcal D_n''(0)
 \ge-n\left(\frac{c^4}{4}+bc\log\frac pq\right).
\]

每一步的不等式方向都与负增量 \(\partial_jr_i\le0\) 相容；未发现符号翻转。

### 10.3 邻点协方差产生 \(A_c\)

该场的 \(L\)-矩阵是 \(z^{-1/2}\Lambda\)，对应 DPP 核

\[
 K=qI+cP.
\]

所以

\[
 \operatorname{Cov}(Y_i,Y_j)=-c^2|P_{ij}|^2.
\]

对循环相邻点，

\[
 |P_{i,i+1}|=\frac1{n\sin(\pi/n)}.
\]

又 \(r_i=E(Y_i\mid Y_{-i})\)，故

\[
 \operatorname{Cov}(Y_i,Y_j)=\operatorname{Cov}(r_i,Y_j).
\]

Cauchy–Schwarz 与 \(\operatorname{Var}(Y_j)=1/4\) 给

\[
 E x_i^2=4\operatorname{Var}(r_i)
 \ge16\operatorname{Cov}(Y_i,Y_j)^2
 =\frac{16c^4}{n^4\sin^4(\pi/n)}.
\]

因此有限 \(n\) 即有

\[
-\left(\frac{c^4}{4b^2}+\frac cb\log\frac pq\right)
\le\frac{\mathcal D_n''(0)}{nb^2}
\le-\frac{16c^4}{bn^4\sin^4(\pi/n)}.
\]

这逐项解释了

\[
 L_c=\frac{c^4}{4b^2}+\frac cb\log\frac pq,
 \qquad
 A_c=\frac{16c^4}{b\pi^4}.
\]

## 11. actual-count / field 转换

**状态：VERIFIED。**

### 11.1 Gibbs 层正则性

补发稿所用的 Gibbs overlap 均值、方差和人口二阶差分正是前文已核验的输入。Fourier 补集恒等式给

\[
 a_n^\circ(h,j)=a_n^\circ(k-j,k-h).
\]

在中心对角线上，这使序列关于位移 \(t\) 为偶函数。二阶差分 \(O(n^{-1})\) 因而先给首增量 \(O(n^{-1})\)，再求和得到 \(O(t^2/n)\)。以 Gibbs overlap 的均值替换随机 overlap 只支付方差乘二阶差分，即 \(O(1)\)。

实际计数律在固定宏观带内作指数倾斜后，各 Bernoulli 参数统一远离 \(0,1\)，倾斜中心质量为 \(\Theta(n^{-1/2})\)。率函数二阶导为 \(O(n^{-1})\)。这些事实与相邻二项式比率一起给

\[
 |\mathscr F_l-\mathscr F_k|
 \le C\left(1+\frac{(l-k)^2}{n}\right).
\]

宏观带外，右端已经是 \(O(n)\)，而 \(0\le\mathscr F_l\le n\log2\)，所以同一包络确实覆盖全部层。

### 11.2 两个参数方向没有混淆

共同平移参数 \(a\) 的一阶 score 是 \(X/b\)。在 midpoint 对 \(a\) 再微分，其 score 导数为

\[
 -\frac nb+\frac{2c}{b}T,
\]

其中 \(T\) 是保持平均计数不变的平衡 \(c\)-score。由此精确得到

\[
 \kappa_l
 =\left(\frac{(l-k)^2}{b^2}-\frac nb\right)\pi_l
 +\frac{2c}{b}\dot\pi_l.
\]

对固定高、低两组 Bernoulli 位，\(T\) 的方差为 \(n/(4b)\)。因此 Cauchy–Schwarz、全层前缀界和实际计数四阶矩给

\[
 \left|\sum_l\dot\pi_l\mathscr F_l\right|
 \le\sqrt{\frac n{4b}}\,
 \left[E_\pi(\mathscr F_N-\mathscr F_k)^2\right]^{1/2}
 =O(\sqrt n)=o(n).
\]

所以式 (16) 并未把 \(a\)-导数偷换成 \(c\)-导数；二者差异被显式 score 项支付。

### 11.3 count-only 修正确为 \(o(n)\)

计数倾斜不改变给定 \(N=l\) 时的条件律 \(\gamma_l\)。Bernoulli 产品参考在给定计数后则是均匀切片律。因此 KL 链式法则精确给

\[
 \mathcal D_n(t)
 =E_{\pi_t}\mathscr F_N+R_n(t),
\]

\[
 R_n(t)=D(\pi_t\Vert\operatorname{Bin}(n,m_t)).
\]

有限求和直接微分得到

\[
 R_n''(0)
 =\operatorname{Cov}\left(
 X^2,\log\frac{\pi_N}{\operatorname{Bin}(n,1/2)(N)}
 \right)+nbc^2.
\]

在 \(X=\sqrt n\,y\) 的中央格点，

\[
 \log\frac{\pi_l}{\operatorname{Bin}(n,1/2)(l)}
 =-\frac12\log(4b)
 +\left(2-\frac1{2b}\right)y^2+o(1).
\]

宏观带内的倾斜比较给 \(C(1+y^2)\) 包络，带外实际计数概率指数小，因此乘 \(y^2\) 后仍统一可积。由 \(X/\sqrt n\) 的 Gaussian 极限及四阶矩收敛，

\[
 \frac{R_n''(0)}n
 \longrightarrow
 \left(2-\frac1{2b}\right)2b^2+bc^2=0.
\]

综合 score 修正与该 count-only 修正，

\[
 \boxed{
 W_n^G:=\sum_l\kappa_l\mathscr F_l
 =\frac{\mathcal D_n''(0)}{b^2}+o(n).
 }
\]

因此

\[
 -L_c\le\liminf\frac{W_n^G}{n}
 \le\limsup\frac{W_n^G}{n}\le-A_c.
\]

## 12. 端层、实际权重与最终装配

**状态：VERIFIED_SCOPED。**

精确 Bayesian 分解为

\[
 F_l=\mathscr F_l+U_l+v_l.
\]

前文已核验：

\[
 \frac1n\sum_l\kappa_lv_l\to0,
\]

以及

\[
 -M_bD_c
 \le\liminf\frac1n\sum_l\kappa_lU_l
 \le\limsup\frac1n\sum_l\kappa_lU_l
 \le M_bD_c.
\]

补发稿没有引入新的尾假设。宏观带内 \(U_l\) 与 \(|v_l|\) 一致有界；带外的粗 \(O(n)\) 界被

\[
 1+\frac{(l-k)^2}{n}
\]

吸收。实际 \(\kappa_l\) 的四阶尾账本随后给 \(C/K^2\) 补带误差。

四个端层也没有遗漏：在 \(l=0,n\) 时切片为单点；在 \(l=1,n-1\) 时 half-filled 循环对称性使 heat 和 Gibbs 条件律均为均匀律。因此

\[
 F_l=\mathscr F_l=U_l=v_l=0
\]

在四个端层全部成立。中央层通过 \(\sum_l\kappa_l=0\) 减去中央常数，而不是被删除。

最终得到

\[
\boxed{
-L_c-M_bD_c
\le\liminf\frac{W_n}{n}
\le\limsup\frac{W_n}{n}
\le-A_c+M_bD_c.
}
\]

在 \(c=19/20\) 时，完全解析地有

\[
 1<\rho_c<2,\qquad
 D_c<\frac{1-\log2}{2}<\frac16,
 \qquad
 bM_b=\sqrt{\frac2{\pi e}}<\frac12.
\]

再用 \(c^4>4/5\) 和 \(\pi^4<100\)，

\[
 b(A_c-M_bD_c)
 >\frac{16}{125}-\frac1{12}
 =\frac{67}{1500}>0.
\]

故负号不依赖十进制复算。数值上

\[
 A_c-M_bD_c
 =2.689614884862\ldots.
\]

于是对充分大的偶数 \(n\)，

\[
 \frac{A_c-M_bD_c}{2}\,n
 \le -W_n
 \le (L_c+M_bD_c+1)n.
\]

这证明

\[
 \boxed{-W_n=\Theta(n)}
\]

但不证明 \(W_n/n\) 极限存在。

## 13. 最终裁决与剩余范围

本轮逐项状态：

1. 条件赔率响应恒等式：**VERIFIED**；
2. 负曲率常数 \(A_c,L_c\)：**VERIFIED**；
3. actual-count/field 转换式 (16)–(21)：**VERIFIED**；
4. count-only correction \(R_n''(0)=o(n)\)：**VERIFIED**；
5. 实际权重尾、中央层和四个端层：**VERIFIED**；
6. \(c=19/20\) 的负上包络及 \(-W_n=\Theta(n)\)：**VERIFIED_SCOPED**；
7. 被证明为假的承重主张：**NONE / NO_DISPROOF**。

最强可信结论为

\[
\boxed{
 \limsup_{\substack{n\to\infty\\n\ {\rm even}}}\frac{W_n}{n}
 \le-2.689614884862\ldots,
 \qquad -W_n=\Theta(n).
}
\]

仍不推出：

- \(W_n/n\) 极限存在；
- \(W_n+C_n\) 的符号；
- corrected cyclic law 与真实 sine-Toeplitz 输出律等价；
- 一般密度、全合法 \(a\) 的真实熵率凹性。

因此完整原稿与补证明共同消除了原 PR #15 的来源缺口；二者没有实质数学差异，也没有扩大 corrected-law 的既定作用域。
