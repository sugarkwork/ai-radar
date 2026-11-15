---
name: "ComfyUI MiniMax H3 首尾帧视频工作流"
genre: "video-gen"
url: "https://github.com/pixelaigc/ComfyUI-MiniMax-H3-Workflow"
repo: "pixelaigc/ComfyUI-MiniMax-H3-Workflow"
license: "unknown"
flags: ["unverified"]
risk_notes: "READMEではワークフローのライセンスは作者が別途指定するとされていますが、この資料内にライセンス名はありません。 GitHub APIでライセンスを確認できていません。"
stars: 469
forks: 78
open_issues: 0
size_kb: 1724
language: "unknown"
created: "2026-09-09"
updated: "2026-09-10"
archived: false
commits_30d: 0
commits_90d: 2
commit_cadence: "stale"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/LuisAngelSG8LA8/status/2119031897376583922"]
fetched_at: "2026-11-15T16:07:47.112339+00:00"
---

# ComfyUI MiniMax H3 首尾帧视频工作流

## 出来ること

- ComfyUI上でMiniMax H3を使い、首尾フレーム画像とプロンプトから動画を生成するワークフローです。首フレームのみの画像動画生成、画像を使わないテキスト動画生成にも切り替えられます。動画と音声を別々にデコードして合成し、SaveVideoで保存します。READMEの説明はワークフローJSONとノードソースに基づき、完全な動画生成を再実行してはいません。

## 目的・背景

- モデル読み込み、Turbo LoRA、サンプリング、解像度計算、音声・動画デコードをサブフローにまとめ、よく使うパラメータを外側のパネルから調整できる構成です。

## 依存関係

- MiniMax H3とサブグラフ機能に対応するComfyUI、およびMiniMaxH3TurboLoRAノードを提供するComfyUI-MiniMax-H3-Turboが必要です。READMEではMiniMaxH3ImageToVideo、ResolutionSelector、ComfyMathExpressionは確認対象のComfyUIコアに含まれるとしています。モデル重みはJSONに含まれず、基本モデル、テキストエンコーダー、動画VAE、音声VAE、Turbo LoRAを所定のモデルディレクトリに用意します。

## 実行条件

- README記載のフロントエンドバージョンは1.47.11ですが、最低対応バージョンとして確認された値ではありません。実行には記載のカスタムノードと各モデルファイルが必要です。JSONには画像本体が含まれないため、画像入力モードでは画像を再度アップロードします。GPU、最低VRAM、実行時間は資料に記録されていません。

## 最短手順

- 1. README記載のComfyUI-MiniMax-H3-TurboをComfyUI/custom_nodesに導入して再起動します。2. モデルファイルを指定ディレクトリに配置し、モデル一覧を更新または再起動します。3. ワークフローJSONをComfyUIの画面に読み込みます。4. 首尾フレーム画像を使う場合は画像ノードにアップロードします。5. 外側のパネルでプロンプト、LoRA、ステップ数、時間、解像度を確認し実行します。6. SaveVideoノードの出力を確認します。テキスト動画生成では両方の画像入力を無効にします。

## 変更履歴

- 2026-11-15: 初回登録
