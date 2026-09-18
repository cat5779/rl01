# S61 Cycle 10 独立数学审查

审查日期：2026-09-18

对象：`S61_CYCLE10_RESULT.md`、`s61_checks.py`、S61 冻结任务，以及已审查的 S14/QWE05 单侧输入

## 总裁决

**VERIFIED。** S61 的承重结论成立：对冻结的半密度循环 Fourier-DPP、固定 `c=19/20` 和指定 corrected Johnson 时钟，存在与层和 `n` 无关的常数，使

\[
\mathcal C_{l-1}\le K_1\frac{\log n}{l},
\qquad K_0\log n\le l\le n/2,
\]

并且小层的精确计数通量尾被单独支付。因此

\[
0\le\sum_{m=3}^{k-1}\omega_{n,m}\mathcal C_m
\le K\sqrt n\log n=o(n).
\]

结合 S14 与 QWE05 已审查的两个**单侧上界**，合法推出

\[
W_{\rm rel}\ge-K\sqrt n(1+\log n)=-o(n).
\]

这里没有得到 `|W_rel|=o(n)`，也没有得到真块熵率凹性、一般密度结论或端点一致性。S61 完成的是此前 QWE05 留下的有限循环删除纤维条件信息瓶颈。

## 1. 新工具的概率权重与删除归一

作者把上层实际律和修正律写成同一真实 Fourier 投影先验 `mu(A)=det(P_A)` 下的混合：

\[
p(T)=\sum_A\mu(A)t_A(T),\qquad
\widehat p(T)=\sum_A\mu(A)t_A(T)H(|A\cap T|).
\]

由于给定输出层数后的归一只依赖 `|A|=k`，观察 `T` 不会暗中改变混合前的先验；变化被完整保留在 posterior

\[
\rho_T(A)=\frac{\mu(A)t_A(T)}{p(T)}
\]

中。

删除采用概率核 `1/l`，而不是密度删除的 `1/(n-l+1)`。链式法则给出

\[
\mathcal C_{l-1}
=D(p\Vert\widehat p)-D(Kp\Vert K\widehat p)
=\mathbb E_{\widehat P_-}
 \operatorname{Ent}_{\alpha_{\widehat p}}(p/\widehat p).
\]

本审查重新核对了两种平均测度：定义中的条件 KL 以实际删除边缘 `P_-` 平均；纤维熵形式以修正边缘 `Phat_-` 平均，似然均值正好完成换测度。没有冻结移动权重。

## 2. 截断 posterior-transfer 定理

Theorem 2.1 的证明链完整：

1. corrected posterior 满足
   \[
   \widehat\rho_T(A)=\rho_T(A)H(J_T(A))/F(T).
   \]
2. corrected 联合尾 `epsilon` 转成 actual 坏输出质量时显式支付点态因子 `M`：
   \[
   p(\mathcal G^c)\le M\varepsilon/\delta.
   \]
