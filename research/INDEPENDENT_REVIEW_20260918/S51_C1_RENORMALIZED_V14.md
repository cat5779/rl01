# S51 C1：\(c\uparrow1\) 重标度 V14 独立数学审查

## 裁决

| 审查项 | 裁决 |
|---|---|
| 真无限投影 Ward 恒等式 | `VERIFIED` |
| 有限压缩泄漏及固定谱隙极限 | `VERIFIED_SCOPED` |
| 真配置熵的对数赔率导数桥 | `VERIFIED` |
| actual-law 条件交叉比 \(\mathcal J\) 与非负测度 \(\nu_x\) | `VERIFIED_SCOPED` |
| \(\Gamma_x(0)=\kappa_x^{-1}-\mathcal J(x)\) | `VERIFIED_RELATIVE_TO_S51-B` |
| 完整 V14 平均公式 | `VERIFIED_AS_GROUPED_IDENTITY` |
| 端点对数增长界 | `VERIFIED_AVERAGED_ONLY` |
| 对数补偿弱-* 预紧性 | `VERIFIED_WITH_SCOPE` |
| 自然 \(\kappa_x^2\) 尺度极限 | `CONDITIONAL_ONLY / OPEN` |
| 固定窗口与 \(x\uparrow1\) 不交换 | `VERIFIED_FOR_DISPLAYED_RESPONSE` |
| spacing scale | `CONDITIONAL_NECESSARY_ONLY` |
| \(\Gamma_x(0)\) 的高 \(x\) 符号 | `NOT_PROVED` |

总裁决：相对于已审 S51-B，原稿的核心恒等式、固定谱隙极限和明确标注的分布弱结论成立，未发现关键数学错误。它建立了一个真实 actual-law 的端点研究框架：

\[
\text{投影 Ward 恒等式}
\longrightarrow
\text{条件交叉比次概率测度}
\longrightarrow
\text{完整 V14 平均补偿公式}
\longrightarrow
\text{带对数补偿的分布紧性}.
\]

它没有证明自然 \(\kappa_x^2\) 重标度下的一致可积性、点态或 \(L^1\) 极限，也没有证明 \(x\) 接近 \(1\) 时 \(\Gamma_x(0)\ge0\)。

## 1. 冻结对象与既有接口

固定真实半密度 sine 投影 \(Q\)，令

\[
K_{x,d}
=\frac12I+x\left(Q-\frac12I\right)+dI,
\qquad 0<x<1,\quad |d|<\frac{1-x}{2},
\]

\[
\varepsilon_x=\frac{1-x}{2},
\qquad
\kappa_x=\varepsilon_x(1-\varepsilon_x)
=\frac{1-x^2}{4},
\qquad
x=\tanh(\beta/2).
\]

\(q(x,d,z)\) 是给定全部外部输出后的真实中心后验，

\[
F(x,d)=\mathbb E_{x,d}
\left(q-\frac12\right)\log\frac q{1-q}.
\]

令 \(\overline{\mathcal G}_x\) 为中点、未平滑、完整 moving-law V14 核，并记

\[
\mathcal A(x)
=\mathbb E_{x,0}\overline{\mathcal G}_x
=\partial_d^2F(x,0).
\]

本稿调用的 S51-B 是此前已经单独审查的固定谱隙 value/chord bridge。参数匹配

\[
x=cu,\qquad d=u\delta
\]

给出

\[
\Gamma_c(0)
=\int_0^1u\mathcal A(cu)\,du
=\frac1{c^2}\int_0^c x\mathcal A(x)\,dx.
\]

这里的 \(\Gamma_c\) 与此前熵率桥中的真实 actual-law 曲率对象完全相同，不是重新命名的余项。当前稿没有从 S51-B 借用任何 \(x\uparrow1\) 一致性或符号结论。

## 2. 真无限投影 Ward 恒等式

取 \(C=\mathbb Z\setminus\{0\}\)，在 \(d=0\) 写

\[
B_z=K_{x,C}-D_z^{\rm vac},\qquad
G_z=B_z^{-1},\qquad
b=xQ_{C0},\qquad
v_z=G_zb,
\]

\[
q_z=\frac12-b^*G_zb,\qquad
D_z=q_z(1-q_z).
\]

固定 \(x<1\) 时 \(G_z\) 统一有界，\(v_z\in\ell^2\)。令
\(\xi=(1,-v_z)\)。Schur 方程给出

