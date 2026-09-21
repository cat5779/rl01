# S76 Cycle28 独立复现记录

复现日期：2026-09-20（Asia/Singapore）

## 1. 作者附件状态

两个导出附件未下载。本审查没有作者 NumPy 源码，未执行也未声称执行作者 checker。

## 2. 独立程序

执行：

```text
python -B research/INDEPENDENT_REVIEW_20260920/S76_CYCLE28_INDEPENDENT_CHECK.py
```

环境为 Python 3.12.14，仅使用标准库。退出码 0。实际标准输出见 `S76_CYCLE28_INDEPENDENT_CHECK.log`。

## 3. 覆盖范围

程序独立构造实际 consecutive-Fourier unitary 和 exterior channel，检查：

- channel 每行、每列和为 1；
- \(m=2,3,4,5\)、\(c=.95\) 的全部 midpoint atoms；
- \(C_X,C_D,G'',H_{out}''\)；
- edge Jeffreys energy 与 \(-C_D/(4mL)\) 的一致性；
- 使用真实 \(M_{i,y}^W\) 权重的 \(\overline V_W\)；
- \(\eta_J\ge\overline V_W\)；
- 四点 \(\Xi/\delta\) 阈值和 \(c=.95\) 反例。

## 4. 结果

正文 \(m=2,3,4,5\) 表格逐项复现。额外得到：

| \(m\) | \(\eta_J\) | \(\overline V_W\) | 差值 |
|---:|---:|---:|---:|
| 2 | 0.153627663 | 0.092746875 | 0.060880788 |
| 3 | 0.239699750 | 0.163607281 | 0.076092469 |
| 4 | 0.296296642 | 0.214215685 | 0.082080956 |
| 5 | 0.336648028 | 0.251647871 | 0.085000157 |

四点阈值重算为 `0.5967833208973083`；在 \(c=.95\) 时 \(\Xi/\delta\approx5.2516191941>1\)。

## 5. 证据边界

枚举验证有限尺寸实现和公式配平，不证明全 \(m\) theorem。全尺寸 \(C_D\) sign 与 posterior payment 由 review 中的解析推导支持；\(C_X\) 仍无一般上界。
