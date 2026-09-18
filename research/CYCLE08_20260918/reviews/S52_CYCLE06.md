# S52 cycle06 独立审查：实际输出 Fisher–Bregman 易感性下界

审查对象：`S52_CYCLE06_RESULT.md`、`S52_CYCLE06_checks.py` 与归档输出。

## 1. 裁决

| 项目 | 裁决 |
|---|---|
| 有限偶数 `n` 的 Theorem 1 | `VERIFIED_SCOPED` |
| 无条件下界 `R_n(c) >= -n Phi(c^2)/(2b)` | `VERIFIED` |
| 循环模型渐近改进式 (45) | `VERIFIED_SCOPED` |
| `c=19/20` 数值 | `REPRODUCED` |
| 达到 corrected-law 门槛 | `INCOMPLETE` |
| true Toeplitz 熵率结论 | `NOT CLAIMED / NOT PROVED` |

这里的通过范围是：平衡点上的有限、平衡、循环、秩 `n/2` 投影 DPP 输出律，以及作者稿明确调用的奇偶块接口。它不把有限循环结论升级为 true Toeplitz 熵率结论。

作者稿的主要新结论成立：它把逐边最坏斜率替换为实际输出权重下的条件方格 Bregman 补偿，并用一次精确 Fisher 账本支付正部。所得常数仍离 corrected-law 所需门槛很远，所以作者将整体状态标成 `INCOMPLETE` 是恰当的。

## 2. 模型与归一化

令

\[
H=2P-I,\qquad K_c=\frac{I+cH}{2},\qquad
b=\frac{1-c^2}{4},
\]

其中 `P` 是有限循环模型的秩 `n/2` 投影。对输出 `y`，设

\[
A_y=K_c-\operatorname{diag}(1-y)=\frac{S_y+cH}{2},
\qquad B_y=A_y^{-1}.
\]

因为 `0<K_c<I`，全部精确配置的概率为正，故逆矩阵和对数微分都在有限样本内良定义。稿件使用的两条参数方向必须区分：

- 公共对角方向 `K(a)=K_c+(a-a_*)I`；
- 对比方向 `K_t=(I+tH)/2`。

本审查逐式核对后，未发现两种 Fisher 信息被混用。

## 3. 精确概率与 Fisher 账本

精确配置恒等式

\[
\Pr_K(Y=y)=(-1)^{n-|y|}
\det\!\left(K-\operatorname{diag}(1-y)\right)
\]

给出公共对角 score 和 observed information：

\[
\partial_a\log p_a(y)=\operatorname{Tr}B_y,
\qquad
-\partial_a^2\log p_a(y)=\operatorname{Tr}B_y^2.
\]

谱 Bernoulli 表示给出 Fisher 上界 `n/b`；计数统计量 `N=|Y|` 的 score 协方差与 `Var(N)=nb` 给出反向下界。因此

\[
\mathcal F_{a,n}=\frac nb.
\]

单点对角微分还给出

\[
\mathcal D_n
=\mathbb E\sum_i(B_Y)_{ii}^2
=4\sum_i\mathbb E\frac1{1-x_i^2}.
\]

若

\[
\mathcal O_n=\mathbb E\sum_{i\ne j}|(B_Y)_{ij}|^2,
\]

则 Frobenius 账本精确分解为

\[
\mathcal D_n+\mathcal O_n=\frac nb.
\]

以上推导均是有限 `n` 恒等式，不依赖熵率可微性或极限交换。

## 4. 条件方格与 Bregman 补偿

固定无序对 `{i,j}` 和其余实际输出 `z`，保留四格的全局权重 `p_{11},p_{10},p_{01},p_{00}`，并令

\[
m_z=\sum_{a,b}p_{ab},\qquad
\Delta_z=p_{10}p_{01}-p_{11}p_{00}\ge0.
\]

条件 DPP 的负关联给出

\[
\theta_z=\log\frac{p_{11}p_{00}}{p_{10}p_{01}}\le0.
\]

Desnanot–Jacobi 恒等式逐格给出

\[
|(B_y)_{ij}|^2=\frac{\Delta_z}{p_{ab}^2}.
\]

以归一化后的增益变量 `u_{10},u_{01}` 和损失变量 `v_{11},v_{00}` 表示，可得到精确的一方向差值