\[
\xi^*K_x(I-K_x)\xi=q_z-q_z^2.
\]

真无限 \(Q\) 是正交投影，而

\[
K_x(I-K_x)=\kappa_xI.
\]

因此逐 word 有

\[
\boxed{D_z=\kappa_x(1+\|v_z\|^2).}
\]

再对 \(d\) 求导：

\[
\partial_dq=1+\|v\|^2,
\qquad
\boxed{
\partial_d\log\frac q{1-q}\bigg|_{d=0}
=\frac1{\kappa_x}.}
\]

这是无限投影的精确恒等式。它不适用于固定有限 Toeplitz 压缩而不付边界泄漏。

### 有限压缩泄漏

对包含中心的有限集合 \(A\)，

\[
D_A=\kappa_x(1+\|v_A\|^2)+\Lambda_A,
\]

\[
\Lambda_A
=x^2\xi_A^*(Q_A-Q_A^2)\xi_A
=x^2\|(I-P_A)QP_A\xi_A\|^2\ge0.
\]

固定 \(x<1\) 的紧参数集上，有限 resolvent 向量族具有紧闭包，强收敛的 \(I-P_A\) 在该紧族上一致趋零，故 \(\Lambda_A\to0\)。这一步没有任何 \(x\uparrow1\) 的统一性；后文的不交换现象正说明不能偷偷补上这种统一性。

## 3. 一次翻位和 actual-law 行能量

外部坐标 \(i\) 的赔率由真实条件概率定义，而非零概率无限 word 的密度比。秩一翻位给出

\[
o_i=\sigma_iG_{ii}-1,
\qquad
q(z^i)-q(z)=\frac{\sigma_i|v_i|^2}{o_i},
\]

以及

\[
\boxed{o_i=\kappa_x(G^2)_{ii}+|v_i|^2.}
\]

在真实概率律下，给定其余位并对 \(Y_i=0,1\) 两端加权，严格有

\[
\mathbb E o_i=1.
\]

所以

\[
\boxed{
\kappa_x\mathbb E(G^2)_{ii}
+\mathbb E|v_i|^2=1.}
\]

该式依赖 actual-law 权重，冻结概率律后不能继续使用。

## 4. 真配置熵的对数赔率桥

令

\[
M(x,d)=\mathbb E_{x,d}\log\frac{q(x,d)}{1-q(x,d)}.
\]

有限块完整 Shannon 熵沿共同对角平移满足

\[
\partial_dH_L(x,d)
=-\sum_{i\in A_L}
\mathbb E_{x,d}\log\frac{q_{L,i}}{1-q_{L,i}}.
\]

对距边界至少 \(R\) 的 anchor，条件期望的 \(L^2\) 投影比较把有限后验控制到真实 all-exterior 后验；边界 anchor 只有 \(O(R)\) 个。先取块极限、再积分 \(d\)，得到

\[
\boxed{\partial_dh_x(d)=-M(x,d)}
\]

而不预设熵率可微。

有限外部集合 \(C\) 上，保留实际边缘质量 \(w_z\) 的完整导数后，

\[
\boxed{
\partial_dM_C
=\mathbb E
\frac{1+\|v_C\|^2}{q_C(1-q_C)}
-\mathcal J_C.}
\]

