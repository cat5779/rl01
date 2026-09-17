> **待独立对抗性审查 / PENDING_INDEPENDENT_REVIEW。** 下文保留来源原文；其中 PROVED、PASS、AUDIT 等是作者或既有记录的表述，不代表本次 SA 成果已独立通过。先读本包根目录 REVIEW_REQUEST.md；外部审计与其他 SA 分开进行。

# SA05｜真实律—修正律二阶熵比较交付

任务来源：`randomcat4/dpp-stationary-entropy`，PR #118，
`research/sine-entropy-tool-3-round-prompts` 分支，
`research_prompts/pro_tasks/TASK_05_TRUE_CORRECTED_BRIDGE.md`。

## 核心结论

**PROVED：** 构造 Jacobi–Duhamel 调制相对熵工具。它给出全部 Johnson 模式的精确参数方程、
已知修正律驱动的模式残差，以及包含移动计数的局部二阶熵下界。
在指定 \(c=19/20,a_*=1/40\) 上，
\[
E_n''(a_*)\ge
\mathcal L_n''(a_*)+\sum_l\pi_l''(a_*)D(q_l\Vert\widehat q_l)
-C_{\rm src},
\]
其中 \(C_{\rm src}=349998584954880000/2401\) 与 \(n\) 无关。
这个最坏常数很粗；更实用的图逆范数和一维重叠矩版本均在主文。
得到 \(O(1)\) 支付的是非线性相对熵的**层内**加速，不是完整 \(E_n''\)。
主文另证明真熵梯度上的残差配对为 \(O(\sqrt n)\)，但保留未支付的熵生产差与移动计数项。

**PROVED（跨层补充）：** 均匀删点把真实密度精确传成
\(\mathsf D_m f_{m+1}=f_m+\eta_m f_{m,\xi}\)。
修正律增加显式正热时间；跨层残差仍精确消去常数及度二。
补充给出相邻真层下采样的静态 \(\chi^2\le115520/n\)、
固定模式的 \(O(n^{-2})\) 源界，以及保留反向条件 KL、正平方和移动参考的
完整跨层 KL 账本。**没有对静态距离界形式微分，也没有因此得到跨层 KL 二阶符号。**

**DISPROVED：** 度二匹配推出全律相等、正随机单钟混合精确恢复，
以及全合法区间的两种相反固定符号曲率规则。
本题 \(n=4,6\) 实际完全匹配；首个确实激发的缺陷是 \(n=8,l=4,j=4\)。
解析证明 \(E_8''\) 在合法区间内同时取正值和负值，但未定位参数坐标。

**INCOMPLETE：** 中点全 \(n\) 符号及 \(E_n''\ge-o(n)\)。
尚欠显式高模式熵梯度项与静态跨层相对熵的计数响应。
有限维反例不反驳渐近 \(o(n)\)，也不反驳真实熵凹性。
不涉及循环到 Toeplitz/熵率传递。

## 文件

- [完整证明](SA05_PROOF.md)：对象合成、域外迁移、P1–P3、
  模式/非线性/移动权重全推导、中点及明确邻域引理、合法反例和精确缺口。
- [跨层传递补充](SA05_CROSS_LAYER.md)：真实下采样的参数响应、
  两步 jets、匹配热时间、跨层模式源及非线性 KL 账本。
- [计算交接](SA05_HANDOFF.md)：尚未执行的参数定位、完整配置核查和尺度诊断。
- [审计记录](SA05_AUDIT.md)：证明接口、正性、归一、量词和外部定理条件的复核。
- [主小算程序](checks/check_sa05.py) 与 [实际输出](checks/results.json)；
  [跨层小算程序](checks/check_cross_layer.py) 与 [实际输出](checks/cross_layer_results.json)。
- [工作记录](WORK_RECORD.md)：实际处理窗口、工具交付状态和验证范围。

## 小算复现

从本目录运行：

```bash
python checks/check_sa05.py --output checks/results.json
python checks/check_cross_layer.py --output checks/cross_layer_results.json
```

需要 Python 和 SymPy。主程序只在 \(n=4\) 使用全部 16 个输出原子；
\(n=8\) 只用单原子代数证据、低次多项式及五值重叠变量。
跨层程序只检查 \(k=4,m=2,3,4\) 的有理多项式恒等式，不枚举配置。
两套程序均已实际运行，输出为 `EXACT_PASS`。
已经检查真/修正原子归一、层归一、一二阶 jets、原子与层 Hessian 缺陷、
Jacobi/时钟方程、度二 score 消去、移动参考与图耗散恒等式，
以及跨层连续关系、移动系数导数和两步二阶 jets。

没有运行大配置枚举、密集扫描、旧六点证书重算或哈希检查。
跨层补充 §2 及 §4 的时钟/匹配插值取 \(2\le m<k\)；
\(m\le1\) 的均匀层不引入未定义时钟。
数学结论的状态与工具上传状态分开记录；证明文本不依赖 GitHub 在线可用。
