# S77 Cycle31 独立运行记录

## 审查范围

- 来源：`research/CYCLE31_20260920/S77/S77_VISIBLE_RESULT_PARTIAL.md`
- 来源大小：20150 字节、1304 行。
- 来源首行声明内容在 20000 字符处截断。
- 可完整审查 Sections 1–7；Section 8 只有可见开头。
- 状态标签：`SOURCE_PARTIAL_TAIL`。本审查不声称读取了缺失尾部。

## 作者诊断脚本

脚本 `S77_fisher_burg_diagnostic.py` 先作静态检查：只使用 NumPy 和
标准库，枚举有限 words，不包含网络、外部进程或文件写入。随后实际
运行作者脚本，中心参数表与 45 点扫描均可复现。

六点中心结果：

| 量 | 作者双精度输出 |
|---|---:|
| \(D_F\) | 32.590751960 |
| \(C_{\rm acc}\) | -18.840984490 |
| \(\mathcal I_{\rm rel}\) | 18.552546428 |
| \(\mathcal B_+\) | 6.188926633 |
| \(\mathcal I_{\rm rel}-\mathcal B_+\) | 12.363619795 |
| \(M''\) | 13.749767470 |

45 点扫描中最小的浮点 sufficient-condition value 为
1.3575784131196387，位置是 \(N=2,c=.925,a=.03\)。这些结果没有
directed rounding 或 outward interval，因此运行记录只把它们列为
浮点诊断，不称为严格认证。

## 独立重放

独立脚本：

`research/INDEPENDENT_REVIEW_20260918/S77_CYCLE31/s77_cycle31_replay.py`

输出：

`research/INDEPENDENT_REVIEW_20260918/S77_CYCLE31/S77_CYCLE31_REPLAY.json`

运行环境由 JSON 记录为 Python 3.12.14、NumPy 2.3.5。脚本把每个
atom 独立重建为标量 determinant polynomial
\(\det(aI+B_y)\)，没有复用作者的 cofactor 导数实现。它另行检查：

1. 两个承重标量积分；
2. Fisher–Burg、score covariance 与 acceleration 恒等式；
3. 六点作者输出的一致性；
4. mutual information 的五点有限差分曲率；
5. 45 点浮点扫描；
6. 两点弱耦合比值极限与 \(d^2\) 下界；
7. merge-tree cross-block charge 的 trace 恒等式。

重放总状态：

`PASS_FLOATING_REPLAY_SUPPORTS_VISIBLE_S77_CORE_NOT_A_CERTIFICATE`

所有九项检查均通过。独立实现与作者实现最大差
\(4.98\times10^{-14}\)；六点五点差分曲率为 13.7497671902，和解析
双精度值相差约 \(2.8\times10^{-7}\)。merge-tree trace 检查误差不超过
\(2.5\times10^{-16}\)。

## 证据边界

- 代数推导负责证明可见主体中的 exact identity 与两点级数结论。
- 数值重放只负责发现实现错误并支持诊断，不升级为区间证明。
- PR64 已严格区间认证六点的 \(D_F,C_{\rm acc},M''\) 符号；它没有
  认证 S77 新的 \(\mathcal I_{\rm rel}\) 或 \(\mathcal B_+\) 数值。
- 全参数区间、全部所需 merge 尺度上的 B+ 支付仍未完成。
