# S44 Cycle 04 独立数学审查

日期：2026-09-18
审查对象：`S44_RESULT.md` 与 `S44_checks.py`。
独立性：本报告不使用 S41 Cycle 05 的结论为 S44 背书；两稿的状态分别裁决。
审查方式：逐式核对 posterior projection、Schur localization、actual-law number-variance 平均、Fisher quadratic dual 和 projection completion；在多个 `x` 与随机种子上独立运行 companion。未用哈希作为验收门槛。

## 总裁决

- **projection-completed scalar jet：VERIFIED_SCOPED。** 在 true unsmoothed half-density sine projection 经 balanced BSC 的冻结模型中，完整 infinite Fisher optimizer derivative 确实只依赖标量 posterior `r_infty`，并等于

  \[
  J_{x,\theta,\infty}
  =\psi_{x,\theta}(r_\infty)
  =\frac{4x^2(1-4r_\infty^2)}
  {(1-x^2)(1+\theta r_\infty)^2}.
  \]

- **actual-law posterior localization：VERIFIED_SCOPED。** 半径 `R` 的真实 sine principal marginal posterior `r_R` 满足作者给出的显式 `L^2` 界，速率为 `O_x(log R/R)`。

- **完整 Fisher derivative-jet loss：VERIFIED_SCOPED。** 把无限 optimizer derivative 换成 cylinder function

  \[
  \widehat J_{x,\theta,R}=\psi_{x,\theta}(r_R)
  \]

  时，在**同一个无限 Fisher quadratic dual、同一个 zeroth-order touching optimizer** 内，曲率损失是非负平方误差，并由作者式 (1.6) 支付。

- **有限 marginal 曲率传递：INCOMPLETE。** `widehat J_R` 一般不等于有限输出 marginal 的 optimizer derivative。两者差一个显式非负 hidden covariance completion。故本文没有证明

  \[
  |F_{x,\infty}''(1/2)-F_{x,R}''(1/2)|
  \]

  或其单边版本，也没有证明 `|Gamma-Gamma_R^{obs}|`。

- **最终符号与熵率结论：NOT PROVED。** 没有有限 `R` 的 `Gamma(19/20)>0` 证书，没有一般 `rho,a`，也没有完整配置 Shannon 熵率凹性。

因此作者标题中的 “scoped localization theorem” 可保留，但“finite observation jet”只能解释为**有限可测的 infinite-dual test jet**，不能解释为有限 marginal 的曲率定理。

## 1. 冻结对象与有限 posterior

模型为 half-density sine projection `Q`，输出核

\[
K_x=\frac12I+x(Q-\tfrac12I),\qquad0<x<1.
\]

对 `C_R={j:0<|j|<=R}` 上的实际输出 word，作者使用

\[
B_R=\frac12S_R+x(Q_{C_R}-\tfrac12I),
\quad G_R=B_R^{-1},
\quad b_R=xQ_{C_R,0},
\]

\[
r_R=b_R^*G_Rb_R,qquad q_R=\frac12-r_R.
\]

这是无限实际输出过程的真实 `2R` 点 principal marginal，不是 Fejer、循环近似或把未观测 word 填成固定符号。由 `||Q_C-I/2||<=1/2`，所有 word 上

\[
||G||,||G_R||\le\frac2{1-x}
\]

成立，后续有统一支配。

## 2. same-word Schur localization

把 full response `v=G b` 与 finite response `v_R=G_Rb_R` 放在同一个 full word 上。块方程给

\[
v_I-v_R=-G_RB_{IO}v_O.
\]

投影恒等式

\[
Q_{I,I^c}Q_{I^c,I}=Q_{II}-Q_{II}^2\preceq\tfrac14I
\]

推出 `||B_IO||<=x/2`。因此

\[
||v-\widetilde v_R||^2
\le D_x\,||v_O||^2,
\qquad D_x=1+\frac{x^2}{(1-x)^2}.
\]

又因 `||b||^2=x^2/4`，

\[
|r_\infty-r_R|^2
\le\frac{x^2D_x}{4}\,\tau_R,
\qquad \tau_R=||v_O||^2.
\]

