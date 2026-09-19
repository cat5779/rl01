# Claude/Fable Cycle16 研究建议独立对抗性审计

审查日期：2026-09-19

审查对象：用户粘贴的 Claude/Fable 研究建议及其中的 AUTHOR_ONLY 数值。没有收到原作者数值源码。本文只把明确公式、独立推导和本审查自行生成的有限探针作为证据。

相关已审边界：

- S64 PR46 只证明 block KL 关于长度的离散凸性，并明确禁止把它解释成 entropy 曲率、参数凸性或完整熵率凹性；
- S63 PR47 证明的是 \(\rho=1/3,c=.95,a\in[.021,.024]\) 的 scoped 真分布定理，不自动适用于半密度；
- S68 PR48 的完整附录已有独立 scoped 审核：full-support 二缺陷代数，以及固定体积 projection 的端点系数/增长、余项界、有限边缘窗口传递均为 VERIFIED_SCOPED；joint volume/noise uniform remainder、all-exterior transfer 与 infinite true-law sign 仍未完成。

## 结论先行

| 建议中的核心内容 | 裁决 |
|---|---|
| \(n=12,c=.95\) 的四项数值分解 | VERIFIED_NUMERICAL_REPRODUCTION，作用域为真实 Toeplitz、\(\rho=1/2,a=.025\) |
| 有限熵三项恒等式 | VERIFIED |
| 无限全偶位／有限循环的随机投影表示 | VERIFIED_SCOPED |
| 有限 Toeplitz 条件核也是投影 | COUNTEREXAMPLE_WITH_SCOPE |
| midpoint influence 行和等于 \(c^2\) | 无限投影与匹配循环 VERIFIED；有限 Toeplitz WRONG |
| covariance 行和等同 Dobrushin influence | WRONG_INFERENCE |
| 循环 projection 的 observed Fisher 等于 \(n/b\) | VERIFIED_SCOPED，仅 midpoint、固定粒子数投影 |
| 一般实际 Toeplitz observed Fisher 等于 \(n/b\) | WRONG；只有上界 |
| \(F_n=-H_n''\) 超加性等价于 \(\Gamma_n=F_n/n\) 单调递增 | WRONG_INFERENCE |
| \(F_n\) 超加性本身 | UNPROVED；有限探针未找到反例 |
| Fekete + Dini 自动给 \(-h''=\lim F_n/n\) | WRONG_INFERENCE |
| 单个 \(\Gamma_{20}(a_0)>0\) 证明熵率 midpoint 凹性 | WRONG_INFERENCE |
| resampling 熵分解 | VERIFIED |
| resampling 把问题化为 \(-I_{n,pp}\) 超加性 | VERIFIED 代数重写；不是新不等式 |
| 七点／有限 \(n\) 无违反推出超加性 | UNPROVED |
| Toeplitz/cyclic 数值给出严格熵率上下界 | UNPROVED |
| \(R_*\asymp\varepsilon^{-1/2}\)、\(\Gamma=\Theta(\varepsilon^{-1})\) | UNPROVED HEURISTIC |

最重要的承重判断是：

\[
F_{m+n}(a)-F_m(a)-F_n(a)
=\frac{d^2}{da^2}I(Y_{[m]};Y_{[m+1,m+n]}).
\]

所以新路线真正需要证明或反驳的是：

> 实际 sine Toeplitz 输出的相邻块互信息是否关于共同对角平移参数 \(a\) 凸？

这不是 S64 的 KL 长度凸性，也不是由负相关、谱独立或有限拟合自动推出的结论。

## 对全区间 \(c\in(37/40,1)\) 的当前胜算

这是研究判断而非可证明的置信区间：以现有证据估计，新路线直接闭合整个区间的概率约为 **20%**，合理主观区间为 **15%--25%**。它取得决定性进展（严格反例、有效子区间，或真正弱于原瓶颈的新引理）的概率更高，但这不等于完成原目标。

相对原方法，它有**中等的诊断优势、尚无已验证的证明优势**：相邻块互信息凸性把核心困难冻结成一个可直接证伪的命题，84 个本审查探针没有发现违反；然而该命题与 \(F_n\) 超加性完全等价，resampling 版本又只是带 \(\varepsilon^{-2}\) 的同一曲率差，因此都没有严格减弱主瓶颈。半密度循环 projection 的漂亮等式也不能无损移植到真实有限 Toeplitz；而 \(c\uparrow1\) 所需的 uniform remainder、all-exterior transfer 与 infinite true-law sign 仍未闭合。

