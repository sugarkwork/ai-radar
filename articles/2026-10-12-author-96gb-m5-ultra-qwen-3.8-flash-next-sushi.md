---
name: "96GB M5 UltraでQwen 3.8 Flash NextをSushiで実行した報告"
genre: "article"
url: "https://www.reddit.com/r/MacStudio/comments/1x3z21b/qwen_38_flash_next_on_m5u_96gb_at_90_tks_sushi/"
published: "2026-10-12"
flags: ["unverified"]
risk_notes: "速度や品質評価は投稿者の自己報告で、独立した再現確認はありません。投稿者は128Kコンテキスト、MTP有効、8-bit KV、実際のエージェント負荷で約70–80 tok/s（SSDキャッシュ有効）、約93–100 tok/s（無効）、4bpw版で約45 tok/sと述べています。"
type: "article"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119415614448030071"]
fetched_at: "2026-11-22T04:42:06.554009+00:00"
---

# 96GB M5 UltraでQwen 3.8 Flash NextをSushiで実行した報告

## テーマ

- 96GB M5 Ultra上で、Apple Silicon向け推論エンジンSushiを使いQwen3.8 Flash Nextの2.6bpw量子化版を動かした投稿者の使用報告。4bpw版との速度比較も記載されています。

## 著者の主張

- 投稿者によると、128Kコンテキスト、MTP有効、8-bit KV、エージェント負荷で、2.6bpw版はSSDキャッシュ有効時に約70–80 tok/s、無効時に約93–100 tok/sで、無効時のメモリ使用量は約61GB。プロンプト処理は約3,100 tok/sと述べています。4bpw版は約45 tok/sで、投稿者の非コーディング用途では品質向上を体感できなかったとの評価です。いずれも投稿者の環境での報告値・主観評価です。

## 裏取り・注意点

- 投稿本文で確認できるのは投稿者の構成と報告内容です。速度や品質は独立に検証されていません。本文からは測定機器・反復回数などの詳細は確認できません。投稿には使用した量子化モデルとSushiの配布先リンクがあります。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 出典

- 対象投稿（公開日と本文）: https://www.reddit.com/r/MacStudio/comments/1x3z21b/qwen_38_flash_next_on_m5u_96gb_at_90_tks_sushi/

投稿内のモデル配布先: https://huggingface.co/beamster/Qwen3.8-Flash-Next-Sushi-2.6bpw
投稿内の推論エンジン: https://github.com/beamivalice/sushi

## 変更履歴

- 2026-11-23: 初回登録
