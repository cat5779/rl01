> **待独立对抗性审查 / PENDING_INDEPENDENT_REVIEW。** 下文保留来源原文；其中 PROVED、PASS、AUDIT 等是作者或既有记录的表述，不代表本次 SA 成果已独立通过。先读本包根目录 REVIEW_REQUEST.md；外部审计与其他 SA 分开进行。

# SA01：真实后验的重叠反约束余量证书

**PROVED / DISPROVED / INCOMPLETE**

**PROVED。** 在真实循环半密度投影、`c=19/20, a=1/40` 上，构造下文的有理条件表证书 \(\mathcal T\)、后验相容性泛函 \(\mathfrak J\) 和重叠边泛函 \(\mathfrak W\)，证明
\[
\mathcal R_2\ge \frac15(\Psi-\mathcal E)+\mathcal T,\qquad
\mathcal T\ge B\,\mathbb E\mathfrak J(R^Y)
             \ge B\,\mathbb E\mathfrak W(R^Y),
\quad B=\frac{1478656}{6591}.
\tag{A}
\]
另由真实 Fourier 两点压缩的谱间隙，证明
\[
\mathcal R_2\ge\frac14(\Psi-\mathcal E).
\tag{B}
\]
(A) 的结构性部分不是把原差换名：(i) 定义不含 \(\Lambda\)、原余量或目标 Hessian；(ii) 它的零集有显式的二点块分类；(iii) 原余量在该零集上仍可严格为正。

**DISPROVED。** 第一版局部线性桥
\[
2\Gamma-\Lambda\ \stackrel{\rm false}{\ge}\
\frac{2c^2}{s_{\max}}h\Gamma
\]
被真实 \(P_{4,2}\) 的一个有理条件表反驳，反例余差有严格的有理上界 \(<-1/3\)。错误是把
\(\partial_sG=e^t+e^{-t}-2\) 当成 \(e^t-e^{-t}\)。正文保留反例，不把失败版本隐去。

**INCOMPLETE。** 没有证明这些支付足以使所有维数的真实熵 Hessian 非正，也没有证明熵率的全部参数区域凹性。精确尚缺的支付阈值在第 10 节。有限 Toeplitz 推广与非中点推广分别给出独立证明，不将 Toeplitz 压缩认作有限投影。

本文的 PROVED 表示下列推导已经闭合；不是外部同行复核已经完成的声明。

## 0. 模型、记号与允许使用的输入

主模型选择偶数 \(n=2m\ge4\) 的真实连续频率循环投影
\[
Q=UU^*,\qquad U_{jr}=n^{-1/2}\exp(2\pi {\rm i}jr/n),
\quad 0\le j<n,\quad0\le r<m.
\tag{0.1}
\]
不是小块直和输入，也不是有限 sine Toeplitz 压缩。以下始终使用
\[
X\sim{\rm DPP}(Q),\qquad
\Pr(Y_i=1\mid X)=a+cX_i,\qquad c=\frac{19}{20},\quad a=\frac1{40}.
\]
所有 \(a\) 导数固定 \(c,Q\)，所有对数为自然对数。

令
\[
b=1-a=\frac{39}{40},\quad
\omega=\frac ba=39,\quad
\tau=ab=\frac{39}{1600},\quad
e=\frac c\tau=\frac{1520}{39},
\]
\[
s_*=\frac{1-c^2}{2}=\frac{39}{800},\qquad
s_{\max}=\frac{1+c^2}{2}=\frac{761}{800},\qquad \gamma=\frac95.
\tag{0.2}
\]
\(R^y\) 是完整真实后验 \(\nu_y=\operatorname{Law}(X\mid Y=y)\) 的核，不是仅观察一个位点的后验，也不是产品近似。记
\[
r_i=R_{ii},\quad w_{ij}=|R_{ij}|^2,\quad v_i=r_i(1-r_i),\quad
m_i=\sum_{j\ne i}w_{ij}.
\]
对主模型，正的坐标似然倾斜保持投影性，所以每个 \(R^y\) 都是秩 \(m\) 的投影。此处
\[
\Psi=e^2\mathbb E\sum_i v_i,\qquad
\mathcal E=e^2\mathbb E\operatorname{Var}(|X|\mid Y)=0.
\tag{0.3}
\]
保留 \(\mathcal E\) 的公式用于区分可以迁移到一般压缩的部分。归一后验共同位移的一阶 tangent 在中点消失；本文没有用 \(\Psi\le C\mathcal E\)。

任务文件提供并允许直接使用的恒等式是
\[
M:=\Psi-\mathcal E
=2\sum_{i<j}\mathbb E_{Y_{-ij}}\Gamma_{ij}\ge0,
\]
\[
I''=2\Psi-\mathcal E-\mathcal R_2,\qquad
H(Y)''=-\mathcal D+I'',\qquad
\Psi\le\mathcal D-F_{\rm marg}.
\tag{0.4}
\]
在主模型，
\(\mathcal D=(1600/39)n,\ F_{\rm marg}=4n\)。
这些是起点，不算本交付的新结论。

## 1. 候选工具的明确定义

### 1.1 有理条件表证书

固定 \(i<j\)，取实际外部输出 \(z=Y_{-ij}\)。四原子表
\[
A_{uv}=\Pr(Y_i=u,Y_j=v\mid z),\qquad u,v\in\{0,1\}
\]
严格为正、总和为一。令
\[
d=A_{10}A_{01}-A_{00}A_{11}\ge0,\quad
\Gamma=d\sum_{u,v}A_{uv}^{-1},\quad
\Delta=\frac{d^2}{A_{00}A_{10}A_{01}A_{11}},
\]
\[
h=\frac{A_{00}+A_{11}-s_*}{c^2}.
\tag{1.1}
\]
第 3 节证明这里的 \(h\) 恰好是
\(\Pr(X_i=X_j\mid Y_{-ij}=z)\)，因而 \(0\le h\le1\)。

定义一个固定的、显式的有理函数
\[
\chi(h)=\min\left\{\frac45,\ \frac{72h}{25+40h}\right\}.
\tag{1.2}
\]
本交付的条件表工具为
\[
\boxed{\displaystyle
\mathcal T(Q,a,c)=
2\sum_{i<j}\mathbb E_{Y_{-ij}}
\max\{\chi(h_{ij})\Gamma_{ij},\ \gamma c^2 h_{ij}\Delta_{ij}\}.}
\tag{1.3}
\]
每一项都是允许的实际条件表的有理函数。定义不引用 \(\Lambda\)、\(\mathcal R_2\)、\(I''\) 或 \(H''\)。两个下界取 **max 而不相加**，以免重复支付同一个局部差。

### 1.2 同一个完整后验上的相容性对象

