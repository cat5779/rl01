# S45 Cycle 04 独立数学审查报告

## 总评

- **可见正文完整性：COMPLETE_VISIBLE_REVIEW。** 已审查完整可见的 `S45_EARLY_RESULT.md`。作者所述附件写入失败只影响文件交付，不构成数学失败；本报告不依赖未取得附件，也未读取哈希文件。
- **entropy-drop clock inequality：VERIFIED。** 对实际对称排斥 semigroup，熵产生 `I(s)` 单调不增，故

\[
 sI(s)\le F(0)-F(s).
\]

 与精确时钟链式法则结合，正文式 (3) 的全部符号、归一化和 `Lambda` 消去均正确。
- **“新工具”措辞需收窄。** 这条强于 `sI(s)<=F(0)` 的不等式已经明确出现在旧 S13 上界证明中。S45 的新推进是**不再丢弃终端项 `F(s_l)`，并用既有 pair-mode 定理给它线性下界**；不是首次建立 `sI(s)<=F(0)-F(s)`。
- **初始熵预算：VERIFIED。** 投影 DPP 的 maximal-overlap 初始律满足 `F_l(0)<=min(l,n-l)log2`；Hadamard、Cauchy–Binet 和粒子–空穴补集论证完整。
- **中央旧输入：ACCEPTED_DEPENDENCY_AND_SPOT_CHECKED。** `results/S13/PROOF.md` 给出中央 overlap saddle、三阶矩控制和可微有限修正；`results/S13/AUDIT.md` 已独立接受

\[
 \theta_{n,l}(z_*)\to c^2,
 \qquad
 \partial_z\log\theta_{n,l}(z_*)
 \to\frac{(1-c)^3}{2c(1+c)}
\]

 及终端 `F_l(s_l)>=nJ_pair(c)-o(n)`，均在 `|l-n/2|<=n^(2/3)` 上一致。S45 把它们称为“已建立”有足够的库内依据，而不是只引用作者摘要。
- **旧正下界：ACCEPTED_SEPARATE_RESULT。** `liminf C_n/n>=1.404539...` 已在独立 S13 audit 中通过 scoped 审查。它不是 S45 新证明，也不是新上界的必要前提；只能作为同一 corrected-law 量的另一个独立结果并列。
- **全层与尾部：VERIFIED。** 实际 `pi_l` 是两组 Bernoulli 之和，Hoeffding 给 `2exp(-2n^(1/3))`；全层 clock quotient 有固定 `c` 的统一界。因此补带对 `C_n/n` 的贡献趋零。准确说这是 `n^(1/3)` 尺度的 stretched-exponential 尾，而非 `exp(-cn)`。
- **新渐近上包络：VERIFIED_SCOPED。** 对每个固定 `0<c<1`，沿偶数 `n`，

\[
 \boxed{
 \limsup\frac{C_n(c)}n
 \le
 \frac8{(1-c^2)(-\log c)}
 \left[\frac{\log2}{2}-J_{\rm pair}(c)\right].
 }
\]

 在 `c=19/20` 时右端为 `499.631158492115...`。
- **旧上界与新上界性质不同。** `843421.367...` 是每个偶数 `n>=4` 都成立的全层有限 `n` 上界；`499.631...` 是固定 `c`、`n->infinity` 的 `limsup` 系数，依赖中央渐近和终端 pair-entropy 下界。后者更尖锐，但不是前者的逐 `n` 替换。
- **最终符号：INCOMPLETE。** S45 没有证明 `W_n+C_n` 的符号。即使条件接受 S43 的 `limsup W_n/n<=-2.6896...`，当前两条上界相加仍为正；而本轮对 S43 的独立审查又因承重 count-Stein 曲率正文缺失而未认证该数值。
- **作用域：CORRECTED_LAW_ONLY。** 结果限于冻结 half-density、balanced-point corrected cyclic law；不传递到真实 sine-Toeplitz DPP、一般 `rho` 或全合法 `a`。

