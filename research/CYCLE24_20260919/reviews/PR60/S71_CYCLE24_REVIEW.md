# S71 / QWE08 Cycle24 独立数学审查

审查日期：2026-09-19（Asia/Singapore）

冻结来源：`C:/game/gameproject/showa100/math/sa-dispatch-20260918/harvest/CYCLE24/S71/S71_VISIBLE_RESULT.md`，共 629 行。

来源状态：**`SOURCE_PARTIAL_TAIL`**。API 在 §10 `Resumption boundary` 的一句话中间截断；§1–9 的定理、证明和完整 Python 检查器均可见。本审查不臆造被截掉的结尾，也不因缺少 ZIP、工具回执或最终状态句而否定可见证明。

## 总裁决

**`VERIFIED_SCOPED_TOOL / SOURCE_PARTIAL_TAIL / MAIN TARGET INCOMPLETE`。**

| 审查对象 | 裁决 | 作用域 |
|---|---|---|
| 正秩一核线上的块 multi-information 凸性 | `CORRECT` | 任意有限严格 Hermitian contraction DPP；任意有限分块 |
| 固定负协方差二元共同平移 MI 凸性 | `CORRECT` | 原子在所论区间严格为正 |
| 半密度两点实际 sine 下界 `C(c²/pi²)` | `CORRECT` | 每个 `0<c<1`、每个合法 `a` |
| 两个实际 endpoint laws 的仿射概率律混合反例 | `CORRECT` | 中间点是 law mixture，不是 kernel shift DPP |
| 二元熵补偿后的 mixture MI 凸性与常数 1 | `CORRECT` | 任意有限严格正 endpoint laws；常数在普遍类中 sharp |
| 实际 identity shift 的 Fisher/acceleration 缺口式 | `CORRECT_AS_UNRESOLVED_IDENTITY` | 精确定位未付项，不是已证引理 |
| 原 all-size `M''>=0` | `INCOMPLETE` | 既未证明，也未由 mixture 反例推翻 |
| 整个 `37/40<c<1` | `INCOMPLETE` | 没有新覆盖 |

没有发现需要把 §1–9 判为 `CRITICAL_GAPS` 的承重错误。唯一应补出的微小逻辑分支是 Theorem 1 从 `s²<=Js` 推出 `J>=s` 时：若 `s=0` 结论直接成立，若 `s>0` 才除以 `s`。这不改变定理。

## 1. 有限 DPP、原子与 score 合法性

正文第 49–90 行正确区分了无限 sine 投影与有限主压缩。积分表示给出

\[
0\preceq Q_{\rho,N}\preceq I,
\]

但不把有限压缩误写成投影。严格 gap

\[
\delta I\preceq K\preceq(1-\delta)I
\]

使每个 masked matrix `K-D_(1-y)` 可逆。把它写成符号对角矩阵与 `K-I/2` 之和后，最小奇异值至少为 `delta`，所以

\[
\|R_y\|\le\delta^{-1},\qquad
\delta^N\le P_K(y)\le(1-\delta)^N.
\]

符号因子把原子概率变成行列式绝对值；上下界及逐项微分均合法。

## 2. Theorem 1：正秩一核线

令 `K(t)=K0+t vv*`。对每个 joint atom，矩阵行列式沿 rank-one 方向对 `t` 仿射；每个 block marginal 的核方向是 `v_A v_A*`，故 marginal atoms 也仿射。因此 joint 和 marginal 的原子二阶导均为零，熵二阶导正是 Fisher information 的负值。

### score 单调性

对任意半正定方向 `V`，score 是

\[
S_V(y)=\operatorname{tr}(R_yV).
\]

固定其余坐标，把 `y_i=0` 翻到 `1`。若 `R_0` 是翻转前逆矩阵，则 determinant ratio 给出

\[
1+(R_0)_{ii}=-\frac{P(y_i=1,y_{-i})}{P(y_i=0,y_{-i})}<0.
\]

Sherman–Morrison 于是给出

\[
R_1-R_0
=-\frac{(R_0e_i)(R_0e_i)^*}{1+(R_0)_{ii}}\succeq0.
\]

所以 joint score 和每个 block score 都是各自坐标上的递增函数。

### Lyons 假设映射

