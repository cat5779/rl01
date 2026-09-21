# S73 Cycle25 独立数学审查

审查日期：2026-09-20（Asia/Singapore）
冻结原件：`C:/Users/UIO/Desktop/20260907/S73_RESULT.md` 与 `s73_checks.py`

## 总裁决

**`VERIFIED_WITH_REQUIRED_INTERFACE_CORRECTION / EXACT_CYCLIC_OBSTRUCTION / DIAGONAL_BASELINE_ONLY / MAIN_TARGET_INCOMPLETE`。**

S73 的主体有限维数学结论通过独立验缝：§2 的无限全偶条件律、§3 的真实循环投影观测律、§4 的重叠行列式与 Poisson–binomial 后验、§5–§6 保留全部移动权重的二阶恒等式、§7 中点 Fisher 损失消失、§8 四点真实循环正增益曲率反例及四点总曲率严格为负，均成立。

§9 的区间计算也成立，但它只把已接受的任意 contraction 基线合法地用于两个**对角**二阶偏导。它不证明 mixed response 的符号，因此不闭合总曲率。§10 把剩余条件写成未归一化的

\[
\partial_{p_e}\partial_{p_o}I(Y;T)\ge -1/100
\]

是不精确的。若总站点数为 \(n\)，正确的实际律接口是

\[
v(a,c)=\lim_{n\to\infty}\frac1n
\partial_{p_e}\partial_{p_o}I_n(p_e,p_o)\Big|_{p_e=p_o=p}
\ge -\frac1{100},
\]

其中极限及其与真实 sine 熵率二阶响应的对应必须由已接受的 QWE09 固定正谱隙接口提供。对 \(2m\) 点 cyclic 模型，形式上应除以 \(2m\)，而且还需另证 cyclic-to-Hilbert/Toeplitz 的二阶响应桥；不能把单个未归一化 cyclic mutual information 的下界直接代入。

这项修正不推翻 §2–§9 的已证定理，因为原稿 §9 已把需要的量写成归一化极限 \(v=-\lim H_{st}/n\)，最终分类也把 \(v\ge-1/100\) 列为 `INCOMPLETE`。但它是后续桥接必须修正的量词，不能按 §10 的字面式认证。

全区间 \((0.925,1)\)、任意密度 \(\rho\) 以及真实无限 sine 熵率凹性仍未闭合。

## 分项裁决

| 审查对象 | 裁决 | 关键理由 |
|---|---|---|
| §2 有限/无限全偶条件律 | CORRECT | 构造的是可测随机条件核，不是对指定零概率无限字条件化 |
| 半密度 sine 的奇偶块酉性 | CORRECT | \(Q_{EE}=Q_{OO}=I/2\)，投影恒等式给出 \(UU^*=U^*U=I\) |
| 观测后的条件核 \(M_y\) | CORRECT | 后验逐坐标独立，谱 Bernoulli 参数平均后恰为所给 \(q_0,q_1\) |
| §3 真实 cyclic law | CORRECT | 先采样谱子集再经 \(|\det U_{z,t}|^2\) 外幂通道，正是投影 DPP 的谱采样 |
| 外幂通道双随机 | CORRECT | 每个 Hamming 层的行、列和分别由两侧 Cauchy–Binet 等于 1 |
| §4 重叠行列式 | CORRECT | 直接对 \(U^*D_y(\gamma)U\) 使用 Cauchy–Binet |
| 条件重叠 Poisson–binomial | CORRECT | 条件概率母函数分解为 \(\prod_j(1-r_j+r_je^\tau)\) |
| §5 相对熵表示 | CORRECT | 列随机性使 \(\widetilde J\) 归一，似然比为 \(P_a/Q_a\) |
| §6.1 全支付恒等式 | CORRECT | 熵二阶式给出 acceleration 项与条件 Fisher 损失，未冻结权重 |
| §6.2 cumulant 展开 | CORRECT | \(A\) 对输出可测，\(B,B^2\) 的条件协方差项全部保留 |
| §7 中点 Fisher 损失 | CORRECT_EXACT | 分数 \(S=(|Y|+|Z|-m)/r\) 由 \((Y,T)\) 可测，条件方差恒为 0 |
| §8.1 四点 \(G''>0\) | VERIFIED_EXACT | 正号化为整数比较 `84286283041 > 880843041` |
| §8.2 四点总曲率 | CORRECT_ALL_C | 对每个 \(0<c<1\)，两条严格对数不等式给出负上界 |
| §9 \(37/40<c\le74/77\) | CORRECT_DIAGONAL_ONLY | \(b<3/40\)、\(\alpha\le37/40\) 恰好允许逐 mask 调用对角基线 |
| “全合法偏置” | POINTWISE_ONLY | 每个内点可置于固定正 gap 紧区间；没有端点一致误差或闭区间结论 |
| §10 mixed-MI 式 | REQUIRES_CORRECTION | 缺少除以 \(n\)、极限和 actual-law/cyclic 桥接 |
| 半密度全尺寸总曲率 | INCOMPLETE | 尚无 \(v\ge-1/100\) 或直接 common-direction 证明 |
| \(c>74/77\) | INCOMPLETE | 近合法端点 \(\alpha>37/40\)，旧对角基线不可用 |
| 任意 \(\rho\) | INCOMPLETE | 奇偶对角块不再是 \(I/2\)，本稿的酉分解不适用 |

