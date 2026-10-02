# DPP 高对比度熵路线账本

快照日期：2026-10-02。公开版统一以 `EULER` 表示来源主体；仓库尾名、PR 号、提交 SHA 和仓库内路径保留。本文只做来源考古和状态记账，不重新判定任何定理真假。

## 结论边界

- 当前没有登记到“高对比度真实 sine 熵率命题本身被否定”的证据。精确反例否定的是逐项、逐词、点态预算、条件化单调桥或对象替换。
- 英文有限核共同移位预算法是完整证明：`papers/stationary-channel/main.tex` 的 §4、§5、§5.3、张量 Bernstein 证书与 §6；文件提交 `16d5d55269eca9725e5eb3f5d0e6ebd785396741`，blob `b391f581fe8f9fbcd5a24f2a7f6de73fcb8884da`。
- 高对比度真实 sine 熵率仍是“远尾已付、真实带符号近场未付”。W02 的远尾闭合不等于完整高对比度定理。

## 现成骨架页

| 总览称呼 | 仓库路径 | 最后改动提交 | blob |
|---|---|---|---|
| 工具箱固定页 | `docs/methods-toolbox.md` | `fd7f3b4a6937f3b601371606bc5095a870aac12f` | `20cf46a8ac3276659689a5d2535a6cb85713fe02` |
| 方法边界原页 | `docs/methodbounds01.md` | `16d5d55269eca9725e5eb3f5d0e6ebd785396741` | `46642527dd9b65e8e4cfd8ba76fa7e02cc4c4a5e` |
| 旧路线账 | `docs/rejected-and-stalled-routes.md` | `fd7f3b4a6937f3b601371606bc5095a870aac12f` | `92e3233d1e174c6268c085b4a2a13b884d00e86c` |
| 熵参数地图 | `docs/entropy01.md` | `16d5d55269eca9725e5eb3f5d0e6ebd785396741` | `d6d92a8842caf4349b44b4a47137e6776f022d66` |
| 完整错误链与来源 | `review/sources01.json` | `5128965453df9f4ea4a9ddce85eedaea7bd05f76` | `cc8f8e7a9434aa18a7e81cd554a6b822125bcc20` |

以上五页均位于 `EULER/dpp-entropy-concavity` 的集成树；账本再用原仓库 PR head 和仓库内审查文件回填。

## 七库覆盖

| 仓库 | 分支 | PR | open PR | closed-unmerged PR | ordinary issue |
|---|---:|---:|---:|---:|---:|
| `EULER/dpp-entropy-concavity` | 8 | 7 | 4 | 0 | 1 |
| `EULER/dpp-stationary-entropy` | 118 | 117 | 16 | 16 | 14 |
| `EULER/dpp-entropy-tools` | 128 | 111 | 3 | 4 | 36 |
| `EULER/rl01` | 96 | 95 | 54 | 2 | 0 |
| `EULER/icm-conjecture-results` | 22 | 21 | 21 | 0 | 2 |
| `EULER/icm-conjecture-lab` | 95 | 89 | 84 | 2 | 12 |
| `EULER/i05-private-exploration` | 45 | 58 | 13 | 7 | 35 |
| **合计** | **512** | **498** | **195** | **31** | **100** |

上表是七库来源清单覆盖量：已枚举分支、PR 状态、ordinary issue 与 PR 文件树。它不再被表述为“每个结果文件内的所有子主张均已穷尽提取”。本轮已纠正只读标题/摘要会漏掉 `DISPROVED` 小节的事实，并逐项补入给定差异清单；其余六库仍需同口径的结果正文子主张复扫，故当前 92 行是已核实账目，不是穷尽性完成证书。任务合同、提示词壳和纯排程页不作为数学结果；其中已经关闭且确无交付者列入“无结果中止”。

对象：`(a)` 有限核共同移位；`(b)` 真实平稳 sine 熵率；`(c)` 修正律/循环模型；`(d)` 固定物理符号路径；`(e)` MI 方向变体。

## 正面闭合（限定范围）（21）