这里没有用 scalar posterior closeness 猜测完整 jet；它只是后续 projection closure 的输入。

## 3. hidden posterior projection 与标量闭合

给定 exterior output，正对角 likelihood tilt 把 latent projection DPP 更新为

\[
\Pi^-=DU(U^*D^2U)^{-1}U^*D.
\]

`D` 有统一正上下界，有限 tilts 强收敛；上式定义实际 full-exterior posterior projection。Woodbury 恒等式给

\[
v_i=\frac{2x\sigma_i}{\sqrt{1-x^2}}\Pi^-_{i0},
\]

以及文中给出的 off-diagonal `G_ij` 字典。令 `p=Pi^-_{00}`，则

\[
r_\infty=x(\tfrac12-p),
\qquad
\sum_{j\ne0}|\Pi^-_{0j}|^2=p-p^2.
\]

故

\[
||v||^2+4r_\infty^2
=\frac{x^2(1-4r_\infty^2)}{1-x^2}.
\]

把它代入 rank-one resolvent 给出的 optimizer derivative

\[
4b^*R_\theta(I+4bb^*)R_\theta b
=\frac{4(||v||^2+4r^2)}{(1+\theta r)^2}
\]

即得 scalar closure `psi(r_infty)`。该闭合使用 latent posterior 是投影这一特殊结构，不能无条件推广到一般非投影 DPP。

## 4. actual-law tail 平均

从 response 字典，

\[
\tau_R=\frac{4x^2}{1-x^2}
\sum_{|j|>R}|\Pi^-_{0j}|^2.
\]

再 reveal 中心输出后，单坐标 tilt 的 off-diagonal 更新因子为

\[
\frac{1-x^2}{(1+yxt)^2},
\qquad t=2p-1.
\]

按中心输出条件概率平均，得到

\[
E(T_R^+\mid Y_C)
=\frac{1-x^2}{1-x^2t^2}T_R^-
\ge(1-x^2)T_R^-.
\]

对长度 `L` 的区间，posterior projection 给

\[
\operatorname{Var}(N_{I_L}\mid Y)
=\sum_{i\in I_L,j\notin I_L}|\Pi^+_{ij}|^2.
\]

取 actual expectation 后由全方差公式不超过 latent variance `V_Q(L)`。平移平均中，位移至少 `L` 的每条边被计 `L` 次，故

\[
L\sum_{|j|\ge L}E|\Pi^+_{0j}|^2\le V_Q(L).
\]

取 `L=R+1`，所有常数合并为

\[
E(r_\infty-r_R)^2
\le
\frac{x^4D_x}{(1-x^2)^2}
\frac{V_Q(R+1)}{R+1}.
\]

half-sine 的精确计数方差公式

\[
V_Q(L)=\frac2{\pi^2}
\left(
\sum_{\substack{n\le L\\n\ {m odd}}}\frac1n
+L\sum_{\substack{n>L\\n\ {m odd}}}\frac1{n^2}
\right)
\]

来自跨区间 pair 的精确计数，且确有 `V_Q(L)<=(log L+4)/pi^2`。

## 5. Fisher touching loss

Pearson--Fisher quadratic dual满足逐 atom 完全平方恒等式

\[
\mathcal I_h(\alpha)-\mathcal Q_h(\alpha;f)
=E_{p_{h,\alpha}}(f-f_{*,h,\alpha})^2.
\]

在 `h_0=1/2` 取 touching path

\[
f_h=f_{*,h_0}+(h-h_0)k.
\]

gap 及其一阶导在 `h_0` 消失；二阶导给

\[
F_x''(1/2)-\underline F_x''[k]
=\frac12\int_0^1E_{p_\alpha}(k-\dot f_{*,\alpha})^2d\alpha.
\]

这个等式在展开 `w''`、`w'q'`、`q''` 前成立，所以同一 infinite functional 内的完整 moving-law curvature 已包含在平方损失中。

对

\[
\psi_{x,\theta}(r)
=\frac{4x^2(1-4r^2)}{(1-x^2)(1+\theta r)^2}
\]

有

\[
|\partial_r\psi|
\le\frac{16x^2}{(1-x)^3(1+x)}.
\]

