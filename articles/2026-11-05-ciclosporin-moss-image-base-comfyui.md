---
name: "MOSS-Image-Baseの二段階ComfyUIワークフロー"
genre: "image-gen"
url: "https://www.reddit.com/r/StableDiffusion/comments/1xoqgn0/mossimagebase_two_stage_workflow/"
author: "Ciclosporin"
published: "2026-11-05"
flags: ["unverified"]
risk_notes: "生成は実行しておらず、画質、再現性、必要VRAM、処理時間、配布JSONのライセンスと再配布条件は未確認。作例の枚数、seed、選別の有無は作者の報告。"
type: "article"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/mapte_fireball/status/2118479331551051984"]
fetched_at: "2026-11-10T05:47:18Z"
---

# MOSS-Image-Baseで潜在表現を4MPから6MPに拡大する二段階生成

## テーマ

- ComfyUIでMOSS-Image-Baseを二段階に分けてサンプリングする。段間で画像にデコードせず、潜在表現を拡大して後段へ渡す。

## 著者の主張

- 作者はAurygのKrea-2-Two-Stage-Samplerを使用し、引き継ぎを40%に設定。bislerpで4MPから6MPへ拡大し、Redditのプレビューは共有用に3MPへ縮小したと記載している。
- 前段は52ステップ、CFG 3.0、Eulerとsimple。後段は同じベースモデルにlodestonesの8-steps-dmd2 LoRAを加え、20ステップ、CFG 1.0、dpmpp_2mとkarrasを使用。
- 作者は作例10枚すべてにseed 1を使用し、選別せず、各プロンプトを配布ワークフローに収録したと説明している。

## 裏取り・注意点

- 作者が案内するPastebinの配布ページを閲覧できた。元投稿では、BBOX用のComfyUI-MOSSLayoutとプレビュー用のComfyUI-KJNodesは任意とされている。
- 画質や6MP生成の再現性は独立検証していない。配布JSONのライセンスと再配布条件は未確認。

## 出典

- 作者の元投稿 https://www.reddit.com/r/StableDiffusion/comments/1xoqgn0/mossimagebase_two_stage_workflow/
- 元投稿から案内されているワークフロー配布ページ https://pastebin.com/SXmaiKuv

## 変更履歴

- 2026-11-10: 初回登録
