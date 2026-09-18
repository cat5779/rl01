# S41 Cycle 05 独立数学审查

日期：2026-09-18
审查对象：`S41_CYCLE05_RESULT.md`、`S41_CYCLE05_checks.py`、作者运行输出，以及 S41 Cycle 04 原稿和既有独立审查。
审查方式：逐式审查、独立执行精确 SymPy companion、对旧 Lemma 5.1 的反例适用域和新 `Z_0` 支付链分别核对；未使用哈希作为验收门槛。

## 总裁决

- **旧 Cycle 04 directional estimate：DISPROVED AS STATED。** 新稿给出的十维正交投影满足 `T_0=W_0=0`，但完整 V14 有向导数非零。独立重跑得到

  \[
  Z_0=\frac9{4096},\qquad
  \frac{d\mathscr K}{d\lambda}=\frac{32}{1197},\qquad
  \frac{d\mathscr K}{dt}=-\frac{16}{1197}.
  \]

  合法二元信道 reveal 速度给 `-8 log(3)/1197`。因此只用 `T_0+W_0` 支付所有 directional connected terms 的旧 Lemma 5.1 确实为假。

- **旧 complete-kernel tail 半部：VERIFIED_SCOPED。** 对任意有限正交投影、任意合法 word 和有限分割，完整核从 `E` 截到 `J` 的尾差由 `T_0+W_0` 线性支付；新稿写出了 connected-pair 精确式、三类统一 majorant 及其完整尾求和。该部分不需要新 `Z_0`。

- **新 `Z_0` 修复：VERIFIED_SCOPED。** 新能量

  \[
  Z_0=\sum_{i\in J}T_i\sum_{j\in J}|P_{ij}|^2|P_{j0}|^2
  \]

  正好检测旧证明漏掉的“anchor-inactive 行在翻转 anchor-active 列后被激活”的 connected monomial。新稿的 8 类导数操作、244 个 occurrence、147 个不同 marked monomial 和 33 个最小可求和族构成了 Cycle 04 所缺的完整覆盖账。

- **outside tilt、anchor tilt 与 actual-law 平均：VERIFIED_SCOPED。** `T_0+W_0+Z_0` 在两种对角流下闭合，且随机 anchor 平均中的 `Z_0` 只多支付同一份条件计数方差预算。

- **修复后的观察局部化定理：VERIFIED_SCOPED_WITH_STATED_DEPENDENCY。** 在冻结的 balanced、half-filled V14/local-functional identification 成立的前提下，

  \[
  |\Gamma(c)-\Gamma_N^{\rm av}(c)|
  =O_c\!\left(\sqrt{\frac{\log N}{N}}\right)
  \]

  的证明链现在闭合。该 identification 是旧输入，不由本稿重新证明；故不能把本报告解释为对最终 Shannon 熵率 Hessian 的认证。

- **最终目标：NOT PROVED。** 本稿不给 `Gamma(19/20)` 的可执行正号证书，不覆盖一般 `rho` 或全部合法 `a`，也不证明真实完整配置 Shannon 熵率凹性。

## 1. 反例及其准确适用范围

### 1.1 精确构造

作者取五维压缩

\[
A(\lambda)=UU^*+\lambda ww^*,
\]

并在 `lambda=1/2` 作 Halmos dilation。独立脚本确认：

1. `U^*U=I`、`U^*w=0`；
2. 十维块矩阵 `P` 满足 `P^2=P`；
3. 对 `I={0,1,2,3,4}`、`J={1,2,3,4}`，有 `T_0=W_0=0`；
4. 完整核精确化为

   \[
   \mathscr K_{1/2,J}(\lambda,+)
   =\frac13\log\frac{16\lambda-29}{16\lambda-27}
   -\frac92\log5+\frac92\log3+\frac{544}{45};
   \]

5. 其导数为上文所列非零有理数。

这不是有限浮点迹象，而是符号恒等式。

### 1.2 “合法 posterior”与“sine-specific”不能混淆

给定此 `P`，把 prior 子空间取成 `D_J^{-1} Ran(P)`，观察 `y_J=+` 后 posterior 恰为 `P`；二元信道所有输出字都有正概率，所以构造在一般 projection-DPP + 非退化 BSC 的 posterior 类中合法。

但该 prior 投影不是半填充 sine 投影。故反例的严格含义是：

