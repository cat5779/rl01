# S42 cycle03 独立审查

日期：2026-09-18

审查对象：`research/CYCLE04_20260918/S42_RESULT.md` 的完整可见正文。附件正文未取得，故不把附件卡片、作者状态标签或普通浮点输出当作证明。

## 总结论

S42 的主要有限弦桥接框架是成立的：dyadic 恒等式、绝对收敛、一侧截断、真实 sine 投影的准自由互信息上界、标量核界、数方差常数以及显式 dyadic 尾公式都可独立补全。它确实把无限体积问题归约为有限个**带符号**互信息弦加显式中心值尾项。

但有两个需要改正的严格性问题：

1. `L_J \asymp eta^{-2} log(1/eta)` 只能使正文给出的内部尾界成为 `O(eta^2)`，不能成为 `o(eta^2)`；端点版本 `L_J \asymp eta^{-2} log^2(1/eta)` 同样只有 `O(eta^2)`。
2. 盒装的 `M_12` 充分阈值向下舍入，严格意义上略小于真实缺口，不能直接作为充分条件；必须向上舍入或保留符号公式。

我另用 256 位 Arb 对 `n=6,12` 的真实 Toeplitz DPP 原子作有限全枚举，严格认证了第一项 `Delta_eta J_6>0`。它改善了条件阈值，但没有支付其余 11 或 12 个 dyadic 尺度，因此仍不能宣称熵率弦为负。

## 分项裁决

| 项目 | 状态 | 结论 |
|---|---|---|
| 1. dyadic 有限弦恒等式、绝对收敛与一侧截断 | **VERIFIED_SCOPED** | 恒等式及不要求逐尺度正号的截断正确。 |
| 2. 经典互信息不超过准自由量子互信息 | **VERIFIED_SCOPED** | 正确；`Tr b(K)` 只用于量子冯诺依曼熵，没有被当作经典 Shannon 熵。无限补空间需用有限秩成对模式分解补严。 |
| 3. `g_{a,c}` 内部、平衡、端点界与 `V_rho(L)` 常数 | **VERIFIED_SCOPED** | 各系数和不等式方向正确。 |
| 4. 显式 dyadic 尾界 | **VERIFIED_SCOPED** | (6.1)–(6.5) 的求和常数正确；但由它们推出的小 `o` 尺度声明另行判为错误。 |
| 5. 缩弦的小 `o` 声明 | **DISPROVED** | 正文指定的 `asymp` 尺度只给大 `O`；需额外趋于无穷的乘子。 |
| 6. `c=.95, eta=.01, m=6` 的 M12/M13 归约 | **GAP** | 仍是条件充分条件；M12 小数舍入方向错误，M13 方向合法。 |
| 7. 有限第一步 `Delta_eta J_6` | **VERIFIED_SCOPED** | Arb 严格为正，只支付 `M_J` 的第一项。 |
| 8. benchmark 熵率负弦及完整凹性 | **GAP** | 其余 dyadic 带符号项未界定，结论未完成。 |

## 1. dyadic 恒等式

令 `e_L=H_L/L`。平稳性给出

\[
e_L-e_{2L}=\frac{2H_L-H_{2L}}{2L}=\frac{J_L}{2L}\ge0.
\]

有限字母平稳过程满足 `H_L/L -> h`，故沿 `L=m2^k` 望远镜求和得到

\[
e_m-h=\sum_{k\ge0}\frac{J_{m2^k}}{2m2^k}.
\]

分别在 `a-eta,a,a+eta` 使用此式。因为

\[
|\Delta_\eta J_L(a)|
\le J_L(a+\eta)+J_L(a-\eta)+2J_L(a),
\]

右侧对应的三组非负级数都由望远镜式收敛，所以弦级数绝对收敛，允许逐项相减。遗漏尺度满足

\[
-\Delta_\eta J_L(a)
=2J_L(a)-J_L(a+\eta)-J_L(a-\eta)
\le2J_L(a),
\]

因此正文 (2.1) 与 (2.3) 均成立。这里确实没有假设保留尺度逐项为正。

## 2. 经典/量子互信息与无限补空间

occupation-number 测量准自由态 `rho_K` 得到核为 `K` 的 DPP。对有限站点块 `A,B` 分别作 occupation 测量是局部量子信道，故数据处理给出

\[
I_{\rm classical}(A:B)\le I_{\rm quantum}(A:B)
\le I_{\rm quantum}(A:A^c).
\]

第二个不等式是从完整补系统丢弃 `A^c\setminus B`。

