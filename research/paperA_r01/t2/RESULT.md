# Lyons ICM 2014 Conjecture 5.7：支配界、两种“最优”语义与边界

四条主线的英文数学稿见 [paperA.md](../t1/paperA.md)，其中 §§5–7 与附录 B–C 对应本题及新增的 sofic 尖锐非交换距离界。新增专项复核见 [prob01.md](prob01.md) 与 [dbar01.md](dbar01.md)；本文件保留题 2 的完整专题证明。

日期：2026-10-02

## 结论先行

令 \(\Gamma\) 为可数群，\(Q\in R(\Gamma)\) 是作用在
\(\ell ^2(\Gamma)\) 上的复 Hermitian 正压缩，\(\mu_Q\) 为对应 DPP。写

\[
 \tau(T)=\langle T\delta_e,\delta_e\rangle,
 \qquad
 D(Q)=\exp\tau(\log Q),
\]

其中 \(\exp(-\infty)=0\)。定义普通随机序阈值

\[
 p_-(Q)=\sup\{p:\operatorname{Ber}(p)^\Gamma\preceq\mu_Q\},
 \qquad
 p_+(Q)=\inf\{p:\mu_Q\preceq\operatorname{Ber}(p)^\Gamma\}.
\]

本报告核验得到：

| 主张 | 状态 | 精确结论 |
|---|---|---|
| FK 双侧支配界 | **PROVED** | 对任意可数群，\(D(Q)\le p_-(Q)\) 且 \(p_+(Q)\le1-D(I-Q)\)。不需要 sofic。 |
| 固定 \(Q\) 的逐点最优性 | **DISPROVED** | 在原文 sofic 范围内已有 \(\Gamma=C_3*C_3\) 的投影核满足 \(D(Q)=0<p_-(Q)=1/2\)；其补核给出严格上界反例。 |
| 只依赖各自一个 FK 数值的类上一致最优性 | **PROVED** | 对每个 \(d\in[0,1]\)，标量核 \(Q=dI\) 阻止把下界 \(D(Q)=d\) 一致提高；同一标量核阻止把上界 \(1-D(I-Q)=d\) 一致降低。 |
| 有限群上的逐点最优性 | **PROVED** | \(p_-(Q)=D(Q)\)，\(p_+(Q)=1-D(I-Q)\)。 |
| 可数 amenable 群上的逐点最优性 | **PROVED** | 同上，包括 \(D(Q)=0\)、非满秩和其他奇异端点。 |
| 任意可数群上哪些固定核取等号 | **INCOMPLETE** | 非 amenable 情形没有一般分类；有限压缩行列式增长与 FK 之间的间隙是明确障碍，但它还不是随机序的完整刻画。 |
| \(R(\Gamma,S)\) 的自然非归一化 trace 版本 | **PROVED** | 对 \(\Delta_S(Q)=\exp\tau_S\log Q\) 有同形双侧支配；它在算子类上分别一元锋利，但通常不逐点最优。 |
| 把每坐标归一化 FK 直接搬到多轨道 | **DISPROVED** | 平凡群上的 \(\operatorname{diag}(1/4,3/4)\) 已同时破坏两边。 |

因此，Conjecture 5.7 若把 “optimal” 理解为“每个固定 \(Q\) 的最佳 Bernoulli
参数”，则其**支配部分成立，而最优性部分为假**；若只理解成“所写的一元 FK
函数在整个算子类上不可一致改进”，则该较弱版本成立。

## 1. 原文语义

Lyons 的 ICM 文章在 §5.2 开头把 \(\Gamma\) 置于 sofic 群语境；Conjecture 5.7
随后对 \(\ell^2(\Gamma)\) 上所有等变正压缩写出两条 FK 支配界，并在同一句末尾
说这些界最优。原文没有形式定义这里的“最优”。

### 1.1 两个不同命题

**逐点语义（P）。** 对每个固定 \(Q\)，

\[
 p_-(Q)=D(Q),\qquad p_+(Q)=1-D(I-Q).                 \tag{P}
\]

**类上一致语义（U）。** 对所有核都有效的、只使用所显示单个 FK 数值的下界
\(D(Q)\) 不能一致提高；相应的一元上界不能一致降低。这里不声称一个同时依赖
\((D(Q),D(I-Q))\) 的二元改进不存在；那是另一个问题。

### 1.2 哪个更接近原文

**结论：逐点语义更可能，但不能把未写出的作者意图当成定理。** 理由是：

1. Conjecture 5.7 明说它要推广紧邻的 Theorem 5.2。
2. 该 abelian 先例在 Lyons--Steif Theorem 5.11 中是对每个固定符号 \(f\) 的
   充要条件：下阈值恰为 \(\operatorname{GM}(f)\)，上阈值恰为
   \(1-\operatorname{GM}(1-f)\)。
3. ICM Theorem 5.2 对这一逐符号结论使用了相同的“最优”措辞。

所以（P）是最自然的延伸读法，而（U）是较弱且几乎由标量核立即封口的读法。

