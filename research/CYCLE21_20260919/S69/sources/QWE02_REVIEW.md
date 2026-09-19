# QWE02 独立数学审查

日期：2026-09-18

审查对象：

- `harvest/CYCLE08/QWE02/RESULT.md`；
- `verify_qwe02.py` 与 `checks.json`；
- 原提交 `randomcat4/dpp-stationary-entropy` PR #123。

审查方式：逐式重建完整配置 Shannon 熵曲率、联合/边际 moving-law 差、复 Hermitian 方向的一阶与二阶微分、迹理想估计、偶跨块路径和真实 sine dyadic 尾；原样复跑数值检查。浮点输出只用于证伪和抄写诊断，不作为一般定理证明。

## 总裁决

- **有限谱隙 DPP 定理：VERIFIED。** 若
  \[
  K(a)=aI+K_*,\qquad
  \delta I\preceq K(a)\preceq(1-\delta)I,
  \]
  并把坐标分成 (A\sqcup B)，则经典配置互信息满足
  \[
  \boxed{
  |\mathcal J''(a)|
  \le32\delta^{-12}\|K_{AB}\|_{\rm HS}^2.}
  \]
  常数确实与两块大小无关。
- **完整 moving-law 曲率表示：VERIFIED。** 作者没有把配置概率冻结，也没有删除 (p''\log p)、Fisher 项或边际参考律的导数。联合与两个边际的完整二阶导严格化为同一实际联合律下的跨块缺陷期望。
- **无维数梯度/Hessian 引理：VERIFIED。** 式 (18)--(21) 的矩阵分解、复 Hermitian 二阶微分和常数均成立。线性非对角项保留为算子乘积；只有立方余项使用绝对行和，因此没有隐藏的 (n)、\(\sqrt n\) 或块体积因子。
- **迹理想与偶路径：VERIFIED。** (R'=-RVR)、(R''=2RVRVR) 分别在 Hilbert--Schmidt 与 trace norm 中得到式 (27)。跨块符号酉 (W=I_A\oplus(-I_B)) 使 (F(-\theta)=F(\theta))，故 (F'(0)=0)，Taylor 积分真正产生二次跨块能量。
- **真实 sine 推论：VERIFIED。** 相邻长度 (L) 块的跨边界 HS 能量至多
  \[
  \frac{2+\log L}{\pi^2},
  \]
  对全部 (0<\rho<1) 一致。因此二次弦尾为
  \[
  O_I\!\left(\eta^2\frac{\log L_*}{L_*}\right),
  \]
  且没有交换熵率极限与导数。
- **脚本复现：PASS AS DIAGNOSTIC。** 原样重跑成功；熵曲率的两种有限计算、Fisher 恒等式、跨块缺陷恒等式和复方向微分均与提交记录在舍入量级内一致。
- **逐配置正性：DISPROVED，但不影响定理。** 真 sine 的 (L=1) 混合配置已经给出严格负跨块缺陷。定理使用绝对值及实际律平均，没有依赖逐配置正号。
- **实用性：存在性强、数值性弱。** 在指定 (c=19/20,\delta=3/200) 上，常数约 (4.51\times10^{22})。它闭合了 QWE02 的渐近边界响应义务，但不能直接支付现有小尺度带符号 benchmark，也不证明互信息曲率非负或最终熵率凹性。

建议状态：

> **QWE02 main theorem and sine dyadic-tail corollary: VERIFIED_SCOPED; practical sign closure and full entropy-rate concavity: OPEN.**

## 1. 冻结命题与量词

有限站点上令 (K(a)=aI+K_*) 为 Hermitian DPP 核，并假定整个实区间 (I) 内具有统一谱隙

\[
\delta I\preceq K(a)\preceq(1-\delta)I,
\qquad0<\delta<1/2.
\]

把站点分成任意不交两块 (A,B)，记 (C=K_{AB})。要审查的核心命题是

\[
|I(Y_A;Y_B)''|\le32\delta^{-12}\|C\|_{\rm HS}^2.
\]

这里：

- 熵是完整配置的经典 Shannon 熵；
- (A,B) 大小可不同；
- (K_*)、因而 (C)，不随 (a) 变化；
- 端点导数由有限 DPP 在 (0\prec K\prec I) 的光滑延拓解释；
- 定理不声称曲率有符号。

