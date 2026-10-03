# 题 2 独立数学与来源审计

日期：2026-10-02

## 总裁决

**PROVED：FK 双侧支配。** 对任意可数群 \(\Gamma\) 和任意复 Hermitian 等变正压缩 \(Q\in R(\Gamma)\)，

\[
\operatorname{Ber}(D(Q))^\Gamma\preceq\mu_Q
\preceq\operatorname{Ber}(1-D(I-Q))^\Gamma,
\qquad D(Q)=\exp\tau(\log Q).
\]

证明不使用 soficity，覆盖 \(D(Q)=0\)、非满秩、无谱隙和复核。

**DISPROVED：固定核的逐点“最优”若解释为恒等阈值。** 在 sofic 群 \(C_3*C_3\) 的一份正则表示上，有投影核 \(Q\) 满足 \(D(Q)=0<p_-(Q)=1/2\)；补核给严格上边反例。双侧谱隙扰动及有限支撑群代数逼近仍有严格差距，因此失败不只发生在 FK 为零或无限传播的边界。

**PROVED：有限群与所有可数 amenable 群逐点取等。** 有限群由全体占据事件给必要性；amenable 群由 Li--Thom Theorem 1.4 的有限压缩 determinant infimum 给必要性，再与普适充分性合并。

**INCOMPLETE：一般非 amenable 分类。** 正文给出反例族、诱导核与有限窗口障碍，但没有分类所有非 amenable 群或全部固定核。

## ICM 原句与“optimal”语义

实际打开 Lyons ICM 2014 作者 PDF：

- **Theorem 5.2（printed p. 157）：** abelian 符号的几何平均双侧支配，并称 bounds optimal；
- **Conjecture 5.7（printed p. 158）：** 在 §5.2 的 sofic 语境中，对 \(\ell^2(\Gamma)\) 上等变正压缩提出 FK 双侧支配并称 bounds optimal；原文说即使有限群也开放；
- 原文没有形式定义这里的 “optimal”。

Lyons--Steif **Theorems 5.3 和 5.11** 对 \(\mathbb Z\) 与 \(\mathbb Z^d\) 给每个固定符号的 if-and-only-if 阈值。因此把 Conjecture 5.7 读成固定 \(Q\) 的逐点等号是最自然的延伸，但这是语义判断而非作者意图的额外事实。正文将它与“只依赖一个 FK 数值的全类一致锋利性”分开；后者由标量核 \(Q=pI\) 取等，不能替代逐点命题。

## 普适支配证明

### 1. 有限维方向引理

**PROVED.** 对有限严格正压缩 \(0<C<I\)，令 \(L=C(I-C)^{-1}\)。给定其余配置 \(A\) 后，点 \(i\) 的 conditional odds 是 Schur 补

\[
L_{ii}-L_{iA}L_A^{-1}L_{Ai}.
\]

其变分式随 \(A\) 增大而减小；最小值在 \(A=V\setminus\{i\}\)，转换回概率得到

\[
q_i(A)\ge \frac1{(C^{-1})_{ii}}.
\]

**PROVED.** inclusion functions \(f_B(X)=\mathbf1_{\{B\subseteq X\}}\) 构成全部函数的一组基。沿 \(I-rC\) 求主子式导数，得到

\[
\left.\frac d{ds}\mathbb E^{C+s(I-rC)}f\right|_{s=0}
=\sum_i\mathbb E^C[(1-rq_i)\Delta_i f].
\]

若 \(r\ge\max_i(C^{-1})_{ii}\)，每个系数非正，所以所有递增 \(f\) 的导数非正。此推导只用 Hermitian 正定矩阵的 Schur 补，复数情形完全包含。

### 2. 单轨道 FK 等值路径

设 \(Q\) 有双侧谱隙，\(p=D(Q)\)，并置

\[
a_t=\frac p{D(Q+tI)},\qquad K_t=a_t(Q+tI).
\]

逐式核验结果：

1. **PROVED：起点、终点与谱界。** \(K_0=Q\)；由 \(\lambda+t\ge(1+t)\lambda\) 得 \(a_t\le(1+t)^{-1}\)，故 \(0<K_t<I\)；又 \(D(Q+tI)\sim t\)，所以 \(K_t\to pI\)。
2. **PROVED：路径保持 determinant。** 归一化群迹满足 \(D(cA)=cD(A)\)，故 \(D(K_t)=p\)。
3. **PROVED：导数方向。**
   \[
   K_t'=a_t[I-r_tK_t],\qquad r_t=\tau(K_t^{-1}).
   \]
4. **PROVED：有限压缩条件。** 对 \(C_t=P_VK_tP_V\)，逆压缩变分式给
   \[
   C_t^{-1}\le P_VK_t^{-1}P_V.
   \]
   单轨道等变性使 \(K_t^{-1}\) 的每个对角元等于 \(\tau(K_t^{-1})\)，因此有限方向引理适用。
