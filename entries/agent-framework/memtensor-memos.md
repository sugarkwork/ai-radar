---
name: "MemOS 2.0 Stardust（星尘）"
genre: "agent-framework"
url: "https://github.com/MemTensor/MemOS"
repo: "MemTensor/MemOS"
license: "Apache-2.0"
stars: 12457
language: "TypeScript"
created: "2025-07-06"
updated: "2026-11-20"
forks: 1132
open_issues: 143
commits_30d: 35
commit_cadence: "daily"
commits_90d: 100
size_kb: 75284
archived: false
flags: ["unverified"]
risk_notes: "README内のCloud APIサンプルは一部が伏字・破損しており、そのまま実行できる状態ではありません。セルフホスト手順ではAPIキーの設定が必要とされています。ベンチマーク値や効果はREADMEでのプロジェクト側の報告であり、独立検証としては確認していません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/rosemoni18/status/2119211334797840872"]
fetched_at: "2026-11-20T03:11:16.888925+00:00"
---

# MemOS 2.0 Stardust（星尘）

## 出来ること

- LLM・AIエージェント向けの長期記憶を管理するシステムです。READMEでは、単一APIによる記憶の追加・検索・編集・削除、テキスト・画像・ツール履歴・ペルソナの統合記憶、複数の知識ベース管理、非同期取り込み、自然言語での記憶修正を機能として挙げています。Cloud API、セルフホスト、MemOS Cloud Plugin、ローカルプラグインの利用経路も案内されています。

## 目的・背景

- AIエージェントに長期記憶を持たせ、過去の文脈や利用者の好みに応じた対話、問い合わせ履歴の参照、複数エージェント間の記憶共有・分離に使うことを想定しています。

## 依存関係

- セルフホストのDocker手順はMemOS API、Neo4j、Qdrantを起動します。READMEの構成表ではセルフホストにNeo4jとQdrantが必要とされています。Cloud APIはホスト型、ローカルプラグインはSQLiteを利用する構成として記載されています。

## 実行条件

- 選択する利用経路によって条件が異なります。Cloud APIはAPIキーを取得して利用します。セルフホストはDocker Composeを使う手順が示され、環境変数ファイルにAPIキーを設定するよう案内されています。ローカルプラグインの表記上のセットアップはnpm installとエージェント別設定です。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- セルフホストの場合、READMEのDocker手順はリポジトリをcloneし、docker/.env.exampleを.envへコピーして必要なAPIキーを設定し、dockerディレクトリでdocker compose upを実行する流れです。Cloud APIの場合はダッシュボードでAPIキーを取得し、APIに対して記憶の追加・検索リクエストを送る例が掲載されています。READMEに含まれるCloud APIコード例は伏字・破損箇所があるため、掲載テキストだけではそのまま実行できません。

## 変更履歴

- 2026-11-23: 初回登録
