---
name: "cannon-es"
genre: "other"
url: "https://github.com/pmndrs/cannon-es"
repo: "pmndrs/cannon-es"
license: "MIT"
language: "TypeScript"
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
archived: false
stars: 2090
forks: 158
open_issues: 62
size_kb: 11426
created: "2020-03-03"
updated: "2024-01-06"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/RealMarvelX/status/2118330503040221345"]
fetched_at: "2026-11-11T20:09:08.495552+00:00"
---

# cannon-es

## 出来ること

- cannon.jsを基にした物理エンジン。READMEでは、型安全なフラットバンドルとしてESMとCJSに対応し、tree shakingが可能と説明している。また、Trigger bodies、スリープ中の物体への力・インパルス適用時の再起床、摩擦計算に使う重力の設定などの変更が記載されている。

## 目的・背景

- READMEによると、cannon.jsのメンテナンス版フォーク。元のリポジトリから複数のPRを取り込み、非推奨のプロパティとメソッドを削除したとしている。

## 依存関係

- READMEはthree.jsとReact環境でreact-three-fiberを使う場合のラッパーとしてuse-cannonを案内している。その他の依存関係はREADMEの提示内容からは確認できない。

## 実行条件

- READMEには現代的な環境で使えるESMおよびCJSのフラットバンドルと記載されている。具体的なランタイムやバージョン要件は提示内容から確認できない。

## 最短手順

- README記載の手順は、`yarn add cannon-es`でインストールし、`import { World } from 'cannon-es'`で読み込む。webpackでは`import * as CANNON from 'cannon-es'`の例もある。

## 変更履歴

- 2026-11-11: 初回登録