无限补空间可以不靠“无穷减无穷”的熵差处理。设 `u_r` 是有限压缩 `Q_A` 的非平凡本征向量，`Q_Au_r=lambda_ru_r`，定义

\[
v_r=\frac{(I-P_A)Qu_r}{\sqrt{\lambda_r(1-\lambda_r)}}\in A^c.
\]

投影恒等式直接给出 `v_r` 正交，并且在 `span{u_r,v_r}` 上

\[
Q=\begin{pmatrix}
\lambda_r&\sqrt{\lambda_r(1-\lambda_r)}\\
\sqrt{\lambda_r(1-\lambda_r)}&1-\lambda_r
\end{pmatrix}.
\]

令 `C=span{v_r}`。`C` 的维数至多为 `|A|`；`D=A^c\ominus C` 在 `Q` 下不与 `A` 耦合。于是相关矩阵 `K=aI+cQ` 对 `(A\oplus C)\oplus D` 分块，准自由态的 `D` 因子与 `A\oplus C` 乘积分离。因此

\[
I_{\rm quantum}(A:A^c)=I_{\rm quantum}(A:C),
\]

右侧是有限模式量。若要求站点有限逼近，可用 `A^c` 中有限支撑向量逼近每个 `v_r` 并正交化；固定至多 `2|A|` 个模式的相关矩阵收敛，有限维准自由态及其互信息随之连续收敛。

每个二模对的全局一粒子本征值为 `a,a+c`，两个边际占据数为 `a+c lambda_r` 与 `a+c(1-lambda_r)`，故量子互信息贡献正是

\[
g_{a,c}(\lambda_r)
=b(a+c\lambda_r)+b(a+c(1-\lambda_r))-b(a)-b(a+c).
\]

这里 `Tr b(K)` 只计算准自由态的**量子冯诺依曼熵**。经典块熵从未被等同于 `Tr b(K)`；经典量只通过 occupation 测量和数据处理进入。因此定理 3.1 的逻辑合法。

## 3. 标量核与数方差

### 3.1 严格内部

在 `[a,a+c]` 上令 `beta=min x(1-x)`。因为 `b''(x)=-1/[x(1-x)]`，

\[
g''_{a,c}(\lambda)\ge-\frac{2c^2}{\beta}.
\]

对 `F=(c^2/beta)lambda(1-lambda)-g` 有 `F''<=0` 且 `F(0)=F(1)=0`，凹性给 `F>=0`。故 `C_int=c^2/beta` 正确。

### 3.2 平衡点

在 `a=(1-c)/2`，令 `x=1-2lambda`。正文使用

\[
\operatorname{arctanh}(cx)\le x\operatorname{arctanh}(c),\qquad 0\le x\le1,
\]

这是凸函数 `arctanh` 与原点弦的正确方向。由此得到

\[
g_{a,c}(\lambda)\le2c\log\frac{1+c}{1-c}\,\lambda(1-\lambda).
\]

系数在 `lambda->0,1` 时切线尖锐。

### 3.3 端点安全界

Bernoulli 最大耦合给 `|b(x)-b(y)|<=b(|x-y|)`。取 `d=min(lambda,1-lambda)`、`s=lambda(1-lambda)`，有 `d<=2s` 且 `2cs<c/2<1/2`，所以

\[
g_{a,c}(\lambda)\le2b(cd)\le2b(2cs).
\]

Jensen 即得 (4.4)，再用 `b(x)<=x(1-log x)` 得 (4.5)。这一步对 `a=0,1-c` 仍合法。

### 3.4 sine 数方差

跨区间两侧、距离为 `r` 的有序点对恰有 `2min(r,L)` 个，故

\[
V_\rho(L)=\frac2{\pi^2}\sum_{r\ge1}
\frac{\min(r,L)\sin^2(\pi\rho r)}{r^2}.
\]

以 `sin^2<=1`、调和和及积分尾得到统一界 (5.2)。半填充时只剩奇数距离，(5.3) 正确。偶数 `L` 的奇调和和写成 `H_L-H_{L/2}/2`，配合奇数平方倒数的中点积分，得到 (5.5)；(5.4) 是其更松的全 `L` 版本。常数均核对通过。

## 4. dyadic 尾界

把 (5.5) 代入 `sum_{j>=0} J_{2^jL}/(2^jL)`，使用

\[
\sum2^{-j}=2,\quad \sum j2^{-j}=2,\quad
\sum8^{-j}=8/7,
\]

恰得到 (6.1)。(6.2)、(6.3) 分别来自 (5.4)、(5.2)，系数正确。

端点安全式中，函数 `v[1+log(L/(2cv))]` 在所需区间递增。用数方差上界并丢弃负项 `-log A` 后，半填充展开

