# QWE06 / PR127 独立数学审查

## 总裁决

**PARTIALLY VERIFIED WITH EXPLICIT REVIEWER REPAIRS；主目标仍为 INCOMPLETE。**

投稿没有证明

\[
\inf_{a\in I}B_n(a)\ge-r_n,
\qquad r_n/n\to0,
\qquad I=[1/50,3/100],
\]

也没有给出该命题、真实熵凹性或 sine 熵率猜想的反例。

逐项裁决如下。

| 项目 | 裁决 | 说明 |
|---|---|---|
| A1：folded count-flux 恒等式及端点因子 | **VERIFIED** | 直接离散分部求和；有序边与中心边均正确。 |
| A2：\(\omega_m\ge0\) | **AUTHOR GAP / REVIEWER-REPAIRED** | 原稿仅以“对数凹、单峰、均值同侧”推出反射序，此推理一般不成立；本审查用本题特殊 Bernoulli 因子逐配置配对补证。 |
| B：稀有 count layers 的完整 moving-reference 响应为 \(o(1)\) | **AUTHOR GAP / CONCLUSION REPAIRED_SCOPED** | 原稿没有给出 shortest-path 计数、\(f,g\) 两阶导数和端点账；更粗的统一多项式包络足以补出 \(o(1)\)。稿称的特定 \(T_n=O(n^3)\) 不予认证。 |
| C：每个固定 \(a\ne a_*\) 有一半典型质量满足 \(M_L<0\) | **AUTHOR GAP / CLAIM REPAIRED AND VERIFIED** | 原稿只写“微分同一 Fourier 积分”，未给误差控制；统一 differentiated local CLT 可补证，clock 界和 UI 足够完成结论。 |
| C 的加权正部极限 | **VERIFIED AFTER SAME REPAIR** | 由 score 二阶矩和 clock 一致界给统一可积性。 |
| D：\(a-a_*=\beta n^{-1/2}\) 的固定 \(\beta\) 极限 | **VERIFIED_SCOPED** | 固定 \(\beta\) 公式正确；原稿没有完整的 shrinking-window 统一 transition theorem，本审查给出序列三分法。 |
| E：剩余典型层预算及充分方向 | **VERIFIED AS A REDUCTION ONLY** | 公式和充分性方向正确，但 (6.2) 是支付已处理项后的原目标剩余部分，不是新的闭合估计；(6.3) 是未证的更强条件。 |

作者浮点脚本复跑成功，但只实现 negative-damping 诊断；投稿所说的 folded/full-interface 全配置回归没有随本次 PR127 交付可复跑脚本，不能作为独立证据。

## 1. 冻结模型和依赖边界

审查对象是 PR127 完整 `RESULT.md`、`typical_negative_damping.py`、原任务及 QWE06 source packet。冻结：

\[
n=2k,\quad c=19/20,\quad a_*=1/40,\quad
I=[1/50,3/100],
\]

\[
\xi=\frac{a(1-c-a)}c,\qquad
h=\xi_a=\frac{1-c-2a}{c},\qquad
\xi_{aa}=-2/c.
\]

真实对象是实际 cyclic half-Fourier 输出；修正对象只能是任务指定的 degree-two matched Johnson heat law。S14 独立审查只按其明示范围输入；SA05 自审标签不当作认证。

## 2. A：folded flux 恒等式

令

\[
G_a(t)=A_t^kB_t^k,
\quad A_t=1-a-c+(a+c)t,
\quad B_t=1-a+at.
\]

则

\[
\partial_aG_a(t)=(t-1)K_a(t),
\]

\[
K_a(t)=kA_t^{k-1}B_t^k+kA_t^kB_t^{k-1}
=\sum_{r=0}^{n-1}\kappa_rt^r,
\]

所以在约定 \(\kappa_{-1}=\kappa_n=0\) 下

\[
\pi_l'=\kappa_{l-1}-\kappa_l.
\]

由于条件层 KL 只通过 \(\xi\) 变化，

\[
R_{l,a}=hR_{l,\xi},\qquad
R_{l,aa}=h^2R_{l,\xi\xi}-\frac2cR_{l,\xi}.
\]

