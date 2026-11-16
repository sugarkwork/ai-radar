---
name: "Athenaion"
genre: "3d-motion"
url: "https://github.com/Leonxlnx/athenaion"
flags: ["unverified"]
risk_notes: "READMEには依存パッケージのバージョン、対応環境、必要なハードウェアの詳細が記載されていない。"
repo: "Leonxlnx/athenaion"
stars: 709
forks: 90
open_issues: 0
size_kb: 62135
language: "JavaScript"
created: "2026-10-17"
updated: "2026-10-17"
archived: false
license: "MIT"
commits_30d: 2
commits_90d: 2
commit_cadence: "monthly"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/dextune/status/2119029602257351106"]
fetched_at: "2026-11-16T03:11:13.835807+00:00"
---

# Athenaion

## 出来ること

- 古代ギリシャ風の大規模な3D世界をthree.jsでコード生成する。READMEでは、建築物、彫像、滝、植生、雲、海などのシーン要素と、アンチエイリアス・ソフトシャドウ・モーションブラー等を備えたオフラインレンダラーを説明している。機能説明はREADMEの記載であり、独立した動作検証ではない。出典: https://github.com/Leonxlnx/athenaion#readme

## 目的・背景

- 9枚の参照画像に合わせた世界を構築したプロジェクト。README作者はClaude Code（Opus 5.5）で約2日間制作したと報告している。報告値は作者によるもので、独立実測ではない。出典: https://github.com/Leonxlnx/athenaion#readme

## 依存関係

- READMEはthree.jsをクレジットに記載している。セットアップ手順はnpm install。依存パッケージの完全な一覧やバージョンはREADMEから確認できない。出典: https://github.com/Leonxlnx/athenaion#readme

## 実行条件

- READMEの起動手順はnpm installの後にnode tools/serve.mjsを実行するもの。重い地形・彫像・巨大な頭部メッシュは初回実行時に生成されるため遅いと説明されている。静止画・動画の描画にはChromeまたはEdgeが必要と記載されている。出典: https://github.com/Leonxlnx/athenaion#readme

## 最短手順

- README記載の手順: 1. リポジトリを取得する。2. npm installを実行する。3. node tools/serve.mjsを実行する。4. ブラウザーで表示する。描画にはREADME記載のtools/render.mjsまたはtools/render-video.mjsのコマンドを使う。出典: https://github.com/Leonxlnx/athenaion#readme

## 変更履歴

- 2026-11-16: 初回登録
