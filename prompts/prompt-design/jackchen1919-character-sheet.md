---
name: "キャラクター三面図プロンプト（GPT / MageSpace）"
genre: "prompt-design"
url: "https://x.com/jackchen1919/status/2118770137394532543"
prompt_sha1: "7f9915cb213bd5e09c3324430183a6359586678f"
target: "GPT / MageSpace などの画像生成"
transcribed_from: "text"
flags: ["unverified"]
risk_notes: "投稿はプロンプト本文＋生成結果8枚で、特定の製品・モデルの配布ではない。生成画像は著者の作例で、再現性・品質は未検証（当方では生成していない）。実在の人物・既存キャラクターに寄せると権利侵害になり得る。"
type: "prompt"
added: "2026-11-08"
first_seen: "2026-11-08"
sources: ["https://x.com/jackchen1919/status/2118770137394532543", "https://x.com/jackchen1919/status/2118770137394532543?a=zqdC3nDy3vjN4FaO0GI&s=46"]
fetched_at: "2026-11-08T06:40:00Z"
author: "@jackchen1919"
source_post: "https://x.com/jackchen1919/status/2118770137394532543"
amplifiers: []
previous_prompt_sha1: "4acce17224c6073b83044ab62c35572af30f06f7"
---

# キャラクター三面図プロンプト（GPT / MageSpace）

## 目的

- 1人のキャラクターについて、左にアップ、右に全身の前・横・後ろを並べた**キャラクターデザインシート**を1枚で生成する。
- 服装・髪型・小物を固定した三面図を作り、後の画像生成や動画化で参照画像として使う。

## 前提

- 画像生成に対応したモデル（投稿では GPT / MageSpace）。
- アスペクト比は `--ar 16:9`。モデルによっては `--ar` が無視されるため、UI側で16:9を指定する。
- 出力は3Dレンダー調（`3D render`）。アニメ調にしたい場合は末尾のスタイル指定を差し替える。

## プロンプト本文

```
A character design showcase sheet of a single stylish girl, split-screen layout with a close-up portrait on the left and full-body front, side, and back views on the right. She has shoulder-length dark brown bob hair with bangs, elegant facial features, heart-shaped earrings. Outfit: a light blue long-sleeve oversized button-up shirt, a high-waisted red mini skirt, blue mid-calf socks, red mary jane flats, holding a small leopard-print handbag. Retro chic fashion, soft studio lighting, neutral gray background, ultra-detailed, 8k, 3D render. --ar 16:9
```

## 使い方

- そのまま画像生成モデルに貼る。キャラクターを変える場合は、髪型・服装・小物の記述だけを差し替える。
- 得られたシートを参照画像として固定すると、以降のポーズ違い・動画化で顔と服の一貫性を保ちやすい。
- 三面図のレイアウトが崩れる場合は、`split-screen layout` 以降の構図指定を先頭に移す。

## 注意点

- 生成結果は著者の作例8枚のみで、モデル・バージョン・seedは明示されていない。同じプロンプトでも出力は変わる。
- 実在の人物・有名人・既存キャラクターに似せると権利侵害になり得る。商用利用は各モデルのライセンスに従う。
- `8k` などの品質指定はモデルによって効果が異なる。過剰な指定は構図崩れの原因になることがある。

## 変更履歴

- 2026-11-08: 初回登録（注意点を明記して収録）

## 追加出典・確認範囲（2026-11-09）

キャラクターのアップと全身前後側面を分割配置する英語プロンプト。

GPT/MageSpace向けの原文は既存エントリに保存済み。その本文とハッシュを変更せず維持する。

画像生成・指示効果の再現試験は行っていない。別人の返信にある指示文を混入しない。

概要は2026-11-08の確認記録・紹介投稿に基づく。過去の数値はその確認時点のもので現在値としない。今回の実行確認はない。

- @jackchen1919: https://x.com/jackchen1919/status/2118770137394532543

- 2026-11-09: 関連出典と確認範囲を追記。既存の記述・過去の数値・原文プロンプトは維持。今回の実行確認なし。

- 2026-11-09: 原文は変更せず、正規化SHA-1を検算して訂正。前回値はprevious_prompt_sha1に保存。