对任何 Hermitian 收缩核 \(R\)，定义
\[
h_{ij}(R)=1-r_i-r_j+2r_ir_j-2w_{ij}
=\Pr_R(X_i=X_j),
\]
\[
\boxed{\displaystyle
\mathfrak J(R)=\sum_{i<j}w_{ij}h_{ij}(R),}
\tag{1.4}
\]
以及
\[
\boxed{\displaystyle
\mathfrak W(R)=\sum_i\left(m_i^2-\sum_{j\ne i}w_{ij}^2\right)
=2\sum_i\sum_{\substack{j<k\\j,k\ne i}}w_{ij}w_{ik}.}
\tag{1.5}
\]
\(\mathfrak W\) 测量共享中心的两条非零相关边。它只用一个完整后验的核，所有边来自同一个 \(R^y\)。

可取较弱、但完全核化的证书
\[
\mathcal L_{\rm ker}
=\frac15M+B\,\mathbb E\mathfrak J(R^Y)
\quad\text{或}\quad
\frac15M+B\,\mathbb E\mathfrak W(R^Y).
\tag{1.6}
\]
对主模型还可把两个已证界组合成
\[
\boxed{\displaystyle
L_{\rm SA01}=\frac15M+\max\{\mathcal T,\ M/20\}.}
\tag{1.7}
\]
最终证明的是 \(\mathcal R_2\ge L_{\rm SA01}\)，不是以原差定义 \(L_{\rm SA01}\)。

## 2. 域外迁移：从反约束失配到谱相容性

源机制是加权二元反约束。对固定非负图权 \(w_{ij}\)，约束 \(X_i\ne X_j\) 的未满足代价为
\[
\sum_{i<j}w_{ij}{\bf1}_{\{X_i=X_j\}}
=\frac12\sum_{i<j}w_{ij}(1+\sigma_i\sigma_j),
\quad \sigma_i=2X_i-1.
\tag{2.1}
\]
它是加权 MAX CUT 目标的补量；这个标准编码可见 Goemans–Williamson [GW95] 第 2 节。这里不使用其近似算法或近似比，也不把它当作后验定理。

本题的对应是：取**真实后验**作为二元配置分布，再以该后验自身的
\(|R_{ij}|^2\) 为图权。于是 (2.1) 的后验均值就是 \(\mathfrak J(R)\)。
源机制需要同一组随机变量与同一张图；各 pair 自由选取的条件表不满足这个要求。因此必须先用 Bayes 重基把各个外部条件律送回同一个完整后验。

仅迁移奇环冲突是不够的。真实 \(P_{4,2}\) 的原核图是一张四圈：邻边权 \(1/8\)，对角线权零。纯 MAX CUT 未满足代价的最小值为零，交替着色就满足全部边；但实际
\(\mathfrak J(Q)=\mathfrak W(Q)=1/8>0\)。
任意二元律可以集中在交替配置上，DPP 后验却还必须满足所有非正交叉协方差和核谱约束。

新增的构件有两个。第一是第 4 节的有限似然比 Bayes 桥，把标量等号缺陷送回真正共同的后验。第二是第 5 节的谱刚性恒等式，它把“两个反约束共享一个变量”变成显式非负的边乘积；并进一步给出到二点块投影集合的定量稳定性估计。它们不来自 MAX CUT 近似定理。这里主张的是一项已写出证明的机制迁移，不主张未经全面文献核查的首次发明。

## 3. P1 与标量稳定性：所有表都是实际条件表

### 3.1 等输出质量与真正输入等号事件

在中点，若输入两位相反，输出相同的概率为 \(2ab=s_*\)；若输入两位相同，输出相同的概率为 \(a^2+b^2=s_{\max}\)。对真实外部条件律平均，
\[
s:=A_{00}+A_{11}=s_*+(s_{\max}-s_*)h=s_*+c^2h.
\tag{3.1}
\]
这证明 (1.1) 的 \(h\) 有真实概率意义。没有调整表的边际、外部权重或归一化。

仅在证明中引入
\[
t=\log\frac{A_{10}A_{01}}{A_{00}A_{11}}\ge0.
\]
四原子代数给出
\[
\Gamma=G(s,t):=s(e^t-1)+(1-s)(1-e^{-t}),
\quad
\Delta=e^t+e^{-t}-2.
\tag{3.2}
\]
例如，令 \(p=A_{00}A_{11}\)、\(q=A_{10}A_{01}=pe^t\)，则
\(d\sum A^{-1}=(e^t-1)s+(1-e^{-t})(1-s)\)，而
\(d^2/(pq)=e^t+e^{-t}-2\)。

### 3.2 一个解析校准：\(\gamma=9/5\)

**引理 3.1。** 对所有 \(t\ge0\)，
\[
t\le\frac95G(39/800,t).
\tag{3.3}
\]

**证明。** 置
\[
F(t)=\frac{351}{4000}e^t-\frac{6849}{4000}e^{-t}
+\frac{3249}{2000}-t.
\]
\(F(0)=0\)。其导数的两个零点对应
\[
z_\pm=e^t=\frac{2000\pm\sqrt{1596001}}{351},
\]
两根均大于一，故最小值只能出现在 \(t=0\) 或 \(\log z_+\)。
在后者，
\[
F(\log z_+)=
\frac{3249+\sqrt{1596001}}{2000}-\log z_+.
\]
由 \(1263^2<1596001<1264^2\)，有
\(z_+<1088/117\)。有限 Taylor 下界给出
\[
e^{9/4}>\sum_{k=0}^6\frac{(9/4)^k}{k!}
=\frac{3082913}{327680}>\frac{1088}{117}.
\]
因此
\[
F(\log z_+)>\frac{3249+1263}{2000}-\frac94=\frac3{500}>0.
\]
导数分段符号与 \(F(0)=0\) 完成整个半轴上的证明。没有参数拟合。∎

这个纯标量校准不是本交付的主要创造性内容；它为后面的结构支付提供明确系数。

### 3.3 两个不循环定义的稳定性下界

**引理 3.2。** 对任何上述真实中点条件表，
\[
\gamma\Gamma-t\ge\chi(h)\Gamma,\qquad
\gamma\Gamma-t\ge\gamma c^2h\Delta.
\tag{3.4}
\]

**证明。** 当 \(0\le h\le1/2\) 时，对 \(s\) 的仿射性给出
\[
G(s_*+c^2h,t)
=(1-2h)G(s_*,t)+2hG(1/2,t).
\]
而 \(G(1/2,t)=\sinh t\ge t\)。由引理 3.1，
\[
\Gamma\ge\frac{1+2(\gamma-1)h}{\gamma}\,t.
\]
移项即得
\[
\gamma\Gamma-t\ge
\frac{2\gamma(\gamma-1)h}{1+2(\gamma-1)h}\Gamma.
\]
当 \(h\ge1/2\)，\(s\ge1/2\)，故 \(\Gamma\ge t\)，从而差至少为
\((\gamma-1)\Gamma\)。两段正好组成 \(\chi\)。

第二个下界直接来自正确的斜率
\[
G(s_*+c^2h,t)=G(s_*,t)+c^2h\Delta
\]
及引理 3.1。这里的增量是二次型 \(\Delta\)，不是双曲正弦项。∎

