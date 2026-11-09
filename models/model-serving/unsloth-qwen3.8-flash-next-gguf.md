---
type: "model"
name: "unsloth/Qwen3.8-Flash-Next-GGUF"
genre: "model-serving"
url: "https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF"
author: "unsloth"
source_post: "https://x.com/sasasin_net/status/2118729264149491929"
sources: ["https://x.com/sasasin_net/status/2118729264149491929?a=tWrww52LyfJHPpXLuT4&s=46", "https://x.com/sasasin_net/status/2118729264149491929", "https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF/tree/main/UD-IQ2_XS", "https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ3_S", "https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF"]
first_seen: "2026-11-06"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "サイズが小さいことは性能同等の証明ではない。原チェックのlicenseはotherで、基底モデルと量子化配布の条件を確認する。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "unsloth/Qwen3.8-Flash-Next-GGUF"
license: "other"
base_model: ["Qwen/Qwen3.8-Flash-Next"]
downloads: 1548621
likes: 1534
format: "gguf"
size: "配布中の重みファイル 67本・合計1,638,719,221,860 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-08-26"
updated: "2026-11-07"
fetched_at: "2026-11-09T00:30:29.946386+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
license_name: "qwen-community-1.0"
---

# unsloth/Qwen3.8-Flash-Next-GGUF

## 出来ること

Qwen3.8-Flash-NextのUnsloth配布GGUF量子化群。紹介対象のUD-IQ2_XSは3分割で約70.6GiB。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:29.946386+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:30:29.946386+00:00）。重み 67本。

- `BF16/Qwen3.8-Flash-Next-BF16-00001-of-00008.gguf` — 10,946,368 bytes
- `BF16/Qwen3.8-Flash-Next-BF16-00002-of-00008.gguf` — 10,447,201,664 bytes
- `BF16/Qwen3.8-Flash-Next-BF16-00003-of-00008.gguf` — 102,400,491,712 bytes
- `BF16/Qwen3.8-Flash-Next-BF16-00004-of-00008.gguf` — 48,394,236,672 bytes
- `BF16/Qwen3.8-Flash-Next-BF16-00005-of-00008.gguf` — 48,367,899,040 bytes
- `BF16/Qwen3.8-Flash-Next-BF16-00006-of-00008.gguf` — 48,615,233,984 bytes
- `BF16/Qwen3.8-Flash-Next-BF16-00007-of-00008.gguf` — 48,367,899,040 bytes
- `BF16/Qwen3.8-Flash-Next-BF16-00008-of-00008.gguf` — 47,426,022,016 bytes
- ほか59本。複数形式・量子化・分割を含むため全量ダウンロードを推奨する意味ではない。

[ファイル一覧](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

分割ファイルと対応ランタイム、MoE推論に必要なメモリ・ディスクを用意する必要がある。

サイズが小さいことは性能同等の証明ではない。原チェックのlicenseはotherで、基底モデルと量子化配布の条件を確認する。

## 使い方

[公式モデルカード](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @sasasin_net: https://x.com/sasasin_net/status/2118729264149491929
- 対象資料: https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF
- 参照: https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF/tree/main/UD-IQ2_XS
- 参照: https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ3_S

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
