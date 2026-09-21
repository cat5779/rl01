# 稀疏重采样的二缺陷系数、循环端点奇异性与二阶量传递

**研究包日期：2026-09-19。** 全文使用自然对数。本文中的证明为本轮作者推导，随包提供代数检查和一个纯整数区间证书；它们不是外部独立审稿。本文没有证明完整的 \(C(0,1)\)，也没有给出该猜想的反例。

## 0. 本轮结论与两个必须修正的判断

本轮不再给原来的 \(\Gamma\) 添加一个新名字，而是直接计算用户指定的重采样模型。

**第一项修正：互信息的二阶展开不能只有异点 pair。** 正确的自然分解是

\[
 I(E;Y)=\varepsilon\sum_iD(P_i^p\Vert P)
 +\varepsilon^2\left\{\sum_{i<j}\mathcal J_{ij}(p)
 -\frac12\sum_i\chi^2(P_i^p\Vert P)\right\}
 +\mathcal R_{n,3}.
 \tag{0.1}
\]

缺少的对角项在 \(n=1\) 已非零。它不是可以并入三阶 remainder 的小量。

**第二项修正：投影端点的固定体积奇异展开没有完全相同的一阶曲率相消。** 对全支撑于 \(k\)-粒子层的循环投影输入，

\[
 H_{pp}(\varepsilon,p)
 =-\varepsilon\left(\frac{n-k}{p}+\frac{k}{1-p}\right)
 +4k(n-k)\varepsilon^2\log(1/\varepsilon)
 +\varepsilon^2 B_{2,n}''(p)
 +O_{n,p}(\varepsilon^3(1+|\log\varepsilon|)).
 \tag{0.2}
\]

这不反驳 full-support 情形的一阶相消；两者的支持集假设不同。

本轮进一步证明了以下结构性结果。

* 自然异点系数的曲率 **精确等于 S52 actual-output Fisher–Bregman skew 的两倍**，不只是在形式上类似；且该曲率与 \(p\) 无关。
* 在**真实半密度 sine 的六点 Toeplitz 压缩**中，存在具有正实际概率的条件表，使该 skew 严格为正。纯有理区间证书验证此事；同一 pair 按全部实际外部权重求和后为负。这排除了“在 sine 可达表上逐表支付”的加强假设，并不排除平均支付。
* 对正则化循环投影基准律，异点曲率和有显式 \(-A_n(p_0)/\eta\) 留数，而且常对角投影满足
  \[
  A_n(p_0)\ge \frac{k(n-k)}{n p_0(1-p_0)}.
  \tag{0.3}
  \]
  因而有限循环对象的 \(n\)-一致 logarithmic 界不成立。没有据此交换极限或宣称无限 sine 的 \(\Gamma\) 猜想被证伪。
* 对半密度循环投影，真正的二阶常数项满足
  \[
  B_{2,n}''(1/2)=-\Theta(n^2\log n).
  \tag{0.4}
  \]
  证明用真实插入后验熵及显式 Vandermonde 交换能量。不能孤立地依据 (0.2) 中正的 logarithmic 项判断曲率翻号。
* 给出带完整谱隙常数的二阶量传递不等式，以及真正可证明的**对数增长窗口**结论。没有覆盖自然候选尺度 \(n\asymp1/\varepsilon\)。

详细 remainder、传递证明见 `APPENDIX_BOUNDS.md`；投影分层、留数和 (0.4) 的证明见 `APPENDIX_PROJECTION.md`。来源和本地访问边界见 `SOURCE_AUDIT.md`。

---

## 1. 模型与精确互信息分解

令 \(X\sim P\) 为 \(\{0,1\}^n\) 上的固定基准律。独立取

\[
 E_i\sim\operatorname{Bern}(\varepsilon),\qquad
 Z_i\sim\operatorname{Bern}(p),\qquad
 Y_i=(1-E_i)X_i+E_iZ_i.
\]

这里 \(E\) 是“是否重采样”的掩码，**不是是否实际翻位的掩码**。记 \(r_p(1)=p,r_p(0)=1-p\)。给定缺陷集合 \(A=\{i:E_i=1\}\)，实际输出概率为

\[
 P_A^p(y)=P(y_{A^c})\prod_{i\in A}r_p(y_i),
 \qquad
 Q_{\varepsilon,p}(y)=\sum_A
 \varepsilon^{|A|}(1-\varepsilon)^{n-|A|}P_A^p(y).
 \tag{1.1}
\]

所有边缘化均对基准真实概率进行。给定 \(A\)，被重采样坐标与保留坐标独立，因此

\[
 H(Y\mid E)=\mathbb E_EH(X_{E^c})+n\varepsilon b(p),
 \quad b(p)=-p\log p-(1-p)\log(1-p).
\]

由互信息定义，