3. 相邻输出 posterior 的耦合若使 overlap 位移至多 `b`，则两个好端点的 normalizer 比满足
   \[
   |\log r(T')-\log r(T)|
   \le bL-\log(1-\delta).
   \]
   这里事件补集确实强迫耦合两端都落在缩小窗口之外，因此两端各自的 corrected posterior 尾均可支付。
4. 一个 retained set 只要含坏扩展就标为坏。对固定坏上层集合求和，正确得到
   \[
   \sum_{S\subset T}P_-(S)
   \le[1+B(n-l)]p(T).
   \]
   该式包含实际上层项和所有 Johnson 相邻项，没有漏掉删除归一。
5. 好纤维上用 Hoeffding 引理控制 log-likelihood 的指数倾斜 KL；坏纤维则用 `p_min/M` 的显式最小 corrected 条件概率支付。

因此

\[
\mathcal C_{l-1}\le
\frac{[bL-\log(1-\delta)]^2}{8}
+D_*\min\left\{1,[1+B(n-l)]\frac{M\varepsilon}{\delta}\right\}
\]

是合法的实际边缘结论，不是“给定潜变量 `A` 后的条件结论”。

## 3. 强 Rayleigh posterior 耦合

Fourier 投影先验的生成多项式为

\[
\det(V^*\operatorname{diag}(x_i)V).
\]

当所有 `Im x_i>0` 时，其虚部在 `C^k` 上正定，所以矩阵不可奇异；故该多项式实稳定。正外场保持实稳定，因此每个 actual posterior 仍是齐次 strong-Rayleigh 律。

本审查核对了 Pemantle--Peres Proposition 2.2 的实际假设：strong-Rayleigh 条件确实蕴含 stochastic covering；对齐次 `k`-集律，在单点条件 `0/1` 下，去掉该坐标后的两个条件律可耦合为相差至多一个元素。改变一个正外场只改变该点 indicator 的混合概率，而不改变两个条件律，所以可把两次外场变化分别耦合。

当 `T'=T-i+j` 时，两次外场变化使潜在 `k`-集至多发生两次交换；再加输出集合自身的一次交换，得到

\[
\big||A\cap T|-|A'\cap T'|\big|\le3.
\]

方向、齐次性和退化 indicator 情形均已覆盖。该步骤没有假设 corrected posterior 具有 covering 性质。

参考：[Pemantle--Peres 原文](https://arxiv.org/abs/1108.0687)。

## 4. Johnson 热流的实稳定性与 overlap 分解

初始 `l`-子集核的生成多项式是 `A` 内变量的 elementary symmetric polynomial，实稳定。Johnson 生成元可精确写成

\[
L_l=\frac1{l(n-l)}\sum_{i<j}(\sigma_{ij}-I).
\]

对每一对坐标，

\[
e^{s(\sigma-I)}
=\frac{1+e^{-2s}}2I+rac{1-e^{-2s}}2\sigma
\]

是 Borcea--Brändén--Liggett partial symmetrization 定理允许的凸组合。Lie--Trotter 极限与稳定多项式的系数闭性因此覆盖指定的连续时间 Johnson 半群。

这与 BBL Proposition 5.1 对有限 symmetric exclusion process 的结论完全一致；该命题的证明正是用 Theorem 4.20 加 Trotter 乘积。作者没有把离散一步保持性未经证明地外推到连续时间。

将 `A` 内变量设为一个计数变量、外变量设为一，得到的真实及 corrected overlap pgf 都只有严格负实根且全系数为正，故两者都可表示为 `l` 个参数严格位于 `(0,1)` 的独立 Bernoulli 和。

参考：[BBL 原文及 Proposition 5.1](https://www.ams.org/journals/jams/2009-22-02/S0894-0347-08-00618-8/S0894-0347-08-00618-8.pdf)。

## 5. 时钟二次匹配、方差与均值

有限系数恒等式给出真实 overlap 的二次中心矩

\[
\mathbb E_wH_2=H_0\theta,
\qquad \theta=Q_{l-2}^{(d)}(\xi_*)/Q_l^{(d)}(\xi_*).
\]

而 Johnson 生成元满足 `L H_2=-gamma_2 H_2`；指定时钟正好令 `exp(-gamma_2 tau)=theta`，所以 corrected overlap 的同一二次矩精确匹配。

真实 overlap 是超几何 Bernoulli 分解的 `z`-倾斜。逐 Bernoulli 比较给出真实方差下界。对 corrected overlap，精确公式

\[
\widehat v
=v_0(1-\theta)+\frac{l^2}{4}
 (\theta-\theta^{n/(n-1)})
\]

与 `1-theta>=1/z` 给出同阶下界。于是两者统一满足

\[
\nu l\le v,\widehat v\le l/4,
\qquad \nu=1/(8z).
\]

由二次矩匹配、实际均值离中心至少 `cl/2` 以及方差上界，得到

\[
|\mu-\widehat\mu|\le1/(2c).
\]

这里不需要、也没有声称两个方差接近。

## 6. 局部连续概率比

Lemma 5.1 对线性方差的 Poisson-binomial 和给出

\[
\left|\log\frac{\Pr(X=j+1)}{\Pr(X=j)}\right|
\le C_\nu\left(\frac{|j-\mathbb EX|}{N}+N^{-1/2}\right)
\]

于线性大小的中等偏差窗口内成立。证明中的三个承重点均有效：

- 特征函数界 `exp[-2v sin^2(t/2)]` 给出相邻质量差 `O(1/v)`；
- 均值为整数时的统一局部中心极限定理给中心质量下界 `Omega(v^-1/2)`；
- 一般整数 `j` 用指数倾斜移到中心，倾斜方差满足 `e^{-|s|}v<=v(s)<=e^{|s|}v`，所选窗口保证存在 `|s|<=1/2` 的倾斜参数。

两套 overlap 律的均值只差常数，因此在半径 `R` 的共同窗口上

\[
|\Delta\log H|\le
K_c\left((R+1)/l+l^{-1/2}\right).
\]

没有把全局多项式似然比误当成局部梯度界。

## 7. 大层、坏纤维与计数尾

取

\[
\delta=n^{-2},\qquad
R=3+\sqrt{\frac l2[\log(2M_n)+10\log n]}.
\]

corrected overlap 的 Bernoulli Chernoff 界给 `epsilon<=1/(M_n n^10)`。因此：

- actual 坏输出质量至多 `n^-8`；
- 坏 retained-set 质量至多 `O(n^-7)`；
- 即使粗用 `D_*=O(n)`，坏纤维贡献仍只有 `O(n^-6)`。

当 `l>=K_0 log n` 时，窗口落入局部概率比引理允许的范围，且

\[
L=O(\sqrt{\log n/l}),
\]

从而得到 `C_(l-1)<=K log(n)/l`。

对 `m+1<n/4`，使用粗界 `C_m<=log M_n`。精确计数多项式归一后是两个、每个都含 `n-2` 个 Bernoulli 的分布之混合，均值为 `k-1`。Hoeffding 给

\[
B_{n,\lfloor n/4\rfloor}\le n^2e^{-n/32}.
\]

由于 `sum_{m<=r}omega_(n,m)=B_(n,r)`，小层包括 `m=3` 的全部通量被指数尾支付。其余层使用 `l>=n/4` 的 `K log(n)/n` 界和总通量 `O(n^{3/2})`。中心边 `m=k-1` 也在大层证明范围内。

## 8. 复现

在隔离目录中运行作者程序，结果全部通过：

- 153 个精确有理系数实例，覆盖偶数 `8<=n<=40`；
- 15 个完整空间 Fourier-DPP 实例，覆盖 `8<=n<=16`；
- 15 个 overlap 大尺度矩实例，最大 `n=8192`；
- KL 链式法则最大误差 `4.09e-16`；
- 纤维熵表示最大误差 `3.28e-17`；
- 实际/修正 latent mixture 最大误差 `1.69e-16`；
- 显式两次外场耦合边缘误差 `3.50e-10`，交换数至多二；
- 大尺度热矩公式最大误差 `1.10e-10`。

这些检查只作有限验证；渐近认证来自上面的证明链。

## 9. 对 PR128 资源分配的影响

S61 改变了此前的瓶颈分配：固定 `c=19/20`、半密度、有限循环模型中的 `W_rel>=-o(n)` 不应再列为开放主攻项。QWE05 的非线性插值支付与 S61 的删除纤维支付已经接合。

但 PR128 不能把 S61 直接当作全局定理复用。仍需独立解决：

1. **真块/非循环转移：** S61 使用精确循环 Fourier 投影和循环 Johnson corrected law；真 Toeplitz 块的边界、接缝及导数极限仍需支付。
2. **一般密度与参数：** 证明冻结在半密度和 `c=19/20`。posterior 耦合工具较一般，但 overlap 二次匹配和常数验证不是一般密度定理。
3. **dyadic/尺度拼接：** S61 是单一有限 `n` 的层间估计，不提供块尺寸之间的次可加、dyadic 传递或导数交换。
4. **端点 `c->1`：** 作者参数满足 `z=(1+xi)/xi=((1+c)/(1-c))^2`（在 `c=19/20` 时为 `1521`）；方差常数 `nu=1/(8z)`、中等偏差阈值和最终常数都会退化，没有端点一致性。
5. **其余曲率账：** `W_rel` 只是完整熵曲率分解的一项。其他真律、线性或极限预算必须另证。

因此本审查支持把“有限循环删除条件信息”从核心开放项移出，把资源转向真块识别、一般密度、dyadic 传递和端点控制。

## 10. 状态表

| 声明 | 状态 |
|---|---|
| 截断 posterior-to-fiber 工具 | VERIFIED |
| actual Fourier posterior overlap 位移至多三的耦合 | VERIFIED |
| Johnson semigroup 保持实稳定性 | VERIFIED |
| 两 overlap 律的 Poisson-binomial 分解 | VERIFIED |
| 二次时钟匹配、线性方差、均值差有界 | VERIFIED |
| 局部连续概率比引理 | VERIFIED |
| `C_(l-1)<=K log(n)/l`（大层） | VERIFIED |
| 小层精确 count-flux 尾，包括 `m=3` | VERIFIED |
| `sum omega_m C_m<=K sqrt(n)log n=o(n)` | VERIFIED_ONE_SIDED |
| `W_rel>=-o(n)` | VERIFIED_ONE_SIDED |
| `|W_rel|=o(n)` | NOT CLAIMED |
| 真块/一般密度/dyadic/端点结论 | OPEN / OUT OF SCOPE |

## 最终意见

S61 是一个真正改变项目分工的承重结果。它没有从删除边缘反推纤维信息，而是新增并验证了 actual posterior 的纤维局部正则性；坏 posterior、坏输出和坏 retained fiber 的换测度成本全部显式支付。证明能够承受从 QWE05 到 `W_rel>=-o(n)` 的连接。

建议接受 S61 的固定模型结论，同时在任何上层汇总中保留三条醒目标注：**仅单侧、仅固定循环模型、没有端点一致性。**
