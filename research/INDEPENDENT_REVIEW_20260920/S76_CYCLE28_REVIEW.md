# S76 Cycle28 独立数学审查

审查日期：2026-09-20（Asia/Singapore）

## 总裁决

**`VERIFIED_FULL_ORIGINAL / AUTHOR_NUMPY_REPLAYED / D_SECTOR_PAID_ALL_SIZE_ALL_CONTRAST_AT_MIDPOINT / C_X_REMAINS_OPEN / MAIN_TARGET_INCOMPLETE`。**

S76 的主要结构结论成立：在半密度中点，对每个 \(m\ge1\)、每个 \(0<c<1\) 和每个保持 Hamming layer 的双随机通道，equal-pair acceleration 扇区 \(C_D\) 有精确非正表示

\[
C_D=-4mL\eta_J\le0.
\]

Cycle28 可见稿略写成 “direct binary calculation” 的后验方差下界

\[
\eta_J\ge\overline V_W
\]

是承重步骤。本审查先在原假设下独立补全，不需要新增 exterior-minor 假设：对每条相邻 \(y,y^{(i)}\) 边，以真实混合参考

\[
M_{i,y}=\tfrac12(P_y+P_{y^{(i)}})
\]

和其真实输出权重 \(M_{i,y}^W\) 计算，结论归结为 \(\operatorname{atanh}\) 的凸性。Cycle30 收到的 453 行完整原稿已经在 §4 写出同一推导，因而原先的自包含性缺口已经消除；本 PR 保留“审查先独立补全、附件后到”的时间顺序，不把后到原稿倒写成初审依据。

剩余 \(C_X\) 公式、归一化和总曲率预算也正确。S76 只支付了 acceleration 的 \(D\) 扇区，没有证明 \(C_X\) 的所需上界，因而没有证明总凹性。四点 actual cyclic 的 \(\Xi_O/\delta_O\) 发散和阈值反例正确，只否定小的 contrast-independent 点态支付。

Cycle30 又收到并复跑作者 NumPy 源码，`--c 0.95 --max-m 5` 退出码为 0。主表与正文和独立标准库枚举一致；有限差分残差随运行环境有末位差异，但均保持在 \(10^{-9}\) 量级。独立实现还额外核对了 \(\eta_J\ge\overline V_W\) 的真实 posterior weights。

## 分项裁决

| 对象 | 裁决 | 说明 |
|---|---|---|
| 中点 acceleration split | CORRECT_EXACT | pair log-acceleration 求和后系数完全一致 |
| score output-measurable | CORRECT | Hamming-layer preservation 给出 \(|Z|=|T|\) |
| Fisher loss 为零 | CORRECT_EXACT | \(S=X/r\) 是输出函数 |
| \(k\partial_kL=N_yL\) | CORRECT | Walsh degree 与 \(k\)-次数相同 |
| Jeffreys 边能量系数 \(1/4\) | CORRECT | Boolean Dirichlet 对称化恰产生该因子 |
| 输入边能量 \(mkL/2\) | CORRECT | 每条边 \(J=2kL\)，共有 \(m\) 个方向 |
| \(C_D=-8\Delta\mathcal E/k\) | CORRECT | \(C_D=4\partial_\lambda G_0\)、\(\partial_\lambda=-2\partial_k\) |
| \(C_D=-4mL\eta_J\le0\) | CORRECT_ALL_m_c | 适用于全部 \(m\ge1,0<c<1\) 的中点问题 |
| \(\eta_J\ge\overline V_W\) | CORRECT_SELF_CONTAINED_IN_FULL_ORIGINAL | 完整原稿用真实 mixture/reference 和 atanh 凸性证明；初审已独立得到同一推导 |
| \(C_X\) posterior 公式 | CORRECT | covariance 符号与 \(4L\kappa_2\) 系数正确 |
| 总中点曲率公式 | CORRECT | 与 S73 的 input curvature 和 \(G''\) 一致 |
| 剩余 \(C_X\) 预算 | GENUINE_OPEN_OBLIGATION | (5.5) 经 (5.4) 与同一有限模型的中点总凹性等价；“更窄”仅指结构上只剩一个扇区 |
| 四点 \(\Xi/\delta\) 公式 | CORRECT_EXACT | 比值随 \(c\uparrow1\) 发散 |
| 阈值 \(0.5967833208\ldots\) | CORRECT | 由比值大于 1 的代数等价直接得到 |
| 作者 NumPy 表 | REPLAYED_EXIT_0 | 主表复现；有限差分残差仅有平台相关末位差异，量级一致 |
| 全半密度 all-size 总凹性 | INCOMPLETE | 尚缺 actual consecutive-Fourier 的 \(C_X\) 上界 |
| true sine rate / 任意 \(\rho\) | INCOMPLETE | 归一化 bridge、off-midpoint 和一般密度均未闭合 |

