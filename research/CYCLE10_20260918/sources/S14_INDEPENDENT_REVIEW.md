# S14 独立数学审查报告

## 总评

- **审查完整性：COMPLETE_SCOPED_REVIEW。** 已覆盖循环修复、计数 Hessian 分解、非负系数/实根/单峰、`R_{m,xi}` 的方向性、主剩余项量词、删除链恒等式、条件路线及扩散尺度障碍。
- **主要新结构：VERIFIED_SCOPED。** 精确计数运输公式、正权重一阶差分表示、扩散剖面定理和删除链调制熵恒等式在所述范围内成立。
- **方向性强度：VERIFIED_SCOPED（按核心推导实际所需的单侧形式）。** 稿件只证明 `R_{m,xi}` 的单侧上界，却把加权项写成双侧 `O(sqrt(n))`。正确且已验证的结论是该项的**上侧/不利方向**至多 `C sqrt(n)`；这正是后续 `U_n` 下界所需的方向。双侧绝对值表述不纳入认证，但不影响核心推导。
- **无条件目标 `U_n>=-o(n)`：NOT_REVIEWED（无证明提交）。** 作者明确保留两个未付的有符号聚合预算；没有找到或声称实际 SA05 渐近反例。
- **旧 `n=8` 区间脚本：NOT_REVIEWED。** 本轮没有重跑该附件；只独立核对了新运输公式给出的中心系数。

## 1. §§5.3–5.4 的非循环修复

**状态：VERIFIED_SCOPED。** 对应新稿第 1 节。

对 `J=|S cap A|`，Johnson 上下跳率为

\[
b_J=\frac{(m-J)(k-J)}{m(n-m)},\qquad
d_J=\frac{J(k-m+J)}{m(n-m)}.
\]

因为 `t(J+1)/t(J)=z=(1+xi)/xi`、`t(J-1)/t(J)=z^{-1}`，直接计算而不作中心化，确实得到

\[
\frac{L_lt_A}{t_A}
=\frac{J^2-(m+k+n\xi)J+(1+\xi)mk}
{\xi(1+\xi)m(n-m)}.
\]

先对此式取期望并用生成元保守性，才得到

\[
y^2+(k-m+n\xi)y+v=mk\xi,
\quad y=m-\mu.
\]

随后令 `X=J-mu`，常数项才可替换成 `-v`。这消除了旧文本“先使用中心化常数、再由该式证明中心化矩恒等式”的循环。

指数倾斜微分也正确：

\[
(\log z)_\xi=-\frac1{\xi(1+\xi)},\qquad
\mu_\xi=-\frac v{\xi(1+\xi)},
\]

从而

\[
\frac{t_{A,\xi}}{t_A}=-\frac X{A(\xi)},\qquad
\frac{t_{A,\xi\xi}}{t_A}
=\frac{X^2-v+(1+2\xi)X}{A(\xi)^2}.
\]

在中点 `xi_a=0, xi_aa=-2/c`，稿件给出的 `a` 二阶式随之成立。度二正交先写成

\[
\mu_4-v^2+(2\mu-m)\mu_3
+\mathfrak b[\mu_3+(2\mu-m)v]=0
\]

再解出 `mathfrak b`，逻辑顺序正确。背景 §5.4 随后用修复后的矩恒等式证明有缺陷层 `m>=4` 的分母严格为正；故不存在未支付的除零问题。

## 2. 中点计数 Hessian 的精确因子分解

**状态：VERIFIED_SCOPED。** 对应第 2 节。

令 `s=a-a_*`。一高一低两个 Bernoulli 位的 PGF 精确为

\[
p_s(t)=p_0(t)+s(t^2-1)+s^2(1-t)^2,
\]

其中

\[
p_0(t)=\rho(1+t^2)+bt,
\quad \rho=(1-c^2)/4,
\quad b=(1+c^2)/2.
\]

对 `Pi_s=p_s^k` 求二阶导，确实得到

\[
\Pi_0''(t)=(1-t)^2B_n(t),
\]

\[
B_n(t)=2kp_0^{k-1}+k(k-1)(1+t)^2p_0^{k-2}.
\]

因此对任意实序列 `h_0,...,h_n`，系数移位给出

\[
\sum_l\pi_l''h_l
=\sum_{r=0}^{n-2}B_{n,r}(h_r-2h_{r+1}+h_{r+2}).
\]

这里没有使用 `h` 的平滑性、非负性或概率解释。

## 3. 实根、正系数、单峰与正权重运输

**状态：VERIFIED_SCOPED。**

正文只简述了实根性，本轮独立核对如下。`p_0` 是正系数回文二次式，其判别式为正，两个根均为负。剩余回文二次因子

\[
Q(t)=2kp_0(t)+k(k-1)(1+t)^2
\]

的中间系数减去两倍端系数正好是

\[
2k(b-2\rho)=2kc^2>0.
\]