## 1. 冻结范围与依赖

本审查完整读取 867 行原稿和 192 行程序。文件完整结束于 §12，不存在截尾。哈希、环境和原始输出见 `S73_CYCLE25_SOURCE.md` 与 `S73_CYCLE25_REPLAY.md`。

允许使用的已审输入只有：

1. QWE09 PR57 已审的固定正 gap 二阶响应接口；
2. 同一审查中明确接受的 S55 任意 contraction 对角基线；
3. S71 PR60 只作范围对照，没有被当作 S73 的证明步骤。

本审查没有把 cyclic 投影自动等同于 finite Toeplitz compression，也没有从有限数值曲率推出无限熵率符号。

## 2. §2：无限全偶条件律

令

\[
Q=\frac12\begin{pmatrix}I&U\\U^*&I\end{pmatrix}.
\]

由 \(UU^*=U^*U=I\) 可直接验得 \(Q^2=Q\)。限制核 \(Q_{EE}=I/2\)，所以 \(X_E\) 是 iid 公平 Bernoulli。

对任意有限 \(A\subset E,B\subset O\)，构造的条件核

\[
P_x=U^*\operatorname{diag}(1-x)U
\]

给出

\[
\mathbb E\!\left[\prod_{i\in A}X_i\det(P_X)_B\right]
=2^{-|A|-|B|}\det(I_B-U_{A,B}^*U_{A,B}),
\]

这与 \(\det Q_{A\cup B}\) 一致。无限和绝对收敛：每个矩阵元是两个 \(\ell^2\) 列的乘积和，可由 Cauchy–Schwarz 控制；有限主行列式因此是坐标可测函数。离散可数配置空间是标准 Borel 空间，有限 cylinder 相关函数确定联合律，故该 Markov kernel 是一个正则条件律版本。

应保持原稿已有的限定：在无限情形，条件律恒等只要求几乎处处成立；这并非声称固定无限字 \(x\) 的事件有正概率。作者对此处理正确。

半密度 sine 投影中，同奇偶非对角项为零而对角为 \(1/2\)，所以投影块恒等式确实令 \(U=2Q_{EO}\) 成为酉算子。

观测 \(Y_E=y\) 后，潜变量后验仍逐坐标独立。再对 odd projection 做噪声谱采样，积分掉后验潜变量后各谱坐标仍独立，其参数分别为

\[
q_1=p-\frac{c^2}{4p},\qquad
q_0=p+\frac{c^2}{4(1-p)}.
\]

因此

\[
M_y=bI+\alpha U^*\operatorname{diag}(1-y)U
\]

成立。这里用的是“共同特征基下独立谱 Bernoulli 的混合”，不是一般 DPP 混合仍为 DPP 的错误断言。

## 3. §3–§4：cyclic law、外幂通道与后验

给定 even 潜字 \(x\)，odd 噪声 DPP 的特征向量为 \(U\)，特征值为 \(a+c(1-x_i)\)。标准谱采样先生成独立 \(Z_i\)，随后投影 DPP 在空间基上产生 \(T\)，条件概率正是

\[
W_U(z,t)=|\det U_{z,t}|^2\mathbf 1_{|z|=|t|}.
\]

对固定 \(t\) 或固定 \(z\) 使用 Cauchy–Binet，均得到 Hamming 层内和为 1，所以通道逐层双随机。平均 iid 公平 \(x_i\) 后，\((Y_i,Z_i)\) 的四格表为 \((v,q,q,u)\)，且直接展开得到