## 1. 冻结前提与作用域

初审完整读取 `S76_VISIBLE_RESULT.md` 全部 274 行，正文正常结束于 Files 段，没有截尾。Cycle30 又完整读取后到的 `S76_RESULT.md` 全部 453 行；它补全了 binary posterior-variance 推导和计算执行记录，但没有把未解的 \(C_X\)、rate bridge、off-midpoint 或一般 \(\rho\) 变成已证结论。任务允许采用已经独立审计的 S73/PR62，具体包括：

1. midpoint iid pair source 后接 exterior channel 的精确 law；
2. overlap determinant 与 posterior cumulants；
3. compensated curvature identity；
4. midpoint score output-measurable，Fisher loss 为零；
5. input pair curvature \(m(4L-2/r)\)。

本审查没有把 S73 的 finite cyclic identities 自动升级成 true Toeplitz/Hilbert entropy-rate theorem。

## 2. Acceleration 的 \(X,D\) 分解

中点四格 pair atoms 中，`00,11` 的概率为 \(r\)，一阶导分别为 \(-1,+1\)，二阶导均为 2；`01,10` 的概率为 \(s\)，一阶导为 0，二阶导为 \(-2\)。

令 \(D\) 是 equal-pair 数，\(X\) 是 `11` 数减 `00` 数。总 score 是

\[
S=X/r.
\]

乘积律的 acceleration 等于 score 平方加各 pair log-acceleration：

\[
\begin{aligned}
\mathcal A
&=\frac{X^2}{r^2}
+D\left(\frac2r-\frac1{r^2}\right)
-(m-D)\frac2s\\
&=\frac{X^2-D}{r^2}
+\frac{D-2mr}{rs},
\end{aligned}
\]

其中最后一步使用 \(r+s=1/2\)。正文分解正确。

通道保持每个 Hamming layer，故 \(|Z|=|T|\)，

\[
X=|Y|+|Z|-m=|Y|+|T|-m
\]

由输出 \(O=(Y,T)\) 可测。因此 Fisher-loss 项精确为零，\(G''=C_X+C_D\)。

## 3. Boolean number operator 与 Jeffreys 能量

条件于 \(Y=y\) 的输入密度可写成

\[
P_y(z)=2^{-m}\prod_i(1-k\sigma_i\tau_i).
\]

经过固定通道 \(W\) 后，\(L_k(y,t)=2^mP_y^W(t)\)。在 \(y\) 的 Walsh 展开中，degree-\(d\) 项恰带 \(k^d\)，而

\[
N_y=\tfrac12\sum_i(I-\mathrm{flip}_i)
\]

在该项上乘以 \(d\)。所以

\[
k\partial_kL_k=N_yL_k.
\]

对

\[
I_W=4^{-m}\sum_{y,t}L_k\log L_k
\]

求导，质量导数项求和为零。对每个方向把 \(y\) 与 \(y^{(i)}\) 对称化：

\[
\sum_y(L_y-L_{y^i})\log L_y
=\frac12\sum_y(L_y-L_{y^i})(\log L_y-\log L_{y^i}).
\]

连同 \(N_y\) 自带的 \(1/2\)，得到

\[
kI_W'(k)=\frac14\sum_i\mathbb E_y
J(P_y^W,P_{y^i}^W).
\]

这解释了系数 \(1/4\)。

未处理输入中，相邻 pair 只交换第 \(i\) 个二元分布 \(((1-k)/2,(1+k)/2)\)，其 Jeffreys divergence 是

\[
J(P_y,P_{y^i})=2k\log\frac{1+k}{1-k}=2kL.
\]

因此输入总边能量为 \(mkL/2\)。双向 log-sum 分别收缩两个 KL 项，故 \(0\le\mathcal E_W\le\mathcal E_{id}\)。

## 4. \(C_D\) 的精确支付

令 equal-pair 概率

\[
\lambda=2r=(1-k)/2.
\]

