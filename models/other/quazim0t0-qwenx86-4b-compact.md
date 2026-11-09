---
type: "model"
name: "Quazim0t0/Qwenx86-4B-compact"
genre: "other"
url: "https://huggingface.co/Quazim0t0/Qwenx86-4B-compact"
author: "Quazim0t0"
source_post: "https://x.com/teksedge/status/2118857211992854892"
sources: ["https://x.com/teksedge/status/2118857211992854892?a=nohsiaOxTo_yMIMJ3ms&s=46", "https://x.com/teksedge/status/2118857211992854892", "https://huggingface.co/Quazim0t0/Qwenx86-4B-compact", "https://huggingface.co/api/models/Quazim0t0/Qwenx86-4B-compact", "https://huggingface.co/Quazim0t0/Qwenx86-4B-compact/raw/main/README.md", "https://huggingface.co/api/models/Quazim0t0/Qwenx86-4B-GGUF", "https://huggingface.co/spaces/Quazim0t0/Qwenx86-Debugger"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "完全なPCや高速な実用計算機ではない。計算一件に数十秒〜数分。GSM8K26/28等は作者測定で、ホスト側メモリ機能と重み内実行を区別する。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "Quazim0t0/Qwenx86-4B-compact"
license: "apache-2.0"
base_model: ["Qwen/Qwen3.5-4B"]
downloads: 54
likes: 41
format: "safetensors"
size: "配布中の重みファイル 8本・合計8,913,661,982 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-11-05"
updated: "2026-11-08"
fetched_at: "2026-11-09T00:30:34.351291+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
---

# Quazim0t0/Qwenx86-4B-compact

## 出来ること

Qwen3.5-4Bの前にコンパイラが計算した13層を足し、x86-64整数命令と小型メモリを重み内で表現する研究モデル。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:34.351291+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:30:34.351291+00:00）。重み 8本。

- `model/atoms.safetensors` — 59,952 bytes
- `model/boot/c.safetensors` — 27,264,536 bytes
- `model/boot/calc.safetensors` — 27,264,512 bytes
- `model/boot/notes.safetensors` — 27,264,536 bytes
- `model/boot/pydoc.safetensors` — 27,264,536 bytes
- `model/boot/python.safetensors` — 27,264,608 bytes
- `model/boot/science.safetensors` — 27,264,560 bytes
- `model/compact.safetensors` — 8,750,014,742 bytes

[ファイル一覧](https://huggingface.co/Quazim0t0/Qwenx86-4B-compact/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

compact版約9GB、calc/python/c/notes/science/python_docの6ブート状態とchipformerコードを同梱するとカードで説明。

完全なPCや高速な実用計算機ではない。計算一件に数十秒〜数分。GSM8K26/28等は作者測定で、ホスト側メモリ機能と重み内実行を区別する。

## 使い方

[公式モデルカード](https://huggingface.co/Quazim0t0/Qwenx86-4B-compact)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @TeksEdge: https://x.com/TeksEdge/status/2118857211992854892
- 対象資料: https://huggingface.co/Quazim0t0/Qwenx86-4B-compact
- 参照: https://huggingface.co/api/models/Quazim0t0/Qwenx86-4B-compact
- 参照: https://huggingface.co/Quazim0t0/Qwenx86-4B-compact/raw/main/README.md
- 参照: https://huggingface.co/api/models/Quazim0t0/Qwenx86-4B-GGUF
- 参照: https://huggingface.co/spaces/Quazim0t0/Qwenx86-Debugger

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