故 `Q` 也有两个负实根。于是 `B_n=p_0^{k-2}Q` 全部实根为负、系数严格为正。Newton 不等式给系数对数凹，无内部零点；结合回文性，

\[
B_{n,0}\le\cdots\le B_{n,k-1},
\quad B_{n,r}=B_{n,n-2-r}.
\]

定义

\[
\omega_{n,0}=B_{n,0},\qquad
\omega_{n,m}=B_{n,m}-B_{n,m-1}\ge0.
\]

对补集对称的 `h_{n-l}=h_l`，把二阶差分在中心两侧配对并做一次离散分部求和，确实得到

\[
\sum_l\pi_l''h_l
=-2\sum_{m=0}^{k-1}\omega_{n,m}(h_{m+1}-h_m).
\]

这不是符号结论：权重非负，但相邻增量仍可有任意符号。

另外 `B_n(1)=n(n-1)`。归一后的 `B` 系数是 `n-2` 个 Bernoulli 位之和的分布，方差为 `Theta_c(n)`，故中心系数为 `O_c(n^{3/2})`。Hoeffding 给出

\[
B_{n,k-w-1}
\le n(n-1)e^{-2w^2/(n-2)},
\]

所以稿件使用的较弱 `e^{-w^2/(n-2)}` 也正确。精确有理复算在 `n=8` 给

\[
\omega_{8,3}
=\frac{1766316767}{102400000}>0,
\]

与稿件一致。

## 4. `U_n` 的精确账本

**状态：VERIFIED_SCOPED（使用背景 CL12 的已写恒等式）。** 对应第 3 节。

由定义

\[
\lambda_l=\langle f_l-g_l,\log g_l\rangle,
\qquad R_l=D(f_l\Vert g_l),
\]

逐项恒等式为

\[
\epsilon_l=D(f_l\Vert u_l)-D(g_l\Vert u_l)
=\lambda_l+R_l.
\]

中点 `xi_a=0`，所有层的一阶 `a` 导数消失，而 `xi_aa=-2/c`。因此

\[
U_n=\mathcal L_n''+\sum_l\pi_l''R_l
=\sum_l\pi_l''\epsilon_l
-\frac2c\sum_l\pi_l\lambda_{l,\xi}.
\]

`epsilon_l` 具有补集对称性；对 `m<=3`，真实与修正律无未匹配模式，所以相应增量为零。对 `m>=3` 使用背景 CL12 后，稿件保留了反向条件 KL、参数响应、正平方和移动参考残差，得到的 `Gamma_m` 账本没有把不利项删去。

## 5. `R_{m,xi}` 只能作单侧控制

**状态：VERIFIED_SCOPED（单侧形式与后续下界）；双侧表述不纳入认证。**

背景图能量论证实际给出

\[
R_{m,\xi}
\le-\tau_{m,\xi}\mathcal D+J_m\sqrt{\mathcal D}
\le\frac{J_m^2}{4\tau_{m,\xi}}
\le K_R.
\]

它没有给 `R_{m,xi}>=-K_R`，所以不能推出 `|R_{m,xi}|<=K_R`。结合 `eta_m>=0`、`eta_m<=C/n` 和 `sum omega=O(n^{3/2})`，严格能推出的是

\[
\boxed{
\sum_m\omega_{n,m}\eta_mR_{m,\xi}
\le C_c\sqrt n.}
\]

不能写成

\[
\sum_m\omega_{n,m}\eta_mR_{m,\xi}=O(\sqrt n)
\]

或其绝对值版本。若该和很负，它反而有利于 `U_n` 的下界。

在精确式

\[
U_n=-2\sum_m\omega_m(\Gamma_m+\eta_mR_{m,\xi})
-\frac2c\sum_l\pi_l\lambda_{l,\xi}
\]

中，`R_{m,xi}` 前的系数是负的，所以所需的正是上述上界。因此仍可严格写成

\[
U_n\ge
-2\left(\sum_m\omega_m\Gamma_m\right)_+
-\frac2c\left(\sum_l\pi_l\lambda_{l,\xi}\right)_+
-C_c\sqrt n.
\]

这里最后的 `-C_c sqrt(n)` 是单侧罚项，不是对原加权和的双侧量级声明。后续不得把它改用于绝对误差、上界或极限等式。

## 6. 删除链调制熵恒等式

**状态：VERIFIED_SCOPED。** 对应第 5 节。

KL 链式分解对“保留的 `m` 集 + 被删点”给出

\[
\epsilon_{m+1}=\epsilon_m^\downarrow+\mathcal H_m^{del}.
\]

在 `P` 下加减修正条件律的 KL，逐条件使用

\[
D(\alpha_p\Vert u)-D(\alpha_{\widehat p}\Vert u)
=D(\alpha_p\Vert\alpha_{\widehat p})
+\sum_x(\alpha_p-\alpha_{\widehat p})
 \log(\alpha_{\widehat p}/u),
\]