## 2. 任意可数群的双侧 FK 支配界

### 定理 2.1（**PROVED**）

对任意可数群 \(\Gamma\) 及任意 \(Q\in R(\Gamma)\)、\(0\le Q\le I\)，

\[
 \operatorname{Ber}(D(Q))^\Gamma\preceq\mu_Q
 \preceq
 \operatorname{Ber}(1-D(I-Q))^\Gamma.               \tag{2.1}
\]

证明只用有限 DPP 的导数公式、逆压缩和谱演算；复数内积空间上的 Hermitian
矩阵完全包含在内。

### 2.1 有限维导数引理

设 \(V\) 有限，\(0<C<I\) 是 \(\mathbb C^V\) 上的 Hermitian 正压缩。若

\[
 r\ge \max_{i\in V}(C^{-1})_{ii},                    \tag{2.2}
\]

则对每个递增函数 \(f:2^V\to\mathbb R\)，

\[
 \left.\frac d{ds}\mathbb E^{C+s(I-rC)}f\right|_{s=0}\le0. \tag{2.3}
\]

令 \(L=C(I-C)^{-1}\)。因为 \(0<C<I\)，每个配置都有正概率。给定
\(X\setminus\{i\}=A\) 时，点 \(i\) 的条件 odds 是 Schur 补

\[
 \frac{q_i(A)}{1-q_i(A)}
 =L_{ii}-L_{iA}L_A^{-1}L_{Ai}.                       \tag{2.4}
\]

还可把右端写成变分式

\[
 \min\{v^*Lv:v_i=1,\ \operatorname{supp}v\subseteq A\cup\{i\}\}. \tag{2.4a}
\]

因此它随 \(A\) 增大而减小；在 \(A=V\setminus\{i\}\) 时等于
\(1/(L^{-1})_{ii}\)。因 \(L^{-1}=C^{-1}-I\)，

\[
 q_i(A)\ge \frac1{(C^{-1})_{ii}}\ge\frac1r.         \tag{2.5}
\]

再写 \(\Delta_i f(A)=f(A\cup\{i\})-f(A)\)。以下把所用导数恒等式完整
核验。函数 \(f_B(X)=\mathbf1_{\{B\subseteq X\}}\)（\(B\subseteq V\)）构成
\(2^V\) 上函数空间的一组基，而且

\[
 \Delta_i f_B(A)=\mathbf1_{\{i\in B\}}
                  \mathbf1_{\{B\setminus\{i\}\subseteq A\}}.
\]

故

\[
 \sum_i\mathbb E^C\Delta_i f_B(X\setminus\{i\})
 =\sum_{i\in B}\det C[B\setminus\{i\}]
 =\left.\frac d{ds}\det(C[B]+sI_B)\right|_{s=0},
\]

以及

\[
 \sum_i\mathbb E^C\!\left[
 \mathbf1_{\{i\in X\}}\Delta_i f_B(X\setminus\{i\})\right]
 =|B|\det C[B]
 =\left.\frac d{ds}\det((1+s)C[B])\right|_{s=0}.
\]

第一式减去 \(r\) 倍第二式，再对 \(X\setminus\{i\}\) 条件化并线性扩张，
得到精确恒等式

\[
 \left.\frac d{ds}\mathbb E^{C+s(I-rC)}f\right|_{s=0}
 =\sum_i\mathbb E^C\!\left[
 (1-rq_i(X\setminus\{i\}))\Delta_i f(X\setminus\{i\})
 \right].                                             \tag{2.6}
\]

递增性给 \(\Delta_i f\ge0\)，而 (2.5) 给每个系数非正，故 (2.3) 成立。

### 2.2 保持 FK 的插值

先假设有谱隙 \(\varepsilon I\le Q\le(1-\varepsilon)I\)，并令 \(p=D(Q)\)。对
\(t\ge0\) 置

\[
 a_t=\frac{p}{D(Q+tI)},\qquad K_t=a_t(Q+tI).          \tag{2.7}
\]

归一化群迹满足 \(\tau(I)=1\)，所以 \(D(cA)=cD(A)\)。因此

\[
 K_0=Q,\qquad D(K_t)=p,\qquad K_t\longrightarrow pI
 \quad(t\to\infty).                                  \tag{2.8}
\]

并且 \(0<K_t<I\)。确实，对 \(0<\lambda\le1\)，
\(\lambda+t\ge(1+t)\lambda\)，故 \(a_t\le(1+t)^{-1}\)，而
\(\|Q\|<1\) 给 \(\|K_t\|<1\)。求导得

\[
 K_t'=a_t(I-r_tK_t),\qquad r_t=\tau(K_t^{-1}).        \tag{2.9}
\]

取任意有限 \(V\Subset\Gamma\)，记 \(C_t=K_t[V]\)。逆的变分公式给出逆压缩

\[
 C_t^{-1}\le P_VK_t^{-1}P_V.                         \tag{2.10}
\]

