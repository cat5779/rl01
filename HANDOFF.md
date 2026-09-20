# 主实例交接 — Cycle34 / 2026-09-20

## 接手的第一件事

先读 README.md、STATUS.md、COUNTEREXAMPLES.md、RESULTS.md，再核对本机 STATE.json 和最新独审。用户正在更换网页版来源；**暂停向旧网页版投放，不按历史队列自动补发。** 用户确认的新来源到位后，先核对已有任务，再决定新题。此暂停不妨碍收件与已有独审。

总目标仍是 TARGET.md 的真实 sine-Toeplitz 全配置 Shannon 熵率、全密度、全部合法偏置、整个 c∈(37/40,1)。已证局部区域不是全局定理；现无真实 sine 熵率反例。

## 当前收件和独审

- S76、S78：完整原件、作者程序与独审复跑已收。
- QWE08：完整结果与严格小尺寸连续参数证书，RL01 PR70。
- S77：可见数学主体第1–7节完整、后面截断；主体和脚本审查在 PR67。新 Burg seed 表格仍只是浮点。
- S79：数学主体第1–10节与脚本已审 PR69；原稿 ledger 尾部未齐。不能记成全文已审。
- S80：完整 S80_RESULT.md 已收到，原 SolA 独审PR71完成，值级telescope和逐word导数工具正确；无新凹性区域。最终回执见 research/CYCLE34_20260920/STATUS.md。
- 所有旧网页版结果已返回，当前网页版活动／预留槽为0。此次没有新网页版投放。

本轮没有必要催 S77/S79 重做数学；如导出容易，可补齐原稿尾部作出处完整性。S80作者可执行脚本未收到，正文不因此失效。

## 调度规则（用户要求，跨实例保持）

1. 网页版最多3个，sidebar Sol high最多2个，**独立计数**。用户自行启动和延迟待确认发送也计入网页版。
2. 每份完整任务只发送一次。idle、旧问候、同步延迟不表示失败，不补发 continue、启动词、全文或换窗口。先记尝试，后记回执。
3. S17绝对只读：6aab690d-4390-83e9-bde3-8dad680da3f8。禁止发送、追加、中断、重启。
4. 验证复用下面两个现有 Sol；分原稿、分关键结论独立审，不建立新本地任务或额外审稿智能体。
5. 新研究题面用英文，并保留：Think for at least 120 minutes, unless you achieve major progress earlier. 不伪报用时，不休眠凑时。
6. 明文要求：Do not route the user to Work, another chat, an agent, or a cloud task. This is a mathematical derivation task; deliver the reasoning here.
7. 鼓励创造可复用数学工具、跨领域迁移、理论推导；不再限制只做小算或强制重计算交接。
8. 不设 SHA、checksum 或其他哈希验收门槛。正文完成但导出失败仍算已交付正文；源完整性和数学通过分开。
9. 用户可见答复中文，PR和文件位置用可复制普通文字，不加超链接。
10. 运行失败不等于数学证伪；负局部项不等于完整熵反例。失败PR关闭前保留独特证据；成功PR也只按准确范围合并，不能盲合并大档案。

## 恢复位置与线程

公开仓库：cat5779/rl01。原件总档案 PR54，分支 research/sa-cycle19-harvest-20260919。
本机档案工作树：C:/game/gameproject/showa100/math/rl01-cycle19-harvest
权威运行账本：C:/game/gameproject/showa100/math/sa-dispatch-20260918/STATE.json
运行日志：C:/game/gameproject/showa100/math/sa-dispatch-20260918/LOG.md
用户收件目录：C:/Users/UIO/Desktop/20260907

SolA：SA02｜S18 接班：完整负曲率证书
thread 01a0b04a-afe9-7393-ba97-58270365d292，gpt-5.6-sol high。
本轮S80独审已完成PR71；原 QWE08审查已完成PR70。当前可用。

SolB：SA新稿｜Sol high 独立验证与缺口核查
thread 01a0b050-7e8f-75a3-a672-0200b567524b，gpt-5.6-sol high。
本轮反例地图证据审计已完成；输出已保存到 COUNTEREXAMPLES.md 的附录来源。当前可用。

旧结果线程，仅用于收件，不自动续派：
- Say s77：6aaed213-5cdc-83ee-b11a-384797c586b6
- Say S78：6aaed261-b570-83e8-b966-86b9cb058bd4
- Say s79：6aaed271-7c94-83e8-9875-30d90900e4da
- Say S80：6aaed27a-ea38-83e8-b183-5d93ce8ead7a（Cycle32完整任务已发送一次）

135分钟心跳：sa-135，当前绑定旧主实例 01a0ae39-4e85-7173-bb99-cd31b35ab0e6。本轮已清除过时Cycle11派活队列。接手到新实例后，应将同一心跳迁移到新主实例或暂停旧心跳，避免两个主实例同时调度；不要另建重复心跳。未获新来源前只收件、审查和汇报。

## 建议下一轮投入

优先将 QWE08 的秩一／小尺寸 MI 正性与 S77 的精确 Fisher–Burg 接口组合成一个明确的 all-size 支付题；目标是处理有符号负环项，不是重新证明秩一。
第二候选：S78 从逐对logdet补偿升级为多中心整体预算，须同时减少核心约486.93和O(k*l)累加；仅再压远尾不够。
第三候选：S79利用同一exterior-unitary跨层一致性支付 K''+J''>=H_hat''。不能要求任意layer-bistochastic通道也成立；那已严格失败。
S80已审通过限定弦差接口。没有弦面积尺度的残差不能付局部曲率，不为“全尺度”字样单独续费。

以上是候选顺序，不是已发任务。新来源可用后按最新证据选最多3题；避免三题都重做同一桥。
