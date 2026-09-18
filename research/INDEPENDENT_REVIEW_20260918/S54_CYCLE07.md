# S54 Cycle 07 独立数学审查

日期：2026-09-18

审查对象：`S54_CYCLE07_RESULT.md`、`S54_CYCLE07_checks.py` 与原 ZIP。审查继承已经独立核验的 S43 cycle03/cycle05 径向局部极限、实际 (\kappa_l) 账本及全层尾界；本报告重新核对这些输入在 S54 中的方向、归一化和调用范围，不重审整份历史证明。

## 总裁决

- **conditional-likelihood projection：VERIFIED。** 精确链式法则为
  \[
  D(p_l^H\Vert q_l^G)-D(\mu_l\Vert\gamma_l)
  =\mathbb E_{\gamma_l}
    \operatorname{Ent}_{Q_{n,l,S}}(h_{n,l}),
  \]
  KL 方向始终是任务要求的 (D(\mu_l\Vert\gamma_l))，没有换成反向 KL。
- **Gibbs posterior：VERIFIED。** 条件于空间输出 (S)，overlap (R) 确为参数由 (P_S) 谱给出的 Poisson-binomial；half-Fourier 对称使谱按 (\lambda\leftrightarrow1-\lambda) 配对。
- **paired posterior-variance certificate：VERIFIED。** 作者式 (3.6) 是精确有理因式分解，逐谱对求和得到
  \[
  V_S\ge\mathsf A_c(l/2-M_S)-\mathsf B_cT(S).
  \]
  两矩约束下的 sharpness mixture 也满足所需的 mean/leakage moments。
- **中央 leakage 与均值控制：VERIFIED_SCOPED。** 二点 slice 插值、(\mathbb ET/n\to(3+c^2)/48)、strong-Rayleigh Lipschitz concentration、全方差与 Chebyshev 共同给 posterior variance floor
  \[
  V_S/(nv_G)\ge\tau_c^{\rm post}-o(1)
  \]
  于概率趋一的中央 good set 上，一致于每个固定 (K\sqrt n) 窗。
- **Gaussian entropy payment：VERIFIED_SCOPED。** 已审 radial local limit 与统一 Poisson-binomial local CLT 足以通过 bounded-window localization 得到 Gaussian entropy 下界；subcritical 条件 (2a_c\tau<1) 已严格支付。该 Gaussian entropy 在允许的均值偏移和方差范围内，最小值恰为 (\Delta_c>0)。
- **actual signed sum：VERIFIED_SCOPED。** 中央负系数使用 (U_{n,l}\le D_c-\Delta_c+o_K(1))，正系数只用 (U\ge0)；所有非中央层由已审实际 (\kappa_l) quadratic tail 与 output envelope 支付，四个端层为零。没有用 Gaussian 权重替换真实权重。
- **数值改进：VERIFIED。** 在 (c=19/20)，
  \[
  \Delta_c=0.0004524239233156623590\ldots,
  \]
  \[
  M_b\Delta_c=0.00898242826785511160\ldots,
  \]
  故损失从
  \(2.7990951599080403202\ldots\)
  降为
  \[
  \boxed{2.7901127316401852086\ldots}.
  \]
- **脚本：PASS AS DIAGNOSTIC。** 精确 SymPy 因式分解通过；高精度常数、有限 slice 两点公式及 PPVC slack 均复现。有限浮点/枚举不承担渐近证明。
- **排版问题：MINOR。** 原稿式 (5.6) 的 `\frac` 首字符被写成不可见 form-feed；上下文与脚本中的公式明确，不影响数学内容，建议合并时修正。
- **零消去目标：OPEN。** 本稿没有证明 (\Psi_n\to0)、(\liminf\Psi_n\ge0) 或完整 layer profile。它只是把已审 signed KL 下界严格改善约 (0.00898)。
- **最终凹性：OPEN。** 在 compensated ledger 中，S52 susceptibility 的充分门槛改善为严格条件
  \[
  \liminf R_n/n>-1.2098872683598147\ldots,
  \]
  但 S54 没有证明该门槛。

