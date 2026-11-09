---
type: "model"
name: "Quazim0t0/Qwenx86-4B-GGUF"
genre: "other"
url: "https://huggingface.co/Quazim0t0/Qwenx86-4B-GGUF"
author: "Quazim0t0"
source_post: "https://x.com/teksedge/status/2118857211992854892"
sources: ["https://x.com/teksedge/status/2118857211992854892?a=nohsiaOxTo_yMIMJ3ms&s=46", "https://x.com/teksedge/status/2118857211992854892", "https://huggingface.co/Quazim0t0/Qwenx86-4B-compact", "https://huggingface.co/api/models/Quazim0t0/Qwenx86-4B-compact", "https://huggingface.co/Quazim0t0/Qwenx86-4B-compact/raw/main/README.md", "https://huggingface.co/api/models/Quazim0t0/Qwenx86-4B-GGUF", "https://huggingface.co/spaces/Quazim0t0/Qwenx86-Debugger", "https://huggingface.co/Quazim0t0/Qwenx86-4B-GGUF"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "compact版のサイズ・速度・検証結果をそのままこのGGUF版の独立実測として転載しない。現時点の各量子ファイルの動作は未確認。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "Quazim0t0/Qwenx86-4B-GGUF"
license: "apache-2.0"
base_model: ["Quazim0t0/Qwenx86-4B-compact"]
downloads: 572
likes: 1
format: "safetensors / gguf"
size: "配布中の重みファイル 9本・合計13,888,219,624 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-11-07"
updated: "2026-11-07"
fetched_at: "2026-11-09T00:30:34.893116+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
---

# Quazim0t0/Qwenx86-4B-GGUF

## 出来ること

Qwenx86-4Bの同一作者によるGGUF配布。重み内で整数命令を実行する研究デモの量子化系統。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:34.893116+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:30:34.893116+00:00）。重み 9本。

- `gguf/qwenx86-machine-bf16.gguf` — 8,700,224,704 bytes
- `gguf/qwenx86-text-q4_k_m.gguf` — 5,024,347,680 bytes
- `model/atoms.safetensors` — 59,952 bytes
- `model/boot/c.safetensors` — 27,264,536 bytes
- `model/boot/calc.safetensors` — 27,264,512 bytes
- `model/boot/notes.safetensors` — 27,264,536 bytes
- `model/boot/pydoc.safetensors` — 27,264,536 bytes
- `model/boot/python.safetensors` — 27,264,608 bytes
- ほか1本。複数形式・量子化・分割を含むため全量ダウンロードを推奨する意味ではない。

[ファイル一覧](https://huggingface.co/Quazim0t0/Qwenx86-4B-GGUF/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

GGUFに対応する指定ランタイムとコードの互換性を配布元で確認する。compactのsafetensors版とは別の配布ID。

compact版のサイズ・速度・検証結果をそのままこのGGUF版の独立実測として転載しない。現時点の各量子ファイルの動作は未確認。

## 使い方

[公式モデルカード](https://huggingface.co/Quazim0t0/Qwenx86-4B-GGUF)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @TeksEdge: https://x.com/TeksEdge/status/2118857211992854892
- 対象資料: https://huggingface.co/Quazim0t0/Qwenx86-4B-GGUF
- 参照: https://huggingface.co/Quazim0t0/Qwenx86-4B-compact
- 参照: https://huggingface.co/api/models/Quazim0t0/Qwenx86-4B-compact
- 参照: https://huggingface.co/Quazim0t0/Qwenx86-4B-compact/raw/main/README.md
- 参照: https://huggingface.co/api/models/Quazim0t0/Qwenx86-4B-GGUF
- 参照: https://huggingface.co/spaces/Quazim0t0/Qwenx86-Debugger

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
