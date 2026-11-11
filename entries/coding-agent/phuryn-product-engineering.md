---
name: "Product Engineering"
genre: "coding-agent"
url: "https://github.com/phuryn/product-engineering"
repo: "phuryn/product-engineering"
stars: 455
forks: 59
open_issues: 0
size_kb: 5866
language: "Python"
created: "2026-10-29"
updated: "2026-11-08"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/TiagerBao/status/2120107853809856738"]
fetched_at: "2026-11-10T23:11:38.679328+00:00"
---

# Product Engineering

## 出来ること

- コーディングエージェントを使い、最初のアイデアから実ユーザー向けの製品開発、リリース、運用まで進めるためのエージェントスキルを提供する。READMEではClaude Code、Codex、Cursor、Gemini CLI、OpenCode、GitHub Copilotなどで利用できると説明されている。

## 目的・背景

- 製品を作る人が、何を作るかの判断や製品の確認を担いながら、コーディングエージェントを使って製品を出荷するためのスキル集。複数エージェントの調整にも対応する。

## 依存関係

- README記載の導入方法は、Claude Codeのプラグイン機能、Codexのプラグイン機能、またはNode.js 22.20以降で動くnpx skills。スキルフォルダーをエージェントが読む場所へ手動コピーする方法も記載されている。

## 実行条件

- 利用するエージェントに応じて導入方法が異なる。Codexではプラグイン導入後に新しいセッションを開始する手順が示されている。npx skillsを使う場合、READMEはNode.js 22.20以降を必要条件としている。

## 最短手順

- READMEでは、対象プロジェクトのフォルダーでエージェントに「Please install skills from phuryn/product-engineering on GitHub in this project only. Enable auto updates.」と依頼する方法を最短手順として案内している。導入後は`/product:start-here`（Codexでは`$product:start-here`）を開始し、現在の状況を伝える。

## 変更履歴

- 2026-11-11: 初回登録
