---
name: "rembg"
genre: "image-gen"
url: "https://github.com/danielgatis/rembg"
repo: "danielgatis/rembg"
license: "MIT"
stars: 25424
language: "Python"
created: "2020-08-10"
updated: "2026-11-06"
forks: 2481
open_issues: 1
commits_30d: 9
commit_cadence: "weekly"
commits_90d: 24
size_kb: 89581
archived: false
flags: ["unverified"]
risk_notes: "READMEに説明されている機能・効果の記載であり、個別環境での動作や出力品質は確認していない。GPU利用には対応する実行環境とバックエンドの追加設定が必要。クラウドモデルは外部APIのキーと課金条件に依存する。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/cryptowluha/status/2118618563703394414"]
fetched_at: "2026-11-11T15:12:36.528978+00:00"
---

# rembg

## 出来ること

- 画像の背景を除去するツール。READMEではCLI、Pythonライブラリ、HTTPサーバー、Dockerコンテナとしての利用を説明。CLIは単体画像、フォルダーのバッチ処理と監視処理、HTTPサーバー、RGB24ストリームを扱える。単体画像処理ではモデル指定、マスクのみの出力、アルファマッティング、ソフトエッジの色にじみ除去にも対応すると記載されている。出典: https://github.com/danielgatis/rembg

## 目的・背景

- 画像から背景を取り除くためのツール。READMEに記載された用途は、ローカルでの画像処理のほか、HTTPサーバーやクラウドモデルを介した処理。効果・出力品質について独立した実測結果はREADMEに示されていない。出典: https://github.com/danielgatis/rembg

## 依存関係

- Python 3.11以上、3.14未満。CPU利用ではonnxruntimeを含む rembg[cpu]、GPU利用では rembg[gpu] が案内されている。GPUはNVIDIA/CUDAまたはAMD/ROCm向けの追加要件があり、READMEは互換性確認と各バックエンドの導入を案内している。CLIを使う場合は cli extra を追加する。出典: https://github.com/danielgatis/rembg

## 実行条件

- READMEではCPU、NVIDIA/CUDA、AMD/ROCmのバックエンドを案内している。GPUの利用可否は環境との互換性に依存する。クラウドモデルはAPIキーを使い、サーバーではリモートモデルが既定で無効。READMEによれば、サーバー環境のAPIキーで課金される場合があるため、リモートモデルを有効にする前にキーと課金条件を確認する必要がある。出典: https://github.com/danielgatis/rembg

## 最短手順

- CPU向けCLIの導入例: `pip install "rembg[cpu,cli]"`。単体画像は `rembg i path/to/input.png path/to/output.png`、フォルダー処理は `rembg p path/to/input path/to/output`。Pythonライブラリでは `from rembg import remove` を使い、画像バイト列を `remove(input)` に渡して出力を書き込む。出典: https://github.com/danielgatis/rembg

## 変更履歴

- 2026-11-11: 初回登録