本模型和指定修正律的补集对称给
\(R_l=R_{n-l}\)，故其 \(\xi\)-导数同样对称。count-score 项为

\[
2h\sum_{l=0}^n\pi_l'R_{l,\xi}
=2h\sum_{r=0}^{n-1}\kappa_r
(R_{r+1,\xi}-R_{r,\xi}).
\]

把边 \(r=m\) 与 \(r=n-1-m\) 配对，得到

\[
2h\sum_{m=0}^{k-1}
(\kappa_m-\kappa_{n-1-m})
(R_{m+1,\xi}-R_{m,\xi}).
\]

因此稿件 (2.1)–(2.2) 的中心边、因子 2 和求和上限均正确。

### 2.1 原稿未证明的反射序

“严格 log-concave/unimodal，且均值位于中心某侧”一般不能推出
\(\kappa_m\) 与 \(\kappa_{n-1-m}\) 的逐点反射序。PR127 没有给本题多项式的额外证明，所以原稿这一行是实质缺口。

### 2.2 审查者修复

设

\[
x=a-a_*,\quad
u=\frac{1+c}{2},\quad v=\frac{1-c}{2},\quad
\rho=\frac12+x.
\]

注意

\[
\frac1nK_a(t)=
[(v-x)+(u+x)t]^{k-1}
[(u-x)+(v+x)t]^{k-1}
[(1-\rho)+\rho t].
\]

所以 \(\kappa_r/n\) 是下列 \(n-1\) 个独立 Bernoulli 之和的概率：

- \(k-1\) 个成功率 \(u+x\)；
- \(k-1\) 个成功率 \(v+x\)；
- 一个成功率 \(1/2+x\)。

把每一对高/低 Bernoulli 的配置 \((H,L)\) 送到
\((1-L,1-H)\)，并翻转中心位。这是成功数 \(m\) 与
\(n-1-m\) 的双射。对 \(x>0\)，令

\[
t_x=\frac{(u+x)(v+x)}{(u-x)(v-x)},\qquad
s_x=\frac{1/2+x}{1/2-x}.
\]

直接展开得

\[
[(u+x)(v+x)](1/2-x)
-[(u-x)(v-x)](1/2+x)
=x[1-2(uv+x^2)]>0,
\]

故 \(t_x>s_x>1\) 在本区间成立。

若某配置有 `#00-#11=A`，中心位为 \(e\)，反射配置与原配置的概率比是

\[
t_x^A s_x^{1-2e}.
\]

当 \(m<k\) 时

\[
n-1-2m=2A+1-2e>0.
\]

若 \(e=0\)，则 \(A\ge0\)，比值至少 \(s_x>1\)；若 \(e=1\)，则 \(A\ge1\)，比值至少 \(t_x/s_x>1\)。因此

\[
x>0\Longrightarrow \kappa_m<\kappa_{n-1-m}\quad(m<k).
\]

对 \(x<0\) 反向，\(x=0\) 相等。又 \(h=-2x/c\)，所以

\[
\omega_m=2h(\kappa_m-\kappa_{n-1-m})\ge0.
\]

最后

\[
\sum_{m<k}\omega_m
\le2|h|\sum_{r=0}^{n-1}\kappa_r
=2|h|n.
\]

这完成了 A，但该关键反射证明属于本审查修复，不属于投稿原证。

## 3. B：稀有层导数尾

Hoeffding 部分正确：实际 count 是 \(k\) 个
`Bern(a+c)` 与 \(k\) 个 `Bern(a)` 之和，所以

\[
\sup_{a\in I}\Pr(|L-n(a+c/2)|>n^{2/3})
\le2e^{-2n^{1/3}}.
\]

问题在于投稿随后只写“counting all shortest Johnson paths”便宣称

\[
|g_\xi/g|=O_I(n),\qquad |g_{\xi\xi}/g|=O_I(n^2),
\]

以及完整 integrand 的 \(T_n=O_I(n^3)\)。没有给出：

