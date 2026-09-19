# S68 Cycle15 独立数学审查

审查日期：2026-09-19（Asia/Singapore）

## 结论先行

**总状态：VERIFIED_SCOPED / INCOMPLETE_MAIN_TARGET。**

完整 44 文件检查点已经补收并逐行审查。S68 的有限维工具链在其明示量词内通过：

- full-support 稀疏重采样的二、三阶展开及显式余项；
- 自然异点系数 \(\mathcal J_{ij}\) 与 S52 actual-output Fisher–Bregman skew 的精确两倍关系；
- projection 正则化的一阶奇异项、pair 极点、有限部和真实插入/删除后验熵公式；
- 常对角投影的严格有限维符号及循环 Vandermonde 的 \(-\Theta(n^2\log n)\) 二阶常数项；
- 共同谱隙下的有限边缘核传递、sine 压缩谱隙下界及作者声称的边缘窗口；
- 六点 true-sine 与八点循环模型的 256 位纯整数/有理区间证书。

我在隔离副本中运行完整入口，得到 124 项主代数检查、90 项极点/留数检查、94 项真实插入熵与增长检查、54 项有限部检查，共 362 项通过；三个指定有限模型的严格区间判号也通过。此前的 **PENDING_SOURCE** 是缺件状态，不是数学否决，现已解除。

这个通过有严格边界。它仍然没有证明：

1. 无限 true-sine 的 signed average 符号；
2. 固定 \(n\) 的 projection 零噪声极点与 \(n\to\infty\)、\(\eta\downarrow0\) 的联合一致控制；
3. 从相同有限边缘窗口传到“观察全部外部输出”后的真熵率 Hessian；
4. 纯 logarithmic 端点包络或完整 \(C(0,1)\)。

因此结论是“有限维、固定量词工具通过，主目标仍未完成”，而不是“主猜想已证”。本审查也不认证外部新颖性。

## 1. 审查材料与边界

已收到并完整读取：

- 作者主正文：harvest/CYCLE15/S68/RESULT.md，815 行；
- 作者可见总结：harvest/CYCLE13/S68/S68_LATEST_VISIBLE_REPLY.md，281 行；
- APPENDIX_BOUNDS.md，502 行；
- APPENDIX_PROJECTION.md，668 行；
- SOURCE_AUDIT.md、README.md、STATUS.json 与 MANIFEST.json；
- src/ 下 9 个程序及 results/ 下的作者留存输出；
- 已审 S52 原稿与独立审查；
- 已审 S51 Cycle06 端点/真熵率接口原稿与独立审查。

RESULT.md 与先前收到的正文逐字节一致。MANIFEST.json 仅作来源账，不被当作正确性门槛。所有会写 results/ 的程序均在隔离副本中运行，未修改作者检查点。SOURCE_AUDIT.md 只说明来源边界，不能代替外部新颖性检索。

### 固定的量词区分

本审查始终区分以下四种对象：

1. 固定 \(n\)、full-support 的基准律 \(P\)；
2. 固定 \(n\) 的粒子数 projection 律及 \(\varepsilon\downarrow0\)；
3. \(m\) 点边缘核与另一个 \(m\) 点边缘核；
4. true-sine 无限体积中，观察全部外部输出后的条件量。

从 2 或 3 不能直接推出 4。有限循环极点不能单独证伪无限 true-sine 的 \(\Gamma\) 端点猜想。

## 2. 逐结论裁决表