等变性使 \(K_t^{-1}\) 的每个对角元都等于 \(\tau(K_t^{-1})=r_t\)。于是
\((C_t^{-1})_{ii}\le r_t\)，有限维引理适用。每个有限支撑递增函数的期望沿
\(t\) 单调不增，结合 (2.8) 得

\[
 \mathbb E^{pI}f\le\mathbb E^Qf.                    \tag{2.11}
\]

这正是下支配。

### 2.3 奇异端点与上支配

对一般 \(Q\)，令

\[
 Q_\eta=\frac{Q+\eta I}{1+2\eta}.
\]

它有双侧谱隙，且 \(Q_\eta\to Q\)；谱测度上的单调收敛给
\(D(Q_\eta)\to D(Q)\)：具体地，\(\int\log(\lambda+\eta)\,d\nu_Q\) 在
\(\eta\downarrow0\) 时单调趋于 \(\int\log\lambda\,d\nu_Q\)，而
\(\log(1+2\eta)\to0\)。这也覆盖极限为零。DPP 的有限柱概率是有限主子式的多项式，
故可在 (2.11) 中取极限。若 \(D(Q)=0\)，所得下界就是确定空集律；若
\(D(Q)=1\)，则 \(\int\log\lambda=0\) 与 \(0\le\lambda\le1\) 迫使 \(Q=I\)。

这里“非满秩”在无限维应精确读成 \(\ker Q\ne\{0\}\)。其零谱投影
\(E_Q(\{0\})\in R(\Gamma)\) 非零时，群迹的忠实性给
\(\tau(E_Q(\{0\}))>0\)，从而 \(D(Q)=0\)。反向不成立：\(Q\) 可以 injective，
但 \(\log\) 谱积分仍为 \(-\infty\)。而且 \(D(Q)=0\) 的普适下界只是参数零的
平凡支配，并不推出 \(p_-(Q)=0\)；第 5 节投影反例正说明这一点，amenable 情形才由
第 4 节得到取等。

最后，DPP 的补集核为 \(I-Q\)：

\[
 \mu_Q[X\cap A=\varnothing]=\det(I-Q)[A].            \tag{2.12}
\]

补集反转随机序。把已经证明的下支配应用于 \(I-Q\)，立即得到 (2.1) 的上边。
因此这里的“双侧”没有依赖另一个未证耦合定理。

一个有用的精确恒等式是

\[
 p_+(Q)=1-p_-(I-Q).                                   \tag{2.13}
\]

## 3. 有限群：逐点最优（**PROVED**）

设 \(|\Gamma|=n\)。在正则单轨道上，等变性给

\[
 \tau(T)=\frac1n\operatorname{Tr}_{\mathbb C^n}T,
 \qquad
 D(Q)=(\det_{\mathbb C^n}Q)^{1/n}.                   \tag{3.1}
\]

若 \(\operatorname{Ber}(p)^\Gamma\preceq\mu_Q\)，对“全体点均占据”这一递增事件，

\[
 p^n\le\det Q,
\]

故 \(p\le D(Q)\)。与定理 2.1 合并即

\[
 p_-(Q)=D(Q).                                         \tag{3.2}
\]

对 \(I-Q\) 使用同一结论与 (2.13)，得到

\[
 p_+(Q)=1-D(I-Q).                                     \tag{3.3}
\]

这些式子包括全部退化情形：

- \(Q\) 非满秩时，\(D(Q)=0\)，所以 \(p_-(Q)=0\)；
- \(I-Q\) 非满秩时，\(p_+(Q)=1\)；
- 真正的非零真投影同时满足 \(p_-=0,p_+=1\)；
- \(Q=0\) 给 \(p_-=p_+=0\)，\(Q=I\) 给 \(p_-=p_+=1\)。

因此原文所说“甚至有限群也未知”的困难属于当时的支配充分性；一旦定理 2.1
建立，有限总体事件立即给出必要性和最优性。

## 4. Amenable 群：逐点最优（**PROVED**）

设 \(\Gamma\) 可数 amenable。Li--Thom
Theorem 1.4 对正元素给出

\[
 D(Q)=\inf_{\varnothing\ne F\Subset\Gamma}
       \det Q[F]^{1/|F|}
     =\lim_{F\to\Gamma}\det Q[F]^{1/|F|},           \tag{4.1}
\]

其中最后一个极限按该定理的 Følner 网理解。等式中的 infimum 已足够用于下文，
不需要任选 Følner 序列都收敛这一额外断言。定理明确允许正元素和零行列式，
因此覆盖 \(D(Q)=0\)。

若 \(\operatorname{Ber}(p)^\Gamma\preceq\mu_Q\)，任一有限 \(F\) 的全占据事件给

\[
 p^{|F|}\le\det Q[F].                                \tag{4.2}
\]

沿 Følner 集取根并用 (4.1)，得 \(p\le D(Q)\)。结合定理 2.1：

\[
 \boxed{p_-(Q)=D(Q),\qquad p_+(Q)=1-D(I-Q)}.          \tag{4.3}
\]

