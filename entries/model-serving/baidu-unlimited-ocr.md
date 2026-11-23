---
name: "Unlimited OCR 2"
genre: "model-serving"
url: "https://github.com/baidu/Unlimited-OCR"
repo: "baidu/Unlimited-OCR"
license: "MIT"
stars: 31316
language: "Python"
created: "2026-06-18"
updated: "2026-11-16"
forks: 3358
open_issues: 96
commits_30d: 20
commit_cadence: "daily"
commits_90d: 21
size_kb: 80188
archived: false
flags: ["unverified"]
risk_notes: "READMEは「文書長にかかわらず推論遅延とメモリ使用量がほぼ一定」「ベンチマークで最先端」と説明しているが、ここでは独立検証していない。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ruyi3699/status/2119301390564819406"]
fetched_at: "2026-11-18T21:26:10.330128+00:00"
---

# Unlimited OCR 2

## 出来ること

- 画像化した文書のOCRと解析を行う。READMEでは、複数ページをまとめて処理する推論ではページ間の文脈を利用でき、各入力ページに対応する出力をページ順に返すと説明している。単一ページ推論は既定で動的タイル分割を使う。

## 目的・背景

- Unlimited OCR 2はSparse Reference Sliding Window Attention（SR-SWA）を用いた長文書解析を目的としている。READMEによると、テキストと画像の注意機構のやり取りを固定サイズの参照集合に圧縮し、文書が長くなった場合の計算量やメモリの制約を抑える設計。性能の説明は開発者による報告。

## 依存関係

- Transformersでの推論例ではPython 3.10、torch 2.13.0、transformers 4.52.1、huggingface-hub 0.36.0、tokenizers 0.21.4などを指定している。SGLang手順ではPython 3.10のuv環境、README記載のカスタムSGLang wheel、PyMuPDF 1.27.2.2、fastokens 0.3.2を使う。

## 実行条件

- Transformersの手順はNVIDIA A800 80GBでテストした構成として掲載され、モデルをbfloat16でCUDAにロードする。SGLangはGPUサーバー起動手順を掲載し、長文書向けページウィンドウやメモリ関連の環境変数を設定する。別のハードウェアでの動作条件はREADMEから確認できない。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- Transformersを使う場合、README記載の依存パッケージをインストールし、Hugging Faceのbaidu/Unlimited-OCR-2からモデルとtokenizerを読み込む。単一ページはmodel.infer(tokenizer, image_file=...)、複数ページはmodel.infer_multi(tokenizer, image_files=...)を呼び出す。SGLangでの提供手順はREADMEの「SGLang」節を参照。

## 変更履歴

- 2026-11-23: 初回登録
