# S53 Cycle 06 独立数学审查

日期：2026-09-18

审查对象：完整原稿 `original/S53_CYCLE06_RESULT.md`、原检查脚本 `original/S53_CYCLE06_checks.py`，并对照较早的截断聊天导出。原 ZIP 已保留。
来源状态：**COMPLETE_SOURCE**。完整稿共 9 节；较早聊天导出的第 11 节编号属于不同排版，不再作为验收主来源。

## 总裁决

- **移动 (L^2) Galerkin 二阶恒等式：VERIFIED。** 式 (1)--(3) 正确保留了移动概率度量、移动条件期望算子、两个优化器及其归一化导数。有限随机模型的独立差分复核与右端吻合到 (4.9\times10^{-6})。
- **Fisher/Jeffreys 到实际后验势的归一化：VERIFIED。** 对
  \[
  \Phi(h,q)=\frac14\frac{q-h}{h(1-h)}
  \left(\log\frac q{1-q}-\log\frac h{1-h}\right)
  \]
  在固定 (q) 下确有
  \[
  \Phi(1/2,q)=\phi(q),\quad
  \partial_h\Phi(1/2,q)=\chi(q),\quad
  \partial_h^2\Phi(1/2,q)=8+8\phi(q).
  \]
  因而正确公式是
  \[
  \mathcal F_{x,J}''(1/2)
  =G_J''(1/2)+2H_J'(1/2)+8+8G_J(1/2),
  \]
  不能只微分 (\mathcal F(1/2)=G(1/2))。
- **完整有限核接口：VERIFIED。** 原稿从真实有限原子律重新推导 flip generator，再得到 (G_E''=\mathbb E\mathscr K_{x,E})，没有把只在 (h=1/2) 成立的等式非法微分。独立四点投影枚举给
  \[
  G_E''(1/2)=10.0946259959,
  \qquad \mathbb E\mathscr K_{x,E}=10.0946236114,
  \]
  差异与二阶有限差分误差一致。
- **S41 四个有限接口的使用：VERIFIED_SCOPED。** 使用范围正是已独立审过的 complete-kernel tail、含 (Z_0) 的 repaired directional estimate、(T_0+W_0+Z_0) 的 outside Gronwall，以及 anchor add/remove 因子。稿件没有复用已被反例推翻的旧 (T_0+W_0) directional lemma。
- **fixed-anchor 质量输运与长路径界：VERIFIED。** 三段路径分解分别给 (1,2,3) 份 tail，推出
  \[
  \mathbb E(T_0+W_0+Z_0)\le
  A_Q(L_1)+2A_Q(L_2)+3A_Q(L_3),
  \]
  且常数 (14/\pi^2) 的简化正确。
- **实际律、无限 posterior 与任意有限超集的一致性：VERIFIED_SCOPED。** 从全观察 posterior 先 erase outside、再 erase anchor 的 (s_x^8) 账目方向正确；有限支撑 tilt 的一致有界可逆性、posterior projection 强收敛及非负能量的 Fatou 传递足以得到全 outside 界。随后只 reveal 任意有限 (E\setminus J_R)，所有路径长度与能量界均不依赖该 annulus 的大小，故式 (59) 的确对每个有限 (E\supset J_R) 一致。
- **有限泛函曲率网：VERIFIED_SCOPED。** 完整稿第 1--6 节足以证明
  \[
  |\mathcal F_{x,E}''(1/2)-\mathcal F_{x,J_R}''(1/2)|
  \le B_x(R)
  =O_x\!\left(\sqrt{\frac{\log R}{R}}\right)
  \]
  并由对所有有限超集的一致性推出有限曲率 directed net 为 Cauchy。这确实补上了 S44 未完成的“有限优化泛函对有限优化泛函”曲率比较。
- **无限泛函可微性：NOT PROVED。** Cauchy 的数列/网只定义了一个 exhaustion-independent 的数值
  \(\lim_E\mathcal F_{x,E}''(1/2)\)。它本身不证明点态极限 (\mathcal F_{x,\infty}(h)) 在 (1/2) 二次可微，更不证明可交换 (E\to\infty) 与两次 (h)-微分。后者仍需一个统一 (h)-邻域的导数控制或独立的微分交换定理。
