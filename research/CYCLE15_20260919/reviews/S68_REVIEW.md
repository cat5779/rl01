# S68 Cycle15 独立数学审查

审查日期：2026-09-19（Asia/Singapore）

## 结论先行

**总状态：INCOMPLETE / PENDING_SOURCE。**

S68 正文中最基础、也最重要的 full-support 代数是正确的：稀疏重采样的二阶互信息展开必须保留同点 \(\chi^2\) 项；自然异点系数 \(\mathcal J_{ij}\) 对 \(p\) 的曲率与 \(p\) 无关；其曲率恰为 S52 actual-output Fisher–Bregman skew 的两倍并按真实外部输出质量加权；共同对角熵 Hessian 的完整二阶账本还必须减去同点 inverse-moment 预算。这一部分是 **VERIFIED_SCOPED**。

正文还正确地区分了：

- full-support 基准与固定粒子数 projection 支持奇异；
- 固定 \(n\) 先取零噪声与先取真实无限体积极限；
- 某个真实可达条件方块的正 skew 与同一 pair 的实际加权平均；
- 相同有限边缘窗口的核传递与观察全部外部输出后的条件量。

但是，作者把以下承重证明放在尚未收到的 APPENDIX_BOUNDS.md、APPENDIX_PROJECTION.md 和代码/证书中：

1. full-support 三阶余项的明确常数；
2. 正则化 projection pair 和的完整 \(-A_n/\eta\) 极点展开；
3. \(B_{2,n}''\) 的精确插入/删除后验熵公式及其 \(-\Theta(n^2\log n)\) 结论；
4. 共同谱隙传递界、sine 压缩谱隙下界和增长窗口；
5. 所谓“纯整数区间证书”的严格复验。

因此这些结论当前不能按作者正文末尾“均给出自包含证明”的说法通过。本文没有发现已审基础代数中的反例，但缺失证明本身是决定性的证据缺口。

本审查不证明完整 \(C(0,1)\)，不证明或反驳无限 true-sine 的纯对数端点猜想，也不认证外部新颖性。

## 1. 审查材料与边界

已收到并完整读取：

- 作者主正文：harvest/CYCLE15/S68/RESULT.md，815 行；
- 作者可见总结：harvest/CYCLE13/S68/S68_LATEST_VISIBLE_REPLY.md，281 行；
- 已审 S52 原稿与独立审查；
- 已审 S51 Cycle06 端点/真熵率接口原稿与独立审查。

未收到：

- APPENDIX_BOUNDS.md；
- APPENDIX_PROJECTION.md；
- SOURCE_AUDIT.md；
- src/interval_certificate.py 及相应严格证书；
- 作者声称的原 44 文件 ZIP 中其余代码、缓存、检查结果和清单。

缺失附录的引用不能充当证明。本文只对正文中可独立重建的部分给出 **VERIFIED_SCOPED**；其余按 **PENDING_SOURCE** 处理。

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
| 368–411 | 六点 true-sine 与八点循环的真实可达局部正 skew | **VERIFIED_SCOPED（数值存在性）**；严格“区间证书” **PENDING_SOURCE** | 独立 90 位/双精度重算复现所有显示值；未收到作者区间程序 |
| 415–448 | 三阶系数 (5.1)/(5.2) | **VERIFIED_SCOPED** | 直接展开 KL 与熵到三阶，系数和符号正确 |
| 450–474 | remainder 界 (5.3)/(5.4) | **PENDING_SOURCE** | 全部 majorant 与常数证明只在缺失的 APPENDIX_BOUNDS.md |
| 478–501 | projection 端点的一阶非零曲率与 \(4k(n-k)\varepsilon^2\log(1/\varepsilon)\) 系数 | **VERIFIED_SCOPED** | 由增删粒子数 \(|G-L|\) 的二阶展开可独立得到；完整 \(B_{2,n}''\) 尚未得到 |
| 503–580 | 正则化 pair 和的 \(-A_n/\eta\) 极点及 (6.3) | **PENDING_SOURCE** | \(A_n\) 的后验碰撞表达与下界代数正确；“它正是 \(S_n\) 留数”的完整分层展开缺失 |
| 549–575 | 常对角投影的 \(A_n\ge kg/[np_0(1-p_0)]\) | **VERIFIED_SCOPED（作为候选留数的下界）** | 零空间 minor 后验与 Hadamard/对角界足够推出 \(\alpha_+\le g^2/n,\alpha_-\le k^2/n\) |
| 584–635 | \(B_{2,n}''\) 的真实插入/删除后验熵公式和严格负号 | **PENDING_SOURCE** | 关键式 (7.2)/(7.3) 的分层收集在缺失附录；独立有限枚举只构成强 sanity check |
| 637–680 | Vandermonde 交换能量 (7.4) 与 \(-\Theta(n^2\log n)\) | (7.4) **VERIFIED_SCOPED**；最终增长 **PENDING_SOURCE** | (7.4) 可由根单位乘积独立重建；增长仍依赖未审的 (7.3) |
| 681–688 | 补偿后有限部分 \(F_n\) 及 \(d_0=O(n^2)\) | **PENDING_SOURCE** | 公式与“不依赖最小原子”的界都只在缺失附录 |
| 694–712 | 共同谱隙传递界 (8.1) | **PENDING_SOURCE** | score/全局四格梯度证明与 \(\delta^{-5}\) 常数未提供 |
| 714–757 | sine 压缩谱隙 \(d_m\)、循环边缘传递 (8.2)–(8.5) | **PENDING_SOURCE** | 插值证明缺失；下游指数运算本身一致 |
| 759–786 | 对数增长窗口与有噪声多项式窗口 | **PENDING_SOURCE / INCOMPLETE** | 都依赖未审 (5.4)、(8.1)、(8.2)；且明确只比较边缘窗口，不是 all-exterior 条件量 |
| 790–815 | 完整 \(C(0,1)\) 未证明、平均符号与高阶余项仍开 | **VERIFIED_SCOPED** | 范围声明准确；但 815 行“均给出自包含证明”不适用于当前收到的材料 |

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