| 原稿位置 | 结论 | 裁决 | 独立证据 / 缺口 |
|---|---|---|---|
| 58–112 | 重采样输出律 (1.1)、熵分解 (1.2)、DPP 核匹配 (1.3) | **VERIFIED_SCOPED** | inclusion minors 的多线性展开直接给出 \((1-\varepsilon)K+\varepsilon pI\) |
| 118–185 | full-support 二缺陷展开 (0.1)/(2.1)，同点 \(\chi^2\) 项不可删除 | **VERIFIED_SCOPED** | 独立展开权重与 \(D(Q\Vert P)\)；\(n=1\) 反例正确 |
| 189–279 | actual-output 四格公式、\(\mathcal J_{ij}''=2\sum m_z(\ell_z-e_z)\)、二次性 | **VERIFIED_SCOPED** | 独立逐格求导，真实 \(m_z\) 未丢；两倍系数正确 |
| 281–309 | 与 S52 skew 的精确识别 | **VERIFIED_SCOPED** | 与已审 S52 式 (21) 完全同一对象；这是识别回旧瓶颈，不是新符号定理 |
| 311–364 | 同点 inverse-moment 预算、\(\mathcal L_n\)、共同对角 Hessian | **VERIFIED_SCOPED** | 从单点 KL 二阶导与完整 moving-law Hessian 独立重建 |
| 368–411 | 六点 true-sine 与八点循环的真实可达局部正 skew | **VERIFIED_SCOPED** | 独立高精度重算与 256 位纯整数/有理区间程序一致；同一 pair 的实际加权平均仍为负 |
| 415–448 | 三阶系数 (5.1)/(5.2) | **VERIFIED_SCOPED** | 直接展开 KL 与熵到三阶，系数和符号正确 |
| 450–474 | remainder 界 (5.3)/(5.4) | **VERIFIED_SCOPED** | Appendix Bounds B1 的 ratio 导数、熵尾和与 \(T=n\varepsilon(1+\beta^{-1})\) 常数逐项通过 |
| 478–501 | projection 端点的一阶非零曲率与 \(4k(n-k)\varepsilon^2\log(1/\varepsilon)\) 系数 | **VERIFIED_SCOPED** | 由增删粒子数 \(|G-L|\) 的二阶展开独立得到；完整 \(B_{2,n}''\) 见后续 P5 裁决 |
| 503–580 | 正则化 pair 和的 \(-A_n/\eta\) 极点及 (6.3) | **VERIFIED_SCOPED** | Appendix Projection P4 给出逐层留数和对角有限部；隔离重放 90 项 residue/asymptotic 检查通过 |
| 549–575 | 常对角投影的 \(A_n\ge kg/[np_0(1-p_0)]\) | **VERIFIED_SCOPED** | 零空间 minor 后验与 Hadamard/对角界推出 \(\alpha_+\le g^2/n,\alpha_-\le k^2/n\) |
| 584–635 | \(B_{2,n}''\) 的真实插入/删除后验熵公式和严格负号 | **VERIFIED_SCOPED** | P5 的层质量收集、链式熵恒等式与投影 minor 后验上界逐项通过；94 项形状/增长检查通过 |
| 637–680 | Vandermonde 交换能量 (7.4) 与 \(-\Theta(n^2\log n)\) | **VERIFIED_SCOPED** | 交换算子恒等式、单位根乘积、显式上下界与有限枚举一致 |
| 681–688 | 补偿后有限部分 \(F_n\) 及 \(d_0=O(n^2)\) | **VERIFIED_SCOPED** | P4 的 \(\gamma_{++},\gamma_{--}\) 界与 P7.1 量级推论通过；54 项有限部检查通过 |
| 694–712 | 共同谱隙传递界 (8.1) | **VERIFIED_SCOPED（有限边缘）** | B2 的原子梯度、kernel-to-law Fisher 路径和 \(4R\delta^{-5}\) 常数通过 |
| 714–757 | sine 压缩谱隙 \(d_m\)、循环边缘传递 (8.2)–(8.5) | **VERIFIED_SCOPED（有限边缘）** | B3 插值下界与 B4 周期核误差/窗口指数通过 |
| 759–786 | 对数增长窗口与有噪声多项式窗口 | **VERIFIED_SCOPED（边缘窗口） / INCOMPLETE（all-exterior）** | B4–B5 的指数算术正确；没有观察全部外部坐标后的信息损失界 |
| 790–815 | 完整 \(C(0,1)\) 未证明、平均符号与高阶余项仍开 | **VERIFIED_SCOPED** | 范围声明准确；“自包含证明”只覆盖附录中列出的有限维与窗口结论，不覆盖主目标 |

## 3. full-support 二缺陷展开的独立重建

令 \(M_i=T_i^p-I\)。有限乘积通道给出

\[
Q_{\varepsilon,p}
=P+\varepsilon v+\varepsilon^2w+O(\varepsilon^3),
\qquad
v=\sum_iM_iP,\quad
w=\sum_{i<j}M_iM_jP.
\]

精确 KL 链式恒等式为

\[
I(E;Y)=\sum_Aw_A D(P_A^p\Vert P)-D(Q_{\varepsilon,p}\Vert P).
\]

第一项的二阶系数是

\[
\sum_{i<j}D_{ij}-(n-1)\sum_iD_i
=\sum_{i<j}(D_{ij}-D_i-D_j).
\]

