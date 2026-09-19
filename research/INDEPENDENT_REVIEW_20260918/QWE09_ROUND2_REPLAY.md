# QWE09 Round 2 独立重放记录

## 冻结来源

```text
repository  randomcat4/dpp-stationary-entropy
PR          131
head        bb9a95edc49a34f45775c011cb35f33b5c0f4d23
round-1     d67db7fdaf8a15b492807745d10ac3b75706690a
new files   results/ROUND2_FINDINGS.md
            results/QWE09_RESULT.md (14-line summary addition)
```

第二轮没有保留原临时脚本。本次重放从定义重新实现，不恢复或猜测作者随机种子。

## 环境

```text
Python 3.12.14
NumPy 2.3.5
Windows x64
```

## 命令

在 RL01 审查 worktree 根目录运行：

```text
python research/INDEPENDENT_REVIEW_20260918/QWE09_ROUND2_REPRO.py
```

退出状态为 `0`。

## 关键输出

### 真实 Toeplitz word 扫描

```text
a=0.025
n=11  minimum= 0.2737787380254857    negative_count=0
n=12  minimum=-6.385418176574598     negative_count=14
n=13  minimum=-18.90527988714043     negative_count=22
n=14  minimum=-25.057769153301273    negative_count=76

a=0.02
n=11  minimum= 0.016903614496854985  negative_count=0
n=12  minimum=-7.263088505954002     negative_count=14

a=0.03
n=11  minimum= 0.016903614496730363  negative_count=0
n=12  minimum=-7.263088505953928     negative_count=14
```

`a=0.025,n=12` 的分类间隔：

```text
largest negative     -1.2164387819398115
smallest nonnegative  1.3282966798295912
```

### 新的显式 pair 见证

```text
theta 0.0733179141207703
U [[0.9973134455261873, -0.07325224483034391],
   [0.07325224483034391, 0.9973134455261873]]

pair mixed curvatures
[[-13.17828732572662,    0.15782100000000002],
 [  0.1578209999999999, -13.178287325726632]]

aggregate mixed curvature -26.04093265145325
common curvature          -136.12667305555223
probability sum              1.0000000000000002
```

### 全新 320 模型探针

```text
common curvature range          [-198.15786767231728, -16.0]
aggregate mixed range          [-37.63094629356886, -0.0]
nonnegative common count        0
positive aggregate count        0
models with positive pair       121
maximum individual pair         0.3408482586994143
maximum probability residual    8.881784197001252e-16
```

## 证据等级

- 四点 `U` 见证是一个新的显式合法投影，足以否定普遍的逐 pair 非正命题；不需要原随机样本。
- `n=12` 的 14 个负 word 与零有超过 1.2 的间隔，足以复现作者明示为探索性的有限数值断点。
- 320 模型结果只重现诊断现象，不是全体 contraction 的区间证书或符号定理。
- 第一轮六点零支付 Jensen 反例已有单独的外向区间与独立 Decimal 审查，本轮没有把它降级为普通浮点证据。
