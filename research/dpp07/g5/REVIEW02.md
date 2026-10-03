# 独立对抗性数学审查

STATUS: CORRECT

## 裁决

在文中明确限定的量词与结论范围内，R、N、J 以及推论 H、法则层结论 L 的承重证明链可以闭合。未发现需要补充新前提、弱化结论或修改量词的关键缺口。

裁决只覆盖文中实际声称的范围：N 对每个固定 \(K,L\) 和每个 \(\eta>0\) 给出近最优相对转移；L 只给出不要求 iid 表示的不变单调 joining；J 只覆盖 \(B-A\in\mathcal C\) 且 \(B-A\ge\delta I>0\) 的 ordered pair。证明没有把一般 ordered pair 的 exact joint-iid 当作已证，也没有从 N 的 \(\eta>0\) 结论直接推出 \(\eta=0\) 的同一映射。

## 1. R：全边界条件核与平均敏感度

由

\[
K-P_{x^c}=\tfrac12J_x[I+J_x(2K-I)]
\]

及 \(\|2K-I\|\le1-2\epsilon\)，Neumann 级数给出对所有 \(x,t\) 一致的可逆性和

\[
\|(K-P_{x^c})^{-1}\|\le\epsilon^{-1}.
\]

同一个一致几何级数给出固定向量上的连续性。有限边界的占用和空置条件化分别由 Schur complement 的负、正秩一更新表示；对 \(K\) 与 \(I-K\) 同时应用 Schur complement，可保持

\[
\epsilon I\le N_F(x)\le(1-\epsilon)I.
\]

有限截断中的投影在 Neumann 级数每一固定阶出现的紧向量族上一致收敛，级数尾则一致几何衰减。因此有限条件核在固定向量上一致趋于所写的全边界核。有限条件期望的鞅收敛把该核识别为所需的条件 DPP；这里只需在原 DPP 下几乎处处识别，公式本身为所有边界配置提供连续且有隙的延拓。

一次外部翻转的 Sherman–Morrison 更新为秩一项。其分母是相应单点条件概率或其补，绝对值至少为 \(\epsilon\)；Schur 向量中的有限块因子范数至多一。故

\[
\left|\operatorname{tr}\!\left(N_F(x^j)-N_F(x)\right)\right|
\le\epsilon^{-1}\sum_{s\in F}|G_x(s,j)|^2.
\]

对平移块 \(gS\) 按重数求和时，每个坐标在恰好 \(|S|\) 个块中出现，所以公共配置处的列和至多

\[
|S|\epsilon^{-1}\|G_x\delta_j\|_2^2
\le |S|\epsilon^{-3}.
\]

由于 \(G_x\) 是 Hermitian，固定行的远尾等于相应列向量的远尾；紧集

\[
\{G_{t,x}\delta_s:(t,x)\in[0,1]\times\{0,1\}^{\Gamma}\}
\]

在 \(\ell^2\) 中具有一致小的坐标尾。于是可先在有限坐标集上使用翻转生成元，再放大有限集。

把 \(L\le U\) 的每个分歧以独立 rate-one 时钟从 \(L\) 翻到 \(U\)。插值时刻 \(r\) 尚未翻转的根分歧密度为 \(de^{-r}\)。质量传输把“根块对所有待翻坐标的行和”改写成“根待翻坐标对所有平移块的列和”；上面的共同配置列界遂给出

\[
\mathbb E\operatorname{tr}(N_S(L)-N_S(U))
\le |S|\epsilon^{-3}d.
\]

这一步没有把逐配置 supremum 分别求和，因而保留了因子 \(d\)。

## 2. R：Lipschitz 正流与共同钟夹逼

有限 DPP 的算子序随机支配说明导数向量 \(b_N\) 位于所有向上 Boolean-cube 边 incidence columns 生成的闭多面锥中。对任一向上边列 \(e\)，

\[
m(e)=\sum_\eta|\eta|e(\eta)=1,
\]

而 \(m(b_N)=\operatorname{tr}(vv^*)=\|v\|^2\)。故锥的 \(m=1\) 截面正是有限边列的凸包。对其作有限三角剖分，在顶点选取非负可行流并作分片仿射延拓，再沿射线齐次延拓，得到全锥上的 Lipschitz 非负右逆。连续条件概率逐步分解且每一步落在 \([\epsilon,1-\epsilon]\)，因此

\[
p_N(\eta)\ge\epsilon^{|S|}.
\]

所以 \(q_N(\eta,i)/p_N(\eta)\) 一致有界并对 \(N\) Lipschitz。

每个站点只属于有限多个平移块，故总 birth rate 有界、连续且等变。区间 \([L,U]\) 内任意两配置的条件核都夹在端点条件核之间。若 \(E\) 是二者之差、\(D=N_S(L)-N_S(U)\ge0\)，则 \(-D\le E\le D\)；从 \(E\) 的正负谱子空间分别取迹得到

\[
\|E\|_1\le\operatorname{tr}D.
\]

结合有限块内的 pattern 分歧与上一节的平均条件核界，得到

