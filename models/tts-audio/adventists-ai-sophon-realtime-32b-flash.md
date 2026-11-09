---
type: "model"
name: "adventists-ai/Sophon-Realtime-32B-Flash"
genre: "tts-audio"
url: "https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Flash"
author: "adventists-ai"
source_post: "https://x.com/nahid_pro09/status/2119427620643418296"
sources: ["https://x.com/nahid_pro09/status/2119427620643418296?a=4RjqYnPJdB4aIeTMLx0&s=20", "https://x.com/nahid_pro09/status/2119427620643418296", "https://huggingface.co/adventists-ai/Sophon-Realtime-v1", "https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Tag", "https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Flash", "https://github.com/adventists-ai/sophon-realtime", "https://raw.githubusercontent.com/adventists-ai/sophon-realtime/main/NOTICE", "https://huggingface.co/mradermacher/gemma-4-31B-it-ARA-heretic-GGUF"]
first_seen: "2026-11-08"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "初音声0.31秒・VoiceBench82.8は配布元の測定。全版が同じ音声品質・遅延ではなく、第三者構成要素の条件も確認する。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "adventists-ai/Sophon-Realtime-32B-Flash"
license: "apache-2.0"
base_model: []
downloads: 10
likes: 0
format: "safetensors / pytorch"
size: "配布中の重みファイル 24本・合計40,868,269,240 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-11-07"
updated: "2026-11-08"
fetched_at: "2026-11-09T00:31:38.140950+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
---

# adventists-ai/Sophon-Realtime-32B-Flash

## 出来ること

Sophon-Realtimeの32B-Flash重み。共通32B brainに軽量な別音声モデルを組み合わせる低遅延版。

2026-11-09確認のカードでは音声段が80msごとにフレームを出し、Tagと同じthinkerを使うが音声側はautoregressiveの軽い構成と説明。1枚80GBで推奨40ユーザーは作者の条件付き値で、同時利用の独立負荷試験はない。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08（原記録）のチェック記録を基にしている。メタ情報は2026-11-09T00:31:38.140950+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:31:38.140950+00:00）。重み 24本。

- `talker/model.safetensors` — 3,857,413,744 bytes
- `talker/speech_tokenizer/model.safetensors` — 682,293,092 bytes
- `thinker/audio/model.safetensors` — 405,001,088 bytes
- `thinker/model-v15-00001-of-00016.safetensors` — 3,879,586,648 bytes
- `thinker/model-v15-00002-of-00016.safetensors` — 2,040,187,152 bytes
- `thinker/model-v15-00003-of-00016.safetensors` — 2,082,100,536 bytes
- `thinker/model-v15-00004-of-00016.safetensors` — 2,082,141,480 bytes
- `thinker/model-v15-00005-of-00016.safetensors` — 2,129,351,336 bytes
- ほか16本。複数形式・量子化・分割を含むため全量ダウンロードを推奨する意味ではない。

[ファイル一覧](https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Flash/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

zh/en、Linux/CUDA/Python3.12/vLLM-Omni、推奨80GB GPU1枚。Tag版とは音声側の構成が異なる。

初音声0.31秒・VoiceBench82.8は配布元の測定。全版が同じ音声品質・遅延ではなく、第三者構成要素の条件も確認する。

## 使い方

[公式モデルカード](https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Flash)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @nahid_pro09: https://x.com/nahid_pro09/status/2119427620643418296
- 対象資料: https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Flash
- 参照: https://huggingface.co/adventists-ai/Sophon-Realtime-v1
- 参照: https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Tag
- 参照: https://github.com/adventists-ai/sophon-realtime
- 参照: https://raw.githubusercontent.com/adventists-ai/sophon-realtime/main/NOTICE
- 参照: https://huggingface.co/mradermacher/gemma-4-31B-it-ARA-heretic-GGUF

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
