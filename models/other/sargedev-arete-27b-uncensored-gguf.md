---
type: "model"
name: "SargeDev/Arete-27B-Uncensored-GGUF"
genre: "other"
url: "https://huggingface.co/SargeDev/Arete-27B-Uncensored-GGUF"
author: "SargeDev"
source_post: "https://x.com/alizeh_ai/status/2119084556343251403"
sources: ["https://x.com/alizeh_ai/status/2119084556343251403?a=rEIho5h4berlsHvuXTk&s=46", "https://x.com/alizeh_ai/status/2119084556343251403", "https://huggingface.co/SargeDev/Arete-27B-Uncensored-GGUF", "https://huggingface.co/SargeDev/Arete-27B-Uncensored", "https://huggingface.co/NousResearch/Arete-27B", "https://huggingface.co/api/models/SargeDev/Arete-27B-Uncensored-GGUF"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "Apache-2.0表記。元派生重みの拒否試験を各GGUFの実行試験にしない。量子化品質・速度は未確認。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "SargeDev/Arete-27B-Uncensored-GGUF"
license: "apache-2.0"
base_model: ["NousResearch/Arete-27B"]
downloads: 3305
likes: 5
format: "gguf"
size: "配布中の重みファイル 8本・合計182,672,862,464 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-11-07"
updated: "2026-11-07"
fetched_at: "2026-11-09T00:31:15.307256+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
---

# SargeDev/Arete-27B-Uncensored-GGUF

## 出来ること

SargeDev/Arete-27B-UncensoredのGGUF変換配布。Q2_K約10.1GiB、Q4_K_M約15.7GiB、Q8_0約27GiB等を案内。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:31:15.307256+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:31:15.307256+00:00）。重み 8本。

- `arete-ablit-Q2_K.gguf` — 10,864,592,288 bytes
- `arete-ablit-Q3_K_M.gguf` — 13,500,736,928 bytes
- `arete-ablit-Q4_K_M.gguf` — 16,810,714,528 bytes
- `arete-ablit-Q4_K_S.gguf` — 15,825,298,848 bytes
- `arete-ablit-Q5_K_M.gguf` — 19,535,701,408 bytes
- `arete-ablit-Q6_K.gguf` — 22,430,999,968 bytes
- `arete-ablit-Q8_0.gguf` — 29,047,084,448 bytes
- `arete-ablit-f16.gguf` — 54,657,734,048 bytes

[ファイル一覧](https://huggingface.co/SargeDev/Arete-27B-Uncensored-GGUF/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

対応ランタイムと選択量子の容量、MTP・画像入力等のサポートを確認する必要がある。

Apache-2.0表記。元派生重みの拒否試験を各GGUFの実行試験にしない。量子化品質・速度は未確認。

## 使い方

[公式モデルカード](https://huggingface.co/SargeDev/Arete-27B-Uncensored-GGUF)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @alizeh_ai: https://x.com/alizeh_ai/status/2119084556343251403
- 対象資料: https://huggingface.co/SargeDev/Arete-27B-Uncensored-GGUF
- 参照: https://huggingface.co/SargeDev/Arete-27B-Uncensored
- 参照: https://huggingface.co/NousResearch/Arete-27B
- 参照: https://huggingface.co/api/models/SargeDev/Arete-27B-Uncensored-GGUF

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
