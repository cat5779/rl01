# S43 Cycle 05 独立数学审查报告

## 总评

- **审查状态：CORRECT / VERIFIED_SCOPED。** 在稿件明示继承 cycle03 与 S45 cycle04 已审输入的前提下，T1--T4、production cancellation 和附录 B 的 `-4n` reference 均成立；未发现会推翻这些结论的公式错误。
- **终端转移：VERIFIED_SCOPED。** 双侧 secant、维数无关生产模量和真实计数权重共同给出

  \[
  \sup_{|l-n/2|\le n^{2/3}}
  \left|\frac{J_l(s_l)}{n^2}-\frac{\mathsf I_n(c)}{2n}\right|\to0,
  \qquad
  C_n(c)=\frac{\mathsf I_n(c)}b+o(n).
  \]

  证明没有微分静态 KL 误差，也没有假设 `\mathsf I_n(c)/n` 收敛。
- **条件赔率包络：VERIFIED。** checkerboard 分块、Schur 补单调性、补集对称和凸序计算均正确；由此得到的 T3 区间及 `c=19/20` 时的系数

  \[
  27.971948500903766\ldots
  \le \liminf C_n/n
  \le \limsup C_n/n
  \le87.472582228429019\ldots
  \]

  正确。
- **联合补偿：VERIFIED_SCOPED。** `W_n` 中的 `-\mathsf I_n(c)/b` 与 `C_n` 中的 `+\mathsf I_n(c)/b` 精确抵消，留下显式 susceptibility 与实际加权输出 KL。T4 在 `c=19/20` 给出的区间

  \[
  -105.331223693047389\ldots
  \le \liminf (W_n+C_n)/n
  \le \limsup (W_n+C_n)/n
  \le32.082474477215733\ldots
  \]

  正确，但不决定联合项符号。
- **KL 方向边界：VERIFIED_WITH_TERMINOLOGY_WARNING。** 实际受控量是

  \[
  U_l=D(\mu_l(s_l)\Vert\gamma_{l,c}),
  \]

  不是反向量 `D(\gamma_{l,c}\Vert\mu_l(s_l))`。若“反向 KL 预算”指后一方向，则该说法没有被本稿证明。
- **附录 B：VERIFIED。** 参考项满足

  \[
  \mathcal A_n''(a_*)=-4n+o(n),
  \qquad
  \widehat H_n''(a_*)=-4n-W_n-C_n+o(n).
  \]

  因而凹性需要的是 `W_n+C_n` 的**下界**跨过 `-4n`，不是上界，也不是必须先证明 `W_n+C_n>=0`。稳健的充分条件是

  \[
  \liminf_{n\to\infty,\ n\ \mathrm{even}}
  \frac{W_n+C_n}{n}>-4.
  \]

  只得到临界等号 `liminf >= -4` 时，还必须继续控制两个 `o(n)` 余项；T4 当前区间跨越 `-4`，所以尚不能判定 corrected Shannon 凹性。
- **计算复跑：VERIFIED_DIAGNOSTIC。** `n=4,6,8,10,12` 的全枚举断言全部通过；复跑与归档的普通量级字段最大相对差约 `7.2e-14`。这些计算只核对实现和显式常数，不证明渐近式。
- **最终作用域：CORRECTED_LAW_ONLY。** 本轮没有证明真实 sine-Toeplitz 输出熵率凹性，没有证明 `W_n/n`、`C_n/n` 收敛，也没有证明 `W_n+C_n` 的符号。

## 1. 审查对象、冻结命题与依赖边界

