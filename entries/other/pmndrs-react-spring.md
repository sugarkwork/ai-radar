---
name: "react-spring"
genre: "other"
url: "https://github.com/pmndrs/react-spring"
repo: "pmndrs/react-spring"
flags: ["unverified"]
risk_notes: "READMEでは対応先と導入例を確認できるが、詳細な依存関係や各環境の利用条件は示されていない。"
stars: 29279
forks: 1236
open_issues: 80
size_kb: 670152
language: "TypeScript"
created: "2018-03-07"
updated: "2026-11-01"
archived: false
license: "MIT"
commits_30d: 23
commits_90d: 78
commit_cadence: "daily"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/aikangarooking/status/2121444332091965629"]
fetched_at: "2026-11-14T07:14:03.435839+00:00"
---

# react-spring

## 出来ること

- READMEはreact-springをクロスプラットフォームのspring物理ベースのアニメーションライブラリと説明している。react-domとreact-three-fiberをサポートし、宣言的または命令的にアニメーションを設定できる。デフォルトではspringを使い、durationとeasingもサポートすると記載されている。

## 目的・背景

- READMEは、springを基礎にしたアニメーションでアイデアを形にするための柔軟なツールを提供すると説明している。

## 依存関係

- READMEに記載の導入パッケージはWeb向けの@react-spring/web、react-three-fiber向けの@react-spring/three。詳細な依存関係の一覧はREADMEに記載されていない。

## 実行条件

- READMEにはnpm install @react-spring/webまたはnpm install @react-spring/threeの例がある。実行環境のバージョン要件はREADMEに記載されていない。

## 最短手順

- Web向けはnpm install @react-spring/webを実行し、@react-spring/webからanimatedとuseSpringをimportする。READMEの例ではuseSpringでopacityとyを設定し、animated.divにstyleとして渡す。react-three-fiber向けには@react-spring/threeをインストールする例がある。

## 変更履歴

- 2026-11-14: 初回登録