把两个界取最大值、按实际外部概率求和，
\[
2\sum_{i<j}\mathbb E(\gamma\Gamma-\Lambda)\ge\mathcal T.
\tag{3.5}
\]
又由 \(M=2\sum\mathbb E\Gamma\)，得到
\[
\mathcal R_2
=\frac15M+2\sum_{i<j}\mathbb E(\gamma\Gamma-\Lambda)
\ge\frac15M+\mathcal T.
\tag{3.6}
\]
(3.6) 的证明允许出现旧差；候选 (1.3) 的**定义**完全不含它。

## 4. P1 的共同后验重基与支付系数

令 \(h_y=\Pr(X_i=X_j\mid Y=y)\)，外部条件下的相应概率仍记 \(h\)。
对固定两位输出 \(u,v\)，任意一个等输入状态与任意一个异输入状态只差一位。中点信道下，它们的似然比介于 \(1/\omega\) 与 \(\omega\)。
在两个事件内部按真实条件概率平均，仍有这个界。因此
\[
h_y\le\frac{\omega h}{1+(\omega-1)h}.
\tag{4.1}
\]
\(h=0,1\) 的情形由直接观察或连续延拓处理。

由于 \(\omega=39\ge2\gamma\)，分两段比较分母可得
\[
\chi(h)\ge \frac{2\gamma(\gamma-1)}{\omega}\,h_y.
\tag{4.2}
\]
具体地，\(h\le1/2\) 时使用
\(\omega-1\ge2(\gamma-1)\)；\(h\ge1/2\) 时使用
\(h_y\le1\) 与 \(2\gamma/\omega\le1\)。

任务提供的精确 Bayes 重基在中点写成
\[
e^2|R^{z,u,v}_{ij}|^2=\frac{d}{A_{uv}^2},
\quad
\Gamma=\sum_{u,v}A_{uv}e^2|R^{z,u,v}_{ij}|^2.
\tag{4.3}
\]
把 (4.2) 乘以 (4.3) 中各非负权并求和，
\[
\chi(h)\Gamma
\ge \frac{2\gamma(\gamma-1)e^2}{\omega}
\mathbb E[w_{ij}(R^Y)h_{ij}(R^Y)\mid Y_{-ij}].
\]
再求外部期望与空间和，得到
\[
\boxed{\displaystyle
\mathcal T\ge
\frac{4\gamma(\gamma-1)e^2}{\omega}
\,\mathbb E\mathfrak J(R^Y)=B\,\mathbb E\mathfrak J(R^Y).}
\tag{4.4}
\]
这一步是相容性所在：右边所有边和共享顶点都属于同一个完整后验 \(R^Y\)。
没有把不同 \(Y_{-ij}\) 下的核混合成一张假图；外部权重也没有被固定不动或漏求平均。

## 5. P2：重叠约束的刚性、零集与定量稳定性

### 5.1 精确的谱刚性分解

**引理 5.1。** 对任何 Hermitian 收缩核 \(R\)，置
\(\eta_i=(R-R^2)_{ii}\ge0\)，则
\[
h_{ij}(R)
=(r_i+r_j-1)^2
+\sum_{k\ne i,j}(w_{ik}+w_{jk})+\eta_i+\eta_j,
\tag{5.1}
\]
\[
\boxed{\displaystyle
\mathfrak J(R)
=\mathfrak W(R)
+\sum_{i<j}w_{ij}(r_i+r_j-1)^2
+\sum_i\eta_i m_i.}
\tag{5.2}
\]
对于投影，最后一项为零。

**证明。** \((R^2)_{ii}=r_i^2+m_i\)，所以
\(r_i(1-r_i)=m_i+\eta_i\)。将其代入
\[
h_{ij}=(r_i+r_j-1)^2+
r_i(1-r_i)+r_j(1-r_j)-2w_{ij}
\]
得到 (5.1)。乘以 \(w_{ij}\) 后求和，注意
\[
\sum_{i<j}w_{ij}(m_i+m_j)=\sum_i m_i^2,\quad
2\sum_{i<j}w_{ij}^2=\sum_i\sum_{j\ne i}w_{ij}^2,
\]
即可得到 (5.2)。∎

因此 \(\mathfrak J\ge\mathfrak W\ge0\)。这给出 (A) 的最后一步。

### 5.2 零集不是“所有块都能分别取最坏值”

对投影 \(R\)，\(\mathfrak W(R)=0\) 当且仅当非零非对角图的每个顶点度数至多为一。于是 \(R\) 经置换后是以下块的直和：单点 \(0\) 或 \(1\)，以及 \(2\times2\) 的秩一投影。反过来，这些块显然使 \(\mathfrak W=\mathfrak J=0\)。

证明非平凡方向只需观察：每个互不重叠的非对角二点块仍是投影；非零非对角元排除秩零和秩二，因此其秩是一。此时两条对角线之和为一，(5.2) 的平方项也为零。

更直接地，若 \(w_{ij}>0\) 且 \(h_{ij}=0\)，则 (5.1) 强迫
\(r_i+r_j=1\) 且所有 \(w_{ik},w_{jk}\)（\(k\ne i,j\)）为零。因此两个共享一个顶点、且具有正权的反约束不能同时精确饱和。这比奇环冲突强：即使图是二分图，重叠仍有代价。这里识别的是标量证明将 \(s\) 降到 \(s_*\) 这一步在正相关分支上的同时饱和情形，不声称仅靠这一分类就确定整条标量不等式的所有极值参数。

对一般收缩核，\(\mathfrak J=0\) 的分类是：非零非对角块仍只能是秩一二点投影，剩余单点可为任意 \([0,1]\) 内的 Bernoulli 参数。\(\mathfrak W=0\) 本身在非投影情形较弱，不能删掉 (5.2) 的 \(\eta_i m_i\) 项。

### 5.3 条件表证书的零集

在严格正信道下，\(\mathcal T=0\) 当且仅当
\(\mathbb E\mathfrak J(R^Y)=0\)。一个方向由 (4.4) 得到。反方向：若外部表 \(d>0\)，则 (4.3) 使四个完整后验的 \(w_{ij}\) 都为正；\(\mathbb E\mathfrak J=0\) 迫使这四个 \(h_y=0\)，从而外部 \(h=0\)，该项 \(\mathcal T\) 为零。若 \(d=0\)，两项本来都为零。

对投影输入，\(Y\equiv0\) 的后验恰好等于原投影，因为每个输入配置都有固定计数。同理 \(Y\equiv1\)。
所以 \(\mathcal T=0\) 当且仅当原投影是上述互不重叠二点块与确定单点的直和。主模型 \(Q_n\)（\(n\ge4\)）不是这种投影。

特别地，秩一二点投影可有 \(\mathcal T=\mathfrak J=\mathfrak W=0\)，而 \(\mathcal R_2>0\)；引理 3.1 的 \(\gamma<2\) 已显示，只要 \(\Gamma>0\)，原二倍差仍严格为正。因此本对象并非原差的改名。

### 5.4 可复用的“距等号集合”估计

令 \(\mathcal Z_m\) 是秩 \(m\)、经置换后由至多二点块组成的投影集合。
以 Frobenius 范数记距离。