## 1. 审查材料与依赖分离

主审材料：

`C:/game/gameproject/showa100/math/rl01-sa-cycle04-20260918/research/CYCLE04_20260918/S45_EARLY_RESULT.md`。

为检查正文所谓“已建立”的旧输入，本报告只读核对：

- `results/S13/PROOF.md`；
- `results/S13/AUDIT.md`；
- `research/HARVEST_20260918/S13.md`；
- `research/CYCLE02_20260918/S41.md`；
- `research/CYCLE02_20260918/recovered/S13/S13_Cn_upper_bound.md`。

依赖层次如下：冻结 `theta_{n,l}`、实际 `pi_l`、规定时钟和 `C_n` 定义是模型输入；S13 的中央渐近、pair KL 下界与正的 `C_n` 下界已有 scoped 独立审查；S45 本轮新审的是保留 terminal entropy 后的上包络装配。

## 2. 熵下降时钟不等式

**状态：VERIFIED。**

令

\[
 F(s)=D(P_sf\Vert u),
 \qquad I(s)=-F'(s).
\]

对切片上的原速率生成元

\[
 G_l=\sum_{i<j}(T_{ij}-I),
\]

熵产生可写成

\[
 I(P_sf)=\frac12\sum_{i<j}E_u
 \Psi(P_sf,T_{ij}P_sf),
\]

其中

\[
 \Psi(x,y)=(x-y)(\log x-\log y).
\]

`Psi` 的 Hessian 半正定，且 `P_s` 与每个换位 `T_ij` 交换。Jensen 与 `u` 的不变性给

\[
 I(s+t)\le I(s).
\]

即使初始密度含零，也可先从正时间应用，再令起始时间降到零；不需要声称 `I(0)` 有限或连续。因此

\[
 sI(s)\le\int_0^sI(t)dt=F(0)-F(s).
\]

令

\[
 s(a)=-\frac{\log\theta(z(a))}{\Lambda}.
\]

在 `z'(a_*)=0` 时，

\[
 -s''(a_*)
 =\frac{z''(a_*)}{\Lambda}\partial_z\log\theta(z_*).
\]

又 `s_*=-log(theta)/Lambda`，所以

\[
 [-s''(a_*)]I(s_*)
 \le z''(a_*)
 \frac{\partial_z\log\theta(z_*)}{-\log\theta(z_*)}
 [F(0)-F(s_*)].
\]

符号和 `Lambda` 的消去均正确。等价微分式

\[
 z''\partial_zF(s(z_*))=[-s''(a_*)]I(s_*)
\]

也成立。

这条 `sI<=F(0)-F(s)` 已出现在旧 S13 上界正文；S45 的实质改进是利用其此前被丢掉的负项 `-F(s_l)`。

## 3. 精确实际层装配

**状态：VERIFIED。**

冻结模型在 midpoint 的第一时钟项因 `z'(a_*)=0` 消失，并给

\[
 C_n=\sum_l\pi_l[-s_l'']I_l^G(s_l),
 \qquad
 s_l=-\frac{\log\theta_{n,l}}{2(n-1)}.
\]

逐层应用上一节，得到

\[
 C_n\le z''(a_*)\sum_l\pi_l
 R_{n,l}(z_*)[F_l(0)-F_l(s_l)],
\]

\[
 R_{n,l}=\frac{\partial_z\log\theta_{n,l}}
 {-\log\theta_{n,l}}.
\]

`G_l=l(n-l)L_l` 的转换和 `Lambda=2(n-1)` 已在乘积中精确抵消，没有残留或漏掉 `l(n-l)`。四个端层的初始律和终端律都是均匀/单点，熵产生为零，可直接定义其贡献为零，无需人为赋时钟。

## 4. 初始熵预算

**状态：VERIFIED。**

令 `m=min(l,n-l)`。先取 `m<=n/2`。maximal-overlap 初始律为

