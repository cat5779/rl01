# S51 高 \(c\) 续稿独立数学审查

## 裁决

| 审查项 | 裁决 |
|---|---|
| SA02 balanced-line seed 的引用 | `VERIFIED_SCOPED`，继承其 frozen pair/row 依赖 |
| 所有有限 \(n\) 的二维窄条带曲率界 | `VERIFIED_SCOPED` |
| full-atom Chebyshev moving-law 展开 | `VERIFIED_WITH_LOCAL_PROOF_REPAIR` |
| mixed \(aac\) 响应与四阶横向增厚 | `VERIFIED` |
| 半密度 complement–gauge 对称与 \(f_{aaa}=0\) | `VERIFIED` |
| 有限强凹弦到真熵率 | `VERIFIED` |
| 接入 S51 bridge 后的实际律 \(\Gamma_c\) 正号 | `VERIFIED_SCOPED` |
| 精确有理算术脚本 | `REPRODUCED_ARITHMETIC_CERTIFICATE` |
| 到 \(0.95\)、全 \(c<1\)、全 \(\rho\) 或宽条带 | `NOT_PROVED` |

总裁决：相对于已经独立审查、但明确依赖旧 frozen pair/row 恒等式的 SA02 balanced-line 接口，续稿的新增推导成立。对真实半密度 sine Toeplitz 主块、每个有限 \(n\)，严格证明了

\[
\boxed{
\partial_a^2 f_n(a,c)\le-\frac1{200}}
\]

在以下闭条带上成立：

\[
\boxed{
\frac{37}{40}\le c\le
\frac{937}{1000}+3\times10^{-13},
\qquad
\left|a-\frac{1-c}{2}\right|\le10^{-9}.}
\]

这里必须直读数值尺度：对比度上端只是

\[
0.9370000000003,
\]

即越过 \(0.937\) 仅 \(3\times10^{-13}\)；横向 \(a\)-半宽为 \(10^{-9}\)。本报告只按这个真实范围评价，不把稿件标题或“improves”措辞升级成更强的客观结论。

## 1. 审查对象和依赖边界

最终来源是完整原稿 `S51_CYCLE06_C37_REFINEMENT.md`（17,749 bytes、712 行）及精确算术脚本 `S51_CYCLE06_C37_REFINEMENT_checks.py`。早先的 chat 导出不作为最终裁决来源。

令

\[
Q_n=(Q_{i-j})_{1\le i,j\le n}
\]

为真实半密度 sine Toeplitz 主块，

\[
f_n(a,c)=\frac1nH\!\left(\operatorname{DPP}(aI_n+cQ_n)\right),
\qquad
m(c)=\frac{1-c}{2}.
\]

续稿只外接两个接口：

1. SA02 已审 balanced line 上
   \[
   f_{n,aa}(m(c),c)\le-\frac1{50},
   \qquad \frac{37}{40}\le c\le\frac{937}{1000}.
   \]
2. 固定合法 \((a,c)\) 时，真 Toeplitz 边际的块熵每点极限存在。

第一项确实包含 \(c=937/1000\) 的闭端点，且适用于每个有限 \(n\)；由 \(f_n=H_n/n\)，SA02 的 \(H_n''\le-n/50\) 正好变成上述归一化界。但 SA02 审查本身明确写明“相对于冻结的 pair 恒等式和定向行预算”。续稿没有重新证明这些底层接口，本报告也不把该依赖抹去。

第二项不需要额外的 Hessian 极限定理。核 \(aI+cQ\) 定义一致的无限平稳 DPP，\(Q_n\) 是其真实有限边际；Shannon 块熵的次可加性给出 \(H_n/n\) 的熵率极限。后文只传值，不传导数。

## 2. 完整 moving-law full-atom 展开

对任意有限 Hermitian contraction \(0\le Q\le I\)，设

\[
K(a,c)=aI+cQ,\qquad
\delta I\le K(a,c)\le(1-\delta)I.
\]