在 pair product law 中，\(D\) 对 \(\lambda\) 的 score 是

\[
\frac{D-m\lambda}{\lambda(1-\lambda)}
=\frac{D-2mr}{4rs}.
\]

对 entropy gain \(G_0=I_{id}-I_W\) 使用一阶 moving-law identity，得到

\[
C_D=4\partial_\lambda G_0.
\]

又 \(\partial_\lambda=-2\partial_k\)，且

\[
k\partial_kG_0=\mathcal E_{id}-\mathcal E_W=\Delta\mathcal E,
\]

所以

\[
C_D=-\frac8k\Delta\mathcal E
=-4mL\eta_J\le0.
\]

这里 \(0<c<1\) 保证 \(k,L>0\)，没有端点的 `0/0` 问题。

## 5. 补全 posterior-variance payment

这是可见稿最需要补写的步骤。

固定一条 oriented edge \((i,y)\)，记

\[
P=P_y,\quad Q=P_{y^i},\quad M=(P+Q)/2,
\]

并始终用未翻转的 \(y\) 定义 \(\zeta=\sigma_i\tau_i\)。因为 \(P,Q\) 只在第 \(i\) 个 binary factor 上相反，\(M\) 下 \(\zeta\) 是公平符号，而且

\[
\frac{dP}{dM}=1-k\zeta,
\qquad
\frac{dQ}{dM}=1+k\zeta.
\]

令

\[
m(t)=\mathbb E_M[\zeta\mid T=t].
\]

通过任意固定 Markov channel \(W\) 后，真实输出参考权重是 \(M^W\)，并有

\[
\frac{dP^W}{dM^W}=1-km(t),
\qquad
\frac{dQ^W}{dM^W}=1+km(t).
\]

因此

\[
J(P^W,Q^W)
=4k\,\mathbb E_{M^W}[m(T)\operatorname{atanh}(km(T))].
\]

输入 Jeffreys 是 \(4k\operatorname{atanh}(k)=2kL\)。逐 edge 的归一化损失为

\[
1-\frac{\mathbb E_{M^W}[m\operatorname{atanh}(km)]}
{\operatorname{atanh}(k)}.
\]

函数 \(\operatorname{atanh}\) 在 \([0,1)\) 上凸且过原点，所以对 \(0\le u\le1\)，

\[
\operatorname{atanh}(ku)\le u\operatorname{atanh}(k).
\]

利用 \(m\operatorname{atanh}(km)\) 的偶性，得到

\[
m\operatorname{atanh}(km)
\le m^2\operatorname{atanh}(k).
\]

故逐 edge 损失至少为

\[
\mathbb E_{M^W}[1-m(T)^2]
=\mathbb E_{M^W}\operatorname{Var}_M(\zeta\mid T).
\]

最后对 \(i\) 和均匀 \(y\) 平均。因为每条输入 edge 的 \(J_{in}=2kL\) 相同，平均后的左边恰是 \(\eta_J\)，右边恰是正文的 \(\overline V_W\)。这证明

\[
\eta_J\ge\overline V_W.
\]

没有把 \(M^W\) 换成 \(P^W\) 或均匀输出权重，也没有把不同 \(y\) 的 reference 混为一个全局 measure。

## 6. \(C_X\)、归一化与剩余义务

给定输出 \(O\)，\(X\) 固定且

\[
D=-X+2B,
\qquad
\operatorname{Var}(D\mid O)=4\kappa_{2,O}.
\]

information density 的隐藏部分是 \(R=\gamma B-\log Z_O\)，\(\gamma=-2L\)。因此

\[
\operatorname{Cov}(D,R\mid O)
=2\gamma\operatorname{Var}(B\mid O)
=-L\operatorname{Var}(D\mid O).
\]

于是

\[
\mathbb E[(X^2-D)R\mid O]
=(X^2-\delta_O)\psi_O+4L\kappa_{2,O},
\]

正文 \(C_X\) 公式和 \(r^{-2}\) 归一化正确。

结合 input curvature 得

\[
H_{out}''=C_X-2m/r+4mL(1-\eta_J).
\]

因此尚缺的不是 acceleration 全项，而是

\[
C_X\le2m/r-4mL(1-\eta_J).
\]