- 它推翻 Cycle 04 **对所有正交投影声称的 universal directional lemma**；
- 它不单独构成 half-sine 最终局部化定理的反例；
- 新修复定理再次对所有投影成立，因而足以覆盖 half-sine 应用。

这一作用域区分必须保留。

## 2. complete-kernel tail

connected ordered-pair 项精确写成

\[
C_{ij}
=-|G_{ij}|^2B_\phi(q+d_j,d_i^j)
+r_ir_j\{B_\phi(q+d_j,d_i^j)-B_\phi(q,d_i)\}.
\]

由两点 Bregman 余项和翻位公式，正文得到

\[
|C_{ij}|\le 2^8A_c^{25}\Omega_{ij},
\]

其中 `Omega_ij` 的三行分别为：

\[
g_{ij}p_ip_j(p_i^2+p_j^2),\quad
g_{ij}^2(p_i^2+p_j^2)^2,\quad
p_i^2p_j^2(p_i^2+p_j^2).
\]

我分别按 `i in O` 与 `i in J,j in O` 拆开求和。第一行唯一看似线性的项由 `sqrt(T_0W_0)` 支付；第二行由投影行平方和和 `W_0` 支付；第三行由 `sum p_i^2<=1/4` 支付。得到正文的

\[
\sum_{i\in O\ \mathrm{or}\ j\in O}\Omega_{ij}
\le7(T_0+W_0).
\]

其余三个单指标组及 `i=j` connected 项都保留了完整 ledger，没有把双指标项藏进未定义余项。因此

\[
|\mathscr K_{x,E}-\mathscr K_{x,J}|
\le2^{12}A_c^{25}(T_0+W_0)
\]

在有限维中成立。

无限维接口也闭合：anchor column 和每一投影行均为 `ell^2`；connected majorant 绝对可和；对任意 exhaustion，`T_0(J_n)->0`，而 `W_0(J_n)->0` 由 dominated convergence 得到。因此无限完整核先有定义，再由尾界得到 exhaustion independence；没有循环地用待证极限定义自身。

## 3. 新 directional 账本

### 3.1 漏项为何恰由 `Z_0` 捕获

旧账本漏掉的典型项是

\[
\|\dot Pe_i\|g_{ij}^4p_j^4,
\]

其中 `p_i=0`、`T_i>0` 而 `p_j>0`。它不能由 `W_0=sum p_i^2T_i` 观察，但

\[
S_i=\sum_jg_{ij}^2p_j^2,
\qquad Z_0=\sum_iT_iS_i
\]

能够支付该族及其转置族。

### 3.2 全部导数源

正文不是只列 prototype：它先对

\[
\eta_{ij}=d_i^j-d_i
\]

给出精确表达，并按 `dot v_i`、`dot u`、`dot r_i`、`dot rho` 四个来源列出全部 15 个 primitive marked family；随后从 connected identity 的两个乘积逐项微分，得到 8 类操作。

独立执行 companion 得：

```text
raw occurrences: 244
distinct monomials: 147
minimal domination families: 33
```

其 33 族与正文的 `dot q / e_i / e_j / gamma_ij / h_i / h_j` 表逐项一致。需要强调：脚本只验证“给定 8 类 exact majorant operations 后的代数展开”；审查接受完整性还依赖正文式 (4.9) 已列出 Bregman 对共同底点、`d_j`、`d_i` 和 `eta` 的四个梯度差。逐式核对后，没有剩余未列 derivative source。

### 3.3 无维数损失求和

33 族中：

- `dot q`、`h_i`、`h_j` 由 `delta_0=||dot P e_0||` 支付；
- `gamma_ij` 由行 `ell^2` 界和
  `delta_1=(sum p_i^2||dot P e_i||^2)^(1/2)` 支付；
- 通常的 `e_i,e_j` 族由 `delta_1` 支付；
- 唯一不由 `delta_1` 覆盖的两族由
  `delta_2=sum_i ||dot P e_i||S_i` 支付。

正文给出的逐族系数均可从 `sum p_i^2<=1/4`、投影行平方和和 Cauchy--Schwarz 推出。特别是危险的转置族必须在另一指标方向先求和，不能形成 `sum_j p_j e_j`；正文已正确这样处理。

因此有限 directional estimate

\[
|\dot{\mathscr K}_{x,J}|
\le2^{26}A_c^{36}(\delta_0+\delta_1+\delta_2)
\]

在声明作用域内成立。

## 4. 两种流和能量闭合

### 4.1 outside diagonal tilt

若 `H` 支持于 `O`，投影导数为