\[
 H(Y)=\mathbb E_EH(X_{E^c})+n\varepsilon b(p)+I(E;Y),
 \qquad
 H_{pp}=-\frac{n\varepsilon}{p(1-p)}+I_{pp}.
 \tag{1.2}
\]

式 (1.2) 无需基准律 full support；但后面的 regular KL 展开需要。

### 1.1 DPP 参数匹配

若 \(P=\operatorname{DPP}(K)\)，则

\[
 Q_{\varepsilon,p}=\operatorname{DPP}((1-\varepsilon)K+\varepsilon p I).
 \tag{1.3}
\]

证明不需引用通道结论：对任意有限坐标集 \(S\)，先对独立重采样取期望，

\[
 \mathbb E\prod_{i\in S}Y_i
 =\sum_{A\subseteq S}(\varepsilon p)^{|A|}
 (1-\varepsilon)^{|S|-|A|}\det K_{S\setminus A}
 =\det((1-\varepsilon)K+\varepsilon pI)_S.
\]

所有 inclusion 概率决定二元有限律。对于用户参数，\(c=1-\varepsilon\)、\(a=\varepsilon p\)。本研究对象始终是配置熵，不是 \(\operatorname{Tr}b(K)\)。

---

## 2. Full-support 基准律：完整二缺陷系数

本节假设 \(P(y)>0\) 对所有 \(y\) 成立，\(0<p<1\)。定义

\[
 D_A=D(P_A^p\Vert P),\qquad
 h_i(y)=\frac{P_i^p(y)-P(y)}{P(y)}.
\]

### 定理 2.1：自然二阶展开

定义真正异点的系数

\[
 \boxed{
 \mathcal J_{ij}(p)=D_{\{i,j\}}-D_{\{i\}}-D_{\{j\}}
 -\sum_y\frac{(P_i^p(y)-P(y))(P_j^p(y)-P(y))}{P(y)}.
 }
 \tag{2.1}
\]

则固定 \(n\) 时 (0.1) 成立，且在任意紧 \(p\)-区间内可逐项求两次导数。一个显式、可随 \(n\) 检查的 remainder 界见第 5 节。

**证明。** 有限 KL 的精确链式恒等式为

\[
 I(E;Y)=\sum_Aw_A D(P_A^p\Vert P)-D(Q_{\varepsilon,p}\Vert P),
 \quad w_A=\varepsilon^{|A|}(1-\varepsilon)^{n-|A|}.
 \tag{2.2}
\]

第一个量的二阶系数是

\[
 \sum_{i<j}(D_{ij}-D_i-D_j).
\]

令

\[
 v=\sum_i(P_i^p-P),\qquad
 w=\sum_{i<j}(P_{ij}^p-P_i^p-P_j^p+P).
\]

因为 \(Q=P+\varepsilon v+\varepsilon^2w+O(\varepsilon^3)\) 且各非零阶系数总和为零，

\[
 D(Q\Vert P)=\frac{\varepsilon^2}{2}\sum_y\frac{v(y)^2}{P(y)}+O(\varepsilon^3).
\]

展开 \(v^2\) 的对角项和异点项，即得 (0.1)。有限全正概率允许在紧区间内使用普通 Taylor 展开。证毕。

### 2.2 为什么不能删去对角项

取 \(n=1\)、\(P=\operatorname{Bern}(q)\)。此时没有异点 pair，而

\[
 I(E;Y)=\varepsilon D(\operatorname{Bern}(p)\Vert\operatorname{Bern}(q))
 -\frac{\varepsilon^2(p-q)^2}{2q(1-q)}+O(\varepsilon^3).
 \tag{2.3}
\]

这是请求中 pair-only 展开的直接反例。对 \(n\ge2\)，当然可以人为定义

\[
 \widetilde{\mathcal J}_{ij}
 =\mathcal J_{ij}-\frac{\chi_i^2+\chi_j^2}{2(n-1)}
\]

以恢复纯 pair 写法；但它把同点预算按 \(n\) 分摊到所有距离，破坏局部/距离分析。本文保留自然的 \(\mathcal J_{ij}\) 和独立的对角项。

---

## 3. Actual-output 公式、二次性与 S52 的精确关系

固定 \(i<j\) 和其余坐标的真实输出 \(z\)。以下四个数是**全局概率质量**：

\[
 t_{ab}=P(X_i=a,X_j=b,X_{-ij}=z),\quad
 m_z=\sum_{a,b}t_{ab},\quad q_{ab}=t_{ab}/m_z.
\]

它们不是任意指定的四元组。记 \(t_{\cdot b}=t_{0b}+t_{1b}\)、\(t_{a\cdot}=t_{a0}+t_{a1}\)。在该输出方块上，

\[
 u^{ij}_{ab}=m_zr_p(a)r_p(b),\quad
 u^i_{ab}=r_p(a)t_{\cdot b},\quad
 u^j_{ab}=r_p(b)t_{a\cdot}.
 \tag{3.1}
\]