其证明使用

\[
(1+ys)^2-(y+s)^2=(1-y^2)(1-s^2)\ge0
\]

且 `|y|<=x, |s|<=1`；方向和分母下界均正确。结合上一节的 `L^2` posterior 界，得到作者式 (1.6)：

\[
\mathcal L^{\rm jet}_{x,R}
\le
\frac{128x^8D_x}{(1-x)^8(1+x)^4}
\frac{V_Q(R+1)}{R+1}.
\]

所以 fixed `x<1` 时 jet loss 为 `O_x(log R/R)`。

## 6. projection completion 与不能越过的边界

观察有限 `C_R` 后，posterior `Pi_R^-` 仍是无限 latent projection。投影行平方和将未由有限 response 坐标表示的能量写成

\[
\mathcal T_R^{\rm hid}
=p_R(1-p_R)
-\frac{1-x^2}{4x^2}||v_R||^2\ge0.
\]

于是

\[
\widehat J_{x,\theta,R}
=J^{\rm fin}_{x,\theta,R}
+\frac{16x^2}{1-x^2}
\frac{\mathcal T_R^{\rm hid}}{(1+\theta r_R)^2}.
\]

这同时证明两件事：

1. `widehat J_R` 是有限 word 可计算的 exact projection completion；
2. 除非 hidden tail 为零，它**不是**有限 output marginal optimizer derivative。

作者 §9 又证明 zeroth-order score 的条件期望投影和 `L^2` 误差，但这仍不足以比较两个优化值函数的二阶导数：finite 和 infinite dual 在不同 zeroth-order optimizer 处 touching。非零 Galerkin residual 的二阶导是带符号项，不能由一阶 jet 平方损失自动支付。

因此本稿的结论不能扩大为：

- `|Gamma-Gamma_R^{obs}|=O(log R/R)`；
- 某个 finite `R` 已认证 `Gamma(19/20)>0`；
- finite posterior curvature 与 infinite curvature 只差非负量；
- 熵率凹性。

该 open obligation 不是措辞问题，而是剩余承重引理。

## 7. 独立计算核对

实际执行作者脚本的三组独立参数：

```text
n=24, radius=5, trials=400
x=0.2: max Schur ratio 0.954977592811
x=0.7: max Schur ratio 0.242749018378
x=0.95: max Schur ratio 0.016294402704
```

posterior projection、response 字典、off-diagonal resolvent 字典、scalar closure 和 projection completion 的最大残差均处于相应 binary64 舍入量级。另在 `x=.95,n=20,R=4` 运行 sine-window demo，hidden completion 严格为正，直接显示 completed jet 与 finite optimizer jet 不同。

这些运行是有限诊断，不代替前述无限证明；其主要作用是排除公式抄写、符号和常数错误。

## 8. 与 S41 的独立关系

S44 不使用 S41 的 33-family complete-V14 directional theorem。它研究的是 Fisher quadratic dual 中 optimizer derivative 的低维闭合；S41 研究的是 V14 grouped kernel 随 outside projection flow 的完整方向导数。两者可以同时成立，也不能互相补齐对方的开放接口。

特别地：

- S41 的 observation localization 在冻结 V14 identification 下比较完整 local kernel；
- S44 的平方损失只比较同一 infinite dual 中 exact jet 与有限可测 test jet；
- S44 尚欠的 Galerkin-curvature transfer 不能由 S41 的通过自动消除。

## 最终裁决

\[
\boxed{
\begin{array}{l}
\widehat J_R=\psi(r_R)\text{ 的 projection completion 和平方 jet-loss 通过；}\\
\text{从该 test jet 到 finite marginal curvature 的 touching-baseline transfer 未完成。}
\end{array}}
\]

建议仓库状态：

- equations (1.3)–(1.6), response dictionary and completion: `VERIFIED_SCOPED`；
- integrated jet-loss budget: `VERIFIED_SCOPED`，但明确“not a Gamma-difference bound”；
- finite `Gamma_R^{obs}` transfer: `INCOMPLETE`；
- positivity and entropy-rate target: `OPEN`。