这包含有限群、\(\mathbb Z^d\) 及所有其他可数 amenable 群。对
\(\mathbb Z^d\)，Lyons--Steif Theorem 5.11 还直接给出每个可测符号的同一
if-and-only-if 结论。

### 4.1 子群诱导的可处理核（**PROVED**）

若 \(H\le\Gamma\)，把 \(H\)-等变核 \(Q_H\) 的卷积系数在
\(\Gamma\setminus H\) 上补零，得到 \(Q_\Gamma\in R(\Gamma)\)。它在各左陪集
\(gH\) 上是 \(Q_H\) 的拷贝，并在不同陪集间为零。因此 \(\mu_{Q_\Gamma}\) 是各
陪集上 \(\mu_{Q_H}\) 的独立积，且

\[
 D_\Gamma(Q_\Gamma)=D_H(Q_H),\qquad
 p_\pm(Q_\Gamma)=p_\pm(Q_H).                         \tag{4.4}
\]

第一式来自单位元处谱迹完全相同。第二式的一个方向由把任意全局随机序限制到
陪集 \(H\) 得到；反方向则把 \(H\) 上的单调耦合在各陪集独立复制。

所以 amenable 子群上的每个已知取等核都能成为任意上层群中的取等核，即使上层群
本身非 amenable；而下节 \(C_3*C_3\) 的反例会原样诱导到每个包含该子群的可数群。
这只分类了一族诱导核，不等于分类上层群的全部核。

## 5. 非 amenable 的逐点反例（**DISPROVED (P)**）

### 5.1 树投影（**DISPROVED (P)**）

令

\[
 \Gamma=C_3*C_3=\langle a,b\mid a^3=b^3=1\rangle.
\]

它是 sofic 群，故反例位于原 ICM 上下文内。其 Bass--Serre 树是三正则树，边作用
自由且传递；于是边空间就是一份 \(\ell^2(\Gamma)\)，没有多轨道迹缩放。

更一般地，在 \(d\)-正则树上选定每条边方向，令

\[
 \nabla f(e)=f(e^+)-f(e^-),\qquad
 \Delta=\nabla^*\nabla=dI-\mathcal A,\qquad
 \Pi=\nabla\Delta^{-1}\nabla^*.                      \tag{5.1}
\]

因为 \(\|\mathcal A\|\le2\sqrt{d-1}<d\)，\(\Delta\) 可逆，\(\Pi\) 是到
\(\overline{\operatorname{ran}\nabla}\) 的正交投影。这里范数界无需外部黑箱：
取根 \(o\) 并令 \(w(v)=(d-1)^{-\operatorname{dist}(o,v)/2}\)，则非根点的
\((\mathcal Aw)(v)/w(v)=2\sqrt{d-1}\)，根点的比值为
\(d/\sqrt{d-1}\le2\sqrt{d-1}\)；Schur 检验即得所需界。令

\[
 r=(d-1)^{-1},\qquad c=\frac{d-1}{d(d-2)}.
\]

Green 核为 \(G(u,v)=cr^{\operatorname{dist}(u,v)}\)。其列属于 \(\ell^2\)，且
\(dr=1+(d-1)r^2\)、\(dc(1-r)=1\) 分别验证离开极点及极点处的径向差分方程；
\(\Delta\) 可逆再给出唯一性。
因此

\[
 \Pi(e,f)=G(e^+,f^+)-G(e^+,f^-)-G(e^-,f^+)+G(e^-,f^-),
 \quad \Pi(e,e)=2/d.                                  \tag{5.2}
\]

每个有限压缩 \(\Pi[S]\) 正定：若有限支撑边向量 \(v\) 满足
\(\langle\Pi v,v\rangle=0\)，则 \(\nabla^*v=0\)；有限树上的有限支撑无散流从叶子
逐层删除即为零。

#### 下支配和精确阈值

给定有限占据集 \(S\) 后，条件核是

\[
 B^S=\Pi-\Pi_{\cdot S}\Pi[S]^{-1}\Pi_{S\cdot}
     =P_{H_S},\qquad H_S=\{h\in\operatorname{ran}\nabla:h|_S=0\}. \tag{5.3}
\]

若再给定有限空集 \(J\)，且该混合历史正概率，则块行列式给

\[
 \Pr(\eta_e=1\mid S\text{ 占据},J\text{ 空})
 =B^S_{ee}+B^S_{eJ}(I-B^S[J])^{-1}B^S_{Je}
 \ge B^S_{ee}.                                        \tag{5.4}
\]

在以根为起点的 BFS 边序中，当前父子边 \(e=(u,v)\) 取势函数：父侧为零，前向
子树上为 \(r^{\operatorname{dist}(v,w)}\)。其梯度 \(h\) 在所有前序边上为零，且

\[
 |h(e)|=1,\qquad \|h\|^2=d-1.                       \tag{5.5}
\]

所以任何正概率前序历史都有

\[
 B^S_{ee}=\|P_{H_S}\delta_e\|^2
 \ge |h(e)|^2/\|h\|^2=r.                             \tag{5.6}
\]