因此 (2.1) 完全展开为

\[
 \boxed{
 \begin{aligned}
 \mathcal J_{ij}(p)=\sum_{z,a,b}\bigg[
 &u^{ij}_{ab}\log\frac{u^{ij}_{ab}}{t_{ab}}
 -u^i_{ab}\log\frac{u^i_{ab}}{t_{ab}}
 -u^j_{ab}\log\frac{u^j_{ab}}{t_{ab}}\\
 &-\frac{(u^i_{ab}-t_{ab})(u^j_{ab}-t_{ab})}{t_{ab}}
 \bigg].
 \end{aligned}}
 \tag{3.2}
\]

所有分母严格正；外部权重 \(m_z\) 没有被置为均匀权重。支持奇异时不得把 (3.2) 的无穷项相减当作定义。

### 定理 3.1：二次性与曲率

令

\[
 \delta_z=q_{10}q_{01}-q_{00}q_{11},\quad
 \ell_z=\log\frac{q_{10}q_{01}}{q_{00}q_{11}},\quad
 e_z=\delta_z\sum_{a,b}\frac1{q_{ab}}.
\]

则

\[
 \boxed{\mathcal J_{ij}''(p)=2\sum_zm_z(\ell_z-e_z).}
 \tag{3.3}
\]

特别地，\(\mathcal J_{ij}\) 在整个 \((0,1)\) 上是一个二次多项式；右边完全不依赖 \(p\)。

**证明。** 对单点，令 \(\pi_i(z)=P(X_i=1\mid X_{-i}=z)\)，则

\[
 D_i=\mathbb E_{X_{-i}}
 \left[p\log\frac p{\pi_i}+(1-p)\log\frac{1-p}{1-\pi_i}\right],
 \quad D_i''=\frac1{p(1-p)}.
 \tag{3.4}
\]

双重重采样中，两个 Bernoulli 熵项给出 \(2/[p(1-p)]\)，恰好与 \(D_i''+D_j''\) 相消；剩下的二阶差分为

\[
 (D_{ij}-D_i-D_j)''=2\sum_zm_z\ell_z.
 \tag{3.5}
\]

再计算交叉项。写 \(s_0=-1,s_1=1\)。由 (3.1)，

\[
 \partial_pu^i_{ab}=m_zs_aq_{\cdot b},\qquad
 \partial_pu^j_{ab}=m_zs_bq_{a\cdot}.
\]

二元表恒等式

\[
 q_{a\cdot}q_{\cdot b}=q_{ab}+s_as_b\delta_z
\]

说明

\[
 \sum_{a,b}\frac{(\partial_pu^i_{ab})(\partial_pu^j_{ab})}{t_{ab}}
 =m_z\delta_z\sum_{a,b}\frac1{q_{ab}}=m_ze_z.
\]

交叉项二阶导数再乘 2，即得 (3.3)。证毕。

### 3.2 与 S52 compensator 的直接代数识别

对 DPP，条件二元表仍满足 \(\delta_z\ge0\)。可直接从条件核的二点行列式证明。定义

\[
 \Phi(u)=-\log(1-u)-u,\qquad
 \Psi(v)=v-\log(1+v).
\]

因为同边缘独立表为

\[
 (q_{11}+\delta,q_{10}-\delta,q_{01}-\delta,q_{00}+\delta),
\]

其 odds ratio 等于 1，所以

\[
 \boxed{
 \ell-e=
 \Phi(\delta/q_{10})+\Phi(\delta/q_{01})
 -\Psi(\delta/q_{11})-\Psi(\delta/q_{00}).
 }
 \tag{3.6}
\]

这是随包 `sources/S52_CYCLE06_RESULT.md` 第 3 节式 (21) 的同一个实际输出对象；式 (3.3) 正好是它乘 \(2m_z\) 后对真实外部输出求和。本文已独立重算 (3.3)–(3.6)，没有把 S52 的作者状态当成新的符号定理。

因此，稀疏缺陷表述确实产生了一个有意义的展开，但**二阶项本身并未绕开 S52 的 signed-average 难点**。真正的新控制必须来自真实条件表随尺度的分布或跨阶补偿。

### 3.3 不可少的对角预算

单点 \(\chi^2\) 满足

\[
 \chi^2(P_i^p\Vert P)
 =\mathbb E\frac{(p-\pi_i)^2}{\pi_i(1-\pi_i)},\qquad
 \frac{d^2}{dp^2}\chi^2(P_i^p\Vert P)
 =2\mathbb E\frac1{\pi_i(1-\pi_i)}.
\]

记

\[
 \mathcal D_n(P)=\sum_i\mathbb E\frac1{\pi_i(1-\pi_i)},\quad
 S_n(P)=\sum_{i<j}\mathcal J_{ij}'',\quad
 \mathcal L_n(P)=S_n(P)-\mathcal D_n(P).
 \tag{3.7}
\]

