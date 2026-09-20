# S78 Cycle31 独立数学审查

审查日期：2026-09-20（Asia/Singapore）

## 总裁决

**`VERIFIED_COMPENSATED_RANK_ONE_REVEAL / TWO_ACTUAL_SINE_COUNTEREXAMPLES_CERTIFIED / R4_COROLLARY_REQUIRES_FIXED_PAIR_QUANTIFIER / RATE_TARGET_INCOMPLETE`。**

续稿的核心补偿定理成立。对严格二点条件核 \(C\)，

\[
\mathcal B(C)=\mathcal F(C)-\log\det C-\log\det(I-C)
\]

沿每条秩一 Hermitian 直线是凸的；用每一步真实的条件概率 \(q\) 做 Jensen，可以按实际顺序处理任意有限个不对易秩一揭示。望远镜后的障碍恰是两个反向 KL，而不是未命名余项。在统一谱隙下，每个固定保留 pair 的总支付至多

\[
2\log\frac1{4\delta(1-\delta)}.
\]

半密度无限星形的 20 阶矩加第 21 阶尾也可独立严格重建，得到与续稿相同的

\[
3.7456951075302371\ldots
\le D_{\star,\infty}^{\rm floor}
\le3.7456952529240384\ldots .
\]

两个 actual-sine 负漂移反例均由另写的外向取整区间程序严格复现：同 parity 中心加入使原始 \(f_{0,-3}\) 漂移为负但补偿漂移为正；双中心下新增 opposite-parity 叶使 \(\Chi\) 漂移为负。作者导出的四个证书未取得，本审查不声称重跑它们。

唯一需要实质改写的数学表述是“第一交互缺陷为 \(O(R^{-4})\)”的量词。该结论对固定保留 pair \((p,i)\)、令新中心 \(q\) 远离时正确；若允许 \(i\) 随 \(q\) 移动，则不一致成立。取 \(i=q+1\) 时，式中的直接项

\[
|b_{qi}|^4=(c/\pi)^4
\]

与 \(R=p-q\) 无关。故公开稿必须写明“固定 \((p,i)\)”或加入 \(|q-i|\gtrsim |R|\)；这不影响任意 block 的 barrier theorem，却禁止把该 \(R^{-4}\) 包络无条件用于 growing-core 的所有移动 pairs。

约 \(107974.95\to490.6744\) 的 220 倍改进是**证明方法的误差包络削减**，不是熵率目标闭合。未变的 full-score core/pair 项仍为 \(486.9287\)，扣除基线与星形下界后仍约为 \(490.391684>0\)，并且 growing core 的 \(O(k\ell)\) 累积尚未解决。

## 分项裁决

| 对象 | 裁决 | 说明 |
|---|---|---|
| 初稿 \(\mathcal F\) 实际权重公式 | CORRECT_EXACT | 四个二点输出原子的真实权重平均 |
| 初稿 \(M_2(\delta)\) 半凸性 | CORRECT_BUT_SUPERSEDED | 任意 Hermitian 方向成立；续稿秩一补偿更强 |
| 初稿矩阵鞅与 \(Q\le1/2\) | CORRECT | 使用移动真实 \(q\)，不要求秩一更新交换 |
| 初稿 block Ward 支付 | CORRECT_SCOPED | 继承 PR61 已审计 Ward 接口 |
| 初稿 \(k=2\) 叶揭示负漂移 | CERTIFIED_INDEPENDENTLY | 外向取整区间严格为负 |
| \(\mathcal F-\ell\) 秩一平方和 | CORRECT_EXACT | 每个 \(s/p_y\) 项化为平方，另留 \(a_{10}^2+a_{01}^2\) |
| 非交换逐次揭示望远镜 | CORRECT | 每步沿自己的秩一直线应用凸性，未交换矩阵 words |
| 终端反向 KL 表示 | CORRECT_EXACT | 由 Bayes 恒等式逐个 \(11,00\) 输出得到 |
| 固定 pair 谱隙常数 | CORRECT | 初始 barrier 上界与终端 barrier 下界直接相减 |
| 星形 barrier 及 20-moment 数值 | CERTIFIED_INDEPENDENTLY | 独立矩递推与外向取整尾界复现原区间 |
| 第一交互 \(R^{-4}\) | CORRECT_AFTER_QUANTIFIER_FIX | 只对固定保留 pair 或 \(|q-i|\gtrsim|R|\)；不对移动 \(i\) 一致 |
| 中心加入 raw-sign 反例 | CERTIFIED_INDEPENDENTLY | 原始漂移负、补偿漂移正 |
| 220 倍改善 | CORRECT_ARITHMETIC_METHOD_BOUND | 只削减旧接口误差，不证明目标符号 |
| 完整熵率凹性 | INCOMPLETE | \(486.9287\) core/pair 支付和 \(O(k\ell)\) 累积仍在 |

