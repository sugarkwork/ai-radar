---
type: model
model: WepeNerd/H3_Ripple
name: H3 Ripple
genre: video-gen
url: https://huggingface.co/WepeNerd/H3_Ripple
author: WepeNerd
license: unknown
format: safetensors
size: "0.30 GB"
downloads: 115
likes: 33
created: 2026-10-30
updated: 2026-10-30
added: 2026-11-04
first_seen: 2026-11-03
source_post: https://x.com/mapte_fireball/status/2117523266122465557
sources:
  - https://wepenerd.github.io/ComfyUI-WepeNerd/
  - https://github.com/WepeNerd/ComfyUI-WepeNerd
pricing: free
pricing_detail: "重み無料（ライセンス表記なし）"
signup_required: false
---

# H3 Ripple

## 出来ること

- **MiniMax H3 FL2VA 用の LoRA**。既存の動画ショットから1〜2枚のアンカーフレームを選び、画像編集で直した内容を、指定した区間の全フレームへ伝播させる。
- 「全フレームを1枚ずつ直す」のではなく、**編集点を決めて差分だけを映像に乗せる**使い方。アンカーはタイムライン上の任意の位置に置ける。
- 編集は手持ちの画像エディタで行えるほか、ComfyUI ノード経由で **Qwen Image 2.1** などのローカル編集モデルの出力も直接渡せる。
- 同梱の ComfyUI ワークフローは2種類: **Simple**（アンカー1枚・90フレーム = 3.75秒）と **Local Editor**（アンカー2枚・124フレーム = 5.17秒、Qwen Image 2.1 で編集）。

## 目的・背景

動画編集で「1箇所だけ直したい」ときに、フレーム間の一貫性を保つのが難しい問題への対処。H3 の映像生成能力を使い、編集済みフレームを条件として残りを再生成する。2026-10-30 公開、11-04 時点で 115 ダウンロード・33 likes。

## 収録ファイル

- `minimax_H3_Ripple-v1.safetensors` — 0.30GB（LoRA 本体）

## 実行条件

- 最新の ComfyUI と **ComfyUI-WepeNerd** カスタムノード
- MiniMax H3 **FL2VA** の重み、H3 のテキストエンコーダ、映像 VAE
- ワークフローは **H3 Turbo 4-step LoRA** も併用する
- Local Editor ワークフローは Qwen Image 2.1 とそのテキストエンコーダ・VAE も必要
- ライセンス表記がリポジトリに無い（モデルカードに license フィールドなし）。利用条件は未確認
- 元映像と編集アンカーの一貫性に結果が依存する。速い動き・オクルージョン・大きな視点変化は伝播しにくい。意図しない細部まで変わる場合がある

## 使い方

```text
1. minimax_H3_Ripple-v1.safetensors を ComfyUI/models/loras/H3/ に置く
2. 同梱ワークフローを読み込む（Simple / Local Editor）
3. 設定: Ripple と Turbo の LoRA 強度 1.0、4ステップ、euler、simple、CFG 1
   出力 1MP、24fps。必要なら Ripple Clip でサイズ・長さを調整
4. Ripple Apply の伝播プロンプトは既定のまま、変更内容は画像エディタ側で表現する
```

## 変更履歴

- 2026-11-04: 初回登録