主审对象是 [PR #22](https://github.com/cat5779/rl01/pull/22) 归档的四个文件：

1. `research/CYCLE06_20260918/S43/S43_CYCLE05_RESULT.md`；
2. `research/CYCLE06_20260918/S43/S43_CYCLE05_checks.py`；
3. `research/CYCLE06_20260918/S43/S43_CYCLE05_checks_output.json`；
4. `research/CYCLE06_20260918/S43/S43_CYCLE05_checks_stdout.txt`。

ZIP 中的四个成员与同目录文件逐字节一致。审查冻结以下量词：`0<c<1` 固定，`n=2k` 沿偶数趋于无穷；对象是循环半密度 Fourier 投影的 corrected law，不是真实有限 Toeplitz 压缩。

稿件明确把下列结论当作已审输入，而不是 cycle05 新证明：

- cycle03 的静态 heat/Gibbs 比较、Gibbs 层正则性、count-Stein 转换、中央径向 KL 与实际 `kappa_l` 尾预算；
- S45 cycle04 的 coefficient-clock 渐近、全层 quotient 与尾部界。

这些输入此前分别在 [S43 cycle03](S43_CYCLE03.md) 与 [S45 cycle04](S45_CYCLE04.md) 独立报告中核验。本报告重新检查它们在 cycle05 中的调用条件、方向和归一化，但不把 593 行新稿误称为完全自包含的零依赖证明。

## 2. 全空间生产的维数无关模量

令

\[
Q_{n,u}=\operatorname{DPP}((1-u)I/2+uP),
\qquad
\mathscr E_n(u)=D(Q_{n,u}\Vert2^{-n}).
\]

写 `u=e^{-2t}`，速率一 bit-flip 半群给 `d\mathscr E_n/dt=-\mathsf I_n`，所以

\[
\mathscr E_n'(u)=\frac{\mathsf I_n(u)}{2u}.
\]

对应 `L`-matrix 的谱在 `[r^{-1},r]`，其中 `r=(1+u)/(1-u)`。Schur 补及其参数微分给

\[
|h_i|\le\log r,
\qquad
|\partial_u h_i|\le\frac2{1-u^2}.
\]

固定第 `i` 个条件赔率，增加一个其余坐标时的 log-odds 变化可由 Schur 补写成 `-log(1-x)`。利用 `M^2\preceq rM`，全部增加坐标的绝对变化和至多 `r^2`；Jacobi 对偶把删除坐标变为 `L^{-1}` 的增加，再付 `r^2`。因此

\[
\sum_{j\ne i}|h_i(S\triangle\{j\})-h_i(S)|\le2r^2.
\]

对 `f(h)=h\tanh(h/2)`，其 Lipschitz 常数不超过 `1+\log(r)/2`。同时使用观测量导数与

\[
\partial_uQ_{n,u}=-(2u)^{-1}L_{\rm flip}^*Q_{n,u}
\]

的测度导数，得到正文 (3.4)。右端在 `u` 的任意紧子区间上与 `n` 无关。这正是后续收缩 secant 所需的统一性。

## 3. 双侧 secant 与 T1

计数链式法则精确给

\[
\mathscr E_n(u)=\sum_l\pi_l(u)\mathscr F_l(u)
+D(\pi(u)\Vert\operatorname{Bin}(n,1/2)).
\]

模态概率下界与 Bernoulli `chi^2` 上界给

\[
0\le D(\pi(u)\Vert\operatorname{Bin}(n,1/2))
\le\log(n+1)+4b_u.
\]

结合已审的 Gibbs 层正则性，在 `B_n={|l-k|\le n^{2/3}}` 上得到

\[
F_l(\sigma_l(u))=\mathscr E_n(u)
+O_u(\log(n+1)+(l-k)^2/n),
\]

其误差一致为 `o(n)`。

`J_l=-F_l'` 随热时间非增。对固定 `u_-<c<u_+`，正文 (4.3) 的左右 secant 方向正确：较晚区间的平均生产不超过当前生产，较早区间的平均生产不小于当前生产。时钟差为 `Theta(1/n)`，静态误差为 `o(n)`；除以 `n^2` 后 secant 误差仍为 `o(1)`。

先令 `n` 趋于无穷，再令固定夹点 `u_-,u_+` 收缩到 `c`，上一节的维数无关模量消去 secant 与端点生产的差。因此 T1 成立。这里没有交换未经证明的一致极限，也没有把静态 KL 误差求导。

## 4. 实际权重聚合与 T2

在中央带上，已审 clock 输入给

\[
nd_l(c)\to\frac2b.
\]

故

\[
\frac{d_lJ_l(s_l)}n
=(nd_l)\frac{J_l(s_l)}{n^2}
=\frac{\mathsf I_n(c)}{bn}+o(1)
\]

对 `l\in B_n` 一致成立。

补带不能直接丢弃。稿件使用真实计数权重的 Hoeffding 界

\[
\pi(B_n^c)\le2e^{-2n^{1/3}},
\]

以及全层

\[
0\le d_lJ_l(s_l)\le K_c n\log2/2.
\]

因此补带对 `C_n/n` 的贡献趋零；四个端层按定义精确为零。中央带实际质量趋于一，于是

\[
C_n(c)=\frac{\mathsf I_n(c)}b+o(n).
\]

正文关于原速率 `G_l` 与归一化 `L_l` 的换算也正确，没有漏掉 `l(n-l)` 因子。

## 5. checkerboard 条件赔率与 T3

奇偶重排后 Fourier 投影满足

\[
P=\frac12\begin{pmatrix}I&V\\V^*&I\end{pmatrix},
\qquad VV^*=I.
\]

任一奇偶半边都是独立公平 bits。令 `a=c^2`、`y=\sum_jw_j(1-2Y_j)`，则一站点条件均值精确为

\[
E[x_i\mid Y_{\rm opp}]=ay.
\]

DPP log-odds 对其余同奇偶位单调不增。固定对立奇偶模式后，同奇偶位全零给 Schur 补极值；再以补集对称取得另一端，得到

\[
\frac{a(y-a)}{1-ay}\le x_i\le\frac{a(y+a)}{1+ay},
\qquad |x_i|\le c^2.
\]

偶凸函数

\[
g(x)=x\log\frac{1+x}{1-x}
\]

在给定均值与区间时由两端点变量支配。正文的 `\Phi_a` 展开系数全为正，所以 chord bound (5.5) 成立。又有精确恒等式

\[
E y^2=v_n=\frac13+\frac8{3n^2}.
\]

这给出 `\mathsf I_n(c)/n` 的有限上界。只揭示两个最近的对立奇偶邻点并用条件 Jensen，则得到有限下界 `\frac12g(t_n)`，其中 `t_n\to8c^2/\pi^2`。与 T2 合并即得 T3。

显式常数已用独立高精度算术复核。它们是解析公式的数值显示，不是用有限 `n` 拟合出来的区间。

## 6. production cancellation、KL 预算与 T4

已审 count-Stein 转换给

\[
W_n=\frac{\mathcal D_n''(0)}{b^2}
+\sum_l\kappa_lU_l+o(n),
\]

\[
\mathcal D_n''(0)
=b^2\sum_{i\ne j}E\partial_jh_i
-b\mathsf I_n(c)+nbc^2.
\]

除以 `b^2` 并加上 T2 后，`\mathsf I_n(c)/b` 一正一负精确抵消：

\[
W_n+C_n=
\underbrace{\sum_{i\ne j}E\partial_jh_i+nc^2/b}_{\mathsf R_n(c)}
+\sum_l\kappa_lU_l+o(n).
\]

这不是把两个无关区间相加，而是同一个空间生产项在 signed count response 与 terminal clock response 之间的代数抵消。

### 6.1 KL 方向

正文定义并使用

\[
U_l=D(\mu_l(s_l)\Vert\gamma_{l,c})\ge0.
\]

中央上界、`kappa_l` 的正负质量和实际尾账给

\[
-M_bD_c\le\liminf\frac1n\sum_l\kappa_lU_l
\le\limsup\frac1n\sum_l\kappa_lU_l\le M_bD_c.
\]

由于 `kappa_l` 带符号，这一步必须同时使用 `U_l>=0` 与上界；不需要 `U_l` 的层间导数。它没有证明 KL 反向后的同一结论。

### 6.2 susceptibility 上下界

Stein 响应恒等式为

\[
b\sum_{j\ne i}E\partial_jr_i=b-E[r_i(1-r_i)].
\]

因为 `\partial_jr_i\le0` 且 `|x_i|\le c^2`，logit 导数界在乘负增量时必须反向。正文正确得到

\[
\frac4{1-c^4}\partial_jr_i
\le\partial_jh_i\le4\partial_jr_i.
\]

令 `V_n=\sum_iEx_i^2`，则

\[
\frac{V_n-nc^6}{b(1-c^4)}
\le\mathsf R_n(c)\le\frac{V_n}{b}.
\]

条件 Jensen 与同一两端点凸序进一步给

\[
c^4v_n\le V_n/n\le(1-v_n)c^8+v_nc^4.
\]

合并 KL 预算即为 T4；所有不等号方向均与负响应一致。

## 7. 附录 B 与正确凹性方向

写

\[
\mathcal A_n(a)=H(\pi(a))+\sum_l\pi_l(a)\log\binom nl,
\qquad
f_l=\log\frac{\pi_l}{\operatorname{Bin}(n,1/2)(l)}.
\]

因为

\[
\mathcal A_n=n\log2-D(\pi\Vert\operatorname{Bin}(n,1/2)),
\]

在中点 `\pi_l'/\pi_l=X/b`，score-square 项为 `EX^2/b^2=n/b`。故

\[
\mathcal A_n''(a_*)=-\sum_l\kappa_lf_l-\frac nb.
\]

精确计数恒等式

\[
\kappa_l=(X^2/b^2-n/b)\pi_l+(2c/b)\dot\pi_l
\]

把第一部分化为 `\operatorname{Cov}(X^2,f_N)/b^2`。局部极限中 `f_N` 的二次系数为

\[
2-\frac1{2b}=-\frac{c^2}{2b},
\]

而 `\operatorname{Var}(X^2)=2n^2b^2+o(n^2)`，所以

\[
\operatorname{Cov}(X^2,f_N)=-nbc^2+o(n).
\]

balanced score 项由 Cauchy--Schwarz 和同一二次包络控制为 `O(\sqrt n)=o(n)`。于是

\[
\mathcal A_n''
=\frac{nc^2}{b}-\frac nb+o(n)
=-4n+o(n).
\]

再用冻结模型中 `\widehat K_n''=W_n+C_n`，得到

\[
\widehat H_n''=-4n-W_n-C_n+o(n).
\]

因此尺度 `n` 上的凹性门槛是对 `W_n+C_n` 作**下界**：必须阻止它比 `-4n` 更负。若存在固定 `\delta>0` 使

\[
W_n+C_n\ge(-4+\delta)n
\]

最终成立，则中点凹性随即成立。当前 T4 的下端约为 `-105.33`，远低于 `-4`；上端约为 `32.08`，又高于 `-4`。所以 T4 既不能证明凹性，也不能证明非凹性。

## 8. 计算复跑与证据限度

使用隔离依赖环境重跑归档规模 `4,6,8,10,12`，全部断言通过。复核结果包括：

- 全配置律枚举全部 `2^n` 个状态，切片枚举全部组合，不是随机采样；
- 质量、条件赔率区间、Stein 恒等式、熵账本和有限抵消残差均在浮点误差范围内；
- stdout 的五个 JSON 对象与归档 `finite_cases` 一致；
- 复跑与归档的普通量级字段最大绝对差约 `6.1e-13`、最大相对差约 `7.2e-14`；
- `27.9719...`、`87.4725...`、T4 两端点与 `A_c-M_bD_c=2.689614884862...` 均由独立高精度算术复核。

这些计算没有严格有向舍入区间，归档也没有保存原始完整命令和依赖版本。脚本在 `c=.95` 上稳定，但普通浮点实现不能覆盖理论开区间 `0<c<1` 的极端端点。更重要的是，五个小规模不能证明任何渐近结论：例如 `n=12` 的 terminal-transfer difference 仍很大，正说明这些点不应被画成趋近 T3 常数的拟合证据。

## 9. 依赖性缺口与最终裁决

若要求 cycle05 目录单独构成零外部依赖的完整证明，则仍有三组明示依赖：

1. T1--T2 使用的静态 heat/Gibbs 比较、层正则性和 coefficient-clock 输入；
2. T4 使用的 count-Stein 转换、中央径向 KL 与实际 `kappa_l` 尾预算；
3. 附录 B 使用的计数局部极限、倾斜尾界和二次包络。

这些不是隐藏前提：正文逐项标出来源，且相应历史报告已经独立核验。按该依赖契约，本轮结论为：

1. T1：**VERIFIED_SCOPED**；
2. `C_n=\mathsf I_n(c)/b+o(n)`：**VERIFIED_SCOPED**；
3. 条件赔率包络与 T3：**VERIFIED**；
4. production cancellation 与 T4：**VERIFIED_SCOPED**；
5. 附录 B 的 `-4n` reference：**VERIFIED**；
6. 正确凹性方向 `W_n+C_n` 需从下方跨过 `-4n`：**VERIFIED**；
7. `W_n+C_n` 的符号或 corrected Shannon 凹性：**OPEN**；
8. 真实 sine-Toeplitz 熵率凹性：**OUT_OF_SCOPE / OPEN**。

未发现满足冻结前提的反例，也未发现作者把有限计算冒充渐近证明。cycle05 的实际进展是把 terminal production 转为全空间条件赔率生产，并在 `W_n+C_n` 中显式消去该生产；剩余承重对象是 susceptibility 与带符号输出 KL，而不是未经量化的 transport 导数。