逐点共用 iid uniform 变量便构造
\(\operatorname{Ber}(r)^E\preceq\mu_\Pi\)。这是普通随机序耦合；不要求耦合不变。

反向必要性来自精确有限行列式。若 \(F\) 是含 \(m\) 条边的任意有限连通边集，
以 \(D_F\) 表示其关联矩阵、\(R(u,v)=r^{\operatorname{dist}(u,v)}\)，则

\[
 \Pi[F]=D_F(cR)D_F^*,
 \qquad
 \det\Pi[F]=r^m\left(1+\frac{d-2}{d}m\right).        \tag{5.7}
\]

这里使用的恒等式

\[
 \det(D_FCD_F^*)=\det C\,\mathbf1^*C^{-1}\mathbf1
\]

来自有限树关联矩阵的全体最大子式；而树上 AR(1) 创新变换给
\(\det R=(1-r^2)^m\) 与
\(\mathbf1^*R^{-1}\mathbf1=1+m(1-r)^2/(1-r^2)\)。若 Bernoulli \(p\)
被 \(\mu_\Pi\) 支配，则 (5.7) 的全占据事件给 \(p\le r\)。故

\[
 p_-(\Pi)=\frac1{d-1}.                                \tag{5.8}
\]

一个顶点的全星压缩有特征值一，因为 \(\nabla\delta_v\) 属于梯度空间且支撑在
该星上。因此该星全空概率为零，推出

\[
 p_+(\Pi)=1.                                          \tag{5.9}
\]

#### 回到正则表示

对 \(C_d*C_d\)，Bass--Serre 边标号给出一份正则表示，且 \(\tau(\Pi)=2/d\)。
这里把两类顶点分别记为 \(\Gamma/C_d^{(a)}\) 与 \(\Gamma/C_d^{(b)}\)，统一从
第一类指向第二类；左 \(\Gamma\) 作用保持这两个类型，所以 \(\nabla\) 真正 intertwine
而没有随群元素变化的符号扭曲。
投影的迹谱测度在零点质量 \(1-2/d\)，在一点质量 \(2/d\)，所以 \(D(\Pi)=0\)。

在 \(d=3\) 时，若 \(\ell(g)\) 为约化 syllable 长度，核明确为

\[
 Q(x,y)=
 \begin{cases}
 2/3,&x=y,\\[1mm]
 \displaystyle\frac{(-1)^{\ell(x^{-1}y)+1}}{3\,2^{\ell(x^{-1}y)}},&x\ne y.
 \end{cases}                                          \tag{5.10}
\]

于是

\[
 \boxed{D(Q)=0<1/2=p_-(Q),\qquad p_+(Q)=1}.           \tag{5.11}
\]

补集反转给

\[
 \boxed{p_+(I-Q)=1/2<1=1-D(Q)}.                       \tag{5.12}
\]

这同时覆盖 \(D(Q)=0\) 和非满秩边界，且反例满足原题的等变、正压缩、单正则轨道
和 sofic 前提。

### 5.2 排除“只是零谱端点”的解释（**DISPROVED**）

令上述 \(d=3\) 投影仍记为 \(Q\)，并置

\[
 \widehat Q=\frac{I+63Q}{128}.                        \tag{5.13}
\]

先把 \(\mu_Q\) 与独立 Bernoulli \(1/64\) 作并，再共同以概率 \(1/2\) 稀疏化；
这保持逐点包含关系，并把核变成 \(\widehat Q\)。由 \(p_-(Q)=1/2\) 得

\[
 p_-(\widehat Q)\ge65/256.                            \tag{5.14}
\]

\(\widehat Q\) 的谱为 \(1/128\)（迹质量 \(1/3\)）和 \(1/2\)（迹质量 \(2/3\)），
故

\[
 D(\widehat Q)=(1/128)^{1/3}(1/2)^{2/3}=1/8.
\]

所以它在两个谱端点之外仍满足

\[
 \boxed{1/8=D(\widehat Q)<65/256\le p_-(\widehat Q)}. \tag{5.15}
\]

补核同样有双侧谱隙，且

\[
 p_+(I-\widehat Q)\le191/256<7/8=1-D(\widehat Q).     \tag{5.16}
\]

### 5.3 有限支撑群代数核中仍有反例（**DISPROVED**）

投影 \(Q=\Pi\) 本身含 \(\Delta^{-1}\)，不是有限传播核；所以 (5.11) 不能未经
说明就拿来否定 \(\mathbb C\Gamma\) 子类。这个边界可用范数逼近闭合。

在三正则 Bass--Serre 树上，\(\Delta\) 的谱包含在某个紧区间
\([c,C]\subset(0,\infty)\)。取实系数多项式 \(p_n\) 在该区间上一致逼近
\(\lambda^{-1}\)，并令

\[
 P_n=\nabla p_n(\Delta)\nabla^*,\qquad
 Q_n=\frac{I+63P_n}{128}.                             \tag{5.17}
\]

