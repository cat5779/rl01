# PRO02 独立 PRO 任务

从 PROMPT.md 开始。inputs/ 含仅与 SA02 有关的完整旧交付和必要背景；SOL_REVIEW.md 是本题 Sol 限定范围审查。

本包可单独启动，不依赖其他两个新 PR。源文件中的历史待审标签保留；Sol 首审不会替代待进行的外部对抗审计，也不会认证本轮新结果。审查行号对应原始 DPP 文件，公开副本顶部增加了两行待审说明，定位时优先使用章节与式号。

RESULT.md 为建议交付名，无仓库写权限时直接交正文。不要求哈希、重型计算或合并 PR。

接管后的第二轮结果见 `ROUND2_RESULT.md`。其状态是范围内新引理已证、完整基准负曲率仍未闭合；`checks/` 中的脚本复现可见 S18 数值并压力检查新储备与 pair-cut 公式。

随后从本地下载目录恢复了 S18 完整正文与配套脚本，分别收入 `S18_RESULT.md` 和 `checks/S18_PRO02_checks.py`。范围内复现审计与严格加强见 `ROUND3_REPRODUCTION.md`、`ROUND3_S18_AUDIT_AND_REFINEMENT.md`：S18 四个承重点和原脚本均已核对，新充分条件同时使用尖锐 `c^2` 储备折扣、变分容量与 sine-specific 完整 pair-cut。大窗口 `W_(m,L)` 的认证负上界仍未得到，因此 PR 继续保持不请求合并的研究状态。

平衡线上的方法比较、闭合尺度和严格前沿见 `ROUND4_C37_TO_ONE_ADVANTAGE_BOUNDARY.md`，复核入口见 `ROUND4_VERIFICATION.md`。新增证书把原双预算沿平衡线延伸到 `c=937/1000`，并在 `c=15/16` 给出严格有理障碍；在 `c=19/20` 的实际十点 sine 后验上，Arb 进一步认证旧 pointwise pair 比较失败。新定位式相对 S18 将同口径窗口尺度缩小约 `12.59` 倍，但尚未在 `c=19/20` 给出不借用旧曲率的大窗口负界，故仍不请求合并。

S18 Round 2 可见回复的新有限体积结论由 `ROUND5_S18_ROUND2_INDEPENDENT_REBUILD.md` 独立重建，入口为 `checks/verify_s18_round2_finite.py`。它不依赖缺失附件，逐原子 Arb 复核 `n=6`、`n=12`、完整六坐标 Hessian、六点邻域及首次 `6 -> 12` 总相关修正；有限结论成立，但全尺度/熵率曲率仍未闭合。
