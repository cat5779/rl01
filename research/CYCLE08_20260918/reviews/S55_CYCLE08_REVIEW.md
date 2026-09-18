# S55 Cycle 08 独立数学审查

## 总裁决

**VERIFIED_SCOPED。** 我支持 S55 的主结论：对实际偶数循环投影族与真实半密度 sine 族，在任意固定紧致合法内参数集

\[
D\Subset\{(c,d):0<c<1,\ |d|<(1-c)/2\}
\]

上，

\[
\sup_{(c,d)\in D}\left|
\frac1n\partial_d^2H_n^{\rm cyc}(c,d)-h_c''(d)
\right|\longrightarrow0.
\]

证明没有从熵值的 `o(n)` 误差中求导，而是先在有限体把完整 Shannon Hessian 重组为锚点响应，再证明该响应在所有外部符号词上一致收敛且空间尾可和，最后用真实 Toeplitz 块的全锚点平均和精确弦恒等式识别极限。此次审查没有发现破坏主定理的符号、因子、边界或极限交换错误。

但对“相对于原有方法，在 \(c=37/40\) 是否真正有优势”的答案是：**没有直接定量优势。** 已有双预算法在这个点直接给任意有限正压缩、全合法位移区间的

\[
H''\le -n/50,
\]

并可由三点 Jensen 不等式传到平稳熵率。S55 只给紧致内区间的定性曲率传递，不给物理体积收敛率，也不独立证明 \(h_c''<0\)。所以在恰好 \(37/40\) 处，旧方法对“凹性与余量”更强；S55 的新优势在另一个方向：它把循环量 \(R_n,J_n\) 以及 corrected-law 账本合法地接到真实 sine 熵率，因而是继续攻 \(c>37/40\) 的接口工具。

## 审查对象与依赖边界

主审对象：

- `S55_CYCLE08_RESULT.md`；
- `S55_CYCLE08_checks.py` 及归档输出；
- 原任务 `prompts/CYCLE08/S55.md`。

核对的已审依赖：

- S51 Cycle 06 独立审查，只用于真实半密度 sine 熵率在合法内区间满足 \(h_c''=-\Gamma_c\) 的命名识别；
- S43 Cycle 05 独立审查和原始稿，只用于 corrected-law 账本及 KL 方向。

没有把待审 S51 C1 端点重整化、S52、S54 或 QWE02 当作前提。

## 1. 完整有限体二阶响应

对有限 DPP 的实际原子概率，作者从行列式多线性得到

\[
p_d'(y)=\sum_i(2y_i-1)p_{d,V\setminus i}(y_{-i}).
\]

因此移动观察律的导数为

\[
\frac d{dd}\mathbb E_df_d
=\mathbb E_d\partial_df_d+
\sum_j\mathbb E_{d,C\setminus j}\Delta_jf_d.
\]

把它应用于完整熵的一阶恒等式而不是单点条件熵，得到

\[
H_V''=-\sum_i\mathbb E\partial_dh_i
-\sum_{i\ne j}\mathbb E\Delta_jh_i.
\]

第二项确为有序对；其期望使用删去 \(i,j\) 后的实际边际。独立复算确认没有遗漏概率律导数、score 项或额外的 `1/2`。

固定外部词下，令 \(B_z=S_z/2+T\)、\(v=B_z^{-1}\xi\)、\(q=k_0-\xi^*B_z^{-1}\xi\)，则

\[
q'=1+\|v\|_2^2,
\qquad
\partial_d\log\frac q{1-q}
=\frac{1+\|v\|_2^2}{q(1-q)}.
\]

这与直接原子概率 jet 一致。

## 2. 正影响与平方空间尾

翻转第 \(j\) 个外部位后，行列式引理与 Sherman--Morrison 公式给

\[
q_{z^j}-q_z=\frac{\sigma_j|v_j|^2}{o_j},
\qquad
o_j=\frac{w(z^j)}{w(z)}.
\]

统一 non-nullness 给 \(o_j\ge\varepsilon/(1-\varepsilon)\)，故 log-odds 影响满足

\[
0\le \ell_j\le \varepsilon^{-2}|v_j|^2.
\]