| 编号 | 名称 | 来源仓库 | 分支或PR | 对象 | 参数 | 原始主张 | 状态 | 致死证据 | 死因归类 | 后续 | 是否可能复活 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | 有限核共同移位至23/25 | EULER/dpp-entropy-concavity | sync01；Draft PR7；文件提交16d5d55269eca9725e5eb3f5d0e6ebd785396741 | (a) | 任意有限Hermitian正压缩K；0<=c<=23/25；0<=a<=1-c；任意n | “Bayes reallocation”与两层Fisher–Schur预算给出H''<=-(2/5)n，并由有限强Jensen传递到平稳率。 | 正面闭合（限定范围） | papers/stationary-channel/main.tex §§4–6；computations/stationary/verify_stationary_double_budget*.py；主文件blob b391f581fe8f9fbcd5a24f2a7f6de73fcb8884da | 不适用 | 被37/40层及W02微延伸继承；证明结构也是后续高对比尝试的基线。 | 不适用 |
| P02 | W02通用微延伸 | EULER/dpp-stationary-entropy | PR13；ba48e51efcfc8cccb6055e579bf2a5df970b67f7 | (a)(b) | 任意有限K；0<=c<=925003/10^6；全闭合法a；任意n | “H_n''<=-n/1000”；同一有限强Jensen结论传给任意固定平稳符号。 | 正面闭合（限定范围） | web_tasks/W02/PROOF.md；verify_bridge.py；receipt.json；冻结对象18bee13c9ddfb14797a6ac99157fe3e642f4a44c | 不适用 | 保留37/40层更强模数；不能外推到c=.95。 | 不适用 |
| P03 | PR4稀疏密度全移位区 | EULER/dpp-stationary-entropy | PR4；d6910de48c4b5bc52b35352645663a5ea12ebc1d | (b) | min(rho,1-rho)<=1/50；23/25<=c<=19/20；全闭合法a | “H_n''<=-(148/625)n”，继而得到真实平稳DPP熵率强凹。 | 正面闭合（限定范围） | research/sine-structure-above-37-40-20260913/PROOF.md §6；audit/pr4-sine-independent-20260913/REVIEW.md | 不适用 | 与中心偏置局部区只能取并集，不能拼成未证笛卡尔盒。 | 不适用 |
| P04 | SA02中点强凹区 | EULER/rl01 | PR3/PR11；74383ffba4419b1c20fe8926b23a4022c8df8d8c | (b) | rho=1/2；.925<=c<=.937；a=(1-c)/2 | 中点有H_n''<=-n/50的审定区。 | 正面闭合（限定范围） | research/INDEPENDENT_REVIEW_20260918/SA02_C37_BOUNDARY.md | 不适用 | S51只在极窄移位条带扩展；.95及全移位仍未付。 | 不适用 |
| P05 | S51窄移位条带 | EULER/rl01 | PR31；6b4070352cc85a888501cb0e779b2495f1a13f7b | (b) | rho=1/2；.925<=c<=.937；\|a-(1-c)/2\|<=10^-9 | 冻结依赖下的窄条带强凹。 | 正面闭合（限定范围） | research/INDEPENDENT_REVIEW_20260918/README.md | 不适用 | 有效窄区不因更宽估计失败而撤销。 | 不适用 |
| P06 | S63半径22局部区 | EULER/rl01 | PR47；4aae11873a593fbc42d75d98586d8d4dc6a02b0e | (b) | rho=1/3；c=.95；.021<=a<=.024 | H_n''<=-n/25+399。 | 正面闭合（限定范围） | research/INDEPENDENT_REVIEW_20260918/S63_ROUND2_REVIEW.md | 不适用 | QWE07继承22点核心并运输到窄密度带。 | 不适用 |
| P07 | QWE07窄密度运输 | EULER/dpp-stationary-entropy + EULER/rl01 | stationary PR129 6a1eb3ae06bcf5a220cbb55b74ca7aef9ae3f0e4；rl01 PR52 b9bcbd5db6dc41d89893b2a5b91088551cf6ddac | (b) | c=.95；rho∈[1/3,1009/3000]；.021<=a<=.024 | 真实complete-configuration law上H_n''<=-n/25+399；严格有限负性仅n>=9976。 | 正面闭合（限定范围） | research/INDEPENDENT_REVIEW_20260918/QWE07_CYCLE17_REPRODUCTION/README.md；1536 guards、55 nodes、每点2^22 words | 不适用 | 扩带、全a和全密度未闭合。 | 不适用 |
| P08 | S69移位区 | EULER/rl01 | PR55；bf52b165e41ef57924e5db9fb9436e77b72dd8b1 | (b) | rho=1/3；c=.95；.02<=a<=.0255 | 上舍入修复后得到限定强凹区。 | 正面闭合（限定范围） | research/INDEPENDENT_REVIEW_20260918/S69_CYCLE18_REPLAY.md | 不适用 | 下一段(.0255,.03]未付；a=.026的冻结框架失败另列W02。 | 不适用 |
| P09 | S70偏置密度盒 | EULER/rl01 | PR53；e9a5069528ba63c4d82f382cc8eaf2d77fb028e8 | (b) | rho=1/3；.95<=c<=.9535；p∈[.42,.48] | 限定参数盒内强凹。 | 正面闭合（限定范围） | research/INDEPENDENT_REVIEW_20260918/S70_CYCLE18.md | 不适用 | c=.96,p=.45的冻结见证失败另列W03。 | 不适用 |
| P10 | S74极端密度区 | EULER/rl01 | PR64；49aae706927a43329fe0cfb7ed07ec94bcdd23cf | (b) | .925<=c<=.95；.02<=a<=.03；min(rho,1-rho)<=10^-21 | 极窄边缘密度强凹。 | 正面闭合（限定范围） | research/INDEPENDENT_REVIEW_20260920/S74_CYCLE26_REPLAY.md | 不适用 | 普通密度未覆盖；六点mixed entry不能改写为共同方向结论。 | 不适用 |
| P11 | S71与QWE08小尺寸MI | EULER/rl01 | PR60 69eb3af06e632d2eb2d32322ea7d51df355c4a06；PR70 ad7161a4d0634d2a538445c870b867b4172a2ac7 | (e) | rank-one二部MI；真实半sine至n=3,4连续偏置 | rank-one MI凸性及小尺寸区间证书在其范围内成立。 | 正面闭合（限定范围） | research/INDEPENDENT_REVIEW_20260918/S71_CYCLE24_REPLAY.md；QWE08_CYCLE33/QWE08_CYCLE33_REVIEW.md | 不适用 | 不能把rank-one核线替换为rank-n共同移位。 | 不适用 |
| P12 | S76循环D-sector | EULER/rl01 | PR66；9292a5275619a682ed710cbb5e4a94d8642db29d | (c) | 半填充中点循环模型；每层；0<c<1 | 修正循环律的D-sector逐层非正。 | 正面闭合（限定范围） | research/INDEPENDENT_REVIEW_20260920/S76_CYCLE28_REPLAY.md | 不适用 | X-sector、真实Toeplitz、偏心与一般密度未传回。 | 不适用 |
| P13 | S61单侧删除流 | EULER/rl01 | PR44；b94d2b6578ea607cf8087b19ecf0b70144771953 | (c) | 指定半密度修正律；n→∞ | W_rel>=-O(sqrt(n)log n)=-o(n)。 | 正面闭合（限定范围） | research/INDEPENDENT_REVIEW_20260918/S61_CYCLE10_REVIEW.md | 不适用 | 这不是\|W_rel\|=o(n)，也不是到真实熵率的二阶桥。 | 不适用 |
| P14 | PR136固定物理符号路径 | EULER/dpp-entropy-tools | PR136；39098dac760cea2d27f2955bed31f80c87913810；merge f1c8b9a28dc6bb3abbfc8d69e3332c0550d8703d | (d) | f_t(theta)=1/2+cos(4πtheta)/4+t cos(2πtheta)/8；t∈[1/2,3/2] | 真实Shannon熵率满足h''(t)<-1/3000。 | 正面闭合（限定范围） | ENTROPY_KL_C2_TAIL.md；research/S2-pr136-independent-finite-audit-20260911/continuation/PR136_LOCAL_CONTINUATION.md | 不适用 | 保留complete-law二阶响应；旧PR112/115证书不因此获得认证。 | 不适用 |
| P15 | QWE02有隙边界响应 | EULER/dpp-stationary-entropy + EULER/rl01 | stationary PR123 f359b3c0b7fa03de1f4824ab4986edb186c3e3e0；rl01 PR33 661bb2fcd1729a391f4785d962deb7c9c7ec0d82 | (e) | 固定有隙benchmark；δ>0 | \|MI''\|<=32 δ^-12 \|\|K_AB\|\|_HS^2；只给大小不判符号。 | 正面闭合（限定范围） | research/INDEPENDENT_REVIEW_20260918/QWE02_BOUNDARY_RESPONSE.md | 不适用 | δ^-12接口被QWE08复用；不能当共同移位曲率符号。 | 不适用 |
| P16 | S4极端迹密度高对比区 | EULER/dpp-entropy-concavity | main 227f71d08a570a753c12d6c5d4eea239382901db | (a) | Tr(K)/n<=1/100或>=99/100；37/40<=c<=959/1000；(1-c)/4<=a<=3(1-c)/4；任意n | 有限核共同移位满足H''<=-11n/250，并给率级11/500强Jensen。 | 正面闭合（限定范围） | research/overnight-reviewed-20260917/group-b/research/s4-round4-information-payment-20260917/source/S4_round4_information_payment/proof.md及INDEPENDENT_AUDIT | 不适用 | 补足极端平均迹密度；不覆盖一般密度。 | 不适用 |
| P17 | 三点核全对比共同移位 | EULER/dpp-stationary-entropy | PR7；2d912c1747ffa044ed0582fed9557becc6a03c62 | (a) | 任意3x3 Hermitian contraction；0<=c<1；0<=a<=1-c | 内点H_3''<=-6 log 3，闭区间上全局凹。 | 正面闭合（限定范围） | research/n3-all-contrast-swap-20260913/PROOF.md；reviews 5190271775与5190273180 | 不适用 | 覆盖0.925<c<1但只限n=3。 | 不适用 |
| P18 | S6临界层全有限核条带 | EULER/dpp-entropy-concavity | main 227f71d08a570a753c12d6c5d4eea239382901db | (a) | 任意有限K,n；37/40<=c<=37/40+10^-13；\|a-(1-c)/2\|<=1/200 | H''/n<=-1/200。 | 正面闭合（限定范围） | research/s6-round4-reviewed-20260916/source/proof.md | 不适用 | 只给极薄对比度层和中点附近条带。 | 不适用 |
| P19 | 秩一或余秩一核全高对比 | EULER/dpp-entropy-concavity | main 227f71d08a570a753c12d6c5d4eea239382901db | (a) | n>=2；rank(K)=1或rank(I-K)=1；1/2<=c<1；全闭合法a | H''<=-4n(n-1)/(n+2)。 | 正面闭合（限定范围） | research/s23-reviewed-20260916/README.md | 不适用 | 覆盖整个0.925<c<1但只限秩一或余秩一。 | 不适用 |
| P20 | 实二点核全局凹性 | EULER/dpp-entropy-tools | main 237097124869b3bb04c139d4c4599e6bda7d344d；review 603300c06059518961766c724377c3b9d1198fc5 | (a) | 严格可行实对称2x2核；完整事件熵；全可行共同移位弦 | 全局凹；每条非平凡弦都有严格中点损失。 | 正面闭合（限定范围） | research/R1/proofs/n2_concavity.md；research/R1/verification/n2_concavity_commit_review.md | 不适用 | 给出n=2实核完整结论；不含一般复Hermitian或高维。 | 不适用 |
| P21 | Ward--Stein结构恒等式与标量区 | EULER/rl01 | PR39 20f7ddcce56a57b68328c9d1f00cb8a368b9b5c4；PR40 26ad777f9656f3fe3f15ea0dfc5a8f8338647c89 | (b) | 有限后验；正可逆Ward生成元；标量闭合c<=sqrt(3)/2 | Ward/Bayes/chord恒等式、正可逆生成元及E B_c=bJ(c)成立；标量预算只闭合至c<=sqrt(3)/2。 | 正面闭合（限定范围） | research/CYCLE09_20260918/reviews/WARD_STEIN_PR2_REVIEW.md及独立复核 | 不适用 | 点态B_c(z)<=1被D18否定；平均c=.95符号仍未闭合。 | 不适用 |