这些复算强力支持“真实可达局部正、实际平均仍可负”的范围判断。不过作者声称的是纯整数区间证书；相应程序和证书未收到，所以“严格认证”这一证据等级仍为 **PENDING_SOURCE**。

局部反例只否定逐表非正的加强规则，不否定实际加权平均，更不否定无限体积熵率凹性。

## 6. projection 支持奇异：已核验与未核验部分

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

但是，完整的 \(B_{2,n}''\)、奇异 remainder 及各层常数并未在正文展开，不能据上述两项就验证 (0.2) 的全部内容。

### 候选留数下界

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

这段下界是自包含并通过的。尚未通过的是：缺失附录必须证明这个 \(A_n\) 确实是完整 \(S_n(\mu_\eta)\) 展开中的 \(-1/\eta\) 留数，并控制余项。故 (6.3) 整体仍为 **PENDING_SOURCE**。

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

作者的关键式 (7.2)/(7.3) 把 \(B_{2,n}''\) 表成交换能量与真实一、二次插入/删除后验熵。缺失附录前，本文不把它升级为证明。独立枚举只作 sanity check：

| \(n\) | (7.3) 右端 | 从精确有限通道 \(H_{pp}\) 在 \(\varepsilon=10^{-5}\) 提取的 \(B_{2,n}''\) |
|---:|---:|---:|
| 4 | \(-9.5451774445\) | \(-9.5461430211\) |
| 6 | \(-29.5360218495\) | \(-29.5399833381\) |
| 8 | \(-66.4406329980\) | \(-66.4506899659\) |

误差随 \(\varepsilon\downarrow0\) 单调缩小，强烈支持系数公式，但这不是所有 \(n\) 的证明。

如果 (7.3) 成立，那么：

- projection minor 后验最大概率不超过 \(2^{-r}\)，故 \(h_1\ge\log2,h_2\ge2\log2\)；
- \(B_{2,n}''(1/2)\le-n-2\mathscr D_\mu<0\)；
- 结合 (7.4) 和粗熵界，(7.5)–(7.7) 的 \(-\Theta(n^2\log n)\) 推论代数正确。

当前应发布为：“增长结论有一致的独立有限证据和正确的下游代数，但承重分层公式等待附录核验。”

## 8. remainder、传递与增长窗口

### full-support remainder

(5.3)/(5.4) 给出的具体常数依赖：

- 对所有高阶通道项的统一 majorant；
- \(p\) 的两次导数；
- 后验归一化产生的重复坐标项；
- \(\beta_n\) 恶化时的精确量词。

正文只陈述结果并指向缺失附录。因此状态是 **PENDING_SOURCE**。三阶显式系数 (5.1)/(5.2) 本身已独立通过，但不能替代整个尾和。

### 共同谱隙传递

(8.1) 的 \(\delta^{-5}\) 常数必须同时支付实际原子权重变化和条件四格变化。正文没有给出 score 到全局四格函数的完整梯度账，因此状态是 **PENDING_SOURCE**。

### 窗口算术

在假定 (5.4)、(8.1)、(8.2) 后，正文的下游指数运算一致：

