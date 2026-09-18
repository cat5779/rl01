# S51 Cycle 06 完整原稿独立数学审查

## 裁决

| 审查项 | 裁决 |
|---|---|
| 完整原稿 §§1–11 | `VERIFIED_SCOPED` |
| 真 Shannon 熵率的 noise-flow 值恒等式 | `VERIFIED` |
| 随机 anchor 平均及 \(u=0\) 端点 | `VERIFIED` |
| 有限观察窗的完整 moving-law 二阶 jet | `VERIFIED` |
| §5.3 connected 双重和、§6.1 全 sign-word Neumann 紧性 | `VERIFIED` |
| §6.3 全部尾项、式 (6.24) 与统一 \(\overline{\mathcal G}_R\) 收敛 | `VERIFIED_SCOPED` |
| 有限弦到熵率、\(C^2\) 与 \(h_c''=-\Gamma_c\) | `VERIFIED` |
| 完整 §8：\(s=0\) 与旧 SA03 的无限体 \(\Gamma(c)\) 对象相同 | `VERIFIED_WITH_NOTATION_GAP` |
| 随附有限数值检查 | `REPRODUCED_SANITY_CHECK_ONLY` |
| 全 \(\rho\) 扩展、合法端点、\(\Gamma_c\) 的符号 | `NOT_PROVED / OPEN` |

总裁决是：在半密度真 sine projection、任意固定紧致合法内区间上，完整原稿的主定理链条成立。未发现会破坏值恒等式、二阶局部核、无限体积极限、弦传递或 SA03 无限体中点识别的数学反例。

审查对象是后来补齐的原始文件 `S51_CYCLE06_RESULT.md`（30,882 bytes、1,247 行）以及 `S51_CYCLE06_checks.py`（7,314 bytes）。早先 20,000 字符的 chat API 截断件只用于初审，最终裁决以完整原稿为准。随附脚本只作有限维 sanity check，不替代本文解析证明。

## 1. 冻结范围

固定半密度投影 \(Q\)，考察

\[
K_{u,s}=\frac12I+u\left[c\left(Q-\frac12I\right)+sI\right],
\qquad 0\le u\le1,
\]

其中 \(0<c<1\)，而 \(s\) 只在合法开区间

\[
J=\left(-\frac{1-c}{2},\frac{1-c}{2}\right)
\]

的任意固定紧子区间 \(I\Subset J\) 上变化。结论适用于分配中要求的半密度合法内区间；不延伸到端点，也不判定 \(\Gamma_c(s)\) 的正负。

令 \(h_c(s)\) 为真配置 Shannon 块熵的每点极限。令 \(q_{u,s}\) 是在真实无限外部配置下中心位为一的后验，并设

\[
\phi(q)=\left(q-\frac12\right)\log\frac q{1-q},
\qquad
F_\infty(u,s)=\mathbb E_{u,s}\phi(q_{u,s}).
\]

本次审查的关键不是把 \(\operatorname{Tr} b(K)\) 当作配置熵，而是验证作者是否真的从有限配置熵出发并保持真实概率律。

## 2. 真熵率值恒等式、anchor 平均与 \(u=0\)

### 2.1 有限体 noise flow

对固定 \(s\)，\(K_{u,s}\) 正是对 \(u=1\) 的有限块配置施加独立二元对称通道、相关系数为 \(u\) 后得到的核。取 \(u=e^{-t}\) 时，每位翻转率是 \(1/2\)。在有限块上对超立方体无向边配对，得到

\[
\partial_u H_L(u,s)
=-\frac1u\sum_{i\in[1,L]}F_{L,i}(u,s).
\]

这里 \(F_{L,i}\) 使用给定有限块中除 anchor \(i\) 外的全部观测，不是把空间平均替换成单个中心点。

### 2.2 anchor 夹逼没有偷换平均

若 \(F_R\) 只条件于 anchor 周围半径 \(R\) 的窗口，而 \(F_\infty\) 条件于全部外部坐标，则条件 Jensen 和 \(\phi\) 的凸性给出

\[
F_R\le F_{L,i}\le F_\infty
\]

对每个距块边界至少 \(R\) 的 anchor 成立。因此

\[
\left(1-\frac{2R}{L}\right)_+F_R
\le \frac1L\sum_iF_{L,i}
\le F_\infty.
\]

先令 \(L\to\infty\)，再令 \(R\to\infty\)。有限窗口后验是有界 martingale，故 \(F_R\to F_\infty\)。这一步保留了随机 anchor 平均，补上了过去不能仅凭中心位曲率替代熵率曲率的缺口。

### 2.3 \(u=0\) 端点已支付