## 方法被精确反例否定（29）

| 编号 | 名称 | 来源仓库 | 分支或PR | 对象 | 参数 | 原始主张 | 状态 | 致死证据 | 死因归类 | 后续 | 是否可能复活 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D01 | S21逐系数支付 | EULER/dpp-entropy-concavity + EULER/rl01 | rl01 PR49 10f186e94e71a659a3e08449cffe41671c1c4d82；docs提交16d5d55269eca9725e5eb3f5d0e6ebd785396741 | (a) | 六点Fourier投影；c=.95；a=1/40 | 企图逐项证明支付多项式每个系数非正。 | 方法被精确反例否定 | docs/methodbounds01.md： [c^36]U_P=94817639921336320/150094635296999121>0；同点H_aa≈-165.799，aggregate≈-77.28 | 逐项收费过强 | 后续改用同一posterior中的带补偿平均。 | 否；被否定的是逐系数符号要求，原熵命题未被否定 |
| D03 | 六点后验零支付Jensen | EULER/dpp-entropy-concavity | docs/methodbounds01.md；提交16d5d55269eca9725e5eb3f5d0e6ebd785396741 | (b) | rho=1/2；c=19/20；a=1/40；n=6；条件word 00011 | 要求每个条件word的局部势Jensen差无需额外支付。 | 方法被精确反例否定 | Delta_Phi∈[-.106585307859143407,-.106585307859143406]；Delta_Chi约-.09639546527；所需lambda>0.625832574752639508>5/8 | 逐项收费过强 | 真实律全部word的加权平均仍需带补偿处理。 | 否；零支付逐word主张已破，平均方法仍可能 |
| D04 | 463/500点态双预算 | EULER/dpp-stationary-entropy | PR1证书链；review/verification.md；集成提交9ce5dd43d0b27f8f017fb2cff613b9572e9ed61d | (a)(b) | c=463/500=.926；精确有理可行局部表 | 继续要求g_+<=gamma(K+D)且gamma<=2。 | 方法被精确反例否定 | exact rational witness violates even gamma=2；review/claim-ledger.md | 逐项收费过强 | 高对比路线必须保留跨pair、跨state平均。 | 否；该点态常数已死，不是否定完整输出平均 |
| D05 | 条件化曲率单调桥 | EULER/dpp-stationary-entropy | PR4；d6910de48c4b5bc52b35352645663a5ea12ebc1d | (e) | rho=1/2；c=.95；a=1/40；4096 outside histories；8192中心事件 | 更多双侧条件化会使中心预测曲率更负，并可单调传给单侧熵率。 | 方法被精确反例否定 | research/sine-structure-above-37-40-20260913/RESULTS.json与审查：MI''≈+24.571 | 量词顺序错误 | PR136完整响应保留p'F'与p''F项，绕开单调桥。 | 否；桥本身已破，但非线性预测增益和熵率命题未被否定 |
| D06 | S41旧complete-jet方向引理 | EULER/rl01 | PR17/PR19；1dd3038e27b9d0840364d2dbbf05501dcb371546 | (b) | 十维投影；冻结半填充局部泛函 | 旧方向引理声称complete-jet具有所需统一符号。 | 方法被精确反例否定 | research/INDEPENDENT_REVIEW_20260918/S41_CYCLE04.md：exact 10-dimensional projection counterexample | 逐项收费过强 | S41 Cycle05的Z0修复另列R01。 | 否；旧方向引理不可复用 |
| D07 | RL01 S3六点坏原子 | EULER/rl01 | S3审查链；主快照4cf1a8e6682e44d741f877a5acc387854c3ab124 | (b) | 真实六点sine；高对比局部原子 | 一次性逐原子支付应逐word为好号。 | 方法被精确反例否定 | 坏原子严格反号；同一证据同时给完整熵Hessian<-1000 | 逐项收费过强 | 后续路线保留原子间抵消；该证据反而确认不是熵反例。 | 否；坏原子精确，但平均路线仍活 |
| D08 | S64原始窗口单调性 | EULER/rl01 | PR46；10b4ba30ae899080581e0c769cbf6a26b8d02c86 | (b) | 固定窗口；真实posterior | 两条原始窗口量应随窗口单调并直接给预算。 | 方法被精确反例否定 | research/INDEPENDENT_REVIEW_20260918/S64_CYCLE11_REVIEW.md记录两项raw monotonicities失败 | 量词顺序错误 | S64的KL长度工具被保留；S67另做Green预算。 | 否；单调性形式已破，工具子引理可继承 |
| D09 | S75旧逐word/一般密度漂移 | EULER/rl01 | PR65；2ee4934155db0b7ef302b98e19ee6e9663de817f | (b) | 单中心扩展到背景word或一般rho | 背景逐word漂移及一般密度逐pair漂移应非负。 | 方法被精确反例否定 | research/INDEPENDENT_REVIEW_20260918/S75_CYCLE26/S75_CYCLE26_REVIEW.md记录二者可负 | 逐项收费过强 | 只保留单中心真实无条件平均的正面结论。 | 否；逐word推广已破 |
| D10 | S77固定theta<1加次二次余项 | EULER/rl01 | PR67；66147b020e846aef73c82b5fcf78c9deb6d907af | (b) | 弱割摄动；固定theta<1；余项o(d^2)，其中d=\|\|K_AB\|\|_HS^2 | 用固定theta<1乘Fisher--Burg主项，再加小于d^2量级的余项，可统一支付弱割。 | 方法被精确反例否定 | research/INDEPENDENT_REVIEW_20260918/S77_CYCLE31/S77_CYCLE31_REVIEW.md：-C_acc/D_F趋于1 | 逐项收费过强 | 不排除theta=1、另一项二次余量或sine专用非摄动估计。 | 否；只排除该固定theta与次二次余项组合 |
| D13 | QWE08单项Taylor正性 | EULER/rl01 | PR70；ad7161a4d0634d2a538445c870b867b4172a2ac7 | (e) | QWE08小尺寸MI Taylor展开 | 要求展开中的相关单项逐项非负。 | 方法被精确反例否定 | research/INDEPENDENT_REVIEW_20260918/QWE08_CYCLE33/QWE08_CYCLE33_REVIEW.md：出现-s^10/27 | 逐项收费过强 | 只能使用完整展开的总和或带补偿分组；不再重复计入S21证据。 | 否；该单项符号已被精确系数否定 |
| D14 | 全局修正差凸性快捷法 | EULER/rl01 | SA05 PR5/PR7；PR42/PR44 | (c) | n=8修正律与真实律之差 | E差应全局凸或全局凹，从而直接传回真实律。 | 方法被精确反例否定 | SA05审查：n=8 E difference neither convex nor concave | 对象替换错误（计数熵、谱熵、循环模型等） | QWE05/S61改做一侧删除KL与W_rel。 | 否；全局曲率符号主张已破 |
| D15 | 任意二元输入渠道替代 | EULER/dpp-entropy-concavity | docs/rejected-and-stalled-routes.md；fd7f3b4a6937f3b601371606bc5095a870aac12f | (a) | 任意相关Bernoulli输入 | 把DPP专有负相关/Schur结构丢掉后仍主张共同噪声凹性。 | 方法被精确反例否定 | 固定页记录三比特非DPP输入反例 | 对象替换错误（计数熵、谱熵、循环模型等） | 后续限定为DPP complete-event结构。 | 否；泛化对象已被反例否定 |
| D17 | 信道复合提升对比度 | EULER/dpp-entropy-concavity | docs/rejected-and-stalled-routes.md；fd7f3b4a6937f3b601371606bc5095a870aac12f | (a) | 从低c基线向高c | 把高对比信道写成低对比信道再复合。 | 方法被精确反例否定 | 旧路线账：channel composition cannot increase contrast | 其他（信道参数方向错误） | 后续只能建立新的高对比预算或结构区。 | 否；参数单调方向错误 |
| D18 | Ward--Stein逐词B_c不超过1 | EULER/rl01 | PR39 20f7ddcce56a57b68328c9d1f00cb8a368b9b5c4；PR40 26ad777f9656f3fe3f15ea0dfc5a8f8338647c89 | (b) | 32站点rank-16平衡Hadamard投影；c=19/20 | 对每个词z都有B_c(z)<=1。 | 方法被精确反例否定 | research/CYCLE09_20260918/reviews/WARD_STEIN_PR2_REVIEW.md：B_c=1.1776728191029975>117/100>1，证书复核 | 逐项收费过强 | P21的恒等式与平均结构保留；c=.95平均符号仍未付。 | 否；只否定逐词上界，不否定Ward--Stein结构 |
| D19 | S18所有混合元非正 | EULER/rl01 | PR8；b6cf597d262ab78eb39f909d3358705f8b55acb6 | (a) | 六点half-sine；rho=1/2；c=19/20；a=1/40 | 完整熵Hessian的所有混合元均非正。 | 方法被精确反例否定 | research/CYCLE02_20260918/S18_ROUND2_LATEST.md：∂t1∂t6 H_6>0.000379092242041686，而完整6x6 Hessian仍严格负定 | 逐项收费过强 | 共同方向凹性未被否定；只能放弃逐元符号。 | 否；精确反例只打掉逐元非正 |
| D20 | QWE01两点混合元非负 | EULER/rl01 | PR36；6974b50d89c5d349412115c11af3a1e40ce485ba；PR64复核 | (a) | K=[[1/5,1/10],[1/10,3/5]]；v=(1,1) | 用混合Hessian逐元非负推出共同方向符号。 | 方法被精确反例否定 | research/CYCLE08_20260918/reviews/QWE01_REVIEW.md：混合元=-7058578388000000/3400782877756341<-2；共同方向=1095440907576040000/3400782877756341>0 | 逐项收费过强 | 共同方向仍可为正；逐元桥不可用。 | 否；逐元主张已有有理精确反例 |
| D21 | S74混合坐标非负 | EULER/rl01 | PR64；49aae706927a43329fe0cfb7ed07ec94bcdd23cf | (a)(b) | 六点half-sine；c=.95；a=.025；u,v∈[0,10^-10] | 局部矩形上的混合坐标曲率非负。 | 方法被精确反例否定 | research/INDEPENDENT_REVIEW_20260920/S74_CYCLE26_REVIEW.md：M_uv(0,0)≈-0.000379092242041686；全矩形M_uv<-3/10000；矩形缺陷<-3e-24 | 逐项收费过强 | 同点D_F+C_acc>0，故共同方向结论未被否定。 | 否；混合坐标符号已被区间证书否定 |
| D22 | S18精确势沿秩一揭示凸性 | EULER/rl01 | PR3 ec08fb588c34cfebe5d8853067bff2ad8113b644；PR8汇总 | (a) | 一般严格DPP posterior；delta=1/40；c=19/20 | 指定精确势在每次秩一揭示下凸，且可取小统一补偿gamma。 | 方法被精确反例否定 | research/PRO02/S18_RESULT.md §11：归一化Hessian 2-c^2/[8delta(1+c/2)]<0；gamma>=125/236≈.529661 | 逐项收费过强 | 不排除替代势或加权资源。 | 是；只否定指定势与小补偿见证，不建议沿原势继续 |
| D23 | S63 O1计数唯一得分 | EULER/rl01 | PR45；aff202e94902289d3993f59139fd2d6d71eb2637 | (a)(c) | 六点rank-two循环Fourier投影；rho=1/3；c=19/20；a=1/50 | 共同移位得分只依赖计数\|Y\|。 | 方法被精确反例否定 | research/CYCLE12_20260919/S63/S63_CYCLE11_RESULT.md：同计数Y={0,1}与Y'={0,3}的h分别1/36与1/9，posterior overlap与score不同；z=4753/3 | 对象替换错误（计数熵、谱熵、循环模型等） | 不能压缩为count-only score；D11的更宽计数熵替换仍只登记为缺口。 | 否；该count-only得分主张有精确反例 |
| D24 | S67点态factor-one J不超过W | EULER/rl01 | PR51；8cb6f9b01b0b9b3e7f4ca80cbfef39ab5bfde43c | (b) | 四站点真实sine模型；固定pair与posterior | 逐点有J^b_ij<=W^b_ij。 | 方法被精确反例否定 | research/INDEPENDENT_REVIEW_20260918/S67_CYCLE17_REPLAY.md及S67_ACCELERATION_RESULT.md：Arb区间证书给出反例 | 逐项收费过强 | 有界odds下J<=3W/2仍保留。 | 否；factor-one逐点形式已死 |
| D25 | S67真实律平均factor-one | EULER/rl01 | PR51；8cb6f9b01b0b9b3e7f4ca80cbfef39ab5bfde43c | (b) | 六站点真实sine模型；所有外部配置按真实概率求和 | 对真实律平均后仍有factor-one付款。 | 方法被精确反例否定 | research/INDEPENDENT_REVIEW_20260918/S67_CYCLE17_REPLAY.md及S67_ACCELERATION_RESULT.md：穷举全部外部配置的实际概率平均反例 | 逐项收费过强 | D24不是唯一障碍；全局Green架构仍需另行分配。 | 否；实际律平均形式也被否定 |
| D26 | S67计数倾斜与有限压缩交换 | EULER/rl01 | PR56；e30114f78d922146dcc7aef636289b163e54119a | (b)(c) | n=1；z=6/5 | 计数倾斜函数演算与有限压缩无误差交换：f_z(K_{b,n})=uI+(v-u)Q_n。 | 方法被精确反例否定 | research/INDEPENDENT_REVIEW_20260918/S67_CYCLE20_REVIEW.md：n=1,z=6/5精确反例 | 有限证书无法传到无限体积 | 后续路线显式支付interaction-level非交换误差。 | 否；无误差等式已被精确否定 |
| D27 | SA03带符号输运分量非负 | EULER/rl01 | PR2；PR5 7444d97217c090e246c3188031ffd67c4d2437e7 | (b)(d) | R=1真实Fejer DPP；u≠0 | 带符号输运分量逐词非负。 | 方法被精确反例否定 | research/COMPUTE01/analytic_sa03/verdict.md及SA03_S9_SIGNED_TRANSPORT.md：T B_phi=-4u^2 B_t<0 | 逐项收费过强 | 不否定补偿后的期望级路线。 | 否；分量逐词符号被解析式否定 |
| D28 | SA03完整局部核逐词非负 | EULER/rl01 | PR5；7444d97217c090e246c3188031ffd67c4d2437e7 | (b)(d) | R=9；u=1；物理词001010011001101011 | 完整局部带符号核在每个物理词上非负。 | 方法被精确反例否定 | research/COMPUTE01/analytic_sa03/route_registry.md及SA03_S9_SIGNED_TRANSPORT.md：归一化核=-1.9552822249；残差0,-4.1063612421,+5.5419951053,-11.3909160881，baseline=8 | 逐项收费过强 | 期望补偿或Gamma路线未因此被否定。 | 否；指定物理词给出数值证书 |
| D29 | S42有限半径圆柱表示 | EULER/rl01 | PR10 | (c) | n=6循环半密度Fourier；x=.7；m=1；alpha=.5 | 所需修正量由固定半径圆柱观察决定。 | 方法被精确反例否定 | research/INDEPENDENT_REVIEW_20260918/S42.md：z=(00000)与z'=(00100)有同半径一观察，但k=2.7026222222与2.8370178761 | 其他（有限半径可测性错误） | 抽象L2圆柱闭包仍可保留；固定半径精确表示不可用。 | 是；只否定固定半径精确表示 |
| D30 | S55无泄漏有限Toeplitz压缩 | EULER/rl01 | PR32/PR38；PR63原结果 | (b)(c) | 单点A={0}；Q_A=q=1/2；v=0 | 有限Toeplitz压缩没有边界泄漏项。 | 方法被精确反例否定 | research/CYCLE08_20260918/S55/original/S55_CYCLE08_RESULT.md：遗漏泄漏=c^2/4；正确项为c^2 x*(Q_A-Q_A^2)x | 有限证书无法传到无限体积 | 后续传递必须显式带泄漏项。 | 否；无泄漏等式已有最小精确反例 |
| D31 | S55循环投影算子范数收敛 | EULER/rl01 | PR32/PR38；PR63原结果 | (c)(b) | 零延拓循环投影到Toeplitz投影；n趋于无穷 | 有限循环投影按算子范数收敛到无限Toeplitz投影。 | 方法被精确反例否定 | research/CYCLE08_20260918/S55/original/S55_CYCLE08_RESULT.md：operator-norm convergence标为DISPROVED | 有限证书无法传到无限体积 | 主传递只使用强收敛，不依赖被否定的算子范数捷径。 | 否；范数收敛捷径已死，强收敛路线保留 |
| D32 | S59局部Bellman统一选取 | EULER/rl01 | PR45；aff202e94902289d3993f59139fd2d6d71eb2637 | (b) | 两点合法DPP经1/40 BSC；posterior四界内；cross-ratio=6 | Phi_*(q)=1/[q(1-q)-b]可在所有channel-legal表上作统一局部Bellman选取。 | 方法被精确反例否定 | research/CYCLE11_20260918/S59/S59_CYCLE09_RESULT.md：表(29679,9126,579121,29679)/647605；log(6)/E>147/100 | 其他（局部Bellman选取不兼容合法表） | N03继续登记S59主Gamma符号无结果；两者不是同一层主张。 | 否；指定统一选取被精确表否定 |
| D33 | S42指定尺度给出小o二次误差 | EULER/rl01 | PR16 | (c) | 指定eta尺度；修正律圆柱近似 | 冻结尺度自动把误差改进为o(eta^2)。 | 方法被精确反例否定 | S42_CYCLE03：该尺度只给O(eta^2)，要小o尚需额外发散乘子 | 值界缺弦长平方 | G03保留更宽的dyadic弦接口缺口。 | 是；改尺度可绕开，但原冻结尺度主张不成立 |