最强可信标签：

> **T1--T6: VERIFIED_SCOPED_WITH_REVIEWED_INPUTS; strict signed-KL improvement: VERIFIED; (\Psi\to0), susceptibility threshold, and entropy-rate concavity: OPEN.**

## 1. CLP 恒等式与 KL 方向

在 Gibbs joint law (J_G(A,S)) 下，令

\[
Q_{n,l,S}=\operatorname{Law}_{J_G}(R\mid S),
\qquad
h(r)=p_l^H(r)/q_l^G(r).
\]

由于两个 conditional channels 在每个 overlap orbit 内均匀，joint likelihood ratio 只依赖 (R)：

\[
\frac{dJ_H}{dJ_G}(A,S)=h(R).
\]

输出 likelihood ratio 为条件期望

\[
\frac{\mu_l(S)}{\gamma_l(S)}=\mathbb E_Qh.
\]

于是

\[
\begin{aligned}
D(J_H\Vert J_G)-D(\mu_l\Vert\gamma_l)
&=\sum_S\gamma_l(S)
\left\{E_Q[h\log h]-(E_Qh)\log(E_Qh)\right\}\\
&=E_{\gamma_l}\operatorname{Ent}_Q(h).
\end{aligned}
\]

又因 joint likelihood ratio 仅由 (R) 决定，

\[
D(J_H\Vert J_G)=D(p_l^H\Vert q_l^G).
\]

因此 CLP 完全精确。对事件 (A)，分解 (A,A^c) 后，剩余 conditional means 的二点 Jensen gap 非负，从而

\[
\operatorname{Ent}_Q(h)
\ge Q(A)\operatorname{Ent}_{Q(\cdot\mid A)}(h).
\]

这正是后续 bounded-window localization 的合法接口。

## 2. Posterior Poisson-binomial 结构

Gibbs posterior 为

\[
\nu^G(A\mid S)
\propto\nu(A)z^{|A\cap S|}.
\]

Cauchy--Binet 给 generating function

\[
E[w^X\mid S]
=\frac{\det(I+(zw-1)P_S)}
       {\det(I+(z-1)P_S)}.
\]

若 (\lambda_i) 是 (P_S) 的本征值，则

\[
X\mid S=\sum_i\operatorname{Bernoulli}
\left(\frac{z\lambda_i}{1+(z-1)\lambda_i}\right)
\]

为独立和；等价地

\[
R=l-X=\sum_i\operatorname{Bernoulli}
\left(\frac{1-\lambda_i}{1+(z-1)\lambda_i}\right).
\]

half-Fourier 投影满足

\[
D_SP_SD_S=I_S-P_S,
\]

所以 (\lambda\) 与 (1-\lambda) 成对；奇数 (l) 时的 (1/2) 自配本征值按半个 pair 计入，公式仍成立。

## 3. PPVC 因式分解

对一对谱 (\lambda,1-\lambda)，令

\[
u=(2\lambda-1)^2,
\qquad
\chi=\frac{2c}{1+c^2}.
\]

正文给出的 (m_c(u),v_c(u),t(u)) 分别是该 pair 对 posterior mean、variance 与 leakage 的贡献。独立符号复算确认

\[
\begin{aligned}
v_c(u)-\mathsf A_c(1-m_c(u))+\mathsf B_ct(u)
=\frac{4c^4(1-c^2)^2(1-u)(6u-1-c^2)^2}
{(c^2+3)^2((1+c^2)^2-4c^2u)^2}\ge0.
\end{aligned}
\]

逐 pair 求和即得 PPVC。等号点是

\[
u=1,
\qquad u_0=(1+c^2)/6.
\]

权重

\[
\omega_c=(3+c^2)/(5-c^2)
\]