**命题 5.2。** 对任意秩 \(m\) 的 \(n\) 维投影，
\[
\boxed{\displaystyle
\operatorname{dist}_F(R,\mathcal Z_m)^2
\le (3+\sqrt5)\sqrt{n\,\mathfrak W(R)}.}
\tag{5.3}
\]
因此
\[
\mathcal T\ge
\frac{B}{(3+\sqrt5)^2n}
\mathbb E\,\operatorname{dist}_F(R^Y,\mathcal Z_m)^4.
\tag{5.4}
\]
(5.4) 只是同一个已证工具的稳定性解释；无需求这个距离即可使用 (1.3) 或 (1.5)。

**证明。** 若 \(W:=\mathfrak W(R)=0\)，上一小节已证明。设 \(W>0\)，取
\(\epsilon=\sqrt{W/n}\)。在权图 \(w_{ij}\) 上不断选一条当前权至少为 \(\epsilon\) 的边并删除其两端点，留下一个 matching；不存在这种边时停止。某次选边的权为 \(w\)，因本次删除而丢弃的其他边总权为 \(D\)，则两个端点的原始 wedge 量至少为 \(2wD\)。各次选取端点不重叠，故重边阶段丢弃总权至多 \(W/(2\epsilon)\)。

余图每条边权小于 \(\epsilon\)。设其总边权为 \(L\)，度权为 \(d_i\)。其 wedge 量不超过原 \(W\)，另一方面
\[
W\ge \sum_i d_i^2-\sum_{i,j}w_{ij}^2
\ge \frac{4L^2}{n}-2\epsilon L.
\]
解二次式，
\[
L\le\frac{n\epsilon+\sqrt{n^2\epsilon^2+4nW}}4
=\frac{1+\sqrt5}{4}\sqrt{nW}.
\]
所以 matching 之外的总边权
\[
D_{\rm all}\le\frac{3+\sqrt5}{4}\sqrt{nW}.
\]

从 \(R\) 删去 matching 之外的非对角元，得块对角收缩 \(R_0\)，块尺寸至多二。它保留迹 \(m\)，并且
\[
\|R-R_0\|_F^2=2D_{\rm all},\qquad
\operatorname{Tr}(R_0-R_0^2)=2D_{\rm all}.
\]
按块特征向量选取 \(R_0\) 的最大的 \(m\) 个特征值并置为一，其余置零，得 \(P_0\in\mathcal Z_m\)。若 \(0\le\lambda_i\le1\) 且 \(\sum\lambda_i=m\)，则
\(\sum\lambda_i^2\le\sum_{i\le m}\lambda_i\)（降序排列；可用第 \(m\) 个特征值比较上下两部分）。因而
\[
\|R_0-P_0\|_F^2\le\operatorname{Tr}(R_0-R_0^2).
\]
块外差与块内差 Frobenius 正交，得到
\(\|R-P_0\|_F^2\le4D_{\rm all}\)，即 (5.3)。∎

### 5.5 空间聚合和局部证书

(1.5) 中每个以 \(i\) 为中心、叶子为无序对 \(\{j,k\}\) 的 wedge 只出现一次，系数为二。可以只保留某个空间尺度内的 wedge，也可以给每个 wedge 一个 \([0,1]\) 权重；所得 \(\mathfrak W_{\rm loc}\le\mathfrak W\) 仍是合法支付。若多个局部块覆盖同一 wedge，分配系数的总和须不超过一。

这给出明确的“不重复消费”规则。不能对任意许多重叠块各付一次完整 \(\mathfrak W\)，也不能用不同外部后验各自优化权图。

### 5.6 正坐标场下的维数无关稳定性

下面的性质使 \(\mathfrak W\) 不只适用于有统一两点谱间隙的投影。

**命题 5.3。** 设 \(K\) 是任意有限 Hermitian 收缩，真实 DPP 律按正场
\(\prod_i d_i^{X_i}\) 倾斜后核为 \(R_d\)。则
\[
\boxed{\displaystyle
e^{-10\|\log d\|_\infty}\mathfrak W(K)
\le\mathfrak W(R_d)
\le e^{10\|\log d\|_\infty}\mathfrak W(K).}
\tag{5.5}
\]
若 \(K\) 是投影，还可用全局场缩放不变性把因子改写为
\((d_{\max}/d_{\min})^{\pm5}\)。

**证明。** 取辅助场路径 \(\prod_i d_i^{tX_i}\)，\(0\le t\le1\)，并写
\(H=\operatorname{diag}(\log d_i)\)、\(h_\infty=\|H\|\)。
可选 Hermitian 后验核满足
\[
\dot R=\tfrac12(HR+RH)-RHR.
\tag{5.6}
\]
对投影由 (6.2) 求导即得；对一般收缩，可用 (11.1) 的投影扩张并在辅助坐标上放零场，取左上压缩，得到同一个闭合方程。这个 \(t\) 是证明用的坐标场插值，不是目标函数的 \(a\) 导数。

令 \(A=R-\operatorname{diag}(r_i)\)。由于 \(0\preceq R\preceq I\)，
\(-I\preceq A\preceq I\)，故 \(\|A\|\le1\)；又
\[
|A_{ik}|^2=w_{ik}\le m_i\le r_i(1-r_i)\le1/4.
\]
在非对角位置，
\[
\dot A_{ij}=b_{ij}A_{ij}-(AHA)_{ij},\qquad
b_{ij}=h_i(1/2-r_i)+h_j(1/2-r_j),\quad |b_{ij}|\le h_\infty.
\]

对互异 \(i,j,k\) 定义张量 \(T_{ijk}=A_{ij}A_{ik}\)，其他位置置零，则
\(\|T\|_F^2=\mathfrak W(R)\)。直接系数项
\((b_{ij}+b_{ik})T_{ijk}\) 的范数至多 \(2h_\infty\|T\|_F\)。
对卷积项
\[
(AHA)_{ij}A_{ik}
=\sum_{\ell\ne k}h_\ell A_{\ell j}T_{i\ell k}
+h_k A_{kj}A_{ik}^{\,2},
\]
第一部分是矩阵 \(A^\mathsf{T}H\) 作用于固定 \(i\) 的叶子指标，然后限制到互异指标，因此总 Frobenius 范数至多
\(h_\infty\|T\|_F\)。第二部分的平方范数至多
\[
h_\infty^2\sum_k\sum_{i\ne k}w_{ik}^2(m_k-w_{ik})
\le\frac{h_\infty^2}{4}\mathfrak W(R).
\]
另一个卷积项同样估计，所以
\[
\|\dot T\|_F\le
(2+1+\tfrac12+1+\tfrac12)h_\infty\|T\|_F
=5h_\infty\|T\|_F.
\]
从而
\[
|\dot{\mathfrak W}|\le10h_\infty\mathfrak W.
\]
Gronwall 的上下界给出 (5.5)，也涵盖 \(\mathfrak W=0\)。
投影情况下，全局乘 \(d_i\) 一个共同正数不改变律；将 \(\log d_i\) 中心化到最大最小值的中点，即得所述比值版本。∎