\[
\mathbb E(a_e^+-a_e^-)
\le c\,\mathbb P(L_e\ne U_e).
\]

共同 Poisson marks 的上下包络迭代具有路径序单调性：lower 接受阈值 infimum 以下的 mark，upper 接受 supremum 以下的 mark。每站点在有限时间内只有有限 marks，所以每个 mark 的 lower/upper 决策分别单调稳定；紧性把区间 extrema 传到极限。两极限首次分离只能发生在两阈值之间的 mark，补偿公式与上式给出

\[
d(t)\le c\int_0^t d(s)\,ds,
\]

因而 \(d(t)=0\)。逐站点、逐有理时刻再结合有限跳跃性，得到整条路径的几乎处处合并。

对 nonadapted relaxed solution 不需增加可预测性。这是逐路径的序夹逼：若上一轮已有 lower \(\le Z\le\) upper，则 \(Z\) 的自身阈值位于区间 infimum 与 supremum 之间；严格低于 infimum 的 mark 必须被 \(Z\) 接受，严格高于 supremum 的 mark 必须被拒绝，相等处任意选择仍不破坏夹逼。归纳后 \(Z\) 被所有包络轮次夹住，包络合并即强制其等于唯一极限。

## 3. R：边缘识别、共同输入收敛与可测性

对支撑于 \(gS\) 的扰动 \(h v_gv_g^*\)，外部压缩不变，而全边界条件核恰增加同一秩一矩阵。因此有限流的 divergence 恒等式可以在条件分布中使用。对柱函数只有有限多个平移块相交，故求和有限，并得到

\[
\partial_t\mu_{K_t}(f)=\mu_{K_t}(\mathcal L_t f).
\]

对有限 \(\Lambda\)，条件平均率 \(\widehat a_i^\Lambda\) 给出有限状态纯生链的精确 Kolmogorov 方程；有限 ODE 的唯一性确定其时刻 \(t\) 的 law 为 \(\mu_{K_t}|_\Lambda\)。若两个配置在 \(\Lambda\) 上一致，则条件平均率位于原 rate 在该 cylinder 上的最小值与最大值之间。紧空间上的一致连续性因此给出：沿 exhaustion，对每个固定站点与匹配输入，\(\widehat a_i^\Lambda-a_i\) 一致趋零。

在同一初始配置和同一组站点时钟上运行有限链，并冻结外部坐标。任一子列都可由逐坐标有限 clock lists 抽出整路径收敛的子子列。阈值的一致逼近说明该极限是 relaxed solution；共同钟唯一性又迫使它等于包络解。于是所有 exhaustion 而非仅一条子列都在共同输入上收敛。有限链的精确边缘给出极限的全部包含概率，inclusion–exclusion 再识别完整 DPP 边缘。

包络迭代、有限链、逐坐标稳定和失败回退都由可数次 Borel 运算组成；成功集由逐坐标和有理时刻条件刻画，故为 Borel 且平移不变。R 的异常输入回到初始常路径，仍在每个输入上保持 pure-birth order。

有限范围包络的祖先链数由

\[
O((M|W_m|)^n/n!)
\]

控制，故局部构造几乎处处只有有限祖先。局部 rate 区间比完整区间至多多 \(2\omega_m\)，Gronwall 与产生分歧的 marks 计数给出

\[
\mathbb P(L_e^m\ne U_e^m\text{ as paths})
\le \frac{2(e^c-1)}c\,\omega_m,
\]

其中 \(c=0\) 取连续延拓值 \(2\)。选取可和的 \(\omega_{m_k}\) 因而给出同输入的实际路径逼近，而不只是分布收敛。

## 4. N：有隙接口、强逼近与奇异端点

若 \(D\in\mathcal C\) 且 \(D\ge\delta I\)，对 residual \(R_n\) 以有限支撑 \(T_n\) 逼近 \((R_n/2)^{1/2}\)，使

\[
\|T_nT_n^*-R_n/2\|\le\min\sigma(R_n)/4.
\]

因为 \((\min\sigma R_n)I\le R_n\)，可得

\[
R_n/4\le T_nT_n^*\le3R_n/4,
\qquad
R_n/4\le R_{n+1}\le3R_n/4.
\]

所以 increments 严格正、residual 以范数几何趋零，且每一步 R 所需的整个路径保持有隙。单调合成的根变化概率等于强度差 \(\tau D\)。对 \(D=D_+-D_-\in\mathcal C\)，中介

\[
C_j\le C_j+D_+/n+\beta I\ge C_{j+1}
\]

的两条正 increments 均属于 \(\mathcal C\) 且由 \(\beta I\) 严格正；取细分足够细可保持统一 gap。所有步骤的根成本为 \(\tau|D|+2n\beta\)。

对一般 self-adjoint \(D\)，有限卷积截断 \(S_m\) 在有限支撑向量上趋于 \(D\)。恒等式

\[
(S_m-i)^{-1}(D-i)u-u=(S_m-i)^{-1}(D-S_m)u
\]

