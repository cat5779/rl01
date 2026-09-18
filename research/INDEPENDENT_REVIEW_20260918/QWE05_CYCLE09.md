# QWE05 独立审查：泊松跳数提升确实支付了非线性插值项，但反向条件删除 KL 仍是目标级瓶颈

审查日期：2026-09-18

被审查提交：`randomcat4/dpp-stationary-entropy` PR #126，QWE05 完整结果包

审查对象：`QWE05_RESULT.md`、`README.md`、两份 Python 程序、JSON/CSV/log 附件，以及任务包指定的 S14/SA05 背景材料

## 1. 总结裁决

**裁决：`PARTIALLY VERIFIED — NEW J_m PAYMENT VERIFIED, FULL TARGET INCOMPLETE`。**

QWE05 的核心新增结论可以认证：在冻结的循环 Fourier-DPP 模型、`c=19/20`、`a_*=1/40`、`xi_*=1/1520` 下，存在与 `n,m` 无关的常数 `K`，使充分大的偶数 `n` 及 `4<=m<n/2` 满足

\[
\mathcal J_m\le K\frac{1+\log n}{n}.
\]

结合已经审查过的精确非负计数通量，确实得到

\[
\sum_{m=3}^{k-1}\omega_{n,m}\mathcal J_m
=O(\sqrt n\log n)=o(n).
\]

这相对于原有账本是**真正的新优势**：此前未支付的完整非线性插值积分被统一控制，而且没有冻结计数权重、没有把实际输出 KL 换成径向 KL、没有对静态 KL/`chi^2` 不等式作非法微分，也没有重复使用 S14 的响应项 Dirichlet 预算。

但是，完整目标

\[
W_n^{\rm rel}=\sum_l\pi_l''(a_*)R_l(a_*)\ge-o(n)
\]

仍未证明。现有推导只给出

\[
W_n^{\rm rel}
\ge -2\sum_{m=3}^{k-1}\omega_{n,m}\mathcal C_m
-O(\sqrt n\log n),
\]

其中 `C_m` 是实际真律与修正律在均匀删除下丢失的**反向条件 KL**。提交者明确把

\[
\sum_m\omega_{n,m}\mathcal C_m=o(n)
\]

列为尚未证明的充分条件，没有把它伪装成已完成结论。这个边界陈述是诚实且正确的。

因此：QWE05 证明了一个重要的局部闭合，但没有完成 PR #126 的目标级闭合，也没有建立实际渐近反例。

## 2. 已认证的证明链

### 2.1 精确删除账本与符号方向

任务所用的精确恒等式是

\[
R_{m+1}-R_m
=\mathcal C_m+\eta_mR_{m,\xi}+\mathcal J_m.
\]

结合补集对称和 S14 已核验的计数输运，

\[
W_n^{\rm rel}
=-2\sum_{m=0}^{k-1}\omega_{n,m}(R_{m+1}-R_m),
\qquad \omega_{n,m}\ge0.
\]

QWE05 对 `eta_m R_{m,xi}` 只使用了所需方向的上界

\[
\sum_m\omega_{n,m}\eta_mR_{m,\xi}\le O(\sqrt n),
\]

没有写成绝对值估计或双侧 `O(sqrt n)`。这与 S14 独立审查的限定完全一致，符号方向正确。

### 2.2 泊松均匀化引理

令 `L` 为总跳率至多一的可逆 Markov 生成元，`M=I+L`，`G_T=e^{TL}r`。把热流写成

\[
G_T=\mathbb E[M^Nr],\qquad N\sim\operatorname{Poisson}(T),
\]

后，热时间变化的输出似然比是潜在 Poisson 跳数似然比的条件期望。数据处理与条件 Jensen 给出的前向/反向 `chi^2`、KL 以及平方余项界均成立。特别是

\[
\left\langle
\frac{(G_T+\ell LG_T-G_{T+h})^2}{G_T}
\right\rangle
\le e^{h^2/T}-1-\frac{h^2}{T}+\frac{(h-\ell)^2}{T}
\]

的代数展开正确，并且对任意初始密度成立，因此确实绕开了“逐个高模式估计后无法求和”的旧障碍。

在本模型的时钟尺度下，提交中使用的

\[
T=\tau_m\gtrsim m,\qquad h,\ell=O(m/n),
\qquad h-\ell=O(m/n^2)
\]

推出修正删除失配 `chi^2=O(n^{-1})` 和全密度源平方范数 `O(n^{-2})`；量级和归一均核对无误。

### 2.3 实际核的点态似然比