对中点实际信道，每个 \(d_i\in\{\omega,\omega^{-1}\}\)，故
\[
\boxed{\mathcal T\ge
B\,\mathbb E\mathfrak W(R^Y)
\ge B\,\omega^{-10}\mathfrak W(Q).}
\tag{5.7}
\]
这是一条只用原核即可读出的、较保守的结构性证书。它不把后验直接替换成原核，而是支付了明确的场稳定性损失。指数 10 未宣称最优。

### 5.7 保留自适应权重：一个纯重叠支付，而不先损失到常数 \(B\)

统一 Bayes 常数很保守。可以保留条件表权重，再作同一个后验的几何分解，而不多消费一份局部差。

对外部表 \(\Gamma>0\)，定义
\[
q_{ij}(z)=
\max\{\chi(h),\ \gamma c^2h\Delta/\Gamma\};
\]
若 \(\Gamma=0\)，令 \(q_{ij}=0\)。对完整输出 \(y\)，置
\[
\lambda_{ij}(y)=
\begin{cases}
q_{ij}(y_{-ij})/h_{ij}(R^y),&h_{ij}(R^y)>0,\\
0,&h_{ij}(R^y)=0.
\end{cases}
\tag{5.8}
\]
后一情形中严格正信道保证外部 \(h=0\)，所以 \(q_{ij}=0\)，这个约定没有丢失质量。权重不含原余量或任何对数。它们也不会因分母趋零而无控发散：事件似然比的两向界给出 \(h/h_y\le\omega\)，且
\(\Delta/\Gamma\le1/s\le1/s_*\)，所以
\[
0\le\lambda_{ij}\le
\max\{2\gamma(\gamma-1)\omega,\ \gamma c^2\omega/s_*\}
=\frac{6498}{5}.
\]

精确重基给出
\[
\mathcal T
=2e^2\mathbb E\sum_{i<j}
\lambda_{ij}w_{ij}h_{ij}.
\]
将 (5.1) 乘以这些非负的、同一完整后验上的权重，得到
\[
\begin{aligned}
\frac{\mathcal T}{2e^2}
=\mathbb E\Bigg[&
\sum_i\sum_{\substack{j<k\\j,k\ne i}}
(\lambda_{ij}+\lambda_{ik})w_{ij}w_{ik}\\
&+\sum_{i<j}\lambda_{ij}w_{ij}(r_i+r_j-1)^2
+\sum_i\eta_i\sum_{j\ne i}\lambda_{ij}w_{ij}\Bigg].
\end{aligned}
\tag{5.9}
\]
这是一次精确的预算分解，不是三份可另行相加的新支付。

定义纯重叠证书
\[
\boxed{\displaystyle
\mathcal T_{\rm ov}
=2e^2\mathbb E
\sum_i\sum_{\substack{j<k\\j,k\ne i}}
(\lambda_{ij}+\lambda_{ik})w_{ij}w_{ik}.}
\tag{5.10}
\]
于是
\[
\boxed{\displaystyle
\mathcal R_2\ge\frac15M+\mathcal T_{\rm ov},\qquad
\mathcal T\ge\mathcal T_{\rm ov}\ge B\,\mathbb E\mathfrak W(R^Y).}
\tag{5.11}
\]
最后一步也有明确的逐项证明：若一个 wedge 的乘积为正，(5.1) 使其两条边的 \(h_y\) 都为正；由 (4.2)，每条相关 \(\lambda\) 至少为
\(2\gamma(\gamma-1)/\omega\)，再检查 (1.5) 中的因子二即可。

因此纯重叠部分本身就保持维数一致的正性；局部块可以分配 (5.10) 中已有的 weighted wedge，但每个 wedge 的累计分配比例不超过一。这个自适应形式避免把所有局部系数先降到最坏常数 \(B\)。

## 6. P3：真实 Fourier 几何强迫一个均匀的局部余量

### 6.1 两点原压缩有确定谱间隙

对 (0.1)，若 \(i\ne j\)，
\[
|Q_{ij}|=\frac{|\sin(\pi(i-j)/2)|}{n|\sin(\pi(i-j)/n)|}
\le\frac1{n\sin(\pi/n)}
\le\frac1{2\sqrt2}<\frac5{14}.
\]
最后一个非严格界对偶数 \(n\ge4\) 成立：\(x\sin(\pi/x)\) 在 \(x\ge2\) 上递增，可直接对其求导证明。于是每个二点集合 \(S\) 满足
\[
\frac17I_S\preceq Q_S\preceq\frac67I_S.
\tag{6.1}
\]
这是实际连续 Fourier 子空间的性质，不是给各 pair 单独挑选一个核。

### 6.2 正坐标倾斜的压缩谱界

投影输入的正坐标倾斜有显式公式
\[
R_D=D\,U(U^*D^2U)^{-1}U^*D.
\tag{6.2}
\]
证明可由 Cauchy–Binet 得到：固定计数原子乘以
\(\prod_{i\in X}D_i^2\)，归一常数为 \(\det(U^*D^2U)\)，归一后的原子正是 (6.2) 对应投影的行列式。对实际完整后验，\(D_i^2=g_1(y_i)/g_0(y_i)\)；对 \(Y_{-S}\) 后验，令未观测的 \(S\) 上 \(D_i^2=1\)。

**引理 6.1。** 假设
\[
\alpha I_S\preceq Q_S\preceq(1-\alpha)I_S,\quad0<\alpha\le1/2.
\]
若 \(S\) 上的 \(D_i^2\) 落在 \([\ell_S,u_S]\)，补集上落在
\([\ell_T,u_T]\)，则 \(R_{D,S}\) 的特征值处在
\[
\left[
\frac{\alpha\ell_S}{\alpha\ell_S+(1-\alpha)u_T},\
1-\frac{\alpha\ell_T}{\alpha\ell_T+(1-\alpha)u_S}
\right].
\tag{6.3}
\]

**证明。** 令 \(V=U_S,\ A=VV^*=Q_S,\ B_0=V^*V\)，并令
\(Z=U_{S^c}^*D_{S^c}^2U_{S^c}\)。因 \(\|A\|<1\)，
\[
\ell_T(I-B_0)\preceq Z\preceq u_T(I-B_0),\qquad Z>0.
\]
设
\(H=D_SVZ^{-1}V^*D_S\)。Woodbury 恒等式给出
\(R_{D,S}=H(I+H)^{-1}\)，并且
\[
V(I-B_0)^{-1}V^*=A(I-A)^{-1}.
\]
由 \(A\) 的谱界，
\[
\frac{\ell_S}{u_T}\frac{\alpha}{1-\alpha}I
\preceq H
\preceq
\frac{u_S}{\ell_T}\frac{1-\alpha}{\alpha}I.
\]
对正矩阵应用 \(x\mapsto x/(1+x)\)，即得 (6.3)。∎

### 6.3 中性外部观察后，输入两位不能接近一个纯二点反约束

