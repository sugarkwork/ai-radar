---
repo: "nidhinjs/prompt-master"
name: "prompt-master"
genre: prompt-design
url: "https://github.com/nidhinjs/prompt-master"
license: "MIT"
stars: 15469
language: "未確認"
created: "2026-03-11"
updated: 2026-10-22
added: "2026-11-03"
first_seen: "2026-11-03"
sources: ["https://x.com/dopamine_crypto/status/2119199466565824535?a=JCNAhMHI75BTvYNW4Vc&s=46", "https://x.com/dopamine_crypto/status/2119199466565824535", "https://github.com/nidhinjs/prompt-master", "https://raw.githubusercontent.com/nidhinjs/prompt-master/main/README.md"]
flags: ["unverified"]
risk_notes: "今回の投稿は機能紹介で新たな実行試験ではない。 今回の動作・推論・生成・性能は未検証。"
forks: 1791
open_issues: 30
commits_30d: 7
commit_cadence: weekly
size_kb: 170
archived: false
commits_90d: 13
fetched_at: "2026-11-03T23:05:35Z"
type: "repo"
author: "nidhinjs"
source_post: "https://x.com/dopamine_crypto/status/2119199466565824535"
amplifiers: []
---

# prompt-master

## 出来ること

- Claude のスキルとして動き、「どの AI ツール向けのプロンプトか」を判定したうえで、その道具に合った形式のプロンプトを1つ返す。
- 手順が固定されている: 対象ツール判定 → 意図の9項目抽出（タスク・入力・出力・制約・文脈・読み手・記憶・成功条件・例）→ 不足があれば最大3問だけ確認 → フレームワーク選択 → トークン効率の監査 → コピー可能なブロックとして出力。
- 「最新モデルに依存する依頼」では、公式ドキュメントでモデル名やパラメータを確認する手順を含む。
- 既存の雑なプロンプトを渡して改修させる、他ツール向けに移植する、といった使い方も想定。
- 対応先として Claude / ChatGPT / Codex / Gemini / Cursor / Copilot / Midjourney / SD / ComfyUI / Sora / ElevenLabs などを列挙。

## 目的・背景

「プロンプト生成器は往々にして長くするだけ」という問題意識から、語を削って狙いを鋭くする方向を掲げるスキル。成果物はプロンプト本文で、実行は元のツール側で行う。

## 依存関係

- 追加のランタイム依存なし（Markdown のスキル本体のみ、リポジトリは約 170KB）。
- claude.ai の Skills、または Claude Code の `~/.claude/skills`。

## 実行条件

- 実行先は Claude 系のスキル機構。README に並ぶ他ツール名は「生成対象」であって実行先ではない。
- ブラウザ版はリポジトリを ZIP で落として claude.ai → Customize → Skills → Upload a Skill。Claude Code へは clone して配置（README では「推奨しない」と注記）。
- スキル本文の品質評価は未実施。効果（トークン削減量など）を数値で示す一次データはリポジトリに無い。

## 最短手順

```bash
git clone https://github.com/nidhinjs/prompt-master.git ~/.claude/skills/prompt-master
# もしくは ZIP をダウンロードして claude.ai の Skills にアップロード
```

## 変更履歴

- 2026-11-03: 初回登録（★15,469 / pushed 2026-10-22 / MIT）

## 追加出典・確認範囲（2026-11-09）

対象ツールを判定し、意図を9項目に分け最大3問の確認から短い指示を作るClaude向けprompt-master skill。

各生成サービスを直接呼ぶ実装ではない。添付はGitHubカードで別の原文指示はない。

今回の投稿は機能紹介で新たな実行試験ではない。

対象固有の機能・制約の説明は2026-11-08（原記録）のチェック記録を基にしている。メタ情報は2026-11-09T00:31:29.818839+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

### 今回取得した公式メタ情報

既存フロントマターの過去値は維持し、今回の取得値を下に併記する。どちらも実行・性能の追試ではない。

| 項目 | 値 |
|---|---|
| repo | nidhinjs/prompt-master |
| url | https://github.com/nidhinjs/prompt-master |
| license | MIT |
| language | unknown |
| created | 2026-03-11 |
| updated | 2026-10-22 |
| stars | 15725 |
| forks | 1814 |
| open_issues | 30 |
| commits_30d | 7 |
| commits_90d | 13 |
| commit_cadence | weekly |
| size_kb | 170 |
| archived | False |
| fetched_at | 2026-11-09T00:31:29.818839+00:00 |


- @dopamine_crypto: https://x.com/dopamine_crypto/status/2119199466565824535
- 対象資料: https://github.com/nidhinjs/prompt-master
- 参照: https://raw.githubusercontent.com/nidhinjs/prompt-master/main/README.md

- 2026-11-09: 関連出典と確認範囲を追記。既存の記述・過去の数値・原文プロンプトは維持。今回の実行確認なし。
