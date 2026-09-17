> **待独立对抗性审查 / PENDING_INDEPENDENT_REVIEW。** 下文保留来源原文；其中 PROVED、PASS、AUDIT 等是作者或既有记录的表述，不代表本次 SA 成果已独立通过。先读本包根目录 REVIEW_REQUEST.md；外部审计与其他 SA 分开进行。

# SA03 附录：有符号局部曲率核的体积极限

**状态：PROVED（本文给出证明，尚未独立审查）。** 同一个候选工具，不引入计数替代律或第二条主路线。本附录先给定性证明；`SA03_EFFECTIVE_REMAINDER.md` 另把误差量化。常数符号和首个非零更细项未定。

## V1. 结论和范围

固定 0<c<1，对任务中对齐的 Fejer 半径和条件半径，

\[
\boxed{A_R''(0)=\Gamma(c)+o(1),\quad R\to\infty\text{ 沿正奇数}.} \tag{V1}
\]

不是把 Gamma 定义为待求曲率的极限，而是

\[
\boxed{\Gamma(c)=\int_0^1uE_{\infty,u}\overline{\mathcal G}_{\infty,u}\,du
 =4+\int_0^1uE_{\infty,u}[\overline{\mathcal G}_{\infty,u}-8]\,du.} \tag{V2}
\]

E_(infty,u) 是未平滑 sine 符号 1/2+uc(1_E-1/2) 的真实无限 DPP 外部律，E=[-1/4,1/4]。核由下面的绝对可求和公式定义。

主报告点态界延伸为

\[
|\overline{\mathcal G}_{\infty,u}-8|\le C_cu^4,
\quad C_c={21c^4\over16[(1-c)/2]^{18}},
\quad |\Gamma(c)-4|\le C_c/6.                            \tag{V3}
\]

(V1) 不表示 Gamma 非零，不提供符号，也不是完整 1/R 展开。没有把 Gamma 未经论证称为真实熵率的负 Hessian。

## V2. 共同 Hilbert 空间

C_infty=Z minus {0}，Hspace=ell^2(C_infty)，Omega={0,1}^C_infty 取可数乘积拓扑，是紧致度量空间。P_R 是到 C_R 的正交投影，S_z=diag(2z_i-1)。

令 Q^(R)=T(p_R) 为整个整数格的 Fejer Toeplitz 正压缩，Q^(infty)=T(1_E)。定义

\[
H_R^0=cP_R(Q^{(R)}_{C_\infty}-I/2)P_R,
\quad b_R^0=cP_RQ^{(R)}_{C_\infty,0},
\]
\[
H_\infty^0=c(Q^{(\infty)}_{C_\infty}-I/2),
\quad b_\infty^0=cQ^{(\infty)}_{C_\infty,0}.                \tag{V4}
\]

范数均分别 <=c/2，并且

\[
H_R^0\to H_\infty^0\text{ 强收敛},\qquad
b_R^0\to b_\infty^0\text{ 在 }\ell^2\text{ 中收敛}.       \tag{V5}
\]

证明：Fejer 核非负、积分 1、固定零点邻域之外质量趋零，故 p_R 在 1_E 连续点趋向 1_E，且 0<=p_R<=1。Fourier 乘子表示和支配收敛给出强算子收敛，再用 P_R 强趋 I。中心列也可由 |p_hat_R(k)|<=1/(pi|k|) 的平方可求和界直接支付。

对 u in [0,1] 定义

\[
G_R(u,z)=(S_z/2+uH_R^0)^{-1},\quad
v_R=G_Rub_R^0,\quad q_R=1/2-u(b_R^0)^*v_R.                \tag{V6}
\]

在 C_R 内它们正是原真实条件逆、中心响应和后验；补空间逆矩阵是 2S_z。这个嵌入只比较算子，不改变概率律。i 不在 C_R 时 v_i=0，翻转 z_i 不影响 q 或有限 Bregman 核，所以写成无限索引和不会新增物理贡献。

## V3. 统一于全部 word 的 resolvent 引理

### 引理 V3.1

若 H_j 强趋 H，sup_j||2H_j||<=c<1，b_j 在 ell^2 中趋 b，则

\[
\sup_{u\in[0,1],z\in\Omega}
\|(S_z/2+uH_j)^{-1}ub_j-(S_z/2+uH)^{-1}ub\|\to0.         \tag{V7}
\]

