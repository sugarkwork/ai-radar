---
type: "model"
name: "pentacoxian-dev/Qwen3.8-Flash-Next-IQ3E-Q8D-MTP-GGUF"
genre: "model-serving"
url: "https://huggingface.co/pentacoxian-dev/Qwen3.8-Flash-Next-IQ3E-Q8D-MTP-GGUF"
author: "pentacoxian-dev"
source_post: "https://x.com/_ryu15_/status/2119318395430551580"
sources: ["https://x.com/_ryu15_/status/2119318395430551580?a=yCDo-wHy6DxHFi53EG0&s=46", "https://x.com/_ryu15_/status/2119318395430551580", "https://github.com/Niko1221/Strata", "https://raw.githubusercontent.com/Niko1221/Strata/main/data/experimental-speed-projection/README.md", "https://huggingface.co/pentacoxian-dev/Qwen3.8-Flash-Next-IQ3E-Q8D-MTP-GGUF"]
first_seen: "2026-11-08"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "v4/v5は回帰で撤回と明記。一般的なllama.cppや他GPUでそのまま動くとは限らず、速度・control vectorとの組合せは未確認。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "pentacoxian-dev/Qwen3.8-Flash-Next-IQ3E-Q8D-MTP-GGUF"
license: "other"
base_model: ["Qwen/Qwen3.8-Flash-Next"]
downloads: 29140
likes: 23
format: "gguf"
size: "配布中の重みファイル 1本・合計85,923,705,344 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-09-24"
updated: "2026-09-27"
fetched_at: "2026-11-09T00:31:33.789955+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
license_name: "qwen-community-1.0"
---

# pentacoxian-dev/Qwen3.8-Flash-Next-IQ3E-Q8D-MTP-GGUF

## 出来ること

Qwen3.8-Flash-NextのIQ3E/Q8D/MTP向けGGUF派生。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08（原記録）のチェック記録を基にしている。メタ情報は2026-11-09T00:31:33.789955+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:31:33.789955+00:00）。重み 1本。

- `Qwen3.8-Flash-Next-IQ3E-Q8D-MTP.gguf` — 85,923,705,344 bytes

[ファイル一覧](https://huggingface.co/pentacoxian-dev/Qwen3.8-Flash-Next-IQ3E-Q8D-MTP-GGUF/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

V10032GB×2を想定し専用llama.cppパッチが必須。カードはv3推奨。

v4/v5は回帰で撤回と明記。一般的なllama.cppや他GPUでそのまま動くとは限らず、速度・control vectorとの組合せは未確認。

## 使い方

[公式モデルカード](https://huggingface.co/pentacoxian-dev/Qwen3.8-Flash-Next-IQ3E-Q8D-MTP-GGUF)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @_ryu15_: https://x.com/_ryu15_/status/2119318395430551580
- 対象資料: https://huggingface.co/pentacoxian-dev/Qwen3.8-Flash-Next-IQ3E-Q8D-MTP-GGUF
- 参照: https://github.com/Niko1221/Strata
- 参照: https://raw.githubusercontent.com/Niko1221/Strata/main/data/experimental-speed-projection/README.md

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
