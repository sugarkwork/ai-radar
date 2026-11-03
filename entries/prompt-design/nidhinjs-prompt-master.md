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
sources: []
flags: []
risk_notes: ""
forks: 1791
open_issues: 30
commits_30d: 7
commit_cadence: weekly
size_kb: 170
archived: false
commits_90d: 13
fetched_at: "2026-11-03T23:05:35Z"
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