结合 (1.2)、(3.4)，

\[
 \boxed{H_{pp}(\varepsilon,p)=\varepsilon^2\mathcal L_n(P)
 +\partial_p^2\mathcal R_{n,3}.}
 \tag{3.8}
\]

一阶曲率相消成立，但“因此只需研究异点 pair”不成立。同点 inverse moment 以准确负号出现在真实二阶预算中；不能单独上界后丢弃相应补偿。

本文 \(S_n\) 使用无序 pair。若采用有序求和，则 \(n^{-1}\sum_{i\ne j}\mathcal J_{ij}''=2S_n/n\)。所有数表报告的是 \(S_n/n\)。

### 3.4 与共同对角熵 Hessian 的识别

设 \(P=\operatorname{DPP}(K)\)、\(0<K<I\)。沿 \(K+tI\) 的完整实际律记为 \(P_t\)。精确原子式

\[
 P_t(y)=(-1)^{n-|y|}\det(K+tI-\operatorname{diag}(1-y))
\]

给出

\[
 \left.\frac{d^2}{dt^2}H(P_t)\right|_{t=0}=\mathcal L_n(P).
 \tag{3.9}
\]

也可从二元表直接证明：共同对角导数是各坐标的 \((-m,m)\) 之和；二阶混合导数是每个条件方块的 \(2m(1,-1,-1,1)\)。完整 Hessian

