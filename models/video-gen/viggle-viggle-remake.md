---
type: model
model: Viggle/Viggle-Remake
name: Viggle Remake（MiniMax-H3 ベースの動画リメイク）
genre: video-gen
url: https://huggingface.co/Viggle/Viggle-Remake
author: Viggle
license: MiniMax H3 Community License（独自。EU・UK・韓国・米国は対象外）
base_model: [MiniMaxAI/MiniMax-H3]
format: safetensors / GGUF / LoRA
size: "未確認（リポジトリに複数形式）"
downloads: 5215
likes: 105
created: 2026-10-22
updated: 2026-11-04
added: 2026-11-05
first_seen: 2026-11-05
source_post: https://x.com/HuggingModels/status/2118445754675335509
sources: ["https://viggle.ai/meme/app/home?ui=v2", "https://x.com/aiaicreate/status/2119247949347815472"]
flags: ["unverified"]
risk_notes: "MiniMax H3 Community License を継承。EU・UK・韓国・米国は Applicable Territory から除外されており、これらの地域での利用・配布は別途ライセンスが必要。実在人物・既存作品の置換が可能なため、肖像権・著作権・パロディ表記の確認が必要。"
fetched_at: "2026-11-09T00:31:33.400445+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
license_name: "minimax-h3-community-license"
amplifiers: []
---

# Viggle Remake

## 出来ること

- **動画のリメイク（キャラクター置換・衣装・天候・小物の追加削除・スタイル変更）**を行う video-to-video モデル。MiniMax-H3 をベースにした LoRA として配布されている。
- 1本の動画と言葉1つで指示できる設計。カットを自動で検出し、カットごとに置換を適用する。
- **エージェント前提**の構成で、MCP サーバー経由で Claude Code / Codex などから操作できる（README に "built agent-first" と明記）。
- ComfyUI 用ノード（`ComfyUI-Viggle-Remake`）を同梱。GGUF 版もある。
- 公式アプリ（viggle.ai）でも試せる（セットアップ・GPU 不要）。

## 目的・背景

「動画を丸ごと作り直す」のではなく、**既存の動画の要素だけを差し替える**用途に絞ったモデル。投稿では La La Land の1ショットを22通りに作り直す例、Uptown Funk のミュージックビデオを69カット再キャストする例が紹介されている（いずれも権利者非公認のパロディである旨が明記）。

## 収録ファイル

- `comfyui/ComfyUI-Viggle-Remake/`（ノード実装）
- `lora/swap`（キャラクター置換用 LoRA）
- GGUF 版、`PROMPTING.md`（プロンプト例）、`COMFYUI.md`（導入手順）
- ライセンス: `LICENSE`（MiniMax H3 Community License）、`LICENSE-CODE`、`NOTICE`、`MODIFICATIONS.md`

## 実行条件

- **地域制限**: Applicable Territory は全世界から **EU・UK・韓国・米国を除く**。日本は対象内だが、これら地域のユーザー・サーバーでの利用は別契約が必要。
- ベースモデルの H3 が動く GPU が必要（ComfyUI 経由）。GGUF 版は量子化で必要VRAMを下げられる。
- 実在人物・既存映像の置換ができるため、**肖像権・著作権・AI生成であることの表示**を確認する。商用利用は H3 コミュニティライセンスの条件に従う。
- 投稿時点で 5,215 DL / 105 likes。2026-10-22 公開。

## 使い方

```text
1. HF から model / LoRA / ComfyUI ノードを取得
2. ComfyUI の custom_nodes に ComfyUI-Viggle-Remake を置く
3. 参照動画 + 置換指示（「全員を猫にする」など）を入力
4. カット検出 → 置換 → 書き出し
```

## 変更履歴

- 2026-11-05: 初回登録（DL 5,215 / likes 105 / license: MiniMax H3 Community / updated 2026-11-04）

## 追加出典・確認範囲（2026-11-09）

Viggle-Remakeを紹介する反応まとめの追加出典。

元の動画リメイクモデルと同一配布対象。

Reddit反応のまとめに新たな品質・実行の情報はない。

対象固有の機能・制約の説明は2026-11-08（原記録）のチェック記録を基にしている。メタ情報は2026-11-09T00:31:33.400445+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

### 今回取得した公式メタ情報

既存フロントマターの過去値は維持し、今回の取得値を下に併記する。どちらも実行・性能の追試ではない。

| 項目 | 値 |
|---|---|
| model | Viggle/Viggle-Remake |
| url | https://huggingface.co/Viggle/Viggle-Remake |
| license | other |
| base_model | ["MiniMaxAI/MiniMax-H3"] |
| downloads | 76308 |
| likes | 194 |
| format | safetensors / gguf |
| size | 配布中の重みファイル 16本・合計167,175,729,456 bytes（複数形式・量子化・派生を含む。必要メモリではない） |
| created | 2026-10-22 |
| updated | 2026-11-07 |
| fetched_at | 2026-11-09T00:31:33.400445+00:00 |
| pricing | free |
| pricing_detail | 重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。 |
| signup_required | False |
| license_name | minimax-h3-community-license |


- @aiaicreate: https://x.com/aiaicreate/status/2119247949347815472
- 対象資料: https://huggingface.co/Viggle/Viggle-Remake

- 2026-11-09: 関連出典と確認範囲を追記。既存の記述・過去の数値・原文プロンプトは維持。今回の実行確認なし。