1. shortest paths 的下界和 posterior jump-count 尾；
2. \(\tau,\tau_\xi,\tau_{\xi\xi}\) 的组合界；
3. 实际条件密度 \(f\) 的一、二阶 likelihood 界；
4. KL 两次微分中所有 score/reference 项；
5. \(m<4\) 端点为何为零。

所以特定的 `O(n^3)` 主张未由投稿证明。

### 3.1 足够完成尾部结论的较粗修复

所幸 `o(1)` 不需要三次多项式的精确次数，只需任一固定多项式包络。

在 \(I\) 上，四个通道概率

\[
a, a+c, 1-a, 1-a-c
\]

均至少为 \(1/50\)。把实际原子概率写成对 latent \(A\) 的正混合，可逐项对数微分；每个乘积 likelihood 的一阶 score 是 `O(n)`，二阶相对 jet 是 `O(n^2)`。正混合和按 count 条件化保持同阶粗界。因此

\[
|\partial_a\log f_l|\le Cn,\qquad
|\partial_a^2 f_l/f_l|\le Cn^2,\qquad
|\log f_l|\le Cn.
\]

对修正律，写 \(Q=I+L_l\)，

\[
g_\tau(S)=e^{-\tau}\sum_{j\ge0}
\frac{\tau^j}{j!}Q^jr^{\max}(S).
\]

在 \(m\ge4\) 时，clock lower bound 在本固定 \(\xi\)-区间给
\(\tau\ge c_0>0\)；Jacobi 多项式的正系数公式给
\(\tau,\tau_\xi,\tau_{\xi\xi}\le n^{C_0}\)。因为
\(r^{\max}\) 的平均为一，可选一状态 \(T\) 使
\(r^{\max}(T)\ge1\)。任意 \(S\) 与 \(T\) 的 Johnson 距离至多 \(m\)，保留一条 shortest path 即得

\[
g_\tau(S)\ge
e^{-\tau}\frac{\tau^d}{d!}C_l^{-d},\qquad d\le m.
\]

结合 \(r^{\max}\le\binom nl\le2^n\)，得到

\[
|\log g_\tau(S)|\le n^{C_1}.
\]

按投稿 (3.2) 定义 posterior jump count \(J_S\)，

\[
\mathbb E(2^{J_S})=e^\tau g_{2\tau}(S)/g_\tau(S).
\]

上式的对数至多为某固定多项式。Markov 尾
\(\Pr(J_S\ge r)\le \mathbb E2^{J_S}2^{-r}\)
于是给 \(J_S\) 的任意固定阶矩一个统一多项式界。由

\[
\partial_\tau\log g=\mathbb EJ_S/\tau-1
\]

及二阶对应式，\(g\) 的一、二阶 \(a\)-jets 也有统一多项式包络。

把这些界代入移动 KL 的直接两次微分，存在固定 \(C\) 使

