# 原件、独审与证据索引 — 2026-09-20 / Cycle34

PR号默认属于cat5779/rl01；源DPP仓库会另写全名。research/CYCLExx路径相对PR54的research/sa-cycle19-harvest-20260919分支，不保证都在main。先读独审的作用域，再使用作者正文。

## 本轮与最新成果

| 结果 | 原件／档案 | 独审快照与裁决 |
|---|---|---|
| S80 | research/CYCLE34_20260920/S80/S80_RESULT.md | PR71；research/CYCLE34_20260920/reviews/PR71/；值级telescope与逐word工具正确，局部判号缺口仍在 |
| 反例地图证据 | research/CYCLE34_20260920/COUNTEREXAMPLE_AUDIT.md | 原SolB逐项整理，冻结参数和作用域；不包含独立S80审查 |
| QWE08 | research/CYCLE33_20260920/QWE08/；原仓库randomcat4/dpp-stationary-entropy PR130 | PR70；research/CYCLE33_20260920/reviews/PR70/；秩一和固定n<=4连续区间通过，全尺寸未解 |
| S78完整包 | research/CYCLE33_20260920/S78/S78_bundle.zip | PR68；research/CYCLE33_20260920/reviews/PR68_FINAL/；作者4证书复跑通过；R^-4固定pair修正必读 |
| S77 | research/CYCLE31_20260920/S77/S77_VISIBLE_RESULT_PARTIAL.md | PR67；research/CYCLE31_20260920/reviews/PR67/；主体通过，正文尾部不全，新seed浮点 |
| S79 | research/CYCLE31_20260920/S79/ | PR69；research/CYCLE31_20260920/reviews/PR69/；主体恒等式通过，任意通道反例，真实exterior未解 |
| S76 | research/CYCLE30_20260920/ | PR66；research/CYCLE30_20260920/reviews/PR66_FINAL/；完整原件与作者重放 |
| S75 | research/CYCLE27_20260920/ | PR65；research/CYCLE27_20260920/reviews/PR65/；无条件星形定理与条件障碍 |
| S74 | research/CYCLE27_20260920/ | PR64；research/CYCLE27_20260920/reviews/PR64_FINAL/；负mixed-entry证书、极密度率区域 |

S78 必带修正：research/CYCLE31_20260920/S78/REQUIRED_SCOPE_CORRECTION.md。
S79 必带修正：research/CYCLE31_20260920/S79/REQUIRED_LOGIC_CORRECTIONS.md。
QWE08 接口：research/CYCLE33_20260920/QWE08/ACCEPTED_INTERFACE_PR70.md。

## 真实率定理入口

- PR47：S63，rho=1/3,c=.95，非中点a区间。
- PR52：QWE07，rho小条带；原randomcat4/dpp-stationary-entropy PR129。
- PR53：S70旧成果，rho=1/3，c到.9535，偏置p区间。
- PR55：S69旧成果，更宽a区间；必须使用每线程向上舍入修正版。
- PR64：S74极稀／极密区域；密度限制1e−21，不能省略。

准确参数、常数与不能合并的边界见STATUS.md。

## 仍承重的历史入口

- PR16 / S42：occupation dephasing、准自由熵与有限弦/率传递。
- PR33 / QWE02：真实MI有限弦与巨大常数远尾；不是Ward–Stein。
- PR35 / S51、PR48 / S68：端点与重采样相关材料，固定n与率极限区分。
- PR38 / S55：半密度compact interior定性循环桥。
- PR40 / Ward–Stein：源randomcat4/dpp-entropy-concavity PR2；通用逐word反例，非实际sine率反例。
- PR42、44 / QWE05、S61：指定冻结循环单侧条件信息义务已完成。
- PR46 / S64：真实dyadic弦的有限保留尺度工作。
- PR51、56 / S67：count-gauge、加速度上界，剩余Fisher预算未付。
- PR60、61、62、63：S71、S72、S73及双点加速度/Fisher边界。

早期S1–S19的results目录与旧索引未删除。原根README、STATUS、METHODS、RESULTS快照在docs/history/20260918-root/；SYNC.json是旧同步出处，不代表当前研究状态。

## 使用原则

正文完整性、公式正确、严格数值证书、all-size定理、熵率结论分别登记。review通过不意味着整个研究目标通过；commit仅作出处，不设哈希验收。缺附件不重复派题；缺尾部则标SOURCE_PARTIAL，承重正文可单独审。