固定列 e_i 代替 ub_j 时同样成立；极限是 (u,z) 的连续 ell^2 值函数。

**证明。** 对固定 x，z->S_zx 强连续，因为坐标收敛由 4 sum_i|x_i|^2 支配。(z,x)->S_zx 联合连续，算子范数恒为 1。Neumann 级数为

\[
(S_z/2+uH_j)^{-1}=2\sum_{k\ge0}(-2uS_zH_j)^kS_z.          \tag{V8}
\]

尾部在 j,u,z 上由 c^k 一致控制。每个固定 k 的极限项作用于 ub 后，是紧空间 [0,1]xOmega 的连续像，故为紧向量集。一致有界的强收敛算子在每个紧向量集上都一致收敛：有限向量网加统一范数界即可证明。对 k 归纳，有限项一致收敛；最后支付几何尾即得 (V7)。列向量证明相同。

### 推论 V3.2

所有有限 R 及 infinity、u、z 的 v_R 族有紧闭包；每个固定 i 的 G_R e_i 族亦然。因此

\[
\tau_m=\sup_{R,u,z}\sum_{i\notin C_m}|v_{R,i}|^2\to0,    \tag{V9}
\]
\[
\eta_{i,m}=\sup_{R,u,z}\sum_{j\notin C_m}|(G_R)_{ji}|^2\to0
\quad\hbox{对固定 i}.                                    \tag{V10}
\]

这里紧性只给趋零；有效非幂次尾由定量附录另付。q_R、每个固定赔率、翻位后验及有限条目均在 (u,z) 上一致收敛，极限连续。

## V4. 无限后验确实是真实后验

固定 u，先不改变未平滑核，只增加真实无限 DPP 的条件窗口。有限后验由同一 Schur 补给出，矩阵为 P_m H_infty^0 P_m，列为 P_m b_infty^0。引理 V3.1 说明它们一致趋向 (V6) 的 q_infty。

另一方面，有限窗口后验是有界条件期望 martingale，几乎处处及 L1 趋向 P(Y0=1 | Y_Cinfty)。所以 q_infty 是真实完整双侧后验的一个连续版本，不是计数后验或修正律。对每个固定 u 成立，足以用于真实期望。

## V5. 双翻位尾和一致局部逼近

令 a=2/(1-c)、L=ac/2。全部 R,u,z 上 ||G||<=a、||v||<=L，赔率和其倒数统一有界。主报告翻位式和带权估计可先在有限部分和上使用，再取单调极限。

### V5.1 一次和

|d_i|<=a|v_i|^2，故

\[
\sup\sum_{i\notin C_m}|d_i|\le a\tau_m,\quad
\sup\sum_{i\notin C_m}d_i^2\le a^2L^2\tau_m.              \tag{V11}
\]

这支付 Bcal_psi 尾。参数导数项也可支付，因为 q'/u=1+||v||^2、|d_i'|/u=| ||v(z^i)||^2-||v(z)||^2 |<=2L^2，r_i'/u^2=(G^2)_ii<=a^2。结合主报告的 Bregman 值及导数界，正规化单和尾一致趋零。

### V5.2 二次和

e_ij=Delta_j d_i、D_ij=max(|d_i(z)|,|d_i(z^j)|)。主报告带权连通估计把二次和控制为下列非负核的有限线性组合：

\[
|G_{ij}||v_i|^3|v_j|,\quad |G_{ij}|^2|v_i|^4,
\quad |G_{ij}|^2|v_i|^2|v_j|^2,\quad |G_{ij}|^4|v_i|^4,     \tag{V12}
\]

及交换 i,j 的版本，还有 |d_j|D_ij^2。

第一核，i 在尾部时总和 <=aL tau_m^(3/2)，j 在尾部时 <=aL^3 sqrt(tau_m)，均由 Cauchy–Schwarz 支付。

第二核，i 在尾部由 a^2L^2 tau_m 支付；j 在尾部时，先把 i 限于固定较小窗口 C_l，有限行尾用 (V10)，余下 i 用 a^2L^2 tau_l。先取 l 大，再取 m 大。Hermitian 性使行尾等于列尾。

第三核任一指标在尾部，由 a^2L^2 tau_m 支付；第四核不超过 a^2 倍第二核。

最后，(V11) 对每个翻位 word 同样成立，因此