则 \(P_n\to\Pi\)、\(Q_n\to\widehat Q\) 都是算子范数收敛。沿上一段固定的
两顶点类型方向，\(\nabla\) 与左 \(\Gamma\) 作用 intertwine；因此 \(P_n\) 是边正则
表示上的等变有限传播 Hermitian 核。边作用自由传递且有限半径球有限，所以这种
核恰由有限支撑卷积元给出，即 \(P_n,Q_n\in\mathbb C\Gamma\)。充分大的 \(n\)
还满足 \(0<Q_n<I\)。

写 \(\varepsilon_n=\|Q_n-\widehat Q\|\)。算子序给

\[
 Q_n\ge L_n:=\left(\frac1{128}-\varepsilon_n\right)I
                 +\frac{63}{128}\Pi .                \tag{5.18}
\]

当 \(\varepsilon_n<1/128\) 时，\(L_n\) 可实现为：先把 \(\mu_\Pi\) 与适当参数的
独立 Bernoulli 作并，再作独立稀疏化。把同样操作施于
\(\operatorname{Ber}(1/2)\preceq\mu_\Pi\)：具体取
\(s_n=1/2-\varepsilon_n\)、
\(q_n=(1/128-\varepsilon_n)/s_n\)，先作并再以 \(s_n\) 稀疏化，精确得到

\[
 p_-(L_n)\ge \frac{65}{256}-\varepsilon_n.           \tag{5.19}
\]

正压缩的算子序蕴含对应 DPP 的普通随机序，故
\(p_-(Q_n)\ge p_-(L_n)\)：严格地说，对每个有限 \(F\)，压缩满足
\(0\le L_n[F]\le Q_n[F]\le I_F\)，有限 DPP 的算子序支配定理适用；再遍历所有
递增柱事件，就得到可数空间的普通随机序。另一方面，\(\widehat Q\) 有统一下谱隙，因而
\(\log\) 在共同谱区间上算子范数连续，给出

\[
 D(Q_n)\longrightarrow D(\widehat Q)=1/8.            \tag{5.20}
\]

由于 \(65/256>1/8\)，充分大的 \(n\) 满足
\(D(Q_n)<p_-(Q_n)\)。因此固定核逐点最优性即使限制到
\(\mathbb C(C_3*C_3)\) 的满秩严格正压缩也为假。这里证明的是反例存在性；
不把原投影本身误称为有限支撑。

还可完全固定一个实例。令 \(\mathcal A\) 是三正则树邻接算子，
\(\Delta=3I-\mathcal A\)，并取

\[
 p_N(\Delta)=\frac13\sum_{k=0}^{N}(\mathcal A/3)^k,\qquad N=255. \tag{5.21}
\]

因 \(\|\mathcal A\|/3\le2\sqrt2/3<19/20\) 且 \(\|\nabla\|^2=\|\Delta\|<6\)，
对应 (5.17) 的核满足

\[
 \varepsilon_N=\|Q_N-\widehat Q\|
 <20(19/20)^{256}<1/1024.                            \tag{5.22}
\]

所以 \(Q_N\ge(7/1024)I\)，并由 \(\log\) 的 resolvent 积分得
\(\|\log Q_N-\log\widehat Q\|\le1/7\)。于是

\[
 D(Q_N)\le e^{1/7}/8<7/48<259/1024\le p_-(Q_N).     \tag{5.23}
\]

其中 \(e^{1/7}<7/6\) 可由
\(\log(1+x)\ge x/(1+x)\) 在 \(x=1/6\) 处直接验证。故 (5.21) 给出一个明确的
有限支撑反例，而不仅是存在性逼近。

## 6. 任意可数群的精确障碍（**PROVED / INCOMPLETE**）

对任意单轨道核定义

\[
 \delta(Q)=\inf_{\varnothing\ne F\Subset\Gamma}
             \det Q[F]^{1/|F|}.                       \tag{6.1}
\]

全占据柱事件总给

\[
 p_-(Q)\le\delta(Q).                                  \tag{6.2}
\]

另一方面，令 \(P=P_F\)。对正可逆 \(T\)，逆压缩的变分公式给

\[
 (PTP+sI_P)^{-1}\le P(T+sI)^{-1}P\qquad(s\ge0).     \tag{6.3a}
\]

把它代入

\[
 \log T=\int_0^\infty
 \left((1+s)^{-1}I-(T+sI)^{-1}\right)\,ds           \tag{6.3b}
\]

（先在两个谱界之间积分，再取极限），得到
\(\log(PTP)\ge P(\log T)P\)。取 \(T=Q+\varepsilon I\)，用等变性把右端
迹写成 \(|F|\tau\log(Q+\varepsilon I)\)，最后令
\(\varepsilon\downarrow0\)，得到

\[
 D(Q)\le\delta(Q).                                    \tag{6.3}
\]

Amenability 通过 Følner 行列式逼近把 (6.3) 变成等号。树反例则有

\[
 D(Q)=0<\delta(Q)=p_-(Q)=1/2.                         \tag{6.4}
\]

