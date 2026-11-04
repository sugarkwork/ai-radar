---
type: model
model: localai0301/Anima-RGBA
name: Anima RGBA
genre: video-gen
url: https://huggingface.co/localai0301/Anima-RGBA
author: localai0301
license: Apache-2.0
base_model: [circlestone-labs/Anima]
format: safetensors
size: "VAE 508 MB / LoRA 184 MB"
downloads: 8
likes: 37
created: 2026-11-02
updated: 2026-11-03
added: 2026-11-04
first_seen: 2026-11-04
source_post: https://x.com/UNfukashigi/status/2117818752847036487
sources: []
pricing: free
pricing_detail: "重み無料（Apache-2.0）"
signup_required: false
---

# Anima RGBA

## 出来ること

- アニメ画像モデル **Anima** で、**透過（RGBA）画像を生成**するための VAE と LoRA のセット。
- **RGBA VAE**: Anima が使う Qwen-Image VAE の4チャンネル版。Anima の latent を、不透明な RGB ではなく実際のアルファ付き画像にデコードする（508MB、ComfyUI の Qwen-Image VAE キー形式）。
- **RGBA LoRA**: この VAE の latent で学習した LoRA。Anima 側が「VAE で透過になる latent」を出すようになる（184MB、step 25,000）。
- カスタムノード不要。既存の Anima ワークフローの VAE を差し替え、LoRA を足し、プロンプトに `transparent background` を入れるだけで動く。
- 背景を消す後処理ではなく、**生成の段階で背景とキャラクターを分離**する。髪の毛ごと消えるような後処理の破綻を避けられる、というのが作者の主張。

## 目的・背景

AI 漫画・イラスト制作で、キャラクターを背景から切り抜く作業を生成側に寄せる試み。VAE は Qwen-Image VAE（Apache-2.0）由来で、その学習済みデコーダを4チャンネル化し、LoRA は同 VAE の latent に合わせて学習されている。2026-11-02 公開、11-04 時点で 37 likes（ダウンロード数は公開直後で8）。

## 収録ファイル

- `anima_rgba_vae.safetensors` — 508MB（エンコーダ＋デコーダ）
- `anima_rgba_lora.safetensors` — 184MB（Anima DiT 用、step 25,000）

## 実行条件

- ComfyUI と Anima 本体（`circlestone-labs/Anima`）、Anima 用のテキストエンコーダ
- VAE は 512px クロップで学習されている。高解像度でもデコードはするが、髪の毛・ガラス・煙のような**細かい半透明表現は最も弱い**
- 生成されるアルファはほぼ二値。**透ける服は不透明になりやすい**
- 画面いっぱいの接写では白背景が残ることがある（他の LoRA を重ねると頻度が上がる）
- アニメ／イラスト（Anima）向け。実写用途は想定されていない
- LoRA 無しでも VAE 単体でアルファは出るが、輪郭がぼやける

## 使い方

```text
1. anima_rgba_vae.safetensors → ComfyUI/models/vae に置き、Load VAE で Qwen-Image VAE の代わりに選択
2. anima_rgba_lora.safetensors → ComfyUI/models/loras に置き、通常の LoRA ローダーで strength 1.0
3. プロンプトに "transparent background"（または "isolated on a transparent background"）を追加
   → VAE Decode が4チャンネル（RGB+alpha）を出力し、Save Image が RGBA PNG で保存
背景が不透明なままなら、LoRA 強度ではなくトリガーの重みを上げる（例: (transparent background:1.3)）。
LoRA を 1.5 にすると被写体の周囲に半透明のゴミが出やすい。
```

## 変更履歴

- 2026-11-04: 初回登録
