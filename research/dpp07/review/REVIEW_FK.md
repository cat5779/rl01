# 独立对抗审查：`proof14.tex`

## 裁决

**实际定理：CORRECT。**

对任意可数离散群 \(\Gamma\) 及任意与左正则作用交换的复 Hermitian 正压缩 \(0\le Q\le I\)，稿件确实证明
\[
 \operatorname{Bern}(\operatorname{FK}(Q))
 \preceq \mathbf P^Q
 \preceq
 \operatorname{Bern}(1-\operatorname{FK}(I-Q)).
\]
它还正确证明了第 89--91 行明确定义的较弱锋利性：只把界看成所显示 FK 数据的、在整个算子类上一致适用的函数时，不能统一改进。

**原题完整覆盖：未完成。** Lyons 的 Conjecture 5.7 在给出两条支配界后说 “these bounds are optimal”。结合其所称被推广的 \(\mathbb Z^d\) 结果，Lyons--Steif Theorem 5.11 对每个固定 \(f\) 给出当且仅当阈值，这里的实质读法是逐核最优：对给定 \(Q\)，最大的被支配 Bernoulli 参数应为 \(\operatorname{FK}(Q)\)，最小的支配 Bernoulli 参数应为 \(1-\operatorname{FK}(I-Q)\)。稿件第 89--91 行明确放弃该结论，第 286--290 行只用标量核证明类上一致锋利。因此不能把全文宣告为对原猜想（含实质最优性）的完整解决；它完整证明了原猜想的两条普通 stochastic-domination 不等式，并证明了一个弱于逐核最优性的统一锋利性陈述。

## 证明核查

### 1. 有限维方向导数：成立

第 146--173 行的恒等式可在基 \(f_B(S)=\mathbf1_{\{B\subseteq S\}}\) 上逐项验证。\(I\) 方向给出
\(\sum_{i\in B}\det K_{B\setminus\{i\}}\)，\(-rK\) 方向给出 \(-r|B|\det K_B\)。条件化后正好得到第 148--151 行。包含指标函数构成 \(\mathbb R^{2^V}\) 的基，故线性延拓到任意 \(f\)。这里没有把只对事件成立的式子错误延伸到一般递增函数。

### 2. 条件概率与 odds 下界：成立

第 124--143 行中 \(L=K(I-K)^{-1}>0\)，所有配置概率均正。Schur 补给出的条件 odds 正确。随着 \(A\) 扩大，约束向量空间扩大，变分最小值下降；在 \(A=V\setminus\{i\}\) 时为 \(1/(L^{-1})_{ii}\)。由于 \(L^{-1}=K^{-1}-I\)，从 odds 转为概率后恰为
\[
q_i(A)\ge ((K^{-1})_{ii})^{-1}.
\]
于是 \(r\ge\max_i(K^{-1})_{ii}\) 确保第 175--177 行每一系数非正。方向没有反转。

### 3. FK 等值路径与正收缩性：成立

在第 183--209 行的谱隙假设下 \(p=\operatorname{FK}(Q)>0\)。第 191--194 行路径满足 \(K_0=Q\) 与 \(\operatorname{FK}(K_t)=p\)；标量齐次性来自归一化群迹 \(\tau(I)=1\)。第 198--200 行的范数收敛由 \(Q/t\to0\) 及连续函数演算得到。对 \(0<\lambda\le1\)，\(\lambda+t\ge(1+t)\lambda\)，故第 206--209 行确实给出 \(0<K_t<I\)。

第 211--218 行的微分也正确：
\[
K_t'=a_t\bigl(I-\tau(K_t^{-1})K_t\bigr).
\]
正因子 \(a_t\) 只重参数化有限维引理中的方向，不改变导数符号。

### 4. 逆压缩与群量词：成立

第 223--240 行使用
\[
((K_t)_V^{-1})_{ii}\le \langle K_t^{-1}\delta_i,\delta_i\rangle.
\]
给出的变分证明方向正确：把全空间上确界限制到 \(\ell^2(V)\) 只会减小确界值。与左正则平移交换使右侧对 \(i\) 恒等于 \(\tau(K_t^{-1})\)。因此每个有限支撑递增柱函数均满足沿路径期望不增。这一步只需要可数离散群和正则表示的不变性，没有暗用 amenability、soficity 或有限生成。

### 5. 正则化、奇异端点与上界：成立

第 248--269 行的
\(Q_\eta=(Q+\eta I)/(1+2\eta)\)
具有双侧谱隙并范数收敛到 \(Q\)。单调收敛确实处理 \(\int\log\lambda=-\infty\)；再计入趋于 1 的分母 \(1+2\eta\)，得到 \(\operatorname{FK}(Q_\eta)\to\operatorname{FK}(Q)\)。有限柱配置概率由包含概率作有限 inclusion--exclusion，故可过极限。\(\operatorname{FK}(Q)=0\) 时下界退化为空集点质量，逻辑完整。