对配置 \(S\) 写

\[
A_S=K-D_{S^c}.
\]

原子恒等式

\[
p_{a,c}(S)=(-1)^{n-|S|}\det A_S=|\det A_S|
\]

以及真配置熵表示

\[
f(a,c)
=-\frac1{2n}\mathbb E_{a,c}\operatorname{Tr}\log A_Y^2
\]

均正确；这里不是 \(\operatorname{Tr}b(K)\)。

原稿把

\[
\delta^2I\le A_S^2\le I
\]

简写为来自 “eigenvalue interlacing”。单靠这句话不足以说明零点附近的谱隙。本审查补出短证明。令 \(S_S=I-2D_{S^c}\)，则

\[
A_S=\frac{S_S}{2}
+\left(K-\frac12I\right)
=\frac{S_S}{2}
\left[I+2S_S\left(K-\frac12I\right)\right].
\]

由于

\[
2\left\|K-\frac12I\right\|\le1-2\delta,
\]

括号可由 Neumann 级数求逆，且 \(\|A_S^{-1}\|\le\delta^{-1}\)。这给出所需下界；上界由 \(\|A_S\|\le1\) 得到。故这是局部证明说明缺失，不是定理缺口。

取

\[
r=\frac{1-\delta}{1+\delta},
\qquad
X_Y=\frac{2A_Y^2-(1+\delta^2)I}{1-\delta^2},
\]

标量 Chebyshev 展开给出

\[
f(a,c)=C_\delta+\sum_{m\ge1}u_m(a,c),
\qquad
\|u_m\|_\infty\le\frac{r^m}{m}.
\]

关键的 moving-law 账目也完整。Boolean 化前
\(\operatorname{Tr}T_m(X_Y)\) 在 \((a,c,Y)\) 中总次数至多 \(2m\)；每个单项式

\[
a^pc^q\prod_{i\in V}Y_i,
\qquad p+q+|V|\le2m,
\]

在实际 DPP law 下满足

\[
\mathbb E_{a,c}\prod_{i\in V}Y_i
=\det(aI+cQ)_V.
\]

右端总次数为 \(|V|\)，所以取实际律期望后总次数仍不超过 \(2m\)。后续参数微分已经包含 probability weights 的全部导数，没有 frozen-law 遗漏。

## 3. mixed \(aac\) 响应

原稿先在 \(a\) 方向应用内区间二阶 Bernstein 界，再对多项式 \(P_{aa}(a,\cdot)\) 在 \(c\) 方向应用一阶界，得到

\[
\|\partial_c\partial_a^2P\|
\le\frac8{\ell_c\ell_a^2}
\left(
\frac{D^3}{\sigma_c\sigma_a^2}
+\frac{D^2}{\sigma_c\sigma_a^3}
\right)\|P\|.
\]

代入 \(D=2m\) 和 \(\|u_m\|\le r^m/m\) 后，两项分别产生

\[
64\sum_{m\ge1}m^2r^m=64S_2(r),
\qquad
32\sum_{m\ge1}mr^m=32S_1(r).
\]

导数级数由 \((m^2+m)r^m\) 控制，故逐项 mixed differentiation 合法，且常数与 \(n\) 无关。

在外矩形

\[
I_c=[0,471/500],
\qquad
I_a=[17/1000,41/1000]
\]

上，谱隙为 \(\delta=17/1000\)，

\[
r=\frac{983}{1017}.
\]

目标 midpoint 曲线上的角余量及几何和给出精确界

\[
\boxed{|f_{n,aac}(m(c),c)|<4.5\times10^{10}}
\]

对所有 \(n\) 一致成立。精确脚本实际算得右端模板值约 \(4.410084\times10^{10}\)。

## 4. 半密度对称和混合三阶链式法则

令原整数格奇偶规范

\[
D_{jj}=(-1)^j.
\]

半密度 sine 系数在非零偶距离为零、在奇距离经 \(D\) 共轭变号，而对角元为 \(1/2\)，故