\[
\left|R_{l,aa}+2(\pi_l'/\pi_l)R_{l,a}\right|
\le n^C
\]

对所有 \(m\ge4\) 及 \(a\in I\) 成立；这里
\(|\pi_l'/\pi_l|=O(n)\) 由同一 latent score 条件期望给出。
对 \(m\le3\)，Fourier 补集奇模式消去且 degree 0、2 已匹配，故
\(f_l=g_l\)、\(R_l\equiv0\)。

因此

\[
\sup_{a\in I}\left|
\sum_{l\notin\mathcal T_n(a)}\pi_l
[R_{l,aa}+2\varphi_lR_{l,a}]
\right|
\le2n^Ce^{-2n^{1/3}}=o(1).
\]

这修复了 B 的结论，但不认证原稿更尖锐的 `O(n^3)` 包络。

## 4. C：典型负 damping

令

\[
\rho(a)=a+c/2,\qquad
v(a)=\frac{1-c^2}{4}-(a-a_*)^2.
\]

则 \(EL=n\rho(a)\)、`Var(L)=nv(a)`。

### 4.1 原稿的 local-CLT 缺口

投稿给出

\[
\varphi_l=\frac{l-n\rho(a)}{v(a)}+O_{I,K}(1)
\]

但证明只有“differentiate the same Fourier integral”一句。对局部概率微分后再除以 \(\pi_l\)，必须控制导数余项；普通未微分 local CLT 不自动给这个结论。

### 4.2 审查者修复

单对 Bernoulli 的特征函数为

\[
\chi_a(t)=
[1-(a+c)+(a+c)e^{it}]
[1-a+ae^{it}],
\]

count 特征函数是 \(\chi_a(t)^k\)。参数在紧集 \(I\) 上远离 0、1。
把 Fourier 积分分为：

1. `|t| <= n^{-2/5}`：对中心化 `log chi_a(t)` 及其 \(a\)-导数作统一四阶 Taylor 展开；
2. `n^{-2/5}<|t|<=delta`：使用统一 Gaussian 衰减
   \(|\chi_a(t)|^k\le e^{-cn t^2}\)，导数仅增加多项式因子；
3. `delta<=|t|<=pi`：使用 \(\sup_{a\in I}|\chi_a(t)|<1\) 的指数界。

中心区积分给，在每个固定 \(K\) 上一致地

\[
\pi_l=\frac{\phi(x)}{\sqrt{nv(a)}}
[1+O_{I,K}(n^{-1/2})],
\]

\[
\partial_a\pi_l
=\pi_l\left[\frac{l-n\rho(a)}{v(a)}+O_{I,K}(1)\right],
\quad
x=\frac{l-n\rho(a)}{\sqrt{nv(a)}}.
\]

故

\[
\frac{\varphi_L}{\sqrt n}\Rightarrow
\frac Z{\sqrt{v(a)}}.
\]

另外，\(\varphi_L\) 是完整 independent-Bernoulli score 对 count 的条件期望，所以数据处理给

\[
\sum_l\pi_l\varphi_l^2\le C_In.
\]

这也支付后续统一可积性。

### 4.3 clock 项和符号极限

degree-two clock 的 Stieltjes 表示给

\[
0<\tau_{l,\xi},\qquad
0<-\tau_{l,\xi\xi}/\tau_{l,\xi}\le2/\xi,
\]

并由相邻两个 Jacobi 商得到

\[
0\le\gamma_{2,l}\tau_{l,\xi}\le2/\xi.
\]

所以

\[
\frac2c\le
\frac{\Lambda_l}{\tau_{l,\xi}}
\le\frac2c+\frac{4h^2}{\xi}.
\]

对固定 \(a\ne a_*\)，

\[
\frac{M_L}{\tau_{L,\xi}\sqrt n}
=\frac1{\sqrt n}\frac{\Lambda_L}{\tau_{L,\xi}}
-2h\frac{\varphi_L}{\sqrt n}
\Rightarrow -\frac{2h}{\sqrt{v(a)}}Z.
\]

极限连续且关于零对称，因此

\[
\Pr\{m(L)\ge4,\ M_L<0\}\to1/2.
\]

Hoeffding 使加入 \(|L-n\rho(a)|\le n^{2/3}\) 不改变极限。由 score 二阶矩和 clock 一致界还得到 UI，故

\[
\frac1{\sqrt n}\sum_l\pi_l
\left(-\frac{M_l}{\tau_{l,\xi}}\right)_+
\to\frac{2|h|}{\sqrt{2\pi v(a)}}.
\]

该结论只否定“负 damping 只在 rare layers”这一中间规则；它没有给 \(M_l\mathcal D_l\) 的总和赋号。

## 5. D：critical scale 的精确作用域

若

\[
a_n=a_*+\beta/\sqrt n
\]

且固定 \(\beta\)，则 \(h_n=-2\beta/(c\sqrt n)\)。三角阵列版 score CLT 与 clock 界给

\[
\frac{M_L}{\tau_{L,\xi}}
\Rightarrow
\frac2c+\frac{4\beta}{c\sqrt{v_*}}Z,\qquad
v_*=(1-c^2)/4.
\]

因此对 \(\beta\ne0\)，

\[
\Pr(M_L<0)\to
\Phi\left(-\frac{\sqrt{v_*}}{2|\beta|}\right).
\]

固定 \(\beta\) 公式正确。更完整的序列三分法是：令
\(\lambda_n=\sqrt n(a_n-a_*)\) 且 \(a_n\to a_*\)，则

- 若 \(\lambda_n\to0\)，负概率趋于 0；
- 若 \(\lambda_n\to\beta\in\mathbb R\setminus\{0\}\)，趋于上述 Gaussian transition；
- 若 \(|\lambda_n|\to\infty\)，负概率趋于 \(1/2\)。

固定 off-midpoint 情形是第三种的更远版本。投稿没有陈述并证明对所有 shrinking windows 的 uniform rate，所以只能把“crossover scale is \(n^{-1/2}\)”理解为上述序列级量纲结论，不能外推成未写明的统一过渡定理。

## 6. E：剩余预算没有闭合

由 folded identity，B 的尾部支付，以及 S14 已审的单侧
\(R_{m,\xi}\le K_R\)，有

\[
-\frac2c\sum_m\varpi_mR_{m,\xi}
\ge-2K_R/c.
\]

所以只剩

\[
\mathfrak C_n(a)=
h^2\sum_{m\in\mathrm{typ}}\varpi_mR_{m,\xi\xi}
+\sum_{m\in\mathrm{typ\ edges}}\omega_m
(R_{m+1,\xi}-R_{m,\xi}).
\]

若 \(\inf_{a\in I}\mathfrak C_n(a)\ge-o(n)\)，确实推出原目标。
而若典型窗上一致有

\[
(R_{m,\xi\xi})_-\le A_n=o(n),\qquad
(R_{m+1,\xi}-R_{m,\xi})_-\le G_n=o(1),
\]

则利用 \(\sum\varpi_m=1\) 与
\(\sum\omega_m\le2|h|n\) 也足够。

方向正确，但 (6.2) 只是把原目标减去已经支付的 `O(1)+o(1)` 项后重写；它没有降低典型层 signed budget 的本质难度。(6.3) 是更强的局部正则条件，投稿没有证明，也没有证据表明它比直接平均补偿更容易。

## 7. 诊断复跑与独立有限检查

随附脚本复跑输出与投稿表格一致：在 \(a=.02\) 时，negative-damping mass 从

\[
0.209447\ (n=400)
\]

增至

\[
0.468442\ (n=40000),
\]

加权正部也向理论常数 `0.0538229...` 移动。该脚本只检查 C/D 的浮点趋势，不证明 CLT。

本审查另对 `n=4,...,200`、41 个 \(a\)-网格共 4059 组系数重建 \(\kappa\)，未发现 \(\omega_m<0\)；随机补集对称层序列上的 folded identity 最大残差约 `3.4e-16`。这只作 A 的代数回归，正式证明是 §2.2 的逐配置配对。

## 8. 与 S9 及 QWE05 的边界

S9 的障碍涉及 moving count-layer Jensen contribution 的宏观负质量；QWE06 的 C 涉及 within-layer moving-reference identity 中 \(M_l\) 的符号。两者系数、权重和结论不同，不能相互替代。QWE06 的“一半负 damping”不推出总预算线性为负，因为 \(\mathcal D_l\)、正平方和两个 signed pairings 仍随层变化。

QWE05/PR126 当前只收到 `PR126_RESULT_COMMENT.md`。评论声称存在
\(O((1+\log n)/n)\) interpolation remainder 和 `o(n)` flux payment，但完整 `QWE05_RESULT_20260918.md` 与 bundle 尚未收到。本审查没有据该摘要认证 QWE05，也没有替作者重建其证明。

## 9. 最终状态

- **主目标：INCOMPLETE。**
- **A：恒等式通过；非负反射序由审查者补证。**
- **B：稀有层 `o(1)` 可保留；作者 `O(n^3)` 细界未证明。**
- **C：固定 off-midpoint 的 `1/2` prevalence 结论正确，但需要审查者补齐 differentiated local CLT。**
- **D：固定 \(\beta\) 临界公式正确；完整 shrinking-window 作用域按三分法理解。**
- **E：只完成精确定位，没有支付 typical signed budget。**

因此 PR127 是一个有用的局部化与方法障碍结果，但不是 QWE06 目标的闭合，也不是任何 entropy-concavity 反例。