若路 2 能给出覆盖端点邻域的严格区间符号证书，并找到从有限块到任意块的传播机制，胜算会实质上升；在此之前，把“无小反例”折算成高完成概率是不可靠的。

## 1. 冻结符号

对真实有限 Toeplitz 块定义

\[
K_n(a)=aI_n+cQ_{\rho,n},\qquad
H_n(a)=H(\operatorname{DPP}(K_n(a))).
\]

冻结

\[
F_n(a):=-H_n''(a),\qquad
\Gamma_n(a)=\frac{F_n(a)}n.
\]

实际完整配置 Fisher 信息是

\[
J_n(a)=\sum_y\frac{(p_a'(y))^2}{p_a(y)}.
\]

它不是 count Fisher，也不是 complete-data Fisher。完整 moving-law 恒等式为

\[
H_n''(a)
=-J_n(a)-\sum_y p_a''(y)\log p_a(y).
\]

因此

\[
F_n=J_n+\sum_y p_a''\log p_a.
\]

讨论“天花板”“余量”和单调方向时必须固定这组符号。

## 2. 半密度奇偶约化

### 2.1 无限投影

对无限 half-density sine projection，

\[
Q_{2r,2s}=\frac12\mathbf 1_{r=s},
\qquad Q_{2r+1,2s+1}=\frac12\mathbf 1_{r=s}.
\]

故两个 parity 压缩均为 \(I/2\)，潜变量 \(X_{\rm even}\) 是 iid 公平硬币。

将算子按 even/odd 分块，由 \(Q^2=Q\) 得

\[
Q_{oe}Q_{eo}=Q_{oo}-Q_{oo}^2=\frac14I,
\]

另一侧也同样成立。因此 \(U=2Q_{eo}\) 是酉算子。

在给定全部偶位配置 \(x\) 的正规条件分布意义下，形式计算给

\[
Q_{o\mid x}
=\frac12I+2Q_{oe}S_xQ_{eo}
=I-U^*\operatorname{diag}(x)U,
\]

其中 \(S_x=\operatorname{diag}(1-2x)\)。右侧确为投影。

这一步若用于无限熵，仍需通过有限条件和条件熵率极限处理；不能直接相减三个无限熵。

### 2.2 有限循环

匹配的偶数长度 half-band cyclic Fourier projection 满足同样的 parity block 恒等式。\(X_e\) 有 \(2^{n/2}\) 个等权配置，每个条件 odd 核是酉共轭的坐标投影。

所以“随机投影系综”在此模型是准确说法。

### 2.3 有限 Toeplitz

有限 Toeplitz 压缩仍有

\[
(Q_n)_{ee}=(Q_n)_{oo}=I/2,
\]

所以窗口内 \(X_e\) 仍是 iid 公平硬币。条件核公式也仍正确：

\[
(Q_n)_{o\mid x}
=\frac12I+2(Q_n)_{oe}S_x(Q_n)_{eo}.
\]

但 \(Q_n^2\ne Q_n\)，故一般

\[
(Q_n)_{oe}(Q_n)_{eo}\ne I/4,
\]

\(U=2(Q_n)_{eo}\) 不是酉矩阵，条件核不是投影。

这是一个严格 scoped 反例。取 \(n=2,\rho=1/2\)，

\[
Q_2=
\begin{pmatrix}
1/2&1/\pi\\
1/\pi&1/2
\end{pmatrix}.
\]

给定唯一偶位 bit 后，odd 条件核分别为

\[
\frac12+\frac2{\pi^2},
\qquad
\frac12-\frac2{\pi^2},
\]

二者都不属于 \(\{0,1\}\)，所以不是一维投影。

**裁决：COUNTEREXAMPLE_WITH_SCOPE。** “64 个随机投影”不能描述 \(n=12\) 真 Toeplitz 实验；准确名称是 64 个条件 contraction kernels。

## 3. \(n=12,c=.95\) 数字复现

本审查脚本 CLAUDE_CYCLE16_checks.py 使用真实 \(12\times12\) sine Toeplitz 压缩，

\[
\rho=\frac12,\qquad c=.95,\qquad a=.025,
\]

枚举全部 \(2^{12}\) 个输出配置，并用

\[
p' =p\,\operatorname{Tr}G,\qquad
p''=p\{(\operatorname{Tr}G)^2-\operatorname{Tr}(G^2)\}
\]

计算共同对角导数。

自行生成的结果是

\[
H_{12}''=-126.1801285607,
\]

\[
H''(Y_e)=-24,
\]

\[
E_xH''(Y_o\mid X_e=x)=-66.6215671493,
\]

\[
\partial_a^2 I(X_e;Y_o\mid Y_e)=-35.5585614114.
\]

最不负的条件 odd 曲率为

\[
\max_x H_x''=-48.6848604730.
\]

条件互信息值本身为

\[
I(X_e;Y_o\mid Y_e)=0.1607583383\ \text{nat}.
\]

这些值与建议中的 \(-126.2,-24.0,-66.6,-35.6,-48.7,.16\) 一致，因而可反推其实际参数和模型就是上述真 Toeplitz midpoint，而不是循环 projection。

同一次计算给出 64 个条件核的投影缺陷

\[
\|B_x^2-B_x\|_{\rm op}\in[0.2162,0.2397],
\]

并给出

\[
\|Q_{12}^2-Q_{12}\|_{\rm op}=0.1992.
\]

因此数值是可复现的，但“随机投影”解释错误。

## 4. 完整熵三项分解

在任意有限窗口，链式法则给

\[
H(Y_e,Y_o)=H(Y_e)+H(Y_o\mid Y_e).
\]

插入 \(X_e\)：

\[
\begin{aligned}
H(Y_o\mid Y_e)
&=H(Y_o\mid X_e,Y_e)
+I(X_e;Y_o\mid Y_e)\\
&=E_xH(Y_o\mid X_e=x)
+I(X_e;Y_o\mid Y_e).
\end{aligned}
\]

第二个等号使用

\[
Y_o\perp Y_e\mid X_e,
\]

因为 \(Y_e\) 只使用 \(X_e\) 和独立通道噪声。

潜变量 \(X_e\) 的权重与 \(a\) 无关，所以

\[
\partial_a^2E_xH(Y_o\mid X_e=x)
=E_x\partial_a^2H(Y_o\mid X_e=x).
\]

但互信息项的全部分布都随 \(a\) 移动。某个条件核系综平均凹并不足以证明总熵凹；仍需控制

\[
\partial_a^2 I(X_e;Y_o\mid Y_e).
\]

在上述 \(n=12\) 点它为负并帮助凹性，但单点负号不是全参数、全体积定理。

**裁决：恒等式 VERIFIED；由系综平均直接闭合总熵属于 WRONG_INFERENCE。**

## 5. midpoint influence 行和

在 infinite half-density projection 的 midpoint，

\[
K_{ii}=\frac12,\qquad K_{ij}=cQ_{ij}\quad(i\ne j).
\]

投影恒等式给

\[
\sum_{j\ne i}|Q_{ij}|^2
=(Q^2)_{ii}-Q_{ii}^2
=\frac14.
\]

所以

\[
\sum_{j\ne i}
\frac{|K_{ij}|^2}{K_{ii}(1-K_{ii})}
=c^2
=1-4b,
\qquad b=\frac{1-c^2}{4}.
\]

匹配有限循环 projection 也成立。

有限 Toeplitz 中

\[
\sum_{j\ne i}^{n}
\frac{|K_{ij}|^2}{1/4}
=4c^2\{(Q_n^2)_{ii}-1/4\}
<c^2,
\]

缺口正是窗口外 Fourier leakage，且依赖位置。上面的 \(n=2\) 例子已经给出严格不等。

更重要的是，该行和是归一化 pair covariance 的和，因为 DPP 有

\[
\operatorname{Cov}(X_i,X_j)=-|K_{ij}|^2.
\]

Dobrushin 系数则是对所有外部边界词取 sup 的条件概率变化和；二者不是同一对象。即使某个 pinning 定理给出不超过 1，也不提供严格小于 1 的统一余量，更不自动控制全条件 log-odds。

**裁决：无限/循环恒等式 VERIFIED；有限 Toeplitz 等号与 Dobrushin 识别 WRONG_INFERENCE。**

## 6. Fisher、曲率和 \(\Gamma\)

令

\[
a_*=\frac{1-c}{2},\qquad
b=a_*(1-a_*)=\frac{1-c^2}{4}.
\]

在 half density midpoint，完整潜变量/输出数据得分的 Fisher 信息是

\[
J_n^{\rm complete}=\frac nb.
\]

实际只观察 \(Y\) 时由条件 Jensen

\[
J_n^{\rm observed}\le\frac nb.
\]

若潜在 DPP 是有限 rank-\(n/2\) projection，则 \(|X|=n/2\) 恒定，完整得分化为

\[
S=\frac{|Y|-n/2}{b},
\]

已经是 \(Y\) 的函数。因此循环 projection 在 midpoint 确有

\[
J_n^{\rm observed}=\frac nb.
\]

有限 Toeplitz 压缩不是固定粒子数 projection，等号失效。本审查的 \(n=12,c=.95\) 真 Toeplitz 重算给

\[
J_{12}^{\rm observed}=246.3619198,
\qquad
\frac{12}{b}=492.3076923.
\]

“约为完整数据天花板的 50%”在这个单点数值上准确，但不是一般定理。

同一点

\[
F_{12}=126.1801286,\qquad
\Gamma_{12}=10.5150107.
\]

所以 \(J_n\)、\(F_n\) 和 \(n/b\) 是三个不同对象。

对循环 projection，本审查重现

\[
\Gamma_8=25.3484,\quad
\Gamma_{10}=23.6224,\quad
\Gamma_{12}=22.2841,\quad
\Gamma_{16}=20.3663,
\]

同时 \(J_n/n=1/b=41.02564\)。这些是有限循环数据，不是 true-sine 熵率上界。

按冻结定义 \(\Gamma=-H''/n\)，\(\Gamma\) 越大表示负曲率越强。把“接近 Fisher 天花板”称作“凹性余量归零”会混淆：

- 凹性量本身 \(\Gamma\) 在增大；
- 可能缩小的是 Fisher 天花板与实际曲率之间的 pair-payment 差。

二者必须分名。

## 7. 曲率超加性捷径

令

\[
A_{m,n}(a)=H_m(a)+H_n(a)-H_{m+n}(a).
\]

平稳相邻块下，

\[
A_{m,n}=I(Y_{[m]};Y_{[m+1,m+n]}).
\]

精确微分给

\[
A_{m,n}''
=H_m''+H_n''-H_{m+n}''
=F_{m+n}-F_m-F_n.
\]

因此

\[
F_{m+n}\ge F_m+F_n
\quad\Longleftrightarrow\quad
A_{m,n}''\ge0.
\]

这是一条清楚、可证伪的新命题：相邻块互信息对 \(a\) 凸。

### 7.1 与 \(\Gamma_n\) 单调不等价

若 \(\Gamma_n\) 随每个整数 \(n\) 单调递增，则

\[
F_{m+n}=(m+n)\Gamma_{m+n}
\ge m\Gamma_m+n\Gamma_n,
\]

所以它蕴含超加性。

反向不成立。纯数列

\[
F_n=\lfloor n/2\rfloor
\]

是超加的，但

\[
\frac{F_2}{2}=\frac12,\qquad
\frac{F_3}{3}=\frac13.
\]

故“超加性等价于 \(\Gamma_n\) 单调增”是严格错误。

### 7.2 Fekete 不完成导数识别

若对固定 \(a\)，\(F_n(a)\) 超加，Fekete 只给

\[
\lim_n\frac{F_n(a)}n
=\sup_n\frac{F_n(a)}n.
\]

它没有自动给

\[
-h''(a)=\lim_nF_n(a)/n.
\]

即使另知 \(h\in C^2\)，函数值 \(H_n/n\to h\) 也不足以交换二阶导数。

Dini 定理要求一列连续函数在紧集上单调点态收敛到连续极限。这里：

1. 超加性不使 \(\Gamma_n\) 随全部 \(n\) 单调；
2. 极限 \(\Gamma(a)\) 的连续性尚未证明；
3. 在识别 \(\Gamma=-h''\) 前，引用 \(h\in C^2\) 并不补足前两项。

### 7.3 单点信息不够

只有

\[
\Gamma_{20}(a_0)>0
\]

不能证明 \(h\) 在 \(a_0\) 附近凹。曲率结论需要参数邻域上的控制，才能积分成弦差。

一个合法的修正版是：

> 在开区间 \(I\) 上，对所有 \(a\in I\) 和全部 \(m,n\)，证明 \(F_{m+n}(a)\ge F_m(a)+F_n(a)\)。再找到某个固定 \(r\) 与 \(\kappa>0\)，使 \(F_r(a)\ge\kappa r\) 对整个较小闭区间 \(I_0\Subset I\) 成立。则 \(F_{kr}(a)\ge\kappa kr\)。对有限 \(H_{kr}\) 的曲率界积分并沿倍数子列取熵值极限，可直接得到 \(h\) 在 \(I_0\) 上的强弦凹性，系数为 \(\kappa/2\)。

这条修正版不需要 Dini，也不需要先识别 \(h''\)。

### 7.4 廉价反例搜索

本审查对真实 sine Toeplitz 模型自行扫描：

- \(\rho\in\{.2,1/3,.5,.7\}\)；
- \(c\in\{.5,.8,.95\}\)；
- \(a/(1-c)\in\{.02,.1,.3,.5,.7,.9,.98\}\)；
- 所有 \(m,n\ge1,\ m+n\le10\)。

共 84 个参数点，没有发现

\[
F_{m+n}-F_m-F_n<0.
\]

最小浮点余量约为 \(0.0110\)。另一次更宽的 120 点、\(m+n\le12\) 探针同样无反例。

这些是本审查自行生成的双精度探针，不是区间证书。它们使该命题值得继续攻击，但不能把 UNPROVED 升级为 VERIFIED。

## 8. resampling 分解

令

\[
\varepsilon=1-c,\qquad a=\varepsilon p.
\]

独立选择 resampling mask \(E\)，每点以概率 \(\varepsilon\) 进入；在 \(E\) 上用 iid \(\operatorname{Bernoulli}(p)\) 替换，在补集保留 \(X\)。则输出核恰为

\[
cQ+aI.
\]

条件于 \(E\)，

\[
H(Y\mid E)
=E_EH(X_{E^c})+n\varepsilon h_{\rm b}(p).
\]

由 \(H(Y)=H(Y\mid E)+I(E;Y)\)，得到

\[
\boxed{
H_n
=n\varepsilon h_{\rm b}(p)
+E_EH(X_{E^c})
+I_n(E;Y).
}
\]

这是 VERIFIED。

关于 \(p\) 求导，

\[
H_{n,pp}
=-\frac{n\varepsilon}{p(1-p)}
+I_{n,pp}.
\]

因为 \(\partial_a=\varepsilon^{-1}\partial_p\)，

\[
\boxed{
F_n(a)
=\frac{n}{\varepsilon p(1-p)}
-\frac1{\varepsilon^2}I_{n,pp}(p).
}
\]

所以

\[
F_{m+n}-F_m-F_n
=-\frac1{\varepsilon^2}
\{I_{m+n,pp}-I_{m,pp}-I_{n,pp}\}.
\]

线性于体积的基准项完全抵消。于是 \(F_n\) 超加等价于 \(-I_{n,pp}\) 超加，但这只是移项；核心不等式没有变容易。

同时

\[
F_{m+n}-F_m-F_n=A_{m,n}''.
\]

所以 resampling 版本和“邻块互信息关于 \(a\) 凸”是同一个 blocker 的两种写法。S64 的 KL length supermodularity 不支付这里的 moving-reference \(I_{n,pp}\)。

## 9. 对数／幂次端点猜想

有限数据中 \(\Gamma b\) 约为常数量，至多支持

\[
\Gamma\approx\frac{\text{常数}}b
\sim\frac{\text{常数}}{\varepsilon}
\]

作为猜想。若该渐近在先取 \(n\to\infty\) 后严格成立，则因

\[
-h_{pp}=\varepsilon^2\Gamma,
\]

会导向 \(-h_{pp}=\Theta(\varepsilon)\)。

当前证据不足，因为：

1. 只有少数 \(c\) 和有限 \(n\)；
2. \(n\to\infty\) 与 \(\varepsilon\downarrow0\) 的双极限没有统一控制；
3. \(c=1\) projection 端点失去 full support；
4. 循环固定体积的极点不决定 true-sine 熵率极点；
5. \(R_*\asymp\varepsilon^{-1/2}\) 没有从可检查公式推出。

因此 \(c\in[.93,.97]\) 的实验适合作为证伪／尺度辨识任务，不能称作“危险区已证明”。

## 10. 对用户给出的其余数值的裁决

| 数值陈述 | 裁决 |
|---|---|
| \(n=12,c=.95\) 的 \(-126.2,-24,-66.6,-35.6,-48.7,.16\) | 本审查独立重现 |
| true Toeplitz \(\Gamma_n\) 在 \(n=1,\ldots,12\) 递增 | 本审查独立重现；有限探针 |
| cyclic \(\Gamma_8=25.35\) 且随后下降 | 本审查重现到 \(n=16\)；有限探针 |
| cyclic observed Fisher \(=n/b\) | midpoint projection 下严格成立 |
| \(\Gamma_{20}(.95)=11.836\) | AUTHOR_ONLY，本审查未重算 \(n=20\) |
| 七个 \(a\) 点、\(n=6,\ldots,18\) 零违反 | AUTHOR_ONLY；与本审查较小扫描相容 |
| 三个 \(\Gamma_\infty\) 区间 | 不是严格区间，除非另证超加下界和 cyclic/Toeplitz 上界 |
| 天花板 \(1/b=41.0256\) | complete Fisher per-site 上界；不是 \(\Gamma\) 的已达值 |

有限 Toeplitz \(\Gamma_n\) 增和循环 \(\Gamma_n\) 减，不能在没有模型比较定理时自动夹出熵率。

## 11. 六路任务分工的数学风险与可用修正版

以下只是任务设计建议，不是启动六路。

### 路 1：模型卫生与 parity 表示

**修正版任务：**分别为无限全偶位、有限循环、有限 Toeplitz 写出对象、条件核和极限接口；禁止共用“random projection”标签。

**风险：中。** 代数容易，但无限条件与有限熵率接口会偷入边界项。

**成功证据：**有限窗口恒等式、循环投影证明、Toeplitz leakage 的显式式子。

### 路 2：超加性反例搜索

**修正版任务：**直接认证

\[
A_{m,n}''(a)
=F_{m+n}(a)-F_m(a)-F_n(a)
\]

的符号；覆盖一般 \(a\)、端点附近、\(\rho=1/2\) 和普通密度。

**风险：最高，但最便宜。** 浮点零违反很可能掩盖窄小负区。

**成功证据：**满足真实 sine Toeplitz 前提的向外区间反例，或覆盖明确有限盒的零反例证书。

### 路 3：相邻块互信息凸性证明

**修正版任务：**若路 2 未发现反例，证明或定位

\[
\partial_a^2 I(Y_{[m]};Y_{[m+1,m+n]})\ge0.
\]

**风险：最高。** 这是全新 moving-law 参数凸性；负相关和 S64 KL 长度凸性都不够。

**禁止：**用“\(\Gamma_n\) 看起来递增”替代证明。

### 路 4：有限曲率到熵率弦差

**修正版任务：**证明第 7.3 节的 interval-uniform finite-chord lemma。

**风险：低到中。** 只需超加性在整个参数邻域成立；不必使用 Dini 或交换二阶导数。

**成功证据：**对倍数子列积分有限曲率并取熵值极限。

### 路 5：resampling mutual-information 曲率

**修正版任务：**在保留 \(\varepsilon^{-2}\) 的前提下研究

\[
I_{m+n,pp}\le I_{m,pp}+I_{n,pp}.
\]

**风险：最高。** 它与原超加性等价，可能只是换名 blocker。

**成功证据：**严格弱于原题的可组合不等式；单纯重写熵分解不算进展。

### 路 6：端点尺度证伪实验

**修正版任务：**在 \(c\in[.93,.97]\) 分别控制 finite-size、true Toeplitz/cyclic 差和 \(p\) 位置，检验 \(R_*\) 与 \(\Gamma b\) 尺度。

**风险：中。** 容易把双极限拟合误写成定理。

**成功证据：**预注册的 competing exponents、误差条和有限尺寸外推；结论只标 EXPERIMENTAL。

## 12. 推荐优先级

1. **先做路 2。** 超加性若有小反例，Fekete 路线立即停止。
2. **并行做路 1。** 防止循环 projection 与真 Toeplitz 再次混用。
3. **路 2 存活后才做路 3。**
4. **路 4 可作为低风险接口任务提前形式化。**
5. **路 5 不应与路 3同时包装成两条独立进展；它们共享同一 blocker。**
6. **路 6 只负责证伪和尺度辨识，不给证明票。**

## 最终裁决

Claude/Fable 建议包含三个真实有用对象：

1. half-density parity 条件分解；
2. 相邻块互信息凸性这一明确可证伪命题；
3. resampling 的精确熵账本。

但其主要“捷径”尚未成立。超加性与 \(\Gamma_n\) 逐 \(n\) 单调不等价；Fekete 不自动识别熵率二阶导；Dini 的前提缺失；单个 \(\Gamma_{20}>0\) 不能完成 midpoint 熵率凹性。

建议把下一轮核心题冻结为：

> 对真实 sine Toeplitz DPP，证明或反驳相邻块互信息 \(A_{m,n}(a)\) 对共同对角平移 \(a\) 的凸性；若只在某个参数区间成立，给出该区间和严格边界。

在这个命题获得证明或严格反例之前，不能把有限拟合的 \(\Gamma\) 区间称为熵率上下界。
