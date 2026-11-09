---
type: "model"
name: "spybyscript/scyllasband"
genre: "tts-audio"
url: "https://huggingface.co/spybyscript/scyllasband"
author: "spybyscript"
source_post: "https://x.com/mapte_fireball/status/2118974266784018721"
sources: ["https://x.com/mapte_fireball/status/2118974266784018721?a=7bYEtVD_cM2eDkGAIBM&s=46", "https://x.com/mapte_fireball/status/2118974266784018721", "https://www.reddit.com/r/LocalLLaMA/comments/1xpq3l0/scyllas_band_v4_open_source_tts_with_code_to_run/", "https://huggingface.co/spybyscript/scyllasband", "https://github.com/lowkeytea/scyllasband", "https://api.github.com/repos/lowkeytea/scyllasband"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "iPhone17 Pro Maxのwarm初音声70ms等は作者の特定環境の計測。WER/UTMOSも第三者評価提出待ちの自己報告。声の権利は別途確認。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "spybyscript/scyllasband"
license: "apache-2.0"
base_model: []
downloads: 516
likes: 12
format: "onnx / tflite / pytorch-bin / pytorch"
size: "配布中の重みファイル 97本・合計3,937,327,347 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-08-05"
updated: "2026-11-05"
fetched_at: "2026-11-09T00:31:00.799623+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
---

# spybyscript/scyllasband

## 出来ること

発話と歌唱をdelivery_modeで切り替えるScylla's Bandの音声重み。14声と発話の多言語・歌唱の英語対応を案内。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:31:00.799623+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:31:00.799623+00:00）。重み 97本。

- `coreml/coreml/duration_predictor.mlmodelc/analytics/coremldata.bin` — 243 bytes
- `coreml/coreml/duration_predictor.mlmodelc/coremldata.bin` — 554 bytes
- `coreml/coreml/duration_predictor.mlmodelc/weights/weight.bin` — 10,580,928 bytes
- `coreml/coreml/g2p.mlmodelc/analytics/coremldata.bin` — 243 bytes
- `coreml/coreml/g2p.mlmodelc/coremldata.bin` — 377 bytes
- `coreml/coreml/g2p.mlmodelc/weights/weight.bin` — 27,346,752 bytes
- `coreml/coreml/pitch_context_encoder.mlmodelc/analytics/coremldata.bin` — 243 bytes
- `coreml/coreml/pitch_context_encoder.mlmodelc/coremldata.bin` — 476 bytes
- ほか89本。複数形式・量子化・分割を含むため全量ダウンロードを推奨する意味ではない。

[ファイル一覧](https://huggingface.co/spybyscript/scyllasband/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

歌唱は歌詞＋音符＋拍のJSON、BigVGANv2、発話はVocos。LiteRT/CoreML/CoreAI/ONNX/WebGPU/PyTorch等でバンドルが異なる。

iPhone17 Pro Maxのwarm初音声70ms等は作者の特定環境の計測。WER/UTMOSも第三者評価提出待ちの自己報告。声の権利は別途確認。

## 使い方

[公式モデルカード](https://huggingface.co/spybyscript/scyllasband)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @mapte_fireball: https://x.com/mapte_fireball/status/2118974266784018721
- 対象資料: https://huggingface.co/spybyscript/scyllasband
- 参照: https://www.reddit.com/r/LocalLLaMA/comments/1xpq3l0/scyllas_band_v4_open_source_tts_with_code_to_run/
- 参照: https://github.com/lowkeytea/scyllasband
- 参照: https://api.github.com/repos/lowkeytea/scyllasband

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
