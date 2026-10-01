$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$csvPath = Join-Path $here 'ledger.csv'
$mdPath = Join-Path $here 'ledger.md'
$rows = Import-Csv -LiteralPath $csvPath -Encoding utf8

$statusOrder = @(
  '正面闭合（限定范围）',
  '方法被精确反例否定',
  '只有见证/分配失败（方法本身未被否定）',
  '发现缺口后未修',
  '修复后被后续路线继承',
  '无结果中止',
  '来源缺失'
)

function Escape-Cell([string]$value) {
  if ($null -eq $value) { return '' }
  return (($value -replace '\|', '\|') -replace "`r?`n", '<br>')
}

$lines = [System.Collections.Generic.List[string]]::new()
$lines.Add('# DPP 高对比度熵路线账本')
$lines.Add('')
$lines.Add('快照日期：2026-10-02。公开版统一以 `EULER` 表示来源主体；仓库尾名、PR 号、提交 SHA 和仓库内路径保留。本文只做来源考古和状态记账，不重新判定任何定理真假。')
$lines.Add('')
$lines.Add('## 结论边界')
$lines.Add('')
$lines.Add('- 当前没有登记到“高对比度真实 sine 熵率命题本身被否定”的证据。精确反例否定的是逐项、逐词、点态预算、条件化单调桥或对象替换。')
$lines.Add('- 英文有限核共同移位预算法是完整证明：`papers/stationary-channel/main.tex` 的 §4、§5、§5.3、张量 Bernstein 证书与 §6；文件提交 `16d5d55269eca9725e5eb3f5d0e6ebd785396741`，blob `b391f581fe8f9fbcd5a24f2a7f6de73fcb8884da`。')
$lines.Add('- 高对比度真实 sine 熵率仍是“远尾已付、真实带符号近场未付”。W02 的远尾闭合不等于完整高对比度定理。')
$lines.Add('')
$lines.Add('## 现成骨架页')
$lines.Add('')
$lines.Add('| 总览称呼 | 仓库路径 | 最后改动提交 | blob |')
$lines.Add('|---|---|---|---|')
$lines.Add('| 工具箱固定页 | `docs/methods-toolbox.md` | `fd7f3b4a6937f3b601371606bc5095a870aac12f` | `20cf46a8ac3276659689a5d2535a6cb85713fe02` |')
$lines.Add('| 方法边界原页 | `docs/methodbounds01.md` | `16d5d55269eca9725e5eb3f5d0e6ebd785396741` | `46642527dd9b65e8e4cfd8ba76fa7e02cc4c4a5e` |')
$lines.Add('| 旧路线账 | `docs/rejected-and-stalled-routes.md` | `fd7f3b4a6937f3b601371606bc5095a870aac12f` | `92e3233d1e174c6268c085b4a2a13b884d00e86c` |')
$lines.Add('| 熵参数地图 | `docs/entropy01.md` | `16d5d55269eca9725e5eb3f5d0e6ebd785396741` | `d6d92a8842caf4349b44b4a47137e6776f022d66` |')
$lines.Add('| 完整错误链与来源 | `review/sources01.json` | `5128965453df9f4ea4a9ddce85eedaea7bd05f76` | `cc8f8e7a9434aa18a7e81cd554a6b822125bcc20` |')
$lines.Add('')
$lines.Add('以上五页均位于 `EULER/dpp-entropy-concavity` 的集成树；账本再用原仓库 PR head 和仓库内审查文件回填。')
$lines.Add('')
$lines.Add('## 七库覆盖')
$lines.Add('')
$lines.Add('| 仓库 | 分支 | PR | open PR | closed-unmerged PR | ordinary issue |')
$lines.Add('|---|---:|---:|---:|---:|---:|')
$lines.Add('| `EULER/dpp-entropy-concavity` | 8 | 7 | 4 | 0 | 1 |')
$lines.Add('| `EULER/dpp-stationary-entropy` | 118 | 117 | 16 | 16 | 14 |')
$lines.Add('| `EULER/dpp-entropy-tools` | 128 | 111 | 3 | 4 | 36 |')
$lines.Add('| `EULER/rl01` | 96 | 95 | 54 | 2 | 0 |')
$lines.Add('| `EULER/icm-conjecture-results` | 22 | 21 | 21 | 0 | 2 |')
$lines.Add('| `EULER/icm-conjecture-lab` | 95 | 89 | 84 | 2 | 12 |')
$lines.Add('| `EULER/i05-private-exploration` | 45 | 58 | 13 | 7 | 35 |')
$lines.Add('| **合计** | **512** | **498** | **195** | **31** | **100** |')
$lines.Add('')
$lines.Add('覆盖包含所有分支、全部 PR 状态、ordinary issue、PR 文件树及已存审查文件。2026-09-29 之后新增的分支/PR逐项按标题、正文和文件树筛查；新增项属于其他 DPP、耦合或 FIID 问题，没有发现新的本账对象 (a)–(e) 结果。任务合同、提示词壳和纯排程页不作为数学结果；其中已经关闭且确无交付者列入“无结果中止”。')
$lines.Add('')
$lines.Add('对象：`(a)` 有限核共同移位；`(b)` 真实平稳 sine 熵率；`(c)` 修正律/循环模型；`(d)` 固定物理符号路径；`(e)` MI 方向变体。')
$lines.Add('')

$columns = @('编号','名称','来源仓库','分支或PR','对象','参数','原始主张','状态','致死证据','死因归类','后续','是否可能复活')
foreach ($status in $statusOrder) {
  $subset = @($rows | Where-Object { $_.状态 -eq $status })
  $lines.Add("## $status（$($subset.Count)）")
  $lines.Add('')
  if ($subset.Count -eq 0) {
    $lines.Add('无。')
    $lines.Add('')
    continue
  }
  $lines.Add('| ' + ($columns -join ' | ') + ' |')
  $lines.Add('|' + (($columns | ForEach-Object {'---'}) -join '|') + '|')
  foreach ($row in $subset) {
    $cells = foreach ($column in $columns) { Escape-Cell ([string]$row.$column) }
    $lines.Add('| ' + ($cells -join ' | ') + ' |')
  }
  $lines.Add('')
}

$lines.Add('## 来源缺失与排除项')
$lines.Add('')
$lines.Add('本轮所列种子没有遗留“来源缺失”项。专门核对过：五个固定骨架页、英文证明源与证书目录、七库全部分支/PR/issue、关闭未合并 PR、`rl01` 的 Cycle09–Cycle34 来源状态和审查文件，以及总览 PDF 引用的 SHA。S77/S79 的“尾部可见性有限”被记为缺口，不伪装成来源完全缺失。')
$lines.Add('')
$lines.Add('以下不进入路线分母：仅复制任务合同但仍开放、尚未声称数学交付的排程 PR；与对象 (a)–(e) 无关的其他 DPP/FIID/耦合项目；以及同一结果的镜像、整合页和纯导航提交。')
$lines.Add('')
$lines.Add('## 逻辑隔离')
$lines.Add('')
$lines.Add('1. “方法被精确反例否定”只否定该行的一句话主张。')
$lines.Add('2. “只有见证/分配失败”不否定方法架构，更不否定原熵命题。')
$lines.Add('3. “正面闭合”只在该行参数与对象内成立，局部参数区不得拼接成全区。')
$lines.Add('4. 本账没有把修正律、计数熵、谱熵、有限循环或 rank-one 核线替换成真实 sine 配置熵率。')

[System.IO.File]::WriteAllLines($mdPath, $lines, [System.Text.UTF8Encoding]::new($false))
Write-Output "Wrote $mdPath with $($rows.Count) route rows."
