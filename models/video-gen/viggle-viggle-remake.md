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
sources:
  - https://viggle.ai/meme/app/home?ui=v2
flags: []
risk_notes: "MiniMax H3 Community License を継承。EU・UK・韓国・米国は Applicable Territory から除外されており、これらの地域での利用・配布は別途ライセンスが必要。実在人物・既存作品の置換が可能なため、肖像権・著作権・パロディ表記の確認が必要。"
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