\[
\begin{aligned}
&m_z(-\theta_z)-\Delta_z\sum_{a,b}\frac1{p_{ab}}\\
&\quad=m_z\{\Phi(u_{10})+\Phi(u_{01})
-\Psi(v_{11})-\Psi(v_{00})\},
\end{aligned}
\]

其中

\[
\Phi(u)=-\log(1-u)-u,\qquad
\Psi(v)=v-\log(1+v).
\]

符号并非逐点固定。作者给出的四格

\[
(A,B,C,D)=(0.089,0.811,0.011,0.089)
\]

满足 `BC-AD=0.001`，且上式左端严格为正。这直接否定“条件 log-odds 总能由端点 observed Fisher 逐格控制”的点态 ansatz；它不是循环易感性猜想本身的反例。把这个反例直接写入正文是必要的范围控制。

## 5. BSC 上界与一次性支付

平衡核 `K_c=(I+cH)/2` 的输出律可由投影 DPP 经相关系数 `c` 的独立 BSC 得到。对任一实际条件方格，稿件证明

\[
0\le u_{10},u_{01}\le c^2.
\]

由于 `Phi(u)/u` 在 `[0,1)` 单调增加，令

\[
\alpha_c=\frac{\Phi(c^2)}{c^2},
\]

保留负的 `-Psi` 项并只对两个增益格应用端点上界，可得

\[
\Xi_n\le\alpha_c\mathcal G_n,
\]

其中 `G_n` 是异值输出边上的 observed Fisher 质量。

关键账本来自 `S_YB_Y=2I-cHB_Y`。用对比方向的 score 恒等式展开一次，得到

\[
\boxed{
\mathcal G_n
=\frac12\left(\frac nb-4n-4c^2\mathcal F_{H,n}(c)\right).
}
\]

此处 `G_n` 只被代入一次；稿件没有把同一 Fisher 预算既用于局部上界又再次扣除。结合

\[
R_n=\mathcal D_n-4n-\Xi_n
\]

便得

\[
\boxed{
R_n(c)\ge
4\sum_{i=1}^n\mathbb E\frac{x_i^2}{1-x_i^2}
-\frac{n\Phi(c^2)}{2b}
+2\Phi(c^2)\mathcal F_{H,n}(c).
}
\]

前后两个附加项均非负，故无条件地

\[
R_n(c)\ge-\frac{n\Phi(c^2)}{2b}.
\]

系数、方向和 `alpha_c c^2=Phi(c^2)` 的归一化均核对无误。

## 6. 循环渐近改进

奇偶块写成

\[
H=\begin{pmatrix}0&V\\V^*&0\end{pmatrix}.
\]

由接口 `E[x_i | opposite parity]=c^2y_i` 和凸性，作者从对角 Fisher 得到

\[
\liminf\frac{\mathcal D_n-4n}{n}\ge d_3(c),
\]

其中

\[
d_3(c)=4\left(
\frac{c^4}{3}+
\frac{71c^8}{315}+
\frac{24587c^{12}}{155925}
\right).
\]

这里使用的 Rademacher 二、四、六阶矩与幂和常数相互一致。

对比统计量

\[
T_k=\sum_{a=0}^{k-1}S_{E,a}S_{O,a}
\]

的均值导数和方差给出 score-Cauchy–Schwarz 下界。结合

\[
|v_0|^2\to\frac4{\pi^2},\qquad
\sum_d|v_d|^2|v_{-d}|^2\to\frac2{\pi^2},
\]

得到

\[
\liminf\frac{\mathcal F_{H,n}(c)}n\ge f_*(c),
\qquad
f_*(c)=\frac{32c^2/\pi^4}{1+2c^4/\pi^2}.
\]

因此

\[
\liminf_{n\to\infty,\;2\mid n}\frac{R_n(c)}n
\ge d_3(c)-\frac{\Phi(c^2)}{2b}
+2\Phi(c^2)f_*(c).
\]

这是有限循环序列的渐近结论；它没有建立 true Toeplitz 核的熵率极限、极限可微性或从 cyclic 到 Toeplitz 的误差传递。

