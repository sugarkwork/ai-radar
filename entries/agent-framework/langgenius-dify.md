---
name: "Dify"
genre: "agent-framework"
url: "https://github.com/langgenius/dify"
repo: "langgenius/dify"
license: "unknown"
language: "Python"
created: "2023-04-12"
updated: "2026-11-16"
archived: false
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "ライセンスは取得データ上unknown。Docker、Docker Compose v2.35.0以降、OpenSSLが必要。最低要件はCPU 2コア、RAM 4 GiB。README記載以外の効果や依存条件は未確認。 GitHub APIでライセンスを確認できていません。"
stars: 161287
forks: 25516
open_issues: 1402
size_kb: 715885
commits_30d: 100
commits_90d: 100
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2118043980420030914"]
fetched_at: "2026-11-16T21:38:56Z"
last_release: "1.19.0"
last_release_at: "2026-11-04"
---

# Dify

## 出来ること

- AIワークフローの構築・テスト、複数の推論プロバイダーやセルフホスト環境のモデル連携、プロンプト作成とモデル比較、文書取り込みから検索までのRAG、サンドボックス内でコマンド実行やファイル操作を行うエージェントを提供する。

## 目的・背景

- プロトタイプから本番環境まで進められる、オープンソースのLLMアプリ開発プラットフォームとして説明されている。

## 依存関係

- READMEのDocker Compose手順では、稼働中のDockerデーモン、Docker Compose v2.35.0以降、OpenSSLが必要。

## 実行条件

- 最低要件はCPU 2コア以上、RAM 4 GiB以上。

## 最短手順

- リポジトリのdockerディレクトリで.env.exampleを.envにコピーし、openssl rand -hex 32で生成した値を.envのDIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKENに設定する。docker compose up -dで起動し、docker compose ps --allで状態を確認する。

## 変更履歴

- 2026-11-11: 初回登録
