---
repo: "OpenBMB/MiniCPM-V"
name: "MiniCPM-V"
genre: "model-serving"
url: "https://github.com/OpenBMB/MiniCPM-V"
license: "Apache-2.0"
stars: 27093
language: "Python"
created: "2024-01-29"
updated: "2026-10-30"
forks: 2123
open_issues: 64
commits_30d: 33
commit_cadence: "daily"
commits_90d: 42
size_kb: 815156
archived: false
last_release: "20250527"
last_release_at: "2025-05-27"
author: "OpenBMB"
flags: []
risk_notes: "GitHub Releases は 2025-05-27 の 20250527 が最新で、4.7 の告知は README と Hugging Face 側。速度・ベンチ数値は提供元自身の計測で、独立した再現評価は確認していない。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/opensourcelab9/status/2113035113537970380"]
fetched_at: "2026-11-08T16:03:30Z"
---

# MiniCPM-V 4.7

## 出来ること

- 画像1枚・複数画像・文書・動画を読むマルチモーダルモデル。35B-A3B（MoE、総35B・活性3B）と 1B の2サイズがあり、どちらも Instruct モードで使える。
- スマホ・タブレットの端末内で動かせる。iOS / Android / HarmonyOS 向けの公式デモアプリが別リポジトリで公開され、GGUF 重みを llama.cpp 系で実行する。TestFlight と APK の配布あり。
- Ollama の公式モデルページから取得でき、llama.cpp / vLLM / SGLang / Transformers の手順も Cookbook に揃っている。
- 視覚トークンの圧縮率を 4x / 16x で切り替えられる。16x は軽い代わりに精度が少し落ち、OCRBench は 91.20（4x）→ 90.40（16x）。細かい文字を読ませたいときは 4x。
- 量子化違いを配布: BF16 / FP8 / int4（bitsandbytes）/ AWQ / GPTQ（W4A16）/ GGUF。GGUF は CPU 推論にも使える。
- 投機的デコード用の DSpark ヘッド（BF16 / GGUF）が 1B・35B-A3B それぞれに用意されている。

## 目的・背景

- 「MoE は総パラメータが多く、端末のメモリに専門家を全部載せられない」問題への回答。専門家を SSD に置いたまま、次層で使われそうな専門家を先読みしてロード待ちを隠す LES（Lookahead Expert Scheduling）が設計の中心。
- 予測はプリフェッチにだけ使い、計算は元のルーティングに従う。予測を外しても必要専門家を普通にロードして評価するので、能力を犠牲にせず速度だけを稼ぐ建前になっている。
- 2026-10-12 公開。シリーズは THUNLP と ModelBest の共同開発で、コードとモデル重みは Apache-2.0。
- 投稿が挙げる「撮った書類をネットに上げずに読ませる」用途は、端末内で完結するこの構成と噛み合う。ただし精度・速度の数値は提供元自身の計測で、第三者による再現評価は見当たらない。

## 依存関係

- Python から使う場合: transformers 5.18.0 以上、torchvision、torchcodec（動画デコード用）。
- torch 2.11 以降は CUDA 13.1 を同梱するため、CUDA 12.x 環境では torchcodec のロードで `RuntimeError: Could not load libtorchcodec` が出ることがある。その場合は torchcodec の代わりに PyAV を使うか、CUDA 12.8 の wheels を指定する。
- 配信は Hugging Face（openbmb/MiniCPM-V-4.7-35B-A3B、openbmb/MiniCPM-V-4.7-1B ほか）と ModelScope。
- サーバ用途は vLLM / SGLang、ローカルは llama.cpp / Ollama、ファインチューニングは SWIFT / LLaMA-Factory。
- 端末アプリを自前ビルドする場合は Xcode + CMake 3.28（iOS）、Android NDK 27.0.12077973、DevEco Studio 5.0（HarmonyOS）。iOS は llama.xcframework と onnxruntime をローカルで用意する手順になっている。

## 実行条件

- 35B-A3B を端末で動かす場合、アプリ側の推奨は 12GB RAM 以上、ダウンロード合計 約16.6GB（空き 17GB 程度）。専門家を SSD から都度読むため、高速な内部ストレージが前提。
- README の「3GB」はデコード時に使うメモリの話で、端末の総所要 RAM ではない。同じ README が検証機を iPhone 17 Pro Max（12GB 機）と明記している。RAM が少ない端末では専門家キャッシュを縮めて動くが、かなり遅くなる。
- 1B は 4GB RAM 以上・ダウンロード約1.8GB。
- 13+ tokens/s は iPhone 17 Pro Max・35B-A3B・LES 有効時の提供元計測。iPad Pro M4 の「5倍」は最適化前後の比較値。
- ライセンスはコードが Apache-2.0、Hugging Face 上の配布重みも apache-2.0。商用利用可だが、重みの利用条件はモデルカード側の記載も確認する。
- GitHub の Releases は 2025-05-27 の 20250527 が最新で、4.7 の告知は README と Hugging Face 側。更新は main ブランチと HF の lastModified で追うのが確実。

## 最短手順

- Python から試す場合（GPU 推論）:
- ```bash
pip install "transformers[torch]>=5.18.0" torchvision torchcodec
```
- ```python
from transformers import AutoModelForImageTextToText, AutoProcessor

model_id = "openbmb/MiniCPM-V-4.7-35B-A3B"
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForImageTextToText.from_pretrained(
    model_id, torch_dtype="auto", device_map="auto"
)
```
- 画像を渡すときは `downsample_mode` を `apply_chat_template` と `generate` の両方に渡す（既定は `"16x"`、細部重視なら `"4x"`）。
- 簡易サーバで済ませるなら `transformers serve openbmb/MiniCPM-V-4.7-35B-A3B --port 8000`（OpenAI 互換）。Ollama なら公式モデルページのタグをそのまま取得。
- 端末で試すなら公式アプリ（iOS は TestFlight、Android は APK）を入れ、アプリ内のモデル管理から重みをダウンロードする。

## 変更履歴

- 2026-11-09: 初回登録