再支付边缘 `P-widehat P` 的变化，正好得到稿件列出的三项；没有把两个带符号线性项吞进正 KL。

对 CL12 插值，Taylor 积分式给

\[
\epsilon_{m+1}-\epsilon_m
=\mathcal H_m^{del}
+\eta_m\epsilon_{m,\xi}
+\int_0^1(1-t)\Phi_m''(t)dt.
\]

减去 CL12 后得到 `lambda`、`C_m`、`J_m` 的盒装恒等式。它只是精确重新编账，不赋予未知积分或线性项有利符号。

## 7. 条件路线的量词

### 7.1 中央一步路线

**状态：VERIFIED_SCOPED。**

若在 `|m-k|<=n^(2/3)` 内有统一单侧条件

\[
(\epsilon_{m+1}-\epsilon_m)_+\le A/n,
\]

则中央正权重总质量 `O(n^{3/2})` 只产生 `O(sqrt n)=o(n)` 的不利项。窗外取 `w=n^(2/3)` 时，Hoeffding 尾为 `n(n-1)exp[-Theta(n^(1/3))]`；即使用多项式粗界乘邻层差，仍为 `o(n)`。再单独假设平均响应正部 `o(n)`，即可推出 `U_n>=-o(n)`。

这是充分条件，不是稿件已经证明的实际 SA05 性质。

### 7.2 宏观剖面路线

**状态：VERIFIED_SCOPED，量词必须保持固定剖面。**

这里 `H in C^2([0,1])` 必须是一个固定、补集对称的函数，并要求中央窗上的一致误差趋零。固定 `H(l/n)` 的二阶差分是 `O(n^{-2})`，乘 `B` 总质量 `O(n^2)` 仅为 `O(1)`；误差项用 `||pi''||_1=O_c(n)` 和中央一致 `o(1)` 得 `o(n)`，尾部由集中性消去。若允许 `H=H_n` 在扩散尺度振荡，结论不成立；这正是下一节的障碍。

平均 `lambda_xi` 响应仍必须作为独立假设，不能从静态剖面逼近推出。

## 8. 扩散尺度剖面与障碍

**状态：VERIFIED_SCOPED。** 对应第 7 节。

归一 `B_{n,r}/[n(n-1)]` 后得到一个由 `n-2` 个独立 Bernoulli 位组成的分布，均值 `k-1`，方差与

\[
\sigma_n^2=n(1-c^2)/4
\]

之比趋于一。Lindeberg 条件自动成立。对

\[
h_{n,l}=H((l-k)/\sigma_n),
\]

二阶差分的积分形式与 `H''` 的一致连续性给

\[
\sigma_n^2\Delta^2h_{n,r}
\to H''((r-k)/\sigma_n)
\]

且误差一致趋零。结合上述 CLT，

\[
\frac1n\sum_l\pi_l''h_{n,l}
\to\frac4{1-c^2}E[H''(Z)].
\]

高斯分部积分给等价式 `E[(Z^2-1)H(Z)]`。取 `H(x)=exp(-x^2/2)`，

\[
E[H''(Z)]=-\frac1{2\sqrt2},
\]

因此极限为 `-sqrt(2)/(1-c^2)`，与稿件常数一致。

这个例子严格反驳“补集对称 + 非负 + 层层 `O(1)` 足以推出移动计数 Hessian 为 `o(n)`”的规则。它不是实际 Fourier-DPP 的 `epsilon_l`，不能当作 SA05 的渐近反例。

稿件最后的诊断定理同理：只有在 `G_n=sigma_n^2 Delta^2 epsilon_n` 统一有界、在扩散尺度局部收敛，并且平均 `lambda_xi/n` 收敛时，才可得到 `U_n/n` 的极限。缺少任一量词都不能使用该结论。

## 9. 最强可保留结论与最小后续义务

可以保留：非循环的一维源推导；精确正权重计数运输；实根、单峰和显式尾；删除链调制熵账本；方向正确的 `-C sqrt(n)` 下界罚项；两条明确的条件充分路线；扩散尺度的抽象反例。

不能保留为已证结论：

- 加权 `eta_mR_{m,xi}` 项的双侧 `O(sqrt n)`；
- 实际 `mathfrak A_n=o(n)` 或 `mathfrak B_n=o(n)`；
- 实际 `U_n>=-o(n)`；
- 真实 SA05 序列具有稿件构造的高斯剖面；
- 任何真实输出熵或 Toeplitz 结论。

建议性、非阻断的书写修订是把第 4 节相关句子统一改成“一侧上界/对下界的不利贡献为 `O(sqrt n)`”。若要升级为真正双侧 `O(sqrt n)`，必须另证 `R_{m,xi}` 的统一下界或绝对值界；若要完成无条件目标，还须独立证明两个有符号聚合预算的次线性估计。任何此类新证明都需要重新独立验证。
