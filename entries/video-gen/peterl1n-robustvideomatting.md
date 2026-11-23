---
name: "Robust Video Matting (RVM)"
genre: "video-gen"
url: "https://github.com/PeterL1n/RobustVideoMatting"
repo: "PeterL1n/RobustVideoMatting"
license: "GPL-3.0"
language: "Python"
created: "2021-08-30"
updated: "2024-04-02"
commit_cadence: "stale"
archived: false
flags: ["unverified"]
risk_notes: "README記載の4K 76FPS・HD 104FPSはNvidia GTX 1080 Ti上での作者報告であり、独立した実測ではありません。現在の環境での性能は未確認です。"
stars: 9620
forks: 1196
open_issues: 124
size_kb: 9193
commits_30d: 0
commits_90d: 0
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/RoundtableSpace/status/2123027189276778909"]
fetched_at: "2026-11-18T15:16:41.301702+00:00"
---

# Robust Video Matting (RVM)

## 出来ること

- 動画内の人物を対象に、時間方向の情報を利用してマッティングを行うモデルです。READMEは動画から合成映像、アルファ予測、前景映像を出力する例を示しています。作者はGTX 1080 Tiで4K 76FPS、HD 104FPSと報告していますが、これは作者の記載であり独立実測ではありません。

## 目的・背景

- READMEによると、RVMはフレームを独立した画像として処理する既存モデルと異なり、再帰型ニューラルネットワークで動画を処理し、時間メモリを使う設計です。追加入力なしで動画のマッティングを行うことを目的としています。

## 依存関係

- PyTorch推論例では、依存関係を`requirements_inference.txt`からインストールします。

## 実行条件

- READMEのPyTorch例は、モデルを`eval()`に設定し、`.cuda()`でGPUに載せて重みを読み込みます。`convert_video`の説明ではモデルはCPUまたはCUDAのいずれのデバイスでも利用可能とされています。CoreML配布モデルはiOS 13以降が必要で、CoreMLは動的解像度に対応しないとREADMEに記載されています。

## 最短手順

- 1. `pip install -r requirements_inference.txt`で依存関係を入れます。
2. `MattingNetwork('mobilenetv3').eval().cuda()`でモデルを作成し、配布重みを`load_state_dict`で読み込みます。`resnet50`も選べます。
3. `inference.convert_video`に入力動画と出力先を渡します。出力形式は動画またはPNG連番で、アルファや前景の出力先も指定できます。

## 変更履歴

- 2026-11-23: 初回登録
