> **待独立对抗性审查 / PENDING_INDEPENDENT_REVIEW。** 下文保留来源原文；其中 PROVED、PASS、AUDIT 等是作者或既有记录的表述，不代表本次 SA 成果已独立通过。先读本包根目录 REVIEW_REQUEST.md；外部审计与其他 SA 分开进行。

# SA01｜真实后验余量工具交付

任务来源：`randomcat4/dpp-stationary-entropy`，PR #118，分支
`research/sine-entropy-tool-3-round-prompts` 的
`research_prompts/pro_tasks/TASK_01_POSTERIOR_SLACK.md`。

## 结果状态

**PROVED：** 已给出完整推导的真实后验有理条件表证书 \(\mathcal T\)，以及同一个完整后验上的相容性泛函 \(\mathfrak J\)、重叠边泛函 \(\mathfrak W\)。主模型为真实偶数维连续频率循环半密度投影，\(c=19/20,\ a=1/40\)。

核心不等式为
\[
\mathcal R_2\ge\tfrac15(\Psi-\mathcal E)+\mathcal T,\qquad
\mathcal T\ge\tfrac{1478656}{6591}\mathbb E\mathfrak J(R^Y)
\ge\tfrac{1478656}{6591}\mathbb E\mathfrak W(R^Y).
\]
由实际 Fourier 二点谱间隙，还有
\[
I''\le
\min\{\tfrac95\Psi-\tfrac45\mathcal E-\mathcal T,\
      \tfrac74\Psi-\tfrac34\mathcal E\}.
\]
投影中点 \(\mathcal E=0\)，新几何量仍严格为正。正文识别了其二点块零集，证明了距零集的定量稳定性和正坐标场下的维数无关稳定性。

**DISPROVED：** 第一版局部线性桥被真实四点循环模型反驳；正文保留完整合法表和有理误差界，没有删除失败版本。

**INCOMPLETE：** 没有证明全维熵凹性或熵率凹性。真正尚缺的是结构支付是否达到正文 (10.2) 的阈值，而不是证书非负性。有限 Toeplitz 与非中点推广分别论证，未与投影中点混同。

## 文件

| 文件 | 内容 |
|---|---|
| [MODEL_AND_NOTATION.md](MODEL_AND_NOTATION.md) | 完整模型、一般 offset 的权重及任务已审核恒等式 |
| [REPORT.md](REPORT.md) | 对象定义、域外迁移、P1–P3、完整证明、零集、合法反例、适用域与精确缺口 |
| [verify_n4.py](verify_n4.py) | 仅六个输入、十六个输出的真实四点有理检查；标准库实现 |
| [n4_results.json](n4_results.json) | 已运行检查得到的精确分数；非认证浮点对数另设字段 |
| [HANDOFF.md](HANDOFF.md) | 后续独立审阅与必要计算的精确公式、输入域和符号标准 |

`MODEL_AND_NOTATION.md` 与正文内含所需模型和已审核恒等式；包可以离线阅读。参考文献仅用于来源定位，不是重新执行所必需的网络依赖。

## 复现

Python 3.10 或以上，无第三方依赖：

```bash
python verify_n4.py
python verify_n4.py --output reproduced_n4_results.json
```

所有程序断言均使用 `Fraction`，即使启用 `python -O` 也不会跳过检查。程序只对本次工具作四点小算；它不执行增长维数枚举、密集扫描、拟合、哈希检查或旧六点证书重算。

本次四点应用的精确结果包括
\[
\mathcal T=
\frac{29416022942438399308}{634555434772830493},\quad
H_4''\le
-\frac{67558913439941061604}{1903666304318491479}<-35.
\]
保留自适应权重后，仅重叠边部分的支付就严格超过 32，独立给出 \(H_4''<-21\) 的有限上界。完整证书再加入其精确分配的对角失衡项，得到上面的 \(<-35\)。

这个有限负号用来展示新工具，不作为全维结论，也不宣称四点熵负号本身是新发现。

`PROVED` 是正文证明已经闭合的作者状态；没有声称外部独立同行复核已经完成。