紧区间 \(I\Subset J\) 上存在 \(\varepsilon>0\)，使全部通道概率、有限和无限后验都落在 \([\varepsilon,1-\varepsilon]\)。独立通道还给出

\[
\left|q-\frac12\right|
\le u\left(\frac c2+s_*\right),
\]

从而一致地 \(\phi(q)=O_I(u^2)\)，即 \(F_R/u\) 与 \(F_\infty/u\) 均为 \(O_I(u)\)。在 \(u=0\) 时输出是公平独立位，有限块熵等于 \(L\log2\)。积分端点因此可积，得到真熵率值恒等式

\[
\boxed{
h_c(s)=\log2-\int_0^1F_\infty(u,s)\,\frac{du}{u}.}
\]

这条识别由有限配置熵独立导出，不依赖 S41 先前缺失的 rate identification。

## 3. 完整有限 moving-law 二阶 jet

对外部 word \(z\) 的真实原子权重 \(w_z(s)\)，逐坐标通道成功率对 \(s\) 的导数均为 \(u\)。因此

\[
w_z'=u\sum_i\sigma_i(w_z+w_{z^i}),
\]

而含中心占据的联合原子还多出中心项 \(uw_z\)。定义跳率 \(r_i=-u\sigma_i o_i\)、输运算子 \(T\) 及随实际律移动的导数 \(D=\partial_s+T\)，商法则中的 score 项恰好相消，得到

\[
Dq=u.
\]

于是对任意光滑 \(\psi\)，

\[
D\psi(q)=u\psi'(q)+\mathcal B_\psi,
\]

再施加一次 \(D\) 得

