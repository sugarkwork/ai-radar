---
type: "model"
name: "Qwen3.8-27B TURBO Fable Cold Fusion Heretic NEO-CODER-MAX MTP GGUF"
genre: "other"
url: "https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF"
author: "DavidAU"
source_post: "https://x.com/Oluwaphilemon1/status/2118900933350277415"
sources: ["https://x.com/oluwaphilemon1/status/2118900933350277415?a=xSK1et5rIZBer5g0Q8A&s=46", "https://x.com/Oluwaphilemon1/status/2118900933350277415", "https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF", "https://huggingface.co/Qwen/Qwen3.8-27B", "https://huggingface.co/Qwen/Qwen3.8-27B/raw/main/config.json", "https://huggingface.co/api/models?search=Qwen3.8-27B"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "11.67GBを27B原本のサイズとしない。拒否0/100はカードに根拠を見つけられず未確認。256Kコンテキスト表記は実用メモリを保証しない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF"
license: "apache-2.0"
base_model: ["DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NM-DAU"]
downloads: 1553252
likes: 2708
format: "gguf"
size: "配布中の重みファイル 23本・合計389,004,245,760 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-09-01"
updated: "2026-10-17"
fetched_at: "2026-11-09T00:30:50.862079+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
---

# DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF

## 出来ること

Qwen3.8-27Bの長名のGGUF配布。紹介の11.67GBはIQ2_Mファイルに一致し、他に複数の高ビット量子とmmprojがある。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:50.862079+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:30:50.862079+00:00）。重み 23本。

- `Qwen3.8-27B-TurboFCFusion-735-882-Here-Uncen-NEO-CODER-MAX-IQ2_M.gguf` — 11,673,303,648 bytes
- `Qwen3.8-27B-TurboFCFusion-735-882-Here-Uncen-NEO-CODER-MAX-IQ3_M.gguf` — 14,080,727,648 bytes
- `Qwen3.8-27B-TurboFCFusion-735-882-Here-Uncen-NEO-CODER-MAX-IQ4_XS.gguf` — 16,582,359,648 bytes
- `Qwen3.8-27B-TurboFCFusion-735-882-Here-Uncen-NEO-CODER-MAX-LOW-MTP-IQ4_XS.gguf` — 15,309,039,136 bytes
- `Qwen3.8-27B-TurboFCFusion-735-882-Here-Uncen-NEO-CODER-MAX-LOW-MTP-Q6_K.gguf` — 22,431,000,096 bytes
- `Qwen3.8-27B-TurboFCFusion-735-882-Here-Uncen-NEO-CODER-MAX-MTP-IQ2_M.gguf` — 12,124,624,416 bytes
- `Qwen3.8-27B-TurboFCFusion-735-882-Here-Uncen-NEO-CODER-MAX-MTP-IQ3_M.gguf` — 14,532,048,416 bytes
- `Qwen3.8-27B-TurboFCFusion-735-882-Here-Uncen-NEO-CODER-MAX-MTP-IQ4_XS.gguf` — 17,033,680,416 bytes
- ほか15本。複数形式・量子化・分割を含むため全量ダウンロードを推奨する意味ではない。

[ファイル一覧](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

IQ3_M約14.08GB、Q4_K_M約18.05GB、Q8_0約30.24GB、mmproj約0.93GBという原チェック。対応する視覚入力ランタイムの確認が必要。

11.67GBを27B原本のサイズとしない。拒否0/100はカードに根拠を見つけられず未確認。256Kコンテキスト表記は実用メモリを保証しない。

## 使い方

[公式モデルカード](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @Oluwaphilemon1: https://x.com/Oluwaphilemon1/status/2118900933350277415
- 対象資料: https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF
- 参照: https://huggingface.co/Qwen/Qwen3.8-27B
- 参照: https://huggingface.co/Qwen/Qwen3.8-27B/raw/main/config.json

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
