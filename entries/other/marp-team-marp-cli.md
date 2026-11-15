---
name: "Marp CLI"
genre: "other"
url: "https://github.com/marp-team/marp-cli"
repo: "marp-team/marp-cli"
license: "MIT"
stars: 3922
language: "TypeScript"
created: "2018-08-09"
updated: "2026-09-08"
forks: 207
open_issues: 20
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 19
size_kb: 14801
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/noa_gpt/status/2121774600321486897"]
fetched_at: "2026-11-15T05:28:34.503405+00:00"
---

# Marp CLI

## 出来ること

- Marp/Marpit形式のMarkdownスライドをHTML/CSS、PDF、PowerPoint（PPTX）、PNG/JPEG画像へ変換できる。PDFには発表者ノートの注釈やアウトラインを付けられる。通常のPPTXはレンダリング済み画像を含み、編集可能なPPTX出力は実験的機能として提供される。

## 目的・背景

- MarpおよびMarpitベースのスライドデッキ変換をコマンドラインから行うツール。

## 依存関係

- Node.jsで利用する場合はNode.js v18以降が必要。PDF、PPTX、画像への変換ではGoogle Chrome、Microsoft Edge、Mozilla Firefoxのいずれかが必要。編集可能なPPTXではブラウザーに加えてLibreOffice Impressが必要。

## 実行条件

- Markdownファイルを入力して実行する。Node.js環境ではnpxまたはnpmで利用できる。PDF、PPTX、画像への変換には対応ブラウザーをインストールする。

## 最短手順

- HTML出力: `npx @marp-team/marp-cli@latest slide-deck.md`。PDF出力: `npx @marp-team/marp-cli@latest slide-deck.md --pdf`。PPTX出力: `npx @marp-team/marp-cli@latest slide-deck.md --pptx`。これらのコマンドはREADME記載の例。

## 変更履歴

- 2026-11-15: 初回登録