## 只有见证/分配失败（方法本身未被否定）（6）

| 编号 | 名称 | 来源仓库 | 分支或PR | 对象 | 参数 | 原始主张 | 状态 | 致死证据 | 死因归类 | 后续 | 是否可能复活 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D02 | 22点最近邻PSD分配 | EULER/dpp-entropy-concavity | docs/methodbounds01.md；提交16d5d55269eca9725e5eb3f5d0e6ebd785396741 | (b) | rho=1/3；c=.95；a=.026；n=22 | 固定最近邻PSD分配与test function应支付目标负担。 | 只有见证/分配失败（方法本身未被否定） | 最大支付<=17.56799346358776726593；负担>=17.66432819592507325913；gap<=-0.09633473233730599320 | 其他（固定资源与测试分配不足） | S63/QWE07改用不同参数区与更完整资源。 | 是；只否定该固定分配，但不建议只继续调同一test function |
| W02 | S69下一框架a=.026 | EULER/rl01 | PR55；bf52b165e41ef57924e5db9fb9436e77b72dd8b1 | (b) | rho=1/3；c=.95；a=.026 | 冻结S69框架应继续覆盖下一小段。 | 只有见证/分配失败（方法本身未被否定） | research/INDEPENDENT_REVIEW_20260918/S69_CYCLE18_REPLAY.md：frozen frame fails at .026 | 其他（冻结框架余量不足） | 保留已证[.02,.0255]；下一段需换或强化见证。 | 是；是框架边界，不是H''正例；不建议无变化重跑同一框架 |
| W03 | S70在.96与.45的冻结见证 | EULER/rl01 | PR53；e9a5069528ba63c4d82f382cc8eaf2d77fb028e8 | (b) | rho=1/3；c=.96；p=.45 | S70同一冻结证书可外推到更高对比。 | 只有见证/分配失败（方法本身未被否定） | research/INDEPENDENT_REVIEW_20260918/S70_CYCLE18.md记录冻结witness失败 | 其他（证书余量不足） | 保留c<=.9535局部盒。 | 是；见证失败而非熵反例，但不建议原样外推 |
| W04 | S78 logdet补偿余量 | EULER/rl01 | PR68；0e0df56a634b09545ae45caaacf2c693ddf4f885 | (b) | rank-one reveal；reverse-KL telescope；moving pair | logdet补偿与R^-4尾可把总上界压到非正。 | 只有见证/分配失败（方法本身未被否定） | research/INDEPENDENT_REVIEW_20260920/S78_CYCLE31/S78_CYCLE31_REPLAY.md：约220倍包络改进后总上界仍约+490.39；moving-pair obstruction | 其他（补偿余量仍为正） | 非交换reveal与telescope被S79/后续保留。 | 是；结构工具未被否定，但需新的collective core/pair补偿；不建议只优化同一包络 |
| W05 | QWE09逐词零支付与巨大常数 | EULER/dpp-stationary-entropy + EULER/rl01 | stationary PR131 bb9a95edc49a34f45775c011cb35f33b5c0f4d23；rl01 PR57/58/59 | (b) | 六点及n=12局部词；mask-uniform接口 | 逐词Phi零支付及当前常数足以推出全尺寸平均符号。 | 只有见证/分配失败（方法本身未被否定） | QWE09_CYCLE22_REPLAY.md、ACTUAL_PAYMENT_CYCLE23.md、QWE09_ROUND2_REPLAY.md：严格局部障碍；当前gap常数约1.76e15不可用 | 逐项收费过强 | 保留O(log n/sqrt n)接口，最终平均符号仍未付。 | 是；逐词形式已死，但mask-uniform接口可换资源再试；不建议追逐零支付 |
| W07 | QWE07旧仿射两点付款 | EULER/rl01 | PR52；b9bcbd5db6dc41d89893b2a5b91088551cf6ddac | (b) | c=.95；a=3/125；rho=.34及rho=.5；同一仿射B_z与固定test f | 原两点付款见证可从基准密度直接延拓。 | 只有见证/分配失败（方法本身未被否定） | research/INDEPENDENT_REVIEW_20260918/QWE07_CYCLE17_REPRODUCTION：rho=.34时P-(C0-1)d∈[-0.06194256,-0.06194254]；rho=.5时∈[-122.92793866,-122.92793864] | 其他（固定见证与密度运输不足） | P07改用完整22点证书，仅覆盖rho∈[1/3,1009/3000]。 | 是；只否定同一仿射见证，不否定H''符号或整体架构；不建议继续固定test |