Lyons, *Determinantal probability measures*, Theorem 8.1 确实对任意 positive contraction 的 determinantal measure 给出 conditional negative association with external fields，因而包含这里所需的普通 negative association。当前对象满足：有限 ground set、Hermitian positive contraction、函数依赖互不相交的 blocks。score 可能取负值不构成问题：有限状态上先加常数使其非负，协方差不变，再用 event layer-cake 形式。

### Fisher 超可加

条件 score 恒等式

\[
S_j=\mathbb E[S\mid Y_{A_j}]
\]

来自实际 marginalization。置

\[
J=\mathbb E S^2,\quad J_j=\mathbb E S_j^2,\quad
s=\sum_jJ_j,\quad T=\sum_jS_j.
\]

负关联给出 `E T²<=s`，而条件期望给出 `E(ST)=s`。Cauchy–Schwarz 因而给出

\[
s^2\le J\,\mathbb ET^2\le Js.
\]

当 `s=0` 时 `J>=s` 平凡；当 `s>0` 时除以 `s`，得到 `J>=sum J_j`。于是

\[
\mathcal M''=J-\sum_jJ_j\ge0.
\]

最后 `|S|<=||v||²/delta` 给出

\[
0\le\mathcal M''\le\|v\|^4\delta^{-2}.
\]

证明覆盖复 Hermitian `v`，没有暗用实对称性。

## 3. Theorem 2：二元共同平移

固定 covariance `-d` 时，四个 atoms 对 `d` 的导数为 `(-1,-1,+1,+1)`，marginals 不随 `d` 变化。因此

\[
I(a,0)=I_d(a,0)=0,
\qquad I_{dd}(a,d)=\sum_{x,y}\frac1{q_{xy}(a,d)}.
\]

在所有 atoms 严格为正的共同平移区间上，四个 reciprocal 都对 `a` 凸。mixed atoms 是正的凹二次式的倒数；`11` atom 满足

\[
\partial_a^2(uv-r)^{-1}
=\frac{2((u+v)^2-(uv-r))}{(uv-r)^3}>0,
\]

`00` atom 对称。对正核 `(d-r)` 积分，得到 MI 凸性；`d>0` 时严格。

equal-marginal 情形的 integrand 关于 `t` 在 `1/2` 取得下界，正文给出的

\[
C(d)=\frac{2}{1/4-d}
+4\log\frac{1/4-d}{1/4+d}-8
\]

满足 `C(0)=0` 且

\[
C'(d)=\frac{4d}{(1/4-d)^2(1/4+d)}>0.
\]

对实际半密度相邻两点，`t=a+c/2`、`d=c²/pi²`，全部 atoms 在 `0<c<1, 0<a<1-c` 内严格为正，故

\[
M_{1,1}''(a)\ge C(c^2/\pi^2)>0.
\]

在 `c=19/20` 时，独立数值 sanity check 得 `C≈1.5454670142325355`、`8+C≈9.545467014232536`；数值只核对代数，不承担证明。

## 4. 两个真实 endpoint laws 的仿射混合障碍

正文没有把

\[
\overline P_\lambda=(1-\lambda)P_{a_0}+\lambda P_{a_1}
\]

误写成 `P_(a_lambda)`。同 parity 两点在每个半密度 endpoint DPP 下独立，但 mixture 因隐藏 label 产生

\[
\operatorname{Cov}(Y_i,Y_j)
=\lambda(1-\lambda)(a_1-a_0)^2>0.
\]

因此 endpoint 的 negative association 不能传给 mixture。

label identity

\[
I_{\bar P}(A;B)-\mathbb E_T I_{P_T}(A;B)
=I(T;A)+I(T;B)-I(T;A,B)
\]

由 chain rule 精确成立。若两个 blocks 各以错误率至多 `epsilon` 分类二元 label，Fano 给出 `H(T|A),H(T|B)<=h_b(epsilon)`，从而

\[
\operatorname{Gap}_\lambda M_{\rm mixture}
\ge h_b(\lambda)-2h_b(\epsilon).
\]

半密度 count variance 的 leakage 项

\[
D_L=\frac2{\pi^2}
\left[
\sum_{\substack{1\le r<L\\r\text{ odd}}}\frac1r
+L\sum_{\substack{r\ge L\\r\text{ odd}}}\frac1{r^2}
\right]
\]

来自距离展开与 Parseval，方向正确；`D_L<=(log L+4)/pi²` 足以支持后续粗界。