\[
\sup\sum_{i\notin C_m\ {
m or}\ j\notin C_m}|d_j|D_{ij}^2
 \le4a^3L^4\tau_m\to0.                                  \tag{V13}
\]

对角 i=j 单独用一次尾处理。故所有已分组的二次翻位差分和都有一致消失的空间尾；没有把不收敛的裸双项分开求和。

### V5.3 无限核的明确公式

避免 u=0 除零，直接定义

\[
\bar r_i=\sigma_i-G_{ii},\quad
\bar{\mathcal B}_\psi=\sum_i\bar r_i\operatorname{Breg}_\psi(q(z^i),q(z)),
\quad A_z=1+\|v_z\|^2,
\]
\[
\begin{aligned}
\overline{\mathcal G}(z)={}&\phi''(q)+\bar{\mathcal B}_{\phi'}
 +\sum_i(G^2)_{ii}\operatorname{Breg}_\phi(q(z^i),q)\\
&+\sum_i\bar r_i[(\phi'(q(z^i))-\phi'(q))A_{z^i}-\phi''(q)d_iA_z]\\
&+\sum_j\bar r_j[\bar{\mathcal B}_\phi(z^j)-\bar{\mathcal B}_\phi(z)].
\end{aligned}                                             \tag{V14}
\]

有限 R、u>0 时它等于主报告 Gcal/u^2。u=0 时 b=0、q=1/2、全部 d_i=0，所以等于 8。

V5.1–V5.2 证明无限和绝对收敛且可在 R,u,z 上一致截断。固定有限指标的全部条目由引理 V3.1 一致收敛。因此

\[
\boxed{\sup_{u,z}|\overline{\mathcal G}_{R,u}(z)
              -\overline{\mathcal G}_{\infty,u}(z)|\to0.} \tag{V15}
\]

极限在紧空间 [0,1]xOmega 上连续，点态界通过极限保留。

不声称无限超立方体对任意有界函数都有总速率有限的生成元；只定义 (V14) 中已经证明可求和的动作。无需无限计数、无限 word 密度或无限 score。

## V6. 真实概率律变化和积分

P_(R,u) 表示整个整数格 Fejer DPP 的外部边缘，P_(infty,u) 表示真实未平滑外部律。barG_R 只依赖 C_R，所以在 P_(R,u) 下的期望就是原任务的实际有限期望。

每个固定有限窗口的真实 word 概率由有限行列式给出。核条目随 R 收敛且在 u in [0,1] 上一致，所以该窗口每个 word 的概率也一致收敛。

barG_infty 是紧空间上的连续函数，可以在 u,z 上一致逼近为有限窗口函数，例如固定窗口外参考 word 后利用一致连续性。对这个有限窗口函数，实际概率收敛可逐项求和。结合 (V15)，

\[
\boxed{\sup_{u\in[0,1]}|E_{R,u}\overline{\mathcal G}_{R,u}
                  -E_{\infty,u}\overline{\mathcal G}_{\infty,u}|\to0.} \tag{V16}
\]

原曲率恰为 int_(1/N)^1 u E_R barG_R du。由 (V16) 可在可积 u 权重下通过极限，缺失 [0,1/N] 段由 8u+C_cu^5 控制，得到 (V1)–(V2)。

若把 (V16) 上确界记为 epsilon_R->0，则

\[
|A_R''(0)-\Gamma(c)|\le\epsilon_R/2+4N^{-2}+C_c/(6N^6).   \tag{V17}
\]

epsilon_R 是已经构造的局部核和实际律的逼近误差，不是目标曲率的改名。本附录到此只证明趋零；定量附录 (Q4)–(Q5) 给出完全显式上界。该误差可能支配小 u 截断误差。

## V7. 剩余缺口

本附录移除了“是否存在有限次主阶极限”的缺口，没有完成符号。若另证 Gamma(c)>0，则推出充分大 R 的 A_R''>0；当前没有该下界或有效判号半径。Gamma=0 时还需研究更小尺度。

剩余问题须区分：Gamma(19/20) 的符号；尖锐 R 误差/首个非零更细项；把有限曲率极限识别并传递为真实熵率的二阶性质。定量附录只支付一个保守有效误差，不能代替这些问题。最后一项不能仅从 delta=0 曲率收敛和函数值收敛推出。

没有使用拟合、巨大枚举、未核验的无限 Poisson 定理或微分实值误差；证明使用主报告局部核、Neumann 收敛、紧性和真实有限概率的一致性。
