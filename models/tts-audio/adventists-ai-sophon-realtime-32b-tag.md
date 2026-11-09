---
type: "model"
name: "adventists-ai/Sophon-Realtime-32B-Tag"
genre: "tts-audio"
url: "https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Tag"
author: "adventists-ai"
source_post: "https://x.com/nahid_pro09/status/2119427620643418296"
sources: ["https://x.com/nahid_pro09/status/2119427620643418296?a=4RjqYnPJdB4aIeTMLx0&s=20", "https://x.com/nahid_pro09/status/2119427620643418296", "https://huggingface.co/adventists-ai/Sophon-Realtime-v1", "https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Tag", "https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Flash", "https://github.com/adventists-ai/sophon-realtime", "https://raw.githubusercontent.com/adventists-ai/sophon-realtime/main/NOTICE", "https://huggingface.co/mradermacher/gemma-4-31B-it-ARA-heretic-GGUF"]
first_seen: "2026-11-08"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "初音声約0.6秒・VoiceBench82.8は配布元の測定。Apache-2.0表記でもNOTICEの第三者構成要素を確認。日本語対応と実機動作は未確認。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "adventists-ai/Sophon-Realtime-32B-Tag"
license: "apache-2.0"
base_model: []
downloads: 202
likes: 2
format: "safetensors / onnx / pytorch"
size: "配布中の重みファイル 32本・合計44,592,307,025 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-10-29"
updated: "2026-11-08"
fetched_at: "2026-11-09T00:31:38.085100+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
---

# adventists-ai/Sophon-Realtime-32B-Tag

## 出来ること

Sophon-Realtimeの32B-Tag重み。共通32B brainと表情豊かな別音声モデルを組み合わせる版。

2026-11-09確認のカードはthinker→tag-tts talker→flow/HiFT vocoderを単一vLLM-Omniモデルとして提供すると説明。音声タグは発話時に演技へ反映し文字出力から除去する。E2E版は別のプレビューで、Tagの構成とは異なる。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08（原記録）のチェック記録を基にしている。メタ情報は2026-11-09T00:31:38.085100+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:31:38.085100+00:00）。重み 32本。

- `talker/CosyVoice-BlankEN/model.safetensors` — 988,097,824 bytes
- `talker/campplus.onnx` — 28,303,423 bytes
- `talker/flow.decoder.estimator.fp32.onnx` — 1,326,227,682 bytes
- `talker/flow.pt` — 1,329,140,683 bytes
- `talker/hift.pt` — 83,202,622 bytes
- `talker/llm.pt` — 2,569,227,765 bytes
- `talker/speech_tokenizer_v3.batch.onnx` — 969,451,579 bytes
- `talker/speech_tokenizer_v3.onnx` — 969,451,503 bytes
- ほか24本。複数形式・量子化・分割を含むため全量ダウンロードを推奨する意味ではない。

[ファイル一覧](https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Tag/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

zh/en、Linux/CUDA/Python3.12/vLLM-Omni、推奨80GB GPU1枚。音声モデル等は別の構成要素。

初音声約0.6秒・VoiceBench82.8は配布元の測定。Apache-2.0表記でもNOTICEの第三者構成要素を確認。日本語対応と実機動作は未確認。

## 使い方

[公式モデルカード](https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Tag)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @nahid_pro09: https://x.com/nahid_pro09/status/2119427620643418296
- 対象資料: https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Tag
- 参照: https://huggingface.co/adventists-ai/Sophon-Realtime-v1
- 参照: https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Flash
- 参照: https://github.com/adventists-ai/sophon-realtime
- 参照: https://raw.githubusercontent.com/adventists-ai/sophon-realtime/main/NOTICE
- 参照: https://huggingface.co/mradermacher/gemma-4-31B-it-ARA-heretic-GGUF

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
