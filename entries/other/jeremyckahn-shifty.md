---
name: "Shifty"
genre: "other"
url: "https://github.com/jeremyckahn/shifty"
repo: "jeremyckahn/shifty"
license: "MIT"
stars: 1569
language: "TypeScript"
created: "2011-05-20"
updated: "2026-11-14"
forks: 88
open_issues: 0
commits_30d: 8
commit_cadence: "weekly"
commits_90d: 14
size_kb: 9006
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/Feljoy_ix/status/2121787138455040333"]
fetched_at: "2026-11-15T03:17:23.689019+00:00"
---

# Shifty

## 出来ること

- TypeScript向けのtweenエンジン。個別tweenの再生制御、tweenのライフサイクルに対する拡張フック、Promiseを使ったasync/awaitに対応する。READMEは処理・メモリのオーバーヘッドを抑える設計と説明している。

## 目的・背景

- カスタマイズ可能なアニメーションを構築するために必要な機能を提供する軽量ライブラリとして説明されている。上位ツールに組み込む用途を想定している。

## 依存関係

- 利用手順ではnpmでパッケージ `shifty` をインストールする。READMEに具体的な実行時依存パッケージの一覧は記載されていない。

## 実行条件

- README記載の公式サポート対象はEvergreenブラウザー、Safari、Node 10以降。Internet Explorerはv2でサポートすると記載されている。ES module、CommonJS、AMDで読み込める。

## 最短手順

- `npm install --save shifty` で導入し、`import { tween } from 'shifty'` などで読み込む。`tween` に `from`、`to`、`duration`、`render` を渡してアニメーションを記述する。

## 変更履歴

- 2026-11-15: 初回登録