5. **PROVED：积分与极限。** 每个有限支撑递增柱函数的期望随 \(t\) 不增，终点 \(pI\) 给 \(\operatorname{Ber}(p)^\Gamma\preceq\mu_Q\)。

### 3. 奇异端点与上边

**PROVED.** 正则化

\[
Q_\eta=\frac{Q+\eta I}{1+2\eta}
\]

具有双侧谱隙并收敛到 \(Q\)。谱测度上的单调收敛给 \(D(Q_\eta)\to D(Q)\)，包括极限零；DPP 有限柱概率是有限主子式的多项式，故支配关系可取极限。

**PROVED.** DPP 补集核为 \(I-Q\)，补集反转随机序。将下边用于 \(I-Q\) 即得到上边，并有

\[
p_+(Q)=1-p_-(I-Q).
\]

这里没有暗用另一个未证耦合定理。

## 群类与逐点最优性

### 有限群

**PROVED.** 若 \(|\Gamma|=n\)，则 \(D(Q)=(\det Q)^{1/n}\)。全体点均占据事件给 \(p^n\le\det Q\)，与普适下支配合并得到 \(p_-(Q)=D(Q)\)；补核给 \(p_+(Q)=1-D(I-Q)\)。这包含零核、恒等核、非满秩和真投影。

### 可数 amenable 群

**PROVED.** Li--Thom **Theorem 1.4** 的原文条件是：\(\Gamma\) 为 countable discrete amenable，\(g\in M_d(\mathcal N\Gamma)\) 为 positive；它允许奇异正元素，并给

\[
\det_{\mathcal N\Gamma}g
=\inf_F(\det g_F)^{1/|F|}
=\lim_F(\det g_F)^{1/|F|}
\]

（最后是 Følner 网）。对单轨道 \(Q\)，全占据柱事件给 \(p\le(\det Q[F])^{1/|F|}\)；对所有有限 \(F\) 取 infimum 即 \(p\le D(Q)\)。所以所有可数 amenable 群逐点取等，包括 \(D(Q)=0\) 和其他奇异端点。

### 非 amenable 反例

**DISPROVED（普遍逐点等号）。** 三正则 Bass--Serre 树的边作用对 \(C_3*C_3\) 自由且传递，因此边空间正是一份 \(\ell^2(\Gamma)\)，没有多轨道迹归一化问题。梯度投影

\[
\Pi=\nabla(3I-\mathcal A)^{-1}\nabla^*
\]

是等变投影，迹为 \(2/3\)，故 \(D(\Pi)=0\)。BFS 条件概率论证给 \(\operatorname{Ber}(1/2)\preceq\mu_\Pi\)，而任意含 \(m\) 条边的有限连通子树满足

\[
\det\Pi[F]=2^{-m}(1+m/3).
\]

从全占据事件令 \(m\to\infty\) 得反向界，所以 \(p_-(\Pi)=1/2\)。一个顶点的全星压缩含特征值一，故 \(p_+(\Pi)=1\)。补核给严格上边反例。

**PROVED：双侧谱隙反例。** 对

\[
\widehat Q=\frac{I+63\Pi}{128},
\]

先把 \(\mu_\Pi\) 与 Bernoulli \(1/64\) 作并，再共同以 \(1/2\) 稀疏化，得到

\[
p_-(\widehat Q)\ge65/256,\qquad D(\widehat Q)=1/8.
\]

\(\widehat Q\) 的谱位于 \([1/128,1/2]\)，所以严格差距不来自零谱端点。补核给相应严格上边。

### 有限支撑群代数反例

**PROVED.** 原投影含 \(\Delta^{-1}\)，本身不是有限传播核；正文没有混淆这一点。由于树 Laplacian 的谱在紧区间 \([c,C]\subset(0,\infty)\)，取实多项式 \(p_n\) 一致逼近 \(\lambda^{-1}\)，并令

\[
P_n=\nabla p_n(\Delta)\nabla^*,\qquad
Q_n=\frac{I+63P_n}{128}.
\]

则 \(P_n\to\Pi\)、\(Q_n\to\widehat Q\) 为算子范数收敛。每个 \(P_n\) 等变、Hermitian 且有限传播；边作用自由传递，故它对应有限支撑卷积元，\(P_n,Q_n\in\mathbb C\Gamma\)。充分大的 \(n\) 有 \(0<Q_n<I\)。

写 \(\varepsilon_n=\|Q_n-\widehat Q\|\)。算子序给

\[
Q_n\ge L_n=
\left(\frac1{128}-\varepsilon_n\right)I+\frac{63}{128}\Pi.
\]