\[
uv-q^2=-c^2/4.
\]

这证明 Theorem 3.1 对真实 \(2m\) 点 cyclic projection 成立。

把四格权重写成 \(v^m e^{\theta A+\gamma B}\)，再利用 \(|Z|=|T|\)，输出 atom 中只有隐藏重叠 \(B=|Y\cap Z|\) 需要求和。Cauchy–Binet 给出

\[
Z_{y,t}(\gamma)=\det(I_t+(e^\gamma-1)(U^*P_yU)_{t,t}).
\]

压缩矩阵的特征值在 \([0,1]\)，故条件概率母函数逐因子分解，重叠确为独立 Bernoulli 和。\(|\kappa_3|\le\kappa_2\) 逐项来自 \(|1-2r_j|\le1\)。

## 4. §5–§6：相对熵和全部移动权重

定义 \(J=P_aW_U\)、\(\widetilde J=Q_aW_U\)。对每个输出列求和为 1，因此 \(\widetilde J\) 是概率律；在 \(J>0\) 的支撑上 \(\widetilde J>0\)，似然比为 \(P_a/Q_a\)。于是

\[
G=H(Q_a)-H(P_a)=D(J\Vert\widetilde J).
\]

对任意正有限律，

\[
H(P_a)''=-\mathbb E[\mathcal A\log P_a]-\mathbb E[S^2].
\]

输出 score 与 acceleration 分别是输入量的条件期望。相减后正好得到

\[
G''=\mathbb E[\mathcal AR]+\mathbb E\operatorname{Var}(S\mid O).
\]

这一步没有把权重、归一化或 acceleration 冻结。

进一步写 \(S=C_1+\gamma'B\) 后，Fisher 项为 \((\gamma')^2\mathbb E\kappa_2\)。将