取 \(S=\{i,j\}\)，只观察外部输出。此时 \(S\) 上
\(\ell_S=u_S=1\)，外部 \(\ell_T=1/\omega,\ u_T=\omega\)。由 (6.1)、(6.3)，真实外部后验的二点压缩 \(\widehat R_S\) 满足
\[
\delta I\preceq\widehat R_S\preceq(1-\delta)I,\qquad
\delta=\frac1{1+6\omega}=\frac1{235}.
\tag{6.4}
\]
设其特征值为 \(\lambda_1,\lambda_2\)。实际输入等号事件概率为
\[
h=\det\widehat R_S+\det(I-\widehat R_S)
=\lambda_1\lambda_2+(1-\lambda_1)(1-\lambda_2).
\]
这个双仿射式在 \([\delta,1-\delta]^2\) 的最小值位于相反角点，所以
\[
h\ge2\delta(1-\delta)=\frac{468}{55225}.
\]
因此每个实际外部表都有
\[
s=A_{00}+A_{11}\ge
s_*+c^2\frac{468}{55225}
=\frac{2491671}{44180000}>\frac1{18}.
\tag{6.5}
\]
这一余量对所有外部输出和所有偶数 \(n\ge4\) 同时成立。

### 6.4 对这个较小的实际表类，系数可以降到 \(7/4\)

**引理 6.2。** 若 \(t\ge0,\ s\ge1/18\)，则
\[
t\le\frac74G(s,t).
\tag{6.6}
\]

**证明。** \(G\) 对 \(s\) 单调不减，只需检查 \(s=1/18\)。定义
\[
F(t)=\frac7{72}e^t-\frac{119}{72}e^{-t}+\frac{14}{9}-t.
\]
其导数零点对应
\(z_\pm=(36\pm\sqrt{463})/7>1\)，全局最小值只需检查零点与
\(\log z_+\)。在后者，
\[
F(\log z_+)=\frac{14}{9}+\frac{\sqrt{463}}{36}-\log z_+.
\]
因为 \(21<\sqrt{463}<22\)，\(z_+<58/7\)，且
\[
e^{17/8}>\sum_{k=0}^6\frac{(17/8)^k}{k!}
=\frac{314095517}{37748736}>\frac{58}{7},
\]
故临界值严格大于
\(14/9+21/36-17/8=1/72\)。结合 \(F(0)=0\) 得证。∎

由 (6.5)，所有主模型的实际表都满足
\(\Lambda\le(7/4)\Gamma\)。因此
\[
\mathcal R_2\ge2(2-7/4)\sum_{i<j}\mathbb E\Gamma_{ij}
=\frac14M.
\tag{6.7}
\]
这里没有声称 \(\Lambda\le\Gamma\)，也没有排除任务所给的真实六点 sine 正 excess。

## 7. P3 的汇总、系数与维数尺度

结合 (3.6) 与 (6.7)，得到
\[
\boxed{\mathcal R_2\ge
\frac15M+\max\{\mathcal T,M/20\}=L_{\rm SA01}.}
\tag{7.1}
\]
由任务的精确式 (2)，
\[
\boxed{\displaystyle
I''\le
\min\left\{
\frac95\Psi-\frac45\mathcal E-\mathcal T,\
\frac74\Psi-\frac34\mathcal E
\right\}.}
\tag{7.2}
\]
主模型中 \(\mathcal E=0\)，但几何对象并不因此消失。

### 7.1 结构性支付本身也有线性维数下界

对于完整后验，把引理 6.1 中四个场界取为
\(\ell_S=\ell_T=1/\omega,\ u_S=u_T=\omega\)，得
\[
\delta_f I\preceq R_S^y\preceq(1-\delta_f)I,\qquad
\delta_f=\frac1{1+6\omega^2}=\frac1{9127}.
\tag{7.3}
\]
故
\[
v_i-w_{ij}=(R_S^y-(R_S^y)^2)_{ii}
\ge\alpha_f:=\delta_f(1-\delta_f).
\]
投影性给出 \(m_i=v_i\)，从而
\[
\mathfrak W(R^y)=\sum_i\sum_{j\ne i}w_{ij}(v_i-w_{ij})
\ge\alpha_f\sum_i v_i.
\tag{7.4}
\]

对单点使用引理 6.1 的 \(\alpha=1/2\)，得到
\[
\frac1{1+\omega^2}\le r_i\le\frac{\omega^2}{1+\omega^2},
\quad
v_i\ge v_{\min}:=\frac{\omega^2}{(1+\omega^2)^2}.
\tag{7.5}
\]
因此
\[
\boxed{\displaystyle
\mathcal T\ge B\,\mathbb E\mathfrak W(R^Y)
\ge B\alpha_fv_{\min}n
=\frac{778512384}{48242012248609}\,n>0.}
\tag{7.6}
\]
约为 \(1.61376\times10^{-5}n\)。这是一个很保守的**结构性**线性支付；不能把它描述成足以证明熵凹性的大常数。它来自所有后验的谱限制，不是概率指数小的特殊输出事件。

### 7.2 总余量证书的一个较大但仍保守的线性尺度

由 (7.5)，
\[
\Psi\ge ne^2v_{\min}=n(760/761)^2.
\]
所以 (6.7) 给出
\[
\boxed{\displaystyle
\mathcal R_2\ge L_{\rm SA01}\ge
\frac{144400}{579121}\,n.}
\tag{7.7}
\]
这里约 \(0.249343n\) 是**总证书**的尺度；不能把它全部算成 (7.6) 的重叠边支付。标量校准和原始 Fourier 谱间隙均参与了 (7.7)。

### 7.3 原始几何的一个手算量

主模型有精确值
\[
\mathfrak J(Q_n)=\mathfrak W(Q_n)=\frac{n^2-4}{24n}.
\tag{7.8}
\]
证明可不用三角和公式：令 \(n=2m\)，
\[
\sum_{d=0}^{n-1}|Q_{0d}|^4
=\frac1{n^3}\#\{r_1+r_2=r_3+r_4:\ 0\le r_\ell<m\}
=\frac1{12}+\frac1{6n^2}.
\]
这里求和最大差小于 \(n\)，模 \(n\) 等号就是普通等号；三角形和频数的平方和为
\(m^2+2\sum_{k=1}^{m-1}k^2=(2m^3+m)/3\)。
去掉对角项 \(1/16\)，再用 \(m_i=1/4\)，即得 (7.8)。
这也直观显示原始输入远非二点块直和。不能只用该原始值替换
\(\mathbb E\mathfrak W(R^Y)\)；后验平均仍必须保留。

## 8. DISPROVED：第一版线性桥的合法精确反例

