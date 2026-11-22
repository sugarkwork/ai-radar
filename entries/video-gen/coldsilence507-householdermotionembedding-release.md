---
name: "Householder Motion Embedding (NoiseControl)"
genre: "video-gen"
url: "https://github.com/coldsilence507/HouseholderMotionEmbedding-Release"
repo: "coldsilence507/HouseholderMotionEmbedding-Release"
license: "Apache-2.0"
stars: 10
language: "Python"
created: "2026-11-04"
updated: "2026-11-06"
forks: 1
open_issues: 0
commits_30d: 14
commit_cadence: "weekly"
commits_90d: 14
size_kb: 16187
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・実行条件。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/Machinedelusion/status/2119114405740765552"]
fetched_at: "2026-11-16T23:13:20.717649+00:00"
---

# Householder Motion Embedding (NoiseControl)

## 出来ること

- 参照動画からRAFTで光学フローを推定するか、事前計算したフロー場を入力して、FlowHouseholder変換で時間的に相関した初期ノイズを生成し、LoRAを適用したCogVideoX-5B-I2Vで動きに沿う動画を生成します。READMEの出力仕様は49フレーム、480×720、8 fpsです。

## 目的・背景

- 各フレームのノイズを前フレームからピクセル単位のフロー条件付きHouseholder変換で作り、直交変換によってノイズをガウス分布に保ちながら、動きの情報を初期ノイズに反映する設計です。READMEは論文の例を掲載し、MC-Benchの論文数値ではドラッグ対象外のフローをゼロにした一方、infer.pyでは同じ処理を行わず背景にわずかな動きが出る場合があると説明しています。

## 依存関係

- READMEに記載の主な構成要素はPython 3.12、PyTorch 2.7、CUDA 12.8、CogVideoX-5B-I2V、RAFT（torchvision経由）です。推論ではCogVideoXのベースモデルがHugging Face Hubから自動取得されます。LoRA重みは別途4.2 GBのファイルとして案内されています。

## 実行条件

- README記載のテスト環境はPython 3.12、PyTorch 2.7、CUDA 12.8です。推論はGPU・ライブラリの違いで出力の細部が変わり得ます。学習データとしてRealCam-Vidのtrain/test NPZメタデータを要求し、記載の学習設定は4 GPU、GPUあたりバッチサイズ2、LoRA rank 2048、30k steps、bf16です。

## 最短手順

- README記載の手順は、リポジトリを取得しPython 3.12のconda環境を作成してrequirements.txtを導入することです。参照動画から推論する場合はinfer.pyに--ref_video、--first_frame、--prompt、--outputを渡します。事前計算フローを使う場合はinfer_from_flow.pyに--flows、--first_frame、--prompt、--outputを渡します。READMEのgit clone例はhttps://github.com/<user>/NoiseControl.gitというプレースホルダーです。

## 変更履歴

- 2026-11-22: 初回登録
