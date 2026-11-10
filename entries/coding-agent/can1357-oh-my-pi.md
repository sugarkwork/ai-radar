---
repo: "can1357/oh-my-pi"
name: "oh-my-pi"
genre: "coding-agent"
url: "https://github.com/can1357/oh-my-pi"
stars: 38506
forks: 4380
open_issues: 4675
size_kb: 798069
language: "TypeScript"
created: "2025-12-31"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "インストール、モデル接続、LSP連携は未実行。開発元が掲載した編集性能の比較値は、測定条件と再現性を未確認。最新リリースのタグと公開日時、各モデル提供元の料金と利用条件は未確認。コミット件数の100は集計上限で、各期間100件以上を示す。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/opensourcelab9/status/2114967848775041508"]
fetched_at: "2026-11-10T11:46:58Z"
---

# oh-my-pi — LSPを統合した端末向けAIコーディングエージェント

## 出来ること

- 端末で対話しながらコードを編集できる。開発元は、ファイル名の変更時にLSPの workspace/willRenameFiles を使い、移動前にインポートや再エクスポートを更新する例を示している。
- 単発のCLI呼び出し、標準入出力を使うRPC、Node向けSDKがあり、エディターとはACPで連携できる。

## 目的・背景

- Piをフォークし、端末でのコーディングにLSP、セッション管理、拡張機能を組み込んだ。開発元はREADMEに編集方式の比較値を掲載している。実運用での編集精度や速度は今回測定していない。

## 依存関係

- Bunで導入する場合はBun 1.4.4以上。ソースから起動する場合は、ワークスペースの依存パッケージとRust製のN-APIアドオンが必要。
- 本体のライセンスはMIT。利用するモデルに応じて提供元の認証を設定する。外部サービスの料金と利用条件は提供元に従う。

## 実行条件

- 公式READMEの対応OSはmacOS、Linux、Windows。リポジトリを開くとプロジェクトの拡張、フック、MCP設定などを読み込む仕様のため、手順例では信頼できる作業ディレクトリを使う。

## 最短手順

- Bun環境で `bun install -g @oh-my-pi/pi-coding-agent` を実行し、使用するモデル提供元の認証を設定する。
- シェル実行機能を持つAIホストから、信頼できる作業ディレクトリで `omp -p 'このリポジトリの構成を要約してください。ファイルは変更しないでください。'` を子プロセスとして起動し、標準出力を受け取る。

## 変更履歴

- 2026-11-10: 初回登録