## 发现缺口后未修（17）

| 编号 | 名称 | 来源仓库 | 分支或PR | 对象 | 参数 | 原始主张 | 状态 | 致死证据 | 死因归类 | 后续 | 是否可能复活 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D11 | 计数熵快捷法 | EULER/dpp-entropy-concavity | docs/rejected-and-stalled-routes.md；fd7f3b4a6937f3b601371606bc5095a870aac12f | (b) | 高对比真实sine | 用\|X\|的计数熵替代完整配置Shannon熵。 | 发现缺口后未修 | docs/entropy01.md与review/sources01.json只证明完整配置律和count marginal是不同对象；未给此替换的独立数值反例 | 对象替换错误（计数熵、谱熵、循环模型等） | D23另给count-only得分捷径的精确反例，但不能冒充本条更宽主张的反例。 | 是；当前只有对象错配证据，不是精确反例；不建议继续混用对象 |
| D12 | 谱熵快捷法 | EULER/dpp-entropy-concavity | docs/rejected-and-stalled-routes.md；fd7f3b4a6937f3b601371606bc5095a870aac12f | (a)(b) | 一般有限核与sine Toeplitz | 用Tr b(K)的谱函数替代配置Shannon熵。 | 发现缺口后未修 | docs/entropy01.md对象表与review/claim-ledger.md只区分对象；未定位独立精确反例 | 对象替换错误（计数熵、谱熵、循环模型等） | 完整事件行列式微分继续作为真实对象。 | 是；来源只够判对象替换错误，不够判精确反例；不建议混用 |
| D16 | 循环替换Toeplitz快捷法 | EULER/dpp-entropy-concavity | docs/rejected-and-stalled-routes.md；fd7f3b4a6937f3b601371606bc5095a870aac12f | (c)(b) | 循环/clock近似替换真实Toeplitz | 有限循环neutrality足以直接推出真实sine熵率。 | 发现缺口后未修 | 旧路线账只说明circulant不是Toeplitz真律且clock成本仅到O(n)；未定位直接替换命题的独立精确反例 | 对象替换错误（计数熵、谱熵、循环模型等） | S43/S45/S61显式登记修正律到真实律尚缺的二阶桥。 | 是；若补齐二阶传递误差可形成近似路线，但当前不建议当作捷径 |
| W01 | S67全局Green分配接口 | EULER/rl01 | PR51 8cb6f9b01b0b9b3e7f4ca80cbfef39ab5bfde43c；PR56 e30114f78d922146dcc7aef636289b163e54119a | (b) | 真实posterior；Green预算；全pair汇总 | 在修正局部factor和非交换误差后，Green资源仍足以闭合全局Fisher预算。 | 发现缺口后未修 | D24--D26分别登记已死的factor-one与无误差压缩子主张；剩余全局分配未闭合 | 其他（局部资源与全局汇总接口未闭合） | factor 3/2及Green结构仍是局部工具；没有把精确子反例误记成仅见证失败。 | 是；全局架构未被反例否定，但现有局部账不够；暂不建议继续同一固定分配 |
| G01 | SA01边界响应路线 | EULER/rl01 | PR6；dacf3f363a3f56900a21393ffb402a6bc9ec34fa | (b) | 高对比边界局部导数；小尺寸 | 初始局部导数修复后可提供严格边界推进。 | 发现缺口后未修 | SA01_REPORT/MODEL/HANDOFF；完整SA01未找到覆盖全包的独立审查；strict small-size obstruction仍在 | 有限证书无法传到无限体积 | QWE01继承边界响应接口但未完成符号和全尺寸。 | 是；已有局部数据但缺完整核验与率桥；不建议当成现成定理 |
| G02 | SA03第六阶展开与Gamma | EULER/rl01 | PR2 2497558036180e5151a38b638c16f5168851cc35；PR20 e451887a43886a276afbc4e888a6f9fcf4401399 | (b) | 高对比；目标c=.95 | 统一第六阶展开与Gamma(.95)符号可闭合目标。 | 发现缺口后未修 | PR2冻结结果与research/INDEPENDENT_REVIEW_20260918/README.md：Gamma(.95) sign及general uniform sixth expansion未付 | 常数在 c↑1 退化 | 尾恢复被分离给W02/S68。 | 是；局部展开未被反例否定，但缺统一余项；不建议绕过余项直接宣称 |
| G03 | S42 dyadic有限弦 | EULER/rl01 | PR10 8c1737701e2893a31670d4ece3932489e201c921；PR16 6eb2338ee523c06596ec16c5da5fb4d242322a06 | (b)(e) | n=6,12第一doubling；其余尺度 | dyadic弦与准自由MI尾界可逐尺度支付真实率曲率。 | 发现缺口后未修 | research/INDEPENDENT_REVIEW_20260918/S42.md与S42_CYCLE03.md：只付第一doubling；其余11/12带符号尺度无下界；一项remainder为O非o | 有限证书无法传到无限体积 | S80继承value telescope但仍缺弦长平方。 | 是；首尺度和尾工具有效，但不建议把有限doubling当全尺度 |
| G04 | S43/S45修正律clock桥 | EULER/rl01 | PR9/13/15/18/26；最终审查ed34cb800a749f040f1909bb33accecfc0e67d31 | (c) | clock修正律；c=.95 | O(n)比较成本和负线性W足以给真实输出率符号。 | 发现缺口后未修 | S43/S45审查：clock 499.63115849只是limsup；W+C/n∈[-105.3312,32.08247]不推出>=-4 | 对象替换错误（计数熵、谱熵、循环模型等） | S61闭合一侧W_rel；真实二阶桥仍缺。 | 是；修正律内部结果有效，但不能跳过对象传回；建议只作为辅助账项 |
| G05 | S64 KL长度工具到全付款 | EULER/rl01 | PR46；10b4ba30ae899080581e0c769cbf6a26b8d02c86 | (b) | 固定窗口到全窗口 | KL长度与已修窗口工具应推出actual Fisher>=20.75。 | 发现缺口后未修 | S64_CYCLE11_REVIEW.md：工具限定成立，但两项raw单调性失败且全付款缺失 | 量词顺序错误 | S67尝试Green预算。 | 是；有效工具可继承，但需新的平均次序 |
| G06 | S68尾工具来源恢复后接口 | EULER/rl01 | PR48；9444d8b61c9a86e448e997b1b0403db490a1ced2 | (b) | 联合n/噪声极限；外部率预算 | 来源恢复后的局部尾界可统一传到完整exterior/rate。 | 发现缺口后未修 | research/INDEPENDENT_REVIEW_20260918/S68_CYCLE15.md：joint n/noise uniformity及full exterior/rate budget仍缺 | 有限证书无法传到无限体积 | W02的physical far-tail以martingale/Fatou给出另一条已闭子目标。 | 是；数学工具已核验，缺的是联合极限接口 |
| G07 | S72偶奇条件工具 | EULER/rl01 | PR61；eacef81b976e147c4a7d2e95125aacf0a0de0397 | (b) | 小窗口m=2到大窗口 | 条件G''与偶奇分解应直接给大窗付款。 | 发现缺口后未修 | research/INDEPENDENT_REVIEW_20260918/S72_CYCLE24/S72_CYCLE24_REVIEW.md：m2条件G''可正而总H''仍负 | 量词顺序错误 | S73尝试连续体混合预算。 | 是；分解工具有效，但条件项符号不能单独收费 |
| G08 | S73连续体混合预算 | EULER/rl01 | PR62；110d43d545813342468f29bcd49d4ed31b2788be | (b) | 大窗口；normalization 2m | 连续体极限与混合预算可完成big-window付款。 | 发现缺口后未修 | research/INDEPENDENT_REVIEW_20260920/S73_CYCLE25_REPLAY.md：工具限定成立；big-window continuum payment与mixed budget未闭 | 有限证书无法传到无限体积 | S74另开极端密度局部区。 | 是；接口可用但缺承重符号 |
| G09 | S79 same-unitary exterior | EULER/rl01 | PR69；52a413d9f3036b3b1047f7f00976d352e8297fbf | (b) | same-U层；高秩全尺度exterior | 可见正文与部分尾项足以证明actual same-U exterior paid shell。 | 发现缺口后未修 | research/INDEPENDENT_REVIEW_20260920/S79_CYCLE31/S79_CYCLE31_REPLAY.md：exact K''+J''>=Hhat''与paid shell未完成；m=36,c=.8 hybrid H''>10.4745不是实际对象 | 对象替换错误（计数熵、谱熵、循环模型等） | 继承S78的非交换reveal，但仍须锁定实际same-U对象。 | 是；hybrid反例不杀真实路线，但来源尾部和付款均不足 |
| G10 | S80全尺度value telescope | EULER/rl01 | PR71；b65c0e14171a6ecc5282821c8683c1a514e90442 | (b) | L→∞；缩弦 | R_L^q=O(log L/L)的值误差可直接除以弦面积得到曲率。 | 发现缺口后未修 | research/INDEPENDENT_REVIEW_20260918/S80_CYCLE34/S80_CYCLE34_REVIEW.md：误差缺弦长平方 | 值界缺弦长平方 | quantum telescope本身保留；需真正二阶/有限弦估计。 | 是；value工具有效，但不建议再做无二阶余量的同类极限 |
| G11 | QWE01边界主路线 | EULER/dpp-stationary-entropy + EULER/rl01 | stationary PR122 cf9dd59c9f27170ddb3333cd63410620ae5cd29a；rl01 PR36 6974b50d89c5d349412115c11af3a1e40ce485ba | (b) | 高对比边界；全尺寸目标 | 边界响应与SA01工具可闭合sign、endpoint及all-size payment。 | 发现缺口后未修 | research/INDEPENDENT_REVIEW_20260918/QWE01_CONTINUATION.md：continuation-not-completed | 有限证书无法传到无限体积 | QWE02只闭合有隙大小界。 | 是；不是反例，缺最终符号和端点 |
| G12 | QWE06 folded-count运输 | EULER/dpp-stationary-entropy + EULER/rl01 | stationary PR127 3e09ac84b483addf016b9943dee71c433f52af64；rl01 PR41 da1bbbdc37810e3c8ccc98d2cfcab21c69cb3363 | (c)(b) | fixed window；typical count；大n | folded-count与rare-count response足以传到典型计数和真实输出。 | 发现缺口后未修 | QWE06_CYCLE09.md：reflection ordering、O(n^3)尾步骤、differentiated CLT有缺口；fixed-window目标incomplete | 量词顺序错误 | QWE05/S61闭合删除KL子目标，未闭典型signed full budget。 | 是；部分界可保留，需重做极限次序 |
| G13 | W02真实signed near-field | EULER/dpp-stationary-entropy | PR13；ba48e51efcfc8cccb6055e579bf2a5df970b67f7 | (b) | 固定0<c<1、0<a<1-c、固定rho；重点c≈.95 | 远尾后剩余有限半径near-field aggregate应由现有局部付款闭合。 | 发现缺口后未修 | web_tasks/W02/aggregate/AGGREGATE.md及current-head审查："The true signed near-field total remains unpaid" | 逐项收费过强 | 远尾W02-FAR另由R07登记；下一步必须保留pair/state cancellation。 | 是；未出现原熵命题反例，但不建议复活逐pair好号方案 |