所以第一层障碍是：非 amenable 群上，有限窗口的归一化行列式不必逼近群迹的
对数谱平均。第二层障碍是：即使知道 \(\delta(Q)\)，全占据事件也只覆盖递增事件
的一小部分；一般随机序阈值未被所有主子式根值自动刻画。

因此下列分类仍为 **INCOMPLETE**：哪些非 amenable 群对所有 \(Q\) 仍满足逐点
等号；以及给定非 amenable \(Q\) 时如何从算子数据精确计算 \(p_-(Q)\)。

## 7. \(R(\Gamma,S)\) 多轨道矩阵与 trace normalization

Conjecture 5.7 本身陈述在单轨道 \(\ell^2(\Gamma)\) 上。Lyons--Thom Lemma 3.4
把 Cayley diagram 的有限标签边空间写成

\[
 R(\Gamma,S)\cong M_S(R(\Gamma)),
\]

并采用自然的**非归一化**有限标签迹

\[
 \tau_S(T)=\sum_{s\in S}\tau(p_sTp_s),\qquad \tau_S(I)=|S|. \tag{7.1}
\]

令 \(m=|S|\)，并定义自然非归一化 FK 行列式

\[
 \Delta_S(Q)=\exp\tau_S(\log Q).                       \tag{7.2}
\]

群代数上的有限矩阵 \(M_S(\mathbb C\Gamma)\) 是
\(R(\Gamma,S)=M_S(R(\Gamma))\) 的有限传播子类；下述普遍支配定理当然适用于
这一子类。若 \(\Gamma\) amenable，Li--Thom Theorem 1.4 的
\(M_m(\mathcal N\Gamma)\) 版本与全占据事件还给出必要边界

\[
 p_-(Q)\le\Delta_S(Q)^{1/m},\qquad
 p_+(Q)\ge1-\Delta_S(I-Q)^{1/m}.                    \tag{7.2a}
\]

多轨道标签可能异质，故这里不声称 (7.2a) 取等；平凡群的二维对角例马上显示
一般不会取等。结合下述普遍充分界，有限或 amenable 的 \(\Gamma\) 满足夹逼

\[
 \Delta_S(Q)\le p_-(Q)\le\Delta_S(Q)^{1/m},\qquad
 1-\Delta_S(I-Q)^{1/m}\le p_+(Q)\le1-\Delta_S(I-Q). \tag{7.2b}
\]

特别地，\(\Delta_S(Q)=0\) 时仍有 \(p_-(Q)=0\)；每坐标归一化量
\(\Delta_S(Q)^{1/m}\) 在这里是必要上界而不是充分下界。若
\(\Gamma\) 非 amenable，第 5.3 节说明即使 \(S\) 为单点，有限支撑子类也不能
恢复逐点最优性。

### 7.1 自然非归一化版本（**PROVED**）

对任意可数 \(\Gamma\)、有限非空 \(S\) 和
\(Q\in R(\Gamma,S)\)、\(0\le Q\le I\)，有

\[
 \operatorname{Ber}(\Delta_S(Q))^{\Gamma\times S}
 \preceq\mu_Q\preceq
 \operatorname{Ber}(1-\Delta_S(I-Q))^{\Gamma\times S}. \tag{7.3}
\]

证明是定理 2.1 插值的非归一化修正。先设双侧谱隙，记
\(\Delta=\Delta_S(Q)\)，并置

\[
 a_t=\frac{(1+t)^{m-1}\Delta}{\Delta_S(Q+tI)},
 \qquad K_t=a_t(Q+tI).                                \tag{7.4}
\]

因为 \(\Delta_S(cA)=c^m\Delta_S(A)\)，所以

\[
 K_0=Q,\qquad K_t\longrightarrow\Delta I.             \tag{7.5}
\]

对每个谱值 \(0<\lambda\le1\)，有
\(\lambda+t\ge(1+t)\lambda\)。在 \(\tau_S\) 下积分给
\(\Delta_S(Q+tI)\ge(1+t)^m\Delta\)，故
\(a_t\le(1+t)^{-1}\)；上谱隙再给 \(0<K_t<I\)。

对每个标签代表 \(x_s=(e,s)\)，写

\[
 h_s(t)=\langle(Q+tI)^{-1}\delta_{x_s},\delta_{x_s}\rangle.
\]

求导得到

\[
 K_t'=a_t(I-r_tK_t),\qquad
 r_t=\frac{\sum_{s\in S}h_s(t)-(m-1)/(1+t)}{a_t}.     \tag{7.6}
\]

由于 \(Q+tI\le(1+t)I\)，每个 \(h_s(t)\ge1/(1+t)\)。固定任一标签
\(s_0\)，其余 \(m-1\) 项因此给

\[
 \sum_s h_s(t)-\frac{m-1}{1+t}\ge h_{s_0}(t).
\]

而 \(K_t^{-1}=a_t^{-1}(Q+tI)^{-1}\)，所以

\[
 r_t\ge
 \max_s\langle K_t^{-1}\delta_{x_s},\delta_{x_s}\rangle. \tag{7.7}
\]

