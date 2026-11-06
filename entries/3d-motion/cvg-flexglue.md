---
type: "repo"
name: "FlexGlue"
genre: "3d-motion"
url: "https://github.com/cvg/FlexGlue"
author: "cvg (ETH Zurich Computer Vision and Geometry Lab) / Philipp Lindenberger ほか"
pricing: "free"
pricing_detail: "コード・重みとも無償公開。ただし重みの DINOv3 部分は DINOv3 License の制約下"
signup_required: false
repo: "cvg/FlexGlue"
license: "MIT"
stars: 244
language: "Python"
created: "2026-10-25"
updated: "2026-11-03"
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://x.com/tokufxug/status/2118163149983781219"]
flags: []
risk_notes: "コードは MIT だが、重み flexglue.pth は DINOv3 ConvNeXt-B を含み DINOv3 License で利用が制限される（商用利用は要確認）。実用は CUDA GPU 前提で、重みは約 567MB。README は ONNX モデルが COLMAP に使われると書くが、リポジトリのチェックリストでは COLMAP 統合は未チェック（進行中）。学習・評価コードは未公開。"
forks: 13
open_issues: 1
commits_30d: 13
commit_cadence: "daily"
size_kb: 3516
archived: false
fetched_at: "2026-11-06T20:38:56Z"
last_release: "v0.1"
last_release_at: "2026-10-26"
---

# FlexGlue — 密特徴で対応付ける画像マッチングと「似た別場所」の棄却

## 出来ること

- 2枚の画像の対応点を求める。キーポイントあり（双方向連結 or 相互最近傍）／片方のみ／キーポイントなし（密グリッドからサンプリング）の4モード
- `covisibility_score`（同じ場所を写している確率）を出し、閾値未満のペアは全マッチを棄却。見た目が似た別の場所（doppelganger）を誤認しない
- `early_stop_decay` で非対応ペアを浅い層で打ち切って計算を節約
- `match_dense` で密な対応マップ（既定 64x64、RoMa v2 refiner で 512x512）を直接取得
- ONNX 版（descriptor / matcher）を配布。ONNX Runtime だけで動き PyTorch 不要。COLMAP が使用
- Python パッケージ・torch.hub・CLI スクリプト（onnx/match_pair.py）の3経路で呼べる

## 目的・背景

- SfM・3D 復元の前段にあたる画像対応付け（feature matching）を、キーポイントの有無に依らず行うための推論コード
- DINOv3-ConvNeXt で画像を stride-8 の密特徴に符号化し、transformer で2枚の特徴を相互に refine、相関で対応点を求める
- 層ごとに covisibility を予測し、対応不能なペアを早期に検出するのが特徴。反復するファサードなど紛らわしいペアに強い
- 論文: FlexGlue: Sparse-to-Dense Feature Matching and Visual Disambiguation（arXiv:2610.32976）。著者は Philipp Lindenberger, Paul-Edouard Sarlin, Ondrej Miksik, Marc Pollefeys
- LightGlue（同 cvg）のキーポイント検出器と組み合わせる想定。refiner は RoMa v2

## 依存関係

- Python >= 3.9、torch >= 2.0、numpy、opencv-python、matplotlib（requirements.txt）
- キーポイント検出を使う場合のみ LightGlue: `python -m pip install git+https://github.com/cvg/LightGlue.git`（最新コミットが必要）
- ONNX 経路は onnxruntime（CPU）または onnxruntime-gpu と opencv-python のみ。PyTorch 不要
- 重みは初回実行時に GitHub Releases から自動ダウンロード（flexglue.pth 約 567MB、ONNX descriptor 約 360MB）

## 実行条件

- README の例は CUDA GPU 前提（`.cuda()`）。ONNX スクリプトは `--cpu` で CPU 実行も可能だが低速
- 画像は [0,1] に正規化した (3,H,W) の torch.Tensor。キーポイントは COLMAP 規約の corner 座標（左上画素中心が (0.5,0.5)）なので LightGlue の検出器には `origin="corner"` を渡す
- 既定の入力解像度は 512x512。精度を上げる最大のレバーは解像度（`describe_resize=(640,640)`）
- コードは MIT だが重みの DINOv3 部分は DINOv3 License で利用制限あり。商用利用は要確認
- COLMAP 統合はリポジトリのチェックリスト上は未完了（ONNX モデルは COLMAP が利用）

## 最短手順

- MCP サーバや Agent Skill は無い。AI からは (a) CLI スクリプトの実行、(b) Python API の呼び出し、(c) torch.hub の3通りで使う
- 導入: `python -m pip install git+https://github.com/cvg/FlexGlue.git`（重みは初回実行時に自動DL）
- CLI（PyTorch 不要・エージェント向き）: `python -m pip install onnxruntime opencv-python` の後、リポジトリ root で `python onnx/match_pair.py img0.jpg img1.jpg --min_covisibility 0.8 --cpu --output matches.png`。標準出力にマッチ数と covisibility、閾値未満なら The pair is rejected を出す
- Python API: `import torch; from flexglue import FlexGlue; m = FlexGlue(min_covisibility=0.8).eval().cuda()` とし、`pred = m.match_pair(img0, img1)` で `pred["covisibility_score"]`（同一場所か）と `pred["matches0"]`（対応点 index）を取得
- クローンせず使う: `torch.hub.load("cvg/FlexGlue", "flexglue", trust_repo=True)`
- 判定に組み込む場合: `covisibility_score` が閾値未満なら「別の場所」として棄却し、そのペアのマッチを捨てる（全マッチが invalid になる）

## 変更履歴

- 2026-11-06: 初回登録
