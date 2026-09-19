# S75 Cycle26 运行记录

日期：2026-09-20（Asia/Singapore）

## 静态安全检查

- `s75_certificate.py`：仅使用标准库整数区间运算，主程序写同目录
  `S75_CERTIFICATES.json`；无网络、无子进程、无仓库操作。
- `s75_diagnostics.py`：使用 NumPy 做有限枚举，主程序写同目录
  `S75_DIAGNOSTICS.json`；无网络、无子进程、无仓库操作。
- 为避免改写作者目录，严格 certificate 通过模块导入并直接调用
  `main()`，不执行其 `if __name__ == '__main__'` 写文件分支。

## 作者严格 certificate 重跑

运行环境：Python 3.12.14。

结果：

```text
PASS_EXACT_RATIONAL_INTERVAL_CERTIFICATES
returned object matches supplied S75_CERTIFICATES.json exactly: true
unconditional sparse-pair drift:
  [-0.000177079144736247071677,
   -0.000177079144736247071676]
conditional old-background star drift:
  [-0.000000743263519109895773,
   -0.000000743263519109895772]
unconditional star drift:
  [0.000013875271794819793250,
   0.000013875271794819793251]
infinite midpoint star lower bound:
  [0.262755862074718609606873,
   0.262755862074718609606874]
```

## 独立重放

命令：

```powershell
python -B research/INDEPENDENT_REVIEW_20260918/S75_CYCLE26/s75_cycle26_replay.py `
  --source-dir C:/game/gameproject/showa100/math/sa-dispatch-20260918/harvest/CYCLE26/S75/original/S75 `
  --output research/INDEPENDENT_REVIEW_20260918/S75_CYCLE26/S75_CYCLE26_REPLAY.json
```

环境：Python 3.12.14，NumPy 2.3.5。

终端状态：

```text
PASS_INDEPENDENT_REPLAY_SUPPORTS_SCOPED_STAR_THEOREM
```

全部检查为 `true`：作者 certificate 与随附 JSON 一致；一般
`rho=.45` 稀疏 mask 负漂移；固定旧背景星形负漂移；全背景平均星形
正漂移；新的随机星形公式与显式下界；实际偏置矩和 Taylor 系数；
整个 support 收敛域；矩余尾；0.26275 下界；式 (22)--(23) 空间尾；
约 107974 的 rate 残余包络算术。

作者源目录没有被写入；全部新增文件均位于本审计目录。