同一标签轨道内的对角元由 \(\Gamma\)-等变性保持相等。对任意有限压缩再用
逆压缩不等式，有限维导数引理的条件 (2.2) 成立。于是沿路径所有递增柱函数期望
下降，极限 (7.5) 给出 (7.3) 的下边；上边仍由补核得到。最后用
\(Q_\varepsilon=(Q+\varepsilon I)/(1+2\varepsilon)\) 去掉谱隙，包含
\(\Delta_S(Q)=0\) 情形。

这一非归一化版本在“只使用一个 \(\Delta_S\) 数值”的算子类意义下分别锋利：

- \(Q=\operatorname{diag}(p,1,\ldots,1)\otimes I_\Gamma\) 有
  \(\Delta_S(Q)=p=p_-(Q)\)；
- \(Q=\operatorname{diag}(p,0,\ldots,0)\otimes I_\Gamma\) 有
  \(1-\Delta_S(I-Q)=p=p_+(Q)\)。

它一般不逐点最优，也不等于把 trace 除以 \(m\) 后的“每坐标几何平均”。

### 7.2 每坐标归一化版本的二维反例（**DISPROVED**）

若为了得到每坐标 FK 数值而改用
\(\bar\tau_S=m^{-1}\tau_S\)，则原单轨道公式不能直接照搬。

取平凡群、\(S=\{1,2\}\) 及

\[
 Q=\operatorname{diag}(1/4,3/4).                      \tag{7.8}
\]

其 DPP 就是两个成功率分别为 \(1/4,3/4\) 的独立 Bernoulli 位，所以

\[
 p_-(Q)=1/4,\qquad p_+(Q)=3/4.                        \tag{7.9}
\]

然而归一化迹给

\[
 D_{\bar\tau_S}(Q)=D_{\bar\tau_S}(I-Q)=\sqrt3/4.     \tag{7.10}
\]

于是候选下界 \(\sqrt3/4\) 大于真实下阈值 \(1/4\)，候选上界
\(1-\sqrt3/4\) 小于真实上阈值 \(3/4\)：两边同时失败。该例已是满秩、复
Hermitian（实对角是其特例）。

用非归一化迹时，\(\Delta_S(Q)=3/16\)，定理 (7.3) 正确给出较弱的两边；但对
\(Q=qI_S\)，它给 \(q^m\)，而真实逐点阈值是 \(q\)，所以不能把它误称为
逐点阈值公式。

单轨道定理 2.1 的关键一步是每个坐标都有
\(\langle K^{-1}\delta_x,\delta_x\rangle=\tau(K^{-1})\)。在
\(\Gamma\times S\) 只有 \(\Gamma\) 作用时，各标签是不同轨道；归一化 trace 只给
这些对角元的平均，不能控制最大值。这正是 (7.8) 暴露的失效点。非归一化证明
之所以能修复，是 (7.6) 保留了其他 \(m-1\) 个轨道各自至少 \(1/(1+t)\) 的贡献。

若追求比 (7.3) 更锋利的多轨道结论，可允许标签依赖的 Bernoulli 参数，或加入
在标签间传递的更大对称群使整个坐标集重新成为单轨道。没有这些附加结构时，
每坐标归一化 FK 不是 Conjecture 5.7 标量公式的无损替换。

## 8. 最终裁决

1. **PROVED：** FK 给出的两条普通随机序支配界对任意可数群成立；证明覆盖
   \(D(Q)=0\)、不要求有界可逆、非满秩以及复 Hermitian 核。
2. **DISPROVED：** “每个固定 \(Q\) 的阈值都等于 FK”在原 sofic 范围内为假，
   且失败不局限于零谱端点或非有限传播核；满秩有限支撑群代数核已有反例。
3. **PROVED：** 固定 \(Q\) 等号在有限群和所有可数 amenable 群成立。
4. **PROVED：** 若“最优”仅指所显示的一元 FK 函数不能在整个类上一致改进，
   标量核已给锋利性。
5. **PROVED / DISPROVED：** 在 \(R(\Gamma,S)\) 中，自然非归一化迹给出有效且
   一元类上锋利的同形界；把迹除以 \(|S|\) 后直接套用同形公式则已被二维对角核
   否定。
6. **INCOMPLETE：** 任意非 amenable 群/核的逐点阈值分类，以及依赖两个 FK
   数值的统一精细改进。

辅助精确程序 `check01.py` 复算了 9 条边窗口的全部 511 个非空主子式、133 个
连通子树行列式与 346 个正概率 BFS 历史，并核验双侧谱隙算术和
\(R(\Gamma,S)\) 二维归一化反例。独立程序 `mcheck.py` 又在一个复 Hermitian
四维核及其补核上枚举全部 168 个递增事件，精确验证插值初始方向非正，并用两个
单点事件否定归一化多轨道公式。两份程序均通过；这些有限检验不替代上述无限维
证明。

复现命令（在本目录运行）为

```text
python check01.py
python mcheck.py
```

`check01.py` 只用 Python 标准库；`mcheck.py` 需要 SymPy 1.14.0。
