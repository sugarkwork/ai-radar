---
name: "AgentFlux"
genre: "agent-framework"
url: "https://github.com/davemessew/AgentFlux"
repo: "davemessew/AgentFlux"
flags: ["unverified"]
risk_notes: "READMEによるとログイン機能はなく、単一ユーザー向けです。共有または公開アクセスにはアクセス制御層と適切なネットワーク設定が必要です。"
stars: 182
forks: 4
open_issues: 1
size_kb: 1324
language: "TypeScript"
created: "2026-10-27"
updated: "2026-10-30"
archived: false
license: "Apache-2.0"
commits_30d: 5
commits_90d: 16
commit_cadence: "weekly"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/AIExplorerTim/status/2118910064606233060"]
fetched_at: "2026-11-15T00:18:25.064256+00:00"
---

# AgentFlux

## 出来ること

- 文書・データソース・言語モデルを視覚的なワークフローで接続し、タスク説明からエージェントにワークフローを作成させられます。READMEは、事前設定済みの17ステップと8テンプレート、分岐、動画解析によるワークフロー生成、ローカル文書の検索、Ollama・LM Studio・vLLM・OpenAI互換エンドポイントへの接続、JSON・CSV・Markdownレポートの出力を説明しています。出典: https://github.com/davemessew/AgentFlux

## 目的・背景

- READMEでは、自分のデータ・モデル・ワークフローを使うエージェント型AIプラットフォームとして説明されています。アプリはコンピューターまたはサーバー上で動作し、ブラウザーから操作します。出典: https://github.com/davemessew/AgentFlux

## 依存関係

- Docker版の利用にはDocker Composeが必要です。エージェントや動画解析には、利用者が接続する言語モデルまたは画像対応モデルが必要です。READMEによると、DockerリリースにはFFmpegとWhisper baseを使うローカル音声サービスが含まれます。出典: https://github.com/davemessew/AgentFlux

## 実行条件

- README記載のv0.3.0事前ビルド版はLinux/amd64向けです。WindowsではDocker DesktopのLinuxコンテナモードを使う手順が示されています。他アーキテクチャはソースからビルドできますが、このリリースでは未テストと記載されています。既定の設定はポート4310をlocalhostにバインドします。出典: https://github.com/davemessew/AgentFlux

## 最短手順

- READMEは、同じフォルダーにリリースv0.3.0のDockerイメージアーカイブとcompose.yamlを用意し、DockerでイメージをロードしてComposeを起動する手順を示しています。起動後はlocalhost:4310を開きます。ソースからのビルド手順とDockerを使わないインストール手順もREADMEに案内されています。出典: https://github.com/davemessew/AgentFlux

## 変更履歴

- 2026-11-15: 初回登録