## 1. 初稿：粗半凸工具正确但已被续稿取代

对

\[
C=\begin{pmatrix}\alpha&z\\\bar z&\beta\end{pmatrix},\qquad s=|z|^2,
\]

四个原子概率为 \(p_{11},p_{10},p_{01},p_{00}\)，初稿定义

\[
\mathcal F(C)=s\sum_y\frac1{p_y}
+\log\frac{p_{11}p_{00}}{p_{10}p_{01}}.
\]

这是 PR65 已审计的两输出实际权重平均。沿一般 Hermitian 方向写

\[
a_y=(\log p_y)',\qquad \ell_y=(\log p_y)'',
\]

则一个 cell 的二阶导确为

\[
\left(\frac{s}{p_y}+\epsilon_y\log p_y\right)''
=\frac{s''-2s'a_y+sa_y^2}{p_y}
+\left(\epsilon_y-\frac{s}{p_y}\right)\ell_y.
\]

由 \((s')^2\le2ss''\)、signed resolvent 的谱隙界以及初稿列出的四个 \(s/p_y\) 上界，得到

\[
D^2\mathcal F(C)[H,H]\ge-M_2(\delta)\|H\|_F^2.
\]

常数虽松但方向正确。条件 pair 核满足真实矩阵鞅关系，故半凸化后 Jensen 给出初稿的 Frobenius 方差支付。又因 \(0\preceq C\preceq I\)，

\[
\mathbb E\|C_{\rm fine}-C_{\rm coarse}\|_F^2
=\mathbb E\operatorname{tr}C_{\rm fine}^2
-\mathbb E\operatorname{tr}C_{\rm coarse}^2
\le\operatorname{tr}C_{\rm coarse}(I-C_{\rm coarse})\le\frac12.
\]

所以初稿 \(M_2/4\) 的 fixed-pair cap 成立。它在 \(c=.95,\delta=.02\) 给出 \(47537.632653\ldots\)，加上 \(486.928738\ldots\) 后为 \(48024.561391\ldots\)。这比旧 \(107974.948965\ldots\) 好约 2.248 倍，但续稿已经用精确补偿把它替代。

## 2. 续稿：秩一平方和恒等式

令

\[
\ell(C)=\log\det C+\log\det(I-C),\qquad
\mathcal B=\mathcal F-\ell.
\]

在 \(C(t)=C+t vv^*\) 上，置 \(h=v_1\overline v_2\)。每个 signed determinant \(p_y(t)\) 都是 \(t\) 的仿射函数；若

\[
a_y=\frac{p_y'}{p_y}
=v^*(C-\operatorname{diag}(1-y))^{-1}v,
\]

则 \(a_y'=-a_y^2\)。同时 \(z(t)=z+th\)，所以

\[
\left(\frac{s}{p_y}\right)''
=\frac{2|h-a_yz(t)|^2}{p_y(t)}.
\]

从 \(\mathcal F\) 减去 \(\ell=\log p_{11}+\log p_{00}\) 后只剩 \(-\log p_{10}-\log p_{01}\)，其二阶导分别是 \(a_{10}^2,a_{01}^2\)。因此

\[
\mathcal B''
=\sum_y\frac{2|h-a_yz|^2}{p_y}
+a_{10}^2+a_{01}^2\ge0.
\]

这是精确恒等式，不使用谱隙常数，也不把一般方向的半凸性误当作矩阵全局凸性。它只需要揭示两端及中间线段保持严格 pair kernel；实际 DPP 条件核满足这一点。

## 3. 真实揭示、非交换更新与反向 KL

单站揭示的两个端点为

\[
C_1=C-\frac{bb^*}{q},\qquad
C_0=C+\frac{bb^*}{1-q},
\]

并且 \(qC_1+(1-q)C_0=C\)。二者与 \(C\) 位于同一秩一直线上，故 \(\mathcal B\) 的凸性给出

\[
q\mathcal F(C_1)+(1-q)\mathcal F(C_0)-\mathcal F(C)
\ge q\ell(C_1)+(1-q)\ell(C_0)-\ell(C).
\]

对多个站点逐次应用即可。第 \(r\) 步只使用该步的真实 \(q_r\) 和真实秩一方向；矩阵更新之间无需交换。因此任意有限 block 的结论是合法望远镜，而不是把非交换中心写成 pairwise additive。

对给定粗背景，令 \(P_R\) 是新增 block 的实际律。Bayes 给出

\[
\frac{P_R^{11}(r)}{P_R(r)}
=\frac{\Pr(11\mid r)}{\Pr(11)}.
\]

于是

\[
\mathbb E_R[\log\Pr(11\mid R)-\log\Pr(11)]
=-D(P_R\Vert P_R^{11}),
\]

对 \(00\) 同理。两式相加即为续稿的终端 reverse-KL 表示。独立枚举中两边误差为 \(6\times10^{-100}\)。

## 4. 谱隙保持和固定-pair 常数

条件更新后的上下谱隙由 \(K-\delta I\) 与 \(I-K-\delta I\) 的 Schur complement 保持。若每个条件 pair 的特征值仍在 \([\delta,1-\delta]\)，则

\[
\ell(C_{\rm terminal})
\ge2\log[\delta(1-\delta)].
\]

另一方面任意 \(2\times2\) strict kernel 满足

\[
\ell(C_{\rm initial})
=\sum_{r=1}^2\log[\lambda_r(1-\lambda_r)]
\le2\log\frac14.
\]

故总 barrier loss 至多

\[
2\log\frac1{4\delta(1-\delta)}.
\]

这是每个固定保留 pair 的总 block 支付，与 block 中新增站点个数无关；对 \(k\ell\) 个保留 cross pairs 求和仍然是 \(O(k\ell)\)。

## 5. 星形 barrier 与独立矩证书

在一中心星形中，保留 pair 的一个对角保持为 \(d\)，另一个写成 \(d+t\)，且 \(\mathbb Et=0\)、

\[
\mathbb Et^2=\frac{\sum_{\ell\ne i}w_\ell^2}{d(1-d)}.
\]

沿该标量方向，谱隙给出

\[
\ell''(t)\le-\frac2{(1-\delta)^2}.
\]

因此强凹性直接产生续稿的负方差修正。两个对称 base determinants 的乘积只依赖 \(d(1-d)\)，且该量在 \(d=1/2\) 最大；负方差项也在 \(d=1/2\) 最不负，所以整个上界确在中点最大。

中点令 \(A_0=1/4-s\)。若 \(u\) 是其他叶造成的对角偏移，

\[
\ell(C_\star)
=2\log A_0
-\sum_{n\ge1}\frac{u^{2n}}{n(4A_0^2)^n}.
\]

对 sine star，

\[
|u|\le2T,\qquad T=c^2/4-s<A_0,
\]

故全 support 严格位于收敛域。独立程序用 Rademacher cumulants 和 Bell recurrence 精确生成到 42 阶矩；第 21 项以后逐点使用 \(|u|/(2A_0)\le T/A_0\) 支付几何尾。再用 Machin 公式的有理交错级数包住 \(\pi\)，所有 Decimal 运算和 logarithm 外向取整，得到

\[
\begin{aligned}
D_{\star,\infty}^{\rm floor}\in[&3.7456951075302371445688510467130,\\
&3.7456952529240383889998002404104].
\end{aligned}
\]

这严格包含续稿的显示区间。它是 spectral-floor **支付上界的认证值**，不是实际 full-line reverse KL 的测量值。

## 6. 第一交互 \(R^{-4}\) 的正确量词

续稿的一步粗界

\[
\mathbb E\Delta\mathcal F
\ge-\frac2{\delta^3}
\mathbb E(|\tau|^2+|b_{qi}|^2)^2
\]

可由 barrier Hessian 和真实 \(q\in[\delta,1-\delta]\) 得到。真实 sine overlap 也确有

\[
S_2=\sum_\ell |b_{p\ell}|^2|b_{q\ell}|^2
=\frac{c^4}{2\pi^2R^2}.
\]

由 \(S_4\le S_2^2\)，

\[
\mathbb E\tau^4=O(R^{-4}).
\]

但完整缺陷还有 \(2|b_{qi}|^2\mathbb E\tau^2+|b_{qi}|^4\)。若固定 \((p,i)\) 而令 \(|q-p|=|R|\to\infty\)，则 \(|q-i|\asymp|R|\)，这两项也都是 \(O(R^{-4})\)。若量词允许 \(i=i(q)\)，取 \(i=q+1\) 即有

\[
|b_{qi}|^4=(c/\pi)^4,
\]

完全不衰减。独立探针在 \(R=10,20,40,80\) 上均得到同一常数 \(0.0083617067088\ldots\)。

所以合法版本是：**对固定保留 pair \((p,i)\)，第一个远中心的缺陷为 \(O_{p,i,c,\delta}(R^{-4})\)**。不能宣称对所有 retained leaves 一致，也不能据此消除 growing core 的 \(O(k\ell)\) 障碍。

## 7. 两个 actual-sine 反例的独立严格证书

独立程序直接对真实半密度 sine 主压缩枚举全部 DPP words；没有随机矩阵替代。它从 Machin 公式构造 \(\pi\) 的有理区间，并对 determinant、Schur complement、四 cell、logarithm 和期望全程外向取整。

### 7.1 Same-parity 中心加入

对 \(P=\{0,-3\}\)、旧集合 \(\{0,-3,1,3\}\)、新增中心 \(-4\)，得到

\[
\mathbb E\Delta f_{0,-3}
\in[-0.001933130713983040159308864984082,
-0.001933130713983040159308864984081]<0.
\]

同时

\[
\mathbb E\Delta\ell
\in[-0.158200253002973652106393280,
-0.158200253002973652106393279],
\]

所以

\[
\mathbb E\Delta(\mathcal F-\ell)
\in[0.1562671222889906119470844149006591,
0.1562671222889906119470844149006592]>0.
\]

这同时严格证伪 raw monotonicity 并严格验证补偿方向。

### 7.2 双中心下 opposite-parity 叶加入

对 centers \(\{0,10\}\)、core leaf \(7\)、旧叶 \(-3\)、新增叶 \(-1\)，

\[
\mathbb E\Delta\Chi
\in[-4.912434017602194,
-4.912434017602193]\times10^{-7}<0.
\]

这与初稿和续稿的显示区间一致。两个反例都只否定零支付 reveal sign，不是 Shannon entropy concavity 的反例。

## 8. 率接口与真实剩余量

续稿把一 pair 的 missing-parity 支付由初稿 \(M_2Q/2\) 换成 star barrier：

\[
\mathbb Ef_{12}(G_{A_L})\ge L_L(a)-D_{\star,L}.
\]

在 \(c=19/20,\delta=1/50\) 下，采用严格上端点

\[
D_{\star,\infty}<3.745695253
\]

并保留 PR65 中已审计的独立 full-score core/pair 支付

\[
486.9287385765045\ldots,
\]

得到

\[
490.674433829429\ldots .
\]

旧包络与新包络之比为

\[
\frac{107974.9489647355\ldots}{490.674433829429\ldots}
=220.0541571364\ldots .
\]

算术和接口方向都正确，但这只是最坏误差包络的改善。即使远尾消失，再减去 \(1/50\) 基线和 \(0.26275\) 星形下界，仍为

\[
490.391683829\ldots>0.
\]

因此不能写成“高对比度种子已闭合”，更不能外推到全部 \((37/40,1)\)、任意密度或完整 entropy-rate concavity。

## 9. 精确剩余义务

1. 将 \(486.9287385765\ldots\) 的 full-score core/pair truncation 降到可由基线和星形势支付的尺度。
2. 对 growing two-parity core，把逐 pair 的 \(O(k\ell)\) barrier 累积降到 \(O(k+\ell)\) 或证明独立的 block-cut cancellation。
3. 若使用第一交互空间尾，必须保持固定 retained pair 的量词，不能让叶随新增中心移动后仍引用 \(R^{-4}\)。
4. 给出连续参数区间而非单个 \(c=.95,\rho=.5\) benchmark 的最终符号证书。
5. 作者导出证书到达后可做来源重放；在此之前，本审查只认证可见证明和这里另写的独立区间证书。

最终状态：**精确 log-determinant 补偿定理和两个反例通过；初稿粗界被合法取代；空间衰减需补固定-pair 量词；率目标仍远未闭合。**
