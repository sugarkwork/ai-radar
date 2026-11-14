---
name: "Upscayl"
genre: "image-gen"
url: "https://github.com/upscayl/upscayl"
repo: "upscayl/upscayl"
license: "AGPL-3.0"
stars: 52517
language: "TypeScript"
created: "2022-07-30"
updated: "2026-10-05"
forks: 2751
open_issues: 56
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 568363
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/bkdgiffug/status/2118778945424212086"]
fetched_at: "2026-11-14T05:14:20.166596+00:00"
---

# Upscayl

## 出来ること

- AIモデルを使って低解像度画像を拡大・補正するデスクトップアプリです。READMEではReal-ESRGANとVulkanを使用すると説明されています。READMEのFAQによると、ピンぼけや完全にぼけた画像の補正には向かないとされています。

## 目的・背景

- 画像の解像度を上げ、低解像度やピクセル化した画像を補正する用途を掲げています。

## 依存関係

- 画像処理にはVulkan対応GPUが必要とREADMEに記載されています。開発手順ではNode.jsの導入にVoltaを推奨し、依存関係の導入にnpm installを案内しています。

## 実行条件

- Linux、macOS 12以降、Windows 10以降の導入手順があります。READMEはVulkan対応GPUを必要条件として挙げ、統合GPUの多くは動作しない場合があるとしています。

## 最短手順

- 利用者向けには、READMEの各OSの手順に従って配布版を導入します。開発サーバーを起動する場合は、README記載の手順でNode.js環境を準備し、リポジトリを取得してnpm install、npm run startを実行します。

## 変更履歴

- 2026-11-14: 初回登録
