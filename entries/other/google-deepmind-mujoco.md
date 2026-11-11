---
name: "MuJoCo"
genre: "other"
url: "https://github.com/google-deepmind/mujoco"
repo: "google-deepmind/mujoco"
license: "Apache-2.0"
stars: 17326
language: "C++"
created: "2021-08-27"
updated: "2026-11-10"
forks: 2146
open_issues: 332
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 154330
archived: false
flags: ["unverified"]
risk_notes: "READMEの取得内容がライセンス節の途中で途切れているため、ライセンス本文の条件はこの資料から確認できない。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/GitTrend0x/status/2119950747898974362"]
fetched_at: "2026-11-10T23:13:41.871917+00:00"
---

# MuJoCo

## 出来ること

- 関節構造と環境が相互作用する物理シミュレーションを行う汎用エンジン。C API、Python bindings、Unityプラグインを提供し、ネイティブデスクトップウィンドウとWebブラウザーでの対話型可視化、物理量計算用のユーティリティ関数を備える。READMEはロボティクス、生体力学、グラフィックス・アニメーション、機械学習などの研究・開発用途を挙げている。出典: https://github.com/google-deepmind/mujoco

## 目的・背景

- MuJoCoは「Multi-Joint dynamics with Contact」の略称。高速かつ正確な関節構造のシミュレーションを必要とする分野の研究・開発を支援することを目的としている。リポジトリはGoogle DeepMindが保守している。出典: https://github.com/google-deepmind/mujoco

## 依存関係

- READMEには、実行時依存関係の一覧や詳細は記載されていない。Python bindingsはPython 3.11以降を対象としている。

## 実行条件

- 推奨利用方法はGitHub Releasesのプリビルドバイナリで、Linux (x86-64、AArch64)、Windows (x86-64)、macOS (universal) 向けが案内されている。Python bindingsはPyPIから `pip install mujoco` で導入できる。READMEはLinux wheelの対象をmanylinux2014としている。mainブランチ先端は不安定な場合があるとの記載がある。出典: https://github.com/google-deepmind/mujoco

## 最短手順

- Python bindingsを使う場合はPython 3.11以降の環境で `pip install mujoco` を実行する。プリビルド版のviewerを使う場合は、公式ドキュメントのGetting Startedに従って対応OS向けリリースを取得し、MuJoCo Studioまたはsimulate viewerを起動する。出典: https://github.com/google-deepmind/mujoco

## 変更履歴

- 2026-11-11: 初回登録
