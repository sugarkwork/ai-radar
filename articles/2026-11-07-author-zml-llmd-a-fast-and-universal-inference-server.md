---
name: "zml/llmd: a fast and universal inference server"
genre: "article"
url: "https://reddit.com/r/LocalLLaMA/comments/1xpppfl/zmlllmd_a_fast_and_universal_inference_server"
published: "2026-11-07"
flags: ["unverified"]
risk_notes: "記事の対応機種・モデル一覧やコンテナイメージ容量は投稿者の説明で、独立した動作確認や性能測定としては確認していない。公式GitHub READMEで確認できたLLM Quickstartのモデル一覧はLlama 3.1/3.2、Qwen 3.5、LFM 2.5で、投稿の列挙とは範囲が異なる。"
type: "article"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119310454266741105"]
fetched_at: "2026-11-19T00:21:11.077991+00:00"
---

# zml/llmd: a fast and universal inference server

## テーマ

- zml/llmdの推論サーバーを紹介する投稿。投稿者はNVIDIA、AMD、Intel、TPU、Metalで動作すると述べ、現代的なLLMサーバー機能を列挙している。

## 著者の主張

- 投稿者は連続バッチ処理、prefix caching、DFlash系の投機的デコード、tool calling、tensor/expert parallelの自動シャーディング、s3://・hf://対応VFSを挙げている。また各プラットフォーム向けイメージの容量を記載し、新リリースを告知している。これらは投稿者による説明。

## 裏取り・注意点

- 公式zml/zml READMEでは、ZMLをZig、MLIR、Bazelを用いる推論スタックと説明し、NVIDIA CUDA、AMD ROCm、Intel OneAPI、Google TPU、AWS Trainium/Inferentia 2向けのプラットフォームフラグ、LLMの実行例、ローカル・hf://・s3://からのモデル読み込みを掲載している。READMEのLLM Quickstartで確認できるモデルはLlama 3.1/3.2、Qwen 3.5、LFM 2.5。記事の全機能・全モデル・容量や「最速」という性能主張は、今回確認したREADMEでは裏付けられず、独立した比較測定も確認していない。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 出典

- 記事: https://reddit.com/r/LocalLLaMA/comments/1xpppfl/zmlllmd_a_fast_and_universal_inference_server
公式リポジトリ: https://github.com/zml/zml

## 変更履歴

- 2026-11-23: 初回登録
