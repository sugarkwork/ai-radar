---
name: "SenseNova-Loop-9B"
genre: "model-serving"
url: "https://github.com/OpenSenseNova/SenseNova-Loop"
repo: "OpenSenseNova/SenseNova-Loop"
license: "Apache-2.0"
stars: 157
language: "unknown"
created: "2026-10-29"
updated: "2026-11-17"
forks: 9
open_issues: 1
commits_30d: 37
commit_cadence: "daily"
commits_90d: 37
size_kb: 101572
archived: false
flags: ["unverified"]
risk_notes: "READMEの提示範囲では、具体的な導入・推論手順と依存関係・実行環境の要件を確認できない。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/watayuki_334BM/status/2122731117400981890"]
fetched_at: "2026-11-17T23:11:48.778147+00:00"
---

# SenseNova-Loop-9B

## 出来ること

- READMEによると、テキストと画像を入力し、テキストを生成する約9Bパラメータのマルチモーダルモデル。長文脈理解と複数段階のタスクに対応すると説明され、コンテキスト長は最大512Kトークン。公式AWQ 4-bit版も公開されたと記載されている。これらの機能や評価結果は配布者の説明で、独立実測ではない。

## 目的・背景

- 配布者は、共有重みを使うループ構造とmanifold-constrained hyper-connections（mHC）により、パラメータ規模を抑えながら計算深度を拡張する設計と説明している。32個の異なるデコーダ層のうち中間層を再利用し、1回のforward passで56層分の計算を行う。

## 依存関係

- 提示されたREADME範囲では、必要なソフトウェア依存関係は確認できない。

## 実行条件

- READMEはBF16バックボーンとFP32のmHCルーティングパラメータを記載している。また、4-bit重みと8-bit KV cacheを用いた256Kコンテキストのマルチモーダル推論には約15 GiBのGPUメモリが必要と説明している。具体的な対応ソフトウェアや実行環境の要件は提示範囲では確認できない。

## 最短手順

- 提示されたREADME範囲には、導入や推論の具体的な手順が記載されていない。モデル配布先としてREADMEに記載されたHugging FaceのSenseNova-Loop-9Bページを参照できる。

## 変更履歴

- 2026-11-22: 初回登録
