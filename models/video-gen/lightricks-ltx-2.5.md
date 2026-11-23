---
name: "LTX-2.5"
genre: "video-gen"
url: "https://huggingface.co/Lightricks/LTX-2.5"
model: "Lightricks/LTX-2.5"
license: "ltx-2.x-community-license-agreement"
downloads: 2828071
likes: 12467
created: "2026-07-23T07:55:24.000Z"
updated: "2026-10-11T07:00:53.000Z"
flags: ["unverified"]
risk_notes: "モデルファイルへのアクセスにはHugging Face情報の共有への同意が必要と表示されています。投稿にある「動画モデルで最もダウンロードされた」という比較主張は、このモデルカードの情報だけでは確認できません。"
type: "model"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/IU0QVW/status/2122955661797405025"]
fetched_at: "2026-11-18T09:57:39Z"
---

# LTX-2.5

## 出来ること

- 公式モデルカードはLTX-2.5を動画・音声・世界シミュレーション向けとして説明し、テキストからの動画生成、画像からの動画生成、動画・音声を含む複数の入出力形式を掲載しています。カード内の手順にはテキスト動画生成、画像動画生成、空間アップスケーリングの例があります。

## 目的・背景

- Lightricksが公開するLTX-2.5の公式モデルリポジトリです。カードはフル制御とカスタマイズ、自前環境での実行を案内しています。ライセンス欄はLTX-2.x Community License Agreementで、年間売上1000万ドル未満の商用・本番利用は無償、ファインチューンの移転には有料ライセンスが必要となる場合があると記載されています。

## 収録ファイル

- モデルカードは22Bの蒸留版・開発版Transformer、テキストエンコーダー、動画・音声VAE、空間・時間アップサンプラー、LoRAなどを掲載しています。BF16、ComfyUI向けINT8、NVFP4などのファイルがあります。NVFP4版はComfyUI、またはBlackwell環境で所定の量子化オプションを使うltx-pipelines向けと説明されています。

## 実行条件

- 公式カードのPython手順はLTX-2パイプラインの取得、uvによる依存関係同期、複数の重みファイルのダウンロードを案内しています。動画サイズは幅・高さを32の倍数にし、フレーム数は8で割った余りが1となる値にするよう記載されています。必要なGPU機種・VRAM容量の明示は確認できませんでした。

## 使い方

- 公式カードにはPythonのltx-pipelines、ComfyUI、Diffusersの利用経路があります。Pythonでは必要なTransformer、テキストエンコーダー、VAE、アップサンプラー等を指定して蒸留パイプラインを実行します。低VRAM向けの例としてfp8-cast量子化とCPUオフロードも記載されています。ComfyUI用INT8ファイルはltx-pipelines/PyTorch経路では読み込めないとの注意があります。

## 変更履歴

- 2026-11-23: 初回登録