\[
\sum_{j\ge0}2^{-j}(A+jr)(B+jr)
=2AB+2r(A+B)+6r^2,
\]

得到 (6.4)。统一密度时第一因子为 `A+2jr`，得到 (6.5)。因此三类显式尾界本身为 **VERIFIED_SCOPED**。

## 5. 小 `o` 声明的纠正

令 `t=log(1/eta)`。若

\[
L_J\sim k\eta^{-2}t,
\]

则 (6.1) 的显式右端满足

\[
\frac{R_{\rm sharp}(C,L_J)}{\eta^2}
\longrightarrow\frac{4C}{\pi^2k}>0,
\]

而不是趋于零。仅写 `L_J\asymp eta^{-2}t` 更不可能推出小 `o`。端点界以 `L_J\asymp eta^{-2}t^2` 代入同样留下非零数量级。

由现有尾界严格推出小 `o` 的充分写法是

\[
\frac{L_J\eta^2}{\log L_J}\to\infty
\]

（内部），以及

\[
\frac{L_J\eta^2}{(\log L_J)^2}\to\infty
\]

（端点）。例如在正文尺度后再乘任意趋于无穷的因子。固定足够大的常数倍可把大 `O` 系数压到给定种子模以下，但仍不能称为小 `o`，且保留尺度的带符号和仍需另付。

## 6. benchmark 与舍入方向

正文的解析公式给

\[
C_{\rm bal}=\frac{19}{10}\log39,
\]

并且

\[
R_{12}=0.0007503305037653779838419\ldots,
\quad
R_{13}=0.0003950569391094011622658\ldots .
\]

若只使用 `44.9 eta^2/6` 的种子，则 J=12 的真实缺口是

\[
D_{12}=1.99717043204465050858\ldots\times10^{-6}.
\]

正文盒装条件写成 `M_12>1.99717043204465e-6`，其右端略小于 `D_12`，所以不是严格充分条件。可改成

\[
M_{12}>1.997170432044651\times10^{-6},
\]

或直接写 `M_12>R_sharp(C,24576)-44.9 eta^2/6`。J=13 写出的负阈值比真实阈值略强，方向合法。

## 7. 有限第一步 Arb 证书及改进后的条件阈值

检查程序逐一枚举 `a=3/200,1/40,7/200` 下的 64 个六点原子和 4096 个十二点原子，使用 256 位 Arb 外向舍入。得到

\[
\frac{\Delta_\eta H_6}{6}
=-0.00083182848877725559073564039336\ldots<0,
\]

\[
\Delta_\eta J_6
=0.00278611912300986244662340386488\ldots>0,
\]

以及

\[
\frac{\Delta_\eta J_6}{12}
=0.00023217659358415520388528365540\ldots>0.
\]

全部区间半径低于 `3.6e-73`。作者的普通双精度值在约 `3e-14` 处偏离，但符号正确。

直接使用严格的有限 `Delta H_6/6`，而非较松的 `-44.9 eta^2/6`，条件阈值改善为

\[
M_{12}>-0.0000814979850118776068937\ldots,
\]

\[
M_{13}>-0.0004367715496678544284698\ldots .
\]

再支付已证的第一项后，尚未认证的剩余带符号和分别只需满足

\[
\sum_{k=1}^{11}\frac{\Delta_\eta J_{6\cdot2^k}}{12\cdot2^k}
>-0.0003136745785960328107790\ldots,
\]

或

\[
\sum_{k=1}^{12}\frac{\Delta_\eta J_{6\cdot2^k}}{12\cdot2^k}
>-0.0006689481432520096323551\ldots .
\]

这些是**条件性减少**，不是完成：剩余 11/12 个尺度仍可能有任意合法负贡献，目前没有下界。

复现命令：

```powershell
uv run --with python-flint python research/CYCLE04_20260918/checks/verify_s42_first_chord.py
```

## 最终状态

- dyadic 真 sine 有限弦桥：**VERIFIED_SCOPED**。
- 准自由量子互信息主控与无限补空间配对：**VERIFIED_SCOPED**（本文补全有限秩模式论证）。
- `g_{a,c}`、`V_rho(L)` 与显式尾常数：**VERIFIED_SCOPED**。
- 正文指定尺度推出 `o(eta^2)`：**DISPROVED**；只能推出 `O(eta^2)`。
- 原 M12 盒装小数阈值：**GAP**（舍入方向错误，可一位向上修复）。
- 有限第一 doubling 弦：**VERIFIED_SCOPED**。
- M12/M13 全带符号和、benchmark 熵率负弦、完整凹性：**GAP**。