关键不只是逐点界，而是

\[
\sum_{j\notin F}\ell_j
\le\varepsilon^{-2}\|1_{F^c}v\|_2^2.
\]

后续 compact-resolvent 论证确实证明右侧在参数与全部符号词上一致趋零，因此没有把单项误差乘上 \(n\)。

## 3. 带符号 resolvent 的一致强收敛

产品拓扑下 \(S_zx\) 对每个固定 \(x\in\ell^2\) 连续。谱隙给所有逆统一界 \(\varepsilon^{-1}\)。因此

\[
(\theta,z)\mapsto(S_z/2+T_\theta)^{-1}\xi_\theta
\]

是进入 \(\ell^2\) 的连续映射，其像是紧集。统一有界的强算子收敛在该紧向量集上一致；由此得到全部符号词的一致 resolvent 收敛和统一坐标尾。这一步只用强收敛，没有暗中要求不可能成立的算子范数收敛。

截断有限个 flip 后，保留部分由 posterior 的一致收敛控制，遗漏部分由上述平方尾控制，故完整响应 \(\mathcal T_n\) 在参数和所有词上一致收敛。实际外部边际的有限 cylinder 概率也一致收敛，于是变化的 observable 与变化的真实概率律可以同时传极限。

## 4. 循环核的 gauge、接缝与真实局部律

对 \(n=2k\)，作者使用与 \(d\) 无关的对角 gauge，精确得到

\[
\widetilde P_n(s,t)=
\frac{\sin(\pi(s-t)/2)}{n\sin(\pi(s-t)/n)}
\quad(s\ne t).
\]

该 gauge 保持全部主子式，故保持实际 DPP 律。稿件没有把有边界 twist 的矩阵误当成普通实 circulant；循环平移性来自原 Fourier 核。

零延拓投影 \(\Pi_n\) 对每个坐标列弱收敛到 \(Qe_j\)，且两边列范数最终都为 \(1/\sqrt2\)，所以列强收敛；再由稠密性得到 \(\Pi_n\to Q\) 强收敛。根列在接缝处仍按循环距离控制，远端平方质量为 `O(1/R)`。这支付了任务中特别要求的 phase、wrap-around 与强收敛升级。

固定 cylinder 的实际概率是有限个收敛矩阵元的行列式多项式，故在紧参数集上一致全变差收敛。有限循环律的平移性又把全锚点和精确化为 \(n\) 倍根响应。

## 5. 全外部极限、所有真块锚点与非循环识别

对任意有限观察集 \(C\supset F_R\)，压缩算子满足一致的 directed strong convergence。因而有限观察 posterior 与响应一致趋于全外部的连续版本；martingale 收敛确认它确实是实际条件概率，而不是形式 resolvent 候选。

对真实 Toeplitz 块，距离边界至少 \(R\) 的锚点误差至多 \(\omega_R\)，边界锚点至多 \(2R\) 个且响应一致有界，故

\[
\left|L^{-1}H_{L,dd}^{\rm true}-C(c,d)\right|
\le \omega_R+4MR/L.
\]

先令 \(L\to\infty\)，再令 \(R\to\infty\)。之后才使用有限体精确弦公式

\[
\Delta_th_c(d)=\int_{-t}^t(t-|s|)C(c,d+s)\,ds
\]

识别 \(h_c''=C\)。因此证明没有对未知速率的熵值误差求两次导数，也没有循环地预设 \(h_c\in C^2\)。

## 6. Ward 恒等式、Toeplitz 泄漏与中点归一化

完整投影在中点满足 \(K(I-K)=bI\)，从而逐外部词

\[
q(1-q)=b(1+\|v\|^2).
\]

真实有限 Toeplitz 压缩则是

\[
q(1-q)=b(1+\|v\|^2)
+c^2x^*(Q_A-Q_A^2)x.
\]

后项非负且通常不为零；单点块已经反驳删掉它的捷径。S55 在主传递中没有误用有限块投影恒等式。

条件二点 cross-ratio 的符号为

\[
\Delta_jh_i=-\log\frac{p_{10}p_{01}}{p_{00}p_{11}}.
\]