\[
 q_m^{\max}(S)=\frac{\det P_S}{\binom{n/2}{m}}.
\]

投影的 Cauchy–Binet 展开验证归一化；因 `P_ii=1/2`，Hadamard 给

\[
 \det P_S\le2^{-m}.
\]

相对于均匀切片的密度满足

\[
 \|r_m^{\max}\|_\infty
 \le\frac{\binom nm}{2^m\binom{n/2}m}
 \le2^m.
\]

最后一步来自

\[
 \binom nm/\binom{n/2}m\le4^m.
\]

因此

\[
 F_l(0)\le\log\|r_l^{\max}\|_\infty
 \le m\log2.
\]

对 `l>n/2` 用补集投影 `I-P`，其对角仍为 `1/2`，故同一界成立。中央带中 `m<=n/2`，于是 `F_l(0)<=n log2/2`；这里甚至不需要 `+o(n)`。

## 5. 中央时钟系数的旧证明是否足够

**状态：ACCEPTED_DEPENDENCY_AND_SPOT_CHECKED。**

S13 完整证明不是只写了一个极限结论。它对 overlap 权重给出精确相邻比，证明统一严格对数凹、中央 sub-Gaussian 尾和三阶绝对矩 `O_c(n^(3/2))`，然后用指数族恒等式处理 `partial_z theta`。这足以在

\[
 |l-n/2|\le n^{2/3}
\]

上一致得到

\[
 \theta_{n,l}(z_*)\to c^2,
 \qquad
 \partial_z\log\theta_{n,l}(z_*)
 \to\frac{(1-c)^3}{2c(1+c)}.
\]

第三中心矩界正是微分有限 `O(1/n)` 修正所需的支付项。该链条已在 `results/S13/AUDIT.md` 中单独接受，本报告抽查公式与尺度未发现缺口。

结合

\[
 z''(a_*)=\frac{32c}{(1-c)^4},
 \qquad -\log(c^2)=-2\log c,
\]

得到

\[
 z''R_{n,l}\to
 A_c=\frac8{(1-c^2)(-\log c)}
\]

且在中央带上一致。

## 6. 终端 pair-entropy 下界

**状态：ACCEPTED_DEPENDENCY_AND_SPOT_CHECKED。**

S13 的 adjacent-pair 论证作用在实际 terminal heat law `P_{s_l}r_l^max`，不是径向替代律。它利用：

1. degree-one 平均模式消失后仍存活的 adjacent degree-two 模式；
2. `theta_{n,l}` 对该模式的精确乘子；
3. 周期平移不变性；
4. 把偶数周期划分为 `n/2` 个不交相邻对并用熵次可加性。

中央相邻对边缘一致趋于

\[
 (p_-,p_+,p_+,p_-),
 \qquad
 p_\pm=\frac14\pm\frac{c^2}{\pi^2}.
\]

因此终端切片 KL 满足

\[
 F_l(s_l)\ge nJ_{\rm pair}(c)-o(n)
\]

在中央带上一致，其中

\[
 J_{\rm pair}(c)=
 \log2+p_-\log p_-+p_+\log p_+.
\]

于是

\[
 F_l(0)-F_l(s_l)
 \le n\left(\frac{\log2}{2}-J_{\rm pair}(c)\right)+o(n).
\]

这一步使用的是对 terminal entropy 的已审下界，并没有把 `F_l(s_l)` 当成已知极限或对 `O(1)` KL 余项求导。

## 7. 实际计数权重和补带

**状态：VERIFIED。**

在 midpoint，

\[
 M\overset d=
 \operatorname{Bin}\left(n/2,\frac{1+c}{2}\right)
 +\operatorname{Bin}\left(n/2,\frac{1-c}{2}\right),
\]

故 `EM=n/2`。Hoeffding 对偏差 `n^(2/3)` 给

\[
 P(|M-n/2|>n^{2/3})
 \le2e^{-2n^{1/3}}.
\]

旧 S13 全层系数证明给

