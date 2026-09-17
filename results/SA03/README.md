> **待独立对抗性审查 / PENDING_INDEPENDENT_REVIEW。** 下文保留来源原文；其中 PROVED、PASS、AUDIT 等是作者或既有记录的表述，不代表本次 SA 成果已独立通过。先读本包根目录 REVIEW_REQUEST.md；外部审计与其他 SA 分开进行。

# SA03 / S9：真实 word 的有限通量抵消

对应 PR #118 的 `TASK_03_S9_SUBLEADING_RESIDUE.md`。所有结果使用原题真实 Fejer Toeplitz DPP：c=19/20、rho=1/2、正奇数 R、u in [1/(R+1),1]，固定 X=(M-R)/sqrt(R)。不把物理 word 换成谱 Bernoulli 配置，不把 J_R 当作块熵率。

## 最终数学状态

**PROVED（附证明，尚未独立审查）：** 实际 word 上的有符号运输 T、固定差分 L、正出生减可逆 Poisson 反项，以及逐 word 身份

\[
L^*w=T^*w=w',\qquad(\partial_\delta+T)q=u,
\qquad(\partial_\delta+T)G_z=0.
\]

实际后验是漂移缺陷 Poisson 方程的显式解。非线性剩余是一次/二次翻位 Bregman 缺陷。固定测试 F 的完整曲率为

\[
\partial_\delta^2E[F\phi(q)]
 =E[F\mathcal G+2\mathcal H LF+\phi(q)L^2F].
\]

F=1 时两项边界运输逐 word 为零，中心带与补带在有限 R 精确抵消。

令 epsilon_c=(1-c)/2、N=R+1，

\[
\left|A_R''(0)-4(1-N^{-2})\right|
 \le{7c^4\over32\epsilon_c^{18}}(1-N^{-6}),\qquad A_R''(0)=O_c(1).
\]

另证 A_R''(0)->Gamma(c)，Gamma 由真实无限后验的绝对可求和局部核定义。有效截断误差在定量附录 Q4–Q5，保守速率为

\[
A_R''(0)=\Gamma(c)+O_c(e^{-\kappa_c^{3/2}(\log R)^{1/4}/16}),
\quad\kappa_c=\min\{1/2,-\log c\}.
\]

常数和起始范围极大，不宣称最优性、幂次展开或实用判号半径。

**后续已完成：** `SA03_UNIFORM_WEAK_NOISE.md` W2–W4 逐项证明复对称双翻位估计，付清结构补充原 S4 候选及主报告原先单列的小 u 余项一致性。真实奇数子格独立给精确首项平均：cu<=1/8 时

\[
|I_R''(u,0)-8u^2-384S_R^0c^4u^6|
 \le{16C_0c^6u^8\over1-16c^2u^2},
\quad S_R^0=\sum_i|\widehat p_R(i)|^4.
\]

C0 在该补充明确给出。此前文件中关于这个候选“未完成”的历史表述由上述证明更新。小参数指 cu，术语应为弱耦合/低有效对比度，不是物理噪声较小。完整 word 仍不独立。

**DISPROVED：** 将 T Bcal_phi 当成非负耗散的闭合规则。真实 R=1 模型中

\[
T\mathcal B_\phi=-{16u^2t^2\over1-4t^2}<0,\quad t=c^2u^2/\pi^2.
\]

同一 R=1 模型总曲率可证明为正，所以这不是总曲率或全局猜想的反例。

**INCOMPLETE：** Gamma(19/20) 的符号、成长 R 完整曲率的符号、尖锐 R 误差/首个非零更细项、J_R 到真实熵率的导数或固定弦桥接。绝对值界、有限 R 正性和小 cu 展开都不能支付这些缺口。

## 文件与阅读顺序

- `SA03_S9_SIGNED_TRANSPORT.md`：候选、域外迁移、P1–P3、有限抵消、维度无关估计、真实 R=1 正总和与负分量。
- `SA03_VOLUME_LIMIT.md`：真实无限后验、绝对可求和核、真实律变化与有限极限。
- `SA03_EFFECTIVE_REMAINDER.md`：尾包络、有限数据稳定性、实际 word 总变差及显式误差。
- `SA03_STRUCTURAL_REFINEMENT.md`：速率二次抵消、正预算与混合缺陷、逐 word 首项；`SA03_UNIFORM_WEAK_NOISE.md`：完成其原 S4 候选。
- 三个小检查脚本及结果 JSON；`COMPUTATION_HANDOFF.md` 是尚未执行的后续工作，`VERIFICATION_NOTES.md` 给最终范围与运行记录。

```bash
python small_check_r1.py
python check_resolvent_algebra.py
python check_r1_refinement.py
```

Python 3，SymPy 1.14.0。第一脚本仅真实 R=1 的 8 个联合原子/4 个外部 word；第二脚本仅两个相互作用外部位的通用矩阵单元；第三脚本复用第一脚本的相同四个 word，不扩大枚举。PASS 只证明所列有限代数断言，成长体积结论来自正文。

## 文献迁移边界

Braverman，*The prelimit generator comparison approach of Stein's method*，arXiv:2102.12027v4：迁移有限尺度 Poisson 中心化，而非队列模型 Stein 因子。Chafai，*Binomial-Poisson entropic inequalities and the M/M/∞ queue*，ESAIM P&S 10 (2006),317–339，arXiv:math/0510488v2：迁移精确离散链式缺陷，不迁移正耗散。

未主张首次发明，未完成全面新颖性检索。原 PR 的旧 S9 审核不覆盖本次新结果。