在 `c=19/20`、`a0=1/50`、`a1=3/100`、`lambda=1/2`、两个 blocks 各长 20000 时，独立执行可见 exact checker 得

```text
count variance strict upper       879127/1800
classification error strict upper 879127/18000000 < 1/20
MI chord gap strict lower          1/10 nat
same-parity mixture covariance     1/40000
```

所以 mixture MI 在中点严格高于 endpoint chord，确实反驳该辅助插值上的凸性。它不反驳实际 kernel-shift 路径。

一般 chord 的尺寸

\[
L\ge\left\lceil\frac{16}{\alpha\Delta^2}\right\rceil,
\qquad \alpha=\min(\lambda,1-\lambda),
\]

由 `Var(N_L)<=L/4` 和 Chebyshev 直接给出 `epsilon<=alpha/16`；正文的 elementary entropy bounds 足以推出 `2h_b(alpha/16)<h_b(alpha)`。范围和退化依赖均标注正确。

## 5. Theorem 4：binary-entropy compensation

对 arbitrary positive endpoint laws，mixture atoms 及所有 observed marginals 都关于 `lambda` 仿射。若 `J,J_A,J_B` 为相应 Fisher informations，则 conditional expectation of scores 给出

\[
J\ge\max(J_A,J_B).
\]

complete-data label score 的 Fisher information 是 `1/[lambda(1-lambda)]`，而 observed scores 是它的条件期望，所以 `J_A,J_B` 均不超过该量。于是

\[
M''=J-J_A-J_B
\ge-\frac1{\lambda(1-\lambda)}
=h_b''(\lambda).
\]

即 `M-h_b` 凸。`r` blocks 时保留最大的 block Fisher term，其余 `r-1` 项逐一用 label Fisher 支付，得到 total correlation 减 `(r-1)h_b` 凸。

常数 1 对两 blocks 在普遍类中 sharp：若两个 blocks 的 label error 都趋零，Theorem 3 的 mixture MI gap 趋于 `h_b(lambda)`。这不是对实际 DPP kernel shift 的 sharpness 结论。

## 6. 实际 identity shift 的缺口式

对一般 smooth finite law，移动 joint/marginal references 后

\[
M''=
\bigl(ES^2-ES_A^2-ES_B^2\bigr)
+\sum_yP''(y)\log\frac{P(y)}{P_A(y_A)P_B(y_B)}.
\]

实际 identity shift 有

\[
S(y)=\operatorname{tr}R_y,
\qquad
\frac{P''(y)}{P(y)}
=(\operatorname{tr}R_y)^2-\operatorname{tr}(R_y^2).
\]

因为方向 `I` 半正定，score 仍递增，故 Fisher defect 非负；但 acceleration term 没有由此得到下界。秩一坐标方向分别凸不能推出它们总和方向凸，因为 Hessian 的跨坐标 mixed terms 没有被控制。mixture 中点也不是目标 DPP。

正文第 524–535 行写出的 signed inequality 正是原问题剩余条件的等价改写。它没有被证明，作者也明确没有把它包装成弱引理。此处裁决为 `CORRECT_AS_UNRESOLVED_IDENTITY`。

## 7. 占位与新颖性边界

已核对的经典输入只有 Lyons Theorem 8.1 的 positive-contraction conditional negative association；其假设与调用方向正确。label-mixture chain identity、Fano、score 条件期望、Fisher data processing 和 binary-entropy compensation 都属于标准信息论/有限概率推导。

有限的精确关键词检索没有定位到“DPP 正秩一核线上的 arbitrary-block total correlation 凸性”的同结论原定理，但这只能记为 **`NOVELTY_UNCONFIRMED`**，不能写成首次结果。Theorem 1 可以作为候选工具接受；其研究新颖性需另做系统文献审计。

## 8. 最终边界

- 可接受：秩一工具、实际两点 seed、law-mixture 障碍、熵补偿 mixture theorem、实际路径的精确缺口式。
- 不可接受为已证：rank-`N` identity direction、任意相邻块 `M''>=0`、finite seed 支付未知边界、整个高对比度熵率凹性。
- 来源尾部：只记录 `SOURCE_PARTIAL_TAIL`；不猜测 §10 被截掉的内容。

所以这份可见稿完成的是一个正确但方向受限的候选工具包，不是原 all-size 定理。