## 修复后被后续路线继承（7）

| 编号 | 名称 | 来源仓库 | 分支或PR | 对象 | 参数 | 原始主张 | 状态 | 致死证据 | 死因归类 | 后续 | 是否可能复活 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R01 | S41 Z0修复 | EULER/rl01 | PR24；43345bd6d3e0c41e197bf2d150c99caaef647aa5 | (b) | 冻结半填充V14局部泛函；N尺度 | Z0修复在受限接口内恢复O_c(sqrt(log N/N))定位。 | 修复后被后续路线继承 | research/INDEPENDENT_REVIEW_20260918/S41_CYCLE05.md：支付244 occurrences、147 terms、33 families | 不适用 | 替代D06旧方向引理；Gamma高c符号仍未得。 | 不适用 |
| R02 | SA02点态预算修复后的限定区 | EULER/rl01 | PR3/PR11 | (b) | rho=1/2；c<=.937限定区 | 避开gamma<2在真实posterior上的失败，以修订边界证书保留中点区。 | 修复后被后续路线继承 | PR3冻结审查与SA02_C37_BOUNDARY.md；同时明确gamma<2 strong pointwise budget fails | 逐项收费过强 | S51继承限定强凹区。 | 不适用 |
| R03 | SA04层熵差与heat修复 | EULER/rl01 | PR4/13/15/26；ed34cb800a749f040f1909bb33accecfc0e67d31 | (c) | clock层；O(n)预算 | 把原<30改为<600并删除错误的delete+positive-heat断言后，留下可用O(n)层工具。 | 修复后被后续路线继承 | PR4冻结审查；S45.md；S43_CYCLE03.md；最终README.md | 其他（原常数和符号断言错误） | S43/S45与S61继承修订版。 | 不适用 |
| R04 | SA05到一侧W_rel子目标 | EULER/rl01 | PR5/7/42/44 | (c) | 指定修正律；n→∞ | 把错误的绝对值sublinear flux改成一侧W_rel>=-o(n)。 | 修复后被后续路线继承 | QWE05_CYCLE09.md；S61_CYCLE10_REVIEW.md | 对象替换错误（计数熵、谱熵、循环模型等） | 删除KL子缺口闭合；完整真实熵凹性未闭。 | 不适用 |
| R05 | S47漏Fisher项修复 | EULER/dpp-stationary-entropy + EULER/rl01 | QWE02源；rl01 PR10/16 | (e) | relative-entropy二阶响应 | 补回漏掉的Fisher/分布移动项后使用expanded formula (5)。 | 修复后被后续路线继承 | research_tasks/external_20260918/QWE02/sources/S47_FORMULA_CORRECTION.md；S42_CYCLE03.md：旧formula (4)在P=Q即错 | 其他（微分公式漏项） | QWE02、QWE08和PR136完整二阶响应继承修订公式。 | 不适用 |
| R06 | QWE05删除KL与S61继承 | EULER/dpp-stationary-entropy + EULER/rl01 | stationary PR126 b57787138c6d20c31a843240b244e64c7958b1fa；rl01 PR42/44 | (c) | 一侧删除；指定半密度模型 | designated deletion-KL gap及一侧W_rel子目标闭合。 | 修复后被后续路线继承 | QWE05_CYCLE09.md；S61_CYCLE10_REVIEW.md | 不适用 | QWE06与真实输出bridge尚缺，不能升级为全目标。 | 不适用 |
| R07 | W02真实physical远尾 | EULER/dpp-stationary-entropy | PR13；ba48e51efcfc8cccb6055e579bf2a5df970b67f7 | (b) | 固定0<c<1、0<a<1-c、固定rho；距离D | 2 sum_{i<j,j-i>D} E\|g_ij(full)\| <= n A_h(1+D)^(-beta)。 | 修复后被后续路线继承 | web_tasks/W02/aggregate/AGGREGATE.md；review 5205135521对应current head；full-posterior Schur行能量+martingale+Fatou | 常数在 c↑1 退化 | 把未决问题缩到真实signed near-field；不直接微分无限MI。 | 不适用 |