\[
\dot P=(I-P)HP+PH(I-P).
\]

故

\[
\delta_0\le h\sqrt{T_0},\qquad
\delta_1\le h\sqrt{W_0},\qquad
\delta_2\le\frac h2\sqrt{Z_0}.
\]

对 `Z_0=Tr(D_TM D_p^2M^*)` 微分，`D_T`、两个 `M` 和 `D_p^2` 的贡献分别由 `Z_0`、`sqrt(W_0Z_0)` 和 `sqrt(T_0Z_0)` 支付，得到

\[
|Z_0'|\le h(T_0+W_0+4Z_0).
\]

与旧 `T_0,W_0` 微分式合并即得

\[
\widetilde U_0(t)\le e^{4ht}\widetilde U_0(0).
\]

### 4.2 anchor tilt

只缩放 anchor 时，正文列出的三个投影条目导数由同一投影流直接得到。利用

\[
\sum_ip_i^2S_i\le\frac1{16}
\]

可得

\[
|Z_0'|\le|\eta|\left(\frac12T_0+W_0+\frac72Z_0\right),
\]

从而

\[
\widetilde U_0(P^-;I)\le s_x^4\widetilde U_0(P^+;I).
\]

两条流都没有产生未支付的 `sum_i sqrt(T_i)` 或体积因子。

## 5. actual-law random-anchor 平均

条件于完整 `Y_I` 后，posterior 仍为投影。对所有 anchor 求和：

\[
\sum_aT_a\le\sum_iT_i,
\qquad
\sum_aW_a\le\sum_iT_i,
\]

而新项满足

\[
\sum_aZ_a
\le\sum_{a,i,j\in I}T_i|P_{ij}|^2|P_{ja}|^2
\le\sum_iT_i.
\]

同时

\[
\sum_{i\in I}T_i
=\operatorname{Var}(N_I\mid Y_I).
\]

全方差公式给其 actual-law 期望不超过 latent sine count variance `V_Q(N)`。移除 anchor observation 再用上一节的 `s_x^4` 比较，得到

\[
\frac1N\sum_aE\widetilde U_a(P_a^-;I)
\le3s_x^4\frac{V_Q(N)}N.
\]

这是期望平均，不是逐 word 界；正文没有混淆两者。

## 6. 有限到无限接口和最终作用域

从 finite posterior 到 full posterior 的 outside reveal 是有界对角流；有限 `J` 上使用 directional theorem，full posterior 上使用已验证 tail theorem。平均后用 Jensen 处理平方根，得到作者式 (8.2)。当 `Q` 为 half-filled sine projection 时，

\[
V_Q(N)\le\frac{\log N+4}{\pi^2},
\]

于是速率为 `O_c(sqrt(log N/N))`。

这一步仍有一个明示依赖：`Gamma(c)` 与 finite V14 grouped kernel 的冻结 identification。新稿没有重新证明该 identification，也没有把它偷换成 Toeplitz finite compression 是投影。故最强认证表述必须是：

> 在冻结 V14/local-functional identification 下，balanced、half-filled sine 的 actual-law averaged observation localization 具有上述速率。

不能从本稿推出：

1. `Gamma(19/20)>0`；
2. 可实际执行的有限 `N` 判号（常数在 `c=.95` 极大）；
3. 一般密度或全合法 `a`；
4. 从 local `Gamma` 到真实完整配置 Shannon 熵率 Hessian 的最终桥。

## 7. 独立复现记录

实际执行：

```powershell
uv run --with sympy --with numpy python S41_CYCLE05_checks.py --show-monomials
```

输出与作者 receipt 一致，包括精确反例、244/147/33 项计数和全部最小族。运行成功只认证有限精确代数；无限可和性、Gronwall、random-anchor 与 V14 接口由前述证明审查承担。

## 最终裁决

\[
\boxed{
\begin{array}{l}
\text{Cycle 04 的 }T_0+W_0\text{ directional lemma 为假；}\\
\text{加入 }Z_0\text{ 后，complete-jet 定向账本与实际平均闭合；}\\
\text{观察局部化速率在冻结 V14 作用域内通过独立审查。}
\end{array}}
\]

建议仓库状态：

- old directional Lemma 5.1: `DISPROVED`；
- new tail/directional/energy lemmas: `VERIFIED_SCOPED`；
- repaired Theorem 8.1: `VERIFIED_SCOPED_WITH_DEPENDENCY`；
- final entropy-rate target: `OPEN`。
