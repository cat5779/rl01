# S75 Cycle26 独立数学审查

## 总裁决

**`VERIFIED_SCOPED_STAR_TOOL / DISPROVED_EXTENSIONS / RATE_TARGET_INCOMPLETE`。**

我支持 S75 在其明示作用域内的核心结论：

1. 一中心、单 parity 叶子的实际 DPP 星形中，固定核心的
   \(\Chi\) 在新增叶子后具有无条件、实际权重平均的严格正漂移；
2. 两输出平均恒等式、真实偏置矩的符号、pair 势的非负系数幂级数和
   整个实际 support 内的一致绝对收敛均成立；
3. 有限矩递推给出无需全 word 枚举的下界，式 (19) 的余尾估计正确；
4. 星形内部的一侧长 pair 增量非负，式 (22)--(23) 的双侧截断包络正确；
5. 一般 sine 几何中“每个 individual cross pair 都有非负无条件漂移”
   是假的；即便在星形内，固定旧背景 word 后的条件漂移也可为负。

这些结果没有闭合标准两 parity interval halo，也没有消除 full-score
core/pair 截断。\(0.26275\) 是无限星形中一个最近邻 pair 的下界，
不是实际全线 \(V\)；约 107974 的量是残余统一支付包络，也不是实际
全线 \(V\)。完整高对比度熵率目标仍未完成。

审查来源为：

`C:/game/gameproject/showa100/math/sa-dispatch-20260918/harvest/CYCLE26/S75/original/S75/`

包含 `RESULT.md`、严格 certificate、浮点 diagnostics 及其输出。

## 1. 星形几何与实际 DPP

核为

\[
K=
\begin{pmatrix}
d&z^*\\ z&dI
\end{pmatrix},
\qquad
T=\sum_i|z_i|^2<\min(d,1-d)^2.
\]

非平凡特征值是 \(d\pm\sqrt T\)，所以该条件恰好保证严格正压缩。
叶子主边缘核是 \(dI\)，故叶子输出在边缘律下独立
Bernoulli\((d)\)。正文没有把这种边缘独立误写成给定中心后的条件独立。

在 \(\rho=1/2\) 的真实 sine 核中，固定中心，只取相反 parity 叶子，
任意两叶之差为偶数，因此叶间 sine kernel 元素为零，正好得到上述
星形。此时

\[
d=a+c/2,qquad
w_i=|z_i|^2=\frac{c^2}{\pi^2(i-j)^2},
\qquad
\sum_iw_i=c^2/4.
\]

合法 \(a\) 给出 \(d>c/2\) 且 \(1-d>c/2\)，所以
\(c^2/4<\min(d,1-d)^2\)。这覆盖每个固定
\(0<c<1\)、全部合法内部 \(a\)，但没有给出靠近端点或
\(c\to1\) 的统一 gap 常数。

## 2. 两输出平均恒等式

对条件二点核

\[
C=\begin{pmatrix}\alpha&z\\\bar z&\beta\end{pmatrix},
\qquad s=|z|^2,
\]

四个实际原子是

\[
p_{11}=\alpha\beta-s,quad
p_{10}=\alpha(1-\beta)+s,quad
p_{01}=(1-\alpha)\beta+s,quad
p_{00}=(1-\alpha)(1-\beta)-s.
\]

逐 word 代入二点逆矩阵可得

\[
p_y f_{ij}
=\frac{s}{p_y}
+\sigma_i\sigma_j\log\frac{D_y}{D_y+s}.
\]

四个 logarithm 相加后，独立 cell 分母抵消，留下

\[
\mathcal F(\alpha,\beta,s)
=s\sum_y\frac1{p_y}
+\log\frac{p_{11}p_{00}}{p_{10}p_{01}}.
\]

因此式 (6) 是真实输出权重下的精确恒等式，包含 opposite-sign words，
不是把 pair 势用某个典型 word 代替。

独立重放中，直接全 word score 期望与该 reduced formula 的最大误差为
\(4.69\times10^{-16}\)。

## 3. 偏置矩、幂级数与 support

经 particle-hole 反射可取 \(d\ge1/2\)，置 \(u=1-d\)、

\[
t=\beta-1/2=d-1/2+\sum_k\xi_k,
\]

其中

\[
\xi_k=
\begin{cases}
-w_k/d,&\text{概率 }d,\\
w_k/u,&\text{概率 }u.
\end{cases}
\]

于是

\[
\mathbb E\xi_k^\ell
=w_k^\ell\{(-1)^\ell d^{1-\ell}+u^{1-\ell}\}\ge0.
\]

\(\ell=1\) 时为零；偶数阶显然为正；奇数
\(\ell\ge3\) 时由 \(u\le d\) 得到非负。独立性和 multinomial 展开
继承到 \(\mathbb Et^k\ge0\)。这一步正确处理了非中点偏置；证明并未
暗中假定对称 Bernoulli 增量。