代回完整 Hessian 后得到

\[
\frac1nH_{n,dd}^{\rm cyc}=-\frac1b+J_n
=-4-\frac{R_n}{n},
\qquad
\frac{R_n}{n}=\frac{c^2}{b}-J_n.
\]

有序对归一化和符号均正确。全外部 pair sum 的每项由 martingale posterior 识别，整个无限和由平方尾支配，故 \(J_n\to J_\infty\) 不是只凭固定 pair 收敛。

## 7. corrected law 的作用域

从已审 S43 账本

\[
W_n+C_n=R_n+n\Psi_n+o(n),
\qquad
\widehat H_n''=-4n-W_n-C_n+o(n)
\]

和 S55 的实际循环恒等式可得

\[
\frac1n\widehat H_n''=h_c''(0)-\Psi_n+o(1).
\]

稿件保留了 \(\Psi_n\) 的符号不确定性，并正确说明：\(\Psi_n\) 的下界给 corrected curvature 的上界；不能把 corrected 与真实凹性无条件等同。没有使用待审 S54 的更小损失。

## 8. 在 \(c=37/40\) 的相对优势判断

既有双预算法的独立审查确认，`23/25 <= c <= 37/40` 的局部扩展证书本身通过；在 \(c=37/40\) 得到

\[
g_+\le\frac{199}{100}(\mathcal K_{ij}+\mathcal D_{ij}),
\qquad
H''\le-\frac1{200}\mathcal I\le-\frac n{50}.
\]

因此比较如下：

| 性质 | 原双预算法在 \(37/40\) | S55 |
|---|---:|---:|
| 有限维、任意正压缩 | 是 | 否，仅指定循环逼近族 |
| 全合法闭区间 | 是 | 否，仅紧致合法内区间 |
| 显式负余量 | \(1/50\) | 无 |
| 真实熵率值传递 | 三点 Jensen，足以保凹性 | 是，并识别 Hessian |
| 循环 \(R_n,J_n\) 与全外部响应的精确识别 | 否 | 是 |
| 与 corrected-law signed-KL 账本对接 | 否 | 是 |

所以 S55 **不是 \(c=37/40\) 的更强凹性证明**。它也没有闭合此前提出的有限 \(m,L\) 严格不等式

\[
\mathcal W_{m,L}+C_*h_m/m+
\frac{50251200}{2197}(1/m+1/L)<0,
\]

因为 S55 明确不给物理体积速率。它提供的是一个严格弱化瓶颈的合法替代接口：若未来在真实 sine 全外部响应上证明符号，或控制 \(\Psi_n\)，即可无缝回到熵率/修正律；但在 \(37/40\) 本身，旧证书已经更直接、更强。

## 9. 复现记录与最终范围

作者诊断脚本在实际运行时通过：30 个循环参数实例、12 个使用全部锚点的真 Toeplitz 实例，以及一个一般复 Hermitian gapped kernel；gauge 检查至 \(n=64\)。我另在 \(c=37/40\) 独立枚举实际循环律，得到

| \(n\) | \(H_{n,dd}^{\rm cyc}/n\) |
|---:|---:|
| 2 | -22.5985021771 |
| 4 | -19.1350694234 |
| 6 | -16.8627317399 |
| 8 | -15.3320094806 |
| 10 | -14.2576681439 |

这些数值只核对实现与有限恒等式，不证明渐近符号。

最终状态：

- **VERIFIED_SCOPED**：紧致合法内区间的循环到真实 sine 曲率传递；完整 moving-law 二阶响应；全部符号词与空间尾控制；全外部 posterior；所有真块锚点；中点 \(R_n,J_n\) 恒等式与无限 pair sum；corrected-law 账本的正确作用域。
- **NO ADVANTAGE AT \(c=37/40\) FOR SIGN/MARGIN**：旧双预算法已有全区间显式有限维余量。
- **OPEN / NOT CLAIMED**：\(c>37/40\) 的一般凹性、端点或 \(c\to1\) 一致性、\(\Gamma\) 的符号、\(\Psi_n\) 的所需单侧控制，以及任何有限体物理速率。
