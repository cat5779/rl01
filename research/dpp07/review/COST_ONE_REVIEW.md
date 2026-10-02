# 对 repair01.md 的独立数学审计

**STATUS: CORRECT**

未发现关键缺口。候选稿的抽象引理成立，并且确实推出冻结题面中的相对稀疏修复结论 (RC)。承重步骤是标准的完整截面 cost 压缩公式；对 \(F_2\times F_2\) 的应用使用该群已有的 fixed price \(1\)，所以这是标准 cost 理论在指定输入接口上的推论，不是一般 Lyons–Gaboriau 问题的新突破。

## 1. 抽象引理

设 \(R\) 是标准非原子概率空间上的非周期可数 pmp 等价关系，\(C_\mu(R)=1\)，且 \(S\subseteq R\) 是非周期子关系。子关系 \(S\) 仍然是 pmp 的。

非周期可数 Borel 等价关系的 marker/完整截面定理给出：对每个 \(\delta>0\)，存在 \(S\)-完整 Borel 集 \(A\)，满足
\[
0<\mu(A)<\delta.
\]
这里的正性不是额外假设：若 \(\mu(A)=0\)，则其 \(S\)-饱和集作为可数个零测集的并仍为零测，不可能余零。因为 \(S\subseteq R\)，\(S\)-完整性立即推出 \(R\)-完整性。

对任意 pmp 可数等价关系及其完整截面，Gaboriau 的未归一化压缩公式是
\[
C_\mu(R)=C_{\mu|A}(R|A)+\mu(X\setminus A).
\]
因此
\[
C_{\mu|A}(R|A)=C_\mu(R)-1+\mu(A)=\mu(A). \tag{1}
\]
此版本不要求遍历性。也可直接核对：在每个 \(R\)-类内取一棵通向 \(A\) 的 Borel 根森林，其 cost 是 \(1-\mu(A)\)；把其余 graphing 边沿根映射投影到 \(A\)，得到 \(R|A\) 的 graphing。反向把根森林加回任意 \(R|A\) 的 graphing。两边取下确界即得公式。该论证不要求各遍历分量中的截面比例一致，也没有归一化 \(\mu|A\)。

取 \(0<\mu(A)<\eta/2\)，再由 (1) 选择 \(R|A\) 的 graphing \(\Phi\)，使
\[
C_\mu(\Phi)<\mu(A)+\eta/2<\eta.
\]
若 \(xRy\)，可分别在它们的 \(S\)-类中选到 \(a,b\in A\)。于是 \(aRb\)，所以 \(\Phi\) 在 \(A\) 内连接 \(a,b\)，而 \(S\) 连接 \(x\) 到 \(a\)、\(y\) 到 \(b\)。故
\[
S\vee R_\Phi=R
\]
模零成立。这里不需要 \(S\) 遍历、正规或具有任何交叠性质；只需其类几乎处处无限。

## 2. \(F_2\times F_2\) 上的应用

在 FUSF 与 fresh iid 的乘积空间
\[
X=\{0,1\}^{E(G)}\times[0,1]^\Gamma
\]
上，\(\Gamma=F(a,b)\times F(c,d)\) 的移位作用 pmp；连续 iid 坐标使作用本质自由。题面给定 \(\beta_1^{(2)}(\Gamma)=0\) 以及 FUSF=WUSF，而 WUSF 的每个分量几乎处处无限。因此 forest-component 子关系 \(S_F\) 是非周期 pmp 子关系。

该具体群的 fixed price \(1\) 可直接核对。对任意自由 pmp 作用，保留完整的 \(a\)-变换，cost 为 \(1\)。在任意小的 \(a\)-轨道完整截面上分别保留 \(c,d\) 的限制；由对易性恢复完整的 \(c,d\)-变换。再在任意小的 \(c\)-轨道完整截面上保留 \(b\) 的限制，由 \(b\) 与 \(c\) 对易恢复完整的 \(b\)-变换。于是有 cost 小于 \(1+\varepsilon\) 的全轨道 graphing；非周期关系的普遍下界给出 \(C(R)=1\)。所以 fixed price \(1\) 确实作用于当前的 \((F,U)\) 作用，而不只是另一个作用或群 cost 的下确界。