QWE05 不是只在径向替代模型中工作。它先固定一个真实输入集合，把实际条件重叠核写成有限 Jacobi 多项式，再对同一先验平均，最后用正半群比较得到完整输出的点态界

\[
f_m/g_m\le M_n,
\qquad M_n=9e^{1/4+D_0b_0^2}n^{2D_0}.
\]

本审查逐项核对了以下关键环节：

- Stieltjes 根表示给出的 `tau_xi>0`、`tau_xixi<=0` 及上下界方向正确；
- 小噪声锚点使用的是同一实际输入条件核，不是把完整 Fourier 输出替换为径向熵；
- 源项在度零、度二方向消失后确实化为中心化二次式；
- Jacobi 变换 (4.11a) 给出全负实根，因而倾斜分布可分解为 Bernoulli 和；
- 有限多项式恒等式 (4.11b) 与度二匹配的归一一致；
- `|b|<=13/7`、`H>=261m^2/1600` 以及势函数积分产生多项式 `n^{2D_0}`，常数虽粗但足够。

本审查还用精确有理数独立重算了 (4.11b)：对所有偶数 `8<=n<=40` 及 `2<=m<=n/2`，多项式每一项系数完全相等。该检查不依赖作者的浮点程序。

### 2.4 有界似然下的 Poisson score 迁移

若联合空间上 `N~Poisson(T)`、`0<=H<=M`、`EH=1`，提交证明

\[
\mathbb E[H(N-T)^2]\le16(Tu+u^2),
\qquad u=1+\log(2M).
\]

其尾积分论证成立：原 Poisson 偏差的 Chernoff 界乘以 `M` 后，把阈值参数平移 `log(2M)`，即可由一个指数尾变量控制。这里不要求 `H` 与 `N` 独立。

将 `H` 取为输出似然比并条件化到输出，得到

\[
\mathbb E_f\left(\frac{LG_T}{G_T}\right)^2,
\quad
\mathbb E_f\left|\frac{L^2G_T}{G_T}\right|
\le 32\left(\frac uT+\frac{u^2}{T^2}\right).
\]

二阶 Poisson score `((N-T)^2-N)/T^2` 的归一正确。实际插值的似然比由

\[
f_t\le(1+t_m\mu_m)f_m,
\qquad g_t\ge e^{-h}g_m
\]

与上一节的点态界合法连接，不是另加未证明假设。

### 2.5 非线性插值项

完整移动参考 KL 恒等式保留了参考加速项：