因为 \(\sum_yv(y)=\sum_yw(y)=0\)，

\[
D(Q\Vert P)
=\frac{\varepsilon^2}{2}\sum_y\frac{v(y)^2}{P(y)}
+O(\varepsilon^3).
\]

展开 \(v^2\) 后，异点交叉项的系数恰为 1，而同点项保留系数 \(1/2\)。因此作者的 (0.1) 与 (2.1) 正确。

\(n=1\) 时没有异点 pair，但二阶项

\[
-\frac{(p-q)^2}{2q(1-q)}
\]

一般非零，故 pair-only 版本确实被最小反例否定。这个修正不是记号选择，而是完整 Hessian 账本所必需。

## 4. \(\mathcal J_{ij}\) 曲率、真实权重与 S52 的两倍系数

固定实际外部输出 \(z\)，写 \(t_{ab}=m_zq_{ab}\)。单点重采样质量 \(u^i,u^j\) 对 \(p\) 线性。KL 部分二阶导为

\[
(D_{ij}-D_i-D_j)''
=2m_z\log\frac{q_{10}q_{01}}{q_{00}q_{11}}.
\]

交叉 \(\chi^2\) 项的二阶导为

\[
2m_z\delta_z\sum_{a,b}\frac1{q_{ab}},
\qquad
\delta_z=q_{10}q_{01}-q_{00}q_{11}.
\]

所以

\[
\mathcal J_{ij}''(p)
=2\sum_zm_z
\left[
\log\frac{q_{10}q_{01}}{q_{00}q_{11}}
-\delta_z\sum_{a,b}\frac1{q_{ab}}
\right].
\]

这里：

- \(m_z\) 是实际外部输出质量，不是均匀权重；
- 因右边与 \(p\) 无关，\(\mathcal J_{ij}\) 确为二次多项式；
- 括号内正好是已审 S52 一方向 skew；
- S52 同时计数 \(i\to j\) 与 \(j\to i\)，故本式的系数 \(2m_z\) 完全正确。

因此 S68 在此处的贡献是一个干净的重采样解释和系数校准，但没有绕过 S52 的 signed-average 难题。

同点项满足

\[
\frac{d^2}{dp^2}\chi^2(P_i^p\Vert P)
=2\mathbb E\frac1{\pi_i(1-\pi_i)}.
\]

故完整二阶系数是

\[
\mathcal L_n
=\sum_{i<j}\mathcal J_{ij}''
-\sum_i\mathbb E\frac1{\pi_i(1-\pi_i)}.
\]

对 \(0<K<I\)，沿 \(K+tI\) 的实际配置律直接求 Hessian，得到同一个 \(\mathcal L_n\)。没有冻结实际权重，也没有漏掉 probability acceleration。

## 5. 局部反例的独立复算

### 5.1 六点 true-sine

按原稿 370–400 行的六点 Toeplitz 核、pair \((1,4)\) 和外部 word \((1,1,0,0)\)，独立 90 位 Decimal 行列式枚举得到

\[
m_z=0.0945535763276685359583532945794\ldots
\]

以及按 \((00,10,01,11)\) 排列的条件表

\[
(0.0809695421255\ldots,\,
0.0391858694964\ldots,\,
0.7988750462526\ldots,\,
0.0809695421255\ldots).
\]

由此

\[
\ell_z-e_z
=0.289522163649931513468379560714\ldots>0.
\]

同一 pair 的全部实际外部输出加权后

\[
\mathcal J_{14}''=-1.4635919704066288\ldots<0,
\]

且

\[
S_6/6=-13.097521130943996\ldots,\quad
\mathcal D_6/6=13.414272186880060\ldots,
\]

\[
\mathcal L_6/6=-26.511793317824057\ldots.
\]

十五个 pair 的实际平均在 \(c=1\) 下均为负；最靠近零的是 \((0,5)\)，约为 \(-0.04691473466\)。

在 \(c=19/20\) 的同一 true-sine 六点模型中，局部值独立复算为

\[
\ell_z-e_z=0.12980507246666996\ldots>0.
\]

### 5.2 八点循环 projection 加噪

用 rank 4 的八点连续 Fourier 模式投影、\(c=19/20\)、pair \((1,6)\) 与原稿指定外部 word，独立枚举得到

\[
\ell_z-e_z=0.5649663065659791\ldots>0,
\]

而同一 pair 的实际加权曲率为