\[
\partial_s^2F_C(u,s)
=u^2\,\mathbb E\,\overline{\mathcal G}_C,
\qquad
\overline{\mathcal G}_C
=\phi''(q)+u^{-1}\mathcal B_{\phi'}+u^{-2}D\mathcal B_\phi.
\]

作者的普通坐标展开完整保留了 \(w''\phi\)、\(2w'\phi'q'\)、Fisher 型项和后验加速度 \(q''\)；没有冻结实际律。determinant lemma、Sherman–Morrison 和

\[
G'=-uG^2,
\quad q'=u(1+\|v\|^2),
\quad r_i'=u^2(G^2)_{ii}
\]

的符号及归一化均正确。式 (5.26) 的 normalized V14 分组包含一次翻位、posterior derivative 和 connected 双翻位的全部项。有限体 \(u=0\) 时 \(q=1/2\)、\(v=d=0\)，只剩 \(\phi''(1/2)=8\)。

## 4. §5.3 的体积无关控制

设 \(a=\varepsilon^{-1}\)。对任意 sign word，写

\[
B_z=\frac{S_z}{2}(I+2uS_zH_s).
\]

由于 \(\|2uS_zH_s\|\le1-2\varepsilon\)，Neumann 逆界给出

\[
\|G\|\le a.
\]

一次翻位满足 \(|d_i|\le a|v_i|^2\)。对 \(i\ne j\)，作者的 connected 变化可核为

\[
|e_{ij}|
\le 2a^2|G_{ij}||v_i||v_j|
+a^3|G_{ij}|^2(|v_i|^2+|v_j|^2).
\]

再用 \(D_{ij}\le |d_i|+|e_{ij}|\)、\(\sum_j|G_{ij}|^2\le a^2\)，全部二重项都落入以下 prototypes 及其交换版本：

\[
|G_{ij}||v_i|^3|v_j|,
\quad |G_{ij}|^2|v_i|^4,
\quad |G_{ij}|^2|v_i|^2|v_j|^2,
\quad |G_{ij}|^4|v_i|^4.
\]

因 \(a\ge2\)，稿中的粗常数 \(8a^{10}\|v\|^4\) 足够，进而得到与观察体积无关的 \(|\partial_s^2F_C|\le B_Iu^2\)。

## 5. §6.1 对全部 sign words 的一致 Neumann 极限

写 \(H_s=c(Q_{C_\infty}-\tfrac12I)+sI\)。在 \(I\Subset J\) 上

\[
\|2uS_zH_s\|\le1-2\varepsilon
\]

对所有 \(u,s,z\) 一致成立，故 Neumann 余项有统一几何界。

原稿把固定阶的极限写成 “term by term”，这里补出其压缩掉的紧性归纳。对任意紧集 \(K\subset\ell^2\)，集合

\[
\{S_zx:z\in\Omega,\ x\in K\}
\]

仍紧；强收敛且一致有界的算子在紧向量集上一致收敛。对 Neumann 展开的固定阶数递归应用这一事实，再用统一几何余项，即得

\[
\sup_{u,s,z}\|v_R-v_\infty\|_2\to0
\]

以及每个固定列 \(G_Re_i\to G_\infty e_i\) 的相同一致结论。有限窗口后验同时是条件期望 martingale，因此 resolvent 极限确实是真实全部外部后验的一个连续版本，而非仅形式上的 resolvent 候选。

这段是本审查对作者简写的独立展开，不是新增假设。

## 6. §6.3 所有尾项及式 (6.24)

由上一节紧性，定义

\[
\tau_m=\sup_{R,u,s,z}\sum_{i\notin C_m}|v_{R,i}|^2\to0,
\]

且对每个固定 \(i\)，

\[
\eta_{i,m}=\sup_{R,u,s,z}\sum_{j\notin C_m}|(G_R)_{ji}|^2\to0.
\]

四类 prototype 的尾部分别由 \(\tau_m\)、\(\sqrt{\tau_m}\)，或“先固定有限 \(C_\ell\) 用 \(\eta_{i,m}\)，再用 \(\tau_\ell\) 支付远端 \(i\)”控制。量词顺序可以产生单一 \(\rho_m\to0\)。nested Bregman 项没有遗漏：若

\[
F(q,d)=\phi(q+d)-\phi(q)-\phi'(q)d,
\]

则 \(|F|\lesssim d^2\)、\(|\partial_dF|\lesssim|d|\)、\(|\partial_qF|\lesssim d^2\)，翻转后只产生已列 prototypes 和 \(|d_j|D_{ij}^2\)。

特别地，式 (6.24) 的常数可逐边恢复：

\[
D_{ij}^2\le d_i(z)^2+d_i(z^j)^2.
\]

其中 \(i\)-tail 和 \(j\)-tail 各不超过 \(2a^3L_*^4\tau_m\)，并集由二者之和控制，正好得到

\[
\sum_{i\notin C_m\ \mathrm{or}\ j\notin C_m}
|d_j|D_{ij}^2
\le4a^3L_*^4\tau_m.
\]

先统一截断有限与无限核、再在固定窗口中使用有限维一致收敛、最后令窗口增大，确实推出

\[
\boxed{
\sup_{u,s,z}
|\overline{\mathcal G}_R(u,s,z)-
\overline{\mathcal G}_\infty(u,s,z)|\to0.}
\]

一处记号建议不影响结论：把有限 \(G_R\) 嵌入全空间比较时，有限 \(\overline{\mathcal G}_R\) 的 flip 和求和指标仍应明确限制在 \(C_R\)；稿件后文实际按这一解释使用。

## 7. 真实移动律、有限弦与 \(C^2\)

有限核是 \(C_R\)-cylinder function，所以在真实无限 exterior law 下的期望等于相应有限边际期望。上一节的 sup-norm 收敛直接给出

\[
\mathbb E_{u,s}\overline{\mathcal G}_R
\longrightarrow
\mathbb E_{u,s}\overline{\mathcal G}_\infty
\]

并且关于 \((u,s)\) 一致。有限 cylinder 概率由行列式给出且连续；无限核是有限 cylinder 函数的一致极限，故实际律变化下的期望也连续，不需要冻结参考测度。

对有限 \(R\) 应用三角核二阶差分恒等式，再用

\[
F_R\to F_\infty,
\qquad
\partial_s^2F_R
=u^2\mathbb E\overline{\mathcal G}_R
\to u^2\mathbb E\overline{\mathcal G}_\infty
\]

以及 \(u=0\) 的一致支配，得到每条包含在合法开区间中的弦

\[
\Delta_\eta h_c(s)
=-\int_{-\eta}^{\eta}
(\eta-|t|)\Gamma_c(s+t)\,dt,
\]

其中

\[
\Gamma_c(s)=
\int_0^1u\,
\mathbb E_{u,s}\overline{\mathcal G}_\infty(u,s)\,du.
\]

\(\Gamma_c\) 连续，所以分布二阶导数可提升为经典导数：

\[
\boxed{h_c\in C^2(J),\qquad h_c''(s)=-\Gamma_c(s).}
\]

这里的 \(C^2\) 是证明结论，不是传递步骤预先假设的正则性。

## 8. 完整 §8 与旧 SA03 \(\Gamma(c)\) 的关系

完整原稿现已给出作者的逐式对应；下述推导由本审查独立核验。

旧 SA03 把

\[
\Gamma(c)=
\int_0^1u\,
\mathbb E_{\infty,u}
\overline{\mathcal G}_{\infty,u}\,du
\]

定义在未平滑符号

\[
\frac12+uc\left(1_E-\frac12\right)
\]

的真实无限 exterior law 上，其 V14 核与本稿式 (5.26) 逐项相同。在本稿 \(s=0\) 时，

\[
H_0=c\left(Q_{C_\infty}-\frac12I\right),
\qquad b_0=cQ_{C_\infty,0},
\]

故其核正是

\[
K_{u,0}=\frac12I+uc\left(Q-\frac12I\right).
\]

配合原稿给出的参数字典 \(x=cu\) 和 \(\partial_s=u\partial_h\)，两边的真实外部律、resolvent、后验 \(q\) 及 normalized V14 核逐点一致。因此

\[
\boxed{\Gamma_c(0)=\Gamma(c)_{\mathrm{SA03}}.}
\]

这个等同只使用旧 SA03 对局部泛函的定义，不使用其当时尚未证明的“该泛函等于真熵率 Hessian”声明。真熵率识别来自本报告 §§2 与 7 已独立核验的 value-flow 和 chord bridge，所以不存在循环依赖。

原稿式 (8.4) 中的 \(F_{x,R}(1/2)\) 没有定义。若把它理解为旧 SA03 的 finite-\(R\) Fejér functional，该中间等号并不成立，因为本稿从头使用 exact sine principal block。正确而不含歧义的有限体写法应是：令 \(\widetilde F_R(h,x)\) 表示核

\[
hI+x\left(Q-\frac12I\right)
\]

在窗口 \(C_R\) 下的 exact-sine 条件泛函，则

\[
F_R(u,s)=\widetilde F_R\left(\frac12+us,cu\right),
\qquad
\partial_s^2F_R(u,0)
=u^2\partial_h^2\widetilde F_R\left(\frac12,cu\right).
\]

删去或按此定义原稿中间记号后，式 (8.5)–(8.6) 的无限体识别不受影响。故本项裁决是 `VERIFIED_WITH_NOTATION_GAP`，不是对 finite-\(R\) Fejér/exact-sine 对象的混同。

## 9. 随附检查脚本复跑

使用随附脚本的原参数复跑成功：

| 检查 | 复跑绝对误差 | 脚本阈值 |
|---|---:|---:|
| 有限块 entropy production | \(1.367\times10^{-11}\) | \(10^{-7}\) |
| 完整 moving-law V14 二阶差分 | \(1.591\times10^{-8}\) | \(2\times10^{-6}\) |

脚本逐组包含 \(\phi''+\overline{\mathcal B}_{\phi'}\)、\(G^2\)-Bregman 项、\(A_{z^i}\) 响应项和 connected double-flip 项；\(1/u\) 与 \(u^2\) 因子正确。它只检查一个五点有限 DPP，不覆盖 \(u=0\)、一般 \(\rho\)、合法端点或无限体极限，因此证据等级仅是 `SANITY_CHECK`。

## 10. 局部缺口与剩余问题

1. 原稿式 (8.4) 的 \(F_{x,R}\) 未定义，并有混同旧 finite-\(R\) Fejér 对象与本稿 exact-sine 对象的风险；上一节给出了无歧义修正。
2. §10.1 的 \(\|Q_{\rho,C0}\|^2=\rho(1-\rho)\) 只在 \(C=C_\infty=\mathbb Z\setminus\{0\}\) 时成立。有限 \(C\) 应写 \(\|Q_{\rho,C0}\|^2\le\rho(1-\rho)\)。同节的 \(h_\rho(u,s)\) 是中心对角元，建议改名以免与熵率混淆。
3. 一般 \(\rho\) 目前只是条件性扩展蓝图：仍须实例化 \(\rho\)-dependent V14、重验 connected-tail truncation，并另做 \(\rho\)-特定的符号或定量定位。本报告不把它提升为全 \(\rho\) 定理。
4. 原稿第 396、956、992、1042、1065 行有五处制表符加 `o0` 的 LaTeX 损坏，语义显然应为 \(\to0\)，应在发布源稿时修复。
5. 本报告不证明 \(\Gamma_c(s)>0\)、\(<0\) 或非零，也不覆盖触及 \(s=\pm(1-c)/2\) 的合法端点弦；端点处统一 non-nullness 消失，需要新的边界一致可积性。

因此最准确的发布表述是：**S51 Cycle 06 完整原稿在半密度任意紧致合法内区间上的真熵率值流、完整 moving-law 二阶核、无限尾、弦传递和 SA03 无限体中点识别通过独立数学审查；存在两处不改变主定理的局部记号/作用域缺口。全 \(\rho\)、合法端点与 \(\Gamma_c\) 符号仍未证明。**