\[
 0\le R_{n,l}(z_*)
 \le\frac2{(z_*-1)\beta(z_*)},
 \qquad
 \beta(z)=2\log\frac{z+1}{z-1}.
\]

其依据是 `partial_z log theta<=2/(z-1)` 和

\[
 \theta_{n,l}\le\left(\frac{z-1}{z+1}\right)^2.
\]

结合 `0<=F_l(0)-F_l(s_l)<=n log2/2`，补带对 `C_n/n` 的贡献至多固定 `c` 常数乘 `e^{-2n^(1/3)}`。这支付了实际 `pi_l` 尾，没有 Gaussian 替代。端层单独为零。

措辞上应称为 stretched-exponential in `n`；精确指数已足够趋零。

## 8. 渐近上包络装配

**状态：VERIFIED_SCOPED。**

在中央带，系数和 entropy drop 上界都一致；中央实际质量趋于一。补带由上一节消失。因此

\[
\limsup_{\substack{n\to\infty\\n\ \mathrm{even}}}
\frac{C_n(c)}n
\le
A_c\left[\frac{\log2}{2}-J_{\rm pair}(c)\right].
\]

即

\[
\boxed{
\limsup\frac{C_n(c)}n
\le
\frac8{(1-c^2)(-\log c)}
\left[\frac{\log2}{2}-J_{\rm pair}(c)\right].
}
\]

量词是：每个**固定** `0<c<1`，沿偶数 `n`。常数不在 `c->0` 或 `c->1` 时一致。

## 9. 数值复算与上下界性质

**状态：VERIFIED。**

在 `c=19/20`，独立复算得到

\[
 p_-\approx0.158557631762790,
 \qquad
 p_+\approx0.341442368237210,
\]

\[
 J_{\rm pair}\approx0.0342356540889006,
 \qquad
 D_{\rm pair}=2J_{\rm pair}\approx0.0684713081778011,
\]

\[
 A_c\approx1599.64929199784,
\]

从而

\[
 A_c\left(\frac{\log2}{2}-J_{\rm pair}\right)
 \approx499.631158492115.
\]

旧 S13 正下界

\[
 \liminf C_n/n\ge\frac{2D_{\rm pair}}{1-c^2}
 \approx1.40453965492925
\]

也与独立 audit 数值一致。

应保持以下区别：

- `843421.367...`：所有偶数 `n>=4` 的非渐近全层界；
- `499.631...`：固定 `c=19/20` 的渐近 `limsup` 界。

所以“系数降低三阶数量级”只适用于渐近比较，不能宣称已得到同常数的逐 `n` 定理。

## 10. 对 `W_n+C_n` 的含义

**状态：INCOMPLETE。**

本报告此前对 S43 可见部分的审查只认证到条件装配；缺失的 count-Stein 辅助 Gibbs 曲率正文使

\[
 \limsup W_n/n\le-2.689614884862
\]

仍未通过独立审查。因此不能把它作为现成定理与 S45 相加。

即使条件接受该数值，

\[
 \limsup(W_n+C_n)/n
 \le -2.689614884862+499.631158492115
\]

仍为正上界，不能决定和的符号。S45 正确识别出仅控制整个时钟区间的总 entropy drop 太粗；需要 terminal entropy production 的尖锐系数或与 `W_n` 的补偿恒等式。

## 11. 最终裁决

\[
\boxed{
\text{S45 Cycle 04 limiting clock envelope: VERIFIED\_SCOPED}
}
\]

认证内容：在冻结 half-density corrected law 的 midpoint，对每个固定 `0<c<1`，正文式 (13) 成立；`c=19/20` 的上包络常数 `499.631158492115...` 正确。

不认证或不推出：同常数的逐 `n` 上界、`C_n/n` 极限的存在、`W_n` 的新负包络、`W_n+C_n` 的符号、corrected cyclic law 到真实 sine-Toeplitz DPP 的传递，以及一般 `rho,a` 的熵率凹性。
