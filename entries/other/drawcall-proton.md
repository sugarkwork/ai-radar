---
name: "Proton"
genre: "other"
url: "https://github.com/drawcall/Proton"
repo: "drawcall/Proton"
license: "MIT"
stars: 2521
language: "JavaScript"
created: "2013-07-10"
updated: "2026-03-06"
forks: 288
open_issues: 17
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 13480
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/Feljoy_ix/status/2121787138455040333"]
fetched_at: "2026-11-16T21:59:41Z"
last_release: "v5.4.3"
last_release_at: "2022-04-28"
---

# Proton

## 出来ること

- JavaScriptでパーティクルアニメーションを作成できる。READMEでは炎、花火、弾丸、爆発などの効果を例示し、Canvas、DOM、WebGL、Pixel、EaselJS、Pixi.js向けおよびカスタムレンダラーを挙げている。重力やブラウン運動などの物理特性もシミュレートできると説明されている。出典: https://github.com/drawcall/Proton

## 目的・背景

- さまざまなパーティクル効果を簡単に作成するためのJavaScriptライブラリ。READMEは、少ないコードでアニメーションを作れることを特徴として説明している。出典: https://github.com/drawcall/Proton

## 依存関係

- READMEのビルド手順ではNode.jsを依存として挙げ、npm installとnpm run buildを案内している。利用時はnpmでproton-engineをインストールする方法も記載されている。その他の依存関係はREADMEから確認できない。出典: https://github.com/drawcall/Proton

## 実行条件

- JavaScript環境で利用する。READMEにはnpmパッケージとしての利用例と、HTMLからjs/proton.web.min.jsを読み込む方法が記載されている。対応環境の詳細条件はREADMEから確認できない。出典: https://github.com/drawcall/Proton

## 最短手順

- npmでproton-engineをインストールし、Proton、Emitter、Rate、Spanなどを読み込む。Emitterに初期化要素や振る舞いを追加して位置と発生条件を設定し、Protonへ登録した後、CanvasRendererなどのレンダラーを追加する。READMEにコード例あり。出典: https://github.com/drawcall/Proton

## 変更履歴

- 2026-11-15: 初回登録
