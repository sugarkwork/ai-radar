---
type: "model"
name: "mradermacher/gemma-4-31B-it-ARA-heretic-GGUF"
genre: "other"
url: "https://huggingface.co/mradermacher/gemma-4-31B-it-ARA-heretic-GGUF"
author: "mradermacher"
source_post: "https://x.com/nahid_pro09/status/2119427620643418296"
sources: ["https://x.com/nahid_pro09/status/2119427620643418296?a=4RjqYnPJdB4aIeTMLx0&s=20", "https://x.com/nahid_pro09/status/2119427620643418296", "https://huggingface.co/adventists-ai/Sophon-Realtime-v1", "https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Tag", "https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Flash", "https://github.com/adventists-ai/sophon-realtime", "https://raw.githubusercontent.com/adventists-ai/sophon-realtime/main/NOTICE", "https://huggingface.co/mradermacher/gemma-4-31B-it-ARA-heretic-GGUF"]
first_seen: "2026-11-08"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "音声対話モデルやSophonの派生ではない。拒否低減の名称は安全性・能力保持の証明ではなく、量子化推論とライセンス継承の実体は別途確認する。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "mradermacher/gemma-4-31B-it-ARA-heretic-GGUF"
license: "apache-2.0"
base_model: ["richardyoung/gemma-4-31B-it-ARA-heretic"]
downloads: 1292
likes: 7
format: "gguf"
size: "配布中の重みファイル 13本・合計213,908,603,808 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-11-07"
updated: "2026-11-08"
fetched_at: "2026-11-09T00:31:38.638257+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
---

# mradermacher/gemma-4-31B-it-ARA-heretic-GGUF

## 出来ること

gemma-4-31B-it-ARA-hereticのmradermacherによるGGUF配布。Sophon記事の引用にあるが別のテキストモデル。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08（原記録）のチェック記録を基にしている。メタ情報は2026-11-09T00:31:38.638257+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:31:38.638257+00:00）。重み 13本。

- `gemma-4-31B-it-ARA-heretic.IQ4_XS.gguf` — 16,862,235,552 bytes
- `gemma-4-31B-it-ARA-heretic.Q2_K.gguf` — 11,916,315,552 bytes
- `gemma-4-31B-it-ARA-heretic.Q3_K_L.gguf` — 16,628,272,032 bytes
- `gemma-4-31B-it-ARA-heretic.Q3_K_M.gguf` — 15,287,110,560 bytes
- `gemma-4-31B-it-ARA-heretic.Q3_K_S.gguf` — 13,761,358,752 bytes
- `gemma-4-31B-it-ARA-heretic.Q4_K_M.gguf` — 18,687,064,992 bytes
- `gemma-4-31B-it-ARA-heretic.Q4_K_S.gguf` — 17,763,167,136 bytes
- `gemma-4-31B-it-ARA-heretic.Q5_K_M.gguf` — 21,845,572,512 bytes
- ほか5本。複数形式・量子化・分割を含むため全量ダウンロードを推奨する意味ではない。

[ファイル一覧](https://huggingface.co/mradermacher/gemma-4-31B-it-ARA-heretic-GGUF/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

原チェックのHF APIではgated=false、Apache-2.0表記、Q2_K11916315552bytesを確認。

音声対話モデルやSophonの派生ではない。拒否低減の名称は安全性・能力保持の証明ではなく、量子化推論とライセンス継承の実体は別途確認する。

## 使い方

[公式モデルカード](https://huggingface.co/mradermacher/gemma-4-31B-it-ARA-heretic-GGUF)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @nahid_pro09: https://x.com/nahid_pro09/status/2119427620643418296
- 対象資料: https://huggingface.co/mradermacher/gemma-4-31B-it-ARA-heretic-GGUF
- 参照: https://huggingface.co/adventists-ai/Sophon-Realtime-v1
- 参照: https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Tag
- 参照: https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Flash
- 参照: https://github.com/adventists-ai/sophon-realtime
- 参照: https://raw.githubusercontent.com/adventists-ai/sophon-realtime/main/NOTICE

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