失败版本为
\[
2\Gamma-\Lambda\stackrel{\rm false}{\ge}
\frac{2c^2}{s_{\max}}h\Gamma.
\tag{8.1}
\]
取真实 \(P_{4,2}\)，用零起点坐标的 pair \((0,1)\)，条件为
\(Y_2=Y_3=0\)。实际表（依次为 \(00,10,01,11\)）为
\[
(A_{00},A_{10},A_{01},A_{11})
=\frac1{351200}(1521,29679,29679,290321).
\tag{8.2}
\]
外部事件概率为 \(439/3200>0\)。四个相应完整输出原子为
\((1521,29679,29679,290321)/2560000\)；除以这个外部概率便得到 (8.2)。合法性直接来自
\(U_{jr}=2^{-1}e^{2\pi{\rm i}jr/4},\ r=0,1\)：
六个二粒子输入原子中，相邻粒子对概率 \(1/8\)，相对粒子对概率 \(1/4\)，总和为一。使用指定信道即产生 (8.2)，不是另选一个二维 DPP 来充当目标模型。

精确值为
\[
h=\frac{761}{878},\quad
\Gamma=\frac{88349984800}{96990149359},\quad
z=e^\Lambda=\frac{579121}{290321}.
\]
(8.1) 的右边为
\(63788689025600/42578675568601\)，而
\[
2\Gamma-\text{右边}
=\frac{13782597628800}{42578675568601}.
\]
对 \(z\ge1\)，
\[
\log z\ge\frac{2(z-1)}{z+1}
\]
可由求导或 \(\operatorname{arctanh}\) 的正项展开证明。代入得失败式的余差满足
\[
2\Gamma-\Lambda-\text{右边}
\le-\frac{6305136880422404000}{18509844421857795321}
<-\frac13.
\tag{8.3}
\]
因此反例符号不依赖浮点对数。

失效机制很具体：(3.2) 中
\[
\partial_sG(s,t)=e^t+e^{-t}-2,
\]
当 \(t\to0\) 它是二阶小量，不能用一阶量 \(e^t-e^{-t}\) 代替。
修复后的 (3.4) 保留正确的平方行列式项；线性项则由两个端点之间的仿射插值单独证明，系数也完全改变。本文没有把 (8.1) 的失败扩大解释为所有线性后验支付均不成立。

## 9. 一个最小实例：精确四点检查，不承担渐近证明

`verify_n4.py` 仅枚举真实 \(P_{4,2}\) 的六个输入与十六个输出，使用 Python 标准库 `Fraction`。所有断言均为有理恒等式或有理不等式。脚本检查实际归一化、投影协方差行和、(5.1)–(5.2)、Bayes 概率界、重基恒等式、谱界的二阶主子式，以及 (8.3)。连续参数标量引理的证明在正文，脚本只复核其有限有理辅助运算。

本实例得到
\[
\Psi=\frac{837568518400}{8616436959},\qquad \mathcal E=0,
\]
\[
\mathcal T=
\frac{29416022942438399308}{634555434772830493},
\qquad
L_{\rm SA01}=
\frac{125257588507503052004}{1903666304318491479}.
\]
相应十进制约为 \(97.2059010,\ 46.3569002,\ 65.7980804\)。这些小数只是展示有理数，不用于符号认证。由已证 (7.2) 和这些有理数，
\[
H_4''\le
-\frac{67558913439941061604}{1903666304318491479}<-35.
\tag{9.1}
\]
这是**新工具在一个有限实例的可复核应用**，不是把四点熵的负号本身包装成新全局结果，也没有把本例的常数外推为每位点支付。

为了区分几何作用与边际失衡作用，(5.9) 的精确有理分配还给出
\[
\mathcal T_{\rm ov}>32,\qquad
(9/5)\Psi-\mathcal D<11.
\]
所以即使丢掉 (5.9) 的对角失衡平方项，**只用纯重叠支付**，仍有
\[
H_4''\le(9/5)\Psi-\mathcal T_{\rm ov}-\mathcal D<-21.
\tag{9.1a}
\]
其精确上界约为 \(-21.8020431\)；分数保存在 `n4_results.json`，符号断言用有理运算证明。这是同一个四点实例的预算分解，没有扩大配置计算规模。

更小的手算证书只保留 \(Y\equiv0,\,Y\equiv1\)。两者概率均为
\(\tau^2=1521/2560000\)，后验核都等于 \(Q_4\)，且
\(\mathfrak W(Q_4)=1/8\)。所以仅这两个输出就有
\[
B\,\mathbb E\mathfrak W(R^Y)\ge\frac{1083}{32500}>0.
\tag{9.2}
\]
这清楚地区别了零 tangent 与正几何缺陷。但这种特殊事件证明不能承担增长维数尺度；线性尺度使用的是 (7.3)–(7.6)。

`n4_results.json` 中把含浮点对数的实际 \(\mathcal R_2\)、实际 \(H_4''\) 另放在
`diagnostic_float_NOT_USED_FOR_PROOF` 字段；不以这些值作认证证据。

## 10. INCOMPLETE：实际解决了哪个瓶颈，仍欠什么

工具解决的是一个具体瓶颈：仅保留共同位移 tangent 会在投影中点失去全部信息，而 (1.3) 与 (1.5) 仍能捕获共享顶点反约束的冲突。相容性对象有确定零集、明确局部聚合预算、可证明的稳定性解释，并能以给定系数进入任务式 (2)。这不是“存在某个非负补偿项”的陈述。

尚未闭合的是支付的**大小**。例如仅将 \(\Psi\le\mathcal D-4n\) 代入
\(7/4\) 分支，仍只得到
\[
H''\le \frac34\mathcal D-7n=\frac{309}{13}n>0.
\tag{10.1}
\]
这是上界仍偏大的说明，绝不是实际 \(H''\) 为正的断言。

对主模型，若要靠结构分支完成熵凹性，一个明确的充分后续命题是
\[
\boxed{\displaystyle
\mathcal T(Q_n)\ge\frac95\Psi(Q_n)-\mathcal D(Q_n)
\quad\text{对所有偶数 }n\ge4.}
\tag{10.2}
\]
或者让另一分支满足 \(\Psi\le4\mathcal D/7\)。两者的精确组合条件是
\[
\min\{(9/5)\Psi-\mathcal T,\ (7/4)\Psi\}\le\mathcal D.
\]
这些尚未证明；(7.6) 的保守线性常数不能填补这个缺口。也未证明离散循环族到真实熵率的所需极限步骤，更没有交换极限与二阶求导。

固定 \(c=19/20\) 的非中点结构推广在下一节给出，但 \(7/4\) 的加强不自动带过去。其他对比度的具体常数仍需重新校准。任务附带的六点正 excess、二维逐 pair 反例和已有两位熵结论均未被改写或“排除”。

## 11. 已证推广与明确的模型边界

### 11.1 有限 Toeplitz 推广：靠扩张证明，不靠等同

对任意 Hermitian 收缩 \(K\)，矩阵
\[
P=\begin{pmatrix}
K&\sqrt{K(I-K)}\\
\sqrt{K(I-K)}&I-K
\end{pmatrix}
\tag{11.1}
\]
是正交投影。这可直接平方验证，因为所有块都是 \(K\) 的函数。
\({\rm DPP}(P)\) 在前 \(n\) 坐标的边际恰好是 \({\rm DPP}(K)\)，由包含概率的主子式定义即可验证。

