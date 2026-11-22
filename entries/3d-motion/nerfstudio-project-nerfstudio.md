---
name: "Nerfstudio"
genre: "3d-motion"
url: "https://github.com/nerfstudio-project/nerfstudio"
repo: "nerfstudio-project/nerfstudio"
stars: 12219
forks: 1693
open_issues: 974
size_kb: 121997
language: "Python"
created: "2022-05-31"
updated: "2025-07-29"
archived: false
license: "Apache-2.0"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/thegreatest_sv/status/2119129564047982889"]
fetched_at: "2026-11-17T02:20:10.263239+00:00"
---

# Nerfstudio

## 出来ること

- NeRFの作成、学習、テストを支援します。READMEでは各コンポーネントをモジュール化し、NeRFの実装を理解しやすくする方針を説明しています。

## 目的・背景

- NeRFの技術を使い始める人や研究者を支援するため、チュートリアルやドキュメントを提供する、コラボレーションを重視したプロジェクトです。

## 依存関係

- README記載のセットアップでは、PyTorch（CUDA対応）、tiny-cuda-nn、tiny-cuda-nnのビルド用cuda-toolkitが必要です。READMEはCUDA 11.7および11.8でのテストに言及しています。

## 実行条件

- NVIDIA GPUとCUDAが必要です。Python 3.8以上が必要で、READMEではcondaによる環境構築を推奨しています。

## 最短手順

- README記載の手順は、環境と依存関係を用意し、`pip install nerfstudio`で導入した後、`ns-download-data nerfstudio --capture-name=poster`でデータを取得し、`ns-train nerfacto --data data/nerfstudio/poster`で学習を開始します。READMEではnerfactoを実世界のシーン向け推奨モデルとして紹介しています。

## 変更履歴

- 2026-11-22: 初回登録