\[
\mathcal J_m=\int_0^1(1-t)
\left[
Q_t-(s'(t))^2
\left\langle f_t-g_t,
\frac{L(L+\gamma I)g_t}{g_t}\right\rangle
\right]dt.
\]

对真实线性插值 `f_t=f_0+tv`，点态 `f_t>=(1-t)f_0` 给出

\[
\int_0^1(1-t)\left\langle\frac{v^2}{f_t}\right\rangle dt
\le t_m^2v_m.
\]

再用 Poisson score 界控制 `Lg_t/g_t`、`L^2g_t/g_t`，可得

\[
\mathcal J_m
\le2t_m^2v_m+
\frac{S_m^2}{2}
\left(3\mathcal A_m+\gamma\sqrt{\mathcal A_m}\right).
\]

尺度代入后，第一项是 `O(1/n)`，第二项一致为 `O((1+log n)/n)`。`m<=3` 时未匹配模式为空，`J_m=0`。因此加权总量确为 `o(n)`。

## 3. 不能据此跨越的瓶颈

### 3.1 `C_m` 不是径向 KL，也不是修正边缘失配

`C_m` 是 KL 在删除映射下的数据处理缺口，即上层真/修正分布之间被删除映射丢掉的条件信息。作者附件中的径向 KL、修正删除边缘 `chi^2`、热时间源范数都不是这个量。

因此下面的推理不合法：

\[
\chi^2(\mathsf K_m\widehat q_{m+1}\Vert\widehat q_m)=O(n^{-1})
\quad\Longrightarrow\quad
\mathcal C_m=o(n^{-1/2}).
\]

左端只控制修正律删除后的边缘移动；右端要求控制真律与修正律在删除纤维内的条件区别。

### 3.2 一个严格的信息论障碍

均匀删除算子从 `(m+1)`-子集层映到 `m`-子集层。对 `m<k`，上层状态数大于下层状态数，因此这个线性 Markov 算子有非平凡核。取严格正的基准分布 `q` 和非零、总质量为零且 `Kdelta=0` 的核方向 `delta`；对足够小的 `epsilon`，

\[
p=q+\epsilon\delta
\]

仍是概率分布，并满足 `Kp=Kq`，但 `D(p||q)>0`。KL 链式法则此时给出

\[
D(p\Vert q)-D(Kp\Vert Kq)=D(p\Vert q)>0.
\]

所以，仅凭删除后的边缘完全相同，甚至不能推出条件删除 KL 为零。更弱的边缘 `chi^2=O(n^{-1})` 或热源 `O(n^{-2})` 当然也不能单独推出所需的加权 `C_m=o(n)`。

这不是实际 Fourier-DPP 的反例；它严格说明当前工具类型缺少一条“纤维条件稳定性”输入。要完成目标，至少还需要以下之一：

1. 对实际 Fourier-DPP 删除纤维的条件似然比/条件 Fisher 信息作统一控制；
2. 证明 `C_m` 与 `eta_mR_{m,xi}+J_m` 存在可加权利用的负向抵消；
3. 直接证明加权和 `sum omega_m C_m=o(n)`。

在没有这类新输入时，(0.4) 已是当前方法能够合法推出的边界。

## 4. 数值与附件复现

两份程序均先完整阅读，再在隔离副本中运行；没有修改收件目录。

### 4.1 完整小规模模型

`qwe05_verify.py --small-max 18 --radial-max 4096` 成功完成：

- 完整 Fourier-DPP 枚举覆盖偶数 `n=8,10,12,14,16,18`；
- 最大账本误差约 `8.3e-15`；
- 计数质量误差约 `1.8e-13`；
- 径向测试覆盖 24 个 `(n,m)`，最大 `n=4096`；
- 热核质量及两种指数计算的差异保持在约 `1e-14` 量级。

这些结果验证了有限规模归一、删除账本和程序实现，但不替代渐近证明。

### 4.2 新解析引理压力测试

`qwe05_analytic_checks.py` 成功完成：

- 源项 270 例；
- 小噪声锚点 30 例；
- 插值 24 例；
- `max |b| = 0.999999761 < 13/7`；
- `max source/bound = 0.123674`；
- `min H/(261m^2/1600) = 1.14668`；
- `max interpolation bound ratio = 3.89e-5`；
- 最大热质量误差约 `1.1e-14`。

隔离复现与随附摘要仅有浮点末位差异，所有断言通过。

### 4.3 轻微交付缺陷

正文与 README 都列出 `analytic_source_checks.csv`，但收到的结果目录缺少这个文件。程序会正常重新生成它，且 `analytic_check_summary.json`、运行日志和另外两张解析表均已随附。因此这是可修复的打包遗漏，不影响上面的数学裁决；但若要求“清单与附件逐项一致”，提交者应补入该 CSV。

## 5. 逐项状态表

| 声明 | 状态 | 审查意见 |
|---|---|---|
| 泊松均匀化的 KL/`chi^2`/平方余项界 | VERIFIED | 条件期望、归一与常数方向正确 |
| 修正删除边缘 `chi^2=O(n^-1)` | VERIFIED | 是修正边缘结论，不是 `C_m` 结论 |
| 全密度源平方范数 `O(n^-2)` | VERIFIED | 对任意初值，未逐模求和 |
| 实际核点态 `f_m/g_m<=poly(n)` | VERIFIED | Jacobi、Bernoulli 分解、势比较链闭合 |
| 有界似然下的 Poisson score 迁移 | VERIFIED | 不需要似然比与跳数独立 |
| `J_m<=K(1+log n)/n` | VERIFIED | 参考加速残差已保留 |
| `sum omega_m J_m=o(n)` | VERIFIED | 使用精确非负通量总质量 `O(n^{3/2})` |
| 响应项的单侧 `O(sqrt n)` 支付 | VERIFIED_SCOPED | 只按下界所需方向使用 |
| `sum omega_m C_m=o(n)` | OPEN | 本次没有证明 |
| `W_n^rel>=-o(n)` | INCOMPLETE | 仍被 `C_m` 阻塞 |
| 实际渐近反例 | NOT CLAIMED / NOT FOUND | 小 `n` 负值不是渐近反例 |

## 6. 最终结论

QWE05 相对于原有方法确有实质进步：它用一个不依赖高模式总质量的 Poisson-uniformization 工具链，合法关闭了完整非线性插值项，并把目标级账本缩减到一个更清楚的条件信息瓶颈。

但这项进步是“瓶颈缩减”，不是“主定理完成”。反向条件删除 KL `C_m` 仍可能贡献 `Theta(n)` 级的不利通量；当前的边缘、径向和热源估计在信息论上不足以排除这一点。故 PR #126 的最强可认证状态应保持为：**新部分定理成立，完整目标仍 INCOMPLETE。**
