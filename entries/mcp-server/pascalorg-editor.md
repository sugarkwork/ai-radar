---
name: "Pascal Editor"
genre: "mcp-server"
url: "https://github.com/pascalorg/editor"
repo: "pascalorg/editor"
license: "MIT"
stars: 25556
language: "TypeScript"
created: "2025-10-16"
updated: "2026-11-14"
forks: 3177
open_issues: 57
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 192437
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/awe0_io/status/2119016448001728685"]
fetched_at: "2026-11-16T21:55:06Z"
last_release: "@pascal-app/cli@1.1.4"
last_release_at: "2026-11-12"
---

# Pascal Editor

## 出来ること

- READMEによると、Pascal Editorはブラウザー上で3D建物モデルを作成・編集するツールです。サイト、建物、階、壁、床、屋根、開口部、部屋、家具を扱い、3Dスキャンを参照レイヤーとして取り込んで、その上に編集可能な建築要素をモデル化できます。MCPサーバーを通じてエージェントがシーンを読み取り、編集、検証、保存できます。

## 目的・背景

- 建築・エンジニアリング・建設・運用（AECO）向けのローカル優先型エディターとして説明されています。React Three FiberとWebGPUで構築されています。

## 依存関係

- ローカルCLIの利用条件として、Node.js 22.23.4以降（22系）、24.22.1以降（24系）、または26.12.1以降が記載されています。CLIは `npm install --global @pascal-app/cli` でインストールできます。

## 実行条件

- ローカルではCLIがMCPサービスを起動し、プロジェクトを `~/.pascal/data/pascal.db` に保存します。READMEは、ローカルサービスでは同時に有効なエージェントクライアントを1つにするよう案内しています。ホスト型ワークスペースはPascalアカウントの認証が必要で、一部操作はPascal creditsを消費すると記載されています。

## 最短手順

- README記載のローカル起動手順は `npx @pascal-app/cli editor` です。MCP接続には `pascal mcp setup codex` などのクライアント別設定手順があります。これらは資料に記載された手順であり、この精査では実行していません。

## 変更履歴

- 2026-11-16: 初回登録