\[
\mathcal A=(C_1+\gamma'B)^2+C_2+\gamma''B
\]

与 \(BR,B^2R\) 的条件矩配对，可逐项恢复 Theorem 6.2 的 \(\psi,\kappa_2,\kappa_3\) 系数。没有发现少一项、系数错号或把移动 mask 当常量的问题。

## 5. §7：中点的零 Fisher 损失和未支付项

在 \(a=(1-c)/2\) 时，\(u=v=r,q=s\)，且 \(\gamma'=0\)。每个 pair 的 score 在 `00,01,10,11` 上分别为 \(-1/r,0,0,1/r\)，所以

\[
S=(|Y|+|Z|-m)/r.
\]

通道保持 \(|Z|=|T|\)，故 \(S\) 已由输出 \((Y,T)\) 决定，

\[
\operatorname{Var}(S\mid O)=0
\]

是精确恒等式，不是数值近零。

与此同时

\[
\gamma''=-\frac{64c^2}{(1+c^2)(1-c^2)^2}<0,
\]

因此剩余 acceleration/overlap 项确为

\[
\mathbb E[\overline{\mathcal A}\psi]+\gamma\gamma''\mathbb E\kappa_2.
\]

第二项非负，第一项没有点态符号。S73 正确地把它列为未支付量；数据处理或 Fisher 损失本身不能闭合。

## 6. §8：四点 exact obstruction 与总曲率

当 \(m=2\) 时，Hamming-one 通道是均匀 \(2\times2\) 双随机矩阵。只有 \(y=01,10\) 的原子被改变；输入原子是 \(r^2,s^2\)，输出原子均为 \(C=(r^2+s^2)/2\)。中点一阶导为零，三种原子的二阶导均为 \(-4s\)。因此

\[
G''=8s\log\frac{(r^2+s^2)^2}{4r^2s^2}>0.
\]

在 \(c=19/20\) 时，正号完全归结为

\[
84286283041>880843041.
\]

作者程序和独立标准库程序均复现该整数证书。它只反驳“外幂通道熵增关于 \(a\) 凹”以及“Fisher 损失单独支付余项”，不反驳总熵凹性。

总四点曲率令 \(x=s/r>1\) 后为

\[
8\log x-8(1+x)+\frac{8x}{1+x}
\log\frac{x^2+1}{2x}.
\]

因 \((x^2+1)/(2x)<x\) 且

\[
\log x<\frac{x-x^{-1}}2\quad(x>1),
\]

它严格小于 \(-8-8/x<0\)。这覆盖每个 \(0<c<1\)，不是网格实验。

## 7. §9：区间、偏置量词与只闭合对角项

利用半密度补对称，只需 \(p\in(c/2,1/2]\)。函数

\[
b(p)=p-\frac{c^2}{4p}
\]

递增，因此

\[
0<b(p)\le(1-c^2)/2<3/40
\]

在 \(c>37/40\) 成立。又因 \(p(1-p)\) 在该区间递增，

\[
\alpha(p)=\frac{c^2}{4p(1-p)}<\frac{c}{2-c}.
\]

其端点上确有

\[
\frac{74/77}{2-74/77}=\frac{37}{40}.
\]

所以 \(37/40<c\le74/77\) 恰好保证全部合法内点的 \(\alpha\le37/40\)。固定 even shift，只对 odd shift 求二阶导时，even mask 权重、\(\alpha\) 和 \(R_y\) 不动，只有 scalar shift 以斜率 1 移动；逐 mask 调用基线合法。交换奇偶同理。

由此只得到

\[
H_{ss}+H_{tt}\le-n/50,
\]

以及

\[
h''\le-1/50-2v.
\]

它没有给出 \(v\) 的下界。所谓“全部合法偏置”是参数代数覆盖全部开区间内点；QWE09 响应传递仍是固定正 gap 的局部/紧区间论证，不产生靠近端点的一致误差界。

## 8. §10 的正确归一化接口

对于 finite actual-law 窗口，若 \(I_n\) 表示两块观测的未归一化 mutual information，则

\[
H_{n,st}=-\partial_{p_e}\partial_{p_o}I_n.
\]

因此 QWE09 中的量应写成

\[
v(a,c)=\lim_{n\to\infty}\frac1n
\partial_{p_e}\partial_{p_o}I_n.
\]

基线范围的充分条件是这个**每站点极限**不小于 \(-1/100\)。若使用 \(2m\) 点 cyclic 信息 \(I_{m,U_m}\)，相应候选条件是

\[
\liminf_{m\to\infty}\frac1{2m}
\partial_{p_e}\partial_{p_o}I_{m,U_m}\ge-1/100,
\]

并且还必须证明该 cyclic 极限就是真实 Hilbert/Cauchy 或 Toeplitz actual-law mixed response，或给出显式可支付的二阶误差。Theorem 2.1 的无限条件律只确定条件分布，不能替代无限熵及其二阶导的极限交换。

因此 §10 的未归一化式不能作为已成立的统一 \(n\) 结论，也不是 §9 的直接推论。

## 9. 计算复现与证据等级

作者检查器经安全审查后原样执行，退出码 0。它复现：

- 四点整数比值和 \(G''>0\)；
- \(c=.95\) 时 \(m=1,2,3,4\) 的 cyclic 枚举；
- 中点 Fisher 项为数值零；
- off-midpoint 恒等式残差约 \(2.1\times10^{-13}\)。

独立检查程序不复制作者枚举器，使用标准库有理数和 80 位 Decimal：

- 对一个有理 \(2\times2\) 酉矩阵逐项核对 16 个 inclusion-correlation 恒等式；
- 精确核对外幂通道行列和；
- 从二阶 jet 重建四点证书；
- 精确核对 \(b(1/2;37/40)=231/3200<3/40\) 和 \(\sup\alpha(74/77)=37/40\)。

网格上的全 \(c\) 负曲率仅作实现诊断；一般性结论依赖 §8 的解析不等式。

## 10. 精确剩余义务

1. 在 \(37/40<c\le74/77\) 上，证明真实 actual-law 的每站点 mixed response \(v(a,c)\ge-1/100\)，并明确是逐内点还是在给定紧子区间上一致。
2. 若从 cyclic overlap functional 出发，证明按总站点数归一的二阶响应极限，并建立到 Hilbert/Cauchy 条件律或 finite Toeplitz actual-law 的可微桥；有限熵值近似不足够。
3. 对 \(c>74/77\)，另证可覆盖近合法端点的对角 contraction 基线，或直接证明 common-direction 总曲率。
4. 对任意 \(\rho\)，替换半密度特有的 \(I/2\) 奇偶块和酉外幂表示。
5. 保持结论边界：四点 cyclic total curvature 只证明中点和四站点；它不是全尺寸或全偏置定理。

最终状态：**S73 提供了正确的结构展开和一个精确机制反例，并扩展了旧对角基线的合法参数覆盖；它没有解决真实 sine 熵率的全尺寸符号。**
