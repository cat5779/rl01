# S77 Cycle31 独立数学审查

## 来源状态与总裁决

来源文件 `S77_VISIBLE_RESULT_PARTIAL.md` 共 20150 字节、1304 行，并在
文件首行明确声明读取于 20000 字符处截断。可见内容包含 Section 1–7
完整主体和 Section 8 的开头，不包含稿件正常结尾。

**裁决：`VERIFIED_VISIBLE_CORE / SOURCE_PARTIAL_TAIL / FLOAT_DIAGNOSTICS_ONLY / RATE_TARGET_INCOMPLETE`。**

我支持可见主体中的下列数学结论：

1. affine-KL bridge 与离散 cofactor Bochner 恒等式；
2. 精确分解
   \[
   M''=\mathcal I_{\rm rel}-\mathcal B;
   \]
3. \(D_F\)、交叉 marginal-score 协方差与 acceleration 的精确消去；
4. \(M''\ge\mathcal I_{\rm rel}-\mathcal B_+\) 及相应 hybrid residual；
5. 在已知各有限尺度残差上界时成立的 merge-tree/rate 条件接口；
6. 固定 \(\theta<1\) 配 quartic residual 的两点弱耦合障碍；
7. 全部严格 equal-marginal 两点 DPP 的 \(d^2\) 正下界。

不支持以下升级：

- 作者表中的 “Certified lower bound” 数值不是区间证书；它只是严格
  下界公式的双精度求值。
- “proves positivity at this floating-point base point” 不能作为严格
  证明措辞。六点 \(M''>0\) 本身可继承 PR64 的独立区间认证，但 S77
  新的 \(\mathcal I_{\rm rel}-\mathcal B_+>0\) 尚未区间化。
- 全尺度 \(\mathcal B_+\) 支付没有证明，恒等式与条件充分式不能冒充
  已完成的 entropy-rate 定理。

本审查只判断可见 Sections 1–7 与 Section 8 可见开头；不声称已读或
审查缺失尾部。

## 1. Cofactor 方程与 KL bridge

沿共同 identity shift，实际 DPP atom 的一、二阶导为

\[
\dot p(y)=\sum_i\sigma_i p_{-i}(y_{-i}),
\]

\[
\ddot p(y)=2\sum_{i<j}\sigma_i\sigma_jp_{-ij}(y_{-ij}).
\]

因每个对角变量在 determinant 中仿射，二阶只有不同坐标交叉项；
主 cofactor 正是删除坐标后的真实 marginal。对
\(q=p_Ap_B\)，它也是 block-diagonal DPP
\(K_A\oplus K_B\)，故同样满足两式。

置 \(r=p-q\)、\(h_s=q+sr\)。对每个固定参数 \(a\)，

\[
D(h_s\|q)''_{s}=\sum_y\frac{r(y)^2}{h_s(y)}=:J_s.
\]

