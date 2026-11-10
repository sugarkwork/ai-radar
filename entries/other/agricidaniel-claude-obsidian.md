---
repo: "AgriciDaniel/claude-obsidian"
name: "claude-obsidian"
genre: "other"
url: "https://github.com/AgriciDaniel/claude-obsidian"
license: "MIT"
stars: 16310
forks: 1598
open_issues: 25
size_kb: 38035
language: "Python"
created: "2026-04-07"
updated: "2026-10-25"
archived: false
commits_30d: 69
commits_90d: 100
commit_cadence: "daily"
last_release: "v3.0.1"
flags: ["unverified"]
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
risk_notes: ""
sources: ["https://x.com/Bober_smart/status/2117619229465641097"]
fetched_at: "2026-11-10T10:01:55+00:00"
---

# claude-obsidian｜Claude Code で出典付きの Obsidian Wiki を育てる

## 出来ること

- inbox/ に置いた資料の原本を保持し、出典をたどれるリンク付き Markdown ノートを作る。Wiki を読み取り専用で照会し、回答を必要に応じて保存できる。リンク切れや孤立ページも点検できる。

## 目的・背景

- Karpathy の LLM Wiki パターンをもとに、取り込んだ資料と生成ノートを同じ保管庫に蓄積し、後から出典をたどれるようにする。

## 依存関係

- Claude Code プラグイン経由では Claude Code と Python 3.11 以降を使用する。Obsidian はグラフなどの視覚表示に任意。別の Agent Skills 対応ホスト向けのセットアップには Bash を使う。

## 実行条件

- 作者の案内では、Windows で保管庫に書き込む場合は WSL を使用し、ネイティブ Windows では読み取りとプレビューが可能。PDF・EPUB の本文抽出は内蔵せず、Web ページの取得には別途ランナーが必要。
- プラグインは MIT ライセンスで、作者はプラグイン自体の購読料は不要と案内している。AI ホストの利用条件は別途適用される。README によると、Claude Code が読むノートは Anthropic のモデルに送られる。

## 最短手順

- 公式導入ガイドの Claude Code marketplace 手順で AgriciDaniel/claude-obsidian を追加し、プラグインをインストールする。[導入ガイド](https://github.com/AgriciDaniel/claude-obsidian/blob/main/docs/install-guide.md)
- 対象フォルダーで Claude Code を起動し、入力欄から /claude-obsidian:wiki を呼び出して初期化プレビューを確認する。inbox/ に資料を置き、/claude-obsidian:wiki-ingest で取り込み、/claude-obsidian:wiki-query で質問する。[README](https://github.com/AgriciDaniel/claude-obsidian/blob/main/README.md#install)

## 変更履歴

- 2026-11-10: 初回登録