- **compact-(x) 控制：VERIFIED。** 对固定 (c<1)，式 (2.6) 的各系数在 (0\le x\le c) 上可由 (c) 端点统一支配，故
  \[
  \int_0^1uB_{cu}(R)\,du
  \le\frac12\bar B_c(R)\longrightarrow0.
  \]
  这里 (u=0,1) 都没有未付端点；关键是外层 (c) 固定且严格小于 1。
- **Gamma 接口：VERIFIED AS A CONDITIONAL STATEMENT。** 若另有来源以本稿的 (1/4) 归一化严格证明
  \(\Gamma(c)=\int_0^1u\mathcal F_{cu,\infty}''du\) 与相应有限式，则上述控制立即给 Gamma 差界。S53 没有假定或证明这两个 identification，也明确保留 (2H'+8+8G)，所以没有偷渡 Gamma 符号或 Shannon entropy-rate 结论。
- **最终目标：OPEN。** 本稿不证明 (\Gamma(19/20)) 的符号，不证明真实无限 Shannon 熵率的二次可微或凹性，也不覆盖一般密度、非平衡 (a) 或全部合法参数。

最强可信标签是：

> **COMPLETE MANUSCRIPT: VERIFIED_SCOPED_WITH_IMPORTED_INTERFACES; FINITE-CURVATURE NET AND COMPACT-(x) CONTROL: VERIFIED; INFINITE (C^2), GAMMA SIGN, AND ENTROPY TARGET: OPEN.**

## 1. 移动投影恒等式

令 (D(h)=I_h^M-I_h^{J_R}=\|e_h\|_h^2)，其中

\[
e=f-g,\qquad g=P_hf,
\]

而 (P_h) 是固定子空间 (V_R) 在移动内积 (L^2(p_h)) 中的正交投影。记

\[
s=p'/p,\quad t=p''/p,\quad u=d'/p,\quad v=d''/p,
\]

\[
k=u-sg,\qquad z=(I-P)k.
\]

微分 coarse normal equation 给

\[
g'=P(u-sg)=Pk,
\]

所以

\[
z=e'+se,\qquad z\perp V_R.
\]

对有限二次优化值使用 envelope 恒等式

\[
I_h''=2\sum d_h''f_h-\sum p_h''f_h^2
       +2\sum p_h(f_h')^2
\]

并相减，可得

\[
\begin{aligned}
D''={}&2\|z\|_p^2
+2\langle e,v-tg-2sk\rangle_p
+\langle e,(2s^2-t)e\rangle_p.
\end{aligned}
\]

这里 (g'=Pk) 正是移动条件期望算子的导数贡献；没有把 (P_h) 冻结。再由 (d=pf) 的二次微分，等价地得到

\[
D''=2\|e'+se\|_p^2+2\langle e,f''\rangle_p
    +\langle e,(t-2s^2)e\rangle_p.
\]

作者给出的二原子例也正确说明：固定 base residual 与 first jet 后，(f'') 项仍可任意改变曲率。因此一般性的“零阶误差 + first jet 控制二阶曲率”命题为假；真正的二阶 observable 必须支付。

## 2. 归一化与完整核

由 Bayes 公式

\[
P_{(h,1)}^J=w_h^J\frac{q_h^J}{h},\qquad
P_{(h,0)}^J=w_h^J\frac{1-q_h^J}{1-h}
\]

以及

\[
\int_0^1\frac{(a-b)^2}{\alpha a+(1-\alpha)b}\,d\alpha
=(a-b)\log(a/b),
\]

可得精确恒等式

\[
\mathcal F_{x,J}(h)=\mathbb E_{w_h^J}\Phi(h,q_h^J).
\]

把 integrand 先按 (h-1/2) 展开、再对移动期望求导，恰好产生 (2H') 和 (8+8G)。这一步是 S44 到实际 finite curvature 所欠归一化的一部分，现稿已支付。

有限 word 接口中

\[
B_h=(h-1/2)I+\tfrac12S_y+x(Q_E-\tfrac12I),
\quad G_h=B_h^{-1},
\]

\[
q_h=h-b^*G_hb,quad
r_i=y_i-(G_h)_{ii},quad
d_i=-|G_hb|_i^2/r_i.
\]

determinant lemma 与 Sherman--Morrison 给出

\[
\frac{d}{dh}\mathbb EA_h
=\mathbb E\left[\dot A+\sum_i r_i(A(y^i)-A(y))\right].
\]

将其连续应用于 (f(q_h)) 与 (\mathcal B_{f,E})，式 (25) 的五组项完整：双指标组以外看似少掉的
\(\sum_i r_i\Delta_i\) 正包含在第四组的 `+1` 中。代数化简后确得式 (26) 的完整 (\mathscr K_{x,E})，故

\[
G_E''(1/2)=\mathbb E\mathscr K_{x,E}.
\]

## 3. S41 接口的合法作用域

现稿真正使用四项：

1. 同一 posterior projection 上，从 (E) 截到 (J) 的完整核尾界
   \[
   |\mathscr K_{x,E}-\mathscr K_{x,J}|
   \le C_{\rm tail}(x)(T_0+W_0);
   \]
2. outside diagonal tilt 下、保留修复项 (Z_0) 的方向界
   \[
   |\dot{\mathscr K}_{x,J}|
   \le C_{\rm dir}(x)\kappa
   (\sqrt{T_0}+\sqrt{W_0}+\tfrac12\sqrt{Z_0});
   \]
3. (\widetilde U_0=T_0+W_0+Z_0) 的
   \(\widetilde U_0(P_t)\le e^{4\kappa t}\widetilde U_0(P_0)\)；
4. anchor add/remove 的 (s_x^4) 因子。

这些正是 S41 Cycle 05 独立审查接受的 repaired interfaces。它们是有限投影/有限 word 的界，再通过绝对可和、有限支撑 tilt 和强极限进入无限 posterior；不能解释为任意无限泛函已可微。

## 4. fixed-anchor 输运

令 (P^\star) 为观察所有实际 channel outputs（含 anchor）后的平稳 posterior projection。对

\[
T_a(L)=\sum_{|j-a|\ge L}|P^\star_{ja}|^2
\]

已有 actual-law 数方差界

\[
\mathbb ET_0(L)\le A_Q(L)=V_Q(L)/L.
\]

### 4.1 两段路径 (W_0)

若 (0\to i\to o) 且 (|o|>R)，则

\[
|i|\ge L_2(R)\quad\text{或}\quad |o-i|\ge L_2(R).
\]

于是

\[
W_0\le T_0(L_2)+\sum_i|P_{i0}|^2T_i(L_2).
\]

平稳性与投影行平方和给

\[
\mathbb E\sum_i|P_{i0}|^2T_i(L)
=\mathbb E\left[T_0(L)\sum_i|P_{0,-i}|^2\right]
=\mathbb E[T_0(L)P_{00}]
\le\mathbb ET_0(L).
\]

故 (\mathbb EW_0\le2A_Q(L_2))。

### 4.2 三段路径 (Z_0)

展开为 (0\to j\to i\to o)。三条边至少一条长度不小于
\(L_3(R)=\lfloor R/3\rfloor+1\)。前两种长边分别由 (A_Q(L_3)) 支付。长末边使用

\[
\begin{aligned}
&\mathbb E\sum_{i,j}T_i(L)|P_{ij}|^2|P_{j0}|^2\\
&=\mathbb E\left[T_0(L)\sum_k|P_{0k}|^2
                         \sum_m|P_{km}|^2\right]\\
&=\mathbb E\left[T_0(L)\sum_k|P_{0k}|^2P_{kk}\right]
\le\mathbb ET_0(L).
\end{aligned}
\]

所以

\[
\mathbb EZ_0\le3A_Q(L_3).
\]

合计得到作者式 (37)。由 (L_k(R)\ge(R+1)/k) 与
\(V_Q(L)\le(\log L+4)/\pi^2\)，系数是

\[
1+2\cdot2+3\cdot3=14,
\]

故式 (42) 正确。

## 5. 实际律、erase/reveal 与一致性

从 (P^\star) 开始：

- erase 全 outside 的 diagonal likelihood，Gronwall 花费 (s_x^4)；
- erase anchor，再花费 (s_x^4)。

因此

\[
\mathbb E\widetilde U_0(P_R^-;I_R)
\le s_x^8\upsilon(R).
\]

无限 outside 不是形式操作。取递增有限支撑 inverse tilts；其对角似然一致有界且一致远离零。相应 posterior projections 强收敛，坐标项逐点收敛；对 (T,W,Z\ge0) 用 Tonelli/Fatou 即可把有限界传到全 outside。

再从只观察 (J_R) 的 (P_R^-) reveal 任意有限 (E\setminus J_R)。整个 annulus 可由一个对角生成元同时完成，operator-norm 长度至多 (\log s_x)，与坐标数无关。因此：

- endpoint tail 付 (C_{\rm tail}s_x^{12}\upsilon(R))；
- path directional 部分付
  \[
  \frac{\sqrt3}{2}C_{\rm dir}(s_x^2-1)s_x^4\sqrt{\upsilon(R)};
  \]
- (H') 的 tail 与 path 分别付作者式 (52)；
- (G) 的零阶差由 posterior martingale Pythagoras 与 S44 的
  (\eta_x(R)) 支付。

这四项合并恰好给式 (58)，系数没有漏掉归一化中的因子 2 和 8。

对任意两个充分大的有限集合 (E,F\supset J_R)，

\[
|\mathcal F_E''-\mathcal F_F''|
\le2B_x(R),
\]

所以 finite-curvature net 的 Cauchy 结论成立。这里的“一致于任意有限 (E\)”是承重条件，不可降成只沿单一 exhaustion 的估计。

## 6. 在 (c=37/40) 与原方法的真实比较

取 (x=c=37/40=0.925)。原双预算在平衡点
\(a=(1-c)/2=3/80\) 已有严格证书

\[
H''\le-n,
\]

而且不支付观察局部化误差。S53 则只给 half-filled、balanced Fisher 有限曲率的收敛，尚无符号。因此它相对于原方法在该点**没有定理覆盖优势，也没有数值优势**。

把式 (58) 的显式常数代入可见：

\[
\Lambda_c=\frac2{1-c}=\frac{80}{3}\approx26.667,
\qquad s_c\approx5.06623,
\]

\[
\log_{10}C_{\rm tail}\approx39.262,
\qquad
\log_{10}C_{\rm dir}\approx59.162.
\]

式 (58) 中主导 (\sqrt{\upsilon(R)}) 的系数约为

\[
2.04\times10^{63}.
\]

只看这一主导项，令它小于 1 已需约

\[
R\asymp10^{129.25}.
\]

这是数量级诊断，不是最小整数证书；但它足以排除“在 (c=37/40) 上比原直接模 1 证明更实用”的解释。S53 的真实优势是**逻辑接口优势**：它补上 S44 的 finite-to-finite Galerkin curvature 缺口。它不是 (c=37/40) 的判号优势。

## 7. 独立新引理：实际律 one-site reveal 消去一阶项

以下结果不属于作者原稿，也不用于上述验收；它是在审查中得到的进一步工具。

### 引理（Bayes-centered retained-kernel reveal）

设 (P) 是有限 DPP 核，(o\notin S)，(p=P_{oo})。通过 contrast
\(0\le x<1) 的平衡二元信道观察 (X_o)，输出 (y\in\{\pm1\})。则

\[
\pi_y:=\mathbb P(Y_o=y)
=\frac{1+yx(2p-1)}2,
\]

且观察后在保留坐标 (S) 上的 DPP 核为

\[
P^y_{SS}
=P_{SS}-a_yP_{So}P_{oS},
\qquad
a_y=\frac{2yx}{1+yx(2p-1)}.
\]

特别地，

\[
\boxed{\sum_{y=\pm1}\pi_y(P^y_{SS}-P_{SS})=0.}
\]

若 (A) 是保留块上的 (C^2) 泛函，记
\(\Delta_y=P^y_{SS}-P_{SS})，则有精确二阶余项公式

\[
\boxed{
\sum_y\pi_y\{A(P^y_{SS})-A(P_{SS})\}
=\sum_y\pi_y\int_0^1(1-t)
D^2A(P_{SS}+t\Delta_y)[\Delta_y,\Delta_y],dt.}
\]

而且

\[
\sum_y\pi_y a_y^2
=\frac{4x^2}{1-x^2(2p-1)^2}
\le\frac{4x^2}{1-x^2}.
\]

### 证明

对任意 (A_0\subset S)，Bayes 公式与 DPP inclusion moments 给

\[
\mathbb P(A_0\subset X\mid Y_o=y)
=\frac{(1-yx)\det P_{A_0}
       +2yx\det P_{A_0\cup\{o\}}}
      {1+yx(2p-1)}.
\]

Schur 行列式公式把右端写成

\[
\det\left(P_{A_0}-a_yP_{A_0o}P_{oA_0}\right),
\]

故条件 DPP 核公式成立；奇异 (P_{A_0}) 由多项式连续性处理。又

\[
\sum_y\pi_ya_y
=\sum_y\frac{1+yx(2p-1)}2
             \frac{2yx}{1+yx(2p-1)}=0,
\]

所以核增量的实际律均值严格为零。对 (A) 使用带积分余项的 Taylor 公式，一阶 Fréchet 项因上述中心化精确消失。最后直接求和 (a_y^2) 即得显示常数。∎

### 它把瓶颈严格缩到哪里

S53 逐实际 word 积分方向导数，先取绝对值，因而不可避免地产生
\(\sqrt{\widetilde U_0}\)。上述引理说明：若按真实条件概率逐坐标 reveal，并只评价不含被 reveal 坐标的保留块泛函，则一阶项无需支付；平均变化只剩 Hessian 二次项。

因此，把 S53 的

\[
O_x\!\left(\sqrt{\frac{\log R}{R}}\right)
\]

改善到 (O_x(\log R/R)) 的一个合法、进一步减弱后的精确义务是：对
\(A=\mathscr K_{x,J}) 建立无维数损失的加权二阶界

\[
\sum_{o\notin J}
\sup_{0\le t\le1}
\left|D^2A(P+t\Delta_o)[\Delta_o,\Delta_o]\right|
\le C_x\,(T_0+W_0+Z_0)
\]

或一个由同一 sine 数方差支付的更细版本。这个义务严格弱于重新控制任意确定性路径的一阶方向导数；但本审查没有完成该 Hessian ledger，因此不把它写成新的 (O(\log R/R)) 定理。

在 (c=37/40) 上，上述 one-site Bayes 系数只有

\[
\frac{4c^2}{1-c^2}\approx23.70,
\]

远小于 S53 的 (C_{\rm dir}(c)\sim10^{59})。这说明它值得作为后续 sine/state-dependent 路线，但在 Hessian 求和完成前仍不是对原方法的已证优势。

## 8. 完整原稿尾部与检查脚本

完整稿第 7 节定义 (\bar B_c(R)) 时，只把所有 (x)-依赖系数替换为固定端点 (c<1) 的上界；这些系数确随 (x) 增大。于是

\[
B_{cu}(R)\le\bar B_c(R),\qquad 0\le u\le1,
\]

并且

\[
\int_0^1uB_{cu}(R)\,du
\le\frac12\bar B_c(R)\to0.
\]

这一步不需要在 (x=1) 取极限，因为 (x=cu\le c<1)。因此 compact-(x) endpoint 义务已经闭合。

第 8 节对 Gamma 的表述也合格：它只给出“若 source-specific identification 另已证明，则得到差界”的条件推论，并明确指出 frozen (G'') 公式必须补回

\[
2H'(1/2)+8+8G(1/2).
\]

它没有声称自己证明该 identification 或 Gamma 的符号。

原检查脚本已原样执行，四项全部通过：

```text
normalization bridge: OK
covariant Galerkin identity: OK
channel-kernel grouping: OK
first-jet obstruction: OK
```

其中 Galerkin 测试使用精确有理数；脚本只验证有限代数，不替代 S41/S44 的解析尾界、无限极限或本报告的作用域判断。

仍保持开放的事项是：

1. finite-curvature limit 是否等于某个已独立定义的 infinite Fisher functional 的二阶导；
2. source-specific Fisher-to-Gamma identification 本身；
3. 从局部 noise/Fisher 量到真实配置 Shannon 熵率的接口；
4. (c=19/20) 或任意 (c>37/40) 的新符号证书；
5. 一般密度、非平衡 channel shift 和全合法 (a)。

## 最终结论

完整原稿的核心数学是成立的：S53 不再只比较同一无限 dual 中的测试 jet，而是真正给出了任意有限 (E\supset J_R) 与 (J_R) 的优化泛函曲率比较，并以

\[
O_x\!\left(\sqrt{\frac{\log R}{R}}\right)
\]

一致收敛。这是对 S44 缺口的实质补强。

但它在 (c=37/40) 上不优于原双预算：原方法已有直接负模，S53 没有新符号且显式常数仅具存在性。它所定义的是 finite-curvature limit，不是自动获得的 infinite-functional second derivative。完整稿的 compact-(x) 控制已经通过；Gamma 差界仍严格条件于另行证明的 source-specific identification。
