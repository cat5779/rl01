# QWE08 Cycle33 独立数学审查

## 总裁决

**`RANK_ONE_THEOREM_VERIFIED / FINITE_CONTINUUM_CERTIFIED /
TERM_WISE_EXTENSION_DISPROVED / ALL_SIZE_TARGET_INCOMPLETE`。**

我支持 QWE08 的以下作用域结论：

1. 对任意有限 rank-one bipartite common-shift DPP、任意坐标切割，
   classical configuration mutual information 关于共同平移参数凸；存在跨
   cut 非零边时严格凸，正文给出的 \(|C_{eo}|^4\) 定量下界正确。
2. 半密度真 sine-Toeplitz 在总尺寸不超过 3 时，对全部
   \(0<c<1\) 和全部合法内部 \(0<a<1-c\) 的相邻切割严格成立
   \(M_{m,n}''(a)>0\)。
3. 四点 sine 块中指定 monomial 的系数精确为
   \(-s^{10}/27\)。它严格否定逐 monomial 非负扩展，但不是
   \(M''<0\) 或熵率非凹反例。
4. 在 \(c=19/20\)、\(a\in[1/50,3/100]\) 上，全部
   \(m+n\le4\) 的相邻切割具有严格 continuum certificate，统一下界
   大于 1.5454668697424。
5. finite-chord/Fekete 接口合法，不交换熵率极限与二阶导。

需要纠正的是“新增”的分层，而不是数学结论：

- common-shift nilpotent probability operator 已由 S47 的 signed
  translation 给出；S77 的 cofactor 方程是它的一、二阶微分形式。
  QWE08 的新贡献是把该旧工具用于严格有限连续区间证书，不是重新发现
  后将算子本身计为新定理。
- rank-one 证明使用了与 S75 星形方法同源的 actual-weight 偏置矩和
  非负幂级数机制，但定理陈述实质更广：两个 parity 类都可含多个坐标，
  切割任意，结论直接是 mutual-information convexity。它不是 S75
  星形定理的字面重复，也不是完全独立的新机制。
- \(32\delta^{-12}\) 的 dimension-free MI curvature bound 确实来自
  QWE02；S74 是后续的另一层 merge-tree/rate 支付。把原始不等式来源
  写为 QWE02 没有误指，无需改成 S74。

没有证明：全部 \(m,n\)、任何 all-size superadditivity、熵率在目标区间
的最终凹性，或 \((37/40,1)\) 的全范围结论。

## 1. 冻结对象与 rate 接口

目标量是完整配置 Shannon mutual information

\[
M_{m,n}(a)=H_m(a)+H_n(a)-H_{m+n}(a),
\]

其中 \(K_N(a)=aI+cQ_{1/2,N}\)。没有替换为 cyclic projection、count
entropy 或 spectral entropy。

若在一个实参数区间对全部 \(m,n\) 有 \(M_{m,n}''\ge0\)，则 \(M\)
凸。正文的 chord 记号

\[
\operatorname{Gap}_\lambda f
=f(a_\lambda)-(1-\lambda)f(a_0)-\lambda f(a_1)
\]

满足 \(\operatorname{Gap}M\le0\)，故

\[
\operatorname{Gap}H_{m+n}
\ge \operatorname{Gap}H_m+\operatorname{Gap}H_n.
\]

Fekete 用于有限 chord sequence；左端极限只需三个固定参数点上的
\(H_N/N\to h\)。因此

\[
\operatorname{Gap}h\ge r^{-1}\operatorname{Gap}H_r
\]

合法，没有使用 \(-h''=\lim F_N/N\)。但当前 QWE08 只证到总尺寸 4，
所以这个接口尚不能启动全尺度 Fekete 结论。

## 2. Rank-one bipartite 密度公式

令

\[
B=\begin{pmatrix}0&C\\C^*&0\end{pmatrix},\qquad
K(t)=tI+B,
\]

且 \(\operatorname{rank}C\le1\)、
\(\sigma=\|C\|_{\rm op}<t<1-\sigma\)。相对 product
Bernoulli\((t)\) 参考律 \(q_t\)，逐 word 行列式分解给出