有一个不影响渐近结论的有限尺寸例外：稿件以 `V^2` 是非平凡循环移位为由把式 (41) 称为精确方差公式，该论证需 `k=n/2>=2`，即 `n>=4`。当 `n=2`、`k=1` 时 `V^2=I`，实际为 `Var(T_1)=1-t^4`，而不是式 (41) 的 `1+t^4`。式 (43)--(45) 只取 `n→∞`，故 `d_3`、`f_*` 和最终渐近下界不受影响。

## 7. 数值复现

以 `c=19/20` 运行脚本，并使用归档所需的 `--enumerate 6` 选项，得到：

```text
b                              0.024375
Phi(c^2)                       1.42540290098
universal lower bound / n    -29.2390338662
d3                             2.02496602538
f*(c)                          0.254478935055
cyclic lower bound / n       -26.4885978163
M_b D_c                        2.79909515991
target threshold              -1.20090484009
remaining gap                 25.2876929762
```

`n=6` 的全配置枚举还在浮点精度内复现了概率和为 1、`F_a=n/b`、两种 gain 计算一致、`D+O=n/b` 与 `R` 的恒等式。这里的“exact cyclic enumeration”是枚举全部 `2^6` 个配置，不是精确有理认证。它是有限尺寸诊断，不证明矩极限或渐近求和；随机 BSC 测试也不替代 Lemma 4.1 的解析证明。脚本默认运行不含枚举，归档输出可由它公开支持的 `--enumerate 6` 选项完整恢复。

## 8. corrected-law 接口与符号

稿件在 §7 只作范围比较，明确另行假设三条接口：作者提交的 `W_n+C_n` 分解、已审 reverse-KL 下包络，以及 count/reference 二阶导公式。按原方向联立，对某个固定 `epsilon>0`、沿偶数 `n` 可得到

\[
\liminf R_n/n\ge M_bD_c-4+\varepsilon
\Longrightarrow
\liminf(W_n+C_n)/n\ge-4+\varepsilon,
\]

继而推出 corrected cyclic curvature 的负线性结论。

这一推导没有把 reverse KL 换成 forward KL，没有令未知符号项为零，也没有对逐层 `O(1)` 估计求导。但它是条件蕴含，不属于 Theorem 1 的无条件结论；即使门槛最终达到，也仍不能自动推出 true Toeplitz 熵率凹性。

当前循环改进下界为 `-26.4885978163`，而零余量门槛是 `-1.20090484009`，当前证明的每点认证缺口为

\[
25.2876929762.
\]

因此不能声称 corrected cyclic concavity 已获认证。若只把下界推进到零余量门槛，仍只能得到 `Hhat_n''<=o(n)`；要得到严格的负线性余量，改进必须严格超过上述缺口。

## 9. 尚存义务与价值判断

式 (21) 暴露了 Theorem 1 粗 Bregman 支付中的主要损失：可尝试联合利用

\[
\Phi(u_{10})+\Phi(u_{01})-
\Psi(v_{11})-\Psi(v_{00})
\]

的真实分布结构，而不是丢弃两个负 `Psi` 项并把 `Phi(u)/u` 全部替换为端点值。但这不是唯一可能的改进位置：式 (45) 还包含只保留前三个非负矩项的截断损失，以及只用单一统计量做 Cauchy--Schwarz 所得的 Fisher 下界损失。现有认证差距约 `25.2877`/site，量级上仍很大；它不等同于已经证明真实 `R_n/n` 本身有同样缺损。

客观评价是：稿件提供了一个新的、严格且可迁移的有限输出补偿恒等式，也明确排除了一个诱人的错误点态控制；但它尚未把主问题推进到接近目标常数的程度。其价值目前主要是结构化地暴露损失位置，而非完成 corrected-law 或 true-law 结论。

## 10. 编辑性问题

原稿式 (35) 的 `\frac` 被写成了一个 form-feed 控制字符加 `rac`。公式上下文表明应为

\[
|V_{ab}|^2=
\frac1{k^2\sin^2(\pi(a-b-1/2)/k)}.
\]

这是排版错误，不影响本次数学裁决；公开归档时应修正。

另外，作者稿 §§1--5 直接沿用 `R_n`、`h_i`、`x_i`，没有在本稿内重新定义；其中 `x_i=2r_i-1` 可由后文反推，`R_n` 则依赖 S43 的易感性分解。数学账本可核对，但若把本稿作为独立公开文件，宜在开头补齐这三个定义。
