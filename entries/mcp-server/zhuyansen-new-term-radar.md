---
repo: "zhuyansen/new-term-radar"
name: "New Term Radar"
genre: "mcp-server"
url: "https://github.com/zhuyansen/new-term-radar"
flags: ["unverified"]
stars: 2147
forks: 642
open_issues: 3
size_kb: 4649
language: "Python"
created: "2026-10-12"
updated: "2026-11-02"
archived: false
license: "MIT"
commits_30d: 54
commits_90d: 54
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
risk_notes: ""
sources: ["https://x.com/GoSailGlobal/status/2117474999221285252"]
fetched_at: "2026-11-10T09:08:23Z"
---

# New Term Radar — AIの新語を追跡して検索語候補を調べるCLI・MCP

## 出来ること

- X、Hugging Face、GitHub、サイトマップから新しい名称の候補を集め、検索語候補を含むレポートを生成する。MCPでは保存済み候補の参照、指定した名称の検索語調査、収集処理の起動ができる。

## 目的・背景

- 保存したスナップショットと比較し、既存のキーワードツールに載る前の名称を調査候補として拾う設計。READMEには著者の実行例があり、初回は比較用データを作るため、前回との差分を使うシグナルは次回以降に揃う。

## 依存関係

- CLIはPython 3.10以上で動作し、パッケージの基本依存は空。MCPには追加でMCP SDKが必要。Xや検索量などの外部データとモデルにはAIsaを使用し、GoAnyAPIは追加の関連検索語などを取得するための任意設定。

## 実行条件

- コードはMIT。外部APIには別途利用条件と従量費用があり、料金は使用する情報源、モデル、頻度に依存する。MCPの公開設定ではAISA_API_KEYが必須。状態を継続利用する場合は同じ状態ディレクトリを指定する。

## 最短手順

- CLIではuvを用意し、AISA_API_KEYをローカル環境に設定して `uvx new-term-radar daily --out report.md` を実行する。追跡先を変更する場合は `config.example.json` を `config.json` にコピーして編集し、次回も同じ状態を使う。
- AIからは、Claude CodeなどのMCPクライアントにstdioサーバー `uvx --with mcp new-term-radar mcp` を登録する。環境にAISA_API_KEYを渡し、既存の収集結果を参照する場合はRADAR_STATEにその保存先を指定して、エージェントに `recent_leads` で候補を取得するよう依頼する。指定語を調査する `keyword_table` や収集を起動する `run_radar` では費用が発生し得る。

## 変更履歴

- 2026-11-10: 初回登録