\[
\frac{dP_t}{dq_t}(y)
=\det(I+\operatorname{diag}(\xi(y))B).
\]

bipartite 主子式只有 parity-balanced 阶数可能非零。rank one 使所有
四阶及以上 balanced minor 消失，二阶子式为 \(-|C_{eo}|^2\)，所以

\[
f=\frac{dP_t}{dq_t}=1-U,
\qquad
U=\sum_{e,o}|C_{eo}|^2\xi_e\xi_o.
\]

rank one 还给出
\(\sum_{e,o}|C_{eo}|^2=\sigma^2\)。由
\(\min(t,1-t)>\sigma\) 得到逐点 \(|U|<1\)，且
\(E_qU=0\)。因此

\[
D(P_t\|q_t)
=\sum_{k\ge2}\frac{E_qU^k}{k(k-1)}.
\]

上述等式、符号和系数均正确。

## 3. Multigraph 符号与任意 cut 消去

顶点度为 \(r\) 时出现的矩是

\[
\mu_r(t)=t^{1-r}+(-1)^r(1-t)^{1-r}.
\]

置 \(x=2t-1\)。偶数 \(r\ge2\) 的 \(\mu_r\) 是非负系数的偶幂级数；
奇数 \(r\ge3\) 是非正系数的奇幂级数；\(\mu_1=0\)。非零 graph
没有 degree-one 顶点，而奇度顶点数为偶数，故每个非零 multigraph
贡献最终是非负系数的偶幂级数。

对任意坐标切割 \(A|A^c\)，恒等式

\[
I(Y_A;Y_{A^c})
=D(P_V\|q_V)-D(P_A\|q_A)-D(P_{A^c}\|q_{A^c})
\]

成立。完全位于一侧的 multigraph 与对应边缘展开逐项相消；未完全位于
单侧的项保留，且仍有上述非负偶幂系数。注意“保留项”不必每个都含
一条 crossing edge；它也可以由两侧内部的 disconnected pieces 组成。
这不影响非负性。严格下界只保留确实跨 cut 的同一条边重复两次的
\(k=2\) 项。

正文对逐项求二阶导只写了实紧集上的 uniform \(|U|<1\)，说明略短，
但缺口可在原前提下闭合：对任意实紧子区间取一个稍大的复邻域，仍有
\(|t|,|1-t|>\sigma\)，故 geometric expansion 作为解析函数族正常
收敛；也可利用非负 \(x\)-系数，在稍大半径处的有限值控制内部所有导数。
因此二次逐项微分合法，不需要新增假设。

## 4. 定量严格凸下界

一条 crossing edge 重复两次在 \(k=2\) 项中贡献

\[
\frac12|C_{eo}|^4\mu_2(t)^2
=\frac12|C_{eo}|^4[t(1-t)]^{-2}.
\]

两次求导正好是

\[
|C_{eo}|^4
\left[
\frac{3(1-2t)^2}{[t(1-t)]^4}
+\frac{2}{[t(1-t)]^3}
\right].
\]

其余项的二阶导非负，故正文盒装下界与严格性成立。

独立实现以 determinant atoms 和 deleted-coordinate marginals 重建
\(M''\)，没有复用作者证明代码。10 个随机复 rank-one \(2\times3\)
cross blocks、全部 300 个非平凡坐标切割均满足该下界；最小浮点 slack
为 \(1.24\times10^{-8}\)。五点有限差分与 cofactor 解析值最大差
\(3.85\times10^{-8}\)。这些是实现交叉检查，一般证明由上面的级数
论证承担。

## 5. 与 S75 星形方法的关系

S75 的几何是一个中心加单 parity 叶子，cross block 自动为一行或一列。
它证明实际背景权重平均下的 pair potential 正漂移，承重机制也是：

- Bernoulli 偏置矩符号；
- 非负幂级数；
- support 内一致绝对收敛；
- 保留最低非零项得到显式正下界。

QWE08 把这个符号引擎提升到 rank-one outer-product cross block，并借
KL-to-product 展开直接处理任意 coordinate cut 的 mutual information。
当两个 parity 类都含多个坐标时，不能用一般 unitary rotation 把它
化成 classical-coordinate 星形，因为这种 rotation 不保持配置变量。
所以 Theorem 2.1 是相对 S75 的实质定理增量；但方法论应标成
“S75 型 actual-weight moment positivity 的推广”，不应标成完全独立
的全新路线。