从四个 cell 的几何级数与 logarithm 级数展开，得到正文式 (11)。
奇数 \(n\) 只贡献非负偶次系数；偶数 \(n\) 中

\[
(d^{-n}-u^{-n})
\{(1/2+t)^{-n}-(1/2-t)^{-n}\}
\]

的两个因子在奇次系数上同号为负，乘积仍非负。故

\[
\mathcal F(d,1/2+t,s)=\sum_{k\ge0}b_kt^k,
\qquad b_k\ge0.
\]

显式系数式 (13) 的 parity 条件与 \(2^{n+k+1}\) 因子正确；保留
\((n,k)=(3,2)\) 确实给出

\[
b_2\ge256s^3(d^{-3}+u^{-3}).
\]

如果其他叶总权重为 \(S\)，则实际 support 满足

\[
|t|\le d-1/2+S/u.
\]

由 \(S+s<u^2\) 得

\[
d-1/2+S/u<1/2-s/u.
\]

所以整个 support 严格落在收敛圆内；不是只对高概率 words 成立。
这也合法化了期望与幂级数的交换。可数无限星形时，
\(\sum w_i<\infty\) 给出 Schur 和的绝对收敛，固定紧致合法参数区间
可保留一致正 margin。

## 4. 实际权重正漂移

新增叶增量 \(\xi_r\) 独立、中心化，且所有矩非负。因此

\[
\mathbb E[(t+\xi_r)^k-t^k]
=\sum_{\ell=1}^k\binom{k}{\ell}
\mathbb Et^{k-\ell}\mathbb E\xi_r^\ell\ge0.
\]

与 \(b_k\ge0\) 合并，得到无条件 pair 正漂移。保留 \(k=2\) 后

\[
\mathbb E\Delta f_{ij}
\ge
\frac{256(d^{-3}+u^{-3})}{du},w_i^3w_r^2.
\]

对核心叶求和即为 S75 式 (3)，逐叶揭示即为式 (4)。虽然证明重排为
“先平均 core pair，再平均独立叶”，塔式法则保证它等于原 filtration
下使用真实条件概率 \(q\) 的无条件期望；没有把 \(q\) 冻结成 \(d\)。

新的独立随机重放采用 seed 7526、36 个严格合法星形、最多 7 个站点：

- reduced formula 与直接全 word score 的最大误差：
  \(4.6835\times10^{-16}\)；
- 实际漂移减去定理下界的最小余量：
  \(2.3037\times10^{-9}>0\)。

这是浮点一致性检查；一般结论来自上述证明。

## 5. 无枚举矩工具和余尾

矩递推

\[
M_k^{\rm new}
=\sum_{\ell=0}^k\binom{k}{\ell}M_{k-\ell}\mu_\ell(w)
\]