由上一条精确恒等式可见，这个不等式对**同一个给定有限通道**并不是比“中点总凹性”逻辑上更弱的充分条件，而是与 \(H_{out}''\le0\) 精确等价。完整原稿所谓 “strictly narrower obligation” 只能理解为结构性收窄：\(D\) 扇区已经支付，待证式只显式含 \(C_X\)；不能理解成已经得到一个更弱且更容易自动成立的定理。进一步以 \(\overline V_W\) 代替 \(\eta_J\) 的 (5.6) 才是更强的充分条件，并且仍未证明。

所有 `all-size/all-contrast` 量词都只属于：半密度、对称 bias \(a=(1-c)/2\)、Hamming-layer 双随机通道下的 \(D\)-sector theorem。它们不覆盖 off-midpoint、一般密度或 rate bridge。

## 7. 四点 actual-cyclic obstruction

对 \(m=2\) 的真实 cyclic Fourier channel，取 count-one、\(X=0\) 的输出 atom。后验仅有 \(D=2,0\)，权重分别为

\[
\frac{r^2}{r^2+s^2},\qquad
\frac{s^2}{r^2+s^2}.
\]

直接代入 \(\psi\) 与 variance 后，

\[
\frac{\Xi_O}{\delta_O}
=\log\frac{r^2+s^2}{2r^2}.
\]

令 \(x=s/r=(1+k)/(1-k)\)，比值大于 1 等价于

\[
1+x^2>2e.
\]

解得

\[
c>
\sqrt{\frac{\sqrt{2e-1}-1}{\sqrt{2e-1}+1}}
=0.596783320897\ldots.
\]

当 \(c\uparrow1\) 时 \(r\downarrow0\)，比值发散。该反例属于 actual cyclic family，但它只否定 \(\Xi_O\le\delta_O\) 这类点态小系数支付；S73 已证的四点总 curvature 仍为负，与此不矛盾。

## 8. 独立计算与作者附件复现

初审时两个导出附件未下载，因此先另写标准库枚举器：

1. 从前 \(m\) 个 Fourier modes 构造 \(U_m=2(Q_m)_{EO}\)；
2. 计算全部 exterior minors 和 layer channel；
3. 枚举全部 \((Y,Z,T)\) midpoint atoms；
4. 分别计算 \(C_X,C_D,G'',H_{out}''\)；
5. 独立从 edge Jeffreys energies 计算 \(\eta_J\)；
6. 使用每条边自己的 \(M_{i,y}\) 和 \(M_{i,y}^W\) 计算 \(\overline V_W\)。

对 \(c=.95,m=2,3,4,5\)，正文表格全部复现；两种 \(\eta_J\) 算法一致，且每个尺寸都有 \(\eta_J-\overline V_W>0\)。

Cycle30 收到 `s76_checks.py` 后，先检查其只做本地 NumPy 枚举、无网络、子进程、文件写入、动态执行或反序列化，再以 `--c 0.95 --max-m 5` 运行。退出码为 0，作者主表与正文及独立实现一致。`C_D+8 dG/dk` 是浮点中心差分诊断：本次得到的 \(m=3,5\) 数值分别为 `1.264e-09`、`-2.243e-10`，与原稿表中的 `8.2e-10`、`-1.1e-9` 不逐位相同，但同属舍入/步长敏感的 \(10^{-9}\) 残差，不构成主量不一致。作者源码和原始标准输出随本审查归档。

这些运行都只是有限尺寸实现诊断；一般性 inequality 由 §5 的解析推导承担，不能由 \(m\le5\) 浮点表升级得到。

## 9. 精确剩余义务

1. 对 actual consecutive-Fourier \(U_m\) 证明全 \(m\) 的 \(C_X\) 上界。
2. 建立按全部 \(2m\) cyclic sites 归一的 cyclic-to-Hilbert/finite-Toeplitz 二阶响应桥；entropy-value convergence 不可直接求导。
3. 处理 off-midpoint，此时 Fisher loss、\(\gamma'\) 和全部 moving weights 返回。
4. 对任意 \(\rho\) 替换半密度 parity-unitary/Hamming-layer 结构。
5. 公开表述应把 (5.5) 称为“支付 \(D\) 扇区后剩余的结构化义务”，不要让 “strictly narrower” 暗示它在同一有限模型中比中点总凹性逻辑上更弱。

最终状态：**S76 对所有尺寸与对比度严格支付了中点 acceleration 的 equal-pair 扇区，并给出可计算的 posterior-geometric payment；总凹性仍被未解决的 \(C_X\) 扇区阻塞。**