## 6. 半密度总尺寸不超过 3

半密度 sine compression 的非零 off-diagonal entries 只连接不同
parity。总尺寸不超过 3 时，至少一个 parity 类只有一个坐标，所以
cross block rank 至多 1。有限 sine compression 严格满足
\(0\prec Q_{1/2,n}\prec I\)，于是全部
\(0<c<1,0<a<1-c\) 给出严格 DPP contraction，并等价满足
\(\sigma<t<1-\sigma\)。

每个非平凡 adjacent split 都切过一个 odd-distance 非零 sine entry，
故严格凸性成立。独立网格覆盖 \(n=2,3\)、四个 \(c\) 和三个合法 bias
比例，共 36 个相邻切割，最小浮点 \(M''\) 为
\(1.32\times10^{-4}>0\)。一般全参数结论来自 rank-one 定理，不来自
该网格。

## 7. 四点负系数障碍

四点 parity-reordered cross block 是

\[
C=s\begin{pmatrix}1&-1/3\\1&1\end{pmatrix}.
\]

直接用有理多项式展开
\((1+u)\log(1+u)\) 并提取
\(x_1^3x_2^2y_1^2y_2^3s^{10}\)，独立得到精确系数

\[
-\frac1{27}.
\]

这与正文

\[
\alpha^2\beta^3\gamma\delta^2
(2\alpha\delta+3\beta\gamma)
\]

的乘积式一致。代入给出 \(-s^{10}/27\)。对应 Bernoulli moment 是
\(\mu_3^2\mu_2^2\ge0\)，所以负号不会被取期望自动消掉。

这只证明 raw termwise nonnegativity 已失败。完整 \(M''\) 还包含同阶及
其他阶的正负项；QWE08 没有把它误写为 convexity 反例。

## 8. Common-shift operator 的归属

逐坐标算子

\[
(D_ip)(y)=(2y_i-1)[p(y)+p(y^i)]
\]