## 无结果中止（12）

| 编号 | 名称 | 来源仓库 | 分支或PR | 对象 | 参数 | 原始主张 | 状态 | 致死证据 | 死因归类 | 后续 | 是否可能复活 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| N01 | QWE03操作路线 | EULER/dpp-stationary-entropy | PR124；fd7869e49e7686fbf780f23bb5dcb95cccdb306f；closed-unmerged | (b) | 高对比真实sine | 任务启动但应产生可登记定理、反例或证书。 | 无结果中止 | PR124关闭且无研究交付；r1report §6与rl01来源状态明确为administrative closure | 其他（未收到数学交付） | 无后继数学结果。 | 可重新提出新任务，但没有可继承数学内容；不建议按原壳复活 |
| N02 | QWE04操作路线 | EULER/dpp-stationary-entropy | PR125；60dbd8fe530a423c2b1aa24ce927fe48172a0f25；closed-unmerged | (b) | 高对比真实sine | 任务启动但应产生可登记定理、反例或证书。 | 无结果中止 | PR125关闭且无研究交付；r1report §6与rl01来源状态 | 其他（未收到数学交付） | 无后继数学结果。 | 可重新提出新任务，但没有可继承数学内容；不建议按原壳复活 |
| N03 | S59 Gamma主符号 | EULER/rl01 | PR39 20f7ddcce56a57b68328c9d1f00cb8a368b9b5c4；PR45 aff202e94902289d3993f59139fd2d6d71eb2637 | (b) | 目标Gamma高c符号 | 应给出Gamma主符号的证明或反例。 | 无结果中止 | research/CYCLE11_20260918/S59/S59_CYCLE09_RESULT.md：main Gamma sign INCOMPLETE | 其他（未收到主结果） | 若干工具性约化留存，但没有主定理/反例。 | 可重开不同任务；现文件没有可登记主结果，不建议冒充完成 |
| N04 | S60统一Fisher凸性 | EULER/rl01 | PR39/PR45；aff202e94902289d3993f59139fd2d6d71eb2637 | (e) | 统一Fisher convexity目标 | 应给出通用凸性证明或反例。 | 无结果中止 | research/CYCLE11_20260918/S60/S60_CYCLE09_RESULT.md：main universal Fisher convexity INCOMPLETE | 其他（未收到主结果） | 保留精确约化和小子情形。 | 可换更窄命题重开；不建议按通用主张复活 |
| N05 | S62主benchmark符号 | EULER/rl01 | CYCLE12；SOURCE_STATUS.md | (b) | 高对比冻结benchmark | 应完成最终benchmark sign。 | 无结果中止 | research/CYCLE12_20260919/SOURCE_STATUS.md：preliminary/continuation active后main incomplete；initial reply只有local tools | 其他（未收到主结果） | 局部工具未升级为路线结论。 | 可用局部工具另立窄任务；原主目标无结果 |
| N06 | S65待发送路线 | EULER/rl01 | CYCLE12；SOURCE_STATUS.md | (b) | 未实际进入数学执行 | 计划启动高对比子路线。 | 无结果中止 | research/CYCLE12_20260919/SOURCE_STATUS.md：queued zero sends then held | 其他（未收到数学交付） | 无数学后继。 | 不建议称为可复活方法；它只有排程壳 |
| N07 | S66未使用路线 | EULER/rl01 | CYCLE12；SOURCE_STATUS.md | (b) | 未实际进入数学执行 | 计划启动高对比子路线。 | 无结果中止 | research/CYCLE12_20260919/SOURCE_STATUS.md：unused | 其他（未收到数学交付） | 无数学后继。 | 不建议称为可复活方法；它只有排程壳 |
| N08 | W01高对比机制任务壳 | EULER/dpp-stationary-entropy | PR12；e641d36d858137bd97731452f10d5cd589393603；closed-unmerged | (a)(b) | 3x3 Hermitian正压缩；高对比 | 寻找超过37/40的可核查引理、反例或精确候选不等式。 | 无结果中止 | PR12仅web_tasks/W01.md，无结果文件 | 其他（未收到数学交付） | 后续W02及多条S/QWE路线独立推进。 | 可重新发起研究，但原分支无数学资产；不建议按旧路线名复活 |
| N09 | S3 prompt-only分支 | EULER/dpp-stationary-entropy | PR97；68835780b5734a56ca6fa32ea1b9e4ded05a537f；closed-unmerged | (b) | local-to-global structural route | 任务壳预期收到证明结果。 | 无结果中止 | PR97只有research/s-line-proof-prompts-20260916/S3.md | 其他（未收到数学交付） | 后续其他分支出现S3 scoped bridge，但本PR本身无结果。 | 原壳无需复活；如引用后继，应引用其实际结果分支 |
| N10 | S1 prompt-only分支 | EULER/dpp-stationary-entropy | PR98；886cf857ec4c989d412927cc10fdf982a63daf90；closed-unmerged | (b) | posterior global-compensation route | 任务壳预期收到证明结果。 | 无结果中止 | PR98只有research/s-line-proof-prompts-20260916/S1.md | 其他（未收到数学交付） | 后续结果必须按实际交付PR另记。 | 原壳无需复活 |
| N11 | S2 prompt-only分支 | EULER/dpp-stationary-entropy | PR99；8e2a474edc04f5b13036b5fe6ad5e9e43c80b459；closed-unmerged | (b) | projection-minor posterior route | 任务壳预期收到证明结果。 | 无结果中止 | PR99只有research/s-line-proof-prompts-20260916/S2.md | 其他（未收到数学交付） | 后续结果必须按实际交付PR另记。 | 原壳无需复活 |
| N12 | S7早期近远场任务壳 | EULER/dpp-stationary-entropy | PR96；466f3ef7ceb29aefaed6fc8b5a7799f08c8f1161；closed-unmerged | (b) | signed Fourier posterior averaging | 早期分支应形成近远场数学交付。 | 无结果中止 | PR96仅prompt、workflow及README，无结果证书 | 其他（未收到数学交付） | S7 round3 PR111 7578cac7e0fa9a51472cfedb35065f4fc318ea34另有scoped lemma，应引用后者而非本壳。 | 原壳无需复活；后继已换路线并有独立交付 |

## 来源缺失（0）

无。

## 来源缺失与排除项

已登记的 92 行没有遗留“来源缺失”项；这不等于尚未抽取的子主张数量为零。专门核对过：五个固定骨架页、英文证明源与证书目录、七库来源清单、关闭未合并 PR、`rl01` 的 Cycle09–Cycle34 来源状态和审查文件，以及总览 PDF 引用的 SHA。S77/S79 的“尾部可见性有限”被记为缺口，不伪装成来源完全缺失。

以下不进入路线分母：仅复制任务合同但仍开放、尚未声称数学交付的排程 PR；与对象 (a)–(e) 无关的其他 DPP/FIID/耦合项目；以及同一结果的镜像、整合页和纯导航提交。

## 逻辑隔离

1. “方法被精确反例否定”只否定该行的一句话主张。
2. “只有见证/分配失败”不否定方法架构，更不否定原熵命题。
3. “正面闭合”只在该行参数与对象内成立，局部参数区不得拼接成全区。
4. 本账没有把修正律、计数熵、谱熵、有限循环或 rank-one 核线替换成真实 sine 配置熵率。