\[
DQ_nD=I-Q_n.
\]

这对任意连续主块大小 \(n\) 都成立。若使用任意非连续有限索引集，\(D\) 必须保留原格点奇偶，而不能按子矩阵位置重新编号。

DPP 对角规范不改变主子式，配置补集又是双射，所以

\[
f_n(a,c)=f_n(1-a-c,c).
\]

以 \(a=m(c)+s\) 表示时，函数关于 \(s\) 为偶函数，从而对每个有限 \(n\)

\[
\boxed{f_{n,aaa}(m(c),c)=0.}
\]

定义 balanced curvature

\[
\kappa_n(c)=f_{n,aa}(m(c),c).
\]

由于 \(m'(c)=-1/2\)，

\[
\kappa_n'(c)
=f_{n,aac}(m(c),c)-\frac12f_{n,aaa}(m(c),c)
=f_{n,aac}(m(c),c).
\]

混合三阶的系数和符号正确，没有把 midpoint 对称误用于离开 balanced line 的点。

## 5. 从 \(0.937\) 向右的精确 margin

在 \(c_*=937/1000\) 处，SA02 seed 给出

\[
\kappa_n(c_*)\le-\frac1{50}.
\]

配合上一节响应界，在

\[
c_*\le c\le c_*+3\times10^{-13}
\]

上有

\[
\begin{aligned}
\kappa_n(c)
&\le-\frac1{50}
+(4.5\times10^{10})(3\times10^{-13})\\
&=-\frac{13}{2000}.
\end{aligned}
\]

在 \(c\le c_*\) 一侧，旧 seed 的 \(-1/50\) 更强。因此 \(-13/2000\) 覆盖整个

\[
\frac{37}{40}\le c\le
\frac{937}{1000}+3\times10^{-13}.
\]

量词是所有有限 \(n\)，没有从若干数值规模外推。

## 6. 四阶界与横向增厚

原稿的角坐标四阶求导式给出

\[
\|P^{(4)}\|
\le\frac{16}{\ell^4}
\left[
\frac{D^4+11D^2}{\sigma^4}
+\frac{6D^3+6D}{\sigma^5}
+\frac{15D^2}{\sigma^6}
+\frac{15D}{\sigma^7}
\right]\|P\|.
\]

代入 full-atom Chebyshev 项后，四组几何和系数分别是

\[
16S_3+44S_1,\quad
48S_2+12S_0,\quad
60S_1,\quad
30S_0,
\]

均核验无漏项。

公共外区间取

\[
I_4=[0.0146,0.0483],\qquad
\ell_4=0.0337,\qquad
\delta_4=0.0146.
\]

在全部目标点上，角余量严格大于 \(0.93\)，从而

\[
\boxed{|f_{n,aaaa}(a,c)|<2.3\times10^{15}}
\]

对 \(n\) 一致。利用 midpoint 的 \(f_{aaa}=0\)，Taylor 余项是二次而非线性：

\[
|f_{n,aa}(m(c)+s,c)-f_{n,aa}(m(c),c)|
\le\frac12\|f_{n,aaaa}\|s^2.
\]

对 \(|s|\le10^{-9}\)，横向损失为

\[
\frac12(2.3\times10^{15})(10^{-9})^2
=\frac{23}{20000}.
\]

最终

\[
-\frac{13}{2000}+\frac{23}{20000}
=-\frac{107}{20000}
=-0.00535
<-\frac1{200}.
\]

严格余量只有 \(0.00035\)，但符号和不等式均正确。

## 7. finite chord 到熵率

若 \(a_0,a_1\) 位于同一固定 \(c\) 的目标条带，有限体二阶界给出

\[
f_n(a_t,c)
\ge(1-t)f_n(a_0,c)+tf_n(a_1,c)
+\frac1{400}t(1-t)(a_1-a_0)^2.
\]

\(a_t\) 仍在同一凸区间内。对固定的三个点只取值极限，即得真半密度 sine 熵率的相同强凹弦不等式；不需要导数收敛、交换极限与 Hessian，亦不需要预设熵率可微。

## 8. 接入 S51 bridge 后的 \(\Gamma_c\) 正号

先前 S51 bridge 已独立从 finite chord/value flow 得到

\[
h_c''(s)=-\Gamma_c(s),
\qquad
s=a-m(c),
\]

且 \(\Gamma_c\) 在合法内区间连续。当前续稿先用有限曲率和纯值极限独立证明熵率强凹，再调用该无符号输入的 bridge，因此没有循环依赖。

在开条带 \(|s|<10^{-9}\) 内，强凹弦与 \(C^2\) 给出

\[
h_c''(s)\le-\frac1{200},
\qquad
\Gamma_c(s)\ge\frac1{200}.
\]

原稿直接把结论写到闭条带。两个边界点需要补一句：由先前 bridge 已证的 \(\Gamma_c\) 连续性，从内点取极限即可。因此最终

\[
\boxed{
\Gamma_c(s)\ge\frac1{200}
\quad\text{当}\quad
\frac{37}{40}\le c\le
\frac{937}{1000}+3\times10^{-13},
\quad |s|\le10^{-9}.}
\]

这是同一个完整 actual-law moving-law V14 核的符号，不是 corrected-law 或 frozen-weight 代理量。

## 9. 精确脚本复跑

随附脚本以 `Fraction` 作精确有理断言，复跑通过：

| 项目 | 精确模板核验结果 |
|---|---:|
| \(S_1\) | \(864.801903114187<865\) |
| \(S_2\) | \(50870.700183187459<50871\) |
| \(L_{aac}\) | \(4.410084\times10^{10}<4.5\times10^{10}\) |
| \(M_4\) | \(2.260171\times10^{15}<2.3\times10^{15}\) |
| 最终曲率上界 | \(-0.005350000<-0.005\) |

脚本严格认证这些有理算术、角余量硬编码断言和最终预算。它不独立证明 SA02 seed、值极限、Chebyshev 恒等式、moving-law Boolean-degree 引理、Bernstein 求导公式或 complement symmetry；这些解析项由本报告另行核验。

## 10. 作用域和未完成事项

1. 最终结论继承 SA02 “relative to frozen pair/row identities” 的依赖边界，不是从零开始重证旧 pair/row 体系。
2. 原稿第 170 行用 “eigenvalue interlacing” 解释 \(A_S\) 的谱隙不充分；本报告 §2 给出了 Neumann 补证。
3. complement–gauge 的任意索引集版本必须按原格点奇偶定义 \(D\)；对稿件实际使用的连续 Toeplitz 主块没有问题。
4. 闭条带边界的 \(\Gamma_c\) 不等式需要用已证连续性从开条带取极限；原稿省略了这句话。
5. 结果不达到 \(c=0.95\)，不提供从 \(0.937\) 到 \(1\) 的宏观区间，也不恢复已经被实际 sine 后验反例否定的 componentwise pair ansatz。
6. \(f_{aaa}=0\) 是半密度的特殊对称。固定一般 \(\rho\) 时规范变换联结 \(\rho\) 与 \(1-\rho\)，不能直接推出同一密度函数的三阶消失；全 \(\rho\) 二次增厚仍未证明。
7. 本报告不评价“显著改进”等标题措辞，只认证精确的区间、宽度、曲率常数及其依赖。

最准确的发布表述是：**相对于 SA02 已审 balanced-line seed，S51 续稿严格把所有有限 \(n\) 的真半密度 sine 曲率界打开为一个上端 \(c=0.9370000000003\)、横向半宽 \(10^{-9}\) 的二维条带，并由值极限得到熵率强凹弦，再由先前已审 S51 bridge 得到同一 actual-law V14 核的 \(\Gamma_c\ge1/200\)。该结论不延伸到 \(0.95\)、全高对比度或全密度。**