满足 \(p'=\sum_iD_ip\)、\(D_i^2=0\)，且不同 \(D_i\) 交换。因此

\[
p_{a+z}=\sum_{k=0}^n\frac{z^k}{k!}D^kp_a.
\]

代数正确。独立四点重放得到 \(D^5p=0\) 精确到机器零，shift polynomial
与直接 determinant atoms 最大误差 \(4.17\times10^{-17}\)。

但归属上：S47 已给出
\(p_{a+t}=p_aT_t^{\otimes n}\) 与同一 nilpotent generator；S77 的
\(\dot p=\sum_i\sigma_i p_{-i}\)、
\(\ddot p=2\sum_{i<j}\sigma_i\sigma_jp_{-ij}\) 是前两阶。故 Section 5
是正确的复用/再表达。新的是它与 interval Taylor entropy machinery 的
组合。

## 9. 复解析半径、log branch 与 Cauchy 尾

在 \(a_*=1/40,c=19/20\) 有
\(\delta I\preceq K\preceq(1-\delta)I\)、\(\delta=1/40\)。对含
\(r\) 个 holes 的
\(A_y=K-D_{1-y}\)，rank-\(r\) eigenvalue interlacing 给出恰有
\(r\) 个本征值 \(\le-\delta\)，其余 \(\ge\delta\)。所以 atom
polynomial 在 \(|z|<\delta\) 无零，穿过正实中心值的 log branch 唯一
解析。

取 \(R=1/50\)，则 \(R/\delta=4/5\)。由

\[
|\log(1+w)|
\le\sum_{j\ge1}|w|^j/j
\le\log5
\]

得到正文的 atom 与 entropy 圆周界

\[
|H_n(a_*+z)|\le n(9/5)^n\log10.
\]

半密度下 particle-hole 加 alternating diagonal gauge 把 \(z\) 送到
\(-z\)，因此 entropy 是偶解析函数；不是数值观察。

若 \(M=\sum b_{2j}z^{2j}\)，对二阶导余尾取
\(k=L+1,\tau=(r/R)^2\)，则

\[
\sum_{q\ge0}[4(k+q)^2-2(k+q)]\tau^q
\]

正好展开成式 (6.2) 的三项。系数、\(\tau^L\)、\(R^{-2}\) 均正确。
当 \(L=12,r/R=1/4\) 时，检查
\(b_4,\ldots,b_{24}\ge0\) 及 \(2b_2-T>0\) 足以覆盖整个实区间，
不是网格论证。

## 10. 固定点区间脚本审计与实际运行

脚本的有理端点、乘除、倒数、Machin \(\pi\)、atanh-log 余尾均向外
取整。所有接受判据最终比较整数端点；Decimal 只用于打印。conditional
DPP recursion、nilpotent Taylor 系数、formal log/entropy recurrence 与
Cauchy tail 的方向均正确。

实际以 Python 3.12.14 执行

```text
certify_qwe08.py --max-n 4 --order 24
```

重新计算全部 atoms 与系数，四个相邻切割证书全部通过，最小 enclosure
为

\[
[1.5454668697424313269,1.5454668697424313269].
\]

运行生成的最终整数内容与随附 JSON 一致；验收没有读取该 JSON。因而
这是严格 continuum certificate。它的量词仍只有固定
\(c=19/20\)、指定 \(a\)-区间和总尺寸 \(\le4\)。

## 11. QWE02/S74 来源核对

本库的 QWE02 独立审查明确认证

\[
|I(Y_A;Y_B)''|
\le32\delta^{-12}\|K_{AB}\|_{\rm HS}^2.
\]

因此 QWE08 Section 7 将 dimension-free \(\delta^{-12}\) bound 归因
QWE02 是正确来源。S74 的贡献是后续在 merge-tree/Toeplitz 语境中的
支付与接口，不应反过来取代 QWE02 的原定理归属。

## 12. 对 S80 最有用的新承重输入

不向 S80 发送消息的前提下，本审查认为最值得后续接入的是：

1. **rank-one 正基线：** 每条 crossing edge 有显式 quartic
   \(|C_{eo}|^4\) payment。可把一般 cut 分解为 rank-one/spanning
   部分与 determinant-loop defect，而不是重新对全部 acceleration
   取绝对值。
2. **第一个精确 loop defect：** 四点 \(-s^{10}/27\) 指明最早需要
   分组补偿的是 \(2\times2\) determinant loop。S80 若控制 Burg charge，
   应寻找“正 rank-one forests 支付负 loops”的平均不等式，而非逐
   rectangle/monomial 正性。
3. **严格小尺度 seed：** 在 \(c=.95,J=[.02,.03]\) 上，dyadic 前两种
   adjacent merges \(1+1\) 与 \(2+2\) 已有直接 \(M''>0\) continuum
   certificate。它可以令这些尺度的直接 MI residual 为零；但没有认证
   S77 更强的 \(\mathcal B_+\le\mathcal I_{\rm rel}\)。
4. **有限尺度区间化模板：** nilpotent polynomial 加 Cauchy tail 可把
   固定 \(N\) 的全 \(a\)-区间从网格升级为证书。其成本仍随
   \(2^N\) 增长，不能单独承担 all-size 结论。

## 13. 最终边界

- **新定理且已证：** rank-one bipartite 任意切割 MI 凸性及定量下界；
  半密度总尺寸 \(\le3\) 的全 \(c\)/全合法 bias 推论。
- **严格证书：** 固定 \(c=.95\)、\(a\in[.02,.03]\)、总尺寸
  \(\le4\) 的 continuum positivity。
- **严格障碍：** 四点逐 monomial 非负机制失败。
- **重复但正确工具：** common-shift nilpotent operator；QWE02
  \(\delta^{-12}\) bound 的调用。
- **仍未解决：** all-size MI convexity、负 loop 的统一补偿、可支付的
  almost-superadditive defect、最终熵率区间结论。

因此 QWE08 是一个真实的局部推进：它扩展了 S75 型符号机制、给出严格
四点 seed，并精确暴露 rank-two loop 障碍；但它没有结束 all-block 或
entropy-rate 目标。