\[
 -\sum_yP_t''(y)\log P_t(y)-\sum_y\frac{P_t'(y)^2}{P_t(y)}
\]

分别产生 directed log-odds 和 \(\mathcal D_n+2\sum_{i<j}\mathbb E e_{ij}\)。这正是 (3.7)。没有冻结实际概率。

---

## 4. 真正的 sine 可达局部反例；平均符号未被替代

取真正的六点 Toeplitz 核

\[
 K_{rs}=\begin{cases}
 1/2,&r=s,\\
 \sin(\pi(r-s)/2)/(\pi(r-s)),&r\ne s,
 \end{cases}\qquad 0\le r,s\le5.
\]

选 pair \((i,j)=(1,4)\)，给定外部坐标 \((0,2,3,5)=(1,1,0,0)\)。实际归一化条件表按 \((00,10,01,11)\) 排列约为

\[
 (0.08096954,\ 0.03918587,\ 0.79887505,\ 0.08096954).
\]

纯整数/有理区间计算证明

\[
 0.09455357<m_z<0.09455358,
 \qquad
 \boxed{0.28952216<\ell_z-e_z<0.28952217.}
 \tag{4.1}
\]

这里没有使用浮点符号判断。`src/interval_certificate.py` 用 Machin 恒等式界定 \(\pi\)，用带显式尾界的 atanh 级数界定对数，以 256 位 dyadic 区间向外舍入所有算术。完整 determinant 计算严格认证各原子为正。

同一脚本还严格认证：该 pair 对所有真实外部输出求和后 \(\mathcal J_{14}''<0\)，而且该 **n=6 模型的全部十五个实际平均 pair** 都小于零；

\[
 -26.511794<\mathcal L_6/6<-26.511793.
\]

同一纯整数证书还验证了噪声内点 \(c=19/20\) 的两个真实可达反例：

* 对上述六点 true Toeplitz 核施加中点噪声后，同一方块有 \(0.12980507<\ell-e<0.12980508\)。
* 对 **n=8、rank=4 的循环投影中点噪声律**，取 pair \((1,6)\)，外部坐标 \((0,2,3,4,5,7)=(1,1,1,0,0,0)\)，有
  \[
  \boxed{0.56496630<\ell-e<0.56496632.}
  \]
  该循环核只需平方根 \(\sqrt2,\sqrt{2\pm\sqrt2}\)，脚本用整数平方根向外包围计算；没有浮点三角函数。该 pair 按全部真实外部输出求和后仍严格为负。

这只证明上述有限模型的符号，不证明更大体积或无限体积的符号。它也说明必须区分“某个 actual conditional cell 的正 skew”和“该 pair 的 actual weighted average”。本轮不建立逐表非正的新充分条件。

---

## 5. 三阶结构与可检查的 regular-expansion 范围

令 \(T_i^p\) 为坐标重采样算子，\(M_i=T_i^p-I\)，并定义

\[
 v=\sum_iM_iP,\quad
 w=\sum_{i<j}M_iM_jP,\quad
 t=\sum_{i<j<k}M_iM_jM_kP,\quad V=v/P,\ W=w/P.
\]

互信息的三阶系数为

\[
 \boxed{
 [\varepsilon^3]I=
 \sum_{i<j<k}(D_{ijk}-D_{ij}-D_{ik}-D_{jk}+D_i+D_j+D_k)
 -\mathbb E_P[VW]+\frac16\mathbb E_P[V^3].
 }
 \tag{5.1}
\]

熵的三阶系数之 \(p\)-曲率为

\[
 \boxed{
 [\varepsilon^3]H_{pp}
 =-\sum_y t_{pp}\log P
 -\sum_y\frac{v w_{pp}+2v_pw_p}{P}
 +\sum_y\frac{v(v_p)^2}{P^2}.
 }
 \tag{5.2}
\]

“余项从三阶开始”不等于“只来自三个不同坐标的缺陷事件”。后验归一化的 \(VW,V^3\) 也包括重复坐标贡献；\(n=1\) 也有三阶项。

### 定理 5.1：显式 full-support 余项界

设

\[
 \beta=\min_{i,z}\min(\pi_i(z),1-\pi_i(z))>0,\quad
 B=1+\beta^{-1},\quad T=n\varepsilon B\le1/4.
\]

则 (0.1) 的 remainder 满足

\[
 |\mathcal R_{n,3}|\le(4\log(1/\beta)+4)T^3,
 \tag{5.3}
\]

\[
 \boxed{|\partial_p^2\mathcal R_{n,3}|\le(2H(P)+10)T^3
 \le(2n\log2+10)T^3.}
 \tag{5.4}
\]

(5.4) 等价于 (3.8) 的完整熵曲率 remainder 界，并可连续延伸到 \(p=0,1\)。互信息的单独导数在边界仍需按 (1.2) 处理熵奇异项。

证明在 `APPENDIX_BOUNDS.md` §1，明确给出所有导数的 majorant，未假设 \(n\)-一致性。这些常数很粗；当 \(\beta_n\) 变小时，它们只提供一个充分展开区间，不把该界恶化当成实际发散的证明。

---

## 6. 循环 projection：正确的支持奇异展开和留数

取秩 \(k\) 的连续 Fourier 模式循环投影 \(P_N\)，此处体积 \(N=n\)。它的输入律记作 \(\mu\)，避免与投影矩阵混淆。其概率是

\[
 \mu(S)=n^{-k}\prod_{i<j\in S}\left(2\sin\frac{\pi(j-i)}n\right)^2,
 \qquad |S|=k,
 \tag{6.1}
\]

在全部其他粒子层上为零。所有 \(k\)-子集概率严格正。因此 \(D(P_i^p\Vert\mu)=\infty\)，不能将第 2 节的有限 KL 公式用于 \(\eta=0\)。

### 6.1 分层展开

把输出按 \(d=||y|-k|\) 分层。零层的起始阶为 1，一层为 \(\varepsilon\)，二层为 \(\varepsilon^2\)。逐层展开 \(-q\log q\) 得到 (0.2)；实际权重表达式、全部 \(B_2''\) 分量以及显式奇异 remainder 常数均在 `APPENDIX_PROJECTION.md` §1–§4。

其中 \(\varepsilon^2\log\varepsilon\) 的系数只由粒子数变化决定：若 \(G\sim\operatorname{Bin}(n-k,\varepsilon p)\)、\(L\sim\operatorname{Bin}(k,\varepsilon(1-p))\)，则

\[
 \mathbb E|G-L|=\varepsilon[k(1-p)+(n-k)p]
 -2k(n-k)\varepsilon^2p(1-p)+O_n(\varepsilon^3).
\]

这不是交换体积极限的论证。

### 6.2 正则化基准律中的实际 pair 留数

固定另一参数 \(p_0\in(0,1)\)，先令

\[
 \mu_\eta=\operatorname{DPP}((1-\eta)P_N+\eta p_0I),\qquad \eta>0.
\]

现在以 \(\mu_\eta\) 为 full-support 基准，应用第 2 节的自然 \(\mathcal J_{ij}\)。新缺陷的参数 \(p\) 与正则化参数 \(p_0\) 不应混淆；\(\mathcal J_{ij}''\) 与前者无关。

记 \(g=n-k\)，并定义真实一错误输出质量

\[
 A_S=\sum_{i\in S}\mu(S\setminus\{i\}),\quad |S|=k+1;
 \qquad
 B_T=\sum_{j\notin T}\mu(T\cup\{j\}),\quad |T|=k-1.
\]

它们满足 \(\sum A_S=g\)、\(\sum B_T=k\)。定义

\[
 \alpha_+=\sum_{|S|=k+1}\frac{\sum_{i\in S}\mu(S\setminus i)^2}{A_S},
 \quad
 \alpha_-=\sum_{|T|=k-1}\frac{\sum_{j\notin T}\mu(T\cup j)^2}{B_T},
\]

\[
 D_{\rm res}=\frac{\alpha_+}{p_0}+\frac{\alpha_-}{1-p_0},\qquad
 A_n(p_0)=\frac{g-\alpha_+}{p_0}+\frac{k-\alpha_-}{1-p_0}.
 \tag{6.2}
\]

### 定理 6.1：极点及 logarithmic 项

固定 \(n,k,p_0\)，当 \(\eta\downarrow0\)，

\[
 \mathcal D_n(\mu_\eta)=\frac{D_{\rm res}}\eta+O_{n,p_0}(1),
\]

\[
 \boxed{S_n(\mu_\eta)=-\frac{A_n(p_0)}\eta
 +4k(n-k)\log(1/\eta)+O_{n,p_0}(1).}
 \tag{6.3}
\]

若投影矩阵的对角恒等于 \(\rho=k/n\)，则

\[
 \alpha_+\le\frac{g^2}{n},\qquad \alpha_-\le\frac{k^2}{n},
 \qquad A_n(p_0)\ge\frac{kg}{n p_0(1-p_0)}.
 \tag{6.4}
\]

**留数下界的关键证明。** 对 \(|S|=k+1\)，\((P_N)_S\) 的单位零向量 \(v\) 满足

\[
 \frac{\mu(S\setminus i)}{A_S}=|v_i|^2.
\]

这是 rank-\(k\) Gram 矩阵伴随矩阵的对角 cofactor 公式。把 \(v\) 延拓为全空间向量，它属于 \(\ker P_N\)，故

\[
 |v_i|^2\le (I-P_N)_{ii}=1-\rho.
\]

于是后验碰撞概率 \(\sum_i|v_i|^4\le1-\rho\)，按真实输出质量 \(A_S\) 求和得到第一项；补投影给出第二项。代入 (6.2) 即得 (6.4)。完整留数展开见附录。

在半密度、中点，

\[
 \boxed{\lim_{\eta\downarrow0}-\eta\,S_n(\mu_\eta)/n=A_n(1/2)/n\ge1.}
 \tag{6.5}
\]

所以“这些有限循环 pair 和除以 \(n\) 具有统一 \(O(\log(1/\eta))\) 界”是**错误命题**。这是真正的支持奇异性，不是浮点 inverse-moment 失控。

但 (6.5) 中先固定 \(n\)，而目标 \(\Gamma_c\) 先取无限真实 sine 体积。因此，(6.5) **没有证伪** 无限体积 \(\Gamma_c=O(\log(1/(1-c)))\) 的猜想。将两者直接混为一谈，恰好会违反用户要求的不可默认交换极限原则。

---

## 7. 二阶常数项的可证明增长：\(-\Theta(n^2\log n)\)

这是对 (0.2) 中容易被忽略的 \(B_{2,n}''\) 的进一步定量分析。

对任意全支撑 \(k\)-层律 \(\mu\)，定义真实的“均匀选择空位后插入一粒子/两粒子”通道，并令

\[
 h_+=H(X\mid X\cup\{\text{一个均匀空位}\}),\quad
 h_{++}=H(X\mid X\cup\{\text{两个均匀空位}\}),
\]

同样定义删一粒子、删两粒子的反向条件熵 \(h_-,h_{--}\)。这是对真实输入和真实输出的熵，不是对所有输出集合等权求和。

另定义未归一化的完整交换能量

\[
 \mathscr D_\mu=\sum_{|x|=k}\mu(x)
 \sum_{i\in x,j\notin x}\log\frac{\mu(x)}{\mu(x-i+j)}\ge0.
 \tag{7.1}
\]

这只是本节 \(k\)-层原始投影输入的有限代数对象，不是仓库 corrected law 的时钟或 KL 修正。

令 \(d=n-2k\)。实际分层计算给出

\[
 \begin{aligned}
 B_{2,n}''(p)={}&\frac{k(n-k)}{p(1-p)}
 -2k(n-k)\log[p(1-p)]-4k(n-k)-n+\mathcal C_\mu,\\
 \mathcal C_\mu={}&-2\mathscr D_\mu
 +2(n-k)(d-1)h_+-2k(d+1)h_-\\
 &-(n-k)(n-k-1)h_{++}-k(k-1)h_{--}.
 \end{aligned}
 \tag{7.2}
\]

在半密度循环投影中，补集对称给出 \(h_+=h_-=h_1\)、\(h_{++}=h_{--}=h_2\)，故

\[
 \boxed{B_{2,n}''(1/2)=n^2\log2-n-2\mathscr D_\mu
 -2n h_1-(n^2/2-n)h_2.}
 \tag{7.3}
\]

投影几何还能把符号说得更强：插入 r 个粒子后，给定输出的真实父配置后验是一个 r 阶零空间 minor，概率不超过 \((1-\rho)^r\)；删除的对应上界是 \(\rho^r\)。因此半密度下 \(h_1\ge\log2\)、\(h_2\ge2\log2\)，从 (7.3) 得到

\[
 \boxed{B_{2,n}''(1/2)\le-n-2\mathscr D_\mu\le-n<0.}
 \tag{7.3a}
\]

该结论实际对任何满 k-层支撑、常对角 1/2 的秩 n/2 投影成立，不需要其为循环投影。证明见附录 P5.3。它只判断二阶常数项，不能忽略同阶的正 logarithmic 项或 remainder。

Vandermonde 概率又给出一个精确公式

\[
 \boxed{\mathscr D_\mu=2k(n-k)\log n-2(n-1)H(\mu).}
 \tag{7.4}
\]

证明仅使用交换算子在 \(X_iX_j\) 上的显式作用与
\(\prod_{d=1}^{n-1}2\sin(\pi d/n)=n\)，见附录 §6；没有输入未经证明的 sine 刚性速率。

由

\[
 0\le H(\mu)\le\log\binom n{n/2},\quad
 0\le h_1\le\log(n/2+1),\quad
 0\le h_2\le\log\binom{n/2+2}{2},
\]

得到对偶数 \(n\ge4\) 的显式上下界

\[
 \begin{aligned}
 B_{2,n}''(1/2)\ge{}&-n^2\log n+n^2\log2-n
 -2n\log(n/2+1)\\
 &-(n^2/2-n)\log\binom{n/2+2}{2},
 \end{aligned}
 \tag{7.5}
\]

\[
 B_{2,n}''(1/2)\le
 -n^2\log n+n^2\log2-n+4(n-1)\log\binom n{n/2}.
 \tag{7.6}
\]

因此

\[
 \boxed{-2+o(1)\le
 \frac{B_{2,n}''(1/2)}{n^2\log n}
 \le-1+o(1).}
 \tag{7.7}
\]

这是阶的结论，不断言该比值有极限。附录 P4 还给出对角极点之后的显式常数 \(d_0\)，以及真正的补偿后 pair 有限部分

\[
 F_n=\lim_{\eta\downarrow0}[S_n+A_n/\eta-n^2\log(1/\eta)]
 =B_{2,n}''(1/2)+d_0.
\]

其中 \(d_0=O(n^2)\) 有实际错误输出质量的公式和不依赖最小原子的界，故 \(F_n=-\Theta(n^2\log n)\) 也成立。特别地，\(\varepsilon^2\log(1/\varepsilon)\) 的正系数并不是完整二阶效应；同一阶的常数项本身已有负的 \(n^2\log n\) 非一致性。匹配尺度必须同时追踪两者及第三阶 remainder。

---

## 8. 二阶量传递与可证明的增长窗口

### 定理 8.1：共同谱隙下的实际律传递

对同阶 Hermitian 核 \(K,L\)，若

\[
 \delta I\le K,L\le(1-\delta)I,\qquad0<\delta\le1/2,
\]

则

\[
 \boxed{
 \left|\frac{\mathcal L_n(K)-\mathcal L_n(L)}n\right|
 \le2n\delta^{-5}\|K-L\|_F.
 }
 \tag{8.1}
\]

它控制的是完整二阶 entropy/interaction quantity，而非熵值。证明分两步：通过实际原子的 score 控制 \(\|P_K-P_L\|_1\)，再对带全局质量的四元表函数作梯度估计。概率权重的变化与条件表的变化都被支付。完整常数版和证明见 `APPENDIX_BOUNDS.md` §2。

### 8.2 不借用零谱隙极限的显式 sine 剖面

设 \(\tau=\min(\rho,1-\rho)\)、\(a_\rho=\log(2e/\tau)\)。对于真实 \(m\)-点 sine 压缩，定义

\[
 d_m=\frac{(\tau/(2e))^{3(m-1)}}{8\pi m^{3/2}},\qquad m\ge2.
\]

一个有限三角多项式插值论证给出

\[
 d_m I\le Q_{\rho,m}\le(1-d_m)I.
 \tag{8.2}
\]

令 \(P_{N,k}|_{[m]}\) 为循环投影的 **m 点边缘核**，\(m\le N/2\)，则选取合法对角 gauge 后

\[
 e_{m,N}:=\|P_{N,k}|_{[m]}-Q_{\rho,m}\|_F
 \le m|\rho-k/N|+\frac{\pi^2m^2}{12N^2}.
 \tag{8.3}
\]

当右侧不超过 \(d_m/2\) 时，

\[
 \boxed{
 \left|\frac{\mathcal L_m(P_{N,k}|_{[m]})-
 \mathcal L_m(Q_{\rho,m})}{m}\right|
 \le64m d_m^{-5} e_{m,N}.
 }
 \tag{8.4}
\]

若密度精确匹配、\(m\le\kappa\log N\)、\(\kappa<2/(15a_\rho)\)，则右边为

\[
 O_{\rho,\kappa}((1+\log N)^{21/2}N^{-2+15a_\rho\kappa})\longrightarrow0.
 \tag{8.5}
\]

密度只作最近整数匹配时，取 \(\kappa<1/(15a_\rho)\)，对应主幂次为 \(N^{-1+15a_\rho\kappa}\)。

**作用域不能扩大：**这里先取 m 点边缘律，再在这 m 点内部构造条件表。它不是“给定整个 N 点循环外部输出”的条件表；也没有把有限循环投影的 (6.3) 传到 all-exterior sine 条件律。

### 8.3 稀疏展开的一条真实增长窗口结论

将 (8.2) 代入 (5.4)。若 \(n\le\kappa\log(1/\varepsilon)\)、\(\kappa<1/(9a_\rho)\)，则

\[
 \boxed{
 \sup_{p\in[0,1]}
 \left|\frac{H_{pp}(\varepsilon,p)}{n\varepsilon^2}
 -\frac{\mathcal L_n(Q_{\rho,n})}{n}\right|
 \le C_{\rho,\kappa}\varepsilon^{1-9a_\rho\kappa}
 (1+\log(1/\varepsilon))^{15/2}\longrightarrow0.
 }
 \tag{8.6}
\]

这是有限 volume 随噪声增长时的真正曲率 remainder 结论。它不证明 \(\mathcal L_n/n\) 有界或有极限。常数非常保守，所允许的窗口增长很慢；这不是 \(n\asymp1/\varepsilon\) 的 endpoint matching 定理。

### 8.4 有噪声时还能得到多项式窗口传递

两个 m 点边缘核施加相同噪声后，共同谱隙至少为 \(\varepsilon u\)，其中 \(p\in[u,1-u]\)。因此

\[
 \frac{|\mathcal L_m(K_{\varepsilon,p})-\mathcal L_m(L_{\varepsilon,p})|}{m}
 \le2m(\varepsilon u)^{-5}e_{m,N}.
 \tag{8.7}
\]

密度精确匹配且 \(m=O(1/\varepsilon)\) 时，右边为 \(O_u(\varepsilon^{-8}N^{-2})\)。选择 \(N\varepsilon^4\to\infty\) 可在这个 m 窗口尺度上使二阶量的周期化误差趋零。它仍然只是**边缘窗口对边缘窗口**的比较；缺失的全外部条件信息没有被自动支付。证明在附录 B4.3。

---

## 9. 数值诊断、可复核性与剩余义务

真实 Toeplitz 概率以 70 位精度条件递归生成，\(n=18\) 使用 80 位，然后用 float64 做实际加权求和。下表是浮点诊断；其中 n=6 的总曲率另有第 4 节的区间认证。该节还单独认证了 c=19/20 的 true Toeplitz 与循环模型局部反例。

| n，rho=1/2 | \(\mathcal D_n/n\) | \(S_n/n\) | \(\mathcal L_n/n\) |
|---:|---:|---:|---:|
| 4 | 8.107753 | -3.974058 | -12.081811 |
| 6 | 13.414272 | -13.097521 | -26.511793 |
| 8 | 20.454647 | -27.281321 | -47.735967 |
| 10 | 29.196452 | -46.501911 | -75.698363 |
| 12 | 39.641705 | -70.786135 | -110.427841 |
| 14 | 51.798352 | -100.167610 | -151.965962 |
| 16 | 65.674256 | -134.676302 | -200.350558 |
| 18 | 81.275998 | -174.336729 | -255.612727 |

这些数据不支持直接把有限零噪声系数视作 \(n\)-一致 bounded/logarithmic 对象，但也不能据此证明任何幂律。正的局部 skew 已出现，而上述有限样本中每个 pair 的实际平均仍为负。距离分解见 `results/toeplitz_precision_profile.json`，不能据局部样本宣布存在统一可求和 envelope。

本轮真正留下的核心义务是：

1. 对**随噪声正则化的真实 sine 输出**，控制实际权重下的 signed pair 总和与对角预算的联合量；n=6 的可达局部反例已经排除了逐表符号闭合。
2. 在足以匹配刚性尺度的体积范围内，控制完整第三阶及更高阶分组；固定 n 的 projection 极点和固定窗口的 regular 展开不能相互代替。
3. 将 growing marginal-window 的 (8.4) 提升到 all-exterior/entropy-rate 的二阶 quantity，并明确包含外部条件信息的损失；仅有 kernel convergence、熵 \(o(n)\)、有限 n 负号仍不够。

此前 S51 已给出 \(O(\log(1/(1-c))/(1-c))\) 端点包络，本轮没有将其改进为纯 logarithmic 界。相反，本文准确识别了：该改进若成立，必须发生在哪些先取体积极限、保留真实补偿的对象上，不能从错误的 pair-only 展开或未正则化 projection KL 推出。

**最终状态：完整 \(C(0,1)\) 未证明；显式二缺陷系数、支持奇异展开、循环留数下界、循环二阶常数项增长与定量有限窗口传递均给出自包含证明。**
