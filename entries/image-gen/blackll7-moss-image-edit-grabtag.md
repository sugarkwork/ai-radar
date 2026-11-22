---
name: "GrabTag"
genre: "image-gen"
url: "https://github.com/blackll7/MOSS-image-edit-grabtag"
repo: "blackll7/MOSS-image-edit-grabtag"
license: "MIT"
stars: 0
language: "Python"
created: "2026-11-06"
updated: "2026-11-09"
forks: 0
open_issues: 0
commits_30d: 43
commit_cadence: "daily"
commits_90d: 43
size_kb: 10419
archived: false
flags: []
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
risk_notes: ""
sources: ["https://x.com/toyxyz3/status/2119156716340470261"]
fetched_at: "2026-11-17T05:31:37.855694+00:00"
---

# GrabTag

## 出来ること

- 参照画像を名前付き領域に分割し、領域IDカラーマップやlayout.jsonを生成する。READMEによると、plan/build、colormap、depth-colormap、chromaのCLIを備え、chromaはグリーンスクリーンのマッティングに使う。MOSS-Image / ComfyUI向けの入力を作成する。

## 目的・背景

- 領域の位置は画像、領域の内容はテキストで指定するという役割分担に基づき、参照画像の領域と指示文を対応付ける。READMEは、テキストだけでは位置を表現できず、カラーマップだけでは領域の内容を表現できないと説明している。

## 依存関係

- README記載ではコア依存はnumpyとPillow。mask機能にはopencv-pythonとscipy、SAMマスク機能にはtorchとsegment-anythingが追加で必要。

## 実行条件

- Python 3.9以上。コア機能はCPUで利用可能で、SAMをCUDAで使う場合に限りGPUが必要とREADMEに記載されている。

## 最短手順

- READMEの例では、`pip install -e .`でコアをインストールし、`python examples/make_demo.py examples/demo.png`でデモ画像を作成。続けて`python grabtag.py plan --ref examples/demo.png --spec examples/demo_spec.json --out build/demo`を実行し、生成されたregions.jsonを編集してから`python grabtag.py build --dir build/demo`でlayoutを出力する。

## 変更履歴

- 2026-11-22: 初回登録
