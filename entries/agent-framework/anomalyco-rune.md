---
name: "Rune"
genre: "agent-framework"
url: "https://github.com/anomalyco/rune"
repo: "anomalyco/rune"
stars: 7051
forks: 266
open_issues: 377
size_kb: 162387
language: "Rust"
created: "2026-10-22"
updated: "2026-11-14"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/Ryrenz/status/2118775440810680672"]
fetched_at: "2026-11-14T04:16:15.793761+00:00"
---

# Rune

## 出来ること

- macOS、Windows、Linux、Web向けのネイティブGPU描画Rust UIフレームワーク。独自のrenderer、text、layout、springsを備え、アプリをヘッドレスで実行してPNG描画、element treeの出力、スクリプト入力による操作ができるとREADMEは説明している。出典: https://github.com/anomalyco/rune

## 目的・背景

- コーディングエージェントにRuneを使ったアプリを作らせ、ヘッドレスでPNGとelement treeを確認する用途をREADMEが案内している。作者の機能説明であり、独立した実機検証結果ではない。出典: https://github.com/anomalyco/rune

## 依存関係

- RustプロジェクトとしてGit URLとrevを指定して追加する。READMEはWindows MSVCではrustupが求めるVisual Studio C++ build toolsが必要と説明している。Windows GNUではMinGW-w64 binutilsをPATHに追加するか、RUSTFLAGSでdlltoolを指定する必要がある。出典: https://github.com/anomalyco/rune

## 実行条件

- プレリリースで、READMEはdevのrevを固定するよう案内している。Windows GNUではbinutilsがない場合にビルドがdlltoolのエラーで停止すると記載されている。出典: https://github.com/anomalyco/rune

## 最短手順

- 1. READMEの案内どおりexamples/helloとcrates/rune/README.mdを起点にする。2. Cargo.tomlに `rune = { git = "https://github.com/anomalyco/rune", rev = "<dev rev>" }` を追加し、devの具体的なrevを固定する。3. エージェントに実装させ、アプリをヘッドレスで実行してPNGを描画し、element treeを確認する。出典: https://github.com/anomalyco/rune

## 変更履歴

- 2026-11-14: 初回登録
