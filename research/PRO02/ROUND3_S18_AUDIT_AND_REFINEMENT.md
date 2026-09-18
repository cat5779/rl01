# S18 范围内复现审计与严格减弱后的瓶颈

状态：`SUPPORTED_SCOPED`（S18）；`PROVED_HERE / PENDING_FRESH_REVIEW`（新改进）；完整基准负号仍为 `INCOMPLETE`。

## 1. S18 的复现结论

恢复文件：

- `C:\Users\UIO\Desktop\20260907\RESULTS18`，SHA256 `0B7F486029604266A2E092BEC98B12F9C02B7A618392E70F27E52484339C355B`；
- `C:\Users\UIO\Desktop\20260907\PRO02_checks S18`，SHA256 `EE2F53C56E7DE33F8A9AF4A1B7C7B216F727C4EA081919D4752E46E7002BD2DF`。

用隔离依赖环境重新执行第二个文件，逐项得到：

\[
\Gamma_{\rm ro}=\frac{296960000}{6591},\qquad
A_{\rm ro}=\frac{50251200}{2197},
\]

\[
H_6''=-49.5655212392509631975961954433\ldots,
\qquad
\mathcal W_{4,2}=-10.13300431506280689245412\ldots,
\]

精确势恒等式误差小于 `10^{-59}`，500 次随机真实揭示的最小 Jensen slack 为正，三点障碍的有限差商为 `-0.525556206741`，趋向精确下界 `-125/236`。

对正文指定的四个承重点逐项验算：

1. 秩一方向满足 `v''=h''` 与 `d''=0`，直接微分
   \(L=h+d\log(d/v)\) 得到 (5.3)；相反符号情形的平方完成与 (5.6) 的常数 `3` 正确。
2. 权重 `2/(beta_+ beta_-)`、对角正项 `2/beta_i^2` 与无序 pair 求和没有遗漏因子；这给出正文 (5.12)--(5.18) 的 `Gamma_ro`。
3. 交叉块更新的线性项在真实分支概率下消失，且
   \[
   p(1-p)-c^2r(1-r)
   =(1-r)a(1-a)+r d(a+c)>0.
   \]
   因而 (6.6) 的储备非负。
4. Dirichlet 收缩中有序和的两个方向给出 `2*(8/9)`；随机平移分块数至多 `n/m+2`，端点替换至多涉及 `2(m+L)` 个位置，故 (9.7)、(9.14) 的归一化一致。

因此，本次复现**支持** S18 的有限两分支支付、交叉储备、正弦空间界、完整定位式和基准系数。作用域仍限于其显式导入的 S7/SA02 事实；这不是对全部旧包重新认证，也不改变 S18 自己对基准负号的 `INCOMPLETE` 判断。

## 2. 严格储备给出的尖锐 `c^2` 折扣

在平衡通道

\[
a=d=\frac{1-c}{2},\qquad
\beta=a(1-a)=\frac{1-c^2}{4},
\]

令当前揭示列按核心、剩余外部坐标分成 `u,v`，并记

\[
s=\|u\|^2,\quad t=\|v\|^2,
\quad P=p(1-p).
\]

交叉储备的一步期望下降和核心后验二次变差分别为

\[
\Delta\mathscr S
=s\left(1-\frac{c^2t}{P}\right),
\qquad
Q=\mathbb E\|\Delta R_{II}\|_{\rm HS}^2
=\frac{c^2s^2}{P}.
\]

由正压缩的行能量不等式 `s+t<=r(1-r)` 以及

\[
P=\beta+c^2r(1-r)
\]

得到状态依赖支付

\[
\boxed{
\frac{Q}{\Delta\mathscr S}
=\frac{c^2s}{P-c^2t}
\le \frac{c^2s}{\beta+c^2s}
\le c^2.}
\tag{2.1}
\]

最后一步使用 `s<=1/4` 和 `beta=(1-c^2)/4`。沿共同揭示滤过望远镜求和，

\[
\boxed{
\sum_t\mathbb E\|\Delta R_{II,t}\|_{\rm HS}^2
\le c^2\,\mathbb E\mathscr S_0.}
\tag{2.2}
\]

由于 `Delta X=-c Delta R_II`，S18 的 Theorem 7.1 可严格加强为

\[
\boxed{
\mathcal C_I^V
\le -\mathbb E\Phi_I((G_A)_{II})
+\Gamma_{\rm ro}c^4
 \mathbb E\|R^A_{I,V\setminus A}\|_{\rm HS}^2.}
\tag{2.3}
\]

该统一系数对这一个储备是尖锐的。取严格二点压缩

\[
R_\varepsilon=
\begin{pmatrix}1/2&(1-\varepsilon)/2\\(1-\varepsilon)/2&1/2\end{pmatrix},
\]

以第一点为核心、第二点为揭示点，则 `s=(1-epsilon)^2/4`、`r=1/2`、`t=0`，从而

\[
Q/\Delta\mathscr S=4c^2s\uparrow c^2.
\]

