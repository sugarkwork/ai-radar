---
name: "Zdog"
genre: "3d-motion"
url: "https://github.com/metafizzy/zdog"
repo: "metafizzy/zdog"
license: "unknown"
stars: 10725
language: "JavaScript"
created: "2019-03-06"
updated: "2023-07-18"
forks: 412
open_issues: 55
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 659
archived: false
flags: ["unverified"]
risk_notes: "GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/0xCarrera/status/2123762450935771202"]
fetched_at: "2026-11-22T04:49:27.251868+00:00"
---

# Zdog

## 出来ること

- 図形を組み合わせ、シンプルな疑似3Dモデルを作成して表示できます。READMEのデモでは円と四角形を配置し、回転アニメーションとドラッグ操作を設定しています。

## 目的・背景

- 作者は、複雑すぎない3Dエンジンでシンプルな3Dモデルをデザイン・表示する目的で作成したと説明しています。図形はCanvasまたはSVGの2D描画APIで描画されます。

## 依存関係

- READMEには外部の実行時依存関係の記載がありません。

## 実行条件

- READMEには `<canvas>` または `<svg>` の2D描画APIを利用するとあります。より詳しい実行環境の条件は、提示されたREADMEでは確認できません。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- README記載のCDNをHTMLに追加します: `<script src="https://unpkg.com/zdog@1/dist/zdog.dist.min.js"></script>`。その後、`Zdog.Illustration` と図形クラスを使ってモデルを作成し、`updateRenderGraph()` を呼び出します。

## 変更履歴

- 2026-11-23: 初回登録
