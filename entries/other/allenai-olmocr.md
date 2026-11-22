---
name: "olmOCR"
genre: "other"
url: "https://github.com/allenai/olmocr"
repo: "allenai/olmocr"
license: "Apache-2.0"
stars: 19829
language: "Python"
created: "2024-09-17"
updated: "2026-03-25"
forks: 1657
open_issues: 93
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 357497
archived: false
flags: ["unverified"]
risk_notes: "ローカルGPU実行には最近のNVIDIA GPUと少なくとも12 GBのGPU RAM、30 GBの空きディスクが必要とREADMEに記載。費用や処理性能の記述はREADME上の説明であり、独立検証していない。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/bkdgiffug/status/2119235453551604112"]
fetched_at: "2026-11-17T20:10:46.013009+00:00"
---

# olmOCR

## 出来ること

- PDF・PNG・JPEG形式の文書をMarkdownに変換する。READMEでは、数式・表・手書き・複雑な書式、図や複数段組みを含む場合の自然な読み順、ヘッダーとフッターの自動除去を機能として挙げている。

## 目的・背景

- 画像ベースの文書から、読みやすいプレーンテキストを作成するためのツールキット。READMEでは7Bパラメータの視覚言語モデルに基づくためGPUが必要と説明している。

## 依存関係

- PDF画像のレンダリング用にpoppler-utilsと追加フォントが必要。READMEはUbuntu/Debianでの導入コマンドを掲載している。ローカルGPU向けには olmocr[gpu] とCUDA 12.8向けPyTorchインデックスのインストール例がある。

## 実行条件

- README記載のローカルGPU実行要件は、最近のNVIDIA GPU（RTX 4090、L40S、A100、H100でテストと記載）、GPU RAM 12 GB以上、空きディスク30 GB。Python 3.11のconda環境作成例も示されている。リモートvLLMサーバー利用時は基本パッケージの導入を案内している。

## 最短手順

- Ubuntu/Debianでpoppler-utilsと追加フォントを導入し、READMEの例に沿ってPython 3.11のconda環境を作成する。リモートvLLM利用なら pip install olmocr、ローカルGPU利用なら pip install 'olmocr[gpu]' --extra-index-url https://download.pytorch.org/whl/cu128 を実行する。READMEには単一PDFの変換例もある。

## 変更履歴

- 2026-11-22: 初回登録
