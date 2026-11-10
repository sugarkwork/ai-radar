---
name: "obsidian-second-brain"
genre: "coding-agent"
url: "https://github.com/eugeniughelbur/obsidian-second-brain"
flags: ["unverified"]
risk_notes: "README に基づく文書確認。最新版リリース、実環境での導入・各 CLI の動作、検索精度、外部サービスの料金は未確認。"
repo: "eugeniughelbur/obsidian-second-brain"
stars: 5252
forks: 643
open_issues: 8
size_kb: 26749
language: "Python"
created: "2026-03-24"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Bober_smart/status/2117619229465641097"]
fetched_at: "2026-11-10T10:02:48+00:00"
---

# obsidian-second-brain — Obsidian のノートを AI エージェントの継続メモリに

## 出来ること

- 会話からノートを保存し、保管庫の記録を検索して後続セッションで参照できる。README には検索品質を recall@k と MRR で測る評価コマンドも記載されている。

## 目的・背景

- セッションごとに説明し直す手間を減らすため、知識を保管庫内の Markdown に残す。初期化コマンドは保管庫の案内、索引、ログを生成する。

## 依存関係

- Claude Code などの対応ホストと対象の保管庫を用意する。README は Git と Python 補助機能用の uv を前提として挙げる。従来のスクリプト導入には jq が必要で、ローカル意味検索向けの Ollama は任意。

## 実行条件

- Claude Code のプラグイン方式では OBSIDIAN_VAULT_PATH で対象を指定する。README によると基本の保管庫コマンドに API キーは不要。リポジトリは MIT ライセンス。

## 最短手順

- Claude Code 内で `/plugin marketplace add eugeniughelbur/obsidian-second-brain`、続けて `/plugin install obsidian-second-brain@obsidian-second-brain` を入力する。
- `~/.claude/settings.json` の `env` に `OBSIDIAN_VAULT_PATH` を設定して Claude Code を再起動する。保管庫内で `/obsidian-second-brain:obsidian-init` を呼び、会話からの保存には `/obsidian-second-brain:obsidian-save`、検索には `/obsidian-second-brain:obsidian-find` を使う。

## 変更履歴

- 2026-11-10: 初回登録