由于 \(D_0=D_0'=0\)，积分两次得到

\[
M=D(p\|q)=\int_0^1(1-s)J_s\,ds.
\]

这只是辅助概率 bridge，不要求 \(h_s\) 是 DPP。正文只对 cofactor
方程使用线性，而没有对 \(h_s\) 调用负关联，逻辑正确。有限严格 gap
下所有 atom 正，关于 \(a,s\) 的逐项微分和交换积分均合法。

## 2. 离散 Bochner 恒等式

令 \(z=r/h\)。标量恒等式

\[
\left(\frac{r^2}{h}\right)''
=2h(\dot z)^2+2z\ddot r-z^2\ddot h
\]

可由 \(r=hz\) 直接展开。cofactor 分部积分为

\[
\sum_y f(y)\ddot r(y)
=2\sum_{i<j}\sum_{y_{-ij}}r_{-ij}(y_{-ij})\Delta_{ij}f.
\]

又

\[
z_{s,-ij}=r_{-ij}/h_{s,-ij}
=E_{h_s}[z_s\mid Y_{-ij}].
\]

代入并使用

\[
\Delta(z-z_{-ij})^2
=\Delta z^2-2z_{-ij}\Delta z
\]

得到

\[
J_s''
=2E_{h_s}(\dot z_s)^2
-2\sum_{i<j}E_{h_{s,-ij}}
\Delta_{ij}(z_s-z_{s,-ij})^2.
\]

因 rectangle difference 本身没有固定符号，正文没有在这一步偷加凸性。

## 3. 标量积分与精确 Fisher–Burg 分解

写 \(g=p/q\)、\(d_s(x)=1+s(x-1)\)。有

\[
h_s=qd_s(g),\qquad
z_s=\frac{g-1}{d_s(g)},\qquad
\dot z_s=\frac{\dot g}{d_s(g)^2}.
\]

承重积分

\[
2\int_0^1\frac{1-s}{d_s(g)^3}\,ds=\frac1g
\]

方向与系数正确，故正项恰为

\[
\mathcal I_{\rm rel}
=E_p[(\partial_a\log g)^2].
\]

对固定 \(i,j,y_{-ij}\)，置 \(m=g_{-ij}\)。差分满足

\[
z_s(g)-z_s(m)
=\frac{g-m}{d_s(g)d_s(m)}.
\]

第二个标量积分为

\[
2(g-m)^2\int_0^1
\frac{1-s}{d_s(g)^2d_s(m)}\,ds
=2\left[g-m-m\log(g/m)\right].
\]

乘回 \(q_{-ij}\) 并作 rectangle difference，得到正文定义的
\(\mathcal B\)。因此

\[
\boxed{M''=\mathcal I_{\rm rel}-\mathcal B}
\]

严格成立。

独立 160 点 Gauss–Legendre 重放在多组 \((g,m)\) 上得到：式 (23)
最大误差 \(2.76\times10^{-14}\)，式 (26) 最大误差
\(1.96\times10^{-14}\)。这些数值只交叉核对闭式积分，证明仍是上述
初等积分。

## 4. (D_F) 与交叉 score 协方差的消去

边缘 score 满足

\[
S_A=E[S\mid Y_A],\qquad S_B=E[S\mid Y_B],
\]

且

\[
\partial_a\ell=S-S_A-S_B.
\]

展开平方并用
\(E[SS_A]=E[S_A^2]\)、\(E[SS_B]=E[S_B^2]\)，得到

\[
\mathcal I_{\rm rel}=D_F+2E[S_AS_B],
\]

即

\[
D_F=\mathcal I_{\rm rel}-2E[S_AS_B].
\]

结合 S71 已审的 score 单调性与 DPP 负关联，
\(E[S_AS_B]\le0\)，故 \(D_F\ge\mathcal I_{\rm rel}\ge0\)。再与
\(M''=D_F+C_{\rm acc}\) 比较，得到

\[
C_{\rm acc}=2E[S_AS_B]-\mathcal B.
\]

所以 \(D_F\) 的“额外”负协方差部分与 acceleration 中对应部分精确
消去，真正剩余竞争是 \(\mathcal I_{\rm rel}\) 对 \(\mathcal B\)。
这不是把旧 remainder 改名：它把原先各为二阶 cut 大小的两项先精确
抵消，留下 quartic onset。

在六点基准上，独立 determinant-polynomial 路径得到

\[
E[S_AS_B]=-7.019102766297596,
\]

并把上述三个等式都复核到 \(1.5\times10^{-14}\) 内。

## 5. (mathcal B_+) 充分条件的逻辑强度

按 rectangle charge 的正部逐项求和，显然
\(\mathcal B\le\mathcal B_+\)，所以

\[
M''\ge\mathcal I_{\rm rel}-\mathcal B_+.
\]

定义

\[
\varepsilon_{\rm FB}
=[\mathcal B_+-\mathcal I_{\rm rel}]_+
\]

即可得 \(M''\ge-\varepsilon_{\rm FB}\)。若另有 S74 下界
\(M''\ge-B_\delta\|K_{AB}\|_{HS}^2\)，取两个 residual 的最小值
给出 never-worse hybrid bound，方向正确。

必须保持三层逻辑：

1. \(\mathcal B\le\mathcal I_{\rm rel}\) 与 \(M''\ge0\) **等价**，
   不是进展后的弱引理；
2. \(\mathcal B_+\le\mathcal I_{\rm rel}\) 是更强、直接可检查的充分
   条件；
3. 若该条件未在所有需要的尺度和整个参数区间上认证，rate 定理就没有
   闭合。

“可检查”不等于“已经检查所有尺度”。当前只有有限尺寸、有限参数点的
双精度诊断。

## 6. Merge tree 与 rate 接口

令 \(F_N=-H_N''\)。因为

\[
H_{AB}=H_A+H_B-M_{A,B},
\]

所以

\[
F_{AB}=F_A+F_B+M_{A,B}''.
\]

前 \(K\) 层使用 Fisher–Burg residual，后续层使用 S74 quadratic
bound，得到正文式 (31)。在后续层，每对不同 leaf 的无序 sites 只在
最低共同祖先 cut 收费一次，故

\[
\sum_{k>K}\sum_{\rm merges}\|K_{AB}\|_{HS}^2
=\frac{c^2}{2}
\left[
\operatorname{tr}Q_{\rho,qL}^2
-\frac q{2^K}\operatorname{tr}Q_{\rho,2^KL}^2
\right].
\]

独立在 \(\rho=.37,c=.91,L=2,q=8\) 的实际 Toeplitz 核上，对
\(K=0,1,2\) 逐 merge 求和，与 trace 公式的误差均小于
\(2.5\times10^{-16}\)。

固定 \(L,K\)，令 dyadic leaf 数 \(q\to\infty\)，使用
\(\operatorname{tr}Q_N=\rho N\) 与 Toeplitz平方迹极限，后续 tail
每单位长度变成

\[
\frac{B_\delta c^2}{2^{K+1}L}D_{\rho,2^KL}.
\]

因此式 (33)--(34) 是正确的**条件接口**，量词为：

- 一个在整个紧参数区间 \(J\) 上成立的 leaf seed 下界 \(f_L\)；
- 前 \(K\) 个固定尺度的统一 residual 上界 \(e_m(J)\)；
- 固定正 gap 的 S74 tail；
- 先有限体积积分，再取 entropy-value limit。

单点或有限网格上 \(\mathcal I_{\rm rel}-\mathcal B_+>0\) 不能令
\(e_m(J)=0\)，更不能覆盖无限多个尺度。当前稿没有提供这种全尺度、
连续参数认证。因此 merge tree 仍是有效接口，不是已完成的 rate 证明。

## 7. Cut 插值与 quartic onset

对

\[
K_t=\begin{pmatrix}K_A&tX\\tX^*&K_B\end{pmatrix},
\]

逐 word Schur complement 给出

\[
\frac{p_t(y)}{q(y)}
=\det(I-t^2B_y^{-1}X^*A_y^{-1}X).
\]

固定有限维与严格 gap 时一致解析，故

\[
g_t=1-t^2T+O(t^4).
\]

归一化 \(E_qg_t=1\) 迫使 \(E_qT=0\)。展开
\(E_q[g_t\log g_t]\) 后，线性项消失，得到

\[
M_t=\frac{t^4}{2}E_qT^2+O(t^6).
\]

在紧 gap 区间内可对 \(a\) 再微分两次，所以
\(M_t''=O(t^4)\)。同理
\(\partial_a\log g_t=O(t^2)\)，故
\(\mathcal I_{\rm rel}=O(t^4)\)；由 exact identity，
\(\mathcal B=O(t^4)\)。

这说明分别按 \(O(\|X\|_{HS}^2)\) 绝对支付
\(D_F,C_{\rm acc}\) 会丢掉真正的 leading cancellation。

## 8. 固定 \(\theta<1\) 的合法障碍

对 equal-marginal 两点严格 DPP，在 \(u=1/2\) 令
\(d=|z|^2\)、\(x=4d\)。精确公式是

\[
D_F=\frac{8x}{1-x},
\qquad
C_{\rm acc}=4\log\frac{1-x}{1+x}.
\]

因此

\[
D_F=32d+O(d^2),
\qquad
-C_{\rm acc}=32d+O(d^3),
\]

并且

\[
\frac{-C_{\rm acc}}{D_F}\to1.
\]

若存在统一 \(\theta<1\) 与 quartic residual \(Cd^2\)，除以 \(d\)
后令 \(d\downarrow0\) 会得到 \(32\le32\theta\)，矛盾。这里
\(d=\|K_{AB}\|_{HS}^2\)，故 \(d^2\) 确实是 cross amplitude 的四次项。

独立浮点探针得到：

| \(d\) | \(-C_{\rm acc}/D_F\) |
|---:|---:|
| \(10^{-2}\) | 0.96051249 |
| \(10^{-4}\) | 0.99960005 |
| \(10^{-6}\) | 0.99999600 |
| \(10^{-8}\) | 0.99999996 |

障碍只排除“固定 \(\theta<1\)+小于 quadratic 的 residual”。它不排除
\(\theta=1\)、另一个 quadratic residual 或利用固定 sine 几何的非微扰
估计；正文的限定正确。

## 9. 两点 (d^2) 下界

令 \(v=u(1-u)\)、\(\tau=u/(1-u)\)。展开精确两点
\(D_F+C_{\rm acc}\) 得

\[
M''=\sum_{k\ge2}A_kd^k,
\]

\[
A_k=2v^{-k}
\left[
\left(2-\frac1k\right)(\tau^k+\tau^{-k})
+(-1)^k\left(\frac{1-4v}{v}+\frac2k\right)
\right].
\]

\(k=1\) 系数精确消失。偶数 \(k\) 显然为正。奇数 \(k\ge3\) 时，

\[
\tau^k+\tau^{-k}\ge\tau+\tau^{-1},
\qquad
\frac{1-4v}{v}=\tau+\tau^{-1}-2,
\]

所以括号至少为

\[
\left(1-\frac1k\right)(\tau+\tau^{-1}+2)>0.
\]

又

\[
A_2=\frac{3-10v}{v^4}>0
\]

因为 \(v\le1/4\)。因此

\[
\boxed{M''\ge\frac{3-10u(1-u)}{u^4(1-u)^4}d^2},
\]

中点给出 \(M''\ge128d^2\)。系数和不等式正确；它是最小 cut 的
真实 quartic payment，但不能逐 entry 累加到大块，因为 PR64 已严格
认证六点 mixed-coordinate 负例。

独立在 \(u=.1,.25,.5,.75,.9\) 及四种合法 \(d\) 比例上复算，最小
浮点 slack 为 \(3.23\times10^{-6}>0\)。一般证明由上述正系数级数承担。

## 10. 有限诊断与证据等级纠正

作者脚本经过静态检查后实际执行，输出与正文表一致。它枚举全部 words，
没有删除稀有配置。独立重放没有复用作者 cofactor 导数，而是将每个 atom
重建为标量 determinant polynomial \(\det(aI+B_y)\)，直接微分多项式；
再另以五点有限差分核对六点 mutual information 曲率。

六点独立结果为：

\[
D_F=32.59075196032429,
\]

\[
C_{\rm acc}=-18.84098448997100,
\]

\[
\mathcal I_{\rm rel}=18.55254642772911,
\]

\[
\mathcal B=4.802778957375815,
\quad
\mathcal B_+=6.188926633071644,
\]

\[
M''=13.74976747035328,
\quad
\mathcal I_{\rm rel}-\mathcal B_+=12.36361979465747.
\]

独立实现与作者实现的最大差为 \(4.98\times10^{-14}\)；五点曲率为
13.7497671902，与解析浮点值相差约 \(2.8\times10^{-7}\)。45 点扫描的
最小 sufficient-condition value 复现为

\[
1.35757841311964
\]

at \(c=.925,a=.03,N=2\)。

正确的证据表述是：

- \(\mathcal I_{\rm rel}-\mathcal B_+\) **在代数上是严格下界公式**；
- 上述正数是该公式的 **NumPy double 浮点求值**；
- 没有 outward interval、精确有理误差或 directed rounding，因此不能
  标成 “Certified lower bound”；
- PR64 已区间认证同一六点的 \(D_F,C_{\rm acc},M''\)，但没有认证
  S77 新的 \(\mathcal I_{\rm rel},\mathcal B_+\) 数值。

所以“浮点基点上公式值为正”是强诊断，不是对 exact base point 的新
严格 B+ 证书。若需要该有限 seed 承担 rate 证明，至少应把
\(\mathcal I_{\rm rel}-\mathcal B_+\) 在参数区间上做外向区间认证。

## 11. 最小剩余义务

S77 把旧的粗 acceleration 支付压缩为更有结构的 Burg rectangle charge，
但没有支付完它。要产生新的 entropy-rate 区域，仍需至少完成：

1. 对某个固定 leaf seed \(L\) 和紧参数区间 \(J\)，严格认证
   \(F_L(a)\ge f_L\)；
2. 对 merge tree 前若干尺度，统一认证
   \(e_m(J)=[\mathcal B_+-\mathcal I_{\rm rel}]_+\) 的可支付上界，
   最理想是零；
3. 给出足够大的 \(K\)，使 S74 far tail
   \(B_\delta c^2D_{\rho,2^KL}/(2^{K+1}L)\) 小于 seed margin；
4. 将有限点诊断升级为连续参数、全部所需尺度的严格控制。

两点 \(d^2\) 下界不能直接逐边累加；\(\mathcal B\le\mathcal I_{\rm rel}\)
又与原目标等价。因而当前真正的新、非循环义务是对
\(\mathcal B_+\) 的 Toeplitz 多尺度上界，而不是再次陈述 exact identity。

## 12. 最终边界

- **已证：** 可见主体的 Fisher–Burg 恒等式、B+ 充分条件、条件
  merge-tree 接口、weak-cut \(\theta<1\) 障碍、两点 \(d^2\) 下界。
- **严格继承：** PR64 对六点 \(D_F,C_{\rm acc},M''\) 的区间符号。
- **仅浮点：** S77 的六点 \(\mathcal I_{\rm rel},\mathcal B_+\) 表和
  45 点扫描。
- **未证：** 全尺度 B+ 支付、正 rate margin、完整高对比度凹性。
- **未审：** 来源截断后的 Section 8 尾部。

因此 S77 提供了一个正确且比绝对值支付更精确的结构接口，但尚未把该
接口转化为完成率定理。