当 \(\varepsilon_n<1/128\) 时，令

\[
s_n=\frac12-\varepsilon_n,\qquad
q_n=\frac{1/128-\varepsilon_n}{s_n}.
\]

先与 Bernoulli \(q_n\) 作并，再以 \(s_n\) 稀疏化，恰得到核 \(L_n\)。将同样操作施于 \(\operatorname{Ber}(1/2)\preceq\mu_\Pi\)，得到

\[
p_-(L_n)\ge65/256-\varepsilon_n.
\]

正压缩算子序蕴含 DPP 随机序，所以 \(p_-(Q_n)\ge p_-(L_n)\)。另一方面，\(\widehat Q\) 有统一下谱隙，\(\log\) 在共同谱区间上算子范数连续，因此 \(D(Q_n)\to1/8\)。由于 \(65/256>1/8\)，充分大的 \(n\) 仍满足 \(D(Q_n)<p_-(Q_n)\)。故逐点最优性在满秩严格正的有限支撑群代数核中也失败。

**PROVED（显式有限支撑实例）。** 正文进一步固定

\[
p_N(\Delta)=\frac13\sum_{k=0}^{N}(\mathcal A/3)^k,\qquad N=255.
\]

由 \(\|\mathcal A\|/3\le2\sqrt2/3<19/20\)、Neumann 级数尾界和 \(\|\nabla\|^2=\|\Delta\|<6\)，对应核满足

\[
\varepsilon_N<20(19/20)^{256}<1/1024.
\]

因此 \(Q_N\ge7I/1024\)。resolvent 积分给

\[
\|\log Q_N-\log\widehat Q\|
\le \frac{\varepsilon_N}{7/1024}<\frac17,
\]

故 \(D(Q_N)\le e^{1/7}/8<7/48\)；另一方面前述随机序下界给

\[
p_-(Q_N)\ge65/256-\varepsilon_N>259/1024.
\]

数值次序 \(7/48<259/1024\) 正确，且 \(\log(7/6)>1/7\) 给 \(e^{1/7}<7/6\)。所以这不是只靠“充分大 \(n\)”的存在性论证，而是一个固定阶数的有限支撑反例。

### 仍未分类的部分

**INCOMPLETE.** 对任意 \(Q\)，全占据事件只给

\[
p_-(Q)\le\delta(Q):=\inf_F\det Q[F]^{1/|F|},
\]

而 log 的逆压缩积分给 \(D(Q)\le\delta(Q)\)。amenability 使两者相等；树例中 \(D(Q)=0<\delta(Q)=p_-(Q)=1/2\)。一般 \(\delta(Q)\) 只控制一族递增事件，不能据此计算全部随机序阈值。

**PROVED（诱导核族）。** 把 \(H\)-核的卷积系数在 \(\Gamma\setminus H\) 上补零，所得算子按左陪集分块，DPP 是各块独立积。限制耦合和逐陪集复制给 \(p_\pm\) 不变，单位元谱迹给 FK 不变。这只产生一族可处理核，没有声称群级分类。

## \(R(\Gamma,S)\) 多轨道扩展

Lyons--Thom §3 Lemma 3.4 之后使用

\[
R(\Gamma,S)=M_S(R(\Gamma)),\qquad
\tau_S(T)=\sum_{s\in S}\tau(p_sTp_s),\quad \tau_S(I)=m:=|S|.
\]

这是非归一化 trace。令

\[
\Delta_S(Q)=\exp\tau_S(\log Q).
\]

### 非归一化同形界

**PROVED.** 对双侧有谱隙的 \(Q\)，置

\[
a_t=\frac{(1+t)^{m-1}\Delta_S(Q)}{\Delta_S(Q+tI)},
\qquad K_t=a_t(Q+tI).
\]

关键等式均已独立复算：

1. \(\Delta_S(cA)=c^m\Delta_S(A)\)，且 \(a_0=1\)；
2. \(\Delta_S(Q+tI)\ge(1+t)^m\Delta_S(Q)\)，所以 \(a_t\le(1+t)^{-1}\) 且 \(K_t<I\)；
3. \(\Delta_S(Q+tI)=t^m\Delta_S(I+Q/t)\)，所以 \(a_t\sim\Delta_S(Q)/t\) 且 \(K_t\to\Delta_S(Q)I\)；
4. 对
   \[
   h_s(t)=\langle(Q+tI)^{-1}\delta_{(e,s)},\delta_{(e,s)}\rangle,
   \]
   有
   \[
   K_t'=a_t[I-r_tK_t],\qquad
   r_t=\frac{\sum_sh_s(t)-(m-1)/(1+t)}{a_t};
   \]
