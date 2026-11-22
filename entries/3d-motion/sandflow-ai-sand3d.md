---
name: "sand3d"
genre: "3d-motion"
url: "https://github.com/Sandflow-ai/sand3d"
repo: "Sandflow-ai/sand3d"
stars: 2080
forks: 231
open_issues: 14
size_kb: 8093
language: "HTML"
created: "2026-11-03"
updated: "2026-11-16"
archived: false
license: "Apache-2.0"
commits_30d: 25
commits_90d: 25
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/Ryrenz/status/2118917617545072970"]
fetched_at: "2026-11-16T21:34:49Z"
last_release: "v1.6.3"
last_release_at: "2026-11-06"
---

# sand3d

## 出来ること

- Pythonライブラリとして、Blenderのbpy上でプロファイル、立体、編集、フレーム、関節、アセンブリを記述できる。GLB、URDF、USD、IFC、OBJ、STLへ出力する。READMEでは、GLBはメッシュ・マテリアル・関節情報、URDFはリンク・関節と制限、USDAはOpenUSDのツリーとマテリアルを含むと説明している。OBJとSTLは現在の姿勢のメッシュを出力する。

## 目的・背景

- 3Dオブジェクトを短いプログラムとして記述し、モデルが生成しやすく、人が読みやすい形にすることを目的としている。READMEは、名前でパーツ・エッジ・面を参照すること、同じプログラムから同じメッシュを生成することを特徴として説明している。トークン数の比較値はREADME内の作者による説明であり、独立実測としては扱っていない。

## 依存関係

- Python 3.13（推奨）または3.11と、Blenderに付属するbpyが必要。README記載の対応はPython 3.13でbpy 5.2 LTS、Python 3.11でbpy 4.5 LTS。Python 3.12にはbpyのwheelがなく、bpy 5.2以降はIntel Mac向けwheelがないため、READMEはそれらの環境でPython 3.11を使うよう案内している。

## 実行条件

- Python 3.13または3.11の環境で利用する。長さの既定単位はミリメートル。USDの.usd、.usdc、.usdzはUSD付属ツールで.usdaから変換する。Revit形式の.rvtはライブラリから書き出せず、READMEはRevitで開けるIFCの利用を案内している。

## 最短手順

- 1. `pip install sand3d`（uvプロジェクトでは `uv add sand3d`）でインストールする。2. `import sand3d as s3d` として利用し、`s3d.extrude`、`s3d.hole`などで形状を記述する。3. `s3d.export(model, "model.glb")` のように出力する。READMEはAPI資料をLLMのsystem promptに含める方法も案内している。

## 変更履歴

- 2026-11-15: 初回登録
