---
name: "FrontAgent"
genre: "coding-agent"
url: "https://github.com/ceilf6/FrontAgent"
repo: "ceilf6/FrontAgent"
license: "MIT"
stars: 125
language: "TypeScript"
created: "2025-12-16"
updated: "2026-11-18"
forks: 19
open_issues: 10
commits_30d: 13
commit_cadence: "weekly"
commits_90d: 13
size_kb: 52799
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 依存関係。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/RealMarvelX/status/2119259433029033988"]
fetched_at: "2026-11-18T07:14:38.713876+00:00"
---

# FrontAgent

## 出来ること

- フロントエンド向けAIコーディングエージェント。CLI、VS Code拡張、デスクトップアプリ、stdio MCPサーバーを提供し、ReactやTypeScriptなどのWeb UIコード生成・リファクタリング、リポジトリ検索、ブラウザーを使った検証を支援するとREADMEは説明している。

## 目的・背景

- READMEは、仕様駆動開発（SDD）を制約として計画と実行を分け、パスの幻覚を抑えるリポジトリ情報や、明示的な安全制御を備えたフロントエンド開発エージェントと説明している。記載された効果は作者の説明であり、独立検証はしていない。

## 依存関係

- READMEで確認できた要件はNode.js 20以上。

## 実行条件

- CLIはnpm、pnpm、yarnでグローバルインストールできる。LLMのプロバイダー、モデル、接続先、APIキーを環境変数で設定する手順がREADMEにある。VS Code拡張はVS Code 1.120以上。

## 最短手順

- README記載のCLI手順: `npm install -g frontagent` でインストールし、利用するLLMの `PROVIDER`、`BASE_URL`、`MODEL`、`API_KEY` を設定して、対象プロジェクトのディレクトリで `fa init` などのCLIコマンドを使う。

## 変更履歴

- 2026-11-23: 初回登録
