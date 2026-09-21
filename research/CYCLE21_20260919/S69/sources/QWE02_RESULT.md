# QWE02：真实 sine-DPP 互信息弦的边界响应界

**日期：2026-09-18。**  
**任务对应：** `randomcat4/dpp-stationary-entropy`，PR #123；任务包 `research_tasks/external_20260918/QWE02/`。  
**状态：PROVED（本文给出证明；尚未经另行独立审查）。**  
**本轮交付：** 二次弦长因子的全尺度边界响应界及可复现证伪测试。本文不宣称完整熵率凹性。

本文遵循 Google Drive 中的 `QWE02_启动提示词.txt` 和 `QWE02_PACKET.md`。所有熵均为空间配置的经典 Shannon 熵，使用自然对数。不存在以计数熵或量子谱熵替代配置熵的步骤。

---

## 1. 最强结果

### 定理 1：任意一致有谱隙的有限 Hermitian DPP

设有限站点集分成不交的两块 \(A,B\)，

\[
K(a)=aI+K_* ,\qquad
\delta I\preceq K(a)\preceq(1-\delta)I
\quad(a\in I),\qquad 0<\delta<\tfrac12.
\]

这里 \(K_*\) 与 \(a\) 无关，\(I\) 是实区间。令

\[
C=K_{AB},\qquad
\mathcal J(a)=I_{\operatorname{DPP}(K(a))}(Y_A;Y_B).
\]

则在整个区间上有

\[
\boxed{\quad
|\mathcal J''(a)|\le32\delta^{-12}\|C\|_{\mathrm{HS}}^2.
\quad} \tag{1}
\]

块大小可以不相等；常数与块大小、空间排列、配置及 \(a\) 无关。区间端点处的导数理解为由其严格可行邻域给出的导数。只要弦 \([a-\eta,a+\eta]\subset I\)，便有

\[
\boxed{\quad
|\Delta_\eta\mathcal J(a)|
\le32\delta^{-12}\eta^2\|C\|_{\mathrm{HS}}^2.
\quad} \tag{2}
\]

这里不要求互信息曲率为正，也不要求任何配置贡献为正。

### 推论 2：QWE02 指定的真实 sine 模型

取真实 Toeplitz 压缩

\[
(Q_\rho)_{ij}=\begin{cases}
\rho,&i=j,\\
\sin(\pi\rho(i-j))/(\pi(i-j)),&i\ne j,
\end{cases}
\qquad K(a)=aI+cQ_\rho.
\]

在基准

\[
\rho=\tfrac12,\qquad c=\tfrac{19}{20},\qquad
I=[\tfrac3{200},\tfrac7{200}],\qquad\delta=\tfrac3{200},
\]

上，对所有整数 \(L\ge1\) 和所有包含在 \(I\) 内的弦，

\[
\boxed{
(-\Delta_\eta J_L(a))_+
\le C_I\eta^2[1+\log(1+L)],\qquad
C_I=\frac{64(19/20)^2}{\pi^2(3/200)^{12}}.
} \tag{3}
\]

所以题目要求的指数可以取 **\(p=1\)**。事实上本文证明绝对值版本，而不只是负部版本。

更方便求和的形式是

\[
|\Delta_\eta J_L(a)|
\le\Gamma\eta^2(2+\log L),\qquad
\Gamma=\frac{32c^2}{\pi^2\delta^{12}}. \tag{4}
\]

若 \(L_*=m2^N\)，则

\[
\boxed{
\sum_{j\ge N}
\frac{|\Delta_\eta J_{m2^j}(a)|}{2m2^j}
\le\Gamma\eta^2\frac{2+\log L_*+\log2}{L_*}.
} \tag{5}
\]

这给出带有独立 \(\eta^2\) 因子的、按 \(O(\log L_*/L_*)\) 消失的尾界。没有对熵率极限求导。

**常数的实际限制。** 式 (3) 的常数约为 \(4.51\times10^{22}\)，非常保守。它完成题目的定量渐近条件，但不是一个能直接支付原有小尺度 benchmark 有限带符号和的实用常数。本文没有由此推出熵率凹性。