5. 因 \((Q+tI)^{-1}\ge(1+t)^{-1}I\)，固定任一 type \(s_0\) 后，其余 \(m-1\) 项给
   \[
   r_t\ge a_t^{-1}h_{s_0}(t)
   =\langle K_t^{-1}\delta_{(e,s_0)},\delta_{(e,s_0)}\rangle.
   \]
   同 type 内等变，再加逆压缩，即满足有限方向引理。

沿路径积分、取终点并使用同一正则化，得到

\[
\operatorname{Ber}(\Delta_S(Q))^{\Gamma\times S}
\preceq\mu_Q\preceq
\operatorname{Ber}(1-\Delta_S(I-Q))^{\Gamma\times S}.
\]

**PROVED：一元类上锋利。** \(\operatorname{diag}(p,1,\ldots,1)\) 使下边取等；\(\operatorname{diag}(p,0,\ldots,0)\) 使上边取等。它们证明只依赖单个 \(\Delta_S\) 的全类函数不能改进，不证明每个多轨道核逐点取等。

### Amenable 多轨道必要边界

**PROVED.** Li--Thom Theorem 1.4 的 \(M_m(\mathcal N\Gamma)\) 版本与 \(F\times S\) 全占据事件给

\[
p_-(Q)\le\Delta_S(Q)^{1/m},\qquad
p_+(Q)\ge1-\Delta_S(I-Q)^{1/m}.
\]

标签轨道可以异质，因此正文没有把这些必要界误称为等号。

### 归一化 trace 的直接照搬

**DISPROVED.** 对平凡群、\(S=\{1,2\}\) 和

\[
Q=\operatorname{diag}(1/4,3/4),
\]

DPP 是两个独立但不同参数的 Bernoulli 位，所以 \(p_-=1/4,p_+=3/4\)。归一化 determinant 为 \(\sqrt3/4\)，候选下边过大，而 \(1-\sqrt3/4\) 候选上边过小。该反例满秩且有双侧谱隙。

## 计算复核

**PROVED（有限接口检查通过）。** 我独立运行并检查两份精确程序：

- check01.py：9 条边窗口的 511 个非空主子式全部正；133 个连通子树行列式满足闭式；346 个正概率 BFS 历史的最小下一点条件概率为 \(6/11>1/2\)；谱隙算术和二维归一化反例通过。
- mcheck.py：在一个复 Hermitian 四维等变核及其补核上，全部 168 个递增事件的插值初始导数均非正；二维归一化公式由两个单点事件否定。

这些计算只验证有限代数接口，不替代无限维插值、正则化或来源定理。

## 来源完整性

- **Lyons ICM 2014：** Theorem 5.2、Conjecture 5.7 及 sofic 上下文已按作者 PDF 核对；作者 2025-12-30 errata 没有修改或撤回 Conjecture 5.7。
- **Lyons--Steif 2003：** Theorems 5.3、5.11 是普通随机序的逐符号必要充分结论；Definition 5.15 / Theorem 5.16 的 full domination 是更强概念，正文没有混用。
- **Li--Thom 2014：** Theorem 1.4 的 positive、countable amenable、matrix 和奇异端点条件已核对。
- **Lyons--Thom 2016：** §3 Lemma 3.4 与其后的非归一化 \(\tau_S\) 定义已核对。
- **Elek--Szabó 2011：** 正确来源为 *Sofic representations of amenable groups*, Proc. AMS 139, 4285--4291，Theorem 1 给 amenable amalgam 的 sofic closure；最终参考文献题名、页码和 DOI 正确。
- [公开反例稿](https://github.com/cat5779/rl01/pull/93)与[公开联合耦合稿](https://github.com/cat5779/rl01/pull/92)只作为候选材料核验；正文自包含重写了承重步骤，且普通随机序证明不依赖后者的联合 factor coupling。

## 最终状态表

| 主张 | 裁决 |
|---|---|
| C5.7 的 FK 双侧普通随机序支配，对任意可数群 | **PROVED** |
| 支配证明覆盖 FK 为零、非满秩、无谱隙、复 Hermitian | **PROVED** |
| “optimal” 若指每个固定核都取等 | **DISPROVED** |
| “optimal” 若只指单个 FK 数值的全类一元界不可一致改进 | **PROVED** |
| 有限群、所有可数 amenable 群逐点取等 | **PROVED** |
| 双侧谱隙、有限支撑群代数子类仍逐点取等 | **DISPROVED** |
| 所有非 amenable 群/核的阈值分类 | **INCOMPLETE** |
| \(R(\Gamma,S)\) 的自然非归一化 trace 同形界 | **PROVED** |
| 多轨道 normalized trace 的同形界 | **DISPROVED** |
| 依赖 \((D(Q),D(I-Q))\) 两个数值的最优统一改进 | **INCOMPLETE** |
