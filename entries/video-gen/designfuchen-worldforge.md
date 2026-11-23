---
name: "WorldForge"
genre: "video-gen"
url: "https://github.com/designfuchen/worldforge"
repo: "designfuchen/worldforge"
flags: ["unverified"]
risk_notes: "READMEに記載された性能値や品質上の効果（例：モデル切替1.2～1.5秒、120Hz表示）は独立に確認されていません。"
stars: 223
forks: 59
open_issues: 1
size_kb: 26682
language: "Python"
created: "2026-11-08"
updated: "2026-11-08"
archived: false
license: "MIT"
commits_30d: 3
commits_90d: 3
commit_cadence: "monthly"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/Leviwoyun/status/2119335242565865788"]
fetched_at: "2026-11-19T09:13:36.975378+00:00"
---

# WorldForge

## 出来ること

- READMEによると、Colab上のGPUで画像・動画・3D世界の生成を行い、MacのSwiftUI/AppKitアプリまたはWeb UIから操作する制作環境です。画像生成、NVIDIA Lyra 2.0を使った動画・3D世界生成、Diffusers対応モデルの利用、生成物のローカル取得や後処理機能が記載されています。性能・画質に関する数値はREADME上の説明で、独立検証済みではありません。

## 目的・背景

- 作者は、Colabでのモデル再読み込み、複数モデル切替時のメモリ不足、Blackwell GPUでの互換性、SSH接続制限、動画の品質・長さ、高解像度メディア表示の負荷を解消する目的を挙げています。

## 依存関係

- READMEは、ローカル側のPython 3標準ライブラリで動くデーモン、macOSのSwiftUI/AppKitアプリ、Colab上のGPU環境とモデル群を説明しています。Lyra、Qwen-Image、Diffusers系モデルなど個別モデルや追加ツールの利用条件はモデル・機能ごとに異なる可能性があります。

## 実行条件

- READMEの説明では、macOSのStudioアプリとローカルデーモンを使い、Google ColabのVMへSSHトンネル経由で接続します。GPUやモデルの利用には対応するColab環境が必要とされています。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- READMEには「1 分でクイックスタート」へのリンクがありますが、提示されたREADME本文では具体的な起動コマンドや手順を確認できませんでした。

## 変更履歴

- 2026-11-23: 初回登録
