---
name: "Jan"
genre: "model-serving"
url: "https://github.com/janhq/jan"
repo: "janhq/jan"
license: "unknown"
stars: 45734
language: "Rust"
created: "2023-08-17"
updated: "2026-11-16"
forks: 3177
open_issues: 579
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 1582872
archived: false
flags: ["unverified"]
risk_notes: "GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/naka_1717/status/2119034856676159987"]
fetched_at: "2026-11-16T05:27:49.277949+00:00"
---

# Jan

## 出来ること

- ローカルLLMのダウンロードと実行、OpenAI・Anthropicなどのクラウドモデル接続、タスク別アシスタントの作成、localhost:1337でのOpenAI互換API提供、MCP連携に対応するとREADMEに記載されています。ローカル実行は利用者が選択できます。

## 目的・背景

- オープンソースAIを使いやすい製品として提供し、LLMをダウンロード・実行して利用者が制御できることを目指すデスクトップアプリです。READMEはプライバシーを特徴として掲げていますが、ここでは作者の説明として扱います。

## 依存関係

- ソースからビルドする場合、Node.js 20以上、Yarn 4.5.3以上、Make 3.81以上、Rustが必要です。macOS Apple SiliconではMetalToolchainも必要です。WindowsのビルドにはGit Bash、Visual Studio 2022 Build Tools、LLVM、Ninja、CMakeが必要で、CUDA Toolkitはcuda12/cuda13ビルド時のみ必要とされています。

## 実行条件

- README記載の最低要件はmacOS 13.6以上、Windows 10以上、Linuxは多くのディストリビューションです。macOSではモデル規模に応じて8GB（3B）、16GB（7B）、32GB（13B）のRAMが目安として記載されています。WindowsではGPUサポートについての記載があります。

## 最短手順

- READMEは各OS向けの配布版をダウンロードする方法を案内しています。ソースから開発実行する場合は、README記載の手順でリポジトリを取得して `cd jan` の後に `make dev` を実行します。WindowsではGit Bashから実行します。

## 変更履歴

- 2026-11-16: 初回登録