第 271--279 行的补集律 \(\mathbf P^Q\mapsto\mathbf P^{I-Q}\) 与序反转正确，给出上界。第 281--284 行的 \(\operatorname{FK}(Q)=1\Rightarrow Q=I\) 使用谱测度与群迹忠实性，端点处理正确。

### 6. 从有限柱函数到普通 stochastic order：成立，但紧致性范围应严格理解

第 77--80 行可成立：可数 \(\Gamma\) 时 \(2^\Gamma\times2^\Gamma\) 是紧致可度量空间。对每个有限 \(V\)，有限边缘的 stochastic order 给出 Strassen 单调耦合；将其任意扩张为全空间耦合后，有限约束族具有有限交性质，紧致性给出同时满足所有有限边缘及 \(X\subseteq Y\) 的全局耦合。这里紧致性只把所有有限边缘约束拼合起来，并不把有限群事件（尤其“全体点均占据”）搬到无限群。

## 锋利性与原题语义

第 286--290 行的标量例子完整证明如下命题：若只知道 \(x=\operatorname{FK}(Q)\)，则对所有此类 \(Q\) 一致有效的下 Bernoulli 参数不可能超过 \(x\)；若只知道 \(y=\operatorname{FK}(I-Q)\)，则一致有效的上参数不可能低于 \(1-y\)。这是稿件第 89--91 行所定义的实际定理，因而实际定理正确。

但标量例子不能证明任意固定非标量 \(Q\) 的阈值最优。有限群中可用全占据事件得到 \(p^{|\Gamma|}\le\det Q\)，从而 \(p\le\operatorname{FK}(Q)\)；这一论证不能直接移植到无限群，因为不存在有限的“全群占据”柱事件。稿件也没有为任意无限、特别是非 amenable 群构造有限集合族 \(A_n\) 使 \((\det Q_{A_n})^{1/|A_n|}\to\operatorname{FK}(Q)\)。因此逐核必要性没有被证明。

原始文献的量词对比是明确的：

- Lyons 2014, Conjecture 5.7：对所有 \(\Gamma\)-equivariant positive contractions 给出这两条界，并称 “these bounds are optimal”；同段明确说它推广 Theorem 5.2，且即使有限群也开放。原文：[Conjecture 5.7, p. 158](https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf)。
- Lyons--Steif, Theorem 5.11：对每个固定可测 \(f:\mathbb T^d\to[0,1]\)，\(\mu_p\preceq P^f\) 当且仅当 \(p\le\operatorname{GM}(f)\)，且 \(P^f\preceq\mu_q\) 当且仅当 \(q\ge1-\operatorname{GM}(1-f)\)。这不是仅在整个函数类上的标量例子锋利，而是逐 \(f\) 的必要充分条件。原文：[Theorem 5.11](https://rdlyons.pages.iu.edu/pdf/dyn.pdf)。

因此，第 50 行“下面的精确一般群表述就是 ICM 原文所述表述”若连同第 89--91 行的解释一起理解，会缩窄 ICM 中“optimal”的实质含义；第 44--48 行将 Lyons--Steif 的逐核最优性与随后较弱的类上一致锋利并列，也容易造成覆盖强度相同的印象。数学不等式证明不受影响，但完整原题覆盖声明不能成立。

## 可抽离的小理论

证明中可独立抽离出以下有限状态比较原理。

**逆对角控制的 DPP 切向单调性。** 设 \(V\) 有限、\(0<K<I\)，且 \(H\) 为 Hermitian 矩阵。若存在表示
\[
H=c(I-rK),\qquad c\ge0,\qquad r\ge\max_{i\in V}(K^{-1})_{ii},
\]
则对所有递增 \(f:2^V\to\mathbb R\)，
\[
\left.\frac d{ds}\mathbf E^{K+sH}f\right|_{s=0}\le0.
\]
其承重事实是一个更基础的条件强度下界：有限 DPP 的任意单点完全条件概率满足
\[
\mathbf P^K(i\in S\mid S\setminus\{i\}=A)
\ge ((K^{-1})_{ii})^{-1}.
\]
再结合正算子的逆压缩不等式，就得到如下路径原则：若一条严格正压缩路径满足
\(K_t'=c_t(I-r_tK_t)\)、\(c_t\ge0\)，且对每个有限压缩 \(V\) 有
\(r_t\ge\max_{i\in V}((K_t)_V^{-1})_{ii}\)，则相应 DPP 对所有递增柱函数随 \(t\) 单调下降。FK 等值路径只是这一原则的一次群不变应用。