- \(d_m^{-5}\) 产生 \(15a_\rho m\) 的指数代价；
- 精确密度匹配给出 \(N^{-2+15a_\rho\kappa}\)；
- 最近整数匹配给出 \(N^{-1+15a_\rho\kappa}\)；
- \(m=O(1/\varepsilon)\) 时，\(2m(\varepsilon u)^{-5}e_{m,N}=O(\varepsilon^{-8}N^{-2})\)。

但这些只是相同 \(m\) 点边缘律之间的比较。它们没有包含观察其余无限外部坐标所损失的信息，因此不能与 S51 已审的 all-exterior 真熵率 Hessian 识别互换。

## 9. 关键缺口与最小缺件

### CRITICAL_GAPS

1. **当前提交不是自包含证明包。** 原稿 52、474、492、569、645、681–688、712、786 行把承重证明放在缺失附录；815 行“均给出自包含证明”与实际收到的材料不一致。
2. **严格证书不可复验。** 原稿 394–409 行引用 src/interval_certificate.py，但程序和输出均未收到。独立高精度重算支持数值，不等于作者声称的区间认证。
3. **projection 极点与 \(B_{2,n}''\) 的核心分层账未展示。** 候选留数下界和 Vandermonde 能量正确，仍不足以自动推出它们在完整熵展开中的系数。
4. **传递定理的常数与量词未展示。** 不能从核收敛或有限窗口数值直接升级为 all-exterior/entropy-rate 结论。

### PENDING_SOURCE 的最小解除条件

至少需要收到并逐行审查：

1. APPENDIX_BOUNDS.md；
2. APPENDIX_PROJECTION.md；
3. SOURCE_AUDIT.md；
4. src/interval_certificate.py 与它实际读取的输入/输出证书；
5. 若附录引用其他文件，再补齐那些直接依赖，而不是仅提供 44 文件清单。

无需哈希门槛，但文件内容必须可读，且正文中的定理编号、变量和量词必须能与附录逐项对齐。

## 10. 新工具、旧瓶颈与后续价值

### 新而有用

- 自然二缺陷展开中同点 \(\chi^2\) 项的明确纠正；
- \(\mathcal J_{ij}\) 对 \(p\) 二次且曲率不依赖 \(p\) 的精确公式；
- 真实 sine 可达条件方块中的局部正 skew，作为逐表路线的实际模型反例；
- projection 支持奇异下“一阶不相消”的清晰量词修正；
- 候选 projection 留数的后验碰撞表达与常对角下界；
- 若附录通过，\(B_{2,n}''\) 与有限窗口二阶量传递会是可复用工具。

### 识别回既有瓶颈

- \(\mathcal J_{ij}''\) 正好是已审 S52 signed skew 的两倍，并没有产生新的平均符号；
- 同点预算必须与异点预算联合支付；
- 有限循环固定 \(n\) 的 \(\eta\downarrow0\) 极点不能决定 true-sine 先取体积极限的 \(\Gamma\)；
- growing marginal window 仍缺 all-exterior 条件信息；
- S51 的 \(O(\log(1/(1-c))/(1-c))\) 端点包络没有被改进。

### 是否值得后续端点全阶任务

**有条件值得。** 前提是先取得并通过两份承重附录。后续任务不应继续堆叠固定 \(n\) projection 系数，而应冻结为：

> 对随噪声正则化的 true-sine 实际输出，在明确的 \(n=n(\varepsilon)\) 量词下，联合控制
> \[
> S_n-\mathcal D_n+\text{全部三阶及更高阶分组},
> \]
> 并把有限边缘条件量传递到观察全部外部输出后的真熵率对象。

成功标准必须同时支付 signed pair、同点 inverse moment、外部条件信息损失和高阶 remainder。若只再次证明有限循环极点、有限窗口核收敛或局部正/负方块，不足以推进主目标。

## 11. 最终裁决

- full-support 二缺陷代数：**VERIFIED_SCOPED**。
- 与 S52 的精确关系：**VERIFIED_SCOPED**，但属于旧 signed-average 瓶颈。
- 真实可达局部反例：存在性得到独立高精度复算；作者的严格区间证书为 **PENDING_SOURCE**。
- projection 一阶非零曲率与 logarithmic 系数：**VERIFIED_SCOPED**。
- 完整 \(-A_n/\eta\) 极点、\(B_{2,n}''=-\Theta(n^2\log n)\)、full-support remainder、谱隙传递和窗口定理：**PENDING_SOURCE**。
- 无限 true-sine 平均符号、纯 logarithmic 端点界、完整 \(C(0,1)\)：**INCOMPLETE**。
- 外部新颖性：**PENDING_SOURCE**；未收到 SOURCE_AUDIT.md，本审查也未作外部文献认证。