\[
\mathcal J_{1,6}''=-1.5332360604176072\ldots<0.
\]

这些复算与补收的 256 位纯整数/有理区间证书一致。区间程序独立构造 true Toeplitz 与循环核，使用 Machin 恒等式围住 \(\pi\)，用带显式正尾界的 atanh 级数围住对数，并对全部原子作向外舍入。隔离运行严格认证：

- 六点 true-sine 在 \(c=1\) 与 \(19/20\) 的指定局部 skew 为正；
- 同一 pair 的实际权重平均为负；
- \(c=1\) 时全部 15 个实际 pair 平均为负；
- 八点秩四循环模型在 \(c=19/20\) 的指定局部 skew 为正而实际 pair 平均为负。

局部反例只否定逐表非正的加强规则，不否定实际加权平均，更不否定无限体积熵率凹性。

## 6. projection 支持奇异：完整有限维核验

对固定 \(k\)-粒子输入，输出等价于：

- 每个空位以概率 \(\varepsilon p\) 插入粒子；
- 每个已有粒子以概率 \(\varepsilon(1-p)\) 删除粒子。

令增删数为 \(G,L\)。输出层距是 \(|G-L|\)，并且

\[
\mathbb E|G-L|
=\varepsilon[k(1-p)+(n-k)p]
-2k(n-k)\varepsilon^2p(1-p)+O_n(\varepsilon^3).
\]

奇异层熵中的 \(-\mathbb E|G-L|\log\varepsilon\) 因此给出

\[
-\varepsilon\left(\frac{n-k}{p}+\frac{k}{1-p}\right)
+4k(n-k)\varepsilon^2\log(1/\varepsilon)
\]

这两个 \(p\)-曲率系数。故原稿 21–32、490–501 行对“一阶不相消”和 logarithmic 系数的修正是正确的。

Appendix Projection P1–P3 把零层与 \(k\pm1,k\pm2\) 层的 \(v,w\) 系数全部列出，并从