这里 \(\mathcal J_C\) 恰是 \(w_z'\) 对 logit 的贡献，不是人为添加的校正项。

## 5. actual-law 条件交叉比对象

给定除中心与 \(i\) 外的全部输出，令

\[
p_{ab}^{(i)}
=\Pr(Y_0=a,Y_i=b\mid
Y_{\mathbb Z\setminus\{0,i\}}),
\]

\[
J_i
=\log\frac{p_{10}^{(i)}p_{01}^{(i)}}
{p_{00}^{(i)}p_{11}^{(i)}}.
\]

条件后的二点 DPP 仍负相关，等价的一次翻位公式也给出

\[
J_i
=\operatorname{logit}q(Y_i=0)
-\operatorname{logit}q(Y_i=1)
\ge0.
\]

固定 \(x<1\) 的共同谱隙紧集上，

\[
0\le J_i(z)\le C_\varepsilon|v_i(z)|^2.
\]

Neumann 紧向量集论证提供 \(v\) 族的统一 \(\ell^2\) 空间尾，因此

\[
\mathcal J(x)=\sum_{i\ne0}\mathbb E_{x,0}J_i
\]

绝对收敛，并可由有限窗口在参数紧集上局部一致逼近。所有条件概率首先以 martingale 方式在几乎处处意义识别，再选择统一 resolvent 给出的连续版本；因此可以计算全零、全一等零概率极端 word 的连续版本值，但不把它们称为正概率事件。

## 6. 条件交叉比次概率测度

记

\[
\Delta_i=p_{10}p_{01}-p_{00}p_{11}\ge0,
\qquad
E_i=\Delta_i\sum_{a,b}\frac1{p_{ab}},
\]

并在不同 \(i\) 的条件配置空间不交并上定义

\[
d\nu_x(i,z)
=\kappa_xE_i(z)\,
d\mu_{x,0}^{\mathbb Z\setminus\{0,i\}}(z).
\]

独立输出噪声保证四个 \(p_{ab}\ge\varepsilon_x^2\)。按 \(Y_i=0,1\) 的真实权重直接求和，得到

\[
E_i
=\mathbb E\left[
\frac{|v_i|^2}{D}
\mathrel{\Big|}
Y_{\mathbb Z\setminus\{0,i\}}
\right].
\]

Tonelli 与 Ward 恒等式给出精确总质量

\[
\boxed{
\nu_x(\mathrm{all})
=\kappa_x\mathbb E\frac{\|v\|^2}{D}
=1-\kappa_x\mathbb E\frac1D.}
\]

连续后验版本关于每个外部占据坐标单调递减。全一与全零配置分别给出

\[
q_{\mathbf1}=2\kappa_x,
\qquad
q_{\mathbf0}=1-2\kappa_x.
\]

这只是连续版本端点值，不要求两个无限事件具有正概率。因此

\[
2\kappa_x\le q_z\le1-2\kappa_x,
\]

\[
\kappa_x(1+x^2)\le D_z\le\frac14,
\]

进而

\[
\boxed{
\frac{x^2}{1+x^2}
\le\nu_x(\mathrm{all})
\le x^2.}
\]

特别地，\(x\uparrow1\) 时这个带奇异 \(1/D\) 权重的测度总质量不会消失。

令

\[
\ell=\log\frac{p_{10}p_{01}}{p_{00}p_{11}},
\qquad
U=p_{00}+p_{11},
\]

\[
\mathfrak r(p)
=\frac{\ell}
{(1-e^{-\ell})[1+(e^\ell-1)U]}.
\]

则

\[
\boxed{
\kappa_x\mathcal J(x)
=\int\mathfrak r\,d\nu_x,
\qquad
\mathscr R=1-\int\mathfrak r\,d\nu_x.}
\]

这一步保留了真实条件表、真实其余位分布和全部实际权重。一般合法二点 DPP 并不满足逐表 \(\mathfrak r\le1\)，所以最终判号必须依赖实际平均抵消。

## 7. 与熵率曲率及完整 V14 的精确匹配

由

\[
h_x'(d)=-M(x,d)
\]

和中点 Ward 恒等式，

\[
M_d(x,0)
=\frac1{\kappa_x}-\mathcal J(x).
\]

与已审 S51-B 的

\[
h_x''(0)=-\Gamma_x(0)
\]

比较，得到

\[
\boxed{
\Gamma_x(0)
=\frac1{\kappa_x}-\mathcal J(x).}
\]

这不是循环论证：S51-B 先独立把完整 V14 积分识别为真熵率曲率；本稿从有限配置熵、全部 anchor 和实际交叉比极限独立构造另一表达，再比较二者。

由

\[
(x^2\Gamma_x(0))'=x\mathcal A(x),
\qquad
\kappa_x'=-x/2,
\]

可得

\[
\boxed{
\mathcal A(x)
=\frac1{2\kappa_x^2}
-2\mathcal J(x)-x\mathcal J'(x).}
\]

\(\mathcal J'\) 不是 frozen-law 导数。有限窗口公式同时保留外层实际质量的 score 与四个条件原子的 score；共同条件分母的导数在交叉比中抵消。有限 \(\mathcal J_C\) 局部一致收敛足以使 \(\mathcal J_C'\) 在分布意义收敛到 \(\mathcal J'\)，但不说明各个体积级 score 分量分别收敛，更不提供 \(x\uparrow1\) 的一致可积性。

完整 moving-law 二阶 jet 的 Fisher 型部分在无限投影极限中逐 word 等于

\[
\frac1{2\kappa_x^2}.
\]

其余 \(w''\phi\)、\(2w'\phi'q'\) 与 \(w\phi'q''\) 三项只作为完整分组识别为

\[
-2\mathcal J(x)-x\mathcal J'(x).
\]

原稿没有把裸的无限 score 分量错误地单独定义成收敛对象。

## 8. 端点对数界

由后验区间，每次 logit 跳跃满足

\[
0\le\ell\le
2\log\frac{1+x^2}{1-x^2}
=2\log\cosh\beta.
\]

于是

\[
0\le\mathfrak r
\le
B(\beta)
=\frac{2\log\cosh\beta}
{1-\operatorname{sech}^2\beta}.
\]

结合 \(\nu_x(\mathrm{all})\le x^2\)，

\[
1-B(\beta)x^2
\le\mathscr R
\le1,
\]

\[
\boxed{
\left|\Gamma_x(0)\right|
=O\left(
\frac{\log(1/(1-x))}{1-x}
\right).}
\]

这将**实际律平均后的积分曲率**控制到“对数除以谱隙”的量级，是实质改进；它不是逐 word V14 界，也不推出 \(\Gamma_x(0)\ge0\)。

## 9. 对数噪声尺度与补偿弱极限

定义

\[
\mathscr R(\beta)=1-\kappa_x\mathcal J(x),
\qquad
\mathscr V(\beta)=2\kappa_x^2\mathcal A(x).
\]

直接链式法则给出

\[
\boxed{
\mathscr V
=\mathscr R+x\partial_\beta\mathscr R.}
\]

积分因子产生

\[
\boxed{
\mathscr R(\beta)
=\frac{\int_0^\beta
\sinh t\,\mathscr V(t)\,dt}
{\cosh\beta-1}.}
\]

这是归一化 V14 的正权平均恒等式；端点交叉比界另行给出上一节的 \(\mathscr R\) 区间。原稿把二者相邻叙述成“因此 (5.2)”略显跳跃，但不影响任一公式。

若 \(\beta_n\to\infty\)，定义

\[
r_n(t)
=\frac{\mathscr R(\beta_n+t)}
{1+\beta_n+t},
\qquad
V_n(t)
=\frac{\mathscr V(\beta_n+t)}
{1+\beta_n+t}.
\]

\(r_n\) 在每个紧区间上一致 \(L^\infty\) 有界，故存在局部弱-* 子列极限 \(r_*\)，且

\[
-2\le r_*\le0
\quad\text{几乎处处}.
\]

分布分部积分给出

\[
\boxed{
V_n\longrightarrow r_*+r_*'
\quad\text{于分布意义，沿一个子列}.}
\]

准确的证据等级是：

- 弱-* 预紧的是补偿后的 \(r_n\)；
- \(V_n\) 只得到分布子列极限；
- 没有 \(V_n\) 的 \(L^1\) 一致可积性；
- 没有有限测度意义的 tightness；
- 没有点态或 \(L^1_{\rm loc}\) 收敛。

若额外证明

\[
\mathscr R(\beta)\to R_*,
\]

则平移后的 \(\mathscr R\) 局部一致趋于常数，分布导数趋零，从而

\[
\mathscr V(\beta+\cdot)\to R_*
\quad\text{于分布意义},
\qquad
\kappa_x\Gamma_x(0)\to R_*.
\]

这是正确的充分条件，但原稿没有证明此前提。即便此前提成立，也不能自动提升为 \(\mathscr V\) 的一致可积、点态或 \(L^1\) 收敛。

## 10. 真实 sine 的普通平均消失与奇异加权障碍

中点输出的协方差谱密度为

\[
S_x(t)=\kappa_x+x^2|t|,
\qquad -\frac12\le t\le\frac12.
\]

线性预测的最小均方误差是

\[
\left(\int_{-1/2}^{1/2}S_x(t)^{-1}\,dt\right)^{-1}
=
\frac{x^2}
{2\log((1+x^2)/(1-x^2))}.
\]

条件期望优于线性预测，因此

\[
\mathbb E q(1-q)
\le
\frac{x^2}
{2\log((1+x^2)/(1-x^2))}.
\]

结合 Ward 恒等式，

\[
\mathbb E\|\sqrt{\kappa_x}v\|^2
=\mathbb ED-\kappa_x
=O(1/\beta)\to0.
\]

但同时

\[
\mathbb E\frac{\kappa_x\|v\|^2}{D}
=\nu_x(\mathrm{all})
\ge\frac{x^2}{1+x^2}\to\frac12.
\]

这严格说明：普通能量平均趋零不能替代带 \(1/D\) 奇异权重的尾部控制。自然端点尺度最难的部分正是这种加权一致可积性，而不是再做一次普通谱能量估计。

## 11. 有限窗口与无噪声极限不交换

任意固定真 sine 主块满足

\[
0<Q_A<I.
\]

所以在 \(x=1\) 时固定窗口仍有严格谱隙，有限后验与导数保持有界，进而

\[
\lim_{x\uparrow1}
\mathbb E_x
\frac{\kappa_x(1+\|v_A\|^2)}
{q_A(1-q_A)}
=0.
\]

若先令 \(A\uparrow\mathbb Z\)，无限投影 Ward 恒等式使显示的归一化响应恒为 \(1\)。因此两种迭代极限分别为 \(1\) 与 \(0\)。

这个定理只针对上述 posterior response。它没有证明完整 V14 本身的两种迭代极限不同。

## 12. spacing scale 的精确逻辑强度

半径 \(R\) 的固定索引窗内，

\[
\kappa_x
\sum_{0<|i|\le R}\mathbb EJ_i
\le
4R\kappa_x\log\cosh\beta.
\]

因此只有在同时满足以下两个条件时：

1. 全修正 \(\kappa_x\mathcal J(x)\) 有正的下极限；
2. 所选窗口要捕获该修正的固定正比例；

才可推出窗口尺度不能满足

\[
R=o\left(
\frac1{\kappa_x\log(1/\kappa_x)}
\right).
\]

这是**条件性的必要尺度**。它不是无条件发散定理，不是充分定位半径，不给出尾误差率，也没有证明真实质量确实集中在该尺度。

## 13. 计算复核

随附脚本与 JSON 已复跑核对：

- 真 sine 压缩覆盖
  \((n,x)=(5,.6),(5,.95),(7,.99),(5,.9999),(5,.9999999)\)；
- 有限循环投影代数覆盖
  \(n=6\)，\(x=.3,.6,.93\)；
- 新运行结果与归档 JSON 逐字段一致；
- 真 sine 最大显示 V14 误差约
  \(2.73\times10^{-12}\)；
- 循环投影最大重标度恒等式误差约
  \(2.16\times10^{-12}\)。

脚本验证有限浮点代数、泄漏恒等式、完整移动律 jet、测度质量及纯投影代数。它不证明无限极限、端点紧性、谱预测定理、spacing 命题或曲率符号。

## 14. 客观难度与贡献判断

这份工作不只是把旧 V14 换一套记号。真正新增并支付的困难是：

1. 从真配置熵而非谱熵出发，建立保留 actual-law 权重的对数赔率导数桥；
2. 把无限坐标交叉比和重组为具有精确总质量的非负次概率测度；
3. 证明固定谱隙下一次和的绝对收敛和实际条件表极限；
4. 将积分曲率的端点增长从粗糙高次逆谱隙压到对数除以谱隙；
5. 严格识别普通平均消失与 \(1/D\) 奇异加权质量不消失之间的鸿沟；
6. 证明固定窗口与无噪声极限对显示响应确实不交换。

以下部分主要是建立新 \(\mathcal J,\nu_x\) 后的精确代数重组，而不是第二个独立难题：

- \(\mathcal A=(2\kappa_x^2)^{-1}-2\mathcal J-x\mathcal J'\)；
- \(\mathscr V=\mathscr R+x\mathscr R'\)；
- 相应的一阶积分因子公式。

相对于文中列明的既有接口，这构成一组非平凡的端点结构引理：它把原来的“高次逆谱隙局部核”问题改写成一个明确的 actual-law 奇异加权测度问题，并排除了固定窗口逐项极限路线。本报告没有做先行工作或投稿标准审计，因此不判断新颖性和论文等级。它仍不是高 \(c\) 判号定理，更没有解决原始全参数凹性猜想。剩余核心难点——自然 \(\kappa_x^2\) 尺度上的一致可积性、实际远距离质量控制及 \(\mathscr R\) 的端点极限/符号——与本稿已完成的代数 ODE 之间仍有真实数学鸿沟。

最准确的发布表述是：**S51 C1 在固定 \(x<1\) 紧集上严格建立了真投影 Ward、actual-law 条件交叉比测度及完整 V14 平均补偿公式，并得到积分曲率端点对数界、补偿弱-* 子列工具和显示响应的不交换定理；自然 \(\kappa_x^2\) 一致可积性与高 \(x\) 曲率正号仍未证明。**
