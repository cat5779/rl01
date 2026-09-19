# Cycle24：两份新数学答复收齐可见部分，分别独审

更新日期：2026-09-19。整个 c∈(.925,1) 的熵率凹性仍未解决。

## S71：秩一工具与错误插值的障碍

作者给出有限 strict Hermitian-contraction DPP 沿正秩一 kernel line 的分块互信息凸性，以及实际两点共同shift互信息的全偏置严格下界。关键区别：原问题方向是I，不能把逐秩一方向凸性相加后忽略混合项。这仍是待审的候选工具，不是原all-size超加性证明。

作者另外给出真实端点概率律的仿射混合中点反例与二元熵补偿。两个端点是实际sine律，但混合中点不是实际kernel-shift DPP；反例只否定该辅助插值，不能当原猜想反例。可见第1–9节及完整精确checker已归档；API截断发生在第10节恢复说明，结尾尚不完整。作者未执行checker，独立审查将补做实际运行。已单独交SolB。

## S72：声称误差数量级显著下降，仍缺可负担的见证

作者声称 signed Ward coercivity、E[(SG+GS)/2]=2I、实际rank-one单边曲率和自归一化使观察误差在固定c、delta趋零时从O_c(delta^-10)降至O_c(delta^-5)。在原delta=.02基准，观察尾系数从约1.76e15降至约5.02e7(Phi)/2.56e7(Chi)，缩小约3500万/6900万倍。

这些是AUTHOR_ONLY、正在单独交SolA审查的结论。作者自己仍未给出足够大尺度、全参数连续区间的有限见证；m=L=2仍无法支付改进后的误差。误差数量级下降不等于固定c=.95单弦或全区间凹性已经证明。完整可见数学答复已收到；两个附件中的原诊断脚本/可能更长稿尚未收到。

## 同步收齐的外部第二轮结果

DPP PR131 的QWE09第二轮结果与RL01 PR59独立复现现已归档。PR59严格标为PASS_SCOPED_DIAGNOSTIC：真实n=12,c=.95,a=.025模型中，有14个word的Phi为负，最小值约-6.3854；一般二部投影中单个偶奇pair也可有错误符号，但总体混合项在新样本里仍未见正值。

这加强了“需要在word之间/pair之间补偿”的证据。新增n=12与二部模型结果的归档证据是独立浮点复现，不擅自升级为外向区间证书或总体符号定理；原六点零支付Jensen反例则已有PR57严格证书。都不构成真实熵率非凹反例。无需重复跑已完成的PR59复现。

## 调度与收件

网页版上限3，Sol上限2，独立计数。S71、S72本轮已实际交付，释放网页版槽位；S73仍active，保持原任务不打扰。现有两位Sol分别审S71与S72，不合并裁决、不新开本地任务、不派子智能体。S74/S75可用，但本轮先取得新增承重工具的正式裁决再定向续派，不用未审系数开重复证明任务。

需要补收：优先S72新答复中的两个附件（尤其诊断源文件）；其次S71完整回复的第10节结尾。S71无须为了导出失败重新研究，已收到的可见证明立即进入审查，不以ZIP/hash作为数学验收门槛。

四库已检查按更新时间排列的PR、默认分支最新提交和新增评论。本轮新增收件为S71/S72、QWE09第二轮及PR59；另两库只看到已知反例文档同步/无新研究交付。无新网页版发送，无重复投放。

## S71 separate audit received: RL01 PR60

VERIFIED_SCOPED_TOOL / SOURCE_PARTIAL_TAIL / MAIN TARGET INCOMPLETE.
Rank-one block multi-information convexity and two-site common-shift convexity pass independent review. The affine probability-law mixture counterexample is not a counterexample to the actual kernel-shift DPP. Exact checker independently executed successfully. Novelty remains unconfirmed. The missing source tail in section10 does not affect the complete audited sections1-9.
The all-size identity direction and full contrast interval (0.925,1) remain unresolved. Review, replay and checker archived under reviews/PR60. S72 review remains active; S73 still has no research answer. No webpage message sent.
