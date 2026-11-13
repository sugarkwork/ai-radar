---
name: "LapDraw"
genre: "other"
url: "https://github.com/SachinyadavAug20/lapdraw"
repo: "SachinyadavAug20/lapdraw"
stars: 0
forks: 0
open_issues: 0
size_kb: 1023
language: "JavaScript"
created: "2026-11-06"
updated: "2026-11-07"
archived: false
license: "MIT"
commits_30d: 22
commits_90d: 22
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/samtagon38824/status/2118738054374736329"]
fetched_at: "2026-11-13T05:07:47.872720+00:00"
---

# LapDraw

## 出来ること

- READMEによると、ウェブページ上の描画・ハイライト・レビュー用スタンプ、URL単位のノート、無限キャンバス、シーケンス図・UMLクラス図・ERDの作成に対応する。QuickShapeは450ms静止時に線や図形を整形すると説明されている。

## 目的・背景

- READMEは、ノートPCのトラックパッドで描く際の揺れや、技術文書・コードレビューへの視覚的な注釈を用途として挙げている。これらはREADME上の説明であり、独立した効果測定ではない。

## 依存関係

- READMEには「Zero dependencies」「100% local」と記載されている。依存関係の独立確認はしていない。

## 実行条件

- README記載の対象はChrome・Brave・Edge（Manifest V3）とFirefox（Manifest V2）。ビルドにはNode.js/npmが必要とみられるが、READMEにはバージョン条件の記載がない。

## 最短手順

- README記載のChrome系手順：`npm run build`を実行し、ブラウザーの拡張機能ページでDeveloper modeを有効にして、`dist/chrome`をLoad unpackedで読み込む。Firefoxでは`dist/firefox/manifest.json`を一時アドオンとして読み込む。

## 変更履歴

- 2026-11-13: 初回登録