---

## 2. 工具的设计与两条机制

需要构造的工具必须同时具有以下性质：它作用于真实配置原子；保留概率加速度和 Fisher 项；两块独立时严格消失；跨块耦合反号时不变；二阶响应由跨块矩阵的 Hilbert–Schmidt 能量支付，而不带体积因子。

### 机制一：零点隔离与复解析估计——没有采用

下面的原子行列式确实在合法参数区间附近有统一的零点隔离。但是直接用 Cauchy 估计控制复杂概率和会付出体积代价。即使对于独立 Bernoulli 的 DPP，在 \(z=1/2+it\) 处，

\[
\sum_y|p_z(y)|
=(|z|+|1-z|)^n=(1+4t^2)^{n/2}.
\]

因此“每个原子对数有统一解析半径”本身不能提供对整个期望的无体积复范数上界。这只是对该中间估计策略的反例，不是对真实 sine 目标的反例。

另一种已知方向是经典互信息的量子值上界；任务包已经提供了这一机制及其适用范围。本文不微分该值上界。

### 机制二：矩阵扰动与迹理想的二阶消去——采用

本文转而把完整经典熵曲率写成一个配置依赖的矩阵泛函 \(\mathcal T_\sigma(R)\) 的期望。该泛函在块对角矩阵上可加，且关于跨块耦合为偶函数。

从 DPP 理论之外迁移的机制是：**用算子范数控制一阶梯度、用 Hilbert–Schmidt 范数控制 Hessian，再对逆矩阵路径作二阶 Taylor 积分。** 所需迹理想不等式为

\[
|\operatorname{tr}(UZ)|\le\|U\|_{\mathrm{op}}\|Z\|_1,
\qquad
\|XYZ\|_1\le\|X\|_{\mathrm{HS}}\|Y\|_{\mathrm{op}}\|Z\|_{\mathrm{HS}}.
\]

使这项迁移成立的新估计是第 6 节的无维数梯度/Hessian 引理。关键不是简单地对所有矩阵条目取绝对值；那样会重新产生体积因子。关键是把梯度中线性的矩阵部分保留为矩阵乘积，只有立方余项使用绝对行和估计。

以下证明是自包含的；没有借用某篇论文未证明的熵响应结论。

---

## 3. 原子鞍点矩阵与一致条件概率界

### 引理 3.1：完整配置的行列式表示

对配置 \(y\in\{0,1\}^n\)，定义

\[
D_{1-y}=\operatorname{diag}(1-y_i),\qquad
M_y=K-D_{1-y},\qquad R_y=M_y^{-1}.
\]

则