\[
-\sum_y q_y''\log q_y-\sum_y\frac{(q_y')^2}{q_y}
\]

逐层收集出一阶项、\(4k(n-k)\varepsilon^2\log(1/\varepsilon)\) 和完整 \(B_{2,n}''\)。对奇异层的 Taylor 余项，附录以最小正原子和五阶多项式导数给出固定 \(n\) 的显式 \(O(\varepsilon^3(1+|\log\varepsilon|))\) 控制。常数极粗，但量词与用途合法；它没有声称对 \(n\) 一致。

### 实际留数及其下界

对 \(|S|=k+1\)，后验

\[
\Pr(X=S\setminus i\mid S)=|v_i|^2
\]

来自 \((P_N)_S\) 的零空间 minor。常对角 \(\rho=k/n\) 给出

\[
|v_i|^2\le(I-P_N)_{ii}=1-\rho.
\]

所以后验碰撞概率至多 \(1-\rho\)，从而

\[
\alpha_+\le g^2/n.
\]

补投影同理给出 \(\alpha_-\le k^2/n\)，于是

\[
A_n(p_0)\ge\frac{kg}{np_0(1-p_0)}.
\]

Appendix Projection P4 进一步把正则化基准 \(\mu_\eta\) 的对角项与每个自然 pair 逐层展开，证明上述 \(A_n\) 正是完整 \(S_n(\mu_\eta)\) 的 \(-1/\eta\) 留数，并给出 logarithmic 项和有限部。对 \((n,k)=(2,1),(4,2),(5,2),(6,3),(8,4),(10,5)\) 及三个 \(p_0\)，隔离重放的 90 项留数/渐近检查全部通过。

## 7. \(B_{2,n}''\)、交换能量与有限枚举

交换能量

\[
\mathscr D_\mu
=\sum_x\mu(x)\sum_{i\in x,j\notin x}
\log\frac{\mu(x)}{\mu(x-i+j)}
\]

非负，因为无向交换边成对后贡献

\[
(\mu(x)-\mu(x'))\log\frac{\mu(x)}{\mu(x')}\ge0.
\]

对循环 Vandermonde 律，根单位乘积恒等式独立给出

\[
\mathscr D_\mu
=2k(n-k)\log n-2(n-1)H(\mu).
\]

此式在 \(n=4,6,8,10,12\) 的独立枚举中分别以约 \(10^{-15}\) 到 \(10^{-12}\) 的浮点误差吻合。

Appendix Projection P5 从五层质量表直接得到

\[
B_2''(p)=\frac{h}{p(1-p)}-2h\log(p(1-p))-4h-n+\mathcal C_\mu,
\]

并用真实增删通道的链式熵恒等式把 \(\mathcal C_\mu\) 改写为交换能量与一、二次插入/删除反向条件熵。裸的 \(H(\mu)\) 系数确实全部相消。此前的有限枚举现在作为独立交叉检查：

| \(n\) | (7.3) 右端 | 从精确有限通道 \(H_{pp}\) 在 \(\varepsilon=10^{-5}\) 提取的 \(B_{2,n}''\) |
|---:|---:|---:|
| 4 | \(-9.5451774445\) | \(-9.5461430211\) |
| 6 | \(-29.5360218495\) | \(-29.5399833381\) |
| 8 | \(-66.4406329980\) | \(-66.4506899659\) |

误差随 \(\varepsilon\downarrow0\) 单调缩小，并与附录的固定 \(n\) 余项一致。

投影零空间 minor 给出删除集合后验概率至多 \((1-\rho)^r\)，补投影给出删除粒子的对应界。因此：

- projection minor 后验最大概率不超过 \(2^{-r}\)，故 \(h_1\ge\log2,h_2\ge2\log2\)；
- \(B_{2,n}''(1/2)\le-n-2\mathscr D_\mu<0\)；
- 结合 Vandermonde 交换能量和粗熵界，\(B_{2,n}''(1/2)=-\Theta(n^2\log n)\)；
- 对所有允许的有限 \(n\)，半密度常数项严格为负；对偶数 \(n\ge256\)，附录给出显式二侧量级界。

这些结论是 **VERIFIED_SCOPED**，但只关于奇异展开的二阶常数项；同阶仍有正的 logarithmic 项，且固定 \(n\) 的展开没有联合控制 \(n\) 与 \(\varepsilon\)。

## 8. remainder、传递与增长窗口

### full-support remainder

(5.3)/(5.4) 给出的具体常数依赖：

- 对所有高阶通道项的统一 majorant；
- \(p\) 的两次导数；
- 后验归一化产生的重复坐标项；
- \(\beta_n\) 恶化时的精确量词。

Appendix Bounds B1 用 conditional floor \(\beta\) 控制全部 ratio 导数，并以 \(T=n\varepsilon(1+\beta^{-1})\) 收集指数尾。对 \(T\le1/4\)，

\[
|H_{pp}-\varepsilon^2\mathcal L_n|
\le(2H(P)+10)T^3
\]

及互信息值余项 \((4\log(1/\beta)+4)T^3\) 的常数账成立。边界 \(p=0,1\) 由熵表达中的消去处理。124 项主检查包含这些余项的数值压力测试。

### 共同谱隙传递

Appendix Bounds B2 分开控制对角 inverse moment 与四格函数的梯度，再用归一化路径上的 Fisher 恒等式把核距离传到全律 \(L^1\) 距离。共同谱隙 \([\delta,1-\delta]\) 下得到的简化常数 \(2n\delta^{-5}\|K-L\|_F\) 与截断版本 \(4R\delta^{-5}\) 正确。这个定理只比较同一个有限边缘窗口的无条件律。

### 窗口算术

Appendix Bounds B3–B5 给出 sine 压缩的有限谱隙下界、循环核误差以及窗口选择。逐项核对后：

- \(d_m^{-5}\) 产生 \(15a_\rho m\) 的指数代价；
- 精确密度匹配给出 \(N^{-2+15a_\rho\kappa}\)；
- 最近整数匹配给出 \(N^{-1+15a_\rho\kappa}\)；
- \(m=O(1/\varepsilon)\) 时，\(2m(\varepsilon u)^{-5}e_{m,N}=O(\varepsilon^{-8}N^{-2})\)。

所以作者声称的 exact-density、nearest-density 及有噪声边缘窗口都在其量词内成立。它们仍只是相同 \(m\) 点边缘律之间的比较，没有包含观察其余无限外部坐标所损失的信息，因此不能与 S51 已审的 all-exterior 真熵率 Hessian 识别互换。

## 9. 已解除的缺件与仍存在的关键缺口

### 已解除

1. APPENDIX_BOUNDS.md 与 APPENDIX_PROJECTION.md 已补收并完整审查。
2. 严格区间程序及输出已在隔离副本重放。
3. projection 极点、对角有限部、\(B_{2,n}''\) 分层公式和后验熵下界已有自包含推导。
4. 有限边缘传递的梯度常数、sine 谱隙与增长窗口量词已展示。

### 仍存在

1. **真实平均符号仍开。** \(\mathcal J_{ij}''\) 仍回到 S52 的 signed-average 瓶颈；局部正例不决定总体符号。
2. **联合极限仍开。** projection 结论是先固定 \(n\) 再令 \(\eta\downarrow0\)，没有给 \(n=n(\eta)\) 的统一余项。
3. **all-exterior 传递仍开。** 有限边缘核传递没有控制观察无限外部坐标带来的条件信息差。
4. **主端点目标仍开。** 没有纯 logarithmic 包络，也没有完整 \(C(0,1)\)。
5. **外部新颖性未认证。** SOURCE_AUDIT.md 是作者来源账，本审查没有执行独立文献占位检索。

### 隔离重放记录

在 Python 3.12.14、NumPy 2.3.5 下运行完整入口，状态为 PASS：

- verify.py：124 项；
- residue_checks.py：90 项；
- shape_checks.py：94 项；
- finite_part_checks.py：54 项；
- interval_certificate.py：3 个指定模型的严格判号。

合计 362 项有限浮点/代数诊断；严格符号只由 256 位向外舍入的整数/有理区间程序决定，不依赖浮点容差。

## 10. 新工具、旧瓶颈与后续价值

### 新而有用

- 自然二缺陷展开中同点 \(\chi^2\) 项的明确纠正；
- \(\mathcal J_{ij}\) 对 \(p\) 二次且曲率不依赖 \(p\) 的精确公式；
- 真实 sine 可达条件方块中的局部正 skew，作为逐表路线的实际模型反例；
- projection 支持奇异下“一阶不相消”的清晰量词修正；
- projection 留数的后验碰撞表达与常对角下界；
- \(B_{2,n}''\) 的真实反向条件熵公式、补偿后有限部和有限窗口二阶量传递。

### 识别回既有瓶颈

- \(\mathcal J_{ij}''\) 正好是已审 S52 signed skew 的两倍，并没有产生新的平均符号；
- 同点预算必须与异点预算联合支付；
- 有限循环固定 \(n\) 的 \(\eta\downarrow0\) 极点不能决定 true-sine 先取体积极限的 \(\Gamma\)；
- growing marginal window 仍缺 all-exterior 条件信息；
- S51 的 \(O(\log(1/(1-c))/(1-c))\) 端点包络没有被改进。

### 是否值得后续端点全阶任务

**值得定向推进，但不值得继续堆叠固定 \(n\) projection 系数。** 两份承重附录已经通过；下一任务应冻结为：

> 对随噪声正则化的 true-sine 实际输出，在明确的 \(n=n(\varepsilon)\) 量词下，联合控制
> \[
> S_n-\mathcal D_n+\text{全部三阶及更高阶分组},
> \]
> 并把有限边缘条件量传递到观察全部外部输出后的真熵率对象。

成功标准必须同时支付 signed pair、同点 inverse moment、外部条件信息损失和高阶 remainder。若只再次证明有限循环极点、有限窗口核收敛或局部正/负方块，不足以推进主目标。

## 11. 最终裁决

- full-support 二缺陷代数：**VERIFIED_SCOPED**。
- 三阶系数与显式 full-support remainder：**VERIFIED_SCOPED**。
- 与 S52 的精确关系：**VERIFIED_SCOPED**，但属于旧 signed-average 瓶颈。
- 真实可达局部反例与同 pair 实际平均：**VERIFIED_SCOPED**，严格区间证书已独立重放。
- projection 一阶非零曲率与 logarithmic 系数：**VERIFIED_SCOPED**。
- 完整 \(-A_n/\eta\) 极点、对角有限部与 \(B_{2,n}''=-\Theta(n^2\log n)\)：**VERIFIED_SCOPED（固定有限 \(n\)）**。
- 共同谱隙、sine 谱隙与增长窗口：**VERIFIED_SCOPED（有限边缘窗口）**；all-exterior 传递未证。
- 无限 true-sine 平均符号、纯 logarithmic 端点界、完整 \(C(0,1)\)：**INCOMPLETE**。
- 外部新颖性：**NOT_CERTIFIED**；SOURCE_AUDIT.md 已读，但本审查没有作独立外部文献认证。