以及 resolvent 的一致界，先在稠密集、再在全空间给出强 resolvent 收敛；\(-i\) 同理。取紧支撑连续实函数 \(f\)，使其在 \(D\) 的谱区间上等于 identity 且 \(|f|\le\|D\|\)，便得到

\[
D_m=f(S_m)\in\mathcal C,\qquad
D_m\to D\text{ strongly},\qquad
\|D_m\|\le\|D\|.
\]

共同紧谱区间上的多项式逼近还给出 \(|D_m|\to|D|\) strongly，故正规迹满足 \(\tau|D_m|\to\tau|D|\)。这补足了初始近似成本的极限。

选取子列使

\[
\|(D_m-D)\delta_e\|\le e_m,\qquad \sum_m e_m<\infty.
\]

由有限迹 Cauchy–Schwarz，

\[
\tau|E|\le\|E\delta_e\|_2,
\]

所以相邻接口的根失配被 \((e_m+e_{m+1})/n+\zeta_m\) 控制。可和失配与 Borel–Cantelli 说明每个坐标只改变有限次；群可数，故所有坐标同时稳定。\(H_m\to C_{j+1}\) strongly 意味着每个有限压缩收敛，有限 determinants 因而识别稳定极限的 law。这个论证给出实际同输入极限与 Borel 映射，不只是 coupling laws 的弱极限。

奇异端点处，逐位以概率 \(s\) 翻转确实把 inclusion probabilities 变为

\[
\det(sI+(1-2s)K)_F,
\]

故得到有隙核 \(K_s\)，且根成本恰为 \(s\)。从 \(K_s\) 到 \(L_s\) 使用已证有隙接口；随后沿 \(s_m\downarrow0\) 的接口总成本不超过

\[
s\,\tau|I-2L|+\sum_m\zeta_m
\le s+\sum_m\zeta_m.
\]

同一可和失配论证给出实际逐坐标稳定，并以有限 determinants 识别 \(\mu_L\)。合并三段成本并令 \(s\) 与 allowances 足够小，正好得到 N 的

\[
\mathbb P(X_e\ne Y_e)\le\tau|K-L|+\eta
\]

对每个固定 \(\eta>0\) 的陈述。稳定失败集为不变 Borel 零集，在其上回到初始配置不改变 law 或成本结论。

## 5. H、L 与受限 exact J

在 N 中取 \(K=0\) 与确定的空初始配置，就得到每个固定正压缩核的 total Borel equivariant iid sampler H；这里没有循环使用 H。

若 \(A\le B\)，N 给出 exact marginals 且

\[
2\mathbb P(X_e=1,Y_e=0)
=\mathbb P(X_e\ne Y_e)-\tau(B-A).
\]

让 N 的 allowance 趋零，并只对这些不变 joint laws 取弱极限。根处逆序事件是 clopen，极限概率为零；不变性再把这一点传到每个坐标，可数并集给出 \(X\subseteq Y\) 几乎处处。这证明的是 law-level L，没有声称弱极限仍为 joint iid factor。

最后设 \(D=B-A\in\mathcal C\) 且 \(D\ge\delta I\)。由 \(B\le I\) 得 \(A\le(1-\delta)I\)，由 \(A\ge0\) 得 \(B\ge\delta I\)。因此对 \(0<\epsilon_0<\delta/2\)，两核 \(A+\epsilon_0I\) 与 \(B-\epsilon_0I\) 都是有隙正压缩，且它们之差

\[
D-2\epsilon_0I\in\mathcal C,\qquad
D-2\epsilon_0I\ge(\delta-2\epsilon_0)I>0.
\]

H 先采样 lower，严格正 reduced-algebra interface 再单调生成 upper。沿任意严格递减 \(\epsilon_n\downarrow0\)，在 lower 的补配置上增加 \((\epsilon_n-\epsilon_{n+1})I\) 等价于缩小 lower；在 upper 上增加同一 scalar increment 等价于扩大 upper。每步端点都有各自正 gap，并在每个输入上保持

\[
X_{n+1}\subseteq X_n\subseteq Y_n\subseteq Y_{n+1}.
\]

两条逐点单调序列对所有输入都有极限；有限 determinants 分别趋于 \(A\) 与 \(B\) 的 determinants。初始 H、基准 monotone interface 及可数个 scalar interfaces 可编码在一份 regular iid 输入中，其逐点极限仍为 Borel 等变函数。因此 J 在所写严格正 reduced-algebra difference 条件下成立，并允许 \(A\) 在零端或 \(B\) 在一端奇异。

## 6. 边界核对

- 空支撑或 \(T=0\) 时，所有 rates 为零，R 退化为常路径；正流在原点取零与此一致。
- 群只要求可数离散；所有 exhaustion、坐标交和稳定事件均为可数操作。
- 文中所有强极限均通过有限压缩 determinants 识别 DPP law，没有把强算子收敛误当作算子范数收敛。
- 所有无限合成都以可和根失配和不变性推出逐坐标稳定；没有只凭边缘弱收敛定义相对映射。
- exact J 的严格正差保证中间移位核有隙；不需要端点本身有统一 gap。

综上，省略的步骤均可在原前提内补全，裁决为 CORRECT。
