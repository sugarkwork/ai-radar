---
name: "D3D: Decoupled Diffusion Drafting for Asynchronous Speculative Decoding"
genre: "model-serving"
url: "https://github.com/fudan-generative-vision/D3D"
repo: "fudan-generative-vision/D3D"
license: "MIT"
stars: 24
language: "Python"
created: "2026-11-01"
updated: "2026-11-08"
forks: 2
open_issues: 1
commits_30d: 20
commit_cadence: "daily"
commits_90d: 61
size_kb: 26419
archived: false
flags: ["unverified"]
risk_notes: "ベンチマーク表の性能値はREADME記載の条件下での報告であり、独立検証はしていない。GPUやモデルの必要容量など、README抜粋で確認できない実行条件は不明。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119264905119285734"]
fetched_at: "2026-11-18T10:11:10.364344+00:00"
---

# D3D: Decoupled Diffusion Drafting for Asynchronous Speculative Decoding

## 出来ること

- 拡散ドラフトモデルをターゲット検証モデルと別GPUで動かし、ターゲットがドラフトを検証している間に、複数の検証結果に対応する継続候補を準備する非同期デコーディングを行う。READMEはnative D3D推論と、任意の2 GPU SGLang Hybridバックエンドを案内している。

## 目的・背景

- ターゲットによる検証処理とドラフト候補の準備を並行させ、検証結果に合う継続候補を次のデコードに再利用する方式。READMEにはSGLang Hybridを使った7ベンチマークのスループット値が掲載されているが、これは配布者による報告である。

## 依存関係

- READMEに示された導入手順ではPython仮想環境、requirements.txt、flash-attn==2.8.3、および編集可能モードでのD3Dインストールを使う。SGLangバックエンドは別途インストールする任意構成。

## 実行条件

- READMEの例ではCUDA_VISIBLE_DEVICES=0,1を設定し、ターゲットをcuda:0、ドラフトをcuda:1で動かす。例ではQwen3-8Bをターゲット、D3D-1.7B-8Bをドラフトに指定し、dtype bf16を使う。必要なGPU機種・メモリ容量は抜粋では確認できない。

## 最短手順

- README記載の手順: リポジトリをcloneし、D3DディレクトリでPython仮想環境を作成して有効化。pip install -r requirements.txt、pip install flash-attn==2.8.3 --no-build-isolation、pip install -e . --no-depsを実行する。次にCUDA_VISIBLE_DEVICES=0,1を設定し、READMEのsingle-request例などで対象モデル、デバイス、データセット、出力先を指定して推論する。

## 変更履歴

- 2026-11-23: 初回登録
