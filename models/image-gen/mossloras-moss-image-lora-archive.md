---
type: model
model: mossloras/moss-image-lora-archive
name: MOSS-Image LoRA Archive（Civitai日次スクレイプ）
genre: image-gen
url: https://huggingface.co/mossloras/moss-image-lora-archive
author: mossloras
license: unknown
base_model: []
format: safetensors
size: "2,283 weight files / 約341GB（2026-11-08時点）"
downloads: 0
likes: 12
created: 2026-11-05
updated: 2026-11-08
pricing: free
pricing_detail: "重みは無料。個々のLoRAのライセンスはCivitai側の配布条件に従う。"
signup_required: false
added: 2026-11-08
first_seen: 2026-11-08
source_post: https://x.com/SD_Tutorial/status/2119357081715343577
sources: ["https://huggingface.co/mossloras/moss-image-lora-archive", "https://x.com/wildmindai/status/2119204788734935382"]
flags: ["unverified"]
risk_notes: "18+ / NSFW を含む可能性。CivitaiのMOSS-Image向けLoRAを日次で集めたアーカイブで、モデルカード・ライセンスファイルがない。個々のLoRAの再配布・商用利用の許諾は一括では確認できない。2,330ファイル（うち重み2,283本）・約341GB。DL 0・likes 12で独立検証なし。Civitaiの利用規約と各LoRA作者の条件を確認してから使う。"
fetched_at: "2026-11-08T12:40:00Z"
---

# MOSS-Image LoRA Archive（Civitai日次スクレイプ）

> **18+ / NSFW 注意**: Civitai由来のLoRAをまとめたアーカイブです。成人向け表現を含む可能性があります。閲覧・使用は18歳以上、または各法域の年齢要件を満たす場合に限ります。

## 出来ること

- MOSS-Image 向けのLoRAを、Civitaiから日次で集めてHugging Faceに置いているアーカイブ。
- 日付ディレクトリ（`2026-10-17/` 〜）ごとに、作品ID・作者名・LoRA名の階層で `.safetensors` を収録。
- 2026-11-08時点で **2,330ファイル、うち重み2,283本、合計約341GB**。
- 個別のLoRAをダウンロードして、MOSS-Imageの推論環境で使う想定。

## 目的・背景

- Civitai上で配布されているMOSS-Image用LoRAを、まとめて取得・更新できるようにするためのスクレイプ・アーカイブ。投稿では「Daily updated」と説明されている。
- 作成2026-11-05、最終更新2026-11-08。DL 0・likes 12で、まだ広く使われている実績はない。

## 収録ファイル

- `YYYY-MM-DD/MOSS-Image/<作品ID>_<作品名>/<version ID>/<LoRA名>.safetensors`
- ファイルサイズは約0.06〜0.58GB/本。合計は約341GB。
- モデルカード、README、LICENSEファイルは無い（2026-11-08時点）。

## 実行条件

- MOSS-Image 本体と、LoRAを読み込める推論環境（ComfyUIなど）が必要。
- ディスク容量: 全件で約341GB。必要なLoRAだけを選んで取得する。
- 個々のLoRAのベースモデル・推奨強度・トリガー語は、Civitaiの各配布ページを確認する。

## 使い方

```bash
# 例: 特定の日付・作品だけ取得する
hf download mossloras/moss-image-lora-archive \
  --repo-type model --local-dir moss-loras \
  --include "2026-11-08/*"
```

- 全件取得は約341GB。`--include` で日付・作品を絞る。
- 取得後、各LoRAのCivitaiページでライセンスと利用条件を確認する。

## 注意（18+・ライセンス）

- **18+ / NSFW**: Civitai由来のため成人向けLoRAを含む可能性がある。年齢確認と閲覧環境に注意。
- **ライセンス不明**: リポジトリにLICENSEが無く、個々のLoRAのライセンスも一括では分からない。再配布・商用利用・クレジット条件は、各LoRA作者とCivitaiの規約に従う。
- Civitaiのスクレイプ物を再アップロードすること自体が、Civitaiの規約や作者の許諾に反する場合がある。
- DL 0・likes 12の新しいアーカイブで、内容の網羅性・安全性は独立検証されていない。

## 変更履歴

- 2026-11-08: 初回登録（18+注意・ライセンス不明を明記）
