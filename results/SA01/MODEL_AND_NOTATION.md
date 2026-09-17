> **待独立对抗性审查 / PENDING_INDEPENDENT_REVIEW。** 下文保留来源原文；其中 PROVED、PASS、AUDIT 等是作者或既有记录的表述，不代表本次 SA 成果已独立通过。先读本包根目录 REVIEW_REQUEST.md；外部审计与其他 SA 分开进行。

# SA01｜自包含模型与符号

本文件补齐 `REPORT.md` 中引用的任务记号，尤其是非中点推广中的权重。下列恒等式是任务提供的已审核输入，不作为本次新结论。

## 模型和导数方向

固定有限 Hermitian 收缩核 \(0\preceq Q\preceq I_n\)，
\(X\sim\operatorname{DPP}(Q)\)。给定 \(X\)，各坐标的输出独立，且
\[
\Pr(Y_i=1\mid X)=a+cX_i,\qquad 0<c<1,\quad 0<a<1-c.
\]
定义
\[
g_x(1)=a+cx,\quad g_x(0)=1-a-cx,\quad
f_y(x)=\prod_i g_{x_i}(y_i),\quad p_y=\mathbb E f_y(X),
\]
\[
\nu_y(x)=\Pr(X=x\mid Y=y)=\frac{\Pr(X=x)f_y(x)}{p_y}.
\]
严格正信道保证每个 \(p_y>0\)。所有对数是自然对数；所有 \(a\) 导数都固定 \(c,Q\)，作用于完整概率律。\(I=I(X;Y)\)，\(H(Y)=-\sum_y p_y\log p_y\)。

\(R^y\) 是完整后验 \(\nu_y\) 的 Hermitian DPP 核，
\[
C_y=\operatorname{Cov}(X\mid Y=y),\qquad
(C_y)_{ii}=R^y_{ii}(1-R^y_{ii}),\quad
(C_y)_{ij}=-|R^y_{ij}|^2\quad(i\ne j).
\]
这个协方差始终来自同一个完整后验；不能分别指定各 pair 的核后拼接。

## 完整信息、边际信息与缺失信息

令 \(q_i=Q_{ii}\)，并定义
\[
\tau_1=a(a+c),\quad
\tau_0=(1-a)(1-a-c),\quad
e_b=\frac c{\tau_b}\quad(b=0,1),
\qquad e_y=(e_{y_1},\ldots,e_{y_n})^T.
\]
\[
\mathcal D=\sum_i\left[
\frac{1-q_i}{a(1-a)}
+\frac{q_i}{(a+c)(1-a-c)}\right],
\qquad
F_{\rm marg}=\sum_i\frac1{(a+cq_i)(1-a-cq_i)}.
\]
\[
\Psi=\mathbb E_Y\sum_i e_{Y_i}^{\,2}(C_Y)_{ii},\qquad
\mathcal E=\mathbb E_Y e_Y^TC_Ye_Y,
\]
\[
\mathcal S=\mathbb E_Y\sum_{i<j}
e_{Y_i}e_{Y_j}|R^Y_{ij}|^2,\qquad
M=\Psi-\mathcal E=2\mathcal S\ge0.
\]
完整信道 score、真实输出 Fisher 与加速度项分别是
\[
\sigma_y(x)=\sum_i\frac{2y_i-1}{g_{x_i}(y_i)},\qquad
F=\sum_y\frac{(p_y')^2}{p_y},\qquad
A=-\sum_y p_y''\log p_y.
\]
任务提供精确恒等式
\[
F=\mathcal D-\mathcal E,\qquad
I''=A+\mathcal E,\qquad
H(Y)''=-\mathcal D+I''.
\]
并有已审核估计 \(\Psi\le\mathcal D-F_{\rm marg}\)。

## 实际 pair 条件表与任务旧余量

固定 \(i<j\)，令 \(z=Y_{-ij}\)；实际表为
\[
A_{uv}(z)=\Pr(Y_i=u,Y_j=v\mid Y_{-ij}=z)>0.
\]
每张表的四个元素总和为一，外部平均权重是实际
\(\Pr(Y_{-ij}=z)\)。定义
\[
d=A_{10}A_{01}-A_{00}A_{11}\ge0,\qquad
\Lambda=\log\frac{A_{10}A_{01}}{A_{00}A_{11}},\qquad
\Gamma=d\sum_{u,v}A_{uv}^{-1}.
\]
这里 \(A_{uv}\) 是条件原子，和上节的无下标加速度项 \(A\) 不同。

已审核重基和空间和恒等式是
\[
\Gamma_{ij}
=\mathbb E[e_{Y_i}e_{Y_j}|R^Y_{ij}|^2\mid Y_{-ij}],
\qquad
A=2\sum_{i<j}\mathbb E_{Y_{-ij}}\Lambda_{ij}.
\]
当 \(c^2\le23/25\) 时，任务允许取 \(\kappa=2\)，从而
\[
\mathcal R_2
=2\sum_{i<j}\mathbb E_{Y_{-ij}}(2\Gamma_{ij}-\Lambda_{ij})\ge0,
\]
\[
I''=2\Psi-\mathcal E-\mathcal R_2.
\]
本次新证书的定义见 `REPORT.md` (1.3)、(1.4)、(1.5)、(5.10)，不使用本节的旧差循环定义。

## 三个作用域必须区分

主模型是偶数 \(n=2m\ge4\) 的连续频率循环投影
\[
Q=UU^*,\qquad
U_{jr}=n^{-1/2}e^{2\pi{\rm i}jr/n},\quad
0\le j<n,\quad0\le r<m,
\]
以及 \(c=19/20,\ a=1/40\)。此时
\[
e_0=e_1=e=\frac{1520}{39},\qquad
\mathcal D=\frac{1600}{39}n,\qquad F_{\rm marg}=4n,
\]
\[
\mathcal E=e^2\,\mathbb E\operatorname{Var}(|X|\mid Y)=0.
\]
零缺失共同 score 能量不表示每个坐标的后验方差为零。

有限 Toeplitz 推广使用
\[
Q_{ii}=1/2,\qquad
Q_{ij}=\frac{\sin(\pi(i-j)/2)}{\pi(i-j)}.
\]
它不是有限投影，不能把 \(\mathcal E\) 置零。正文通过投影扩张证明压缩谱界；辅助坐标没有成为额外观测或额外支付来源。

固定 \(c=19/20\) 的非中点循环推广使用本文件的一般 \(\tau_b,e_b,\Psi,\mathcal E\)。此时同样不能一般地令 \(\mathcal E=0\)；正文没有把中点的 \(7/4\) 系数宣称为整个 offset 区间的结论。

来源：同分支的 `research_prompts/pro_tasks/TASK_01_POSTERIOR_SLACK.md`、
`research_prompts/pro_tasks/sources/S4_PROOF.md` 及
`research_prompts/pro_tasks/sources/S4_AUDIT.md`。本文只整理给定的数学接口；新证明与尚未闭合的支付阈值分别在 `REPORT.md` 第 1–11 节。
