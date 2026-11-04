---
type: model
model: Pika-Labs/Pika-H3-Flex-Turbo-LoRA
name: Pika H3 Flex Turbo LoRA
genre: video-gen
url: https://huggingface.co/Pika-Labs/Pika-H3-Flex-Turbo-LoRA
author: Pika Labs（LoRA 制作は @_akhaliq）
license: other
license_name: minimax-h3-community-license-agreement
base_model: [Pika-Labs/Pika-H3-Flex, lightx2v/Minimax-h3-Turbo, MiniMaxAI/MiniMax-H3, WarmBloodAban/Minimax-h3_Singularity, Iwannapose/minimax_h3_pdmd_2nfe_comfyui]
format: safetensors
size: "3.9 GB（本編5種）/ 0.31 GB（lite r32）"
downloads: 29390
likes: 103
created: 2026-10-29
updated: 2026-10-30
added: 2026-11-04
first_seen: 2026-11-04
source_post: https://x.com/pika_labs/status/2117772839642386856
sources: []
pricing: free
pricing_detail: "重み無料（MiniMax-H3 Community License）"
signup_required: false
---

# Pika H3 Flex Turbo LoRA

## 出来ること

- Pika のオープンウェイト動画モデル **Pika H3 Flex** に、数ステップ蒸留を合成した LoRA。**2ステップ下書き → 4ステップ本番 → 8ステップ高画質**を、それぞれ単体ファイルで提供する。
- カスタムノードでもパッチでもなく、**通常の LoRA**。既存の H3 環境（ComfyUI / Diffusers、bf16 / int8 / GGUF）にそのまま挿せる。Singularity などの品質マージモデルの上でも動く。
- 各ファイルは2つのアダプタの**厳密な rank 連結**（層ごとに `B_fused @ A_fused == s·(B_flex @ A_flex) + 1.0·(B_turbo @ A_turbo)`）で、近似的なマージではない。スタック読み込みと数学的に同一で、マージ干渉が無いとしている。
- 音声付き動画（同期オーディオ）に対応。Flex のスタイル強度は 0.5（2/4ステップ）/ 0.6（8ステップHD）で焼き込み済み。
- lite 版は rank-32 の SVD 圧縮で、スペクトルエネルギーの 96.1% を保持しつつ 0.31GB（12.6分の1）。

## 目的・背景

Pika H3 Flex の公開から24時間以内に、コミュニティ（@_akhaliq）が ComfyUI / Diffusers 向けの高速化 LoRA として公開し、Pika 公式が「これが weights を公開した理由」と紹介した経緯がある。ベースは Pika H3 Flex、蒸留元は lightx2v Turbo（FL2VA は v1.2 768p、Ref2VA は v0.1）と pDMD 2-NFE（Apache 2.0）。2026-10-29 公開、11-04 時点で 29,390 ダウンロード。

## 収録ファイル

- `pika_h3_flex_turbo_2step_draft_ref2va.safetensors` — 3.9GB、Ref2VA、2ステップ。構図・動きの下書き用
- `pika_h3_flex_turbo_4step_fl2va.safetensors` — 3.9GB、FL2VA、4ステップ。素の H3（T2V/I2V）向けの本番用
- `pika_h3_flex_turbo_4step_ref2va.safetensors` — 3.9GB、Ref2VA、4ステップ。Singularity 併用の推奨
- `pika_h3_flex_turbo_8step_hd_fl2va.safetensors` / `..._8step_hd_ref2va.safetensors` — 3.9GB、8ステップHD（style 0.6）
- `pika_h3_flex_turbo_4step_fl2va_lite_r32.safetensors` / `..._ref2va_lite_r32.safetensors` — 0.31GB、rank-32 圧縮

## 実行条件

- MiniMax H3 のベース重み・テキストエンコーダ・VAE が必要（Pika H3 Flex は H3 系）。
- ライセンスは **MiniMax-H3 Community License**（OSI 承認のオープンソースではない）。
- **音声は6ステップ未満で劣化する**（H3 turbo 共通）。音声を重視するなら4ステップ以上で本番。
- 2ステップは下書き専用で、シーン失敗が時々出る。4ステップ版はちょうど4ステップ用に調整されており、8ステップHDは6〜8ステップで効く。
- 2/4ステップ版に強いスタイル・モーションLoRAを高強度で重ねるのは非推奨。
- 作者計測（H200 / A100、848×480×121フレーム＋ステレオ音声、CFG 1）: 公式6ステップ 60秒 → 4ステップ 40秒（1.5倍速）、2ステップ下書き 約25秒（約2.4倍速）、8ステップHD 70秒。A100 は 109.3秒 → 66.0秒。素の H3（約40ステップ）は約500秒。第三者検証は未確認。

## 使い方

```text
1. 使う transformer に合うファイルを ComfyUI/models/loras に置く
   （Ref2VA = Singularity / 参照ワークフロー、FL2VA = 素の T2V/I2V）
2. いつもの MiniMax-H3 ワークフローに LoraLoaderModelOnly を追加し strength 1.0
3. サンプリング: ファイルに合わせて 2 / 4 / 8 ステップ、CFG 1.0、
   euler / lcm / res_multistep、simple スケジューラ
   Flow shift: video 6.0（FL2VA）/ 12.0（Ref2VA）、audio shift 3.0
```

## 変更履歴

- 2026-11-04: 初回登録（HF モデルをカタログ対象にしたことに伴う追加）