每个叶子对次数 \(0,\ldots,D\) 花费 \(O(D^2)\) 算术，而不是枚举
\(2^{|B|}\) 个背景 word。因为 \(b_k,M_k\ge0\)，部分和是严格下界。
对 \(r_s<R'<R_s\)，逐项用

\[
r_s^k\le(r_s/R')^{D+1}(R')^k,qquad k>D,
\]

即可得到式 (19)。

独立例子取 \(d=.63,s=.02\)、其余权重
\(.015,.01,.008\)、\(D=12\)：

| 量 | 值 |
|---|---:|
| 全 word 精确浮点期望 | 0.00845543689343 |
| 矩级数下界 | 0.00845471234873 |
| 实际余项 | \(7.24545\times10^{-7}\) |
| 式 (19) 上界 | 0.000316605309 |

support 半径为 0.21919，选择的 \(R'=0.33257\)，收敛半径为
0.44595；全部矩和截断系数均非负。余尾包络较松，但方向与量纲正确。

## 6. 星形空间尾

令

\[
e=\min(d,1-d),qquad
\gamma_\star=e^2-c^2/4>0.
\]

其他叶权重至多 \(c^2/4-s\)，所以每个 independent-cell product
至少为 \(\gamma_\star+s\)。把
\(x=s/(\gamma_\star+s)\) 代回绝对级数，得到

\[
|\mathcal F|\le4s^2/\gamma_\star^2.
\]

中点时偶数 \(n\) 消失，级数从 \(n=3\) 起，故

\[
0\le\mathcal F\le4s^3/\gamma_\star^3.
\]

再用双侧 \(r^{-4}\)、\(r^{-6}\) 积分尾，正文式 (22)--(23) 的
系数分别为 \(8/3\)、\(8/5\)，没有遗漏双侧因子。独立求和到距离
200000，再用积分上界补上无限余尾；在 \(R=2,5,10,20\) 均严格
落在两个公式包络内。

## 7. 严格 certificate 与两个反例

### 7.1 作者 certificate 实际重跑

在不触碰作者目录的前提下，我导入 `s75_certificate.py` 并直接调用
`main()`；这执行全部 80 位外向取整区间计算，但避开脚本末尾写文件的
分支。结果为

`PASS_EXACT_RATIONAL_INTERVAL_CERTIFICATES`，且返回对象与作者随附
`S75_CERTIFICATES.json` 完全一致。

区间实现的乘除对所有 endpoint 组合外向取整；Machin 公式、交错
atan/sin/cos 级数和 atanh-log 余尾的下一项/几何包络均方向正确。

### 7.2 一般 \(\rho=.45\) 的三点稀疏 mask

真实 sites 为 \(\{0,3,4\}\)，核心 pair 为 \(\{0,3\}\)，揭示 4。
严格 certificate 给出

\[
\mathbb E\Delta f_{03}
\in[-0.000177080,-0.000177078].
\]

独立全配置 determinant/score 枚举得到

\[
-0.00017707914473614545.
\]

这是真实 sine 主压缩，不是伪造星形。但它仅反驳“一般几何中每个
individual pair 的无条件漂移都非负”；稀疏三点 mask 不是连续 interval
core，也没有对其余 pair 求和，故不是完整 \(\Chi\)、\(\Phi\) 或熵率反例。

### 7.3 固定旧背景与无条件星形

在半密度星形参数

\[
c=.95,quad a=1/2000,quad
\text{core}=\{0,7\},quad
\text{old leaves}=\{-1,1\},quad r=-3,
\]

固定旧背景 word `00` 后，严格区间为

\[
[-7.4327,-7.4325]\times10^{-7}<0.
\]

独立全配置条件枚举得到
\(-7.43263519118\times10^{-7}\)。但是平均全部四个旧背景 words 后，
严格区间和独立枚举分别给出

\[
1.3875271794819\times10^{-5}>0,
\]

\[
1.3875271794856\times10^{-5}>0.
\]

二者不矛盾：S75 定理从未声称给定每个旧背景的条件漂移非负；它依赖
实际偏置矩在旧背景律下的抵消，只断言对旧背景全部平均后的正漂移。

## 8. 无限星形下界不是全线量

在 \(c=.95,a=1/40\) 的半密度中点，最近邻 pair 权重
\(s=c^2/\pi^2\)。使用

\[
\sum_{n\in\mathbb Z,\ n\text{ odd}}|K(0,n)|^4=c^4/48
\]

和式 (18)，严格 certificate 给出

\[
\mathbb Ef_{\rm nearest}(G_{\rm infinite\ star})
>0.26275.
\]

重跑区间为

\[
[0.262755862074718609606873,
  0.262755862074718609606874].
\]

独立浮点复算为 0.26275586207471846。该逆矩阵与期望都属于“中心加
单 parity 叶”星形边缘；标准 full-line score 还包含另一 parity 及其
叶间耦合。因此这个数不得当作 \(V_{m,L}\)、全线 \(\Chi\) 或熵曲率余量。

## 9. rate 接口及仍欠支付

取标准核心 \(I=\{1,2\}\)，星形只观察中心 2 与 odd sites。要回到完整
interval halo，仍须揭示缺失 parity。S72 单侧比较只能给出

\[
V_{2,L}\ge\frac12
\{L_L(a)-\Gamma_\Chi\eta_\delta\mathscr D_L\},
\]

其中 \(\mathscr D_L\) 是完整 score 的真实 missing-parity 能量。Ward
粗界为

\[
\mathscr D_L\le2(2/\delta-4).
\]

此外还有独立的 full-score core/pair 截断项
\(2C_{\log}\widehat\tau(2)\)。在
\(c=.95,J=[.02,.03],\delta=.02\) 下，我独立复算：

| 残项 | 统一包络 |
|---|---:|
| full-score core/pair | 486.9287385765 |
| missing parity | 107488.0202261590 |
| 合计 | 107974.9489647355 |

所以 0.26275 星形下界远不能支付当前完整接口。约 107974 只是使用
Ward cap 后的最坏统一上界，并不表示实际全线 \(V\) 等于或接近该量；
反过来，也不能因为包络巨大就宣称熵非凹。

S75 真正消除的是“保持一中心星形几何的叶揭示损失”。仍未消除：

1. 另一 parity 的补全；
2. full-score core/pair truncation；
3. 任意密度下可接回标准 interval-core 的同类结构；
4. 整个 \((37/40,1)\) 的连续参数负曲率证书。

## 10. 最终边界

- **认证：** 星形实际律正漂移、显式下界、零损失星形望远镜、无枚举
  moment 工具、星形空间尾。
- **严格证伪：** 一般 sine individual pair 无条件正漂移；逐旧背景
  条件星形正漂移。
- **有限诊断：** 36 个新随机星形及直接全配置反例复现。
- **未证明：** 两 parity interval-core 总漂移、full-score 可负担截断、
  全线 \(V\) 正下界、完整熵率凹性。

因此 S75 是一个正确且有方向性的局部工具，但目前仍不是完成
\((37/40,1)\) 的全局证书。