这些量词在正文证明中均未被弱化。

## 2. 原子矩阵与统一翻转比

对配置 (y\in\{0,1\}^n)，令

\[
M_y=K-D_{1-y},\qquad R_y=M_y^{-1}.
\]

完整原子满足

\[
p_K(y)=(-1)^{\#\{i:y_i=0\}}\det M_y.
\]

### 2.1 鞍点逆矩阵

若空位数为 (r)，由

\[
\delta I-D_{1-y}\preceq M_y
\preceq(1-\delta)I-D_{1-y}
\]

和有序本征值单调性可得：(M_y) 的前 (r) 个本征值不大于 (-\delta)，其余本征值不小于 (\delta)。因此

\[
\|R_y\|_{\rm op}\le\delta^{-1}.
\]

该论证不是把 Loewner 不等式错误地逐本征向量使用；它使用的是对应序号的 min--max 单调性，方向正确。

### 2.2 单、双位翻转比

写

\[
\sigma_i=1-2y_i,
\quad t_i=-1-\sigma_iR_{ii},
\]

\[
d_{ij}=t_it_j-\sigma_i\sigma_j|R_{ij}|^2.
\]

determinant lemma 给

\[
t_i=\frac{p(y^i)}{p(y)},qquad
d_{ij}=\frac{p(y^{ij})}{p(y)}.
\]

把任意谱隙核写成

\[
K=\delta I+(1-2\delta)\widetilde K,
\qquad0\preceq\widetilde K\preceq I,
\]

等价于先采样 (\operatorname{DPP}(\widetilde K))，再逐坐标通过 crossover (\delta) 的二元信道。条件于其余输出后，单点两种概率均在 ([\delta,1-\delta])，两点四种模式均在 ([\delta^2,(1-\delta)^2])。因此正文使用的较松界

\[
\delta\le t_i\le\delta^{-1},
\qquad
\delta^2\le d_{ij}\le\delta^{-2}
\]

合法且无体积依赖。这个噪声表示只用于概率比，不参与 (a)-微分，故不存在冻结依赖 (a) 的 latent law 的问题。

## 3. 完整配置熵曲率

定义离散差分

\[
\nabla_i f(y)=f(y_{i\leftarrow1})-f(y_{i\leftarrow0}),
\qquad G=\sum_i\nabla_i.
\]

因为 (K'(a)=I)，余子式微分给

\[
\sum_y p_a'(y)f(y)=\mathbb E Gf,
\qquad
\sum_y p_a''(y)f(y)=\mathbb E G^2f.
\]

这是真实的 moving probability identity；(G^2) 保留全部 (i\ne j) 的概率加速度。

令

\[
\mathcal A_\sigma(R)
=2\sum_{i<j}\sigma_i\sigma_j
\log\frac{t_it_j-\sigma_i\sigma_j|R_{ij}|^2}{t_it_j},
\]

\[
\mathcal T_\sigma(R)=\mathcal A_\sigma(R)+\operatorname{tr}R^2.
\]

两次配置差分给

\[
G^2\log p=\mathcal A_\sigma(R_y).
\]

另一方面

\[
(\log p)'=\operatorname{tr}R_y,qquad
(\log p)''=-\operatorname{tr}R_y^2.
\]

由概率归一化的二阶导，

\[
\mathbb E(\operatorname{tr}R_y)^2
=\mathbb E\operatorname{tr}R_y^2.
\]

于是完整 Shannon 熵满足

\[
\boxed{H''(K(a))=-\mathbb E\mathcal T_\sigma(R_y).}
\]

概率加速度与 Fisher 项都在此式内，没有双算或漏算。

## 4. 联合减边际的精确缺陷

只缩放跨块耦合：

\[
K_\theta=
\begin{pmatrix}K_A&\theta C\\\theta C^*&K_B\end{pmatrix},
\qquad0\le\theta\le1.
\]

这是块对角核与原核的凸组合，所以整条路径保留相同谱隙。对固定 joint word，(R_0=R_A\oplus R_B)，而 (\mathcal T) 在块直和上可加。虽然 (Y_A,Y_B) 在真实联合律下不独立，但

\[
\mathbb E_{p_{AB}}\mathcal T_A(R_A)
=\mathbb E_{p_A}\mathcal T_A(R_A)
\]

只用边际化，因此成立。于是

\[
\boxed{
\mathcal J''(a)
=\mathbb E_{p_a}
[\mathcal T_\sigma(R_1)-\mathcal T_\sigma(R_0)].}
\]

这一式正确保留了两个 moving marginal reference laws，是本稿相对于只处理联合熵的关键接口。

## 5. 式 (18)--(21) 的独立常数审计

对单个 pair 置

\[
f=\varepsilon(\log d-\log t-\log u),
\qquad d=tu-\varepsilon|r|^2.
\]

对复 Hermitian 方向 (Z)，记

\[
h_i=-\sigma_iZ_{ii},\quad h_j=-\sigma_jZ_{jj},
\quad z=Z_{ij},\quad v=\operatorname{Re}(\bar rz).
\]

### 5.1 梯度

直接微分并利用 (d=tu-\varepsilon|r|^2) 消去裸对角项，得到

\[
Df[Z]
=\frac{|r|^2}{td}h_i+rac{|r|^2}{ud}h_j
-\frac{2\operatorname{Re}(\bar rz)}d.
\]

因 (\mathcal A=2\sum_{i<j}f_{ij})，其梯度矩阵 (B) 满足

\[
B_{ii}=-2\sigma_i\sum_{j\ne i}
\frac{|R_{ij}|^2}{t_id_{ij}},
\qquad
B_{ij}=-\frac{2R_{ij}}{d_{ij}}.
\]

对非对角部分使用

\[
\frac1{d_{ij}}
=\frac1{t_it_j}
+\frac{\sigma_i\sigma_j|R_{ij}|^2}{t_it_jd_{ij}}.
\]

第一项保留为

\(-2D_t(R-\operatorname{diag}R)D_t\)，算子范数不超过 (4\delta^{-3})。立方余项每行绝对值和至多

\[
2\delta^{-4}max_j|R_{ij}|\sum_j|R_{ij}|^2
\le2\delta^{-7}.
\]

加上对角项 (2\delta^{-5})，确有

\[
\|B\|_{\rm op}\le8\delta^{-7}.
\]

由 trace/operator 对偶，

\[
|D\mathcal A(R)[Z]|
\le8\delta^{-7}\|Z\|_1.
\]

这里最危险的线性 (R_{ij}) 项没有逐条绝对求和，因此不存在隐藏的 (\sqrt n) 损失。

### 5.2 Hessian

再次微分得到正文式 (25)。独立符号化简确认其与

\[
\varepsilon\left(
\frac{d''}{d}-\frac{(d')^2}{d^2}
+\frac{h_i^2}{t^2}+\frac{h_j^2}{u^2}
\right)
\]

完全一致，包括 (\varepsilon=-1) 与复 (z) 的情形。逐项使用

\(t,u\in[\delta,\delta^{-1}])、(d\ge\delta^2)、
\(|r|^2\le\delta^{-2}) 后，

\[
|D^2f[Z,Z]|
\le5\delta^{-6}|r|^2(h_i^2+h_j^2)
+10\delta^{-6}|z|^2.
\]

求和时

\[
\sum_{j\ne i}|R_{ij}|^2\le\delta^{-2}
\]

支付全部 diagonal directions，而 off-diagonal entries正好按 HS 范数计数。因此

\[
|D^2\mathcal A(R)[Z,Z]|
\le10\delta^{-8}\|Z\|_{\rm HS}^2.
\]

加入 (\operatorname{tr}R^2) 的梯度 (2R) 与 Hessian
\(2\operatorname{tr}Z^2)，正文的

\[
|D\mathcal T[Z]|\le10\delta^{-7}\|Z\|_1,
\quad
|D^2\mathcal T[Z,Z]|
\le12\delta^{-8}\|Z\|_{\rm HS}^2
\]

成立。

## 6. 逆矩阵路径与二次消去

令

\[
V=\begin{pmatrix}0&C\\C^*&0\end{pmatrix},
\quad R_\theta=(M_0+\theta V)^{-1}.
\]

则

\[
R_\theta'=-R_\theta VR_\theta,
\quad
R_\theta''=2R_\theta VR_\theta VR_\theta.
\]

迹理想乘法给

\[
\|R_\theta'\|_{\rm HS}
\le\delta^{-2}\|V\|_{\rm HS},
\]

\[
\|R_\theta''\|_1
\le2\delta^{-3}\|V\|_{\rm HS}^2.
\]

第二式确实只使用两个 HS 因子与一个 operator 因子，没有把 trace norm 粗化为维数乘 operator norm。链式法则给

\[
|F''(\theta)|
\le32\delta^{-12}\|V\|_{\rm HS}^2.
\]

跨块反号酉 (W=I_A\oplus(-I_B)) 满足

\[
R_{-\theta}=WR_\theta W,
\]

而 (\mathcal T) 对此共轭不变，所以 (F'(0)=0)。因此

\[
|F(1)-F(0)|
\le\frac12\,32\delta^{-12}\|V\|_{\rm HS}^2
=32\delta^{-12}\|C\|_{\rm HS}^2,
\]

其中使用了 (\|V\|_{\rm HS}^2=2\|C\|_{\rm HS}^2)。系数链闭合。

## 7. 二次弦与真实 sine 尾

三角核恒等式

\[
\Delta_\eta\mathcal J(a)
=\int_{-\eta}^{\eta}(\eta-|s|)
\mathcal J''(a+s)\,ds
\]

的总质量是 (\eta^2)，故弦界具有真正的独立 (\eta^2) 因子。

对相邻长度 (L) 的 sine 块，距离 (r) 的跨块 pair 数为

\[
w_L(r)=\min(r,2L-r).
\]

于是

\[
\|(Q_\rho)_{AB}\|_{\rm HS}^2
\le\frac1{\pi^2}
\left(\sum_{r=1}^L\frac1r
+L\sum_{r>L}\frac1{r^2}\right)
\le\frac{2+\log L}{\pi^2}.
\]

只使用 (\sin^2(\pi\rho r)\le1)，故覆盖全部 (0<\rho<1)。对于
\(L_j=L_*2^r)，

\[
\sum_{r\ge0}2^{-r}=2,
\qquad
\sum_{r\ge0}r2^{-r}=2
\]

给出

\[
\sum_{j\ge N}
\frac{|\Delta_\eta J_{m2^j}(a)|}{2m2^j}
\le
\Gamma\eta^2
\frac{2+\log L_*+\log2}{L_*}.
\]

该结论只拼接有限尺度弦，不对熵率求导。

## 8. 计算复现与反例作用域

原脚本在固定 seed `20260918` 下复跑成功。重新生成的检查文件位于本地审查目录。主要结果包括：

- 概率归一化误差约 (3.3\times10^{-16})；
- 两种完整熵曲率计算最大差约 (7.1\times10^{-14})；
- Fisher 恒等式残差约 (8.9\times10^{-15})；
- 直接四原子差分与逆矩阵表达的最大差约 (5.8\times10^{-13})；
- 复 Hermitian 一、二阶微分的有限差分误差保持在脚本阈值内。

这些结果排除了明显符号、共轭和实现抄写错误，但不承担一般证明。

在 (L=1\)、平衡点，混合配置的缺陷为

\[
4\log(u/v)+2/v-8<0.
\]

这严格反驳逐配置非负性，却不反驳本文绝对值界。正文对该作用域的说明正确。

## 9. 最强可信结论与未完成目标

可以认证：

1. 任意有限、一致有谱隙 Hermitian DPP 的共同对角平移互信息曲率由跨块 HS 能量控制；
2. 真实 sine 相邻块的二次互信息弦尾为
   (O_I(\eta^2\log L/L))；
3. 结论覆盖所有 (0<\rho<1) 以及任意紧含于合法 shift 区间内部的 (a)-区间；
4. 逐配置贡献无需有符号。

没有完成：

- (J_L''\ge0) 或任何统一符号；
- 小尺度有限带符号 dyadic 和的有用下界；
- 当谱隙 (\delta\downarrow0) 时的一致控制；
- 从式 (30) 自动推出目标熵率凹性；
- 将 (4.51\times10^{22}) 的指定参数常数变成实际可判号常数。

因此该成果是一个正确且可复用的边界响应工具，但不是最终符号定理。
