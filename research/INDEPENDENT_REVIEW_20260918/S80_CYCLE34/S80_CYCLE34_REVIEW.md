# S80 Cycle34 独立数学审查

## 总裁决

**`CORRECT_VALUE_LEVEL_TELESCOPE / NEW_WORD_INTERACTION_LEMMA /
REUSED_QUASIFREE_CHORD_BRIDGE / LOCAL_SIGN_GAP`。**

S80 的全部明示定理在其作用域内成立：

1. Fisher–Burg Jensen tent 等于实际 adjacent-block mutual-information
   Jensen gap；其正部由 apex 处 classical MI、继而由 quasi-free
   quantum MI 控制。
2. 相邻有限 quantum MI 的 dyadic 加权和精确 telescopes，得到有限 seed
   spectral residual \(R_L^{\rm q}\)，rate passage 只取 entropy values 的
   极限，没有微分 \(o(n)\)。
3. \(R_L^{\rm q}\ge0\) 及
   \(R_L^{\rm q}\le\Lambda_Jc^2D_{\rho,L}/(2L)\) 的系数、归一和 sine
   \(D_{\rho,L}\) 公式正确。
4. actual-word determinant interaction lemma 的
   \(\ell,\ell',\ell''\) 及一般 \(r\) 阶界正确；
   \(D_F=-E_p\ell''\) 与
   \(\mathcal I_{\rm rel}\le4\delta^{-6}\|C\|_{\rm HS}^4\) 正确。

但“全尺度已支付”只能理解为：对一个**固定非退化 chord**，在将每层
正 Jensen gap 粗化为 apex MI value 之后，所有 quantum upper payments
有精确 telescope。它不表示：

- 全尺度 \(\mathcal B_+\le\mathcal I_{\rm rel}\) 已证；
- pointwise curvature residual 已支付；
- tent 面积 \(\tfrac12\tau(1-\tau)(y-x)^2\) 被保留；
- entropy-rate 凹性或目标区间已经判号。

因此它是正确的 value-level all-scale inequality，不是主目标的 major
closure。S80 正文的 `INCOMPLETE` 限定对此是诚实的。

## 1. 来源与冻结量词

来源 `S80_RESULT.md` 共 21436 字节、774 行，正文完整、不截尾。对象是

\[
K_n(a)=aI_n+cQ_{\rho,n},\qquad0<a<1-c,
\]

及完整空间配置 Shannon entropy。所有统一常数只在
\(J\Subset(0,1-c)\) 上使用。rate 结论沿有限 dyadic 体积取值极限，
没有把 finite Toeplitz compression 当作 projection，也没有把
\(\operatorname{tr}h(K)\) 当作 classical entropy。

源文件有五个控制字符破坏了 `\big`、`\frac` 的渲染，分别位于式
(2.4)、(4.8)、(5.9) 两处和 (9.2)。上下文中的预期公式唯一明确；这是
排版缺陷，不影响本次数学裁决，但主实例引用前应清理。

## 2. Fisher–Burg Jensen tent

由已审 S77 identity

\[
M_m''=\mathcal I_{\rm rel,m}-\mathcal B_m
\]

和 Green tent 恒等式，S80 的 charge 满足

\[
\mathfrak C_m
=\int G(\mathcal B_m-\mathcal I_{\rm rel,m})
=M_m(z)-(1-\tau)M_m(x)-\tau M_m(y).
\]

tent 高度、两段斜率和面积

\[
\int G=\frac12\tau(1-\tau)(y-x)^2
\]

均正确。由于 mutual information 在三个点都非负，

\[
[\mathfrak C_m]_+
\le M_m(z)
\]

方向正确。

这里必须准确描述信息损失：Fisher 项在第一行 exact integrand 中没有
被删除，但从 \([\mathfrak C_m]_+\) 粗化到 \(M_m(z)\) 时，两个 endpoint
values 与全部 tent-area 信息都被丢掉。后续 bound 不再利用
Fisher–Burg 的局部结构。因此这是 actual-law **重写加 value bound**，
不是新的 pointwise Burg payment。

## 3. Occupation dephasing 主控

有限 gauge-invariant quasi-free state \(\Gamma_K\) 的 occupation
measurement 正好产生 DPP\((K)\)；其子系统边缘为
\(\Gamma_{K_A},\Gamma_{K_B}\)。对 joint occupation dephasing \(\Delta\)，
relative-entropy data processing 给出

\[
I_{\rm classical}(A:B)
\le D(\Gamma_K\|\Gamma_{K_A}\otimes\Gamma_{K_B})
=\operatorname{tr}h(K_A)+\operatorname{tr}h(K_B)-\operatorname{tr}h(K).
\]

product reference dephases 成两个实际 marginal DPP laws 的乘积，故没有
换权重或冻结 moving law。对相邻等长 Toeplitz blocks 得

\[
M_m(a)\le I_m^{\rm q}(a)
=2S_m^{\rm q}(a)-S_{2m}^{\rm q}(a).
\]

证明完整。独立对 \(n=2,4,6\) 的九个相邻切割直接枚举 classical atoms
并对角化 quantum correlations，全部满足 data-processing inequality；
最小浮点 slack 为 0.32369。一般结论来自有限维 data processing，不依赖
这些样本。

## 4. Quantum cut 边界界

令 \(K_0=K_A\oplus K_B\)、\(E=K-K_0\)。由于
\(h'(K_0)\) block diagonal 而 \(E\) block off-diagonal，

\[
D\operatorname{tr}h(K_0)[E]=0.
\]

整个 segment \(K_0+sE\) 处于
\([a,a+c]\subset(0,1)\)。trace spectral Hessian 的 divided-difference
公式及 \(-h''(u)\le\Lambda_J\) 给出

\[
I_m^{\rm q}(a)
\le\frac{\Lambda_J}{2}\|E\|_{\rm HS}^2
=\Lambda_J\|C\|_{\rm HS}^2.
\]

因 \(\|E\|_{\rm HS}^2=2\|C\|_{\rm HS}^2\)，系数没有漏掉二或
Taylor 的 \(1/2\)。Toeplitz block trace expansion 给出精确式

\[
\|(Q_{\rho,2m})_{AB}\|_{\rm HS}^2
=D_{\rho,m}-\frac12D_{\rho,2m}.
\]

这一节正确，但技术来源与 QWE02/S64 已使用的“off-block 一阶消失加
HS 二阶支付”同族。

## 5. 所有 dyadic quantum payments 的 exact telescope

Shannon recursion

\[
H_{2m}=2H_m-M_m
\]

在 chord functional 下给出

\[
\frac{\mathcal J_{H_{2m}}}{2m}
\ge\frac{\mathcal J_{H_m}}m
-\frac{I_m^{\rm q}(z)}{2m}.
\]

而

\[
\frac{I_m^{\rm q}(z)}{2m}
=\frac{S_m^{\rm q}(z)}m
-\frac{S_{2m}^{\rm q}(z)}{2m}.
\]

因此从 \(L\) 到 \(N=2^KL\) 的全部中间项严格 telescope。独立取
\(\rho=.37,c=.81,a=.07,L=3,K=5\) 对角化复算，级数和与 endpoint
difference 都为 0.1669168925470217，浮点误差为零。

令 \(N\to\infty\)，固定三个 chord points 的
\(H_N/N\to\bar H\) 足够；不需要 \(H_N''/N\) 的极限。最终得到

\[
\mathcal J_{\bar H}
\ge\frac{\mathcal J_{H_L}}L-R_L^{\rm q}(z).
\]

这个 rate-value passage 正确。等价地，它给出单点 sandwich

\[
0\le\frac{H_L(a)}L-\bar H(a)
\le R_L^{\rm q}(a).
\]

“没有漏扫 merge level”在这一个值级 sandwich 中为真；不能把它扩张
成“没有剩余 curvature level”。

## 6. 谱残差和 scalar envelope

若 \(q_j\) 是 \(Q_{\rho,L}\) 的本征值，\(L^{-1}\sum q_j=\rho\)。故

\[
R_L^{\rm q}(a)
=\frac1L\sum_j
\{h(a+cq_j)-(1-q_j)h(a)-q_jh(a+c)\}.
\]

binary entropy 凹性给出非负性；端点为零且
\(-\partial_q^2h(a+cq)\le\Lambda_Jc^2\) 给出

\[
0\le R_L^{\rm q}(a)
\le\frac{\Lambda_Jc^2}{2L}
\operatorname{tr}(Q_{\rho,L}-Q_{\rho,L}^2).
\]

parabola 系数 \(1/2\) 正确。对 sine projection，

\[
D_{\rho,L}
=\frac2{\pi^2}\sum_{r=1}^{L-1}\frac{\sin^2(\pi\rho r)}r
+\frac{2L}{\pi^2}\sum_{r=L}^\infty
\frac{\sin^2(\pi\rho r)}{r^2},
\]

且 \(D_{\rho,L}\le2(\log L+3)/\pi^2\)。归一为每 site 后确为
\(O(\log L/L)\)。

这一 residual 是 entropy **value** error。它与 tent 面积无关。若固定
\(L\) 后令 \(y\to x\)，

\[
R_L^{\rm q}(z)/[\tau(1-\tau)(y-x)^2]
\]

发散，所以不能支付缩小弦的 curvature。让 \(L\) 随 chord width 增长
只能回到 S42 已审的 chord-dependent scale selection，仍不是固定尺度的
pointwise sign theorem。

## 7. Actual-word determinant interaction lemma

对 word matrix \(G_y=K-P_Z\)，置
\(J_y=\operatorname{diag}(2y_i-1)\)。按 occupied/holes 排序后，

\[
\frac{J_yG_y+(J_yG_y)^*}{2}
=K_{Z^c,Z^c}\oplus(I-K_{Z,Z})\succeq\delta I.
\]

accretivity 与 Cauchy–Schwarz 给出最小 singular value 至少 \(\delta\)，
故 \(\|G_y^{-1}\|_{\rm op}\le\delta^{-1}\)。同一论证覆盖
\(K_s=K_0+sE\)，因为它是两个 gap-preserving endpoints 的凸组合。

对

\[
\ell_y=\log|\det(G_{0,y}+E)|-\log|\det G_{0,y}|
\]

沿 \(s\) 的一次变分在零点因 block parity 消失。二阶 Taylor 与两个
HS factors 给出

\[
|\ell_y|\le\delta^{-2}\|C\|_{\rm HS}^2.
\]

对 \(F_r(s)=\operatorname{tr}G_{s,y}^{-r}\)，二次微分有
\(r(r+1)\) 个 trace words；每个由两个 HS factors 和总共
\(r+2\) 个 inverses 控制。Taylor 的 \(1/2\) 与
\(\|E\|_{\rm HS}^2=2\|C\|_{\rm HS}^2\) 抵消，得到

\[
|\partial_a^r\ell_y|
\le(r-1)!r(r+1)\delta^{-(r+2)}\|C\|_{\rm HS}^2.
\]

所以 \(r=1,2\) 的系数 2、6 均正确，没有 volume factor。该 lemma 的
proof ingredients 延续 QWE02 的 gap inverse/off-block cancellation，但
“逐 actual word 的 likelihood interaction 及其全部 bias derivatives”
是本审查语料中新的、可复用的明确封装。

## 8. \(D_F=-E\ell''\) 与剩余 acceleration

置 joint score \(S\)、marginal scores \(S_A,S_B\)，则

\[
\ell'=S-S_A-S_B.
\]

条件期望 score identities 给出

\[
\mathcal I_{\rm rel}
=E S^2-E S_A^2-E S_B^2+2E[S_AS_B],
\]

\[
D_F=E S^2-E S_A^2-E S_B^2
=\mathcal I_{\rm rel}-2E[S_AS_B].
\]

直接展开 \(E_p\ell''\) 并使用 joint/marginal normalization，交叉 score
项精确消掉，得到

\[
D_F=-E_p\ell''.
\]

DPP score covariance 的已审符号给出 \(D_F\ge0\)，从而

\[
0\le D_F\le6\delta^{-4}\|C\|_{\rm HS}^2,
\qquad
\mathcal I_{\rm rel}=E(\ell')^2
\le4\delta^{-6}\|C\|_{\rm HS}^4.
\]

独立在六点 hard point 重建全部 64 atoms，得到

\[
D_F=32.59075196032429,
\quad -E\ell''=32.59075196032428,
\]

误差 \(7.11\times10^{-15}\)；所有 pointwise bounds 均通过浮点检查。

但完整曲率仍是

\[
M''=D_F+\sum_y p_y''\ell_y.
\]

逐 word \(|\ell_y|\) 小不控制 signed average
\(\sum p_y''\ell_y\)，因为单独绝对求和 \(p''\) 会恢复体积损失。S80
正确把它列为 gap；这也是 determinant lemma 尚未变成 sign theorem 的
精确位置。

## 9. 半密度 \(L=6\) 复核

只用 odd Fourier separations 与
\(\sum_{r\ge1,\ r\text{ odd}}r^{-2}=\pi^2/8\)，得到

\[
D_{1/2,6}
=\frac32-\frac{806}{75\pi^2}.
\]

直接矩阵 trace 与该闭式的普通双精度差为
\(2.22\times10^{-16}\)。在 \(c=19/20,a=1/40\) 上，

\[
\Lambda=1600/39,
\qquad
\frac{\Lambda c^2}{12}=361/117,
\]

故式 (9.2) 正确。对 \(J=[.02,.03]\)，
\(\Lambda_J=2500/49\) 且系数为 \(9025/2352\)，式 (9.3) 正确。

独立 eigenvalue 复算给

\[
R_6^{\rm q}(.025)=0.17360594686589215.
\]

这只是浮点诊断，不是区间证书。相同浮点路径给 benchmark chord 的
六点 seed gap 每 site 仅
\(0.0001034358898574\)，故 (T) 的下界约为
\(-0.1735025109760\)。这不反驳定理，只直观显示当前 residual 尚不能
判该 chord 的正号。

## 10. 与 S42、QWE02、S64 的去重

| S80 内容 | 裁决 | 与既有工作的关系 |
|---|---|---|
| finite Jensen tent / entropy-value rate passage | **REUSED** | S42/PR16 已审 dyadic finite-chord bridge；S80 改用一般 \(x,z,y\) 记号。 |
| classical MI \(\le\) occupation quasi-free MI | **REUSED** | S42/PR16 已完整审查 data processing 与 quantum entropy 解释。 |
| 相邻 quantum MI 的 exact dyadic telescope | **NEW REFINEMENT** | 比 S42 的逐尺度 scalar/variance tail 更干净，压成 exact seed residual；仍是 value-level。 |
| \(R_L^{\rm q}\) 的 scalar gap 与 \(D_{\rho,L}\) | **REUSED/REFINED** | S42 已用 binary-entropy scalar envelope 和 sine number variance；S64/PR46 也有 spectral/determinant leakage envelope。S80 给出适配 exact telescope 的精确 residual。 |
| gap inverse 与 off-block first variation cancellation | **REUSED TECHNIQUE** | QWE02/PR33 已用相同结构得到 dimension-free cross-HS response bound。 |
| 逐 word \(\ell,\ell',\ell''\) 及一般 \(r\) 阶界 | **NEW TOOL** | 相对已审语料的新封装；推出 \(\mathcal I_{\rm rel}=O(\|C\|^4)\)。 |
| \(D_F=-E\ell''\) | **NEW EXACT INTERFACE** | 与 S77 Fisher–Burg 分解兼容，但未控制 acceleration。 |
| full interval/rate concavity | **GAP** | S42、QWE02、S64 的未解 acceleration/sign 义务仍在。 |

所以 S80 的核心价值是“exact value telescope + new pointwise interaction
lemma”，不是此前 finite-chord/quasi-free 路线的独立替代，也没有消除
S64 已标出的 acceleration bottleneck。

## 11. 真正最小未解义务

要从 S80 推进到局部或全区间凹性，最小的新承重命题必须保留 tent 面积。
等价的可接受形式包括：

\[
M_m''(a)\ge-r_m(a),
\qquad
\sum_{k\ge0}\frac{r_{2^kL}(a)}{2^{k+1}L}<\infty,
\]

并使总和小于 finite seed curvature；或者直接证明

\[
[\mathcal J_{M_m}(x,y;\tau)]_+
\le\frac12\tau(1-\tau)(y-x)^2A_m(J)
\]

且 dyadic 加权 \(A_m\) 可支付。按 S80 自身的精确分解，这归结为对

\[
\sum_y p_y''(a)\ell_y(a)
\]

的 signed、boundary-size、scale-summable 控制，同时保留已经支付的
\(D_F=-E\ell''\)。仅有
\(|\ell|,|\ell'|,|\ell''|\) 或
\(R_L^{\rm q}=O(\log L/L)\) 都不够。

## 12. 最终状态表

| 声明 | 状态 |
|---|---|
| Fisher–Burg tent identity | **CORRECT / REUSED IDENTITY** |
| occupation dephasing MI 主控 | **CORRECT / REUSED** |
| adjacent quantum exact telescope | **CORRECT / NEW REFINEMENT** |
| theorem (T) 与 entropy-value limit | **CORRECT_VALUE_LEVEL** |
| spectral residual (R)、(U)、(D) | **CORRECT / REUSED-REFINED** |
| actual-word determinant derivative lemma | **CORRECT / NEW TOOL** |
| \(D_F=-E\ell''\)、quartic \(\mathcal I_{\rm rel}\) | **CORRECT / NEW INTERFACE** |
| 所有尺度 pointwise Burg/curvature 已支付 | **NOT PROVED** |
| benchmark chord 或目标区间判号 | **GAP** |
| full entropy-rate concavity | **GAP** |

最终应把 S80 接收到工具库，但不得在 README、反例地图或交接包中称为
“major closure”。准确描述是：它严格压缩了 fixed-chord 的所有 quantum
value tails，并新增 actual-word interaction 导数工具；局部 acceleration
符号和 tent-area-sensitive payment 仍是唯一承重缺口。
