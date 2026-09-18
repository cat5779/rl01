# S51 — c→1 的 actual-law V14 重标度与平均抵消

## 状态与依赖

**PROVED：**真实半密度 sine 投影的投影 Ward 恒等式；完整实际律的对数赔率熵导数桥；具有精确总质量的条件交叉比测度；V14 实际律平均的精确重标度/补偿方程；积分曲率的端点对数界；带额外对数归一化的端点分布紧性；有限窗口与无噪声极限的不交换；真实 sine 律的谱预测平均能量界。

**INCOMPLETE：**不带额外对数因子的自然重标度极限，以及靠近 c=1 的曲率非负性。没有证明原始全 a、全 rho 的凹性猜想。

本文以本聊天 `S51_CYCLE06_RESULT.md` 的固定谱隙 value/chord bridge 为接口 S51-B，识别完整 V14 与真实熵率。下面新增的投影恒等式、对数赔率桥、条件交叉比测度及其界全部给出证明，不把来源的作者标签视为独立认证。不使用前一轮极窄 c 延拓条带，不使用 S41 定位常数，不借用外部 QWE 的判号或后验支付结论。本文与检查脚本都是作者推导/检查，不是独立认证。

---

# 1. 参数与主结果

固定真实半密度 sine 投影 Q，令

\[
 K_{x,d}=\tfrac12I+x(Q-\tfrac12I)+dI,
 \qquad 0<x<1,\quad |d|<(1-x)/2.
\]

中点参数记为

\[
 \varepsilon_x=(1-x)/2,\quad
 \kappa_x=\varepsilon_x(1-\varepsilon_x)=(1-x^2)/4,\quad
 \beta=\log\frac{1+x}{1-x},\quad x=\tanh(\beta/2).
\tag{1.1}
\]

令 q=q(x,d,z) 为给定全部外部输出后的实际中心后验，

\[
 \phi(q)=(q-\tfrac12)\log\frac q{1-q},\qquad
 F(x,d)=\mathbb E_{x,d}\phi(q).
\]

\(\overline{\mathcal G}_x\) 指中点、未平滑、完整 actual-law V14 核；令

\[
 \mathcal A(x)=\mathbb E_{x,0}\overline{\mathcal G}_x
              =\partial_d^2F(x,0).
\tag{1.2}
\]

S51-B 的参数匹配为 x=cu、d=u delta。因此

\[
 \Gamma_c(0)=\int_0^1u\mathcal A(cu)\,du
            =\frac1{c^2}\int_0^c x\mathcal A(x)\,dx.
\tag{1.3}
\]

这不是对 Gamma 的重新定义，而是已给出的真实熵率/V14 接口。

本文从实际二点条件概率构造非负函数 \(\mathcal J(x)\)，证明

\[
 \boxed{\Gamma_x(0)=\frac1{\kappa_x}-\mathcal J(x)}
\tag{1.4}
\]

和