只在前 \(n\) 坐标施加实际观察的似然，辅助坐标的场取一。倾斜后投影在前 \(n\) 坐标的压缩，正是原模型的真实后验。扩张只是证明手段，没有给用户的模型增添观测或改动输入律。

因此第 6 节的压缩谱证明同样适用于任何满足
\[
K_{ii}=1/2,\qquad (1/7)I\preceq K_{\{i,j\}}\preceq(6/7)I
\]
的收缩。真正的半密度 sine Toeplitz 压缩
\[
(K_n)_{ii}=1/2,\qquad
(K_n)_{ij}=\frac{\sin(\pi(i-j)/2)}{\pi(i-j)}
\]
满足该条件，因为 \(|K_{ij}|\le1/\pi<5/14\)。所以对每个有限 \(n\ge2\)，(7.1)–(7.2) 也成立，且 \(\mathcal T\ge B\mathbb E\mathfrak J\ge B\mathbb E\mathfrak W\)。

**这里不能令 \(\mathcal E=0\)。** \(K_n\) 不是真正有限投影，
(5.2) 中还保留 \(\sum_i\eta_im_i\)。循环投影的 (7.6)–(7.7) 不能未经额外论证逐字移给这个有限 Toeplitz 模型。

不过命题 5.3 确实给出一条独立的、较弱的 Toeplitz 线性结构支付。对每个内部中心 \(i=1,\ldots,n-2\)，两条最近邻边的权均为 \(1/\pi^2\)。故当 \(n\ge3\)，
\[
\mathfrak W(K_n)\ge\frac{2(n-2)}{\pi^4},\qquad
\boxed{\mathcal T(K_n)\ge\frac{2B\,\omega^{-10}}{\pi^4}(n-2).}
\tag{11.1a}
\]
这保留真实非投影后验及非零 \(\mathcal E\)，常数很小。上述有限不等式都不是熵率凹性证明。

### 11.2 固定 \(c=19/20\) 的所有内部 offset：结构工具的推广

以下仍用真实循环投影；令 \(0<a<1-c\)，并且全部导数仍固定 \(c,Q\)。
写
\[
\epsilon=a-\frac{1-c}{2},\quad
\rho_a=1-\frac{2|\epsilon|}{c}\ge\frac{18}{19},
\]
\[
\ell_1=\frac{a+c}{a},\quad
\ell_0=\frac{1-a-c}{1-a},\quad
\Omega_a=\max\{\ell_1,\ell_0^{-1}\}\ge39,\quad
K_a=\ell_1/\ell_0.
\tag{11.2}
\]
令 \(e_{\min}=\min(e_0,e_1)\)，其中 \(e_b=c/\tau_b\) 沿用任务定义。

对实际外部输入表，记 \(h=\Pr(X_i=X_j\mid Y_{-ij})\)，
\(m=\Pr(11\mid Y_{-ij})-\Pr(00\mid Y_{-ij})\)。直接展开信道给出
\[
s=A_{00}+A_{11}
=s_*+2\epsilon^2+c^2h+2c\epsilon m
\ge s_*+c^2\rho_a h.
\tag{11.3}
\]
定义
\[
u=(s-s_*)/c^2\ge0
\]
并将 \(\chi(u)=\min\{4/5,72u/(25+40u)\}\) 定义在整个非负半轴。
非中点时 \(u\) 不再被冒充为输入等号概率。使用
\[
\mathcal T_a=
2\sum_{i<j}\mathbb E
\max\{\chi(u)\Gamma,\ \gamma(s-s_*)\Delta\}.
\tag{11.4}
\]
引理 3.2 的同一仿射插值证明给出
\[
\boxed{\displaystyle
\mathcal R_2\ge\frac15(\Psi-\mathcal E)+\mathcal T_a,\quad
I''\le\frac95\Psi-\frac45\mathcal E-\mathcal T_a.}
\tag{11.5}
\]
此处 \(\mathcal E\) 一般非零，不能丢掉或设零。

相应的 Bayes 界是
\(h_y\le\Omega_a h/[1+(\Omega_a-1)h]\)。由于
\(\Omega_a\ge39\)、\(18/19\le\rho_a\le1\)，和第 4 节相同的分段分母比较证明
\[
\chi(u)\ge\chi(\rho_a h)
\ge\frac{2\gamma(\gamma-1)\rho_a}{\Omega_a}h_y.
\]
结合一般的精确重基
\(\Gamma=\mathbb E[e_{Y_i}e_{Y_j}|R_{ij}^Y|^2\mid Y_{-ij}]\)，得到
\[
\mathcal T_a\ge B_a\,\mathbb E\mathfrak J(R^Y)
\ge B_a\,\mathbb E\mathfrak W(R^Y),\qquad
B_a=\frac{4\gamma(\gamma-1)\rho_a e_{\min}^2}{\Omega_a}.
\tag{11.6}
\]
若需显式维数尺度，完整场的最大最小比为 \(K_a\)。引理 6.1 给出
\[
\delta_a=\frac1{1+6K_a},\quad
v_a=\frac{K_a}{(1+K_a)^2},\qquad
\boxed{\mathcal T_a\ge B_a\delta_a(1-\delta_a)v_a\,n>0.}
\tag{11.7}
\]
每个固定内部 \(a\) 的常数为正；接近信道端点时这个下界退化。本文不把 \(7/4\) 系数扩张为整个 offset 区间上的结论，也不声称 \(\mathcal T_a\) 的零集仍与中点 \(\mathcal T\) 相同：非中点还含 \(2\epsilon^2\) 的标量增益。

## 12. 来源、复核界面与贡献边界

[任务] `randomcat4/dpp-stationary-entropy`，PR #118，分支
`research/sine-entropy-tool-3-round-prompts`，
`research_prompts/pro_tasks/TASK_01_POSTERIOR_SLACK.md`。
提供真实模型、任务式 (1)/(2)、兼容重基、已审核 \(\kappa=2\) 输入和判伪起点。

[旧证] 同分支的
`research_prompts/pro_tasks/sources/S4_PROOF.md`，第 4–7 节；
`research_prompts/pro_tasks/sources/S4_AUDIT.md`。
旧证的完整信息支付、缺失信息恒等式和标量四原子代数按其已审核作用域使用。本文不重算历史六点证书，不继承旧材料中任何未审核的更强作者主张。

[GW95] Michel X. Goemans and David P. Williamson,
*Improved approximation algorithms for maximum cut and satisfiability problems using semidefinite programming*,
Journal of the ACM **42**(6), 1115–1145 (1995)，第 2 节，式 (Q)。
作者主页原文：<https://math.mit.edu/~goemans/PAPERS/maxcut-jacm.pdf>。
只借用加权反约束的编码与“未满足代价”视角，不借用其算法结论充当本文证明。

本交付自行推导的是有理条件表包络、端点稳定性支付、共同后验 Bayes 系数、重叠边刚性分解、距二点块集合的定量估计、正坐标场的维数无关稳定性，以及实际 Fourier 场约束产生的 \(7/4\) 加强和上述作用域推广。对于文献优先性，仅说明这些是本次组合与推导，不作首次发明声明。