\[
p_K(y)=(-1)^{\#\{i:y_i=0\}}\det M_y. \tag{6}
\]

证明：对空位对应的对角线中 \(-1\) 作行列式多线性展开，得到的正是

\[
\sum_{B\subseteq\{i:y_i=0\}}(-1)^{|B|}
\det K_{\{i:y_i=1\}\cup B}.
\]

这是任务固定的完整配置原子，不是计数概率。证毕。

### 引理 3.2：鞍点逆矩阵的一致有界性

若 \(\delta I\preceq K\preceq(1-\delta)I\)，则

\[
\|R_y\|_{\mathrm{op}}\le\delta^{-1}. \tag{7}
\]

证明：设空位数为 \(r\)。由

\[
\delta I-D_{1-y}\preceq M_y
\preceq(1-\delta)I-D_{1-y}
\]

及有序本征值的单调性，\(M_y\) 最小的 \(r\) 个本征值不超过 \(-\delta\)，其余本征值不小于 \(\delta\)。所以没有本征值落入 \((-\delta,\delta)\)。证毕。

### 引理 3.3：一位与两位翻转比的无体积界

令

\[
\sigma_i=1-2y_i\in\{1,-1\},\qquad
 t_i=-1-\sigma_i(R_y)_{ii},
\]

并对 \(i\ne j\) 定义

\[
\varepsilon_{ij}=\sigma_i\sigma_j,\qquad
q_{ij}=|(R_y)_{ij}|^2,\qquad
 d_{ij}=t_it_j-\varepsilon_{ij}q_{ij}.
\]

如果 \(y^i\) 和 \(y^{ij}\) 分别表示翻转一位和两位，则矩阵行列式引理给出

\[
t_i=\frac{p_K(y^i)}{p_K(y)},\qquad
 d_{ij}=\frac{p_K(y^{ij})}{p_K(y)}. \tag{8}
\]

从而

\[
\delta\le t_i\le\delta^{-1},\qquad
\delta^2\le d_{ij}\le\delta^{-2}. \tag{9}
\]

证明一致界：写

\[
K=\delta I+(1-2\delta)\widetilde K,
\qquad0\preceq\widetilde K\preceq I.
\]

先取 \(X\sim\operatorname{DPP}(\widetilde K)\)，然后逐站点独立通过二元信道

\[
\Pr(Y_i=1\mid X_i)=\delta+(1-2\delta)X_i.
\]

对任意有限集合的包含概率展开乘积，并使用主子式展开，可验证输出核正是 \(K\)。给定其他所有输出后，一个指定输出位的两种概率都在 \([\delta,1-\delta]\) 内；两个指定输出位的四种模式概率都在 \([\delta^2,(1-\delta)^2]\) 内。因此相应翻转比位于

\[
[\delta/(1-\delta),(1-\delta)/\delta],\qquad
[(\delta/(1-\delta))^2,((1-\delta)/\delta)^2],
\]

分别蕴含 (9)。矩阵行列式引理中的单翻转原子有额外负号，而双翻转没有，恰得到 (8)。证毕。

**用途限制。** 这里的噪声表示只用于证明一致概率比界。没有在对 \(a\) 求导时冻结一个实际上依赖 \(a\) 的潜在分布。

---

## 4. 保留全部项的经典熵曲率泛函

对函数 \(f:\{0,1\}^n\to\mathbb R\)，定义

\[
\nabla_i f(y)=f(y_{i\leftarrow1})-f(y_{i\leftarrow0}),\qquad
Gf=\sum_i\nabla_i f.
\]

有 \(\nabla_i^2=0\)，不同坐标的算子可交换。

### 引理 4.1：概率的真实对角平移

当 \(K'(a)=I\) 时，

\[
\sum_y p'_a(y)f(y)=\sum_y p_a(y)Gf(y),
\quad
\sum_y p''_a(y)f(y)=\sum_y p_a(y)G^2f(y). \tag{10}
\]

证明：只对 \(K_{ii}\) 求导，(6) 的余子式表明

\[
\partial_{K_{ii}}p_K(y)
=(2y_i-1)p_{K_{-i}}(y_{-i}).
\]

乘以 \(f(y)\) 后对 \(y_i\) 求和，即为第一式。相应概率演化算子不依赖 \(a\)，再微分得到第二式。这保留了所有多坐标概率加速度，并非把 \(p_a(y)\) 当作仿射函数。证毕。

定义矩阵泛函

\[
\mathcal A_\sigma(R)
=2\sum_{i<j}\varepsilon_{ij}
\log\frac{t_it_j-\varepsilon_{ij}|R_{ij}|^2}{t_it_j},
\qquad t_i=-1-\sigma_iR_{ii}, \tag{11}
\]

以及

\[
\boxed{\quad
\mathcal T_\sigma(R)=\mathcal A_\sigma(R)+\operatorname{tr}(R^2).
\quad} \tag{12}
\]

由翻转比可得

\[
\nabla_i\nabla_j\log p_K(y)
=\varepsilon_{ij}\log\frac{d_{ij}}{t_it_j},
\qquad
G^2\log p_K(y)=\mathcal A_\sigma(R_y). \tag{13}
\]

另一方面，完整原子行列式给出

\[
(\log p_a(y))'=\operatorname{tr}R_y,
\qquad
(\log p_a(y))''=-\operatorname{tr}R_y^2.
\]

由 \(\sum_y p_a''(y)=0\)，

\[
\sum_y p_a(y)(\operatorname{tr}R_y)^2
=\sum_y p_a(y)\operatorname{tr}(R_y^2). \tag{14}
\]

这是 Fisher 项的精确表达，不是额外可重复使用的预算。

把 (10)、(13)、(14) 代入完整 Shannon 熵公式，得到

\[
\begin{aligned}
H''(K(a))
&=-\sum_y p_a''(y)\log p_a(y)
  -\sum_y\frac{p_a'(y)^2}{p_a(y)}\\
&=\boxed{-\mathbb E_{p_a}\mathcal T_\sigma(R_y)}.
\end{aligned} \tag{15}
\]

式 (15) 同时保留了概率加速度和 Fisher 信息。\(\mathcal A\) 与 \(\operatorname{tr}R^2\) 的组合未被假定有符号。

---

## 5. 互信息曲率成为逐配置的跨块缺陷

固定 \(a\) 及配置 \(y=(y_A,y_B)\)，定义只改变跨块耦合的路径

\[
K_\theta=
\begin{pmatrix}K_A&\theta C\\\theta C^*&K_B\end{pmatrix},
\quad
M_\theta=K_\theta-D_{1-y},
\quad R_\theta=M_\theta^{-1},
\quad0\le\theta\le1.
\]

由于块对角压缩和原核都有同一谱隙，凸组合 \(K_\theta\) 也满足相同的 \(\delta\) 界。特别地，(7)、(9) 沿整条路径成立。

在 \(\theta=0\) 时，\(R_0=R_A\oplus R_B\)。由 (11)、(12) 的可加性，

\[
\mathcal T_\sigma(R_0)
=\mathcal T_{\sigma_A}(R_A)+\mathcal T_{\sigma_B}(R_B).
\]

在真实联合分布下取期望，边际期望自动正确。式 (15) 因而给出

\[
\boxed{
\mathcal J''(a)
=\mathbb E_{p_a}
\left[\mathcal T_\sigma(R_1)-\mathcal T_\sigma(R_0)\right].
} \tag{16}
\]

这样，乘积参考分布的导数已通过两个边际熵的完整二阶导保留；没有删除任何 moving-reference 项。

接下来证明的是逐配置的**绝对值**上界，而不是逐配置正号：

\[
\left|\mathcal T_\sigma(R_1)-\mathcal T_\sigma(R_0)\right|
\le32\delta^{-12}\|C\|_{\mathrm{HS}}^2. \tag{17}
\]

---

## 6. 新引理：无维数的梯度与 Hessian 界

本节是边界支付的承重部分。

### 引理 6.1

固定 \(\sigma\in\{\pm1\}^n\)。设 Hermitian 矩阵 \(R\) 满足

\[
\|R\|_{\mathrm{op}}\le\delta^{-1},\quad
\delta\le t_i\le\delta^{-1},\quad
 d_{ij}=t_it_j-\sigma_i\sigma_j|R_{ij}|^2\ge\delta^2.
\]

在其定义域内，对任意 Hermitian 方向 \(Z\)，

\[
|D\mathcal A_\sigma(R)[Z]|
\le8\delta^{-7}\|Z\|_1, \tag{18}
\]

\[
|D^2\mathcal A_\sigma(R)[Z,Z]|
\le10\delta^{-8}\|Z\|_{\mathrm{HS}}^2. \tag{19}
\]

因而

\[
|D\mathcal T_\sigma(R)[Z]|
\le10\delta^{-7}\|Z\|_1, \tag{20}
\]

\[
|D^2\mathcal T_\sigma(R)[Z,Z]|
\le12\delta^{-8}\|Z\|_{\mathrm{HS}}^2. \tag{21}
\]

所有常数与 \(n\) 无关。

### 6.1 一阶微分的完整证明

对一对 \(i<j\)，记

\[
r=R_{ij},\quad q=|r|^2,\quad
 t=t_i,\quad u=t_j,\quad\varepsilon=\sigma_i\sigma_j,
\quad d=tu-\varepsilon q,
\]

并令

\[
f=\varepsilon(\log d-\log t-\log u).
\]

方向 \(Z\) 对应

\[
h_i=-\sigma_iZ_{ii},\quad h_j=-\sigma_jZ_{jj},
\quad z=Z_{ij}.
\]

直接微分并先消去不带 \(q\) 的对角项，得到

\[
Df[Z]=\frac{q}{td}h_i+\frac{q}{ud}h_j
-\frac{2\operatorname{Re}(\bar rz)}d. \tag{22}
\]

因此 \(D\mathcal A(R)[Z]=\operatorname{tr}(BZ)\)，其中 \(B\) 是 Hermitian 矩阵，满足

\[
B_{ii}=-2\sigma_i\sum_{j\ne i}\frac{|R_{ij}|^2}{t_i d_{ij}},
\qquad B_{ij}=-\frac{2R_{ij}}{d_{ij}}\quad(i\ne j). \tag{23}
\]

由于

\[
\sum_j|R_{ij}|^2\le\|R\|_{\mathrm{op}}^2\le\delta^{-2},
\]

对角部分的算子范数不超过 \(2\delta^{-5}\)。

令 \(D_t=\operatorname{diag}(t_i^{-1})\)。关键分解为

\[
\frac1{d_{ij}}
=\frac1{t_it_j}
+\frac{\varepsilon_{ij}|R_{ij}|^2}{t_it_jd_{ij}}. \tag{24}
\]

所以 \(B\) 的非对角部分是

\[
-2D_t(R-\operatorname{diag}R)D_t+E,
\]

其中

\[
|E_{ij}|\le2\delta^{-4}|R_{ij}|^3.
\]

第一项的算子范数不超过 \(4\delta^{-3}\)。余项的每行绝对值和满足

\[
\sum_j|E_{ij}|
\le2\delta^{-4}
\left(\max_j|R_{ij}|\right)\sum_j|R_{ij}|^2
\le2\delta^{-7}.
\]

因为 \(E\) 是 Hermitian，其算子范数也不超过 \(2\delta^{-7}\)。所以

\[
\|B\|_{\mathrm{op}}
\le2\delta^{-5}+4\delta^{-3}+2\delta^{-7}
\le8\delta^{-7}.
\]

用迹对偶性即得 (18)。这一步避免了对线性 \(R_{ij}\) 项直接使用绝对行和所产生的 \(\sqrt n\) 损失。

### 6.2 二阶微分的完整证明

令 \(v=\operatorname{Re}(\bar rz)\)。再次微分 (22)，得到

\[
\begin{aligned}
D^2f[Z,Z]={}&
-q\left(\frac1{t^2d}+\frac{u}{td^2}\right)h_i^2
-q\left(\frac1{u^2d}+\frac{t}{ud^2}\right)h_j^2\\
&-\frac{2q}{d^2}h_ih_j
+\frac{4(uh_i+th_j)v}{d^2}
-\frac{2|z|^2}{d}
-\frac{4\varepsilon v^2}{d^2}.
\end{aligned} \tag{25}
\]

使用 \(t,u\in[\delta,\delta^{-1}]\)、\(d\ge\delta^2\)、\(q\le\delta^{-2}\)，以及 \(2xy\le x^2+y^2\)，各项满足

\[
|D^2f[Z,Z]|
\le5\delta^{-6}q(h_i^2+h_j^2)
+10\delta^{-6}|z|^2. \tag{26}
\]

为核对常数：两个纯对角系数各不超过 \(2\delta^{-6}q\)；对角交叉项不超过 \(\delta^{-6}q(h_i^2+h_j^2)\)；混合项不超过 \(2\delta^{-6}q(h_i^2+h_j^2)+4\delta^{-6}|z|^2\)；最后两项不超过 \(6\delta^{-6}|z|^2\)。

因为 \(\mathcal A=2\sum_{i<j}f_{ij}\)，

\[
\begin{aligned}
|D^2\mathcal A(R)[Z,Z]|
&\le10\delta^{-6}\sum_i |Z_{ii}|^2\sum_{j\ne i}|R_{ij}|^2
 +20\delta^{-6}\sum_{i<j}|Z_{ij}|^2\\
&\le10\delta^{-8}\sum_i|Z_{ii}|^2
 +10\delta^{-6}\sum_{i\ne j}|Z_{ij}|^2\\
&\le10\delta^{-8}\|Z\|_{\mathrm{HS}}^2.
\end{aligned}
\]

这证明 (19)。最后，\(\operatorname{tr}R^2\) 的梯度是 \(2R\)，其沿 Hermitian \(Z\) 的 Hessian 是 \(2\operatorname{tr}Z^2\)。分别加入 (18)、(19)，得到 (20)、(21)。引理证毕。

---

## 7. 二阶跨块积分支付边界能量

令

\[
V=\begin{pmatrix}0&C\\C^*&0\end{pmatrix},\qquad
M_\theta=M_0+\theta V,
\qquad F(\theta)=\mathcal T_\sigma(R_\theta).
\]

逆矩阵微分给出

\[
R_\theta'=-R_\theta V R_\theta,
\qquad
R_\theta''=2R_\theta V R_\theta V R_\theta.
\]

故

\[
\|R_\theta'\|_{\mathrm{HS}}
\le\delta^{-2}\|V\|_{\mathrm{HS}},
\qquad
\|R_\theta''\|_1
\le2\delta^{-3}\|V\|_{\mathrm{HS}}^2. \tag{27}
\]

第二个估计把乘积分组为 \((R_\theta V)R_\theta(VR_\theta)\)，使用两个 Hilbert–Schmidt 因子和一个算子范数因子；没有迹维数损失。

链式法则和引理 6.1 现在给出

\[
\begin{aligned}
|F''(\theta)|
&\le12\delta^{-8}\|R_\theta'\|_{\mathrm{HS}}^2
 +10\delta^{-7}\|R_\theta''\|_1\\
&\le(12\delta^{-12}+20\delta^{-10})\|V\|_{\mathrm{HS}}^2\\
&\le32\delta^{-12}\|V\|_{\mathrm{HS}}^2.
\end{aligned} \tag{28}
\]

取 \(W=I_A\oplus(-I_B)\)。有 \(R_{-\theta}=WR_\theta W\)。\(\mathcal A\) 只依赖对角元和非对角元的绝对值平方，\(\operatorname{tr}R^2\) 同样不变，所以 \(F(-\theta)=F(\theta)\)，特别是 \(F'(0)=0\)。

于是

\[
\begin{aligned}
|F(1)-F(0)|
&=\left|\int_0^1(1-\theta)F''(\theta)\,d\theta\right|\\
&\le16\delta^{-12}\|V\|_{\mathrm{HS}}^2
=32\delta^{-12}\|C\|_{\mathrm{HS}}^2.
\end{aligned}
\]

这就是 (17)。在真实联合分布下取期望，利用 (16)，证明定理 1 的曲率界 (1)。最后，有限维光滑性给出

\[
\Delta_\eta\mathcal J(a)
=\int_{-\eta}^{\eta}(\eta-|s|)\mathcal J''(a+s)\,ds.
\]

三角核质量为 \(\eta^2\)，所以 (2) 成立。

注意这里二次弦因子不是在未支付的余项前形式地添加：支付已经在逐配置估计 (17) 中完成。

---

## 8. 真实 sine 跨边界能量与 dyadic 尾

对于相邻长度 \(L\) 的块，距离为 \(r\) 的跨块站点对数为

\[
w_L(r)=\begin{cases}
r,&1\le r\le L,\\
2L-r,&L<r\le2L-1.
\end{cases}
\]

因而

\[
\begin{aligned}
\|(Q_\rho)_{AB}\|_{\mathrm{HS}}^2
&=\frac1{\pi^2}\sum_{r=1}^{2L-1}
\frac{w_L(r)\sin^2(\pi\rho r)}{r^2}\\
&\le\frac1{\pi^2}
\left(\sum_{r=1}^L\frac1r+L\sum_{r>L}\frac1{r^2}\right)\\
&\le\frac{2+\log L}{\pi^2}. \tag{29}
\end{aligned}
\]

这个估计对所有 \(0<\rho<1\) 有效，且使用真正的 Toeplitz 元素，而非有限循环核。\(C=c(Q_\rho)_{AB}\)，所以 (2) 蕴含 (4)。又有

\[
2+\log L\le2[1+\log(1+L)],
\]

于是 (3) 成立。

对尾部写 \(L_j=L_*2^r\)，并使用

\[
\sum_{r\ge0}2^{-r}=2,
\qquad\sum_{r\ge0}r2^{-r}=2,
\]

直接得到 (5)。代入任务包中已审查的 dyadic 恒等式，得到明确的有限截断：

\[
\boxed{
\Delta_\eta h(a)
\le\frac{\Delta_\eta H_m(a)}m
-\sum_{j=0}^{N-1}\frac{\Delta_\eta J_{m2^j}(a)}{2m2^j}
+\Gamma\eta^2\frac{2+\log L_*+\log2}{L_*}.
} \tag{30}
\]

保留尺度的贡献可以是正或负。式 (30) 没有对 \(h\) 求导，也没有交换任何未经证明的导数与极限。

---

## 9. 证伪尝试与模型内测试

### 9.1 一个解析的真实模型检验：逐配置贡献确实可以为负

取基准的 \(L=1\)、\(a=(1-c)/2\)、\(\rho=1/2\)。记

\[
k=c/\pi,\qquad u=\tfrac14-k^2,\qquad v=\tfrac14+k^2.
\]

四个真实配置概率为

\[
p_{00}=p_{11}=u,\qquad p_{01}=p_{10}=v.
\]

对于混合配置 \(01\) 或 \(10\)，本工具的跨块缺陷精确为

\[
\mathcal T(R_1)-\mathcal T(R_0)
=4\log(u/v)+2/v-8<0. \tag{31}
\]

严格负号只需 \(u<v\) 和 \(v>1/4\)。因此任何“每个配置的边界曲率贡献非负”的规则已经被实际 sine 模型否定；本文没有使用它。

同时直接计算真实互信息得到

\[
J_1''((1-c)/2)=-8-4\log(v/u)+2/u. \tag{32}
\]

在 \(c=.95\) 时约为 \(1.5454670142\)，而 (31) 约为 \(-5.2107391887\)。这种差异说明，带符号平均不可用逐配置正性替代。

这不是对定理 (1) 的反例；它是对一个可能误用的更强中间规则的实际模型反例。

### 9.2 可复现全枚举及微分测试

附带 `verify_qwe02.py` 与完整 `checks.json`。测试全部采用普通双精度，不是区间证书，也不是独立审查。解析证明不依赖测试输出。

程序进行了：

- 真实 sine 核在 \(a=.015,.025,.035\) 和 \(n=1,\ldots,12\) 的完整配置枚举，分别从 \(p',p''\) 和式 (15) 计算熵曲率；
- \(L=1,\ldots,6\) 的真实互信息曲率、弦及逐配置缺陷；
- \(n=3,5,8,10\) 的复 Hermitian 一致有谱隙 DPP，检验不等块的公式；
- 第 6 节一阶和二阶微分公式的有限差分检验；
- 真实 sine 核在 \(L=8,16,32,64,128\) 上，对全空、全满、交替和固定随机种子配置，以及六个跨块耦合强度的逐配置测试。

本次运行的最大归一化误差为 \(3.34\times10^{-16}\) 以下；两种熵曲率计算的最大绝对偏差为 \(5.69\times10^{-14}\) 以下；Fisher 恒等式残差为 \(8.89\times10^{-15}\) 以下。直接用四个配置原子的对数构造每一个二坐标差分，与逆矩阵表达式逐配置比较，最大残差为 \(5.69\times10^{-13}\) 以下。微分公式有限差分的最大偏差分别约 \(6.86\times10^{-9}\) 与 \(9.89\times10^{-8}\)。这些只是浮点一致性诊断。

平衡点 \(a=.025\) 的部分结果如下：

| \(L\) | \(J_L''(.025)\)，双精度 | 负缺陷配置数 / 全配置数 |
|---:|---:|---:|
| 1 | 1.5454670142 | 2 / 4 |
| 2 | 8.3328162802 | 10 / 16 |
| 3 | 13.7497674704 | 30 / 64 |
| 4 | 19.0896099580 | 108 / 256 |
| 5 | 23.1741137615 | 400 / 1024 |
| 6 | 27.0490860822 | 1504 / 4096 |

没有发现对恒等式或所构造工具的数值反例。但这些有限测试绝不用于推断所有尺度的曲率符号。所有尺度的绝对上界来自第 6–8 节的证明。

复现：

```bash
python -m pip install numpy
OPENBLAS_NUM_THREADS=1 python verify_qwe02.py --output checks.json
```

程序使用固定随机种子 `20260918`。不同 BLAS 实现会造成末尾浮点位差异。

---

## 10. 结论边界与可复用交接

**本任务已经支付的量：**

\[
|\Delta_\eta J_L(a)|=O_I(\eta^2\log(1+L)),
\qquad
\sum_{j\ge N}\frac{|\Delta_\eta J_{m2^j}(a)|}{2m2^j}
=O_I\!\left(\eta^2\frac{\log L_*}{L_*}\right).
\]

本轮的证明适用于任意一致有谱隙的有限 Hermitian DPP 的对角平移族，因此不限于半填充或 \(c=.95\)。对一般 \(c<1\)，只需紧区间 \(I\subset(0,1-c)\)，取 \(\delta\le\inf_{a\in I}\min\{a,1-a-c\}\)。

**没有证明的量：** \(J_L''\) 的非负性、有限带符号 dyadic 和的充分下界、全参数熵率凹性，以及允许谱隙 \(\delta\downarrow0\) 的一致界。本文没有在这些范围提出新结论。

按上述证明，QWE02 自身不再留下未支付的边界响应不等式；新证明仍待另行独立核查。后续最有价值的工作是独立检查 (23)–(28) 的常数和维数依赖，并压缩 \(\delta^{-12}\) 的粗损失。这是改善实用常数的任务，不是当前定理中隐含的假设。

可直接复用的数学模块为：完整曲率泛函 (12)、期望恒等式 (16)、无维数微分引理 (18)–(21)、逐配置边界缺陷界 (17)，以及实际 dyadic 尾公式 (5)。

---

## 11. 来源与新旧结论的区分

**任务与已审查输入。** Google Drive 中的 `QWE02_PACKET.md`：`CONTRACT.md`、`TARGET.md`、`TASK.md`、`sources/S42_INDEPENDENT_REVIEW.md` 与 `sources/S47_FORMULA_CORRECTION.md`。这里只使用 S42 已审查的 dyadic 恒等式作为最后的拼接输入。S47 关于 signed translation 和完整曲率项的纠正与第 4 节一致；本文重新给出了所用公式的证明。

**背景原始来源。** J. B. Hough, M. Krishnapur, Y. Peres, B. Virág, *Determinantal Processes and Independence*, Probability Surveys 3 (2006), 206–229，arXiv:math/0503110，DOI 10.1214/154957806000000078。有限 DPP 的存在及标准表示的背景来源；没有从中援引本次响应界。

**备选方向的来源范围。** M. M. Wolf, F. Verstraete, M. B. Hastings, J. I. Cirac, *Area laws in quantum systems: mutual information and correlations*, arXiv:0704.3906。量子互信息与边界的背景；本文没有把其值层面的结论当作经典曲率估计。

**本轮证明。** 第 6 节的明确无维数梯度/Hessian 估计、由此得到的逐配置跨块缺陷界，以及定理 1 和 sine 二次弦尾推论，均是本文提交的新证明内容。这里不作新颖性或优先权主张，也不把本轮复核称为独立审查。