在 (u_0) 与 (1) 之间的混合满足中央目标 leakage；同时其 posterior mean 也达到对应目标。因此“仅知道 pair 平均 mean 与 leakage 时不可统一加强”的 sharpness 说明成立。它不意味着真实 compression spectrum 必然取此极值分布。

## 4. 中央 leakage

### 4.1 二点插值

固定层 law

\[
\gamma_l(S)\propto\det[I+(z-1)P]_S,
\qquad |S|=l.
\]

对 multiaffine determinant generating polynomial 求两个不同坐标的导数，利用 (P^2=P) 与 rank (k=n/2)，得到

\[
E_{\gamma_l}Y_iY_j
=u_{2,l}+\theta_{n,l}
\left[\alpha_l(1/4-|P_{ij}|^2)-u_{2,l}\right].
\]

常数部分由 (\sum_{i\ne j}Y_iY_j=l(l-1)) 固定，故不是近似插值。

### 4.2 (T) 的均值

对 cyclic half-Fourier projection，

\[
\sum_{i\ne j}|P_{ij}|^2=n/4,
\]

\[
\sum_{i\ne j}|P_{ij}|^4=n/48+1/(6n).
\]

代入二点插值后，中央固定窗上 (\theta_{n,l}\to c^2) 一致，从而

\[
E_{\gamma_l}T/n\to t_c=(3+c^2)/48.
\]

### 4.3 浓缩

(\gamma_l) 是 fixed-size determinantal (L)-ensemble，故为 homogeneous strong-Rayleigh measure。增加或删除一个坐标使

\[
T(S)=\sum_{i\in S,j\notin S}|P_{ij}|^2
\]

变化的绝对值不超过 off-diagonal row energy (1/4)；一次保持大小的交换至多付常数 (1/2)。标准 strong-Rayleigh Lipschitz concentration 因而给

\[
T/n-E T/n\to0
\]

于概率，且对固定中央窗一致。正文只需这个趋零结论，不依赖某个最优浓缩常数。

## 5. Posterior variance floor

全方差给

\[
E_{\gamma_l}M_S=\bar r_{n,l},
\quad
\operatorname{Var}_{\gamma_l}(M_S)
\le\operatorname{Var}_G(R)=nv_G+o_K(n).
\]

故 Chebyshev 在概率至少 (1-L^{-2}-o(1)) 的集合上把
\(M_S-\bar r_{n,l}) 控制在 (L\sqrt{nv_G})。结合

\[
\frac1n(l/2-\bar r_{n,l})\to c/4
\]

和 (T/n\to t_c)，PPVC 给

\[
\frac{V_S}{nv_G}\ge
\tau_c^{\rm post}-o(1),
\]

其中

\[
\tau_c^{\rm post}
=\frac{(1-c^2)(5c^2+3)}
{(1+c^2)(c^2+3)}.
\]

另一方面 Poisson-binomial 的 (V_S\le M_S) 给

\[
V_S/(nv_G)\le4/(1+c)+o(1).
\]

正文对

\[
2a_c\frac4{1+c}<1
\]

的证明正确：它等价于 (\rho_c<4/(3-c))，再由给定 (F(c)) 的负导数和 (F(1)=0) 得到严格不等式。故后续 Gaussian 指数矩存在，并且离临界值有固定余量。

## 6. Gaussian entropy payment

已审 exact-clock local limits给，在中央固定窗和 bounded standardized (x) 上

\[
h_{n,l}(r)=p_l^H(r)/q_l^G(r)
\to h_c(x)=\rho_c^{-1/2}e^{a_cx^2}
\]

局部一致。

good set 上的 posterior 是 Poisson-binomial，且方差为 (\Theta(n))。标准 lattice local CLT 对所有这类 triangular arrays 一致，因为误差只需由总方差趋无穷控制。任取反证子列，可进一步取

\[
\xi=(M_S-\bar r)/\sqrt{nv_G}\to\xi_*,
\quad
\tau=V_S/(nv_G)\to\tau_*.
\]

