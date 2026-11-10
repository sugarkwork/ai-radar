---
name: "Bring Agentic Coding On-Device with Foundry Local"
genre: "article"
url: "https://devblogs.microsoft.com/foundry/foundry-local-agentic-coding-qwen3-8-27b/"
published: "2026-11-05"
flags: ["unverified"]
risk_notes: "llama.cppとの速度差とVRAM別のコンテキスト上限はMicrosoftの報告に基づく。実機での再現、Copilotアプリ全体のオフライン動作、利用プランごとの料金・条件は未確認。"
type: "article"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/cutetoxicguy/status/2118504890888564817"]
fetched_at: "2026-11-10T10:09:52Z"
---

# Foundry LocalでQwen3.8-27Bを動かし、GitHub Copilotから使う

## テーマ

- NVIDIA GPUを搭載したPCでQwen3.8-27Bをローカル推論し、GitHub CopilotアプリのBYOK設定から接続する手順。記事ではFoundry Local CLI 0.13.0以降、24 GB以上のVRAM、別途導入するCUDAと互換性のあるcuDNNを要件としている。
- CLIでモデルをロードし、foundry server statusで取得したローカルエンドポイントをCopilotのモデルプロバイダー設定に登録する。

## 著者の主張

- ONNX Runtime上でDFlash2による投機的デコード、INT4重み、KVキャッシュ量子化、プレフィックスキャッシュ、連続バッチ処理などを組み合わせる。記事によると、4ビット版は約18 GBで、VRAM 24 GBでは最大64Kトークン、32 GB以上では最大262Kトークンのコンテキストを扱える。
- MicrosoftはRTX 5090とDGX Sparkで4ビット版を比較し、試したすべての入力長でllama.cppより生成が速く、131Kトークンを超えると差が広がったと報告している。

## 裏取り・注意点

- 記事が掲載した4種のコーディング評価値はQwen公式モデルカードと一致する。モデルカードはApache-2.0と記載している。評価値はモデル提供元の公表値で、Foundry Localの量子化版で同じ品質が得られるかは未確認。
- 速度比較はMicrosoftによる評価。Copilotアプリ全体のオフライン動作と利用プランごとの料金・条件は未確認。MacとAMD GPUへの対応拡大は記事公開時点で計画として記載されている。

## 出典

- [Microsoft Foundry Blogの原記事](https://devblogs.microsoft.com/foundry/foundry-local-agentic-coding-qwen3-8-27b/)
- [Qwen公式モデルカード](https://huggingface.co/Qwen/Qwen3.8-27B)
- [GitHub公式のCopilot BYOKガイド](https://docs.github.com/en/copilot/concepts/models/bring-your-own-key)

## 変更履歴

- 2026-11-10: 初回登録