\[
 \boxed{\mathcal A(x)=\frac1{2\kappa_x^2}
                    -2\mathcal J(x)-x\mathcal J'(x).}
\tag{1.5}
\]

导数 \(\mathcal J'\) 的有限实际律表达及弱极限在第 6 节支付。

定义显式响应与归一化 V14 平均

\[
 \mathscr R(\beta)=1-\kappa_x\mathcal J(x),\qquad
 \mathscr V(\beta)=2\kappa_x^2\mathcal A(x).
\tag{1.6}
\]

则

\[
 \boxed{\mathscr V=\mathscr R+x\,\partial_\beta\mathscr R},
 \qquad
 \boxed{\mathscr R=\kappa_x\Gamma_x(0)}.
\tag{1.7}
\]

后一等式是从显式条件交叉比对象推出的识别，不是用曲率命名余项。

---

# 2. 真无限投影的 Ward 恒等式；有限块的泄漏

取 C=Z\{0}，在中点定义

\[
 B_z=K_{x,C}-\operatorname{diag}(1-z),\quad
 G_z=B_z^{-1},\quad b=xQ_{C0},\quad v_z=G_zb,
\]

\[
 q_z=\tfrac12-b^*G_zb,\qquad D_z=q_z(1-q_z).
\]

对固定 x<1，\(\|G_z\|\le\varepsilon_x^{-1}\)，且 b 属于 ell2。有限 Schur 后验通过统一 Neumann/紧向量集论证收敛到这里的连续版本；再用条件期望 martingale 识别为实际 all-exterior 后验。

令 \(\xi=(1,-v_z)\)。由 Schur 方程

\[
 K_x\xi=(q_z,-D^{\rm vac}_zv_z),\quad
 D^{\rm vac}_z=\operatorname{diag}(1-z),
\]

故

\[
 \xi^*K_x(I-K_x)\xi=q_z-q_z^2.
\]

真正的无限 Q 是投影，所以

\[
 K_x(I-K_x)=\kappa_x I.
\]

得到逐字恒等式

\[
 \boxed{D_z=\kappa_x(1+\|v_z\|^2).}
\tag{2.1}
\]

固定 x 对 d 微分，b 不变、\(\partial_dG=-G^2\)，故

\[
 \partial_dq=1+\|v\|^2,
 \qquad
 \boxed{\left.\partial_d\log\frac q{1-q}\right|_{d=0}
             =\frac1{\kappa_x}.}
\tag{2.2}
\]

这给出正确的横向尺度 d=O(kappa)，而不是一个基于粗逆矩阵范数的猜测。

## 2.1 一次翻位与实际平均行能量

记 \(\sigma_i=2z_i-1\)，无限外部上的赔率严格定义为

\[
 o_i(z)=\frac{\Pr(Y_i=1-z_i\mid Y_{C\setminus\{i\}}=z_{C\setminus\{i\}})}
 {\Pr(Y_i=z_i\mid Y_{C\setminus\{i\}}=z_{C\setminus\{i\}})}.
\]

不使用无限 word 密度之比。有限行列式秩一更新及其局部极限给出

\[
 o_i=\sigma_iG_{ii}-1,\quad
 q(z^i)-q(z)=\frac{\sigma_i|v_i|^2}{o_i}.
\tag{2.3}
\]

因为

\[
 K_{x,C}(I-K_{x,C})=\kappa_xI+bb^*,
\]

以及

\[
 GK_{x,C}(I-K_{x,C})G=(S_zG+GS_z)/2-I,
\]

得到

\[
 \boxed{o_i=\kappa_x(G^2)_{ii}+|v_i|^2.}
\tag{2.4}
\]

在实际律下 \(\mathbb E o_i=1\)：给定其余外部位，若 i 的成功概率是 r，则两端加权和是
\((1-r)r/(1-r)+r(1-r)/r=1\)。因而

\[
 \boxed{\kappa_x\mathbb E(G^2)_{ii}+\mathbb E|v_i|^2=1.}
\tag{2.5}
\]

这里明确使用了实际概率权重，不能冻结概率后引用此式。

## 2.2 有限 Toeplitz 块绝不直接使用 (2.1)

令 A 为包含中心的有限集合、\(Q_A\) 是真投影的主压缩。有限后验向量 \(\xi_A=(1,-v_A)\) 满足

\[
 \boxed{D_A=\kappa_x(1+\|v_A\|^2)+\Lambda_A,}
\tag{2.6}
\]

其中

\[
 \Lambda_A=x^2\xi_A^*(Q_A-Q_A^2)\xi_A
           =x^2\|(I-P_A)QP_A\xi_A\|^2\ge0.
\tag{2.7}
\]

这是恒等式，不是未知误差的重命名。

固定 x<1 时，嵌入后的 \(v_A\) 在全部 word 上一致收敛；其像具有紧闭包。强收敛的 \(I-P_A\) 在该紧向量族上统一趋零，故 \(\Lambda_A\to0\)。本论证只在固定谱隙紧集上一致，未延拓到 x=1。

---

# 3. 新的对数赔率熵导数桥

记

\[
 M(x,d)=\mathbb E_{x,d}\log\frac{q(x,d)}{1-q(x,d)}.
\]

本节独立证明

\[
 \boxed{\partial_d h_x(d)=-M(x,d).}
\tag{3.1}
\]

## 3.1 精确有限块公式与全部锚点

对有限块 A_L，完整实际概率沿对角平移的导数是逐位加性 Bernoulli 信道导数之和。固定锚点 i 并给定其余位，令两端概率为 p0=w(1-q)、p1=wq。该坐标的概率导数为 (-w,w)，故对完整 Shannon 熵的贡献为

\[
 -w\log(p_1/p_0).
\]

于是

\[
 \partial_dH_L(x,d)=-\sum_{i\in A_L}
   \mathbb E_{x,d}\log\frac{q_{L,i}}{1-q_{L,i}}.
\tag{3.2}
\]

这是真实配置熵公式，不是 Tr b(K)。

在参数紧集上所有后验都属于共同的 [epsilon,1-epsilon]。logit 在此区间有统一 Lipschitz 常数。对距边界至少 R 的锚点，条件期望的 L2 投影性质给出

\[
 \mathbb E|q_{L,i}-q_\infty^{(i)}|^2
 \le\mathbb E|q_R-q_\infty|^2\longrightarrow0.
\]

边界锚点仅有至多 2R 个，且 logit 有界。因此 (3.2) 的锚点平均逐点趋向 -M。先积分 d，再由支配收敛和块熵率的值极限得到

\[
 h_x(d_2)-h_x(d_1)=-\int_{d_1}^{d_2}M(x,t)\,dt.
\]

有限后验的局部统一收敛与实际有限边缘概率的连续性使 M 连续，证明 (3.1)。没有假设熵率可微。

## 3.2 完整的一阶移动律导数

对有限外部集 C，令 w_z 是实际边缘质量。其完整对角导数为

\[
 w'_z=\sum_{i\in C}\sigma_i(z)(w_z+w_{z^i}).
\tag{3.3}
\]

对每条边把两端合并，得到

\[
 \boxed{\partial_dM_C
 =\mathbb E\frac{1+\|v_C\|^2}{q_C(1-q_C)}-\mathcal J_C.}
\tag{3.4}
\]

这里没有删除 w'。第二项正是 w' 对 logit 的贡献，定义如下。

给定 C\{i} 的实际输出，取中心与 i 的四个条件概率

\[
 p_{ab}^{(i)}=\Pr(Y_0=a,Y_i=b\mid Y_{C\setminus\{i\}}),
 \quad a,b\in\{0,1\}.
\]

定义

\[
 J_i=\log\frac{p_{10}^{(i)}p_{01}^{(i)}}{p_{00}^{(i)}p_{11}^{(i)}}.
\tag{3.5}
\]

一次翻位公式意味着 q(yi=0)≥q(yi=1)，所以 J_i≥0，而且

\[
 J_i=\operatorname{logit}q(yi=0)-\operatorname{logit}q(yi=1).
\]

\(\mathcal J_C=\sum_{i\in C}\mathbb E J_i\)，期望取真实的其余位边缘律。

## 3.3 一次和的空间尾、参数极限

在任何共同谱隙紧集上，(2.3) 与 logit Lipschitz 性给出

\[
 0\le J_i(z)\le C_\varepsilon |v_i(z)|^2.
\tag{3.6}
\]

S51 中使用的 Neumann 紧向量集引理可以直接在这里证明：

\[
 (S/2+H)^{-1}=2\sum_{k\ge0}(-2SH)^kS,
 \qquad\sup\|2H\|<1.
\]

有限截断算子强收敛；对固定向量，其所有符号翻转组成紧集。一致有界的强收敛算子在紧向量集上统一收敛。逐阶归纳，再支付几何级数尾，得到 v 和固定逆矩阵列的逐字一致收敛。v 族紧性又给出

\[
 \sup\sum_{i\notin C_m}|v_i|^2\to0.
\]

由 (3.6)，全部一次交叉比和有统一消失的空间尾。每个固定指标的条件后验及其翻位值一致收敛。因此 \(\mathcal J_C\to\mathcal J\) 在参数紧集上局部一致，其中

\[
 \boxed{\mathcal J(x)=\sum_{i\ne0}
 \mathbb E_{x,0}\log\frac{p_{10}^{(i)}p_{01}^{(i)}}{p_{00}^{(i)}p_{11}^{(i)}}}
\tag{3.7}
\]

使用全部其余坐标的实际二点条件表。

(3.4) 两项也局部一致收敛，故先对有限 d 弦积分再取极限，证明 M 可微及其极限导数。中点使用 (2.1)，得到

\[
 M_d(x,0)=1/\kappa_x-\mathcal J(x).
\]

结合 (3.1) 和 S51-B 对同一熵率曲率的识别，证明 (1.4)。这是两个独立支付过有限极限操作的局部表达之间的匹配。

---

# 4. 实际条件交叉比测度：新工具的核心对象

以下所有二点表均给定 Z_{Z\{0,i}}，使用真实边缘权重。四个概率严格正：给定潜在输入时两个未观察输出各保留自身噪声，故 p_ab≥epsilon_x^2。

记

\[
 \Delta_i=p_{10}p_{01}-p_{00}p_{11}\ge0,\qquad
 E_i=\Delta_i\sum_{a,b}\frac1{p_{ab}}.
\tag{4.1}
\]

在不同 i 的其余位配置空间的互不相交并上定义

\[
 \boxed{d\nu_x(i,z)=\kappa_x E_i(z)\,
                 d\mu_{x,0}^{\mathbb Z\setminus\{0,i\}}(z).}
\tag{4.2}
\]

它不是抽象余项，而是直接从四个真实条件概率构造的非负测度。

## 4.1 精确总质量

固定其余位，令 r=p01+p11。则

\[
 q_0=p_{10}/(1-r),\quad q_1=p_{11}/r,
 \quad q_0-q_1=\Delta_i/[r(1-r)].
\]

由 (2.3)，

\[
 |v_i(yi=0)|^2=\Delta_i/(1-r)^2,\quad
 |v_i(yi=1)|^2=\Delta_i/r^2.
\]

直接按实际权重 (1-r,r) 求平均得

\[
 \mathbb E\left[\left.\frac{|v_i|^2}{q(1-q)}\right|
                          Y_{\mathbb Z\setminus\{0,i\}}\right]
 =\Delta_i\left(\frac1{p00}+\frac1{p01}+\frac1{p10}+\frac1{p11}\right)
 =E_i.
\tag{4.3}
\]

Tonelli 与 (2.1) 给出

\[
 \boxed{\nu_x(\mathrm{all})
 =\kappa_x\mathbb E\frac{\|v\|^2}{D}
 =1-\kappa_x\mathbb E\frac1D.}
\tag{4.4}
\]

因此原来无限多坐标的正能量和，变成了一个有精确总质量的次概率测度。

## 4.2 半密度真投影的更强后验区间

连续 resolvent 版本的 q 对每个外部占据坐标递减。全 1 word 给出

\[
 q_{\bf1}=1/(K_x^{-1})_{00}=2\kappa_x,
\]

因为 \(K_x^{-1}=(I-K_x)/\kappa_x\) 且中心对角是 1/2。全 0 word 同理给出 \(q_{\bf0}=1-2\kappa_x\)。这里是在计算连续版本在两个配置上的值，不要求这两个无限事件有正概率。

故

\[
 \boxed{2\kappa_x\le q_z\le1-2\kappa_x.}
\tag{4.5}
\]

从而

\[
 \kappa_x(1+x^2)\le D_z\le1/4,
\]

以及

\[
 \boxed{\frac{x^2}{1+x^2}\le\nu_x(\mathrm{all})\le x^2.}
\tag{4.6}
\]

特别地，x→1 时该精确归一化能量测度的总质量不消失。

## 4.3 无量纲二点因子

当 Delta>0，令

\[
 \ell=\log\frac{p10p01}{p00p11},\quad U=p00+p11,
\]

\[
 \boxed{\mathfrak r(p)
 =\frac{\ell}{E_i}
 =\frac{\ell}{(1-e^{-\ell})[1+(e^\ell-1)U]}.}
\tag{4.7}
\]

Delta=0 时置 r=1；该集合的 nu 权重为零。于是

\[
 \boxed{\kappa_x\mathcal J(x)=\int\mathfrak r(p)\,d\nu_x,\qquad
 \mathscr R=1-\int\mathfrak r\,d\nu_x.}
\tag{4.8}
\]

这明确保留了实际条件表、实际其余位分布及全部归一化。

不要求 r≤1。这个逐表不等式对一般合法二点 DPP 是假的。例如

\[
 (p_{ab})=\begin{pmatrix}.01&.97\\ .01&.01\end{pmatrix}
\]

给出 r=1.58300144...>1。该表是合法二点 DPP：可取

\[
 K=\begin{pmatrix}.02&\sqrt{.0096}\\ \sqrt{.0096}&.98\end{pmatrix},
\]

其特征值均严格在 (0,1)。这不是关于此表在真 sine 条件律中可达的断言，更不是凹性猜想的反例；它只否定无条件逐表支付的做法。

---

# 5. 端点平均界：不再支付高次逆谱隙

令

\[
 L_x=\log\frac{1+x^2}{1-x^2}=\log\cosh\beta.
\]

由 (4.5)，任何一次 logit 跳跃满足 0≤ell≤2L_x。因此

\[
 0\le\mathfrak r\le
 B(\beta):=\frac{2\log\cosh\beta}{1-\operatorname{sech}^2\beta}.
\tag{5.1}
\]

证明：式 (4.7) 的第二个方括号≥1，而 t/(1-e^{-t}) 在 t≥0 单调增加。零点取连续值 B(0)=1。

于是

\[
 \boxed{1-B(\beta)x^2\le\mathscr R\le1.}
\tag{5.2}
\]

换回 x，

\[
 \boxed{
 \frac{1-\frac{(1+x^2)^2}{2}\log\frac{1+x^2}{1-x^2}}{\kappa_x}
 \le\Gamma_x(0)\le\frac1{\kappa_x}.}
\tag{5.3}
\]

特别地

\[
 \boxed{|\Gamma_x(0)|=O\!\left(
 \frac{\log(1/(1-x))}{1-x}\right),\quad x\uparrow1.}
\tag{5.4}
\]

这是完整 V14 **积分曲率** 的实际律界，不是单个 word 的 V14 界。没有声称点态核已从高次逆谱隙降到这个阶，也没有由下界在高 c 区判出正号。

---

# 6. 完整 V14 的平均抵消及移动律径向导数

S51-B 给出 \((x^2\Gamma_x(0))'=x\mathcal A(x)\)。将第 3 节独立证明的 \(\Gamma_x(0)=1/\kappa_x-\mathcal J(x)\) 代入，利用 \(\kappa'_x=-x/2\)，得到

\[
 \boxed{\mathcal A(x)=\frac1{2\kappa_x^2}
                 -2\mathcal J(x)-x\mathcal J'(x).}
\tag{6.1}
\]

固定 x<1，S51 的完整局部核连续性使 A 连续；因此从桥的积分式先得到 Gamma 的 C1，再由 (1.4) 推出 J 的 C1。没有预设关于熵率的混合参数可微性。

## 6.1 这是完整 moving-law jet 的抵消

有限条件窗口的精确二阶导数是

\[
 F_C''=\sum_z\{w''\phi+2w'\phi'q'+w\phi'q''+w\phi''(q')^2\}.
\tag{6.2}
\]

撇号对 d 求导。由于 \(\phi''=1/(2D^2)\) 和 (2.2)，固定 x 的无限投影极限满足

\[
 \boxed{\lim_{C\uparrow C_\infty}
       \sum_z w_z\phi''(q_z)(q'_z)^2=\frac1{2\kappa_x^2}.}
\tag{6.3}
\]

其余三个完整项作为有限和整体的极限恰为

\[
 \boxed{\lim_C\sum_z
  [w_z''\phi(q_z)+2w_z'\phi'(q_z)q_z'+w_z\phi'(q_z)q_z'']
       =-2\mathcal J(x)-x\mathcal J'(x).}
\tag{6.4}
\]

不把其中任意一个无限-volume score 项单独定义为收敛对象。式 (6.4) 是对完整分组的识别，不能改成冻结 w 的后验 Hessian。

## 6.2 J' 的有限实际律公式与弱极限

对有限 A={0}∪C、i∈C，设 E=A\{0,i}，W_z=P(Y_E=z)。令

\[
 \mathcal S_E(z)=\operatorname{Tr}[(K_{x,E}-D_z^{\rm vac})^{-1}
                                      (Q_E-I/2)],
\]

\(\mathcal S_{ab,z}\) 是完整 A 配置 (a,b,z) 的相同 x-score。行列式微分给出

\[
 W'_z=W_z\mathcal S_E(z),\qquad
 J_i'=\mathcal S_{10,z}+\mathcal S_{01,z}
              -\mathcal S_{00,z}-\mathcal S_{11,z}.
\]

四个条件概率中共同的 W 分母导数因系数和为零而精确消去；外层 W 的导数仍保留。因此

\[
 \boxed{\mathcal J_C'(x)=\sum_{i,z}W_z\{
   \mathcal S_E(z)J_i(z)+\mathcal S_{10,z}+\mathcal S_{01,z}
                 -\mathcal S_{00,z}-\mathcal S_{11,z}\}.}
\tag{6.5}
\]

不逐项界定体积大小的 score。第 3 节已经证明 J_C 在任意 x<1 的紧集局部一致收敛；故对任意紧支撑光滑测试函数 psi，

\[
 \int\mathcal J_C'\psi=-\int\mathcal J_C\psi'
       \longrightarrow-\int\mathcal J\psi'.
\tag{6.6}
\]

这支付了 (6.1) 所用的实际移动律径向导数，允许弱导数先行；不能由此宣称未补偿的 (6.5) 各分量在端点一致可积。

---

# 7. 对数噪声尺度上的精确转移工具

因 dx/d beta=2kappa，(6.1) 等价于

\[
 \boxed{\mathscr V(\beta)=\mathscr R(\beta)
                       +x(\beta)\mathscr R'(\beta).}
\tag{7.1}
\]

令 beta→0；独立 Bernoulli 给出 A(0)=8、Gamma_0(0)=4，因此 R(0)=V(0)=1。对一阶方程使用积分因子

\[
 x^2/\kappa=4\sinh^2(\beta/2),
\]

得到

\[
 \boxed{\mathscr R(\beta)=
 \frac{\int_0^\beta\sinh t\,\mathscr V(t)\,dt}{\cosh\beta-1}.}
\tag{7.2}
\]

权重为正且积分为 1。因此 (5.2) 是一个完整归一化 V14 的实际平均约束，不是逐字或逐分量符号声明。

写 t=beta-s 后，权重为

\[
 w_\beta(s)=\frac{\sinh(\beta-s)}{\cosh\beta-1}\mathbf1_{0<s<\beta}.
\tag{7.3}
\]

它在固定 s 上趋向 exp(-s)。这展示端点是对数噪声尺度上约一个单位长度的加权平均。由于 V 尚无端点绝对可积界，不能只凭权重收敛就替换被积函数并交换极限。

固定 c 时，归一化熵函数

\[
 \mathfrak h_c(t)=\frac{h_c(\kappa_ct)-h_c(0)}{\kappa_c}
\]

在原合法域内满足

\[
 \mathfrak h_c''(0)=-\kappa_c\Gamma_c(0)=-\mathscr R(\beta_c).
\tag{7.4}
\]

本轮只对中点证明上述投影闭合；不把它自动延伸到 t≠0 的一致有限弦极限。

---

# 8. 已验证的端点弱紧性；自然重标度仍缺什么

## 8.1 无附加假设的对数补偿弱紧性

令 beta_n→∞，在每个固定紧 t 区间上定义

\[
 r_n(t)=\frac{\mathscr R(\beta_n+t)}{1+\beta_n+t},
\qquad
 V_n(t)=\frac{\mathscr V(\beta_n+t)}{1+\beta_n+t}.
\]

(5.2) 保证 r_n 局部统一 L∞ 有界。因为 B(beta)/beta→2、x→1，任意弱星子列极限 r_* 满足

\[
 -2\le r_*\le0\quad\text{几乎处处}.
\]

由 (7.1)，

\[
 V_n=r_n+x_n r_n'+\frac{x_n}{1+\beta_n+t}r_n.
\]

这里 x_n→1、x_n'=2kappa_n→0 在固定紧集一致。分部积分后即可通过弱星极限，得到

\[
 \boxed{V_n\longrightarrow r_*+r_*'\quad\text{于分布意义，沿一个子列}.}
\tag{8.1}
\]

此处所有假设都由实际律的正测度总质量及二点比值界验证了。不需要单独控制随尺度增长的核导数。

## 8.2 自然 kappa^2 重标度的精确充分条件

如果进一步证明显式条件交叉比响应 R(beta) 有有限极限 R_*，那么 (7.1) 立即给出

\[
 \mathscr V(\beta+\cdot)\longrightarrow R_*
 \quad\text{于分布意义},
\]

并且

\[
 \kappa_x\Gamma_x(0)\longrightarrow R_*.
\tag{8.2}
\]

不必额外假设 R'→0；分布分部积分已经处理它。

但是，本文没有证明 R 的有限端点极限，也没有证明不带 (1+beta) 的局部统一有界性。式 (8.1) 不能被改写成 (8.2) 已成立。

---

# 9. 真实 sine 律额外提供的平均消失机制

这一节使用一个可迁移到一般平稳过程的谱线性预测工具，而不是 DPP 专用的形式抵消。

对中点输出，协方差谱密度为

\[
 S_x(t)=\kappa_x+x^2|t|,\qquad -1/2\le t\le1/2.
\tag{9.1}
\]

证明：DPP 协方差为 off-diagonal -x^2|Q_0j|^2、对角 1/4；半圆弧与平移自身的交叠长度为 1/2-|t|，故傅里叶变换给出 (9.1)。

对任意有限线性预测误差系数 a_j，要求 a_0=1，其方差为

\[
 \int_{-1/2}^{1/2}|\widehat a(t)|^2S_x(t)\,dt.
\]

Cauchy–Schwarz 给出下界 \((\int S_x^{-1})^{-1}\)。取 \(\widehat a\) 逼近 \(1/(S_x\int S_x^{-1})\) 的三角多项式并保持常数 Fourier 系数为 1，可达到该下确界。条件期望优于线性预测，故

\[
 \boxed{\mathbb E_{x,0}q(1-q)
 \le\left(\int_{-1/2}^{1/2}\frac{dt}{S_x(t)}\right)^{-1}
 =\frac{x^2}{2\log((1+x^2)/(1-x^2))}.}
\tag{9.2}
\]

x=0 取连续值 1/4。特别地，结合 (2.1)，

\[
 \boxed{\mathbb E\|\sqrt{\kappa_x}\,v\|^2
        =\mathbb E D-\kappa_x=O(1/\beta)\to0.}
\tag{9.3}
\]

但与此同时，第 4 节证明

\[
 \mathbb E\frac{\kappa_x\|v\|^2}{D}
 =\nu_x(\mathrm{all})\ge\frac{x^2}{1+x^2}\to\frac12.
\tag{9.4}
\]

这两个结论可以同时成立。它们严格展示：未经 1/D 重加权的实际能量平均趋零，不能替代 V14/交叉比测度需要的奇异加权控制。

---

# 10. 两种不可忽略的端点空间义务

## 10.1 有限块与无噪声极限确实不交换

对任意固定真 sine 块 A，0<Q_A<I。理由是非零有限三角多项式不可能在 E 或其补集的开区间上恒为零。因此 x=1 时有限块仍有严格谱隙，所有有限后验及其 d 导数均有界。故

\[
 \lim_{x\uparrow1}\mathbb E_x
 \frac{\kappa_x(1+\|v_A\|^2)}{q_A(1-q_A)}=0.
\]

而先取 A↑Z 时，由 (2.1) 该归一化响应恒为 1。因此

\[
 \boxed{\lim_{x\uparrow1}\lim_{A\uparrow\mathbb Z}
 \mathbb E_x\frac{\kappa_x(1+\|v_A\|^2)}{q_A(1-q_A)}=1,
 \quad
 \lim_{A\uparrow\mathbb Z}\lim_{x\uparrow1}
 \mathbb E_x\frac{\kappa_x(1+\|v_A\|^2)}{q_A(1-q_A)}=0.}
\tag{10.1}
\]

这个不交换定理针对显示的后验响应，不冒充已经证明 V14 本身两种迭代极限不同。

## 10.2 任何非零归一化交叉比修正都不能来自固定索引窗

对真正 all-exterior 二点条件表，

\[
 \kappa_x\sum_{0<|i|\le R}\mathbb E J_i
 \le4R\kappa_x\log\cosh\beta.
\tag{10.2}
\]

若 R(x) kappa_x log cosh beta→0，该窗口的归一化修正趋零。若全修正 kappa J 有正的下极限，那么要捕获其固定比例，索引窗口至少不能是 o(1/(kappa log(1/kappa)))。

这是必要的端点空间分辨率，不是充分的定位误差估计，也不改进或借用 S41 常数。它尤其说明不能把固定 i 的端点极限逐项求和。

---

# 11. 精确剩余义务

本轮把判号问题写成

\[
 \Gamma_x(0)\ge0
 \quad\Longleftrightarrow\quad
 \int\mathfrak r\,d\nu_x\le1.
\tag{11.1}
\]

等价地，允许真实平均抵消的支付式是

\[
 \int(\mathfrak r-1)_+\,d\nu_x
 \le\kappa_x\mathbb E(1/D)
      +\int(1-\mathfrak r)_+\,d\nu_x.
\tag{11.2}
\]

没有要求每个二点表 r≤1，也没有证明 (11.2)。端点自然重标度另需控制这些实际加权量在远距离索引/对数尺度上的极限，不能只证明固定条件表收敛。

投影 Ward 的机制适用于一般有界正交投影；半密度用于中心对角 1/2、(4.5) 的对称形式和 (9.1) 的具体谱密度。本文不声称获得全密度、离中点、合法端点的凹性定理。

---

# 12. 来源接口与检查范围

使用的来源：

* 本聊天 `S51_CYCLE06_RESULT.md`，接口仅为完整 actual-law V14 的固定谱隙 value/chord 识别、有限局部完整二阶核的局部统一极限。没有从中借用 x→1 一致性。
* `results/SA03/SA03_S9_SIGNED_TRANSPORT.md`：有限 Schur/翻位/完整移动律 jet。本文使用的相关一阶恒等式重新推导；来源作者状态不被视为独立认证。
* `results/SA03/SA03_VOLUME_LIMIT.md`：确认 V14 的完整分组与原始 scope warning。未使用 Fejer 近似；一直采用真 Q 的主压缩。
* `TARGET.md`：冻结的完整配置熵、真 sine 核、独立条件噪声模型与未解决区间。

未使用：S41 的定位常数、S43/S44 未审结论、前轮 C37 极窄条带、任何外部 QWE 判号结论。

公开来源根：
`https://raw.githubusercontent.com/cat5779/rl01/research/sa-cycle06-s51-s56-20260918/`

检查脚本 `S51_C1_checks.py` 明确保留真有限 sine 块的 Lambda 泄漏，并另设有限循环正交投影检查纯投影代数。后者不是实际 sine 极限的替代物。

浮点检查包括：完整概率归一化；Ward+泄漏；M 的完整移动律一阶 jet；nu 精确质量；有限 V14 完整二阶 jet；有限真投影上的 (6.1)。最大显示误差约 2e-12 量级。它们不证明无限极限或符号，不构成独立认证。

对 n=5 的真 sine 块，归一化响应 E[kappa(1+||v||^2)/D] 在 x=0.9999 为约 0.00198671，在 x=0.9999999 为约 0.00000200263；丢失部分恰是 E[Lambda/D]，两者之和为 1。这只是 (10.1) 的有限代数演示。

## 结论

本轮获得的是一条可复用的端点研究主干：

\[
 \text{真实投影 Ward}
 \ \longrightarrow\ 
 \text{实际条件交叉比次概率测度}
 \ \longrightarrow\ 
 \mathscr V=\mathscr R+x\mathscr R'
 \ \longrightarrow\ 
 \text{严格的端点补偿弱极限工具}.
\]

核心新增结果已证明；自然重标度的有限极限及高 c 非负性仍明确保留为未完成义务。
