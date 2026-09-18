# 当前状态 — 2026-09-18

## 主目标

对实际正弦 Toeplitz 核

\[
K_n(a)=aI+cQ_{\rho,n},
\]

在每个固定 `0<rho<1`、`0<c<1` 和全部合法 `0<=a<=1-c` 上证明完整配置 Shannon 熵率凹性。

**状态：OPEN / NOT PROVED。** 下面所有通过项都是严格限定结论；修正循环律、半密度平衡点、有限观测或有限维证书都不能自动升级为这个主目标。

## 已独立认证的当前结论

| 对象 | 状态 | 已认证范围 | 明确排除 |
|---|---|---|---|
| [S43 cycle03](research/INDEPENDENT_REVIEW_20260918/S43_CYCLE03.md) | `VERIFIED_SCOPED` | 修正循环半密度律、`c=19/20`、偶数 `n`：`limsup W_n/n <= -2.689614884862...`，并且 `-W_n=Theta(n)` | 不给出 `W_n/n` 极限，不决定 `W_n+C_n`，不证明真实输出熵率凹性 |
| [S45 cycle03](research/INDEPENDENT_REVIEW_20260918/S45.md) | `VERIFIED_SCOPED` | 固定 `c` 的修正律中 `|W_n|=O(n)` | 不给符号或极限系数 |
| [S45 cycle04](research/INDEPENDENT_REVIEW_20260918/S45_CYCLE04.md) | `VERIFIED_SCOPED` | 固定 `c`、偶数 `n` 的 clock limsup 上包络；在 `c=.95` 的系数为 `499.631158492115...` | 不推出 `W_n+C_n` 的符号；该系数不是逐个有限 `n` 的界 |
| [S42 cycle03](research/INDEPENDENT_REVIEW_20260918/S42_CYCLE03.md) | `VERIFIED_SCOPED` + `DISPROVED` + `GAP` | dyadic 有限弦桥、准自由互信息主控、标量核、数方差和显式尾界通过；第一 doubling 弦严格为正 | 指定尺度只有 `O(eta^2)`，不是 `o(eta^2)`；剩余 11/12 个带符号尺度未支付 |
| [S41 cycle03](research/INDEPENDENT_REVIEW_20260918/S41_CYCLE03.md) | `VERIFIED_SCOPED` | 可见 §1–§7 的半填充平衡点有限观测证书 | 截断的 §8 未审；常数在 `c=.95` 附近不实用 |
| [S41 cycle04](research/INDEPENDENT_REVIEW_20260918/S41_CYCLE04.md) | 骨架通过，主引理 `GAP` | posterior projection、Schur 字典、边界能量、outside / anchor flow、随机 anchor 平均与条件装配 | complete-jet Lemma 5.1 没有完整展开和覆盖账本；Theorem A 仅条件成立 |
| [SA02 平衡线边界](research/INDEPENDENT_REVIEW_20260918/SA02_C37_BOUNDARY.md) | `VERIFIED_SCOPED` | `c=37/40` 平衡点及 `37/40<=c<=937/1000` 的平衡线区间；`c=.95` 有真实 sine 后验障碍 | 不覆盖同一 `c` 的全部合法 `a`；“唯一失效前沿”没有单调性证明 |

## 已证伪或仍缺的承重点

- [S42](research/INDEPENDENT_REVIEW_20260918/S42_CYCLE03.md)：`L_J` 取固定倍数的正文尺度不能推出小 `o(eta^2)`；M12 的十进制充分阈值舍入方向也需修正。
- [S47](research/INDEPENDENT_REVIEW_20260918/S47_CYCLE04.md)：原式 (4) 被 `P=Q` 这一最小反例否定；当前代数重写没有给出真正依赖弦结构的 true-sine tail。
- [S41](research/INDEPENDENT_REVIEW_20260918/S41_CYCLE04.md)：缺的不是更大常数，而是完整 connected expansion、逐项 prototype 覆盖表和 marked 导数账本。
- 修正律的 `W_n+C_n` 符号仍未决定；即使决定，也仍需支付到实际正弦输出熵率的桥。

## 其他已审工具

S13、S14、S16、S17 以及早期 S42/S43 的分项结论保存在[审查索引](research/INDEPENDENT_REVIEW_20260918/README.md)。其中旧的 `O(n^(3/2))` 或“符号未知”描述已被后续 S45 / S43 在相同冻结修正律范围内推进，但原文件仍作为研究历史保留。

## 尚未合入的分级证据

[Draft PR #5](https://github.com/cat5779/rl01/pull/5) 继续保留以下四类材料，尚未整体进入主线：

- SA05 `n=8` 的严格有限区间证书；
- SA03 的有限数值障碍，其中部分仍待区间化和独立复现；
- SA04 的待审作者证明；
- SA03 / SA04 的探索性 MCMC。

它们不能合并成一个“已证明”的状态。当前分支保留，待拆分验收。

## 当前研究

[Cycle 05](prompts/CYCLE05/README.md) 正在攻击 S41 complete-jet 缺口和 S43 的 `W+C` 联合支付；S44 的既有定位任务继续运行。任务已派出不等于产生或认证了新结论。