## 3. partial graphing 到全输入等变加边图

先取不变余零 Borel 集 \(X_0\)，使 \(\Gamma\) 作用自由、FUSF 分量无限，并且 \(S_F\vee R_\Phi=R\) 在其上逐点成立。把各坏集取可数 \(R\)-饱和即可统一成这样的集合。

写 \(\Phi=\{\phi_n:D_n\to E_n\}\)。由作用在 \(X_0\) 上自由，每个 \(D_n\) 可按唯一满足
\[
\phi_n(x)=g\cdot x
\]
的 \(g\in\Gamma\) 分成可数个 Borel 块。把每个 graphing 发生项在同一轨道内平移回 \(\Gamma\) 坐标并加入相应无向边。每条候选边的成员关系是可数个 Borel 条件的并，因此得到 Borel 且精确 \(\Gamma\)-等变的
\[
A_\eta:X_0\longrightarrow\{0,1\}^{\binom{\Gamma}{2}}.
\]

关系生成性给出连通性：\(S_F\)-步对应 \(F(x)\) 中的有限路径，\(\Phi\)-步对应一条新增边；故 \(F(x)\cup A_\eta(x)\) 连接全部 \(\Gamma\) 顶点。

预算也匹配。对单个 \(\phi_n\)，单位元作为 graphing 边定义域端点的概率是 \(\mu(D_n)\)，作为值域端点的概率是 \(\mu(E_n)=\mu(D_n)\)。按发生项计重，
\[
\frac12\,\mathbb E\deg_{A_{\eta,n}}(e)\le\mu(D_n).
\]
求和得
\[
\frac12\,\mathbb E\deg_{A_\eta}(e)
\le\sum_n\mu(D_n)=C_\mu(\Phi)<\eta. \tag{2}
\]
删去环、重复无向边以及已经属于 \(F\) 的边只会减小 (2) 的左端，也不改变 \(F\cup A_\eta\) 的连通性。

最后在不变 Borel 零测集 \(X\setminus X_0\) 上定义 \(A_\eta=\varnothing\)。由于该集合不变，空图扩张保持每个输入上的精确等变性；因此映射全定义且 Borel，而连通性和预算在题面规定的输入律下成立。有限期望也由 (2) 直接得到。

## 4. 范围裁决

- 对每个 \(\eta>0\) 单独选择 graphing 和映射；题面不要求关于 \(\eta\) 的一致选择。
- H77 不需要使用：森林已经作为指定输入给出；fresh iid 保证相对输入作用自由并可被 Borel graphing 读取。
- 输出可使用任意长边，不声称局部、finitary、有效算法、短边或 determinantal 结构。
- 结论不与历史上的 DPP、独立 sprinkling 或短边桥障碍冲突：这里允许依赖整个 \((F,U)\) 的任意 Borel graphing。
- 对一般有限 cost 的非周期 \(R\)，同一论证只给
  \[
  \rho_\mu(R:S)\le C_\mu(R)-1,
  \]
  不推出一般 Lyons–Gaboriau 上界。
- 该结论与指定数学输入 r06/g3/source.md 第 4 节的相对压缩式 (15)–(16) 相同；本次审计补足的是冻结题面要求的 \((F,U)\) 全输入 Borel 等变接口。它不应作为新的研究定理宣传。

## 主要来源

- D. Gaboriau, *Coût des relations d'équivalence et des groupes*, Invent. Math. 139 (2000), Proposition II.6（完整截面的未归一化 cost 公式）；同文关于含无限阶元的直积群 fixed price \(1\) 的结果。https://perso.ens-lyon.fr/gaboriau/Travaux-Publi/Cout/Cout.pdf
- I. Benjamini, R. Lyons, Y. Peres, O. Schramm, *Uniform Spanning Forests*, Ann. Probab. 29 (2001), 1–65（WUSF 的基本构造与 Cayley 图分量性质）。https://rdlyons.pages.iu.edu/pdf/usf.pdf
