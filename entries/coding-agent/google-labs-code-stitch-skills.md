---
name: "Stitch Design Skills"
genre: "coding-agent"
url: "https://github.com/google-labs-code/stitch-skills"
repo: "google-labs-code/stitch-skills"
license: "Apache-2.0"
stars: 10093
language: "TypeScript"
created: "2026-01-16"
updated: "2026-08-17"
forks: 1328
open_issues: 21
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 248
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 実行条件。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/TheArthiAI/status/2122838487741436387"]
fetched_at: "2026-11-18T00:24:52.717005+00:00"
---

# Stitch Design Skills

## 出来ること

- Google Stitch向けのスキルとプラグインを提供する。READMEでは、デザイン生成・編集、デザインシステム管理、フロントエンドコードからの変換、React/React Native向けコンポーネント生成、プロンプト改善などの用途を案内している。

## 目的・背景

- Google Stitchの設計・構築ワークフローを、Agent Skills標準に沿ったスキルや各エージェント向けプラグインとして利用するためのリポジトリ。

## 依存関係

- READMEによると、スキルの利用にはエージェント環境でStitch MCPサーバーを設定・起動し、セットアップ手順に従って環境変数と認証情報を用意する必要がある。選択的にスキルを導入する場合、スキル間の依存関係にも注意が必要とされている。

## 実行条件

- Codex、Antigravity、Gemini CLI、Claude Code、Cursor、OpenCodeとの互換性をREADMEが案内している。OpenCodeではスキルとStitch MCPを手動設定し、スキル名のfrontmatterが小文字のkebab-caseでディレクトリ名と一致する必要があると記載されている。

## 最短手順

- CodexではREADME記載の`codex plugin marketplace add google-labs-code/stitch-skills --ref main`に、必要に応じて`--sparse`パスを付けてマーケットプレイスを追加し、`stitch-design`、`stitch-build`、`stitch-utilities`から必要なプラグインを導入する。利用前にStitch MCPを設定する。

## 変更履歴

- 2026-11-22: 初回登録