所以仅靠该储备和一般正压缩约束，不能把 `c^2` 再统一降低；任何进一步改进必须使用正弦结构或换储备。

## 3. 正弦变分容量

令 `I subset A subset V`，对所有满足 `f=1` 于 `I`、`f=0` 于 `V\A` 的实函数定义

\[
\operatorname{Cap}_Q(I,A)
=\inf_f \operatorname{Var}_Q\!\left(\sum_x f_x\xi_x\right).
\tag{3.1}
\]

对任一正压缩 DPP 后验 `R`，

\[
\operatorname{Var}_R\!\left(\sum_x f_x\xi_x\right)
=\frac12\sum_{x,y}|R_{xy}|^2|f_x-f_y|^2
+\sum_x f_x^2(R-R^2)_{xx}.
\tag{3.2}
\]

右边第一项已经包含 `I` 与 `V\A` 之间的两个有序方向，故

\[
\|R_{I,V\setminus A}\|_{\rm HS}^2
\le \operatorname{Var}_R\!\left(\sum_x f_x\xi_x\right).
\]

对输出条件取期望并用全方差公式，得到

\[
\boxed{
\mathbb E\|R^A_{I,V\setminus A}\|_{\rm HS}^2
\le \operatorname{Cap}_Q(I,A).}
\tag{3.3}
\]

半密度正弦核中，试函数 `f=1_I` 给出

\[
\operatorname{Cap}_Q(I,A)\le V_m,
\quad
V_m=\frac m4-\frac2{\pi^2}
\sum_{\substack{1\le r<m\\r\ {m odd}}}\frac{m-r}{r^2}.
\tag{3.4}
\]

同时保留 S18 的空间界，记

\[
B_{m,L}:=min\left\{
\operatorname{Cap}_Q(I,I+[-L,L]),
\frac9{16}\left(1+\frac mL\right)
\right\}.
\tag{3.5}
\]

则观察域支付每单位长度至多

\[
\boxed{\Gamma_{\rm ro}c^4\frac{B_{m,L}}m.}
\tag{3.6}
\]

## 4. 完整 pair-cut 的正弦数目方差支付

在平衡点 `beta=(1-c^2)/4`，后验归一化给出

\[
|G_{ij}|^2=\frac{c^2}{\beta^2}|R^Y_{ij}|^2.
\]

又由 S18 (9.12)，所有输出符号下均有

\[
|L(v_{ij},h_{ij})|
\le \ell(\kappa)h_{ij},
\quad
\ell(x)=\frac{(1+x)\log(1+x)-x}{x}.
\]

对任一分块 `pi`，条件 DPP 方差满足

\[
\sum_{I\in\pi}\operatorname{Var}_{R^Y}(N_I)
\ge 2\sum_{\substack{i<j\\i,j\ {m in\ different\ blocks}}}
|R^Y_{ij}|^2.
\]

再用全方差收缩并对随机平移分块平均，得到完整跨块 pair 代价

\[
\boxed{
\frac{\text{pair-cut cost}}n
\le C_{\rm pair}V_m\left(\frac1m+\frac2n\right),
\qquad
C_{\rm pair}=\frac{c^2}{\beta^2}\ell(\kappa).}
\tag{4.1}
\]

基准处

\[
C_{\rm pair}
=\frac{6400}{1521}
\left[400\log\frac{400}{39}-361\right]
=2399.100214664\ldots,
\]

而旧常数为 `C_*=16694.857647373...`。式 (4.1) 支付的是完整 pair-cut，不是只支付新增余量。

## 5. 严格减弱后的充分条件

合并 (2.3)、(3.5) 和 (4.1)，得到新的渐近充分条件：

\[
\boxed{
\mathcal W_{m,L}
+C_{\rm pair}\frac{V_m}{m}
+\Gamma_{\rm ro}c^4\frac{B_{m,L}}m<0.}
\tag{5.1}
\]

这严格替代 S18 的

\[
\mathcal W_{m,L}
+C_*\frac{\mathsf h_m}{m}
+A_{\rm ro}\left(\frac1m+\frac1L\right)<0.
\]

例如只使用 `B_(m,L)<=min{V_m,9(1+m/L)/16}`，误差预算为：

| `m` | `L/m` | pair-cut | observation | total positive cost |
|---:|---:|---:|---:|---:|
| 5000 | 1 | 0.524447 | 8.022217 | 8.546664 |
| 5000 | 16 | 0.524447 | 4.386544 | 4.910991 |
| 10000 | 16 | 0.279073 | 2.193272 | 2.472345 |
| 100000 | 16 | 0.033504 | 0.219327 | 0.252832 |

因此原来数万量级的定位障碍已经缩成一个明确的真窗口断言；例如 `(m,L)=(5000,80000)` 时只需认证

\[
\mathcal W_{5000,80000}<-4.910991\ldots.
\]

当前已有的精确枚举只到小窗口，不能证明这一大窗口断言。故完整基准负曲率仍是 `INCOMPLETE`；但 (5.1) 是严格更弱、已给完整证明的新瓶颈，而不是计划或摘要。
