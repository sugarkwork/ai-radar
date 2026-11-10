---
repo: "anthropics/claude-code"
name: "Claude Code"
genre: "coding-agent"
url: "https://github.com/anthropics/claude-code"
stars: 155135
forks: 24886
open_issues: 16966
size_kb: 34723
language: "TypeScript"
created: "2025-02-22"
updated: "2026-11-10"
archived: false
license: "unknown"
commits_30d: 54
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "投稿のClaude Opus 5.5の使用、2.5D制作工程の一貫実行、完成動画の品質、費用ゼロの主張は未確認。CLIやMCPは公式文書で確認し、動作と効果の独立実測は行っていない。最新リリースと再配布条件の詳細は未確認。90日コミット数の100は集計上限で、100件以上を示す。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Y0urDumble/status/2117030430507401326"]
fetched_at: "2026-11-10T08:15:51+00:00"
---

# Claude Code — CLIとMCPで使えるコーディングエージェント

## 出来ること

- 端末から自然言語でコードの説明、定型作業、Gitワークフローを依頼できる。設定済みのMCPサーバーを通じて外部ツールやデータソースも利用できる。

## 目的・背景

- 既存のコードベースを対象に作業するAnthropicのコーディングエージェント。非対話CLIを備え、別のAIエージェントやスクリプトからも呼び出せる。投稿の動画制作工程は、この候補で検証した機能の範囲外。

## 依存関係

- 公式セットアップに従ってCLIを導入する。Gitはオプション。外部ツール連携には対象のMCPサーバーと、接続先に応じた認証が必要。

## 実行条件

- 公式セットアップでは対応するmacOS、Windows、Linux環境、4 GB以上のRAM、x64またはARM64、インターネット接続を案内している。非対話実行にも認証が必要。利用料金は認証先のプランや契約条件を確認する。READMEには商用利用規約への案内があり、GitHub APIのライセンス値はunknown。

## 最短手順

- 公式セットアップでCLIを導入し、認証済み環境の作業ディレクトリで `claude` を起動する。最初は『このプロジェクトの構成を説明して』など、読み取り中心の依頼で試せる。
- 別のAIエージェントから呼ぶ場合は、そのシェル実行ツールで認証済み環境の `claude -p 'このプロジェクトの構成を説明して'` を起動し、標準出力を受け取る。Claude Codeから外部ツールを呼ぶ場合は、公式MCPガイドに沿って対象サーバーを `claude mcp add` で登録し、対話セッションでそのツールを使うよう依頼する。

## 変更履歴

- 2026-11-10: 初回登録
