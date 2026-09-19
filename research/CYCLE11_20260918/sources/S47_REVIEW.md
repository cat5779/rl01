# S47 cycle04 独立短审

日期：2026-09-18

审查对象：`research/CYCLE04_20260918/S47_EARLY_RESULT.md` 的完整可见正文。附件正文未取得。

## 结论

S47 的 signed nilpotent translation

\[
p_{a+t}^{(n)}=p_a^{(n)}T_t^{\otimes n},
\qquad D^2=0,
\]

是正确的；有限体积三点弦的三角核积分也正确。但正文的相对熵二阶配方 (4) 有明确代数错误，与其自身的展开式 (5) 不一致。修正后得到的仍只是 `J_L''` 的精确重写，没有给出任何 true-sine adverse-curvature 上界。

因此：

- signed translation：**VERIFIED_SCOPED**；
- 熵 Hessian 式 (3)：**VERIFIED_SCOPED**；
- 相对熵紧凑式 (4)：**DISPROVED**；
- 展开式 (5) 及修正后的紧凑式：**VERIFIED_SCOPED**；
- (6)–(7) 有限弦积分：**VERIFIED_SCOPED**；
- `E_tail(L)` 有限、趋零或 `O(log L/L)`：**GAP**；
- 已支付 `eta^2` 尾界、得到新的可用 true-sine 约束：**GAP / NO NEW USABLE BOUND**。

不建议仅为这个重写继续新的 PRO 轮次。

## 1. signed translation

对任意概率行向量 `(p_0,p_1)`，

\[
(p_0,p_1)T_t=(p_0-t,p_1+t),
\]

因为 `p_0+p_1=1`。故 `W_aT_t=W_{a+t}`。给定任意 latent law 后逐坐标张量化，确有

\[
p_{a+t}^{(n)}=p_a^{(n)}T_t^{\otimes n}.
\]

矩阵 `D=[[-1,1],[-1,1]]` 满足 `D^2=0`，不同坐标的 `D_i` 可交换，所以

\[
T_t^{\otimes n}=\exp(tG_n),
\qquad G_n=\sum_iD_i.
\]

由此得到 `p'=pG_n`、`p''=pG_n^2`，正文 (1)–(3) 正确。`T_t` 不是 Markov 核，正文拒绝直接套数据处理也是正确的。

## 2. 相对熵二阶导的正确配方

令

\[
D(P\|Q)=\sum_yP\log(P/Q),
\quad s_P=P'/P,\quad u_P=P''/P,
\]

并类似定义 `s_Q,u_Q`。第一次微分为

\[
D'=\sum P'\log(P/Q)-\sum P s_Q.
\]

再次微分得到

\[
\begin{aligned}
D''
={}&\sum P''\log(P/Q)
+\sum\frac{(P')^2}{P}
-2\sum\frac{P'Q'}Q\\
&-\sum\frac{PQ''}Q
+\sum P\frac{(Q')^2}{Q}.
\end{aligned}
\]

这正是正文 (5)。写成 score/acceleration 形式应为

\[
\boxed{
D''=
\mathbb E_P\left[
u_P\log\frac PQ+(s_P-s_Q)^2-u_Q
\right].
}
\]

正文 (4) 写成

\[
u_P\log(P/Q)+(s_P-s_Q)^2-(u_Q-s_Q^2),
\]

比正确式多出 `s_Q^2`，因而与 (5) 不等价。

### 最小反例：`P=Q`

若 `P=Q` 是任意非平凡光滑概率族，则 `D(P||Q)` 恒为零，所以二阶导也恒为零。正确式给

\[
-\mathbb E_Pu_P=-\sum_yP''(y)=0.
\]

原 (4) 却给

\[
\mathbb E_Ps_P^2>0
\]

（除非该族局部不动）。因此 (4) 被直接证伪。

这个错误可通过用上面的盒装式替换 (4) 修复；后续若始终以定义 `B_L=J_L''` 或正确的 (5) 为准，三角核积分不受影响。

## 3. 弦积分没有自动产生尾估计

对严格内部有限体积分布，`J_L` 光滑，故

\[
\Delta_\eta J_L(a)
=\int_{-\eta}^{\eta}(\eta-|t|)J_L''(a+t)\,dt.
\]

若另有 `J_L''>=-E_L`，则 `Delta_eta J_L>=-eta^2E_L`。这两步正确，但 `eta^2` 只是二阶弦恒等式自带的核质量；真正困难仍是给 `E_L` 一个边界尺度而非体积尺度的上界。

正文定义

\[
E_{\rm tail}(L)=
\sum_{j\ge0}\frac{
\sup_{u\in[a-\eta,a+\eta]}[-J_{2^jL}''(u)]_+
}{2^{j+1}L}.
\]

若这个级数有限，则逐项积分确可推出 (9)。但正文没有证明它有限。若 `E_tail(L)=infinity`，(9) 只读作“左端不小于负无穷”，是没有信息的真空下界。若只由局部 atom-ratio 界得到体积级 `[-J_L'']_+=O(L)`，则 dyadic 级数中的每项为常数量级，仍会发散。

因此 (8)–(10) 是所需定理的重新命名，而不是对尾的支付。假设 (11) `[-J_L'']_+<=C log L` 当然足够，但它正是尚未证明的承重内容。

## 4. 是否产生真实新增可用约束

有两个有限层面的正确对象：

1. 参数变化可由一个 signed nilpotent operator 精确表示；
2. `J_L''` 可按正确的 (5) 保留所有 moving-law score 与 acceleration 项。

它们可作为未来证明的记号与代数起点，但目前没有给出：

- 跨边界抵消；
- `O(log L)` adverse-curvature 界；
- `E_tail(L)<infinity`；
- `E_tail(L)->0`；
- benchmark 尾项的数值或区间支付。

所以相对 S42 的现有 unsigned value tail，S47 没有形成新的已证可用约束；它只把未付义务改写成 `J_L''` 的负部 dyadic 和。作者“不宣称最终结论”的范围声明是正确的，但“已经精确支付 quadratic chord factor”只能理解为形式恒等式，不能理解为已经取得消失尾界。

## 最终状态

- **VERIFIED_SCOPED：** (1)–(3)、(5)、修正后的紧凑配方、(6)–(7)。
- **DISPROVED：** 原 (4)；`P=Q` 即为最小反例。
- **GAP：** (8) 的有限性、(10)、(11)、真正的 chord-sensitive true-sine tail。
- **研究价值判断：** 当前是合法但尚无定量约束的代数重写，不足以续开一轮仅重复该路线的 PRO。
