---
name: "Product Launch Motion"
genre: "video-gen"
url: "https://github.com/AbubakrChan/product-launch-motion"
repo: "AbubakrChan/product-launch-motion"
stars: 452
forks: 59
open_issues: 0
size_kb: 51948
language: "JavaScript"
created: "2026-07-27"
updated: "2026-10-21"
archived: false
license: "MIT"
commits_30d: 33
commits_90d: 44
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/PromptLabCN/status/2120750742785171596"]
fetched_at: "2026-11-12T06:13:54.236477+00:00"
---

# Product Launch Motion

## 出来ること

- READMEでは、WebサイトのURLを入力として、Claude Codeが構成を作り、HTMLベースの動画を制作・レンダリングするスキルと説明されている。作者は音楽・効果音を同期させた60 fpsのMP4を出力すると述べている。これはREADME上の説明であり、独立した動作確認ではない。出典: https://github.com/AbubakrChan/product-launch-motion

## 目的・背景

- 製品のローンチ動画を、テンプレートやAfter Effectsを使わずに作るためのClaude Codeスキル。READMEは、実作品のレビューから得た制作ルールとプロンプト・レビュー記録を再利用できる資料として挙げている。出典: https://github.com/AbubakrChan/product-launch-motion

## 依存関係

- READMEに記載の要件はClaude CodeとOpus 5.5、Node.js 20以上、Playwright、FFmpeg、Python 3とnumpy。約120 BPMのロイヤリティフリー楽曲は任意で、各トラックのライセンス確認が必要とされている。出典: https://github.com/AbubakrChan/product-launch-motion

## 実行条件

- READMEによれば、処理はローカルで行われ、動画レンダリングにはPlaywrightとFFmpegを使う。楽曲の利用条件はトラックごとに確認する必要がある。出典: https://github.com/AbubakrChan/product-launch-motion

## 最短手順

- README記載の導入コマンドは `npx skills add AbubakrChan/product-launch-motion`。導入後、Claude Codeに `Make a launch video for https://your-website.com` のように依頼する。READMEは更新時に `npx skills update` を案内している。出典: https://github.com/AbubakrChan/product-launch-motion

## 変更履歴

- 2026-11-12: 初回登録
