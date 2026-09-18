# QWE05 研究交付包

## 结论状态

原始目标 `W_n^rel >= -o(n)`：**INCOMPLETE**。本文没有给出实际模型渐近反例。

报告 `QWE05_RESULT.md` 给出新的部分定理与自包含证明：支付指定删除链中的非线性插值项，使其在精确计数通量下的上侧贡献为 `O(sqrt(n) log n)`；同时给出全模式修正删除源的 Fisher 平方范数 `O(n^-2)`。结合已独立审查的单侧参数响应估计，剩余的一个足够目标是实际反向条件删除 KL 的加权和为 `o(n)`。

这些新证明是本次作者推导，**未经过独立逐项审查**。小体积完整模型的数值结果与较大体积的条件核结果有明确区分；浮点检查不作为渐近证明。

## 阅读顺序

先读 `QWE05_RESULT.md` 的第 0 节（最强结果）、第 3–6 节（工具与证明）、第 9 节（精确剩余义务）。第 8 节汇报反证尝试和数值检验，第 10 节标明来源与认证边界。

## 复现

需要 Python 3.10+、NumPy、SciPy。完整配置枚举随 n 指数增长；已经运行的上限为 n=18，不建议未经资源评估直接提高上限。

```bash
OPENBLAS_NUM_THREADS=1 python qwe05_verify.py --small-max 18 --radial-max 4096
OPENBLAS_NUM_THREADS=1 python qwe05_analytic_checks.py
```

脚本把 CSV、JSON 和测试结果写入自身所在目录。`run.log` 与 `analytic_run.log` 保存了本次实际运行输出。脚本不访问网络、不写入云盘或仓库。

## 数值结果的作用域

`full_model.csv` 与 `deletion_ledger.csv`：实际完整 Fourier-DPP 条件律及指定修正律，n=8,10,...,18。

`radial_checks.csv`：给定输入集合后的实际一维重叠核与指定热核，n 最大 4096。此表不是完整输出相对熵。

`analytic_source_checks.csv`、`anchor_checks.csv`、`interpolation_checks.csv`：新引理的条件核压力测试，分别有 270、30、24 个测试点。

## 仓库与源资料

任务来自 `randomcat4/dpp-stationary-entropy` 的 PR #126，QWE05_PACKET.md。未修改任务源文件，未将 PR 标记为已解决，未执行其它 QWE 任务。