用 CLP localization 先限制在 (|x|\le B)，在该有界区间通过局部极限；再令 (B\to\infty)。这避免了在有限 (n) 上直接要求未证明的全尾指数支配。由于 (2a_c\tau_*<1)，极限 Gaussian 的 (h_c\) 与 (h_c\log h_c) 都可积。

对 (N(\xi,\tau))，直接积分给正文式 (6.5)。其关于 (\xi^2) 严格递增；在 (\xi=0) 时令 (x=a_c\tau)、(d=1-2x)，

\[
\frac{x}{d}+\frac12\log d
\]

从 0 出发的导数为 (2x/d^2>0)。完整函数 (G(x)) 也严格递增。因此允许范围内的最小值在

\[
\xi=0,
\qquad\tau=\tau_c^{\rm post}
\]

取得，正是 (\Delta_c)。

good-set 概率先给因子 (1-L^{-2})；按 (n\to\infty)、再 (L\to\infty)、最后 leakage 容差趋零的顺序，即得统一下界。此处没有把固定概率 good set 误写成概率 1。

## 7. Signed (\kappa_l) 账本

CLP 与上一节给中央固定窗

\[
U_{n,l}\le D_c-\Delta_c+o_K(1).
\]

在

\[
\Psi_n=\frac1n\sum_l\kappa_lU_{n,l}
\]

中：

- (\kappa_l>0) 的项只用 (U\ge0)，可从下界中丢弃；
- 中央 (\kappa_l<0) 项使用上述上界；
- 非中央项由
  \[
  \frac1n\sum_{|l-k|>K\sqrt n}|\kappa_l|
  \left(1+\frac{(l-k)^2}{n}\right)
  \le C_c/K^2
  \]
  与同型 (U)-envelope 支付；
- (l=0,1,n-1,n) 的 (U_l) 精确为零。

先 (n\to\infty)，再 (K\to\infty)，并使用正负总质量均趋 (M_b)，得到

\[
\liminf\Psi_n(c)\ge-M_b(D_c-\Delta_c).
\]

真实系数

\[
\kappa_l=
\left((l-k)^2/b^2-n/b\right)\pi_l
+(2c/b)\dot\pi_l
\]

完整保留；没有删除 balanced-amplitude derivative。

## 8. 数值复现

使用隔离依赖环境原样运行脚本，得到：

```text
exact symbolic PPVC factorization: PASS
numeric PPVC grid: PASS
n=4,6,8,10,12 finite slice checks: PASS
```

在 (c=.95) 的高精度输出为

\[
\begin{aligned}
\rho_c&=1.9495835525079867983\ldots,\\
D_c&=0.14098388277826699493\ldots,\\
M_b&=19.854008165673300496\ldots,\\
\tau_c^{\rm post}&=0.09865555032699985942\ldots,\\
\Delta_c&=0.00045242392331566235904\ldots.
\end{aligned}
\]

由此

\[
M_b(D_c-\Delta_c)
=2.7901127316401852086183\ldots.
\]

这些是解析公式的高精度显示；渐近结论来自前述证明。

## 9. 作用域与建议状态

可以认证：

1. (D(p^H_l\Vert q^G_l)-D(\mu_l\Vert\gamma_l)) 在中央层有严格正的一致下界 (\Delta_c)；
2. 径向 data-processing 上界在实际输出上不能渐近饱和；
3. 实际 signed KL 损失在 (c=.95) 从 (2.7990951\ldots) 改善到 (2.7901127\ldots)；
4. 改善对每个固定 (0<c<1) 均严格为正。

不能认证：

- (\Psi_n\to0) 或非负；
- S52 susceptibility 已达到新的 (-1.209887\ldots) 门槛；
- corrected midpoint Shannon 凹性；
- 真实 sine-Toeplitz 全配置熵率凹性；
- 从小规模有限枚举外推渐近符号。

因此 S54 是一项正确、严格但数值较小的 signed-output-KL 改进，不是最终目标的闭合。
